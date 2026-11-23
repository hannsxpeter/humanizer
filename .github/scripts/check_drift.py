#!/usr/bin/env python3
"""Fail when humanizer's docs drift out of agreement with each other.

Checks versions, catalog and example counts, adapter bodies, file
references, the README layout and anchors, eval structure, and house style.
Repository tooling, not part of the skill. Standard library only; run from
anywhere inside the repository:

    python3 .github/scripts/check_drift.py
"""
import json
import os
import re
import subprocess
import sys

ROOT = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True
).stdout.strip()
os.chdir(ROOT)
TRACKED = subprocess.run(
    ["git", "ls-files"], capture_output=True, text=True, check=True
).stdout.splitlines()

LAYOUT_EXEMPT = {"README.md", "LICENSE", ".gitignore"}
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
WORDS = (
    "zero one two three four five six seven eight nine ten eleven twelve "
    "thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty"
).split()
# Built from code points so this file stays ASCII and cannot trip its own check.
DASH = re.compile("[%s%s]" % (chr(0x2013), chr(0x2014)))
EMOJI = re.compile("[%s-%s%s-%s%s-%s]" % (
    chr(0x2600), chr(0x27BF), chr(0x2B00), chr(0x2BFF), chr(0x1F000), chr(0x1FAFF)))

TEXT = {}
for _path in TRACKED:
    try:
        with open(_path, encoding="utf-8") as _f:
            TEXT[_path] = _f.read()
    except (UnicodeDecodeError, IsADirectoryError):
        pass

problems = []


def report(path, line, message):
    problems.append((path, line, message))


def line_of(path, index):
    return TEXT[path].count("\n", 0, index) + 1


def number(word):
    word = word.lower()
    if word.isdigit():
        return int(word)
    return WORDS.index(word) if word in WORDS else None


def frontmatter(path):
    match = re.match(r"\A---\n(.*?)\n---\n", TEXT[path], re.S)
    return match.group(1) if match else None


def strip_frontmatter(text):
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)


def normalize(text):
    return " ".join(text.split())


def parse_frontmatter(block):
    """Top-level keys of a simple YAML mapping, with block scalars folded."""
    keys, values = [], {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        match = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", lines[i])
        i += 1
        if not match:
            continue
        key, rest = match.groups()
        nested = []
        while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
            nested.append(lines[i])
            i += 1
        keys.append(key)
        if rest in (">", ">-", ">+", "|", "|-", "|+"):
            values[key] = " ".join(l.strip() for l in nested if l.strip())
        elif rest:
            values[key] = rest.strip().strip("'\"")
        else:
            values[key] = "\n".join(nested)
    return keys, values


def check_skill_frontmatter():
    block = frontmatter("SKILL.md")
    if block is None:
        report("SKILL.md", 1, "missing YAML frontmatter")
        return None
    keys, values = parse_frontmatter(block)
    for key in keys:
        if key not in SPEC_KEYS:
            report("SKILL.md", 1, f"frontmatter key '{key}' is not in the Agent Skills spec")
    name = values.get("name", "")
    if len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        report("SKILL.md", 1, f"name '{name}' must be 1-64 lowercase letters, digits, and single hyphens")
    description = values.get("description", "")
    if not 1 <= len(description) <= 1024:
        report("SKILL.md", 1, f"description is {len(description)} characters; the spec allows 1-1024")
    if len(values.get("compatibility", "")) > 500:
        report("SKILL.md", 1, "compatibility is over the spec's 500-character limit")
    match = re.search(r"^\s+version:\s*['\"]?(\d[\w.-]*)", values.get("metadata", ""), re.M)
    if not match:
        report("SKILL.md", 1, "metadata.version is missing")
        return None
    return match.group(1)


def check_versions(version):
    readme, log = "README.md", "CHANGELOG.md"
    sources = [
        (readme, re.search(r"badge/version-(\d[\w.]*?)-\w+\)", TEXT[readme]), "README version badge"),
        (log, re.search(r"^## \[(\d[\w.]*)\]", TEXT[log], re.M), "latest CHANGELOG release"),
        (log, re.search(r"^\[(\d[\w.]*)\]: \S+", TEXT[log], re.M), "first CHANGELOG version link"),
        ("package.json", re.search(r'^  "version": "(\d[\w.-]*)"', TEXT["package.json"], re.M),
         "package.json version"),
    ]
    for path, match, label in sources:
        if not match:
            report(path, 1, f"cannot find the {label}")
        elif match.group(1) != version:
            report(path, line_of(path, match.start()), f"{label} says {match.group(1)}, SKILL.md says {version}")
    link = sources[2][1]
    if link and not link.group(0).endswith(f"v{version}"):
        report(log, line_of(log, link.start()), f"the {version} link should point at tag v{version}")


def check_catalog():
    path = "references/tell-patterns.md"
    text = TEXT[path]
    heads = [(int(m.group(1)), m.group(2).strip(), m.start())
             for m in re.finditer(r"^### (\d+)\. (.+)$", text, re.M)]
    numbers = [n for n, _, _ in heads]
    if numbers != list(range(1, len(numbers) + 1)):
        report(path, 1, f"pattern headings must be numbered 1-{len(numbers)} in order")
    toc = re.search(r"^## Table of contents\n(.*?)^---$", text, re.M | re.S)
    if not toc:
        report(path, 1, "no '## Table of contents' section ending at a '---' line")
    else:
        entries = {int(n): title.strip() for n, title in re.findall(r"^(\d+)\. (.+)$", toc.group(1), re.M)}
        for n, title, index in heads:
            if entries.get(n) != title:
                report(path, line_of(path, index), f"table of contents entry {n} reads '{entries.get(n)}'")
        for n in sorted(set(entries) - set(numbers)):
            report(path, line_of(path, toc.start()), f"table of contents lists pattern {n}, which has no heading")
    families = len(re.findall(r"^## Family [A-Z]:", text, re.M))
    return len(heads), families


def check_examples():
    path = "references/examples.md"
    numbers = [int(n) for n in re.findall(r"^## Example (\d+):", TEXT[path], re.M)]
    if numbers != list(range(1, len(numbers) + 1)):
        report(path, 1, f"examples must be numbered 1-{len(numbers)} in order")
    return len(numbers)


def check_evals(examples):
    path = "evals/evals.json"
    try:
        evals = json.loads(TEXT[path]).get("evals", [])
    except json.JSONDecodeError as error:
        report(path, error.lineno, f"invalid JSON: {error.msg}")
        return 0
    ids = [case.get("id") for case in evals]
    if ids != list(range(1, len(evals) + 1)):
        report(path, 1, f"eval ids must run 1-{len(evals)} in order")
    required = {"id", "prompt", "expected_output", "files", "expectations"}
    for case in evals:
        missing = required - set(case)
        if missing:
            report(path, 1, f"eval {case.get('id')} is missing {', '.join(sorted(missing))}")
        if not case.get("expectations"):
            report(path, 1, f"eval {case.get('id')} has no expectations")
        for name in case.get("files", []):
            if name not in TEXT:
                report(path, 1, f"eval {case.get('id')} needs missing file {name}")
    if len(evals) < examples:
        report(path, 1, f"{len(evals)} evals for {examples} worked examples; each example needs a mirror eval")
    return len(evals)


def check_counts(counts):
    patterns, families, examples, evals = counts
    for path, text in TEXT.items():
        if path == "CHANGELOG.md":
            continue
        for match in re.finditer(r"\b(\d+)[- ]patterns?\b", text):
            if int(match.group(1)) != patterns:
                report(path, line_of(path, match.start()), f"says '{match.group(0)}'; the catalog has {patterns}")
        for match in re.finditer(r"\b(\w+) families\b", text):
            n = number(match.group(1))
            if n is not None and n != families:
                report(path, line_of(path, match.start()), f"says '{match.group(0)}'; the catalog has {families}")
        example_phrases = (
            r"\b(\w+) (?:full )?worked (?:end-to-end )?(?:runs|examples)\b",
            r"\b(\w+) full runs\b",
        )
        for phrase in example_phrases:
            for match in re.finditer(phrase, text, re.I):
                n = number(match.group(1))
                if n is not None and n != examples:
                    report(path, line_of(path, match.start()), f"says '{match.group(0)}'; examples.md has {examples}")
        for match in re.finditer(r"\b(\w+) verification cases\b", text):
            n = number(match.group(1))
            if n is not None and n != evals:
                report(path, line_of(path, match.start()), f"says '{match.group(0)}'; evals.json has {evals}")
    badge = re.search(r"tell%20catalog-(\d+)%20patterns", TEXT["README.md"])
    if not badge or int(badge.group(1)) != patterns:
        report("README.md", 1, f"the tell catalog badge should say {patterns} patterns")


def check_tools():
    readme = TEXT["README.md"]
    badge = re.search(r"works%20with-(\d+)%20", readme)
    section = re.search(r"^## Works with your tools\n(.*?)(?=^## )", readme, re.M | re.S)
    if not badge or not section:
        report("README.md", 1, "cannot find the tools badge or the Works with your tools section")
        return 0
    rows = [l for l in section.group(1).splitlines()
            if l.startswith("|") and not re.match(r"^\|\s*(Tool\b|-)", l)]
    if len(rows) != int(badge.group(1)):
        report("README.md", line_of("README.md", badge.start()),
               f"badge says {badge.group(1)} tools, the Supported tools table has {len(rows)} rows")
    return len(rows)


def check_adapters():
    """GEMINI.md imports AGENTS.md; every other adapter carries its body verbatim."""
    def body(text):
        return normalize(re.sub(r"\A# .*\n", "", strip_frontmatter(text).lstrip()))

    count = 1
    if "GEMINI.md" in TEXT:
        count += 1
        if not re.search(r"^@(\./)?AGENTS\.md\s*$", TEXT["GEMINI.md"], re.M):
            report("GEMINI.md", 1, "must import AGENTS.md with an '@./AGENTS.md' line")
    for path, text in sorted(TEXT.items()):
        if path in ("AGENTS.md", "GEMINI.md"):
            continue
        if not strip_frontmatter(text).lstrip().startswith("# humanizer ("):
            continue
        count += 1
        block = frontmatter(path)
        for offset, line in enumerate((block or "").splitlines(), 2):
            if not re.match(r"^[A-Za-z][\w-]*:( .*)?$", line):
                report(path, offset, f"frontmatter line is not 'key: value': {line}")
        if body(text) != body(TEXT["AGENTS.md"]):
            report(path, 1, "body differs from AGENTS.md; adapters carry it verbatim")
    return count


def check_references():
    for path in TRACKED:
        if path.startswith("references/") and f"`{path}`" not in TEXT["SKILL.md"]:
            report("SKILL.md", 1, f"never mentions {path}, so the skill cannot load it")
    for path, text in TEXT.items():
        if path == "CHANGELOG.md":
            continue
        for match in re.finditer(r"`((?:references|evals|\.cursor|\.continue|\.github)/[^`\s*]+)`", text):
            ref = match.group(1)
            if not ref.endswith("/") and ref not in TEXT:
                report(path, line_of(path, match.start()), f"mentions missing file {ref}")


def check_layout():
    readme = TEXT["README.md"]
    block = re.search(r"^## Layout\n+```\n(.*?)\n```", readme, re.M | re.S)
    if not block:
        report("README.md", 1, "cannot find the Layout code block")
        return
    start = line_of("README.md", block.start(1))
    listed = {}
    for offset, line in enumerate(block.group(1).splitlines()):
        if line.strip():
            listed[line.split()[0]] = start + offset
    folders = [p for p in listed if p.endswith("/")]
    for path, line in listed.items():
        exists = any(t.startswith(path) for t in TRACKED) if path in folders else path in TRACKED
        if not exists:
            report("README.md", line, f"Layout lists {path}, which does not exist")
    for path in TRACKED:
        covered = path in listed or any(path.startswith(f) for f in folders)
        if not covered and path not in LAYOUT_EXEMPT:
            report("README.md", start, f"Layout does not list {path}")


def slug(heading):
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def check_anchors():
    for path, text in TEXT.items():
        if not path.endswith(".md"):
            continue
        anchors = {slug(h) for h in re.findall(r"^#+ (.+)$", text, re.M)}
        for match in re.finditer(r"\]\(#([^)\s]+)\)", text):
            if match.group(1) not in anchors:
                report(path, line_of(path, match.start()), f"link to #{match.group(1)} has no matching heading")


def check_style():
    for path, text in TEXT.items():
        for number_, line in enumerate(text.splitlines(), 1):
            if DASH.search(line):
                report(path, number_, "em or en dash; use a comma, colon, parentheses, or a hyphen")
            if EMOJI.search(line):
                report(path, number_, "emoji; use words or an icon instead")
            if line != line.rstrip(" \t"):
                report(path, number_, "trailing whitespace")
        if text and not text.endswith("\n"):
            report(path, text.count("\n") + 1, "missing final newline")
        if not path.endswith((".md", ".mdc")):
            continue
        in_code = False
        body_start = len(text) - len(strip_frontmatter(text))
        first_line = text.count("\n", 0, body_start) + 1
        for number_, line in enumerate(text.splitlines(), 1):
            if number_ < first_line:
                continue
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code or line.lstrip().startswith(("|", "![", "[![", "<")):
                continue
            if len(line) > 80:
                report(path, number_, f"{len(line)} columns; wrap prose at 80")


def escape(value, prop=False):
    value = value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    return value.replace(":", "%3A").replace(",", "%2C") if prop else value


def main():
    version = check_skill_frontmatter()
    if version:
        check_versions(version)
    patterns, families = check_catalog()
    examples = check_examples()
    evals = check_evals(examples)
    check_counts((patterns, families, examples, evals))
    tools = check_tools()
    adapters = check_adapters()
    check_references()
    check_layout()
    check_anchors()
    check_style()

    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    for path, line, message in sorted(set(problems)):
        if in_actions:
            print(f"::error file={escape(path, True)},line={line}::{escape(message)}")
        else:
            print(f"{path}:{line}: {message}")
    if problems:
        print(f"\ndrift check failed: {len(set(problems))} problem(s)")
        return 1
    print(f"drift check passed: version {version}, {patterns} patterns in {families} families, "
          f"{examples} examples, {evals} evals, {tools} tools, {adapters} adapters, "
          f"{len(TRACKED)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())

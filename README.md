# humanizer

![version](https://img.shields.io/badge/version-1.3.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![type](https://img.shields.io/badge/type-pure--prompt%20skill-purple)
![dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
![patterns](https://img.shields.io/badge/tell%20catalog-32%20patterns-orange)
![tools](https://img.shields.io/badge/works%20with-13%20AI%20coding%20tools-teal)
[![drift check](https://github.com/hannsxpeter/humanizer/actions/workflows/drift.yml/badge.svg)](https://github.com/hannsxpeter/humanizer/actions/workflows/drift.yml)

A standalone, pure-prompt skill that rewrites AI-sounding prose so it reads as
genuinely human, and rewrites in a specific writer's voice when a sample or
style profile is available. It also conservatively cleans suspicious invisible
Unicode in supplied prose. It is just instructions: `SKILL.md` plus a few
reference files. No scripts, no dependencies, no network access.

## Install

`humanizer` is an [Agent Skill](https://agentskills.io): a folder whose
`SKILL.md` any skills-aware tool can load. Clone it into a skills folder your
tool scans, and keep the folder name `humanizer`, which must match the skill's
`name`.

```bash
git clone https://github.com/hannsxpeter/humanizer ~/.claude/skills/humanizer
```

That folder serves Claude Code, and Cursor, OpenCode, and GitHub Copilot in VS
Code read it too. For Codex, Gemini CLI, Pi, Devin Desktop, Zed, and Copilot
outside VS Code, use the shared folder instead:

```bash
git clone https://github.com/hannsxpeter/humanizer ~/.agents/skills/humanizer
```

To scope the skill to one project, clone it into `.claude/skills/humanizer` or
`.agents/skills/humanizer` inside that project; Google Antigravity reads the
project form. Cline uses its own folder, `~/.cline/skills/humanizer`. Update
with `git pull` in the clone. Tools without skill support, and setups that
prefer rules files, use an adapter instead; see
[Supported tools](#supported-tools).

## Usage

Ask, in plain language, to humanize, de-slop, or fix prose that "reads like
AI," "sounds corporate," or is "too generic," or to make a draft sound like
you or a named author. You do not need to say the word "humanize."

For voice-matched output, do one of:

- paste a sample of the target writing,
- name a well-known author, or
- keep a `VOICE.md` (schema in `references/voice-matching.md`) or a
  `STYLE-GUIDE.md` in the project; it is discovered automatically.

A sample or author named in the request wins over a profile file. Ask for
"more edge" or "a take" to turn on stance mode, which adds opinion about your
facts but never new facts.

Every run returns the rewritten text plus a short report: what changed, what
was deliberately left alone, a text-hygiene status, a meaning check, and a
next step.

## Why this one is different

- **Faithfulness over liveliness.** Each pass carries an anti-fabrication
  rule, and a mandatory meaning check closes every run. Together they stop
  the most common humanizer failure: inventing plausible facts, causes, or
  quotes to make a rewrite "sound concrete."
- **Restraint by design.** A density pre-check scales effort to evidence, and
  an explicit do-not-flag reference protects already-human writing instead of
  laundering it into smooth, average prose.
- **Variance, not synonym-swapping.** It targets the real signature of
  machine text (uniform rhythm) rather than relocating it with a thesaurus.
- **Voice-first.** When a writing sample or a `VOICE.md` / `STYLE-GUIDE.md`
  is present, it rewrites in that author's cadence and stance, not generic
  neutral prose.
- **Opt-in edge.** A stance mode adds opinion and punch on explicit request,
  hard-blocked from inventing content.
- **Conservative text hygiene.** It removes high-confidence invisible
  formatting residue while preserving script joiners, direction controls,
  display selectors, locale spacing, code, and exact-value spans when they are
  load-bearing.

## What it removes

A 32-pattern catalog in six families, each with detect / why / before-after /
restraint notes: inflated significance, promotional and evasive language,
formulaic structure, lexical tics, syntactic tics, and formatting artifacts,
including chat-UI contamination, debunking-pose headings, and diff-anchored
writing.

## Prompt-only text hygiene

Every run includes a text-hygiene preflight. When the host exposes the
characters, the skill can remove stray zero-width spaces, soft formatting
controls, unexpected direction controls, free-floating tag characters, and
copy-paste spacing residue. When the prose is in a file, one regex search
locates every invisible or unusual-space codepoint in the hygiene table;
confusable letters still need a reading check. It reports what changed and
keeps ambiguous or load-bearing Unicode, such as the joiners some scripts need
for correct spelling, instead of normalizing it blindly.

This feature adapts the prompt-compatible text-layer ideas from
[watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover).
That project also offers scripts for C2PA, EXIF, XMP, document metadata, and
media processing. Humanizer remains pure prompt, so those container and media
features are deliberately outside its scope. A prose rewrite may disturb
statistical token patterns as a side effect, but this skill cannot verify or
promise their removal.

### Feature adoption matrix

Humanizer borrows selected ideas, not the complete `watermarks-remover`
toolchain:

| Source capability | Humanizer support | Boundary |
|---|---|---|
| Invisible Unicode and unusual-space cleanup | Adapted | Prompt-level and limited to characters the host exposes |
| Statistical token-pattern disruption | Side effect only | The quality rewrite changes wording and syntax; nothing is tuned for this, verified, or promised |
| C2PA, EXIF, XMP, PDF, and document metadata | Not included | Requires deterministic file-processing tools |
| Pixel, image, audio, and video marks | Not included | Requires media tooling or external models |
| Directory and website provenance audits | Not included | Outside a prose-rewriting skill |

This boundary keeps Humanizer dependency-free and prevents a prose rewrite
from being misreported as a full provenance scrub.

## Supported tools

Tools that support Agent Skills load `SKILL.md` natively from a skills folder
(see [Install](#install)). Each tool also reads a rules file, which is how the
skill works when this repository is the workspace, or when you copy an
adapter into your own project together with `SKILL.md` and `references/`.
Every adapter shares one body that routes the agent to the same `SKILL.md`
and `references/`, so the workflow is identical across tools.

| Tool | Rules file it reads | Agent Skills folders |
|---|---|---|
| Claude Code | `AGENTS.md` when no `CLAUDE.md` exists (recent versions) | `~/.claude/skills/` |
| Codex | `AGENTS.md` | `~/.agents/skills/` |
| Cursor | `.cursor/rules/humanizer.mdc` (applied when relevant) and `AGENTS.md` | `~/.agents/skills/`, `~/.claude/skills/` |
| GitHub Copilot | `.github/copilot-instructions.md`; also `AGENTS.md` in VS Code, the CLI, and the cloud agent | `~/.agents/skills/`, `.github/skills/`; in VS Code also `~/.claude/skills/` |
| Gemini CLI | `GEMINI.md` | `~/.agents/skills/`, `~/.gemini/skills/` |
| Google Antigravity | `AGENTS.md` and `GEMINI.md` | `.agents/skills/` in the project |
| OpenCode | `AGENTS.md` | `~/.agents/skills/`, `~/.claude/skills/` |
| Pi | `AGENTS.md` | `~/.agents/skills/`, `~/.pi/agent/skills/` |
| Devin Desktop (formerly Windsurf) | `AGENTS.md` | `~/.agents/skills/` |
| Cline | `AGENTS.md` | `~/.cline/skills/` |
| Continue | `.continue/rules/humanizer.md` (applied when relevant) | not documented |
| Zed | the first rules file it finds; here `.github/copilot-instructions.md` | `~/.agents/skills/` |
| Aider | `CONVENTIONS.md`, via `aider --read CONVENTIONS.md` or `read: CONVENTIONS.md` in `.aider.conf.yml` | none |

If your project already has its own `AGENTS.md`, install the skill natively
instead of overwriting that file.

## Scope

This skill improves prose quality and authentic voice. It is not designed or
tuned to defeat plagiarism checkers or AI-detection systems, and it names no
detector. Requests framed as passing AI work off as a person's own for a
graded or contractual assessment are reframed toward the quality-and-voice
use the skill actually serves. Text hygiene applies only to characters in the
supplied prose. It does not inspect or strip file-container provenance or
media marks.

## Evals

`evals/evals.json` holds eight verification cases: one per worked example,
plus checks for a detector-evasion request, an oblique trigger, and a single
chat-UI artifact in human-written text. Each case gives a prompt, the
expected behavior, and checkable expectations. They are not part of the
runtime skill. Run them with an eval harness such as Anthropic's
skill-creator, or paste each prompt into a fresh session and grade the output
against its expectations.

## Layout

```
SKILL.md                        orchestrator: workflow, guardrails, output contract
AGENTS.md                       entry point for every tool that reads AGENTS.md
GEMINI.md                       Gemini CLI context
CONVENTIONS.md                  Aider conventions
.cursor/rules/humanizer.mdc     Cursor project rule
.continue/rules/humanizer.md    Continue rule
.github/copilot-instructions.md GitHub Copilot instructions (also Zed's pick here)
references/tell-patterns.md     the 32-pattern catalog (read in Pass 2)
references/do-not-flag.md       false positives, human markers, stop conditions
references/voice-matching.md    voice discovery and application
references/text-hygiene.md      conservative invisible-Unicode cleanup
references/examples.md          five worked end-to-end runs
evals/evals.json                eight verification cases (not part of the runtime skill)
evals/files/VOICE.md            voice profile used by eval 2 and Example 2
CHANGELOG.md                    release history
.github/workflows/drift.yml     CI: runs the drift check on pushes and pull requests
.github/scripts/check_drift.py  the drift check (repo tooling, not part of the skill)
```

## Contributing

Pull requests are welcome. The method lives in `SKILL.md` and `references/`;
the adapters only route to it. When you change the method, keep these in
step:

- **Adapters.** They share one body. Edit them together and keep the bodies
  identical; only titles, frontmatter, and tool-specific lines differ.
- **Counts.** The 32 patterns (`SKILL.md`, `AGENTS.md`, this README and its
  badge), the five worked examples (`SKILL.md`, `references/examples.md`, this
  README), and the 13 tools (badge and table).
- **Examples and evals.** Every worked example has a mirror eval. Examples
  obey the hard rule themselves: no fact, number, or name the source lacks.
- **Releases.** Move the `Unreleased` notes in `CHANGELOG.md` under the new
  version, bump `metadata.version` in `SKILL.md` and the README badge, then
  tag `vX.Y.Z` and publish a GitHub release.
- **House style.** These docs use no em dashes, en dashes, or emojis, and
  prose wraps at 80 columns.

Run `python3 .github/scripts/check_drift.py` before you open a pull request.
CI runs the same check on every push and pull request. It enforces most of
the list above; whether the examples stay faithful still needs a human read.

## Where this comes from

This skill was built from the voice-preservation logic that powers
[Scriveno](https://github.com/hannsxpeter/scriveno) (formerly Scriven), an
AI-native longform writing system whose core promise is narrow and
high-stakes: drafted prose should sound like the writer, not like AI.
Scriveno is a spec-driven creative-writing, publishing, and translation
pipeline for AI coding agents. It profiles a writer's voice, loads that
Voice DNA into every drafting step, keeps each unit on fresh context, and
runs a Polish pass (editor review, line and copy edit, voice check,
originality check) so prose stays specific to the project instead of
collapsing into generic machine output.

`humanizer` lifts the part of that pipeline that finds and removes AI writing
tells while protecting a writer's authentic voice, and packages it as a
standalone, tool-agnostic skill: the same de-slop, restraint, and
voice-matching philosophy Scriveno applies across a full manuscript, usable
on any prose in any supported tool. If you want the whole writing,
publishing, and translation pipeline rather than just this de-slop layer, see
Scriveno (npm package `scriveno`, run with `npx scriveno@latest`).

## License

MIT. See [LICENSE](LICENSE).

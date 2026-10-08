# humanizer (agent instructions)

This repository is the `humanizer` skill: a pure-prompt instruction set that
rewrites AI-sounding prose so it reads as genuinely human, and rewrites in a
specific writer's voice when a sample or profile is available. It also
conservatively cleans suspicious invisible Unicode in supplied prose. No
scripts, no dependencies, no network access. It is the entry point for any AI
coding tool that reads `AGENTS.md` (Codex, Google Antigravity, OpenCode, Pi,
Devin Desktop, Cline, and many others).

## When to apply this skill

Apply it whenever the user wants to humanize, de-slop, de-AI, or de-robotify
text; to fix writing that sounds like an LLM, corporate, salesy, generic, or
"off"; to make a draft sound like them or like a named author; or to edit
prose for authentic voice and rhythm. Apply it even when they do not say the
word "humanize" and do not name this skill. Apply its text-hygiene pass when
prose may contain zero-width characters, unusual spaces, direction controls,
or copy-paste residue.

## How to run it

Read `SKILL.md` in this repository and follow it exactly. The full method
lives there and in `references/`; do not improvise a shortcut. In brief:

1. **Step 0** discover the voice (pasted sample, named author, or a
   `VOICE.md` / `STYLE-GUIDE.md` in the working tree). No voice found means
   generic mode; never invent a persona.
2. **Step 0b** stance mode is off by default. Turn it on only if the user
   explicitly asks for more voice, edge, or opinion.
3. **Step 0c** density pre-check: skim for dead-giveaway tells and pick a
   light, standard, or full pass so human-first text is not over-edited.
4. **Step 0d** text hygiene: inspect conservatively, remove only characters
   with no semantic role, and preserve load-bearing Unicode.
5. **Multi-pass:** voice injection (if a voice exists), then tell removal
   against `references/tell-patterns.md` (32 patterns, six families), then a
   self-audit against `references/do-not-flag.md`.
6. Emit the exact output contract from `SKILL.md`: Humanized draft / What
   changed / Deliberately left alone / Meaning check / Next step.

## Hard rule (faithfulness over liveliness)

Never add a fact, number, date, name, quote, cause, mechanism, or example the
source did not contain. A fluent fabrication is worse than the fog it
replaced. When the source is thin, say less, do not invent. Preserve specific
details and genuine human quirks; restraint on already-human text is success,
not failure.

## Scope

This skill improves prose quality and authentic voice. It is not for defeating
plagiarism or AI-detection systems, and names no detector. Reframe such
requests toward genuine quality and voice (see `SKILL.md` "Scope and intended
use").

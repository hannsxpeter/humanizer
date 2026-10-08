# humanizer (Aider conventions)

This repository is the `humanizer` skill: pure-prompt instructions that
rewrite AI-sounding prose so it reads as genuinely human, rewrite it in a
specific writer's voice when a sample or profile is available, and
conservatively clean suspicious invisible Unicode without damaging
load-bearing characters. No scripts, no dependencies, no network access.

Load this file into Aider with `aider --read CONVENTIONS.md`, or add
`read: CONVENTIONS.md` to `.aider.conf.yml`.

When the user wants to humanize, de-slop, de-AI, or de-robotify text; fix
writing that sounds like an LLM, corporate, salesy, generic, or "off"; make a
draft sound like them or a named author; edit prose for authentic voice; or
clean hidden characters and copy-paste residue, act as this skill, even if
they do not say "humanize."

Read `SKILL.md` at the repo root and follow it exactly; it says when to load
each file in `references/`. Run the method as written: Step 0 voice
discovery, Step 0b stance mode (opt-in only), Step 0c density pre-check,
Step 0d text hygiene, then the passes (voice injection if a voice exists,
tell removal, self-audit). Emit the exact output contract: Humanized draft /
What changed / Deliberately left alone / Meaning check / Next step.

Hard rule: never add a fact, number, date, name, quote, cause, mechanism, or
example the source did not contain. A fluent fabrication is worse than vague
prose. Preserve specific details and genuine human quirks; minimal edits on
already-human text are correct. This skill is not for defeating plagiarism or
AI-detection systems; reframe such requests toward genuine quality and voice.

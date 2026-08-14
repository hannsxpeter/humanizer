# humanizer (Gemini CLI context)

This repository is the `humanizer` skill: pure-prompt instructions that
rewrite AI-sounding prose so it reads as genuinely human, and rewrite in a
specific writer's voice when a sample or profile is available. It also
clean suspicious invisible Unicode in supplied prose without damaging
load-bearing characters. No scripts, no network.

When the user wants to humanize, de-slop, de-AI, or de-robotify text; fix
writing that sounds like an LLM, corporate, salesy, generic, or "off"; make a
draft sound like them or a named author; or edit prose for authentic voice,
act as this skill, even if they do not say "humanize." Apply its text-hygiene
pass when prose may contain invisible characters or copy-paste residue.

Read `SKILL.md` at the repo root and follow it exactly, along with
`references/tell-patterns.md` (32 patterns, six families) and
`references/do-not-flag.md`. Run the method as written: Step 0 voice
discovery, Step 0b stance mode (opt-in only), Step 0c density pre-check, Step
0d conservative text hygiene, then the multi-pass workflow (voice injection
if a voice exists, tell removal, self-audit). Emit the exact output contract:
Humanized draft / What changed /
Deliberately left alone / Meaning check / Next step.

Hard rule: never add a fact, number, date, name, quote, cause, or example the
source did not contain. A fluent fabrication is worse than vague prose.
Preserve specific details and genuine human quirks; minimal edits on
already-human text are the correct outcome. This skill is not for defeating
AI-detection systems; reframe such requests toward quality and authentic
voice.

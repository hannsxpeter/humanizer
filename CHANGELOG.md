# Changelog

All notable changes to this skill are documented here. This project adheres
to semantic versioning.

## [1.2.0] - 2026-08-14

### Added

- Conservative text-hygiene preflight and final verification for suspicious
  invisible Unicode, zero-width residue, unusual spaces, bidi controls, tag
  characters, and variation selectors in supplied prose.
- `references/text-hygiene.md` with load-bearing Unicode exceptions,
  prompt-only limitations, and bounded reporting language.
- Evaluation coverage for removing high-confidence invisible residue while
  preserving a legitimate script joiner.

### Changed

- The output header now reports text-hygiene status on every run.
- All tool adapters now route the Step 0d text-hygiene pass consistently.
- Documented the feature boundary: wording-level rewrites are unverified,
  while file metadata and media provenance remain outside this pure-prompt
  skill.

## [1.1.1] - 2026-05-29

Documentation consistency pass. No change to the skill's method or behavior.

### Fixed

- Worked-example count corrected from three to four in `SKILL.md` and
  `references/examples.md`; the stance-mode example (Example 4) had been added
  without updating the count (the README and this changelog already said four).
- AI-vocabulary tell citation in `references/examples.md` Example 1: pattern 15
  (diff-anchored writing) corrected to pattern 16 (overused AI vocabulary).

### Added

- Keep a Changelog version-comparison links in this file's footer.

## [1.1.0] - 2026-05-29

### Added

- Five more tool integrations, bringing supported tools from 8 to 13:
  Windsurf (`.windsurfrules`), Cline (`.clinerules`), Continue and Zed
  (`.continue/rules/humanizer.md`), and Aider (`CONVENTIONS.md`). Every
  adapter points at the same `SKILL.md` and `references/`, so the workflow is
  identical across tools.
- "Where this comes from" section in the README crediting Scriveno, the
  longform writing system this skill's voice-preservation logic is drawn from.

### Fixed

- Restraint example (Example 3 in `references/examples.md`) described "two em
  dashes" the text never contained and cited pattern 21; reframed the lesson
  around the colon, parenthetical, and tricolon actually present, with em
  dashes referenced only by analogy and the citation corrected to pattern 22.
- Aligned the eval #3 description in `evals/evals.json` with the corrected
  example.
- Synced the `compatibility` field in `SKILL.md` to all 13 supported tools.
- Corrected the tool name from Scriven to Scriveno in `SKILL.md` and
  `references/voice-matching.md`.

## [1.0.0] - 2026-05-15

First stable release.

### Added

- Pure-prompt `humanizer` skill: `SKILL.md` plus four on-demand reference
  files. No scripts, no dependencies, no network access.
- 32-pattern tell catalog in six families, each with detect / why /
  before-after / restraint guidance (`references/tell-patterns.md`),
  including chat-UI contamination, debunking-pose headings, and diff-anchored
  writing.
- Restraint reference (`references/do-not-flag.md`): false positives, human
  markers to preserve, model idiolects, and hard stop conditions.
- Voice-first workflow with filesystem voice discovery and an optional
  `VOICE.md` schema (`references/voice-matching.md`).
- Density pre-check (Step 0c) that scales effort to evidence so human-first
  text is not over-edited.
- Opt-in stance mode (Step 0b) for livelier output on explicit request,
  hard-blocked from inventing content.
- Three-layer anti-fabrication guard and a mandatory meaning check covering
  both invented specifics and soft causal or temporal inference.
- Four worked end-to-end examples (`references/examples.md`).
- Multi-tool support: Claude Code, Cursor, Codex, Antigravity, Gemini CLI,
  Pi Coder, OpenCode, and GitHub Copilot, via `SKILL.md`, `AGENTS.md`,
  `.cursor/rules/humanizer.mdc`, `GEMINI.md`, and
  `.github/copilot-instructions.md`.
- Verification eval set (`evals/evals.json`), MIT license.

[1.2.0]: https://github.com/hannsxpeter/humanizer/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/hannsxpeter/humanizer/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/hannsxpeter/humanizer/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/hannsxpeter/humanizer/releases/tag/v1.0.0

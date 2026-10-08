# Changelog

All notable changes to this skill are documented here. This project adheres
to semantic versioning.

## [Unreleased]

## [1.3.1] - 2026-10-07

Tooling-only patch. No change to the skill's method or behavior.

### Added

- A drift check, `.github/scripts/check_drift.py`, and a GitHub Actions
  workflow that runs it on every push to `main` and every pull request. It
  fails when versions, counts, the shared adapter text, file references, the
  README layout and anchors, eval structure, or house style drift apart, and
  it annotates the offending lines in pull requests.
- A README status badge for the check, Layout entries for its files, and a
  Contributing note on running it locally.

## [1.3.0] - 2026-10-07

### Added

- An exact codepoint search in `references/text-hygiene.md`: one regex that
  covers every range in the hygiene table, for prose that lives in a file.
  Step 0d points to it.
- Hygiene table rows for joiners (U+200C, U+200D) and direction marks
  (U+200E, U+200F, U+061C), plus U+2061-U+2064 as zero-width residue.
- Eval 7 (stance mode must not invent a cause) and eval 8 (one chat-UI
  artifact in human-first text still gets a light pass). Eval 2 now also
  fails a voice rewrite that invents facts.
- A low-confidence suffix for the output header's Voice line, demonstrated
  in Example 2.
- `license: MIT` in the `SKILL.md` frontmatter.
- README install commands for native Agent Skills folders, plus Evals and
  Contributing sections.

### Changed

- The tool adapters share one body text, so a method change lands the same
  way in every tool.
- Stance mode now states that it applies on a light density pass, while
  density still scopes tell removal.
- `references/text-hygiene.md` is loaded only when Step 0d finds something
  or prose in a file needs the exact search, and Step 0d reserves "not
  verifiable" for when the characters can be neither seen nor searched.
- `allowed-tools` uses the space-separated form from the Agent Skills spec,
  which Claude Code also accepts.
- The README tool table matches current tool behavior: Windsurf is now Devin
  Desktop, "Pi Coder" is Pi, and Zed reads only the first rules file it
  finds.
- The README feature matrix lists statistical token-pattern disruption as a
  side effect only, matching the skill's scope.

### Removed

- `.windsurfrules` and `.clinerules`. Devin Desktop (formerly Windsurf) and
  Cline load `AGENTS.md`, so these legacy single-file adapters only
  duplicated it. To use either tool in your own project, install the skill
  natively or copy `AGENTS.md`.

### Fixed

- Worked Examples 1 and 2 invented facts (quarterly surveys, team sizes, a
  retention comparison) while their meaning checks said nothing was invented.
  Example 2 also broke its own VOICE.md and listed its own insertions as
  "Deliberately left alone." Every claim in both drafts now traces to the
  source, and both meaning checks name what was cut. Example 4 keeps the
  source's "temporarily" in view and questions it without asserting that
  costs are still high, drops a stock negative parallelism, and no longer
  claims to remove tells the source never had.
- `references/voice-matching.md` ranked a discovered VOICE.md above a named
  author, contradicting `SKILL.md`. Explicit input now wins in both.
- `references/tell-patterns.md`: a note that After lines assume
  writer-supplied facts, the pattern 29 table-of-contents title, and an em
  dash house-style note that conflicted with authentic author habits.
- Example 1 cited pattern 13 under the name of pattern 14.
- Grammar and line-wrap defects in the adapters, and a "Continue / Zed"
  rule title (Continue does not run in Zed).
- The README pointed to `scriveno-cli`, an npm package that was unpublished
  in May 2026. Scriveno ships as `scriveno`.
- The 1.2.0 entry below now records the fifth worked example and the
  removal of the `compatibility` frontmatter field.

## [1.2.1] - 2026-08-15

Documentation-only patch. No change to the humanization or text-hygiene
workflow.

### Changed

- Added an explicit feature adoption matrix to `README.md` showing which
  `watermarks-remover` concepts Humanizer adapts, partially overlaps with, or
  excludes.
- Clarified that Humanizer includes prompt-level Unicode hygiene and an
  existing quality rewrite that may disturb statistical token patterns, but
  does not include file metadata, media processing, or audit tooling.
- Bumped the documented skill version to 1.2.1.

## [1.2.0] - 2026-08-14

### Added

- Conservative text-hygiene preflight and final verification for suspicious
  invisible Unicode, zero-width residue, unusual spaces, bidi controls, tag
  characters, and variation selectors in supplied prose.
- `references/text-hygiene.md` with load-bearing Unicode exceptions,
  prompt-only limitations, and bounded reporting language.
- Example 5 in `references/examples.md`: text hygiene without language
  damage.
- Evaluation coverage for removing high-confidence invisible residue while
  preserving a legitimate script joiner.

### Changed

- Rewrote the `SKILL.md` description to cover text hygiene and removed the
  `compatibility` frontmatter field.
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

[Unreleased]: https://github.com/hannsxpeter/humanizer/compare/v1.3.1...HEAD
[1.3.1]: https://github.com/hannsxpeter/humanizer/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/hannsxpeter/humanizer/compare/v1.2.1...v1.3.0
[1.2.1]: https://github.com/hannsxpeter/humanizer/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/hannsxpeter/humanizer/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/hannsxpeter/humanizer/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/hannsxpeter/humanizer/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/hannsxpeter/humanizer/releases/tag/v1.0.0

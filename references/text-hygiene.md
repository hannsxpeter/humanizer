# Text Hygiene

Read this during Step 0d and the final verification. Its job is to remove
invisible formatting residue without damaging real language, typography, or
meaning. This is a conservative prompt-level adaptation of the text-layer
ideas in `guillaumemeyer/watermarks-remover`; it does not bundle or reproduce
that project's scripts.

## Operating rule

Treat a character as a formatting problem only when its role is clear from
context. An invisible codepoint is not evidence of AI authorship. It may come
from a word processor, website, keyboard, language convention, or copy-paste.

Never claim that clean-looking text is free of statistical, vendor, or secret
marks. The host may normalize or hide characters before the skill sees them.

## Conservative inspection

Inspect the source before changing wording. When the host exposes codepoints,
record the codepoint, count, and location. Group findings by kind rather than
listing every occurrence.

| Kind | Common codepoints | Default action |
| --- | --- | --- |
| Soft formatting | U+00AD soft hyphen, interior U+FEFF BOM | Remove when it has no visible or linguistic role |
| Zero-width residue | U+200B zero-width space, U+2060 word joiner, U+2061-U+2064 invisible operators | Remove when embedded in ordinary Latin-script prose without a clear purpose |
| Joiners | U+200C ZWNJ, U+200D ZWJ | Preserve inside scripts and emoji sequences that need them; remove only when stranded in Latin-script prose |
| Direction marks and controls | U+200E, U+200F, U+061C marks; U+202A-U+202E, U+2066-U+2069 | Remove only when unpaired, unexpected, or embedded in otherwise unidirectional prose |
| Tag characters | U+E0001-U+E007F | Remove when free-floating; preserve valid flag or display sequences |
| Variation selectors | U+FE00-U+FE0F, U+E0100-U+E01EF | Preserve when attached to a character whose display they control; remove only when free-floating or clearly injected |
| Space variants | U+00A0, U+2000-U+200A, U+202F, U+205F, U+3000 | Normalize to U+0020 only when line breaking, alignment, and locale typography do not depend on them |
| Confusable letters | Cyrillic or fullwidth characters resembling Latin | Report for review; do not replace automatically |

Do not apply broad Unicode normalization such as NFKC by default. It can
change mathematical symbols, compatibility characters, typography, and text
that the writer intended to preserve.

### Exact search

When the prose is in a file and the host offers a regex search tool (such as
Grep or ripgrep), search for every range in the table at once:

```text
[\x{00A0}\x{00AD}\x{061C}\x{2000}-\x{200F}\x{202A}-\x{202F}\x{205F}-\x{2069}\x{3000}\x{FE00}-\x{FE0F}\x{FEFF}\x{E0001}-\x{E007F}\x{E0100}-\x{E01EF}]
```

A hit locates a candidate, not a verdict: joiners, marks, and selectors that
carry meaning match too. Narrow a hit with a single range (for example
`[\x{200C}\x{200D}]` for joiners), then apply the table and the exceptions
below. Confusable letters need a reading check; no single pattern finds them.

## Load-bearing exceptions

Preserve these unless the user explicitly asks for destructive normalization
and understands the tradeoff:

- ZWNJ and ZWJ inside scripts where they shape spelling or joining.
- Direction marks and isolates that make mixed right-to-left and left-to-right
  text display correctly.
- Variation selectors and joiners attached to valid display sequences.
- Tag characters that belong to a valid flag or display sequence.
- Non-breaking and narrow spaces used for locale typography, units, tables,
  or layout.
- Any unusual character inside code, identifiers, quoted source material,
  hashes, signatures, or other exact-value spans.

If intent is ambiguous, preserve the character and name it under
`Deliberately left alone`. Meaning and display integrity outrank cleanup.

## Order of operations

1. Inspect the original source before rewriting.
2. Remove or normalize only high-confidence formatting residue.
3. Run the voice and tell-removal passes on the cleaned source.
4. Inspect the final prose again for suspicious characters introduced or
   preserved accidentally.
5. Report only verified actions.

Do not count Unicode findings as AI-writing tells in the density pre-check.
Do not infer a vendor, model, or author from them.

## Reporting

Use one of these header states:

- `Text hygiene: no suspicious characters visible`
- `Text hygiene: cleaned: 2 zero-width characters, 1 space normalized`
- `Text hygiene: not verifiable in this interface`

Use `no suspicious characters visible`, not `watermark-free`. The first is a
bounded observation; the second is a claim this skill cannot support.

When characters changed, add one grouped bullet under `What changed`, such as:

`- Text hygiene: removed two U+200B zero-width spaces and normalized one
U+00A0 no-break space that had no layout role.`

In `Meaning check`, confirm that the hygiene edit changed formatting only.
If a load-bearing character was intentionally changed, state the visible or
linguistic consequence instead of calling the edit lossless.

## Scope boundary

This reference covers the text layer supplied to the model. It cannot inspect
or remove file-container provenance, C2PA, EXIF, XMP, document properties,
pixel signals, audio signals, or video signals. It also cannot verify whether
a wording-level statistical pattern remains after rewriting. Route those
requests to dedicated tools and do not imply completion from a prose rewrite.

Source concept: https://github.com/guillaumemeyer/watermarks-remover

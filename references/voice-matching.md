# Voice Matching

Read this only when Step 0 found a voice source. Its job: rewrite so the text
sounds like a specific writer, not like generic "human-ish" prose. Generic
de-slopping removes a machine signature. Voice matching replaces it with a
person's signature, which is far harder to flag and far more useful.

## Part 1: Voice sources, in priority order

1. **Explicit input in the request.** This matches SKILL.md Step 0:
   - *A sample the user pasted or pointed to.* Their own earlier writing, an
     excerpt, or a file path they named. This is the strongest source: it is
     the real distribution, not a description of it. Read it and infer
     (Part 2).
   - *A named, well-known author.* "make it sound like Hemingway / Joan
     Didion / Paul Graham." Use your knowledge of that author's actual
     habits, but match the *instincts* (sentence rhythm, diction, stance),
     never copy their famous sentences.
2. **A discovered profile file.** `VOICE.md`, `STYLE-GUIDE.md`,
   `voice-profile.{md,yaml,json}`, `.manuscript/STYLE-GUIDE.md`, or a voice
   section inside `AGENTS.md` / `CLAUDE.md`. Use the documented schema if it
   matches Part 3, otherwise read it as prose and extract what you can.

If sources conflict (a pasted sample and a stale STYLE-GUIDE.md, or a named
author and a VOICE.md in the project), the explicit request wins; mention the
conflict in the output header.

## Part 2: Reading a voice off a raw sample

You do not need a schema to extract a voice. From any sample of roughly 150
words or more, read off these dimensions. If the sample is shorter than ~150
words, extract cautiously and say so in the output header (low confidence).

- **Cadence and sentence-length distribution.** Are sentences mostly short?
  Wildly varied? Long and subordinated? Note the actual swing, not an average.
  This is the single most identifying feature; reproduce its *shape*.
- **Diction and register.** Anglo-Saxon and plain, or Latinate and formal?
  Technical? Slangy? Profane? Era-marked? Note the ceiling and floor.
- **Signature constructions.** Habitual moves: rhetorical questions, sentence
  fragments, semicolon chains, starting with "And" or "But," dashes,
  parentheticals, direct address to the reader.
- **Punctuation habits.** Does this writer genuinely love em dashes? Use
  semicolons? Avoid the Oxford comma? Their real habit overrides the generic
  tell rule (see Part 4).
- **Paragraph shape.** One-line paragraphs for punch? Long dense blocks?
  Topic-sentence-first or buried lede?
- **Stance and attitude.** Confident and unhedged? Wry? Earnest? Skeptical?
  Warm? Combative? Self-deprecating? Voice is as much attitude as syntax.
- **The avoid-list.** What does this writer never do? No exclamation points,
  no jargon, no first person, no profanity. Absences define a voice as much
  as habits.

Build a short internal model across these seven, then write Pass 1 so the
output sits inside that distribution. Match the *instincts*, not specific
phrases.

## Part 3: Optional VOICE.md schema (interop convenience, not a requirement)

The skill works with no profile file at all. This schema exists so users (and
adjacent tools like Scriveno STYLE-GUIDE.md or a Pillars AGENTS.md voice
section) can hand the skill a structured profile and get sharper results. If a
file roughly follows this shape, read it directly; if it does not, fall back
to Part 2 and read it as prose.

```markdown
# Voice

## Cadence
Sentence-length pattern and rhythm. e.g. "Mostly short. Occasional long
subordinated sentence for contrast. Never two long sentences in a row."

## Diction
Register, word origin, jargon tolerance, profanity, era markers.

## Signature moves
Habitual constructions to reproduce.

## Avoid
Things this writer never does.

## Stance
Attitude and emotional temperature.

## Sample
One representative paragraph (~80-150 words) of the writer's real prose.
```

Every section is optional. The `## Sample` is the most valuable: if present,
prefer inferring from it (Part 2) over trusting the bullet descriptions, since
real prose beats self-description.

## Part 4: Applying voice without overfitting

- **Match the distribution, not the wording.** Reproduce the rhythm, register,
  and instincts. Never lift a distinctive sentence, image, or coinage from the
  sample into the user's text. That is plagiarism of the sample and produces
  obvious seams.
- **Voice beats the generic rule.** If the writer genuinely and consistently
  uses em dashes, long sentences, or "moreover," those are not tells for this
  writer. The tell-pattern catalog yields to a documented authentic habit.
  Conflict resolution order: **authentic author habit > generic tell rule >
  neutral default.**
- **Do not caricature.** Matching Didion does not mean every sentence is a
  fragment about dread. Take the central tendencies and a little of the
  variance, not the extremes turned up to maximum. Caricature is its own
  detectable signature.
- **Preserve the user's meaning, not the sample's content.** The sample
  supplies *how*; the user's draft supplies *what*. Never let the sample's
  topic, facts, or opinions bleed into the rewrite.
- **Confidence honesty.** If the sample was thin or the profile sparse, say so
  in the output header ("Voice: from VOICE.md, low-confidence: 60-word
  sample") so the user can supply more.

## Part 5: When voice and de-slopping cooperate

Voice-first ordering exists because voice is generative and de-slopping is
subtractive. Establish cadence, diction, and stance in Pass 1, then run Pass 2
tell removal *within* that voice: a tell fix that would flatten the
established rhythm is the wrong fix; find one that keeps the voice. Pass 3 then
checks both that machine tells are gone and that the voice is intact and not
caricatured. A rewrite that is clean but no longer sounds like the writer has
failed, even if every tell is gone.

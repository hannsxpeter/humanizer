# Tell-Pattern Catalog

Read this during Pass 2 (tell removal). This is a diagnostic lens, not a
find-and-replace table. For every flag, fix the underlying thought, then check
the **Restraint** note before touching anything. A single instance is rarely a
tell; recurrence and co-occurrence are what give a machine away. The one
exception is pattern 31 (chat-UI contamination): a single instance is
near-certain confirmation.

Each entry has four parts:

- **Detect** what it looks like in the wild.
- **Why it reads as AI** the underlying tendency, so you fix the cause.
- **Before / After** one concrete pair. Where an After names a figure, cause,
  or source the Before lacks, assume the writer supplied it. The pair shows
  the shape of a fix, never permission to invent; without a real detail to
  surface, the honest After is shorter, not more specific.
- **Restraint** when this is genuinely fine and should be left alone.

## Table of contents

**Family A: Inflated significance**
1. Undue emphasis on significance, legacy, and broader trends
2. Notability and media-coverage name-dropping
3. Superficial "-ing" analyses
4. Persuasive-authority tropes

**Family B: Promotional and evasive language**
5. Promotional and advertisement-like language
6. Vague attribution and weasel words
7. Sycophantic and servile tone
8. Filler phrases
9. Excessive hedging

**Family C: Formulaic structure**
10. Formulaic "challenges and future prospects"
11. Negative parallelism and tailing negation
12. Rule-of-three overuse
13. Generic positive conclusion
14. Signposting and announcements
15. Diff-anchored writing

**Family D: Lexical tics**
16. Overused AI vocabulary
17. Elegant variation (synonym cycling)
18. False ranges
19. Hyphenated-pair overuse

**Family E: Syntactic tics**
20. Copula avoidance
21. Passive voice and subjectless fragments

**Family F: Formatting and artifacts**
22. Em dash overuse
23. Boldface overuse
24. Inline-header vertical lists
25. Title case in headings
26. Decorative emojis
27. Curly quotation marks
28. Collaborative chatbot artifacts
29. Knowledge-cutoff and capability disclaimers
30. Fragmented headers
31. Chat-UI contamination artifacts
32. Debunking-pose headings

---

## Family A: Inflated significance

The model reaches for importance it has not earned. The fix is almost always
to delete the inflation and let the concrete fact carry its own weight.

### 1. Undue emphasis on significance, legacy, and broader trends

- **Detect:** "marks a pivotal moment," "stands as a testament," "underscores
  the importance of," "reflects a broader shift," "a turning point in."
- **Why it reads as AI:** the model editorializes about importance instead of
  reporting the thing, because grand framing is high-probability filler.
- **Before:** "The acquisition stands as a pivotal moment, reflecting broader
  shifts in the tooling landscape."
- **After:** "The acquisition was Notion's biggest yet, and it finally gave
  them the calendar product they had failed to build twice."
- **Restraint:** real historical significance, stated plainly with evidence, is
  not this pattern. "It was the first FDA approval for the class" is a fact.

### 2. Notability and media-coverage name-dropping

- **Detect:** listing outlets or famous names purely to borrow credibility:
  "covered by major outlets," "praised by leading experts."
- **Why it reads as AI:** the model gestures at authority it cannot cite
  specifically, so it name-drops categories.
- **Before:** "The study was widely covered by major media and praised by
  leading researchers."
- **After:** "Nature ran it as a cover story; two replication attempts have
  since failed."
- **Restraint:** a specific, sourced attribution ("per the FT's March audit")
  is the opposite of this pattern. Keep it.

### 3. Superficial "-ing" analyses

- **Detect:** participle phrases tacked on to simulate depth: "...sparking
  debate," "...highlighting the need for," "...paving the way for."
- **Why it reads as AI:** the trailing gerund implies analysis without doing
  any. It is a rhythmic reflex, not a thought.
- **Before:** "The feature shipped late, highlighting the need for better
  planning and underscoring broader process gaps."
- **After:** "The feature shipped six weeks late because the spec changed
  twice in QA."
- **Restraint:** a participle that carries real information ("...shipping with
  a known data-loss bug") is fine. The test is whether it says anything.

### 4. Persuasive-authority tropes

- **Detect:** "at its core," "what really matters here," "the key takeaway is,"
  "make no mistake," "the truth is."
- **Why it reads as AI:** the model performs insight with a frame instead of
  delivering the insight.
- **Before:** "At its core, what really matters here is that users want speed."
- **After:** "Users abandoned the flow at the 4-second mark. They want speed."
- **Restraint:** an occasional emphatic frame in genuinely argumentative or
  spoken-register prose is human. One per piece is not a tell.

---

## Family B: Promotional and evasive language

The model sells, softens, or pads. Fixes here usually shorten the text.

### 5. Promotional and advertisement-like language

- **Detect:** "vibrant," "stunning," "seamless," "breathtaking," "nestled,"
  "rich tapestry," "must-have," "game-changing."
- **Why it reads as AI:** marketing register is dense in training data and
  gets applied where neutral description belongs.
- **Before:** "This stunning, seamless platform offers a rich tapestry of
  game-changing features."
- **After:** "The platform does three things: import, dedupe, and export.
  The dedupe is the only part competitors do not have."
- **Restraint:** actual marketing copy the user asked for can be vivid. Match
  the brief. This pattern is about unbidden ad-speak in neutral prose.

### 6. Vague attribution and weasel words

- **Detect:** "experts say," "studies show," "many believe," "it is widely
  regarded," "some argue."
- **Why it reads as AI:** the model invokes consensus it cannot source.
- **Before:** "Experts say the approach is generally effective."
- **After:** "In the 2024 Cochrane review of 12 trials, it beat placebo in 9."
  (If no source exists, drop the claim or own it: "I think it works.")
- **Restraint:** honest uncertainty stated as the writer's own ("I am not
  sure, but my read is...") is human and should stay.

### 7. Sycophantic and servile tone

- **Detect:** "Great question!" "I hope this helps," "happy to dive deeper,"
  reflexive praise of the topic or reader.
- **Why it reads as AI:** assistant-training rewards agreeableness; it leaks
  into the prose.
- **Before:** "That's a fantastic point, and it's absolutely worth exploring
  this important topic further."
- **After:** (delete entirely; start with the substance.)
- **Restraint:** genuine warmth in a personal letter or note is not servility.
  Context decides.

### 8. Filler phrases

- **Detect:** "due to the fact that," "in order to," "it is worth noting
  that," "in the realm of," "when it comes to."
- **Why it reads as AI:** padding raises token count without raising content.
- **Before:** "In order to improve performance, it is worth noting that
  caching, when it comes to read paths, helps."
- **After:** "Caching the read path cut p95 latency in half."
- **Restraint:** "in order to" once, for rhythm, is not a crime. Flag the
  cluster, not the lone instance.

### 9. Excessive hedging

- **Detect:** stacked qualifiers: "may potentially sometimes," "it could
  arguably be considered," "in some cases this might possibly."
- **Why it reads as AI:** safety training rewards non-commitment.
- **Before:** "This could potentially, in some cases, arguably be considered a
  minor improvement."
- **After:** "This is a small improvement. It saves about 200ms."
- **Restraint:** one honest hedge on a genuinely uncertain claim is good
  writing. Mixed feelings are a human marker (see do-not-flag.md). Keep them.

---

## Family C: Formulaic structure

The model defaults to template shapes. Fixes here change the architecture of
the passage, not its words.

### 10. Formulaic "challenges and future prospects"

- **Detect:** a section that lists generic difficulties followed by generic
  optimism: "Despite challenges, the future looks bright."
- **Why it reads as AI:** it is a learned essay scaffold filled with
  placeholders.
- **Before:** "Despite challenges around adoption and cost, the future of the
  technology remains promising."
- **After:** "The blocker is cost: it is 4x the incumbent and the price has
  not moved in two years. Nobody has a credible plan to change that."
- **Restraint:** a real, specific risk-and-outlook discussion is valuable.
  Specificity is the line.

### 11. Negative parallelism and tailing negation

- **Detect:** "not only X but also Y," "it's not about X, it's about Y," and
  clipped negations appended for drama: "...and that's no accident."
- **Why it reads as AI:** the contrastive frame is a high-probability rhetorical
  reflex.
- **Before:** "It's not just a tool, it's a movement. And that's no accident."
- **After:** "It is a tool. About 9,000 teams use it daily."
- **Restraint:** "not only... but also" used once for a true two-part point is
  ordinary English. Flag the reflex, not the construction.

### 12. Rule-of-three overuse

- **Detect:** ideas forced into triads everywhere: "fast, simple, and
  powerful"; three-item lists where two or four would be honest.
- **Why it reads as AI:** tricolons are rhythmically rewarded and overfit.
- **Before:** "It is fast, reliable, and scalable, offering speed, safety,
  and simplicity."
- **After:** "It is fast. It is not yet reliable: there is a known crash on
  reconnect."
- **Restraint:** one well-earned tricolon in a piece is good prose. The tell
  is the *pattern* of threes, not any single three.

### 13. Generic positive conclusion

- **Detect:** an ending that affirms vaguely: "Ultimately, this represents an
  exciting step forward for everyone involved."
- **Why it reads as AI:** the model resolves on an upbeat major chord by
  default.
- **Before:** "Ultimately, this is an exciting development that will benefit
  the entire ecosystem."
- **After:** "Whether it matters depends on the pricing, which ships in Q3.
  Until then this is a demo."
- **Restraint:** a genuine, earned conclusion that happens to be positive is
  fine. The tell is vagueness and reflexive uplift, not positivity itself.

### 14. Signposting and announcements

- **Detect:** "Let's dive in," "In this section we will explore," "Now, let's
  take a closer look at."
- **Why it reads as AI:** the model narrates its own structure instead of
  delivering content.
- **Before:** "Let's dive into the three main benefits. First, let's explore
  performance."
- **After:** "Performance first. The rewrite cut cold start from 1.8s to
  0.4s."
- **Restraint:** a brief roadmap sentence in a long technical document can aid
  navigation. Once, with substance, is acceptable.

### 15. Diff-anchored writing

- **Detect:** prose, docs, or comments that describe what *changed* from a
  prior state instead of what the thing *is*: "this was added to replace,"
  "we removed X because," "the old method caused," "now uses Y instead,"
  "previously this did Z."
- **Why it reads as AI:** the model is anchored to the diff in its context
  rather than the artifact's steady state, so it narrates its own edit. The
  result is unreadable to anyone who does not know the prior version.
- **Before:** "This function was added to replace the previous approach of
  iterating through all items, which caused O(n^2) performance, so we now use
  a hash map instead."
- **After:** "This function uses a hash map for O(1) lookups per item,
  avoiding the O(n^2) cost of naive iteration."
- **Restraint:** version-scoped documents (changelogs, release notes,
  migration guides, PR and commit messages) are *supposed* to reference
  change. The tell is diff-narration in steady-state docs, code comments, and
  prose, where only the present state matters.

---

## Family D: Lexical tics

Specific words and micro-constructions that cluster in machine prose. Replace
by re-thinking the sentence, never by swapping in a single fixed synonym (that
just creates a new signature; see SKILL.md anti-signature guidance).

### 16. Overused AI vocabulary

- **Detect:** "delve," "landscape," "tapestry," "realm," "navigate the
  complexities," "robust," "leverage," "crucial," "pivotal," "underscore,"
  "myriad," "testament," "showcase," "foster," "intricate."
- **Why it reads as AI:** these are disproportionately frequent in model output
  relative to human baselines.
- **Before:** "We must delve into the intricate landscape to leverage robust,
  crucial insights."
- **After:** "We dug into the logs. Two queries caused 80% of the load."
- **Restraint:** any of these words can be the right word once. "Robust" in a
  statistics context is precise. Flag clustering and reflex use, not the word.

### 17. Elegant variation (synonym cycling)

- **Detect:** the same referent renamed every mention to avoid repetition:
  "the dog... the canine... the four-legged companion... the pup."
- **Why it reads as AI:** an overlearned "don't repeat words" heuristic applied
  past the point of clarity.
- **Before:** "The startup raised a round. The fledgling venture... The young
  firm... The nascent company..."
- **After:** "The startup raised a round. The startup spent it in eight
  months." (Repeating the plain noun is usually correct.)
- **Restraint:** purposeful, limited variation for genuine flow is normal
  craft. The tell is compulsive, clarity-harming cycling.

### 18. False ranges

- **Detect:** "from X to Y" where the endpoints are not a real continuum:
  "from coding to creativity," "from startups to enterprises."
- **Why it reads as AI:** the range frame sounds comprehensive while saying
  little.
- **Before:** "It helps with everything from productivity to happiness."
- **After:** "It does one thing: it batches your notifications into a 6pm
  digest."
- **Restraint:** a true numeric or ordered range ("ages 4 to 7," "from prototype
  to GA") is legitimate.

### 19. Hyphenated-pair overuse

- **Detect:** stacked compound modifiers as a default register: "data-driven,
  results-oriented, future-proof, end-to-end, best-in-class."
- **Why it reads as AI:** consultancy-deck phrasing is dense in training data.
- **Before:** "Our data-driven, results-oriented, end-to-end solution is
  best-in-class."
- **After:** "We A/B test every change. Last quarter, 6 of 19 tests won."
- **Restraint:** a precise compound ("read-after-write consistency") is
  technical vocabulary, not a tic. Do not strip hyphens from genuine compound
  modifiers ("high-quality" is correct); the tell is the *stacking*, not the
  hyphen.

---

## Family E: Syntactic tics

### 20. Copula avoidance

- **Detect:** systematic dodging of "is/are" via "serves as," "stands as,"
  "represents," "boasts," "constitutes."
- **Why it reads as AI:** elevated linking verbs are overrewarded; plain "is"
  is treated as too flat.
- **Before:** "The library serves as a wrapper and boasts strong typing,
  representing a solid choice."
- **After:** "The library is a typed wrapper around the REST API. It is a good
  default."
- **Restraint:** "serves as" is correct when service or function is the actual
  point ("the room serves as both office and studio").

### 21. Passive voice and subjectless fragments

- **Detect:** agent consistently hidden: "mistakes were made," "it was
  decided," "the feature was deprioritized."
- **Why it reads as AI:** passive construction avoids committing to who did
  what; it is safe and high-probability.
- **Before:** "It was determined that the rollout would be paused."
- **After:** "The release team paused the rollout after the 2am page."
- **Restraint:** passive is correct when the agent is unknown, irrelevant, or
  the object is the true topic ("the protein is phosphorylated at Ser-9").
  Scientific and legal registers use it well. Do not crusade against it.

---

## Family F: Formatting and artifacts

Surface markers. Most are individually weak signals; the catalog flags them
because they *cluster*. Read the Restraint notes carefully here: this family
is where over-editing destroys legitimate human writing. The exception is
pattern 31 (chat-UI contamination), which is near-certain confirmation on its
own.

### 22. Em dash overuse

- **Detect:** the long dash (the em dash, U+2014) used repeatedly as an
  all-purpose connector, several per paragraph, where commas, colons, periods,
  or parentheses belong.
- **Why it reads as AI:** sales and blog registers (dash-heavy) are dense in
  training data, so the dash becomes a default joint.
- **Before:** a sentence welding three independent clauses together with em
  dashes where two periods belong.
- **After:** split into two sentences, or use a comma and a colon.
- **Restraint:** one or two em dashes in a whole piece is normal human
  punctuation. A writer with a known dash habit (see voice-matching.md) keeps
  it. Frequency and monotony are the tell, not the glyph. Note: this
  repository's own documentation avoids em dashes as a house style. That is a
  choice for these files, not a rule for rewrites and not a universal
  correctness claim.

### 23. Boldface overuse

- **Detect:** bold sprinkled on phrases mid-paragraph for emphasis the prose
  should carry itself.
- **Why it reads as AI:** the model mechanically marks "key" terms.
- **Before:** "This is **critical** because the **main benefit** is **speed**."
- **After:** "This matters because it is faster: 0.4s versus 1.8s."
- **Restraint:** bold for genuine UI labels, defined terms, or doc structure is
  correct. Prose emphasis is the problem, not all bold.

### 24. Inline-header vertical lists

- **Detect:** every bullet shaped "**Term:** one explanatory sentence," used
  where flowing prose would read better.
- **Why it reads as AI:** a learned listicle scaffold.
- **Before:** a five-bullet "**X:** ... **Y:** ..." list for what is really one
  short argument.
- **After:** two or three sentences of connected prose.
- **Restraint:** true reference material, option comparisons, and specs are
  legitimately lists. Do not de-list a genuine list.

### 25. Title case in headings

- **Detect:** "How To Improve Your Workflow" where sentence case is the
  document's norm.
- **Why it reads as AI:** blog-title casing is a frequent default.
- **Before:** "## The Key Benefits Of This Approach"
- **After:** "## Why this is faster"
- **Restraint:** match the surrounding document. If the project uses title case
  for headings, keep title case. Consistency beats the rule.

### 26. Decorative emojis

- **Detect:** emojis ornamenting headings, bullets, or sentence ends.
- **Why it reads as AI:** chat-assistant formatting habit.
- **Before:** a heading or bullet decorated with a rocket or checkmark emoji.
- **After:** the same line with the decoration removed.
- **Restraint:** if the user's medium genuinely uses emoji (some social posts,
  some product UIs) and they asked for that register, match it.

### 27. Curly quotation marks

- **Detect:** typographic curly quotes and apostrophes where the surrounding
  text or codebase uses straight quotes.
- **Why it reads as AI:** some models emit smart quotes by default.
- **Before:** a sentence with curly quotes inside an otherwise straight-quote
  document.
- **After:** straight quotes, matching the document.
- **Restraint:** curly quotes alone are NOT an AI tell (many CMSs and word
  processors insert them for humans). Only normalize for consistency with the
  surrounding text. Never flag this in isolation.

### 28. Collaborative chatbot artifacts

- **Detect:** "Sure! Here's the rewrite:", "Let me know if you'd like me to
  adjust anything," "Certainly, I can help with that."
- **Why it reads as AI:** assistant turn-taking scaffolding bleeding into the
  artifact.
- **Before:** "Certainly! Here is your improved paragraph: ... Let me know if
  you want changes!"
- **After:** (deliver the paragraph only; no preamble, no sign-off.)
- **Restraint:** in genuine conversational chat this framing is fine. It is a
  tell only when it contaminates a standalone written deliverable.

### 29. Knowledge-cutoff and capability disclaimers

- **Detect:** "as of my last update," "I do not have access to real-time
  data," "based on my training."
- **Why it reads as AI:** model self-reference leaking into prose.
- **Before:** "As of my knowledge cutoff, the latest version is 3.2."
- **After:** "The latest version is 3.2 (released March 2025)." (Or, if truly
  unknown: "Check the changelog for the current version.")
- **Restraint:** a human writer's honest temporal caveat ("as of this writing,
  the API is still in beta") is legitimate and should stay.

### 30. Fragmented headers

- **Detect:** a heading immediately followed by a single sentence that just
  restates the heading, then the real content.
- **Why it reads as AI:** template echo: header, then a throat-clearing
  paraphrase of the header.
- **Before:** "## Performance\nPerformance is an important consideration.\nThe
  rewrite cut..."
- **After:** "## Performance\nThe rewrite cut cold start from 1.8s to 0.4s."
- **Restraint:** a heading followed by a genuine framing sentence that adds
  context (not a restatement) is good structure.

### 31. Chat-UI contamination artifacts

- **Detect:** strings that exist only because text was pasted out of a chat or
  search interface without scrubbing: citation and markup tokens
  (`turn0search0`, `citeturn0news`, `:contentReference[oaicite:0]`,
  `oai_citation`, `[web:1]`, `[attached_file:1]`, JSON-shaped attribution
  payloads), tracking parameters (`utm_source=chatgpt.com`,
  `referrer=grok.com`), unfilled placeholders (`[INSERT NAME]`, `[COMPANY]`,
  `[YEAR]`, `2025-xx-xx` access dates), and leftover scaffolding (stray
  triple-backtick fences around prose, "Would you like me to convert this to
  a table?").
- **Why it reads as AI:** these do not occur in genuinely human-written prose.
  Unlike every other pattern in this family, presence is near-certain
  confirmation, not a weak signal. This is the one pattern where a single
  instance is decisive.
- **Before:** "...meeting compliance requirements:contentReference[oaicite:4].
  Let me know if you'd like this as a table."
- **After:** "...meeting compliance requirements." (Remove the artifact
  entirely. If a placeholder like `[COMPANY]` is present, fill it from the
  source if the source supplies it, otherwise flag it to the user; never
  invent a value.)
- **Restraint:** a citation marker the writer intentionally placed, or a
  placeholder a writer is knowingly using in a working template, is content,
  not contamination. Distinguish leaked machinery from intended structure.

### 32. Debunking-pose headings

- **Detect:** headings that pose against an implied wrong version of the topic
  without delivering anything a plain heading would not: "The real reason X,"
  "X, actually," "The truth about X," "X, demystified," "Why everyone is
  wrong about X," "The X nobody tells you about," "X: what they don't tell
  you."
- **Why it reads as AI:** pattern 4 (persuasive authority) and pattern 1
  (significance inflation) operating at the heading level. The pose promises a
  reveal it does not keep. Headings slip through editing because editors,
  human and machine, treat them as structure rather than copy.
- **Before:** "## The real reason your tests are slow"
- **After:** "## Why the suite takes nine minutes" (name the actual content).
- **Restraint:** a heading that genuinely contradicts a specific widespread
  belief, where the section then delivers exactly that contradiction, is
  earned. The tell is the pose without the payoff.

---

## Closing note: fix by re-thinking, not find-replace

Every entry above is a symptom. The cause is the same in nearly all of them:
the model produced the highest-probability shape instead of the true,
specific thing. The reliable fix is to ask "what is actually being said here?"
and write that, in concrete terms, with the sentence length the thought
deserves. Swapping "delve" for "explore" everywhere does not humanize text; it
relocates the signature. Replace the thought, vary the structure, and most of
these patterns dissolve at once.

One sharp boundary on "concrete": it means the real specifics already present
in the text, surfaced and stated plainly, not specifics you invent to fill the
gap. Several patterns here (1, 5, 6, 13) tell you to replace vague inflation
with the concrete claim underneath. When there genuinely is no concrete claim
underneath (pure scaffolding), the correct move is to say less, not to supply
a number, date, name, or example the source never had. A manufactured
specific is the most human-sounding output you can produce and the worst,
because it is a confident lie wearing a real writer's voice. If you find
yourself about to add a detail to make a thin sentence land, cut the sentence
down instead. Then go to do-not-flag.md and check what you should have left
alone, including anything you were tempted to add.

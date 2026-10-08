# Worked Examples

Read this when you are unsure what good output looks like. Five full runs:
generic de-slop, voice-first, restraint, stance mode, and text hygiene. Each
shows the input, brief pass-by-pass reasoning, and the final deliverable in the
exact output contract.

The third example is the most important. It shows the skill correctly doing
almost nothing to prose that only looks sloppy. If you can do Example 3, you
will not over-edit.

---

## Example 1: Generic de-slop (no voice available)

**User:** "this reads like ChatGPT, can you fix it"

**Input:**
> In today's rapidly evolving digital landscape, it is important to note that
> customer feedback stands as a pivotal cornerstone of product success.
> Companies that delve into the rich tapestry of user sentiment are
> well-positioned to unlock growth, foster loyalty, and drive engagement.
> Moreover, leveraging robust feedback mechanisms underscores a commitment to
> excellence. Ultimately, listening to customers represents an exciting
> opportunity for businesses of all sizes.

**Step 0:** No sample, no author named. `Glob` finds no VOICE.md or
STYLE-GUIDE.md. Generic mode. Skip Pass 1.

**Pass 2 (tell removal, against the catalog):** Inflated significance
("pivotal cornerstone," pattern 1). AI vocabulary cluster ("landscape,"
"delve," "tapestry," "robust," "foster," pattern 16). Filler and hedging ("it
is important to note," pattern 8). Rule-of-three ("unlock growth, foster
loyalty, and drive engagement," pattern 12). Generic positive conclusion
("Ultimately ... represents an exciting opportunity," pattern 13). The whole
thing asserts importance and says nothing concrete. Fix by writing the actual
claim, and introduce real sentence-length variance.

**Pass 3 (self-audit):** What still reads as machine? The original had no
specifics at all, so the rewrite must not invent any. An early draft reached
for "quarterly surveys" and "a two-person team"; both sound human and both are
invented, so both go. Keep it short and honest. Check: did I install a
uniform rhythm? Vary the closing sentence so it does not match the opening
shape. "Drive engagement" adds nothing that keeping customers does not already
cover, so fold it in and say so in the meaning check.

### Humanized draft
Voice: generic
Density: high -> full pass
Text hygiene: no suspicious characters visible

> Customer feedback is central to whether a product succeeds. Companies that
> pay attention to what their users say are better placed to grow and to keep
> the customers they have. Taking the trouble to collect it well shows that a
> company cares about quality. Size does not change that.

### What changed
- Inflated significance and copula avoidance: "stands as a pivotal
  cornerstone" is now "is central to"; the importance framing is gone.
- Lexical tics: removed the landscape / delve / tapestry / robust / foster
  cluster and "leveraging."
- Filler and hedging: cut "it is important to note" and "Moreover."
- Formulaic structure: the growth / loyalty / engagement triad is now a pair,
  and the "exciting opportunity" close is a flat five-word sentence.
- Rhythm: sentence lengths now swing from a five-word close to a
  twenty-one-word middle sentence.

### Deliberately left alone
- The neutral, mildly persuasive register. The user did not give a voice, so
  generic mode keeps a plain professional tone rather than inventing a persona.
- The generality. The source never says how much feedback helps or why, so
  the rewrite stays general instead of supplying numbers or anecdotes.

### Meaning check
The four claims survive: feedback matters to product success, attentive
companies are better placed to grow and keep customers, collecting feedback
well signals care for quality, and this holds at any size. "Drive engagement"
was folded into keeping customers rather than restated. No facts, numbers, or
examples were added.

### Next step
No file path was given. Stopping here.

---

## Example 2: Voice-first (a VOICE.md was found)

**User:** "humanize this and make it sound like me, my style file is in the
repo"

**Input:** same paragraph as Example 1.

**Discovered `VOICE.md`** (the same file as the eval fixture
`evals/files/VOICE.md`):
```
# Voice

## Cadence
Short. Blunt. One long sentence per paragraph, maximum, for contrast.

## Diction
Plain Anglo-Saxon. No business words. Mild profanity allowed.

## Signature moves
Start sentences with "And" or "But." Ask a rhetorical question, then answer it.

## Avoid
Adverbs. The word "leverage." Tricolons. Uplift.

## Stance
Skeptical, a little tired, has seen the cycle before.

## Sample
Most "process improvements" are just meetings with a new name. We tried the
new sprint board for a month. It did not ship anything faster. It just gave
everyone a tidier place to watch the same work not happen. The thing that
actually helped was boring: we deleted half the backlog and stopped lying
about dates.
```

**Step 0:** Profile found. Voice mode. Read voice-matching.md.

**Pass 1 (voice injection):** Re-cast toward the profile first: short blunt
sentences around one long contrast sentence, a rhetorical question answered at
once, an "And" or "But" opener, a skeptical, tired stance, no tricolons, no
uplift. The bullets also ban adverbs, yet the profile's own Sample uses "just"
and "actually." voice-matching.md says the Sample beats the self-description,
so a stray "just" would be in voice. This rewrite did not need one.

**Pass 2 (tell removal, within the voice):** Same catalog flags as Example 1,
but the fixes must stay inside this voice. The generic rule says vary rhythm;
this voice *is* a rhythm (short, with one long sentence), so respect the
profile over the generic default.

**Pass 3 (self-audit):** Tells gone? Yes. Voice intact and not a caricature?
Keep the skepticism dry, not a parody of world-weariness. Check the avoid-list
once more: no "leverage," no tricolon, no uplift. Then check faithfulness. A
skeptical voice invites invented asides (a consultant, a slide deck, a survey
nobody reads); none of them are in the source, so none go in. The stance stays
a reaction to what the source says.

### Humanized draft
Voice: from VOICE.md
Density: high -> full pass
Text hygiene: no suspicious characters visible

> Does customer feedback matter to a product? Yes. A lot rides on it.
> Companies that listen to their users are in better shape to grow and to
> hang on to the ones they have, and doing the work to hear them out shows
> they care about getting it right. None of this is news. But it holds for a
> small shop the same as a big one.

### What changed
- Voice: re-cast per VOICE.md into short blunt sentences around one long one,
  with a rhetorical question answered at once, a "But" opener, and a tired,
  been-here-before stance.
- Lexical tics: removed the landscape / delve / tapestry / robust cluster and
  "leverage" (explicitly on the avoid-list).
- Formulaic structure: the growth / loyalty / engagement triad is now a pair
  (tricolons are on the avoid-list), and the "exciting opportunity" close is
  flat.
- Inflated significance and filler: "pivotal cornerstone," "it is important
  to note," and "Moreover" are gone.

### Deliberately left alone
- The rhetorical question and the dry "None of this is news." Both could pass
  for tells, but the profile asks for question-then-answer and a tired,
  skeptical stance; here they are voice.

### Meaning check
The four claims survive: feedback matters to a product's success, companies
that listen are better placed to grow and keep users, the effort of hearing
users out signals care for quality, and this holds at any size. "Drive
engagement" was folded into keeping users. "None of this is news" is the
profile's stance toward those claims, not a new claim about the world. No
facts, numbers, or examples were added.

### Next step
The user pointed to a style file, not a target file for the draft, so there
is nothing to write. Stopping here.

---

## Example 3: Restraint (genuine human prose that only looks sloppy)

**User:** "make this sound less like AI"

**Input (a real person, formal register, a colon, a parenthetical, one
tricolon):**
> I have taught this seminar for nineteen years, and the pattern never
> changes: the students who struggle most in October are, almost without
> exception, the ones who do best in May. What looks like confusion in week
> three (the long silences, the abandoned drafts, the office-hours visits that
> start with "I think I'm lost") is usually the sound of someone actually
> rebuilding how they read. It is uncomfortable to watch and worse to
> experience. I no longer try to rescue them too early.

**Step 0:** No voice file, no sample. Generic mode.

**Pass 2 (tell removal):** Run the catalog honestly. Candidate flags and the
verdicts:
- A tricolon ("the long silences, the abandoned drafts, the office-hours
  visits"): pattern 12, but it is a single earned list with a specific,
  concrete payload, not reflexive padding. Leave it.
- The colon after "never changes" and the parenthetical aside: ordinary human
  syntax doing real work. A single strong connective like this is normal
  punctuation, the same way one or two em dashes would be (pattern 22
  restraint); it is not a tell.
- "almost without exception": mild hedge, but it is the writer's honest,
  load-bearing qualifier (pattern 9 restraint, and a human marker in
  do-not-flag.md Part 2). Keep it.

There is nothing machine here. The prose has specific details (nineteen years,
October, May, week three, a quoted student line), mixed feeling (uncomfortable
to watch and worse to experience), and real sentence-length swing. These are
the human markers do-not-flag.md says to protect.

**Pass 3 (self-audit):** The honest answer to "what would tip a reader that a
machine wrote this" is: nothing would. A heavy rewrite here would be the
failure. Output minimal edits (none needed) and explain the restraint.

### Humanized draft
Voice: generic
Density: low -> light pass
Text hygiene: no suspicious characters visible

> I have taught this seminar for nineteen years, and the pattern never
> changes: the students who struggle most in October are, almost without
> exception, the ones who do best in May. What looks like confusion in week
> three (the long silences, the abandoned drafts, the office-hours visits that
> start with "I think I'm lost") is usually the sound of someone actually
> rebuilding how they read. It is uncomfortable to watch and worse to
> experience. I no longer try to rescue them too early.

(Unchanged. This is already human writing.)

### What changed
- Nothing. No machine tells were present.

### Deliberately left alone
- The colon and the parenthetical aside: a single strong connective and one
  aside, within normal human range (pattern 22 applies the same restraint to
  one or two em dashes), not artifacts.
- The tricolon: a single earned list with concrete content, not pattern-12
  padding.
- "almost without exception": the writer's honest qualifier and a human
  marker; removing it would change the claim.

### Meaning check
Nothing changed, so nothing to drift. Flagging this would have stripped
specific detail and voice from genuine human prose, which is the worst error
this skill can make.

### Next step
No file path was given. Stopping here.

---

## Example 4: Stance mode on (opt-in liveliness without fabrication)

**User:** "humanize this and give it some edge, don't keep it so neutral:
Our migration from a monolith to microservices was completed over seven
months (January to July 2024) by a team of twelve engineers. Using Kubernetes,
deployment time fell from 45 minutes to 6. Infrastructure costs rose 18%
temporarily during the transition."

**Step 0:** No voice file, no sample. **Step 0b:** the user explicitly asked
for edge and "not so neutral", so stance mode is on. Generic + stance.
**Step 0c:** no dead-giveaway tells, so density is low. The light pass limits
tell removal; the requested stance still reshapes register and rhythm.

**Pass 2 (tell removal, with stance):** de-slop normally, but the narrator now
has a point of view about the stated facts. The danger to watch: stance must
stay a reaction to what is there. The source says costs rose 18%; it does not
say why. An opinion about the 18% is allowed; an invented reason for it is
not.

**Pass 3 + Meaning check (extra force in stance mode):** confirm every
opinionated clause attaches to a stated fact, and that no cause, mechanism, or
event was smuggled in as "candor."

### Humanized draft
Voice: generic + stance
Density: low -> light pass
Text hygiene: no suspicious characters visible

> Seven months, twelve engineers, one monolith taken apart and put back
> together as microservices. January to July 2024. The headline number is the
> one worth caring about: deploys went from 45 minutes to 6 once we were on
> Kubernetes. That is not a tuning win, that is a different way of working.
> The bill has a catch. Infrastructure ran 18% higher during the move, and
> "temporarily" is carrying a lot of weight in that sentence.

### What changed
- Stance: added a clear point of view (the deploy number is what matters; the
  cost framing deserves skepticism), per the user's explicit request for edge.
- Rhythm and register: the flat report sentences became fragments, a short
  aside, and a longer close. The source had no machine tells to remove, so
  every change comes from the request for edge.

### Deliberately left alone
- Every figure: seven months, Jan-Jul 2024, twelve engineers, 45 to 6
  minutes, 18%, Kubernetes. Stance never touches the numbers.

### Meaning check
No facts, numbers, names, or claims changed. On stance discipline: the line
"that is a different way of working" is a judgment about the stated 45-to-6
result, not a new fact. The skepticism about "temporarily" is an opinion about
the source's own word, not an invented cost cause; I specifically did not
write anything like "costs rose because we ran both systems in parallel,"
since the source never states why costs rose. It also stops short of
implying the costs are still high, which the source does not say either. No
invented mechanism, event, person, or experience.

### Next step
No file path was given. Stopping here.

---

## Example 5: Text hygiene without language damage

**User:** "clean up this paragraph; I think copy-paste added hidden
characters, but keep the Persian word exact"

**Input, with invisible characters annotated for the example:**
> Customer[U+200B] feedback[U+00A0]helps. The Persian word
> می[U+200C]روم must stay exact.

**Step 0:** No voice file or sample. Generic mode. **Step 0c:** no prose tells,
so density is low and the wording should remain untouched. **Step 0d:** the
U+200B inside ordinary Latin prose has no semantic role, and the U+00A0 has no
layout role here. Remove the first and normalize the second. The U+200C inside
the Persian word is a load-bearing script joiner, so preserve it.

**Passes 2 and 3:** No language edit is needed. Verify that only formatting
changed and that the Persian word still contains its joiner.

### Humanized draft
Voice: generic
Density: low -> light pass
Text hygiene: cleaned: 1 zero-width character, 1 space normalized

> Customer feedback helps. The Persian word می‌روم must stay exact.

### What changed
- Text hygiene: removed one U+200B zero-width space and normalized one U+00A0
  no-break space that had no layout role.

### Deliberately left alone
- The wording, because no AI-writing tells were present.
- The U+200C joiner inside `می‌روم`, because it is part of the word's intended
  spelling and display.

### Meaning check
No facts, claims, or wording changed. The cleanup affected formatting only,
and the load-bearing Persian joiner was preserved.

### Next step
No file path was given. Stopping here.

---

## What these examples teach

1. Generic mode de-slops without inventing a persona or fake specifics.
2. Voice mode lets the profile override the generic rhythm rule; a clean
   rewrite that does not sound like the writer has failed.
3. The catalog is a question, not a verdict. Run every flag through its
   restraint note and do-not-flag.md before you touch anything. Doing nothing,
   explained, is a correct and common output.
4. Stance mode (opt-in) adds attitude, not content. An opinion about a stated
   fact is the goal; an invented cause or event behind that fact is the exact
   failure the mode is designed to prevent.
5. Text hygiene removes only high-confidence residue. A hidden character that
   carries language or display meaning stays.

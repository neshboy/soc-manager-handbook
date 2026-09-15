# SOC Manager's Operating Handbook — STYLE-GUIDE.md

**Status:** Adopted for Volume 3 of the NESHBOY SOC Professional Library, adapted from the Detection Engineering Handbook V2 `STYLE-GUIDE.md` for series consistency.
**Applies to:** every part, appendix, template, and figure in this book.
**Audience:** every writer, technical reviewer, and editor working on this book.

## Why this document exists

This is a cross-series brand standard, not a from-scratch style guide. The voice rules, the banned-filler list, and the general mechanic of "six content tags, one fixed callout-box system, four figure-evidence classes" are carried over near-verbatim from the Detection Engineering Handbook V2's style guide, which itself exists because that book's V1 shipped with real, diagnosed drift — the same callout rendering five different ways across parts, tags appearing bare in one part and bolded in the next, no diagram ever rendered. This book adopts the same fixed contract before a single unit is drafted, so a reader moving between all three NESHBOY volumes recognizes the same mechanics even though the subject matter — people and operations, not detection logic — is different. Only the *content* of the tags, callouts, and evidence classes is redesigned for a manager audience; the *mechanic* (bold bracketed tag, fixed blockquote template, no invented variants) is not.

**"Must"** means a PR gets rejected if it doesn't comply. **"Should"** means deviate only with a reason recorded in the PR description. **"Avoid"** is a strong default a reviewer can override with justification, and a documented override is a guide change, not silent drift.

This guide governs prose voice, Markdown conventions, the eight recurring callout boxes, content-level tags, cross-book citation format, and the evidence-classification system for figures. It does not cover technical review standards (accuracy of a cited detection claim, correctness of a budget model's arithmetic) — that is a separate concern with a separate reviewer, per the production model in `BOOK-INDEX.md`.

---

## 1. Voice and Tone

### 1.1 The core rule

Write like a senior SOC manager explaining a staffing, budget, or risk-acceptance decision to a peer who will have to defend it in the same room — not like a vendor blog post trying to rank for "SOC best practices 2026." The reader already knows what a SOC is and does not need to be sold on the importance of security. Every sentence should survive the question: **what does this actually tell me to decide, check, or expect?** If it doesn't, cut it.

Concretely:

- **State the claim, then the evidence.** Don't build up to it with scene-setting.
- **Name the failure mode; don't gesture at it.** "This burns out your best analyst in eight months" beats "this can present challenges to team sustainability."
- **Prefer the concrete number over the vague qualifier.** "A 1:6 analyst-to-shift-lead ratio is where coaching quality starts to slip" beats "staffing ratios significantly impact quality."
- **Name the mechanism, the dollar figure, the headcount number, the threshold** — not the adjective. Say what happens, not that something is important.
- **Prefer active voice with a named actor** ("the manager," "the analyst," "the vendor," "the board") over passive constructions that hide who does what. Passive is acceptable only when the actor genuinely doesn't matter ("the SLA is measured from ticket creation").
- **Commit to a claim.** If evidence is thin, say so explicitly ("this attrition-cost model is a rough industry-median estimate, not validated against this book's own data — treat it as a starting point for your own numbers") rather than hedging with vague qualifiers.
- Second person ("you") is fine for procedural instructions; first person plural ("we") is fine for the book's own reasoning. Neither should be used to manufacture urgency or as a substitute for a real subject in an explanatory sentence.
- It is okay to say a program is boring, cheap, or already solved. Not every staffing decision needs to sound like a transformation initiative.

### 1.2 Banned filler — and the actual rule behind the ban

The patterns below are banned **only in their AI-marketing-filler usage** — as a load-bearing transition, hedge, or intensifier that could be deleted with no loss of meaning, or that signals "content" rather than a claim. Mechanically grepping-and-blocking normal English is explicitly wrong: several of these words have legitimate, specific uses that are fine to keep. **The reviewer's test: does this phrase carry information, or does it just sound like it does?** If a reviewer can delete the phrase and the sentence loses nothing, it's filler — cut it. If they can't, it's not the pattern this ban targets — leave it. Do not add a global regex ban to a CI check for this reason: it will both miss the actual pattern (which is about rhetorical function, not literal string) and false-positive on legitimate uses.

| Banned pattern (as filler) | Why it's banned | Legitimate exception |
|---|---|---|
| "in today's rapidly evolving threat landscape" | Says nothing; every landscape is always evolving | None — always cut, replace with the specific change you mean |
| "it is crucial / critical / important / paramount that..." | Asserts importance instead of demonstrating it | Rewrite as the concrete consequence of not doing the thing |
| "robust posture / robust detection" | "Robust" as a vague virtue word attached to abstract nouns | Fine describing a specific measurable property: "robust to a 20% surge in ticket volume" |
| "leveraging" | Nearly always means "using" | Keep only if something is literally used as leverage in a specific mechanical sense (rare) |
| "holistic" | Vague scope-inflation word | Cut; say what specific things are actually being combined |
| "seamlessly" | Unfalsifiable marketing adjective | Cut; if integration quality matters, describe the failure mode when it *isn't* seamless |
| "delve into" | AI-pattern verb-of-choice for "discuss/examine" | Use "look at," "cover," "walk through" |
| "in conclusion" / "to summarize" as a section opener | Signposting the reader doesn't need — headings already do this | None in body prose; the book doesn't use a literal debate/thesis structure |
| "it is important to note that..." | Hedge that adds no information; if worth saying, say it directly | None — cut the phrase, keep the note only if something remains |
| "landscape" (standalone, as in "security landscape") | Vague spatial metaphor standing in for a specific claim | Fine in a literal geographic/org-chart sense ("the reporting landscape across three business units") |
| "unlock / empower / elevate" as verbs for tools enabling actions | Marketing verbs, not operational verbs | Use the literal verb: "lets the team triage faster," "gives the board visibility into," "cuts backlog age by..." |
| "at the end of the day" | Filler transition | Cut |
| "game-changer / game-changing / cutting-edge / best-in-class" | Unfalsifiable superlative | Cut, or state the measurable change |

A phrase is **not** banned just because it contains one of these words. Two tests:

- "This ratio is important because at 1:8 analyst-to-lead, coaching drops to a monthly cadence and QA findings stop translating into behavior change within the same quarter" — `important` is load-bearing and explained. Keep it.
- "The hiring landscape for mid-level analysts changed materially after two regional MSSPs opened local offices and started poaching at a 15% pay premium" — a specific, falsifiable claim, not the stock phrase. Keep it.

### 1.3 Worked GOOD vs. BAD examples

**Example 1 — opening a section**

> BAD: "In today's rapidly evolving threat landscape, it is crucial for SOC leaders to maintain a robust and holistic approach to staffing their teams."

> GOOD: "A 24/7 SOC covering three shifts with no overlap needs a minimum of 10–12 analysts to sustain one person per shift after accounting for PTO, sick leave, and training time — not the 6–7 a naive headcount-by-shift-count calculation suggests. The gap is shrinkage, and it's the single most common staffing-model error covered in Part 5."

**Example 2 — describing a limitation**

> BAD: "It is important to note that this approach may present certain challenges when leveraging vendor benchmarking data."

> GOOD: "This breaks the moment you compare your ratio against a vendor's published benchmark report: the report's respondent pool is self-selected — mostly the vendor's own customers who agreed to be surveyed — so a 1:12 analyst-to-alert-volume ratio in the report tells you nothing about whether that's healthy, only that it's common among that vendor's buyers."

**Example 3 — closing a section**

> BAD: "In conclusion, a holistic, seamless approach to SOC staffing will empower teams to elevate their operational posture."

> GOOD: "None of this works if the headcount model is rebuilt once at budget time and never touched again. A model built in January against last year's alert volume is already wrong by the time a new detection ships in March and doubles the queue for one specific alert type."

**Example 4 — a hedge that should just be a claim**

> BAD: "It is crucial to note that promoting a top analyst into a management role is paramount to consider carefully."

> GOOD: "Your best analyst and your best manager are not the same skill, and promoting one into the other without a transition plan is one of the most common ways SOCs lose both a strong analyst and gain a struggling manager in the same move. Test for management aptitude — coaching, delegation, difficult conversations — before the promotion, not after."

**Example 5 — false confidence vs. honest uncertainty**

> BAD: "This retention program provides a robust, comprehensive solution to SOC attrition."

> GOOD: "This retention program addresses burnout-driven exits in the 12–24 month range through rotation and career-pathing. It does not address competitor poaching at the senior-analyst level — see Part 18 for why pay-band correction, not culture, is the lever that actually moves that number."

### 1.4 Sentence and paragraph mechanics

- Default to active voice; passive only when the actor genuinely doesn't matter.
- One claim per sentence where possible. If a sentence needs three commas and an em dash to hold together, it's probably two sentences. Prefer sentences under ~30 words; if a sentence has more than one comma-joined independent clause carrying operational content, split it.
- One idea per paragraph. A paragraph that introduces a staffing model, then its failure mode, then a budget implication, then a cross-reference should be four short paragraphs or a callout box, not one block.
- Numbers: use digits for headcount, percentages, dollar amounts, SLA minute/hour values, and any count ≥ 10; spell out one through nine in prose ("three analysts," not "3 analysts") — except inside tables, where digits are always used for scanability, and except for counts paired with an identifier or unit (Tier 2, a 15-minute SLA, Part 27, a 1:8 ratio), which always use digits regardless of size.
- Contractions ("doesn't," "isn't," "won't") are fine and preferred — this book has a spoken-voice register, not a legal-document register.

---

## 2. Heading Level Conventions

Locked down for series consistency:

| Level | Use for | Example |
|---|---|---|
| `#` (H1) | Part title only. One per file, first line of the file. | `# Part 5 — Headcount & Capacity Modeling` |
| `##` (H2) | Major numbered sections within a part (the part's own table-of-contents entries). Number sequentially: `## 1. Title`, `## 2. Title`. | `## 3. Modeling shrinkage` |
| `###` (H3) | Subsections within a major section — a specific model, a specific template, a specific sub-topic. Number as `### 3.2 Title` under `## 3`, never restarted as an independent `### 1`. | `### 3.2 PTO, sick leave, and training-time deductions` |
| `####` (H4) | Rare; only for structured sub-breakdowns inside a long H3 that need their own anchor (e.g., "Inputs," "Worked example," "Common mistakes" inside one model writeup, when those aren't rendered as callout boxes). Do not nest deeper than H4. | `#### Common mistakes` |

Rules:

- **Callout boxes are never headings** (see §6) — they are blockquotes opened with a bold label, at the same nesting level as the paragraph they annotate. A callout must not consume a heading level, and a heading must never be used as a way to bold a single line of text.
- Never skip a level (no H2 directly to H4).
- Every part must open with an unnumbered `## Why this part exists` section before numbering starts at `## 1.` — mandatory for all 33 parts.
- Every H2 and H3 must be unique within its file — needed for stable anchor links from the index and cross-references.
- Section titles are sentence case, not Title Case ("Modeling shrinkage," not "Modeling Shrinkage"). Part titles use title case with an em dash, per the series convention (`# Part 5 — Headcount & Capacity Modeling`).
- When a named template or model gets a dedicated `###` walkthrough, format the heading as a plain descriptive label, not a restated sentence: `### The three-shift shrinkage model`, not `### This is how you calculate shrinkage for a three-shift model`.

---

## 3. Template, Worksheet & Framework Block Conventions

This book's structured artifacts are templates, worksheets, scorecards, decision matrices, and org/process diagrams — not source code. Fenced blocks are still used, but the convention is adapted from the Detection Engineering Handbook V2's code-block rules rather than copied wholesale:

| Content type | Fence tag | Notes |
|---|---|---|
| Reusable template body (job description, scorecard, memo, checklist) | `` ```text `` or `` ```markdown `` (whichever the template is authored in) | Precede with a one-line label: `TEMPLATE — <name>, permanent ID TMPL-####`. The template's permanent ID and its home appendix (per §5) go in that label line, not buried in prose. |
| Worked numeric example (budget line, headcount calculation, TCO model) | `` ```text `` | Every invented number in a worked example — a budget figure, a headcount count, a benchmark percentage that isn't sourced — carries the label `CONCEPTUAL SAMPLE — illustrative numbers, not sourced benchmark data` directly above the block. Reserve this for teaching examples; never label a real, sourced case this way (use the §9 evidence-class caption instead). |
| Org chart, RACI matrix, process/escalation flow, roadmap timeline | `` ```mermaid `` | See §10 — the fenced source stays in the file as the editable source of truth alongside its rendered image reference, never deleted once rendered. |
| Contract clause or policy language quoted verbatim from a real (anonymized) source | `` ```text `` | Must carry an evidence-class caption per §9 (typically `ANONYMIZED CASE EXAMPLE` or `OFFICIAL REFERENCE`), not just the fence. |

Additional rules:

- Every template block must be preceded by one sentence stating who uses it and when, and followed by one sentence stating its main limitation or the judgment call it doesn't automate — a bare template with no framing is grounds for reviewer rejection.
- Inline code (single backtick) is for field-like tokens inside prose — a template ID (`` `TMPL-0004` ``), a job-title code, a contract-clause number — never a substitute for a fenced block when showing more than one line of structured content.
- Annotations inside a template explain *why* a field exists or *what* a manager should write there, not restate the obvious: `<!-- state the specific coverage gap this shift pattern leaves, not "gaps may exist" -->`, not `<!-- this is a text field -->`.

---

## 4. Citing the Other Two Books — Cross-Reference Format

Because this book's entire value proposition rests on not re-explaining what SOC Playbook Handbook and Detection Engineering Handbook V2 already own, a sloppy or bare citation is a structural defect, not a style nit.

- **First cross-reference to a given part within a section:** full form — book title, comma, "Part NN," em dash, part title. `SOC Playbook Handbook, Part 27 — Escalation Quality`. `Detection Engineering Handbook V2, Part 41 — Detection Coverage`.
- **Subsequent references to the same part within the same section:** short form is fine — `SOC Playbook Part 27` or `DEH Part 41`. Never invent other abbreviations (no "STA," no "DEH2").
- **Never cite bare.** A cross-reference must state, in the same sentence, what the reader will find there — "for the mechanics of a good hand-off," "for the metric's exact definition," "for the technical cost of a schema migration." "See Part 27" with no reason is a lint failure.
- A single-clause pointer belongs inline. A pointer that needs more than one sentence of setup belongs in a **Cross-Book Pointer** callout (§6.6) instead of being stretched across surrounding prose.
- Every cross-reference added anywhere in the book must also be reflected in Appendix A8's lookup table — treated as a build-check requirement, not a nice-to-have, because A8 is the artifact a reader checks first when they suspect a topic is missing.
- Never cite a part number from memory without checking the current `BOOK-INDEX.md` of the target book — part numbers in either companion volume can shift on a future revision, and a stale citation is worse than no citation.
- Do not re-explain the cited material "just enough to be self-contained." If a paragraph needs more than the one-clause reason to make sense, that's a sign the paragraph is drifting into the other book's territory — cut it back to the pointer.

---

## 5. Referencing Templates, Cases & Figures

Permanent, position-independent IDs, tracked the same way the Detection Engineering Handbook V2 tracks detections, hunts, and figures:

- **`TMPL-####`** — every reusable template in the appendices. First reference in a chapter: full name plus ID, `the headcount calculator worksheet (TMPL-0001)`. Subsequent references in the same section: bare ID, `TMPL-0001`. Tracked in `TEMPLATE-INVENTORY.md`.
- **`CASE-####`** — every named case example used in a Management Autopsy box or a worked example (real, anonymized, or explicitly composite per §9). Same first-use/subsequent-use pattern. Tracked in `CASE-INVENTORY.md`.
- **`FIG-####`** — every rendered diagram or captured figure. Same pattern as the companion volumes. Tracked in `VISUAL-INVENTORY.md`.
- IDs are assigned once, at creation, and never reused or renumbered when the book's part order changes — this is what makes a cross-reference from another chapter (or another book) survive a reorganization.
- Never invent a placeholder ID "to be assigned later" in body text — request the next ID from the relevant inventory file before the unit is marked `reviewed`.

---

## 6. Callout Boxes — Exact Templates

All eight use the same base shape: a **blockquote** (`>`) opened with a bold label line, visually and structurally consistent with each other and distinguished only by label text and (for some) internal sub-structure. They sit inline in the flow of a section — never a jump-target the table of contents would list separately, and never nested one inside another.

**General template:**

```
> **[Label — optional short qualifier]**
> Body text, 1–5 sentences. Can include inline code and a short template excerpt if needed.
```

If a box needs more than ~5 sentences, it isn't a callout — promote it to a real `###`/`####` subsection with prose.

### 6.1 Management Autopsy

Dissects a real or realistic management decision that shipped broken: the decision, why it seemed reasonable, how it failed, what replaced it. The highest-frequency callout in the book.

```
> **Management Autopsy — "<the decision in one clause>"**
>
> **The decision:** <what was actually decided, plain description>.
>
> **Why it seemed reasonable:** <the logic that got this decision approved>.
>
> **How it failed:** <the specific mechanism, with a concrete scenario>.
>
> **The fix:** <what the corrected approach adds or changes>.
```

Worked example:

```
> **Management Autopsy — "promote the top analyst into the open team-lead slot"**
>
> **The decision:** The highest-performing Tier 1 analyst, with the best QA scores and fastest
> handle time, is promoted directly into a vacant team-lead role with no transition period.
>
> **Why it seemed reasonable:** She was the obvious top performer, and promoting from within
> signals a real career ladder to the rest of the team.
>
> **How it failed:** Individual triage skill and people-management skill are different
> competencies; six months in, she was still doing the fastest triage on the team herself instead
> of delegating, coaching, or running QA calibration — the team's overall throughput barely moved
> and she was working two jobs at once.
>
> **The fix:** Separate the promotion decision from the transition plan — a 90-day ramp with a
> reduced individual queue, explicit coaching-skill assessment (see Part 8's assessment methods
> applied internally), and a mentor who is already a team lead.
```

### 6.2 Manager's Note

A tactical, practitioner-voice aside — a tip or "this is what actually works" observation. Shorter and more informal than the other boxes, but still no filler.

```
> **Manager's Note**
> The tip or observation, stated as something you'd actually say out loud to another manager over
> coffee.
```

Worked example:

```
> **Manager's Note**
> Run your calibration session on a ticket everyone already agrees was handled well, before you
> run one on a disputed ticket. It's the fastest way to find out reviewers don't actually share a
> definition of "good" yet — better to discover that on an easy case than in a real disagreement
> that affects someone's review.
```

### 6.3 Operational Reality

A grounded statement about what actually happens in production SOC operations — staffing plans, budget assumptions, vendor promises — as opposed to what the plan or policy document implies.

```
> **Operational Reality**
> The gap between the documented plan and what actually happens in practice, stated as a fact,
> plus the practical consequence.
```

Worked example:

```
> **Operational Reality**
> A headcount model built once a year at budget time is already stale by the second quarter — new
> detections ship, alert volume shifts, and nobody updates the shrinkage assumption after two
> analysts go on parental leave in the same month. Treat the model as a living worksheet reviewed
> quarterly, not a number you defend once and forget.
```

### 6.4 Blind Spot

A specific, named gap in what a manager's visibility or process actually covers — organizational or programmatic, not a technical telemetry gap (that's the other books' Blind Spot usage).

```
> **Blind Spot**
> What this process/metric/program cannot see, stated specifically — the failure mode or
> population it misses.
```

Worked example:

```
> **Blind Spot**
> Exit interviews only capture why people who already decided to leave are leaving — they tell
> you nothing about the analyst who's disengaged, updating their resume, and hasn't resigned yet.
> A retention program built only on exit-interview themes is reacting to attrition that already
> happened, not the attrition that's six weeks from happening.
```

### 6.5 People Risk Trap

Names a specific, common people or process risk that will bite a manager, and what to do about it.

```
> **People Risk Trap**
> The specific common mistake or risk. The fix: the concrete process change that resolves it — or
> an explicit statement that this is a tradeoff with no clean fix.
```

Worked example:

```
> **People Risk Trap**
> Letting a QA program's findings feed directly into performance reviews with no calibration step
> teaches analysts to game the QA sample instead of doing consistently good work — if analysts can
> tell which tickets get reviewed, behavior shifts only on those tickets. Sample randomly, keep the
> sampling method undisclosed in its specifics, and calibrate reviewers before scores ever touch a
> review cycle.
```

### 6.6 Cross-Book Pointer

An explicit "go here for the mechanics" reference into SOC Playbook Handbook or Detection Engineering Handbook V2, used when a single inline citation (§4) isn't enough context to orient the reader.

```
> **Cross-Book Pointer**
> What this book does not cover here, which companion-book part covers it, and the one-clause
> reason a reader would actually go read it.
```

Worked example:

```
> **Cross-Book Pointer**
> This part does not explain how to score an alert's severity — that's a per-alert triage
> decision, not a staffing decision. See SOC Playbook Handbook, Part 29 — Playbook Severity Model
> for the scoring mechanics; come back here once you're using severity as an input to the workload
> model in §4 of this part.
```

### 6.7 Field Test

A concrete, reproducible exercise or drill a manager can run to validate that a program actually works, plus the expected result.

```
> **Field Test**
> **Setup:** what needs to be in place first, one line.
> **Action:** the exercise or drill, stated concretely.
> **Expected result:** what should be observably true afterward.
```

Worked example:

```
> **Field Test**
> **Setup:** A written surge-staffing plan exists on paper but has never been exercised.
> **Action:** Run an unannounced tabletop where the on-call lead is told, mid-exercise, that two
> of the four analysts named in the plan are "unreachable."
> **Expected result:** The plan should name a specific backup path (not just "escalate to the
> manager") and the backup path should resolve within the drill's timed window. If it doesn't,
> the plan is aspirational, not operational — fix it before relying on it in a real incident.
```

### 6.8 What Would Change My Mind

An explicit falsifiability statement — what evidence, if observed, would change the stated conclusion or confidence level. Carried over from the series' epistemic-honesty standard.

```
> **What Would Change My Mind**
> The specific observation, data point, or result that would overturn or materially revise the
> claim just made — a concrete, checkable condition, not a vague "more research needed."
```

Worked example:

```
> **What Would Change My Mind**
> This part assumes a 1:8 analyst-to-team-lead ratio is roughly where coaching quality starts to
> degrade, based on the case studies in Part 16. If a team consistently held QA scores and
> retention flat at 1:12 with a strong async-coaching system, that would move this book's default
> recommendation, and the confidence rating on this claim would drop from "generally reliable
> heuristic" to "context-dependent — audit your own coaching cadence before trusting the ratio."
```

### 6.9 Callout usage density

A single part typically carries one or two Management Autopsy boxes, zero-to-one People Risk Trap, and one Cross-Book Pointer where the topic genuinely borders another book; the rest are used opportunistically. A section stacking all eight callouts is over-boxed — if every paragraph needs an annotation, the prose isn't doing its job.

---

## 7. Content-Level Tags

Format locked to `**[TAG]**` — bold, brackets, all caps, placed at the start of the paragraph or subsection it governs. Never a heading, never a footer note, never two tags on one paragraph (a sign the paragraph is doing two jobs — split it).

| Tag | Use for | Do not use for |
|---|---|---|
| `[CONCEPT]` | Foundational explanation of an operating model, program, or decision, with no assumption the reader acts on it directly — the "what and why" a reader needs before anything else in the section makes sense. | Anything that specifies a concrete process, template, or number — that's a lower tag even if conceptually simple. |
| `[FRONTLINE MANAGER]` | Shift-lead/team-lead-facing content: day-to-day scheduling, coaching conversations, queue triage, the things a first-line manager does this week. | Budget, contract, or board-level content — that's `[SENIOR MANAGER]` or `[EXECUTIVE]`. |
| `[SENIOR MANAGER]` | SOC manager/director-facing content: headcount planning, budget defense, vendor negotiation strategy, cross-team politics, risk-acceptance calls. | Day-to-day coaching or scheduling mechanics that a team lead actually executes — that's `[FRONTLINE MANAGER]`. |
| `[HR/PEOPLE]` | Hiring process design, performance-management mechanics, career ladders, burnout/retention programs, culture — content that typically requires HR partnership or awareness even when the SOC manager owns the decision. | Budget or contract content with no people-process component — that's `[SENIOR MANAGER]` or `[VENDOR/PROCUREMENT]`. |
| `[VENDOR/PROCUREMENT]` | Tooling selection process, MSSP/vendor contract structuring, renewal negotiation, vendor governance and risk scoring. | Internal staffing or budget content with no external vendor involved. |
| `[EXECUTIVE]` | Content aimed at the CISO/board-facing conversation: reporting cadence and format, risk narrative construction, budget justification framed for non-technical stakeholders, crisis communication upward. | Internal reporting between a team lead and a SOC manager — that's `[FRONTLINE MANAGER]` or `[SENIOR MANAGER]`. |

Tagging guidance:

- Most `##` sections carry more than one tag across their subsections — a single section on QA program design plausibly has a `[CONCEPT]` opening, a `[SENIOR MANAGER]` subsection on program design and budget, an `[HR/PEOPLE]` subsection on calibration and performance-review integration, and a `[FRONTLINE MANAGER]` subsection on running the actual calibration session. That's expected and good.
- `[CONCEPT]` is the only tag allowed to open a section before any other tag appears — every section needs grounding before it gets role-specific.
- The two pairs authors most often confuse: `[FRONTLINE MANAGER]` (executes the process day to day) vs. `[SENIOR MANAGER]` (designs the process, defends its budget, owns the escalation when it breaks); `[HR/PEOPLE]` (the people-process mechanics themselves) vs. `[EXECUTIVE]` (translating those mechanics into a board-level risk or budget narrative). When in doubt, ask "who is the primary actor for this paragraph, and what room are they standing in" and match to the tag whose column that falls under above.

---

## 8. Table Conventions

- Every data table gets a one-line lead-in sentence stating what decision it supports, not just "the following table shows..." — e.g., "The table below maps shift-pattern options to their typical coverage gaps and burnout risk."
- Header row uses short noun phrases, capitalized like a title ("Typical Failure Mode," not "typical failure mode" or a full sentence).
- Left-align text columns; skip explicit `:---:` alignment markers unless a column is genuinely numeric and benefits from right-alignment.
- Cell content: fragments, not full sentences with terminal periods, unless a cell genuinely needs more than one sentence (rare — if so, reconsider whether it belongs in a table at all).
- Template IDs, case IDs, and field-like tokens inside cells use inline code ticks, same as in prose: `` `TMPL-0001` ``, `` `CASE-0012` ``.
- Never leave a cell blank — use an em dash "—" for "not applicable" so the omission is visibly deliberate.
- Cross-references to the other two books get their own greppable column where a table compares topics across the series, and must follow the §4 citation rules inside the cell too (full form on the row's first appearance in the table, short form after).
- Tables built from invented/illustrative data are marked `(CONCEPTUAL SAMPLE)` in the caption, same standard as template blocks in §3.

---

## 9. Figures: Evidence Classification

This book has far fewer screenshots than a technical volume, but real weight rests on org charts, RACI matrices, process/escalation-flow diagrams, and (occasionally) anonymized real artifacts — a redacted budget worksheet, a real headcount model, an actual QA scorecard. The same discipline the Detection Engineering Handbook V2 applies to screenshots and diagrams applies here, adapted to what this book actually has evidence of.

### 9.1 Evidence classes (exactly four, always tagged)

| Tag | Meaning | Allowed for |
|---|---|---|
| `ANONYMIZED CASE EXAMPLE` | Drawn from a real SOC/organization the author has direct knowledge of, with identifying details scrubbed or rounded (org name, exact dollar figures, headcount). Must be scrubbed of anything that could re-identify the organization before inclusion. | Redacted worksheets, real org charts, real QA scorecards, direct quotes from a real contract clause. |
| `COMPOSITE CASE EXAMPLE` | Constructed by merging patterns from multiple real situations into one illustrative narrative — used when a single traceable real case would be too identifiable or too thin to generalize from. Must state in the caption that it is composite. | Management Autopsy narratives, worked judgment-call case studies in Part 25. |
| `OFFICIAL REFERENCE` | Sourced from a published benchmark report, vendor documentation, industry survey, or standards body, reproduced or closely adapted with attribution. | Benchmark charts, published staffing-ratio survey data, cited industry frameworks. |
| `CONCEPTUAL` | An illustrative diagram or template with no claim of representing a captured real case. | Org charts, RACI matrices, process-flow/escalation diagrams, roadmap timelines, blank templates. |

A figure with no real captured evidence behind it yet is `CONCEPTUAL` if it's a diagram or template, or an explicit **pending placeholder** (§9.3) if it's meant to eventually be a real captured artifact. Never label an uncaptured, aspirational artifact `ANONYMIZED CASE EXAMPLE` "because a real one will be sourced later" — the tag describes what evidence backs the figure *right now*.

### 9.2 Caption format — rendered figure

```
**Figure N.M — [Short descriptive title].** *[Evidence class tag].* One to two sentences: what the
figure shows and what it's evidence of, or — for CONCEPTUAL figures — what it illustrates rather
than proves. If OFFICIAL REFERENCE: source citation. If ANONYMIZED/COMPOSITE CASE EXAMPLE: enough
context to be useful (org size band, industry, rough date) without being identifying.
```

Worked examples:

```
**Figure 3.1 — Tiered vs. tierless escalation flow.** *CONCEPTUAL.* Illustrates the structural
difference between a strict L1→L2→L3 hand-off model and a tierless "follow-the-alert" model. This
is a process diagram of two design options, not a capture of either model in production — see
Figure 3.2 for an anonymized real-world comparison.
```

```
**Figure 5.4 — A three-shift shrinkage model with a 34% deduction.** *ANONYMIZED CASE EXAMPLE.*
Headcount worksheet from a 24-person SOC (mid-market financial services, ~2026), with organization
name, exact salary bands, and specific analyst names removed. Shrinkage figure is real; headcount
total has been rounded to the nearest even number to reduce re-identification risk.
```

```
**Figure 31.2 — Published analyst-to-alert-volume ratios by organization size.** *OFFICIAL
REFERENCE.* Reproduced from [industry benchmark source noted in REFERENCES.md], year and
respondent-pool size as published. See Part 31 for the caveats on self-selected survey populations
before treating this as a target.
```

### 9.3 Pending placeholder format

```
> **[FIGURE PENDING — target evidence class: <ANONYMIZED CASE EXAMPLE | COMPOSITE CASE EXAMPLE |
> OFFICIAL REFERENCE | CONCEPTUAL>]** What the figure will show, one sentence. Why it isn't
> sourced/rendered yet, one sentence. What claim in the surrounding text it would support.
```

A reviewer finding this block logs it in the tracked-placeholder list in `VISUAL-INVENTORY.md`; it must be resolved before the unit ships — never left as permanent content.

---

## 10. Diagram Rendering Requirement

Org charts, RACI matrices, escalation-flow diagrams, and roadmap timelines are drafted as Mermaid source and treated the same way the Detection Engineering Handbook V2 treats every diagram — as a draft, not a deliverable:

- Every `` ```mermaid `` block must be rendered to a static image (SVG preferred, PNG acceptable) and committed alongside the source, referenced via the §9.2 caption format with a real evidence-class tag (almost always `CONCEPTUAL`, unless it's a literal reproduction of an `OFFICIAL REFERENCE` diagram).
- The Mermaid source stays in the file, directly above or below the rendered image reference — it is the editable source of truth, not dead weight to delete once rendered.
- A unit is not review-complete if it contains a `mermaid` fence with no paired rendered figure reference. This is enforced as a build check, not a manual convention (see `BOOK-INDEX.md` production model).

---

## 11. Review Checklist (for the independent reviewer, per unit)

Work from this list, not from vibes:

1. **Voice:** any banned filler pattern present without being rewritten? Any sentence that doesn't survive the "what does this tell me to decide/check/expect" test?
2. **Headings:** correct level nesting, no heading used as a bold-line substitute, `## Why this part exists` present?
3. **Templates/blocks:** every template block labeled with its name and `TMPL-####`, every invented worked number marked `CONCEPTUAL SAMPLE`, framing sentences present?
4. **Cross-book citations:** full form on true first use per section, short form after, never bare (§4 test: does the sentence state *why* the reader would go there), reflected in Appendix A8?
5. **IDs:** `TMPL-####`/`CASE-####`/`FIG-####` used correctly, no placeholder IDs left unassigned, inventories updated?
6. **Callouts:** correct label string, correct blockquote structure, body length in range, no box type nested in another, density not excessive (§6.9)?
7. **Tags:** every `##`/`###` subsection carries at least one `[TAG]`, no paragraph carries two?
8. **Tables:** lead-in sentence present, no blank cells, code-tick usage consistent with prose, cross-reference formatting followed inside cells?
9. **Figures:** every figure has a caption with an evidence-class tag; every pending figure uses the `[FIGURE PENDING]` blockquote and is logged in `VISUAL-INVENTORY.md`; every Mermaid block has (or is tracked toward) a paired rendered image?
10. **Scope-boundary check (this book's own version of the depth check):** does this unit re-explain anything already owned by SOC Playbook Handbook or Detection Engineering Handbook V2 instead of citing it? This is the single most important item on this list, given the book's entire reason for existing.

Match this guide over inventing local precedent. Any deviation a reviewer approves gets recorded as a documented change to this file, not silent local drift.

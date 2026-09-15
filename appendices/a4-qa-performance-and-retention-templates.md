---
title: "Appendix A4 — QA, Performance & Retention Templates"
appendix: "A4"
author: "author-agent"
reviewer: "technical-reviewer-agent"
status: "reviewed"
last_validated: "2026-09-15"
depends_on: ["part15", "part16", "part18"]
---

# Appendix A4 — QA, Performance & Retention Templates

## Why this appendix exists

**[CONCEPT]** This appendix carries the four fillable artifacts that Part 15 — Quality Assurance Programs, Part 16 — Performance Management & Coaching, and Part 18 — Attrition & Retention each build toward but stop short of publishing in full: a QA ticket scorecard (`TMPL-1501`), a calibration-session guide (`TMPL-1502`), a performance-improvement-plan template (`TMPL-1601`), and an exit-interview question set (`TMPL-1801`). None of the four is new content — each one is the working paper version of a structure those three parts already justify, section by section, on the reasoning that a rubric, a session format, a plan, or a question set needs to exist *before* the judgment calls those parts spend most of their pages on can happen at all.

**[CONCEPT]** The four templates are also a deliberate chain, not four unrelated forms. A QA scorecard (§1) produces the score that Part 15's sampling and calibration program is built to trust; a calibration-session guide (§2) is how a team keeps more than one reviewer's scorecard meaning the same thing; a performance-improvement plan (§3) is where a *sustained, calibrated* pattern of low scores ends up, per Part 16's three-stage pipeline, and only after the diagnostic in that part's §3 has ruled out a training gap or a broken rule; and an exit-interview question set (§4) is run on the analyst a manager couldn't keep, coded against the same attrition taxonomy Part 18 builds its retention levers from. Read together, they cover the full path from "did this analyst do good work on this ticket" to "why did we lose this analyst," which is not a coincidence — Parts 15, 16, and 18 were written as one continuous accountability chain for exactly that reason.

**[CONCEPT]** None of the four templates automates the judgment call the companion part spends its pages developing. A scorecard doesn't decide whether a rubric category is well-calibrated for a given ticket type; a PIP form doesn't decide whether a recurring miss is a skill gap or a broken detection rule; a question set doesn't make a departing analyst candid. Each template's limitation is stated explicitly where it appears below, per this book's own convention that a bare template with no stated limitation is treated as incomplete, not helpful.

## 1. QA ticket scorecard (`TMPL-1501`)

**[SENIOR MANAGER]** A team lead or QA specialist fills one of these out per sampled ticket immediately after reviewing it, rather than reconstructing a score from memory later — the same independent-judgment discipline Part 15 §3.2 requires of calibration-session scoring, applied here to routine, single-reviewer sampling rather than a shared batch. The category weights below are the illustrative starting rubric from Part 15's Table 15.2 (CONCEPTUAL SAMPLE — a reasonable default weighting, not a fixed standard); a program should revisit its own weights annually against what its own incident history says actually predicts a missed threat, per Part 15 §4.2.

```text
TEMPLATE — QA ticket scorecard, permanent ID TMPL-1501

Ticket ID:  ______________        Analyst reviewed:  ______________
Reviewer:   ______________        Review date:       ______________
Sampling reason:  [ ] Risk-weighted (P1/P2)   [ ] Random baseline   [ ] Targeted (complaint/reopen)
<!-- Sampling reason feeds the ratio Part 15 §2.3 tracks -- do not leave blank. -->

| Category                     | Weight | Score (1-5) | Weighted | Reviewer note (cite the specific evidence the score is based on) |
|-------------------------------|--------|-------------|----------|---------------------------------------------------------------------|
| Technical accuracy            | 30%    |             |          |                                                                       |
| Escalation judgment           | 25%    |             |          |                                                                       |
| Documentation completeness    | 20%    |             |          |                                                                       |
| Process adherence             | 15%    |             |          |                                                                       |
| Communication and tone        | 10%    |             |          |                                                                       |
| TOTAL WEIGHTED SCORE          | 100%   |             |          |                                                                       |

Below program's coaching threshold?  [ ] Yes   [ ] No
<!-- State your program's own numeric cutoff here once set -- Part 15 does not fix one for you. -->
Coaching conversation scheduled for (date):  ______________
<!-- Part 15 SS5.4's own Field Test checks this field gets filled, not left as an intention. -->
```

> **Manager's Note**
> Fill the reviewer-note cell for every category, not only the ones that scored low. A 5 with no note is indistinguishable from a rushed review, and the note is what makes a disputed score defensible weeks later, when neither reviewer remembers the ticket without it.

**[SENIOR MANAGER]** This scorecard does not decide, by itself, whether a low score is noise, a coaching moment, or evidence for Part 16's formal track — that routing decision is Part 15's Figure 15.2, and this form only supplies the calibrated input that decision needs.

## 2. Calibration-session guide (`TMPL-1502`)

**[FRONTLINE MANAGER]** A facilitator — usually the SOC manager or a senior reviewer — runs this guide at least once a quarter, the cadence Part 15 §6.2 sets, following the session mechanics Part 15 §3.2 lays out. Every reviewer scores the shared batch independently before Step 2 opens; comparing scores before independent scoring is complete defeats the session's purpose.

```text
TEMPLATE — Calibration-session guide, permanent ID TMPL-1502

Session date:  ______________     Facilitator:  ______________
Reviewers present:  ______________________________________________
Rubric version reviewed:  ______________
Batch (5-10 already-closed, unscored tickets):  ______________________

STEP 1 -- Independent scoring (complete before Step 2)
| Ticket ID | Category               | Reviewer A | Reviewer B | Reviewer C | Reviewer D | Spread |
|-----------|--------------------------|-----------|-----------|-----------|-----------|--------|
|           |                          |           |           |           |           |        |

STEP 2 -- Agreement calculation
% of category-scores within 1 point of that ticket's median across reviewers:  ______%
<!-- Part 15 SS3.3 treats <80% as not yet trustworthy for coaching or PIP input. -->

STEP 3 -- Divergent-category log (discuss widest-spread categories only; skip categories
already in agreement)
| Category | Ticket ID | Spread | What each reviewer weighed differently | Written anchor example agreed |
|----------|-----------|--------|------------------------------------------|----------------------------------|
|          |           |        |                                          |                                   |

STEP 4 -- Next step
Blind rescore date (same batch, ~2 weeks out):  ______________
Agreement target for rescore:  ______% (program's own working threshold)
```

**[FRONTLINE MANAGER]** This guide structures the conversation; it doesn't resolve a disagreement for the room. If Step 3's discussion keeps tracing back to "what does a good hand-off even require" rather than a scoring-consistency question, the gap is in the team's shared understanding of SOC Playbook Handbook, Part 27 — Escalation Quality, not in this rubric — see Part 15 §3.3's Cross-Book Pointer before assuming another anchor example will fix it.

## 3. Performance-improvement-plan template (`TMPL-1601`)

**[HR/PEOPLE]** A manager completes this only after Part 16 §3's three-hypothesis diagnostic has ruled out a training gap and a broken process, and only after the specific gap has already appeared in a dated, prior 1:1 note — the two preconditions Part 16 §4.1 sets before a PIP is opened at all. Route the completed draft through Part 27's legal-review step before delivery in any jurisdiction with meaningful wrongful-termination exposure.

```text
TEMPLATE — Performance improvement plan, permanent ID TMPL-1601

Analyst:  ______________          Manager:  ______________
Start date:  ______________       Plan length:  [ ] 30 days  [ ] 45 days  [ ] 60 days
Prior documented coaching this gap traces to (1:1 date):  ______________
<!-- Must predate this plan by more than a few days -- see the People Risk Trap below. -->
HR partner reviewed:  [ ] Yes, on (date) ______________   [ ] Not yet

PROBLEM STATEMENT
<!-- The specific, observable gap, tied to the 1:1 date above or a QA score (TMPL-1501) --
     not a general impression. -->
______________________________________________________________________

SUCCESS CRITERIA
<!-- A measurable target tied to an existing baseline (team QA average, handle-time norm,
     error rate on a named alert type) -- not a subjective bar. -->
______________________________________________________________________

SUPPORT COMMITTED
<!-- Specific coaching time, shadowing, or resources the manager is actually scheduling --
     not "will be available if needed." -->
______________________________________________________________________

CHECKPOINT LOG
| Checkpoint date | Progress against success criteria | Support delivered this period | Adjustment (if any) |
|------------------|--------------------------------------|----------------------------------|------------------------|
|                  |                                      |                                  |                        |

CONSEQUENCE OF NON-IMPROVEMENT (state plainly)
______________________________________________________________________

CLOSING OUTCOME (complete at plan end):
[ ] Criteria met -- plan closed          [ ] Partial, bounded extension granted (new end date: ____)
[ ] Criteria not met -- route to Part 27's termination-documentation process
```

> **People Risk Trap**
> A "prior documented coaching" field filled in retroactively, after the plan is already drafted, defeats the precondition it exists to prove — it launders a plan that was never actually preceded by real coaching into looking like one that was. Only complete that field by pointing to a 1:1 note dated and written before this plan was drafted, never backfilled the same week the plan opens.

**[HR/PEOPLE]** This template does not automate the diagnostic call in Part 16 §3 — no template can — and a completed form with a vague problem statement or no interim checkpoint is the exact failure pattern Part 16's `CASE-1602` shows collapsing under a wrongful-termination challenge.

## 4. Exit-interview question set (`TMPL-1801`)

**[HR/PEOPLE]** An HR partner, or a manager one level removed from the departing analyst's own chain, runs this — never the departing analyst's direct manager, who is both an interested party and often not trusted with a fully candid answer, per Part 18 §3.1. Code every answer against Table 18.1's taxonomy before filing; a set of uncoded narrative answers analyzes badly no matter how thorough the conversation felt.

```text
TEMPLATE — Exit-interview question set, permanent ID TMPL-1801

Departing analyst (role / tenure band, not name, for aggregation):  ______________
Interview date:  ______________     Interviewer:  ______________
Voluntary departure?  [ ] Yes   [ ] No (route to Part 16 -- not this program's territory)

FIXED QUESTIONS (ask in this order; do not paraphrase into a single open prompt)
1. What is the primary reason you're leaving?
2. Did compensation play a role? If so, how does the new role's pay compare to this one?
3. In the last 6 months, did workload, shift pattern, or on-call burden affect this decision?
4. Did you feel there was a clear path for growth here? What would that path have needed
   to include?
5. Was this decision tied to a specific team, shift, or manager, rather than the role overall?
6. What would have needed to change in the last 3 months for you to stay?
7. Is there anything you raised before now that, if addressed, would have changed this decision?

CODING (interviewer completes after the conversation, against Table 18.1)
[ ] Burnout-driven exit        [ ] Competitor poaching        [ ] Plateau / no-growth exit
[ ] Shift-burden exit          [ ] Performance-managed-out     [ ] Other: ______________
Named competitor/destination (if poaching):  ______________
Corroborated against a leading indicator (Part 18 SS2.1) or stay-interview data (SS2.3)?
[ ] Yes   [ ] No   [ ] Not checked
```

COMPOSITE CASE EXAMPLE — illustrative coded response, not a real interview:
A mid-tenure L2 analyst's coded answers named a specific competing MSSP and a stated pay gap in Question 2, with no workload or growth complaints in Questions 3–6 — coded as **Competitor poaching**, consistent with Part 18's `CASE-1801` pattern, and routed to a pay-band review rather than a culture-side fix.

**[HR/PEOPLE]** This question set cannot make a departing employee candid who has already decided candor isn't worth the effort on the way out — Part 18 §2.2's Blind Spot applies here directly. Corroborate its coded themes against leading indicators and stay-interview data before treating any single exit interview's coding as a confirmed organizational pattern.

---

## Cross-references

**Within this book:** Companion to Part 15 — Quality Assurance Programs (`TMPL-1501`, `TMPL-1502`), Part 16 — Performance Management & Coaching (`TMPL-1601`), and Part 18 — Attrition & Retention (`TMPL-1801`). See those parts for the sampling methodology, the diagnostic judgment call, and the retention-lever taxonomy each template assumes rather than restates here.

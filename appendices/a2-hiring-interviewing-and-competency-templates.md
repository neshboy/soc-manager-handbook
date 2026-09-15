---
title: "Appendix A2 — Hiring, Interviewing & Competency Templates"
appendix: "A2"
author: "author-agent"
reviewer: "technical-reviewer-agent"
status: "reviewed"
last_validated: "2026-09-15"
depends_on: ["part07", "part08", "part10"]
---

# Appendix A2 — Hiring, Interviewing & Competency Templates

## Why this appendix exists

**[CONCEPT]** This appendix is the fillable companion to three chapters: Part 7 — Hiring & Sourcing Analysts, Part 8 — Interviewing & Technical Assessment Design, and Part 10 — Competency Models & Skills Matrices. Those chapters make the case for why a leveled job description, a calibrated interview loop, and a four-axis competency matrix each beat their informal alternative — tenure-only promotion, an unstructured "just have a conversation" interview, a kitchen-sink requirements list. This appendix does not repeat that argument. It carries the actual artifact each chapter promised: the leveled job-description skeleton (`TMPL-0701`), the structured-interview scorecard and practical-assessment rubrics (`TMPL-0801`), and the tiered competency-matrix worksheet (`TMPL-1001`).

**[HR/PEOPLE]** Use this appendix the way the chapters intend: fill in one skeleton, not three unrelated documents, when a req opens against a tier Part 3 already defines; run the scorecard and rubrics live during an actual interview loop, one per candidate per stage; and revisit the matrix worksheet at nomination for a tier change or roughly annually, never as a stand-in for a monthly performance review. None of the three templates decides the judgment call it sits on top of — a hiring manager still has to draw the must-have/strongly-preferred line, a panel still has to write its own pass-bar language, and a reviewer still has to write the actual anchor text for each tier. Each template below states its specific unautomated judgment call where it applies.

**[SENIOR MANAGER]** Sample values inside any block below are marked CONCEPTUAL SAMPLE — illustrative, not sourced benchmark data or a real requisition — per this book's evidence-classification standard. Substitute your own tier definitions, rubric language, and pass bars before using a template on a real candidate or a real nomination.

## 1. Leveled job-description template (`TMPL-0701`)

**[HR/PEOPLE]** A hiring manager or team lead fills this in once per requisition, against a tier Part 3's model already defines, before a req is posted to any sourcing channel from Part 7. It is one skeleton with a level parameter, not a separate document per tier — the level line changes; the structure underneath it doesn't.

```text
TEMPLATE — Leveled analyst job description skeleton, permanent ID TMPL-0701

ROLE: SOC Analyst — [Tier: L1 / L2 / L3]
SHIFT COMMITMENT: [State the actual pattern from Part 6 — do not write "flexible
  hours" if the role is a fixed night rotation]

SCOPE OF WORK (what this person owns, not what the team owns):
  - <!-- state the specific alert categories, ticket types, or investigation depth
       this level handles unsupervised, not "monitors security events" -->

DECISION AUTHORITY:
  - <!-- what this level can close/escalate/contain without sign-off, and what
       always requires a hand-off -->

MUST HAVE (screens candidates out — keep this list to three items or fewer):
  - <!-- the two or three things a person genuinely cannot do the job without,
       stated as a capability, not a certification: "can read raw firewall logs
       and reconstruct a session," not "CCNA required" -->

STRONGLY PREFERRED (does not screen out; used to break ties):
  - <!-- everything else that would be nice -->

EQUIVALENT-EXPERIENCE CLAUSE:
  - <!-- name the concrete non-traditional background that satisfies a must-have
       item, per Part 7 §6 — "or two years in a role requiring structured
       investigation under time pressure," not a bare "equivalent experience
       considered" -->

GROWTH PATH: What "ready for the next tier" looks like, one sentence, pointing
  to Part 13's ladder rather than restating it.

ON-CALL / ESCALATION EXPECTATION: <!-- the actual frequency, stated as a number
  ("one week in six"), not "occasional on-call support may be required" -->
```

**[HR/PEOPLE]** Filled example (CONCEPTUAL SAMPLE — illustrative values, not a real requisition):

```text
ROLE: SOC Analyst — L2
SHIFT COMMITMENT: Rotating 12-hour day shift, one weekend in three
MUST HAVE:
  - Forms and tests a hypothesis across multiple log sources with no playbook
  - Decides when to escalate vs. close an ambiguous severity call, unsupervised
  - Comfortable building an ad hoc cross-tool query with no saved-search template
EQUIVALENT-EXPERIENCE CLAUSE:
  - Two years of internal audit or compliance investigation work reconstructing
    an anomaly from disparate logs satisfies the first must-have item above
ON-CALL: One week in six, secondary rotation
```

**[HR/PEOPLE]** The template does not decide where the must-have/strongly-preferred line sits for a given tier — that judgment belongs to whoever owns the competency matrix in `TMPL-1001` (§3 below), and a copy filled in without that input just relocates the kitchen-sink problem from "must have" to "strongly preferred" instead of fixing it.

## 2. Structured-interview scorecard and practical-assessment rubrics (`TMPL-0801`)

**[CONCEPT]** Part 8's three-stage loop — screen, practical assessment, panel — needs a scorecard for the panel stage and a dedicated rubric for each of the two practical exercises it describes: the log-triage exercise and the mock-escalation exercise. All three share one design rule from Part 8 §4.1: every line has to name what an interviewer would actually see or hear, not a restated impression. All three also feed the same four axes `TMPL-1001` uses later, so a candidate's assessment record and an analyst's ongoing competency record are scored on the same vocabulary from day one.

### 2.1 Panel scorecard

**[HR/PEOPLE]** One interviewer fills in exactly one copy per candidate per interview, independently, before any debrief conversation starts — the fix Part 8 §2.3 names for debrief-order and recency bias.

```text
TEMPLATE — Structured-interview panel scorecard, permanent ID TMPL-0801 (Part A)

CANDIDATE ID: ____   REQ / TARGET TIER: [L1 / L2 / L3]   STAGE: Panel & behavioral loop
INTERVIEWER: ____   DATE: ____

For each dimension, score 1-5 and state the specific observed behavior that
earned the score — a score with no observed-behavior line is not valid input
to the debrief.

| Dimension          | Score (1-5) | Observed behavior (what was seen/heard) |
|--------------------|-------------|------------------------------------------|
| Technical skill    |             | <!-- e.g., correctly named the missing field without prompting --> |
| Tool proficiency   |             | <!-- e.g., built the cross-tool query within the time budget --> |
| Communication      |             | <!-- e.g., explained the disposition in under two minutes, unprompted --> |
| Judgment           |             | <!-- e.g., named the specific enrichment needed to resolve the ambiguity --> |

OVERALL RECOMMENDATION: [Advance / Hold / Reject]   SUBMITTED BEFORE DEBRIEF: [Y/N]
```

**[HR/PEOPLE]** This scorecard does not set the pass-bar language for a given tier — that comes from the calibration exercise Part 8 §3.3 describes, run before the first real candidate, and belongs in the "observed behavior" column as a written standard the interviewer checks against, not invented fresh per candidate.

### 2.2 Log-triage exercise rubric

**[FRONTLINE MANAGER]** The assessment designer or SOC manager who built the exercise fills in the scenario-specific detail; the interviewer proctoring it fills in the score, per Part 8 §3.1's rule that the reasoning path is scored, not the final disposition label alone.

```text
TEMPLATE — Log-triage exercise rubric, permanent ID TMPL-0801 (Part B)

CANDIDATE ID: ____   TARGET TIER: ____   TIME USED / BUDGET: ____ / ____ min

| Rubric line                                  | Score | Evidence |
|-----------------------------------------------|-------|----------|
| Reached a defensible disposition              |       | <!-- reasoning stated, not just the label --> |
| Correctly identified missing/ambiguous evidence |     | <!-- named the specific gap, not "something's off" --> |
| If "unable to determine": named the exact enrichment needed |  | <!-- specific query/source, not "more info" --> |
| Reasoning reconstructable by a second reviewer |      | <!-- could a reviewer retrace this without the candidate present --> |

PASS BAR FOR THIS TIER (from Part 8 §3.3's calibration table): ____
RESULT: [Clears bar / Does not clear bar]
```

**[FRONTLINE MANAGER]** This rubric does not supply the underlying alert or log excerpt — Part 8 §3.1 requires that material be sanitized real detection content, not an invented puzzle, and sourcing it is a per-SOC task this template assumes is already done.

### 2.3 Mock-escalation exercise rubric

**[FRONTLINE MANAGER]** A team lead or senior analyst playing the receiving Tier 2 role scores this rubric live, against the same standard a real escalation is judged against — SOC Playbook Handbook, Part 27 — Escalation Quality — rather than a hiring-specific standard invented for the exercise.

```text
TEMPLATE — Mock-escalation exercise rubric, permanent ID TMPL-0801 (Part C)

CANDIDATE ID: ____   TIME USED / BUDGET: ____ / 10-15 min

| Rubric line (per SOC Playbook Part 27) | Met? (Y/N) | Note |
|------------------------------------------|-----------|------|
| Context included (what the receiver needs to pick this up cold) |  |  |
| Severity justified, not just asserted    |           |      |
| Concrete next action named               |           |      |

RESULT: [Clears bar / Does not clear bar]
```

**[FRONTLINE MANAGER]** This rubric does not define what a mechanically good hand-off contains — that standard lives in SOC Playbook Part 27, and this exercise borrows it directly so a strong performer here already escalates the way the SOC wants escalations to look on day one.

> **Manager's Note**
> Time-box the mock escalation the same way for every candidate, and don't let how much of the window a candidate used factor into the score — only the rubric content should. It's the same completion-speed bias Part 8 §5.3 names for unpaid take-home exercises, showing up here as "sounded confident and finished in eight minutes" outscoring a candidate who used the full 15 to reason carefully.

## 3. Competency-matrix worksheet (`TMPL-1001`)

**[SENIOR MANAGER]** A team lead or SOC manager fills this in per analyst at nomination for a tier change, and roughly annually otherwise — never on the same monthly cadence as a performance review, per Part 10 §1's hard split between competency and performance. The four axis rows are fixed; the tier-floor and evidence columns are what a reviewer writes in, calibrated against their own tier definitions from Part 3.

```text
TEMPLATE — Tiered competency-matrix worksheet, permanent ID TMPL-1001

ANALYST: ____   CURRENT TIER: ____   TARGET TIER: ____   REVIEW DATE: ____
REVIEWER(S): ____ (calibration requires a second independent reviewer on any
  disputed axis, per Part 10 §6)

| Axis              | Target-tier floor (write the specific observable behavior) | Evidence source | Status |
|-------------------|--------------------------------------------------------------|------------------|--------|
| Technical skill   | <!-- e.g., forms and tests a hypothesis across multiple log sources unaided --> | <!-- QA sample / shadowed session --> | [Met / Not yet met / Not yet tested] |
| Tool proficiency  | <!-- e.g., builds an ad hoc cross-tool query with no documentation --> | <!-- timed practical / ride-along --> | [Met / Not yet met / Not yet tested] |
| Communication     | <!-- e.g., briefs a stakeholder outside the SOC, live, unscripted --> | <!-- QA sample of escalations / observed call --> | [Met / Not yet met / Not yet tested] |
| Judgment          | <!-- e.g., resolves an ambiguous severity call without escalating by default --> | <!-- live ambiguous-ticket walkthrough --> | [Met / Not yet met / Not yet tested] |

GATE CHECK (no averaging — Part 10 §4.1):
  [ ] All four axes independently show "Met." If yes: forward to Part 13's
      promotion process.
  [ ] Any axis "Not yet met": route to a named hold with a specific
      remediation plan and a reassessment date — per axis, not blended.
  [ ] Any axis "Not yet tested": log the evidence gap and assign a way to
      gather it before the next review; do not score it as "Not yet met"
      (Part 10 §8's distinction between an unmeasured skill and an unmet one).
```

**[SENIOR MANAGER]** This worksheet does not write the anchor language itself — the specific behavior that counts as "meets the L2 floor" for technical skill or judgment is a per-SOC calibration exercise, worked through in full with a filled example at the L1-to-L2 boundary in Part 10 §4.2. A copy of this worksheet filled in without that calibration step just moves the "I'd know it if I saw it" problem from an unstructured promotion conversation into a structured-looking document that still means nothing.

## Cross-references

This appendix is the template companion to Part 7 — Hiring & Sourcing Analysts (`TMPL-0701`), Part 8 — Interviewing & Technical Assessment Design (`TMPL-0801`), and Part 10 — Competency Models & Skills Matrices (`TMPL-1001`); it does not restate those chapters' arguments and assumes a reader has already read the relevant part before filling in a template here. The mock-escalation rubric in §2.3 cites SOC Playbook Handbook, Part 27 — Escalation Quality for its scoring standard. See Appendix A3 for what happens to a hire after the offer (onboarding and the career ladder) and Appendix A4 for the QA calibration mechanism this appendix's scorecards and matrix both reuse.

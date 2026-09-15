---
title: "Appendix A3 — Onboarding, Training & Career-Ladder Templates"
appendix: "A3"
author: "author-agent"
reviewer: "technical-reviewer-agent"
status: "reviewed"
last_validated: "2026-09-15"
depends_on: ["part11", "part12", "part13"]
---

# Appendix A3 — Onboarding, Training & Career-Ladder Templates

## Why this appendix exists

**[CONCEPT]** This appendix carries the three fillable artifacts Parts 11 through 13 each promise a reader rather than re-derive inline: a 90-day onboarding plan and gate sign-off tracker, a training-budget and bench-depth worksheet, and a career-ladder and promotion-evidence-packet template. None of the three makes a judgment call for you — they exist to hold the judgment calls those chapters describe in a form a team lead, an HR partner, or a promotion committee can actually fill in, defend, and revisit later.

**[CONCEPT]** Part 11 — Onboarding & Ramp-Up Programs defines the four-phase ramp structure, the gate logic between phases, and the pacing adjustments a lateral hire or career-changer needs; `TMPL-1101` below is the fillable phase/gate document that part's §7 and §10 both point to. Part 12 — Ongoing Training & Skill Development defines what a continuing-education budget actually has to cover and how a bench-depth gap gets tracked to closure; `TMPL-1201` is the worksheet its §1.1 and §5.2 both cite. Part 13 — Career Ladders & Promotion Criteria defines the rungs, the branch bars into detection engineer, threat hunter, or team lead, and the evidence a promotion committee should expect before a name is even discussed; `TMPL-1301` is the fillable version of that ladder and its evidence packet. Read the relevant part before filling in its template — this appendix states what goes in each field, not why the bar is set where it is.

**[CONCEPT]** Every blank field below is intentionally undated and unscored — a manager filling this in for a real analyst enters real dates, real names, and real evidence, and every cell that would otherwise carry an invented number is marked `CONCEPTUAL SAMPLE` or `COMPOSITE CASE EXAMPLE` per the book's evidence-classification standard so a reader never mistakes an illustrative fill-in for a benchmark to copy.

## 1. The 90-day onboarding plan and gate sign-off tracker (`TMPL-1101`)

**[HR/PEOPLE]** The team lead and the new hire open this document on day one and both add to it through day 90; HR references the same document for the parallel probationary-period record rather than keeping a separate, silently drifting copy. It gives a phase/gate structure a specific place to record planned versus actual dates, the exit-criteria evidence a gate actually checked, and who signed off — the fillable counterpart to Part 11's Table 11.1, with the pacing-adjustment note Part 11 §10 requires attached to the same record rather than a separate memo.

```text
TEMPLATE — 90-day onboarding plan and gate sign-off tracker, permanent ID TMPL-1101, home appendix A3

ANALYST: __________________     START DATE: __________     TEAM LEAD: __________
BACKGROUND: [ ] New to SOC work (standard pacing, no Table 11.4 adjustment)
  Or, per Part 11 Table 11.4: [ ] Help-desk/internal transfer
  [ ] Career-changer / apprenticeship pipeline  [ ] Experienced lateral hire  [ ] MSSP transfer
PACING ADJUSTMENT APPLIED: ____________________________________________________
  REASON (one line, citing the Table 11.4 row that applied): ______________________

| Phase                       | Planned dates | Actual dates | Exit criteria met? (evidence) | Gate result                       | Sign-off name / date |
|-----------------------------|---------------|--------------|--------------------------------|------------------------------------|------------------------|
| 1. Shadowing                |               |              | <!-- names the 5 seeded alerts and escalation paths --> | [ ] Advance [ ] Hold [ ] Remediate |                        |
| 2. Supervised triage        |               |              | <!-- 3 consecutive shifts, 0 overturned dispositions --> | [ ] Advance [ ] Hold [ ] Remediate |                        |
| 3. Graduated independence   |               |              | <!-- spot-check pass rate, 2 consecutive weeks --> | [ ] Advance [ ] Hold [ ] Remediate |                        |
| 4. Simulation certification |               |              | <!-- link to the certification report, Part 11 Table 11.3 --> | [ ] Pass [ ] Fail — remediation plan attached |                        |

REMEDIATION LOG (one row per failed gate; a gate can appear more than once):
| Gate failed | Date | Specific gap named | Remediation plan (2-week default) | Retest date | Retest result |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
```

This tracker does not define what counts as a passed gate — that bar comes from Part 10's competency matrix and Part 11's Table 11.1 — and it is not a substitute for Table 11.3's certification report, which stays a separate document a promotion or audit trail can point to on its own.

## 2. The training-budget and bench-depth worksheet (`TMPL-1201`)

**[SENIOR MANAGER]** A SOC manager fills in Part A once during annual budget planning and updates the utilization column monthly, per Part 12's Manager's Note that a training line sitting unspent by October is a scheduling failure, not evidence the team doesn't want training. Part B is a per-request decision log a manager fills in each time a certification funding request arrives, and Part C is the standing cross-training tracker Part 12 §3.2 and §5.2 both assume exists, rebuilt on whatever cadence the manager chooses — quarterly is Part 12's own default.

```text
TEMPLATE — Training-budget and bench-depth worksheet, permanent ID TMPL-1201, home appendix A3

PART A — Per-analyst annual allocation, by category (Part 12 §1.1)
| Analyst | Paid study/lab hours | Certification/exam fees | Internal lab/range access | Content licensing | Conference/other | Total allocated | Spent to date | Utilization |
|---|---|---|---|---|---|---|---|---|
| CONCEPTUAL SAMPLE — J. Alvarez | 32 hrs | $1,600 | $300 | $200 | $0 | $2,100 + 32 hrs | $1,900 + 18 hrs | 90% $ / 56% hrs |

PART B — Certification funding request log (Part 12 §2.1, §2.5)
| Analyst | Certification requested | Exam format (hands-on / multiple-choice) | Cost | Internal role/track this targets | Service commitment attached? | Decision | Decision date |
|---|---|---|---|---|---|---|---|
|   |   |   |   | <!-- if blank, see Part 12 §2.5 before approving spend above ~$1,000 --> |   |   |   |

PART C — Bench-depth gap tracker (Part 12 §3.2, §5.2)
| Specialist function | Analysts unsupervised-capable | Target bench depth | Gap | Closing format | Planned closure date | Actual closure date | Status |
|---|---|---|---|---|---|---|---|
| CONCEPTUAL SAMPLE — SOAR playbook administration | 1 | 2 | 1 | Paired rotation, 60 days | 2026-11-15 | — | In progress |
```

The worksheet tracks allocation, utilization, and gap-closure dates; it does not decide whether a specific certification predicts on-the-job capability — that question belongs to Part 12 §2.2's certification scorecard, applied before Part B's decision column ever gets filled in.

> **Manager's Note**
> Review Part A's utilization column at the same meeting where you review queue-health metrics, not on a separate HR calendar — a training line that's technically "on track" against the annual total but never actually protected against backlog pull-backs (Part 12 §1.2) will still show 90% spent by October with almost none of it converted into a closed bench-depth gap in Part C.

## 3. The career-ladder and promotion-evidence-packet template (`TMPL-1301`)

**[HR/PEOPLE]** An HR partner and the SOC manager fill in Part A once, when the ladder is first published or formally revised — not per candidate, per Part 13 §1's warning against treating the ladder as a title generator. A nominating team lead fills in Part B per candidate, per promotion cycle, and the SOC manager or HR partner runs Part C on the audit cadence Part 13 §5.3 sets.

```text
TEMPLATE — Career ladder and promotion evidence packet, permanent ID TMPL-1301, home appendix A3

PART A — Ladder rung and branch definitions (Part 13 §2–§3; fill in once, revise rarely)
| Rung / branch | Title | Minimum bar (matrix rows, QA score, tenure floor, work sample) | Pay band | Sign-off authority |
|---|---|---|---|---|
| 1 | Analyst I | — | — | — |
| 2 | Analyst II / Senior Analyst | — | — | — |
| 3a | Detection Engineer | <!-- work-sample count from merged detections, Part 13 §3.1 --> | — | — |
| 3b | Threat Hunter | <!-- completed-hunt count and hypothesis-discipline check, §3.2 --> | — | — |
| 3c | Team Lead | <!-- coaching-aptitude assessment + shadow-lead cycle, §3.3 --> | — | — |
| 4 | Principal / Staff Analyst | <!-- the fourth road, §3.4 — do not leave this row blank --> | — | — |

PART B — Promotion evidence packet (Part 13 §4.2; one packet per candidate, per cycle)
| Evidence item | Source | Minimum bar | Met? | Evidence attached / link | Reviewer |
|---|---|---|---|---|---|
| Competency matrix rating | Part 10 matrix | "Meets" on every next-level row | [ ] |   |   |
| QA calibration score | Part 15 QA program | ≥85%, sustained 2 quarters | [ ] |   |   |
| Handle time and independence | Ticket system | Within 15% of median; <20% escalation | [ ] |   |   |
| Open PIP or coaching plan | Part 16 records | None open, trailing 6 months | [ ] |   |   |
| Peer input | Peer-nomination form | ≥2 submissions, no unaddressed concern | [ ] |   |   |
| Branch-specific work sample | PRs / hunt records / shadow-lead log | Meets the §3 branch bar | [ ] |   |   |

PART C — Leveling-audit snapshot (Part 13 §5.3; run on a fixed schedule)
| Level | Target % of headcount | Target headcount | Actual headcount | Gap | Corrective action |
|---|---|---|---|---|---|
|   |   |   |   |   | <!-- correct forward only — never a demotion, per §5.3 -->|
```

Filling in every field does not make a promotion decision for the committee, and it cannot resolve a split vote — that judgment stays with the committee process Part 13 §4 defines. What it produces is the packet a candidate, a peer, or an auditor can be shown a year later as the actual basis for the call.

---

## Cross-references

Companion to Part 11 — Onboarding & Ramp-Up Programs, Part 12 — Ongoing Training & Skill Development, and Part 13 — Career Ladders & Promotion Criteria. Also draws on Part 10 — Competency Models & Skills Matrices (the bar every gate and rung checks against), Part 15 — Quality Assurance Programs and Part 16 — Performance Management & Coaching (the QA score and PIP fields in `TMPL-1301`'s evidence packet), and Part 20 — Building & Defending the SOC Budget (where `TMPL-1201`'s allocation line sits inside the wider budget).

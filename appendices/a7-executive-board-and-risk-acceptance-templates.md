---
title: "Appendix A7 — Executive, Board & Risk-Acceptance Templates"
appendix: "A7"
author: "author-agent"
reviewer: "technical-reviewer-agent"
status: "reviewed"
last_validated: "2026-09-15"
depends_on: []
---

# Appendix A7 — Executive, Board & Risk-Acceptance Templates

## Why this appendix exists

**[EXECUTIVE]** This appendix carries the four fillable artifacts that Part 24 — Executive & Board Reporting, Part 25 — Risk Acceptance & Manager Decision-Making Under Uncertainty, and Part 29 — Post-Incident Organizational Review each build toward but stop short of formatting as a standalone, copyable document: the board deck skeleton (`TMPL-2401`), the risk-acceptance memo (`TMPL-2501`), the post-incident organizational review record (`TMPL-2901`), and its companion corrective-action tracker (`TMPL-2902`). All four are grouped here because they share the same sourcing logic — each one is the durable, dated written record of a judgment call a SOC manager made under some amount of uncertainty, and each one is the artifact a skeptical board member, a future reviewer, or the manager's own successor eventually goes looking for.

**[SENIOR MANAGER]** None of the four templates below teaches the judgment they record. The board deck skeleton assumes the translation recipe built in Part 24 §3 and the metric-selection scorecard in Part 24 §6 have already run; it only formats what those sections produce. The risk-acceptance memo assumes the four-dimension scoring in Part 25's Table 25.1 has already been worked through honestly; it only forces that scoring to be dated and written down before the decision gets made or defaulted into by inaction. The post-incident review record and the corrective-action tracker both assume the blameless-facilitation mechanics in Part 29 §4 and the taxonomy in Part 29's Table 29.2 are already in use; they only give those mechanics somewhere permanent to live. Fill in any of these forms without doing that upstream work first, and the result is a well-formatted document that records a decision nobody actually made carefully.

**[SENIOR MANAGER]** Use this appendix by copying the relevant fenced block, filling every field, and keeping the result somewhere that survives past the meeting that produced it — a shared risk register, a tracked ticket, a versioned document store. A template filled out once and left in a slide deck's speaker notes is functionally the same as not having filled it out at all, which is the exact failure both `CASE-2501` (Part 25) and `CASE-2902` (Part 29) trace back to.

## 1. Board deck template — `TMPL-2401`

**[EXECUTIVE]** The SOC manager or the CISO uses this skeleton to build the quarterly (or per-bylaws) board or audit-committee deck described in Part 24 §5. Start from all five sections every cycle and drop any section with nothing real to report — a slide added only to fill the slot is the same failure mode as a metrics dashboard nobody prunes. This template does not decide which metrics belong in the deck or how to translate a raw number into a risk narrative; that's Part 24 §3's translation recipe and §6's scorecard, applied before a single field below gets filled in.

```markdown
TEMPLATE -- Board deck template (five-section skeleton), permanent ID TMPL-2401

SECTION 1 -- RISK POSTURE SUMMARY (1 slide, 3-5 lines)
<!-- One line per metric that scored 6+ on Part 24 Table (S6)'s selection scorecard. -->
| Metric | This Quarter | Last Quarter | Trend | Risk Translation (one sentence) | What This Should Prompt the Board To Do |
|---|---|---|---|---|---|
|        |               |              |       |                                  |                                          |

SECTION 2 -- INCIDENTS OF NOTE (1 slide per incident; at most 2-3 incidents)
<!-- Source this from the incident's own post-incident organizational review (TMPL-2901), not from memory. -->
| Incident ID | Severity Tier | What Happened (2-3 sentences) | What the Response Demonstrated | Source Review |
|---|---|---|---|---|
|             |               |                                |                                 |               |

SECTION 3 -- TREND METRICS (1 slide)
<!-- Reuse Section 1's row format for any metric tracked but not urgent enough to lead with. -->
| Metric | Trend (4-quarter view) | One-Sentence Mechanism |
|---|---|---|
|        |                        |                        |

SECTION 4 -- RESOURCING / SPEND ASK (only when there's an actual ask -- omit otherwise)
<!-- State the ask as a decision, not a status update: what the board approves, not what's happening. -->
| The Ask (dollars or headcount) | Risk It Reduces | Consequence If Not Funded | Owner |
|---|---|---|---|
|                                 |                  |                            |       |

SECTION 5 -- FORWARD RISK ITEMS (1 slide)
<!-- Pull directly from the open risk-acceptance register (TMPL-2501 entries) -- this is not a new list. -->
| Risk Item | Current Acceptance Level | Expected Escalation/Review Date | Source Memo |
|---|---|---|---|
|           |                          |                                  |             |

SKEPTICAL-QUESTION PREP (not presented; rehearsed beforehand per Part 24 S7)
<!-- Fill this in for every question you can anticipate, not just the comfortable ones. -->
| Anticipated Question | Headline Answer | Evidence Ready | Honest Bound |
|---|---|---|---|
|                       |                  |                |              |
```

> **Manager's Note**
> Fill the skeptical-question-prep table before you finalize a single slide, not after the deck is done. If you can't write a headline, evidence, and an honest bound for the question you're most afraid of getting, the deck itself isn't ready yet, no matter how polished the other five sections look.

## 2. Risk-acceptance memo template — `TMPL-2501`

**[SENIOR MANAGER]** The SOC manager, or whoever the escalation path in Part 25 §2.1 names, fills this out the moment a known, standing risk is first identified — not months into living with it — to force Table 25.1's four-dimension scoring into writing before the risk gets formally accepted, escalated, or defaulted into by nobody stopping the process carrying it. The memo does not calculate the dollar-exposure figure or verify the compensating control on its own; both come from the manager's own analysis, informed by Part 5's and Part 9's models where relevant. What the memo forces is that the reasoning gets dated, written down, and given a calendar date to be checked again — the exact discipline `CASE-2501` shows going missing for six months.

```markdown
TEMPLATE -- Risk-acceptance memo, permanent ID TMPL-2501

Risk ID / short title:
Date identified:
Description of the gap (plain language, not the fix -- state what is actually wrong):

TABLE 25.1 SCORING
<!-- A risk landing in the right-hand column on any single row is a strong candidate for
     escalation even if the other three rows look manager-level. -->
| Dimension | Manager-Level Signal Present? (Y/N + evidence) | Board/CISO-Level Signal Present? (Y/N + evidence) |
|---|---|---|
| Dollar exposure if it materializes |  |  |
| Reversibility |  |  |
| Blast radius (validated, not assumed) |  |  |
| Duration / standing nature |  |  |

Decision: Accepted at [ SOC manager / CISO / Board ] level
Reasoning (written now, not reconstructed later):

Compensating control relied upon, and how/when it was last verified:
<!-- Name the specific control and the date someone last actually re-checked it -- not the date
     it was designed or first approved. -->

Re-check date (mandatory -- re-verifies the fact this acceptance depends on, not just that the
memo still exists on file):

What specific, checkable evidence would change this decision, and by when could it arrive:

Sign-off: Name / Title / Date
```

**COMPOSITE CASE EXAMPLE — illustrative filled memo, based on `CASE-2501` (Part 25 §2.3).** Risk ID: legacy file-cluster coverage gap. Dollar exposure: worst case roughly $1.2 million, above the organization's $250,000 manager-authority threshold — a board/CISO-level signal on that row alone. Reversibility and duration: contained within a named 14-month decommission window — manager-level signal. Blast radius: confirmed bounded by a verified firewall-segmentation rule at the time of signing — manager-level signal. Decision: accepted at the SOC-manager level, reasoning that the verified segmentation boundary made the realistic exposure far below the unmitigated worst case. Re-check date: the field this real case was missing, which is exactly what let a later firewall exception move the control's boundary for two months with nobody watching.

## 3. Post-incident organizational review template — `TMPL-2901`

**[SENIOR MANAGER]** The facilitator named for a given incident — never someone who worked the incident directly, per Part 29 §3.1 — fills this out for the per-incident review, scheduled 5 to 10 business days after the incident closes. The template's fixed field for a role-based timeline exists because a document that circulates outside the review room and still names an individual analyst against a specific action teaches the floor to stop volunteering honest detail, the exact failure `CASE-2901` walks through. This template does not, by itself, make a review blameless — that depends on the facilitation mechanics in Part 29 §4.1 and the psychological-safety precondition Part 19 builds; a form filled out by a room that doesn't feel safe yet is still an incomplete record, however cleanly the fields are completed.

```markdown
TEMPLATE -- Post-incident organizational review, permanent ID TMPL-2901

Incident ID / near-miss flag ID:
Trigger reason: [ mandatory severity tier / discretionary request / random sample / near-miss flag ]
Review date:                          Incident closed on:
Facilitator (must be independent of this incident):
Attendees (by role, e.g. "on-call analyst," "detection engineer," not required to be a fixed roster):

TIMELINE (role-based language only -- "the reviewing analyst," "the on-call engineer," never a
named individual, in any version of this document that leaves the room)
<!-- Ask what made the gap hard to see in time, not who missed it. -->


WHAT HAPPENED (blameless account -- system and process focus)


FINDINGS
<!-- Category taken from Table 29.2; log every finding here even if its fix is trivial -- a
     finding that never reaches the tracker (TMPL-2902) cannot be checked for recurrence later. -->
| Finding (plain-language gap) | Taxonomy Category | Owner | Due Date | Routed To (part/other book) |
|---|---|---|---|---|
|                               |                    |       |          |                             |

Facilitator sign-off:                 SOC manager sign-off:
```

## 4. Corrective-action tracker — `TMPL-2902`

**[SENIOR MANAGER]** This is a standing register, not a per-incident form — every finding logged from every filled `TMPL-2901` lands here, and the standing review board (Part 29 §3.2) queries this register on its own monthly or quarterly cadence, independent of any single incident's timing. The tracker does not run the dedup matching described in Part 29 §6.2 automatically; deciding whether a new finding matches a prior one "in substance, not exact wording" is a human judgment call the standing board makes each cycle, not a keyword search this register performs on its own.

```markdown
TEMPLATE -- Corrective-action tracker, permanent ID TMPL-2902

| Field | Entry |
|---|---|
| Finding ID |  |
| Gap statement (plain language) |  |
| Taxonomy category (Table 29.2) |  |
| Source incident / near-miss ID |  |
| Owner (a named person, not a team) |  |
| Due date |  |
| Verification method (stated in advance -- what evidence proves this is fixed) |  |
| Status: open / owner-reported done / independently verified closed |  |
| Verifier (must not be the owner) |  |
| Prior-match check: new finding / matches Finding ID ___ |  |
| Occurrence count (this exact gap, trailing 18 months) |  |
| Escalation trigger: 3rd-or-later occurrence -> escalate beyond original owner |  |
```

> **People Risk Trap**
> Letting a finding's own owner also mark it verified closed concentrates the same conflict Part 15's QA program names for a reviewer scoring their own report — a busy owner under pressure to show progress calls "a ticket was filed" the same thing as "the fix was verified," which is exactly the pattern `CASE-2902` shows the same access gap surviving three separate times. Route the verifier field to someone other than the owner every time, even when it adds a short delay to closing the item.

---

**Cross-references.** Companion to Part 24 — Executive & Board Reporting (`TMPL-2401`, §5), Part 25 — Risk Acceptance & Manager Decision-Making Under Uncertainty (`TMPL-2501`, §2.4), and Part 29 — Post-Incident Organizational Review (`TMPL-2901` and `TMPL-2902`, §3 and §5). See those parts for the translation recipe, the risk-acceptance scorecard, and the facilitation and taxonomy discipline this appendix's templates format but do not teach. `CASE-2501`, `CASE-2901`, and `CASE-2902` (`CASE-INVENTORY.md`) are the worked examples this appendix's filled sample draws on.

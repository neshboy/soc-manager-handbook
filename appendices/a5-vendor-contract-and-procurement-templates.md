---
title: "Appendix A5 — Vendor, Contract & Procurement Templates"
appendix: "A5"
author: "author-agent"
reviewer: "technical-reviewer-agent"
status: "reviewed"
last_validated: "2026-09-15"
depends_on: ["part21", "part22", "part23"]
---

# Appendix A5 — Vendor, Contract & Procurement Templates

## What this appendix contains

**[CONCEPT]** This appendix is the filing cabinet for the three standing instruments Part 21 — Tooling Procurement & Platform Strategy, Part 22 — MSSP & Managed-Service Contract Management, and Part 23 — Vendor Relationship & Renewal Management each build a piece of, but never fully house inline: a weighted RFP/PoC evaluation scorecard, a library of contract-clause language for the terms that most often go wrong after signing, and a standing vendor risk-scoring worksheet. None of the three is new content invented for this appendix — each is the fillable, standalone version of a template those three chapters already describe and cite by ID, assembled here so a negotiator or a procurement lead can copy the actual worksheet instead of reconstructing it from prose scattered across three chapters.

**[CONCEPT]** The RFP/PoC scorecard (`TMPL-2101`) is Part 21's instrument for scoring SIEM, EDR, SOAR, or TIP finalists on functional fit, total cost of ownership, and exit-cost exposure together, rather than letting a feature bake-off decide the purchase alone. The SLA contract-clause library (`TMPL-2201`) turns the clause-by-clause negotiation guidance in Part 22 — clock-start definitions, coverage-hours minimums, service-credit scaling, right-to-audit scope, and transition-out terms — plus the lock-in mitigation terms Part 21, §4.1 argues belong in the same contract, into draftable contract language a negotiator can hand to legal counsel as a starting point, rather than drafting each clause from a blank page under time pressure. The vendor risk-scoring worksheet (`TMPL-2301`) is Part 23's standing, six-dimension instrument for catching a vendor's financial, ownership, support, or security drift on a fixed cadence, long before it shows up as a bad renewal quote.

**[CONCEPT]** None of the three templates automates the judgment call it exists to support. The scorecard still requires someone to have actually run the proof-of-concept and the off-list reference call Part 21 describes before its rows mean anything; the clause library still requires review by qualified legal counsel before any language is put in front of a vendor, because contract enforceability is jurisdiction-specific in ways this appendix cannot generalize across; and the risk-scoring worksheet still requires a named reviewer willing to write down an honest score and a real reason, not a number chosen to avoid an uncomfortable conversation. Treat every value in this appendix's worked rows marked CONCEPTUAL SAMPLE as illustrative, not sourced benchmark data.

## 1. RFP/PoC weighted evaluation scorecard (`TMPL-2101`)

**[VENDOR/PROCUREMENT]** A SOC manager or the designated procurement lead uses this scorecard once per finalist platform, filled in only after the proof-of-concept and reference calls described in Part 21 — Tooling Procurement & Platform Strategy, §2.3–§2.4 are both complete — never filled in from a vendor's own pitch deck or a gut read of the demo. Score each row against evidence the buying organization gathered itself; a row with no evidence behind it should stay blank rather than get a guessed number.

The legend below defines what each 1–5 score means, since a shared scale across finalists and reviewers is what keeps the total comparable.

| Score | Meaning |
|---|---|
| 1 | Fails to meet the requirement; a disqualifying gap |
| 2 | Meets the requirement only with significant workaround or added cost |
| 3 | Meets the requirement adequately, no notable strength or weakness |
| 4 | Meets the requirement well, with a specific advantage over the alternative(s) |
| 5 | Exceeds the requirement in a way that materially changes the decision |

TEMPLATE — Platform RFP/PoC weighted evaluation scorecard, permanent ID `TMPL-2101`

```text
VENDOR/FINALIST: ______________________   EVALUATOR: ______________________   DATE: __________

CRITERION                                              WEIGHT   SCORE (1-5)   WEIGHTED
Functional fit against the use cases named in the RFP    25%        __            __
  <!-- score only against the use cases the RFP actually named, not the
       vendor's full feature list -->
Data ingest/normalization fit, worst-case log source      15%        __            __
  <!-- score from the PoC's messiest, most poorly-parsed log source,
       never from the vendor demo's cleanest one -->
Integration surface (SOAR, ticketing, IdP, EDR)            10%        __            __
Three-year total cost of ownership (license + migration    25%        __            __
+ retraining)
  <!-- pull this number from a completed TCO worksheet, never the
       vendor's list price alone -->
Exit-cost / lock-in exposure                                15%        __            __
  <!-- pull this number from a completed exit-cost estimate: egress
       fees, content re-migration, and any early-termination penalty -->
Vendor viability & support model                              5%        __            __
Reference-customer signal, including one off-list call        5%        __            __
                                                          ------
                                                 TOTAL      100%                       __
```

**[VENDOR/PROCUREMENT]** This scorecard's default weighting deliberately puts three-year TCO and exit-cost exposure at 40% combined, above functional fit's 25%, because a standard feature bake-off already over-weights functional fit on its own. Adjust the weights for a genuinely different risk profile — a heavily regulated environment might push exit-cost exposure higher still — but do the adjusting before scoring starts, not after a preferred finalist's total comes in low.

## 2. SLA contract-clause library (`TMPL-2201`)

**[VENDOR/PROCUREMENT]** A contract negotiator preparing for or reviewing an MSSP, MDR, or managed-service statement of work uses this library as starting language for six clause families: the five Part 22 — MSSP & Managed-Service Contract Management identifies as the ones most likely to be either missing or too vague to enforce — the SLA clock-start definition, the coverage-hours staffing minimum, service-credit scaling, right-to-audit scope, and the transition-out clause — plus the lock-in mitigation set Part 21 — Tooling Procurement & Platform Strategy, §4.1 argues is cheapest to negotiate into the same contract before signing rather than left for a separate conversation later. Each block below is drafted to be filled in with the buying organization's own negotiated numbers, then handed to qualified legal counsel for jurisdiction-specific review — none of this language is a substitute for that review, and none of it should go to a vendor unreviewed.

TEMPLATE — SLA contract-clause library, permanent ID `TMPL-2201`

```text
CLAUSE 1 — NOTIFICATION CLOCK-START DEFINITION (Part 22 §1.2)
Vendor shall notify Client of any Critical-severity security event within [__]
minutes of the Event Timestamp. "Event Timestamp" means the earlier of: (a) the
timestamp recorded by Vendor's detection platform at first alert generation, or
(b) the timestamp of the underlying log event that triggered the alert, as
recorded in a system Client can independently verify. Vendor shall additionally
report, on a monthly basis and regardless of whether the primary SLA in this
Section was met, the secondary metric "Total Elapsed Time from Alert Generation
to Client Notification" for all Critical-severity events during the reporting
period.
  <!-- if Vendor will not agree to (b), the secondary metric is the fallback
       Part 22 §1.2 recommends -- it carries no remedy but keeps the gap visible -->

CLAUSE 2 — COVERAGE-HOURS STAFFING MINIMUM (Part 22 §1.3)
Vendor shall maintain no fewer than [__] dedicated, named security-operations
analysts staffed continuously on every shift, 24 hours per day, 7 days per
week, covering no more than [__] client accounts per analyst per shift. Client
may verify this commitment under the right-to-audit provisions of Section [__]
without advance notice exceeding [__] hours.
  <!-- "24/7 monitored" alone commits to nothing; name the analyst count and
       the per-analyst account load explicitly -->

CLAUSE 3 — SERVICE-CREDIT SCHEDULE, SCALED BY SEVERITY (Part 22 §1.4)
  Severity tier scored under Section [__]   |  Credit per missed instance  |  Cap per billing period
  Critical                                   |  [__]% of monthly fee        |  [__]% of monthly fee
  High                                        |  [__]% of monthly fee        |  [__]% of monthly fee
  Medium                                      |  [__]% of monthly fee        |  [__]% of monthly fee
  A missed Critical-severity SLA occurring during a Client-confirmed security
  incident shall be escalated for a documented root-cause review within [__]
  business days, independent of whether a credit was issued.
  <!-- a flat, low percentage cap regardless of severity is the trap Part 22
       §1.4 names -- scale the cap, don't just scale the credit -->

CLAUSE 4 — RIGHT-TO-AUDIT (Part 22 §2.1–§2.2)
Client shall have the right to conduct, no more than [__] time(s) per contract
year without cause, a [ ] documentation and access review  [ ] technical
control assessment  [ ] on-site assessment of Vendor's security controls
relevant to the delivery of the Services, upon no fewer than [__] and no more
than [__] days' written notice. [Vendor / Client / the parties in proportion
to scope] shall bear the cost of any such review. Vendor shall remediate any
confirmed finding within [__] days of written notice, with escalation to
[named contact/role] if the deadline is missed. This right extends to any
subcontractor, offshore delivery tier, or fourth-party platform Vendor
utilizes to deliver any portion of the Services, and Vendor shall disclose
the existence and role of any such subcontractor upon request.
  <!-- the subcontractor/fourth-party sentence is the clause most often left
       out entirely -- see Part 22 §2.2's fourth-party blind spot -->

CLAUSE 5 — TRANSITION-OUT / OFFBOARDING (Part 22 §3.2)
Upon termination or expiration of this Agreement, Vendor shall: (a) return all
Client historical alert, case, and log data in [named portable format, e.g.
CEF/JSON export] within [__] days of the termination date; (b) retain a copy
of such data for [__] days post-termination for reconciliation purposes only,
accessible to Client on request, and provide written certification of
deletion upon expiration of that period; (c) provide a documented,
human-readable statement of the logic and tuning rationale behind every
custom detection rule, playbook, or enrichment routine built for Client's
environment during the term, not solely the underlying rule syntax; (d) make
personnel reasonably available to Client and Client's incoming vendor or
internal team for a Transition-Assistance Period of [__] days following
termination; and (e) charge no fee for the activities in (a)–(d) beyond
[capped amount / rate], regardless of the reason for termination.
  <!-- item (e)'s cap is the highest-priority, cheapest-to-negotiate line in
       this entire library per Part 22 §5's negotiation-priority table --
       push for it even when nothing else in this clause moves -->

CLAUSE 6 — LOCK-IN MITIGATION SET (Part 21 §4.1)
(a) Export format: Vendor shall provide, on request and at no additional
    charge, an export of all Client-authored detection/correlation logic in
    [a documented, non-proprietary format] sufficient to permit re-authoring
    on an alternative platform.
(b) Egress allowance: Vendor shall include [__] TB per year of historical-data
    bulk export within the base subscription fee, with any excess billed at a
    disclosed, capped rate of no more than $[__] per additional TB.
(c) Price-increase ceiling: Any renewal price increase shall not exceed [__]%
    year-over-year absent a material, individually itemized change in scope.
```

**[VENDOR/PROCUREMENT]** This library gives a negotiator draftable starting language for the clause families that are cheapest to negotiate before signing and most expensive to renegotiate after; it does not tell a negotiator which of the six clauses to prioritize when a vendor is only willing to concede on some of them. Part 22, §5's negotiation-priority table answers that ordering question — use it alongside this library, not instead of it.

## 3. Vendor risk-scoring template (`TMPL-2301`)

**[VENDOR/PROCUREMENT]** A vendor-governance owner uses this worksheet on a fixed cadence — quarterly for a Tier 1 vendor, at minimum annually for everyone else, per the contract-tier calendar in Part 23 — Vendor Relationship & Renewal Management, §2.1 — to catch drift in a vendor's financial health, ownership, support quality, roadmap, security posture, or concentration risk before that drift shows up as a bad renewal quote or a support failure during a live incident. File a completed copy alongside the renewal-calendar entry for the same vendor each cycle, so the trend line across quarters, not just the current score, is visible at the next review.

TEMPLATE — Standing vendor risk scorecard, permanent ID `TMPL-2301`

```text
VENDOR: __________________     REVIEW PERIOD: Q___ 20___     REVIEWER: __________

| Dimension               | Score (1-5) | Evidence / reason for this score          | Change vs. last review |
|--------------------------|-------------|---------------------------------------------|---------------------------|
| Financial stability      |    __       | <!-- cite the specific signal, not a gut feel --> |                     |
| Ownership / M&A exposure |    __       |                                               |                           |
| Support quality trend    |    __       | <!-- compare to a specific prior-period number, e.g. median response time --> | |
| Product / roadmap health |    __       |                                               |                           |
| Security posture         |    __       |                                               |                           |
| Concentration risk       |    __       | <!-- name the specific functions that depend on this vendor with no fallback --> | |

OVERALL FLAG: [ ] Green (no action)   [ ] Yellow (monitor, revisit next cycle)
              [ ] Red (any single dimension at 4-5, or 2+ dimensions worsened
                  since last review -- build a contingency plan before the
                  next renewal date, regardless of how far out it is)
```

CONCEPTUAL SAMPLE — illustrative scoring, not sourced benchmark data.

```text
VENDOR: [EDR platform, Tier 1]          REVIEW PERIOD: Q3 2026     REVIEWER: [name/role]

| Dimension               | Score | Evidence / reason for this score                         | Change |
|--------------------------|-------|-------------------------------------------------------------|--------|
| Financial stability      |  2    | No distress signals; steady renewal pricing                 |  same  |
| Ownership / M&A exposure |  4    | Acquired by PE-backed consolidator 14 months ago; no        |  +2    |
|                          |       | integration roadmap published yet                            |        |
| Support quality trend    |  4    | Median ticket response rose from ~4 business hours to ~3     |  +2    |
|                          |       | business days over two quarters; named TAM left, unreplaced   |        |
| Product / roadmap health |  3    | No material feature release addressing our use case in 10 months |  +1   |
| Security posture         |  1    | SOC 2 Type II current; no disclosed incidents                |  same  |
| Concentration risk       |  3    | Sole source for endpoint detection; no fallback tooling staged|  same  |

OVERALL FLAG: [ ] Green   [ ] Yellow   [X] Red
Note: two dimensions (ownership/M&A exposure, support quality trend) are
already at 4, and three dimensions have worsened since the last review --
this trips Red under both criteria. Build the contingency plan now rather
than waiting for the next quarterly cycle.
```

**[VENDOR/PROCUREMENT]** This worksheet catches gradual, visible drift reasonably well; it does not catch a sudden, non-public event between review cycles — an acquisition announced the week after a review just ran, a breach disclosed on a delay. Pair the fixed cadence with a standing habit of watching public M&A and security-disclosure news for every Tier 1 vendor between formal reviews, per Part 23, §3.3's Blind Spot.

---

## Cross-references

This appendix is the companion filing for Part 21 — Tooling Procurement & Platform Strategy (`TMPL-2101`, §2.2), Part 22 — MSSP & Managed-Service Contract Management (`TMPL-2201`, §1–§3, §5), and Part 23 — Vendor Relationship & Renewal Management (`TMPL-2301`, §3.2). It also assumes the TCO and exit-cost worksheets described in Part 21, §3–§4 as direct inputs to `TMPL-2101`'s two highest-weighted rows, and the negotiation-priority ordering in Part 22, §5 as the sequencing guide for `TMPL-2201`. See Appendix A6 — Budget & Business-Case Templates for the TCO calculator itself, and Appendix A8 — Cross-Series Quick Reference for where MSSP severity terminology diverges from the internal severity model owned by SOC Playbook Handbook, Part 29 — Playbook Severity Model.

---
title: "Appendix A6 — Budget & Business-Case Templates"
appendix: "A6"
author: "author-agent"
reviewer: "technical-reviewer-agent"
status: "reviewed"
last_validated: "2026-09-15"
depends_on: ["part02", "part20"]
---

# Appendix A6 — Budget & Business-Case Templates

## Why this appendix exists

**[CONCEPT]** This appendix holds the three fillable artifacts Part 2 — SOC Operating Models and Part 20 — Building & Defending the SOC Budget both build toward but deliberately don't reprint in full: a budget worksheet organized by Part 20 §1's five categories (`TMPL-2001`), the weighted build-vs-buy-vs-outsource decision matrix Part 20 §6 walks through inline for one composite organization (`TMPL-2002`), and a three-year total-cost-of-ownership calculator that extends a single year's budget into the multi-year comparison Part 20 §5 argues is the minimum defensible horizon (`TMPL-2003`). Every field in every template below matches a section those two parts already justify — this appendix doesn't introduce new budget logic, it makes the logic fillable.

Part 2 makes the build/buy/blend operating-model decision on cost, control, retention, telemetry sensitivity, and coverage-hours economics; Part 20 turns that decision into dollars a CFO can hold onto and a business case that survives more than a Year 1 comparison. Both chapters use one composite 4,000-endpoint organization as a running worked example, and this appendix reuses the same organization's numbers throughout so a reader can trace a figure from a chapter straight into the worksheet that produced it, rather than reconciling two unrelated sets of illustrative numbers.

None of the three templates automates the judgment calls Part 2 and Part 20 both flag as unresolved by dollars alone — how much a weight in the decision matrix should favor control over cost, whether a rising cost-per-alert is a real efficiency gain or a quality problem in disguise, whether a model's detection coverage holds up once the cost comparison is settled. Fill these out as the documented starting point for that conversation, not as a substitute for having it.

## 1. Budget worksheet by category

**[SENIOR MANAGER]** A SOC manager or budget owner fills this out when building the annual budget request, or on the quarterly refresh cadence Part 20 §8 recommends, using the five-category structure Part 20 §1 defines: headcount, tooling, training, facilities, and vendor services. Complete the Basis/Driver column for every line — a category with no stated driver is exactly the "single number, no explanation" budget Part 20 §1 says doesn't survive a finance reviewer's first question.

```text
TEMPLATE — Budget worksheet by category, permanent ID TMPL-2001, home appendix A6

| Category | Line Item | Basis / Driver | Prior-Year Actual | Current-Year Budget | Variance ($) | Variance (%) | Notes |
|---|---|---|---|---|---|---|---|
| Headcount | Tier 1/2/3 analysts (loaded cost x headcount) | Coverage-hours target, Part 5 headcount model | — | — | — | — | <!-- state the shrinkage assumption feeding this year's headcount number, not "based on last year" --> |
| Headcount | Team leads | Span-of-control ratio, Part 13 | — | — | — | — | |
| Headcount | SOC manager allocation | Org chart, Part 4 | — | — | — | — | |
| Tooling | SIEM licensing | Data volume / seat count | — | — | — | — | <!-- note pricing structure: per-endpoint, per-GB-ingested, or per-user, per Part 2 Sec. 2.1 --> |
| Tooling | EDR licensing | Endpoint count | — | — | — | — | |
| Tooling | SOAR / TIP licensing | Feature-tier, seat count | — | — | — | — | |
| Training | Certifications | Headcount growth, skill-gap plan (Part 12) | — | — | — | — | |
| Training | Conferences | Headcount x per-head allowance | — | — | — | — | |
| Training | Internal knowledge-sharing time | Opportunity cost, no line-item price (Part 12) | — | — | — | — | <!-- state the estimation method used, not "n/a" --> |
| Facilities | Secure floor / badge access | On-site headcount | — | — | — | — | |
| Facilities | Redundant power / network circuits | Coverage-hours model | — | — | — | — | |
| Facilities | Remote-work provisioning (stipends, hardened endpoints) | Remote/on-site mix | — | — | — | — | |
| Vendor services | MSSP / MDR contract | Operating-model choice, Part 2 | — | — | — | — | <!-- name the pricing structure and renewal date --> |
| Vendor services | Standing IR retainer | Part 28 activation policy | — | — | — | — | |
| Vendor services | Threat-intel feed subscriptions | Coverage scope | — | — | — | — | |
| Vendor services | Pentest / red-team engagements | Annual test cadence | — | — | — | — | |
| TOTAL | | | — | — | — | — | |
```

The worked block below shows the worksheet filled in for the fully in-house model Part 20 §2 prices for its composite 4,000-endpoint organization, so the shape of a completed row is visible before a reader fills in their own numbers.

```text
CONCEPTUAL SAMPLE -- extends Part 20 Sec. 2's composite fully-in-house organization,
not sourced benchmark data.

Headcount   | 11 Tier 1/2/3 analysts x $95,000       | Coverage-hours target | $1,045,000
Headcount   | 2 team leads x $130,000                | Span-of-control ratio |   $260,000
Headcount   | 1 SOC manager                          | Org chart             |   $160,000
Tooling     | SIEM + EDR + SOAR licensing             | Data volume/seat count|   $450,000
Training    | $3,000/analyst x 11, $2,500/lead x 3    | Headcount growth      |    $40,500
Facilities  | Secure floor, redundant network, badge  | Coverage-hours model  |    $60,000
Vendor svcs | Threat-intel feed + standing IR retainer| Part 28 policy         |    $90,000
                                                                        Total = $2,105,500/year
```

This worksheet totals dollars correctly, but it doesn't decide which category *should* be growing this year — that diagnostic call belongs to Part 20 §1, and a worksheet with every Basis/Driver cell filled in with "same as last year" produces a number a finance reviewer can add up but not defend.

## 2. Build-vs-buy-vs-outsource decision matrix

**[SENIOR MANAGER]** Fill this out when defending or reconsidering Part 2's operating-model decision, after completing a `TMPL-2001` worksheet for each candidate model and the TCO calculator (`TMPL-2003`, §3 below) — Part 20 §6 walks through the identical matrix inline, scored for one composite organization, and this is the reusable blank version of that same instrument. Score each model 1 through 5 (5 is best) per dimension, then multiply by the dimension's weight and sum for a weighted total.

```text
TEMPLATE — Build-vs-buy-vs-outsource decision matrix, permanent ID TMPL-2002, home appendix A6

| Dimension | Weight (%) | Fully In-House (1-5) | Fully Outsourced (1-5) | Hybrid + Embedded DE (1-5) | Co-Managed (1-5) |
|---|---|---|---|---|---|
| 3-year TCO (lower cost scores higher) | — | — | — | — | — |
| Cost-per-alert trend (Part 20 §4/§5.2) | — | — | — | — | — |
| Tuning-authority latency / control (Part 2 §3) | — | — | — | — | — |
| Telemetry-sensitivity fit (Part 2 §4) | — | — | — | — | — |
| Retention lever for senior talent (Part 2 §5) | — | — | — | — | — |
| Coverage-hours cost efficiency, thin shifts (Part 2 §6) | — | — | — | — | — |
| WEIGHTED TOTAL (weight x score, summed) | 100% | — | — | — | — |

<!-- state why each weight was set where it was -- "cost-constrained, low telemetry sensitivity,
     no near-term retention crisis" -- not just the number, per Part 20 Sec. 7's Operational
     Reality on documenting weighting rationale -->
```

The block below is Part 20 §6's own worked scoring, reproduced here as the filled-in reference case rather than re-derived:

```text
CONCEPTUAL SAMPLE -- illustrative weights and scores for the composite organization
used throughout Part 2 and Part 20, not a universal scoring or weighting key.

Weights: TCO 30%, cost-per-alert 15%, control 15%, sensitivity fit 15%,
         retention 15%, coverage-hours efficiency 10%

Dimension                          In-House  Outsourced  Hybrid  Co-Managed
3-year TCO                             1          5          4        2
Cost-per-alert trend                   1          5          4        2
Tuning-authority latency/control       5          2          4        3
Telemetry-sensitivity fit              5          1          3        4
Retention lever                        4          1          4        4
Coverage-hours efficiency              1          5          4        4
                         Weighted total: 2.65       3.35       3.85     2.95
```

A weighted total is only as honest as the weights behind it, and the matrix has no way to check whether the winning model's actual detection coverage holds up — Part 20 §5.3's Cross-Book Pointer sends that specific check to Detection Engineering Handbook V2, Parts 41–43 before treating a weighted win as the final answer.

## 3. Three-year TCO calculator

**[SENIOR MANAGER]** Use this once each candidate model has a completed `TMPL-2001` worksheet, to extend a single year's steady-state budget into the multi-year comparison Part 20 §5.2 argues every build-vs-buy case needs — a Year 1 comparison alone hides the one-time hiring or vendor-onboarding cost every model carries and, per Part 20 §5.2's Management Autopsy, can make the wrong model look cheapest.

```text
TEMPLATE — Three-year TCO calculator, permanent ID TMPL-2003, home appendix A6

| Model | Year 1 Steady-State Budget (TMPL-2001 total) | One-Time Ramp/Transition Cost | Year 2 Budget | Year 3 Budget | 3-Year TCO | 3-Yr Alerts Triaged | Blended Cost-per-Alert |
|---|---|---|---|---|---|---|---|
| Fully in-house | — | — | — | — | — | — | — |
| Fully outsourced | — | — | — | — | — | — | — |
| Hybrid + embedded DE | — | — | — | — | — | — | — |
| Co-managed | — | — | — | — | — | — | — |

<!-- Year 2/3 budgets default to the Year 1 steady-state figure carried flat unless a known
     driver change (renewal, headcount growth, a new data source) is documented in a footnote -->
```

The worked block below reproduces Part 20 §5.2's own four-model comparison, so the calculator's output is checkable against the chapter that specifies it:

```text
CONCEPTUAL SAMPLE -- extends Part 20 Sec. 5.2's composite organization,
not sourced benchmark data. Assumes flat alert volume across 3 years
(219,000 alerts/year, 657,000 over the window) -- a simplifying
assumption, not a forecast; see Part 20 Sec. 4's What Would Change My
Mind before trusting a flat-volume 3-year projection for your own SOC.

Model                Y1 Budget    Ramp Cost   3-Yr TCO      Blended $/Alert
Fully in-house       $2,105,500   $342,000    $6,658,500    $10.13
Fully outsourced     $1,157,000    $65,000    $3,536,000     $5.38
Hybrid + embedded DE $1,229,000    $62,000    $3,749,000     $5.71
Co-managed           $1,738,000    $88,000    $5,302,000     $8.07
```

This calculator assumes Year 2 and Year 3 hold the Year 1 driver assumptions flat unless a footnote says otherwise, and it says nothing about detection quality — pair its output with the decision matrix in §2 above rather than treating the cheapest 3-year number as the recommendation on its own, per Part 20 §5.3.

---

**Cross-references:** Companion to Part 2 — SOC Operating Models: In-House, MSSP, Co-Managed, Hybrid (the operating-model decision `TMPL-2002` scores) and Part 20 — Building & Defending the SOC Budget (the five-category structure behind `TMPL-2001`, the TCO methodology behind `TMPL-2003`, and the cost-per-analyst/cost-per-alert framings both templates report against). See Part 20 §5.3 and Detection Engineering Handbook V2, Parts 41–43, for the detection-coverage/quality check none of these three templates performs.

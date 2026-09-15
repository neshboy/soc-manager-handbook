---
title: "Appendix A1 — Staffing, Shift-Design & Capacity-Model Templates"
appendix: "A1"
author: "author-agent"
reviewer: "technical-reviewer-agent"
status: "reviewed"
last_validated: "2026-09-15"
depends_on: ["part05", "part06"]
---

# Appendix A1 — Staffing, Shift-Design & Capacity-Model Templates

## Why this appendix exists

**[CONCEPT]** This appendix holds the fillable worksheets that Part 5 — Headcount & Capacity Modeling and Part 6 — Shift Pattern & Coverage Design build formulas for but don't reproduce as blank, reusable artifacts. Both parts cite these templates by permanent ID rather than re-deriving their arithmetic — this is the file those citations resolve to. Four templates are collected here: the headcount calculator worksheet (`TMPL-0001`), the shift-pattern templates covering fixed, rotating, follow-the-sun, and on-call/bridge coverage (`TMPL-0601`), the shift-handoff content checklist (`TMPL-0602`), and the on-call rotation calculator (`TMPL-0603`).

Each template is a companion to a specific section of Part 5 or Part 6, and each assumes the reader has already read the reasoning behind it — this appendix does not re-argue why shrinkage matters, why a flat daily average misstates concurrency, or why rotation direction affects error rate. It only gives the reader something to fill in. Where a worksheet needs an example value to show the arithmetic working, that value is drawn from Part 5's `CASE-0501` (a composite, illustrative regional-bank SOC) or is marked as a conceptual sample — neither is a benchmark to target, only a demonstration of the math.

Treat every template below as a working document, not a form filled in once and filed away. Part 5 §8 makes this point explicitly for the headcount worksheet — a model built once at budget time and never re-run is already stale by the next quarter — and the same discipline applies to the shift-pattern and on-call templates: a rotation calendar built for a 12-person team doesn't survive three new hires and one resignation without being rebuilt, not just relabeled.

## 1. Headcount calculator worksheet (`TMPL-0001`)

**[SENIOR MANAGER]** A SOC manager building or defending a headcount number at budget time, or re-running the model on Part 5 §8's quarterly cadence, uses this worksheet. It walks the same seven steps Part 5 §3–§7 develops in prose: a coverage-hours floor, volume and handle time segmented by time block, a shrinkage stack, and a stress-test check against a high-percentile day — fill it in top to bottom with your own data.

```text
TEMPLATE — Headcount Calculator Worksheet, permanent ID TMPL-0001

STEP 1 — Coverage-hours floor (Part 5 §3.3)
| Coverage target                     | Weekly hours covered | Coverage-floor seats |
|--------------------------------------|-----------------------|-----------------------|
| Business hours only (5x10)          | 50                    | 1                     |
| Extended hours (2 shifts x 8 hrs)   | 80                    | 2                     |
| 24/7, single-seat minimum           | 168                   | 3 (1 per shift)       |
| 24/7, two-person overnight minimum  | 168                   | varies — see Part 5 §7.1 |
| Follow-the-sun (regional handoff)   | 168                   | varies by region      |
Your coverage target: ______________________   Coverage-floor seats: ______

STEP 2 — Volume & handle time by time block (Part 5 §3.1–§3.2; split at minimum by business/overnight)
| Time block  | Hrs/day in block | Days/yr | Alert vol./block (post-automation) | Avg handle time (min) | Raw analyst-min (vol x time) | Raw analyst-hrs | Concurrent analysts (raw = hrs / block hrs) | Concurrent analysts (round up) |
|-------------|-------------------|---------|--------------------------------------|-------------------------|-------------------------------|-------------------|-----------------------------------------------|----------------------------------|
| ___________ | ___               | ___     | ___                                  | ___                      | ___                            | ___                | ___                                             | ___                              |
| ___________ | ___               | ___     | ___                                  | ___                      | ___                            | ___                | ___                                             | ___                              |
Example (CASE-0501, COMPOSITE CASE EXAMPLE): Business hours — 12 hrs, 365 days, 420 tickets, 15 min, 6,300 min, 105.0 hrs, 8.75, 9. Overnight — 12 hrs, 365 days, 180 tickets, 15 min, 2,700 min, 45.0 hrs, 3.75, 4.

STEP 3 — Seat-hours per year
Seat-hrs/yr = SUM over every time block of (Concurrent analysts, rounded up) x (Hrs/day) x (Days/yr)
Your total: ______________
Example: (9 x 12 x 365) + (4 x 12 x 365) = 39,420 + 17,520 = 56,940 seat-hrs/yr

STEP 4 — Shrinkage stack (Part 5 §4.1)
| Category                              | Hours/yr | % of 2,080 nominal |
|-----------------------------------------|----------|----------------------|
| PTO & vacation                          | ___      | ___                  |
| Sick leave                              | ___      | ___                  |
| Company holidays                        | ___      | ___                  |
| Training & certification                | ___      | ___                  |
| Coaching, 1:1s, QA calibration          | ___      | ___                  |
| Team meetings & admin overhead          | ___      | ___                  |
| Paid breaks & shift-change overlap      | ___      | ___                  |
| Fleet-wide new-hire ramp deduction       | ___      | ___                  |
| Total shrinkage                         | ___      | ___                  |
Reference point only, not a target: Part 5 §4.1 works a ~32% stack from these same eight categories.

STEP 5 — Productive hours per FTE
Productive hrs/FTE = 2,080 x (1 - Total shrinkage %)
Your value: ______________   Example at 32%: 2,080 x 0.68 = 1,414.4

STEP 6 — Draft headcount
Headcount = Seat-hrs/yr (Step 3) / Productive hrs/FTE (Step 5), rounded up
Your value: ______________   Example: 56,940 / 1,414 = 40.28 -> 41 FTE

STEP 7 — Stress-test check before this number ships (Part 5 §7)
[ ] Re-run Step 2's binding time block at its P90 daily volume, not the mean — does concurrency change?
[ ] Does any resulting shift staff at exactly 1 analyst (queue-of-one, Part 5 §7.1)? If yes, name the backup path here: ______________
[ ] Is a surge/overflow lever documented for a spike beyond P90 (MSSP overflow — Part 22; pre-approved overtime; cross-trained pool)? ______________
[ ] Re-run date scheduled (quarterly default, Part 5 §8): ______________
```

**[SENIOR MANAGER]** This worksheet automates the arithmetic; it does not automate the two judgment calls Part 5 §7 flags as the model's real limits — what percentile of volume to size standing concurrency against, and whether an organization is willing to accept a queue-of-one shift's zero reserve capacity rather than fund a second seat. Both are risk-tolerance decisions a spreadsheet can't make for the manager signing off on it.

## 2. Shift-pattern templates (`TMPL-0601`)

**[FRONTLINE MANAGER]** A team lead or SOC manager building the actual calendar that delivers Step 6's headcount number uses these four fillable calendars, one per coverage model from Part 6 Table 6.1. Pick the model Part 6 §8's decision framework points to before filling in the corresponding table — these aren't four options to blend, they're four different answers to the same coverage question.

```text
TEMPLATE — Fixed Shift Calendar, permanent ID TMPL-0601 (Part A: fixed, Part 6 §2)

| Crew    | Shift block | Local start–end | Days-on / days-off pattern | Night differential? |
|---------|-------------|-------------------|-------------------------------|------------------------|
| Crew A  | Day         | 07:00–15:00       | 5 on / 2 off                  | No                     |
| Crew B  | Evening     | 15:00–23:00       | 5 on / 2 off                  | Partial                |
| Crew C  | Night       | 23:00–07:00       | 5 on / 2 off                  | Yes                    |
CONCEPTUAL SAMPLE — illustrative start/end times; set to your own shift boundaries and Step 1's coverage-floor seat count per crew.
For a two-shift 12-hour model instead (Part 6 §2.2), replace the three rows above with Day (07:00–19:00) and Night (19:00–07:00), each crew on a 2-2-3 pattern across a 14-day cycle.
```

```text
TEMPLATE — Rotating Shift Ladder, permanent ID TMPL-0601 (Part B: rotating, Part 6 §3)

One crew's path through a slow, forward rotation (day -> evening -> night, per Part 6 §3.2's direction guidance),
with a rest-day buffer inserted at each direction change:

| Rotation step | Shift block | Length (days) | Buffer before next block |
|----------------|-------------|-----------------|------------------------------|
| 1              | Day         | 5               | —                            |
| 2              | Evening     | 5               | 1 rest day (forward: D->E)   |
| 3              | Night       | 5               | 1 rest day (forward: E->N)   |
| 4              | Off / rest  | 4               | returns to step 1            |
CONCEPTUAL SAMPLE — offset each additional crew's start point by one step to keep every shift covered every day; do not compress the buffer to save calendar days (Part 6's `CASE-0601` shows what removing it costs in QA-scored error rate).
```

```text
TEMPLATE — Follow-the-Sun Coverage Map, permanent ID TMPL-0601 (Part C: follow-the-sun, Part 6 §4)

| Region   | Local business hours | Coverage window (UTC) | Handoff to next region (UTC) | Analysts on shift |
|----------|-------------------------|--------------------------|----------------------------------|-----------------------|
| Americas | 08:00–17:00 local       | ___–___                  | ___                              | ___                   |
| EMEA     | 08:00–17:00 local       | ___–___                  | ___                              | ___                   |
| APAC     | 08:00–17:00 local       | ___–___                  | ___                              | ___                   |
CONCEPTUAL SAMPLE — the 08:00–17:00 local business-hours window is an illustrative placeholder for all three regions; set each region's actual local business hours before deriving its UTC coverage window and handoff time.
Set analysts-on-shift to at least the coverage-floor seats from Step 1 per region; price the regional-overhead line (management, duplicated tooling, cross-region calibration) per Part 6's `CASE-0602` before comparing total cost to a single-site model.
```

```text
TEMPLATE — On-Call / Bridge Coverage Calendar, permanent ID TMPL-0601 (Part D: on-call, Part 6 §5)

| Week starting | Primary on-call | Secondary on-call | Bridge escalation contact(s) |
|-----------------|--------------------|------------------------|----------------------------------|
| ___             | ___                | ___                    | ___                              |
See `TMPL-0603` for sizing how many analysts need to be in this rotation and how often each one carries it.
```

**[FRONTLINE MANAGER]** None of these four calendars decides which model to run — that choice is Part 6 §8's decision framework, applied before this template is opened. What this template doesn't automate is the exception handling a real calendar always needs: a named backup when a crew member on a fixed or rotating schedule is out, and a documented rule for who absorbs a shift nobody volunteers for during a holiday window (Part 6 §6).

## 3. Shift-handoff content checklist (`TMPL-0602`)

**[FRONTLINE MANAGER]** The outgoing analyst on any shift fills this in during the shift's final 30 minutes, before the incoming analyst arrives — not narrated from memory during the overlap itself. The incoming analyst reads it, asks clarifying questions during the overlap window, and signs the acknowledgment field before the outgoing analyst is released. This is a shift-level transfer, distinct from the per-ticket escalation quality owned by SOC Playbook Handbook, Part 27 — Escalation Quality; if an item below needs its own ticket-level escalation, route it there instead of trying to close it out inside this checklist.

```text
TEMPLATE — Shift-Handoff Content Checklist, permanent ID TMPL-0602

Shift date: ____________  Outgoing analyst: ____________  Incoming analyst: ____________
Outgoing shift block: ____________  Handoff record completed at (time): ____________
Incoming acknowledgment (initials + time): ____________

| Category                     | What to record                                                                 | Detail | Confirmed read by incoming analyst? |
|-------------------------------|----------------------------------------------------------------------------------|--------|----------------------------------------|
| Open work in progress        | Case/ticket IDs, current status, what's already ruled out, next-action owner    | ___    | [ ] Y  [ ] N                           |
| Watch items                  | Anything informally monitored that isn't yet a ticket, and why it's being watched | ___  | [ ] Y  [ ] N                           |
| System / tooling status      | Known outages, ingestion delays, maintenance windows, workarounds in use        | ___    | [ ] Y  [ ] N                           |
| What to expect next          | Scheduled changes, planned noisy events, known upcoming activity                | ___    | [ ] Y  [ ] N                           |

If any row above needs its own escalation, log it on a ticket via the standard escalation path (SOC Playbook Handbook, Part 27 — Escalation Quality) rather than leaving it only in this record.
```

**[FRONTLINE MANAGER]** This checklist's main limitation is the same one Part 6 §7.2 names directly: it only works if the outgoing analyst gets protected time to fill it in before the overlap starts, and if the incoming analyst's acknowledgment is a real, checked step rather than an assumed formality. A checklist filled in after the outgoing analyst has already logged off isn't a handoff — it's a note nobody was required to read.

## 4. On-call rotation calculator (`TMPL-0603`)

**[SENIOR MANAGER]** A SOC manager sizing a primary/secondary on-call rotation — for the on-call/bridge coverage model itself, or as the surge lever named in Step 7 of `TMPL-0001` — uses this calculator to check whether the eligible pool is large enough to keep on-call from becoming a chronic burden rather than an occasional one.

```text
TEMPLATE — On-Call Rotation Calculator, permanent ID TMPL-0603

INPUTS
| Input                                              | Your value |
|-------------------------------------------------------|--------------|
| Analysts eligible for on-call rotation                | ___          |
| Rotation length (days per on-call turn)                | ___ (7 recommended — Part 6 §5) |
| Primary ack window (minutes)                           | ___ (10–15 typical — Part 6 §5) |
| Secondary ack window after a missed primary page (min) | ___          |
| Avg. off-hours pages/week (trailing 90 days)            | ___          |
| On-call stipend per week ($)                            | ___          |

CALCULATION
On-call weeks per analyst per year = 52 / (Analysts eligible for on-call rotation)
Your value: ______________
CONCEPTUAL SAMPLE: 8 eligible analysts -> 52 / 8 = 6.5 weeks/analyst/year (about one week every 8 weeks)

SUSTAINABILITY CHECK
[ ] Is on-call weeks/analyst/year at or below roughly one week in 6 (a rough starting heuristic for this worksheet, not a figure Part 17 specifies or a validated threshold — calibrate against your own team's actual complaint/attrition pattern)?
[ ] If below that line, is a stipend (not just a per-page bonus) budgeted to compensate the lost personal time (Part 18)?
[ ] Does the secondary's ack window plus the primary's ack window still land inside the response-time target the alert's severity requires (SOC Playbook Handbook, Part 29 — Playbook Severity Model)?

ROSTER
| Week starting | Primary on-call | Secondary on-call | Stipend paid (Y/N) | Bridge contacts if a major incident is declared |
|-----------------|--------------------|------------------------|-------------------------|------------------------------------------------------|
| ___             | ___                | ___                    | ___                     | ___                                                    |
```

**[SENIOR MANAGER]** The sustainability check's threshold is a starting heuristic, not a validated number this book has tested against its own data — a team with a genuinely low off-hours page volume may tolerate a tighter rotation than a team fielding frequent 2 a.m. pages on the same cadence. What this calculator doesn't decide is whether the pain of a tight rotation is better solved by hiring into the on-call pool or by reducing off-hours page volume at the source — that's the same staffing-versus-detection-quality judgment call Part 9 walks through for the standing queue.

---

**Cross-references.** This book: Part 5 — Headcount & Capacity Modeling (source of `TMPL-0001`'s formulas and `CASE-0501`'s worked figures); Part 6 — Shift Pattern & Coverage Design (source of `TMPL-0601`'s four coverage models, `TMPL-0602`'s handoff categories, and `TMPL-0603`'s on-call structure); Part 9 — Queue Health & Workload Management (the staffing-vs.-detection-quality judgment call referenced in §4); Part 17 — Burnout, Fatigue & Wellbeing (rotation-direction and on-call-frequency fatigue evidence behind §2 and §4's checks); Part 18 — Attrition & Retention (on-call compensation as a retention lever); Part 22 — MSSP & Managed-Service Contract Management (the surge/overflow lever in `TMPL-0001` Step 7 and `TMPL-0601` Part C's follow-the-sun cost comparison). Other volumes: SOC Playbook Handbook, Part 27 — Escalation Quality (per-ticket hand-off, distinct from `TMPL-0602`'s shift-level transfer) and Part 29 — Playbook Severity Model (per-alert response timing, distinct from `TMPL-0603`'s ack-window fields).

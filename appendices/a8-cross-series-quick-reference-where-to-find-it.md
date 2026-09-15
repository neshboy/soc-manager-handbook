---
title: "Appendix A8 — Cross-Series Quick Reference: Where to Find It"
appendix: "A8"
author: "author-agent"
reviewer: "technical-reviewer-agent"
status: "reviewed"
last_validated: "2026-09-15"
depends_on: []
---

# Appendix A8 — Cross-Series Quick Reference: Where to Find It

## Why this appendix exists

**[CONCEPT]** Part 1 — SOC Manager Foundations & the Series Map previews the three-book split in miniature: a short table mapping a handful of representative questions to whichever volume actually owns the answer, plus a "which book do I open" decision tree collapsed to three yes/no questions. Part 1 says explicitly that its own table is "a working summary, not the authoritative index" and points forward to this appendix for the full version. This is that full version: every distinct cross-reference this book's 33 parts actually make into *SIGNAL TO ACTION: The Complete SOC Playbook Handbook* and *The Detection Engineering Handbook V2*, compiled once, grouped by topic, and checked against each companion volume's own current `BOOK-INDEX.md` rather than trusted from memory.

**[CONCEPT]** This is the single place a reader checks before assuming a topic is missing from this book. If a paragraph anywhere in Parts 1–33 cites a companion-volume part by number and name, that citation is supposed to resolve to a row below — per this book's own production model, a build check fails if it doesn't. Nothing below is a template or a worksheet; unlike Appendices A1–A7, this appendix has no fillable artifact, because its job is navigation, not documentation. Read Part 1 first for the thesis behind the three-book split (a SOC manager's job, a detection engineer's job, and a client-facing playbook's job are three different units of analysis, not three difficulty tiers of the same subject); read this appendix when you already know roughly what you're looking for and need the specific part number.

**[SENIOR MANAGER]** Maintenance discipline matters more for this appendix than for any other, because a stale row here is worse than no row at all — it sends a reader to a part number a companion volume has since renumbered. Every row below was checked against *SOC Playbook Handbook*'s and *Detection Engineering Handbook V2*'s own `BOOK-INDEX.md` files as of this appendix's `last_validated` date, not reconstructed from memory. Whoever adds a new cross-reference anywhere in this book adds the matching row here in the same pull request — that is the build-check contract `BOOK-INDEX.md` describes, not a suggestion.

## 1. How to read this table

**[CONCEPT]** Each section below groups a topic area and lists, for every distinct question this book's chapters actually route elsewhere, which companion part owns the answer and why a reader would go there. The **Cited From** column names which part(s) of *this* book carry that specific cross-reference today — useful for auditing a citation against its actual source paragraph, and for spotting a topic this book touches only glancingly. An em dash (`—`) means no cross-reference exists for that cell, not that the topic doesn't matter. Where a part number could be confused with a same-numbered or similarly-titled part in the *other* companion volume, that collision is called out explicitly in the section it falls under — §5 carries the sharpest one.

## 2. Staffing, Shift Design & Operating Model

**[SENIOR MANAGER]** The table below covers operating-model, tiering, and staffing questions that this book owns outright but that brush up against a companion volume's mechanics at a specific, narrow point.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| Mechanics of a good Tier 1 → Tier 2 hand-off, on one ticket | SOC Playbook Handbook, Part 27 — Escalation Quality | What context has to travel, how to phrase an escalation note, how a manager audits hand-off quality at scale | Parts 1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 15, 20, 26, 30, 32 |
| How an individual alert's severity is scored | SOC Playbook Handbook, Part 29 — Playbook Severity Model | The per-ticket scoring mechanics this book's staffing and risk-acceptance decisions treat as an already-settled input | Parts 1, 3, 6, 9, 10, 22, 25, 26, 28, 29, 31 |
| What to automate vs. gate for human review | SOC Playbook Handbook, Part 30 — Automation and SOAR | The automation/human-review boundary decision itself, distinct from this book's staffing consequences of that decision (Part 21, Part 32) | Parts 1, 5, 21, 26, 31, 32 |
| Client-facing and third-party stakeholder communication content and timing | SOC Playbook Handbook, Part 28 — SOC-to-Stakeholder Communication | Who owns what gets told to a customer, partner, or the public, and when — run in parallel with, never confused with, this book's upward-only cadence in Part 28 | Parts 1, 28 |
| Detection rule logic, telemetry, and query-language mechanics behind any tool a SOC operates or migrates | Detection Engineering Handbook V2, Parts 3–29 | The technical content this book cites by name rather than re-derives whenever a staffing, hiring, or tooling decision touches a rule's internals | Parts 1, 2, 3, 10 |
| SIEM/EDR/SOAR platform-migration engineering cost (field mapping, parity testing, dual-running) | Detection Engineering Handbook V2, Part 6 — Normalisation | The component cost model this book's TCO worksheets (Part 21) and budget business case (Part 20) pull directly rather than re-price | Parts 1, 2, 21, 33 |
| Detection-as-code discipline: git-based rule review, ownership metadata, version control | Detection Engineering Handbook V2, Part 22 — Detection as Code | The review-pipeline standard a cross-trained detection engineer (Part 12), a promoted branch candidate (Part 13), a departing engineer's rule-ownership metadata (Part 14), or a new threshold-tuning role (Part 32) is held to | Parts 2, 12, 13, 14, 32 |

## 3. Escalation, Severity & Stakeholder Communication

**[CONCEPT]** This section repeats the two most heavily cited SOC Playbook Handbook parts on their own, because "escalation" and "severity" are the two topics this book's chapters reach for a companion citation on most often — worth its own quick lookup rather than only appearing folded into §2's broader table.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| Escalation-quality mechanics for a single ticket | SOC Playbook Handbook, Part 27 — Escalation Quality | See §2 above — repeated here because it is this book's single most frequently cited companion part | Parts 1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 15, 20, 26, 30, 32 |
| Playbook severity scoring for a single alert | SOC Playbook Handbook, Part 29 — Playbook Severity Model | See §2 above | Parts 1, 3, 6, 9, 10, 22, 25, 26, 28, 29, 31 |
| Contractual SLA response-time commitment vs. an internal severity-driven triage target | SOC Playbook Handbook, Part 29 — Playbook Severity Model | The internal scoring instrument this book's Part 22 explicitly distinguishes from a negotiated, remedy-backed MSSP contract clause | Part 22 |
| Individual playbook breakdowns: which step failed, in which incident | SOC Playbook Handbook, Part 35 — Playbook Failure Examples | The single-playbook, single-incident lens Part 29 of this book deliberately does not re-walk — Part 29 owns the pattern across many incidents instead | Parts 1, 29 |

## 4. Metrics

**[SENIOR MANAGER]** One structural rule governs every row in this section: a metric's *definition* lives with whichever volume actually owns it — the companion Playbook Handbook for MTTR, MTTA, and false-positive rate, or this book itself for handle time, backlog age, and MTTD, none of which the Playbook defines. Metric *use* — headcount modeling, board narratives, benchmarking caution, QA scoring — stays in this book either way. Redefining a metric that belongs to the other volume is treated as a defect, not a stylistic choice.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| What MTTR and false-positive rate precisely mean, and how they're instrumented consistently | SOC Playbook Handbook, Part 32 — Metrics | The fixed definitions every headcount model (Part 5), queue-health signal (Part 9), onboarding metric (Part 11), training review (Part 12), QA rubric (Part 15), attrition leading indicator (Part 18), budget cost-per-alert figure (Part 20), board translation (Part 24), and benchmark comparison (Part 31) treats as an already-settled input | Parts 1, 5, 9, 11, 12, 15, 18, 20, 24, 30, 31, 33 |
| What this book means by "handle time," "backlog age," or "MTTD" | This book's own operational definitions — Part 5 §2 (handle time), Part 9 §1 (backlog age), Part 24 §3 (MTTD) | Terms the Playbook Handbook never defines; owned locally so headcount modeling (Part 5), queue-health signal (Part 9), and board translation (Part 24) have one audited definition instead of three local ones | Parts 1, 5, 9, 24 |

## 5. Detection Engineering & Telemetry

**[CONCEPT]** This is where a manager's decision most often brushes against technical territory this book has no business re-deriving — a QA review touches escalation quality, a performance conversation touches false-positive engineering, a rationalization audit touches detection coverage. Every row below is a case where this book's own governing test (`STYLE-GUIDE.md` §1, Part 1 §2.1) routed the technical claim to a citation instead of a rewrite.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| Vocabulary for triage judgment (event, signal, alert, disposition) and what collapsing "the rule matched" into "the activity was malicious" gets wrong | Detection Engineering Handbook V2, Part 1 — Detection Engineering Foundations | The foundational distinctions this book's hiring-assessment rubric (Part 8) and competency matrix (Part 10) borrow rather than reinvent | Part 8 |
| Query-language mechanics across Sigma, KQL, SPL, AQL, YARA-L, and Elastic | Detection Engineering Handbook V2, Parts 24–29 | The six query-syntax parts, carried through a canonical detection so a reader can compare semantics across languages rather than learning six disconnected ones | Part 1 |
| Correlation engineering, baselining, threat intelligence as a scoring input, and risk-based detection | Detection Engineering Handbook V2, Parts 30–33 | The analytic-technique dependency chain (correlation → baselining → threat intel → risk scoring) this book's series map previews but never develops | Part 1 |
| False-positive tuning mechanics for a noisy detection rule | Detection Engineering Handbook V2, Part 38 — False Positive Engineering | The technical fix behind every case this book routes to a rule rather than a roster — a queue-health decomposition (Part 9), a performance diagnostic (Part 16), an alert-fatigue rotation decision (Part 17), a tooling migration (Part 21), a board translation (Part 24), or a risk-acceptance dual-track holding pattern (Part 25) | Parts 1, 3, 9, 16, 17, 24, 25 |

> **Blind Spot**
> Both companion volumes have a chapter called "False Positive Engineering," at two different part numbers, covering two different things — a naming collision this book's own citations navigate correctly but a reader checking a companion index cold could easily miss. *SOC Playbook Handbook, Part 25 — False Positive Engineering* covers the client-facing tuning workflow and correlation-thinking side of the problem, filed under that book's Operations & Governance section alongside SIEM queries and client-approval workflow. *Detection Engineering Handbook V2, Part 38 — False Positive Engineering* covers the technical taxonomy, tuning mechanics, and exception-list-as-debt framing, filed under that book's Testing & Quality Engineering section. Every citation inside this book's 33 parts that reads "Part 38 — False Positive Engineering" means the Detection Engineering Handbook V2 chapter specifically — none of this book's chapters currently cite SOC Playbook Handbook's Part 25 version. If a reader's own question is closer to "how do we get a client to sign off on a tuning change" than "how do we measure and fix a rule's false-positive rate," SOC Playbook Part 25, not DEH Part 38, is the one to open.

## 6. Threat Hunting

**[CONCEPT]** Threat hunting shows up in this book only as an organizational-design and career-track question — where hunting sits relative to the tiers, how a hunter branch is staffed and protected, what a hunter candidate has to demonstrate to earn the title. The methodology itself lives entirely in one companion volume.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| Threat-hunting methodology broadly: hypothesis formation, scoping, pivoting, converting a hunt into a detection candidate | Detection Engineering Handbook V2, Parts 34–36 — Threat Hunting Methodology | The technical content this book's specialist-tier design (Part 3), cross-training rotation (Part 12), and branch-promotion bar (Part 13) all cite rather than re-teach | Parts 1, 3, 12 |
| Hypothesis formation and the specific discipline of stating, before touching the data, what a negative result would look like | Detection Engineering Handbook V2, Part 34 — Threat Hunting Fundamentals | The work-sample standard a threat-hunter branch candidate's completed-hunt record is measured against | Part 13 |
| The range of hunt types (IOC-based, TTP-based, anomaly-based, intel-led, incident-led, gap-driven, retrospective) | Detection Engineering Handbook V2, Part 35 — Hunt Types | The taxonomy behind "at least two structured hunts" in a threat-hunter branch's entrance bar | Part 13 |

## 7. Detection Coverage, Quality & Debt

**[SENIOR MANAGER]** These three parts are the technical measurement layer underneath a large share of this book's judgment-call chapters — a queue-health decomposition, a tool-rationalization audit, a board translation, and the maturity synthesis in §11 below all consume this trio as a finished input rather than re-scoring anything themselves.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| Testing whether a detection fires correctly, for the right reason, and survives a schema change, clock skew, or high volume | Detection Engineering Handbook V2, Part 37 — Detection Testing | The test-case patterns this book's ramp-certification exercises (Part 11) pull sanitized scenarios from | Part 11 |
| Whether a validated, tested detection exists for a given technique in the organization's own threat profile | Detection Engineering Handbook V2, Part 41 — Detection Coverage | The six-tier coverage model this book's tool-rationalization audit (Part 23), cross-team severity-authority dispute (Part 26), and maturity synthesis (Part 30) all cite as the technical arbitration this book itself never performs | Parts 1, 20, 23, 24, 26, 30, 31 |
| Precision/recall in SOC terms, alert-to-incident ratio, analyst handling time, and suppression tracking as measures of an existing detection's own quality | Detection Engineering Handbook V2, Part 42 — Detection Quality | The measurement this book's queue-health decision tree (Part 9) and board-facing translation of a false-positive-rate figure (Part 24) both route to before treating a lean ratio as good news | Parts 1, 9, 17, 20, 23, 24, 30, 31 |
| Detection debt, telemetry debt, parser debt, and tuning debt as an inventory-and-payoff ledger | Detection Engineering Handbook V2, Part 43 — Detection Debt | The framework this book routes to whenever a recurring miss, a departing detection engineer's undocumented rule, or a third-time-recurring postmortem finding turns out to be a rule problem, not a people problem | Parts 1, 3, 10, 14, 16, 18, 19, 20, 25, 29, 31, 32 |
| Whether a rationalization candidate is the sole source of coverage for a technique before it's retired | Detection Engineering Handbook V2, Parts 41–43 | The combined coverage/quality/debt check a tool-sprawl retirement decision (Part 23) or a build-vs-buy business case (Part 20) cannot substitute for on its own | Parts 20, 23 |

## 8. AI Security

**[CONCEPT]** This book's AI content is scoped narrowly and deliberately: the staffing and organizational-design consequences of AI copilots and agentic automation, not the workflow mechanics of using one or the technical detection content an AI system itself generates. The gap between what this book covers and what a reader might actually be looking for under "AI security" is real enough to state plainly rather than paper over.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| Which Tier 1 work is genuinely displaced by AI-assisted triage, and what that does to headcount, competency matrices, and career tracks | This book, Part 32 — AI, Automation, and the Future Shape of the SOC | This book's own territory, owned outright | — |
| Tool selection inside a triage workflow, confidence-threshold implementation, and human-review gating at the ticket level | SOC Playbook Handbook, Part 31 — AI-Assisted SOC Operations | The operational mechanics this book's Part 32 explicitly does not re-cover | Parts 1, 32 |
| Prompt injection, RAG/knowledge-base poisoning, agent and MCP-tool abuse, AI API compromise — the technical detection content for an AI system itself | Detection Engineering Handbook V2, Part 20 — AI Systems Telemetry & Audit-Trail Engineering, Part 21 — AI Security Detection Engineering | The telemetry and analytic layers for AI-specific attacks — **not currently cross-referenced from any part of this book**; a reader landing here from this book's index will not find a pointer to it anywhere else in these 33 parts | — |
| Per-alert playbooks for AI Security incidents (prompt injection, malicious file upload, agent abuse) and the multi-stage AI malicious-file-upload master playbook | SOC Playbook Handbook, AI Security playbook category (Category 18) | The client-facing, per-alert response playbooks for the same attack surface DEH V2 Parts 20–21 detect — **also not currently cross-referenced from this book** | — |
| The full attack-stage model for an AI system compromise (prompt/file → model → RAG → agent → tool → sensitive system → external destination) | Detection Engineering Handbook V2, Part 48 — AI Compromise Model | The applied compromise model for this domain, alongside the ransomware, identity, and web compromise models Part 28 of this book cites collectively as "Parts 44–48" without singling Part 48 out by name | — |

## 9. Major Incidents & Post-Incident Review

**[SENIOR MANAGER]** Major-incident content is split three ways across the series on purpose, and this section's three rows are that split made literal: the technical attack-stage analysis, the analyst/incident-commander-level operational playbook, and the manager's-chair layer neither of the other two books has a reason to cover.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| The incident-commander role and the technical containment/eradication sequence for a ransomware event | SOC Playbook Handbook, Ransomware Master Playbook | The operational playbook this book's Part 28 explicitly does not re-derive — the manager's-chair complement, not a replacement | Parts 1, 28 |
| The technical attack-stage analysis behind a specific compromise (ransomware, identity, web, AI) | Detection Engineering Handbook V2, Parts 44–48 — Applied Compromise Models | The third leg of the series' deliberate three-way split of major-incident content — cited once by this book's Part 28 and not referenced again, because none of that technical detail changes what a manager decides | Part 28 |
| Insider-threat detection and escalation mechanics: the behavioral indicators and correlation logic that confirm a finding | SOC Playbook Handbook, Insider Threat Playbooks (Category 19) | The detection-and-confirmation mechanics this book's Part 27 explicitly starts after — Part 27 owns the organizational aftermath of an already-confirmed finding, not detecting one | Part 27 |
| Individual playbook breakdowns inside one incident's own response | SOC Playbook Handbook, Part 35 — Playbook Failure Examples | See §3 above — the single-incident lens Part 29's organizational review deliberately does not duplicate | Parts 1, 29 |
| Client-facing communication cadence during a live major incident | SOC Playbook Handbook, Part 28 — SOC-to-Stakeholder Communication | See §2 and §3 above — runs in parallel with, and is never the same conversation as, this book's upward-only board cadence | Parts 1, 28 |

## 10. Playbook Mechanics, Testing & Governance

**[CONCEPT]** A small cluster of citations exists purely to keep this book from re-authoring playbook structure or test methodology anywhere a manager's chapter happens to touch a playbook in passing.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| How to write or structure a specific playbook, from a bare detection rule to a finished document | SOC Playbook Handbook, Foundations / Playbook Library | Playbook mechanics across the whole series — the destination for tribal knowledge this book's Part 14 identifies as needing to be written down, once it's ready to become a playbook | Parts 1, 14 |
| Simulation and lab-based methodology for producing realistic test telemetry | SOC Playbook Handbook, Part 34 — Playbook Testing | The methodology this book's ramp-certification program (Part 11) and playbook-quality maturity model (Part 30, via Appendix 38A) both cite rather than re-derive | Part 11 |

## 11. Maturity Models

**[SENIOR MANAGER]** Three maturity models exist across the series, deliberately kept from collapsing into one blended score — Part 30 of this book is the synthesis chapter that reads all three together without letting a strong score on one stand in for the others.

| Topic / Question | Book & Part | What You'll Find There | Cited From (this book) |
|---|---|---|---|
| Organizational-design maturity: staffing ratios, process maturity, training-program maturity, tooling maturity | This book, Part 30 — SOC Maturity Models | This book's own model, owned outright | — |
| Playbook-quality maturity: whether a specific playbook is complete, clear, and produces a proper hand-off | SOC Playbook Handbook, Appendix 38A — Playbook Maturity Model | The structural-quality lens this book's Part 30 cites and never re-scores | Part 30 |
| Detection coverage/quality maturity: whether a validated, tested detection exists per technique, and performs well | Detection Engineering Handbook V2, Part 41 — Detection Coverage, Part 42 — Detection Quality | The technical-content lens Part 30's three-lens synthesis reads alongside the other two, in that order, when sequencing an investment decision | Part 30 |

## Cross-references

**[CONCEPT]** This appendix is the standing, build-checked expansion of Part 1 — SOC Manager Foundations & the Series Map §2's series-map table; every cross-book citation added anywhere in Parts 2–33 must resolve to a row above.

# The SOC Manager's Operating Handbook

**Staffing, Shift Design, Quality, Vendors, Budget, and Crisis Leadership — Running the Team, Not the Queue**

📄 **[Download the full PDF](./SOC_Manager_Operating_Handbook.pdf)** — 511 pages, ~209,000 words across 33 parts and 8 appendices.

Volume 3 of the **NESHBOY SOC Professional Library**, alongside [SIGNAL TO ACTION: The Complete SOC Playbook Handbook](https://github.com/neshboy/soc-playbook-handbook) and [The Detection Engineering Handbook V2](https://github.com/neshboy/detection-engineering-handbook).

This is a handbook for the person who runs a SOC — not the analyst working a queue, not the engineer building a rule, but the manager who decides how many analysts there are, what shift they work, whether that rule ships, whether that vendor gets renewed, and what the board is told when it goes wrong. The other two volumes in this series already own the technical and playbook-mechanics side of SOC operations in depth; this book deliberately does not re-walk that ground. Its subject is staffing and capacity modeling, shift design, hiring and competency, quality assurance as a program, burnout and attrition, vendor/MSSP contract management, budget and tooling procurement, cross-team politics, risk-acceptance judgment calls, crisis leadership from the manager's chair, and SOC maturity — cross-referencing the other two volumes by name and part number wherever a topic is genuinely theirs.

## Reading the book

- **[SOC_Manager_Operating_Handbook.pdf](./SOC_Manager_Operating_Handbook.pdf)** — the assembled, print-ready book. Start here.
- **[BOOK-INDEX.md](./BOOK-INDEX.md)** — the full part/appendix table with per-unit scope, plus a "Key structural decisions and provenance" section recording exactly which scope boundaries against the other two books were deliberate.
- **[Appendix A8 — Cross-Series Quick Reference](./appendices/a8-cross-series-quick-reference-where-to-find-it.md)** — an exhaustive, checked-against-source lookup table mapping topics to whichever of the three NESHBOY volumes actually owns the answer. Start here if you're not sure this is the right book for your question.
- **[STYLE-GUIDE.md](./STYLE-GUIDE.md)** — the voice, formatting, and figure-evidence-classification contract every part follows: six content tags (`[CONCEPT]`, `[FRONTLINE MANAGER]`, `[SENIOR MANAGER]`, `[HR/PEOPLE]`, `[VENDOR/PROCUREMENT]`, `[EXECUTIVE]`) and eight recurring callouts (Management Autopsy, Manager's Note, Operational Reality, Blind Spot, People Risk Trap, Field Test, Cross-Book Pointer, What Would Change My Mind), adapted from the Detection Engineering Handbook V2's style contract for series-wide consistency.

## What's synthetic vs. real

Every case study, dollar figure, and worked example in this book is either a **CONCEPTUAL** illustration, a **COMPOSITE CASE EXAMPLE** (a plausible scenario built from patterns, not one real event), or explicitly cited as an **OFFICIAL REFERENCE** to real published research (e.g. shift-work circadian science) — never a claim that a real, identifiable organization or incident is being described unless genuinely public and named. Diagrams are original Mermaid flowcharts and decision trees. This book contains no fabricated screenshots or invented "real" company data. **[REFERENCES.md](./REFERENCES.md)** lists every real external source cited inline, with the part/section it backs.

## How it was built

- `build/build_book.js` — parses `BOOK-INDEX.md`'s part/appendix tables, assembles all 41 chapter/appendix files into one HTML document, and prints it to PDF via headless Chrome.
- `build/mmdc_render.py` — renders Mermaid diagram source to SVG via `@mermaid-js/mermaid-cli`.
- `build/add_watermark.py` — applies the diagonal `neshboy` watermark to every page.
- `CASE-INVENTORY.md`, `VISUAL-INVENTORY.md` — permanent IDs for every named case study and figure, tracked independently of position in the book so cross-references (this book cites its own case studies across chapters constantly) never break on reorganization.

## Rebuilding it yourself

```
cd build
npm install
node build_book.js
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer ^
  --print-to-pdf="..\_build\SOC_Manager_Operating_Handbook.pdf" "..\_build\book.html"
python add_watermark.py
```

## Repository layout

- `chapters/`, `appendices/` — the 33 parts + 8 appendices, Markdown source of record.
- `assets/diagrams/` — rendered Mermaid SVGs.
- `build/` — the build/render/watermark tooling above.
- `BOOK-INDEX.md`, `STYLE-GUIDE.md`, `CASE-INVENTORY.md`, `VISUAL-INVENTORY.md`, `REFERENCES.md` — cross-cutting project documentation.

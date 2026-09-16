import os
import subprocess
import textwrap
from PIL import Image, ImageDraw, ImageFont

# Figure 1.1 -- Risk-acceptance escalation path, Part 1, `FIG-0001`.
# Verbatim mermaid source, copied from
# chapters/part01-soc-manager-foundations-and-the-series-map.md, rendered
# the same way build/mmdc_render.py renders every other figure in this book.
FIG_0001_MERMAID = """flowchart LR
    A["Analyst flags a risk\\n(e.g. a known FP pattern,\\na coverage gap, a missed SLA)"] --> B{"Reversible within\\none shift? Bounded\\nblast radius?"}
    B -->|Yes| C["Team lead accepts\\nor escalates"]
    B -->|No| D{"Within the SOC\\nmanager's standing\\nbudget/policy authority?"}
    D -->|Yes| E["SOC manager accepts\\nthe risk -- Part 25"]
    D -->|No| F["Escalate to CISO/board\\nwith a written risk memo\\n-- Part 24, Appendix A7"]
"""


def render_mermaid_to_png(mmd_text, out_png):
    tmp_mmd = out_png + ".mmd"
    with open(tmp_mmd, "w", encoding="utf-8") as f:
        f.write(mmd_text)
    cmd = ["npx", "-y", "@mermaid-js/mermaid-cli", "-i", tmp_mmd, "-o", out_png, "-b", "white"]
    subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=90)
    os.remove(tmp_mmd)
    if not (os.path.exists(out_png) and os.path.getsize(out_png) > 0):
        raise RuntimeError("mermaid render failed for " + out_png)

FONT_DIR = r"C:\Windows\Fonts"
SANS = os.path.join(FONT_DIR, "segoeui.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "segoeuib.ttf")
SANS_SEMIBOLD = os.path.join(FONT_DIR, "seguisb.ttf")
MONO = os.path.join(FONT_DIR, "consola.ttf")

# palette (dataviz skill reference instance, light mode) -- matches the
# Detection Engineering Handbook reference pack exactly.
SURFACE = (252, 252, 251)
PAGE = (249, 249, 247)
INK = (11, 11, 11)
SECONDARY = (82, 81, 78)
MUTED = (137, 135, 129)
HAIRLINE = (225, 224, 217)
ACCENT = (42, 120, 214)       # categorical slot 1 - blue
GOOD = (12, 163, 12)
CRITICAL = (208, 59, 59)

W = H = 1200
BOOK_TITLE = "The SOC Manager's Operating Handbook"

HERE = os.path.dirname(os.path.abspath(__file__))


def F(path, size):
    return ImageFont.truetype(path, size)


def new_card():
    img = Image.new("RGB", (W, H), SURFACE)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 10], fill=ACCENT)
    return img, d


def eyebrow(d, text, y, x=80):
    f = F(SANS_BOLD, 20)
    d.text((x, y), text.upper(), font=f, fill=ACCENT)
    return y + 34


def wrap_draw(d, text, x, y, font, fill, max_w_chars, line_h, max_lines=None):
    lines = textwrap.wrap(text, width=max_w_chars)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        d.text((x, y), line, font=font, fill=fill)
        y += line_h
    return y


def footer(d, label):
    f = F(SANS, 18)
    d.text((80, H - 56), label, font=f, fill=MUTED)


# ---------------------------------------------------------------------------
# Card 1 - title-stats
# ---------------------------------------------------------------------------

def card1():
    img, d = new_card()
    y = eyebrow(d, "New handbook", 100)

    title_f = F(SANS_BOLD, 66)
    title_lines = ["The SOC Manager's", "Operating Handbook"]
    y = 168
    for line in title_lines:
        d.text((80, y), line, font=title_f, fill=INK)
        y += 78

    sub_f = F(SANS, 30)
    y += 8
    subtitle = ("Staffing, Shift Design, Quality, Vendors, Budget, and Crisis "
                "Leadership \u2014 Running the Team, Not the Queue")
    y = wrap_draw(d, subtitle, 80, y, sub_f, SECONDARY, max_w_chars=44, line_h=42)

    y += 28
    d.line([(80, y), (W - 80, y)], fill=HAIRLINE, width=2)
    y += 55

    stats = [
        ("33", "Parts"),
        ("61", "Case studies"),
        ("37", "Diagrams"),
        ("511", "Pages"),
    ]
    col_w = (W - 160) / 4
    num_f = F(SANS_BOLD, 60)
    label_f = F(SANS, 22)
    stats_top = y
    for i, (num, label) in enumerate(stats):
        cx = 80 + i * col_w
        d.text((cx, stats_top), num, font=num_f, fill=INK)
        d.text((cx, stats_top + 78), label, font=label_f, fill=SECONDARY)
        if i > 0:
            d.line([(cx - 30, stats_top + 3), (cx - 30, stats_top + 120)], fill=HAIRLINE, width=2)
    y = stats_top + 165

    d.line([(80, y), (W - 80, y)], fill=HAIRLINE, width=2)
    y += 45

    quote_f = F(SANS, 28)
    quote = ("Every chapter carries a mandatory adversarial reviewer, "
             "not a copy-edit pass \u2014 and a status that only advances "
             "draft \u2192 reviewed \u2192 tested \u2192 released.")
    wrap_draw(d, quote, 80, y, quote_f, SECONDARY, max_w_chars=48, line_h=40)

    footer(d, BOOK_TITLE)
    return img


# ---------------------------------------------------------------------------
# Card 2 - quote-autopsy
# ---------------------------------------------------------------------------

def card2():
    img, d = new_card()
    y = eyebrow(d, "The book's central thesis, in one case study", 100)

    quote_f = F(SANS_SEMIBOLD, 42)
    quote = ('\u201cA staffing model that can\u2019t survive its own team\u2019s '
              'normal attrition rate isn\u2019t a staffing model; it\u2019s a bet '
              'that nobody quits this year.\u201d')
    y = 168
    y = wrap_draw(d, quote, 80, y, quote_f, INK, max_w_chars=28, line_h=54)

    y += 20
    d.line([(80, y), (170, y)], fill=ACCENT, width=5)
    y += 45

    body_f = F(SANS, 27)
    para1 = ("A 24/7, three-shift SOC budgeted 15 analysts with a flat 10% "
             "shrinkage allowance \u2014 a number that matched the prior year's "
             "PTO usage almost exactly. Real shrinkage, once training days, sick "
             "leave, and one parental leave were counted, ran closer to 32%.")
    y = wrap_draw(d, para1, 80, y, body_f, SECONDARY, max_w_chars=52, line_h=39)

    y += 22
    para2 = ("When two senior analysts resigned in the same quarter \u2014 an "
             "unremarkable 13% attrition event \u2014 there was no buffer to "
             "absorb it, and mandatory overtime became the only lever left.")
    y = wrap_draw(d, para2, 80, y, body_f, SECONDARY, max_w_chars=52, line_h=39)

    y += 30
    d.line([(80, y), (W - 80, y)], fill=HAIRLINE, width=2)
    y += 35

    muted_f = F(SANS, 23)
    muted = ("The overtime premium alone cost more across eight weeks than "
             "opening the requisitions immediately would have.")
    y = wrap_draw(d, muted, 80, y, muted_f, MUTED, max_w_chars=58, line_h=32)

    tag_text = "Part 1 \u2014 SOC Manager Foundations, CASE-0001"
    tag_f = F(SANS_BOLD, 22)
    tw = d.textlength(tag_text, font=tag_f)
    tag_y = H - 130
    d.rectangle([80, tag_y, 80 + tw + 32, tag_y + 44], outline=ACCENT, width=2)
    d.text((96, tag_y + 10), tag_text, font=tag_f, fill=ACCENT)

    footer(d, BOOK_TITLE)
    return img


# ---------------------------------------------------------------------------
# Card 3 - diagram-showcase
# ---------------------------------------------------------------------------

def card3():
    img, d = new_card()
    y = eyebrow(d, "Whose call is this \u2014 Part 1", 100)

    title_f = F(SANS_BOLD, 40)
    y = 168
    title = "The risk-acceptance escalation path"
    y = wrap_draw(d, title, 80, y, title_f, INK, max_w_chars=30, line_h=50)

    box_x0, box_y0, box_x1, box_y1 = 80, 300, W - 80, 760
    d.rectangle([box_x0, box_y0, box_x1, box_y1], outline=HAIRLINE, width=2, fill=SURFACE)

    diagram_path = os.path.join(HERE, "_fig0001_tmp.png")
    render_mermaid_to_png(FIG_0001_MERMAID, diagram_path)
    diagram = Image.open(diagram_path).convert("RGB")
    os.remove(diagram_path)
    pad = 40
    max_w = (box_x1 - box_x0) - 2 * pad
    max_h = (box_y1 - box_y0) - 2 * pad
    scale = min(max_w / diagram.width, max_h / diagram.height)
    new_size = (int(diagram.width * scale), int(diagram.height * scale))
    diagram = diagram.resize(new_size, Image.LANCZOS)
    paste_x = box_x0 + ((box_x1 - box_x0) - new_size[0]) // 2
    paste_y = box_y0 + ((box_y1 - box_y0) - new_size[1]) // 2
    img.paste(diagram, (paste_x, paste_y))

    d = ImageDraw.Draw(img)
    cap_f = F(SANS, 25)
    caption = ("A flagged risk escalates from team lead to SOC manager to "
               "CISO/board as its blast radius and reversibility grow \u2014 "
               "never accepted by default just because nobody stopped it.")
    wrap_draw(d, caption, 80, box_y1 + 42, cap_f, SECONDARY, max_w_chars=58, line_h=36)

    footer(d, BOOK_TITLE)
    return img


# ---------------------------------------------------------------------------
# Card 4 - Management Autopsy
# ---------------------------------------------------------------------------

def card4():
    img, d = new_card()
    y = eyebrow(d, "Management Autopsy", 100)

    title_f = F(SANS_BOLD, 44)
    y = 168
    title = "\u201cStaff to headcount, not to shrinkage\u201d"
    y = wrap_draw(d, title, 80, y, title_f, INK, max_w_chars=26, line_h=54)

    box_top = 300
    box_bottom = 900
    gutter = 40
    box_w = (W - 160 - gutter) / 2
    left_x0, left_x1 = 80, 80 + box_w
    right_x0, right_x1 = left_x1 + gutter, left_x1 + gutter + box_w

    d.rectangle([left_x0, box_top, left_x1, box_bottom], outline=HAIRLINE, width=2)
    d.rectangle([right_x0, box_top, right_x1, box_bottom], outline=HAIRLINE, width=2)

    tag_f = F(SANS_BOLD, 20)

    def tag(x0, y0, text, color):
        tw = d.textlength(text, font=tag_f)
        d.rectangle([x0, y0, x0 + tw + 24, y0 + 36], fill=color)
        d.text((x0 + 12, y0 + 8), text, font=tag_f, fill=(255, 255, 255))

    pad = 28
    tag(left_x0 + pad, box_top + pad, "THE DECISION", CRITICAL)
    tag(right_x0 + pad, box_top + pad, "THE FIX", GOOD)

    body_f = F(SANS, 22)
    line_h = 31

    left_text = (
        "15 analysts budgeted, 5 per shift, with a flat 10% shrinkage "
        "allowance that matched last year's PTO almost exactly.\n\n"
        "Real shrinkage ran ~32%, not 10%. When two senior analysts "
        "resigned in one quarter, there was no buffer \u2014 13 remaining "
        "analysts absorbed ~15 extra hours a week each for 8 straight "
        "weeks of mandatory overtime."
    )
    ty = box_top + pad + 55
    for para in left_text.split("\n\n"):
        ty = wrap_draw(d, para, left_x0 + pad, ty, body_f, SECONDARY,
                        max_w_chars=34, line_h=line_h)
        ty += 18

    right_text = (
        "Model headcount against realistic shrinkage (Part 5), and treat "
        "\u201ctwo analysts leave without notice\u201d as an expected event a "
        "standing buffer absorbs \u2014 not an exception that justifies "
        "emergency overtime.\n\n"
        "The overtime premium (~$54/hr worked) cost more across those 8 "
        "weeks than a new hire's incremental cost (~$7,800/month) would "
        "have \u2014 and 3 more analysts started job-hunting within two "
        "quarters."
    )
    ty = box_top + pad + 55
    for para in right_text.split("\n\n"):
        ty = wrap_draw(d, para, right_x0 + pad, ty, body_f, SECONDARY,
                        max_w_chars=34, line_h=line_h)
        ty += 18

    muted_f = F(SANS, 24)
    muted_y = box_bottom + 45
    muted = ("A staffing model that can't survive its own team's normal "
             "attrition rate is a bet that nobody quits this year \u2014 the "
             "pattern Part 5's headcount loop exists to catch.")
    wrap_draw(d, muted, 80, muted_y, muted_f, MUTED, max_w_chars=62, line_h=33)

    footer(d, BOOK_TITLE)
    return img


if __name__ == "__main__":
    out_dir = HERE
    card1().save(os.path.join(out_dir, "01-title-stats.png"))
    card2().save(os.path.join(out_dir, "02-quote-autopsy.png"))
    card3().save(os.path.join(out_dir, "03-diagram-showcase.png"))
    card4().save(os.path.join(out_dir, "04-autopsy.png"))
    print("done")

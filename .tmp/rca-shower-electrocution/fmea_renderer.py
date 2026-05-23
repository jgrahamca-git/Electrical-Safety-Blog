#!/usr/bin/env python3
"""
ELI Safety Blog — FMEA Renderer
================================
Per-RCA CONFIG for: The Fatal Shower — Missing EGC Electrocution
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import textwrap

# ============================================================================
# CONFIG — Rooftop Water Pump Electrocution (2008 RPC Shower Incident)
# ============================================================================

POST_SLUG = "shower-electrocution"
TITLE     = "FAILURE MODES AND EFFECTS ANALYSIS"
SUBTITLE  = "Ungrounded Water Pump Electrocution  /  Missing EGC Energizes Building Plumbing"
OUTPUT    = f"fmea-{POST_SLUG}.png"

MODES = [
    {"n":1, "mode":"Missing Equipment Grounding Conductor on pump motor",
     "cause":"Pump installed without dedicated EGC; no low-impedance fault return path to source.",
     "effect":"Phase-to-casing fault energizes pump housing and all connected metalwork at line voltage. Breaker cannot trip.",
     "s":10,"o":9,"d":8,
     "control":"None — visual inspection cannot confirm continuity without testing.",
     "action":"Verify EGC continuity with low-resistance ohmmeter at every motor installation and during annual PM."},
    {"n":2, "mode":"Motor winding insulation degradation (phase-to-casing short)",
     "cause":"Thermal cycling, moisture ingress, vibration fatigue degrade stator insulation over service life.",
     "effect":"Dead short from phase conductor to motor casing. Initiating event for electrocution sequence.",
     "s":9,"o":5,"d":10,
     "control":"None — no insulation resistance testing program in place.",
     "action":"Implement annual megger (insulation resistance) testing on all pump and motor circuits. Trend results."},
    {"n":3, "mode":"No GFCI protection on wet-location utilization circuit",
     "cause":"Circuit supplying pump and downstream wet-location outlets installed without GFCI protection.",
     "effect":"Leakage current through plumbing/water/person undetected; no fast-trip personnel protection.",
     "s":9,"o":8,"d":5,
     "control":"Visually detectable at panel if inspector knows to look.",
     "action":"Install GFCI protection on all circuits supplying equipment in wet or damp locations per NEC 210.8 / CEC 26-700."},
    {"n":4, "mode":"No EGC continuity verification in preventive maintenance program",
     "cause":"PM checklist covers operational parameters only; EGC integrity never tested after initial install.",
     "effect":"Silent EGC degradation (corrosion, vibration loosening) goes undetected until fault occurs.",
     "s":9,"o":8,"d":7,
     "control":"None — not in PM scope.",
     "action":"Add EGC continuity test to every motor PM cycle. Record readings. Flag any reading > 1 ohm."},
    {"n":5, "mode":"Unqualified personnel performing electrical maintenance",
     "cause":"Contractor staffing gap; maintenance workers lack electrical qualifications and diagnostic tools.",
     "effect":"Hazards not identified during inspections; band-aid repairs perpetuate unsafe conditions.",
     "s":8,"o":6,"d":5,
     "control":"Credential verification at hiring (inconsistently enforced).",
     "action":"Require verified electrical qualifications for all personnel performing electrical work. Audit contractor compliance."},
    {"n":6, "mode":"No periodic insulation resistance (megger) testing on pump motors",
     "cause":"Facility has no IR testing program; motor condition assessed only by operational performance.",
     "effect":"Winding degradation invisible until catastrophic short. No early warning, no trending.",
     "s":8,"o":7,"d":8,
     "control":"None.",
     "action":"Deploy annual IR testing on all motors. Establish baseline and trend. Replace or rewind at 1 megohm minimum."},
    {"n":7, "mode":"Metallic plumbing not included in equipotential bonding assessment",
     "cause":"Plumbing system treated as mechanical, not electrical; excluded from bonding surveys.",
     "effect":"Energized equipment transfers voltage to plumbing throughout building. Shock hazard at every fixture.",
     "s":9,"o":7,"d":7,
     "control":"Code requires bonding but compliance not verified at this facility.",
     "action":"Include all metallic water piping in bonding surveys per NEC 250.104(A) / CEC 10-406. Verify with ohmmeter."},
    {"n":8, "mode":"No ground-fault monitoring or indication system",
     "cause":"Older facility; no GFI relay, no ground-fault alarm, no leakage current monitoring.",
     "effect":"Low-level ground faults persist undetected; no alarm to trigger investigation before contact.",
     "s":7,"o":7,"d":8,
     "control":"None.",
     "action":"Install ground-fault indication on critical feeders. Alarm at threshold. Investigate every alarm."},
    {"n":9, "mode":"Production pressure overriding safety verification hold-points",
     "cause":"Operational tempo prioritizes uptime; safety checks deferred or skipped to restore service.",
     "effect":"Systemic enabler — every other procedural gap persists because verification is bypassed.",
     "s":8,"o":8,"d":7,
     "control":"Safety management system exists on paper but not enforced in practice.",
     "action":"Establish mandatory safety hold-points that cannot be overridden without site electrical authority sign-off."},
    {"n":10,"mode":"Band-aid repair culture — symptomatic fixes without root-cause investigation",
     "cause":"Maintenance responds to symptoms (no water) not causes (electrical fault). No RCA process.",
     "effect":"Underlying hazards persist and compound. Each repair masks the real problem.",
     "s":7,"o":8,"d":6,
     "control":"Repeat-failure patterns occasionally noticed but not formally tracked.",
     "action":"Implement work-order root-cause field. Flag repeat failures for electrical investigation before re-energizing."},
]

PRIORITY_WHY = {
    1: "The primary fatal mode. Without an EGC, every other protection layer becomes irrelevant.",
    4: "Highest-leverage procedural fix. One PM line item catches mode 1 before it kills.",
    2: "The initiating failure. Insulation testing is the earliest possible detection point.",
    6: "Detection gap that lets mode 2 progress undetected for months or years.",
}

# ============================================================================
# LOCKED LAYOUT — do not change without updating FMEA_VISUAL_STANDARD.md
# ============================================================================

# Brand tokens
BG_BLACK     = "#0D0F12"
BG_DARK      = "#141720"
BG_PANEL     = "#1A1E26"
BG_HEADER    = "#252A35"
BORDER       = "#2A3040"
TEXT_WHITE   = "#F2EDE8"
TEXT_DIM     = "#A8A398"
ARC_ORANGE   = "#E8680A"

# RPN class colors (locked rubric)
RPN_CRITICAL = "#8B1A1A"
RPN_HIGH     = "#C85A1A"
RPN_MEDIUM   = "#D4A017"
RPN_LOW      = "#2E7D32"

def rpn_color_class(rpn: int):
    if rpn >= 500: return RPN_CRITICAL, "CRITICAL"
    if rpn >= 350: return RPN_HIGH,     "HIGH"
    if rpn >= 200: return RPN_MEDIUM,   "MEDIUM"
    return RPN_LOW, "LOW"

# Figure dimensions — 16:9 landscape
FIG_W, FIG_H = 32.0, 18.0
DPI          = 110

# Margins
LEFT_MARGIN  = 0.4
RIGHT_MARGIN = 0.4
USABLE_W     = FIG_W - LEFT_MARGIN - RIGHT_MARGIN  # 31.2

# Column definitions (name, width-in-inches)
COLS = [
    ("#",                  0.45),
    ("Failure Mode",       4.30),
    ("Cause",              4.80),
    ("Effect",             4.10),
    ("S",                  0.45),
    ("O",                  0.45),
    ("D",                  0.45),
    ("RPN",                1.00),
    ("Class",              1.30),
    ("Current Control",    5.20),
    ("Recommended Action", 8.70),
]
_widths_sum = sum(w for _, w in COLS)
assert abs(_widths_sum - USABLE_W) < 0.05, f"col sum {_widths_sum} != {USABLE_W}"

# Row + section heights
ROW_H           = 1.05
HEADER_H        = 0.50
TITLE_H         = 0.95
SUMMARY_TITLE_H = 0.45
PRIORITY_ROW_H  = 0.70

# Text wrapping calibration (DejaVu Sans, with cell padding)
CHARS_PER_INCH = {7.5: 12, 8: 11, 8.5: 10, 9: 9.5, 9.5: 9, 10: 8.5}

def chars_for(width_in, fs):
    cpi = CHARS_PER_INCH.get(fs, 9.5)
    return max(6, int((width_in - 0.20) * cpi))

def wrap_text(t, max_chars):
    return "\n".join(textwrap.wrap(t, width=max_chars)) if t else ""

def col_x(idx):
    x = LEFT_MARGIN
    for i in range(idx):
        x += COLS[i][1]
    return x

def col_w(idx):
    return COLS[idx][1]

# ============================================================================
# Top-4 auto-derivation from MODES + PRIORITY_WHY
# ============================================================================

def compute_top_priorities(modes, priority_why):
    scored = []
    for m in modes:
        rpn = m["s"] * m["o"] * m["d"]
        scored.append((m["n"], rpn, m["mode"]))
    scored.sort(key=lambda t: (-t[1], t[0]))
    top = scored[:4]
    out = []
    for n, rpn, mode_name in top:
        _, klass = rpn_color_class(rpn)
        klass_title = klass.title()
        why = priority_why.get(n, "(no rationale provided — add to PRIORITY_WHY)")
        short_name = mode_name if len(mode_name) <= 60 else mode_name[:57] + "..."
        out.append((f"#{n}", rpn, klass_title, short_name, why))
    return out

TOP_PRIORITIES = compute_top_priorities(MODES, PRIORITY_WHY)

# ============================================================================
# Render
# ============================================================================

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H), dpi=DPI)
fig.patch.set_facecolor(BG_BLACK)
ax.set_facecolor(BG_BLACK)
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.axis("off")

# ---- Title bar ----
title_y = FIG_H - 0.35 - TITLE_H
ax.add_patch(Rectangle(
    (LEFT_MARGIN, title_y), USABLE_W, TITLE_H,
    facecolor=BG_PANEL, edgecolor=ARC_ORANGE, linewidth=2.5,
))
ax.add_patch(Rectangle(
    (LEFT_MARGIN, title_y), 0.10, TITLE_H,
    facecolor=ARC_ORANGE, edgecolor="none",
))
ax.text(LEFT_MARGIN + 0.30, title_y + TITLE_H * 0.62,
        TITLE, ha="left", va="center",
        fontsize=22, weight="bold", color=ARC_ORANGE, family="DejaVu Sans")
ax.text(LEFT_MARGIN + 0.30, title_y + TITLE_H * 0.25,
        SUBTITLE, ha="left", va="center",
        fontsize=12, color=TEXT_WHITE, family="DejaVu Sans")
ax.text(LEFT_MARGIN + USABLE_W - 0.20, title_y + TITLE_H * 0.50,
        "ELI Safety Blog  •  RPN = S × O × D  /  1–10 scale",
        ha="right", va="center",
        fontsize=10, color=TEXT_DIM, family="DejaVu Sans Mono")

# ---- Header row ----
hdr_y = title_y - 0.18 - HEADER_H
ax.add_patch(Rectangle(
    (LEFT_MARGIN, hdr_y), USABLE_W, HEADER_H,
    facecolor=BG_HEADER, edgecolor=BORDER, linewidth=1,
))
for i, (name, _) in enumerate(COLS):
    cx = col_x(i) + col_w(i) / 2
    ax.text(cx, hdr_y + HEADER_H / 2, name,
            ha="center", va="center",
            fontsize=10, weight="bold", color=TEXT_WHITE, family="DejaVu Sans")
    if i < len(COLS) - 1:
        sep_x = col_x(i) + col_w(i)
        ax.plot([sep_x, sep_x], [hdr_y, hdr_y + HEADER_H], color=BORDER, linewidth=0.8)

# ---- Data rows ----
row_top = hdr_y
for idx, m in enumerate(MODES):
    row_top -= ROW_H
    bg = BG_PANEL if idx % 2 == 0 else BG_DARK
    ax.add_patch(Rectangle(
        (LEFT_MARGIN, row_top), USABLE_W, ROW_H,
        facecolor=bg, edgecolor=BORDER, linewidth=0.5,
    ))

    rpn = m["s"] * m["o"] * m["d"]
    rpn_clr, rpn_class = rpn_color_class(rpn)

    for i, (col_name, _) in enumerate(COLS):
        cx_left = col_x(i)
        cw      = col_w(i)
        cy_mid  = row_top + ROW_H / 2

        if col_name == "#":
            ax.text(cx_left + cw/2, cy_mid, str(m["n"]),
                    ha="center", va="center",
                    fontsize=13, weight="bold", color=TEXT_WHITE, family="DejaVu Sans")

        elif col_name == "Failure Mode":
            wrapped = wrap_text(m["mode"], chars_for(cw, 9))
            ax.text(cx_left + 0.10, cy_mid, wrapped,
                    ha="left", va="center",
                    fontsize=9, weight="bold", color=TEXT_WHITE,
                    family="DejaVu Sans", linespacing=1.18)

        elif col_name == "Cause":
            wrapped = wrap_text(m["cause"], chars_for(cw, 8.5))
            ax.text(cx_left + 0.10, cy_mid, wrapped,
                    ha="left", va="center",
                    fontsize=8.5, color=TEXT_WHITE,
                    family="DejaVu Sans", linespacing=1.18)

        elif col_name == "Effect":
            wrapped = wrap_text(m["effect"], chars_for(cw, 8.5))
            ax.text(cx_left + 0.10, cy_mid, wrapped,
                    ha="left", va="center",
                    fontsize=8.5, color=TEXT_WHITE,
                    family="DejaVu Sans", linespacing=1.18)

        elif col_name in ("S", "O", "D"):
            val = m[col_name.lower()]
            ax.text(cx_left + cw/2, cy_mid, str(val),
                    ha="center", va="center",
                    fontsize=14, weight="bold", color=TEXT_WHITE, family="DejaVu Sans")

        elif col_name == "RPN":
            pad = 0.06
            ax.add_patch(Rectangle(
                (cx_left + pad, row_top + pad), cw - 2*pad, ROW_H - 2*pad,
                facecolor=rpn_clr, edgecolor="none",
            ))
            ax.text(cx_left + cw/2, cy_mid, str(rpn),
                    ha="center", va="center",
                    fontsize=18, weight="bold", color="#FFFFFF", family="DejaVu Sans")

        elif col_name == "Class":
            pad = 0.06
            ax.add_patch(Rectangle(
                (cx_left + pad, row_top + pad), cw - 2*pad, ROW_H - 2*pad,
                facecolor=rpn_clr, edgecolor="none",
            ))
            ax.text(cx_left + cw/2, cy_mid, rpn_class,
                    ha="center", va="center",
                    fontsize=12, weight="bold", color="#FFFFFF", family="DejaVu Sans")

        elif col_name == "Current Control":
            wrapped = wrap_text(m["control"], chars_for(cw, 8.5))
            ax.text(cx_left + 0.10, cy_mid, wrapped,
                    ha="left", va="center",
                    fontsize=8.5, color=TEXT_WHITE,
                    family="DejaVu Sans", linespacing=1.18)

        elif col_name == "Recommended Action":
            wrapped = wrap_text(m["action"], chars_for(cw, 9))
            ax.text(cx_left + 0.10, cy_mid, wrapped,
                    ha="left", va="center",
                    fontsize=9, color=TEXT_WHITE,
                    family="DejaVu Sans", linespacing=1.18)

        if i < len(COLS) - 1:
            sep_x = cx_left + cw
            ax.plot([sep_x, sep_x], [row_top, row_top + ROW_H], color=BORDER, linewidth=0.4)

# ---- Top-4 priorities summary ----
sum_top = row_top - 0.30
sum_height = SUMMARY_TITLE_H + PRIORITY_ROW_H * len(TOP_PRIORITIES) + 0.30
sum_bottom = sum_top - sum_height

ax.add_patch(Rectangle(
    (LEFT_MARGIN, sum_bottom), USABLE_W, sum_height,
    facecolor=BG_PANEL, edgecolor=ARC_ORANGE, linewidth=1.5,
))
title_bar_top = sum_top
ax.add_patch(Rectangle(
    (LEFT_MARGIN, title_bar_top - SUMMARY_TITLE_H), USABLE_W, SUMMARY_TITLE_H,
    facecolor=BG_HEADER, edgecolor="none",
))
ax.text(LEFT_MARGIN + 0.25, title_bar_top - SUMMARY_TITLE_H / 2,
        "TOP-4 RPN PRIORITIES",
        ha="left", va="center",
        fontsize=13, weight="bold", color=ARC_ORANGE, family="DejaVu Sans")

prow_top = title_bar_top - SUMMARY_TITLE_H - 0.05
for ref, rpn, klass, name, why in TOP_PRIORITIES:
    prow_top -= PRIORITY_ROW_H
    color, _ = rpn_color_class(rpn)
    ax.add_patch(Rectangle(
        (LEFT_MARGIN + 0.20, prow_top + 0.15), 0.15, PRIORITY_ROW_H - 0.30,
        facecolor=color, edgecolor="none",
    ))
    ax.text(LEFT_MARGIN + 0.55, prow_top + PRIORITY_ROW_H * 0.65,
            ref, ha="left", va="center",
            fontsize=14, weight="bold", color=ARC_ORANGE, family="DejaVu Sans")
    ax.text(LEFT_MARGIN + 1.00, prow_top + PRIORITY_ROW_H * 0.65,
            f"RPN {rpn}  /  {klass}",
            ha="left", va="center",
            fontsize=10, weight="bold", color=TEXT_DIM, family="DejaVu Sans Mono")
    ax.text(LEFT_MARGIN + 0.55, prow_top + PRIORITY_ROW_H * 0.30,
            name, ha="left", va="center",
            fontsize=11, weight="bold", color=TEXT_WHITE, family="DejaVu Sans")
    ax.text(LEFT_MARGIN + 9.80, prow_top + PRIORITY_ROW_H * 0.50,
            why, ha="left", va="center",
            fontsize=10, color=TEXT_WHITE, family="DejaVu Sans")

# ---- Footer ----
foot_y = sum_bottom - 0.25
ax.text(LEFT_MARGIN, foot_y,
        "RPN classes:  Critical ≥500  /  High 350–499  /  Medium 200–349  /  Low <200      "
        "ELI Safety Blog  •  safetyblog.eli-intelligence.com",
        ha="left", va="center",
        fontsize=9, color=TEXT_DIM, family="DejaVu Sans Mono")

# ============================================================================
# Save
# ============================================================================

plt.savefig(OUTPUT, facecolor=BG_BLACK, dpi=DPI, bbox_inches="tight", pad_inches=0.10)
print(f"Saved: {OUTPUT}")

# RPN distribution summary
dist = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
for m in MODES:
    rpn = m["s"] * m["o"] * m["d"]
    _, klass = rpn_color_class(rpn)
    dist[klass.title()] += 1
print(f"\nRPN distribution (n={len(MODES)} modes):")
for k, v in dist.items():
    print(f"  {k:9s}: {v}")

print(f"\nTop-4 priorities (auto-selected):")
for ref, rpn, klass, name, _ in TOP_PRIORITIES:
    print(f"  {ref}  RPN {rpn}  {klass:8s}  {name}")

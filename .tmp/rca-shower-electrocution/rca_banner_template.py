"""
ELI Safety Blog — Post Banner Renderer  (canonical v4)
Per-RCA CONFIG for: The Fatal Shower — Missing EGC Electrocution
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, FancyBboxPatch
from matplotlib import font_manager, rcParams
import matplotlib.image as mpimg
import os

# ====================================================================
# CONFIG — Shower Electrocution RCA
# ====================================================================

RCA_TYPE    = "INCIDENT RCA"
CRITICALITY = "L3"
CRIT_LABEL  = "CRITICAL"
PUB_DATE    = "2026-05-26"

TITLE       = ["MISSING EGC", "ELECTROCUTION"]
SUBTITLE    = "Rooftop water pump phase-to-ground fault"

FEATURE_STRIP = "WEEKLY INCIDENT RCA"

HAZARDS = [
    ("MISSING GROUNDING CONDUCTOR", "L3"),
    ("MOTOR INSULATION FAILURE",    "L2"),
    ("NO GFCI PROTECTION",          "L2"),
    ("UNQUALIFIED PERSONNEL",       "L1"),
]

CATEGORIES = "ELECTROCUTION  ·  GROUNDING  ·  MAINTENANCE  ·  CONTRACTOR SAFETY"

SYMBOL_PATH = "rca_symbol.png"

OUTPUT_FILE = "banner-shower-electrocution.png"

# ====================================================================
# ELI BRAND TOKENS
# ====================================================================

ELI_BLACK   = "#0D0F12"
ELI_DARK    = "#141720"
ELI_PANEL   = "#1A1E26"
ELI_CARD    = "#1F2430"
ELI_BORDER  = "#2A3040"
ELI_ACCENT  = "#E8680A"
ELI_AMBER   = "#F0A030"

CRIT_STYLES = {
    "L0": {"text": "#5DD470", "bg": "#17351E", "border": "#3DAA50", "label": "NORMAL"},
    "L1": {"text": "#E8C040", "bg": "#2F2509", "border": "#E0AC10", "label": "ADVISORY"},
    "L2": {"text": "#FF8030", "bg": "#2F1505", "border": "#E8680A", "label": "WARNING"},
    "L3": {"text": "#FF5555", "bg": "#2D0A0A", "border": "#CC2222", "label": "CRITICAL"},
}

ELI_WHITE   = "#F2EDE8"
ELI_MUTED   = "#8A909E"

# ====================================================================
# FONT STACK
# ====================================================================

FONT_DISPLAY = ["Bebas Neue", "DejaVu Sans Condensed", "Impact", "sans-serif"]
FONT_SUB     = ["Rajdhani", "DejaVu Sans Condensed", "sans-serif"]
FONT_BODY    = ["DM Sans", "DejaVu Sans", "sans-serif"]
FONT_MONO    = ["Share Tech Mono", "DejaVu Sans Mono", "monospace"]

def _check_fonts():
    installed = set(f.name for f in font_manager.fontManager.ttflist)
    brand_fonts = ["Bebas Neue", "Rajdhani", "DM Sans", "Share Tech Mono"]
    missing = [f for f in brand_fonts if f not in installed]
    if missing:
        print(f"[NOTE] Missing brand fonts, using fallbacks: {missing}")
    else:
        print("[OK] All ELI brand fonts available.")

# ====================================================================
# DRAWING HELPERS
# ====================================================================

def draw_circuit_grid(ax, x, y, w, h, spacing=0.55, opacity=0.07):
    nx = int(w / spacing) + 1
    for i in range(nx):
        ax.plot([x + i * spacing, x + i * spacing], [y, y + h],
                color=ELI_ACCENT, alpha=opacity, linewidth=0.6, zorder=1)
    ny = int(h / spacing) + 1
    for i in range(ny):
        ax.plot([x, x + w], [y + i * spacing, y + i * spacing],
                color=ELI_ACCENT, alpha=opacity, linewidth=0.6, zorder=1)

def draw_feature_strip(ax, y, height, text, date_str=None):
    ax.add_patch(patches.Rectangle((0.30, y), 15.7, height,
                                    facecolor=ELI_PANEL, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((0.30, y + height - 0.03), 15.7, 0.03,
                                    facecolor=ELI_ACCENT, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((0.30, y), 15.7, 0.02,
                                    facecolor=ELI_ACCENT, edgecolor='none', alpha=0.6, zorder=2))
    cy = y + height / 2
    ax.text(0.55, cy, text,
            ha='left', va='center',
            fontfamily=FONT_SUB, fontsize=18, fontweight='bold',
            color=ELI_WHITE, zorder=4)
    if date_str:
        ax.text(15.70, cy, date_str,
                ha='right', va='center',
                fontfamily=FONT_MONO, fontsize=16, fontweight='bold',
                color=ELI_WHITE, zorder=4)

def place_symbol(ax, image_path, cx, cy, target_height):
    if not os.path.exists(image_path):
        print(f"[WARN] Symbol image not found: {image_path}")
        return
    img = mpimg.imread(image_path)
    ih, iw = img.shape[:2]
    aspect = iw / ih
    target_width = target_height * aspect
    extent = (cx - target_width / 2, cx + target_width / 2,
              cy - target_height / 2, cy + target_height / 2)
    ax.imshow(img, extent=extent, zorder=3, interpolation='bilinear')

# ====================================================================
# RENDER
# ====================================================================

def render():
    _check_fonts()
    rcParams['font.family'] = FONT_BODY

    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
    ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis('off')

    ax.add_patch(patches.Rectangle((0, 0), 16, 9,
                                    facecolor=ELI_BLACK, edgecolor='none', zorder=0))
    draw_circuit_grid(ax, 0, 0, 16, 9, spacing=0.55, opacity=0.07)

    # Left full-height accent stripe
    ax.add_patch(patches.Rectangle((0, 0), 0.15, 9,
                                    facecolor=ELI_ACCENT, edgecolor='none', zorder=4))

    # Single header strip
    strip_h = 0.85
    strip_y = 9 - strip_h - 0.15
    draw_feature_strip(ax, strip_y, strip_h, FEATURE_STRIP, date_str=PUB_DATE)

    # Symbol
    symbol_height = 3.4
    place_symbol(ax, SYMBOL_PATH, cx=3.1, cy=4.5, target_height=symbol_height)

    # Title
    title_x = 6.3
    title_lines = TITLE if isinstance(TITLE, list) else [TITLE]
    n_lines = len(title_lines)
    title_fs = 48 if n_lines == 1 else 36
    line_h_units = 0.62 if n_lines > 1 else 0
    block_top_y = 5.8 + (n_lines - 1) * line_h_units / 2

    title_objs = []
    for i, line in enumerate(title_lines):
        ty = block_top_y - i * line_h_units
        t = ax.text(title_x, ty, line,
                ha='left', va='center',
                fontfamily=FONT_DISPLAY, fontsize=title_fs, color=ELI_WHITE, zorder=3)
        title_objs.append(t)

    # Dynamic underline
    fig.canvas.draw()
    max_w = 0
    for t in title_objs:
        bbox = t.get_window_extent(renderer=fig.canvas.get_renderer())
        bbox_data = bbox.transformed(ax.transData.inverted())
        max_w = max(max_w, bbox_data.width)

    underline_y = block_top_y - (n_lines - 1) * line_h_units - 0.55
    ax.add_patch(patches.Rectangle((title_x, underline_y), max_w, 0.06,
                                    facecolor=ELI_ACCENT, edgecolor='none', zorder=3))

    # Subtitle
    sub_y = underline_y - 0.45
    ax.text(title_x, sub_y, SUBTITLE.upper(),
            ha='left', va='center',
            fontfamily=FONT_SUB, fontsize=18, fontweight='semibold',
            color=ELI_ACCENT, zorder=3)

    # Hazards section
    haz_label_y = 3.0
    ax.text(title_x, haz_label_y, "[ IDENTIFIED HAZARDS ]",
            ha='left', va='center',
            fontfamily=FONT_MONO, fontsize=10, color=ELI_ACCENT, zorder=3)
    rule_w = min(10, 15.5 - title_x)
    ax.add_patch(patches.Rectangle((title_x, haz_label_y - 0.18), rule_w, 0.015,
                                    facecolor=ELI_BORDER, edgecolor='none', zorder=3))

    bullet_fs = 13
    row_h = 0.45
    n = len(HAZARDS)
    if n >= 4:
        col1 = HAZARDS[:(n + 1) // 2]
        col2 = HAZARDS[(n + 1) // 2:]
    else:
        col1 = HAZARDS
        col2 = []

    col1_x = title_x
    col2_x = title_x + 5.5
    first_row_y = 2.5

    for i, (hazard_text, _level) in enumerate(col1):
        y = first_row_y - i * row_h
        ax.add_patch(patches.Circle((col1_x + 0.12, y), 0.07,
                                     facecolor=ELI_ACCENT, edgecolor='none', zorder=4))
        ax.text(col1_x + 0.32, y, hazard_text,
                ha='left', va='center',
                fontfamily=FONT_MONO, fontsize=bullet_fs,
                color=ELI_WHITE, zorder=4)

    for i, (hazard_text, _level) in enumerate(col2):
        y = first_row_y - i * row_h
        ax.add_patch(patches.Circle((col2_x + 0.12, y), 0.07,
                                     facecolor=ELI_ACCENT, edgecolor='none', zorder=4))
        ax.text(col2_x + 0.32, y, hazard_text,
                ha='left', va='center',
                fontfamily=FONT_MONO, fontsize=bullet_fs,
                color=ELI_WHITE, zorder=4)

    # Footer
    ax.add_patch(patches.Rectangle((0.5, 0.7), 15, 0.015,
                                    facecolor=ELI_BORDER, edgecolor='none', zorder=3))
    ax.text(0.5, 0.38, f"CATEGORY:  {CATEGORIES}",
            ha='left', va='center',
            fontfamily=FONT_MONO, fontsize=9, color=ELI_MUTED, zorder=3)
    ax.text(15.5, 0.38, "SAFETYBLOG.ELI-INTELLIGENCE.COM",
            ha='right', va='center',
            fontfamily=FONT_MONO, fontsize=9, color=ELI_ACCENT,
            fontweight='bold', zorder=3)

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(OUTPUT_FILE, dpi=150, bbox_inches='tight',
                facecolor=ELI_BLACK, pad_inches=0)
    print(f"Saved: {OUTPUT_FILE}")

if __name__ == "__main__":
    render()

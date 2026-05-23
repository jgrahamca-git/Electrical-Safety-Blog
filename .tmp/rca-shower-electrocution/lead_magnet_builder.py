"""
Lead magnet builder — ELI Safety Blog
=====================================
Per-RCA CONFIG for: The Fatal Shower — EGC Continuity Verification Checklist
"""

import os
from weasyprint import HTML

# =============================================================================
# CONFIG — EGC Continuity & Bonding Verification Checklist
# =============================================================================

CRITICALITY = "L3"

CHECKLIST_TITLE    = "EGC Continuity & Bonding"
CHECKLIST_SUBTITLE = "Verification Checklist"
CHECKLIST_TAGLINE  = "A field checklist for verifying equipment grounding conductor integrity on motor and pump circuits"

LEAD_PARAGRAPH_1 = (
    "A water pump motor shorted to its casing. Because the Equipment Grounding "
    "Conductor was missing, the breaker never tripped — and the building's "
    "plumbing became energized at line voltage. A worker was fatally electrocuted "
    "in the shower. The EGC was the single point of failure that turned a "
    "routine motor fault into a fatality."
)

LEAD_PARAGRAPH_2 = (
    "Use this checklist during installation, commissioning, and preventive "
    "maintenance of any motor or pump circuit. Each item is a verifiable "
    "action — not a reminder to 'be safe.' Sign each line. File the completed "
    "checklist with the PM work order."
)

COMPANION_RCA_TITLE = "The Fatal Shower: When Missing Grounding Conductors Kill"
AUDIENCE            = "E&I technicians, maintenance electricians, contractors, PM planners"
STANDARDS_SHORTLIST = "NEC 250, CEC Section 10, NFPA 70E, OSHA 1910.304"

INTRO_PARAGRAPH = (
    "<strong>Use this checklist at every motor/pump installation and during "
    "annual preventive maintenance.</strong> Each item must be verified by a "
    "qualified person and recorded on the work order. If you cannot verify an "
    "item, do not energize the circuit."
)

CHECKLIST_SECTIONS = [
    (
        "1. Pre-Work Verification",
        [
            (
                "Circuit de-energized and LOTO applied.",
                "Lockout/tagout per site procedure before any EGC inspection or "
                "testing. Verify zero energy with rated voltage tester. Test-before-touch."
            ),
            (
                "As-built drawing reviewed for grounding path.",
                "Confirm the design specifies a dedicated EGC (not reliance on "
                "conduit alone). Identify EGC type and size on the drawing. Flag "
                "any circuit where no EGC is shown."
            ),
            (
                "Correct test instruments available.",
                "Low-resistance ohmmeter (or 4-wire milliohm meter) for EGC "
                "continuity. Insulation resistance tester (megger) for motor "
                "winding checks. Both instruments calibrated and in-date."
            ),
        ],
        [],
    ),
    (
        "2. Visual Inspection of EGC Installation",
        [
            (
                "Dedicated EGC is physically present in the raceway or cable.",
                "Visually confirm a green, green/yellow, or bare copper conductor "
                "is pulled. Do not accept 'conduit is the ground' in high-vibration "
                "or corrosive environments."
            ),
            (
                "EGC sized correctly per code.",
                "Verify conductor size against NEC Table 250.122 / CEC Table 16 "
                "for the overcurrent device rating protecting the circuit."
            ),
            (
                "EGC terminated at both ends — source and equipment.",
                "Confirm the EGC is landed on the ground bus at the panel/MCC and "
                "on the equipment grounding lug at the motor junction box. No "
                "floating, cut, or unterminated ends."
            ),
            (
                "Bonding jumpers intact at all metallic junctions.",
                "Check bonding jumpers across flexible conduit, expansion fittings, "
                "and isolation joints. Each jumper mechanically tight and corrosion-free."
            ),
        ],
        [],
    ),
    (
        "3. Continuity and Resistance Testing",
        [
            (
                "EGC end-to-end continuity verified with low-resistance ohmmeter.",
                "Measure from the equipment grounding lug at the motor to the "
                "ground bus at the source panel. Record the reading on the work order."
            ),
            (
                "Resistance reading within acceptable limits.",
                "Total EGC path resistance must provide a low-impedance fault "
                "return path capable of operating the overcurrent device. Flag "
                "any reading above the threshold below for investigation."
            ),
            (
                "Motor insulation resistance tested (megger).",
                "Measure phase-to-ground insulation resistance on the motor "
                "windings. Record reading and compare to baseline/trend. Flag "
                "any reading below 1 megohm for immediate investigation."
            ),
        ],
        [
            (
                "Pass criteria — EGC continuity",
                "End-to-end EGC resistance: <code>&lt; 1 &#8486;</code> measured "
                "with a low-resistance ohmmeter. For long runs or small conductors, "
                "calculate expected resistance from conductor tables and flag readings "
                "exceeding 150% of calculated value. Motor insulation resistance: "
                "<code>&gt; 1 M&#8486;</code> phase-to-ground (IEEE 43 minimum). "
                "Record all readings on PM work order for trending."
            ),
        ],
    ),
    (
        "4. Bonding of Metallic Systems",
        [
            (
                "Metallic water piping bonded per code.",
                "Verify bonding conductor from metallic water piping to the "
                "grounding electrode system per NEC 250.104(A) / CEC 10-406. "
                "This prevents plumbing from becoming an unintended fault path."
            ),
            (
                "Equipment in wet/damp locations has GFCI protection.",
                "Confirm GFCI protection is installed on circuits supplying "
                "equipment in wet or damp locations per NEC 210.8 / CEC 26-700. "
                "Test GFCI trip function."
            ),
            (
                "Structural steel and building metalwork included in bonding survey.",
                "Any metallic structure in contact with or near the equipment "
                "must be bonded to the grounding electrode system. Verify with "
                "continuity test."
            ),
        ],
        [],
    ),
    (
        "5. Post-Energization Verification",
        [
            (
                "No objectionable current on EGC after energization.",
                "With circuit energized and motor running, measure current on "
                "EGC with True-RMS clamp meter. Any current above normal leakage "
                "indicates a fault condition requiring immediate investigation."
            ),
            (
                "Touch potential spot-check at equipment frame.",
                "With motor running, measure voltage between equipment frame and "
                "nearest grounded structure. Any reading above 2V warrants "
                "investigation of bonding path integrity."
            ),
        ],
        [
            (
                "Pass criteria — post-energization",
                "EGC current: <code>&lt; 50 mA</code> under normal load (higher "
                "values indicate insulation degradation or wiring error). Touch "
                "potential: <code>&lt; 2 V</code> between equipment frame and "
                "grounded reference. Use True-RMS instruments only — averaging "
                "meters under-read distorted waveforms by 30–50%."
            ),
        ],
    ),
    (
        "6. Documentation and Sign-Off",
        [
            (
                "All readings recorded on PM work order.",
                "EGC resistance, insulation resistance, post-energization EGC "
                "current, and touch potential readings logged with date, "
                "instrument serial number, and technician name."
            ),
            (
                "Deficiencies flagged and tracked to closure.",
                "Any failed item generates a corrective action work order. "
                "Circuit remains de-energized (or flagged for immediate "
                "follow-up) until deficiency is resolved and re-verified."
            ),
        ],
        [],
    ),
]

REFERENCE_STANDARDS = [
    ("NEC Article 250",                  "Grounding and bonding — EGC sizing (Table 250.122), effective fault current path (250.4)"),
    ("NEC 250.104(A)",                   "Bonding of metallic water piping to grounding electrode system"),
    ("NEC 250.112 / 250.114",           "Grounding of specific equipment; equipment in wet or damp locations"),
    ("CEC Section 10",                   "Grounding and bonding — Rules 10-206, 10-400, 10-406"),
    ("CEC Section 26",                   "Installation of electrical equipment (motors)"),
    ("NFPA 70E Article 110.5",          "Electrical safety program requirements"),
    ("OSHA 1910.304(g)(5)",             "Permanent and continuous path to ground"),
    ("IEEE 43",                          "Recommended practice for testing insulation resistance of electric machinery"),
]

OUTPUT_PDF      = "egc-continuity-verification-checklist.pdf"
TEMPLATE_FILE   = "lead_magnet_template.html"
INTERIM_HTML    = "lead_magnet.html"

# =============================================================================
# RENDER (locked — do not edit per-RCA)
# =============================================================================

def render_checklist_sections(sections):
    html_blocks = []
    for heading, items, spec_blocks in sections:
        html_blocks.append(f'  <h2>{heading}</h2>\n')
        if items:
            html_blocks.append('  <div class="checklist">\n')
            for title, detail in items:
                html_blocks.append(
                    '    <div class="check-item">\n'
                    '      <div class="check-box"><span class="box"></span></div>\n'
                    '      <div class="check-text">\n'
                    f'        <strong>{title}</strong>\n'
                    f'        <span class="detail">{detail}</span>\n'
                    '      </div>\n'
                    '    </div>\n'
                )
            html_blocks.append('  </div>\n')
        for label, body in spec_blocks:
            html_blocks.append(
                '  <div class="spec-block">\n'
                f'    <strong>{label}</strong>\n'
                f'    {body}\n'
                '  </div>\n'
            )
    return ''.join(html_blocks)


def render_reference_standards(standards):
    return '\n      '.join(
        f'<li><strong>{code}</strong> — {purpose}</li>'
        for code, purpose in standards
    )


def build():
    if not os.path.exists(TEMPLATE_FILE):
        raise FileNotFoundError(
            f"Template not found: {TEMPLATE_FILE}. "
            f"Place lead_magnet_template.html in the same folder as this script."
        )

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    replacements = {
        "[[CRITICALITY]]":          CRITICALITY,
        "[[CHECKLIST_TITLE]]":      CHECKLIST_TITLE,
        "[[CHECKLIST_SUBTITLE]]":   CHECKLIST_SUBTITLE,
        "[[CHECKLIST_TAGLINE]]":    CHECKLIST_TAGLINE,
        "[[LEAD_PARAGRAPH_1]]":     LEAD_PARAGRAPH_1,
        "[[LEAD_PARAGRAPH_2]]":     LEAD_PARAGRAPH_2,
        "[[COMPANION_RCA_TITLE]]":  COMPANION_RCA_TITLE,
        "[[AUDIENCE]]":             AUDIENCE,
        "[[STANDARDS_SHORTLIST]]":  STANDARDS_SHORTLIST,
        "[[INTRO_PARAGRAPH]]":      INTRO_PARAGRAPH,
        "[[CHECKLIST_SECTIONS]]":   render_checklist_sections(CHECKLIST_SECTIONS),
        "[[REFERENCE_STANDARDS_LIST]]": render_reference_standards(REFERENCE_STANDARDS),
    }

    populated = template
    for marker, value in replacements.items():
        populated = populated.replace(marker, value)

    leftover = [m for m in replacements if m in populated]
    if leftover:
        raise RuntimeError(f"Unfilled markers remain in template: {leftover}")

    if "Disclaimer & limitation of liability" not in populated:
        raise RuntimeError(
            "Disclaimer block missing from rendered HTML. "
            "Do not deploy a lead magnet without the locked disclaimer block."
        )

    with open(INTERIM_HTML, "w", encoding="utf-8") as f:
        f.write(populated)

    HTML(INTERIM_HTML).write_pdf(OUTPUT_PDF)
    print(f"Rendered: {OUTPUT_PDF}")
    print(f"Interim HTML (debug): {INTERIM_HTML}")


if __name__ == "__main__":
    build()

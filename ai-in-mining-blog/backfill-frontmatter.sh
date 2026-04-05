#!/bin/bash
# ============================================================
# ELI Blog — Frontmatter Backfill Script
# Adds criticality + conclusion_state to all existing posts
#
# Run from your project root:
#   cd ~/Blog_EI_Safety/ai-in-mining-blog
#   chmod +x backfill-frontmatter.sh
#   ./backfill-frontmatter.sh
#
# The script uses Python to safely insert fields after the
# closing --- of the frontmatter only if not already present.
# Safe to run multiple times — skips files already patched.
# ============================================================

CONTENT_DIR="./src/content"

# ── HELPER FUNCTION ──
# Usage: patch_file <filepath> <criticality> <conclusion_state>
patch_file() {
  local file="$1"
  local criticality="$2"
  local conclusion="$3"

  # Skip if already has criticality field
  if grep -q "^criticality:" "$file"; then
    echo "  SKIP (already patched): $file"
    return
  fi

  # Use Python to insert after the closing --- of frontmatter
  python3 - "$file" "$criticality" "$conclusion" << 'PYEOF'
import sys

filepath = sys.argv[1]
criticality = sys.argv[2]
conclusion = sys.argv[3]

with open(filepath, 'r') as f:
    content = f.read()

lines = content.split('\n')

# Find the second --- (closing frontmatter delimiter)
dash_count = 0
insert_at = -1
for i, line in enumerate(lines):
    if line.strip() == '---':
        dash_count += 1
        if dash_count == 2:
            insert_at = i
            break

if insert_at == -1:
    print(f"  ERROR: Could not find frontmatter in {filepath}")
    sys.exit(1)

# Insert the new fields before the closing ---
new_lines = (
    lines[:insert_at] +
    [
        f'criticality: "{criticality}"',
        f'conclusion_state: "{conclusion}"',
        'agent_suggested: false',
        'editor_confirmed: true',
    ] +
    lines[insert_at:]
)

with open(filepath, 'w') as f:
    f.write('\n'.join(new_lines))

print(f"  PATCHED: {filepath}")
PYEOF
}

echo ""
echo "======================================================"
echo " ELI Frontmatter Backfill — Starting"
echo "======================================================"
echo ""

# ══════════════════════════════════════════════════════════
# INCIDENTS — All L3 Critical / hazard conclusion
# These are documented incidents with serious consequences
# ══════════════════════════════════════════════════════════
echo "── INCIDENTS (L3 / hazard) ──"

patch_file "$CONTENT_DIR/incidents/tingling-drill-rig.md"     "L3" "hazard"
patch_file "$CONTENT_DIR/incidents/tingling-drill-rig.mdx"    "L3" "hazard"

# Add any other incident files found automatically
for f in "$CONTENT_DIR/incidents/"*.{md,mdx}; do
  [ -f "$f" ] || continue
  patch_file "$f" "L3" "hazard"
done

echo ""

# ══════════════════════════════════════════════════════════
# SAFETY NEWS — L1 Advisory / neutral conclusion
# Product reviews and news are informational
# ══════════════════════════════════════════════════════════
echo "── SAFETY NEWS (L1 / neutral) ──"

patch_file "$CONTENT_DIR/safety-news/smart-ppe-voltage-sensing.md"   "L1" "neutral"
patch_file "$CONTENT_DIR/safety-news/smart-ppe-voltage-sensing.mdx"  "L1" "neutral"
patch_file "$CONTENT_DIR/safety-news/advanced-ngr-relays.md"         "L1" "neutral"
patch_file "$CONTENT_DIR/safety-news/advanced-ngr-relays.mdx"        "L1" "neutral"
patch_file "$CONTENT_DIR/safety-news/sample-product.md"              "L0" "neutral"
patch_file "$CONTENT_DIR/safety-news/sample-product.mdx"             "L0" "neutral"

# Catch any others
for f in "$CONTENT_DIR/safety-news/"*.{md,mdx}; do
  [ -f "$f" ] || continue
  patch_file "$f" "L1" "neutral"
done

echo ""

# ══════════════════════════════════════════════════════════
# SAFETY TOPICS — Individual assignments based on content
# Green/safe = correct practice topics
# Orange/hazard = hazard-focused topics
# ══════════════════════════════════════════════════════════
echo "── SAFETY TOPICS (individual assignments) ──"

# L0 / safe — correct practice, educational, grounding/bonding
patch_file "$CONTENT_DIR/safety-topics/lockout-tagout.md"                    "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/lockout-tagout.mdx"                   "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/master-lockbox-method.md"             "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/master-lockbox-method.mdx"            "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/preventing-ground-faults.md"          "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/preventing-ground-faults.mdx"         "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/test-before-touch.md"                 "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/test-before-touch.mdx"                "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/inspecting-ppe.md"                    "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/inspecting-ppe.mdx"                   "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/ten-foot-rule-mobile-equipment.md"    "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/ten-foot-rule-mobile-equipment.mdx"   "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/safety-plcs-and-architecture.md"      "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/safety-plcs-and-architecture.mdx"     "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/understanding-cat-ratings.md"         "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/understanding-cat-ratings.mdx"        "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/emergency-stop-testing.md"            "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/emergency-stop-testing.mdx"           "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/tryout-in-loto.md"                    "L0" "safe"
patch_file "$CONTENT_DIR/safety-topics/tryout-in-loto.mdx"                   "L0" "safe"

# L1 / neutral — advisory, awareness topics
patch_file "$CONTENT_DIR/safety-topics/complacency-trap.md"                  "L1" "neutral"
patch_file "$CONTENT_DIR/safety-topics/complacency-trap.mdx"                 "L1" "neutral"
patch_file "$CONTENT_DIR/safety-topics/identifying-frayed-cables.md"         "L1" "neutral"
patch_file "$CONTENT_DIR/safety-topics/identifying-frayed-cables.mdx"        "L1" "neutral"
patch_file "$CONTENT_DIR/safety-topics/normalizing-deviations-ppe.md"        "L1" "hazard"
patch_file "$CONTENT_DIR/safety-topics/normalizing-deviations-ppe.mdx"       "L1" "hazard"

# L2 / hazard — serious hazard topics, failure modes
patch_file "$CONTENT_DIR/safety-topics/arc-flash-boundaries.md"              "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/arc-flash-boundaries.mdx"             "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/first-60-seconds-arc.md"              "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/first-60-seconds-arc.mdx"             "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/limit-of-rubber-gloves.md"            "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/limit-of-rubber-gloves.mdx"           "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/lethal-myth-of-earth.md"              "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/lethal-myth-of-earth.mdx"             "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/ct-open-circuit-hazards.md"           "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/ct-open-circuit-hazards.mdx"          "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/vfd-dc-bus-discharge-times.md"        "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/vfd-dc-bus-discharge-times.mdx"       "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/motor-space-heater-hazards.md"        "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/motor-space-heater-hazards.mdx"       "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/backfed-control-transformers.md"      "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/backfed-control-transformers.mdx"     "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/aluminum-copper-terminations.md"      "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/aluminum-copper-terminations.mdx"     "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/intrinsic-safety-bypassing.md"        "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/intrinsic-safety-bypassing.mdx"       "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/dual-source-equipment.md"             "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/dual-source-equipment.mdx"            "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/multimeter-deadly-jack.md"            "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/multimeter-deadly-jack.mdx"           "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/bess-thermal-runaway.md"              "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/bess-thermal-runaway.mdx"             "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/solar-inverter-backfeed.md"           "L2" "hazard"
patch_file "$CONTENT_DIR/safety-topics/solar-inverter-backfeed.mdx"          "L2" "hazard"

# Catch any remaining safety topics not explicitly listed — default L1/neutral
for f in "$CONTENT_DIR/safety-topics/"*.{md,mdx}; do
  [ -f "$f" ] || continue
  patch_file "$f" "L1" "neutral"
done

echo ""
echo "======================================================"
echo " Backfill complete!"
echo " Review any SKIP messages above — those were already patched."
echo " Run: npm run dev"
echo " Check the homepage — criticality badges should now appear on cards."
echo "======================================================"
echo ""

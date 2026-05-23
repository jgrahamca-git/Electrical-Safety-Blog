# ELI Safety Blog — Skill Context

Condensed reference bundled with the eli-blog-assistant skill. The living project log lives at `C:\Users\jgrah\My Drive\01_ELI\ELI_Blog_Tracker.md`. Jason may paste or upload that file for detailed project work.

Last updated: 2026-04-26 (FMEA visual rendering standard merged in)

## Pipeline at a glance

- **Blog:** safetyblog.eli-intelligence.com (Astro + Netlify via GitHub)
- **Content AI:** Gemini + Antigravity (research, drafting, image generation, deploys)
- **Quality + Assets AI:** Claude (editorial, FMEA, banner, lead magnet)
- **Email:** MailerLite RSS automation (hourly polling)
- **Scheduling:** Zapier daily 5:00 AM EST build hook → Netlify rebuild
- **LinkedIn:** Bi-weekly via Python scripts (`post_to_linkedin.py`). OAuth token 60-day expiry.

## Workflow split

| Asset | Produced by | Phase |
|---|---|---|
| RCA narrative (MDX body) | Gemini | Draft |
| Editorial review of draft | Claude | Review |
| FMEA table PNG | Claude | Review |
| RCA banner PNG | Claude | Review |
| Lead magnet PDF | Claude | Review |
| Git commit + Netlify deploy | Gemini (Antigravity) | Deploy |

Gemini leaves placeholders in draft MDX for Claude-scope assets:
- `[FMEA section — Claude]`
- `[Lead magnet CTA — Claude]`

Claude replaces those placeholders during editorial review with real content and linked assets.

## Templates system
Installed at `C:\Users\jgrah\My Drive\01_ELI\07_Blog\templates\`:

| File | Purpose |
|---|---|
| `fmea_renderer.py` | FMEA table PNG generator |
| `fmea_hero_crop.py` | FMEA-to-hero crop (currently dormant) |
| `lead_magnet_template.html` | Field checklist PDF source |
| `rca_banner_template.py` | Banner with RCA symbol + hazards |
| `rca_symbol.png` | Fishbone/magnifier brand symbol (required by banner) |
| `preprocess_symbol.py` | Gemini symbol preprocessor |
| `README.md` | Templates documentation |

Use these templates — don't rebuild from scratch every week.

## Per-RCA workflow (the weekly loop)

1. Gemini generates draft MDX with placeholders for FMEA and lead magnet CTA
2. Claude reviews the draft:
   - Editorial pass (tone, terminology, technical accuracy)
   - Enforce 10-part structure (see below)
   - Flag any residency issues (blame-the-victim language, imprecise codes, missing systemic framing)
3. Claude builds FMEA by editing `fmea_renderer.py` CONFIG block
4. Claude builds banner by editing `rca_banner_template.py` CONFIG block
5. Claude builds lead magnet by copying `lead_magnet_template.html` and filling `[[...]]` markers, then rendering to PDF
6. Hand deliverables back to Gemini — updated MDX + FMEA PNG + banner PNG + checklist PDF
7. Gemini commits to Git and deploys after Jason's final sign-off

## 10-part Incident RCA structure (LOCKED)
Every Incident RCA uses exactly this structure:

1. **The Hook (Flashpoint)** — open on the moment of failure, not background
2. **The Setup** — context that makes the reader feel present
3. **The Breakdown** — chronological forensic sequence
4. **Interactive Quiz** — Astro `<Quiz>` component testing reader understanding
5. **The RCA** — direct cause AND systemic/human cause (never blame the worker alone)
6. **Failure Modes and Effects Analysis (FMEA)** — embedded PNG via click-to-expand markdown pattern
7. **Codes & Standards** — specific references to CEC, NEC, CSA Z462, NFPA 70E, IEEE 142, etc.
8. **Lead Magnet CTA** — paragraph + link to the paired field checklist PDF
9. **Actionable Takeaways** — specific and implementable, not "be more careful"
10. **Closing Statement** — one-sentence systemic lesson

*(The earlier 7-part structure is legacy. All RCAs from April 2026 onward use the 10-part structure.)*

## FMEA scoring rubric (LOCKED)
Formula: `RPN = Severity × Occurrence × Detection` (1–10 scales)

- **Severity (S):** 1 = no effect → 10 = fatal/catastrophic
- **Occurrence (O):** 1 = extremely rare → 10 = frequent/inevitable
- **Detection (D):** 1 = certain catch → 10 = impossible to detect before failure

Score RPN before recommended controls. RPN color thresholds:

| Range | Class | Color |
|---|---|---|
| ≥ 500 | Critical | Deep red `#8B1A1A` |
| 350–499 | High | Orange `#C85A1A` |
| 200–349 | Medium | Amber `#D4A017` |
| < 200 | Low | Green `#2E7D32` |

Every FMEA has 8–12 failure modes spanning: equipment failure, procedural gaps, detection gaps, PPE/mitigation, human factors, system/control failures. Summary beneath the FMEA table lists top-4 RPN priorities.

## FMEA visual rendering standard (LOCKED — apply to every render)
Canonical FMEA layout. Every render — through `fmea_renderer.py` or any standalone renderer — must conform.

**Aspect ratio and dimensions:**
- 16:9 landscape — non-negotiable
- Default canvas: 32 × 18 inches at 110 DPI = 2750 × 1546 px (after `bbox_inches="tight"`, `pad_inches=0.10`)
- Background: ELI Black `#0D0F12`
- Margins: 0.4" left, 0.4" right (usable width 31.2")

**Title bar (0.95" tall):**
- Background ELI Panel; border Arc Orange 2.5pt; left accent stripe Arc Orange 0.10" wide
- Title: FAILURE MODES AND EFFECTS ANALYSIS, 22pt bold Arc Orange
- Subtitle: post-specific, 12pt Warm White
- Right meta: ELI Safety Blog • RPN = S × O × D / 1–10 scale, 10pt mono Text Dim

**Header row (0.50" tall):** 
background `#252A35`; column labels 10pt bold Warm White centered; separators 0.8pt Border.

**Column widths (sum 31.2"):**

| Column | Width | Alignment | Font |
|---|---|---|---|
| # | 0.45" | center | 13pt bold |
| Failure Mode | 4.30" | left | 9pt bold, wrap |
| Cause | 4.80" | left | 8.5pt, wrap |
| Effect | 4.10" | left | 8.5pt, wrap |
| S | 0.45" | center | 14pt bold |
| O | 0.45" | center | 14pt bold |
| D | 0.45" | center | 14pt bold |
| RPN | 1.00" | center | 18pt bold WHITE on solid colored fill |
| Class | 1.30" | center | 12pt bold WHITE on solid colored fill |
| Current Control | 5.20" | left | 8.5pt, wrap |
| Recommended Action | 8.70" | left | 9pt, wrap |

**Data rows (1.05" tall):**
- Alternating background: even rows ELI Panel `#1A1E26`, odd rows ELI Dark `#141720`
- Row separator 0.5pt Border; left text padding 0.10"; line spacing 1.18 for wrapped text
- Font: DejaVu Sans (falls back to brand fonts if installed)

**Critical rendering rule — RPN and Class cells:**
The RPN and Class cells BOTH get a solid color fill matching the RPN class threshold (full cell minus 0.06" padding). Text is rendered AFTER the fill in white `#FFFFFF` regardless of which class color sits underneath. White text reads cleanly against all four threshold colors. This visual is what lets a reader scan the right side of the table and see RPN distribution at a glance — do not change it.

**Top-4 priorities summary block** (sits below the table inside a single Arc Orange-bordered panel):
- Title bar 0.45", TOP-4 RPN PRIORITIES 13pt bold Arc Orange left-aligned
- Each priority row 0.70": color bar (0.15" wide) at left matching RPN class color; #N reference Arc Orange 14pt bold; RPN xxx / Critical Text Dim 10pt mono; mode name Warm White 11pt bold; one-line "why" Warm White 10pt at `x = LEFT_MARGIN + 9.80"`

**Footer:** 
single line, 9pt mono Text Dim — RPN classes: Critical ≥500 / High 350–499 / Medium 200–349 / Low <200      ELI Safety Blog • safetyblog.eli-intelligence.com

**Character-width calibration for `textwrap.wrap()`** (DejaVu Sans, with 0.20" cell padding subtracted):

| Font size | Chars per inch |
|---|---|
| 7.5pt | 12 |
| 8.0pt | 11 |
| 8.5pt | 10 |
| 9.0pt | 9.5 |
| 9.5pt | 9 |
| 10.0pt | 8.5 |

Formula: `chars = max(6, int((cell_width_inches - 0.20) * cpi))`

**Output:**
- Filename: `fmea-<short-slug>.png` (e.g. `fmea-triplen-neutral-overload.png`)
- Save: `plt.savefig(out, facecolor="#0D0F12", dpi=110, bbox_inches="tight", pad_inches=0.10)`
- Astro embed (click-to-expand): `[![alt text](../../assets/<filename>.png)](../../assets/<filename>.png)`

**Reference implementation:** `fmea_renderer.py` at `C:\Users\jgrah\My Drive\01_ELI\07_Blog\templates\` is the canonical renderer. CONFIG block at top is editable per RCA (POST_SLUG, SUBTITLE, MODES, PRIORITY_WHY); locked layout constants below the CONFIG block must not be changed without updating this section. Top-4 priorities are auto-derived from MODES by RPN (ties broken by mode order); PRIORITY_WHY supplies one-line rationale per top-4 mode.

## Brand system (summary — full reference is the source of truth)
Full reference: `C:\Users\jgrah\My Drive\01_ELI\01_Brand\Blog Colors and Design\ELI_Brand_System_Reference.md`
Jason should upload that reference at the start of any visual-work session. If he hasn't, ask for it before producing visual assets.

**Key tokens (summary):**

| Element | Hex |
|---|---|
| Arc Orange (primary accent) | `#E8680A` |
| Hazard Amber | `#F0A030` |
| ELI Black (page background) | `#0D0F12` |
| ELI Dark (section background) | `#141720` |
| ELI Panel (card background) | `#1A1E26` |
| Warm White (body text) | `#F2EDE8` |
| L0 Green | `#5DD470` |
| L1 Yellow | `#E8C040` |
| L2 Orange | `#FF8030` |
| L3 Red | `#FF5555` |

**Fonts (Google Fonts):**
- Bebas Neue — display / hero titles
- Rajdhani — headlines / labels
- DM Sans — body
- Share Tech Mono — badges / meta / code

Templates auto-fall-back to DejaVu variants if brand fonts aren't installed on Jason's machine.
Circuit grid texture: Arc Orange at 7% opacity, 55px grid (used on dark panels in the banner).

## Terminology locks (non-negotiable)
Full terminology reference in `editorial-standards.md`. Most common:
- "Objectionable current" — not "stray current" (IEEE 142 framing)
- "Equipment grounding conductor" (EGC) — not "ground wire" (except in direct quotes)
- "Ground-fault protection of equipment" (GFPE) — include NEC 230.95 / CEC 14-102 where relevant

## Critical editorial rules (summary)
Full rules in `editorial-standards.md`. Core principles:
- Never blame the victim. Root causes are systemic — management, design, training, procedure.
- Technical accuracy first. If unsure about a code reference, say so. Don't guess.
- Tone: journeyman teaching apprentice — not academic, not corporate safety department.
- Industrial/mining audience. Not residential, not general workplace safety.

## Content formats
**Daily Safety Topics (batched 7 per week)**
- Future-dated one per day for upcoming week
- Concise, educational, actionable takeaway
- Technical accuracy on codes references
- MDX format

**Incident RCAs (weekly, full 10-part structure)**
- Fatal or near-fatal documented incidents
- Paired with FMEA + banner + lead magnet
- Criticality level: typically L2 or L3
- Publishing cadence: Fridays

**LinkedIn cross-posts (bi-weekly)**
- Hook → Story → Lesson → Link → CTA → Tags
- 150–300 words for engagement
- Genuine discussion CTA (not yes/no)
- Link to specific blog post

## Content pillars
- Grounding and bonding (primary pillar)
- Arc flash and electrical safety
- Electrical safety culture and human factors
- Industrial AI and OT/SCADA safety
- Codes and standards updates

*Data center and BESS electrical safety is an underserved niche identified for expansion.*

## Published work to date (summary)
- **Silent Shock (Mar 2026, L3)** — trailing cable GFGC relay failure, fatal shock. Lead magnet (Trailing-Cable GFGC Inspection and Test Checklist) referenced but not yet built.
- **Bubbler Tube (Apr 13, 2026, L3)** — liquid nitrogen release, 6 fatalities. Uses manually-designed arc flash incident pyramid hero.
- **The Hidden Fault (Apr 20, 2026, L3)** — severing an active ground path. First full use of the template system (FMEA + lead magnet + banner). Complete 10-part structure.

## Guardrails
- Product ladder discipline: Blog is Tier 1 (YouTube Authority). Don't propose Tier 2 (digital products), Tier 3 (AI tools), or Tier 4 (ecosystem) work prematurely.
- Gemini writes; Claude builds supporting assets. Don't duplicate Gemini's work.
- Two approval gates are sacred. Never deploy without Jason's explicit sign-off at both.
- Visual work follows the brand reference. Ask Jason to upload if not present in session.
- Tracker lives at `01_ELI/ELI_Blog_Tracker.md` — append decisions and progress there, not in this skill file.

## Open items (as of 2026-04-19)
These are parked but actionable when time allows:
- Silent Shock lead magnet backfill
- RCA symbol bolt swap (replace `?` with lightning bolt in `rca_symbol.png`) — Canva job
- Astro static hero redesign (replace manually-designed hero with Gemini-designed version matching ELI branding)
- Silent Shock banner retrofit using template system
- Brand font install on Windows (Bebas Neue, Rajdhani, DM Sans, Share Tech Mono)

*See TODO in chat or ELI_Blog_Tracker.md for current status.*

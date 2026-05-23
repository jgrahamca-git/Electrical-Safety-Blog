# ELI Safety Blog — Editorial Standards

> Editorial reference bundled with the eli-blog-assistant skill. These standards are non-negotiable when reviewing RCAs, Daily Safety Topics, and LinkedIn posts. The living project log lives at `C:\Users\jgrah\My Drive\01_ELI\ELI_Blog_Tracker.md`.

**Last updated:** 2026-05-21

---

## Critical editorial rules (non-negotiable)

These rules apply to every piece of ELI content without exception:

1. **Never blame the victim.** Root causes are systemic — management failures, design gaps, training deficiencies, procedural breakdowns, fatigue, time pressure. A worker making a mistake is *always* a symptom, not the cause.
2. **Technical accuracy first.** If uncertain about a code reference or technical fact, flag the uncertainty — do not guess. Wrong CEC/NEC/IEEE/CSA numbers destroy credibility with the professional audience.
3. **Tone: experienced journeyman teaching an apprentice.** Not academic. Not corporate safety department. Not bureaucratic. The voice is practical, direct, and respectful.
4. **Respect for real people in real incidents.** Use anonymization where appropriate. Avoid sensationalism. The purpose is learning, not spectacle.
5. **Industrial and mining audience.** Not residential. Not general workplace safety. Not DIY. The reader is an E&I professional in heavy industry, pulp and paper, mining, forestry, water treatment, or power generation.

---

## Terminology locks (use these exact terms)

These are the correct terms — do not substitute variants:

| ✅ Correct | ❌ Incorrect | Why |
|---|---|---|
| Objectionable current | Stray current, leakage, parasitic current | IEEE 142 framing — "stray" is imprecise |
| Equipment grounding conductor (EGC) | Ground wire, green wire | Except in direct dialogue quotes |
| Ground-fault protection of equipment (GFPE) | GFCI, ground-fault detection | GFCI is residential; industrial uses GFPE (NEC 230.95 / CEC 14-102) |
| Earthing | Grounding to earth grid (ambiguous) | In grounding/bonding educational pieces, distinguish earthing (Xo to grid) from bonding |
| Bonding | Grounding equipment frames | Bonding = metal-to-metal equipotential; grounding = connection to earth |
| Residual current device (RCD) | GFCI (outside residential context) | Industrial terminology |
| Arc flash hazard | Arc flash accident, arc flash event | "Hazard" is the standard NFPA 70E / CSA Z462 term |
| Incident energy | Blast force, arc energy | IEEE 1584 terminology |

---

## 10-part Incident RCA structure (LOCKED)

Every Incident RCA uses exactly this structure. Do not merge, split, or reorder sections:

1. **The Hook (Flashpoint)** — Open on the moment of failure, not background. Reader should feel the incident happening before they know the context.
2. **The Setup** — Context that makes the reader feel present. Location, shift, workers involved, task. Avoid opinion — just facts.
3. **The Breakdown** — Chronological forensic sequence. Numbered events. What happened, in order, with technical precision.
4. **Interactive Quiz** — Astro `<Quiz>` component testing reader understanding of the physics/mechanism. One correct answer with a clear explanation that teaches the key concept.
5. **The RCA** — Must have BOTH:
   - **Direct cause** — the immediate technical/mechanical failure
   - **Systemic/Human cause** — management, training, procedural, or design failure that allowed the direct cause to occur
6. **Failure Modes and Effects Analysis (FMEA)** — Embedded PNG via click-to-expand markdown pattern. Produced by Claude using `fmea_renderer.py`.
7. **Codes & Standards** — Specific references with section numbers. Examples: CEC Section 10, NEC 230.95, CSA Z462, NFPA 70E, IEEE 142, IEEE 1584. Cite the standard, section number, and what it requires.
8. **Lead Magnet CTA** — Paragraph describing the paired field checklist, followed by download link. Produced by Claude using `lead_magnet_template.html`.
9. **Actionable Takeaways** — Specific and implementable. Not "be more careful." Items like "Verify EGC current with clamp meter before disconnection" are good. Items like "Follow safety procedures" are useless.
10. **Closing Statement** — One sentence that names the systemic lesson. This is the line people remember and share.

**Legacy:** The earlier 7-part structure (pre-April 2026) is deprecated. All RCAs from April 2026 onward use the 10-part structure.

---

## Daily Safety Topics

Daily Safety Topics follow a simpler format but still meet brand standards:

- **Format:** Concise, educational, actionable takeaway. Not preachy.
- **Batching:** 7 per batch, future-dated one per day for the upcoming week
- **Tone:** Same journeyman-to-apprentice voice as RCAs
- **Technical accuracy:** Same non-negotiable standards on codes/standards references
- **MDX format:** Astro content collection entry
- **Length:** 300–600 words typical
- **Structure:** Hook (1–2 sentences) → Key concept → Why it matters → Action step
- **Consistent voice across batch:** All 7 posts in a week should read like one person wrote them

---

## LinkedIn cross-posts

When reviewing LinkedIn drafts for the bi-weekly cross-post:

| Check | Standard |
|---|---|
| Hook (first line) | Must create curiosity or tension. If it doesn't stop the scroll, rewrite it. |
| Length | 150–300 words for LinkedIn algorithm engagement |
| Story compression | Enough to learn from, not enough to skip the blog post |
| Lesson | ONE clear takeaway, not a list |
| CTA question | Invites genuine professional discussion — not yes/no |
| Hashtags | Relevant to industrial E&I audience (#ElectricalSafety, #IndustrialSafety, #MiningSafety, #ArcFlash, etc.) |
| Link placement | Direct URL to the specific blog post |

When the hook is weak, provide 2–3 alternative opening lines. Don't just say "make the hook stronger."

---

## Code and standards references

Always cite specific sections. Common references Claude should recognize:

### Canadian
- **Canadian Electrical Code (CEC)** — CSA C22.1
  - Section 10: Grounding and bonding
  - Rule 10-208: Objectionable current
  - Rule 14-102: Ground-fault protection of equipment
  - Section 26: Installation of electrical equipment
- **CSA Z462** — Workplace Electrical Safety
- **CSA C22.2 No. 61010** — Safety requirements for electrical test equipment

### American
- **NFPA 70 (NEC)** — National Electrical Code
  - 230.95: Ground-fault protection of equipment (1000A+ services, 480V/277V)
  - 250: Grounding and bonding
  - 450: Transformers
- **NFPA 70E** — Standard for Electrical Safety in the Workplace
  - Article 130: Work involving electrical hazards
  - Table 130.7: PPE categories
- **NFPA 110** — Emergency and standby power

### IEEE
- **IEEE 142** ("Green Book") — Grounding of industrial and commercial power systems
- **IEEE 1584** — Guide for performing arc-flash hazard calculations
- **IEEE 242** ("Buff Book") — Protection and coordination

### International
- **IEC 60364** — Low-voltage electrical installations
- **IEC 61936-1** — Power installations exceeding 1 kV AC

When a draft references a code generally without a section number, flag it and request specificity.

---

## Victim-blaming detection checklist

Flag these patterns when editing:

- Language suggesting the worker "should have known better"
- Phrases like "careless," "negligent," "failed to follow procedure" without examining *why* the procedure failed to prevent this
- RCAs that stop at human error without asking why the human was in a position to err
- Implicit framing where the worker is the problem to be trained, rather than the system being the problem to be redesigned

Replace with systemic framing:
- "The procedure did not require verification before disconnection — a policy gap"
- "Fatigue from a 60-hour week eroded judgment — a workload issue"
- "No clamp meter was available at the MCC — a tooling gap"
- "The crew had not been trained on GFPE behavior under high-impedance faults — a training gap"

---

## Technical precision standards

When reviewing for technical accuracy, verify:

1. **Voltage references are correct** (e.g., 480V/277V not "480V/480V", 600Y/347V for Canadian industrial)
2. **Fault current behavior matches the system type** (grounded wye behaves differently than ungrounded delta)
3. **Protection device operation** is described correctly (GFPE vs. overcurrent vs. GFCI vs. AFCI — these are not interchangeable)
4. **Grounding hierarchy is correct:**
   - Earthing (Xo to ground electrode)
   - Bonding (equipment frame to EGC)
   - Equipotential (bonded metallic parts at same potential)
   - Residual current devices (protection against ground faults)
5. **PPE categorization** matches CSA Z462 / NFPA 70E tables, not outdated guidelines
6. **Arc flash calculations** reference IEEE 1584 methodology, not rules of thumb

---

## Editorial review workflow

When Jason shares a draft RCA for review, Claude works through:

1. **Structural check:** Does it hit all 10 parts? Are any collapsed or missing?
2. **Terminology check:** Search for deprecated terms (stray current, ground wire, GFCI when GFPE is meant)
3. **Victim-blame check:** Does every "worker error" have a matching systemic cause?
4. **Code accuracy check:** Are references specific (section numbers)? Are they correctly cited?
5. **Tone check:** Does it read as journeyman-to-apprentice, or has it drifted to academic or corporate?
6. **Quiz quality check:** Does the quiz explanation teach the correct physics?
7. **FMEA placeholder:** Is `[FMEA section — Claude]` present so Claude can build Section 6?
8. **Lead magnet placeholder:** Is `[Lead magnet CTA — Claude]` present so Claude can build Section 8?

Flag issues by severity:
- **Must fix** — factual errors, victim-blaming, missing structure, deprecated terminology
- **Should fix** — weak hooks, generic takeaways, unclear technical descriptions
- **Nice to have** — minor tone drift, opportunity to add a specific example

Offer specific rewrites for Must Fix and Should Fix items, not vague suggestions.

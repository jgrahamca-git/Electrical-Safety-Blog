# ELI safety blog project tracker

> **Purpose:** Single source of truth for the ELI Safety Blog and LinkedIn publishing pipeline. Feed this file to any AI (Claude, Gemini, ChatGPT) to give it full project context instantly.
>
> **Claude Reference Location:** `C:\Users\jgrah\My Drive\01_ELI\ELI_Blog_Tracker.md`
>
> **Update rules:**
> - **Section 1 (Snapshot):** Overwrite to reflect current state after any significant change
> - **Section 2 (Decision log):** Append only. Never edit old entries.
> - **Section 3 (Progress log):** Append only. Never edit old entries.
> - **Update trigger:** Workflow changes, milestones, new content format decisions, tool changes, or Sunday after weekly review

---

## 1. Current state snapshot

*Last updated: 2026-04-04*

### Project identity

- **Project name:** ELI Safety Blog
- **URL:** safetyblog.eli-intelligence.com
- **Owner:** Jason — Certified Electrical Technologist, industrial mining
- **Parent project:** ELI (Electric Learning Insights) — YouTube-first digital knowledge business
- **Product ladder position:** Tier 1 (YouTube Authority). Blog builds audience and content library for future Tier 2 digital products.
- **Time budget:** Part of the 5–10 hr/week ELI allocation. Sunday is the primary content review day.

### Tech stack

- **Site:** Astro 6.0.8 (SSG) + Netlify, deployed via GitHub. Astro 6.1.3 available — defer update until after Phase 6.
- **Dev server:** `npm run dev` from `~/Blog_EI_Safety/ai-in-mining-blog` (astro CLI not in PATH — always use npm)
- **Content AI:** Gemini + Antigravity (agentic research, drafting)
- **Image Gen:** Imagen 3 via Gemini ("nano banana") — hardware close-ups only, no humans. NotebookLM editorial infographic style — primary for all conceptual/framework content. EdrawMax — ALL electrical diagrams and schematics (no AI ever for circuit diagrams).
- **Quality AI:** Claude (research review, editorial, LinkedIn review, brand build)
- **Animation:** GSAP already installed — use for Phase 2 nav + card animations
- **CSS:** Tailwind active + ELI token file. Bear Blog base CSS present — test element overrides carefully.
- **Email:** MailerLite with RSS automation (hourly polling)
- **Scheduling:** Zapier free tier — daily 5:00 AM EST build hook to Netlify
- **LinkedIn:** Bi-weekly, automated via Zapier RSS integration.

### Current status

- **Blog:** Live and operational
- **Daily Safety Topics:** Publishing weekly (7 future-dated posts per Sunday push)
- **Incident RCAs:** Publishing as strong incidents are available (not weekly)
- **Email automation:** MailerLite RSS polling active
- **Zapier metronome:** Daily build hook active (5:00 AM EST)
- **LinkedIn:** Bi-weekly cross-posting active
- **Subscriber count:** [3]
- **Total posts published:** [31]
- **Brand build plan:** Phase 01 ACTIVE (started 2026-04-04) — 6 phases, 27 tasks

### Phase 01 task status

| Task | Status | Notes |
|------|--------|-------|
| 1. Save brand decisions to context | ✅ DONE | Tracker updated both Windows + Ubuntu. Brand PDFs created. |
| 2. Export brand board as PDF | ✅ DONE | v1 + v2 PDFs created — save to Design and update to blog folder |
| 3. Add Google Fonts to BaseLayout.astro | ⏳ PENDING | Not yet started |
| 4. Create eli-tokens.css | ✅ DONE | File at src/styles/eli-tokens.css. Import added to global.css line 7. Dev server confirmed clean. |
| 5. Update favicon, meta tags, OG image | ⏳ PENDING | Blocked — need PNG 512×512 transparent bg export from Photoshop PSD |
| 6. Update PRODUCE agent 3-output spec | ⏳ PENDING | Not yet started |

### Weekly cycle (Sunday)

1. Gemini researches 10 safety topics/incidents
2. Jason reviews, selects topics
3. Gemini drafts 7 future-dated Daily Safety Topics
4. Gemini drafts Incident RCAs when strong incidents are available
5. Claude reviews drafts (quality, technical accuracy, editorial standards)
6. Jason approves at Gate 1 (content + criticality + conclusion_state fields confirmed, editor_confirmed flipped to true)
7. Approved .mdx files saved locally
8. Jason pushes batch to GitHub
9. Zapier triggers daily Netlify rebuilds → one post unlocks per day
10. MailerLite picks up new post via RSS → emails subscribers

### Bi-weekly cycle (LinkedIn)

1. PRODUCE agent generates LinkedIn draft as part of same post run (no separate session)
2. Claude reviews for engagement quality at Gate 1 alongside post draft
3. Jason approves at Gate 2
4. Zapier automatically broadcasts new blog URLs via RSS feed (or Jason copy-pastes approved text block)

### PRODUCE agent — single-run output spec (updated 2026-04-04)

Every PRODUCE agent run outputs THREE deliverables reviewed together at Gate 1:

**Output 1: Post Draft**
- Full MDX content per content format
- `criticality` suggestion: L0 | L1 | L2 | L3 with one-line rationale
- `conclusion_state` suggestion: safe | hazard | neutral with one-line rationale
- `editor_confirmed: false` — Jason flips to true at Gate 1
- Imagen 3 prompt for thumbnail (hardware only, no humans, no connections)

**Output 2: SEO Block**
- `seoTitle` — 60 chars max
- `metaDescription` — 155 chars max
- `primaryKeyword` — one exact-match phrase
- `longTailKeywords` — 5 phrases, industrial/technical audience
- `slug` recommendation
- `heroImageAlt` — descriptive, keyword-rich

**Output 3: LinkedIn Draft**
- Hook line (scroll-stopper — curiosity or tension)
- Setup — 3 lines of incident/topic context
- Core failure or lesson
- One clear takeaway
- CTA question — invites professional discussion, not yes/no
- Blog link placeholder
- 5 relevant hashtags

### MDX frontmatter schema (updated 2026-04-04)

```yaml
---
title: "..."
description: "..."
pubDate: "YYYY-MM-DD"
category: "incidents" | "safety-topics" | "safety-news"
tags: ["tag1", "tag2"]
image: "./eli-[category]-[L0-3]-[slug].jpg"
# Agent-suggested — Jason confirms at Gate 1
criticality: "L0" | "L1" | "L2" | "L3"
conclusion_state: "safe" | "hazard" | "neutral"
agent_suggested: true
editor_confirmed: false
# SEO fields
seoTitle: "..."
metaDescription: "..."
primaryKeyword: "..."
---
```

### MDX body formatting rules

- **NO H1 Titles in Body:** Since the Astro layout auto-renders the post title directly from the frontmatter, the generated MDX body content **MUST NOT** include the H1 `# Title`. The MDX should start directly with the first section heading (e.g., `### 1. Introduction` or `### 1. The Flashpoint`).

### ELI brand system (locked 2026-04-04)

**Colors:**
- Void Black `#0D0F12` — primary background
- Arc Orange `#E8680A` — primary brand accent + L2 Warning status
- Hazard Amber `#F0A030` — secondary accent / L1 Advisory
- System Green `#5DD470` — L0 Normal / safe-state badges / correct practice conclusions
- Fault Red `#FF5555` — L3 Critical / incident RCAs only
- Warm White `#F2EDE8` — body text
- Muted `#8A909E` — metadata / secondary text

**Color rule:** Green = status/safe-state only (never decorative). Orange = brand + L2. Red = L3 incidents only.

**Typography:**
- Display: Bebas Neue (hero titles)
- Headlines: Rajdhani 700 (section titles, card headlines)
- Subheadings: Rajdhani 500 (labels, categories)
- Body: DM Sans 300/400 (article text)
- Mono: Share Tech Mono (code, badges, standards codes)

**Criticality scale:**

| Level | Label | Color | Use |
|-------|-------|-------|-----|
| L0 | Normal | Green #5DD470 | Educational, no active hazard, correct practice topics |
| L1 | Advisory | Yellow #E8C040 | Near-miss, equipment damage, caution |
| L2 | Warning | Orange #FF8030 | Serious injury potential — arc flash, shock |
| L3 | Critical | Red #FF5555 | Fatality, catastrophic failure, major RCA |

**conclusion_state logic:**
- `safe` — Post concludes with confirmed correct/protected practice. Green takeaway badge.
- `hazard` — Post concludes with failure mode or do-not-do warning. Red takeaway badge.
- `neutral` — Informational, standards reference, product overview. Gray badge.

**Category badge colors:**
- Grounding / Bonding / LOTO / Zero Energy → Green (safe-state by nature)
- Arc Flash / High Voltage / Shock Risk → Orange
- Incident RCA / Fatality → Red
- Controls / Instrumentation / VFD → Neutral gray
- Standards / Codes (CEC, NFPA, IEC) → Blue
- Near-Miss / Advisory → Yellow

### Image generation — hard rules (locked 2026-04-04)

| Content Type | Tool | Rule |
|---|---|---|
| Incident RCA | NotebookLM editorial | Fault sequence / cause-effect diagram |
| Grounding / Bonding | EdrawMax | Jason draws it — no AI |
| Protection Systems | EdrawMax | Jason draws it — no AI |
| Controls / Instrumentation | EdrawMax | Jason draws it — no AI |
| Arc Flash | Imagen 3 | Hardware close-up — NO humans, NO connections |
| LOTO / Safe Work | NotebookLM editorial | Conceptual diagram only |
| PPE / Human in context | Real Photo | Licensed stock or field photo |
| Safety News / Products | Imagen 3 | Product on dark surface — NO hands |
| ANY circuit diagram | NEVER AI | EdrawMax only, always |
| ANY human using a tool | NEVER AI | Real photo only, always |
| ANY meter display | NEVER AI | AI meter readings are always wrong |
| ANY wiring schematic | NEVER AI | AI produces incorrect topology |

**Fallback Images:**
- `src/assets/category-safety-news.jpg` — Use for safety news posts that lack a specific image.

**Image naming convention:** `eli-[category]-[L0-3]-[slug].jpg`
Example: `eli-grounding-L0-bonding-busbar.jpg`

**Imagen 3 prompt rule:** Physical descriptors only — "close-up of a copper bonding busbar, surface oxidation, single warm sidelight from left, dark background." Never topology, never connections, never people.

**Post-processing (all image types):** Apply in Canva — darken to 60% brightness, warm orange color grade, circuit grid overlay at 8% opacity, vignette.

**EdrawMax ELI color palette:**
- Background: #0D0F12 · Normal path: #5DD470 · Fault path: #FF5555 · Active/live: #E8680A · Neutral: #8A909E

**Important image asset note:** Existing assets in src/assets/ have inconsistent naming (spaces, mixed case). Apply new naming convention to NEW images only — do NOT rename existing files as it will break current post image references.

### Brand build plan — 6 phases (started 2026-04-04)

| Phase | Scope | Status |
|-------|-------|--------|
| 01 | CSS tokens, Google Fonts, favicon/OG, PRODUCE agent 3-output update | **Complete** |
| 02 | Astro components — Zod schema, CriticalityBadge, ConclusionBadge, CategoryBadge, PostCard, Nav rebuild | **Complete** |
| 03 | Image pipeline — Imagen 3 prompts, NotebookLM scope, Canva template, prompt library doc | Pending |
| 04 | SEO — keyword universe, JSON-LD schema, SEO frontmatter fields in Astro | Pending |
| 05 | LinkedIn — Canva graphic templates (4 criticality variants), post copy templates, scheduling | Pending |
| 06 | Agent config — update PRODUCE + TRIAGE prompts, Netlify editor_confirmed build guard | Pending |

Total: 27 tasks · ~36 hours

### Content formats

**Daily Safety Topics:** 7 per batch, future-dated (Mon–Sun). Concise, educational, actionable. `.mdx` format with Astro frontmatter.

**Incident RCAs (strict 6-part narrative):**
1. Safety Hook Title (frontmatter)
2. The Hook (Flashpoint) — moment of failure
3. The Setup — context
4. The Breakdown — technical sequence
5. Interactive Quiz Component (Astro/MDX)
6. The RCA — direct AND systemic causes
7. Actionable Takeaways

**LinkedIn posts:** 150–300 words. Hook → Setup (3 lines) → Core Failure → Takeaway → Blog Link → CTA Question → Tags. Bi-weekly cadence tied to RCA publication. Generated by PRODUCE agent in same run as post draft.

### Editorial standards

- Never blame the victim. Root causes are systemic — management failures, design gaps, training deficiencies, procedural breakdowns.
- Technical accuracy on all code/standard references (CEC, NEC, CSA Z462, NFPA 70E, IEC)
- Tone: experienced journeyman teaching an apprentice — not academic, not corporate safety department
- Real incidents handled with respect for people involved
- Industrial/mining audience — not residential/consumer
- **Scope:** Incidents and topics do NOT have to be strictly personnel hazards (shocks/arc flashes). They can and should equally cover massive equipment damage, downtime triggers, and industrial fires.

### Content pillars

1. Grounding and bonding (primary — Jason's core expertise)
2. Arc flash and electrical safety
3. Electrical safety culture and human factors
4. Industrial AI and OT/SCADA safety
5. Codes and standards updates (CEC, NEC, ISA, IEC)

### Blockers and open questions

- [x] Confirm Astro version (4.x or 5.x) — Confirmed Astro v6.0.4
- [x] Confirm global CSS file path and BaseLayout.astro location — Confirmed in Phase 01/global.css
- [x] Confirm BaseLayout.astro location — confirmed at src/layouts/
- [ ] Export ELI logo PNG 512×512 transparent bg from Photoshop PSD — needed for favicon + OG image (Task 5)
- [ ] Add Google Fonts link tag to BaseLayout.astro (Task 3)
- [ ] Update PRODUCE agent with 3-output spec (Task 6)
- [ ] Subscriber count needs to be kept current here
- [ ] Verify Zapier automation correctly pulled this week's RSS feed on publishing day
- [x] Provide Gemini with the small weekly incident image (for the blog post header/preview)
- [x] Provide Gemini with the high-res GFGC FMEA table image for the Astro popout
- [x] Create the MailerLite automation hook to send the GFGC Checklist PDF to new subscribers
- [ ] No content calendar beyond the current weekly cycle
- [ ] **Future Feature (Gamification):** Implement backend tally logic for Astro `<Quiz />` components to track user scores. Build a public Leaderboard that posts user names and high scores to heavily drive engagement over time.

---

## 2. Decision log

*Append new entries at the top. Format: date, decision, rationale, what it replaced.*

### 2026-04-04 — PRODUCE agent expanded to 3-output single run

- **Decision:** PRODUCE agent now outputs three blocks per run: (1) post draft with criticality + conclusion_state field suggestions, (2) SEO block (title tag, meta desc, primary KW, 5 long-tail KWs, slug, alt text), (3) LinkedIn draft (hook, setup, failure, takeaway, CTA, hashtags). All three reviewed together at Gate 1.
- **Rationale:** Reduces separate Claude sessions per post from 3 to 1. LinkedIn and SEO work is downstream of post content — same context window produces better alignment between post, distribution copy, and search targeting.
- **Replaced:** SEO and LinkedIn drafts done as separate sessions after post approval.

### 2026-04-04 — MDX frontmatter — criticality + conclusion_state + SEO fields added

- **Decision:** Added `criticality` (L0/L1/L2/L3), `conclusion_state` (safe/hazard/neutral), `agent_suggested`, `editor_confirmed`, `seoTitle`, `metaDescription`, `primaryKeyword` to all post frontmatter. PRODUCE and TRIAGE agents auto-suggest criticality and conclusion_state with rationale. Jason confirms by flipping `editor_confirmed: true` at Gate 1.
- **Rationale:** Astro components read frontmatter and render badges automatically — no manual color decisions. Agent classification reduces cognitive load at review. SEO fields ensure every post is search-optimized at publish, not retroactively. Zod schema validation at build time prevents unconfirmed posts going live.
- **Replaced:** Manual badge assignment, no SEO field structure, no machine-readable criticality data.

### 2026-04-04 — Image generation hard rules locked

- **Decision:** Three-tool image hierarchy: NotebookLM editorial (primary, all conceptual content), Imagen 3 via Gemini "nano banana" (hardware close-ups only, zero human presence), EdrawMax (all circuit diagrams — no AI ever), Real Photos (any human-in-context). Hard rule: no AI for circuit diagrams, schematics, one-line diagrams, meter displays, or humans using tools.
- **Rationale:** AI generators produce electrically incorrect circuit diagrams that look plausible but contain topology errors that destroy credibility with the E&I tech audience. Hands/tools/meter displays also fail consistently across all AI tools. EdrawMax already owned and optimal for electrical symbol depth.
- **Replaced:** Ad-hoc image tool selection per post. Previous plan included Midjourney — replaced by Imagen 3 via existing Gemini subscription.

### 2026-04-04 — ELI brand system v2 locked

- **Decision:** Full brand system locked — color palette, typography stack (Bebas Neue/Rajdhani/DM Sans/Share Tech Mono), industrial criticality scale (Green L0/Yellow L1/Orange L2/Red L3), category badge color rules, image post-processing protocol. Green expanded beyond L0 status to include validated safe-state practice categories (Grounding, LOTO, Zero Energy, Correct Practice conclusions).
- **Rationale:** Blog had no coherent visual system. Brand consistency is prerequisite for audience growth and LinkedIn distribution effectiveness. Industrial criticality color language (green→yellow→orange→red) leverages existing mental models of E&I tech audience from HMI/DCS/SCADA work.
- **Replaced:** Ad-hoc visual decisions per post. No token file, no reusable component library.

### 2026-04-04 — EdrawMax retained as sole diagram tool

- **Decision:** Keep Wondershare EdrawMax for all electrical diagram work. Draw.io and Lucidchart evaluated and rejected.
- **Rationale:** EdrawMax has 26,000+ industrial-standard symbols including IEC 60617, IEEE electrical, and P&ID libraries. Jason already owns the tool and has muscle memory. Lucidchart is general-purpose with no deep electrical symbol library. Draw.io has performance issues on complex diagrams.
- **Replaced:** Proposed evaluation of draw.io (free tier). No migration — EdrawMax already optimal.

### 2026-03-26 — Standalone blog tracker created

- **Decision:** ELI Blog Tracker lives as a standalone markdown file in `01_ELI/`, separate from the Claude skill. Same update rules as the PKA Project Tracker.
- **Rationale:** Embedding the tracker inside the skill's reference file required re-packaging the skill on every update. A standalone file in Drive matches the PKA pattern and is editable anytime, portable to any AI.
- **Replaced:** Initial plan to embed tracker in the eli-blog-assistant skill's `references/blog-context.md`.

### 2026-03-26 — Separate skill for blog pipeline

- **Decision:** Created eli-blog-assistant skill for Claude, separate from pka-project-assistant. Claude's role: quality review of Gemini's research output, editorial on blog drafts, LinkedIn post review, and project tracking.
- **Rationale:** Blog pipeline is Gemini-primary with Claude as quality reviewer. PKA is Claude-primary with Gemini as complement. Different workflows, tools, outputs, and cadence need separate skills to avoid routing confusion.
- **Replaced:** No prior skill. Blog work was managed ad-hoc across Gemini and Claude sessions.

### Pre-tracker decisions (recorded retroactively)

- **Astro + Netlify via Antigravity** chosen as blog platform (SSG for future-dating, Netlify for build hooks)
- **Zapier daily build hook** chosen for post scheduling (free tier, no server, stateless)
- **MailerLite RSS automation** chosen for email distribution (no manual sends, hourly polling)
- **Gemini + Antigravity** chosen as content generation engine (native Google ecosystem, 1M context, image sourcing)
- **Bi-weekly LinkedIn cadence** chosen (tied to RCA publication, not arbitrary schedule)
- **6-part RCA narrative structure** defined and locked

---

## 3. Progress log

*Append new entries at the top. Format: date, event type (milestone/progress/blocker/change), description.*

### 2026-04-05 — Phase 01 & 02 completion

- milestone | Brand Build Phase 01 & 02 Complete — Transformed site to dark industrial theme (eli-brand-redesign branch). Implemented CSS tokens, Astro Badges (Criticality, Conclusion, Category), rebuilt homepage, updated Zod schema, and backfilled all existing published posts with new frontmatter fields.

### 2026-04-04 — Phase 01 execution

- progress  | Phase 01 Task 1 DONE — brand decisions saved, ELI_Blog_Tracker updated both Windows + Ubuntu. ELI_Brand_Build_Session_Notes.md created and saved to Design and update to blog folder.
- progress  | Phase 01 Task 2 DONE — ELI_Brand_Board_v1.pdf + ELI_Brand_Board_v2_Criticality_ImageGen.pdf created and saved to Design and update to blog folder
- progress  | Phase 01 Task 3 PENDING — Google Fonts not yet added to BaseLayout.astro
- progress  | Phase 01 Task 4 DONE — eli-tokens.css created at src/styles/eli-tokens.css. Import line added to global.css. Dev server confirmed clean via npm run dev — no errors, site loads identically.
- progress  | Phase 01 Task 5 PENDING — blocked on PNG export of ELI logo from Photoshop PSD (512×512 transparent bg)
- progress  | Phase 01 Task 6 PENDING — PRODUCE agent update not yet started
- blocker   | Logo only exists as Photoshop PSD — need PNG 512×512 transparent bg for favicon + OG image. SVG conversion needed later for site header wordmark.
- observation | Astro confirmed 6.0.8. Content config at src/content.config.ts. Styles at src/styles/global.css. Layouts at src/layouts/.
- observation | GSAP already installed — use for Phase 2 nav hover sweep + card animations, do not add another animation library
- observation | Tailwind active in global.css — Phase 2 components can use Tailwind utilities alongside ELI tokens
- observation | Existing global.css uses RGB channel syntax for some vars (--black: 24,24,27) — check component usage before removing old vars in Phase 2
- observation | Bear Blog base CSS present — test all element-level overrides in dev server before committing
- observation | Astro 6.1.3 update available — deferred until after Phase 6 complete
- observation | Image asset naming inconsistent in src/assets/ — apply new convention to new images only, never rename existing files
- progress  | Rewrote image_generation_workflow.md to enforce locked image hard rules (zero humans, physical descriptors only, Imagen 3 for hardware, NotebookLM for conceptuals)
- progress  | Selected 7 safety topics for upcoming week (Dual-Source Equip, Multimeter Jacks, PPE Deviations, Tryout, BESS Stranded Energy, Solar Inverter Backfeed)
- progress  | Created image_generation_workflow.md to formalize the Gemini + Nano Banana (Imagen 3) image generation pipeline
- milestone | ELI brand system v2 locked — color palette, typography, criticality scale, image routing hard rules
- milestone | PRODUCE agent 3-output spec defined — post draft + SEO block + LinkedIn draft per run
- milestone | MDX frontmatter schema updated — criticality, conclusion_state, editor_confirmed, SEO fields
- milestone | Image hard rules locked — EdrawMax for all circuits, no AI for humans/meters/schematics
- milestone | EdrawMax confirmed as sole diagram tool — draw.io and Lucidchart evaluated and rejected
- progress  | Brand build plan initiated — 6 phases, 27 tasks, ~36 hrs. Phase 01 ACTIVE.
- progress  | ELI Blog Tracker updated with all 2026-04-04 decisions

### 2026-03-29

- progress | Generated deep-dive research on Functional Safety, SIL, 2oo3 Voting Logic, and AI implementations in E&I safety. Saved local artifact to `research/functional_safety_ai_research.md` to be used as foundational seed material for the next week's Safety Topics and RCAs.

### 2026-03-26

- milestone | ELI Blog Tracker created as standalone file in 01_ELI/
- milestone | eli-blog-assistant Claude skill built and packaged
- milestone | Full 4-phase blog pipeline documented (Content Gen → Deployment → Email → LinkedIn)

### Prior (pre-tracker)

- milestone | Blog live at safetyblog.eli-intelligence.com
- milestone | MailerLite email capture active with RSS automation
- milestone | Zapier daily build hook operational (5:00 AM EST)
- milestone | LinkedIn posting automated via Python scripts
- milestone | Gemini weekly research cycle established (10 topics, Sunday review)
- milestone | Incident RCA 6-part narrative structure defined
- milestone | Daily Safety Topics 7-post weekly batch format established

---

## 4. How to use this file with AI

Paste or upload this entire file at the start of any AI conversation about the ELI blog. Then ask your question.

**Example prompts after loading this file:**

- "Review this research output from Gemini — which topic should I pick for this week's RCA?"
- "Edit this blog draft for technical accuracy and editorial tone"
- "Review this LinkedIn post draft for engagement"
- "What content gaps do I have in my pillars?"
- "What's my current blog status and what should I focus on this Sunday?"
- "I changed X in the workflow — update the tracker"
- "Generate the SEO block and LinkedIn draft for this post"
- "Suggest criticality and conclusion_state for this post draft"

**When to update this file:**

- Sunday after weekly review (log what was published, any issues)
- When the workflow changes (new tool, new format, new cadence)
- When you make a decision (log it with rationale)
- When you hit a milestone (new subscriber threshold, N posts published, etc.)
- After each brand build phase completes

---

## 5. Topics Queue (Upcoming Posts)

These six topics are planned but not yet drafted. Antigravity must use the pre-approved `criticality` and `conclusion_state` metrics below:

| Topic | criticality | conclusion_state |
|-------|-------------|-----------------|
| Dual-Source Equipment hazards | L2 | hazard |
| Multimeter Deadly Jack mistake | L2 | hazard |
| Normalizing PPE deviations | L1 | hazard |
| Tryout step in LOTO | L0 | safe |
| BESS Thermal Runaway and Stranded Energy | L2 | hazard |
| Solar Inverter Backfeed — Grid vs Array isolation | L2 | hazard |

---

## 6. Topics log (previously covered)

*Do not propose these topics again for Daily Safety Topics or RCAs to prevent duplicates.*

- Identifying Frayed Cables (`identifying-frayed-cables.md`)
- Arc Flash Boundaries (`arc-flash-boundaries.md`)
- Understanding CAT Ratings (`understanding-cat-ratings.md`)
- The Complacency Trap (`complacency-trap.md`)
- Emergency Stop Testing (`emergency-stop-testing.md`)
- The First 60 Seconds of an Arc Flash (`first-60-seconds-arc.md`)
- Inspecting PPE (`inspecting-ppe.md`)
- Limits of Rubber Gloves (`limit-of-rubber-gloves.md`)
- Lockout Tagout Foundations (`lockout-tagout.md`)
- Master Lockbox Method (`master-lockbox-method.md`)
- Preventing Ground Faults (`preventing-ground-faults.md`)
- Safety PLCs and Architecture (`safety-plcs-and-architecture.md`)
- Ten Foot Rule for Mobile Equipment (`ten-foot-rule-mobile-equipment.md`)
- Test Before Touch (`test-before-touch.md`)
- Intrinsic Safety (IS) Barrier Bypassing (`intrinsic-safety-bypassing.md`)
- VFD DC Bus Discharge Wait Times (`vfd-dc-bus-discharge-times.md`)
- Motor Space Heater Hazards During LOTO (`motor-space-heater-hazards.md`)
- Current Transformer (CT) Open-Circuit Hazards (`ct-open-circuit-hazards.md`)
- The Lethal Myth of "Earth" as a Fault Return Path (`lethal-myth-of-earth.md`)
- Why Aluminum-to-Copper Terminations Burn Down Panels (`aluminum-copper-terminations.md`)
- The Hidden Danger of Back-fed Control Transformers (`backfed-control-transformers.md`)
- The Rise of Smart PPE and Voltage-Detecting Gloves (`smart-ppe-voltage-sensing.md`)
- The Silent Shock: Why a Tingling Drill Rig Is a Deadly Warning (`tingling-drill-rig.md`)
- Eliminating Trailing Cable Fires: Advanced NGR Relays for Mobile Mining Equipment (`advanced-ngr-relays.md`)
- Selected Product of the Week: Enhanced Arc Flash PPE (`sample-product.md`)
- The Hidden Danger of Dual-Source Equipment (`dual-source-equipment.md`)
- Multimeter Discipline: The "Deadly Jack" Mistake (`multimeter-deadly-jack.md`)
- Normalizing Deviations with PPE (`normalizing-deviations-ppe.md`)
- Understanding the "Tryout" in LOTO (`tryout-in-loto.md`)
- BESS: Thermal Runaway and Stranded Energy (`bess-thermal-runaway.md`)
- Solar Inverter Backfeed: Isolating the Grid vs The Array (`solar-inverter-backfeed.md`)
- Backfed Generator Shock (`backfed-generator-shock.mdx`)
- Induced Voltage Incident (`induced-voltage.mdx`)
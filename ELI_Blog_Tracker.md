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

*Last updated: 2026-03-26*

### Project identity

- **Project name:** ELI Safety Blog
- **URL:** safetyblog.eli-intelligence.com
- **Owner:** Jason — Certified Electrical Technologist, industrial mining
- **Parent project:** ELI (Electric Learning Insights) — YouTube-first digital knowledge business
- **Product ladder position:** Tier 1 (YouTube Authority). Blog builds audience and content library for future Tier 2 digital products.
- **Time budget:** Part of the 5–10 hr/week ELI allocation. Sunday is the primary content review day.

### Tech stack

- **Site:** Astro (SSG) + Netlify, deployed via GitHub
- **Content AI:** Gemini + Antigravity (agentic research, drafting, image sourcing)
- **Quality AI:** Claude (research review, editorial, LinkedIn review)
- **Email:** MailerLite with RSS automation (hourly polling)
- **Scheduling:** Zapier free tier — daily 5:00 AM EST build hook to Netlify
- **LinkedIn:** Bi-weekly, automated via Python scripts (`post_to_linkedin.py`, `check_linkedin_token.py`). OAuth token has 60-day expiry.

### Current status

- **Blog:** Live and operational
- **Daily Safety Topics:** Publishing weekly (7 future-dated posts per Sunday push)
- **Incident RCAs:** Publishing as strong incidents are available (not weekly)
- **Email automation:** MailerLite RSS polling active
- **Zapier metronome:** Daily build hook active (5:00 AM EST)
- **LinkedIn:** Bi-weekly cross-posting active
- **Subscriber count:** [3]
- **Total posts published:** [12]

### Weekly cycle (Sunday)

1. Gemini researches 10 safety topics/incidents
2. Jason reviews, selects topics
3. Gemini drafts 7 future-dated Daily Safety Topics
4. Gemini drafts Incident RCAs when strong incidents are available
5. Claude reviews drafts (quality, technical accuracy, editorial standards)
6. Jason approves at the gate
7. Approved .mdx files saved locally
8. Jason pushes batch to GitHub
9. Zapier triggers daily Netlify rebuilds → one post unlocks per day
10. MailerLite picks up new post via RSS → emails subscribers

### Bi-weekly cycle (LinkedIn)

1. Gemini scans `src/content/incidents/` for latest RCA
2. Gemini drafts LinkedIn post (Hook → Story → Lesson → Link → CTA → Tags)
3. Claude reviews for engagement quality
4. Jason approves at the gate
5. Token check script runs (`check_linkedin_token.py`)
6. Post script executes via LinkedIn API (`post_to_linkedin.py`)

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

**LinkedIn posts:** 150–300 words. Hook → Story → Lesson → Blog link → CTA question → Tags. Bi-weekly cadence tied to RCA publication.

### Editorial standards

- Never blame the victim. Root causes are systemic — management failures, design gaps, training deficiencies, procedural breakdowns.
- Technical accuracy on all code/standard references (CEC, NEC, CSA Z462, NFPA 70E, IEC)
- Tone: experienced journeyman teaching an apprentice — not academic, not corporate safety department
- Real incidents handled with respect for people involved
- Industrial/mining audience — not residential/consumer

### Content pillars

1. Grounding and bonding (primary — Jason's core expertise)
2. Arc flash and electrical safety
3. Electrical safety culture and human factors
4. Industrial AI and OT/SCADA safety
5. Codes and standards updates (CEC, NEC, ISA, IEC)

### Blockers and open questions

- [ ] Subscriber count and total posts published need to be recorded here
- [ ] LinkedIn OAuth token expiry tracking — when does the current token expire?
- [ ] Lead magnet strategy not yet defined (Gemini flagged this as next step)
- [ ] No content calendar beyond the current weekly cycle

---

## 2. Decision log

*Append new entries at the top. Format: date, decision, rationale, what it replaced.*

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

**When to update this file:**

- Sunday after weekly review (log what was published, any issues)
- When the workflow changes (new tool, new format, new cadence)
- When you make a decision (log it with rationale)
- When you hit a milestone (new subscriber threshold, N posts published, etc.)
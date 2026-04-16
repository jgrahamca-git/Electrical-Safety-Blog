# DIRECTIVE-01: INCIDENT RCA NARRATIVE STRUCTURE

## Purpose
This document strictly defines the storytelling architecture and formatting requirements the AI must use when generating any new **Incident Root Cause Analysis (RCA)** markdown files for the blog. It ensures high engagement, professional forensic tone, and maximum reader takeaways.

## 6-Part Narrative Format

Every Incident RCA must adhere rigidly to the following 6 chronological sections:

### 0. The Frontmatter (Safety Hook Title)
- **Format:** The `title` field in the frontmatter MUST be a "safety hook title" – punchy, immediate, and communicating the critical stakes of the incident. It should grab attention immediately.

### 1. The Hook (The Flashpoint)
- **Format:** A punchy 1-2 sentence opening that immediately describes the most dramatic moment of the incident. No gradual buildup to start; go straight to the impact. The impact does not always have to be a personal injury—it can be catastrophic equipment damage, a massive fire, or a narrow near-miss that caused heavy downtime.
- **Example:** "At 10:15 AM on a rainy Tuesday, what should have been a routine 480V breaker replacement turned into a catastrophic arc blast that hospitalized two senior electricians." OR "A loose aluminum termination went unnoticed for three years—until it melted through the 600V busbar and burned down the entire motor control center."

### 2. The Setup (The Context & Environment)
- **Format:** Rewind the clock to set the scene. Thoroughly detail the weather, the time of day, how long the shift had been running (analyzing fatigue factor), the exact equipment involved, and all the trades present on site.

### 3. The Breakdown (Chronological Forensics)
- **Format:** A step-by-step, urgent retelling of exactly how the incident unfolded. Highlight the very specific moment where a protocol was breached (e.g., LOTO was skipped, limits of approach were crossed, or a mechanical failure triggered). Maintain an objective yet fast-paced tone.

### 4. The Interactive Knowledge Check (Quiz Component)
- **Format:** Injected directly into the `.mdx` file immediately prior to the RCA section, you must include the custom `<Quiz />` Astro component.
- **Requirements:** 
  - Save the file as `.mdx` (not `.md`) to support Astro components natively.
  - Add `import Quiz from '../../components/Quiz.astro';` directly beneath the frontmatter.
  - Code the `<Quiz />` block with exactly 1 highly relevant multiple-choice question testing the reader's forensic awareness, 4 `options`, the `correctAnswerIndex` (0-3), and a comprehensive `explanation`.

### 5. The RCA (Root Cause Analysis)
- **Format:** A forensic breakdown divided clearly into two parts:
  - **Direct Cause:** The physical trigger (e.g., a dropped uninsulated wrench shorted the A and C phases).
  - **Systemic/Human Cause:** Why the operator made that specific choice (e.g., perceived time pressure from management, muscle-memory complacency, or completely skipped job briefings).

### 6. Relevant Codes & Standards
- **Format:** Explicitly reference and briefly explain the sections of relevant safety codes (e.g., NEC, CEC, NFPA 70E, OSHA, CSA Z462) that were violated or applied to the scenario. Mention roughly where they can be found.

### 7. The "Takeaway" (Actionable Conclusion)
- **Format:** Exactly 3 clear, highly actionable bullet points that the reader can implement on their own job site *today* to ensure this never happens to their crew. Do not write generic advice; be incredibly specific to the incident.

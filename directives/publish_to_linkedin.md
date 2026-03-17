# Directive: Publish to LinkedIn

**Goal:** Draft an optimized LinkedIn post for the newest incident article, present it to the user for review, and push it only after explicit human approval.

## Context
This workflow allows the user to publish a bi-weekly post linking back to the latest `Incident RCA` article on the blog. The post must be optimized for engagement and must require a human-in-the-loop approval before hitting the LinkedIn API.

## Inputs
- `src/content/incidents/` directory (to find the latest published `.mdx` file based on date).
- The `Ai-in-mining-blog` website URL to build the direct link (e.g., `https://eli-ei-safety.netlify.app/incidents/slug_name`).

## Workflow Steps

### 1. Identify the Latest Article
Examine the `src/content/incidents/` directory to pinpoint the most recently published incident based on the `pubDate` in the frontmatter.

### 2. Draft the LinkedIn Post
The Orchestrator will draft the LinkedIn post. This draft MUST follow these optimization guidelines:
*   **The Hook:** Start with a bold statement or question about the root cause (e.g., "Why did a 'dead' circuit almost cost a life?").
*   **The Story:** A brief, 2-3 sentence summary of the incident and the failure point.
*   **The Lesson:** The clear, actionable takeaway for electrical/controls professionals.
*   **Formatting:** Use line breaks (whitespace) to make it skimmable. Avoid 'wall of text'.
*   **The Link:** A clear call to read the full Root Cause Analysis on the blog, including the direct URL.
*   **Call to Action (CTA):** End with a question to encourage comments (e.g., "How does your site handle induced voltage checks?").
*   **Tags:** Include 3-5 highly relevant hashtags (e.g., `#ElectricalSafety`, `#RootCauseAnalysis`, `#LOTO`).

### 3. Human Review Step (CRITICAL)
Present the drafted post to the user via the chat UI.
**DO NOT proceed until the user explicitly approves the drafted text.** The user may request edits.

### 4. Execute the Python Script
Once the user approves the specific text, execute the deterministic `execution/post_to_linkedin.py` script.
- Ensure the `.env` file contains `LINKEDIN_ACCESS_TOKEN` and `LINKEDIN_AUTHOR_URN` (e.g. `urn:li:person:12345`).
- Pass the approved text and the URL as arguments to the script.

**Example execution:**
```bash
python execution/post_to_linkedin.py --text "Approved text here" --url "https://eli-ei-safety.netlify.app/incidents/induced-voltage/"
```

### 5. Verify and Annotate
If the script succeeds, inform the user that the post is live. If it fails, self-anneal (check token expiration, API formatting) and update this directive if you discover API changes.

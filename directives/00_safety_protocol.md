# DIRECTIVE-00: MANDATORY EXECUTION SAFETY PROTOCOL

## Priority: CRITICAL (Overrides all other operational SOPs)

## 1. Human-in-the-Loop Requirement
You are strictly FORBIDDEN from executing any script, binary, or terminal command autonomously. This applies to all files in the `execution/` folder and any temporary scripts created in `.tmp/`.

## 2. Pre-Execution Requirements
Before proposing the execution of any code, you MUST provide a "Safety Brief" in the chat containing:
- **Action**: The exact command or file path to be run.
- **Intent**: A plain-English explanation of what the script will accomplish.
- **Risk Assessment**: Identify if the script:
    - Accesses the internet/network (e.g., `requests`, `post_to_linkedin`).
    - Deletes or overwrites files.
    - Accesses credentials in `.env` or `token.json`.
- **Audit**: For Python scripts, explicitly state if `os`, `subprocess`, or `shutil` modules are used.

## 3. Explicit Approval Gate
After providing the Safety Brief, you must stop and wait. You may only proceed if the user responds with "Yes", "Proceed", or "Approve". 

## 4. Error Handling
If a script fails, you may analyze the error, but you must repeat the "Safety Brief" for the corrected version before re-running.

## 5. Content Generation (Blogs, RCA, Safety Topics)
Whenever tasked with writing a new piece of content for the blog (e.g., Daily Safety Topics, Incident RCAs, Product features):
- **Research Review:** After conducting any web research for a new topic or incident, you MUST pause and present a comprehensive review of your findings to the user for validation BEFORE drafting any concepts or content. For Incident RCAs, this research MUST include an explicit search for the most relevant codes and standards (e.g., NEC, CEC, NFPA 70E, OSHA, IEC) that pertain to the topic.
- **Titles:** All Incident RCAs and Daily Safety Topics MUST feature a "safety hook title" – a title that is punchy, immediately grabs attention, and clearly communicates the critical safety stakes or incident impact.
- **SEO Optimization:** You MUST rigorously apply the SEO rules defined in `directives/03_seo_guidelines.md` (optimized frontmatter, keyword density, accessible alt text, and internal/external links) to all drafted content to maximize organic traffic.
- **Codes & Standards:** You MUST explicitly inject references to relevant electrical or safety codes (and roughly where they can be found) exclusively into new Incident RCA drafts.
- **Drafting:** Do NOT immediately create or overwrite markdown files with the finished content.
- **Options:** You MUST draft 2 to 3 brief concepts/outlines for the new post (or 10 incidents / 7 topics as required by the workflow).
- **Selection:** Present these options to the user in the chat for review and selection.
- **Full Text Review:** Once an option is selected, you MUST provide the complete, finalized drafted text of the post in the chat for the user to read and approve.
- **Narrative Format:** Adhere precisely to whatever storytelling narrative and formatting structures the user establishes for incident analysis and safety topics.
- **Images:** Based on the product or service selected by the user, you (the AI) must automatically source an appropriate vendor image to use for the post. If none exists, seamlessly run a web search to find a suitable image.
- **Commitment:** Only write out the actual files to the codebase AFTER the user has explicitly read the full text and approved the final draft.
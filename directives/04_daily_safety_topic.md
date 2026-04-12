# DIRECTIVE-04: DAILY SAFETY TOPIC OUTLINE TEMPLATE

## Purpose
This document defines the architecture and requirements for the AI when generating any new **Daily Safety Topic** markdown files for the blog. It ensures consistent structure, educational value, and strict adherence to electrical codes and standards.

## Daily Safety Topic Format
Daily Safety Topics are strictly educational and actionable posts designed to be concise and referenceable.

Every Daily Safety Topic should adhere to the following structure:

### 0. The Frontmatter
- **Format:** Standard `.mdx` frontmatter matching the Astro schema.
- **Safety Hook Title:** The `title` field MUST be a clear, engaging "safety hook title" that immediately communicates what the safety topic covers and why it matters.

### 1. Introduction & Context
- Introduce the topic quickly and establish why it represents a safety risk or a critical Best Practice in the field. 

### 2. The Core Issue
- Provide the technical breakdown of the topic.
- Maintain an objective, educational tone appropriate for an experienced journeyman teaching an apprentice.

### 3. Standards and Code Referencing (MANDATORY)
- You MUST explicitly reference relevant sections of the **NEC (National Electrical Code)**, **CEC (Canadian Electrical Code)**, and any other associated standards (e.g., **NFPA 70E**, **CSA Z462**, **OSHA**, **IEC**) that govern or apply to the specific topic.
- Quote or contextualize the specific articles or sections to validate the safety practices discussed.

### 4. Actionable Takeaways
- Exactly 3-4 clear, highly actionable bullet points that the reader can implement on their job site *today*.
- Do not write generic advice; be incredibly specific to the equipment, procedure, or topic discussed.

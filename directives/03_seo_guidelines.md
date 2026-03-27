# DIRECTIVE-03: SEO OPTIMIZATION PROTOCOL

## Purpose
To ensure every piece of content generated for the ELI Safety Blog (Daily Safety Topics, Incident RCAs) is rigorously optimized for search engines (Google, Bing) to drive maximum organic traffic from industrial and electrical safety professionals.

## 1. Frontmatter Optimization
Every generated `.mdx` or `.md` file MUST include the following SEO-critical frontmatter fields:
- **`title`**: (The Safety Hook Title) Must include the primary target keyword naturally (e.g., "Lockout/Tagout", "Arc Flash", "Induced Voltage") within the first 60 characters.
- **`description`**: A compelling, 150-160 character meta description that summarizes the actionable value of the post and includes the primary keyword. This is what appears in Google search results.
- **`keywords`**: A comma-separated list of 3-5 highly specific, long-tail technical keywords (e.g., "480V arc flash mitigation", "CSA Z462 compliance").

## 2. Structural SEO (Content Formatting)
- **H1 Header**: The main title must be wrapped in a single `#` (H1) and should closely match the meta title.
- **H2 & H3 Subheaders**: Break the content up with `##` and `###` headers. These subheaders MUST contain secondary/LSI (Latent Semantic Indexing) keywords. Instead of a generic subheader like "What Happened", use "The Protocol Failure: Skipping the Arc Flash Risk Assessment".
- **Short Paragraphs & Bullet Points**: Search engines heavily favor high "readability." Keep paragraphs to 2-3 sentences max. Use bullet points for takeaways.
- **Keyword Density**: The primary keyword must appear naturally in the introductory paragraph (first 100 words), wrapped in `**bold**` at least once, and scattered 2-3 times throughout the body. Avoid "keyword stuffing" (forcing it unnaturally).

## 3. Image SEO
- **File Naming**: Whenever an image is requested or sourced, recommend that the filename be descriptive with dashes (e.g., `/images/arc-flash-ppe-failure.jpg` instead of `/images/IMG_8829.jpg`).
- **Alt Text**: Any image embedded in the Markdown must have descriptive `alt` text that includes a keyword if relevant. Example: `![Burnt 480V industrial breaker box demonstrating arc flash damage](/images/arc-flash-damage.jpg)`

## 4. Internal & External Linking
- **External Authority Links**: Include at least 1 outbound link to a highly authoritative, reputable source (e.g., OSHA.gov, NFPA.org, CSA group) to prove the technical claims are grounded in established standards.
- **Internal Audience Links**: When referencing concepts covered in past RCAs or Daily Topics (e.g., LOTO, PPE), insert a placeholder link for the user to connect to older blog posts.

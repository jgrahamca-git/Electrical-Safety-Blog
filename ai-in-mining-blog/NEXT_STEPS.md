# Next Steps: Deployment and Development

## How to view the site locally
To view the blog during development, make sure you are in the project folder and run the dev server:

```bash
cd "c:\Users\jgrah\My Drive\Blog_Test\ai-in-mining-blog"
npm run dev
```

Then open your web browser and navigate to: **[http://localhost:4321](http://localhost:4321)**

## What to do next to deploy

To get this live on Netlify, follow these steps:

1. **Initialize Git and Push to GitHub (or similar)**
   Open a new terminal window, navigate to your new blog folder, and push the code:
   ```bash
   cd "c:\Users\jgrah\My Drive\Blog_Test\ai-in-mining-blog"
   git init
   git add .
   git commit -m "Initial commit - Astro AI in Mining Blog"
   ```
   *Then, create a new repository on your Git hosting provider (like GitHub) and push your code there.*

2. **Deploy via Netlify**
   - Log into your [Netlify account](https://app.netlify.com/).
   - Click **"Add new site"** > **"Import an existing project"**.
   - Connect your GitHub account and select your new repository.
   - Netlify will automatically read the `netlify.toml` configuration we set up. The build settings (`npm run build` and `dist` folder) are already handled.
   - Click **"Deploy site"**.

## Writing Future Content
To add more posts, simply create new `.md` or `.mdx` files inside the `src/content/safety-topics/` or `src/content/incidents/` folder. 

**CRITICAL SEO REQUIREMENT (As of April 2026):**
All new content must include the standardized SEO fields in the frontmatter before publishing. Do not publish without:
```yaml
seoTitle: "..." # 50-60 chars max. Lead with the primary keyword.
metaDescription: "..." # 140-155 chars max. Provide a curiosity hook describing what the reader learns.
primaryKeyword: "..." # 1 exact phrase, 3-5 words matching search intent.
```

**IMAGE SEO RULES:**
1. **Filename:** `[specific-subject]-[hazard-or-context].jpg`
   - Max 5-6 hyphenated words.
   - NO `eli-` prefixes, L0/L1/L2 codes, category labels, or underscore characters.
   - Good: `multimeter-current-jack-voltage-arc-flash.jpg`
2. **Alt Text:** Use 10-15 words max. Describe exactly what the image shows (start with the subject noun). Include the primary keyword naturally. 
   - Good: "Prove-test-prove method for voltage absence verification before electrical work"

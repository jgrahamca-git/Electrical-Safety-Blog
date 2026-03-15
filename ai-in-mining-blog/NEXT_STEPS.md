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
To add more posts, simply create new `.md` or `.mdx` files inside the `src/content/blog/` folder. Astro will automatically pick them up and generate the pages based on the frontmatter!

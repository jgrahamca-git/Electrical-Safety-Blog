# DIRECTIVE-02: AUTOMATED DAILY DEPLOYMENT

## Purpose
Because this blog uses a Static Site Generator (Astro), posts built with future `pubDate` stamps will be filtered out at the time of the initial build. To ensure full automation of scheduled posts (e.g., releasing a new Daily Safety Topic exactly at 3:00 AM each morning to beat MailerLite's RSS campaign), a daily scheduled rebuild of the live Netlify site is strictly required.

## The Webhook Automation Architecture

### Component 1: Netlify Build Hook
- The Netlify dashboard must be configured with a generated "Build Hook" URL. 
- When an external server sends an empty HTTP POST request to this URL, Netlify triggers a fresh snapshot build of the `main` branch. This forces Astro to re-evaluate the current `Date.now()`, automatically releasing any post stamped for that specific day.

### Component 2: GitHub Actions Daily Build Workflow
- A GitHub Actions workflow (`daily-build.yml`) acts as the automated metronome for the blog.
- **Trigger:** Schedule via GitHub cron -> Set to run at `07:00 UTC` (3:00 AM Eastern Time) every day.
- **Action:** Triggers a curl POST request to the unique Netlify Build Hook URL using the repo secret `NETLIFY_ELI_BUILD_HOOK`.

## Execution Sequence
1. The AI generates exactly 7 future-dated Daily Safety Topics.
2. The User pushes all 7 files to Git on Sunday.
3. The Initial build hides the files seamlessly.
4. The GitHub Actions Daily Build pings Netlify at exactly 3:00 AM every single morning.
5. The daily Netlify rebuild pulls the curtain back on exactly one post per day.
6. The MailerLite RSS automation, scanning every hour, seamlessly picks up the newly unlocked post and sends the daily blast at 5:30 AM Eastern.

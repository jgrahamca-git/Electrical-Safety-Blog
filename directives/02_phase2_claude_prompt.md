# Claude Code: Phase 2 Execution Prompt

When you are ready to have Claude Code review the RCA draft and generate the FMEA and Lead Magnet assets, launch `claude` in the terminal and copy/paste the prompt below.

*Make sure to replace the `[INSERT_FILENAME.mdx]` placeholder with the actual name of the Incident RCA drafted for the week!*

---

**Copy the text below:**

> We are starting Phase 2. First, please read `CLAUDE.md` and `ELI_Blog_Tracker.md` to understand your operational instructions and Phase 2 workflow. Then, please read your main skill definition at `skill-creator/eli-blog-assistant-skill.md`, along with your specific reference files located at `skill-creator/references/blog-context.md` and `skill-creator/references/editorial-standards.md`. Once you understand your role and editorial guidelines, please review the RCA draft at `ai-in-mining-blog/src/content/incidents/[INSERT_FILENAME.mdx]` for technical accuracy and editorial tone. Finally, grab the JSON config blocks from the HTML comments at the very bottom of that MDX file, and use them to execute `fmea_renderer.py` and `lead_magnet_builder.py` located at `/mnt/c/Users/jgrah/My Drive/01_ELI/07_Blog/templates/` to generate the final assets.

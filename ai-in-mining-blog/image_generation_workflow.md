# Image Generation Workflow

This document outlines the frictionless workflow for using Gemini alongside your image generation tool ("Nano Banana") specifically using the Graphic Novel style.

## The Sequence of Events (For your separate Gemini chat)

To save tokens and context window inside your main coding chat, follow this sequence in a brand new Gemini session:

**Step 1:** Start a new Gemini chat and paste this exact macro prompt:
> "I am generating blog images. Whenever I give you a safety topic, output exactly one image prompt in a 'high-contrast Graphic Novel / line-art' style. Output ONLY the prompt as copy-pasteable text with NO markdown formatting, asterisks, or conversational text. Include any specific aspect ratio tags (e.g. --ar 16:9) at the end."

**Step 2:** Wait for Gemini to acknowledge the rules.

**Step 3:** Paste **ALL 7 safety topics AT ONCE** into the chat. You do not need to do them separately! Gemini will instantly spit out 7 cleanly separated Graphic Novel style prompts.

**Step 4:** Highlight and copy all 7 prompts (or use your clipboard history manager) and paste them directly into your image generator in rapid succession.

**Step 5:** Save the generated images directly into `/home/jgrah/Blog_EI_Safety/ai-in-mining-blog/src/assets/` with descriptive names (e.g., `20260408-BESS-Toxicity-Hero.jpg`).

---

## Your 7 Chosen Topics (To paste into Step 3)
1. "Test Before Touch": The Ultimate Lifesaver
2. The Hidden Danger of Dual-Source Equipment
3. Multimeter Discipline: The "Deadly Jack" Mistake
4. Normalizing Deviations with PPE
5. Understanding the "Tryout" in LOTO
6. BESS: Thermal Runaway and Stranded Energy
7. Solar Inverter Backfeed: Isolating the Grid vs The Array

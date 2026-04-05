# Image Generation Workflow (Strict Guidelines)

This document outlines the frictionless workflow for using Gemini alongside your image generation tool ("Nano Banana" / Imagen 3) in strict compliance with the locked ELI Brand rules.

**CRITICAL RULE ENFORCEMENT:**
- **NO HUMANS:** Never prompt for people, hands, or PPE on bodies.
- **NO METER READINGS:** AI cannot draw text/readings correctly.
- **NO CIRCUIT DIAGRAMS/SCHEMATICS:** Use EdrawMax for topology.
- **IMAGEN 3 STYLE:** Hardware close-ups using physical descriptors, dramatic lighting, no connections, and dark industrial backgrounds. 
- **NOTEBOOKLM:** Use NotebookLM editorial mode ONLY for conceptual topics (e.g., Bow-tie incident diagrams, isolation maps).

---

## 1. The Sequence of Events (For your separate Gemini chat)

To save tokens and context window inside your main coding chat, follow this sequence:

**Step 1:** Start a new Gemini chat and paste this exact macro prompt to format the AI:
> "I am generating blog header images using Imagen 3. Whenever I give you a safety topic, output exactly one image prompt. **STRICT RULES:** Physical hardware details ONLY. NO humans, NO hands, NO tools, NO meter readings, NO wire connections. Describe isolated, dramatic close-ups of industrial hardware (e.g., scorched busbars, weathered buttons, dark backgrounds). Output ONLY the raw prompt as copy-pasteable text. Include any specific aspect ratio tags (e.g. --ar 16:9)."

**Step 2:** Wait for Gemini to acknowledge the rules.

**Step 3:** Paste **ALL 7 safety topics AT ONCE** into the chat. You do not need to do them separately! Gemini will instantly spit out 7 cleanly separated, compliant hardware prompts.

**Step 4:** Highlight and copy all 7 prompts (or use your clipboard history manager) and paste them directly into your image generator in rapid succession.

**Step 5:** Save the generated images directly into `/home/jgrah/Blog_EI_Safety/ai-in-mining-blog/src/assets/` using the strict naming convention: `[specific-subject]-[hazard-or-context].jpg` (max 5-6 hyphenated words, NO eli- prefixes or category labels, e.g., `multimeter-current-jack-voltage-arc-flash.jpg`). Apply standard Canva post-processing (60% brightness, orange grade, 8% grid overlay).

---

## 2. Your 7 Chosen Topics & Compliant Example Prompts

*(If you bypass Gemini entirely, you can just use these pre-written, highly compliant prompts directly in Nano Banana/Imagen 3)*

### 1. "Test Before Touch": The Ultimate Lifesaver
**Prompt:** Extreme macro close-up of a heavy industrial copper lug bolted to a dark steel backplate. Deep black scorch marks radiate outward from the center bolt. Harsh, dramatic, warm sidelight illuminating fine metallic dust on the surface, emphasizing danger. Dark, moody industrial background. --ar 16:9

### 2. The Hidden Danger of Dual-Source Equipment
**Prompt:** Close-up of a massive, heavy-duty industrial disconnect switch housing made of thick grey steel. Two distinct, oversized, thick black conduits enter the box from opposite sides. Clean, sharp lines, cinematic lighting with strong contrast, emphasizing a heavy industrial power distribution element. Deep void background. --ar 16:9

### 3. Multimeter Discipline: The "Deadly Jack" Mistake
**Prompt:** Macro photography close-up of a single red electrical testing probe resting on a heavily charred steel surface. The tip of the probe is violently melted, bubbled, and blackened. Warm, low-key lighting casting long shadows across the textured industrial surface. Hyperrealistic detail. --ar 16:9

### 4. Normalizing Deviations with PPE
**Prompt:** Close-up on the heavy steel hinge of a massive electrical switchgear door that is cracked slightly open. A fine layer of dark, powdery soot coats the cracked edge and the hinge mechanism. Dramatic contrast between the safety-orange paint on the metal and the void blackness inside the crack. --ar 16:9

### 5. Understanding the "Tryout" in LOTO
**Prompt:** Extremely detailed, zoomed-in view of a heavy-duty green industrial 'START' push button mounted on a steel pedestal. The button is deeply weathered, scratched, and coated in fine industrial dust from years of pushing. Intense, dramatic spotlight illuminating the rugged texture of the green plastic. --ar 16:9

### 6. BESS: Thermal Runaway and Stranded Energy
**Prompt:** Close proximity shot of a large, high-capacity lithium-ion rack module made of black anodized aluminum. The front cooling fins are severely warped, bubbling, and discolored with dark ash indicating extreme internal heat damage. Cool, clinical lighting contrasting with the violent heat damage. Void dark background. --ar 16:9

### 7. Solar Inverter Backfeed: Isolating the Grid vs The Array
**Prompt:** Close detail shot of thick, ominous, ribbed black photovoltaic DC cables terminating heavily into the underside of a dark, industrial junction box. Harsh, stark desert sunlight casting sharp shadows across the ribbed cables, giving them a menacing weight. Dusty industrial aesthetic. --ar 16:9

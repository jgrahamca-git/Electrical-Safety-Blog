---
title: "Understanding CAT Ratings on Voltage Test Meters"
description: "Why bringing a commercial multitester to an industrial panel is a deadly mistake."
pubDate: "Mar 26 2026"
heroImage: "../../assets/category-testing.jpg"
criticality: "L0"
conclusion_state: "safe"
agent_suggested: false
editor_confirmed: true
---
Not all electrical multimeters are created equal. A multimeter built for testing standard 120V wall outlets can literally explode in your hand if used carelessly on the main bus of an industrial 480V motor control center (MCC).

### The IEC Category (CAT) System

The IEC establishes safety ratings based on a meter's ability to withstand incredibly high, brief voltage spikes (transients) that occur frequently on industrial grids.

- **CAT II (Plug-In Loads):** Safe for standard appliances and portable tools plugged into residential or light commercial receptacles. Warning: *Never use a CAT II meter inside a heavy industrial panel.*
- **CAT III (Distribution Level):** Designed for 3-phase distribution, commercial lighting circuits, and heavy feeder panels. This is the minimum rating for most industrial floor work. 
- **CAT IV (Origin of Installation):** Required for utility-level equipment, the main service entrance of a facility, and outdoor primary connections.

### The Blast Hazard

If a massive voltage transient travels down the line while you are testing a circuit with an under-rated meter, the internal components will arc over. Because industrial circuits have massive available fault current, that tiny arc inside the meter instantly vaporizes the copper traces, blowing the meter apart like a grenade.

Always check the faceplate of your meter—and its probe leads—for a clear CAT III or CAT IV stamp before approaching an industrial cabinet.

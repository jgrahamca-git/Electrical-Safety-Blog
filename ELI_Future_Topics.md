# ELI Blog — Future Topics & Discussions Log

> **Purpose:** A centralized repository for high-quality, deeply technical blog post ideas, discussions, and concepts that have not yet been placed into the weekly production queue.

## Proposed Topics from 2026-04-10 Research

### 1. "The Black Box Problem" — Why AI Cannot Yet SIL-Certify
- **Pillar:** Industrial AI and OT/SCADA Safety
- **Focus:** Functional safety requires perfectly deterministic logic (mathematical certainty). Neural networks infer probabilistically. Explaining why AI is strictly limited to supervisory (SIL 0) roles and why the final trip command must remain on a hardwired Safety PLC.

### 2. The 2oo3 Voting Logic Gold Standard
- **Pillar:** OT, Controls, and Reliability
- **Focus:** Breaking down how 2oo3 (Two-out-of-Three) voting logic for Emergency Shutdown Systems (ESD) achieves SIL 3 risk reduction by tolerating a dangerously stuck sensor, while simultaneously slashing nuisance trips (Spurious Trip Rate) to near zero.

### 3. Predictive Proof Testing via Smart Instruments
- **Pillar:** Industrial AI and OT/SCADA Safety
- **Focus:** Moving beyond mechanical 6-month proof tests. How AI models analyze continuous diagnostic data streams (HART/Profibus PA) from transmitters to detect membrane fouling or micro-resistance changes before a critical failure occurs.

### 4. Dynamic Arc Flash Incident Energy Modeling
- **Pillar:** Arc Flash and Electrical Safety
- **Focus:** Shifting from static, 5-year snapshot arc flash studies to real-time SCADA-integrated calculations. Explaining how live utility impedance and tie-breaker configurations dynamically alter incident energy boundaries millisecond by millisecond.

### 5. Computer Vision for Electrical Boundaries
- **Pillar:** Industrial AI and OT/SCADA Safety
- **Focus:** Replacing standard light curtains with ML vision models. The system detects if a worker crossing the restricted approach boundary is actually wearing the correct high-cal PPE (face shield, arc-rated balaclava) before triggering a local alarm.

### 6. The De-Energize to Trip (Failsafe) Principle
- **Pillar:** Codes and Standards Updates / Controls
- **Focus:** Why critical SIS/ESD loops must use Normally Energized coils. A severed cable, relay destruction, or power loss must automatically drop out the coil and default the system to the tripped/safe state (unlike inherent non-failsafe shunt trips).

### 7. Control vs. Safety Separation (BPCS and SIS)
- **Pillar:** Codes and Standards Updates (ISA-84) / Controls
- **Focus:** A foundational rule: You cannot execute Safety Instrumented Functions (SIFs) in the Basic Process Control System (BPCS). Exploring why physical and logical separation is non-negotiable for system survivability.

### 8. Smart Ground Fault/Check Pattern Recognition in Mining
- **Pillar:** Grounding and Bonding / Industrial AI
- **Focus:** Standard GFGC relays struggle with VFD switching noise in deep underground trailing cables. How AI analyzes the high-frequency waveforms of leakage currents to differentiate a fracturing conductor from harmless capacitive charging.

### 9. The Danger of Forced / Bridged Contacts in PLCs
- **Pillar:** Electrical Safety Culture and Human Factors / Controls
- **Focus:** The normalization of deviance when maintenance technicians implement temporary software "forces" or hardware jumpers to defeat interlocks for troubleshooting, but forget to remove them—leading to permanent blind spots.

### 10. The Hazards of Incorrect VFD Carrier Frequencies
- **Pillar:** Controls / Arc Flash
- **Focus:** How improperly tuning the switching frequency (PWM) on large Variable Frequency Drives can induce excessive motor heating, insulation breakdown, and bearing current damage, eventually culminating in a catastrophic short circuit.

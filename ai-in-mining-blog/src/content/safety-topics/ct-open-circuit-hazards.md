---
title: "Thursday: Current Transformer (CT) Open-Circuit Hazards"
description: "Why lifting a wire on an energized CT secondary creates immediate, lethal high voltage."
pubDate: 2026-04-02
heroImage: "../../assets/category-electrical-safety-systems.jpg"
criticality: "L2"
conclusion_state: "hazard"
agent_suggested: false
editor_confirmed: true
---

Instrument technicians routinely land wires while circuits are live, but there is one component that bends the rules of electrical physics into a lethal hazard: **The Current Transformer (CT).**

CTs wrap around massive primary conductors to step down hundreds or thousands of amps into a measurable 0-5A secondary signal for a meter or protective relay. 

As long as the secondary circuit is closed (forming a loop through the meter), the CT acts normally. But if you lift a wire or accidentally open-circuit the secondary while the primary bus is energized, the CT instantly attempts to push current across an infinite impedance (the air gap).

Because `Voltage = Current × Resistance`, pushing current against infinite resistance causes the voltage to skyrocket instantly. The magnetic core of the CT violently saturates, and the secondary terminals will rapidly generate thousands of lethal volts. This extreme overvoltage destroys the CT insulation, sparks an explosive arc flash, and is highly fatal to anyone holding the wire.

Never open a live CT secondary. You **must** install and engage a CT shorting block to keep the circulating current safely flowing before removing any downstream instrumentation.

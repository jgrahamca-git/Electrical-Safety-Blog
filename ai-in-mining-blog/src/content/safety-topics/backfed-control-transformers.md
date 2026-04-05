---
title: "Sunday: The Hidden Danger of Back-fed Control Transformers"
description: "A lethal trap inside Motor Control Centers (MCCs) where 120V can magically step up to 480V."
pubDate: 2026-04-05
heroImage: "../../assets/category-controls.jpg"
criticality: "L2"
conclusion_state: "hazard"
agent_suggested: false
editor_confirmed: true
---

You approach a bucket on a Motor Control Center (MCC). You flip the main disconnect switch down to the OFF position, open the door, and throw your meter across the primary 480V stabs. The meter lights up to 480 Volts. The bucket is dead, but the stabs are fully energized. 

**Wait—how is this possible if the bucket disconnect is off?**

Welcome to the lethal danger of back-fed Control Power Transformers (CPTs). In older MCCs and complex automated systems, external control panels (like a centralized PLC cabinet) often send 120VAC control signals out to various field devices and buckets.

If a remote 120V source is accidentally wired straight into the 120V secondary side of the bucket’s internal CPT, the transformer doesn’t care that the main AC power is off. Transformers work in both directions! The 120V control power flows backward into the secondary coil, magnetically induces standard flux, and steps *up* the voltage to backfeed 480 Volts onto the primary lines attached to the stabs inside the bucket. 

Always execute a full Test-Before-Touch protocol on *every* terminal block inside an MCC. Isolate both the primary power and all foreign control voltages, or you risk being severely shocked by a "dead" transformer.

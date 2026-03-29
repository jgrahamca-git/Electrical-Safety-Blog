---
title: "Tuesday: VFD DC Bus Discharge Wait Times"
description: "Why opening a Variable Frequency Drive cabinet immediately after power-down is an extreme shock hazard."
pubDate: 2026-03-31
heroImage: "../../assets/category-testing.jpg"
---

You approach a Variable Frequency Drive (VFD) cabinet to troubleshoot a fault. You throw the main disconnect to the OFF position, confirm the panel HMI has gone dark, and immediately reach for the cabinet latch.

**Stop.** You are standing inches away from lethal, stored DC voltage.

VFDs convert incoming AC power into DC power (the "DC Bus") before inverting it back into variable-frequency AC for the motor. This DC bus uses massive capacitor banks to smooth the voltage ripple. When you throw the main disconnect, you kill the incoming AC power, but those massive capacitors remain fully charged—often holding upwards of 600 VDC to 1000 VDC.

These capacitors take time to bleed off their lethal energy through internal discharge resistors. Opening the cabinet too early exposes you to exposed DC bus bars that are still fully hot. 

Always look at the manufacturer's warning label on the drive front panel. It will specifically dictate the **mandatory wait time** (usually 5 to 15 minutes) before the door can be safely opened. After waiting, you must still physically verify zero energy on the DC bus using a properly rated multimeter before touching anything inside.

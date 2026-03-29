# Trailing-Cable GFGC / Ground-Check Inspection and Test Checklist

Below is a field-ready checklist you can paste into Word and adapt to your mine/equipment. It is built around the core MSHA ideas that the ground-check / ground-wire monitor must cause the corresponding circuit-interrupting device to open, that testing includes breaking continuity of the ground-check conductor and actuating protective relays, and that unsafe conditions found during testing require the equipment to be removed from service or repaired immediately. For high-voltage continuous mining machines, MSHA also requires 7-day tests, daily full-length trailing-cable inspections, and beginning-of-shift visual cable inspections.

---

**Equipment ID:** __________  
**Location / Section:** __________  
**Date:** __________  
**Time:** __________  
**Qualified person:** __________  
**Voltage class:** Low / Medium / High  
**Protected device:** Breaker / Contactor / Starter / Other __________  
**Relay make/model:** __________  
**Cable ID / length:** __________  
**OEM / site procedure reference:** __________  
**Test interval required at this site:** Daily / Shift / 7-day / 30-day / Monthly / Other __________  

### 1) Safe condition before inspection
- [ ] Equipment identified correctly
- [ ] Circuit de-energized and isolated
- [ ] Lockout / tagout applied per site procedure
- [ ] Test instrument proven on known source before use
- [ ] PPE verified
- [ ] Work area dry / safe access confirmed

### 2) Visual inspection — trailing cable
*Pass / Fail / N.A.*
- [ ] Outer jacket intact with no cuts exposing inner insulation
- [ ] No crushed, flattened, pinched, or abraded sections
- [ ] No burn marks, overheating, arc damage, or chemical attack
- [ ] Splices / repairs intact, secure, and mechanically protected
- [ ] Cable guards / bridging / protection in place where required
- [ ] Strain relief intact at machine, coupler, and power source ends
- [ ] No evidence of excessive twist, pull, or reel damage
- [ ] Cable routing acceptable; not subject to run-over / pinch hazard
- [ ] Ground conductor termination secure
- [ ] Pilot / ground-check conductor termination secure
- [ ] Separate frame terminations for ground and pilot confirmed where applicable
- [ ] Coupler shell, pins, sockets, latch, and insulation in good condition
- [ ] No moisture ingress / contamination in coupler or termination
- [ ] Unauthorized temporary repairs not present

> *This section is consistent with MSHA’s requirement to visually observe circuit-breaker auxiliary-device components, with high-voltage continuous mining machine rules requiring daily full-length cable inspection including splices and repairs, plus beginning-of-shift visual inspection for outer-jacket damage. MSHA technical guidance also emphasizes separate ground and pilot connections and proper coupler behavior.*

### 3) Relay / control-panel inspection
*Pass / Fail / N.A.*
- [ ] Relay nameplate and settings legible
- [ ] Trip / alarm targets and indication healthy
- [ ] Control power healthy
- [ ] Relay fuse(s) intact
- [ ] No loose wiring, corrosion, heat damage, or contamination
- [ ] CT / sensor wiring intact and correctly landed
- [ ] Trip path wiring matches latest approved schematic
- [ ] Interposing relay present if required by design
- [ ] Breaker UVR / shunt-trip / trip coil connections intact
- [ ] No bypasses, jumpers, or defeated interlocks present

### 4) Ground-check continuity functional test
*Pass / Fail / N.A.*
- [ ] Initiate approved ground-check test method
- [ ] Break continuity of the ground-check conductor using approved method
- [ ] Verify GFGC / ground-check relay changes state correctly
- [ ] Verify corresponding circuit-interrupting device opens
- [ ] Verify main power is removed downstream
- [ ] Verify restart is not possible until fault/reset sequence is completed
- [ ] Record trip time / observed behavior if required
- [ ] Restore circuit correctly after test

> *MSHA’s testing requirement explicitly includes breaking continuity of the ground check conductor, and the performance requirement is that the fail-safe ground-check circuit causes the breaker to open when the ground or pilot check wire is broken. For longwall/high-voltage equipment, MSHA also states the ground-wire monitor and associated circuits must be examined and tested to verify they will cause the corresponding interrupting device to open.*

### 5) Ground-fault / auxiliary-relay proof test
*Pass / Fail / N.A.*
- [ ] Operate relay test function or approved external test method
- [ ] Actuate at least two auxiliary protective relays where applicable
- [ ] Verify trip indication occurs
- [ ] Verify corresponding circuit-interrupting device opens
- [ ] Verify downstream voltage is absent after trip
- [ ] Verify breaker / contactor status indication matches actual state
- [ ] Verify manual / electrical reset behaves correctly
- [ ] Verify no abnormal delay or chatter

> *For underground high-voltage breakers, MSHA requires monthly testing and specifies that tests include actuating at least two auxiliary protective relays. For high-voltage continuous mining machines, the ground-fault test circuit must be activated at least every 7 days and before tramming to verify it opens the corresponding interrupting device.*

### 6) Trip-chain integrity check — important for “failed closed” output contacts
*Pass / Fail / N.A.*
- [ ] Confirm the relay output used in the trip chain is the correct contact per approved design
- [ ] Confirm the breaker / contactor actually drops out when the relay commands trip
- [ ] Confirm main contacts are physically open, not just indicated open
- [ ] Confirm downstream voltage absence with test instrument
- [ ] Confirm no restart is possible with relay held in trip condition
- [ ] Confirm reset cannot occur until fault is cleared
- [ ] If interposing relay is used, verify both the relay and final trip device change state correctly
- [ ] If undervoltage release is used, verify loss of control power causes drop-out as designed
- [ ] If shunt-trip is used, confirm site engineering has accepted that architecture and functional testing passes

> *This section matters because MSHA acceptance criteria for ground-wire-monitor systems explicitly treat welded relay contacts as a known exception in the “failsafe” definition, and Littelfuse’s public SE-135 manual says fail-safe undervoltage mode is recommended while non-fail-safe shunt-trip operation is not recommended. MSHA also notes that the protective circuits depend on the breaker / UVR chain functioning correctly. A welded or failed-closed relay output can leave the breaker/contactor energized if the trip architecture depends on that contact opening. That is why this checklist includes a separate trip-chain integrity check.*

### 7) Resistance / continuity checks
*Pass / Fail / N.A.*
- [ ] Ground conductor continuity acceptable: ________ ohms
- [ ] Pilot / ground-check conductor continuity acceptable: ________ ohms
- [ ] No abnormal increase from baseline
- [ ] Frame-to-ground bonding path acceptable
- [ ] Coupler pin-to-pin continuity acceptable
- [ ] Insulation resistance test completed if required by site/OEM: ________ MΩ
- [ ] Results compared against previous records / trend

> *MSHA technical guidance describes trip action when the grounding-circuit impedance rises beyond the amount that would allow excessive frame voltage under fault conditions, so trend changes in loop resistance matter even before an outright open circuit occurs.*

### 8) Coupler / termination checks
*Pass / Fail / N.A.*
- [ ] Correct coupler type installed
- [ ] No damaged or recessed pins
- [ ] Pilot contact condition acceptable
- [ ] Ground contact condition acceptable
- [ ] Correct terminator / end-of-loop device installed where used
- [ ] Separate pilot and ground frame connections verified
- [ ] No evidence of overheating or tracking
- [ ] Mechanical latch / retention acceptable

> *MSHA technical guidance states couplers used with ground-check circuits must be designed so the pilot wire breaks first when the coupler is separated, and the pilot and ground must be connected to equipment frames by separate connectors.*

### 9) Frequency / recordkeeping box
*Minimum frequency applied to this equipment: __________________*
- [ ] Shift / pre-use visual inspection completed
- [ ] Daily full-length cable inspection completed where required
- [ ] 7-day functional tests completed where required
- [ ] 30-day / monthly auxiliary-device and ground-wire-monitor test completed
- [ ] Signature and date entered
- [ ] Unsafe conditions recorded
- [ ] Corrective action recorded
- [ ] Record retained per site / regulatory requirement

> *MSHA examples include: monthly testing of high-voltage breakers and auxiliary devices; testing by breaking ground-check continuity and actuating relays; 30-day testing of ground-wire-monitor circuits for longwall equipment; and, for high-voltage continuous mining machines, every-7-day ground-fault and ground-wire-monitor tests plus daily/shift cable inspections. Records and certifications are required and must note unsafe conditions and corrective actions.*

### 10) Defects / corrective actions
**Defect found:** ____________________________________________  
**Immediate risk level:** Low / Medium / High  
**Removed from service?** Yes / No  
**Corrective action taken:** __________________________________  
**Parts replaced:** __________________________________________  
**Retest completed:** Yes / No  
**Returned to service by:** __________________ **Date:** __________  

> *MSHA requires equipment to be removed from service immediately or repaired immediately when testing reveals a fire, shock, ignition, or operational hazard.*

### 11) Sign-off
**Inspector / Qualified person:** __________________  
**Signature:** __________________  
**Date:** __________________  

**Supervisor / Foreman review:** __________________  
**Signature:** __________________  
**Date:** __________________  

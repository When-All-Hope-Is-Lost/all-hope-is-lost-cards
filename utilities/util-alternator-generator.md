---
id: util-alternator-generator
title: "Making 12V power from a car alternator (wind, bike, water wheel)"
category: utilities
tags: [alternator, generator, 12v, bike generator, wind, water wheel, pulley, battery charging]
urgency: info
version: 0.1.1
last_reviewed: 2026-10-22
sources:
  - title: "DOE Energy Saver: Small Wind Electric Systems"
    url: https://www.energy.gov/cmei/systems/windexchange/small-wind-guidebook
    checked_date: 2026-10-21
    license: "Public domain (US Government work)"
  - title: "DOE Energy Saver: Microhydropower Systems"
    url: https://docs.nlr.gov/docs/fy01osti/29065.pdf
    checked_date: 2026-10-21
    license: "Public domain (US Government work)"
  - title: "OSHA: Electrical safety"
    url: https://www.osha.gov/electrical
    checked_date: 2026-10-21
    license: "Public domain (US Government work)"
card_license: CC BY-SA 4.0
review_status: draft
region: US
needs_professional_review: true
verify:
  - "Car alternators usually need roughly 1,000+ RPM at the alternator shaft before they charge (estimate; varies by model)"
  - "Pulley ratio examples are arithmetic only, not tested designs"
  - "Drafted from general knowledge of the listed sources; source text not re-checked line by line this cycle"
---

> **Not yet professionally reviewed.** This card has not been checked by a qualified medical professional. Please confirm with a professional.

## Do this now
**Charge a 12V battery, never your house wiring, and keep every spinning part guarded.**

## Steps
1. A car alternator already has a built-in rectifier (turns AC into 12V DC) and usually a voltage regulator. Use it to charge a 12V battery, then run 12V devices or an inverter from the battery.
2. It must spin fast. Gear it up with belts and pulleys: speed gain = big drive pulley diameter ÷ small alternator pulley diameter. Example arithmetic: a 20-inch wheel driving a 2.5-inch pulley spins the alternator 8 times faster.
3. Most alternators need a small 12V current on the field (exciter) terminal to start charging. Wire it through a switch so the field does not drain the battery when stopped.
4. Bike: mount the bike on a stand, run a belt from the rear wheel to the alternator. Expect it to be hard work; output is small (estimate).
5. Wind or water wheel: power varies with wind or water flow. Put a charge controller or the alternator's own regulator between source and battery so it cannot overcharge.
6. Fuse the positive lead close to the battery. Use thick wire sized for the current.
7. Inverter: makes 120V AC from the battery for small loads. Size it above the load, connect with short thick cables and a fuse, and run it only in a ventilated spot.

## If / then
- **If** the battery gets hot, swells, or smells like rotten eggs **then** stop charging, ventilate, keep sparks away
- **If** you want to power house circuits **then** use only a properly installed transfer switch or interlock, done by an electrician
- **If** the shaft wobbles or the belt slips **then** stop and fix the mount before running again

## Don't
- Never connect a generator or inverter to a house outlet or panel without a transfer switch. Backfeeding can kill line workers and neighbors.
- Don't charge lead-acid batteries indoors without ventilation; they release hydrogen gas that can explode.
- Don't wear loose clothing or long hair near belts and pulleys.
- Don't short battery terminals with tools or jewelry.

## Get help now
- Electric shock, burns, or battery acid in the eye: call 911; flush eyes with clean water for at least 15 minutes.

## Source & license
Summarized from the sources listed above. Reference to any agency does not imply endorsement by the U.S. Government. CDC material is available free at cdc.gov. Draft card, not professionally reviewed. Card text CC BY-SA 4.0.

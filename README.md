# All Hope Is Lost: offline emergency cards

> **⚠️ DRAFT — pending expert review. Not medical, legal, or professional advice. In an emergency call your local emergency number (911 in the US).**

Short, plain-language cards for the worst days: a crisis, a medical emergency, no water, no food, nowhere to sleep, a shutoff notice, or no way to get your medication. Each card tells you **what to do right now**, then gives numbered steps, if/then rules, a "don't" list, and who to call.

The cards are plain Markdown files. You can read them in any text editor or in a browser, or load them into an app. **They work with no internet, no account, and no AI model.**

## What's here

| Path | What it is |
|---|---|
| `<category>/<id>.md` | One card per file (crisis, first-aid, water, food, shelter, utilities, medication, fire, vehicle, structure, comms, weather, wildlife, animals, hazmat) |
| `index.md` | Human-readable list of all cards, with review status |
| `index.json` | Machine-readable index, with a SHA-256 hash per card so mirrors can be checked for tampering |
| `FORMAT.md` | The card format: required fields, headings, and content rules |
| `QA.md` | Review checklist and per-card review log |
| `tools/build_index.py` | Validates every card and rebuilds both index files (Python 3, standard library only) |
| `tools/intl_block.py` | Adds the "Outside the US" emergency-number and warning-service block to weather cards |
| `LICENSE` | Licenses for the content and the code |

## Using it offline

1. Download the repository as a ZIP (or clone it) while you have a connection.
2. Copy it to your phone, laptop, or a USB stick.
3. Open `index.md`, or browse a category folder. Every instruction you need is in the card text. Links and phone numbers are extras.

Print the crisis and first-aid cards now. Paper works when batteries don't.

To check the cards after editing: `python3 tools/build_index.py` (run from the repository root).

## Sources and licenses

- Cards are written in our own words from **public-domain US government sources** (Army ATP 4-02.11 and ATP 3-50.21, FEMA / Ready.gov / CERT, CDC, NWS, USDA, HUD, SAMHSA, HRSA) and state agency material, plus **Wikipedia** (CC BY-SA 4.0).
- Copyrighted material (Red Cross, AHA, extension services, wikiHow, etc.) is **linked, never copied**.
- Every card lists its sources, the date they were checked, and their license.
- Card text: **CC BY-SA 4.0**. Code in `tools/`: **MIT**. See `LICENSE`.
- The card layout (do-this-now line, numbered steps, if/then rules, a don't list) was inspired by other emergency-card apps. None of their text is used.
- CDC material is used under CDC's terms. Its use doesn't imply CDC endorsement, and the originals are free at cdc.gov. No government agency endorses this project.

## Important: not medical, legal, or professional advice

These cards are general safety information to use **when you can't reach help, or while you wait for it**. They don't replace a doctor, EMS, a crisis counselor, a lawyer, or local authorities. Laws, benefits, and phone numbers change, and some cards are marked with items that still need checking. **In an emergency, call your local emergency number (911 in the US).** If you're thinking about suicide or are in emotional crisis, **call or text 988**.

Review status is shown on every card. First-aid, crisis, and medication cards are **self-reviewed only** until a qualified professional reviews them.

## Contributing

Contributions are welcome, especially reviews from EMTs, nurses, physicians, crisis counselors, and legal aid workers.

- Follow `FORMAT.md`: the six required headings in order, at least one source per fact, and a source/license line.
- Use public-domain or CC BY-SA sources only. Link copyrighted sources, but never copy their text.
- Never add instructions for harming people or animals.
- Don't make up numbers. If you're unsure, add the item to the card's `verify` list.
- Run `python3 tools/build_index.py` before opening a pull request.
- By contributing, you agree to license your contribution under the licenses in `LICENSE`.

# State data set schema (v1.0)

## Why this exists
Each US state (plus DC) gets one offline JSON record that the app can read directly and that `tools/states_render.py` turns into a readable card (`states/<xx>-survival-guide.md`). Keeping facts in data, not prose, lets reviewers fix one field and regenerate every card, and keeps unverified items visible.

## File
`states/data/states/<XX>.json` (two-letter USPS code, upper case). UTF-8. Source of truth after seeding (`tools/states_seed.py` is a one-time seed).

## Fields (all required)
| field | type | rule |
|---|---|---|
| schema_version | string | "1.0" |
| code, name | string | code == file name |
| last_reviewed | string | ISO date |
| review_status | string | draft / self-reviewed / expert-reviewed |
| needs_professional_review | bool | true until a wildlife-law and plant-ID reviewer signs off |
| agency | object | name, home_url (https), regulations_url (URL or "unverified"), url_check {date, result: ok / blocked} |
| law_note | string | licenses, seasons and methods apply; survival needs don't override law |
| game_species, fish_species | list of {name, seasons} | seasons MUST be "check agency". No bag limits, dates or legal specifics. game_species may be empty (DC) |
| forage | list of {name, scientific, lookalike_warning} | scientific names per USDA PLANTS |
| hardiness_zones | {value, source} | approximate USDA 2023 range; users confirm by ZIP |
| climate_class | string | cold-humid, cold-dry, mixed-humid, mixed-dry, hot-humid, hot-dry, hot-mixed, marine-and-cold-dry, mixed-dry-marine, subarctic-arctic, tropical |
| heating_cooling | string | shelter priority for the climate |
| water | object | risks (list), drinking_water_program, emergency_treatment (EPA URL) |
| hazard_cards | list | ids of existing `weather/` cards; build fails if missing |
| region | string | template key used for species/forage lists |
| note | string | state-specific note, may be empty |
| unverified | list | every field not yet checked against a cited page; becomes the card's `verify:` list |

## Validation
`python3 tools/states_render.py && python3 tools/build_index.py` must report 0 errors. The build checks JSON validity, required fields and types, https agency links, "check agency" seasons, forage lookalike warnings, hazard card ids, and that each JSON has a rendered card.

## Optional fields (added in verification round 1)
| field | type | rule |
|---|---|---|
| verified | list of {field, how, date} | what was checked and how (http200, http200-hub, search, USDA PLANTS distribution) |
| agency.regulations_url_check | {date, result} | http200 = page loaded from the box; http200-hub = agency hunting hub page that links the regulations; search = official page confirmed in web search (site blocks automated fetches) |
| feral_hog_note | string | replaces feral hogs in species lists; rules vary and some states ban taking them |
| forage[].usda_symbols, forage[].usda_present | list, bool | USDA PLANTS symbols checked against the state distribution |

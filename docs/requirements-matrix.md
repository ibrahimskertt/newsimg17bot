# Requirements matrix — news-image-20261117

Source: kit RULES.txt / competition.yaml (kit level as downloaded
2026-11-18). Importance: C = critical (gate), H = high (judged), M = medium.

| # | Requirement | Imp. | Implementation | Evidence | Gap |
|---|---|---|---|---|---|
| R1 | Program at repo root: main.py (Python 3.13) or main.ts (Node 22) | C | main.py, stdlib only | Gemini session writes it with file tools; kit check | none |
| R2 | Program writes ONE image to /output/entry.png | C | main.py copies the committed entry.png to /output/entry.png (kit starter pattern) | double-run test in build session + local QA | none |
| R3 | Image PNG or JPEG, whole file, told apart by first bytes | C | entry.png holds JPEG bytes (quality 88) | PIL format check in QA | none |
| R4 | ≤ 1 MiB (1,048,576 bytes) and ≤ 1024×1024 px | C | 1024×1024, ~271 KB at V1 | measured each stage | none |
| R5 | No network at runtime; two runs byte-identical | C | pure file copy; no time/random inputs | SHA-256 of two runs compared each stage | none |
| R6 | Public GitHub repo owned by the user, created after the opening (2026-11-17T23:43Z), OSI licence | C | gh repo create (public) + MIT LICENSE from `makefun init` | repo URL in final report | none |
| R7 | Transcripts of the build sessions uploaded; sessions inside the competition window; thinking gates pass | C | bundle per the proven 2026-11-18 recipe (system-prompt file, --mcp none, harness facts, --muse-usage) | official `check` = 0 failures before every submit | none |
| R8 | Limits: 10 submissions/day, 20 total; last submission counts (Force_Last) | H | staged plan V1–V5, each a substantive improvement | submission log in final report | none |
| R9 | Image sums up Tuesday 17 Nov 2026 and names the day | H | masthead + "TUESDAY, NOVEMBER 17, 2026" date line; content from docs/research.md | visual inspection full-size + 300px | none |
| R10 | Breadth: the day's most consequential stories across regions/fields | H | 1 hero story + 5 supporting caption chips (Middle East, Europe, Asia diplomacy, markets/AI, Africa health, Africa conflict) | docs/research.md ranking | none |
| R11 | Faithful: no hype, no unverified claims shown as fact | H | chips use only wire-confirmed facts; Iranian mine claims excluded; collapse attributed per Ukraine's General Staff via Reuters/AP | docs/research.md sourcing notes | none |
| R12 | Craft: one clear composition, legible at ~300px, no garbled text | H | AI art generated with NO text; all text composited in PIL with vetted fonts; 300px read-through each stage | QA screenshots each stage | hull micro-markings in base art (negligible at final size; monitored) |
| R13 | Sessions must not begin before the opening; build inside the window | C | all build sessions started 2026-11-18, after the 2026-11-17T23:43Z opening | bundle dry-run listing | none |

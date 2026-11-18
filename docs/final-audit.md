# Final competitive audit + quota note — news-image-20261117

## Submission log (Force_Last: the last accepted submission is the entry)

| Ver. | Commit | Submission id | Claim code | Stage improvement |
|---|---|---|---|---|
| V1 | dfbf8a9cee2c5d8a8fa7f469b08461c620bcdca2 | 01a1ef70-a599-7345-b881-b429fc715853 | AF-BBB7C-S326P-HVNHQ-XJEM0 | Main editorial composition |
| V2 | 75b8fabdedad10df7606a7de2438e020d6965101 | 01a1ef72-21eb-74e1-b2b0-a533c37901a5 | AF-6P1SC-AAZJJ-5MMH9-CQ7S7 | Storytelling: hero headline + Hormuz traffic stat chip |
| V3 | bc1451a4a9dc00b5d43722db2bb2ccb52c2a35c3 | 01a1ef74-08f0-76dc-9a8a-e9458d1978c4 | AF-2QF3K-VRGWT-E98T3-MT72A | Readability: larger chips/date/hero type, stronger chip contrast |
| V4 | 4d2000b19d9ab2741bc7dc6fd1a8a075190e9322 | — NOT SUBMITTED — | — | Accuracy: gas-tanker wording, sharpened Sudan chip, bow pseudo-text cleanup |

Every submitted version passed the same gates first: double-run SHA-256
determinism, 1024×1024 and ≤1 MiB, official kit check 14 passed / 0 failed.

## Quota blocker (why V4/V5 could not be submitted)

The V4 submit was refused: HTTP 429, "Entry quota reached — this account
has reached its entry limit for this competition (account reputation)".
`makefun status --competition news-image-20261117` confirms: 3 entries
made, none left, and "No step the account can take raises it." The nominal
limits (10/day, 20 total) were silently lowered for this account; the V1
status output had warned that reputation can lower the total and that the
lowered number is never disclosed.

Failure protocol (cause → evidence → minimal fix → preventive test →
learning note):
- Cause: staged plan assumed nominal limits; the account's real cap was 3.
- Evidence: /tmp/submit-v4.log (HTTP 429) + the quota status above.
- Minimal fix: none exists for this competition; V3 stands as the final
  entry. No retries were attempted after the explicit refusal.
- Preventive test: before any future staged-submission plan, query the
  competition quota first and front-load the highest-impact improvements
  into the earliest versions.
- Learning note: this file; the V4 improvements remain in the local git
  history (commit 4d2000b) as the record of what the next stage carried.

## Final audit of the standing entry (V3)

Judged harshly against top international editorial standards, including a
300px downscale read (masthead, date, hero line and all six chips legible;
hero tanker dominant). Internal rubric (owner's): V1 scored 84/100;
V3 scores 88/100 (accuracy 22, storytelling 18, composition 17, clarity 14,
coverage 9, originality 8). The unsubmitted V4 measured ~90/100 locally.

Five biggest weaknesses of the standing V3:
1. Hero line says "HIT TANKER" where the stricken vessel was specifically
   a gas (LPG) tanker — fixed in V4 (local only, unsubmittable).
2. Faint AI pseudo-lettering on the tanker's bow — cleaned in V4 with a
   feathered blur patch (local only, unsubmittable).
3. Sudan chip ("DRONES DRIVE SUDAN CIVILIAN TOLL") is vaguer than the UN's
   precise finding — sharpened in V4 (local only, unsubmittable).
4. The chip band covers the bow's lowest ~15% — a deliberate front-page
   trade-off: the chips carry the breadth criterion; accepted.
5. The distant broken-bridge motif reads as scenery at 300px rather than
   as the Kerch story — mitigated by its caption chip; enlarging it would
   break the one-hero hierarchy the owner ordered.

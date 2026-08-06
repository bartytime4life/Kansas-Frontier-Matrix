# Historical place resolution fixtures

This directory contains **synthetic, deterministic, no-network** fixtures for the
`HistoricalPlaceResolutionCandidate` profile.

## Valid lane

| Fixture | Expected result |
|---|---|
| `variant_resolved.json` | one authority-backed variant resolves to `high / candidate_review` |
| `post_office_resolved.json` | GNIS + AHCB + synthetic post-office lifespan resolves to `high / candidate_review` |
| `rail_stop_hold.json` | a rail-stop label remains `medium / hold_for_review` |
| `ambiguous_hold.json` | two time-scoped candidates remain `medium / hold_for_review` |
| `out_of_time_abstain.json` | no candidate supports the query year, so the profile returns `low / abstain` |

## Invalid lane

Each invalid JSON file has one `.expected_error.txt` sidecar naming a required
semantic finding. Invalid cases cover derived place identity drift, rail-stop
overclaiming, attempted public release, and source-reference reuse.

## Authority boundary

All names, counties, authority identifiers, source references, and scan identifiers
are synthetic sentinels. The fixtures do not access GNIS, BGN, AHCB/Newberry,
KSHS/Baughman, maps, newspapers, or any live service. Passing tests do not establish
a real place identity, legal status, historical boundary, source rights, EvidenceBundle
closure, policy approval, release, or publication authority.

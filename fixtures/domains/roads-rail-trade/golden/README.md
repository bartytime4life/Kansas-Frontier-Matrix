# Roads/Rail/Trade golden fixtures

`fixtures/domains/roads-rail-trade/golden/`

Status: draft / fixture lane, first payload added. `PLACEHOLDER.md` is
retained alongside this README.

Stable expected-output pairs for the Roads/Rail/Trade domain. A passing
check proves only that the declared consumer produced the paired expected
output for this synthetic case — not that any route, corridor, or trade
claim is real, released, or publication-ready.

| File pair | Scenario | Expected outcome |
|---|---|---|
| `corridor_route_lookup.input.json` / `.expected.json` | Lookup of the synthetic `CorridorRoute` added in `../valid/valid_1_corridor_route.json`. | `ANSWER` — returns the candidate corridor with generalized geometry and `release_posture: candidate`. |

See also: [`../valid/README.md`](../valid/README.md) · [`../corridor_route/valid/valid_historic_candidate.json`](../corridor_route/valid/valid_historic_candidate.json)

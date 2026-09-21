# Roads/Rail/Trade valid fixtures

`fixtures/domains/roads-rail-trade/valid/`

Status: draft / fixture lane, first payload added. `PLACEHOLDER.md` is
retained alongside this README.

| File | Object family | Scenario | Expected outcome |
|---|---|---|---|
| `valid_1_corridor_route.json` | `CorridorRoute` | Synthetic historic-corridor candidate, same shape family as `../corridor_route/valid/valid_historic_candidate.json`. | Passes shape check; `claim_status` stays `candidate`, geometry stays `generalized`. |

Shared posture: all identifiers, geometry references, and evidence refs are
synthetic. A passing check proves only the declared shape expectation, not
transport-corridor truth, evidence closure, or release readiness.

See also: [`../golden/README.md`](../golden/README.md) · [`../corridor_route/valid/valid_historic_candidate.json`](../corridor_route/valid/valid_historic_candidate.json)

# Roads/Rail/Trade valid fixtures

`fixtures/domains/roads-rail-trade/valid/`

Status: draft / fixture lane, first payload added. `PLACEHOLDER.md` is
retained alongside this README.

| File | Object family | Scenario | Expected outcome |
|---|---|---|---|
| `valid_1_corridor_route.json` | `CorridorRoute` | Synthetic historic-corridor candidate, same shape family as `../corridor_route/valid/valid_historic_candidate.json`. | Passes shape check; `claim_status` stays `candidate`, geometry stays `generalized`. |
| [`road_segment/valid_1_road_segment.json`](road_segment/README.md) | `RoadSegment` | Synthetic generalized road segment. | Passes shape check; not released. |
| [`rail_segment/valid_1_rail_segment.json`](rail_segment/README.md) | `RailSegment` | Synthetic generalized rail segment. | Passes shape check; not released. |
| [`wzdx_v4/valid_1_wzdx_feature.json`](wzdx_v4/README.md) | WZDx v4 `RoadEventFeature` | Synthetic work-zone event, generalized county location. | Passes shape check; not released. |

Shared posture: all identifiers, geometry references, and evidence refs are
synthetic. A passing check proves only the declared shape expectation, not
transport-corridor truth, evidence closure, or release readiness.

See also: [`../golden/README.md`](../golden/README.md) · [`../corridor_route/valid/valid_historic_candidate.json`](../corridor_route/valid/valid_historic_candidate.json)

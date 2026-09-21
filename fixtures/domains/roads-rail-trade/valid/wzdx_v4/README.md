# Roads/Rail/Trade valid — wzdx_v4 fixtures

`fixtures/domains/roads-rail-trade/valid/wzdx_v4/`

Status: draft / fixture lane, first payload added.

Small synthetic examples shaped like a Work Zone Data Exchange (WZDx) v4
feature, used to exercise ingestion/mapping checks for the `wzdx` connector
without reading a live feed. These are not real work-zone data.

| File | Scenario | Expected outcome |
|---|---|---|
| `valid_1_wzdx_feature.json` | Synthetic WZDx v4 `RoadEventFeature`-shaped record with a generalized event location. | Passes shape check; not released. |

See also: [`../../golden/README.md`](../../golden/README.md) · [`../../../../../connectors/wzdx/`](../../../../../connectors/wzdx/)

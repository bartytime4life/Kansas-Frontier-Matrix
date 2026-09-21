# Soil SSURGO map unit — golden fixtures

`fixtures/domains/soil/ssurgo_mapunit/golden/`

Status: draft / fixture lane, first payload added.

Stable expected-output pair for the `SoilMapUnit` object family already
exercised by the `valid_static` case in
[`../../soil_map_unit/cases.json`](../../soil_map_unit/cases.json).

| File pair | Scenario | Expected outcome |
|---|---|---|
| `map_unit_lookup.input.json` / `.expected.json` | Lookup of the synthetic map unit `soil-map-unit:7f8a1fa441002a00faf4d843` (MUKEY `MUKEY-TEST-001`). | `ANSWER` — returns the map unit with `geometry_posture: SOURCE_POLYGON` and `public_use_allowed: false`. |

See also: [`../../soil_map_unit/cases.json`](../../soil_map_unit/cases.json)

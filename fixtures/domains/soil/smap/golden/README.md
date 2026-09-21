# Soil SMAP — golden fixtures

`fixtures/domains/soil/smap/golden/`

Status: draft / fixture lane, first payload added.

Stable expected-output pair for the satellite soil-moisture (`SMAP`-style)
object family already exercised in
[`../../soil_moisture_observation/valid/answer_satellite_surface.json`](../../soil_moisture_observation/valid/answer_satellite_surface.json).

| File pair | Scenario | Expected outcome |
|---|---|---|
| `satellite_grid_cell_lookup.input.json` / `.expected.json` | Lookup of the synthetic satellite grid-cell observation `soil-moisture:be4da95c2211800990b09f03`. | `ANSWER` — returns the generalized grid-cell measurement with `public_use_allowed: false`. |

See also: [`../../soil_moisture_observation/valid/answer_satellite_surface.json`](../../soil_moisture_observation/valid/answer_satellite_surface.json)

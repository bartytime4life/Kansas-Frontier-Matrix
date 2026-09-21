# Soil golden fixtures

`fixtures/domains/soil/golden/`

Status: draft / fixture lane, first payload added. `PLACEHOLDER.md` is
retained alongside this README.

Stable expected-output pair for the Soil domain, paired with the existing
`../valid/public_safe_observation.json`. A passing check proves only that
the declared consumer produced this expected output for the synthetic
case, not that real soil-moisture data, evidence closure, or release
readiness exists.

| File pair | Scenario | Expected outcome |
|---|---|---|
| `soil_observation_lookup.input.json` / `.expected.json` | Lookup of the synthetic station observation in `../valid/public_safe_observation.json`. | `ANSWER` — returns the generalized county-level observation with `release_state: not_released`. |

See also: [`../valid/public_safe_observation.json`](../valid/public_safe_observation.json)

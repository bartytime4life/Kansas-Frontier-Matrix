# Soil spec_hash fixtures

`fixtures/domains/soil/spec_hash/`

Status: draft / fixture lane, first payload added.

Small synthetic examples exercising `spec_hash` integrity checks across Soil
object families: a matching digest (valid) and a deliberately mismatched
one (invalid), mirroring the `hash_mismatch` case already present in
[`../soil_map_unit/cases.json`](../soil_map_unit/cases.json).

| File | Scenario | Expected outcome |
|---|---|---|
| `valid_1_matching_spec_hash.json` | `spec_hash` matches the canonicalized content it pins. | Passes integrity check. |
| `invalid_1_spec_hash_mismatch.json` / `.expected_error.txt` | `spec_hash` does not match the canonicalized content. | `ERROR` — `SPEC_HASH_MISMATCH`. |

See also: [`../soil_map_unit/cases.json`](../soil_map_unit/cases.json)

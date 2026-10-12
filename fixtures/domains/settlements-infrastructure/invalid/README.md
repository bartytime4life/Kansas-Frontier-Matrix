# Settlements/Infrastructure — invalid fixtures

`fixtures/domains/settlements-infrastructure/invalid/`

Status: draft / fixture lane. `PLACEHOLDER.md` is retained because
[`.github/workflows/domain-settlements-infrastructure.yml`](../../../../.github/workflows/domain-settlements-infrastructure.yml)
checks for its presence; the payloads below are the first real content in
this lane.

| File | Scenario | Expected outcome |
|---|---|---|
| `invalid_1_missing_source_role.json` / `.expected_error.txt` | A `Settlement` identity omits `source_role`, so historical vs. regulatory provenance cannot be distinguished. | `ERROR` — identity validation fails once the recommended-semantics validator named in the schema's `x-kfm` is implemented (documented target; the current PROPOSED schema stub does not yet enforce it). |
| `invalid_2_public_condition_leak.json` / `.expected_error.txt` | An `InfrastructureAsset` marks `sensitivity_tier: "T0"` while still carrying a `condition_observation` field. | `DENY` — condition/vulnerability detail may never reach T0/T1 per infrastructure sublane §7.2 invariant 6. |

Every file here is synthetic and safe to store; the "leak" examples contain
only placeholder field names, never real condition or vulnerability content.

See also: [`../README.md`](../README.md) · [`../valid/README.md`](../valid/README.md)

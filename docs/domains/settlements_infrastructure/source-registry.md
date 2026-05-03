# Settlements & Infrastructure Source Registry Guidance

This file defines the source descriptor requirements for this lane.

## Required fields

- `source_id`
- `source_name`
- `owner`
- `steward`
- `source_role` (`authority`, `observation`, `documentary`, `derived`, `mirror`, `aggregate`)
- `rights` (license + redistribution constraints)
- `sensitivity` (`public`, `review_required`, `restricted`)
- `spatial_support` (geometry type/precision)
- `temporal_support` (event time semantics + cadence)
- `stable_keys` (identifiers preserved end-to-end)
- `ingest_mode` (`fixture_only` or `live`)
- `activation_state` (`planned`, `approved`, `active`, `blocked`)

## Admission checklist

1. Rights and sensitivity are explicit and reviewed.
2. Source role is compatible with claim class.
3. Stable keys and timestamps survive normalization.
4. Negative fixtures exist for denial/abstention paths.
5. Policy checks enforce fail-closed publication behavior.

# Agriculture Source Registry Guidance

This file documents what each agriculture source descriptor must contain before activation.

## Required fields

- `source_id`: immutable unique source key.
- `source_name`: human-friendly name.
- `owner` and `steward`: accountable parties.
- `source_role`: one of `authority`, `observation`, `aggregate`, `remote_sensing`, `derived`, `mirror`, `documentary`.
- `rights`: license/terms, redistribution constraints, and citation requirements.
- `sensitivity`: `public`, `review_required`, or `restricted`.
- `spatial_support`: geometry type and precision class.
- `temporal_support`: cadence, timestamp semantics, and staleness rule.
- `stable_keys`: source identifiers that must survive normalization.
- `ingest_mode`: `fixture_only` or `live`.
- `activation_state`: `planned`, `approved`, `active`, or `blocked`.

## Admission checklist

A source is admissible only when all checks pass:

1. Rights and sensitivity are explicit and reviewed.
2. Source role is non-ambiguous and claim-scope compatible.
3. Stable keys and timestamps are demonstrably preserved.
4. Required negative fixtures exist.
5. Policy checks enforce fail-closed outcomes.

# control_plane

## Purpose
Machine-readable governance maps too operational for prose, not source data, not schemas. The `what governs what?` layer.

## Authority level
canonical

## What belongs here
YAML registers, crosswalk tables, machine indices that govern docs, sources, object families, domain lanes, policy gates, release state, contradictions, deprecations.

## What does not belong here
Source data, processed data, schemas, code, policy rules, executable validators.

## Inputs
See related folders.

## Outputs
See related folders.

## Validation
See `tests/` and `tools/validators/`.

## Review burden
Maintainer review; steward review for trust-bearing changes.

## Related folders
`docs/registers/` carries human-readable counterparts; `tools/validators/` checks register integrity.

## Status
PROPOSED

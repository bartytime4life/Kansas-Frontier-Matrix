# Hydrology Identity Model

## Identity priorities
1. Prefer stable, source-native permanent identifiers.
2. Keep legacy identifiers for compatibility only.
3. Preserve relationship class (`exact`, `split`, `merge`, `retired`, `ambiguous`).

## Canonical keys
- `huc12_id` for hydrologic units.
- `permanent_id` for NHDPlus HR when available.
- `comid` as non-authoritative compatibility field.
- `site_id` + `parameter_code` + timestamp tuple for observations.

## Ambiguity policy
- Unresolved identity ambiguity must be explicit.
- Runtime/release decision should return `ABSTAIN` unless evidence-backed disambiguation exists.
- Ambiguous records are quarantined with reason codes and linkage evidence.

## Required trace fields
- `source_id`
- `as_of`
- `valid_from` / `valid_to` where applicable
- `lineage_ref`
- `confidence` (for joins/derivations)

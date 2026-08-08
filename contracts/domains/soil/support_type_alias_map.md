# Soil SupportTypeAliasMap

Status: PROPOSED_INACTIVE  
Authority: compatibility normalization for the existing Soil support-type profile only.

`SupportTypeAliasMap` records exact legacy Soil vocabulary aliases that may be normalized to the canonical tokens already defined by `pipeline_specs/soil/support_type_profile.v1.json`.

It is not a new global vocabulary, does not add support classes, and does not convert one support class into another.

## Canonical authority

The canonical profile-local tokens remain those in `SoilSupportTypeProfile`:

- `authoritative_static_soil`
- `governed_change_evidence`
- `gridded_derivative_soil`
- `profile_soil_evidence`
- `reference_station_soil_climate`
- `satellite_soil_moisture_grid`
- `soil_interpretation`
- `station_soil_moisture`

Older Soil contract prose still contains three exact alternate machine-like tokens. This compatibility map normalizes only those known aliases:

| Legacy alias | Canonical profile token | Class preserved |
|---|---|---|
| `satellite_grid_soil_moisture` | `satellite_soil_moisture_grid` | satellite grid observation |
| `pedon_evidence` | `profile_soil_evidence` | pedon/profile evidence |
| `interpretation` | `soil_interpretation` | soil interpretation |

Unknown aliases fail closed. Canonical tokens pass through unchanged. An alias may never map to another support class.

## Boundary

Normalization changes vocabulary only. It does not alter source family, source role, spatial support, claim kind, evidence state, policy state, review state, lifecycle state, release state, or publication authority.

The map performs no network access and writes no lifecycle data. A normalized token is not evidence closure, source admission, policy approval, promotion, release, deployment, publication, or public-use permission.

## Rollback

Before merge, close the draft PR. After an authorized merge, revert the complete alias-map slice. No data migration or published-state reversal is required because the profile remains inactive and the normalizer is fixture/test infrastructure only.

# Georeference control-point-set identity — source map

## Mined need

KFM now has separate fixture-first georeference quality lanes for affine residual behavior and resource-space GCP distribution. Those lanes can only be meaningfully compared if they refer to the same underlying control-point set.

The current transform-quality and IIIF fixture shapes embed points independently. Repository search at authoring time found no canonical GCP-set identity profile.

## Adaptation

Introduce a small upstream identity object that binds the exact ordered point IDs, image-resource coordinates, target coordinates, resource dimensions, and synthetic target-unit declaration.

Three deterministic identities allow later profiles to bind at the appropriate level:

- full `set_id` for exact resource+target correspondence;
- `resource_set_hash` for resource-space distribution checks; and
- `target_set_hash` for future target-space checks.

Coordinate JSON spelling is normalized to canonical decimal strings before hashing so `50`, `50.0`, and `50.00` do not mint incompatible identities.

## Deliberate limits

This profile does not establish source provenance or GCP accuracy. It does not introduce real CRS/datum/epoch semantics, image access, transformation, residual quality, spatial-distribution thresholds, evidence resolution, rights/CARE/policy, review approval, release, deployment, or publication.

## Follow-up candidates

1. Add a compatibility adapter that projects an accepted `GeoreferenceControlPointSet` into the existing affine-quality fixture input without changing affine-quality semantics.
2. Bind the spatial-distribution profile to `resource_set_hash` after that profile lands and is independently reviewed.
3. Add real CRS/coordinate-epoch declarations only through a separately reviewed geodetic identity profile.

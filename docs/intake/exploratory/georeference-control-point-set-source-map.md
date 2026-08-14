<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/georeference-control-point-set-source-map
title: Georeference control-point-set identity — source map
type: intake/exploratory
version: v1.1
status: draft
owners: map-steward, docs-steward
created: 2026-08-06
updated: 2026-08-14
policy_label: public
owning_root: docs/
responsibility: Exploratory source-to-repository adaptation record for canonical georeference control-point-set identity.
truth_posture: Proposed implementation source map; does not create source, GCP, evidence, policy, review, release, or publication authority.
related:
  - docs/intake/exploratory/georeference-transform-quality-source-map.md
  - contracts/map/georeference_control_point_set.md
tags: [georeference, gcp, identity, intake, exploratory]
notes: Fixture-only source map for deterministic control-point-set identity.
[/KFM_META_BLOCK_V2] -->

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

1. **Implemented:** `tools/generators/project_georeference_transform_quality.py` validates an accepted `GeoreferenceControlPointSet`, preserves its three identities in a projection wrapper, and maps the exact ordered point set into the existing affine-quality v1 candidate without changing affine-quality semantics.
2. **Implemented:** `tools/generators/project_georeference_spatial_distribution.py` validates an accepted `GeoreferenceControlPointSet`, binds its `resource_set_hash` in a projection wrapper, and maps the exact ordered IDs and resource coordinates into the unchanged spatial-distribution v1 candidate. Target-coordinate-only changes do not change this resource-space projection.
3. Add real CRS/coordinate-epoch declarations only through a separately reviewed geodetic identity profile.

Both adapters are fixture-only, deterministic, no-network, stdout-only by default, and overwrite-denying unless `--force` is explicit. Their embedded candidates remain independently validatable by the existing v1 validators; the wrappers do not create new GCP, quality, evidence, policy, release, or publication authority.

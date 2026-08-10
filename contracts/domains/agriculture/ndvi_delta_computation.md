<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/agriculture/ndvi-delta-computation
title: Deterministic NDVI Delta Computation Contract
type: semantic-contract
version: v0.1.0
status: proposed-fixture-profile
owners: OWNER_TBD — Agriculture steward · Remote-sensing steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; fixture-or-captured-input-only; no-network; non-authoritative
owning_root: contracts/
responsibility: Define the bounded meaning of a deterministic cell-level NDVI delta calculation without source access, raster processing, evidence closure, or publication authority.
truth_posture: cite-or-abstain
related:
  - ../../../tools/generators/compute_ndvi_delta.py
  - ../../../schemas/contracts/v1/domains/agriculture/ndvi_delta_computation.schema.json
  - ../../../fixtures/domains/agriculture/ndvi_delta_computation/cases.json
  - ../../../docs/intake/exploratory/pass-32-ndvi-delta-computation-source-map.md
  - vegetation_connectivity_gate.md
  - hls_ndvi_zonal_materiality.md
[/KFM_META_BLOCK_V2] -->

# Deterministic NDVI Delta Computation

**Status:** `PROPOSED` fixture/captured-input profile
**Source candidate:** Pass 32 `KFM-P32-PROG-0005`

## Purpose

Compute a deterministic per-cell NDVI baseline median, recent median, and delta from caller-supplied scaled red/NIR observations. The computation is a bounded precursor to the existing vegetation connectivity gate; it does not label connected pixels or satisfy that gate.

## Frozen arithmetic

- NDVI is `(NIR - red) / (NIR + red)` represented as signed millionths.
- Division and even-cardinality medians use integer round-half-away-from-zero.
- Scene cloud fraction is expressed in basis points. Equality with `max_scene_cloud_fraction_bps` is rejected because the source proposal requires cloud fraction to be **less than** the maximum.
- A pixel-level cloud mask also rejects the observation.
- Baseline and recent clear-observation minima are explicit inputs.
- Baseline below the configured vegetation floor is `SUPPRESSED_NON_VEGETATED`.
- Delta equality is inclusive: `>= threshold` is `GAIN_CANDIDATE`; `<= -threshold` is `LOSS_CANDIDATE`.
- Other complete calculations are `STABLE`; incomplete clear windows are `INSUFFICIENT_CLEAR_OBSERVATIONS`.

The supplied source proposal uses a `0.15` vegetation floor and a `±0.12` delta threshold. The synthetic fixtures freeze those values as `150000` and `120000` millionths while keeping them explicit in every request.

## Determinism and failure posture

Input objects use exact keys, bounded arrays, unique/disjoint observation identifiers, integer reflectance, and finite strict JSON. Clear observations with `NIR + red == 0` are invalid rather than silently discarded. The output preserves accepted and cloud-rejected identifiers and binds both input and result with SHA-256 over the module's documented canonical JSON subset.

Malformed, ambiguous, over-size, symlink, duplicate-key, or non-finite input fails closed.

## Trust boundary

`GAIN_CANDIDATE` and `LOSS_CANDIDATE` are computational classifications only. They are not observations, alerts, scientific validation, connected vegetation patches, EvidenceBundles, policy or promotion decisions, released map layers, or public claims.

The module performs no network request, raster read, source activation, RAW admission, evidence resolution, promotion, release, publication, or public-use authorization. All such fields are fixed to `false` in the result schema.

## Rollback

Remove this contract and its paired generator, schema, synthetic fixtures, tests, workflow, source map, and generated receipt. The slice creates no external or lifecycle state.

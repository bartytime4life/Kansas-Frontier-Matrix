<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/agriculture/vegetation-connectivity-gate
title: Vegetation Connectivity Gate Assessment Contract
type: semantic-contract
version: v0.1.0
status: proposed-fixture-profile
owners: OWNER_TBD — Agriculture steward · Evidence steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; fixture-only; no-network; non-authoritative
owning_root: contracts/
responsibility: Define the bounded meaning of a precomputed vegetation-component persistence gate without performing raster analysis or authorizing publication.
truth_posture: cite-or-abstain
related:
  - ../../../schemas/contracts/v1/domains/agriculture/vegetation_connectivity_gate.schema.json
  - ../../../tools/validators/domains/agriculture/vegetation_connectivity_gate/validate_connectivity_gate.py
  - ../../../fixtures/domains/agriculture/vegetation_connectivity_gate/cases.json
  - ../../../docs/intake/exploratory/pass-32-vegetation-connectivity-gate-source-map.md
  - hls_ndvi_zonal_materiality.md
  - ndvi_readiness.md
[/KFM_META_BLOCK_V2] -->

# Vegetation Connectivity Gate Assessment

**Status:** `PROPOSED` fixture profile  
**Owning domain:** Agriculture  
**Artifact family:** `VegetationConnectivityGateAssessment`  
**Source candidate:** Pass 32 `KFM-P32-PROG-0006` — connected-component vegetation gate

## Purpose

Define a deterministic, no-network gate over **precomputed synthetic component summaries**. The gate verifies that a proposed NDVI-derived indicator has at least the configured number of spatially coherent components whose area and multi-observation persistence meet declared fixture thresholds.

This contract does **not** calculate NDVI, open raster bytes, label connected pixels, perform geometry operations, establish scientific validity, activate a source, create evidence, make policy, or authorize a public indicator.

## Inputs and bounded meaning

A payload contains:

- one county or HUC12 identifier;
- an ordered set of synthetic observation identifiers;
- references to prior NDVI materiality/readiness assessment candidates;
- fixture thresholds expressed as integers;
- ordered precomputed component summaries;
- a deterministic summary and finite review outcome; and
- an all-false authority posture.

The component summaries use integer square metres and basis points. No implicit unit conversion or floating-point tolerance is permitted.

## Fixture decision rules

Threshold equality is admitted in this fixture profile. A component qualifies only when all conditions hold:

1. `area_m2 >= min_component_area_m2`;
2. the component is present in at least `min_persistent_observations` observations; and
3. its rounded persistence basis points are at least `min_persistence_basis_points`.

Persistence basis points are recomputed as:

```text
round_half_up(10,000 × present_observation_count / total_observation_count)
```

The assessment returns `PROPOSED_INDICATOR_CANDIDATE` only when:

- every input receipt state is `RESOLVED`;
- at least one component passes the area threshold;
- at least one area-qualified component also passes persistence; and
- the number of qualifying components reaches `min_qualifying_component_count`.

Otherwise it returns `HOLD` with the exact sorted reasons applicable to the payload:

- `INPUT_RECEIPT_UNRESOLVED`;
- `AREA_THRESHOLD_NOT_MET`;
- `PERSISTENCE_THRESHOLD_NOT_MET`; or
- `QUALIFYING_COMPONENT_COUNT_NOT_MET`.

## Deterministic integrity rules

- `spec_hash` binds the RFC 8785/JCS canonical payload excluding `spec_hash`.
- Observation IDs, input references, component IDs, and per-component observation IDs are ordered and unique.
- Every component observation ID must exist in the assessment observation set.
- Stored persistence, qualification flags, summary counts, areas, and decision fields must equal recomputed values.
- Findings are finite, sorted, and path-addressed.

## Trust boundary

A valid `PROPOSED_INDICATOR_CANDIDATE` means only that synthetic summaries satisfy this frozen fixture gate. It is not an observation, EvidenceBundle, PolicyDecision, PromotionDecision, ReleaseManifest, agricultural alert, map layer, or published claim.

The profile fixes network, raster processing, source activation, RAW admission, promotion, release, publication, and public-use authority to `false`.

## Rollback

Remove this contract and its paired schema, fixture manifest, validator, tests, workflow, source adaptation record, and generated authoring receipt. The slice creates no live source, raster product, database record, API, cache, release object, or public artifact.

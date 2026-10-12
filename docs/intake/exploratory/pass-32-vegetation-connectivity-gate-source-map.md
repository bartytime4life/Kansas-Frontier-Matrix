<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-vegetation-connectivity-gate-source-map
title: Pass 32 Vegetation Connectivity Gate Source Map
type: source-adaptation-record
version: v0.1.0
status: draft
owners: OWNER_TBD — Agriculture steward · Source steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; fixture-only
owning_root: docs/
responsibility: Record how Pass 32 KFM-P32-PROG-0006 was bounded to a no-network repository validator packet.
truth_posture: cite-or-abstain
related:
  - ../../../contracts/domains/agriculture/vegetation_connectivity_gate.md
  - ../../../contracts/domains/agriculture/hls_ndvi_zonal_materiality.md
  - ../../../contracts/domains/agriculture/ndvi_readiness.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 32 Vegetation Connectivity Gate Source Map

## Candidate

Pass 32 card `KFM-P32-PROG-0006` proposes a connected-component vegetation gate requiring spatially coherent NDVI clusters, area thresholds, and persistence before emitting a `PROPOSED` indicator.

The Pass 32 atlas is a downstream carrier. It does not by itself establish repository placement, scientific validity, source authority, production thresholds, or publication authority.

## Current repository evidence

Implementation inspection used `main@f622ec9fc52dfb762aa39d709094e6c8af749dfb` after merged PR #2245.

The current repository already has agriculture-domain lanes for:

- `HlsNdviZonalMaterialityAssessment`, which validates precomputed county/HUC12 NDVI summary materiality without raster calculation; and
- `NdviReadinessAssessment`, which validates smoke-aware readiness and input-receipt closure without source access or COG generation.

No exact `VegetationConnectivityGateAssessment` contract, schema, validator, fixture family, test, or workflow was found. The new packet extends those verified responsibility lanes rather than creating a root, parallel schema home, or release surface.

## Adaptation decision

The source candidate is narrowed to a fixture-only gate over synthetic **precomputed component summaries**. It validates:

- canonical observation, input, and component identity;
- declared integer area thresholds;
- persistence derived from component membership across observations;
- qualification, summary, and finite decision closure;
- deterministic `spec_hash`; and
- all-false source, lifecycle, release, and publication authority.

The packet explicitly does not implement connected-component labeling over raster pixels. That operation, its neighborhood definition, projection, resolution, edge behavior, scientific fitness, source rights, and production thresholds remain `NEEDS VERIFICATION` before any future raster-processing slice.

## Placement basis

- semantic meaning: `contracts/domains/agriculture/`;
- machine shape: `schemas/contracts/v1/domains/agriculture/`;
- deterministic enforcement: `tools/validators/domains/agriculture/`;
- public-safe synthetic cases: `fixtures/domains/agriculture/`;
- enforcement tests: `tests/validators/domains/agriculture/`;
- source lineage: `docs/intake/exploratory/`;
- authoring process memory: `data/receipts/generated/`; and
- bounded CI: `.github/workflows/`.

ADR-0029 accepted Directory Governance Standard v2; no new responsibility root or authority-changing placement is introduced.

## Non-effects

The packet does not activate a source, read raster bytes, calculate NDVI, create a geometry, admit RAW data, resolve an EvidenceBundle, make a PolicyDecision, approve an indicator, promote lifecycle state, release, deploy, publish, or authorize public use.

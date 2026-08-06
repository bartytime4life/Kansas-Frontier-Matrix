# Fixture-Only USGS Water API Cutover Assessment Contract

**Status:** PROPOSED fixture profile  
**Owning domain:** Hydrology  
**Artifact family:** `UsgsWaterApiCutoverAssessment`  
**Source basis:** *New Ideas 4-2-26.pdf* — legacy NWIS/WaterServices migration and modern Water Data API cutover planning  
**Directory Rules basis:** hydrology meaning belongs under `contracts/domains/hydrology/`; machine shape belongs under `schemas/contracts/v1/domains/hydrology/`; deterministic enforcement belongs under `tools/validators/domains/hydrology/`.

## Purpose

Define a deterministic, no-network assessment for a proposed USGS Water Data connector cutover. The profile verifies that required data roles are represented by active modern endpoint fixtures, legacy dependencies have been inventoried, rewrite mappings are complete, dual-run comparisons are reconciled when used, and the source descriptor state is resolved.

The profile is a review gate only. It does not contact USGS, activate a connector, rewrite a production client, admit source bytes, replace provisional values with approved values, or authorize release.

## Required distinctions

The assessment preserves these source and migration distinctions:

- `modern_waterdata` is distinct from `legacy_waterservices` and `legacy_nwisweb`;
- monitoring-location metadata is administrative, continuous values are observations, and daily values are aggregates;
- `modern_only`, `dual_run`, and `legacy_only` are different operating modes;
- dual-run parity evidence is required before a dual-run candidate can become a cutover candidate;
- a resolved `SourceDescriptor` is necessary but not sufficient for activation;
- `CUTOVER_CANDIDATE` is not production activation, promotion, release, or publication.

## Deterministic rules

A payload is a `CUTOVER_CANDIDATE` only when all conditions hold:

1. the source descriptor state is `RESOLVED`;
2. every required role has an active `modern_waterdata` endpoint fixture;
3. required-role and endpoint collections are canonical and duplicate-free;
4. the rewrite map is complete;
5. no legacy dependencies remain;
6. `modern_only` has no active legacy endpoint;
7. `dual_run` includes an active legacy endpoint and has `COMPLETE` reconciliation with evidence references;
8. the deterministic `spec_hash` matches the canonical payload;
9. governance remains fixture-only and non-releasing.

`HOLD` is used for incomplete but potentially remediable migration state. `DENY` is used for legacy-only reliance, denied source-descriptor state, active legacy endpoints in modern-only mode, or conflicted dual-run evidence. Invalid shape or internally inconsistent decisions produce validator `ERROR`.

## Finite reason codes

- `ACTIVE_LEGACY_ENDPOINT_IN_MODERN_ONLY`
- `DUAL_RUN_LEGACY_ENDPOINT_MISSING`
- `DUAL_RUN_RECONCILIATION_MISSING`
- `DUAL_RUN_CONFLICT`
- `LEGACY_DEPENDENCIES_REMAIN`
- `LEGACY_ONLY_MODE`
- `REQUIRED_ROLE_MISSING`
- `REWRITE_MAP_INCOMPLETE`
- `SOURCE_DESCRIPTOR_DENIED`
- `SOURCE_DESCRIPTOR_UNRESOLVED`

## Trust boundary

This slice does not:

- call `api.waterdata.usgs.gov`, `waterservices.usgs.gov`, NWISWeb, or any live endpoint;
- assert current decommission dates or production endpoint availability;
- activate a `SourceDescriptor`;
- fetch, normalize, compare, or publish hydrologic observations;
- treat daily aggregates as instantaneous observations;
- issue flood, dam-operation, water-rights, safety, or life-safety guidance;
- write any KFM lifecycle state;
- create an `EvidenceBundle`, `PolicyDecision`, `ReleaseManifest`, or public layer.

## Rollback

The slice is additive. Remove the contract, schema, validator, fixtures, tests, workflow, and generated authoring receipt. No source, connector, database, API, cache, release, or published artifact requires cleanup.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-aod-readme
title: data/processed/atmosphere/aod/README.md — Atmosphere AOD Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; aod-raster-lane; remote-sensing-proxy-lane
status: repository-grounded draft; PROPOSED lane contract; payload and runtime enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Remote-sensing steward · AOD steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; remote-sensing-proxy; source-role-preserved; release-gated
tags: [kfm, data, processed, atmosphere, aod, AODRaster, aerosol-optical-depth, remote-sensing, raster, proxy, QA, cloud-mask, evidence, policy, correction, rollback]
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../contracts/domains/atmosphere/SmokeContext.md
  - ../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/AODRaster.schema.json
  - ../../../../policy/domains/atmosphere/
  - ../../../../policy/sensitivity/
  - ../../../raw/atmosphere/
  - ../../../work/atmosphere/
  - ../../../quarantine/atmosphere/
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../catalog/stac/atmosphere/
  - ../../../catalog/dcat/atmosphere/
  - ../../../catalog/prov/atmosphere/
  - ../../../triplets/
  - ../../../published/
  - ../../../proofs/
  - ../../../receipts/
  - ../../../registry/
  - ../../../../release/
notes:
  - "This file preserves the existing path and document identity while aligning the lane to the current data/processed authority contract."
  - "This lane owns normalized AOD raster candidates and supporting metadata, not PM2.5 measurements, ground observations, AQI, proof closure, catalog admission, release authority, public tiles, or health guidance."
  - "The AODRaster semantic contract is substantive, but the paired JSON Schema remains a permissive PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "AOD artifacts must preserve product lineage, source role, pixel/value semantics, QA/cloud masks, spatial/temporal support, uncertainty, correction lineage, evidence, policy, and release posture."
  - "Prior blob and documentation rollback target: 4da0fc85e5ebad0534fcae92149e3b7fad40c9e3."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/aod/` — AOD Raster Candidates

> **One-line purpose.** Own normalized, source-traced aerosol optical depth raster candidates and interpretation sidecars that have passed applicable WORK checks but have not thereby become cataloged, released, public, or valid substitutes for ground-level air-quality measurements.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Character: remote sensing proxy](https://img.shields.io/badge/character-REMOTE__SENSING__MASK-0969da?style=flat-square)](#proxy-boundary)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#validation)

> [!IMPORTANT]
> Directory placement, raster normalization, a successful QA check, a map render, a pull request, or a merge does not create truth, EvidenceBundle closure, catalog admission, policy permission, release approval, or KFM publication.

> [!WARNING]
> AOD is a remotely sensed aerosol-opacity proxy. It is not PM2.5, AQI, a ground sensor observation, an exposure estimate, a smoke-impact conclusion, or health guidance by itself.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Proxy boundary](#proxy-boundary) · [Raster contract](#raster-and-qa-contract) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This child lane owns processed AOD raster candidates under the Atmosphere responsibility segment. Typical artifacts include normalized aerosol optical depth grids, controlled raster references, QA or cloud-mask sidecars, source-vintage metadata, and comparison-ready derivatives.

The lane may support downstream smoke, aerosol, weather, forecast, or air-quality context, but it does not itself establish PM2.5 concentration, AQI, ground-level exposure, visibility impact, smoke impact, health effect, hazard impact, or public-warning state.

## Authority level

**Canonical PROCESSED responsibility; non-public by default.**

This path may own normalized raster candidates and lane-local explanatory sidecars. It does not own:

- source-native satellite products or original pixels;
- object meaning or machine shape;
- EvidenceBundle or proof authority;
- policy, sensitivity, or release decisions;
- catalog, triplet, publication, tile-service, API, UI, map, AI, or download behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/atmosphere/aod/README.md` |
| Version | `v0.2.0` |
| Prior blob | `4da0fc85e5ebad0534fcae92149e3b7fad40c9e3` |
| Parent lane | `data/processed/atmosphere/` |
| Semantic contract | `contracts/domains/atmosphere/AODRaster.md` — CONFIRMED |
| Paired schema | Present, but permissive PROPOSED scaffold with empty `properties` and `additionalProperties: true` |
| Recursive payload inventory | UNKNOWN |
| Validator and CI enforcement | NEEDS VERIFICATION |
| Public readiness | DENY BY DEFAULT |

## What belongs here

Subject to policy, rights, and local convention, this lane may contain:

- normalized aerosol optical depth rasters or controlled references to processed raster assets;
- grid-aligned, clipped, reprojected, mosaicked, resampled, or analysis-ready derivatives with preserved lineage;
- product name, source, collection, platform/sensor or source-system, processing level, version, and algorithm identifiers;
- raster footprint, CRS, transform, resolution, dimensions, tile/chunk layout, nodata, valid range, units or dimensionless semantics, and scale/offset metadata;
- source QA, cloud, snow, glint, confidence, retrieval-status, and validity masks;
- temporal metadata distinguishing source acquisition, observation/valid, retrieval, processing, correction, supersession, release, and withdrawal times where material;
- uncertainty, missingness, coverage, caveat, and fitness-for-use sidecars;
- controlled joins or comparison references to `SmokeContext`, `AirObservation`, `PM25Observation`, weather, wind, forecast, or advisory context when object and source-role boundaries remain explicit;
- lane-local inventory, digest, migration, correction, or disposition notes that do not become parallel authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Source-native satellite products, downloads, original rasters, original QA bands, logs, or source identifiers | `data/raw/atmosphere/` |
| Reprojection experiments, mask tuning, cloud-handling trials, notebooks, temporary mosaics, or unresolved QA work | `data/work/atmosphere/` |
| Rights-unclear, malformed, stale-unclear, unsupported, disputed, unsafe, or source-role-unclear products | `data/quarantine/atmosphere/` |
| PM2.5 observations, AQI reports, ground-sensor measurements, regulatory observations, or modeled concentration products | Their correct Atmosphere object-family lanes |
| Catalog, STAC, DCAT, PROV, graph, proof, receipt, registry, release, policy, schema, validator, fixture, test, pipeline, package, API, UI, tile, or published artifacts | Their governed responsibility roots |
| Exposure, health, visibility, smoke-impact, hazard-impact, emergency, or public-warning conclusions | Separate evidence, policy, domain, and release paths; otherwise abstain |
| Credentials, private endpoints, sensitive processing secrets, or unsafe operational logs | Approved secret and restricted operational systems |

## Inputs

Admitted inputs should be governed WORK products or resolved QUARANTINE exits with, as applicable:

- source identity and rights posture;
- source role and knowledge character;
- raster identity, digest, product version, and algorithm version;
- spatial and temporal support;
- QA, cloud, validity, missingness, and uncertainty context;
- transform and processing lineage;
- contract/schema references;
- validation references and review state.

## Outputs

Outputs are processed raster candidates and interpretation sidecars suitable for downstream catalog, STAC/DCAT/PROV projection, EvidenceBundle assembly, comparison, and release-candidate review.

PROCESSED placement does not mean the asset is public-safe, cataloged, published, released, current, or appropriate for concentration or health interpretation.

## Proxy boundary

`AODRaster` has the `REMOTE_SENSING_MASK` knowledge character. Preserve these boundaries:

| Boundary | Required rule |
|---|---|
| AOD vs. PM2.5 | AOD must not be presented as PM2.5 concentration. Any modeled relationship requires a separate governed method, contract, validation, evidence, policy, and release decision. |
| AOD vs. AQI | AOD is not an AQI report and cannot establish AQI by itself. |
| AOD vs. ground observation | A raster is not a station or sensor reading. |
| AOD vs. model field | Source role must distinguish retrieved remote-sensing products from modeled aerosol fields. |
| AOD vs. SmokeContext | AOD may inform smoke context but does not replace smoke object meaning or Hazards event/impact truth. |
| AOD vs. exposure or health | AOD alone does not prove ground-level exposure, dose, health effect, or safety condition. |
| AOD vs. public map | A render is not release; public display still requires catalog, policy, evidence, release, correction, and rollback closure. |

## Raster and QA contract

These expectations are semantic and **PROPOSED** until enforceable schemas, validators, fixtures, and CI are verified:

| Requirement | Meaning |
|---|---|
| Stable identity | Raster and derivative identities should bind source product, version, temporal scope, spatial support, processing method, and digest where practical. |
| Pixel semantics | Value meaning, units or dimensionless status, scale, offset, valid range, fill/nodata, saturation, and missingness must be explicit. |
| Spatial support | CRS, transform, footprint, resolution, dimensions, alignment, resampling method, and edge effects should be recorded. |
| Temporal support | Acquisition, observation/valid, retrieval, processing, correction, supersession, release, and withdrawal times must remain distinguishable where material. |
| QA and masks | Cloud, snow, glint, confidence, retrieval-status, invalid-pixel, and source QA semantics must remain linked and machine-addressable where possible. |
| Source role | Retrieved, modeled, aggregate, candidate, and synthetic products are not interchangeable. |
| Lineage | Collection, platform/sensor or source-system, processing level, algorithm/version, transforms, and predecessor/successor references should be resolvable. |
| Uncertainty | Quality limits, coverage gaps, retrieval failure modes, model dependence, and fitness-for-use caveats must remain visible. |
| Correction | Reprocessing, corrected granules, supersession, withdrawal, and downstream invalidation require recorded lineage and rollback targets. |
| Evidence | Claims about source, time, extent, product identity, QA, transform, or release should resolve downstream to EvidenceBundle support. |

## Validation

Validate, at minimum:

- path placement and lifecycle stage;
- stable identity, version, and digest;
- source role, rights, and lineage;
- CRS, transform, footprint, resolution, dimensions, nodata, scale, and value semantics;
- QA/cloud/mask references and missingness handling;
- acquisition, retrieval, processing, correction, and freshness state;
- no unsupported AOD-to-PM2.5, AQI, exposure, health, or hazard inference;
- contract/schema references and their actual enforcement scope;
- evidence, policy, catalog, release, correction, and rollback dependencies;
- sensitive or harmful cross-lane joins;
- Markdown links, anchors, metadata, and rollback references.

No complete lane-wide validator was verified. A pass proves only the declared scope of the check that ran.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Material changes should include Atmosphere, remote-sensing, AOD, data, validation, evidence, rights, policy, and release reviewers as applicable.

Independent review is required before changes that affect:

- AOD-to-concentration methods;
- QA interpretation or validity thresholds;
- public raster rendering or tile generation;
- rights or source-role posture;
- cross-lane smoke, observation, health, exposure, or hazard joins;
- correction, supersession, withdrawal, or rollback behavior.

CODEOWNERS routing is not approval evidence.

## Correction and rollback

A corrected or reprocessed product must not silently overwrite the meaning of its predecessor. Preserve:

- predecessor and successor identity;
- correction or reprocessing reason;
- changed source/algorithm/version/QA state;
- affected downstream catalog, graph, proof, tile, cache, export, and AI derivatives;
- invalidation and recomputation status;
- withdrawal or stale-state notice where required;
- tested rollback target.

Documentation rollback target: prior blob `4da0fc85e5ebad0534fcae92149e3b7fad40c9e3`.

## Related folders

- Parent processed lane: [`../README.md`](../README.md)
- Lifecycle parent: [`../../README.md`](../../README.md)
- Contract: [`AODRaster.md`](../../../../contracts/domains/atmosphere/AODRaster.md)
- Paired schema: [`AODRaster.schema.json`](../../../../schemas/contracts/v1/domains/atmosphere/AODRaster.schema.json)
- Adjacent contracts: [`SmokeContext.md`](../../../../contracts/domains/atmosphere/SmokeContext.md) · [`AirObservation.md`](../../../../contracts/domains/atmosphere/AirObservation.md) · [`PM25Observation.md`](../../../../contracts/domains/atmosphere/PM25Observation.md) · [`ForecastContext.md`](../../../../contracts/domains/atmosphere/ForecastContext.md)
- Lifecycle: [`raw/`](../../../raw/atmosphere/) · [`work/`](../../../work/atmosphere/) · [`quarantine/`](../../../quarantine/atmosphere/) · [`catalog/`](../../../catalog/domain/atmosphere/README.md) · [`published/`](../../../published/)
- Trust support: [`proofs/`](../../../proofs/) · [`receipts/`](../../../receipts/) · [`registry/`](../../../registry/) · [`release/`](../../../../release/)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive payload inventory | NEEDS VERIFICATION | Pinned tree, asset families, formats, LFS/external stores, rights, owners |
| Schema enforcement | UNKNOWN | Accepted schema version, required fields, negative fixtures, validator output |
| QA semantics | NEEDS VERIFICATION | Product-specific QA definitions, masks, thresholds, missingness, confidence rules |
| Writers and consumers | UNKNOWN | Connectors, pipelines, tools, catalog builders, API/UI/tile consumers |
| Evidence and release closure | UNKNOWN | EvidenceBundles, receipts, catalog identity agreement, policy decisions, release manifests |
| Correction and invalidation | UNKNOWN | Reprocessing procedure, stale/withdrawal handling, cache and derivative invalidation, rollback drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle role | Preserved and clarified |
| AOD-is-not-PM2.5 boundary | Preserved and strengthened |
| Source, QA, raster, uncertainty, evidence, policy, release, correction, and rollback controls | Preserved and expanded |
| Prior contract and schema references | Preserved with current scaffold status made explicit |
| Prior blob and rollback target | Recorded |
| Payload, source, schema, policy, validator, release, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the lane with the current processed-data authority contract;
- bounded schema and validator claims to verified evidence;
- strengthened proxy, raster, QA, correction, review, and rollback controls;
- changed Markdown only.

[Back to top](#top)

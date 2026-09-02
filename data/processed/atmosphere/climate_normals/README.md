<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-climate-normals-readme
title: data/processed/atmosphere/climate_normals/README.md — Climate-Normal Candidate Lane
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; climate-normal-lane; baseline-context-lane
status: repository-grounded draft; PROPOSED lane contract; schema and runtime enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Climate steward · Baseline steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; baseline-aware; aggregation-aware; release-gated
tags: [kfm, data, processed, atmosphere, climate-normal, ClimateNormal, baseline, reference-period, aggregation, comparability, correction, rollback]
related:
  - ../README.md
  - ../aggregate/climate/README.md
  - ../climate_anomaly/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/ClimateNormal.md
  - ../../../../contracts/domains/atmosphere/ClimateAnomaly.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/ClimateNormal.schema.json
  - ../../../../schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json
  - ../../../../policy/domains/atmosphere/
  - ../../../raw/atmosphere/
  - ../../../work/atmosphere/
  - ../../../quarantine/atmosphere/
  - ../../../catalog/domain/atmosphere/
  - ../../../triplets/
  - ../../../published/
  - ../../../proofs/
  - ../../../receipts/
  - ../../../registry/
  - ../../../../release/
notes:
  - "This file preserves the existing path and document identity while aligning the lane to the current data/processed authority contract."
  - "The lane owns normalized climate-normal candidates and baseline sidecars, not automatically machine-enforced ClimateNormal instances."
  - "The paired ClimateNormal schema is a permissive PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "The broader aggregate/climate lane overlaps this object-named lane; neither may become a parallel truth store without a documented disposition."
  - "Prior blob and rollback target: df6e4807ff75266fa97cc29c8266a76c68b02cdf."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/climate_normals/` — Climate-Normal Candidates

> **One-line purpose.** Own normalized, source-traced, reference-period climate-baseline candidates that have passed applicable WORK checks but have not thereby become cataloged, released, public, or machine-enforced `ClimateNormal` records.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Schema: scaffold](https://img.shields.io/badge/schema-scaffold-d97706?style=flat-square)](#schema-posture)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#validation)

> [!IMPORTANT]
> Directory placement, a successful aggregation, a baseline calculation, a map render, a pull request, or a merge does not create truth, schema enforcement, evidence closure, policy permission, catalog admission, release approval, or KFM publication.

> [!WARNING]
> A climate normal is a declared reference-period baseline. It is not a raw observation, climate anomaly, forecast, model field, attribution claim, trend proof, hazard claim, or public-health conclusion.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Lane disposition](#lane-disposition-and-anti-parallel-authority) · [Baseline contract](#baseline-and-comparability-contract) · [Schema](#schema-posture) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This object-named child lane owns processed climate-normal candidates under the Atmosphere responsibility segment. Typical artifacts represent reference-period baselines, aggregation-ready normal values, baseline grids, station-network summaries, or interpretation sidecars that preserve enough context to explain the source, variable, period, spatial support, method, uncertainty, and correction state.

This lane may support downstream `ClimateAnomaly` comparisons, but it does not itself establish anomaly meaning, attribution, trend significance, event causation, damages, hazard impact, or policy conclusions.

## Authority level

**Canonical PROCESSED responsibility if the object-family lane convention is retained; non-public by default.**

This path may own normalized climate-normal candidates and lane-local explanatory sidecars. It does not own:

- raw source captures or source-native normals;
- semantic object meaning or machine shape;
- policy, rights, or sensitivity decisions;
- EvidenceBundle or proof authority;
- catalog, triplet, release, correction, or publication decisions;
- public API, UI, map, tile, AI, report, or download behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/atmosphere/climate_normals/` |
| Version | `v0.2.0` |
| Prior blob | `df6e4807ff75266fa97cc29c8266a76c68b02cdf` |
| Parent lane | `data/processed/atmosphere/` |
| Overlapping sibling | `data/processed/atmosphere/aggregate/climate/` |
| Semantic contract | `contracts/domains/atmosphere/ClimateNormal.md` — CONFIRMED |
| Machine schema | CONFIRMED file; PROPOSED permissive scaffold |
| Recursive payload inventory | UNKNOWN |
| Active writers and consumers | UNKNOWN |
| Public readiness | DENY BY DEFAULT |

## What belongs here

Subject to steward review and the unresolved lane disposition, this lane may contain:

- normalized reference-period baseline candidates for supported Atmosphere variables;
- station, grid, county, region, basin-adjacent, or other governed spatial baseline products;
- monthly, seasonal, annual, climatological-period, or other reviewed temporal normals;
- baseline dictionaries and references that preserve source identity and reference period;
- method, aggregation, coverage, uncertainty, missingness, interpolation, correction, and quality sidecars;
- stable identity, digest, version, predecessor, successor, and supersession metadata;
- review-ready products for downstream catalog, evidence, anomaly-comparison, and release-candidate assembly;
- lane-local README, inventory, migration, or disposition notes that do not create parallel authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw station observations, source-native grids, source downloads, or source-native normals | `data/raw/atmosphere/` |
| Temporary calculations, joins, interpolation experiments, or QA scratch | `data/work/atmosphere/` |
| Baseline-unclear, rights-unclear, disputed, malformed, unsupported, or unsafe material | `data/quarantine/atmosphere/` |
| Climate-anomaly records | Accepted `climate_anomaly/` lane |
| Observation, forecast, model, AOD, smoke, air-quality, advisory, or hazard objects | Their correct Atmosphere or cross-domain lanes |
| Catalog, STAC, DCAT, PROV, triplet, or graph records | `data/catalog/` and `data/triplets/` |
| Evidence bundles, receipts, source-registry records, policy decisions, release records, and rollback cards | Their governed trust and authority roots |
| Published layers, tiles, downloads, API/UI payloads, or Focus Mode answers | Governed published and delivery interfaces after release |
| Attribution, trend-significance, event-causation, damages, health, or policy conclusions | Separate claim-specific evidence, review, and release paths |

## Inputs

Admissible inputs are governed WORK products or resolved QUARANTINE exits with, as applicable:

- source identity, role, rights, and lineage;
- supported variable and units;
- source, observed, valid, retrieval, processing, release, and correction times where material;
- reference period and baseline-construction method;
- spatial support, coordinate reference system, grid or station-network definition;
- aggregation, weighting, interpolation, missingness, coverage, and quality posture;
- stable identity, version, and digest;
- validation and receipt references.

## Outputs

Outputs are processed climate-normal candidates and sidecars suitable for:

- Atmosphere catalog and metadata projection;
- `ClimateAnomaly` baseline reference;
- EvidenceBundle assembly;
- triplet or graph projection after policy-safe catalog closure;
- release-candidate review.

PROCESSED output remains non-public and is not direct input to normal public clients.

## Lane disposition and anti-parallel authority

The repository contains both:

```text
data/processed/atmosphere/aggregate/climate/
data/processed/atmosphere/climate_normals/
```

The first is a broad aggregate-climate lane; the second is object-named for `ClimateNormal`. Their final relationship is **NEEDS VERIFICATION**.

| Disposition | Meaning | Required control |
|---|---|---|
| Object-family lane is canonical | `climate_normals/` owns normal candidates; aggregate lane references them. | Parent indexes, writers, validators, and migration notes must agree. |
| Aggregate lane is canonical | `aggregate/climate/` owns normal candidates; this lane becomes compatibility/index only. | Stop new canonical writes here and record predecessor/successor links. |
| Both retained with distinct responsibilities | One owns object candidates; one owns mixed aggregates. | Explicit non-overlap contract and tests are required. |
| Unresolved | Current state. | Do not dual-write the same truth-bearing artifact. |

> [!CAUTION]
> Do not copy the same climate-normal candidate into both lanes as independent authority. A migration, alias, or index must preserve one canonical identity, digest, predecessor/successor relation, correction state, and rollback target.

## Baseline and comparability contract

These expectations are semantic and **PROPOSED** until verified validators and CI enforce them.

| Requirement | Meaning |
|---|---|
| Stable identity | Each candidate should have a stable identity tied to source, variable, spatial support, reference period, method, and version where practical. |
| Reference period | Start/end or otherwise explicit baseline period is required; a label alone is insufficient for consequential comparison. |
| Variable identity | Variable, statistic, units, scale, and value semantics must be explicit. |
| Spatial support | Station, grid, county, region, basin-adjacent, or other unit must be declared and versioned where boundaries change. |
| Temporal support | Monthly, seasonal, annual, rolling, or other aggregation window must be explicit. |
| Aggregation method | Weighting, interpolation, compositing, filtering, rounding, and missing-data behavior must be disclosed. |
| Coverage posture | Station count, grid coverage, gaps, exclusions, and network-composition changes should remain visible. |
| Source-role preservation | Observation-derived, modeled, hybrid, aggregate, administrative, candidate, and synthetic inputs must not be collapsed. |
| Comparability | Normals compared across versions must have compatible variable, units, spatial support, temporal support, period, and method—or disclose the mismatch. |
| Anomaly anchor | A downstream `ClimateAnomaly` must reference a specific normal or reviewed baseline identity; it must not rely on an implicit default. |
| Uncertainty | Sampling, interpolation, network, model, and method uncertainty must be preserved where material. |
| Correction lineage | Reprocessed, corrected, superseded, withdrawn, or invalidated baselines must retain predecessor/successor and affected-derivative references. |
| Evidence linkage | Consequential baseline claims should resolve downstream to EvidenceBundle support. |

## Schema posture

The paired schema exists at:

```text
schemas/contracts/v1/domains/atmosphere/ClimateNormal.schema.json
```

Current verified posture:

| Schema fact | Status |
|---|---|
| File exists | CONFIRMED |
| Status is `PROPOSED` | CONFIRMED |
| `properties` is empty | CONFIRMED |
| `additionalProperties` is `true` | CONFIRMED |
| Title is `Climatenormal` | CONFIRMED |
| Field-level enforcement | NOT PRESENT IN THE VERIFIED SCHEMA |
| Validator and fixture enforcement | NEEDS VERIFICATION |

Therefore, presence in this directory or successful validation against the current scaffold must not be described as proof that an artifact satisfies the full `ClimateNormal` semantic contract.

## Validation

Validate, within the declared scope of available checks:

- placement and lane disposition;
- identity, digest, version, predecessor, and successor;
- source role, rights, and lineage;
- reference period and baseline identity;
- variable, statistic, units, scale, and value semantics;
- spatial and temporal support;
- aggregation, weighting, interpolation, coverage, missingness, and uncertainty;
- comparability with related normals and anomaly consumers;
- contract/schema version and actual enforcement scope;
- receipts, evidence references, policy/review state, correction dependencies, and rollback target;
- links, anchors, metadata, and sensitive-content exposure.

No complete lane-wide validator was verified. A passing check proves only its declared scope.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Material changes should involve climate, baseline, source/rights, data, validation, evidence, policy, and release reviewers as applicable.

Independent review is required before consequential changes to:

- reference periods or baseline definitions;
- source-network composition;
- interpolation, weighting, or aggregation methods;
- variable or units semantics;
- lane disposition or migration;
- public-serving, correction, invalidation, or rollback behavior.

CODEOWNERS routing is not approval evidence.

## Correction and rollback

A corrected or superseded normal must not silently overwrite the meaning of an earlier baseline. Record, as applicable:

1. prior and replacement identities and digests;
2. correction, reprocessing, supersession, or withdrawal reason;
3. changed source, period, method, units, coverage, or uncertainty;
4. affected anomaly, map, report, cache, index, graph, and release dependencies;
5. invalidation or rebuild status;
6. review and release decision;
7. rollback target.

Documentation rollback for this change is the prior blob `df6e4807ff75266fa97cc29c8266a76c68b02cdf`. Data rollback requires the governed release and correction artifacts for the affected product; reverting this README does not revert data state.

## Related folders

- Parent: [`data/processed/atmosphere/`](../README.md)
- Broad aggregate climate lane: [`aggregate/climate/`](../aggregate/climate/README.md)
- Anomaly lane: [`climate_anomaly/`](../climate_anomaly/README.md)
- Processed parent contract: [`data/processed/`](../../README.md)
- Contract: [`ClimateNormal`](../../../../contracts/domains/atmosphere/ClimateNormal.md)
- Schema: [`ClimateNormal.schema.json`](../../../../schemas/contracts/v1/domains/atmosphere/ClimateNormal.schema.json)
- Lifecycle siblings: `data/raw/atmosphere/` · `data/work/atmosphere/` · `data/quarantine/atmosphere/` · `data/catalog/` · `data/triplets/` · `data/published/`
- Trust and authority: `data/proofs/` · `data/receipts/` · `data/registry/` · `policy/` · `release/`

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Canonical relationship to `aggregate/climate/` | NEEDS VERIFICATION | Parent indexes, writer inventory, ADR or migration/disposition record |
| Recursive subtree and payload inventory | NEEDS VERIFICATION | Pinned tree, payload families, external stores, rights, owners |
| Writers and consumers | UNKNOWN | Pipelines, tools, workflows, catalog, API/UI, reports, deployed consumers |
| Enforceable schema and validators | UNKNOWN | Accepted schema, fixtures, validators, CI, negative cases |
| Receipt and evidence closure | UNKNOWN | Emitted receipts, EvidenceBundles, identity/digest agreement |
| Anomaly dependency tracking | UNKNOWN | Explicit baseline references and correction propagation |
| Public serving and invalidation | UNKNOWN | Governed routes, caches, stale/correction/withdrawal behavior, drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| Climate-normal baseline purpose | Preserved and clarified |
| `ClimateNormal` versus observation/anomaly/forecast/attribution boundaries | Preserved and strengthened |
| Sibling-lane overlap warning | Preserved and expanded into a disposition contract |
| Rights, evidence, policy, release, correction, and rollback controls | Preserved and strengthened |
| Prior blob and rollback target | Recorded |
| Payload, move, deletion, migration, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the lane with the current processed-data authority model;
- bounded claims to the verified semantic-contract and scaffold-schema evidence;
- added baseline comparability, anti-parallel-authority, correction, verification, and no-loss controls;
- changed Markdown only.

[Back to top](#top)

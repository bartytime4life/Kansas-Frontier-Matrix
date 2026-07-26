<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-wind-field-readme
title: data/processed/atmosphere/wind_field/README.md — Atmosphere WindField Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; wind-field-lane; observed-model-boundary
status: repository-grounded draft; PROPOSED lane contract; runtime and payload enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Weather steward · Wind steward · Forecast/model steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; source-role-preserved; model-is-not-observation; release-gated
tags: [kfm, data, processed, atmosphere, wind-field, WindField, observed-sensor, atmospheric-model-field, vector, gust, model-run, uncertainty, evidence, policy, correction, rollback]
related:
  - ../README.md
  - ../observed/README.md
  - ../weather_observations/README.md
  - ../weather_stations/README.md
  - ../modeled/README.md
  - ../forecast_context/README.md
  - ../smoke_context/README.md
  - ../../../../contracts/domains/atmosphere/WindField.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/WindField.schema.json
  - ../../../../policy/domains/atmosphere/
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../proofs/
  - ../../../receipts/
  - ../../../../release/
notes:
  - "This file preserves the existing path and document identity while aligning the lane to the current data/processed authority contract."
  - "This lane owns normalized wind candidates and interpretation sidecars, not source captures, semantic contracts, machine schemas, proof closure, policy decisions, release authority, or public-serving behavior."
  - "Modeled wind remains ATMOSPHERIC_MODEL_FIELD and must never be promoted or displayed as OBSERVED_SENSOR wind."
  - "Wind speed, direction, vector components, gust semantics, height, station/grid context, model-run lineage, uncertainty, correction, and invalidation must remain explicit."
  - "Prior blob and rollback target: 937f331cdbd65a49c2762c57f0e3eb2932c637f5."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/wind_field/` — Wind Field Candidates

> **One-line purpose.** Own normalized, source-traced wind candidates and sidecars that preserve observed-versus-modeled role, vector semantics, model-run lineage, uncertainty, and correction state without thereby becoming cataloged, released, public, or authoritative hazard conclusions.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Role: model is not observation](https://img.shields.io/badge/model-is%20not%20observation-d1242f?style=flat-square)](#source-role-and-wind-semantics)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#validation)

> [!IMPORTANT]
> Directory placement, a completed vector transform, a model run, a successful check, a map render, a pull request, or a merge does not create truth, EvidenceBundle closure, policy permission, catalog admission, release approval, or KFM publication.

> [!WARNING]
> Modeled, forecast, reanalysis, or gridded wind must remain `ATMOSPHERIC_MODEL_FIELD`. It must never be promoted or displayed as `OBSERVED_SENSOR` wind merely because it has been normalized or rendered alongside station observations.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Semantics](#source-role-and-wind-semantics) · [Vector contract](#vector-and-time-contract) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane holds processed wind-field candidates after source capture, WORK transforms, and any resolved QUARANTINE disposition. Typical artifacts include station wind observations, gridded analyses, forecast or reanalysis wind fields, speed/direction records, vector-component products, gust records, and interpretation sidecars.

The lane may support weather, smoke-transport, climate, advisory, and hazard-context analysis, but it does not itself establish smoke exposure, PM2.5, fire spread, storm impact, crop loss, infrastructure damage, health effect, emergency instruction, or other consequential cross-domain truth.

## Authority level

**Canonical PROCESSED responsibility; non-public by default.**

This path may own normalized wind candidates, grids, vectors, station-linked records, uncertainty fields, model-run references, correction maps, and lane-local explanatory sidecars. It does not own:

- source-native captures or original model/station products;
- semantic object meaning or machine shape;
- station identity or source-registry authority;
- policy, EvidenceBundle, proof, catalog, triplet, release, or publication decisions;
- public API, UI, map, tile, AI, alerting, or download behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/atmosphere/wind_field/` |
| Version | `v0.2.0` |
| Prior blob | `937f331cdbd65a49c2762c57f0e3eb2932c637f5` |
| Semantic contract | `CONFIRMED` — `contracts/domains/atmosphere/WindField.md` |
| Schema posture | `CONFIRMED` permissive PROPOSED scaffold with empty `properties` and `additionalProperties: true` |
| Payload inventory | `UNKNOWN` |
| Active writers/consumers | `UNKNOWN` |
| Public readiness | `DENY BY DEFAULT` |

Because the schema is still permissive scaffolding, a file in this lane is a processed wind candidate or sidecar unless separate evidence proves conformance to an accepted schema, validator, policy, evidence, and release chain.

## What belongs here

Subject to rights, source-role, validation, and sensitivity review:

- observed station wind speed, direction, gust, or vector-component candidates;
- gridded wind analyses and model/reanalysis/forecast wind candidates with explicit model role;
- source, station, grid, model-run, variable, units, height/level, time, QA, uncertainty, and lineage sidecars;
- station/model comparison products that preserve both roles rather than merging them;
- correction, supersession, reprocessing, merge/split, predecessor/successor, and invalidation maps;
- lane-local inventories, digests, migration notes, and disposition metadata.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw station feeds, model products, files, logs, or source-native grids | `data/raw/atmosphere/` |
| Scratch transforms, experiments, unreconciled joins, or temporary QA | `data/work/atmosphere/` |
| Missing-role, missing-model-run, rights-unclear, stale-current, malformed, disputed, or unsafe material | `data/quarantine/atmosphere/` |
| Weather-station identity or exact site metadata | `data/processed/atmosphere/weather_stations/` and governed station authority |
| Generic weather observations without material wind-vector semantics | `data/processed/atmosphere/weather_observations/` or accepted observation lane |
| Forecast/run context that is not itself a wind field | `data/processed/atmosphere/forecast_context/` or `modeled/` |
| Smoke, PM2.5, exposure, hazard-event, impact, damage, or advisory truth | Their governed domain/object lanes |
| Catalog, proof, receipt, registry, release, schema, policy, validator, API/UI, or published artifacts | Their canonical responsibility roots |

Never store secrets, private endpoints, access instructions, harmful station-siting detail, or implementation parameters that enable unauthorized access or unsafe exposure.

## Inputs

Governed WORK products or approved quarantine exits should carry, as applicable:

- stable source and artifact identity;
- `source_role` and knowledge character;
- station/network, grid, source-product, or model-run reference;
- speed, direction, gust, component, height/level, and unit semantics;
- observed, run, valid, retrieval, processing, correction, and supersession times;
- rights, sensitivity, QA, uncertainty, missingness, caveat, and freshness posture;
- transform and validation references.

Missing role, missing units, missing time semantics, or missing model-run/uncertainty for modeled fields should fail closed rather than default plausibly.

## Outputs

Permitted outputs are candidates for downstream catalog/triplet projection, EvidenceBundle assembly, model/observation comparison, and release-candidate review.

PROCESSED placement does not make a wind product public, observed, current, safe, or suitable for operational decisions. Public clients must not read this lane directly.

## Source-role and wind semantics

| Character | Required posture | Must not become |
|---|---|---|
| `OBSERVED_SENSOR` | Station/sensor context, observation time, units, QA, correction, freshness, and evidence support | model, forecast, hazard proof, or advisory instruction |
| `ATMOSPHERIC_MODEL_FIELD` | Model/run identity, initialization/run time, valid time, level/height, grid, uncertainty, caveats, and model receipt | observed sensor data |
| Analysis/reanalysis candidate | Explicit source role and method; relationship to observations and models stated | unqualified observation or forecast truth |
| Aggregate/climate derivative | Aggregation method, period, coverage, uncertainty, and separate object-family routing | source wind observation or climate baseline by implication |

A display or derivative that combines observed and modeled wind must retain the role of each input and must not flatten them into an unlabeled “wind truth” surface.

## Vector and time contract

Every consequential candidate should preserve enough information to distinguish:

- speed from gust;
- direction-from from direction-to conventions;
- scalar speed/direction from `u`/`v` components;
- source units from normalized units;
- observation height or model level;
- instantaneous, averaged, maximum, sustained, or gust windows;
- station-point, grid-cell, raster, vector, or interpolated spatial support;
- observation time from model run, valid, retrieval, processing, release, correction, and supersession time.

Vector conversions must record convention, units, coordinate orientation, formula or implementation version, and round-trip or tolerance checks. Calm, variable, missing, trace-like, and below-detection states must not be collapsed into numeric zero without an explicit rule.

## Validation

No complete lane-wide validator was verified. A passing check proves only its declared scope.

At minimum, validation should cover:

- path and lifecycle placement;
- source and artifact identity/digest/version;
- role separation between observation and model;
- variable, units, convention, height/level, averaging, and vector consistency;
- station/grid/model-run references;
- observed/run/valid/retrieval/correction time ordering and meaning;
- QA, missingness, uncertainty, freshness, and caveat posture;
- rights and sensitivity;
- duplicate, overlap, predecessor/successor, correction, and invalidation state;
- EvidenceRef, policy, catalog, release, and rollback dependencies;
- prohibited model-as-observation, hazard/impact, health, and advisory claims.

Negative fixtures should include missing role, modeled data labeled observed, absent run identity, inconsistent `u`/`v` and speed/direction, ambiguous direction convention, missing height/level, incompatible units, stale-as-current material, and wind-as-hazard-proof claims.

## Review burden

Accountable owners remain **NEEDS VERIFICATION**. Changes affecting source admission, model-run semantics, station joins, vector conventions, uncertainty, rights, sensitivity, public geometry, corrections, or public serving require the relevant domain, model, validation, evidence, policy, and release reviewers.

CODEOWNERS routing or CI success is not approval evidence. Material releases should preserve separation between generation, review, and release authority.

## Correction and rollback

Corrections must be explicit and reversible. A correction should identify:

- affected wind candidate IDs, source products, stations, grids, model runs, and time ranges;
- superseded and replacement digests;
- changed units, vector conventions, QA, uncertainty, or role labels;
- dependent comparisons, smoke/weather derivatives, catalog/triplet projections, caches, indexes, tiles, and released products;
- correction, withdrawal, reprocessing, invalidation, and rollback targets.

Changing model role to observed role is not an ordinary correction. It requires source-role re-admission and full review. Silent in-place replacement is not acceptable where downstream derivatives exist.

Documentation rollback target: restore prior blob `937f331cdbd65a49c2762c57f0e3eb2932c637f5` or revert the implementing commit.

## Related folders

- Parent: [`data/processed/atmosphere/`](../README.md)
- Observation routing: [`observed/`](../observed/README.md) · [`weather_observations/`](../weather_observations/README.md) · [`weather_stations/`](../weather_stations/README.md)
- Model routing: [`modeled/`](../modeled/README.md) · [`forecast_context/`](../forecast_context/README.md)
- Related context: [`smoke_context/`](../smoke_context/README.md) · [`temperature/`](../temperature/README.md) · [`precipitation/`](../precipitation/README.md)
- Authority: [`WindField` contract](../../../../contracts/domains/atmosphere/WindField.md) · [schema](../../../../schemas/contracts/v1/domains/atmosphere/WindField.schema.json)
- Trust support: [`proofs/`](../../../proofs/) · [`receipts/`](../../../receipts/) · [`release/`](../../../../release/)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive subtree/payload inventory | `NEEDS VERIFICATION` | Pinned tree, payload families, external stores, rights, sensitivity, owners |
| Writers and consumers | `UNKNOWN` | Pipeline, model, validator, API/UI, workflow, and deployed-consumer inventory |
| Contract/schema enforcement | `UNKNOWN` | Accepted schema, validators, fixtures, CI and negative cases |
| Model-run and uncertainty closure | `NEEDS VERIFICATION` | Emitted receipts, run identity, valid-time semantics, uncertainty fields |
| Station/grid routing | `NEEDS VERIFICATION` | Canonical station and grid references, duplicate and migration policy |
| Evidence/catalog/release closure | `UNKNOWN` | EvidenceBundles, identity agreement, policy decisions, release and rollback links |
| Public invalidation | `UNKNOWN` | Cache/index/tile invalidation, stale/correction/withdrawal behavior and drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle boundary | Preserved and aligned to the parent contract |
| Observed-versus-modeled distinction | Preserved and strengthened |
| Vector, gust, units, time, model-run, QA, and uncertainty controls | Preserved and expanded |
| Station, forecast, smoke, climate, hazard, and advisory boundaries | Preserved |
| Evidence, policy, release, correction, and rollback controls | Preserved and strengthened |
| Payload, schema, policy, validator, release, runtime, or public-state change | None |
| Prior blob and rollback target | Recorded |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the lane to the current processed-data authority model;
- bounded contents as candidates and sidecars because schema enforcement is unverified;
- strengthened observed/model role, vector, time, uncertainty, correction, and invalidation controls;
- changed Markdown only.

[Back to top](#top)

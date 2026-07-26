<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-temperature-readme
title: data/processed/atmosphere/temperature/README.md — Atmosphere TemperatureObservation Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; temperature-observation-lane
status: repository-grounded draft; PROPOSED lane contract; runtime and payload enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Weather steward · Temperature steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; source-role-preserved; canonical-units-aware; release-gated
tags: [kfm, data, processed, atmosphere, temperature, TemperatureObservation, canonical-units, measurement-height, exposure-context, source-role, QA, correction, rollback]
related:
  - ../README.md
  - ../observed/README.md
  - ../precipitation/README.md
  - ../modeled/README.md
  - ../forecast_context/README.md
  - ../climate_normals/README.md
  - ../climate_anomaly/README.md
  - ../aggregate/climate/README.md
  - ../advisory_context/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/TemperatureObservation.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/TemperatureObservation.schema.json
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
  - "This lane owns normalized temperature candidates and sidecars, not source captures, machine-schema authority, proof closure, release authority, or public-serving behavior."
  - "The TemperatureObservation semantic contract is substantive, while the paired JSON Schema remains a permissive PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "Temperature records must preserve source role, variable/variant identity, units, measurement height or exposure context where material, time semantics, QA, correction lineage, uncertainty, and downstream release dependencies."
  - "Prior blob and rollback target: f4373e3b57b95066f5aa43cbd014931a3b1d90ef."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/temperature/` — Temperature Candidates

> **One-line purpose.** Own normalized, source-traced temperature candidates and interpretation sidecars that have passed applicable WORK checks but have not thereby become validated `TemperatureObservation` instances, cataloged claims, released products, public guidance, or hazard conclusions.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Units: canonical required](https://img.shields.io/badge/units-canonical%20required-1a7f37?style=flat-square)](#temperature-semantics)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#publication-boundary)

> [!IMPORTANT]
> Directory placement, successful normalization, a rendered map, a pull request, or a merge does not create truth, schema enforcement, evidence closure, policy permission, release approval, or KFM publication.

> [!WARNING]
> Temperature values can inform climate, hazards, agriculture, infrastructure, and health analysis, but this lane does not establish heat or cold events, exposure, damage, crop loss, medical risk, emergency guidance, or operational action.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Semantics](#temperature-semantics) · [Schema posture](#schema-posture) · [Routing](#object-family-routing) · [Validation](#validation) · [Review](#review-burden) · [Publication](#publication-boundary) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane owns processed temperature candidates under the Atmosphere responsibility segment. Typical artifacts normalize temperature-related records from governed sources while preserving enough context to explain what was measured or derived, where, when, in which units, under which source role, and with which QA and correction state.

The lane may support downstream climate, weather, hazard, agricultural, infrastructure, or health analysis. It does not itself establish:

- a climate normal or anomaly;
- a forecast or modeled field;
- a heat wave, cold wave, frost, or freeze event;
- exposure, illness, mortality, crop loss, damage, or infrastructure impact;
- advisory, emergency, medical, or life-safety guidance.

## Authority level

**Canonical PROCESSED responsibility; non-public by default.**

This path may own normalized temperature tables, vectors, rasters, observation candidates, derived-index candidates, uncertainty products, and lane-local interpretation sidecars. It does not own:

- source-native captures or raw station payloads;
- semantic contract or machine-schema authority;
- policy, rights, sensitivity, or admissibility decisions;
- EvidenceBundle or proof authority;
- catalog, triplet, release, or publication decisions;
- public API, UI, map, tile, AI, alerting, or download behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Item | Bounded status |
|---|---|
| Path | `data/processed/atmosphere/temperature/` — **CONFIRMED** |
| Prior blob | `f4373e3b57b95066f5aa43cbd014931a3b1d90ef` — **CONFIRMED** |
| Semantic contract | `contracts/domains/atmosphere/TemperatureObservation.md` exists and is substantive — **CONFIRMED** |
| Paired schema | Exists, status `PROPOSED`, empty `properties`, `additionalProperties: true` — **CONFIRMED** |
| Machine enforcement | **UNKNOWN / NEEDS VERIFICATION** |
| Recursive payload inventory | **UNKNOWN** |
| Active writers and consumers | **UNKNOWN** |
| Public readiness | **DENY BY DEFAULT** |

The current schema posture means this README describes candidate-data expectations. It does not claim every artifact in this lane is a machine-validated `TemperatureObservation` instance.

## What belongs here

Subject to source rights, policy, and local conventions, this lane may hold:

- normalized air-temperature candidates;
- source-coded temperature candidates whose meaning is preserved;
- apparent-temperature, heat-index, wind-chill, dew-point, or wet-bulb candidates with explicit methods and inputs;
- minimum, maximum, mean, instantaneous, interval, or aggregate temperature candidates with declared temporal semantics;
- station-, network-, grid-, raster-, or source-product-linked temperature candidates;
- source-role, units, timing, QA, uncertainty, correction, and limitation sidecars;
- migration, inventory, digest, and disposition metadata that does not become a parallel authority;
- candidates prepared for catalog, proof assembly, or release-candidate review.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw station feeds, source grids, source downloads, QA payloads, or logs | `data/raw/atmosphere/` |
| Parsing, conversion trials, derived-index experiments, notebooks, or scratch outputs | `data/work/atmosphere/` |
| Rights-unclear, source-role-unclear, unit-unclear, stale, malformed, disputed, or unsafe material | `data/quarantine/atmosphere/` |
| General weather records without temperature-specific semantics | Accepted `WeatherObservation` lane or parent `observed/` lane |
| Forecast or modeled temperature | `forecast_context/` or `modeled/`, with model role preserved |
| Climate normals or anomalies | `climate_normals/`, `climate_anomaly/`, or accepted aggregate-climate lane |
| Heat/cold event, exposure, impact, health, crop-loss, or infrastructure claims | Governing downstream domain and evidence path |
| Proofs, receipts, catalog records, triplets, policy, release decisions, or public bytes | Their canonical roots |
| Public maps, APIs, tiles, UI payloads, AI answers, alerts, or guidance | Governed released interfaces only |

## Inputs

Admissible inputs are governed WORK products or resolved QUARANTINE exits with, as applicable:

- source identity and source role;
- rights, sensitivity, and citation posture;
- variable and temperature-variant identity;
- source units and intended canonical units;
- observation, valid, retrieval, processing, and correction times;
- station, network, grid, raster, or source-product context;
- measurement height, sensor exposure, shelter, indoor/outdoor, surface/air, or equivalent context when material;
- QA, missingness, uncertainty, provisional/final, and correction state;
- transform and validation references.

## Outputs

Outputs are normalized temperature candidates and sidecars suitable for:

- object-family validation;
- catalog and triplet projection;
- EvidenceBundle or proof assembly;
- climate aggregation with baseline/anomaly separation;
- governed cross-domain analysis;
- release-candidate review.

PROCESSED placement does not make an output public or authoritative.

## Temperature semantics

A temperature candidate should preserve the following distinctions where applicable:

| Dimension | Required distinction |
|---|---|
| Variable | air temperature, surface temperature, apparent temperature, heat index, wind chill, dew point, wet bulb, minimum, maximum, mean, or source-coded variant |
| Source role | observed sensor, meteorological context, archive, model, aggregate, candidate, or other reviewed role |
| Value semantics | instantaneous reading, interval summary, daily extreme, rolling value, derived index, or aggregate |
| Units | source units, canonical units, conversion method/version, precision, and rounding |
| Spatial support | station point, network, grid cell, raster footprint, polygon summary, or source-product footprint |
| Vertical/exposure context | sensor height, shelter/exposure, indoor/outdoor, near-surface, surface skin, or unknown |
| Temporal support | observed time, interval start/end, valid time, retrieval time, processing time, correction time |
| Quality | QA flags, missingness, uncertainty, provisional/final state, correction or supersession state |

### Derived-index rule

Heat index, wind chill, apparent temperature, wet bulb, and similar values are not interchangeable with measured air temperature. A derived candidate should retain:

- method or algorithm identity;
- method version where available;
- required input variables and their source roles;
- units and conversions;
- applicability range and caveats;
- treatment of missing or out-of-range inputs;
- uncertainty and correction lineage.

### Zero, missing, and sentinel rule

A numerical zero is not automatically missing, below detection, unavailable, or not applicable. Source fill values, sentinels, missing states, invalid values, and suppressed values must remain distinct.

## Schema posture

The paired schema is:

```text
schemas/contracts/v1/domains/atmosphere/TemperatureObservation.schema.json
```

Verified current posture:

| Schema fact | Status |
|---|---|
| File exists | **CONFIRMED** |
| Title is `Temperatureobservation` | **CONFIRMED** |
| `x-kfm.status` is `PROPOSED` | **CONFIRMED** |
| `properties` is empty | **CONFIRMED** |
| `additionalProperties` is `true` | **CONFIRMED** |
| Field-level enforcement | **NOT ESTABLISHED** |
| Validator and negative-fixture coverage | **NEEDS VERIFICATION** |

Schema validity under this scaffold cannot prove correct units, source role, temperature variant, method, time semantics, measurement height, QA, evidence, or release readiness.

## Object-family routing

| Record character | Preferred lane | Boundary |
|---|---|---|
| Temperature-specific observed or meteorological candidate | `temperature/` | This lane |
| General weather observation | `weather_observations/` or `observed/` | Do not duplicate temperature authority |
| Station or network metadata | `weather_stations/` | Station context is not a value |
| Forecast/model temperature | `forecast_context/` or `modeled/` | Model is not observation |
| Climate baseline | `climate_normals/` or accepted aggregate lane | Baseline is not observation |
| Climate anomaly | `climate_anomaly/` | Anomaly must reference a baseline |
| Advisory/referral context | `advisory_context/` | Temperature does not create guidance |
| Hazard event or impact | Hazards lane | Temperature is context, not proof |

Do not write the same temperature object into multiple processed lanes as parallel authorities. Use stable references, migration records, or controlled aliases instead of duplicate truth stores.

## Validation

A bounded validation pass should check, at minimum:

- correct lifecycle and domain placement;
- stable identity, version, and digest posture;
- source identity, source role, and rights;
- temperature variable and variant semantics;
- source and canonical units plus conversion details;
- plausible value handling without silently clipping valid extremes;
- station/grid/product and measurement-height/exposure context;
- observed, interval, valid, retrieval, and correction times;
- QA, missingness, uncertainty, provisional/final, and supersession state;
- derived-index method, inputs, applicability, and caveats;
- distinction from model, climate, advisory, hazard, impact, and health claims;
- evidence, policy, release, correction, and rollback dependencies;
- sensitive or harmful-precision exposure.

No lane-wide validator or CI enforcement was verified in this task. A pass proves only the declared scope of the actual check.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Review should include the relevant temperature/weather steward, data steward, validation steward, evidence steward, and policy/release reviewers when claims, source activation, sensitivity, public use, correction, or rollback are affected.

Specialist review is required for:

- unit-conversion or derived-index method changes;
- station exposure or measurement-height interpretation;
- observed/model role changes;
- climate aggregation or baseline dependencies;
- health, exposure, agricultural, infrastructure, or hazard joins;
- public-serving, correction, or rollback behavior.

## Publication boundary

This lane is not a public data service. Public use requires governed downstream support appropriate to significance, including:

- source rights and source role;
- canonical units and visible temperature semantics;
- QA, freshness, uncertainty, and caveats;
- EvidenceRef resolution to EvidenceBundle where claims depend on evidence;
- policy and review state;
- release manifest and public-safe output path;
- correction, supersession, invalidation, and rollback support.

Temperature candidates must not be presented as emergency, medical, occupational, agricultural, engineering, or life-safety guidance.

## Correction and rollback

Corrections should preserve:

- prior identity and digest;
- corrected identity or version;
- reason and evidence for correction;
- affected stations, grids, products, intervals, and derivatives;
- affected climate aggregates, anomaly dependencies, hazard context, maps, tiles, caches, indexes, and AI retrieval products;
- supersession or withdrawal state;
- revalidation and rerelease requirements.

Rollback is required if this lane becomes a RAW or WORK store, quarantine bypass, duplicate object-family authority, proof store, policy authority, catalog or release authority, public-serving shortcut, model-as-observation source, health/hazard guidance source, or publication substitute.

Documentation rollback target: restore blob `f4373e3b57b95066f5aa43cbd014931a3b1d90ef` or revert the modernization commit.

## Related folders

- Parent Atmosphere lane: [`../README.md`](../README.md)
- Parent observed lane: [`../observed/README.md`](../observed/README.md)
- Precipitation sibling: [`../precipitation/README.md`](../precipitation/README.md)
- Model context: [`../forecast_context/README.md`](../forecast_context/README.md) · [`../modeled/README.md`](../modeled/README.md)
- Climate context: [`../climate_normals/README.md`](../climate_normals/README.md) · [`../climate_anomaly/README.md`](../climate_anomaly/README.md) · [`../aggregate/climate/README.md`](../aggregate/climate/README.md)
- Semantic contract: [`../../../../contracts/domains/atmosphere/TemperatureObservation.md`](../../../../contracts/domains/atmosphere/TemperatureObservation.md)
- Paired schema: [`../../../../schemas/contracts/v1/domains/atmosphere/TemperatureObservation.schema.json`](../../../../schemas/contracts/v1/domains/atmosphere/TemperatureObservation.schema.json)
- Lifecycle parents: [`../../../raw/atmosphere/`](../../../raw/atmosphere/) · [`../../../work/atmosphere/`](../../../work/atmosphere/) · [`../../../quarantine/atmosphere/`](../../../quarantine/atmosphere/)
- Downstream: [`../../../catalog/domain/atmosphere/`](../../../catalog/domain/atmosphere/) · [`../../../triplets/`](../../../triplets/) · [`../../../published/`](../../../published/)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive payload inventory | `UNKNOWN` | Pinned tree, payload families, formats, rights, owners |
| Active writers and consumers | `UNKNOWN` | Pipelines, tools, workflows, API/UI, deployed consumers |
| Contract/schema enforcement | `NEEDS VERIFICATION` | Accepted fields, validators, positive/negative fixtures, CI |
| Unit and derived-index enforcement | `NEEDS VERIFICATION` | Conversion registry, method versions, tests, receipts |
| Station exposure and height handling | `NEEDS VERIFICATION` | Source definitions, normalization rules, fixtures |
| Receipt/proof/catalog/release closure | `UNKNOWN` | Emitted instances and identity agreement |
| Correction and invalidation | `UNKNOWN` | Dependency map, cache/index/AI invalidation, drills |
| Public serving | `UNKNOWN` | Governed routes, hosting, access, stale/withdrawal behavior |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED-stage responsibility | Preserved and clarified |
| Temperature-specific semantics | Preserved and expanded |
| Canonical-unit requirement | Preserved and strengthened |
| Observation/model/climate/hazard boundaries | Preserved and strengthened |
| Rights, evidence, policy, release, correction, rollback controls | Preserved |
| Prior blob and rollback target | Recorded |
| Payload, schema, policy, release, runtime, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the README with the current processed-data authority model;
- made the permissive schema posture explicit;
- strengthened temperature semantics, unit, exposure, derived-index, routing, validation, correction, and rollback controls;
- changed Markdown only.

[Back to top](#top)

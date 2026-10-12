<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-precipitation-readme
title: data/processed/atmosphere/precipitation/README.md — Atmosphere PrecipitationObservation Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; precipitation-observation-lane
status: repository-grounded draft; PROPOSED lane contract; runtime and payload enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Weather steward · Precipitation steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; canonical-units-required; source-role-preserved; release-gated
tags: [kfm, data, processed, atmosphere, precipitation, PrecipitationObservation, observed-sensor, meteorological-context, canonical-units, accumulation-window, gauge, radar, grid, evidence, correction, rollback]
related:
  - ../README.md
  - ../observed/README.md
  - ../modeled/README.md
  - ../forecast_context/README.md
  - ../climate_normals/README.md
  - ../climate_anomaly/README.md
  - ../aggregate/climate/README.md
  - ../derived/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/PrecipitationObservation.md
  - ../../../../contracts/domains/atmosphere/WeatherObservation.md
  - ../../../../contracts/domains/atmosphere/WeatherStation.md
  - ../../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../../contracts/domains/atmosphere/ClimateNormal.md
  - ../../../../contracts/domains/atmosphere/ClimateAnomaly.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/PrecipitationObservation.schema.json
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
  - "This lane owns normalized precipitation candidates and sidecars, not source captures, schema authority, proof closure, catalog admission, release authority, or public-serving behavior."
  - "The paired PrecipitationObservation schema remains a permissive PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "Precipitation candidates must preserve variable identity, canonical units, accumulation window, source role, spatial support, time semantics, QA, uncertainty, correction lineage, and release posture."
  - "Precipitation does not prove flood, drought, crop loss, infrastructure damage, hazard impact, or life-safety guidance by itself."
  - "Prior blob and rollback target: 623e90c2ad24b98d85609d7bf9f164411ab5c6a5."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/precipitation/` — Precipitation Candidates

> **One-line purpose.** Own normalized, source-traced, unit-disciplined precipitation candidates that have passed applicable WORK checks but have not thereby become cataloged, released, public, or authoritative hydrology or hazard conclusions.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Units: canonical required](https://img.shields.io/badge/units-canonical%20required-1a7f37?style=flat-square)](#precipitation-semantics)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#outputs)

> [!IMPORTANT]
> Directory placement, a successful unit conversion, a gauge/radar comparison, a rendered map, a pull request, or a merge does not create truth, evidence closure, policy permission, catalog admission, release approval, or KFM publication.

> [!CAUTION]
> Precipitation is weather evidence or meteorological context. It is not, by itself, flood truth, drought truth, crop-loss proof, infrastructure-impact proof, emergency guidance, or a life-safety instruction.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Semantics](#precipitation-semantics) · [Comparability](#comparability-contract) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane holds processed precipitation candidates under the Atmosphere responsibility segment. Typical artifacts represent precipitation amount, accumulation, rate, intensity, phase, type, trace state, or related meteorological context while preserving source role, units, time, spatial support, QA, uncertainty, and correction lineage.

The lane may support downstream weather, climate, hydrology, agriculture, or hazards analysis, but it does not itself establish streamflow, flood extent, drought status, crop damage, infrastructure impact, emergency conditions, or public action guidance.

## Authority level

**Canonical PROCESSED responsibility; non-public by default.**

This path may own normalized precipitation tables, vectors, rasters, grid products, station-linked records, comparison products, uncertainty sidecars, and lane-local documentation. It does not own:

- source-native station, gauge, radar, gridded, or forecast payloads;
- object meaning or machine shape;
- policy, proof, catalog, release, or publication decisions;
- canonical Hydrology or Hazards truth;
- public API, UI, map, tile, AI, alerting, or download behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/atmosphere/precipitation/README.md` |
| Version | `v0.2.0` |
| Prior blob | `623e90c2ad24b98d85609d7bf9f164411ab5c6a5` |
| Semantic contract | `CONFIRMED` at `contracts/domains/atmosphere/PrecipitationObservation.md` |
| Paired schema | `CONFIRMED` file; permissive `PROPOSED` scaffold with empty properties and `additionalProperties: true` |
| Recursive payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Validator and CI enforcement | `NEEDS VERIFICATION` |
| Public readiness | `DENY BY DEFAULT` |

A processed artifact may be contract-informed without being machine-enforced. Until schema, fixtures, validators, and CI are verified, records in this lane are **precipitation candidates**, not automatically validated `PrecipitationObservation` instances.

## What belongs here

Subject to verified local conventions and applicable policy, this lane may contain:

- normalized precipitation amount, accumulation, rate, intensity, type, phase, and trace-state candidates;
- station-, gauge-, grid-, radar-, or source-product-linked precipitation records;
- source-role-preserved observed-sensor or meteorological-context candidates;
- gauge/radar/grid comparison products with explicit method and uncertainty;
- canonical-unit values plus preserved source-unit and conversion lineage;
- QA, missingness, confidence, provisional/final, correction, and limitation sidecars;
- climate-aggregation inputs that remain distinct from climate normals and anomalies;
- lane-local inventory, digest, migration, and disposition notes that do not create parallel authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw station feeds, gauge products, radar/gridded products, source downloads, logs, or QA payloads | `data/raw/atmosphere/` |
| Parsing, unit-conversion experiments, gauge/radar reconciliation work, notebooks, scratch, or unresolved joins | `data/work/atmosphere/` |
| Rights-unclear, role-unclear, unit-unclear, malformed, disputed, stale-sensitive, or unsupported material | `data/quarantine/atmosphere/` |
| Generic weather records lacking precipitation-specific semantics | Appropriate WeatherObservation lane or quarantine pending classification |
| Forecast/model precipitation represented as observation | `forecast_context/` or `modeled/`, with model role preserved |
| Climate normals or anomalies | `climate_normals/`, `climate_anomaly/`, or governed aggregate-climate lane |
| Streamflow, gauge-stage, watershed, inundation, or flood canonical truth | Hydrology responsibility roots |
| Hazard event, impact, damage, emergency, or life-safety claims | Hazards or official-authority systems with separate evidence and governance |
| Catalog, triplet, proof, receipt, registry, release, or published artifacts | Their governed roots |
| Schema, contract, policy, validator, fixture, pipeline, app, API, UI, or tile implementation | Their responsibility roots |

## Inputs

Governed WORK products or approved quarantine exits may enter this lane only with enough support to interpret the candidate. As applicable, inputs should resolve:

- stable candidate identity, version, and digest;
- source identity and source role;
- station, gauge, grid, radar, or source-product context;
- variable and precipitation semantic class;
- source units, canonical units, conversion method, and precision;
- amount, rate, accumulation, intensity, type, phase, or trace meaning;
- accumulation or sampling window;
- observed, source, retrieval, valid, processing, correction, and supersession times;
- spatial support, footprint, grid, station point, or areal support;
- QA, missingness, uncertainty, rights, sensitivity, and limitation posture;
- transform and validation references.

Unresolved unit, time-window, source-role, or spatial-support ambiguity fails closed to WORK or QUARANTINE.

## Outputs

Permitted outputs are candidates for:

- object-family routing and normalization;
- catalog or triplet projection;
- EvidenceBundle and proof assembly;
- climate aggregation or model comparison;
- release-candidate review after policy and validation closure.

PROCESSED remains non-public by default. Public clients must not read this lane directly.

## Precipitation semantics

A precipitation candidate must preserve what the value means.

| Semantic class | Required distinction |
|---|---|
| Amount | Quantity over a declared observation or accumulation window |
| Accumulation | Running or interval total with clear reset/window semantics |
| Rate | Quantity per unit time, not interchangeable with accumulation |
| Intensity | Method-defined severity or rate class with explicit method |
| Type or phase | Rain, snow, sleet, mixed, unknown, or source-specific reviewed class |
| Trace | Detected but below reporting threshold; not zero and not missing |
| Missing | No supported value; must not be encoded as zero or trace |
| Gauge observation | Point or instrument support; not equivalent to radar or grid estimate |
| Radar/grid estimate | Areal or modeled/derived support; source role and method must remain explicit |
| Forecast/model precipitation | Model context, never relabeled observed |

Canonical units are required for comparison, but source values, source units, conversion method, rounding, and precision must remain recoverable through lineage or receipts.

## Comparability contract

Two precipitation candidates are comparable only when the comparison is explicitly supported.

| Dimension | Minimum requirement |
|---|---|
| Variable semantics | Same or explicitly crosswalked amount/rate/accumulation/intensity/type semantics |
| Units | Compatible canonical units with documented conversion |
| Accumulation window | Same window or reviewed normalization method |
| Time basis | Compatible observed/valid periods and timezone/calendar handling |
| Spatial support | Comparable point, grid, radar, basin-adjacent, county, or other declared support |
| Source role | Observation, meteorological context, radar estimate, grid product, and model role remain distinct |
| Gauge/radar treatment | Bias correction, interpolation, compositing, or reconciliation method disclosed |
| Missingness | Missing, zero, trace, below-detection, and not-reported states remain distinct |
| QA | Comparable quality flags, provisional/final state, and correction posture |
| Versioning | Source collection, algorithm, station/network, and processing versions disclosed |

A map overlay or aligned grid does not, by itself, establish comparability.

## Validation

Validation should be deterministic, bounded, and fixture-backed. At minimum, verify:

- path placement and object-family routing;
- stable identity, digest, and version;
- source and source-role trace;
- precipitation semantic class;
- canonical units and source-unit preservation;
- accumulation or sampling window;
- observed, retrieval, valid, processing, and correction time semantics;
- spatial support and CRS where applicable;
- missing, zero, trace, and below-threshold distinctions;
- QA, uncertainty, provisional/final, and correction state;
- gauge/radar/grid/model distinctions;
- rights, sensitivity, evidence, and release dependencies;
- no direct public-serving or cross-domain truth collapse.

No complete precipitation-lane validator was verified. A passing check proves only its declared scope.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Changes should include precipitation/weather, data, pipeline, validation, evidence, and policy reviewers as applicable.

Specialist review is required for:

- canonical-unit or conversion changes;
- accumulation-window reinterpretation;
- gauge/radar/grid reconciliation methods;
- source-role changes;
- station/network or spatial-support changes;
- climate, hydrology, agriculture, or hazards joins;
- correction, invalidation, release, or rollback changes.

CODEOWNERS routing is not approval evidence.

## Correction and rollback

Corrections must preserve predecessor/successor identity and identify dependent artifacts.

A correction should record, as applicable:

1. affected candidate IDs and versions;
2. reason for correction;
3. source or algorithm version change;
4. changed units, window, time, QA, spatial support, or source role;
5. replacement or superseding artifact;
6. dependent catalog, proof, triplet, climate, hydrology, hazards, map, cache, or release objects requiring invalidation;
7. correction notice, review state, and rollback target.

Rollback is required if this lane becomes a RAW store, WORK area, QUARANTINE bypass, generic weather authority, forecast/model authority, climate authority, Hydrology truth store, Hazards truth store, proof store, catalog root, release root, public-serving shortcut, or life-safety guidance source.

Documentation rollback target: prior blob `623e90c2ad24b98d85609d7bf9f164411ab5c6a5`.

## Related folders

- Parent Atmosphere lane: [`../README.md`](../README.md)
- Observed parent lane: [`../observed/README.md`](../observed/README.md)
- Model and forecast context: [`../modeled/README.md`](../modeled/README.md) · [`../forecast_context/README.md`](../forecast_context/README.md)
- Climate context: [`../climate_normals/README.md`](../climate_normals/README.md) · [`../climate_anomaly/README.md`](../climate_anomaly/README.md) · [`../aggregate/climate/README.md`](../aggregate/climate/README.md)
- Semantic contract: [`../../../../contracts/domains/atmosphere/PrecipitationObservation.md`](../../../../contracts/domains/atmosphere/PrecipitationObservation.md)
- Paired schema: [`../../../../schemas/contracts/v1/domains/atmosphere/PrecipitationObservation.schema.json`](../../../../schemas/contracts/v1/domains/atmosphere/PrecipitationObservation.schema.json)
- Lifecycle support: [`../../../raw/atmosphere/`](../../../raw/atmosphere/) · [`../../../work/atmosphere/`](../../../work/atmosphere/) · [`../../../quarantine/atmosphere/`](../../../quarantine/atmosphere/)
- Trust support: [`../../../proofs/`](../../../proofs/) · [`../../../receipts/`](../../../receipts/) · [`../../../registry/`](../../../registry/)
- Downstream authority: [`../../../catalog/domain/atmosphere/`](../../../catalog/domain/atmosphere/) · [`../../../../release/`](../../../../release/) · [`../../../published/`](../../../published/)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive subtree and payload inventory | `NEEDS VERIFICATION` | Pinned tree, payload families, LFS/external stores, owners |
| Writers and consumers | `UNKNOWN` | Connectors, pipelines, tools, workflows, API/UI, deployed consumers |
| Enforceable schema | `NEEDS VERIFICATION` | Non-scaffold schema, required fields, negative cases, compatibility plan |
| Unit and semantic validators | `UNKNOWN` | Fixture-backed canonical-unit, window, trace/missing, and source-role tests |
| Gauge/radar/grid reconciliation | `UNKNOWN` | Methods, receipts, QA thresholds, uncertainty, versioning |
| Evidence/catalog/release closure | `UNKNOWN` | Emitted instances, identity agreement, review, release, rollback links |
| Correction propagation | `UNKNOWN` | Dependency graph, cache/index invalidation, supersession and rollback drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle role | Preserved and clarified |
| Canonical-unit discipline | Preserved and strengthened |
| Amount/rate/accumulation/intensity/type/trace distinctions | Preserved and expanded |
| Weather/model/climate/hydrology/hazards boundaries | Preserved and strengthened |
| Evidence, policy, release, correction, and rollback gates | Preserved |
| Prior blob and rollback target | Recorded |
| Payload, move, deletion, migration, schema, policy, runtime, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the lane to the current processed-data authority model;
- documented the permissive scaffold-schema posture;
- strengthened units, windows, comparability, source-role, correction, and cross-domain boundaries;
- changed Markdown only.

[Back to top](#top)

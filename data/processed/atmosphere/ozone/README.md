<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-ozone-readme
title: data/processed/atmosphere/ozone/README.md — Atmosphere OzoneObservation Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; ozone-observation-lane; air-quality-role-boundary
status: repository-grounded draft; PROPOSED lane contract; schema and runtime enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Air-quality steward · Ozone steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; source-role-preserved; AQI-concentration-separated; release-gated
tags: [kfm, data, processed, atmosphere, ozone, OzoneObservation, OBSERVED_SENSOR, PUBLIC_AQI_REPORT, concentration, AQI, averaging-period, evidence, policy, correction, rollback]
related:
  - ../README.md
  - ../observed/README.md
  - ../air_observations/README.md
  - ../air_stations/README.md
  - ../pm25/README.md
  - ../forecast_context/README.md
  - ../modeled/README.md
  - ../aod/README.md
  - ../smoke_context/README.md
  - ../advisory_context/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/OzoneObservation.md
  - ../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../contracts/domains/atmosphere/AirStation.md
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../contracts/domains/atmosphere/SmokeContext.md
  - ../../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/OzoneObservation.schema.json
  - ../../../../policy/domains/atmosphere/
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/doctrine/trust-membrane.md
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
  - "This lane owns normalized ozone candidates and interpretation sidecars, not source captures, generic air observations, proof closure, policy decisions, release authority, or public-serving behavior."
  - "Ozone concentration and AQI/report posture are separate knowledge characters. A report/index value must never be presented as raw concentration."
  - "The paired OzoneObservation schema is currently a permissive PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "Prior blob and rollback target: e879df17bf3f2f2de8db093a45d4e39dd2b38f68."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/ozone/` — Ozone Observation Candidates

> **One-line purpose.** Own normalized, source-traced ozone observation and ozone report candidates that have passed applicable WORK checks but have not thereby become cataloged, released, public, or authoritative health, compliance, or life-safety conclusions.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Role: separated](https://img.shields.io/badge/AQI%20vs%20concentration-separated-1a7f37?style=flat-square)](#ozone-semantics)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#validation)

> [!IMPORTANT]
> Directory placement, unit conversion, AQI calculation, a successful check, a pull request, or a merge does not create truth, evidence closure, policy permission, catalog admission, release approval, or KFM publication.

> [!WARNING]
> Ozone concentration, AQI/report posture, modeled ozone, station metadata, regulatory archive context, exposure claims, and health guidance are distinct responsibilities. This lane must not collapse them.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Ozone semantics](#ozone-semantics) · [Units and averaging](#units-averaging-and-time) · [Source-role routing](#source-role-and-routing) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane owns processed ozone-related candidates under the Atmosphere responsibility segment. Typical artifacts include concentration observations, public AQI/report records, regulatory/archive candidates, and lane-local sidecars that preserve source, role, units, averaging period, time, QA, freshness, uncertainty, correction, and downstream readiness.

The lane may support downstream air-quality analysis, but it does not itself establish regulatory exceedance, exposure, health effect, medical advice, emergency guidance, or public release.

## Authority level

**Canonical PROCESSED responsibility; non-public by default.**

This path may own normalized ozone values, report/index records, pollutant-specific metadata, QA summaries, correction mappings, and lane-local explanatory sidecars. It does not own:

- source-native feeds or original station payloads;
- semantic object meaning or machine shape;
- station/network authority;
- policy, health, compliance, or release decisions;
- EvidenceBundle or proof authority;
- catalog, triplet, tile, API, UI, alerting, or publication behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/atmosphere/ozone/` |
| Version | `v0.2.0` |
| Prior blob | `e879df17bf3f2f2de8db093a45d4e39dd2b38f68` |
| Semantic contract | `contracts/domains/atmosphere/OzoneObservation.md` exists |
| Machine schema | Exists, but remains a permissive PROPOSED scaffold |
| Recursive payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Public readiness | `DENY BY DEFAULT` |

**CONFIRMED:** target path, current README, `OzoneObservation` contract, paired scaffold schema, parent Atmosphere lane, and AQI/concentration anti-collapse doctrine.

**PROPOSED:** lane-specific fields, routing, validation, correction, and review expectations.

**NEEDS VERIFICATION:** actual payloads, source descriptors, validators, fixtures, CI, policy enforcement, receipts, EvidenceBundles, release state, public consumers, and rollback drills.

## What belongs here

Subject to contract, source-role, rights, QA, and policy review, this lane may contain:

- normalized ozone concentration candidates tied to governed station or network references;
- ozone AQI/report candidates explicitly labeled `PUBLIC_AQI_REPORT` or equivalent reviewed report role;
- regulatory/archive ozone candidates with issuing authority, vintage, role, and evidence support;
- pollutant identity, units, averaging period, observation time, source time, retrieval time, processing time, freshness, QA, uncertainty, and correction sidecars;
- deterministic identity, content digest, predecessor/successor, supersession, and withdrawal metadata;
- review-ready downstream handoff material for catalog, proof assembly, triplet projection, or release-candidate review;
- README, inventory, migration, reconciliation, or disposition documentation that does not become parallel authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw sensor feeds, agency AQI feeds, station payloads, source downloads, QA files, or logs | `data/raw/atmosphere/` |
| Parsing, conversion, AQI calculation, QA experiments, joins, notebooks, or scratch outputs | `data/work/atmosphere/` |
| Unit-unclear, role-unclear, rights-unclear, stale-current, malformed, disputed, or unsafe material | `data/quarantine/atmosphere/` |
| General non-ozone air observations | `data/processed/atmosphere/air_observations/` or accepted object-specific lane |
| PM2.5 observations or PM2.5 AQI/report records | `data/processed/atmosphere/pm25/` |
| Station/network metadata and siting authority | `data/processed/atmosphere/air_stations/` |
| Modeled or forecast ozone fields | `data/processed/atmosphere/modeled/` or `forecast_context/` |
| AOD, smoke masks, or remote-sensing proxies | `data/processed/atmosphere/aod/` or `smoke_context/` |
| Advisory or warning context | `data/processed/atmosphere/advisory_context/` or governed compatibility lane |
| Catalog, proof, receipt, registry, release, schema, policy, validator, API/UI, tile, or published artifacts | Their canonical responsibility roots |

This lane must not contain or imply:

- AQI-to-concentration or concentration-to-AQI substitution without a separately governed method;
- regulatory exceedance proof;
- exposure or health-effect proof;
- medical advice, emergency instruction, or life-safety guidance;
- public alerting or official advisory authority;
- release or publication approval.

## Inputs

Inputs are governed WORK products or resolved QUARANTINE exits with, as applicable:

- `SourceDescriptor` or equivalent source identity;
- pollutant identity explicitly set to ozone;
- source role and knowledge character;
- station/network reference separated from observed value;
- units, scale, precision, and averaging period;
- observed, source, retrieval, processing, correction, and release times kept distinct;
- QA flags, method, detection or reporting conventions, and missingness;
- rights, caveats, uncertainty, correction state, and validation support.

## Outputs

Outputs are non-public processed candidates for:

- ozone-specific catalog records;
- EvidenceRef/EvidenceBundle assembly;
- governed comparison with PM2.5, weather, smoke, AOD, model, or advisory context;
- triplet projection that preserves source role and pollutant identity;
- release-candidate review after policy, evidence, correction, and rollback dependencies close.

PROCESSED placement proves only lifecycle disposition. It does not prove that an ozone value is correct, comparable, current, regulatory, health-relevant, released, or publicly safe.

## Ozone semantics

| Knowledge character | Meaning | Hard boundary |
|---|---|---|
| `OBSERVED_SENSOR` | Ozone concentration observed by an admitted sensor or archive method. | Must carry units, averaging period, station/network context, time, QA, and evidence. |
| `PUBLIC_AQI_REPORT` | Agency or reviewed report/index posture for ozone. | AQI/report is not raw concentration. |
| Regulatory/archive context | Reviewed archive or compliance-adjacent record. | Does not prove exceedance or legal status by directory placement. |
| Modeled/forecast context | Predicted ozone or model field. | Must not be stored or presented as observed ozone. |
| Candidate/synthetic | Candidate or generated derivative. | Must remain labeled and cannot substitute for observation or report authority. |

A single payload must not silently switch roles. When the same source supplies concentration and AQI/report values, those values need separate role-bearing fields or records and explicit linkage.

## Units, averaging, and time

Ozone candidates should preserve enough information to prevent false comparability:

| Dimension | Required posture |
|---|---|
| Pollutant | Explicit ozone identity; do not infer from lane name alone. |
| Units | Original and normalized units, conversion method, scale, precision, and detection/reporting limits where material. |
| Averaging period | Instantaneous, hourly, 8-hour, daily, or other source-defined window must remain explicit. |
| Time | Observation, source publication, retrieval, processing, correction, supersession, and release times remain distinct. |
| Station context | Stable station/network reference, method, and siting sensitivity posture without duplicating station authority. |
| QA | Source flags, invalidation, calibration/correction status, missingness, and provisional/final state. |
| Comparability | Comparisons require compatible units, averaging windows, methods, roles, and temporal support. |

A conversion that changes units does not change source role. An AQI calculation creates a report/index derivative; it does not rewrite the original concentration observation.

## Source role and routing

Route candidates according to their actual knowledge character:

- observed ozone concentration → this lane;
- ozone AQI/report → this lane only with explicit report role;
- generic air observation without ozone-specific semantics → `air_observations/`;
- PM2.5 → `pm25/`;
- station metadata → `air_stations/`;
- modeled ozone → `modeled/` or `forecast_context/`;
- AOD/smoke proxy → `aod/` or `smoke_context/`;
- advisory context → `advisory_context/`;
- unresolved role or unit semantics → quarantine.

Do not duplicate the same ozone truth-bearing record across object-family lanes. Use controlled references, aliases, migration records, or predecessor/successor relations instead.

## Validation

No complete lane-wide validator was verified. A pass proves only the declared scope of the check.

Before a candidate advances, validate as applicable:

- path and object-family placement;
- deterministic identity, version, digest, predecessor/successor, and duplicate state;
- pollutant identity and source role;
- station/network linkage without authority duplication;
- units, scale, precision, conversion, and averaging period;
- observation, source, retrieval, processing, correction, and release times;
- QA flags, provisional/final state, missingness, calibration/correction posture, and caveats;
- AQI/report separation from concentration;
- observed separation from model, proxy, advisory, exposure, health, proof, and release roles;
- rights, sensitivity, evidence, policy, catalog, release, correction, and rollback references;
- links, anchors, metadata, and accidental sensitive-content exposure.

Failure should keep the artifact in WORK, return it to QUARANTINE, or hold it at PROCESSED with a structured reason. Validation must not silently promote or relabel role.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Changes involving any of the following require specialist review:

- source activation or rights changes;
- unit conversion or averaging-period changes;
- AQI calculation or report-role assignment;
- station/network identity or siting sensitivity;
- provisional-to-final correction;
- low-cost or non-reference sensor caveats;
- regulatory/archive posture;
- public-serving, health, compliance, correction, withdrawal, or rollback behavior.

CODEOWNERS routing is not evidence of approval. Release authority must remain distinct from authorship when significance warrants separation of duties.

## Correction and rollback

Corrections must be explicit and traceable. At minimum, a correction should identify:

- affected ozone candidate identities and digests;
- source correction, QA invalidation, unit or averaging-period correction, station reassignment, or role correction;
- predecessor and successor records;
- affected catalog, proof, triplet, release, cache, index, export, and UI dependencies;
- stale, superseded, withdrawn, or invalid state;
- correction notice and rollback target where applicable.

Rollback is required if this lane becomes a RAW source root, WORK scratch area, QUARANTINE bypass, station authority, generic air-observation authority, PM2.5 authority, AQI/concentration substitution path, model-as-observation path, proof store, receipt store, catalog root, release authority, public API/UI shortcut, health-guidance source, alerting surface, or publication shortcut.

Documentation rollback target: prior blob `e879df17bf3f2f2de8db093a45d4e39dd2b38f68`.

## Related folders

- Parent Atmosphere lane: [`../README.md`](../README.md)
- Observed parent: [`../observed/README.md`](../observed/README.md)
- General air observations: [`../air_observations/README.md`](../air_observations/README.md)
- Station context: [`../air_stations/README.md`](../air_stations/README.md)
- PM2.5: [`../pm25/README.md`](../pm25/README.md)
- AOD proxy: [`../aod/README.md`](../aod/README.md)
- Smoke context: [`../smoke_context/README.md`](../smoke_context/README.md)
- Forecast/model context: [`../forecast_context/README.md`](../forecast_context/README.md)
- Advisory context: [`../advisory_context/README.md`](../advisory_context/README.md)
- Semantic contract: [`../../../../contracts/domains/atmosphere/OzoneObservation.md`](../../../../contracts/domains/atmosphere/OzoneObservation.md)
- Machine schema: [`../../../../schemas/contracts/v1/domains/atmosphere/OzoneObservation.schema.json`](../../../../schemas/contracts/v1/domains/atmosphere/OzoneObservation.schema.json)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive payload inventory | `NEEDS VERIFICATION` | Pinned tree, payload families, storage location, rights, owners, sensitivity |
| Writers and consumers | `UNKNOWN` | Pipelines, tools, jobs, API/UI, exports, deployed consumers |
| Schema enforcement | `UNKNOWN` | Non-scaffold schema, fixtures, validator behavior, negative cases |
| AQI method and role enforcement | `UNKNOWN` | Versioned method, unit/averaging inputs, source role, tests, review |
| Station and sensor posture | `UNKNOWN` | Network registry, siting sensitivity, calibration, provisional/final rules |
| Evidence and release closure | `UNKNOWN` | EvidenceBundles, receipts, catalog/triplet agreement, release and rollback links |
| Correction propagation | `UNKNOWN` | Downstream dependency map, cache/index invalidation, drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle role | Preserved and clarified |
| Ozone-specific object-family scope | Preserved |
| AQI/report versus concentration boundary | Preserved and strengthened |
| Station, model, AOD, smoke, advisory, proof, and release boundaries | Preserved and strengthened |
| Evidence, policy, correction, and rollback controls | Preserved and expanded |
| Prior blob and rollback target | Recorded |
| Payload, move, deletion, migration, release, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the lane to the current processed-data authority model;
- documented permissive scaffold-schema posture;
- strengthened pollutant, role, units, averaging-period, QA, time, correction, and routing controls;
- added verification and no-loss ledgers;
- changed Markdown only.

[Back to top](#top)

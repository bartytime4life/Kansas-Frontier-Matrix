<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-observed-readme
title: data/processed/atmosphere/observed/README.md — Atmosphere Observed Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; observed-parent-lane; compatibility-and-routing-guide
status: repository-grounded draft; PROPOSED lane contract; payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Observation steward · Air-quality steward · Weather steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; source-role-preserved; anti-collapse; release-gated
tags: [kfm, data, processed, atmosphere, observed, observation, source-role, anti-collapse, compatibility, evidence, correction, rollback]
related:
  - ../README.md
  - ../air_observations/README.md
  - ../air_stations/README.md
  - ../weather_observations/README.md
  - ../weather_stations/README.md
  - ../temperature/README.md
  - ../precipitation/README.md
  - ../wind_field/README.md
  - ../pm25/README.md
  - ../ozone/README.md
  - ../forecast_context/README.md
  - ../modeled/README.md
  - ../aod/README.md
  - ../smoke_context/README.md
  - ../advisory_context/README.md
  - ../regulatory/README.md
  - ../aggregate/README.md
  - ../derived/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/
  - ../../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../../policy/domains/atmosphere/
  - ../../../raw/atmosphere/
  - ../../../work/atmosphere/
  - ../../../quarantine/atmosphere/
  - ../../../catalog/domain/atmosphere/
  - ../../../proofs/
  - ../../../receipts/
  - ../../../registry/
  - ../../../../release/
notes:
  - "This file preserves the existing `data/processed/atmosphere/observed/` path while clarifying that it is a parent organization and compatibility lane, not a second object-family authority."
  - "Observed Atmosphere values must preserve source role, variable identity, units, observed time, retrieval time, station/network context, QA, correction lineage, caveats, evidence linkage, policy posture, and release state."
  - "Object-specific lanes own normalized records where established; this parent lane must not duplicate `air_observations`, `weather_observations`, `temperature`, `precipitation`, `wind_field`, `pm25`, or `ozone` truth."
  - "Observed values do not become AQI reports, model fields, AOD/smoke proxies, advisories, exposure claims, health guidance, proof, or release authority through placement here."
  - "Prior blob and documentation rollback target: b7849001c720837880581ca3eb68c1ad82c9b53c."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/observed/` — Observed Atmosphere Candidates

> **One-line purpose.** Organize normalized, source-traced observed Atmosphere candidates and route them to the correct object-family lanes without becoming a parallel observation authority, public data service, or proof of atmospheric conditions.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Role: observed](https://img.shields.io/badge/source%20role-observed-1a7f37?style=flat-square)](#observation-semantics)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#validation)

> [!IMPORTANT]
> Directory placement, a normalized value, a successful QA check, a map render, a pull request, or a merge does not create factual truth, EvidenceBundle closure, policy permission, catalog admission, release approval, or KFM publication.

> [!WARNING]
> `observed/` is a parent organization and compatibility lane. Where an object-specific lane exists, new canonical records should be routed there rather than duplicated here.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Observation semantics](#observation-semantics) · [Lane routing](#object-family-routing) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane groups processed Atmosphere observations after applicable normalization and QA-oriented work while keeping them upstream of catalog, proof closure, release, and public serving.

It may organize or temporarily contain observed-value candidates when their final object-family placement is unresolved, but it must not silently become a duplicate home for records already owned by narrower lanes.

## Authority level

**Canonical PROCESSED responsibility for parent organization; non-public by default.**

This path may own:

- lane-local routing inventories;
- compatibility references;
- normalized observed-value candidates awaiting object-family disposition;
- observation-sidecar metadata that does not belong in proofs, receipts, registry, catalog, policy, schema, or release roots.

It does not own:

- raw sensor feeds or original source payloads;
- station/network identity authority;
- semantic contract or schema authority;
- policy, evidence, catalog, release, or public-serving authority;
- canonical object-family records when a narrower lane already owns them.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/atmosphere/observed/` |
| Version | `v0.2.0` |
| Prior blob | `b7849001c720837880581ca3eb68c1ad82c9b53c` |
| Parent lane | `data/processed/atmosphere/` |
| Object-family overlap | CONFIRMED with narrower observed-value lanes |
| Recursive payload inventory | UNKNOWN |
| Active writers and consumers | UNKNOWN |
| Validator and CI enforcement | NEEDS VERIFICATION |
| Public readiness | DENY BY DEFAULT |

## What belongs here

Subject to local steward review, this lane may contain:

- routing manifests that map observed candidates to object-specific lanes;
- compatibility aliases or migration references that do not duplicate canonical truth;
- normalized observed-value candidates whose final family is unresolved;
- records preserving source identity, source role, parameter identity, units, observed time, retrieval time, QA state, uncertainty, correction lineage, and restriction posture;
- lane-local inventory, limitations, disposition, or migration sidecars;
- references to observation-specific artifacts stored in narrower lanes.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw sensor feeds, source-native archives, QA payloads, or logs | `data/raw/atmosphere/` |
| Parsing, correction experiments, joins, notebooks, or scratch work | `data/work/atmosphere/` |
| Rights-unclear, malformed, disputed, source-role-unclear, or unsafe material | `data/quarantine/atmosphere/` |
| General air observations | `data/processed/atmosphere/air_observations/` |
| Weather observations | `data/processed/atmosphere/weather_observations/` |
| Temperature observations | `data/processed/atmosphere/temperature/` |
| Precipitation observations | `data/processed/atmosphere/precipitation/` |
| Wind records | `data/processed/atmosphere/wind_field/`, preserving observed versus modeled role |
| PM2.5 or ozone object-family records | `data/processed/atmosphere/pm25/` or `ozone/` |
| Station or network metadata | `air_stations/` or `weather_stations/` |
| Forecasts and modeled fields | `forecast_context/` or `modeled/` |
| AOD, smoke masks, or remote-sensing proxy products | `aod/` or `smoke_context/` |
| AQI, compliance, or regulatory-report posture | `regulatory/` or the accepted report/index family |
| Advisory or official-source referral context | `advisory_context/` |
| Aggregate or public-safe derivatives | `aggregate/` or `derived/` |
| Catalog, proofs, receipts, registry, release, schemas, policy, validators, tests, apps, APIs, or tiles | Their governed responsibility roots |

## Inputs

Admissible inputs are governed WORK products or resolved quarantine exits with, as applicable:

- source and source-role identity;
- stable object or candidate identity;
- observation, retrieval, processing, release, and correction time distinctions;
- parameter code and human-readable variable meaning;
- units, scale, precision, valid range, and missing-data semantics;
- station, network, grid, or source-product context;
- QA, correction, uncertainty, rights, sensitivity, and caveat posture;
- validation and transform references.

## Outputs

Outputs are routing-ready or object-ready observed candidates for narrower processed lanes, downstream catalog/triplet projection, proof assembly, or release-candidate review.

This lane does not emit public truth directly. Public clients must use governed released interfaces rather than reading this directory.

## Observation semantics

An observed record must preserve the difference between the measured or reported value and adjacent knowledge characters.

| Boundary | Required rule |
|---|---|
| Observation vs. station | The value and the observing site/network are separate objects or references. |
| Observation vs. model | A modeled or forecast field must not be relabeled observed. |
| Observation vs. proxy | AOD, smoke masks, and remote-sensing proxies are not ground observations. |
| Concentration vs. AQI/report | Concentration and report/index semantics remain distinct. |
| Observation vs. advisory | An observation is not an advisory, warning, or life-safety instruction. |
| Observation vs. exposure/impact | A measured value does not prove exposure, health effect, damage, or hazard impact by itself. |
| Observation vs. proof | Schema validity or QA success does not establish EvidenceBundle closure. |
| Observation vs. release | PROCESSED placement does not authorize public use. |

Low-cost or community-sensor observations require explicit correction, calibration, confidence, limitation, source-role, and fitness-for-use posture before consequential use.

## Object-family routing

Where a narrower lane exists, it should own new canonical records. This parent lane should route, index, or hold compatibility state only.

| Candidate family | Preferred lane | Boundary |
|---|---|---|
| General air-quality observation | `../air_observations/` | Not station metadata, AQI report, AOD, model, or advisory. |
| Weather observation | `../weather_observations/` | General meteorological observation; use narrower variable lanes when appropriate. |
| Temperature | `../temperature/` | Does not prove heat/cold hazard or exposure. |
| Precipitation | `../precipitation/` | Does not prove flooding, drought, damage, or crop loss. |
| Wind | `../wind_field/` | Preserve observed versus modeled role. |
| PM2.5 | `../pm25/` | AOD is not PM2.5; low-cost caveats apply. |
| Ozone | `../ozone/` | Concentration and AQI/report posture remain distinct. |

Do not write the same canonical object to both this lane and a narrower lane. If historical duplication exists, record identity mapping, predecessor/successor state, canonical target, correction consequences, and rollback support before migration.

## Validation

No complete lane-wide validator was verified. A validation pass proves only its declared scope.

At minimum, review should test:

- path and object-family routing;
- stable identity, digest, version, and duplicate detection;
- source role and lineage;
- parameter identity and units;
- observation, retrieval, processing, correction, and release times;
- QA flags, valid range, missingness, uncertainty, and caveats;
- station/network reference integrity without collapsing site and value;
- observed-versus-modeled/proxy/report/advisory separation;
- rights, sensitivity, and harmful-precision posture;
- evidence, policy, catalog, release, correction, and rollback dependencies;
- direct-public-path denial.

Failures should remain in WORK, return to QUARANTINE, or produce a structured hold. They must not silently promote.

## Review burden

Accountable owners remain **NEEDS VERIFICATION**. Material changes should include Atmosphere, observation, data, validation, evidence, policy, privacy/sensitivity, and release reviewers as applicable.

Independent review is required before:

- changing canonical routing between this lane and object-specific lanes;
- activating a new source or writer;
- interpreting low-cost sensor data for consequential use;
- changing unit conversion, correction, calibration, or QA semantics;
- exposing station-linked or sensitive location context;
- publishing new public observed-value surfaces;
- changing correction or rollback behavior.

## Correction and rollback

Corrections must preserve lineage rather than silently replacing observations.

A correction or routing change should identify:

- affected object and candidate IDs;
- prior and successor values or lane locations;
- source correction, calibration, or QA reason;
- impacted aggregates, derived products, catalogs, proofs, caches, indexes, and releases;
- correction notice, invalidation set, and rollback target where applicable.

Rollback is required if this lane becomes a duplicate object-family authority, raw/source store, quarantine bypass, catalog root, proof store, receipt store, release authority, public API shortcut, public tile source, health-guidance surface, or model/proxy/report collapse point.

Documentation rollback target: prior blob `b7849001c720837880581ca3eb68c1ad82c9b53c`.

## Related folders

- Parent processed lane: [`../README.md`](../README.md)
- Object-specific observed lanes: [`../air_observations/`](../air_observations/README.md) · [`../weather_observations/`](../weather_observations/README.md) · [`../temperature/`](../temperature/README.md) · [`../precipitation/`](../precipitation/README.md) · [`../wind_field/`](../wind_field/README.md) · [`../pm25/`](../pm25/README.md) · [`../ozone/`](../ozone/README.md)
- Context lanes: [`../air_stations/`](../air_stations/README.md) · [`../weather_stations/`](../weather_stations/README.md) · [`../forecast_context/`](../forecast_context/README.md) · [`../modeled/`](../modeled/README.md) · [`../aod/`](../aod/README.md) · [`../smoke_context/`](../smoke_context/README.md) · [`../advisory_context/`](../advisory_context/README.md)
- Downstream authority: [`../../../catalog/domain/atmosphere/`](../../../catalog/domain/atmosphere/) · [`../../../proofs/`](../../../proofs/) · [`../../../receipts/`](../../../receipts/) · [`../../../../release/`](../../../../release/)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive child and payload inventory | NEEDS VERIFICATION | Pinned tree, payload families, rights/sensitivity, owners |
| Canonical role of `observed/` | NEEDS VERIFICATION | ADR, lane policy, writer/consumer inventory, migration records |
| Active writers and consumers | UNKNOWN | Pipelines, tools, workflows, APIs, UIs, deployed consumers |
| Contract/schema enforcement | UNKNOWN | Accepted contracts, schemas, fixtures, validators, negative cases, CI |
| Correction and duplicate handling | UNKNOWN | Receipts, predecessor/successor mappings, invalidation tests |
| Public serving and rollback | UNKNOWN | Governed routes, release records, cache invalidation, rollback drills |

Unknowns narrow claims and block higher-risk transitions; they do not authorize plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED-stage responsibility | Preserved and clarified |
| Observed-value scope | Preserved |
| Object-family boundaries | Strengthened |
| AQI, AOD, model, advisory, health, and release anti-collapse rules | Preserved and strengthened |
| Child-lane references | Preserved and made routing-explicit |
| Evidence, policy, correction, and rollback controls | Preserved and expanded |
| Payload, schema, policy, release, or runtime change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned this README to the current processed-data authority model;
- clarified parent-lane and compatibility responsibility;
- added object-family routing and anti-parallel-authority controls;
- strengthened observation semantics, validation, correction, and rollback guidance;
- changed Markdown only.

[Back to top](#top)

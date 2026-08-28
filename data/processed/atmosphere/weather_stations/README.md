<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-weather-stations-readme
title: data/processed/atmosphere/weather_stations/README.md — Atmosphere WeatherStation Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; weather-station-lane; network-and-site-context-lane
status: repository-grounded draft; PROPOSED lane contract; runtime and payload enforcement unverified
owners: NEEDS VERIFICATION — Atmosphere steward · Weather steward · Station/network steward · Sensitivity reviewer · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; siting-sensitive; release-gated
tags: [kfm, data, processed, atmosphere, weather-stations, WeatherStation, network-and-site-context, siting, generalization, lineage, correction, rollback]
related:
  - ../README.md
  - ../observed/README.md
  - ../weather_observations/README.md
  - ../temperature/README.md
  - ../precipitation/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/WeatherStation.md
  - ../../../../contracts/domains/atmosphere/WeatherObservation.md
  - ../../../../contracts/domains/atmosphere/TemperatureObservation.md
  - ../../../../contracts/domains/atmosphere/PrecipitationObservation.md
  - ../../../../contracts/domains/atmosphere/WindField.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/WeatherStation.schema.json
  - ../../../../policy/domains/atmosphere/
  - ../../../../policy/sensitivity/
  - ../../../raw/atmosphere/
  - ../../../work/atmosphere/
  - ../../../quarantine/atmosphere/
  - ../../../catalog/domain/atmosphere/
  - ../../../proofs/
  - ../../../receipts/
  - ../../../registry/
  - ../../../../release/
notes:
  - "This file preserves the existing path and document identity while aligning the lane to the current data/processed authority contract."
  - "This lane owns normalized WeatherStation candidates and lineage sidecars, not raw station feeds, observation values, source registry authority, proof closure, policy decisions, release authority, or public-serving behavior."
  - "Exact siting, private-land context, ownership, access, and infrastructure-sensitive details require restriction or generalization before public release."
  - "The paired JSON Schema remains a permissive PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "Prior blob and rollback target: 2b907b518c2ca65bc1b1536ae1cf107a3d10427f."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/weather_stations/` — Weather-Station Candidates

> **One-line purpose.** Own normalized, source-traced, siting-aware weather-station candidates and lineage sidecars that have passed applicable WORK checks but have not thereby become validated `WeatherStation` instances, cataloged records, released products, or public station services.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Character: network and site](https://img.shields.io/badge/character-NETWORK%20AND%20SITE-1a7f37?style=flat-square)](#station-semantics)
[![Siting: restricted](https://img.shields.io/badge/siting-restricted-d1242f?style=flat-square)](#sensitivity-and-public-geometry)

> [!IMPORTANT]
> Directory placement, successful normalization, a rendered map point, a pull request, or a merge does not create station truth, observation truth, evidence closure, policy permission, catalog admission, release approval, or KFM publication.

> [!WARNING]
> Exact station coordinates, private-land context, ownership, access routes, infrastructure-sensitive context, and security-relevant site details must remain restricted, generalized, quarantined, or denied unless evidence-backed policy and release records explicitly allow exposure.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Station semantics](#station-semantics) · [Sensitivity](#sensitivity-and-public-geometry) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane owns processed weather-station and weather-network site candidates under the Atmosphere responsibility segment. Typical artifacts describe station identity, network membership, station class, site status, siting class, source vintage, relocation history, and observation-link context.

The lane may support downstream weather observations, temperature, precipitation, wind, climate aggregation, and public-safe station summaries. It does not itself establish observation values, sensor quality, exact public siting, ownership, access rights, infrastructure risk, hazard impact, or release approval.

## Authority level

**Canonical PROCESSED responsibility; non-public by default.**

This path may own normalized station records, identity crosswalks, lineage tables, generalized public-geometry candidates, sensitivity labels, and lane-local explanatory sidecars. It does not own:

- source-native station feeds or source registry authority;
- observation values or model fields;
- object meaning or machine shape;
- policy or sensitivity decisions;
- EvidenceBundle or proof authority;
- catalog, triplet, release, or publication decisions;
- public API, UI, map, tile, AI, or download behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Item | Bounded result |
|---|---|
| Path | `data/processed/atmosphere/weather_stations/` |
| Version | `v0.2.0` |
| Prior blob | `2b907b518c2ca65bc1b1536ae1cf107a3d10427f` |
| Semantic contract | `contracts/domains/atmosphere/WeatherStation.md` — CONFIRMED |
| Paired schema | Exists, but remains a permissive PROPOSED scaffold |
| Recursive payload inventory | UNKNOWN |
| Active writers and consumers | UNKNOWN |
| Public readiness | DENY BY DEFAULT |

The semantic contract defines `WeatherStation` as `NETWORK_AND_SITE_CONTEXT`. The paired schema currently has empty `properties` and `additionalProperties: true`; therefore this README describes object-ready candidates and governance expectations, not verified machine enforcement.

## What belongs here

- normalized station, network-site, sensor-node, or comparable meteorological site candidates;
- station identity and source-identifier crosswalks that do not become the source registry;
- network membership, station class, site status, siting class, and source-vintage metadata;
- relocation, decommissioning, reactivation, merge, split, rename, correction, and supersession lineage;
- coordinate-precision, sensitivity, and generalized-public-geometry candidates;
- references linking stations to `WeatherObservation`, `TemperatureObservation`, `PrecipitationObservation`, or observed `WindField` candidates while preserving object-family boundaries;
- lane-local inventory, digest, migration, disposition, limitation, and uncertainty sidecars.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Raw station feeds, source exports, network payloads, logs, or original source geometry | `data/raw/atmosphere/` |
| Geocoding trials, duplicate-resolution experiments, relocation matching, sensitivity experiments, or scratch joins | `data/work/atmosphere/` |
| Rights-unclear, source-role-unclear, disputed, exact-siting-sensitive, ownership/access-sensitive, or unsafe station material | `data/quarantine/atmosphere/` |
| Weather, temperature, precipitation, or wind values | Their object-specific PROCESSED lanes |
| Forecast/model grids or runs | `forecast_context/` or `modeled/` lanes |
| Climate normals or anomalies | Climate-specific processed lanes |
| Source registry records | `data/registry/` |
| Proofs, receipts, catalog records, triplets, releases, and published products | Their governed roots |
| Exact public coordinates, private access instructions, ownership details, or site-security details | Restrict, generalize, quarantine, or deny |

## Inputs

Inputs should be governed WORK products or approved quarantine exits with, as applicable:

- source and network identity;
- source role and rights posture;
- station identifiers and alias history;
- spatial reference and coordinate precision;
- station class, site status, and siting class;
- temporal validity and source vintage;
- sensitivity classification;
- transform and validation references;
- correction and predecessor/successor context.

Unknown or conflicting identity, unresolved exact-siting sensitivity, unclear ownership/access context, or missing rights support must fail closed.

## Outputs

Outputs are normalized station candidates and sidecars suitable for:

- object-family validation;
- observation linkage;
- catalog and triplet preparation;
- EvidenceBundle assembly;
- public-safe geometry review;
- release-candidate review.

PROCESSED remains non-public. Public clients must not read this lane directly.

## Station semantics

`WeatherStation` is network-and-site context, not a weather value.

| Boundary | Required distinction |
|---|---|
| Station vs. observation | Station identifies site/network context; observation carries a measured or contextual value. |
| Station vs. temperature | Temperature values remain in `temperature/`. |
| Station vs. precipitation | Precipitation values remain in `precipitation/`. |
| Station vs. wind | Observed wind may reference a station; modeled wind remains model context. |
| Station vs. forecast/model | Forecast grids, model runs, and model nodes are not station metadata. |
| Station vs. climate | Climate normals/anomalies may use station-derived aggregates but remain separate objects. |
| Station vs. proof | Station metadata does not prove attached observations, quality, ownership, or public safety. |
| Station vs. release | Processed placement does not authorize public map or API exposure. |

Station identity should preserve, where applicable:

- stable station identifier;
- source and network identifiers;
- aliases and prior names;
- network membership periods;
- station class and observing program;
- operational, inactive, relocated, merged, split, decommissioned, or unknown status;
- valid-from and valid-to times;
- predecessor and successor references;
- source vintage and correction lineage.

## Sensitivity and public geometry

Public geometry is a governed derivative, not the canonical station location.

Before public consideration, review:

- coordinate precision and source-provided accuracy;
- private-land or controlled-access context;
- ownership and operator information;
- infrastructure sensitivity;
- security or tampering risk;
- access-route or maintenance-route exposure;
- whether generalization, centroiding, masking, aggregation, or denial is required;
- whether generalized geometry remains fit for the intended public use.

Do not store transform secrets, exact offsets, seeds, restricted precision thresholds, private access instructions, or credentials in this README or ordinary public documentation.

## Validation

A candidate should fail closed unless the declared check scope supports, as applicable:

- stable identity and duplicate resolution;
- source/network trace and source role;
- station class and status semantics;
- spatial reference, coordinate precision, and siting class;
- temporal validity and relocation/decommissioning history;
- rights and sensitivity posture;
- observation-link integrity without value duplication;
- correction, predecessor/successor, merge/split, and supersession lineage;
- public-geometry transform references where applicable;
- evidence, catalog, policy, release, correction, and rollback dependencies.

No complete lane-wide validator was verified. A schema pass against the current scaffold does not prove these requirements, station truth, or publication readiness.

## Review burden

Accountable owners remain **NEEDS VERIFICATION**. Material changes should include:

- Atmosphere and station/network stewardship;
- source and rights review;
- privacy/sensitivity or infrastructure review where exact siting or access context is involved;
- validation and evidence review;
- release review for any public geometry or station summary.

A documentation review, CODEOWNERS route, schema pass, or map preview is not release approval.

## Correction and rollback

Corrections must preserve the prior state and identify affected downstream dependencies.

Correction cases include:

- duplicate stations discovered after normalization;
- station merge or split;
- relocation or coordinate correction;
- network reassignment;
- status correction or decommissioning;
- ownership/access classification change;
- sensitivity reclassification;
- source-vintage supersession;
- invalid public generalization.

Required downstream review may include observation links, aggregates, catalog records, triplets, EvidenceBundles, published station summaries, caches, indexes, and released map layers. Do not silently overwrite identity or geometry.

Documentation rollback target: prior blob `2b907b518c2ca65bc1b1536ae1cf107a3d10427f`.

## Related folders

- Parent Atmosphere lane: [`../README.md`](../README.md)
- Observed parent lane: [`../observed/README.md`](../observed/README.md)
- Weather observations: [`../weather_observations/README.md`](../weather_observations/README.md)
- Temperature: [`../temperature/README.md`](../temperature/README.md)
- Precipitation: [`../precipitation/README.md`](../precipitation/README.md)
- Semantic contract: [`../../../../contracts/domains/atmosphere/WeatherStation.md`](../../../../contracts/domains/atmosphere/WeatherStation.md)
- Paired schema: [`../../../../schemas/contracts/v1/domains/atmosphere/WeatherStation.schema.json`](../../../../schemas/contracts/v1/domains/atmosphere/WeatherStation.schema.json)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive station payload inventory | NEEDS VERIFICATION | Pinned tree, payload families, LFS/external stores, owners |
| Canonical station identity and duplicate rules | UNKNOWN | Contracts, schema, crosswalks, fixtures, validators, negative cases |
| Siting and public-geometry enforcement | UNKNOWN | Policy decisions, transform receipts, fixtures, CI, release records |
| Writers and consumers | UNKNOWN | Pipelines, tools, APIs, UI, catalog, graph, release consumers |
| Correction and invalidation closure | UNKNOWN | Receipts, dependency maps, cache/index invalidation, rollback drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle role | Preserved and clarified |
| WeatherStation network/site semantics | Preserved and strengthened |
| Exact-siting and access sensitivity | Preserved and strengthened |
| Observation, model, climate, proof, and release boundaries | Preserved |
| Correction and rollback posture | Expanded |
| Payload, migration, release, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the README with the current PROCESSED authority model;
- bounded schema maturity to verified scaffold evidence;
- strengthened station identity, siting, sensitivity, lineage, correction, and rollback controls;
- changed Markdown only.

[Back to top](#top)

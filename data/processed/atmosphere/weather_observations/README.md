<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-weather-observations-readme
title: data/processed/atmosphere/weather_observations/README.md — Atmosphere WeatherObservation Processed Data README
version: v0.1
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; weather-observation-lane
status: draft; PROPOSED; data-root; processed-stage; atmosphere; weather-observations; WeatherObservation; release-gated; role-tagging-aware; source-role-aware
owners: OWNER_TBD — Atmosphere steward · Weather steward · Observation steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — one-character placeholder existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; processed; atmosphere; weather-observations; lifecycle; governed; release-gated
tags: [kfm, data, processed, atmosphere, weather-observations, WeatherObservation, WeatherStation, TemperatureObservation, PrecipitationObservation, WindField, ForecastContext, ClimateNormal, ClimateAnomaly, AdvisoryContext, observed-sensor, meteorological-context, role-tagging, lifecycle, RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, EvidenceBundle, SourceDescriptor, RunReceipt, ValidationReport, PolicyDecision, ReleaseManifest]
related:
  - ../README.md
  - ../observed/README.md
  - ../temperature/README.md
  - ../precipitation/README.md
  - ../modeled/README.md
  - ../forecast_context/README.md
  - ../climate_normals/README.md
  - ../climate_anomaly/README.md
  - ../aggregate/climate/README.md
  - ../advisory_context/README.md
  - ../derived/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/WeatherObservation.md
  - ../../../../contracts/domains/atmosphere/WeatherStation.md
  - ../../../../contracts/domains/atmosphere/TemperatureObservation.md
  - ../../../../contracts/domains/atmosphere/PrecipitationObservation.md
  - ../../../../contracts/domains/atmosphere/WindField.md
  - ../../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../../contracts/domains/atmosphere/ClimateNormal.md
  - ../../../../contracts/domains/atmosphere/ClimateAnomaly.md
  - ../../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json
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
  - ../../../../pipelines/
  - ../../../../tools/validators/
notes:
  - "This file replaces a one-character placeholder at `data/processed/atmosphere/weather_observations/README.md`."
  - "This is the PROCESSED-stage sublane for normalized WeatherObservation artifacts under Atmosphere. It is not RAW station/gridded storage, weather-station metadata authority, temperature/precipitation/wind specialization authority, forecast/model authority, climate baseline/anomaly authority, hazards/advisory truth, proof storage, release authority, public API/UI output, or life-safety guidance."
  - "WeatherObservation artifacts must preserve source role, context-vs-primary-claim role, station/grid/source-product context, units, observed time, retrieval time, valid time, QA/correction posture, evidence linkage, policy posture, and release state before public use."
  - "The WeatherObservation contract defines object meaning; this README does not create a second contract or schema authority."
  - "Use TemperatureObservation, PrecipitationObservation, or WindField when variable-specific semantics, units, or model role matter."
  - "Rollback target for this expansion is previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/processed/atmosphere/weather_observations

> Atmosphere PROCESSED-stage sublane for normalized `WeatherObservation` artifacts: governed general meteorological observations, weather-context records, and source-role-tagged weather values that remain distinct from weather-station metadata, variable-specific temperature/precipitation/wind objects, forecast/model fields, climate baselines/anomalies, hazards/advisories, proof, release, and public map/API/UI surfaces.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data/processed/atmosphere/weather_observations" src="https://img.shields.io/badge/root-data%2Fprocessed%2Fatmosphere%2Fweather__observations-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Object: WeatherObservation" src="https://img.shields.io/badge/object-WeatherObservation-purple">
  <img alt="Lifecycle: PROCESSED" src="https://img.shields.io/badge/lifecycle-PROCESSED-purple">
  <img alt="Exposure: not public" src="https://img.shields.io/badge/exposure-not__public-critical">
</p>

**Status:** draft / PROPOSED  
**Owners:** OWNER_TBD — Atmosphere steward · Weather steward · Observation steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward  
**Path:** `data/processed/atmosphere/weather_observations/README.md`  
**Owning root:** `data/processed/`  
**Domain segment:** `atmosphere`  
**Object-family segment:** `weather_observations` / `WeatherObservation`  
**Lifecycle stage:** `PROCESSED`  
**Exposure posture:** not public by default; public use requires governed catalog, evidence, source-role/context-role/freshness/caveat posture, policy, release, correction, and rollback linkage  
**Truth posture:** CONFIRMED target was a one-character placeholder · CONFIRMED `WeatherObservation` contract and schema paths exist · CONFIRMED weather observations have role-dependent `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT` character with role tagging required · PROPOSED weather-observation processed-sublane details · NEEDS VERIFICATION for actual child inventory, validators, receipts, CI enforcement, release linkage, and governed route behavior.

**Quick jumps:** [Purpose](#purpose) · [Lifecycle boundary](#lifecycle-boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [WeatherObservation requirements](#weatherobservation-requirements) · [Weather guardrails](#weather-guardrails) · [Directory map](#directory-map) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/processed/atmosphere/weather_observations/` holds normalized general weather-observation artifacts that have moved beyond RAW capture, WORK transforms, and QUARANTINE holds.

This lane is for processed `WeatherObservation` records or derivatives that preserve source role, context-vs-primary-claim role, station/network/grid/source-product context, source identity, observed time, retrieval time, valid time where applicable, units, QA/correction posture, freshness, evidence references, and downstream catalog readiness.

It is not a weather-station metadata lane. It is not a temperature, precipitation, or wind specialization lane when variable-specific semantics matter. It is not a forecast/model lane. It is not climate baseline/anomaly authority. It is not hazards event/impact truth. It is not advisory issuance, proof store, receipt store, source registry, catalog, release, semantic contract, schema, policy, public layer, public API/UI surface, or life-safety guidance source. It may support downstream catalog records, EvidenceBundle-backed UI payloads, public-safe weather layers, climate aggregation, hazards context, Focus Mode summaries, or release packages only after gates pass.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

```mermaid
flowchart LR
  RAW[data/raw/atmosphere] --> WORK[data/work/atmosphere]
  WORK --> QUAR[data/quarantine/atmosphere]
  WORK --> WOBS[data/processed/atmosphere/weather_observations]
  QUAR --> WOBS
  WOBS --> OBS[data/processed/atmosphere/observed]
  WOBS --> TEMP[data/processed/atmosphere/temperature]
  WOBS --> PRCP[data/processed/atmosphere/precipitation]
  WOBS --> CLIM[data/processed/atmosphere/aggregate/climate]
  WOBS --> CAT[data/catalog/domain/atmosphere]
  WOBS --> STAC[data/catalog/stac/atmosphere]
  WOBS --> DCAT[data/catalog/dcat/atmosphere]
  WOBS --> PROV[data/catalog/prov/atmosphere]
  WOBS -. supports .-> PROOF[data/proofs]
  WOBS -. emits / references .-> RECEIPT[data/receipts]
  CAT --> TRIP[data/triplets/.../atmosphere]
  CAT --> PUB[data/published/.../atmosphere]
  STAC --> PUB
  DCAT --> PUB
  PROV --> PUB
  TRIP --> PUB
  PUB --> REL[release]
```

`data/processed/atmosphere/weather_observations/` is upstream of catalog, triplet, publication, and release. It must not be used as a normal public map/API/UI/AI source.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Raw station feeds, mesonet feeds, gridded products, source downloads, QA payloads, or logs | `data/raw/atmosphere/` | Not this lane. |
| In-process weather parsing, unit normalization, station/grid reconciliation, QA, joins, scratch outputs, or method experiments | `data/work/atmosphere/` | Not this lane. |
| Rights-unclear, source-role-unclear, stale, malformed, unit-unclear, unsupported, disputed, sensitive, or unsafe weather material | `data/quarantine/atmosphere/` | Not this lane until resolved. |
| Normalized WeatherObservation processed artifacts | `data/processed/atmosphere/weather_observations/` | This lane. |
| Observed parent lane | `data/processed/atmosphere/observed/` | Parent/sibling role lane for observed products. |
| Temperature-specific processed artifacts | `data/processed/atmosphere/temperature/` | Use when temperature-specific semantics, units, height/exposure, or heat/cold context matter. |
| Precipitation-specific processed artifacts | `data/processed/atmosphere/precipitation/` | Use when amount, accumulation, trace state, type, gauge/radar method, or canonical-unit rules matter. |
| Wind-specific processed artifacts | WindField processed lane if accepted | Wind can be observed or modeled; role must remain explicit. |
| Weather station/network context | WeatherStation processed lane if accepted | Station metadata is context, not weather observation value. |
| Forecast/model context | `data/processed/atmosphere/forecast_context/` or `data/processed/atmosphere/modeled/` | Forecast/model weather must not impersonate observed weather. |
| Climate normals/anomalies | `data/processed/atmosphere/climate_normals/`, `climate_anomaly/`, or `aggregate/climate/` | Climate products may aggregate weather values but remain separate objects. |
| Advisory/referral context | `data/processed/atmosphere/advisory_context/` | Advisory context remains official-source referral, not WeatherObservation truth. |
| Hazards/event/impact claims | Hazards responsibility roots | Weather observations can contextualize hazards; they do not prove impact. |
| Atmosphere domain catalog records | `data/catalog/domain/atmosphere/` | Downstream catalog stage. |
| Atmosphere STAC/DCAT/PROV records | `data/catalog/{stac,dcat,prov}/atmosphere/` | Downstream catalog projections, if accepted. |
| Atmosphere triplet/graph projections | `data/triplets/.../atmosphere/` | Downstream graph stage. |
| Atmosphere public-safe products | `data/published/.../atmosphere/` | Downstream after release. |
| EvidenceBundle/proof records | `data/proofs/` | Separate proof family. |
| Source, run, transform, validation, policy, correction, and release receipts | `data/receipts/` | Separate receipt family. |
| SourceDescriptor/source registry records | `data/registry/` | Separate registry family. |
| Release decisions, manifests, rollback cards, corrections, withdrawals | `release/` | Separate publication authority. |
| WeatherObservation semantic contract | `contracts/domains/atmosphere/WeatherObservation.md` | Object meaning; not data. |
| WeatherObservation schema | `schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json` | Machine shape; not data. |
| Policy, validators, tests, pipelines, apps, packages | `policy/`, `tools/validators/`, `tests/`, `pipelines/`, `apps/`, `packages/` | Separate roots. |

## Accepted contents

Processed `WeatherObservation` data may include:

- normalized general meteorological observation records tied to a weather station, mesonet station, grid cell, source product, archive, or station/network context;
- source-role-preserving records where `OBSERVED_SENSOR`, `METEOROLOGICAL_CONTEXT`, station, grid, archive, or other admitted role remains explicit;
- context-vs-primary-claim tags where the same source value can support another claim or stand as the claim being inspected;
- weather value, units, observed time, retrieval time, valid time where relevant, source time, QA state, correction lineage, freshness, caveats, confidence, and limitation metadata;
- source-role-aware comparison or joins with `TemperatureObservation`, `PrecipitationObservation`, `WindField`, `ForecastContext`, `ClimateNormal`, `ClimateAnomaly`, or `AdvisoryContext` when object meanings remain visible;
- quality, caveat, missingness, correction, uncertainty, freshness, validation, unit-normalization, and context-role sidecars when those sidecars are not proofs, receipts, source registry records, catalog records, schemas, or policy rules;
- processed artifacts prepared for downstream domain catalog, STAC/DCAT/PROV packaging, EvidenceBundle support, triplet generation, or release review.

## Exclusions

Do not store these under `data/processed/atmosphere/weather_observations/`:

- RAW station feeds, mesonet feeds, gridded products, source downloads, QA payloads, logs, screenshots, or source-native records.
- WORK/scratch outputs that have not passed processing gates.
- Quarantined, malformed, source-role-unclear, rights-unclear, stale, unit-unclear, unsupported, disputed, sensitive, or unsafe weather material.
- Weather station/network metadata, station ownership/access details, or exact station-siting authority.
- Temperature, precipitation, or wind records when variable-specific semantics, units, height/exposure, method, model role, or aggregation rules require specialized objects.
- Forecast/model fields, climate normal records, climate anomaly records, advisory/referral records, hydrology records, hazards records, agriculture records, infrastructure records, or health/exposure records unless only referenced as context and stored in their correct lanes.
- Hazard/event/impact claims, damages, infrastructure impacts, crop-loss claims, health/safety guidance, exposure claims, emergency instructions, regulatory conclusions, or life-safety instructions.
- Forecast/model-as-observation substitution, context-as-primary-proof substitution, or climate baseline/anomaly substitution.
- Domain catalog records, STAC records, DCAT records, PROV records, triplet/graph records, published outputs, proofs, receipts, source registry records, release records, schemas, policy rules, validators, tests, pipelines, app/UI/API code.

## WeatherObservation requirements

PROPOSED until concrete validators and CI enforcement are verified:

| Requirement | Meaning |
|---|---|
| Source trace | Every processed WeatherObservation artifact should trace to SourceDescriptor or source registry context when source authority matters. |
| Weather identity | General weather-observation identity must remain explicit and must not collapse into specialized temperature, precipitation, wind, forecast, climate, hazard, advisory, or health/safety semantics. |
| Source role | `OBSERVED_SENSOR`, `METEOROLOGICAL_CONTEXT`, station, grid, model context, archive, or other admitted role must be explicit and non-collapsing. |
| Context role | Context-vs-primary-claim posture should be explicit so supporting weather context is not inflated into proof of another claim. |
| Station/grid/source context | Weather observations should identify or reference station, grid cell, source product, or network context without turning station metadata into processed observation data. |
| Units and variable hints | Units, variable hints, conversion method where applicable, and specialized-object routing posture should be explicit enough to prevent flattening. |
| Time semantics | Observed time, retrieval time, valid time where relevant, correction time, freshness, aggregation window where relevant, and release time should remain distinguishable where material. |
| QA/correction posture | Quality flags, correction state, calibration/correction lineage, caveats, limitations, missingness, confidence, and uncertainty should remain visible. |
| Evidence linkage | Claims about weather value, source, role, units, time, station/grid, QA, correction, context posture, or release should resolve downstream to EvidenceBundle/proof context. |
| Policy posture | Public display requires rights, source-role, freshness, caveat, sensitivity, and policy/admissibility posture. |
| Catalog readiness | Processed WeatherObservation artifacts intended for discovery should promote through Atmosphere catalog lanes, not directly to public use. |
| Release readiness | Public use requires release state, published output path, correction path, and rollback target. |
| No impact guidance by default | Weather values do not create hazard, crop-loss, infrastructure, health, emergency, exposure, regulatory, or life-safety claims without separate authority and review. |

## Weather guardrails

- `WeatherObservation` is the general meteorological observation/context family, not a replacement for specialized temperature, precipitation, or wind objects when those semantics matter.
- Weather observations must preserve `OBSERVED_SENSOR` versus `METEOROLOGICAL_CONTEXT` role tagging.
- Supporting weather context must not be inflated into primary proof of hazards, impacts, health effects, crop loss, infrastructure effects, hydrology truth, or regulatory claims.
- Forecast/model weather context must remain labeled as model context and not as observed weather.
- Climate baselines/anomalies may use aggregated weather values, but a weather observation is not the baseline or anomaly by itself.
- Weather values may support advisory referral, but they do not create emergency, medical, or life-safety instructions by themselves.
- Public display requires source rights, source role, units, freshness, validation, policy, release record, correction path, and rollback target.
- Unreleased processed weather-observation artifacts are not public merely because they exist under this directory.

> [!CAUTION]
> Do not use this lane as a shortcut from processed weather values to hazards/event truth, exposure claims, crop-loss claims, infrastructure impacts, public health guidance, public alerts, regulatory conclusions, or life-safety instructions. WeatherObservation products must pass catalog, evidence, policy, validation, release, correction, and rollback gates before public use.

## Directory map

Actual child inventory remains **NEEDS VERIFICATION**. Use this as a proposed local organization pattern only after confirming current repo convention and validators.

```text
data/processed/atmosphere/weather_observations/
├── README.md
├── normalized/              # PROPOSED — processed WeatherObservation records
├── observed_sensor/         # PROPOSED — observed weather values with source role and units
├── meteorological_context/  # PROPOSED — supporting context records, not primary proof by default
├── station_grid/            # PROPOSED — station/grid-linked values, not station authority
├── quality/                 # PROPOSED — QA, caveats, missingness, confidence, limitations
├── corrections/             # PROPOSED — correction/calibration lineage sidecars, not receipts
├── joins/                   # PROPOSED — links to WeatherStation, temperature, precipitation, wind, forecast, climate, advisory/hazards context
├── _manifests/              # PROPOSED — lane-local non-release manifests only
└── _README_TODO.md          # PROPOSED — remove after actual child inventory is documented
```

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|
| Previous file | CONFIRMED | Target existed as a one-character placeholder. | Did not define WeatherObservation PROCESSED-stage boundaries. |
| `data/processed/atmosphere/observed/README.md` | CONFIRMED sibling README | Observed parent lane and observed-vs-model/proxy/advisory guardrails. | Does not define weather-observation-specific inventory or release behavior. |
| `data/processed/atmosphere/temperature/README.md` | CONFIRMED sibling README | Specialized temperature lane and weather-variable anti-collapse pattern. | Does not define general weather-observation inventory. |
| `data/processed/atmosphere/precipitation/README.md` | CONFIRMED sibling README | Specialized precipitation lane and weather-variable anti-collapse pattern. | Does not define general weather-observation inventory. |
| `data/processed/atmosphere/forecast_context/README.md` | CONFIRMED sibling README | Forecast/model context remains separate from observations. | Does not define weather-observation inventory. |
| `data/processed/atmosphere/modeled/README.md` | CONFIRMED sibling README | Modeled products are not observations. | Does not define weather-observation inventory. |
| `data/processed/atmosphere/climate_normals/README.md` | CONFIRMED sibling README | ClimateNormal baseline context remains separate from observations. | Does not define weather-observation inventory. |
| `data/processed/atmosphere/climate_anomaly/README.md` | CONFIRMED sibling README | ClimateAnomaly anomaly context remains separate from observations. | Does not define weather-observation inventory. |
| `data/processed/README.md` | CONFIRMED | Parent processed lane is upstream of catalog, triplets, and publication and is not public by default. | Does not prove child inventory under this lane. |
| `data/catalog/domain/atmosphere/README.md` | CONFIRMED | Atmosphere catalog lane includes weather observations downstream and preserves source-role guardrails. | Does not prove weather-observation processed inventory or release behavior. |
| `docs/domains/atmosphere/README.md` | CONFIRMED doctrine / PROPOSED implementation | Atmosphere owns weather/mesonet observations, model/advisory context, climate context, and source-role denials. | Implementation maturity and runtime behavior remain NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/WeatherObservation.md` | CONFIRMED contract file | Defines WeatherObservation as governed general meteorological observation/context with role-tagging and model/climate/hazard/advisory boundary controls. | Contract does not prove schema enforcement, validator behavior, or release approval. |
| `schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json` | CONFIRMED scaffold schema | Paired WeatherObservation schema exists with PROPOSED status. | Properties are currently empty; validator enforcement remains NEEDS VERIFICATION. |
| `docs/doctrine/directory-rules.md` | CONFIRMED doctrine / PROPOSED path specifics | Data paths encode lifecycle phase and domain segment; promotion is governed. | Does not prove runtime enforcement. |

## Validation checklist

- [ ] Confirm actual child directories under `data/processed/atmosphere/weather_observations/`.
- [ ] Confirm accepted WeatherObservation source/domain path convention.
- [ ] Confirm `WeatherObservation` schema fields and title casing are updated beyond scaffold if needed.
- [ ] Confirm WeatherObservation processed validators and CI checks.
- [ ] Confirm SourceDescriptor/source registry linkage for each source-derived weather artifact.
- [ ] Confirm weather-vs-station, weather-vs-temperature, weather-vs-precipitation, weather-vs-wind, weather-vs-forecast/model, weather-vs-climate normal/anomaly, weather-vs-advisory, and weather-vs-hazards/impact boundaries.
- [ ] Confirm station/grid/source context handling without duplicating station authority.
- [ ] Confirm RunReceipt, TransformReceipt, ValidationReport, PolicyDecision, correction path, and rollback target where applicable.
- [ ] Confirm observed time, retrieval time, valid time, source role, context-vs-primary-claim role, units, variable hints, QA/correction posture, caveats, limitations, missingness, confidence, station-location sensitivity, freshness, and public display posture.
- [ ] Confirm no RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, proof, receipt, release, schema, policy, validator, package, pipeline, app, API, station-authority, specialized temperature/precipitation/wind data, forecast/model, climate normal/anomaly, health claim, crop-loss claim, infrastructure claim, hazard-impact claim, advisory, official warning, exposure, or life-safety artifacts are misplaced here.
- [ ] Confirm promotion flow from processed WeatherObservation data to catalog/triplet/published outputs is governed, source-role-safe, role-tagged, evidence-backed, and reversible.
- [ ] Confirm public clients and Focus Mode cannot use this lane as a direct heat/cold/flood/storm hazard, crop-loss, infrastructure, health, regulatory, emergency, hazard-impact, or life-safety source.

## Rollback

Rollback is required if this lane becomes an Atmosphere source-data root, WeatherStation authority root, TemperatureObservation replacement, PrecipitationObservation replacement, WindField replacement, ForecastContext replacement, climate-normal/anomaly source, health/exposure claim root, agriculture/crop-loss claim root, infrastructure-impact root, hydrology/hazards/event/impact root, advisory authority root, official warning/public-alerting root, quarantine bypass, proof store, receipt store, catalog root, triplet root, source-registry root, release-decision root, published-output root, public layer root, public tile root, schema root, policy root, validator root, implementation root, public API shortcut, public exposure shortcut, regulatory-claim source, emergency instruction source, or life-safety guidance source.

Rollback target for this expansion: previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

<p align="right"><a href="#top">Back to top</a></p>

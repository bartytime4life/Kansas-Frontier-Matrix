<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-temperature-readme
title: data/processed/atmosphere/temperature/README.md — Atmosphere TemperatureObservation Processed Data README
version: v0.1
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; temperature-observation-lane
status: draft; PROPOSED; data-root; processed-stage; atmosphere; temperature; TemperatureObservation; release-gated; canonical-units-aware; source-role-aware
owners: OWNER_TBD — Atmosphere steward · Weather steward · Temperature steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — one-character placeholder existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; processed; atmosphere; temperature; lifecycle; governed; release-gated
tags: [kfm, data, processed, atmosphere, temperature, TemperatureObservation, WeatherObservation, WeatherStation, PrecipitationObservation, WindField, ForecastContext, ClimateNormal, ClimateAnomaly, AdvisoryContext, observed-sensor, meteorological-context, canonical-units, lifecycle, RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, EvidenceBundle, SourceDescriptor, RunReceipt, ValidationReport, PolicyDecision, ReleaseManifest]
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
  - ../derived/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/TemperatureObservation.md
  - ../../../../contracts/domains/atmosphere/WeatherObservation.md
  - ../../../../contracts/domains/atmosphere/WeatherStation.md
  - ../../../../contracts/domains/atmosphere/PrecipitationObservation.md
  - ../../../../contracts/domains/atmosphere/WindField.md
  - ../../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../../contracts/domains/atmosphere/ClimateNormal.md
  - ../../../../contracts/domains/atmosphere/ClimateAnomaly.md
  - ../../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/TemperatureObservation.schema.json
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
  - "This file replaces a one-character placeholder at `data/processed/atmosphere/temperature/README.md`."
  - "This is the PROCESSED-stage sublane for normalized TemperatureObservation artifacts under Atmosphere. It is not RAW station/gridded storage, generic WeatherObservation authority, forecast/model authority, climate baseline/anomaly authority, heat/cold hazards truth, proof storage, release authority, public API/UI output, or life-safety guidance."
  - "Temperature artifacts must preserve variable identity, source role, station/grid/source-product context, canonical units, measurement height/exposure context where applicable, observed time, retrieval time, QA/correction posture, evidence linkage, policy posture, and release state before public use."
  - "The TemperatureObservation contract defines object meaning; this README does not create a second contract or schema authority."
  - "Temperature observations may support climate, hazards, agriculture, infrastructure, or health context only through downstream governed lanes; they do not prove heat wave, cold wave, frost/freeze damage, exposure, health effect, crop loss, or infrastructure impacts by themselves."
  - "Rollback target for this expansion is previous placeholder blob SHA `ac044e5e4649cd149e3d0cf9d23720d299288a1e`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/processed/atmosphere/temperature

> Atmosphere PROCESSED-stage sublane for normalized `TemperatureObservation` artifacts: governed temperature reading, apparent temperature, heat-index/wind-chill context, minimum/maximum temperature, dew point, wet bulb, and temperature-related meteorological context records that remain distinct from generic weather observations, forecast/model fields, climate baselines/anomalies, heat/cold hazards, proof, release, and public map/API/UI surfaces.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data/processed/atmosphere/temperature" src="https://img.shields.io/badge/root-data%2Fprocessed%2Fatmosphere%2Ftemperature-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Object: TemperatureObservation" src="https://img.shields.io/badge/object-TemperatureObservation-purple">
  <img alt="Lifecycle: PROCESSED" src="https://img.shields.io/badge/lifecycle-PROCESSED-purple">
  <img alt="Exposure: not public" src="https://img.shields.io/badge/exposure-not__public-critical">
</p>

**Status:** draft / PROPOSED  
**Owners:** OWNER_TBD — Atmosphere steward · Weather steward · Temperature steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward  
**Path:** `data/processed/atmosphere/temperature/README.md`  
**Owning root:** `data/processed/`  
**Domain segment:** `atmosphere`  
**Object-family segment:** `temperature` / `TemperatureObservation`  
**Lifecycle stage:** `PROCESSED`  
**Exposure posture:** not public by default; public use requires governed catalog, evidence, canonical units, source-role/freshness/caveat posture, policy, release, correction, and rollback linkage  
**Truth posture:** CONFIRMED target was a one-character placeholder · CONFIRMED `TemperatureObservation` contract and schema paths exist · CONFIRMED temperature has role-dependent `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT` character with canonical-unit requirements · PROPOSED temperature processed-sublane details · NEEDS VERIFICATION for actual child inventory, validators, receipts, CI enforcement, release linkage, and governed route behavior.

**Quick jumps:** [Purpose](#purpose) · [Lifecycle boundary](#lifecycle-boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [TemperatureObservation requirements](#temperatureobservation-requirements) · [Temperature guardrails](#temperature-guardrails) · [Directory map](#directory-map) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/processed/atmosphere/temperature/` holds normalized temperature observation artifacts that have moved beyond RAW capture, WORK transforms, and QUARANTINE holds.

This lane is for processed `TemperatureObservation` records or derivatives that preserve variable identity, source role, station/network/grid/source-product context, source identity, observed time, retrieval time, valid time where applicable, canonical units, measurement height/exposure context where applicable, temperature variant semantics, QA/correction posture, freshness, evidence references, and downstream catalog readiness.

It is not a generic weather-observation lane. It is not a forecast/model lane. It is not climate baseline/anomaly authority. It is not hazards event/impact truth. It is not a proof store, receipt store, source registry, catalog, release, semantic contract, schema, policy, public layer, public API/UI surface, or life-safety guidance source. It may support downstream catalog records, EvidenceBundle-backed UI payloads, public-safe temperature layers, climate aggregation, hazards context, Focus Mode summaries, or release packages only after gates pass.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

```mermaid
flowchart LR
  RAW[data/raw/atmosphere] --> WORK[data/work/atmosphere]
  WORK --> QUAR[data/quarantine/atmosphere]
  WORK --> TEMP[data/processed/atmosphere/temperature]
  QUAR --> TEMP
  TEMP --> OBS[data/processed/atmosphere/observed]
  TEMP --> CLIM[data/processed/atmosphere/aggregate/climate]
  TEMP --> CAT[data/catalog/domain/atmosphere]
  TEMP --> STAC[data/catalog/stac/atmosphere]
  TEMP --> DCAT[data/catalog/dcat/atmosphere]
  TEMP --> PROV[data/catalog/prov/atmosphere]
  TEMP -. supports .-> PROOF[data/proofs]
  TEMP -. emits / references .-> RECEIPT[data/receipts]
  CAT --> TRIP[data/triplets/.../atmosphere]
  CAT --> PUB[data/published/.../atmosphere]
  STAC --> PUB
  DCAT --> PUB
  PROV --> PUB
  TRIP --> PUB
  PUB --> REL[release]
```

`data/processed/atmosphere/temperature/` is upstream of catalog, triplet, publication, and release. It must not be used as a normal public map/API/UI/AI source.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Raw station feeds, gridded products, source downloads, QA payloads, or logs | `data/raw/atmosphere/` | Not this lane. |
| In-process temperature parsing, unit conversion, derived heat-index/wind-chill work, station/grid reconciliation, QA, joins, scratch outputs, or method experiments | `data/work/atmosphere/` | Not this lane. |
| Rights-unclear, source-role-unclear, stale, malformed, unit-unclear, unsupported, disputed, sensitive, or unsafe temperature material | `data/quarantine/atmosphere/` | Not this lane until resolved. |
| Normalized TemperatureObservation processed artifacts | `data/processed/atmosphere/temperature/` | This lane. |
| General weather observations | WeatherObservation processed lane if accepted, or `data/processed/atmosphere/observed/` as parent | Temperature specialization remains separate when variable-specific semantics apply. |
| Weather station/network context | WeatherStation processed lane if accepted | Station metadata is context, not temperature value. |
| Forecast/model context | `data/processed/atmosphere/forecast_context/` or `data/processed/atmosphere/modeled/` | Forecast temperature must not impersonate observed temperature. |
| Climate normals/anomalies | `data/processed/atmosphere/climate_normals/`, `climate_anomaly/`, or `aggregate/climate/` | Climate products may aggregate temperature but remain separate objects. |
| Hazards/event/impact claims | Hazards responsibility roots | Temperature can contextualize heat/cold hazards; it does not prove impact. |
| Agriculture, infrastructure, health, or exposure claims | Their respective governed responsibility roots | Temperature can supply context, not canonical cross-domain truth. |
| Atmosphere domain catalog records | `data/catalog/domain/atmosphere/` | Downstream catalog stage. |
| Atmosphere STAC/DCAT/PROV records | `data/catalog/{stac,dcat,prov}/atmosphere/` | Downstream catalog projections, if accepted. |
| Atmosphere triplet/graph projections | `data/triplets/.../atmosphere/` | Downstream graph stage. |
| Atmosphere public-safe products | `data/published/.../atmosphere/` | Downstream after release. |
| EvidenceBundle/proof records | `data/proofs/` | Separate proof family. |
| Source, run, transform, validation, policy, correction, and release receipts | `data/receipts/` | Separate receipt family. |
| SourceDescriptor/source registry records | `data/registry/` | Separate registry family. |
| Release decisions, manifests, rollback cards, corrections, withdrawals | `release/` | Separate publication authority. |
| TemperatureObservation semantic contract | `contracts/domains/atmosphere/TemperatureObservation.md` | Object meaning; not data. |
| TemperatureObservation schema | `schemas/contracts/v1/domains/atmosphere/TemperatureObservation.schema.json` | Machine shape; not data. |
| Policy, validators, tests, pipelines, apps, packages | `policy/`, `tools/validators/`, `tests/`, `pipelines/`, `apps/`, `packages/` | Separate roots. |

## Accepted contents

Processed `TemperatureObservation` data may include:

- normalized air temperature, apparent temperature, heat-index/wind-chill context, minimum/maximum temperature, dew point, wet bulb, or source-coded temperature records tied to a weather station, grid cell, source product, or station/network context;
- source-role-preserving temperature records where `OBSERVED_SENSOR`, `METEOROLOGICAL_CONTEXT`, station, grid, archive, or other admitted role remains explicit;
- temperature value, canonical units, measurement height/exposure context where applicable, observed time, retrieval time, valid time where relevant, source time, QA state, correction lineage, freshness, caveats, confidence, and limitation metadata;
- heat-index, wind-chill, apparent-temperature, dew-point, or wet-bulb derivatives only when method, inputs, source roles, units, and caveats remain explicit;
- climate-aggregation inputs only when baseline/anomaly products remain separate and aggregation method is documented downstream;
- processed joins to weather observations, stations, precipitation, wind, forecast, climate, advisory, agriculture, infrastructure, health, or hazards context when the knowledge-character boundary remains visible;
- quality, caveat, missingness, correction, uncertainty, freshness, validation, unit-normalization, measurement-height, and exposure-context sidecars when those sidecars are not proofs, receipts, source registry records, catalog records, schemas, or policy rules;
- processed artifacts prepared for downstream domain catalog, STAC/DCAT/PROV packaging, EvidenceBundle support, triplet generation, or release review.

## Exclusions

Do not store these under `data/processed/atmosphere/temperature/`:

- RAW station feeds, gridded products, source downloads, QA payloads, logs, screenshots, or source-native records.
- WORK/scratch outputs that have not passed processing gates.
- Quarantined, malformed, source-role-unclear, rights-unclear, stale, unit-unclear, unsupported, disputed, sensitive, or unsafe temperature material.
- Generic `WeatherObservation` records unless temperature-specific semantics are preserved here by accepted convention.
- Precipitation observations, wind fields, model/forecast fields, climate normal records, climate anomaly records, advisory/referral records, hazards records, crop records, infrastructure records, or health/exposure records unless only referenced as context and stored in their correct lanes.
- Heat wave, cold wave, frost, freeze, storm, hazard, damage, infrastructure, crop-loss, health/safety, exposure, emergency, regulatory, or impact claims.
- Forecast/model-as-observation substitution or climate baseline/anomaly substitution.
- Domain catalog records, STAC records, DCAT records, PROV records, triplet/graph records, published outputs, proofs, receipts, source registry records, release records, schemas, policy rules, validators, tests, pipelines, app/UI/API code.

## TemperatureObservation requirements

PROPOSED until concrete validators and CI enforcement are verified:

| Requirement | Meaning |
|---|---|
| Source trace | Every processed TemperatureObservation artifact should trace to SourceDescriptor or source registry context when source authority matters. |
| Variable identity | Temperature identity and variant semantics must remain explicit and must not collapse into generic WeatherObservation, forecast, climate, hazards, health, agriculture, or infrastructure semantics. |
| Source role | `OBSERVED_SENSOR`, `METEOROLOGICAL_CONTEXT`, station, grid, model context, archive, or other admitted role must be explicit and non-collapsing. |
| Station/grid/source context | Temperature observations should identify or reference weather station, grid cell, source product, or network context without turning station metadata into processed observation data. |
| Canonical units | Units, conversion method where applicable, measurement height/exposure context, apparent-temperature method, and canonical-unit posture must be explicit. |
| Time semantics | Observed time, retrieval time, valid time where relevant, correction time, freshness, aggregation window where relevant, and release time should remain distinguishable where material. |
| QA/correction posture | Quality flags, correction state, calibration/correction lineage, caveats, limitations, missingness, confidence, and uncertainty should remain visible. |
| Evidence linkage | Claims about temperature value, source, role, units, time, station/grid, QA, correction, or release should resolve downstream to EvidenceBundle/proof context. |
| Policy posture | Public display requires rights, source-role, freshness, caveat, sensitivity, and policy/admissibility posture. |
| Catalog readiness | Processed TemperatureObservation artifacts intended for discovery should promote through Atmosphere catalog lanes, not directly to public use. |
| Release readiness | Public use requires release state, published output path, correction path, and rollback target. |
| No impact guidance by default | Temperature values do not create heat/cold hazard, crop-loss, infrastructure, health, emergency, exposure, regulatory, or life-safety claims without separate authority and review. |

## Temperature guardrails

- `TemperatureObservation` is temperature-specific and must not be flattened into generic `WeatherObservation` when temperature-specific semantics matter.
- Temperature and precipitation are separate weather variables with separate units, methods, QA, and aggregation rules.
- Forecast/model temperature must remain labeled as model context, not observed temperature.
- Climate baselines/anomalies may use temperature aggregates, but a temperature observation is not a normal or anomaly by itself.
- A temperature reading does not prove heat wave, cold wave, frost/freeze damage, health effect, crop loss, infrastructure impact, or other hazards-lane truth by itself.
- Temperature values may support context, but they do not create emergency, medical, exposure, regulatory-exceedance, or life-safety instructions by themselves.
- Public display requires source rights, canonical units, freshness, validation, policy, release record, correction path, and rollback target.
- Unreleased processed temperature artifacts are not public merely because they exist under this directory.

> [!CAUTION]
> Do not use this lane as a shortcut from processed temperature values to heat/cold hazard, crop-loss, infrastructure, health, exposure, regulatory, emergency, or life-safety claims. TemperatureObservation products must pass catalog, evidence, policy, validation, release, correction, and rollback gates before public use.

## Directory map

Actual child inventory remains **NEEDS VERIFICATION**. Use this as a proposed local organization pattern only after confirming current repo convention and validators.

```text
data/processed/atmosphere/temperature/
├── README.md
├── normalized/              # PROPOSED — processed TemperatureObservation records
├── air_temperature/         # PROPOSED — measured air temperature values with canonical units
├── apparent_temperature/    # PROPOSED — heat index, wind chill, apparent temp, method required
├── min_max/                 # PROPOSED — minimum/maximum records with time-window semantics
├── dew_point/               # PROPOSED — dew point records with method/source role
├── wet_bulb/                # PROPOSED — wet bulb records with method/source role
├── quality/                 # PROPOSED — QA, caveats, missingness, confidence, limitations
├── corrections/             # PROPOSED — correction/calibration lineage sidecars, not receipts
├── joins/                   # PROPOSED — links to WeatherStation, WeatherObservation, forecast, climate, hazards/agriculture/infrastructure context
├── _manifests/              # PROPOSED — lane-local non-release manifests only
└── _README_TODO.md          # PROPOSED — remove after actual child inventory is documented
```

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|
| Previous file | CONFIRMED | Target existed as a one-character placeholder containing `R`. | Did not define TemperatureObservation PROCESSED-stage boundaries. |
| `data/processed/atmosphere/observed/README.md` | CONFIRMED sibling README | Observed parent lane and observed-vs-model/proxy/advisory guardrails. | Does not define temperature-specific inventory or release behavior. |
| `data/processed/atmosphere/precipitation/README.md` | CONFIRMED sibling README | Parallel precipitation lane and weather-variable anti-collapse pattern. | Does not define temperature inventory or release behavior. |
| `data/processed/atmosphere/forecast_context/README.md` | CONFIRMED sibling README | Forecast/model context remains separate from observations. | Does not define temperature-value inventory. |
| `data/processed/atmosphere/modeled/README.md` | CONFIRMED sibling README | Modeled products are not observations. | Does not define temperature-value inventory. |
| `data/processed/atmosphere/climate_normals/README.md` | CONFIRMED sibling README | ClimateNormal baseline context remains separate from observations. | Does not define temperature-value inventory. |
| `data/processed/atmosphere/climate_anomaly/README.md` | CONFIRMED sibling README | ClimateAnomaly anomaly context remains separate from observations. | Does not define temperature-value inventory. |
| `data/processed/README.md` | CONFIRMED | Parent processed lane is upstream of catalog, triplets, and publication and is not public by default. | Does not prove child inventory under this lane. |
| `data/catalog/domain/atmosphere/README.md` | CONFIRMED | Atmosphere catalog lane includes temperature observations downstream and preserves source-role guardrails. | Does not prove temperature processed inventory or release behavior. |
| `docs/domains/atmosphere/README.md` | CONFIRMED doctrine / PROPOSED implementation | Atmosphere owns weather/mesonet observations, temperature, climate context, model/advisory context, and source-role denials. | Implementation maturity and runtime behavior remain NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/TemperatureObservation.md` | CONFIRMED contract file | Defines TemperatureObservation as governed temperature reading/context with canonical-unit, source-role, model/climate/hazard boundary controls. | Contract does not prove schema enforcement, validator behavior, or release approval. |
| `schemas/contracts/v1/domains/atmosphere/TemperatureObservation.schema.json` | CONFIRMED scaffold schema | Paired TemperatureObservation schema exists with PROPOSED status. | Properties are currently empty; validator enforcement remains NEEDS VERIFICATION. |
| `docs/doctrine/directory-rules.md` | CONFIRMED doctrine / PROPOSED path specifics | Data paths encode lifecycle phase and domain segment; promotion is governed. | Does not prove runtime enforcement. |

## Validation checklist

- [ ] Confirm actual child directories under `data/processed/atmosphere/temperature/`.
- [ ] Confirm accepted TemperatureObservation source/domain path convention.
- [ ] Confirm `TemperatureObservation` schema fields and title casing are updated beyond scaffold if needed.
- [ ] Confirm TemperatureObservation processed validators and CI checks.
- [ ] Confirm SourceDescriptor/source registry linkage for each source-derived temperature artifact.
- [ ] Confirm temperature-vs-WeatherObservation, temperature-vs-precipitation, temperature-vs-forecast/model, temperature-vs-climate normal/anomaly, and temperature-vs-hazards/health/agriculture/infrastructure boundaries.
- [ ] Confirm station/grid/source context handling without duplicating station authority.
- [ ] Confirm RunReceipt, TransformReceipt, ValidationReport, PolicyDecision, correction path, and rollback target where applicable.
- [ ] Confirm observed time, retrieval time, valid time, aggregation window, source role, canonical units, measurement height/exposure context, apparent-temperature method, QA/correction posture, caveats, limitations, missingness, confidence, station-location sensitivity, freshness, and public display posture.
- [ ] Confirm no RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, proof, receipt, release, schema, policy, validator, package, pipeline, app, API, station-authority, forecast/model, climate normal/anomaly, health claim, crop-loss claim, infrastructure claim, hazard-impact claim, advisory, official warning, exposure, or life-safety artifacts are misplaced here.
- [ ] Confirm promotion flow from processed TemperatureObservation data to catalog/triplet/published outputs is governed, source-role-safe, unit-aware, evidence-backed, and reversible.
- [ ] Confirm public clients and Focus Mode cannot use this lane as a direct heat/cold hazard, crop-loss, infrastructure, health, regulatory, emergency, hazard-impact, or life-safety source.

## Rollback

Rollback is required if this lane becomes an Atmosphere source-data root, WeatherObservation replacement, WeatherStation authority root, ForecastContext replacement, climate-normal/anomaly source, health/exposure claim root, agriculture/crop-loss claim root, infrastructure-impact root, hazards/event/impact root, advisory authority root, official warning/public-alerting root, quarantine bypass, proof store, receipt store, catalog root, triplet root, source-registry root, release-decision root, published-output root, public layer root, public tile root, schema root, policy root, validator root, implementation root, public API shortcut, public exposure shortcut, regulatory-claim source, emergency instruction source, or life-safety guidance source.

Rollback target for this expansion: previous placeholder blob SHA `ac044e5e4649cd149e3d0cf9d23720d299288a1e`.

<p align="right"><a href="#top">Back to top</a></p>

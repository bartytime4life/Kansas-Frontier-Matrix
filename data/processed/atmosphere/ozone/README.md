<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-ozone-readme
title: data/processed/atmosphere/ozone/README.md — Atmosphere OzoneObservation Processed Data README
version: v0.1
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; ozone-observation-lane
status: draft; PROPOSED; data-root; processed-stage; atmosphere; ozone; OzoneObservation; release-gated; source-role-aware; AQI-boundary-aware
owners: OWNER_TBD — Atmosphere steward · Air-quality steward · Ozone steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — one-character placeholder existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; processed; atmosphere; ozone; lifecycle; governed; release-gated
tags: [kfm, data, processed, atmosphere, ozone, OzoneObservation, AirObservation, AirStation, PM25Observation, AQI, concentration, observed-sensor, public-aqi-report, lifecycle, RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, EvidenceBundle, SourceDescriptor, RunReceipt, ValidationReport, PolicyDecision, ReleaseManifest]
related:
  - ../README.md
  - ../observed/README.md
  - ../air_observations/README.md
  - ../air_stations/README.md
  - ../forecast_context/README.md
  - ../modeled/README.md
  - ../aod/README.md
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
  - ../../../../pipelines/
  - ../../../../tools/validators/
notes:
  - "This file replaces a one-character placeholder at `data/processed/atmosphere/ozone/README.md`."
  - "This is the PROCESSED-stage sublane for normalized OzoneObservation artifacts under Atmosphere. It is not RAW sensor-feed storage, generic AirObservation authority, PM2.5 authority, AQI/concentration substitution, model-field authority, advisory authority, proof storage, release authority, public API/UI output, or life-safety guidance."
  - "Ozone artifacts must preserve pollutant identity, source role, station/network context, units, observed time, retrieval time, QA/correction posture, AQI/report posture where applicable, evidence linkage, policy posture, and release state before public use."
  - "The OzoneObservation contract defines object meaning; this README does not create a second contract or schema authority."
  - "Ozone AQI/report values and ozone concentrations must remain role-separated. Do not present AQI/report posture as raw concentration."
  - "Rollback target for this expansion is previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/processed/atmosphere/ozone

> Atmosphere PROCESSED-stage sublane for normalized `OzoneObservation` artifacts: governed ozone concentration, ozone report, and ozone-related air-quality records that remain distinct from generic air observations, PM2.5, AQI/concentration substitution, model fields, AOD/smoke proxies, advisory guidance, proof, release, and public map/API/UI surfaces.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data/processed/atmosphere/ozone" src="https://img.shields.io/badge/root-data%2Fprocessed%2Fatmosphere%2Fozone-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Object: OzoneObservation" src="https://img.shields.io/badge/object-OzoneObservation-purple">
  <img alt="Lifecycle: PROCESSED" src="https://img.shields.io/badge/lifecycle-PROCESSED-purple">
  <img alt="Exposure: not public" src="https://img.shields.io/badge/exposure-not__public-critical">
</p>

**Status:** draft / PROPOSED  
**Owners:** OWNER_TBD — Atmosphere steward · Air-quality steward · Ozone steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward  
**Path:** `data/processed/atmosphere/ozone/README.md`  
**Owning root:** `data/processed/`  
**Domain segment:** `atmosphere`  
**Object-family segment:** `ozone` / `OzoneObservation`  
**Lifecycle stage:** `PROCESSED`  
**Exposure posture:** not public by default; public use requires governed catalog, evidence, source-role/unit/caveat posture, policy, release, correction, and rollback linkage  
**Truth posture:** CONFIRMED target was a one-character placeholder · CONFIRMED `OzoneObservation` contract and schema paths exist · CONFIRMED ozone has role-dependent `OBSERVED_SENSOR` / `PUBLIC_AQI_REPORT` character · PROPOSED ozone processed-sublane details · NEEDS VERIFICATION for actual child inventory, validators, receipts, CI enforcement, release linkage, and governed route behavior.

**Quick jumps:** [Purpose](#purpose) · [Lifecycle boundary](#lifecycle-boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [OzoneObservation requirements](#ozoneobservation-requirements) · [Ozone guardrails](#ozone-guardrails) · [Directory map](#directory-map) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/processed/atmosphere/ozone/` holds normalized ozone observation artifacts that have moved beyond RAW capture, WORK transforms, and QUARANTINE holds.

This lane is for processed `OzoneObservation` records or derivatives that preserve pollutant identity, source role, station/network context, source identity, observed time, retrieval time, units, averaging period, QA/correction posture, freshness, AQI/report posture where applicable, regulatory/archive posture where separately supported, evidence references, and downstream catalog readiness.

It is not a generic air-observation lane. It is not a PM2.5 lane. It is not an AQI-to-concentration conversion lane. It is not a model-field lane. It is not an AOD/smoke-proxy lane. It is not an advisory authority. It is not a proof store, receipt store, source registry, catalog, release, semantic contract, schema, policy, public layer, public API/UI surface, or life-safety guidance source. It may support downstream catalog records, EvidenceBundle-backed UI payloads, public-safe ozone layers, Focus Mode summaries, or release packages only after gates pass.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

```mermaid
flowchart LR
  RAW[data/raw/atmosphere] --> WORK[data/work/atmosphere]
  WORK --> QUAR[data/quarantine/atmosphere]
  WORK --> OZONE[data/processed/atmosphere/ozone]
  QUAR --> OZONE
  OZONE --> OBS[data/processed/atmosphere/observed]
  OZONE --> AIR[data/processed/atmosphere/air_observations]
  OZONE --> CAT[data/catalog/domain/atmosphere]
  OZONE --> STAC[data/catalog/stac/atmosphere]
  OZONE --> DCAT[data/catalog/dcat/atmosphere]
  OZONE --> PROV[data/catalog/prov/atmosphere]
  OZONE -. supports .-> PROOF[data/proofs]
  OZONE -. emits / references .-> RECEIPT[data/receipts]
  CAT --> TRIP[data/triplets/.../atmosphere]
  CAT --> PUB[data/published/.../atmosphere]
  STAC --> PUB
  DCAT --> PUB
  PROV --> PUB
  TRIP --> PUB
  PUB --> REL[release]
```

`data/processed/atmosphere/ozone/` is upstream of catalog, triplet, publication, and release. It must not be used as a normal public map/API/UI/AI source.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Raw ozone sensor feeds, agency AQI feeds, station payloads, source downloads, QA payloads, or logs | `data/raw/atmosphere/` | Not this lane. |
| In-process ozone parsing, unit conversion, AQI/report role review, correction, QA, joins, scratch outputs, or method experiments | `data/work/atmosphere/` | Not this lane. |
| Rights-unclear, source-role-unclear, stale, malformed, unit-unclear, unsupported, disputed, sensitive, or unsafe ozone material | `data/quarantine/atmosphere/` | Not this lane until resolved. |
| Normalized OzoneObservation processed artifacts | `data/processed/atmosphere/ozone/` | This lane. |
| General air-quality observations | `data/processed/atmosphere/air_observations/` | Ozone specialization remains separate when pollutant-specific semantics apply. |
| Observed parent lane | `data/processed/atmosphere/observed/` | Parent/sibling role lane for observed products. |
| Station/network context | `data/processed/atmosphere/air_stations/` | Station metadata is context, not ozone value. |
| PM2.5-specific processed artifacts | Domain-accepted PM2.5 lane, if present | Ozone and PM2.5 are separate pollutant families. |
| Forecast/model context | `data/processed/atmosphere/forecast_context/` or `data/processed/atmosphere/modeled/` | Modeled ozone must not impersonate observed ozone. |
| AOD/remote-sensing proxy context | `data/processed/atmosphere/aod/` | AOD is not ozone, PM2.5, AQI, or a ground observation. |
| Advisory/referral context | `data/processed/atmosphere/advisory_context/` | Advisory context remains official-source referral, not ozone value. |
| Atmosphere domain catalog records | `data/catalog/domain/atmosphere/` | Downstream catalog stage. |
| Atmosphere STAC/DCAT/PROV records | `data/catalog/{stac,dcat,prov}/atmosphere/` | Downstream catalog projections, if accepted. |
| Atmosphere triplet/graph projections | `data/triplets/.../atmosphere/` | Downstream graph stage. |
| Atmosphere public-safe products | `data/published/.../atmosphere/` | Downstream after release. |
| EvidenceBundle/proof records | `data/proofs/` | Separate proof family. |
| Source, run, transform, validation, policy, correction, and release receipts | `data/receipts/` | Separate receipt family. |
| SourceDescriptor/source registry records | `data/registry/` | Separate registry family. |
| Release decisions, manifests, rollback cards, corrections, withdrawals | `release/` | Separate publication authority. |
| OzoneObservation semantic contract | `contracts/domains/atmosphere/OzoneObservation.md` | Object meaning; not data. |
| OzoneObservation schema | `schemas/contracts/v1/domains/atmosphere/OzoneObservation.schema.json` | Machine shape; not data. |
| Policy, validators, tests, pipelines, apps, packages | `policy/`, `tools/validators/`, `tests/`, `pipelines/`, `apps/`, `packages/` | Separate roots. |

## Accepted contents

Processed `OzoneObservation` data may include:

- normalized ozone concentration records tied to an `AirStation` or comparable station/network context;
- source-role-preserving ozone records where `OBSERVED_SENSOR`, `PUBLIC_AQI_REPORT`, regulatory/archive, low-cost sensor, or other admitted role remains explicit;
- ozone value, units, averaging period, observed time, retrieval time, source time, QA state, correction lineage, freshness, caveats, and confidence metadata;
- agency AQI/report ozone values only when labeled as report/index posture and not raw concentration;
- regulatory/archive ozone values only when source role, vintage, issuing authority, evidence support, and release posture are documented;
- processed joins to `AirObservation`, PM2.5, station context, weather, smoke, AOD, forecast, or advisory context when the knowledge-character boundary remains visible;
- quality, caveat, missingness, correction, uncertainty, freshness, validation, unit-normalization, and AQI/report-posture sidecars when those sidecars are not proofs, receipts, source registry records, catalog records, schemas, or policy rules;
- processed artifacts prepared for downstream domain catalog, STAC/DCAT/PROV packaging, EvidenceBundle support, triplet generation, or release review.

## Exclusions

Do not store these under `data/processed/atmosphere/ozone/`:

- RAW ozone sensor feeds, raw agency AQI feeds, station payloads, source downloads, QA payloads, logs, screenshots, or source-native records.
- WORK/scratch outputs that have not passed processing gates.
- Quarantined, malformed, source-role-unclear, rights-unclear, stale, unit-unclear, unsupported, disputed, sensitive, or unsafe ozone material.
- Generic `AirObservation` records unless ozone-specific semantics are preserved here by accepted convention.
- PM2.5 observations or PM2.5 report/index records.
- AQI/report semantics when source role does not explicitly admit `PUBLIC_AQI_REPORT`.
- AQI-to-concentration substitution or concentration-to-AQI substitution without a separately governed method, evidence, policy, and review.
- Model fields, AOD rasters, smoke masks, advisory/referral records, health/safety guidance, exposure claims, regulatory exceedance proof, damages, public alerting behavior, or policy conclusions.
- Domain catalog records, STAC records, DCAT records, PROV records, triplet/graph records, published outputs, proofs, receipts, source registry records, release records, schemas, policy rules, validators, tests, pipelines, app/UI/API code.

## OzoneObservation requirements

PROPOSED until concrete validators and CI enforcement are verified:

| Requirement | Meaning |
|---|---|
| Source trace | Every processed OzoneObservation artifact should trace to SourceDescriptor or source registry context when source authority matters. |
| Pollutant identity | Ozone identity must remain explicit and must not collapse into generic AirObservation, PM2.5, AQI, smoke, or AOD semantics. |
| Source role | `OBSERVED_SENSOR`, `PUBLIC_AQI_REPORT`, regulatory/archive, low-cost sensor, model context, or other role must be explicit and non-collapsing. |
| Station/network context | Ozone observations should identify or reference station/network context without turning station metadata into processed observation data. |
| Units and averaging | Units, averaging period, conversion method where applicable, and report/index posture should be explicit enough to avoid AQI/concentration substitution. |
| Time semantics | Observed time, retrieval time, valid/report time where relevant, correction time, freshness, and release time should remain distinguishable where material. |
| QA/correction posture | Quality flags, correction state, calibration/correction lineage, caveats, limitations, missingness, confidence, and uncertainty should remain visible. |
| Evidence linkage | Claims about ozone value, source, role, units, time, station, QA, correction, or release should resolve downstream to EvidenceBundle/proof context. |
| Policy posture | Public display requires rights, source-role, freshness, caveat, sensitivity, and policy/admissibility posture. |
| Catalog readiness | Processed OzoneObservation artifacts intended for discovery should promote through Atmosphere catalog lanes, not directly to public use. |
| Release readiness | Public use requires release state, published output path, correction path, and rollback target. |
| No action guidance by default | Ozone values do not create medical, emergency, life-safety, exposure, regulatory, or hazard-impact claims without separate authority and review. |

## Ozone guardrails

- `OzoneObservation` is ozone-specific and must not be flattened into generic `AirObservation` when ozone-specific semantics matter.
- Ozone and PM2.5 are separate pollutant-specific object families with separate units, methods, QA, report semantics, and caveats.
- AQI is a report/index posture, not raw ozone concentration.
- Regulatory/archive posture requires source-role, vintage, issuing-authority, and evidence support.
- Modeled ozone or forecast context must remain labeled as model context, not observed sensor data.
- AOD/smoke remote-sensing proxies are not ozone observations.
- Ozone values may support context, but they do not create emergency, medical, exposure, regulatory-exceedance, or life-safety instructions by themselves.
- Public display requires source rights, units, freshness, validation, policy, release record, correction path, and rollback target.
- Unreleased processed ozone artifacts are not public merely because they exist under this directory.

> [!CAUTION]
> Do not use this lane as a shortcut from processed ozone values to public health, exposure, regulatory, emergency, or life-safety claims. OzoneObservation products must pass catalog, evidence, policy, validation, release, correction, and rollback gates before public use.

## Directory map

Actual child inventory remains **NEEDS VERIFICATION**. Use this as a proposed local organization pattern only after confirming current repo convention and validators.

```text
data/processed/atmosphere/ozone/
├── README.md
├── normalized/              # PROPOSED — processed OzoneObservation records
├── concentration/           # PROPOSED — ozone concentration values, source-role and units required
├── aqi_report/              # PROPOSED — ozone AQI/report values, not raw concentration
├── regulatory_archive/      # PROPOSED — regulatory/archive posture with evidence and vintage controls
├── quality/                 # PROPOSED — QA, caveats, missingness, confidence, limitations
├── corrections/             # PROPOSED — correction/calibration lineage sidecars, not receipts
├── joins/                   # PROPOSED — links to AirStation, AirObservation, PM2.5, forecast, AOD, advisory context
├── _manifests/              # PROPOSED — lane-local non-release manifests only
└── _README_TODO.md          # PROPOSED — remove after actual child inventory is documented
```

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a one-character placeholder. | Did not define OzoneObservation PROCESSED-stage boundaries. |
| `data/processed/atmosphere/observed/README.md` | CONFIRMED sibling README | Observed parent lane and observed-vs-model/proxy/advisory guardrails. | Does not define ozone-specific inventory or release behavior. |
| `data/processed/atmosphere/air_observations/README.md` | CONFIRMED sibling README | AirObservation processed lane and generic observed-sensor guardrails. | Ozone specialization remains separate when pollutant-specific semantics apply. |
| `data/processed/atmosphere/air_stations/README.md` | CONFIRMED sibling README | Station/network context remains separate from observation values. | Does not define ozone-value inventory. |
| `data/processed/atmosphere/forecast_context/README.md` | CONFIRMED sibling README | Forecast/model context remains separate from observations. | Does not define ozone-value inventory. |
| `data/processed/atmosphere/aod/README.md` | CONFIRMED sibling README | AOD/remote-sensing proxy is not ground observation or PM2.5. | Does not define ozone-value inventory. |
| `data/processed/README.md` | CONFIRMED | Parent processed lane is upstream of catalog, triplets, and publication and is not public by default. | Does not prove child inventory under this lane. |
| `data/catalog/domain/atmosphere/README.md` | CONFIRMED | Atmosphere catalog lane includes ozone observations downstream and preserves source-role guardrails. | Does not prove ozone processed inventory or release behavior. |
| `docs/domains/atmosphere/README.md` | CONFIRMED doctrine / PROPOSED implementation | Atmosphere owns air-quality observations and source-role denials. | Implementation maturity and runtime behavior remain NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/OzoneObservation.md` | CONFIRMED contract file | Defines OzoneObservation as governed ozone concentration/report/archive object with AQI/concentration and source-role boundaries. | Contract does not prove schema enforcement, validator behavior, or release approval. |
| `schemas/contracts/v1/domains/atmosphere/OzoneObservation.schema.json` | CONFIRMED scaffold schema | Paired OzoneObservation schema exists with PROPOSED status. | Properties are currently empty; validator enforcement remains NEEDS VERIFICATION. |
| `docs/doctrine/directory-rules.md` | CONFIRMED doctrine / PROPOSED path specifics | Data paths encode lifecycle phase and domain segment; promotion is governed. | Does not prove runtime enforcement. |

## Validation checklist

- [ ] Confirm actual child directories under `data/processed/atmosphere/ozone/`.
- [ ] Confirm accepted OzoneObservation source/domain path convention.
- [ ] Confirm `OzoneObservation` schema fields and title casing are updated beyond scaffold if needed.
- [ ] Confirm OzoneObservation processed validators and CI checks.
- [ ] Confirm SourceDescriptor/source registry linkage for each source-derived ozone artifact.
- [ ] Confirm ozone-vs-AirObservation, ozone-vs-PM2.5, AQI-vs-concentration, observed-vs-model, ozone-vs-AOD/smoke, and observation-vs-advisory boundaries.
- [ ] Confirm station context handling without duplicating station authority.
- [ ] Confirm RunReceipt, TransformReceipt, ValidationReport, PolicyDecision, correction path, and rollback target where applicable.
- [ ] Confirm observed time, retrieval time, report/valid time, source role, units, averaging period, QA/correction posture, caveats, limitations, missingness, confidence, station-location sensitivity, freshness, regulatory/archive posture, and public AQI/report labeling.
- [ ] Confirm no RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, proof, receipt, release, schema, policy, validator, package, pipeline, app, API, station-authority, PM2.5, model, remote-sensing proxy, advisory, official warning, exposure, health/safety, or regulatory-claim artifacts are misplaced here.
- [ ] Confirm promotion flow from processed OzoneObservation data to catalog/triplet/published outputs is governed, source-role-safe, unit-aware, AQI-boundary-aware, evidence-backed, and reversible.
- [ ] Confirm public clients and Focus Mode cannot use this lane as a direct public health, exposure, regulatory, emergency, hazard-impact, or life-safety source.

## Rollback

Rollback is required if this lane becomes an Atmosphere source-data root, AirObservation replacement, PM2.5 replacement, station authority root, AQI/concentration substitution root, ForecastContext replacement, AODRaster replacement, advisory authority root, official warning/public-alerting root, quarantine bypass, proof store, receipt store, catalog root, triplet root, source-registry root, release-decision root, published-output root, public layer root, public tile root, schema root, policy root, validator root, implementation root, public API shortcut, public exposure shortcut, public health/exposure source, regulatory-claim source, emergency instruction source, or life-safety guidance source.

Rollback target for this expansion: previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

<p align="right"><a href="#top">Back to top</a></p>

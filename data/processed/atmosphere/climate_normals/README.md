<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-climate-normals-readme
title: data/processed/atmosphere/climate_normals/README.md — Atmosphere ClimateNormal Processed Data README
version: v0.1
type: readme; data-lifecycle-sublane; processed-stage-guide; atmosphere-domain-lane; climate-normal-lane
status: draft; PROPOSED; data-root; processed-stage; atmosphere; climate-normals; ClimateNormal; release-gated; baseline-aware; aggregation-aware; source-role-aware
owners: OWNER_TBD — Atmosphere steward · Climate steward · Baseline steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; processed; atmosphere; climate-normal; lifecycle; governed; release-gated
tags: [kfm, data, processed, atmosphere, climate-normal, climate-normals, ClimateNormal, ClimateAnomaly, baseline, reference-period, aggregation, lifecycle, RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, EvidenceBundle, SourceDescriptor, AggregationReceipt, ValidationReport, PolicyDecision, ReleaseManifest]
related:
  - ../README.md
  - ../aggregate/climate/README.md
  - ../climate_anomaly/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../contracts/domains/atmosphere/ClimateNormal.md
  - ../../../../contracts/domains/atmosphere/ClimateAnomaly.md
  - ../../../../contracts/domains/atmosphere/TemperatureObservation.md
  - ../../../../contracts/domains/atmosphere/PrecipitationObservation.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/ClimateNormal.schema.json
  - ../../../../schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json
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
  - "This file replaces a blank placeholder at `data/processed/atmosphere/climate_normals/README.md`."
  - "This is the PROCESSED-stage sublane for normalized ClimateNormal artifacts under Atmosphere. It is not raw observation storage, anomaly storage, attribution proof, proof storage, release authority, schema authority, or public climate layer output."
  - "ClimateNormal artifacts must preserve reference period, baseline source, aggregation method, spatial/temporal scope, variable, units, uncertainty/caveats, evidence linkage, policy posture, and release state before public use."
  - "The ClimateNormal contract defines object meaning; this README does not create a second contract or schema authority."
  - "The sibling `data/processed/atmosphere/aggregate/climate/` lane covers broader aggregate climate products; this object-named lane must not become a parallel truth store without a documented convention."
  - "Rollback target for this expansion is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/processed/atmosphere/climate_normals

> Atmosphere PROCESSED-stage sublane for normalized `ClimateNormal` artifacts: governed reference-period climate baselines that remain distinct from raw observations, climate anomalies, forecasts, model fields, attribution claims, proof, release, and public climate surfaces.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data/processed/atmosphere/climate_normals" src="https://img.shields.io/badge/root-data%2Fprocessed%2Fatmosphere%2Fclimate__normals-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Object: ClimateNormal" src="https://img.shields.io/badge/object-ClimateNormal-purple">
  <img alt="Lifecycle: PROCESSED" src="https://img.shields.io/badge/lifecycle-PROCESSED-purple">
  <img alt="Exposure: not public" src="https://img.shields.io/badge/exposure-not__public-critical">
</p>

**Status:** draft / PROPOSED  
**Owners:** OWNER_TBD — Atmosphere steward · Climate steward · Baseline steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward  
**Path:** `data/processed/atmosphere/climate_normals/README.md`  
**Owning root:** `data/processed/`  
**Domain segment:** `atmosphere`  
**Object-family segment:** `climate_normals` / `ClimateNormal`  
**Lifecycle stage:** `PROCESSED`  
**Exposure posture:** not public by default; public use requires governed catalog, evidence, baseline/aggregation disclosure, policy, release, correction, and rollback linkage  
**Truth posture:** CONFIRMED target was blank · CONFIRMED `ClimateNormal` contract and schema paths exist · CONFIRMED `ClimateNormal` is the reference baseline for `ClimateAnomaly` comparison · PROPOSED climate-normals processed-sublane details · NEEDS VERIFICATION for actual child inventory, validators, receipts, CI enforcement, release linkage, and governed route behavior.

**Quick jumps:** [Purpose](#purpose) · [Naming and compatibility note](#naming-and-compatibility-note) · [Lifecycle boundary](#lifecycle-boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [ClimateNormal requirements](#climatenormal-requirements) · [Baseline guardrails](#baseline-guardrails) · [Directory map](#directory-map) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/processed/atmosphere/climate_normals/` holds normalized reference-period climate-baseline artifacts that have moved beyond RAW capture, WORK transforms, and QUARANTINE holds.

This lane is for processed `ClimateNormal` records or derivatives that preserve source identity, source role, reference period, baseline source, aggregation method, variable, units, spatial scope, temporal scope, baseline value semantics, uncertainty/caveats, evidence references, and downstream catalog readiness.

It is not a raw observation lane. It is not a climate-anomaly lane. It is not a climate-attribution proof lane. It is not a trend-significance proof lane. It is not a proof store, receipt store, source registry, catalog, release, semantic contract, schema, policy, public layer, or public API/UI surface. It may support downstream catalog records, EvidenceBundle-backed UI payloads, public-safe climate context layers, Focus Mode summaries, anomaly comparison, or release packages only after gates pass.

## Naming and compatibility note

The repo also contains the broader aggregate climate lane:

```text
data/processed/atmosphere/aggregate/climate/README.md
```

That sibling lane covers aggregate climate products, including `ClimateNormal`, `ClimateAnomaly`-ready derivatives, baselines, normals, anomalies, and climate-context aggregate products. This `climate_normals/` README is intentionally object-named and should be treated as one of these until maintainers settle the convention:

| Naming option | Meaning | Required action |
|---|---|---|
| `aggregate/climate/` | Broad aggregate climate sublane. | Keep as canonical for mixed climate aggregate artifacts if repo convention prefers aggregate-family lanes. |
| `climate_normals/` | Object-family sublane mirroring `ClimateNormal`. | Keep as canonical for normal/baseline-only artifacts if repo convention prefers object-family lanes. |
| Both paths | Transitional / compatibility state. | Add a drift or verification note before storing real data in both. |

> [!CAUTION]
> Do not let `aggregate/climate/` and `climate_normals/` become parallel truth stores. If both paths remain, define which one owns climate-normal artifacts and which one is an alias, index, compatibility shim, or deprecated path.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

```mermaid
flowchart LR
  RAW[data/raw/atmosphere] --> WORK[data/work/atmosphere]
  WORK --> QUAR[data/quarantine/atmosphere]
  WORK --> NORM[data/processed/atmosphere/climate_normals]
  QUAR --> NORM
  NORM --> AGGCLIM[data/processed/atmosphere/aggregate/climate]
  NORM --> ANOM[data/processed/atmosphere/climate_anomaly]
  NORM --> CAT[data/catalog/domain/atmosphere]
  NORM --> STAC[data/catalog/stac/atmosphere]
  NORM --> DCAT[data/catalog/dcat/atmosphere]
  NORM --> PROV[data/catalog/prov/atmosphere]
  NORM -. supports .-> PROOF[data/proofs]
  NORM -. emits / references .-> RECEIPT[data/receipts]
  CAT --> TRIP[data/triplets/.../atmosphere]
  CAT --> PUB[data/published/.../atmosphere]
  STAC --> PUB
  DCAT --> PUB
  PROV --> PUB
  TRIP --> PUB
  PUB --> REL[release]
```

`data/processed/atmosphere/climate_normals/` is upstream of catalog, triplet, publication, and release. It must not be used as a normal public map/API/UI/AI source.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Raw climate, weather, station, grid, normal, anomaly, or model source payloads | `data/raw/atmosphere/` | Not this lane. |
| In-process normal calculations, temporary baselines, joins, scratch outputs, or method experiments | `data/work/atmosphere/` | Not this lane. |
| Rights-unclear, baseline-unclear, malformed, unsupported, disputed, stale, or unsafe climate-normal material | `data/quarantine/atmosphere/` | Not this lane until resolved. |
| Normalized ClimateNormal processed artifacts | `data/processed/atmosphere/climate_normals/` | This lane, if object-family naming is accepted. |
| Broader aggregate climate processed artifacts | `data/processed/atmosphere/aggregate/climate/` | Sibling; must not become a parallel truth store. |
| ClimateAnomaly artifacts | `data/processed/atmosphere/climate_anomaly/` or accepted anomaly lane | Anomaly artifacts must reference this baseline rather than redefine it. |
| Atmosphere domain catalog records | `data/catalog/domain/atmosphere/` | Downstream catalog stage. |
| Atmosphere STAC/DCAT/PROV records | `data/catalog/{stac,dcat,prov}/atmosphere/` | Downstream catalog projections, if accepted. |
| Atmosphere triplet/graph projections | `data/triplets/.../atmosphere/` | Downstream graph stage. |
| Atmosphere public-safe products | `data/published/.../atmosphere/` | Downstream after release. |
| EvidenceBundle/proof records | `data/proofs/` | Separate proof family. |
| Source, run, transform, aggregation, validation, policy, correction, and release receipts | `data/receipts/` | Separate receipt family. |
| SourceDescriptor/source registry records | `data/registry/` | Separate registry family. |
| Release decisions, manifests, rollback cards, corrections, withdrawals | `release/` | Separate publication authority. |
| ClimateNormal semantic contract | `contracts/domains/atmosphere/ClimateNormal.md` | Object meaning; not data. |
| ClimateNormal schema | `schemas/contracts/v1/domains/atmosphere/ClimateNormal.schema.json` | Machine shape; not data. |
| Policy, validators, tests, pipelines, apps, packages | `policy/`, `tools/validators/`, `tests/`, `pipelines/`, `apps/`, `packages/` | Separate roots. |

## Accepted contents

Processed `ClimateNormal` data may include:

- normalized reference-period climate-normal records for supported atmosphere/climate variables;
- processed baseline values for temperature, precipitation, drought/climate context, or other supported variables when source role, units, reference period, aggregation window, and method are preserved;
- spatial baseline products such as county, region, grid, tile-safe, station-network, basin-adjacent, or other governed aggregate units when the spatial unit is documented;
- temporal baseline products such as monthly normals, seasonal normals, annual normals, climatological normal periods, rolling-window normals, or other reviewed baseline periods when the temporal unit is documented;
- uncertainty, caveat, quality, missingness, station coverage, interpolation, baseline, and method metadata sidecars when those sidecars are not proofs, receipts, source registry records, catalog records, schemas, or policy rules;
- processed artifacts prepared for downstream domain catalog, STAC/DCAT/PROV packaging, EvidenceBundle support, triplet generation, anomaly comparison, or release review.

## Exclusions

Do not store these under `data/processed/atmosphere/climate_normals/`:

- RAW source files, raw station observations, raw gridded products, source-native climate normals, source-native anomaly products, forecasts, model fields, screenshots, or downloads.
- WORK/scratch outputs that have not passed processing gates.
- Quarantined, malformed, baseline-unclear, source-role-unclear, rights-unclear, unsupported, disputed, stale, or unsafe climate-normal material.
- ClimateAnomaly records unless only referenced as downstream anomaly consumers.
- Direct observation records such as `TemperatureObservation`, `PrecipitationObservation`, `WeatherObservation`, station records, air-quality observations, AQI summaries, smoke/AOD rasters, advisory context, or forecast/model objects unless only referenced as lineage and stored in their correct lanes.
- Climate attribution claims, trend-significance claims, event/hazard truth, damages, health/safety claims, or policy conclusions.
- Domain catalog records, STAC records, DCAT records, PROV records, triplet/graph records, published outputs, proofs, receipts, source registry records, release records, schemas, policy rules, validators, tests, pipelines, app/UI/API code.

## ClimateNormal requirements

PROPOSED until concrete validators and CI enforcement are verified:

| Requirement | Meaning |
|---|---|
| Source trace | Every processed ClimateNormal artifact should trace to SourceDescriptor or source registry context when source authority matters. |
| Reference period | Every normal should identify its reference period, baseline method, source period, and applicability scope. |
| Baseline disclosure | Baseline identity, baseline source, baseline construction method, and caveats should remain visible where material. |
| Aggregation receipt | Aggregation method, spatial unit, temporal unit, variable, units, weighting, interpolation, missingness, and quality posture should resolve to receipt or validation context. |
| Source-role preservation | Observations, model fields, forecasts, normals, anomalies, and derived products must remain labeled as their actual role. |
| Anomaly support | ClimateNormal artifacts may support ClimateAnomaly comparison, but anomaly records must remain separate and explicitly reference the normal/baseline. |
| Evidence linkage | Claims about normal value, baseline period, method, scope, uncertainty, correction, or release should resolve downstream to EvidenceBundle/proof context. |
| Policy posture | Public display requires rights, source-role, baseline, aggregation, caveat, and policy/admissibility posture. |
| Catalog readiness | Processed ClimateNormal artifacts intended for discovery should promote through Atmosphere catalog lanes, not directly to public use. |
| Release readiness | Public use requires release state, published output path, correction path, and rollback target. |
| No attribution by default | ClimateNormal context does not prove cause, impact, damages, or trend significance without separate evidence and review. |
| Path convention | If `aggregate/climate/` and `climate_normals/` both exist, maintainers must decide whether one is canonical and record the decision before storing real artifacts in both. |

## Baseline guardrails

- `ClimateNormal` is a reference-period climate baseline, not a raw observation.
- `ClimateNormal` defines or carries the baseline context that `ClimateAnomaly` may compare against; it is not an anomaly by itself.
- A climate normal does not prove climate attribution, cause, impact, damages, or trend significance by itself.
- Model fields and forecasts must remain labeled as model or forecast context.
- Public climate-normal products require reference-period disclosure, aggregation/method disclosure, evidence, policy, release state, correction path, and rollback target.
- Focus Mode may summarize ClimateNormal context only as evidence-bounded, baseline-aware, aggregation-aware, and release-aware context. It must not invent attribution, trend significance, hazard impacts, damages, or health/safety guidance.
- Unreleased processed ClimateNormal artifacts are not public merely because they exist under this directory.

> [!CAUTION]
> Do not use this lane as a shortcut from processed normal/baseline data to attribution, trend-significance, hazard-impact, damages, or health/safety claims. ClimateNormal products must pass catalog, evidence, policy, validation, release, correction, and rollback gates before public use.

## Directory map

Actual child inventory remains **NEEDS VERIFICATION**. Use this as a proposed local organization pattern only after confirming current repo convention and validators.

```text
data/processed/atmosphere/climate_normals/
├── README.md
├── normalized/              # PROPOSED — processed ClimateNormal records
├── baselines/               # PROPOSED — reference-period baseline products
├── reference_periods/       # PROPOSED — baseline period metadata, not release authority
├── quality/                 # PROPOSED — missingness, coverage, uncertainty, caveats
├── methods/                 # PROPOSED — local method summaries, not canonical receipts
├── joins/                   # PROPOSED — links to observations, anomalies, forecasts, context objects
├── _manifests/              # PROPOSED — lane-local non-release manifests only
└── _README_TODO.md          # PROPOSED — remove after actual child inventory is documented
```

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a blank placeholder. | Did not define ClimateNormal PROCESSED-stage boundaries. |
| `data/processed/atmosphere/aggregate/climate/README.md` | CONFIRMED sibling README | Existing aggregate climate child lane and climate guardrails. | Does not decide whether `aggregate/climate/` or `climate_normals/` is canonical. |
| `data/processed/atmosphere/climate_anomaly/README.md` | CONFIRMED sibling README | Existing object-named ClimateAnomaly lane and baseline-anchor guardrails. | Does not define ClimateNormal inventory or release behavior. |
| `data/processed/atmosphere/README.md` | CONFIRMED | Parent atmosphere processed lane exists as a greenfield stub. | Does not define parent Atmosphere processed boundaries yet. |
| `data/processed/README.md` | CONFIRMED | Parent processed lane is upstream of catalog, triplets, and publication and is not public by default. | Does not prove child inventory under this lane. |
| `data/catalog/domain/atmosphere/README.md` | CONFIRMED | Atmosphere catalog lane includes climate normals downstream and preserves source-role guardrails. | Does not prove ClimateNormal processed inventory or release behavior. |
| `docs/domains/atmosphere/README.md` | CONFIRMED doctrine / PROPOSED implementation | Atmosphere owns climate context, normals, anomalies, and source-role denials. | Implementation maturity and runtime behavior remain NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/ClimateNormal.md` | CONFIRMED contract file | Defines ClimateNormal as governed reference-period baseline context, not raw observation, anomaly, attribution, proof, release, or health/safety guidance. | Contract does not prove schema enforcement, validator behavior, or release approval. |
| `contracts/domains/atmosphere/ClimateAnomaly.md` | CONFIRMED contract file | Defines ClimateAnomaly as a downstream baseline-relative comparison object that must anchor to a normal/baseline. | Contract does not prove schema enforcement, validator behavior, or release approval. |
| `schemas/contracts/v1/domains/atmosphere/ClimateNormal.schema.json` | CONFIRMED scaffold schema | Paired ClimateNormal schema exists with PROPOSED status. | Properties are currently empty; validator enforcement remains NEEDS VERIFICATION. |
| `docs/doctrine/directory-rules.md` | CONFIRMED doctrine / PROPOSED path specifics | Data paths encode lifecycle phase and domain segment; promotion is governed. | Does not prove runtime enforcement. |

## Validation checklist

- [ ] Confirm actual child directories under `data/processed/atmosphere/climate_normals/`.
- [ ] Decide whether `aggregate/climate/` or `climate_normals/` is the canonical processed sublane for `ClimateNormal` artifacts.
- [ ] Confirm accepted ClimateNormal source/domain path convention.
- [ ] Confirm `ClimateNormal` schema fields and title casing are updated beyond scaffold if needed.
- [ ] Confirm ClimateNormal processed validators and CI checks.
- [ ] Confirm SourceDescriptor/source registry linkage for each source-derived ClimateNormal artifact.
- [ ] Confirm ClimateAnomaly anchor handling without duplicating anomaly records.
- [ ] Confirm RunReceipt, TransformReceipt, AggregationReceipt, ValidationReport, PolicyDecision, correction path, and rollback target where applicable.
- [ ] Confirm reference period, baseline source, aggregation method, spatial unit, temporal unit, variable, units, uncertainty, caveats, missingness, and source-role handling.
- [ ] Confirm no RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, proof, receipt, release, schema, policy, validator, package, pipeline, app, API, anomaly, attribution, trend-significance, hazard-impact, or health/safety artifacts are misplaced here.
- [ ] Confirm promotion flow from processed ClimateNormal data to catalog/triplet/published outputs is governed, baseline-aware, aggregation-aware, source-role-safe, evidence-backed, and reversible.
- [ ] Confirm public clients and Focus Mode cannot use this lane as a direct climate-attribution, trend-significance, hazard-impact, damages, or health/safety source.

## Rollback

Rollback is required if this lane becomes an Atmosphere source-data root, duplicate truth store beside `aggregate/climate/`, anomaly authority root, climate-attribution source, trend-significance source, hazard-impact source, quarantine bypass, proof store, receipt store, catalog root, triplet root, source-registry root, release-decision root, published-output root, schema root, policy root, validator root, implementation root, public API shortcut, public exposure shortcut, or health/safety guidance source.

Rollback target for this expansion: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/sources/atmosphere/readme
name: Atmosphere Source Registry README
path: data/registry/sources/atmosphere/README.md
type: data-registry-source-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <atmosphere-domain-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <policy-steward>
  - <hazards-liaison>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry/source-domain
registry_scope: atmosphere-source-descriptor-routing-and-admission-control
path_posture: existing-scaffold-replaced; canonical-under-data-registry-sources; atmosphere-descriptor-payloads-unknown; validators-ci-runtime-readers-unknown; air-vs-atmosphere-slug-drift-needs-adr
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; rights-and-sensitivity-fail-closed; not-emergency-alerting; not-life-safety-advice; official-advisory-redirection-required; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../source_descriptors/README.md
  - ../../../raw/atmosphere/
  - ../../../work/atmosphere/
  - ../../../quarantine/atmosphere/
  - ../../../processed/atmosphere/
  - ../../../catalog/atmosphere/
  - ../../../triplets/atmosphere/
  - ../../../published/atmosphere/
  - ../../../receipts/atmosphere/
  - ../../../proofs/atmosphere/
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../contracts/domains/atmosphere/
  - ../../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../../policy/domains/atmosphere/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../release/candidates/atmosphere/
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/doctrine/directory-rules.md
tags:
  - kfm
  - data
  - registry
  - sources
  - atmosphere
  - air
  - climate
  - weather
  - smoke
  - aerosol
  - air-quality
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - evidence
  - provenance
  - stale-state
  - official-advisory-redirection
  - not-emergency-alerting
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the scaffold at `data/registry/sources/atmosphere/README.md`."
  - "This lane is a domain segment of the canonical source registry parent at `data/registry/sources/`."
  - "Atmosphere source descriptors are admission/control records. They do not store source payloads, decide policy, emit receipts, prove claims, close catalogs, publish artifacts, provide emergency alerts, or authorize public map/API exposure."
  - "Examples of atmosphere source families in this README are routing candidates only until concrete SourceDescriptor records, rights review, sensitivity review, receipts, proofs, catalog records, and release decisions are verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Source Registry

Domain source-registry lane for Atmosphere / Air / Climate source descriptors and admission-control routing.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data registry sources" src="https://img.shields.io/badge/root-data%2Fregistry%2Fsources-0a7ea4">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f8fff">
  <img alt="Boundary: not emergency alerting" src="https://img.shields.io/badge/boundary-not%20emergency%20alerting-critical">
  <img alt="Boundary: not release" src="https://img.shields.io/badge/boundary-not%20release-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) - [Path posture](#path-posture) - [Atmosphere source families](#atmosphere-source-families) - [Source-role handling](#source-role-handling) - [Atmosphere risk controls](#atmosphere-risk-controls) - [Accepted material](#accepted-material) - [Exclusions](#exclusions) - [Suggested directory shape](#suggested-directory-shape) - [Required checks](#required-checks-before-use) - [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/sources/atmosphere/` is a source-registry control lane. It is not atmosphere data storage, current-weather truth, emergency alerting, life-safety advice, AQI truth, air-quality compliance proof, model-output proof, policy authority, proof authority, catalog authority, release authority, public API material, public map material, or generated-answer authority.

---

## Scope

This directory records how atmosphere, air-quality, weather, smoke, aerosol, climate, and forecast-context sources may be treated before their material enters the KFM lifecycle. It belongs under the canonical source-registry parent:

```text
data/registry/sources/
```

Atmosphere SourceDescriptor-style records may describe source identity, source role, steward, upstream authority, rights posture, sensitivity posture, update cadence, valid/effective time, observation time, forecast/model run time, station or grid scope, parameter scope, units, attribution requirements, stale-state handling, correction path, supersession path, and rollback references.

The registry can help decide whether atmosphere material is admitted, quarantined, restricted, delayed, generalized, or denied. It does **not** make an air-quality, weather, smoke, AOD, climate, advisory, forecast, exposure, health, compliance, crop-impact, hydrology-impact, or hazard claim true.

---

## Path posture

The requested lane is:

```text
data/registry/sources/atmosphere/
```

Directory Rules evidence from the attached copy allows domain-scoped registry lanes using either:

```text
data/registry/<domain>/
data/registry/sources/<domain>/
```

The current registry root and source-registry parent identify `data/registry/sources/` as the source admission and authority-control surface. The atmosphere domain docs also list `data/registry/sources/atmosphere/` as the source-descriptor lane in the domain pattern.

Therefore this atmosphere lane is treated as a subtype-first source-registry domain lane, not a parallel domain registry, dataset registry, proof lane, catalog lane, release lane, hazards advisory lane, or public-surface lane.

The sibling compatibility lane:

```text
data/registry/source_descriptors/
```

must not duplicate authoritative atmosphere SourceDescriptor records from this path. If a future migration changes the canonical source-descriptor topology, add a migration note, redirect, ADR reference, or Directory Rules update before moving records.

> [!WARNING]
> The atmosphere docs identify a slug conflict between `air` and `atmosphere` for some contract/schema homes. This README follows the current requested path and the Directory Rules-style domain segment `atmosphere`, but final slug authority remains **NEEDS VERIFICATION** until reconciled by ADR or drift resolution.

---

## Atmosphere source families

The table below is **PROPOSED routing guidance**, not evidence that these records exist in the repo. Add concrete descriptors only after rights, sensitivity, source-role, cadence, unit, stale-state, and steward review.

| Source family | Possible use | Required caution |
|---|---|---|
| Regulatory air-quality observations and archives | Station, parameter, concentration, method, QA, and regulatory archive context. | Preserve parameter, units, method, instrument, averaging interval, QA status, valid time, revision status, and authority scope. Do not treat AQI as concentration. |
| Public AQI and smoke/air-quality reporting feeds | Public-facing AQI, smoke, advisory context, and time-sensitive situational context. | Not health advice or emergency direction. Carry official-source redirection, stale-state handling, valid/effective time, and caveats. |
| Weather station and mesonet observations | Temperature, wind, precipitation, humidity, pressure, and station observation context. | Preserve station identity, sensor type, siting, QA flags, observation time, unit conversions, and missing/stale markers. |
| National weather forecast and advisory context | Forecast context, watches/warnings/advisories as official-source references, and time-aware context. | Hazards owns emergency and life-safety truth. Atmosphere may carry advisory context only with official issuing authority, valid/effective time, and redirection. |
| Climate normals and anomaly products | Normal-period context, departures, climate summaries, and long-term comparison. | Preserve baseline period, method, spatial/temporal scale, uncertainty, and revision state. Do not mix climate normals with real-time observations. |
| Satellite aerosol, smoke, fire, and cloud-adjacent products | AOD rasters, smoke plume context, detected hotspots, imagery-derived atmosphere context. | AOD is not PM2.5. Satellite detections are contextual/derived and require resolution, algorithm, cloud/snow/surface limitations, QA flags, and time scope. |
| Forecast or reanalysis model fields | HRRR-smoke-style fields, forecast grids, reanalysis context, and modeled atmosphere variables. | Model fields are not observations. Preserve model name, run time, forecast hour, inputs, version, uncertainty, and validation state. |
| Low-cost sensor networks | Neighborhood or local sensor context where rights and QA allow. | Requires calibration/correction/caveat posture, confidence limits, sensor owner/terms, privacy review, QA, and release limits. |
| Research, university, or local monitoring projects | Specialized observations, field campaigns, reports, or context. | Treat as contextual or candidate until method, rights, QA, steward, and source role are registered. |
| Historic weather, climate, smoke, or air-quality records | Historical time series, event context, climate history, and archival comparison. | Preserve source vintage, station changes, instrumentation changes, digitization uncertainty, and time-zone/calendar handling. |

---

## Source-role handling

Atmosphere sources are high-risk for role collapse because AQI, concentration, satellite AOD, smoke plumes, model fields, forecasts, advisories, low-cost sensors, and climate normals are often conflated. Preserve source role from admission through processing, proof, catalog, map, graph, and generated-answer use.

| Source role | Atmosphere example | Boundary |
|---|---|---|
| `observed` | QA-qualified station observation or direct measurement with method and time scope. | Does not include AQI summaries, model fields, forecasts, satellite-derived rasters, or low-confidence sensor data unless reviewed as observed. |
| `regulatory` | Official air-quality archive, official advisory, official standard, or compliance-context record. | Regulatory status is not the same as a measured concentration and is not release permission. |
| `modeled` | Forecast grid, smoke model, reanalysis field, AOD-derived estimate, or interpolation surface. | Requires model/run refs, input scope, uncertainty, forecast hour/run time, and validation posture. |
| `aggregate` | Daily summary, county/region average, monitor rollup, climate normal, anomaly, or percentile. | Must not be treated as point-station, household, parcel, field, or event-level truth. |
| `administrative` | Station inventory, network metadata, parameter list, code table, or agency maintained index. | Administrative presence does not prove current operation, data quality, or release status. |
| `candidate` | Unreviewed feed, provisional station match, new sensor, OCR extraction, geocode, or unverified endpoint. | Blocks publication until reviewed, promoted, corrected, or rejected. |
| `synthetic` | Demo atmosphere layer, generated forecast example, tutorial fixture, or simulated weather scenario. | Requires a reality-boundary note and must not be mixed with evidence claims. |
| `context` | Advisory text, smoke context, fire context, climate context, or explanatory report. | Useful for interpretation but insufficient as proof by itself. |
| `restricted` | Rights-limited feed, private sensor network, operational endpoint, security-relevant facility context, or re-identifying join. | Defaults to deny, quarantine, redact, delay, generalize, or restrict until policy and review gates close. |

---

## Atmosphere risk controls

Atmosphere material can be public in broad form while still risky when stale, overclaimed, misinterpreted, joined, or reused as advice. Default to the narrowest accurate claim and carry time/caveat metadata forward.

| Risk | Required posture |
|---|---|
| Emergency or life-safety use | Do not provide advice or operational direction. Redirect to the official issuing authority and Hazards lane where applicable. |
| Stale observations, forecasts, advisories, or feeds | Carry observation time, issue time, valid/effective time, expiration, retrieval time, revision status, and stale-state handling. |
| AQI, concentration, and health interpretation | Do not collapse AQI, concentration, regulatory category, exposure, or health guidance. Cite official scope and preserve units/averaging interval. |
| AOD, smoke, and PM2.5 confusion | AOD and smoke products are context/derived material, not direct PM2.5 measurements unless a governed method proves otherwise. |
| Model fields treated as observations | Preserve model/run identity, forecast hour, inputs, uncertainty, validation state, and RealityBoundaryNote or equivalent when needed. |
| Low-cost or community sensors | Require QA/correction/caveat profile, sensor terms, calibration posture, privacy review, and confidence limits. |
| Cross-domain impact claims | Atmosphere can supply context to hazards, agriculture, hydrology, habitat, flora, fauna, settlements, or infrastructure. It does not own those downstream claims. |
| Private, operational, facility, or security-sensitive joins | Review exact station/facility, infrastructure, private-network, or operational details before public release. |

---

## Accepted material

Accepted material in this lane is limited to source-registry support for Atmosphere / Air / Climate:

- this README and other registry-local guidance;
- atmosphere SourceDescriptor records when their schema home, naming convention, steward, rights review, sensitivity review, source-role review, and stale-state rules are verified;
- atmosphere source-family indexes that point to canonical descriptor records;
- source-role vocabulary notes that do not replace the canonical vocabulary/schema;
- supersession, correction, stale-state, withdrawal, and rollback pointers for atmosphere sources;
- redirect or migration notes if atmosphere descriptors are moved between registry shapes;
- blocker notes that identify missing rights, sensitivity, source-role, units, evidence, receipt, catalog, release, correction, or rollback support.

Keep registry records compact and pointer-based. Store only the control state needed to govern admission and use. Do not embed atmospheric datasets, tiles, model grids, station time series, alert text payloads, or operational endpoint secrets here.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw atmosphere datasets, API dumps, station files, satellite rasters, model grids, alerts/advisory payloads, imagery, tables, shapefiles, GeoJSON, GeoParquet, COG, PMTiles, or time-series exports | `data/raw/atmosphere/`, `data/work/atmosphere/`, or `data/quarantine/atmosphere/` depending on review state |
| Normalized atmosphere objects, station observations, derived fields, rasters, model products, or processed analytics | `data/processed/atmosphere/` |
| Emergency/hazard event truth or life-safety advisory decisions | Hazards-owned lanes and official issuing authority references; not this source registry lane |
| STAC/DCAT/PROV/domain catalog records | `data/catalog/atmosphere/` or accepted catalog lane |
| Graph/triplet projections | `data/triplets/atmosphere/` |
| Published public-safe artifacts | `data/published/atmosphere/` or accepted published lane only after release |
| Validation, ingest, transform, redaction, model, policy, review, or run receipts | `data/receipts/atmosphere/` or accepted receipt lane |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/atmosphere/` or accepted proof lane |
| SourceDescriptor schemas or JSON Schema definitions | `schemas/contracts/v1/` or accepted schema root |
| Semantic contracts | `contracts/domains/atmosphere/` or accepted contract lane after slug resolution |
| Rights, sensitivity, access, stale-state, advisory, runtime, or release policy rules | `policy/domains/atmosphere/`, `policy/rights/`, `policy/sensitivity/`, or accepted policy lanes |
| Connectors, watchers, scrapers, ETL code, model code, or validator code | `connectors/`, `pipelines/`, `packages/`, `tools/`, or accepted implementation roots |
| Release manifests, promotion decisions, correction notices, withdrawal notices, supersession decisions, or rollback cards | `release/candidates/atmosphere/` or accepted release lanes |
| Secrets, credentials, tokens, private endpoint details, or restricted operational access procedures | never in registry; use approved restricted storage and secret management |

---

## Suggested directory shape

This shape is **PROPOSED** until descriptor naming, schema home, validator discovery, slug resolution, and CI are verified.

```text
data/registry/sources/atmosphere/
├── README.md
├── index.local.json                 # PROPOSED pointer index only
├── source_families.local.yaml       # PROPOSED local routing vocabulary only
├── superseded/                      # PROPOSED retained descriptor pointers
│   └── README.md
└── descriptors/                     # PROPOSED only after schema/topology decision
    └── <source_id>.descriptor.yaml
```

Prefer one canonical descriptor location. If descriptor files are placed directly under this directory instead of `descriptors/`, document that convention before adding records.

---

## Minimum descriptor fields

The exact schema remains governed by the accepted SourceDescriptor schema. Atmosphere descriptors should not be considered review-ready unless they can resolve at least the following control facts:

| Field family | Minimum expectation |
|---|---|
| Identity | Stable KFM source ID, upstream source name, upstream identifier where applicable, steward, source owner/authority role, and contact path. |
| Source role | One explicit role with authority scope and no role upgrading. |
| Domain scope | Atmosphere scope plus any linked domain context, such as hazards, hydrology, agriculture, habitat, flora, fauna, settlements, infrastructure, roads/rail/trade, or geology. |
| Time scope | Observation time, issue time, valid/effective time, forecast/model run time, forecast hour, retrieval time, update cadence, expiration, stale-state rule, and revision handling. |
| Measurement scope | Parameter, units, averaging interval, method, instrument/sensor class, QA flags, station/grid scope, resolution, uncertainty, and conversion rules where applicable. |
| Geography scope | Station location, grid extent, plume/raster footprint, aggregation unit, precision, generalization/redaction profile, and uncertainty where applicable. |
| Rights scope | License, terms, attribution, redistribution posture, endpoint terms, use restrictions, expiration, and rights review state. |
| Sensitivity scope | Public/restricted posture, operational endpoint risk, private-network risk, facility/security join risk, and release class. |
| Evidence linkage | EvidenceRef/EvidenceBundle expectations, proof requirements, catalog refs, receipt refs, and release blockers. |
| Correction path | Supersession, withdrawal, correction notice, stale-state, and rollback pointers. |

---

## Required checks before use

- [ ] Confirm the source belongs in the atmosphere source-registry lane and not only in hazards, hydrology, agriculture, habitat, flora, fauna, catalog, proof, release, or another domain lane.
- [ ] Confirm `SourceDescriptor` schema home, descriptor filename convention, validator discovery, slug choice, and CI before adding descriptor payloads.
- [ ] Confirm rights, attribution, endpoint terms, redistribution posture, rate-limit posture, access limits, and review state.
- [ ] Confirm sensitivity and exposure posture, especially for operational feeds, private sensors, restricted endpoint terms, facility/security joins, and public-facing health/advisory reuse.
- [ ] Confirm source role and prevent AQI, AOD, smoke products, model fields, forecasts, advisory context, climate normals, aggregate summaries, or low-cost sensor data from being treated as direct observed truth unless reviewed as such.
- [ ] Confirm observation time, issue time, valid/effective time, forecast/model run time, forecast hour, source vintage, expiration, stale-state handling, correction path, supersession path, and rollback refs.
- [ ] Confirm units, parameter identity, averaging interval, QA flags, conversion rules, method, and uncertainty are preserved.
- [ ] Confirm any cross-domain join has explicit source-role, policy, proof, and release support.
- [ ] Confirm validation, transform, model, QA, policy, and review receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist before consequential atmosphere claims are used publicly.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them here.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, dashboard, fixture, or local index reads this registry lane as direct public truth or emergency guidance.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the scaffold at `data/registry/sources/atmosphere/README.md`. | CONFIRMED authored |
| The requested target path existed in the live repository as a scaffold before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/README.md` exists and frames registry records as governance/control records, not payloads, schemas, policy, receipts, proofs, catalogs, releases, or public output authority. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/README.md` exists and frames `data/registry/sources/` as the pre-RAW source admission and authority-control surface. | CONFIRMED by GitHub contents API during this edit |
| `docs/domains/atmosphere/README.md` identifies Atmosphere as air-quality, weather, smoke, AOD, climate, and model context, not an emergency advisory or life-safety system. | CONFIRMED by GitHub contents API during this edit |
| `docs/domains/atmosphere/README.md` warns that AQI is not concentration, AOD is not PM2.5, model fields are not observations, and low-cost sensor public release requires correction/caveats/confidence/limitations. | CONFIRMED by GitHub contents API during this edit |
| `docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md` lists `data/registry/sources/atmosphere/` as the source-descriptor and rights-record lane, while marking concrete endpoint/rights details as not to infer. | CONFIRMED by GitHub contents API during this edit |
| The attached Directory Rules copy includes `data/registry/<domain>/` or `data/registry/sources/<domain>/` as valid registry/domain shapes. | CONFIRMED by local PDF text extraction during this edit |
| Concrete atmosphere SourceDescriptor payloads exist under this lane. | UNKNOWN |
| Atmosphere descriptor schema home, slug choice, filename convention, validator discovery, and CI enforcement are verified. | NEEDS VERIFICATION |
| Atmosphere rights/sensitivity/stale-state policy profiles are complete. | UNKNOWN |
| Atmosphere catalog/proof/release wiring is implemented. | UNKNOWN |
| Runtime registry resolution or governed API behavior reads this lane. | UNKNOWN |
| This README grants public access to atmosphere source-registry internals or emergency guidance. | DENY |

---

## Maintainer note

Atmosphere source descriptors are useful because they preserve source identity, source role, rights, sensitivity, time scope, units, methods, QA flags, uncertainty, stale-state, correction, and rollback before data enters the KFM lifecycle. They become dangerous when treated as current truth, health advice, emergency direction, or a shortcut around proof and release.

Keep the chain explicit:

```text
Atmosphere SourceDescriptor -> rights/sensitivity/stale-state gate -> RAW or QUARANTINE admission -> lifecycle processing -> validation/QA/model/review receipts -> EvidenceBundle/proof -> catalog/triplet -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> atmosphere truth -> emergency advice/public map/API/generated answer
```

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-atmosphere-pm25-readme
title: data/processed/atmosphere/pm25/ — Atmosphere PM2.5 Processed Data
version: v0.2.0
type: directory-readme
subtype: processed-atmosphere-pm25-observation-lane
status: repository-grounded draft; payload inventory, enforceable schema, validators, fixtures, receipts, proof, release, and runtime behavior remain bounded
owners:
  - "NEEDS VERIFICATION — Atmosphere domain steward"
  - "NEEDS VERIFICATION — PM2.5 and air-quality observation steward"
  - "NEEDS VERIFICATION — source-role, units, QA, low-cost-sensor, and regulatory/archive reviewers"
  - "NEEDS VERIFICATION — data, evidence, policy, release, correction, rollback, and docs stewards"
created: NEEDS VERIFICATION — one-character placeholder existed before v0.1 expansion
updated: 2026-07-25
policy_label: public-doc; processed-stage; atmosphere; pm25; pollutant-specific-observation; source-role-aware; AQI-boundary-aware; low-cost-caveat-aware; release-gated; no-direct-public-path
path: data/processed/atmosphere/pm25/README.md
truth_posture: >
  CONFIRMED exact target path, prior blob, Directory Rules placement, current Atmosphere parent lane,
  PM25Observation semantic contract, paired scaffold schema posture, pollutant-specific boundary,
  AQI/concentration separation, AOD denial, modeled-versus-observed separation, low-cost caveat rule,
  and PROCESSED lifecycle boundary / PROPOSED lane-local admission profile, normalized PM2.5 packet,
  role-specific method and QA requirements, and downstream promotion expectations / UNKNOWN recursive
  payload inventory, production validators, fixtures, receipts, proof closure, release instances, hosting,
  and public behavior / NEEDS VERIFICATION accountable owners, accepted source-role vocabulary,
  unit and averaging conventions, correction methods, freshness limits, regulatory/archive treatment,
  correction propagation, cache invalidation, and rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9f192b09fd64912919acfda69d638006a7817185
  prior_blob: dfd11264924f723065be6d6588a55057bdc3a1a5
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  pm25_contract_blob: dabc318f6dcf4267858cb4953c3379ac2a60879d
related:
  - ../README.md
  - ../observed/README.md
  - ../air_observations/README.md
  - ../air_stations/README.md
  - ../ozone/README.md
  - ../forecast_context/README.md
  - ../modeled/README.md
  - ../aod/README.md
  - ../advisory_context/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../../docs/domains/atmosphere/POLICY.md
  - ../../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../contracts/domains/atmosphere/AirStation.md
  - ../../../../contracts/domains/atmosphere/OzoneObservation.md
  - ../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/PM25Observation.schema.json
  - ../../../../policy/domains/atmosphere/README.md
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../triplets/README.md
  - ../../../proofs/README.md
  - ../../../receipts/README.md
  - ../../../registry/sources/atmosphere/README.md
  - ../../../../release/candidates/atmosphere/README.md
  - ../../../../release/README.md
notes:
  - "Same-path Markdown modernization only; no PM2.5 bytes, source state, contract, schema, policy, validator, workflow, proof, release, route, hosting, or KFM publication state changed."
  - "PM25Observation is pollutant-specific air-quality context whose source role determines whether a value is observed concentration, public AQI/report posture, low-cost sensor data, or separately reviewed regulatory/archive context."
  - "AQI is not concentration, AOD is not PM2.5, modeled PM2.5 is not observed PM2.5, and low-cost values require caveat, correction, confidence, limitation, policy, and review context."
  - "Rollback target for v0.2.0 is prior blob SHA `dfd11264924f723065be6d6588a55057bdc3a1a5`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/atmosphere/pm25/` — Atmosphere PM2.5 processed data

> **One-line purpose.** Hold normalized PM2.5 observation candidates while preserving pollutant identity, source role, station context, concentration or report semantics, units, averaging period, time, method, QA, caveats, uncertainty, evidence, correction, and downstream-use limits.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Role: pollutant specific](https://img.shields.io/badge/role-pollutant%20specific-1f8fff?style=flat-square)](#what-belongs-here)
[![Exposure: not public](https://img.shields.io/badge/exposure-not%20public-b42318?style=flat-square)](#outputs)
[![AQI: not concentration](https://img.shields.io/badge/AQI-not%20concentration-6f42c1?style=flat-square)](#source-role-units-and-method)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation)

> [!IMPORTANT]
> **A PM2.5 number is not self-explanatory.** The same apparent value can represent an observed concentration, a public AQI/report value, a low-cost sensor estimate, an archive record, a modeled field, or an unsupported transformation. Source role, units, averaging period, method, QA, time, and caveats determine what the number can support.

**Path:** `data/processed/atmosphere/pm25/README.md`  
**Owning root:** `data/`  
**Lifecycle phase:** `processed/`  
**Domain segment:** `atmosphere/`  
**Parent lane:** `data/processed/atmosphere/`  
**Lane role:** pollutant-specific `PM25Observation` context  
**Direct public access:** denied  
**Last reviewed:** 2026-07-25

**Quick navigation:** [Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does NOT belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [PM25Observation admission profile](#pm25observation-admission-profile) · [Source role, units, and method](#source-role-units-and-method) · [PM2.5 guardrails](#pm25-guardrails) · [Lifecycle and promotion](#lifecycle-and-promotion) · [Correction and rollback](#correction-and-rollback)

---

## Purpose

This directory is the Atmosphere domain's **PROCESSED-stage lane for pollutant-specific PM2.5 records**. It may hold normalized concentration observations, source-labeled public AQI/report records, caveated low-cost sensor records, separately reviewed regulatory/archive records, and object-ready derivatives that have moved beyond RAW capture, WORK transformation, and QUARANTINE holds.

The lane exists to preserve the answer to seven questions before downstream use:

1. Which pollutant and measurement or report semantics are represented?
2. Which source role applies: observed sensor, public AQI/report, low-cost sensor, regulatory/archive, model context, or another reviewed role?
3. Which station/network, method, instrument, correction, or archive context supports the record?
4. Which units, averaging period, observed time, source time, retrieval time, and freshness state apply?
5. Which QA, uncertainty, caveat, confidence, limitation, and correction state qualify the value?
6. Which evidence, rights, policy, sensitivity, review, release, and rollback states apply?
7. Which downstream claims and uses are allowed, restricted, narrowed, delayed, or denied?

It is not a generic air-observation store, AQI-to-concentration converter, AOD-to-PM2.5 converter, modeled-field store, advisory authority, proof store, receipt authority, catalog authority, release authority, health-advice service, or public map/API/UI source.

## Authority level

**Implementation-bearing lifecycle lane.** The target path is CONFIRMED in the repository and remains under `data/processed/atmosphere/`, consistent with Directory Rules' lifecycle and domain-placement rules.

Its authority is deliberately narrow:

- it may carry processed PM2.5 candidates and lane-local explanatory metadata;
- it does not define `PM25Observation` meaning—that remains in the semantic contract;
- it does not define machine shape—the paired schema remains under `schemas/contracts/v1/domains/atmosphere/`;
- it does not decide whether a value is concentration, AQI/report, regulatory, reference-grade, low-cost, modeled, valid, consequential, or publishable;
- it does not prove calibration, regulatory exceedance, exposure, health effect, damage, or impact;
- it does not authorize emergency, medical, occupational, or life-safety guidance.

## Status

| Surface | Status | Evidence-bounded interpretation |
|---|---|---|
| This README and path | **CONFIRMED** | The file exists at the pinned base and is updated in place. |
| Parent Atmosphere processed lane | **CONFIRMED** | `data/processed/atmosphere/README.md` identifies `pm25/` as the pollutant-specific PM2.5 lane and denies direct public use. |
| `PM25Observation` semantic contract | **CONFIRMED repository document / draft** | Defines role-dependent PM2.5 meaning, AQI/concentration separation, low-cost caveat requirements, AOD/model denial, and non-release authority. |
| Paired `PM25Observation` schema | **CONFIRMED scaffold / not enforceable as verified** | The contract reports empty properties, `additionalProperties: true`, and unresolved title casing. |
| Adjacent observation and context lanes | **CONFIRMED paths** | General observations, stations, ozone, AOD, modeled/forecast, advisory, and observed-parent lanes remain separate responsibilities. |
| Real processed PM2.5 payload inventory | **UNKNOWN** | This documentation task did not inspect or expose PM2.5 data payloads. |
| Validators, fixtures, policy enforcement, and CI | **NEEDS VERIFICATION** | No accepted production PM2.5 enforcement suite was verified. |
| Receipts, proof, release instances, hosting, public behavior | **UNKNOWN / held** | Presence in this directory creates none of these states. |

## What belongs here

Good fits are processed PM2.5 artifacts whose pollutant, source-role, method, time, and QA lineage remain inspectable, including:

- normalized PM2.5 concentration candidates tied to an `AirStation` or other reviewed station/network context;
- source-labeled `OBSERVED_SENSOR` concentration records with explicit units, averaging period, method, time, and QA;
- `PUBLIC_AQI_REPORT` records that preserve the issuing source, index/report role, reporting time, category/breakpoint context where allowed, and explicit non-concentration semantics;
- `LOW_COST_SENSOR` records whose correction method, method version, caveats, confidence, limitations, collocation or comparison context where available, and policy/review state travel with the value;
- separately modeled regulatory/archive records whose issuing authority, source role, vintage, archive context, evidence, and limitations are explicit;
- status, correction, supersession, stale-state, duplicate-resolution, QA, uncertainty, and caveat sidecars that are not proofs, receipts, policy decisions, or releases;
- controlled references to contributing station, weather, smoke, AOD, forecast, modeled, or advisory context without relabeling those inputs as PM2.5 observations;
- public-candidate PM2.5 derivatives that remain upstream of catalog and release review;
- object-ready candidates prepared for future contract/schema validation, EvidenceBundle closure, catalog review, or release review;
- lane-local README or non-release manifest notes that explain artifact identity without becoming authority records.

## What does NOT belong here

Do not place these in `data/processed/atmosphere/pm25/`:

- RAW sensor feeds, source-native agency reports, station payloads, source downloads, QA payloads, logs, screenshots, or unprocessed records;
- WORK parsing, unit-conversion experiments, correction tuning, breakpoint calculations, temporary joins, notebooks, exploratory comparisons, or scratch outputs;
- QUARANTINE material with unresolved rights, source role, units, method, averaging period, time, freshness, low-cost caveats, QA, dispute, sensitivity, or safety state;
- generic `AirObservation` records when pollutant-specific PM2.5 semantics are absent;
- ozone observations, station/site metadata, AOD rasters, smoke masks, model fields, forecast context, climate context, or advisory/referral records except as controlled references;
- AQI or public report values silently relabeled as raw concentration;
- modeled PM2.5 silently relabeled as observed PM2.5;
- AOD, smoke, visibility, proxy, interpolation, or model output silently relabeled as PM2.5 measurement;
- reference-grade or regulatory claims for low-cost sensor data without source, correction, caveat, confidence, limitation, policy, and review support;
- calibration conclusions, regulatory exceedance determinations, exposure estimates, health conclusions, damage claims, warnings, emergency instructions, or life-safety guidance;
- semantic contracts, JSON Schemas, policy rules, validators, tests, fixtures, executable pipelines, source descriptors, catalogs, STAC/DCAT/PROV projections, triplets, proofs, receipts, releases, correction notices, rollback cards, or published artifacts;
- public map, tile, API, download, export, Focus Mode, Evidence Drawer, graph, search, notification, or AI-answer payloads;
- credentials, private station details, exact restricted siting, operator contact data, transform secrets, private thresholds, or parameters whose disclosure would weaken a sensitivity or access control.

## Inputs

Inputs may enter this lane only through governed lifecycle transitions from:

- `data/work/atmosphere/` after pollutant, source role, station context, method, units, averaging period, time, QA, freshness, rights, caveats, evidence, and correction posture are recorded;
- `data/quarantine/atmosphere/` after the hold condition is resolved and the remediation decision is auditable;
- accepted Atmosphere pipelines or tools that preserve source bytes by reference, source/station identifiers, method and correction versions, unit conversion lineage, input digests, QA, uncertainty, and correction state;
- approved observation/context relationships where PM2.5 value ownership remains in this lane and adjacent object ownership remains in its own lane.

A connector-to-PROCESSED, watcher-to-PROCESSED, public-upload-to-PROCESSED, model-to-observation, or renderer-to-PROCESSED shortcut is not an accepted normal path. Connectors, watchers, models, renderers, and AI systems do not silently promote or originate observed PM2.5 truth.

## Outputs

This lane may support downstream candidates for:

- `data/catalog/domain/atmosphere/` and accepted STAC/DCAT/PROV projections;
- `data/triplets/` or other relationship projections that preserve pollutant identity, source role, station context, time, method, units, QA, and evidence references;
- separate `data/proofs/` and `data/receipts/` objects;
- `release/candidates/atmosphere/` after source role, rights, units, method, QA, freshness, caveat, evidence, policy, review, correction, and rollback obligations are met;
- `data/published/` only through a governed release transition and separate released artifact path;
- governed API, MapLibre, Evidence Drawer, export, Focus Mode, or AI carriers only after public-safe release.

> [!CAUTION]
> Ordinary public clients must not read this directory directly. A valid-looking concentration, AQI report, or low-cost reading is not public truth merely because it is normalized, current-looking, or easy to map.

## Validation

No production PM2.5 validator suite was verified in this task. Until accepted contracts, schemas, fixtures, validators, policy checks, and CI evidence exist, field-level enforcement claims remain bounded.

A credible validation profile should check, at minimum:

1. pollutant identity is explicitly PM2.5 and cannot silently accept ozone or generic pollutant values;
2. source role is present and admitted for the record type;
3. concentration and AQI/report semantics cannot occupy the same field without an explicit typed representation;
4. units are declared, recognized, and compatible with the value semantics;
5. averaging period or reporting interval is explicit where required;
6. observed, source, retrieval, correction, release, and stale times are distinguishable where material;
7. station or network references resolve when the record claims station context;
8. low-cost records carry required caveat, correction, confidence, limitation, and review context;
9. regulatory/archive posture carries issuing authority, source role, vintage, and evidence support;
10. model, forecast, AOD, smoke, proxy, and interpolated products cannot masquerade as observed PM2.5;
11. QA flags, uncertainty, missingness, correction, supersession, and stale state are internally consistent;
12. required evidence references resolve to the appropriate EvidenceBundle before consequential use;
13. rights, sensitivity, release, correction, and rollback state are present before public-candidate promotion;
14. direct-public-path, health/advisory overclaim, and unsupported exceedance assertions fail closed.

Validation of shape is not proof of truth, calibration, representativeness, regulatory standing, exposure, health effect, or release readiness.

## Review burden

At least these reviews are appropriate before public or semi-public use:

| Review | Required focus |
|---|---|
| Atmosphere / PM2.5 domain | Pollutant semantics, method fitness, averaging period, units, station/network context, QA, caveats, and scientific claim scope. |
| Source-role / data-quality | Observed, report/index, low-cost, archive, model, proxy, and derived roles remain distinct. |
| Rights / sensitivity | Source terms, station siting, private details, operator information, and public-safe spatial precision. |
| Evidence / validation | EvidenceBundle closure, method lineage, uncertainty, contradictions, correction, and reproducibility. |
| Policy / release | Public scope, disclaimers, release obligations, stale handling, correction path, withdrawal path, and rollback target. |

Policy-significant release duties should remain separated when maturity justifies it. A source steward, validator, policy reviewer, and release steward must not be assumed to be the same actor.

## Related folders

| Responsibility | Repository home | Boundary |
|---|---|---|
| Raw Atmosphere captures | `data/raw/atmosphere/` | Immutable or source-preserved inputs; not public. |
| Transformation workspace | `data/work/atmosphere/` | Parsing, correction, unit conversion, QA, comparison, and candidate work. |
| Held material | `data/quarantine/atmosphere/` | Unresolved role, rights, units, method, QA, caveat, evidence, or safety issues. |
| Parent processed lane | `data/processed/atmosphere/` | Parent index; not public. |
| General air observation | `data/processed/atmosphere/air_observations/` | General family; does not erase PM2.5 specialization. |
| Observed parent | `data/processed/atmosphere/observed/` | Observed-context parent; not a duplicate truth store. |
| Air stations | `data/processed/atmosphere/air_stations/` | Network and siting context, not value-bearing PM2.5 records. |
| Ozone | `data/processed/atmosphere/ozone/` | Separate pollutant family. |
| AOD | `data/processed/atmosphere/aod/` | Remote-sensing proxy/mask; not PM2.5. |
| Modeled / forecast | `data/processed/atmosphere/modeled/`, `forecast_context/` | Model context; not observed PM2.5. |
| Advisory context | `data/processed/atmosphere/advisory_context/` | Official-source referral; not PM2.5 value or KFM guidance. |
| Contracts / schemas / policy | `contracts/domains/atmosphere/`, `schemas/contracts/v1/domains/atmosphere/`, `policy/domains/atmosphere/` | Meaning, shape, and admissibility remain separate. |
| Catalog / proof / receipt / release | `data/catalog/`, `data/proofs/`, `data/receipts/`, `release/` | Downstream authority and audit families. |

## ADRs

No ADR was created or accepted by this documentation-only change.

Potential ADR or drift topics remain:

- accepted PM2.5 source-role vocabulary and relationship to `AirObservation`;
- canonical representation of concentration versus AQI/report records;
- accepted units, precision, averaging-period, and time semantics;
- low-cost correction and caveat profile;
- regulatory/archive role and release posture;
- PM2.5 validator and fixture graduation criteria;
- stale-state, correction propagation, cache invalidation, and withdrawal behavior.

Until resolved, this README records constraints but does not invent canonical field names, thresholds, methods, owners, or enforcement maturity.

## Last reviewed

**Reviewed:** 2026-07-25  
**Evidence base:** repository `main@9f192b09fd64912919acfda69d638006a7817185`, prior target blob `dfd11264924f723065be6d6588a55057bdc3a1a5`, Directory Rules, current Atmosphere parent lane, `PM25Observation` semantic contract, paired scaffold schema posture, and adjacent processed-lane evidence.  
**Current maturity:** repository-grounded documentation; operational enforcement remains bounded.

---

## PM25Observation admission profile

The following packet is **PROPOSED** until accepted schemas, validators, fixtures, policies, and CI prove it:

| Concern | Minimum disclosure before promotion |
|---|---|
| Identity | Stable record ID, source ID, station/network reference where applicable, external record ID, and content/method digest where practical. |
| Pollutant | Explicit PM2.5 parameter identity; no implicit generic pollutant field. |
| Source role | Observed sensor, public AQI/report, low-cost sensor, regulatory/archive, modeled context, or other admitted role. |
| Value semantics | Concentration, AQI/report/index, category, corrected estimate, archive value, or other typed meaning. |
| Units | Declared units, conversion lineage, precision, rounding, and validity for the role. |
| Time | Observed, source, retrieval, averaging/reporting interval, correction, stale, release, and supersession time where material. |
| Method | Instrument, measurement method, archive method, correction method, method version, calibration or collocation context where supported. |
| QA and uncertainty | Flags, qualifiers, detection/measurement limits where relevant, uncertainty, confidence, completeness, missingness, and representativeness caveats. |
| Low-cost posture | Required caveats, correction/confidence/limitation fields, review status, and explicit non-reference-grade status unless separately supported. |
| Rights and sensitivity | Source terms, station-siting posture, operator/private detail restrictions, and public-safe spatial precision. |
| Evidence | EvidenceRefs for source, value semantics, method, QA, correction, caveat, and consequential claims. |
| Lifecycle | Validation state, policy decision, catalog readiness, release state, correction path, withdrawal path, rollback target. |

An object-ready candidate is not an enforced `PM25Observation` merely because its column names resemble this packet.

## Source role, units, and method

### Source-role discipline

| Role | What it may support | What it must not imply |
|---|---|---|
| `OBSERVED_SENSOR` | A measured PM2.5 concentration under the source's method and QA context. | AQI/report posture, regulatory exceedance, exposure, or health outcome by itself. |
| `PUBLIC_AQI_REPORT` | An agency/index/report value or category for public communication. | Raw concentration or direct sensor measurement unless separately supplied and typed. |
| `LOW_COST_SENSOR` | A caveated PM2.5 estimate under declared correction and limitations. | Reference-grade, regulatory, calibrated, or representative truth without separate support. |
| Regulatory/archive context | A historical or authority-issued record under a declared archive role and vintage. | Current operational state, observed truth outside its method, or legal exceedance conclusion by itself. |
| Modeled or forecast context | A model-derived PM2.5 field in its modeled lane. | Observed concentration. |
| Proxy or remote-sensing context | AOD, smoke, visibility, or related proxy context in its owning lane. | PM2.5 measurement. |

### Units and averaging

- Preserve source units and normalized units with explicit conversion method and version.
- Do not compare or merge values across incompatible averaging periods without a reviewed method.
- Keep instantaneous, hourly, rolling, daily, regulatory, public-report, and archive semantics distinct.
- Preserve precision and rounding rules; avoid false precision after conversion or correction.
- Record whether the value is final, preliminary, corrected, provisional, stale, superseded, or withdrawn.

### Method and QA

- A station identity does not prove instrument performance or representativeness.
- Calibration, correction, collocation, drift adjustment, humidity adjustment, or other methods require method identity and reviewable lineage.
- Missingness, invalidation, exceptional events, QA qualifiers, below-detection or out-of-range states, and source corrections must not be silently dropped.
- A low-cost correction model is a derived method and does not convert the source into reference-grade authority.
- Regulatory or health significance requires a separate, evidence-backed and policy-reviewed claim surface.

## PM2.5 guardrails

- AQI or public-report posture is not raw concentration.
- AOD, smoke masks, visibility, and satellite proxies are not PM2.5 measurements.
- Modeled and forecast PM2.5 are not observations.
- Low-cost PM2.5 requires caveats, correction/confidence/limitation context, and explicit role labeling.
- Station metadata is context, not the value itself.
- A normalized value does not prove calibration, representativeness, compliance, exceedance, exposure, health effect, damage, or action guidance.
- Public products must disclose source role, units, averaging/reporting period, time, QA/caveat posture, evidence, release state, correction path, and rollback target.
- KFM does not issue emergency, medical, occupational, or life-safety instructions from this lane.

## Lifecycle and promotion

```text
SOURCE / CONNECTOR
  -> RAW capture + SourceDescriptor
  -> WORK normalization / correction / role assignment
  -> QUARANTINE on unresolved role, rights, units, method, QA, caveat, evidence, or sensitivity
  -> PROCESSED PM2.5 candidate
  -> contract/schema/validator/policy/evidence review
  -> CATALOG / optional TRIPLET projection
  -> release candidate + proof + correction + rollback closure
  -> separate PUBLISHED artifact
  -> governed API / map / drawer / Focus carrier
```

Promotion is a governed state transition. It is not established by copying a file, linking a README, generating a chart, creating a tile, opening a pull request, merging code, or rendering a polished layer.

## Correction and rollback

PM2.5 correction is especially sensitive because revised source data, invalidation, unit errors, station changes, method changes, low-cost correction updates, and stale public reports can alter downstream interpretation.

A credible correction process should:

1. identify the affected source, station/network, record identity, source role, time window, units, averaging period, and method;
2. preserve prior values and evidence rather than silently overwriting them;
3. state whether the change is source-issued, unit-related, QA-related, correction-model-related, role-related, or editorial;
4. recompute affected aggregates, comparisons, AQI/report carriers, derived layers, catalogs, triplets, EvidenceBundles, and public artifacts where applicable;
5. invalidate or rebuild caches and indexes derived from affected values;
6. issue correction, supersession, withdrawal, or stale-state records appropriate to the impact;
7. preserve prior release IDs and a tested rollback target;
8. verify that public clients no longer expose invalid or superseded claims while retaining inspectable correction lineage.

Rollback must not restore a value known to be unsafe, role-collapsed, unsupported, or misleading. In that case, withdraw or hold the affected output and return `ABSTAIN`, `DENY`, or an explicit stale/error state.

<p align="right"><a href="#top">Back to top</a></p>

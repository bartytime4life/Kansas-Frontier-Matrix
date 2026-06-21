<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/weather-observation
title: contracts/domains/atmosphere/WeatherObservation.md — WeatherObservation Contract
type: contract
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Weather steward · Contract steward · Evidence steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; weather-observation; semantic-contract; observed-sensor; meteorological-context; weather
tags: [kfm, contracts, atmosphere, air, WeatherObservation, weather, observed-sensor, meteorological-context, source-role, evidence, policy, validation, release, lifecycle, governance]
related:
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../docs/domains/atmosphere/SOURCE_FAMILIES.md
  - ../../../docs/domains/atmosphere/SOURCES.md
  - ../../../docs/domains/atmosphere/PIPELINE.md
  - ../../../docs/domains/atmosphere/API_CONTRACTS.md
  - ./WeatherStation.md
  - ./TemperatureObservation.md
  - ./PrecipitationObservation.md
  - ./WindField.md
  - ./ForecastContext.md
  - ./ClimateNormal.md
  - ./ClimateAnomaly.md
  - ./AdvisoryContext.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json
  - ../../../policy/domains/atmosphere/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "Expanded from a planned-file scaffold into the object-level WeatherObservation semantic contract."
  - "The paired schema is currently a PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "docs/domains/atmosphere/OBJECT_FAMILY_MAP.md maps Weather Observation to OBSERVED_SENSOR / METEOROLOGICAL_CONTEXT."
  - "The object-family purpose row says Weather Observation is a general meteorological observation and that context vs primary-claim role must be tagged."
  - "Atmosphere policy doctrine requires source role, denies model-as-observation collapse, applies freshness gates, and holds/denies unresolved rights."
  - "This contract defines weather-observation meaning; it does not authorize temperature/precipitation/wind specialization collapse, climate baseline/anomaly claims, forecast/model-as-observation, hazard/impact claims, policy approval, evidence proof, public release, or life-safety guidance."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# WeatherObservation Contract

> Semantic contract for `WeatherObservation`, the Atmosphere/Air-domain object representing a governed general meteorological observation or weather-context record. It preserves the boundary between primary observed weather values, supporting meteorological context, specialized weather variables, model fields, climate context, hazards/impact claims, advisories, evidence proof, and release approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Family: weather" src="https://img.shields.io/badge/family-weather-blue">
  <img alt="Knowledge character: OBSERVED_SENSOR or METEOROLOGICAL_CONTEXT" src="https://img.shields.io/badge/character-OBSERVED__SENSOR%20%7C%20METEOROLOGICAL__CONTEXT-purple">
  <img alt="Role tagging: required" src="https://img.shields.io/badge/role__tagging-required-orange">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold-orange">
</p>

`contracts/domains/atmosphere/WeatherObservation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Weather boundary](#weather-boundary) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/atmosphere/WeatherObservation.md`  
> **Schema path:** `schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json`  
> **Truth posture:** `CONFIRMED` target path, current update, paired scaffold schema, canonical-path lane, object-family map entry, weather-observation purpose row, atmosphere policy anti-collapse/freshness/rights rows, adjacent expanded `TemperatureObservation` and `PrecipitationObservation` patterns, and uploaded authoring guidance. Validator behavior, fixtures, enforceable policy bundles, source registry behavior, EvidenceBundle implementation, release workflow, API behavior, UI behavior, weather pipeline behavior, and runtime behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> This contract defines object meaning only. It does **not** authorize publication, schema enforcement, specialized-variable flattening, forecast/model-as-observation collapse, climate normal/anomaly claims, hazard event or impact claims, health/safety guidance, advisory issuance, policy approval, proof closure, or release of controlled Atmosphere/Air weather products.

---

## Meaning

`WeatherObservation` is the Atmosphere/Air-domain object for a governed general meteorological observation or weather context record. Depending on source role, it may represent an `OBSERVED_SENSOR` weather reading or `METEOROLOGICAL_CONTEXT` supporting context.

A weather observation may support:

- general meteorological observation records tied to a `WeatherStation`, grid cell, source product, or station/network context;
- context-vs-primary-claim tagging where the same source value can either support another claim or stand as the claim being inspected;
- source-role-aware comparison with `TemperatureObservation`, `PrecipitationObservation`, `WindField`, `ForecastContext`, `ClimateNormal`, or `ClimateAnomaly` objects;
- evidence packaging for weather value, source, source role, observed time, retrieval time, valid time, unit, QA, freshness, correction, and release posture;
- public-safe display when source role, rights, units, QA, freshness, validation, policy, and release gates allow.

It is not:

- a substitute for `TemperatureObservation`, `PrecipitationObservation`, or `WindField` when variable-specific semantics are needed;
- a weather station/network metadata object;
- a forecast/model field;
- a climate normal or climate anomaly by itself;
- a hazards/event/impact claim by itself;
- an advisory or life-safety instruction;
- proof of exposure, hazard, damages, regulatory threshold, or event impact by itself;
- an EvidenceBundle;
- a PolicyDecision;
- a ReleaseManifest;
- permission to disclose stale, rights-unclear, source-role-unclear, unit-unclear, station-location-sensitive, or unsupported action/impact claims.

---

## Repo fit

```text
contracts/
└── domains/
    └── atmosphere/
        ├── WeatherObservation.md
        ├── TemperatureObservation.md
        ├── PrecipitationObservation.md
        └── WindField.md
```

Adjacent roots and object families:

| Root or object | Relationship |
|---|---|
| `../../../docs/domains/atmosphere/CANONICAL_PATHS.md` | Confirms the responsibility-root lane pattern for Atmosphere contracts and schemas. |
| `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | Lists `Weather Observation` as an owned weather object with `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT` character. |
| `../../../docs/domains/atmosphere/POLICY.md` | Defines source-role requirement, model-is-not-observation denial, freshness gates, unresolved-rights holds, and public tier transitions. |
| `./WeatherStation.md` | Weather station/network site context that weather observations may attach to. |
| `./TemperatureObservation.md` | Specialized temperature observation family that should be used for temperature-specific semantics. |
| `./PrecipitationObservation.md` | Specialized precipitation observation family that should be used for precipitation-specific semantics. |
| `./WindField.md` | Role-dependent observed/model weather family that may be compared but must preserve source role. |
| `./ForecastContext.md` | Model/context object; modeled weather context must not be presented as observation without explicit role and method support. |
| `./ClimateNormal.md`, `./ClimateAnomaly.md` | Climate baseline/anomaly objects that may aggregate/contextualize weather but must remain distinct. |
| `./AdvisoryContext.md` | Advisory/referral object; weather observations do not generate life-safety instructions. |
| `./AtmosphereAirDecisionEnvelope.md` | Governed response envelope that may explain answer/abstain/deny/error posture for weather questions. |
| `../../../schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json` | Current scaffold schema. |
| `../../../policy/domains/atmosphere/` | Proposed enforceable policy bundle home; behavior not verified here. |
| `../../../data/proofs/` | EvidenceBundle/proof support. |
| `../../../release/` | Release, correction, supersession, and rollback authority. |

---

## Weather boundary

`WeatherObservation` must preserve the difference between primary weather observation, supporting meteorological context, specialized variables, station metadata, model fields, climate context, hazards/impact claims, evidence proof, and release.

| Boundary | Rule |
|---|---|
| WeatherObservation vs. WeatherStation | WeatherObservation carries value/context; WeatherStation carries site/network context and siting sensitivity. |
| WeatherObservation vs. TemperatureObservation | Use TemperatureObservation when temperature-specific units, exposure, measurement height, heat/cold context, or climate aggregation matter. |
| WeatherObservation vs. PrecipitationObservation | Use PrecipitationObservation when amount, accumulation, trace state, precipitation type, gauge/radar method, or canonical-unit rules matter. |
| WeatherObservation vs. WindField | WindField carries wind-specific observed/model field semantics; model-role wind must not be treated as observation. |
| WeatherObservation vs. ForecastContext | Forecast/model weather context must remain labeled as model context and not as observed weather. |
| WeatherObservation vs. ClimateNormal/ClimateAnomaly | Climate baselines/anomalies may use aggregated weather values, but WeatherObservation is not the baseline or anomaly by itself. |
| WeatherObservation vs. hazards/event/impact claims | A weather observation may contextualize a hazard; it does not prove damage, exposure, event impact, crop loss, health effect, or infrastructure impact by itself. |
| WeatherObservation vs. advisory/health guidance | Weather values may support context; they do not create emergency, medical, or life-safety instructions. |
| WeatherObservation vs. public release | Public display requires source rights, source role, units, freshness, validation, policy, release record, correction path, and rollback target. |

---

## Schema posture

The paired schema found for this contract is:

```text
schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json
```

Current schema evidence:

| Schema fact | Status |
|---|---|
| Schema file exists | `CONFIRMED` |
| Schema title is `Weatherobservation` | `CONFIRMED` |
| Schema status is `PROPOSED` | `CONFIRMED` |
| Schema properties are empty | `CONFIRMED` |
| `additionalProperties` is `true` | `CONFIRMED` |
| Schema `source_doc` points to `docs/domains/atmosphere/CANONICAL_PATHS.md` | `CONFIRMED` |
| Schema `contract_doc` points to this contract | `CONFIRMED` |
| Title casing aligned with object name `WeatherObservation` | `NEEDS VERIFICATION` |
| Validator implementation | `UNKNOWN / NOT FOUND IN THIS TASK` |

This contract therefore defines semantic expectations for future schema, fixture, policy, and validator work. It does not claim that machine validation currently enforces those expectations.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Defining the meaning of a general weather-observation object | Yes | Must preserve source role, context-vs-primary-claim role, units, QA, evidence, policy, freshness, and release posture. |
| Linking WeatherObservation to WeatherStation | Conditional | Station siting remains governed by station/network policy and may require generalization before public release. |
| Using WeatherObservation as supporting meteorological context | Conditional | Must label `METEOROLOGICAL_CONTEXT` and not inflate context into the primary claim. |
| Using WeatherObservation as an observed sensor claim | Conditional | Must label `OBSERVED_SENSOR`, carry units/time/source/QA, and preserve evidence support. |
| Routing variable-specific values to specialized objects | Required when material | Use TemperatureObservation, PrecipitationObservation, or WindField when variable-specific semantics, units, or model role matter. |
| Comparing observed weather with forecast/model context | Conditional | Must preserve source role and avoid model-as-observation collapse. |
| Supporting evidence-packaged weather claims | Conditional | Requires EvidenceRef/EvidenceBundle support and clear claim scope. |
| Supporting public-safe display | Conditional | Requires source rights, freshness, validation, policy, release record, correction path, and rollback target. |
| Treating forecast weather as observed weather | No | Model/context families remain distinct. |
| Treating supporting weather context as primary proof | No | Context role must be tagged and bounded. |
| Treating WeatherObservation as hazards/impact proof | No | Hazards/event/impact claims require separate evidence and lane governance. |
| Treating WeatherObservation as health/safety instruction | No | Advisory and health/safety outputs require authoritative source referral and separate policy. |
| Using schema validity as proof of truth | No | Schema shape is not evidence proof. |
| Treating this contract as release approval | No | Release authority remains separate. |

---

## Exclusions

| Does not belong in this contract | Correct home |
|---|---|
| Machine field shape | `../../../schemas/contracts/v1/domains/atmosphere/WeatherObservation.schema.json`. |
| Validator implementation | `../../../tools/validators/...`. |
| Fixtures and tests | `../../../fixtures/domains/atmosphere/`, `../../../tests/domains/atmosphere/`, or policy test homes after verification. |
| Raw station feeds, gridded products, source downloads, QA payloads, logs, or processing workspaces | `../../../data/raw/atmosphere/`, `../../../data/work/atmosphere/`, or `../../../data/quarantine/atmosphere/`, subject to lifecycle, rights, freshness, and validation rules. |
| Weather station/network metadata | `./WeatherStation.md` and paired schema, with siting sensitivity controls. |
| Temperature specialization | `./TemperatureObservation.md` and paired schema. |
| Precipitation specialization | `./PrecipitationObservation.md` and paired schema. |
| Wind observed/model specialization | `./WindField.md` and paired schema. |
| Forecast/model fields | `./ForecastContext.md` and paired schemas where relevant. |
| Climate baseline/anomaly semantics | `./ClimateNormal.md`, `./ClimateAnomaly.md`, and paired schemas. |
| Heat/cold, precipitation, wind, storm, flood, drought, crop-loss, health exposure, infrastructure, or impact truth claims | Governed hazards/impact domain contracts and release controls after verification. |
| EvidenceBundle/proof content | `../../../data/proofs/`. |
| Source registry records | `../../../data/registry/sources/atmosphere/`. |
| Sensitivity, rights, admissibility, or release policy | `../../../policy/domains/atmosphere/` and `../../../policy/sensitivity/` after verification. |
| Release manifests, correction notices, rollback cards | `../../../release/`. |
| Public layer, UI, API, renderer, Focus Mode, notification, tile-service, or map implementation | Governed app/API/UI/layer roots. |

---

## Recommended fields

The current schema does not require these fields. They are `PROPOSED` semantic requirements for future schema/validator work:

| Field | Meaning |
|---|---|
| `weather_observation_id` | Stable deterministic or steward-assigned weather-observation identity. |
| `source_id` | Source descriptor or source family reference. |
| `source_role` | Required role/knowledge character: `OBSERVED_SENSOR`, `METEOROLOGICAL_CONTEXT`, or another reviewed role. |
| `weather_station_ref` | WeatherStation or station/network context reference where applicable. |
| `context_role` | Primary claim, supporting context, comparison context, QA context, or unknown. |
| `parameter_name` | Source weather parameter name when generalized, or route to specialized object when material. |
| `parameter_code` | Source or normalized weather parameter code. |
| `observed_value` | Numeric, categorical, or structured weather value, subject to source role and units. |
| `unit` | Canonical unit or source unit with normalization state. |
| `measurement_method` | Station sensor, manual report, gridded analysis, radar estimate, model-derived context, or other reviewed method. |
| `unit_normalization_state` | Native, normalized, converted, rejected, unknown, or needs verification. |
| `qa_state` | Source QA state, validation state, confidence, uncertainty, or limitation marker. |
| `temporal_scope` | Source, observed, valid, retrieval, release, and correction time fields where material. |
| `freshness_state` | Fresh, stale, historical, superseded, corrected, or unknown. |
| `spatial_context_ref` | Station/site, grid, county, region, or other governed spatial context; direct coordinates should remain governed by station policy. |
| `rights_refs` | Rights, license, terms, or use-permission references. |
| `source_refs` | SourceDescriptor/source record references. |
| `source_roles` | Source roles supporting, contextualizing, or contesting the observation/context. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references. |
| `related_temperature_refs` | TemperatureObservation references where specialization or comparison is governed. |
| `related_precipitation_refs` | PrecipitationObservation references where specialization or comparison is governed. |
| `related_wind_refs` | WindField references where specialization or comparison is governed. |
| `model_context_refs` | ForecastContext references where comparison is governed. |
| `climate_context_refs` | ClimateNormal or ClimateAnomaly references where aggregation/baseline context is governed. |
| `advisory_context_refs` | AdvisoryContext references where weather context is linked to official referral. |
| `confidence_statement` | Bounded confidence, uncertainty, quality, or limitation statement. |
| `contradiction_refs` | Observations, source products, QA runs, model fields, or claims that contest this weather record. |
| `policy_state` | Policy posture or policy-decision reference. |
| `sensitivity_class` | Sensitivity/public-safety classification. |
| `review_refs` | Steward, source, policy, scientific, or release review references. |
| `transform_refs` | SensitivityTransform or PublicationTransformReceipt references for public-safe derivatives. |
| `lineage_refs` | Prior, successor, supersession, correction, reprocessing, calibration, or rollback records. |
| `release_refs` | Release/candidate linkage where applicable. |
| `correction_refs` | Correction/supersession/rollback lineage. |
| `spec_hash` | Integrity pin for the representation. |

---

## Invariants

`WeatherObservation` must preserve these invariants:

- WeatherObservation records are general meteorological observation/context objects, not a shortcut around specialized temperature, precipitation, or wind contracts;
- source role / knowledge character must remain explicit;
- context-vs-primary-claim role must be tagged where material;
- observed weather values must use canonical units or carry a visible unit-normalization state;
- WeatherObservation records are not station metadata, forecast context, climate normals, climate anomalies, advisories, or hazards/impact claims by themselves;
- forecast/model weather must not be presented as observed weather;
- climate baseline/anomaly meaning requires separate ClimateNormal/ClimateAnomaly support;
- weather records are not evidence proof by themselves;
- raw source/station/gridded payloads and contract-level summaries must remain separated;
- rights, freshness, QA, source role, unit normalization, context role, time fields, uncertainty, sensitivity, review posture, and lifecycle state must remain inspectable;
- stale, rights-unclear, QA-failed, role-ambiguous, unit-unclear, context-role-unclear, or evidence-missing products fail closed or restrict public release;
- contradiction, rejection, supersession, calibration, reprocessing, and correction lineage must remain traceable;
- schema validity is not evidence proof;
- public-facing use must be downstream of governed release artifacts and public-safe transforms;
- publication is a governed state transition, not a file move.

---

## Lifecycle

```mermaid
flowchart LR
  SRC[Weather station / sensor / gridded source payload] --> RAW[RAW atmosphere source capture]
  RAW -->|rights + source role + checksum| WORK[WORK normalization]
  WORK -->|schema + QA + units + context role + policy gates| PROC[PROCESSED WeatherObservation]
  PROC --> EVID[EvidenceBundle / weather claim support]
  EVID --> REVIEW[Steward / scientific / policy review]
  REVIEW -->|stale / unclear rights / model collapse / context role unclear| HOLD[QUARANTINE / HOLD]
  REVIEW -->|accepted internal| INTERNAL[Internal WeatherObservation record]
  INTERNAL --> POLICY[Policy + sensitivity + freshness screen]
  POLICY -->|public-safe transform| RELEASE[Release / correction / rollback records]
```

The contract defines the meaning of a weather-observation object. It does not replace station governance, source intake, source-role assignment, rights review, unit normalization, QA, context-role review, EvidenceBundle resolution, schema validation, policy enforcement, transform receipts, release approval, correction, or rollback systems.

---

## Validation

Before relying on this contract, verify:

- schema fields beyond scaffold status;
- validator implementation and fixture coverage;
- canonical WeatherObservation ID and deterministic identity rules;
- title/case consistency between `WeatherObservation`, schema title `Weatherobservation`, and any API/object registry;
- source role / knowledge-character enforcement;
- context-vs-primary-claim tagging behavior;
- variable-specialization routing to TemperatureObservation, PrecipitationObservation, or WindField where material;
- model-as-observation negative tests where weather interacts with ForecastContext/WindField model families;
- climate-anomaly-as-observation negative tests;
- hazard-as-observation negative tests;
- station-reference and station-siting sensitivity handling;
- rights gate behavior for source products;
- freshness gate behavior for source products;
- QA, unit, context-role, measurement-method, missing-value, calibration, and correction handling;
- source, observed, valid, retrieval, release, and correction time separation;
- boundary between WeatherObservation, WeatherStation, TemperatureObservation, PrecipitationObservation, WindField, ForecastContext, ClimateNormal, ClimateAnomaly, and AdvisoryContext;
- transform, release, correction, supersession, withdrawal, and rollback linkage;
- no downstream surface treats this contract as specialized variable proof, forecast/model field, climate anomaly proof, hazard/impact proof, health/safety instruction, or release approval.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `WeatherObservation.md` scaffold | `CONFIRMED` | Target file existed as a planned-file scaffold and cited `docs/domains/atmosphere/CANONICAL_PATHS.md`. | Scaffold did not define authoritative semantics. |
| `WeatherObservation.schema.json` | `CONFIRMED scaffold` | Schema exists, is `PROPOSED`, has empty properties, allows additional properties, and points to this contract. | Does not enforce full WeatherObservation semantics. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED repo evidence` | Lists `Weather Observation` as owned by Atmosphere/Air with role-dependent `OBSERVED_SENSOR` / `METEOROLOGICAL_CONTEXT` character. | Per-object binding is noted as inferred pending ADR in the map itself. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` purpose row | `CONFIRMED repo evidence` | States Weather Observation is a general meteorological observation and context vs primary-claim role must be tagged. | Does not prove schema/validator enforcement. |
| `docs/domains/atmosphere/POLICY.md` | `CONFIRMED repo evidence` | States source role is required, model is not observation, freshness gates apply, unresolved rights hold/deny release, and public tier upgrades require transform receipt plus review record. | Enforceable bundle/test behavior remains unverified in this task. |
| `TemperatureObservation.md` and `PrecipitationObservation.md` | `CONFIRMED adjacent contracts` | Confirm adjacent variable-specific weather contract patterns preserving canonical units and model/climate/hazards boundaries. | Do not define or enforce the WeatherObservation schema. |
| Uploaded authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest Markdown with verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Rollback

Rollback is required if this contract is used to claim schema completeness, validator coverage, context-role enforcement, canonical-unit enforcement, source-rights clearance, source-role enforcement, policy enforcement, freshness enforcement, release execution, API/UI behavior, weather pipeline behavior, EvidenceBundle proof, climate anomaly proof, hazard/impact proof, public health guidance, public disclosure permission, or implementation maturity not verified in this task.

Rollback target: prior scaffold blob SHA `1ea58057a110db0a1ca7c6db41bc67988a104acd`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] WeatherObservation vocabulary is reviewed by the Atmosphere steward, weather steward, evidence steward, policy steward, and release steward.
- [ ] Boundary between `WeatherObservation`, `WeatherStation`, `TemperatureObservation`, `PrecipitationObservation`, `WindField`, `ForecastContext`, `ClimateNormal`, `ClimateAnomaly`, and `AdvisoryContext` is accepted.
- [ ] Paired JSON Schema is expanded from scaffold status.
- [ ] Schema title/casing is reconciled with `WeatherObservation` object-family name.
- [ ] Valid and invalid fixtures cover observed-sensor, meteorological-context, primary-claim, supporting-context, station, gridded, fresh, stale, rights-unclear, QA-failed, unit-invalid, context-role-missing, role-missing, corrected, superseded, quarantined, release-candidate, public-safe derivative, and rollback states.
- [ ] Validator enforces source role, knowledge character, context role, station/spatial refs, time fields, units, measurement method, QA flags, rights refs, evidence refs, policy state, release refs, correction refs, and rollback refs.
- [ ] Negative tests deny WeatherObservation as specialized variable collapse, forecast/model field, climate anomaly proof, hazard/impact proof, advisory instruction, or proof by itself.
- [ ] EvidenceBundle, PolicyDecision, ReviewRecord, PublicationTransformReceipt, ReleaseManifest, CorrectionNotice, and RollbackCard references are validated where required.
- [ ] API/UI surfaces prove they cannot treat WeatherObservation as forecast/model field, climate anomaly proof, hazard/impact proof, health guidance, unsupported event claim, or release approval.
- [ ] Release and rollback dry-runs prove this contract cannot bypass publication gates.

## Status summary

`WeatherObservation` is an Atmosphere/Air general weather observation/context object. It can support general meteorological observations, context-vs-primary-claim tagging, station/sensor/gridded lineage, QA-aware comparison, evidence packaging, correction, and public-safe display when rights, source role, units, evidence, validation, policy, transform, and release allow, but it is not a shortcut around TemperatureObservation, PrecipitationObservation, or WindField; not forecast/model output; not climate anomaly proof; not hazards/impact proof; not health/safety guidance; not evidence proof; and not release approval.

<p align="right"><a href="#top">Back to top</a></p>

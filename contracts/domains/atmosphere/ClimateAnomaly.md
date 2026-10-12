<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/climate-anomaly
title: contracts/domains/atmosphere/ClimateAnomaly.md — ClimateAnomaly Contract
type: contract
version: v0.2
status: draft
owners: OWNER_TBD — Atmosphere steward · Climate steward · Contract steward · Evidence steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; atmosphere; climate-anomaly; semantic-contract; climate-anomaly-context; baseline-relative
tags: [kfm, contracts, atmosphere, air, ClimateAnomaly, climate, anomaly, baseline, climate-normal, climate-anomaly-context, evidence, policy, validation, release, lifecycle, governance]
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
  - ./ClimateNormal.md
  - ./TemperatureObservation.md
  - ./PrecipitationObservation.md
  - ./WeatherObservation.md
  - ./ForecastContext.md
  - ./WindField.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json
  - ../../../policy/domains/atmosphere/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "Expanded from a planned-file scaffold into the object-level ClimateAnomaly semantic contract."
  - "The paired schema is currently a PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "docs/domains/atmosphere/OBJECT_FAMILY_MAP.md maps Climate Anomaly to CLIMATE_ANOMALY_CONTEXT."
  - "The object-family purpose row says Climate Anomaly is a deviation from a Climate Normal and MUST anchor to a Climate Normal."
  - "Publication posture requires climate/anomaly context to carry aggregation receipt and baseline period disclosure."
  - "This contract defines climate-anomaly meaning; it does not authorize observation claims, forecast claims, climate attribution, policy approval, evidence proof, public release, or health/safety guidance."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ClimateAnomaly Contract

> Semantic contract for `ClimateAnomaly`, the Atmosphere/Air-domain object representing a governed baseline-relative climate anomaly statement. It records deviation-from-baseline meaning and lineage without turning the anomaly into a raw observation, weather event, forecast, model field, attribution claim, evidence proof, public layer, or release approval by itself.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Family: climate" src="https://img.shields.io/badge/family-climate-blue">
  <img alt="Knowledge character: CLIMATE_ANOMALY_CONTEXT" src="https://img.shields.io/badge/character-CLIMATE__ANOMALY__CONTEXT-purple">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold-orange">
</p>

`contracts/domains/atmosphere/ClimateAnomaly.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Anomaly boundary](#anomaly-boundary) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/atmosphere/ClimateAnomaly.md`  
> **Schema path:** `schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json`  
> **Truth posture:** `CONFIRMED` target path, current update, paired scaffold schema, canonical-path lane, object-family map entry, climate purpose row, publication-posture climate/anomaly disclosure rule, adjacent `ClimateNormal` scaffold, and uploaded authoring guidance. Validator behavior, fixtures, enforceable policy bundles, source registry behavior, EvidenceBundle implementation, release workflow, API behavior, UI behavior, climate pipeline behavior, and runtime behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> This contract defines object meaning only. It does **not** authorize publication, climate attribution, trend proof, observation substitution, forecast substitution, source-rights clearance, policy approval, proof closure, public layer release, or health/safety guidance.

---

## Meaning

`ClimateAnomaly` is the Atmosphere/Air-domain object for a governed baseline-relative climate anomaly statement. Its knowledge character is `CLIMATE_ANOMALY_CONTEXT`: a comparison against a declared climate normal, reference baseline, aggregation window, or other governed baseline context.

A climate anomaly may support:

- baseline-relative climate context for public-safe maps, reports, or Focus Mode summaries;
- deviation statements tied to a `ClimateNormal` or equivalent reviewed baseline;
- aggregation-aware comparison of temperature, precipitation, drought/climate context, or other atmosphere/climate variables where the variable is supported by source and schema;
- evidence packaging for baseline period, aggregation method, source lineage, units, time span, uncertainty, correction, and release posture;
- public-safe climate/anomaly surfaces when rights, source role, baseline, aggregation receipt, policy, validation, and release gates allow.

It is not:

- a raw weather observation;
- a raw climate normal;
- a forecast or model field by default;
- a station record;
- a single event claim by itself;
- a climate attribution claim by itself;
- proof of cause, impact, hazard, damages, or trend significance by itself;
- an AQI report, AOD raster, smoke context, advisory, or air-quality measurement;
- an EvidenceBundle;
- a PolicyDecision;
- a ReleaseManifest;
- permission to publish baseline-unclear, source-role-unclear, rights-unclear, evidence-missing, stale, or release-missing anomaly claims.

---

## Repo fit

```text
contracts/
└── domains/
    └── atmosphere/
        ├── ClimateAnomaly.md
        ├── ClimateNormal.md
        ├── TemperatureObservation.md
        └── PrecipitationObservation.md
```

Adjacent roots and object families:

| Root or object | Relationship |
|---|---|
| `../../../docs/domains/atmosphere/CANONICAL_PATHS.md` | Confirms the responsibility-root lane pattern for Atmosphere contracts and schemas. |
| `../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | Lists `Climate Anomaly` as an owned Atmosphere object with `CLIMATE_ANOMALY_CONTEXT` character. |
| `../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md` | Requires climate/anomaly context to carry aggregation receipt and baseline-period disclosure. |
| `../../../docs/domains/atmosphere/POLICY.md` | Defines source-role, anti-collapse, rights, freshness, sensitivity, and finite decision posture. |
| `./ClimateNormal.md` | Baseline object that ClimateAnomaly must anchor to. Current file is still a scaffold in this task. |
| `./TemperatureObservation.md`, `./PrecipitationObservation.md`, `./WeatherObservation.md` | Observation/context families that may feed climate aggregation but must remain distinct from the anomaly. |
| `./ForecastContext.md`, `./WindField.md` | Model/context families that must not collapse into climate anomaly or observation semantics. |
| `./AtmosphereAirDecisionEnvelope.md` | Governed response envelope that may explain answer/abstain/deny/error posture for anomaly questions. |
| `../../../schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json` | Current scaffold schema. |
| `../../../policy/domains/atmosphere/` | Proposed enforceable policy bundle home; behavior not verified here. |
| `../../../data/proofs/` | EvidenceBundle/proof support. |
| `../../../release/` | Release, correction, supersession, and rollback authority. |

---

## Anomaly boundary

`ClimateAnomaly` must preserve the difference between baseline-relative climate context, climate normal, observation, model/forecast, event claim, attribution claim, evidence proof, and release.

| Boundary | Rule |
|---|---|
| ClimateAnomaly vs. ClimateNormal | A climate anomaly must anchor to a baseline; it does not define that baseline by itself. |
| ClimateAnomaly vs. observation | An anomaly is a baseline-relative derived/context statement, not a direct sensor reading. |
| ClimateAnomaly vs. weather event | A climate anomaly may contextualize conditions; it is not a discrete event/hazard truth claim by itself. |
| ClimateAnomaly vs. forecast/model field | Modeled or forecast context must remain labeled as model context and cannot be presented as observed anomaly without governed method support. |
| ClimateAnomaly vs. attribution | An anomaly does not prove cause, impact, damages, or trend significance without separate evidence and review. |
| ClimateAnomaly vs. public release | Public use requires rights, baseline, aggregation receipt, evidence, policy, disclosure, release, correction path, and rollback target. |

---

## Schema posture

The paired schema found for this contract is:

```text
schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json
```

Current schema evidence:

| Schema fact | Status |
|---|---|
| Schema file exists | `CONFIRMED` |
| Schema title is `Climateanomaly` | `CONFIRMED` |
| Schema status is `PROPOSED` | `CONFIRMED` |
| Schema properties are empty | `CONFIRMED` |
| `additionalProperties` is `true` | `CONFIRMED` |
| Schema `source_doc` points to `docs/domains/atmosphere/CANONICAL_PATHS.md` | `CONFIRMED` |
| Schema `contract_doc` points to this contract | `CONFIRMED` |
| Title casing aligned with object name `ClimateAnomaly` | `NEEDS VERIFICATION` |
| Validator implementation | `UNKNOWN / NOT FOUND IN THIS TASK` |

This contract therefore defines semantic expectations for future schema, fixture, policy, and validator work. It does not claim that machine validation currently enforces those expectations.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Defining the meaning of a climate-anomaly object | Yes | Must preserve baseline, aggregation, source role, time span, evidence, policy, disclosure, and release posture. |
| Linking ClimateAnomaly to ClimateNormal | Required | Climate anomaly must anchor to a baseline/normal before consequential use. |
| Supporting public-safe climate/anomaly visualization | Conditional | Requires rights, baseline period, aggregation receipt, validation, policy, release record, disclosures, and rollback target. |
| Supporting evidence-packaged anomaly claims | Conditional | Requires EvidenceRef/EvidenceBundle support and clear claim scope. |
| Comparing anomalies with observations or model context | Conditional | Must preserve knowledge character and avoid observation/model collapse. |
| Treating ClimateAnomaly as a raw observation | No | Climate anomaly is baseline-relative context, not an observed sensor value. |
| Treating ClimateAnomaly as climate attribution proof | No | Cause/impact/trend claims require separate evidence and review. |
| Publishing anomaly context without baseline disclosure | No | Baseline period and aggregation method must be visible before release. |
| Publishing rights-unclear anomaly products | No | Fail closed through rights and release gates. |
| Using schema validity as proof of truth | No | Schema shape is not evidence proof. |
| Treating this contract as release approval | No | Release authority remains separate. |

---

## Exclusions

| Does not belong in this contract | Correct home |
|---|---|
| Machine field shape | `../../../schemas/contracts/v1/domains/atmosphere/ClimateAnomaly.schema.json`. |
| Validator implementation | `../../../tools/validators/...`. |
| Fixtures and tests | `../../../fixtures/domains/atmosphere/`, `../../../tests/domains/atmosphere/`, or policy test homes after verification. |
| Raw observations, gridded source files, normals datasets, climate products, source downloads, QA payloads, or processing workspaces | `../../../data/raw/atmosphere/`, `../../../data/work/atmosphere/`, or `../../../data/quarantine/atmosphere/`, subject to lifecycle, rights, freshness, and validation rules. |
| Climate baseline/normal semantics | `./ClimateNormal.md` and paired schema. |
| Observation values | `./TemperatureObservation.md`, `./PrecipitationObservation.md`, `./WeatherObservation.md`, and paired schemas. |
| Model fields or forecast context | `./ForecastContext.md`, `./WindField.md`, and paired schemas. |
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
| `climate_anomaly_id` | Stable deterministic or steward-assigned climate-anomaly identity. |
| `source_id` | Source descriptor or source family reference. |
| `source_role` | Required role/knowledge character; expected default is `CLIMATE_ANOMALY_CONTEXT`. |
| `climate_normal_ref` | Required ClimateNormal or baseline reference. |
| `baseline_period` | Reference period used for the normal/baseline. |
| `anomaly_period` | Period being compared against the baseline. |
| `parameter_name` | Temperature, precipitation, or other supported climate variable. |
| `parameter_code` | Source or normalized parameter code. |
| `anomaly_value` | Numeric, categorical, or structured anomaly value. |
| `unit` | Canonical unit or source unit with normalization state. |
| `directionality` | Above baseline, below baseline, equal/no anomaly, mixed, unknown, or not applicable. |
| `aggregation_method` | Mean, sum, percentile, gridded aggregation, spatial aggregate, temporal aggregate, or other reviewed method. |
| `aggregation_receipt_refs` | Aggregation receipt or processing evidence references required before publication. |
| `spatial_scope_ref` | Region, grid, station aggregate, county, basin, or other governed spatial scope. |
| `temporal_scope` | Source, observed/period, valid, retrieval, release, correction, and supersession times where material. |
| `qa_state` | Source QA, baseline QA, aggregation QA, confidence, uncertainty, or limitation marker. |
| `uncertainty_statement` | Bounded uncertainty, confidence, or limitation statement. |
| `rights_refs` | Rights, license, terms, or use-permission references. |
| `source_refs` | SourceDescriptor/source record references. |
| `source_roles` | Source roles supporting, contextualizing, or contesting the anomaly. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references. |
| `related_observation_refs` | TemperatureObservation, PrecipitationObservation, WeatherObservation, or other references only as support/context. |
| `model_context_refs` | ForecastContext/WindField/climate-model context references where governed comparison is needed. |
| `confidence_statement` | Bounded confidence, uncertainty, quality, or limitation statement. |
| `contradiction_refs` | Source products, baselines, observations, methods, or claims that contest this anomaly. |
| `policy_state` | Policy posture or policy-decision reference. |
| `sensitivity_class` | Sensitivity/public-safety classification. |
| `review_refs` | Steward, source, policy, scientific, or release review references. |
| `transform_refs` | PublicationTransformReceipt or other transform receipt references for public-safe derivatives. |
| `lineage_refs` | Prior, successor, baseline update, reprocessing, correction, supersession, or rollback records. |
| `release_refs` | Release/candidate linkage where applicable. |
| `correction_refs` | Correction/supersession/rollback lineage. |
| `spec_hash` | Integrity pin for the representation. |

---

## Invariants

`ClimateAnomaly` must preserve these invariants:

- ClimateAnomaly records are baseline-relative context, not raw observations;
- ClimateAnomaly records must anchor to a ClimateNormal or reviewed baseline before consequential use;
- ClimateAnomaly records are not forecasts, model fields, AQI reports, AOD masks, advisories, or station records;
- ClimateAnomaly records are not climate attribution proof by themselves;
- ClimateAnomaly records are not evidence proof by themselves;
- source role / knowledge character must remain explicit;
- baseline period, anomaly period, aggregation method, units, uncertainty, rights, review posture, and lifecycle state must remain inspectable;
- public climate/anomaly context requires aggregation receipt and baseline-period disclosure;
- stale, rights-unclear, source-role-unclear, baseline-missing, evidence-missing, or release-missing anomaly products fail closed or restrict public release;
- contradiction, rejection, baseline revision, supersession, reprocessing, and correction lineage must remain traceable;
- schema validity is not evidence proof;
- public-facing use must be downstream of governed release artifacts and public-safe transforms;
- publication is a governed state transition, not a file move.

---

## Lifecycle

```mermaid
flowchart LR
  SRC[Climate / observation / gridded source products] --> RAW[RAW atmosphere source capture]
  RAW -->|rights + source role + checksum| WORK[WORK normalization]
  WORK --> BASE[ClimateNormal / baseline resolution]
  BASE -->|aggregation + anomaly method| PROC[PROCESSED ClimateAnomaly]
  PROC --> EVID[EvidenceBundle / anomaly claim support]
  EVID --> REVIEW[Steward / scientific / policy review]
  REVIEW -->|baseline missing / rights unclear| HOLD[QUARANTINE / HOLD]
  REVIEW -->|accepted internal anomaly| INTERNAL[Internal ClimateAnomaly record]
  INTERNAL --> POLICY[Policy + disclosure + release screen]
  POLICY -->|public-safe climate context| RELEASE[Release / correction / rollback records]
```

The contract defines the meaning of a climate-anomaly object. It does not replace source intake, source-role assignment, rights review, baseline creation, aggregation, evidence resolution, schema validation, policy enforcement, transform receipts, release approval, correction, or rollback systems.

---

## Validation

Before relying on this contract, verify:

- schema fields beyond scaffold status;
- validator implementation and fixture coverage;
- canonical ClimateAnomaly ID and deterministic identity rules;
- title/case consistency between `ClimateAnomaly`, schema title `Climateanomaly`, and any API/object registry;
- required ClimateNormal/baseline reference behavior;
- source role / knowledge-character enforcement;
- aggregation receipt requirements;
- baseline period and anomaly period disclosure rules;
- unit, parameter, QA, missing-value, and correction handling;
- rights gate behavior for source and derived products;
- source, period, valid, retrieval, release, correction, baseline revision, and supersession time separation;
- boundary between ClimateAnomaly, ClimateNormal, TemperatureObservation, PrecipitationObservation, WeatherObservation, ForecastContext, and WindField;
- transform, release, correction, supersession, withdrawal, and rollback linkage;
- no downstream surface treats this contract as raw observation, forecast, attribution proof, health/safety guidance, or release approval.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `ClimateAnomaly.md` scaffold | `CONFIRMED` | Target file existed as a planned-file scaffold and cited `docs/domains/atmosphere/CANONICAL_PATHS.md`. | Scaffold did not define authoritative semantics. |
| `ClimateAnomaly.schema.json` | `CONFIRMED scaffold` | Schema exists, is `PROPOSED`, has empty properties, allows additional properties, and points to this contract. | Does not enforce full ClimateAnomaly semantics. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` | `CONFIRMED repo evidence` | Lists `Climate Anomaly` as owned by Atmosphere/Air with `CLIMATE_ANOMALY_CONTEXT` character. | Per-object binding is noted as inferred pending ADR in the map itself. |
| `docs/domains/atmosphere/OBJECT_FAMILY_MAP.md` purpose row | `CONFIRMED repo evidence` | States Climate Anomaly is a deviation from a Climate Normal and must anchor to a Climate Normal. | Does not prove schema/validator enforcement. |
| `docs/domains/atmosphere/PUBLICATION_POSTURE.md` | `CONFIRMED repo evidence` | Requires climate/anomaly context to carry aggregation receipt and baseline-period disclosure, and blocks promotion when rights/source/evidence/sensitivity/release are unresolved. | Does not prove release implementation. |
| `ClimateNormal.md` scaffold | `CONFIRMED adjacent scaffold` | Confirms adjacent baseline contract path exists as scaffold. | Does not define or enforce the baseline schema. |
| Uploaded authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest Markdown with verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Rollback

Rollback is required if this contract is used to claim schema completeness, validator coverage, baseline existence, source-rights clearance, source-role enforcement, aggregation enforcement, policy enforcement, release execution, API/UI behavior, climate pipeline behavior, EvidenceBundle proof, attribution proof, public health guidance, public disclosure permission, or implementation maturity not verified in this task.

Rollback target: prior scaffold blob SHA `294e7af83e09a0e2349e5c711678c048239911d3`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] ClimateAnomaly vocabulary is reviewed by the Atmosphere steward, climate steward, evidence steward, policy steward, and release steward.
- [ ] Boundary between `ClimateAnomaly`, `ClimateNormal`, `TemperatureObservation`, `PrecipitationObservation`, `WeatherObservation`, `ForecastContext`, and `WindField` is accepted.
- [ ] Paired JSON Schema is expanded from scaffold status.
- [ ] Schema title/casing is reconciled with `ClimateAnomaly` object-family name.
- [ ] Valid and invalid fixtures cover baseline-present, baseline-missing, aggregation-receipt-present, aggregation-receipt-missing, rights-unclear, source-role-missing, evidence-missing, corrected, superseded, quarantined, release-candidate, public-safe derivative, and rollback states.
- [ ] Validator enforces source role, knowledge character, baseline refs, time fields, units, aggregation receipts, rights refs, evidence refs, policy state, release refs, correction refs, and rollback refs.
- [ ] Negative tests deny ClimateAnomaly as raw observation, forecast, model field, climate attribution proof, advisory instruction, or proof by itself.
- [ ] EvidenceBundle, PolicyDecision, ReviewRecord, PublicationTransformReceipt, ReleaseManifest, CorrectionNotice, and RollbackCard references are validated where required.
- [ ] API/UI surfaces prove they cannot treat ClimateAnomaly as observation, forecast, attribution proof, health guidance, unsupported trend claim, or release approval.
- [ ] Release and rollback dry-runs prove this contract cannot bypass publication gates.

## Status summary

`ClimateAnomaly` is an Atmosphere/Air baseline-relative climate-context object. It can support deviation-from-normal explanation, aggregation-aware visualization, evidence packaging, correction, and public-safe display when the baseline, source role, rights, evidence, validation, policy, transform, release, and disclosures are available, but it is not a raw observation, not a forecast, not climate attribution proof, not health/safety guidance, not evidence proof, and not release approval.

<p align="right"><a href="#top">Back to top</a></p>

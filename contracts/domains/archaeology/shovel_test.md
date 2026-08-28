<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/archaeology/shovel-test
title: contracts/domains/archaeology/shovel_test.md — ShovelTest Contract
type: contract
version: v0.2
status: draft
owners: OWNER_TBD — Archaeology steward · Fieldwork steward · Contract steward · Evidence steward · Schema steward · Policy steward · Review steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; contracts; domains; archaeology; shovel-test; semantic-contract; fieldwork; survey; sensitive-lane
tags: [kfm, contracts, archaeology, shovel-test, fieldwork, survey, provenience, sample, artifact, evidence, review, policy, sensitivity, lifecycle, governance]
related:
  - ./README.md
  - ./OBJECT_MAP.md
  - ./survey_project.md
  - ./survey_transect.md
  - ./test_unit.md
  - ./excavation_unit.md
  - ./provenience_context.md
  - ./stratigraphic_unit.md
  - ./artifact_record.md
  - ./sample.md
  - ./domain_observation.md
  - ./candidate_feature.md
  - ./archaeological_site.md
  - ./site_component.md
  - ./chronology_assertion.md
  - ./cultural_review.md
  - ./steward_review.md
  - ./sensitivity_transform.md
  - ./publication_transform_receipt.md
  - ../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
  - ../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../docs/domains/archaeology/ARCHITECTURE.md
  - ../../../docs/domains/archaeology/DATA_LIFECYCLE.md
  - ../../../schemas/contracts/v1/domains/archaeology/shovel_test.schema.json
  - ../../../policy/sensitivity/archaeology/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "Expanded from a planned-file scaffold into the object-level ShovelTest semantic contract."
  - "The paired schema is currently a PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "OBJECT_MAP.md maps ShovelTest to shovel_test.md and shovel_test.schema.json as NEEDS VERIFICATION."
  - "This contract defines shovel-test meaning; it does not authorize fieldwork, publication, recovery proof, site confirmation, policy approval, review approval, or release approval."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ShovelTest Contract

> Semantic contract for `ShovelTest`, the Archaeology-domain object representing a governed shovel-test record or shovel-test pit observation within survey or fieldwork workflows. It records a bounded fieldwork unit and its linked context without converting that record into proof, site confirmation, public geometry, or release approval by itself.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Family: fieldwork" src="https://img.shields.io/badge/family-fieldwork-blue">
  <img alt="Sensitivity: controlled" src="https://img.shields.io/badge/sensitivity-controlled-red">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold-orange">
</p>

`contracts/domains/archaeology/shovel_test.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Fieldwork boundary](#fieldwork-boundary) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/archaeology/shovel_test.md`  
> **Schema path:** `schemas/contracts/v1/domains/archaeology/shovel_test.schema.json`  
> **Truth posture:** `CONFIRMED` target path, current update, paired scaffold schema, object-map row, and uploaded authoring guidance. Validator behavior, fixtures, policy behavior, source registry behavior, evidence-bundle implementation, review workflow, release workflow, API behavior, UI behavior, and runtime behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> This contract defines object meaning only. It does **not** authorize fieldwork, publication, recovery proof, site confirmation, review approval, policy approval, proof closure, public geometry, or release of controlled archaeology field records.

---

## Meaning

`ShovelTest` is the Archaeology-domain object for recording a bounded shovel-test record, shovel-test pit, or shovel-test observation within a survey, transect, project, or fieldwork workflow.

A shovel test may support:

- survey coverage and sampling documentation;
- fieldwork-unit context;
- artifact or sample recovery lineage;
- stratigraphic or soil-profile observation;
- candidate-feature, site-component, or site review;
- evidence packaging, correction, supersession, and rollback workflows.

It is not:

- a raw field form;
- a full excavation unit;
- a test unit by default;
- a provenience context by itself;
- an artifact or sample record;
- a confirmed archaeological site;
- an EvidenceBundle;
- a PolicyDecision;
- a ReviewRecord;
- a ReleaseManifest;
- proof that a site, component, association, or interpretation is true without evidence and review support.

---

## Repo fit

```text
contracts/
└── domains/
    └── archaeology/
        ├── README.md
        ├── shovel_test.md
        ├── survey_transect.md
        ├── provenience_context.md
        └── artifact_record.md
```

Adjacent roots and object families:

| Root or object | Relationship |
|---|---|
| `./README.md` | Archaeology semantic-contract directory boundary. |
| `./OBJECT_MAP.md` | Maps `ShovelTest` to this contract and its expected schema. |
| `./survey_project.md`, `./survey_transect.md` | Survey context that may organize shovel-test records. |
| `./test_unit.md`, `./excavation_unit.md` | Adjacent fieldwork-unit families with different scope. |
| `./provenience_context.md` | Context object that may capture recovery, association, and context relationships. |
| `./stratigraphic_unit.md` | Stratigraphic object that may structure observed deposits or levels. |
| `./artifact_record.md`, `./sample.md` | Recovery objects that may cite the shovel test and context. |
| `./domain_observation.md` | Observation object that may cite or frame shovel-test observations. |
| `./candidate_feature.md`, `./site_component.md`, `./archaeological_site.md` | Higher-order entities that may cite reviewed shovel-test evidence. |
| `./cultural_review.md`, `./steward_review.md` | Review objects required before consequential interpretation or exposure. |
| `../../../schemas/contracts/v1/domains/archaeology/shovel_test.schema.json` | Current scaffold schema. |
| `../../../policy/sensitivity/archaeology/` | Policy gate home; behavior not verified here. |
| `../../../data/proofs/` | EvidenceBundle/proof support. |
| `../../../release/` | Release, correction, supersession, and rollback authority. |

---

## Fieldwork boundary

`ShovelTest` must preserve the difference between fieldwork record, context, recovery, interpretation, proof, and publication.

| Boundary | Rule |
|---|---|
| Shovel test vs. raw field record | This object can summarize or reference field observations; raw records remain in lifecycle data roots. |
| Shovel test vs. survey transect | Transects organize survey coverage; shovel tests are discrete fieldwork observations or units. |
| Shovel test vs. test unit/excavation unit | A shovel test is a smaller or distinct fieldwork object unless reviewed as another unit type. |
| Shovel test vs. provenience context | A shovel test may create context records; context identity remains separate. |
| Shovel test vs. artifact/sample | Recovery records remain separate object families with their own custody and evidence lineage. |
| Shovel test vs. public release | Public use requires review, policy, transform, release, and rollback support. |

---

## Schema posture

The paired schema found for this contract is:

```text
schemas/contracts/v1/domains/archaeology/shovel_test.schema.json
```

Current schema evidence:

| Schema fact | Status |
|---|---|
| Schema file exists | `CONFIRMED` |
| Schema title is `Shovel Test` | `CONFIRMED` |
| Schema status is `PROPOSED` | `CONFIRMED` |
| Schema properties are empty | `CONFIRMED` |
| `additionalProperties` is `true` | `CONFIRMED` |
| Schema `source_doc` points to the planned-files ledger | `CONFIRMED` |
| Schema `contract_doc` points to this contract | `CONFIRMED` |
| Validator implementation | `UNKNOWN / NOT FOUND IN THIS TASK` |

This contract therefore defines semantic expectations for future schema and validator work. It does not claim that machine validation currently enforces those expectations.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Defining the meaning of a shovel-test object | Yes | Must preserve project, survey, fieldwork, recovery, context, evidence, review, sensitivity, and lifecycle posture. |
| Linking shovel tests to artifacts, samples, observations, and stratigraphy | Conditional | Must preserve uncertainty, custody/recovery lineage, review state, and policy controls. |
| Supporting survey, fieldwork, and evidence review | Yes | Must not imply public release or final interpretation. |
| Supporting public-safe summaries | Conditional | Requires policy, review, transform receipt, release record, and safe precision. |
| Treating a shovel test as recovery proof by itself | No | Proof requires evidence resolution and review. |
| Treating a shovel test as site confirmation by itself | No | Site confirmation requires governed evidence and review. |
| Publishing controlled fieldwork detail by default | No | Controlled details fail closed unless approved through governed release. |
| Using schema validity as proof of truth | No | Schema shape is not evidence proof. |
| Treating this contract as release approval | No | Release authority remains separate. |

---

## Exclusions

| Does not belong in this contract | Correct home |
|---|---|
| Machine field shape | `../../../schemas/contracts/v1/domains/archaeology/shovel_test.schema.json`. |
| Validator implementation | `../../../tools/validators/...`. |
| Fixtures and tests | `../../../fixtures/...`, `../../../tests/...`. |
| Raw field forms, notebooks, photographs, instrument files, catalog exports, or bulk shovel-test records | `../../../data/raw/`, `../../../data/work/`, or `../../../data/quarantine/`, subject to lifecycle and sensitivity rules. |
| EvidenceBundle/proof content | `../../../data/proofs/`. |
| Sensitivity, access, admissibility, or release policy | `../../../policy/...`. |
| Steward/cultural review records | Governance/review contract and record homes. |
| Release manifests, correction notices, rollback cards | `../../../release/`. |
| Public layer, UI, API, renderer, or Focus Mode implementation | Governed app/API/UI/layer roots. |

---

## Recommended fields

The current schema does not require these fields. They are `PROPOSED` semantic requirements for future schema/validator work:

| Field | Meaning |
|---|---|
| `shovel_test_id` | Stable deterministic or steward-assigned shovel-test identity. |
| `project_ref` | SurveyProject, fieldwork project, permit, source, or project-scope reference where modeled. |
| `transect_ref` | SurveyTransect reference when the test belongs to transect sampling. |
| `test_label` | Field label, station label, shovel-test number, or repository label. |
| `fieldwork_method` | Method statement or controlled vocabulary for how the shovel test was recorded. |
| `test_geometry_ref` | Internal geometry/support-scope reference; public-safe generalization required before exposure. |
| `spatial_precision_class` | Exact, generalized, suppressed, centroided, binned, county/region, or denied precision posture. |
| `depth_or_level_summary` | Bounded summary of depth, level, or interval information when allowed. |
| `stratigraphic_refs` | StratigraphicUnit references structuring the observation. |
| `provenience_context_refs` | ProvenienceContext references created or used by the shovel test. |
| `artifact_refs` | ArtifactRecord references associated with the shovel test. |
| `sample_refs` | Sample references associated with the shovel test. |
| `observation_refs` | DomainObservation or specialized observation references. |
| `candidate_feature_refs` | CandidateFeature references supported, contested, or created from the test. |
| `site_component_refs` | SiteComponent references only after review and evidence correlation. |
| `source_refs` | SourceDescriptor/source record references. |
| `source_roles` | Source roles supporting, contextualizing, or contesting the record. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references. |
| `confidence_statement` | Bounded confidence, uncertainty, or limitation statement. |
| `contradiction_refs` | Observations, contexts, or claims that contest this record. |
| `review_state` | Intake, needs review, under review, accepted internal record, rejected, superseded, quarantined, release-candidate, or withdrawn. |
| `review_refs` | StewardReview, CulturalReview, project review, or other review record references. |
| `policy_state` | Policy posture or policy-decision reference. |
| `sensitivity_class` | Sensitivity/public-safety classification. |
| `lineage_refs` | Prior, successor, supersession, split, merge, or rollback records. |
| `release_refs` | Release/candidate linkage where applicable. |
| `correction_refs` | Correction/supersession/rollback lineage. |
| `spec_hash` | Integrity pin for the representation. |

---

## Invariants

`ShovelTest` must preserve these invariants:

- shovel-test records are not proof by themselves;
- shovel-test records are not site confirmation by themselves;
- fieldwork identity must remain distinct from survey, context, stratigraphy, artifact, sample, evidence, review, policy, release, correction, and rollback objects;
- raw field/collection records and contract-level summaries must remain separated;
- source, method, recovery, context, uncertainty, sensitivity, review posture, and lifecycle state must remain inspectable;
- controlled fieldwork detail fails closed unless policy, review, and release authorize a public-safe transform;
- contradiction, rejection, supersession, and correction lineage must remain traceable;
- schema validity is not evidence proof;
- public-facing use must be downstream of governed release artifacts and public-safe transforms;
- publication is a governed state transition, not a file move.

---

## Lifecycle

```mermaid
flowchart LR
  SRC[Field / survey source record] --> ST[ShovelTest]
  ST --> LINKS[Survey + context + recovery links]
  LINKS --> EVID[Evidence packaging + review]
  EVID --> REVIEW[Steward / cultural review]
  REVIEW -->|restrict or reject| CONTROL[Restricted / rejected / superseded lineage]
  REVIEW -->|accepted internal record| INTERNAL[Reviewed internal shovel-test record]
  INTERNAL --> POLICY[Policy + sensitivity screen]
  POLICY -->|public-safe transform| RELEASE[Release / correction / rollback records]
```

The contract defines the meaning of a shovel-test object. It does not replace source intake, fieldwork authorization, evidence resolution, schema validation, policy enforcement, review, transform receipts, release approval, correction, or rollback systems.

---

## Validation

Before relying on this contract, verify:

- schema fields beyond scaffold status;
- validator implementation and fixture coverage;
- canonical shovel-test ID and deterministic identity rules;
- boundary between ShovelTest, SurveyProject, SurveyTransect, TestUnit, ExcavationUnit, ProvenienceContext, StratigraphicUnit, ArtifactRecord, and Sample;
- fieldwork, sampling, recovery, collection, and custody linkage requirements;
- EvidenceRef/EvidenceBundle requirements;
- source-role, time-kind, geometry, context, recovery, and association requirements;
- sensitivity handling for controlled fieldwork, context, and collection detail;
- steward/cultural review requirements;
- policy-gate requirements;
- release, correction, supersession, withdrawal, and rollback linkage;
- no downstream surface treats this contract as public disclosure permission, final proof, recovery proof, or site confirmation.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `shovel_test.md` scaffold | `CONFIRMED` | Target file existed as a planned-file scaffold. | Scaffold did not define authoritative semantics. |
| `shovel_test.schema.json` | `CONFIRMED scaffold` | Schema exists, is `PROPOSED`, has empty properties, allows additional properties, and points to this contract. | Does not enforce full shovel-test semantics. |
| `OBJECT_MAP.md` | `CONFIRMED current map` | Maps `ShovelTest` to `shovel_test.md` and `shovel_test.schema.json` with status `NEEDS VERIFICATION`. | Does not prove validator, fixture, policy, or release behavior. |
| Uploaded authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest Markdown with verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Rollback

Rollback is required if this contract is used to claim schema completeness, validator coverage, policy enforcement, review completion, release execution, API/UI behavior, fieldwork authorization, custody proof, evidence proof, recovery proof, site confirmation, public disclosure permission, or implementation maturity not verified in this task.

Rollback target: prior scaffold blob SHA `c3659b166ac4ecd62c38d96964dfebc832312189`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Shovel-test vocabulary is reviewed by the Archaeology steward and fieldwork steward.
- [ ] Boundary between `ShovelTest`, `SurveyProject`, `SurveyTransect`, `TestUnit`, `ExcavationUnit`, `ProvenienceContext`, `StratigraphicUnit`, `ArtifactRecord`, and `Sample` is accepted.
- [ ] Paired JSON Schema is expanded from scaffold status.
- [ ] Valid and invalid fixtures cover internal, restricted, rejected, superseded, corrected, release-candidate, and rollback states.
- [ ] Validator enforces required project, survey, fieldwork, context, source, evidence, stratigraphy, recovery, custody, review, sensitivity, policy, lineage, and visibility fields.
- [ ] Fixtures avoid unsafe fieldwork, context, or collection detail where references or redacted summaries are safer.
- [ ] EvidenceBundle, PolicyDecision, ReviewRecord, SensitivityTransform, PublicationTransformReceipt, ReleaseManifest, CorrectionNotice, and RollbackCard references are validated where required.
- [ ] API/UI surfaces prove they cannot treat a shovel test as proof, recovery proof, site confirmation, or public disclosure permission.
- [ ] Release and rollback dry-runs prove this contract cannot bypass publication gates.

## Status summary

`ShovelTest` is a sensitive Archaeology fieldwork object. It can support survey coverage, recovery lineage, context review, evidence packaging, correction, and public-safe explanation when evidence, review, policy, transform, and release allow, but it is not proof, not recovery proof, not site confirmation, not policy approval, and not release approval.

<p align="right"><a href="#top">Back to top</a></p>

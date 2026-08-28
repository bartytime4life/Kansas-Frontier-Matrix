<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/archaeology/excavation-unit
title: contracts/domains/archaeology/excavation_unit.md — ExcavationUnit Contract
type: contract
version: v0.2
status: draft
owners: OWNER_TBD — Archaeology steward · Fieldwork steward · Contract steward · Evidence steward · Schema steward · Policy steward · Review steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; contracts; domains; archaeology; excavation-unit; semantic-contract; fieldwork; sensitive-lane
tags: [kfm, contracts, archaeology, excavation, fieldwork, provenience, stratigraphy, evidence, review, policy, sensitivity, lifecycle, governance]
related:
  - ./README.md
  - ./OBJECT_MAP.md
  - ./archaeological_site.md
  - ./site_component.md
  - ./survey_project.md
  - ./test_unit.md
  - ./shovel_test.md
  - ./provenience_context.md
  - ./stratigraphic_unit.md
  - ./artifact_record.md
  - ./sample.md
  - ./chronology_assertion.md
  - ./cultural_review.md
  - ./steward_review.md
  - ./sensitivity_transform.md
  - ./publication_transform_receipt.md
  - ../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
  - ../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../docs/domains/archaeology/ARCHITECTURE.md
  - ../../../docs/domains/archaeology/DATA_LIFECYCLE.md
  - ../../../schemas/contracts/v1/domains/archaeology/excavation_unit.schema.json
  - ../../../policy/sensitivity/archaeology/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "Expanded from a planned-file scaffold into the object-level ExcavationUnit semantic contract."
  - "The paired schema is currently a PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "OBJECT_MAP.md maps ExcavationUnit to excavation_unit.md and excavation_unit.schema.json as NEEDS VERIFICATION."
  - "This contract defines excavation-unit meaning; it does not authorize publication, site confirmation, public geometry, policy approval, review approval, or release approval."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ExcavationUnit Contract

> Semantic contract for `ExcavationUnit`, the Archaeology-domain object representing a governed excavation unit, trench, block, square, or comparable controlled fieldwork unit used to organize provenience, stratigraphy, observations, artifacts, samples, reviews, and evidence lineage.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Family: fieldwork" src="https://img.shields.io/badge/family-fieldwork-blue">
  <img alt="Sensitivity: controlled" src="https://img.shields.io/badge/sensitivity-controlled-red">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold-orange">
</p>

`contracts/domains/archaeology/excavation_unit.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Fieldwork boundary](#fieldwork-boundary) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/archaeology/excavation_unit.md`  
> **Schema path:** `schemas/contracts/v1/domains/archaeology/excavation_unit.schema.json`  
> **Truth posture:** `CONFIRMED` target path, current update, paired scaffold schema, object-map row, and uploaded authoring guidance. Validator behavior, fixtures, policy behavior, source registry behavior, evidence-bundle implementation, review workflow, release workflow, API behavior, UI behavior, and runtime behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> This contract defines object meaning only. It does **not** authorize publication, fieldwork approval, site confirmation, review approval, policy approval, proof closure, public geometry, or release of sensitive archaeology records.

---

## Meaning

`ExcavationUnit` is the Archaeology-domain object for a controlled excavation area or comparable fieldwork unit. It records the semantic boundary of a place where archaeological excavation, sampling, stratigraphic recording, artifact recovery, or field documentation is organized.

An excavation unit may support:

- provenience and stratigraphic context linkage;
- field observations and documentation;
- artifact and sample recovery lineage;
- chronology or interpretation review;
- steward or cultural review workflows;
- internal validation, correction, supersession, and rollback checks.

It is not:

- a raw field notebook;
- a full excavation project by itself;
- a confirmed archaeological site;
- an EvidenceBundle;
- a PolicyDecision;
- a ReviewRecord;
- a ReleaseManifest;
- permission to expose precise fieldwork locations, sensitive provenience, or restricted context details;
- proof that recovered materials or interpretations are valid without evidence and review support.

---

## Repo fit

```text
contracts/
└── domains/
    └── archaeology/
        ├── README.md
        ├── excavation_unit.md
        ├── test_unit.md
        ├── provenience_context.md
        └── stratigraphic_unit.md
```

Adjacent roots and object families:

| Root or object | Relationship |
|---|---|
| `./README.md` | Archaeology semantic-contract directory boundary. |
| `./OBJECT_MAP.md` | Maps `ExcavationUnit` to this contract and its expected schema. |
| `./survey_project.md` | Survey/project context that may authorize or contextualize fieldwork. |
| `./test_unit.md`, `./shovel_test.md` | Related controlled fieldwork unit families; boundary requires steward review. |
| `./provenience_context.md` | Context object that may reference excavation-unit provenience. |
| `./stratigraphic_unit.md` | Stratigraphic object that may be recorded within an excavation unit. |
| `./artifact_record.md`, `./sample.md` | Recovery objects that may cite excavation-unit lineage. |
| `./chronology_assertion.md` | Temporal interpretation object that may depend on samples or contexts from an excavation unit. |
| `./cultural_review.md`, `./steward_review.md` | Review objects required before consequential interpretation or exposure. |
| `../../../schemas/contracts/v1/domains/archaeology/excavation_unit.schema.json` | Current scaffold schema. |
| `../../../policy/sensitivity/archaeology/` | Policy gate home; behavior not verified here. |
| `../../../data/proofs/` | EvidenceBundle/proof support. |
| `../../../release/` | Release, correction, supersession, and rollback authority. |

---

## Fieldwork boundary

`ExcavationUnit` must preserve the difference between fieldwork organization, evidence support, interpretation, and publication.

| Boundary | Rule |
|---|---|
| Excavation unit vs. project | The unit is a controlled fieldwork area; project-level authorization and scope live elsewhere. |
| Excavation unit vs. provenience | A unit can organize provenience; `ProvenienceContext` carries context meaning. |
| Excavation unit vs. stratigraphy | A unit may contain or reference stratigraphy; `StratigraphicUnit` carries stratigraphic-unit meaning. |
| Excavation unit vs. recovered objects | Artifacts and samples remain separate object families with their own evidence lineage. |
| Excavation unit vs. interpretation | Fieldwork organization can support interpretation; it is not interpretation proof by itself. |
| Excavation unit vs. release | Public use requires review, policy, transform, release, and rollback support. |

---

## Schema posture

The paired schema found for this contract is:

```text
schemas/contracts/v1/domains/archaeology/excavation_unit.schema.json
```

Current schema evidence:

| Schema fact | Status |
|---|---|
| Schema file exists | `CONFIRMED` |
| Schema title is `Excavation Unit` | `CONFIRMED` |
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
| Defining the meaning of an excavation unit object | Yes | Must preserve project, provenience, stratigraphy, source, evidence, review, sensitivity, and lifecycle posture. |
| Linking excavation units to contexts, artifacts, samples, or observations | Conditional | Must preserve uncertainty, recovery lineage, review state, and sensitivity controls. |
| Supporting internal fieldwork, cataloging, or evidence review | Yes | Must not imply public release or final interpretation. |
| Supporting public-safe summaries | Conditional | Requires policy, review, transform receipt, release record, and safe precision. |
| Treating an excavation unit as site confirmation | No | Site confirmation requires separate governed evidence and review. |
| Treating excavation-unit membership as proof of interpretation | No | EvidenceBundle and review remain separate. |
| Publishing sensitive fieldwork or provenience detail by default | No | Sensitive details fail closed unless approved through governed release. |
| Using schema validity as proof of truth | No | Schema shape is not evidence proof. |
| Treating this contract as release approval | No | Release authority remains separate. |

---

## Exclusions

| Does not belong in this contract | Correct home |
|---|---|
| Machine field shape | `../../../schemas/contracts/v1/domains/archaeology/excavation_unit.schema.json`. |
| Validator implementation | `../../../tools/validators/...`. |
| Fixtures and tests | `../../../fixtures/...`, `../../../tests/...`. |
| Raw field forms, notebooks, photographs, instrument files, or bulk excavation records | `../../../data/raw/`, `../../../data/work/`, or `../../../data/quarantine/`, subject to lifecycle and sensitivity rules. |
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
| `excavation_unit_id` | Stable deterministic or steward-assigned excavation-unit identity. |
| `project_ref` | SurveyProject, excavation project, permit, source, or project-scope reference where modeled. |
| `site_ref` | ArchaeologicalSite or CandidateFeature reference, when allowed and reviewed. |
| `unit_label` | Internal unit label, trench label, grid square, block, or field identifier. |
| `unit_type` | Excavation unit, trench, block, square, profile, section, or other reviewed unit type. |
| `unit_geometry_ref` | Internal geometry/support-scope reference; public-safe generalization required before exposure. |
| `spatial_precision_class` | Exact, generalized, suppressed, centroided, binned, county/region, or denied precision posture. |
| `provenience_refs` | ProvenienceContext references associated with the unit. |
| `stratigraphic_refs` | StratigraphicUnit references recorded within or across the unit. |
| `artifact_refs` | ArtifactRecord references recovered from the unit. |
| `sample_refs` | Sample references recovered from the unit. |
| `observation_refs` | DomainObservation or specialized observation references. |
| `chronology_refs` | ChronologyAssertion or dating/sample references, where applicable. |
| `source_refs` | SourceDescriptor/source record references. |
| `source_roles` | Source roles supporting, contextualizing, or contesting the unit record. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references. |
| `review_state` | Intake, needs review, under review, accepted internal record, rejected, superseded, quarantined, release-candidate, or withdrawn. |
| `review_refs` | StewardReview, CulturalReview, or other review record references. |
| `policy_state` | Policy posture or policy-decision reference. |
| `sensitivity_class` | Sensitivity/public-safety classification. |
| `lineage_refs` | Prior, successor, supersession, split, merge, or rollback unit records. |
| `release_refs` | Release/candidate linkage where applicable. |
| `correction_refs` | Correction/supersession/rollback lineage. |
| `spec_hash` | Integrity pin for the representation. |

---

## Invariants

`ExcavationUnit` must preserve these invariants:

- excavation-unit records are not proof by themselves;
- excavation-unit records are not site confirmation by themselves;
- fieldwork-unit identity must remain distinct from project, provenience, stratigraphic, artifact, sample, evidence, review, policy, release, correction, and rollback objects;
- raw field records and contract-level summaries must remain separated;
- method, source, unit identity, uncertainty, sensitivity, review posture, and lifecycle state must remain inspectable;
- sensitive fieldwork detail fails closed unless policy, review, and release authorize a public-safe transform;
- contradiction, rejection, supersession, and correction lineage must remain traceable;
- schema validity is not evidence proof;
- public-facing use must be downstream of governed release artifacts and public-safe transforms;
- publication is a governed state transition, not a file move.

---

## Lifecycle

```mermaid
flowchart LR
  FIELD[Fieldwork source / project record] --> UNIT[ExcavationUnit]
  UNIT --> CTX[Provenience + stratigraphy + recovery links]
  CTX --> REVIEW[Evidence + steward / cultural review]
  REVIEW -->|restrict or reject| CONTROL[Restricted / rejected / superseded lineage]
  REVIEW -->|accepted internal record| INTERNAL[Reviewed internal excavation-unit record]
  INTERNAL --> POLICY[Policy + sensitivity screen]
  POLICY -->|public-safe transform| RELEASE[Release / correction / rollback records]
```

The contract defines the meaning of an excavation-unit object. It does not replace source intake, fieldwork authorization, evidence resolution, schema validation, policy enforcement, review, transform receipts, release approval, correction, or rollback systems.

---

## Validation

Before relying on this contract, verify:

- schema fields beyond scaffold status;
- validator implementation and fixture coverage;
- canonical excavation-unit ID and deterministic identity rules;
- boundary between ExcavationUnit, TestUnit, ShovelTest, ProvenienceContext, and StratigraphicUnit;
- fieldwork project/permit/source linkage requirements;
- EvidenceRef/EvidenceBundle requirements;
- source-role, time-kind, geometry, and recovery-lineage requirements;
- sensitivity handling for restricted fieldwork and provenience detail;
- steward/cultural review requirements;
- policy-gate requirements;
- release, correction, supersession, withdrawal, and rollback linkage;
- no downstream surface treats this contract as public disclosure permission, final proof, or site confirmation.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `excavation_unit.md` scaffold | `CONFIRMED` | Target file existed as a planned-file scaffold. | Scaffold did not define authoritative semantics. |
| `excavation_unit.schema.json` | `CONFIRMED scaffold` | Schema exists, is `PROPOSED`, has empty properties, allows additional properties, and points to this contract. | Does not enforce full excavation-unit semantics. |
| `OBJECT_MAP.md` | `CONFIRMED current map` | Maps `ExcavationUnit` to `excavation_unit.md` and `excavation_unit.schema.json` with status `NEEDS VERIFICATION`. | Does not prove validator, fixture, policy, or release behavior. |
| Uploaded authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest Markdown with verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Rollback

Rollback is required if this contract is used to claim schema completeness, validator coverage, policy enforcement, review completion, release execution, API/UI behavior, fieldwork authorization, evidence proof, site confirmation, public disclosure permission, or implementation maturity not verified in this task.

Rollback target: prior scaffold blob SHA `0ded14e093836e17af6ea27740dafbc92d209a63`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Excavation-unit vocabulary is reviewed by the Archaeology steward and fieldwork steward.
- [ ] Boundary between `ExcavationUnit`, `TestUnit`, `ShovelTest`, `ProvenienceContext`, `StratigraphicUnit`, `ArtifactRecord`, and `Sample` is accepted.
- [ ] Paired JSON Schema is expanded from scaffold status.
- [ ] Valid and invalid fixtures cover internal, restricted, rejected, superseded, corrected, release-candidate, and rollback states.
- [ ] Validator enforces required project, unit, source, evidence, context, stratigraphy, recovery, review, sensitivity, policy, lineage, and visibility fields.
- [ ] Fixtures avoid unsafe fieldwork or provenience detail where references or redacted summaries are safer.
- [ ] EvidenceBundle, PolicyDecision, ReviewRecord, SensitivityTransform, PublicationTransformReceipt, ReleaseManifest, CorrectionNotice, and RollbackCard references are validated where required.
- [ ] API/UI surfaces prove they cannot treat an excavation unit as proof, site confirmation, or public disclosure permission.
- [ ] Release and rollback dry-runs prove this contract cannot bypass publication gates.

## Status summary

`ExcavationUnit` is a sensitive Archaeology fieldwork-unit object. It can support provenience, stratigraphy, recovery, evidence packaging, review, correction, and public-safe explanation when evidence, review, policy, transform, and release allow, but it is not proof, not site confirmation, not policy approval, and not release approval.

<p align="right"><a href="#top">Back to top</a></p>

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/archaeology/remote-sensing-anomaly
title: contracts/domains/archaeology/remote_sensing_anomaly.md — RemoteSensingAnomaly Contract
type: contract
version: v0.2
status: draft
owners: OWNER_TBD — Archaeology steward · Remote sensing steward · Contract steward · Evidence steward · Schema steward · Policy steward · Review steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; contracts; domains; archaeology; remote-sensing-anomaly; semantic-contract; observation; sensitive-lane
tags: [kfm, contracts, archaeology, remote-sensing, anomaly, observation, candidate-feature, evidence, review, policy, sensitivity, lifecycle, governance]
related:
  - ./README.md
  - ./OBJECT_MAP.md
  - ./domain_observation.md
  - ./lidar_candidate.md
  - ./geophysics_observation.md
  - ./candidate_feature.md
  - ./site_component.md
  - ./archaeological_site.md
  - ./survey_project.md
  - ./survey_transect.md
  - ./domain_feature_identity.md
  - ./cultural_review.md
  - ./steward_review.md
  - ./sensitivity_transform.md
  - ./publication_transform_receipt.md
  - ../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
  - ../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../docs/domains/archaeology/ARCHITECTURE.md
  - ../../../docs/domains/archaeology/DATA_LIFECYCLE.md
  - ../../../schemas/contracts/v1/domains/archaeology/remote_sensing_anomaly.schema.json
  - ../../../policy/sensitivity/archaeology/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "Expanded from a planned-file scaffold into the object-level RemoteSensingAnomaly semantic contract."
  - "The paired schema is currently a PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "OBJECT_MAP.md maps RemoteSensingAnomaly to remote_sensing_anomaly.md and remote_sensing_anomaly.schema.json as NEEDS VERIFICATION."
  - "This contract defines remote-sensing-anomaly meaning; it does not authorize publication, candidate confirmation, site confirmation, policy approval, review approval, or release approval."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# RemoteSensingAnomaly Contract

> Semantic contract for `RemoteSensingAnomaly`, the Archaeology-domain object representing a governed remote-sensing signal, pattern, or anomaly that may support candidate-feature review without converting the anomaly into proof, site confirmation, public geometry, or release approval by itself.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Family: remote sensing" src="https://img.shields.io/badge/family-remote__sensing-blue">
  <img alt="Sensitivity: controlled" src="https://img.shields.io/badge/sensitivity-controlled-red">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold-orange">
</p>

`contracts/domains/archaeology/remote_sensing_anomaly.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Anomaly boundary](#anomaly-boundary) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/archaeology/remote_sensing_anomaly.md`  
> **Schema path:** `schemas/contracts/v1/domains/archaeology/remote_sensing_anomaly.schema.json`  
> **Truth posture:** `CONFIRMED` target path, current update, paired scaffold schema, object-map row, and uploaded authoring guidance. Validator behavior, fixtures, policy behavior, source registry behavior, evidence-bundle implementation, review workflow, release workflow, API behavior, UI behavior, and runtime behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> This contract defines object meaning only. It does **not** authorize publication, candidate confirmation, site confirmation, fieldwork approval, policy approval, review approval, proof closure, public geometry, or release of controlled remote-sensing results.

---

## Meaning

`RemoteSensingAnomaly` is the Archaeology-domain object for a bounded anomaly, pattern, contrast, signature, or signal observed in remote-sensing material. It records the semantic boundary of an anomaly before it is promoted into a `LiDARCandidate`, `GeophysicsObservation`, `CandidateFeature`, `SiteComponent`, `ArchaeologicalSite`, map layer, or public-safe summary.

A remote-sensing anomaly may support:

- remote-sensing triage;
- candidate-feature review;
- comparison with LiDAR, geophysics, field, archival, or other observation families;
- survey planning or review queues;
- internal evidence packaging;
- steward, cultural, policy, validation, correction, and rollback workflows.

It is not:

- a confirmed archaeological site;
- a confirmed candidate feature;
- a raw image, raster, point cloud, tile, or derivative file;
- a public map layer;
- an EvidenceBundle;
- a PolicyDecision;
- a ReviewRecord;
- a ReleaseManifest;
- proof that a cultural feature exists;
- permission to disclose controlled anomaly geometry, interpretation detail, or review context.

---

## Repo fit

```text
contracts/
└── domains/
    └── archaeology/
        ├── README.md
        ├── remote_sensing_anomaly.md
        ├── lidar_candidate.md
        ├── geophysics_observation.md
        └── candidate_feature.md
```

Adjacent roots and object families:

| Root or object | Relationship |
|---|---|
| `./README.md` | Archaeology semantic-contract directory boundary. |
| `./OBJECT_MAP.md` | Maps `RemoteSensingAnomaly` to this contract and its expected schema. |
| `./domain_observation.md` | Generic observation envelope that may frame this anomaly family. |
| `./lidar_candidate.md` | Specialized LiDAR-derived candidate family that may overlap with or derive from anomaly review. |
| `./geophysics_observation.md` | Adjacent non-invasive observation family for cross-corroboration. |
| `./candidate_feature.md` | Candidate object that a reviewed anomaly may support, contest, or route into review. |
| `./site_component.md`, `./archaeological_site.md` | Higher-order archaeological entities that may cite reviewed evidence. |
| `./survey_project.md`, `./survey_transect.md` | Project and survey context that may govern follow-up review. |
| `./domain_feature_identity.md` | Identity/crosswalk object that may reconcile anomaly records with feature-like records. |
| `./cultural_review.md`, `./steward_review.md` | Review objects required before consequential interpretation or exposure. |
| `../../../schemas/contracts/v1/domains/archaeology/remote_sensing_anomaly.schema.json` | Current scaffold schema. |
| `../../../policy/sensitivity/archaeology/` | Policy gate home; behavior not verified here. |
| `../../../data/proofs/` | EvidenceBundle/proof support. |
| `../../../release/` | Release, correction, supersession, and rollback authority. |

---

## Anomaly boundary

`RemoteSensingAnomaly` must preserve the difference between signal, anomaly, candidate, interpretation, proof, and publication.

| Boundary | Rule |
|---|---|
| Anomaly vs. raw remote-sensing data | This object can summarize or reference an anomaly; raw imagery, rasters, point clouds, and tiles remain in lifecycle data roots. |
| Anomaly vs. LiDAR candidate | A LiDAR candidate may be a specialized anomaly or sibling family; the mapping remains subject to steward review. |
| Anomaly vs. geophysics observation | Geophysics may corroborate or contest an anomaly, but each object family keeps its own method lineage. |
| Anomaly vs. candidate feature | A reviewed anomaly may support `CandidateFeature`; it does not confirm one alone. |
| Anomaly vs. EvidenceBundle | Anomalies may be bundled as evidence; they are not the bundle or proof closure. |
| Anomaly vs. public release | Public use requires review, policy, transform, release, and rollback support. |

---

## Schema posture

The paired schema found for this contract is:

```text
schemas/contracts/v1/domains/archaeology/remote_sensing_anomaly.schema.json
```

Current schema evidence:

| Schema fact | Status |
|---|---|
| Schema file exists | `CONFIRMED` |
| Schema title is `Remote Sensing Anomaly` | `CONFIRMED` |
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
| Defining the meaning of a remote-sensing anomaly object | Yes | Must preserve source, processing, observation, evidence, sensitivity, review, and lifecycle posture. |
| Linking anomalies to candidate features or site components | Conditional | Must preserve uncertainty, method limits, correlation evidence, review state, and policy controls. |
| Supporting remote-sensing review queues | Yes | Must not imply public release or final interpretation. |
| Supporting public-safe summaries | Conditional | Requires policy, review, transform receipt, release record, and safe precision. |
| Treating an anomaly as candidate confirmation | No | Confirmation requires governed evidence and review. |
| Treating an anomaly as site proof | No | EvidenceBundle and review remain separate. |
| Publishing controlled anomaly detail by default | No | Controlled details fail closed unless approved through governed release. |
| Using schema validity as proof of truth | No | Schema shape is not evidence proof. |
| Treating this contract as release approval | No | Release authority remains separate. |

---

## Exclusions

| Does not belong in this contract | Correct home |
|---|---|
| Machine field shape | `../../../schemas/contracts/v1/domains/archaeology/remote_sensing_anomaly.schema.json`. |
| Validator implementation | `../../../tools/validators/...`. |
| Fixtures and tests | `../../../fixtures/...`, `../../../tests/...`. |
| Raw imagery, point clouds, rasters, tiles, hillshades, derivatives, or bulk remote-sensing exports | `../../../data/raw/`, `../../../data/work/`, or `../../../data/quarantine/`, subject to lifecycle and sensitivity rules. |
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
| `remote_sensing_anomaly_id` | Stable deterministic or steward-assigned anomaly identity. |
| `anomaly_type` | Spectral, textural, elevation, vegetation, soil-mark, crop-mark, thermal, multispectral, LiDAR-derived, or other reviewed anomaly type. |
| `source_refs` | SourceDescriptor/source record references for imagery, raster, derived product, or report sources. |
| `source_roles` | Source roles supporting, contextualizing, or contesting the anomaly. |
| `processing_refs` | Processing workflow, derivative, visualization, model, or transform references. |
| `anomaly_geometry_ref` | Internal geometry/support-scope reference; public-safe generalization required before exposure. |
| `spatial_precision_class` | Exact, generalized, suppressed, centroided, binned, county/region, or denied precision posture. |
| `anomaly_statement` | Bounded statement of what the anomaly may indicate, with uncertainty and limits. |
| `domain_observation_refs` | DomainObservation references when anomaly evidence is packaged through a generic observation envelope. |
| `lidar_candidate_refs` | LiDARCandidate references where this anomaly participates in a LiDAR-specific workflow. |
| `geophysics_observation_refs` | GeophysicsObservation references that corroborate, contest, or contextualize the anomaly. |
| `candidate_feature_refs` | CandidateFeature references supported, contested, or created from the anomaly. |
| `site_component_refs` | SiteComponent references only after review and evidence correlation. |
| `survey_refs` | SurveyProject or SurveyTransect references for review or follow-up. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references. |
| `confidence_statement` | Bounded confidence, uncertainty, or limitation statement. |
| `contradiction_refs` | Observations or claims that contest this anomaly. |
| `review_state` | Intake, needs review, under review, accepted internal anomaly, rejected, superseded, quarantined, release-candidate, or withdrawn. |
| `review_refs` | StewardReview, CulturalReview, or other review record references. |
| `policy_state` | Policy posture or policy-decision reference. |
| `sensitivity_class` | Sensitivity/public-safety classification. |
| `lineage_refs` | Prior, successor, supersession, split, merge, or rollback anomaly records. |
| `release_refs` | Release/candidate linkage where applicable. |
| `correction_refs` | Correction/supersession/rollback lineage. |
| `spec_hash` | Integrity pin for the representation. |

---

## Invariants

`RemoteSensingAnomaly` must preserve these invariants:

- remote-sensing anomalies are not proof by themselves;
- remote-sensing anomalies are not candidate-feature or site confirmation by themselves;
- source data, processing, anomaly signal, interpretation, candidate feature, evidence, review, policy, release, correction, and rollback objects must remain distinct;
- raw remote-sensing data and contract-level summaries must remain separated;
- source, processing, anomaly statement, uncertainty, sensitivity, review posture, and lifecycle state must remain inspectable;
- controlled anomaly detail fails closed unless policy, review, and release authorize a public-safe transform;
- contradiction, rejection, supersession, and correction lineage must remain traceable;
- schema validity is not evidence proof;
- public-facing use must be downstream of governed release artifacts and public-safe transforms;
- publication is a governed state transition, not a file move.

---

## Lifecycle

```mermaid
flowchart LR
  SRC[Remote-sensing source / derived product] --> ANOM[RemoteSensingAnomaly]
  ANOM --> QA[Validation + remote-sensing review]
  QA --> EVID[Evidence packaging + cross-correlation]
  EVID --> REVIEW[Steward / cultural review]
  REVIEW -->|reject or restrict| CONTROL[Restricted / rejected / superseded lineage]
  REVIEW -->|candidate support| FEATURE[CandidateFeature review]
  FEATURE --> POLICY[Policy + sensitivity screen]
  POLICY -->|public-safe transform| RELEASE[Release / correction / rollback records]
```

The contract defines the meaning of a remote-sensing-anomaly object. It does not replace source intake, remote-sensing processing, evidence resolution, schema validation, policy enforcement, review, transform receipts, release approval, correction, or rollback systems.

---

## Validation

Before relying on this contract, verify:

- schema fields beyond scaffold status;
- validator implementation and fixture coverage;
- canonical remote-sensing-anomaly ID and deterministic identity rules;
- boundary between RemoteSensingAnomaly, LiDARCandidate, GeophysicsObservation, DomainObservation, CandidateFeature, and SiteComponent;
- remote-sensing source, processing, derivative, and confidence vocabulary;
- EvidenceRef/EvidenceBundle requirements;
- source-role, time-kind, geometry, and confidence requirements;
- sensitivity handling for controlled anomaly and interpretation detail;
- steward/cultural review requirements;
- policy-gate requirements;
- release, correction, supersession, withdrawal, and rollback linkage;
- no downstream surface treats this contract as public disclosure permission, final proof, candidate confirmation, or site confirmation.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `remote_sensing_anomaly.md` scaffold | `CONFIRMED` | Target file existed as a planned-file scaffold. | Scaffold did not define authoritative semantics. |
| `remote_sensing_anomaly.schema.json` | `CONFIRMED scaffold` | Schema exists, is `PROPOSED`, has empty properties, allows additional properties, and points to this contract. | Does not enforce full remote-sensing-anomaly semantics. |
| `OBJECT_MAP.md` | `CONFIRMED current map` | Maps `RemoteSensingAnomaly` to `remote_sensing_anomaly.md` and `remote_sensing_anomaly.schema.json` with status `NEEDS VERIFICATION`. | Does not prove validator, fixture, policy, or release behavior. |
| Uploaded authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest Markdown with verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Rollback

Rollback is required if this contract is used to claim schema completeness, validator coverage, policy enforcement, review completion, release execution, API/UI behavior, evidence proof, candidate confirmation, site confirmation, public disclosure permission, or implementation maturity not verified in this task.

Rollback target: prior scaffold blob SHA `6dbbfddec12ac315319b3cb3cd7ac4a7c2d2db98`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Remote-sensing-anomaly vocabulary is reviewed by the Archaeology steward and remote sensing steward.
- [ ] Boundary between `RemoteSensingAnomaly`, `LiDARCandidate`, `GeophysicsObservation`, `DomainObservation`, `CandidateFeature`, and `SiteComponent` is accepted.
- [ ] Paired JSON Schema is expanded from scaffold status.
- [ ] Valid and invalid fixtures cover internal, restricted, rejected, superseded, corrected, release-candidate, and rollback states.
- [ ] Validator enforces required source, processing, anomaly, evidence, observation, confidence, review, sensitivity, policy, lineage, and visibility fields.
- [ ] Fixtures avoid unsafe anomaly or interpretation detail where references or redacted summaries are safer.
- [ ] EvidenceBundle, PolicyDecision, ReviewRecord, SensitivityTransform, PublicationTransformReceipt, ReleaseManifest, CorrectionNotice, and RollbackCard references are validated where required.
- [ ] API/UI surfaces prove they cannot treat a remote-sensing anomaly as proof, candidate confirmation, site confirmation, or public disclosure permission.
- [ ] Release and rollback dry-runs prove this contract cannot bypass publication gates.

## Status summary

`RemoteSensingAnomaly` is a sensitive Archaeology remote-sensing object. It can support anomaly review, candidate-feature evaluation, evidence packaging, correction, and public-safe explanation when evidence, review, policy, transform, and release allow, but it is not proof, not candidate confirmation, not site confirmation, not policy approval, and not release approval.

<p align="right"><a href="#top">Back to top</a></p>

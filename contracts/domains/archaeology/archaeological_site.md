<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/archaeology/archaeological-site
title: contracts/domains/archaeology/archaeological_site.md — ArchaeologicalSite Contract
type: contract
version: v0.2
status: draft
owners: OWNER_TBD — Archaeology steward · Contract steward · Evidence steward · Schema steward · Policy steward · Review steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; contracts; domains; archaeology; archaeological-site; semantic-contract
tags: [kfm, contracts, archaeology, archaeological-site, site, evidence, review, policy, lifecycle, governance]
related:
  - ./README.md
  - ./OBJECT_MAP.md
  - ./candidate_feature.md
  - ./site_component.md
  - ./provenience_context.md
  - ./PublicationTransformReceipt.md
  - ../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
  - ../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../docs/domains/archaeology/ARCHITECTURE.md
  - ../../../docs/domains/archaeology/DATA_LIFECYCLE.md
  - ../../../schemas/contracts/v1/domains/archaeology/archaeological_site.schema.json
  - ../../../policy/sensitivity/archaeology/
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "Expanded from a planned-file scaffold into the object-level ArchaeologicalSite semantic contract."
  - "The paired schema is a PROPOSED scaffold with empty properties and additionalProperties enabled."
  - "No validator implementation was found in this task."
  - "This contract preserves the candidate-vs-confirmed boundary and does not authorize public release or disclosure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ArchaeologicalSite Contract

> Semantic contract for `ArchaeologicalSite`, the Archaeology-domain object representing a reviewed archaeological or cultural-heritage site identity with evidence, source-role, review, policy, lifecycle, and release boundaries preserved.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Family: site" src="https://img.shields.io/badge/family-site-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold-orange">
  <img alt="Validator: missing" src="https://img.shields.io/badge/validator-missing-red">
</p>

`contracts/domains/archaeology/archaeological_site.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/domains/archaeology/archaeological_site.md`  
> **Schema path:** `schemas/contracts/v1/domains/archaeology/archaeological_site.schema.json`  
> **Truth posture:** `CONFIRMED` target path, current update, paired scaffold schema, object-map entry, architecture doctrine, and uploaded authoring guidance. Validator behavior, fixtures, policy behavior, source registry behavior, evidence-bundle implementation, review workflow, release workflow, API behavior, and UI behavior remain `NEEDS VERIFICATION`.

> [!CAUTION]
> This contract defines object meaning only. It does not authorize publication, review approval, policy approval, proof closure, release, public rendering, or access to restricted site details.

---

## Meaning

`ArchaeologicalSite` is the Archaeology-domain object for a reviewed site identity.

It represents the semantic claim that a site identity exists within KFM with:

- source and source-role context;
- evidence support;
- review posture;
- lifecycle state;
- sensitivity/policy posture;
- relationship to site components, contexts, surveys, artifacts, samples, chronology, and release lineage.

It is not a raw source row, not a candidate feature, not a remote-sensing anomaly, not a public layer, not an EvidenceBundle, not a PolicyDecision, not a ReviewRecord, and not a ReleaseManifest.

---

## Repo fit

```text
contracts/
└── domains/
    └── archaeology/
        ├── README.md
        ├── OBJECT_MAP.md
        └── archaeological_site.md
```

Adjacent roots:

| Root | Relationship |
|---|---|
| `./README.md` | Archaeology semantic-contract directory boundary. |
| `./OBJECT_MAP.md` | Maps `ArchaeologicalSite` to this contract and the expected schema. |
| `./candidate_feature.md` | Candidate object boundary; not equivalent to this contract. |
| `./site_component.md` | Component/part relationship to site identity. |
| `./provenience_context.md` | Context/provenience relationship. |
| `../../../schemas/contracts/v1/domains/archaeology/archaeological_site.schema.json` | Current scaffold schema. |
| `../../../policy/sensitivity/archaeology/` | Policy gate home; behavior not verified here. |
| `../../../data/proofs/` | EvidenceBundle/proof support. |
| `../../../release/` | Release, correction, supersession, and rollback authority. |

---

## Schema posture

The paired schema found in this task is:

```text
schemas/contracts/v1/domains/archaeology/archaeological_site.schema.json
```

Current schema evidence:

| Schema fact | Status |
|---|---|
| Schema file exists | `CONFIRMED` |
| Schema title is `Archaeological Site` | `CONFIRMED` |
| Schema status is `PROPOSED` | `CONFIRMED` |
| Schema properties are empty | `CONFIRMED` |
| `additionalProperties` is `true` | `CONFIRMED` |
| Schema `contract_doc` points to this contract | `CONFIRMED` |
| Validator implementation | `UNKNOWN / NOT FOUND` |

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Defining the meaning of a reviewed site identity | Yes | Must preserve evidence, source-role, review, and lifecycle context. |
| Relating a site to components, contexts, surveys, artifacts, samples, or chronology | Yes | Relationships must remain traceable and bounded. |
| Supporting catalog or release review | Conditional | Requires separate evidence, policy, review, and release records. |
| Supporting correction or rollback lineage | Yes | Must preserve prior state and reason for change where material. |
| Treating a candidate as a confirmed site | No | Candidate-to-site promotion is a governed state transition. |
| Using schema validity as proof of truth | No | Schema shape is not evidence proof. |
| Treating this contract as release approval | No | Release authority remains separate. |

---

## Exclusions

| Does not belong in this contract | Correct home |
|---|---|
| Machine field shape | `../../../schemas/contracts/v1/domains/archaeology/archaeological_site.schema.json`. |
| Validator implementation | `../../../tools/validators/...`. |
| Fixtures and tests | `../../../fixtures/...`, `../../../tests/...`. |
| Source registry records | `../../../data/registry/sources/`. |
| EvidenceBundle/proof content | `../../../data/proofs/`. |
| Policy decisions | `../../../policy/...`. |
| Review records | Governance/review contracts and records. |
| Release manifests, correction notices, rollback cards | `../../../release/`. |
| Public layer or UI implementation | Governed app/API/UI/layer roots. |

---

## Recommended fields

The current schema does not require these fields. They are `PROPOSED` semantic requirements for future schema/validator work:

| Field | Meaning |
|---|---|
| `site_id` | Stable site identity. |
| `source_refs` | SourceDescriptor/source record references. |
| `source_roles` | Roles of sources supporting the site identity. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references. |
| `review_refs` | Steward/cultural/reviewer records where applicable. |
| `policy_state` | Policy posture or policy-decision reference. |
| `support_scope_ref` | Reference to spatial/support scope, generalized where needed. |
| `component_refs` | SiteComponent references. |
| `context_refs` | ProvenienceContext or StratigraphicUnit references. |
| `survey_refs` | SurveyProject, SurveyTransect, or fieldwork references. |
| `artifact_refs` | ArtifactRecord or CollectionRepositoryRecord references. |
| `chronology_refs` | CulturalTemporalPeriod or ChronologyAssertion references. |
| `candidate_lineage_refs` | CandidateFeature, RemoteSensingAnomaly, LiDARCandidate, or GeophysicsObservation lineage where relevant. |
| `lifecycle_state` | RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET/PUBLISHED posture where used. |
| `release_refs` | Release/candidate linkage where applicable. |
| `correction_refs` | Correction/supersession/rollback lineage. |
| `spec_hash` | Integrity pin for the representation. |

---

## Invariants

`ArchaeologicalSite` must preserve these invariants:

- a candidate object is not a site until promoted through a governed review transition;
- context from other domains can support but cannot independently confirm a site;
- schema validity is not proof;
- evidence, policy, review, release, correction, and rollback objects remain separate families;
- site identity must remain traceable to sources, evidence, and review posture;
- public-facing use must be downstream of governed release artifacts;
- sensitive or rights-uncertain content remains constrained until policy and review allow a specific downstream use;
- publication is a governed state transition, not a file move.

---

## Lifecycle

```mermaid
flowchart LR
  SRC[Source records] --> CAND[Candidate or input evidence]
  CAND --> REVIEW[Review + evidence gate]
  REVIEW --> SITE[ArchaeologicalSite]
  SITE --> CAT[Catalog / triplet candidate]
  CAT --> POLICY[Policy + release review]
  POLICY --> RELEASE[Release / correction / rollback records]
```

The contract defines the meaning of a site object. It does not replace the review, evidence, policy, validation, release, or rollback systems.

---

## Validation

Before relying on this contract, verify:

- schema fields beyond scaffold status;
- validator implementation and fixture coverage;
- canonical identity and source-role vocabulary;
- candidate-to-site promotion rules;
- EvidenceRef/EvidenceBundle requirements;
- review-record requirements;
- policy-gate requirements;
- release, correction, supersession, and rollback linkage;
- no downstream surface treats this contract as release permission.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `archaeological_site.md` scaffold | `CONFIRMED` | Target file existed and was sourced from the planned-files ledger. | Scaffold did not define authoritative semantics. |
| `archaeological_site.schema.json` | `CONFIRMED scaffold` | Schema exists, is `PROPOSED`, has empty properties, and points to this contract. | Does not enforce full site semantics. |
| `OBJECT_MAP.md` | `CONFIRMED current map` | Maps `ArchaeologicalSite` to `archaeological_site.md` and `archaeological_site.schema.json`. | Map marks status `NEEDS VERIFICATION`. |
| `ARCHITECTURE.md` | `CONFIRMED doctrine / PROPOSED implementation` | Names `ArchaeologicalSite`, candidate-vs-confirmed distinction, cross-domain boundaries, and sensitive-lane posture. | Does not prove schema/validator/test coverage. |
| Uploaded authoring prompt v2 | `CONFIRMED user-supplied guidance` | Requires evidence-grounded, implementation-honest Markdown with verification and rollback posture. | Authoring guidance, not implementation proof. |

---

## Rollback

Rollback is required if this contract is used to claim schema completeness, validator coverage, policy enforcement, review completion, release execution, API/UI behavior, or implementation maturity not verified in this task.

Rollback target: prior scaffold content SHA `c8ad5b36561c162be711f5fa641af0379aa432da`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Schema fields are defined beyond scaffold status.
- [ ] Validator and fixtures are implemented and verified.
- [ ] Candidate-to-site promotion rules are tested.
- [ ] Evidence, policy, review, release, correction, and rollback references are testable.
- [ ] Cross-domain support boundaries are documented and tested.
- [ ] Downstream docs link to this contract as the accepted ArchaeologicalSite meaning boundary.

---

## Status summary

`ArchaeologicalSite` is the semantic contract for reviewed site identity in the Archaeology domain. It is not a candidate feature, not a raw source row, not an EvidenceBundle, not policy approval, not review approval, not release approval, and not implementation proof by itself.

<p align="right"><a href="#top">Back to top</a></p>

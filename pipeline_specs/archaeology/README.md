<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-archaeology-readme
title: Archaeology Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <sensitivity-review-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/archaeology/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/archaeology/README.md
  - docs/domains/archaeology/README.md
  - docs/domains/archaeology/ARCHITECTURE.md
  - docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - docs/domains/archaeology/CULTURAL_REVIEW.md
  - docs/domains/archaeology/PRESERVATION_MATRIX.md
  - docs/domains/archaeology/IDENTITY_MODEL.md
  - docs/domains/archaeology/SOURCE_REGISTRY.md
  - data/registry/sources/archaeology/
  - data/receipts/pipeline/archaeology/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/archaeology/
  - fixtures/pipeline_specs/archaeology/
tags: [kfm, pipeline-specs, archaeology, cultural-heritage, declarative-config, sensitivity, cultural-review, exact-location-denial, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/archaeology stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Archaeology specs configure pipeline intent, source scope, lifecycle gates, cultural-review gates, sensitivity gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Exact archaeological geometry, burial/sacred/culturally sensitive context, collection-security detail, private landowner detail, and unresolved sensitivity fail closed by default."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Pipeline Specs

> Declarative configuration lane for Archaeology and Cultural Heritage pipeline profiles, source scopes, review gates, sensitivity gates, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable Archaeology pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2F-d62728)
![sensitivity](https://img.shields.io/badge/sensitivity-fail%20closed-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/archaeology/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/archaeology/` — executable pipeline logic, the **how**  
**Placement posture:** Archaeology declarative specs belong here unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Spec anti-collapse rules](#3-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Archaeology spec scope](#6-archaeology-spec-scope)
- [7. Lifecycle posture](#7-lifecycle-posture)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Spec profile families](#10-spec-profile-families)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal spec profile shape](#12-minimal-spec-profile-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipeline_specs/archaeology/` owns declarative Archaeology and Cultural Heritage pipeline configuration.

It may describe:

- which Archaeology pipeline profile should run;
- which source descriptor ids are in scope;
- which stage gates are required;
- which cultural/steward review gates are required;
- which sensitivity, redaction, generalization, and publication-transform requirements apply;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Archaeology implementation belongs under `pipelines/domains/archaeology/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `archaeology/`? | Archaeology has a domain pipeline lane and needs sensitive-domain run profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Archaeology objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this approve release? | No. Release decisions, manifests, correction notices, and rollback cards belong under release authority. | CONFIRMED authority separation |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not cultural review, and not release approval.

[⬆ Back to top](#top)

---

## 3. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
validation profile -> ValidationReport
catalog profile -> catalog truth
publish profile -> PUBLISHED
candidate-feature profile -> confirmed site
redaction profile -> cultural-review approval
spec summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- cultural/steward review records remain review artifacts, not spec assertions;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative Archaeology specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- sensitivity-transform profiles;
- cultural/steward review handoff profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- remote-sensing candidate, LiDAR candidate, geophysics, 3D documentation, survey, artifact, context, and chronology profile variants.

A good placement test:

> If the file answers “what Archaeology pipeline should run, with what scope, sensitivity gates, and review gates?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Archaeology pipeline code | `pipelines/domains/archaeology/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/archaeology/` or accepted registry home |
| Archaeology object meaning | `contracts/domains/archaeology/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/archaeology/` or accepted schema home |
| Policy and review decisions | `policy/domains/archaeology/`, `policy/sensitivity/archaeology/`, review roots |
| Tests | `tests/pipeline_specs/archaeology/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/archaeology/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Archaeology spec scope

Archaeology specs may configure profiles for object families and candidate products such as:

- archaeological site candidates and confirmed-site records;
- surveys, survey projects, and survey transects;
- artifacts and artifact-record candidates;
- features, site components, context, and provenience context;
- excavation units and stratigraphic units;
- remote-sensing anomalies and LiDAR candidates;
- geophysics observations;
- 3D documentation metadata;
- cultural review and steward review handoffs;
- collection accession and repository records;
- chronology assertions and cultural-temporal period context;
- sensitivity transforms, redaction receipts, and publication-transform receipts.

Exact site geometry, sacred/burial/human-remains context, cultural sensitivity, collection-security detail, and unresolved rights/sensitivity must default to hold, denial, redaction, or generalized release posture.

[⬆ Back to top](#top)

---

## 7. Lifecycle posture

Specs may target lifecycle stages, but do not create the lifecycle transition themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare:

- input lifecycle state;
- expected output lifecycle state;
- source descriptor refs;
- candidate-versus-confirmed state controls;
- sensitivity transform requirements;
- cultural/steward review requirements;
- EvidenceBundle requirements;
- receipt requirements;
- release blockers;
- rollback and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Archaeology spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Lifecycle gate** — allowed input and output lifecycle states.
5. **Candidate-state gate** — candidate features remain distinct from confirmed sites.
6. **Sensitivity gate** — exact-location, burial/sacred, cultural, collection-security, and private-context handling.
7. **Cultural/steward review gate** — review refs required before any release-facing handoff.
8. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
9. **Validation gate** — validators, finite outcomes, and blocker handling.
10. **Receipt gate** — required run, transform, validation, redaction, cultural-review, publication-transform, or release-readiness receipts.
11. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/archaeology/
├── README.md
├── ingest.yaml                    # PROPOSED
├── normalize.yaml                 # PROPOSED
├── validate.yaml                  # PROPOSED
├── sensitivity_transform.yaml     # PROPOSED
├── cultural_review.yaml           # PROPOSED
├── catalog.yaml                   # PROPOSED
├── triplets.yaml                  # PROPOSED
├── publish.yaml                   # PROPOSED
├── rollback.yaml                  # PROPOSED
├── watchers.yaml                  # PROPOSED
├── remote_sensing_candidates.yaml # PROPOSED
├── lidar_candidates.yaml          # PROPOSED
├── geophysics.yaml                # PROPOSED
├── survey.yaml                    # PROPOSED
└── three_d_documentation.yaml      # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/archaeology/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Archaeology normalize implementation |
| `validate` | Declare validators, finite outcomes, and required reports. | Archaeology validate implementation |
| `sensitivity_transform` | Declare redaction/generalization/publication-transform requirements. | Archaeology sensitivity transform implementation |
| `cultural_review` | Declare cultural/steward review handoff requirements. | Review handoff implementation |
| `catalog` | Declare catalog closure requirements. | Archaeology catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Archaeology triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Archaeology/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Archaeology/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Archaeology/domain watcher support |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/archaeology/` | Declarative config only. |
| Executable target | `pipelines/domains/archaeology/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/archaeology/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/archaeology/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/archaeology/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/archaeology/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/archaeology/`, `release/manifests/archaeology/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal spec profile shape

The final schema is not defined here. This example shows the minimum intent a spec should preserve.

```yaml
schema_version: kfm.pipeline_spec.archaeology.v1
spec_id: archaeology.<profile>
version: 0.1.0
status: draft
domain: archaeology
owner: <archaeology-domain-steward>
implementation:
  target_pipeline: pipelines/domains/archaeology/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  cultural_review_required: true
  sensitivity_transform_required: true
  exact_location_release_allowed: false
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_policy_decision: false
  spec_is_cultural_review_approval: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/archaeology/
├── test_spec_shape.py                      # PROPOSED
├── test_no_runtime_outputs.py              # PROPOSED
├── test_implementation_refs.py             # PROPOSED
├── test_source_descriptor_refs.py          # PROPOSED
├── test_lifecycle_states.py                # PROPOSED
├── test_candidate_vs_confirmed_state.py    # PROPOSED
├── test_sensitivity_gates.py               # PROPOSED
├── test_cultural_review_required.py        # PROPOSED
├── test_required_receipts.py               # PROPOSED
├── test_release_requirements.py            # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, sensitivity gates, cultural/steward review gates, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/archaeology/README.md` stub;
- identifies this path as Archaeology declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, cultural-review approval, release approval, or public API/UI authority;
- defines expected Archaeology profile families, lifecycle gates, sensitivity gates, cultural/steward review gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/review/sensitivity posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-ARCH-001` | Which Archaeology spec schema is canonical for these profiles? | NEEDS VERIFICATION |
| `PIPE-SPEC-ARCH-002` | Which first-wave Archaeology source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-ARCH-003` | Which profile should be implemented first: source intake, candidate features, sensitivity transform, cultural review, catalog, or publish readiness? | NEEDS VERIFICATION |
| `PIPE-SPEC-ARCH-004` | Which CI workflow validates Archaeology specs? | UNKNOWN |
| `PIPE-SPEC-ARCH-005` | Which redaction, generalization, and publication-transform receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-ARCH-006` | Should spec files be split by lifecycle stage, source family, object family, or sensitivity tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, exact-location public artifacts, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.

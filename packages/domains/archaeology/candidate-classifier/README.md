<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-archaeology-candidate-classifier-readme
title: Archaeology Candidate Classifier Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/archaeology/candidate-classifier/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/archaeology/README.md
  - docs/domains/archaeology/README.md
  - pipelines/domains/archaeology/README.md
  - pipeline_specs/archaeology/README.md
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - tests/packages/domains/archaeology/candidate-classifier/
  - fixtures/packages/domains/archaeology/candidate-classifier/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, archaeology, candidate-classifier, candidate-feature, anomaly, classifier, sensitivity, redaction, cultural-review, steward-review, governance]
notes:
  - "This README fills the empty archaeology candidate-classifier package file with a governed helper-package contract."
  - "candidate-classifier is a shared helper package for classifying candidate features or anomalies; it is not site confirmation authority."
  - "Classifier outputs must remain candidate/probabilistic/interpretable until reviewed through governed evidence, cultural/steward review, policy, lifecycle, and release gates."
  - "Exact archaeological locations and sensitive cultural context fail closed for public use unless governed transforms and release controls are satisfied elsewhere."
  - "Concrete model/code exports, language runtime, package manifest, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Candidate Classifier Package

> Shared helper package for candidate-feature and anomaly classification support in the Archaeology and Cultural Heritage domain. It may provide reusable classifier adapters, scoring helpers, candidate labels, uncertainty handling, evaluation utilities, and fixture support. It must not confirm archaeological sites, disclose sensitive locations, decide policy, write lifecycle records, create EvidenceBundles, or approve release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Farchaeology%2Fcandidate--classifier%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20package-0a7ea4)
![candidate](https://img.shields.io/badge/output-candidate%20not%20confirmed-d62728)
![sensitivity](https://img.shields.io/badge/exact%20location-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/archaeology/candidate-classifier/README.md`  
**Parent package:** `packages/domains/archaeology/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/archaeology/`  
**Executable domain-pipeline root:** `pipelines/domains/archaeology/`  
**Declarative pipeline-spec root:** `pipeline_specs/archaeology/`  
**Contract/schema/policy roots:** `contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/`, and `policy/domains/archaeology/`  
**Placement posture:** helper package for candidate classification support only. Runtime, exports, package manifest, active tests, and classifier implementation are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Candidate-classifier boundary](#3-candidate-classifier-boundary)
- [4. Sensitivity and publication boundary](#4-sensitivity-and-publication-boundary)
- [5. Anti-collapse rules](#5-anti-collapse-rules)
- [6. What belongs here](#6-what-belongs-here)
- [7. What does not belong here](#7-what-does-not-belong-here)
- [8. Expected helper families](#8-expected-helper-families)
- [9. Inputs and outputs](#9-inputs-and-outputs)
- [10. Minimal package contract shape](#10-minimal-package-contract-shape)
- [11. Tests and fixtures](#11-tests-and-fixtures)
- [12. Definition of done](#12-definition-of-done)
- [13. Open questions](#13-open-questions)

---

## 1. Purpose

`packages/domains/archaeology/candidate-classifier/` may contain reusable candidate-classifier helper code for archaeology workflows.

It may support:

- candidate-feature and anomaly label helpers;
- classifier adapter interfaces;
- score, threshold, rank, and uncertainty helpers;
- model-output normalization into candidate DTOs;
- explainability and review-queue helper structures;
- evaluation metrics for candidate classification tests;
- safe redaction/generalization labels for classifier outputs;
- schema-bound validation adapters;
- no-network fixture builders for tests.

It does **not** confirm archaeological sites, declare features authentic, decide cultural sensitivity, decide public display, create EvidenceBundles, write lifecycle data, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/archaeology/`? | Candidate-classifier helpers are reusable Archaeology package code, not a new root. | CONFIRMED parent root pattern / NEEDS VERIFICATION for implementation |
| Is this Archaeology doctrine? | No. Doctrine and sensitivity posture belong under `docs/domains/archaeology/`. | CONFIRMED boundary posture |
| Is this a model-training or runtime pipeline? | No. Executable training/inference/promotion logic belongs under approved pipeline or app roots. | PROPOSED / NEEDS VERIFICATION |
| Can this confirm sites? | No. It may produce candidate labels, scores, and review inputs only. | CONFIRMED candidate boundary |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, uncertainty, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> A classifier score is not archaeological confirmation. It is a candidate signal that must remain bounded by evidence, review, sensitivity, policy, lifecycle, and release gates.

[⬆ Back to top](#top)

---

## 3. Candidate-classifier boundary

Allowed direction:

```text
candidate input / feature vector / model output
  -> candidate-classifier helper
  -> candidate label, score, explanation, uncertainty, and review queue payload
  -> governed archaeology pipeline/review flow handles evidence, sensitivity, and lifecycle state
```

Blocked direction:

```text
candidate-classifier helper
  -> confirmed archaeological site
  -> public map layer
  -> exact-location release
  -> policy decision
  -> EvidenceBundle creation
  -> lifecycle promotion
  -> release approval
```

Classifier helpers should be deterministic where practical, transparent about thresholds, and explicit about uncertainty. They should prefer review-ready candidate payloads over authoritative assertions.

[⬆ Back to top](#top)

---

## 4. Sensitivity and publication boundary

Candidate classification for archaeology has elevated exposure risk. This package must preserve these boundaries:

- exact locations are not public by default;
- candidate detections are not site confirmations;
- uncertain, culturally sensitive, sacred, collection-security, or looting-risk-adjacent outputs fail closed;
- public release requires redaction/generalization/sensitivity transforms outside this package;
- cultural and steward review are outside this package and must be recorded by their authority roots;
- generated classifier outputs are not evidence unless tied to an EvidenceBundle by a governed proof workflow.

[⬆ Back to top](#top)

---

## 5. Anti-collapse rules

Disallowed collapses:

```text
classifier score -> confirmed site
candidate label -> archaeological truth
threshold pass -> policy approval
review queue item -> review completion
redaction helper -> public release approval
model output -> EvidenceBundle
fixture candidate -> production candidate
successful package test -> lifecycle promotion
public-safe flag -> release manifest
```

Required separations:

- candidate-classifier helper code stays under `packages/domains/archaeology/candidate-classifier/`;
- Archaeology doctrine stays under `docs/domains/archaeology/`;
- object meaning stays under `contracts/domains/archaeology/`;
- schemas stay under `schemas/contracts/v1/domains/archaeology/`;
- policy and sensitivity rules stay under `policy/domains/archaeology/` and accepted policy roots;
- executable model runs, pipeline runs, and lifecycle writes stay under their executable/data roots;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 6. What belongs here

Appropriate source files include:

- classifier adapter interfaces;
- candidate label and score helpers;
- threshold configuration helpers that do not decide release;
- uncertainty and confidence payload helpers;
- feature-vector and model-output normalizers;
- review queue DTO helpers;
- explanation and provenance helper structures;
- evaluation helper utilities for package tests;
- redaction/generalization metadata helpers that do not approve publication;
- synthetic or sanitized test fixture builders.

A good placement test:

> If the file is reusable classifier support code that produces candidate/review inputs and does not confirm sites, write lifecycle data, decide policy, disclose sensitive locations, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Archaeology doctrine and scope docs | `docs/domains/archaeology/` |
| Archaeology object contracts | `contracts/domains/archaeology/` |
| Archaeology schemas | `schemas/contracts/v1/domains/archaeology/` |
| Archaeology policy decisions/rules | `policy/domains/archaeology/` and accepted policy roots |
| Executable classifier training or inference pipelines | `pipelines/domains/archaeology/` or accepted executable ML lane |
| Candidate lifecycle data | `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Review decisions | cultural/steward review authority roots |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| Public map/UI rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/archaeology/candidate-classifier/` |
| Package fixtures | `fixtures/packages/domains/archaeology/candidate-classifier/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 8. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `adapter` | Model/classifier adapter interfaces. | PROPOSED |
| `labels` | Candidate label vocab helpers that preserve candidate status. | PROPOSED |
| `score` | Score, threshold, rank, and calibration helpers. | PROPOSED |
| `uncertainty` | Uncertainty/confidence payload helpers. | PROPOSED |
| `features` | Feature-vector normalization helpers. | PROPOSED |
| `explain` | Explanation/provenance helper payloads. | PROPOSED |
| `review_queue` | Candidate review queue DTO helpers. | PROPOSED |
| `sensitivity` | Redaction/generalization metadata support, not release approval. | PROPOSED |
| `evaluation` | Package-test evaluation helpers. | PROPOSED |
| `fixtures` | Synthetic/sanitized fixture builders. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/archaeology/candidate-classifier/` | Shared classifier helper code only. |
| Parent helper package | `packages/domains/archaeology/` | Domain helper parent. |
| Domain doctrine | `docs/domains/archaeology/` | Scope and sensitivity posture. |
| Domain contracts | `contracts/domains/archaeology/` | Meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/archaeology/` | Machine shape authority. |
| Domain policy | `policy/domains/archaeology/` | Admissibility/exposure authority. |
| Executable classifier run | executable pipeline/app lane | Not this helper package. |
| Candidate lifecycle data | `data/<phase>/archaeology/` | Not written here as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/archaeology/candidate-classifier/` | Package validation. |
| Fixtures | `fixtures/packages/domains/archaeology/candidate-classifier/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 10. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.archaeology.candidate_classifier
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - archaeology_doctrine
  - site_confirmation
  - exact_location_release
  - model_runtime
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - classifier adapter interfaces
  - candidate label helpers
  - score and threshold helpers
  - uncertainty payload helpers
  - review queue helpers
  - sensitivity metadata helpers
  - evaluation helpers
  - safe fixture builders
required_invariants:
  no_site_confirmation: true
  no_exact_location_publication: true
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  candidate_output_is_not_confirmation: true
```

[⬆ Back to top](#top)

---

## 11. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/archaeology/candidate-classifier/
├── test_candidate_classifier_boundaries.py  # PROPOSED
├── test_score_not_site_confirmation.py      # PROPOSED
├── test_threshold_not_policy_approval.py    # PROPOSED
├── test_review_queue_not_review_complete.py # PROPOSED
├── test_exact_location_not_public.py        # PROPOSED
├── test_no_hidden_lifecycle_writes.py       # PROPOSED
├── test_no_evidence_fabrication.py          # PROPOSED
├── test_no_release_approval.py              # PROPOSED
├── test_synthetic_fixtures_only.py          # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

Fixtures should live in `fixtures/packages/domains/archaeology/candidate-classifier/` unless a package-local convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not expose controlled archaeology locations, cultural context, collection-security detail, or other restricted material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the empty `packages/domains/archaeology/candidate-classifier/README.md` file;
- identifies this path as shared candidate-classifier helper-code space;
- keeps site confirmation, doctrine, contracts, schemas, policy, lifecycle data, evidence, cultural/steward review, and release decisions in their authority roots;
- blocks classifier helpers from becoming site confirmation, exact-location disclosure, model runtime authority, policy approval, lifecycle promotion, EvidenceBundle creation, or release approval;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Archaeology sensitivity, cultural/steward review, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-ARCH-CC-001` | Which language/runtime owns `packages/domains/archaeology/candidate-classifier/`? | UNKNOWN |
| `PKG-DOM-ARCH-CC-002` | Is this helper package model-agnostic, or does it wrap a specific classifier family? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-ARCH-CC-003` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-ARCH-CC-004` | Which canonical schemas own candidate labels, score payloads, uncertainty, review queue, and sensitivity metadata? | NEEDS VERIFICATION |
| `PKG-DOM-ARCH-CC-005` | Which CI workflow validates candidate-not-confirmed and exact-location-denial rules? | UNKNOWN |
| `PKG-DOM-ARCH-CC-006` | Should executable classifier runs live under `pipelines/domains/archaeology/`, an ML root, or an app/service root? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this package helper-focused and subordinate to Archaeology governance. Do not add site-confirmation logic, exact-location publication, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, controlled-location examples, culturally sensitive examples, or generated truth claims here.

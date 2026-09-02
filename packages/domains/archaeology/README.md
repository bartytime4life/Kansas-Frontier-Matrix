<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-archaeology-readme
title: Archaeology Domain Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <schema-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/archaeology/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/README.md
  - docs/domains/archaeology/README.md
  - packages/README.md
  - packages/domains/README.md
  - pipelines/domains/archaeology/README.md
  - pipeline_specs/archaeology/README.md
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - tests/packages/domains/archaeology/
  - fixtures/packages/domains/archaeology/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, archaeology, cultural-heritage, shared-library, mapping-helpers, identity-normalizers, observation-parsers, candidate-features, cultural-review, sensitivity-transform, exact-location-denial, governance]
notes:
  - "This README expands the short packages/domains/archaeology scaffold into a governed domain-helper package contract."
  - "packages/domains/archaeology/ may contain reusable Archaeology helper code only; it is not Archaeology doctrine, schema authority, contract authority, policy authority, lifecycle data, executable pipeline logic, evidence closure, or release approval."
  - "Exact archaeological locations, sacred/culturally sensitive contexts, collection security detail, and looting-risk exposure fail closed unless governed review, sensitivity transform, release, correction, and rollback controls are satisfied elsewhere."
  - "Candidate/anomaly helpers preserve uncertainty and source role; they do not confirm sites or create archaeological truth."
  - "Concrete modules, language runtime, package manifests, exports, build scripts, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Domain Package

> Shared helper-code lane for the Archaeology and Cultural Heritage domain: mapping helpers, identity normalizers, observation parsers, candidate-feature adapters, sensitivity-transform helpers, cultural/steward-review DTO adapters, and fixture utilities. This package supports governed apps, pipelines, workers, tests, and tools, but it does not define archaeological truth, own schemas/contracts/policy, write lifecycle data, close EvidenceBundles, or approve public release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Farchaeology%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20code-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Farchaeology%2F-d62728)
![sensitivity](https://img.shields.io/badge/exact%20location-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/archaeology/README.md`  
**Parent package root:** `packages/domains/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/archaeology/`  
**Executable domain-pipeline root:** `pipelines/domains/archaeology/`  
**Declarative pipeline-spec root:** `pipeline_specs/archaeology/`  
**Contract/schema/policy roots:** `contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/`, and `policy/domains/archaeology/`  
**Placement posture:** helper code only. Runtime, exports, package manifest, child modules, and active tests are `NEEDS VERIFICATION` until verified by repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Archaeology sensitivity boundary](#3-archaeology-sensitivity-boundary)
- [4. Package anti-collapse rules](#4-package-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Expected helper families](#7-expected-helper-families)
- [8. Inputs and outputs](#8-inputs-and-outputs)
- [9. Minimal package contract shape](#9-minimal-package-contract-shape)
- [10. Tests and fixtures](#10-tests-and-fixtures)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`packages/domains/archaeology/` may contain reusable Archaeology helper code that supports KFM domain processing without becoming an authority root.

It may support:

- candidate-feature and anomaly mapping helpers;
- survey, artifact, context, excavation-unit, and chronology DTO adapters;
- LiDAR, geophysics, remote-sensing, and 3D-documentation parsing helpers that preserve uncertainty;
- cultural-review and steward-review reference helpers;
- sensitivity-transform and publication-transform helper utilities;
- source role, source time, valid time, limitation, caveat, and access-state preservation helpers;
- public-safe generalization/redaction helper functions that do not approve publication;
- schema-bound validation adapters that call canonical schema tooling;
- no-network fixture builders for tests.

It does **not** define Archaeology objects, confirm sites, identify sensitive locations for public use, decide cultural sensitivity, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/domains/archaeology/`? | Archaeology helper code belongs under the packages root when reusable across apps, pipelines, workers, and tests. | CONFIRMED root pattern / NEEDS VERIFICATION for implementation |
| Is this Archaeology doctrine? | No. Archaeology doctrine and scope belong under `docs/domains/archaeology/`. | CONFIRMED boundary posture |
| Is this executable pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/archaeology/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs and validation results only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Archaeology helper code can normalize, map, generalize, and translate. It cannot confirm sites, expose exact locations, bypass cultural/steward review, or replace EvidenceBundle closure.

[⬆ Back to top](#top)

---

## 3. Archaeology sensitivity boundary

Archaeology and cultural heritage are highly sensitive. Helper code must preserve these boundaries:

- exact archaeological geometry is denied by default for public surfaces;
- sacred/culturally sensitive contexts, human-remains contexts, collection-security detail, private-landowner detail, unresolved sensitivity, and looting-risk exposure fail closed;
- candidate features, LiDAR anomalies, remote-sensing anomalies, and geophysics observations are candidates unless confirmed through governed review and evidence;
- public products require approved redaction, generalization, or sensitivity transforms outside this package;
- cultural review, steward review, EvidenceBundle, ReleaseManifest, correction path, and rollback posture are required outside this package for public release;
- helper-derived values and generated interpretations are not evidence by themselves.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
archaeology helper -> Archaeology doctrine
candidate parser -> confirmed site
anomaly adapter -> site proof
context normalizer -> provenience truth
chronology helper -> chronology authority
sensitivity helper -> public release approval
redaction helper -> sensitivity decision
cultural-review ref -> review completion
validation helper -> validation pass
successful package test -> lifecycle promotion
```

Required separations:

- helper code stays under `packages/domains/archaeology/`;
- Archaeology doctrine stays under `docs/domains/archaeology/`;
- Archaeology meaning stays under `contracts/domains/archaeology/`;
- Archaeology schemas stay under `schemas/contracts/v1/domains/archaeology/`;
- Archaeology policy stays under `policy/domains/archaeology/` and sensitivity/source policy roots;
- executable transformations stay under `pipelines/domains/archaeology/`;
- declarative run profiles stay under `pipeline_specs/archaeology/`;
- lifecycle records and receipts stay under `data/`;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source files include:

- candidate-feature mapping helpers;
- survey/artifact/context/excavation-unit DTO adapters;
- chronology and temporal-period helper adapters that preserve uncertainty;
- LiDAR/remote-sensing/geophysics/3D-documentation parser helpers that retain candidate status;
- cultural-review and steward-review reference helpers;
- sensitivity-transform and redaction/generalization helper functions that do not approve publication;
- crosswalk helpers that preserve native classifications and source roles;
- schema-generated adapters with generation provenance;
- safe fixture builders and mock helpers for package tests;
- compatibility helpers for Archaeology helper migrations.

A good placement test:

> If the file is reusable Archaeology helper code and does not confirm archaeological truth, write lifecycle data, decide policy, disclose sensitive locations, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Archaeology doctrine and source scope docs | `docs/domains/archaeology/` |
| Archaeology object contracts | `contracts/domains/archaeology/` |
| Archaeology schemas | `schemas/contracts/v1/domains/archaeology/` |
| Archaeology policy decisions/rules | `policy/domains/archaeology/` and accepted policy roots |
| Executable Archaeology pipelines | `pipelines/domains/archaeology/` |
| Declarative Archaeology specs | `pipeline_specs/archaeology/` |
| Source descriptors | `data/registry/sources/archaeology/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Runtime receipts | `data/receipts/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| UI-only rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/archaeology/` |
| Package fixtures | `fixtures/packages/domains/archaeology/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `candidate` | Candidate-feature and anomaly mapping helpers that preserve uncertainty. | PROPOSED |
| `survey` | Survey/project/transect DTO adapters. | PROPOSED |
| `artifact` | Artifact and collection-record helper adapters. | PROPOSED |
| `context` | Context/provenience helper adapters with source-role preservation. | PROPOSED |
| `chronology` | Chronology and temporal-period helpers with caveats. | PROPOSED |
| `sensing` | LiDAR, remote-sensing, geophysics, and 3D-documentation helper adapters. | PROPOSED |
| `review` | Cultural-review and steward-review reference helpers. | PROPOSED |
| `sensitivity` | Redaction/generalization/sensitivity-transform support, not release approval. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Package-only fixture builders, if accepted by package convention. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/archaeology/` | Shared helper source only. |
| Domain doctrine | `docs/domains/archaeology/` | Scope, sensitivity, and human-facing control plane. |
| Domain contracts | `contracts/domains/archaeology/` | Object meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/archaeology/` | Machine shape authority. |
| Domain policy | `policy/domains/archaeology/` | Admissibility/exposure authority. |
| Executable domain pipeline | `pipelines/domains/archaeology/` | Runs transformations. |
| Declarative domain spec | `pipeline_specs/archaeology/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/archaeology/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/archaeology/` | Package validation. |
| Fixtures | `fixtures/packages/domains/archaeology/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.archaeology
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - archaeology_doctrine
  - site_confirmation
  - exact_location_release
  - object_contract
  - schema_home
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - candidate mapping helpers
  - survey and artifact adapters
  - context and chronology parsers
  - remote-sensing helper adapters
  - cultural-review reference helpers
  - sensitivity-transform helper utilities
  - schema-bound adapters
  - safe fixture builders
required_invariants:
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  exact_location_public_denied_by_default: true
  candidate_output_is_not_confirmation: true
```

[⬆ Back to top](#top)

---

## 10. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/archaeology/
├── test_package_boundaries.py                  # PROPOSED
├── test_candidate_not_site_confirmation.py     # PROPOSED
├── test_exact_location_not_public.py           # PROPOSED
├── test_sensitivity_helper_not_release.py      # PROPOSED
├── test_cultural_review_ref_not_completion.py  # PROPOSED
├── test_context_preserves_source_role.py       # PROPOSED
├── test_chronology_preserves_uncertainty.py    # PROPOSED
├── test_no_hidden_lifecycle_writes.py          # PROPOSED
├── test_no_policy_or_release_decisions.py      # PROPOSED
└── test_root_boundary.py                       # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/archaeology/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain exact archaeological locations, culturally sensitive contexts, collection-security details, or looting-risk content unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- expands the scaffold `packages/domains/archaeology/README.md`;
- identifies this path as shared Archaeology helper-code space;
- preserves docs, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, and release roots as separate authorities;
- blocks Archaeology helpers from becoming doctrine, schema, contract, policy, lifecycle, evidence, release, exact-location disclosure, candidate confirmation, or public-trust authority;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Archaeology sensitivity, cultural/steward review, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-ARCH-001` | Which language/runtime owns `packages/domains/archaeology/`? | UNKNOWN |
| `PKG-DOM-ARCH-002` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-ARCH-003` | Which helper modules are actually exported today? | UNKNOWN |
| `PKG-DOM-ARCH-004` | Which canonical schemas own candidate, survey, artifact, context, chronology, sensing, review, and sensitivity helper shapes? | NEEDS VERIFICATION |
| `PKG-DOM-ARCH-005` | Which CI workflow validates Archaeology helper packages and exact-location denial? | UNKNOWN |
| `PKG-DOM-ARCH-006` | Should sensitivity-transform helpers live here, in a policy package, or in a domain pipeline lane? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this package helper-focused and subordinate to Archaeology governance. Do not add Archaeology doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, exact-location examples, culturally sensitive examples, collection-security details, or generated truth claims here.

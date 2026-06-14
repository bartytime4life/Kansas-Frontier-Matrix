<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-archaeology-generalization-readme
title: Archaeology Generalization Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/archaeology/generalization/README.md
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
  - data/proofs/evidence_bundle/
  - release/manifests/
  - tests/packages/domains/archaeology/generalization/
  - fixtures/packages/domains/archaeology/generalization/
tags: [kfm, packages, domains, archaeology, generalization, redaction, sensitivity-transform, public-safe, exact-location-denial, cultural-review, governance]
notes:
  - "This README fills the empty archaeology generalization package file with a governed helper-package contract."
  - "generalization is a shared helper package for public-safe transformation support; it is not a policy engine, sensitivity decision authority, or release authority."
  - "Generalization helpers must preserve exact-source refs, sensitivity-transform refs, evidence refs, review refs, and release refs without exposing restricted detail."
  - "Exact archaeological locations and sensitive cultural context fail closed for public use unless governed review, transform, and release controls are satisfied elsewhere."
  - "Concrete code exports, language runtime, package manifest, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Generalization Package

> Shared helper package for Archaeology public-safe generalization and redaction support. It may help construct generalized geometry descriptors, scale bands, masking metadata, transform refs, and safe display hints, but it must not decide sensitivity, expose exact locations, create EvidenceBundles, write lifecycle records, or approve release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Farchaeology%2Fgeneralization%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20package-0a7ea4)
![output](https://img.shields.io/badge/generalization-not%20release-d62728)
![sensitivity](https://img.shields.io/badge/exact%20location-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/archaeology/generalization/README.md`  
**Parent package:** `packages/domains/archaeology/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/archaeology/`  
**Executable domain-pipeline root:** `pipelines/domains/archaeology/`  
**Contract/schema/policy roots:** `contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/`, and `policy/domains/archaeology/`  
**Placement posture:** helper package for generalization/redaction support only. Runtime, exports, package manifest, active tests, and implementation are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Generalization boundary](#3-generalization-boundary)
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

`packages/domains/archaeology/generalization/` may contain reusable helper code for preparing public-safe generalized or redacted Archaeology projection shapes.

It may support:

- generalized geometry descriptor helpers;
- scale-band and uncertainty-band helper utilities;
- redaction and masking metadata helpers;
- sensitivity-transform reference helpers;
- public-safe display hint helpers;
- limitation and caveat preservation helpers;
- review-ref and release-ref preservation helpers;
- safe missing-transform outcome helpers;
- schema-bound validation adapters;
- no-network fixture builders for tests.

It does **not** decide that a transform is sufficient, publish exact or generalized locations, decide policy, create EvidenceBundles, write lifecycle data, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/archaeology/`? | Generalization helpers are reusable Archaeology package code, not a new root. | CONFIRMED parent root pattern / NEEDS VERIFICATION for implementation |
| Is this a sensitivity policy engine? | No. It may apply already-approved transform parameters, but policy authority stays outside this package. | CONFIRMED policy separation |
| Is this Archaeology doctrine? | No. Doctrine and sensitivity posture belong under `docs/domains/archaeology/`. | CONFIRMED boundary posture |
| Can this publish generalized layers? | No. It may prepare helper shapes only; publication remains a governed release decision. | CONFIRMED release separation |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, limitations, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> Generalization is not release approval. A helper-produced mask, scale band, or generalized geometry descriptor remains downstream of cultural/steward review, policy, EvidenceBundle, sensitivity transform, and release state.

[⬆ Back to top](#top)

---

## 3. Generalization boundary

Allowed direction:

```text
approved transform parameters / EvidenceRef / review refs / policy refs / release refs
  -> generalization helper
  -> generalized descriptor, redaction metadata, scale band, or public-safe display hint
  -> governed API/release surface decides exposure where authorized
```

Blocked direction:

```text
generalization helper
  -> sensitivity decision
  -> exact-location disclosure
  -> release approval
  -> EvidenceBundle creation
  -> lifecycle write
  -> public map-layer authority
  -> site confirmation
```

Generalization helpers should be deterministic, preserve all refs and caveats, and fail safe when evidence, review, policy, transform, or release state is missing or inaccessible.

[⬆ Back to top](#top)

---

## 4. Sensitivity and publication boundary

Archaeology generalization has high exposure risk. This package must preserve these boundaries:

- exact locations are not public by default;
- generalized outputs must not leak restricted geometry, culturally sensitive context, collection-security detail, or looting-risk detail;
- candidate and anomaly context remains candidate unless confirmed through governed review and evidence;
- missing or inaccessible transform state should produce abstain/deny-safe outcomes, not fallback disclosure;
- cultural review, steward review, EvidenceBundle, SensitivityTransform, ReleaseManifest, correction path, and rollback posture remain outside this package;
- helper-derived generalized outputs are not evidence and are not release approval.

[⬆ Back to top](#top)

---

## 5. Anti-collapse rules

Disallowed collapses:

```text
generalization -> release approval
redaction metadata -> sensitivity decision
scale band -> public safety guarantee
masking helper -> exact-location clearance
transform ref -> transform completion
review ref -> review completion
summary geometry -> true site geometry
fixture geometry -> production geometry
successful package test -> lifecycle promotion
public-safe flag -> ReleaseManifest
```

Required separations:

- generalization helper code stays under `packages/domains/archaeology/generalization/`;
- Archaeology doctrine stays under `docs/domains/archaeology/`;
- object meaning stays under `contracts/domains/archaeology/`;
- schemas stay under `schemas/contracts/v1/domains/archaeology/`;
- policy and sensitivity rules stay under `policy/domains/archaeology/` and accepted policy roots;
- executable transform runs and lifecycle writes stay under their executable/data roots;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 6. What belongs here

Appropriate source files include:

- generalized descriptor helper functions;
- redaction and masking metadata helpers;
- scale-band and uncertainty-band helpers;
- transform-ref preservation helpers;
- review-ref and release-ref preservation helpers;
- limitation/caveat preservation helpers;
- safe display-hint DTO helpers;
- missing or inaccessible transform outcome helpers;
- schema-bound validation adapters and safe errors;
- synthetic or sanitized fixture builders.

A good placement test:

> If the file is reusable generalization support code that preserves evidence and governance refs and does not decide sensitivity, reveal sensitive locations, write lifecycle records, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Sensitivity policy decisions | `policy/domains/archaeology/` and accepted policy roots |
| EvidenceBundle storage or creation | `data/proofs/evidence_bundle/` and proof tooling |
| Archaeology doctrine and scope docs | `docs/domains/archaeology/` |
| Archaeology object contracts | `contracts/domains/archaeology/` |
| Archaeology schemas | `schemas/contracts/v1/domains/archaeology/` |
| Executable generalization pipeline | `pipelines/domains/archaeology/` or accepted executable lane |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Review decisions | cultural/steward review authority roots |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| Public map/UI rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/archaeology/generalization/` |
| Package fixtures | `fixtures/packages/domains/archaeology/generalization/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 8. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `geometry` | Generalized geometry descriptors, not true site geometry. | PROPOSED |
| `scale_band` | Scale and uncertainty band helpers. | PROPOSED |
| `masking` | Mask/redaction metadata helpers. | PROPOSED |
| `transform_ref` | SensitivityTransform reference preservation. | PROPOSED |
| `review_refs` | Cultural/steward review reference preservation. | PROPOSED |
| `display` | Public-safe display hint DTOs, not API routes. | PROPOSED |
| `outcomes` | Missing/inaccessible transform abstain/deny-safe outcomes. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Synthetic/sanitized fixture builders. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/archaeology/generalization/` | Shared generalization helper code only. |
| Parent helper package | `packages/domains/archaeology/` | Domain helper parent. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Domain doctrine | `docs/domains/archaeology/` | Scope and sensitivity posture. |
| Domain contracts | `contracts/domains/archaeology/` | Meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/archaeology/` | Machine shape authority. |
| Domain policy | `policy/domains/archaeology/` | Admissibility/exposure authority. |
| Lifecycle data | `data/<phase>/archaeology/` | Not written here as hidden behavior. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/archaeology/generalization/` | Package validation. |
| Fixtures | `fixtures/packages/domains/archaeology/generalization/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 10. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.archaeology.generalization
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - sensitivity_decision
  - exact_location_release
  - evidence_bundle
  - archaeology_doctrine
  - policy_decision
  - lifecycle_write
  - release_decision
allowed_responsibilities:
  - generalized descriptor helpers
  - redaction and masking metadata helpers
  - scale and uncertainty band helpers
  - sensitivity transform reference helpers
  - review reference helpers
  - display hint DTOs
  - safe outcome helpers
  - synthetic fixture builders
required_invariants:
  no_exact_location_publication: true
  no_sensitivity_decision: true
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  generalization_output_is_not_release: true
```

[⬆ Back to top](#top)

---

## 11. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/archaeology/generalization/
├── test_generalization_boundaries.py       # PROPOSED
├── test_generalization_not_release.py      # PROPOSED
├── test_redaction_not_policy_decision.py   # PROPOSED
├── test_exact_location_not_public.py       # PROPOSED
├── test_missing_transform_abstains.py      # PROPOSED
├── test_inaccessible_transform_denies.py   # PROPOSED
├── test_review_ref_not_review_completion.py # PROPOSED
├── test_no_hidden_lifecycle_writes.py      # PROPOSED
├── test_no_release_approval.py             # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

Fixtures should live in `fixtures/packages/domains/archaeology/generalization/` unless a package-local convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not expose controlled archaeology locations, cultural context, collection-security detail, or other restricted material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the empty `packages/domains/archaeology/generalization/README.md` file;
- identifies this path as shared generalization helper-code space;
- keeps sensitivity decisions, doctrine, contracts, schemas, policy, lifecycle data, review decisions, EvidenceBundles, and release decisions in their authority roots;
- blocks generalization helpers from becoming sensitivity decisions, exact-location disclosure, policy approval, lifecycle promotion, proof, or release approval;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Archaeology sensitivity, cultural/steward review, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-ARCH-GEN-001` | Which language/runtime owns `packages/domains/archaeology/generalization/`? | UNKNOWN |
| `PKG-DOM-ARCH-GEN-002` | Which canonical schema owns generalized geometry descriptors and transform references? | NEEDS VERIFICATION |
| `PKG-DOM-ARCH-GEN-003` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-ARCH-GEN-004` | Which CI workflow validates generalization-not-release and exact-location-denial rules? | UNKNOWN |
| `PKG-DOM-ARCH-GEN-005` | Should executable generalization transforms live under `pipelines/domains/archaeology/`, a policy root, or a release-prep lane? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-ARCH-GEN-006` | Which scale bands and masking strategies are canonical versus policy-configured? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package helper-focused and subordinate to Archaeology sensitivity governance. Do not add sensitivity decision logic, exact-location publication, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, controlled-location examples, culturally sensitive examples, collection-security details, or generated truth claims here.

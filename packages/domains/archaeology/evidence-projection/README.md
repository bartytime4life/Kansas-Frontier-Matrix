<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-archaeology-evidence-projection-readme
title: Archaeology Evidence Projection Package README
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
path: packages/domains/archaeology/evidence-projection/README.md
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
  - data/catalog/
  - data/triplets/
  - release/manifests/
  - tests/packages/domains/archaeology/evidence-projection/
  - fixtures/packages/domains/archaeology/evidence-projection/
tags: [kfm, packages, domains, archaeology, evidence-projection, evidencebundle, evidenceref, projection, citation, public-safe, redaction, sensitivity-transform, governance]
notes:
  - "This README fills the empty archaeology evidence-projection package file with a governed helper-package contract."
  - "evidence-projection is a shared helper package for projecting already-governed evidence references into safe DTOs and display envelopes; it is not an EvidenceBundle store or proof authority."
  - "Projection helpers must preserve EvidenceRef, source role, limitation, review state, policy state, release state, and sensitivity-transform references."
  - "Exact archaeological locations and sensitive cultural context fail closed for public use unless governed transforms and release controls are satisfied elsewhere."
  - "Concrete code exports, language runtime, package manifest, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Evidence Projection Package

> Shared helper package for projecting governed Archaeology evidence references into safe citation, summary, review, catalog, triplet, or API-display structures. It may help preserve EvidenceRef, source role, limits, sensitivity-transform refs, and release refs, but it must not create EvidenceBundles, confirm sites, disclose sensitive locations, decide policy, write lifecycle records, or approve release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Farchaeology%2Fevidence--projection%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20package-0a7ea4)
![evidence](https://img.shields.io/badge/projection-not%20proof-d62728)
![sensitivity](https://img.shields.io/badge/exact%20location-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/archaeology/evidence-projection/README.md`  
**Parent package:** `packages/domains/archaeology/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Evidence authority:** `data/proofs/evidence_bundle/` and accepted proof homes  
**Domain doctrine root:** `docs/domains/archaeology/`  
**Executable domain-pipeline root:** `pipelines/domains/archaeology/`  
**Contract/schema/policy roots:** `contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/`, and `policy/domains/archaeology/`  
**Placement posture:** helper package for evidence projection only. Runtime, exports, package manifest, active tests, and implementation are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Evidence-projection boundary](#3-evidence-projection-boundary)
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

`packages/domains/archaeology/evidence-projection/` may contain reusable helper code for converting already-governed Archaeology evidence references into safe projection shapes.

It may support:

- EvidenceRef and EvidenceBundleRef projection helpers;
- citation and summary DTO helpers;
- source-role and limitation preservation helpers;
- cultural-review and steward-review reference preservation;
- sensitivity-transform, redaction, and generalization metadata helpers;
- catalog/triplet projection helper DTOs that do not create records;
- public-safe display envelope helpers for governed APIs;
- safe missing-evidence or inaccessible-evidence outcomes;
- no-network fixture builders for tests.

It does **not** create EvidenceBundles, make claims true, confirm sites, expose sensitive locations, decide policy, write catalog/triplet/lifecycle records, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/archaeology/`? | Evidence projection helpers are reusable Archaeology package code, not a new root. | CONFIRMED parent root pattern / NEEDS VERIFICATION for implementation |
| Is this an EvidenceBundle store? | No. EvidenceBundles live under proof/data homes. | CONFIRMED boundary posture |
| Is this Archaeology doctrine? | No. Doctrine and sensitivity posture belong under `docs/domains/archaeology/`. | CONFIRMED boundary posture |
| Can this publish evidence or map layers? | No. It may prepare safe projection shapes only; release remains outside this package. | CONFIRMED release separation |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, limitations, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> Evidence projection is not evidence closure. A projected DTO or citation display remains downstream of EvidenceBundle, policy, cultural/steward review, sensitivity transform, and release state.

[⬆ Back to top](#top)

---

## 3. Evidence-projection boundary

Allowed direction:

```text
EvidenceRef / EvidenceBundleRef / review refs / policy refs / release refs
  -> evidence-projection helper
  -> safe citation, summary, catalog/triplet projection, or API-display payload
  -> governed API/release surface decides exposure where authorized
```

Blocked direction:

```text
evidence-projection helper
  -> EvidenceBundle creation
  -> confirmed archaeological site
  -> exact-location disclosure
  -> policy decision
  -> lifecycle write
  -> catalog/triplet authority
  -> release approval
```

Projection helpers should be deterministic, preserve all refs and caveats, and fail safe when evidence, review, policy, or release state is missing or inaccessible.

[⬆ Back to top](#top)

---

## 4. Sensitivity and publication boundary

Archaeology evidence projection has high exposure risk. This package must preserve these boundaries:

- exact locations are not public by default;
- evidence summaries must not leak restricted geometry, culturally sensitive context, collection-security detail, or looting-risk detail;
- candidate and anomaly evidence remains candidate unless confirmed through governed review and evidence;
- missing or inaccessible EvidenceBundle resolution should produce abstain/deny-safe outcomes, not fabricated summaries;
- public release requires redaction/generalization/sensitivity transforms outside this package;
- cultural review, steward review, ReleaseManifest, correction path, and rollback posture remain outside this package.

[⬆ Back to top](#top)

---

## 5. Anti-collapse rules

Disallowed collapses:

```text
projection -> proof
EvidenceRef -> EvidenceBundle closure
citation display -> source authority
summary DTO -> public release approval
redaction metadata -> sensitivity decision
catalog projection -> catalog truth
triplet projection -> graph truth
review ref -> review completion
release ref -> release approval
successful package test -> lifecycle promotion
```

Required separations:

- evidence-projection helper code stays under `packages/domains/archaeology/evidence-projection/`;
- EvidenceBundles stay under proof homes;
- Archaeology doctrine stays under `docs/domains/archaeology/`;
- object meaning stays under `contracts/domains/archaeology/`;
- schemas stay under `schemas/contracts/v1/domains/archaeology/`;
- policy and sensitivity rules stay under `policy/domains/archaeology/` and accepted policy roots;
- catalog/triplet records stay under data/catalog and data/triplets lifecycle homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 6. What belongs here

Appropriate source files include:

- EvidenceRef projection helper functions;
- citation display DTO helpers;
- evidence summary shape helpers that preserve limitations;
- source-role and confidence/caveat helpers;
- review-ref preservation helpers;
- sensitivity-transform reference helpers;
- safe redaction/generalization metadata helpers;
- catalog/triplet projection helper DTOs that do not write records;
- missing or inaccessible evidence outcome helpers;
- synthetic or sanitized fixture builders.

A good placement test:

> If the file is reusable projection support code that preserves evidence and governance refs and does not create proof, write lifecycle records, disclose sensitive locations, decide policy, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| EvidenceBundle storage or creation | `data/proofs/evidence_bundle/` and proof tooling |
| Archaeology doctrine and scope docs | `docs/domains/archaeology/` |
| Archaeology object contracts | `contracts/domains/archaeology/` |
| Archaeology schemas | `schemas/contracts/v1/domains/archaeology/` |
| Archaeology policy decisions/rules | `policy/domains/archaeology/` and accepted policy roots |
| Executable projection pipeline | `pipelines/domains/archaeology/` or accepted executable lane |
| Catalog/triplet records | `data/catalog/`, `data/triplets/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/published` |
| Review decisions | cultural/steward review authority roots |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| Public map/UI rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/archaeology/evidence-projection/` |
| Package fixtures | `fixtures/packages/domains/archaeology/evidence-projection/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 8. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `evidence_ref` | EvidenceRef and EvidenceBundleRef projection helpers. | PROPOSED |
| `citation` | Citation display DTO helpers. | PROPOSED |
| `summary` | Evidence summary helpers that preserve caveats and limitations. | PROPOSED |
| `review_refs` | Cultural/steward review reference preservation. | PROPOSED |
| `sensitivity` | Redaction/generalization/sensitivity-transform references, not policy decisions. | PROPOSED |
| `catalog_projection` | Catalog projection DTO helpers, not catalog writes. | PROPOSED |
| `triplet_projection` | Triplet projection DTO helpers, not graph truth. | PROPOSED |
| `outcomes` | Missing/inaccessible evidence abstain/deny-safe outcomes. | PROPOSED |
| `fixtures` | Synthetic/sanitized fixture builders. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/archaeology/evidence-projection/` | Shared projection helper code only. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Parent helper package | `packages/domains/archaeology/` | Domain helper parent. |
| Domain doctrine | `docs/domains/archaeology/` | Scope and sensitivity posture. |
| Domain contracts | `contracts/domains/archaeology/` | Meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/archaeology/` | Machine shape authority. |
| Domain policy | `policy/domains/archaeology/` | Admissibility/exposure authority. |
| Catalog/triplet records | `data/catalog/`, `data/triplets/` | Not written here as hidden behavior. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/archaeology/evidence-projection/` | Package validation. |
| Fixtures | `fixtures/packages/domains/archaeology/evidence-projection/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 10. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.archaeology.evidence_projection
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - evidence_bundle
  - archaeology_doctrine
  - site_confirmation
  - exact_location_release
  - policy_decision
  - lifecycle_write
  - catalog_truth
  - triplet_truth
  - release_decision
allowed_responsibilities:
  - EvidenceRef projection helpers
  - citation display DTO helpers
  - evidence summary helpers
  - review reference preservation
  - sensitivity transform reference helpers
  - catalog projection helper DTOs
  - triplet projection helper DTOs
  - safe outcome helpers
  - synthetic fixture builders
required_invariants:
  no_evidence_fabrication: true
  no_exact_location_publication: true
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_release_approval: true
  projection_output_is_not_proof: true
```

[⬆ Back to top](#top)

---

## 11. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/archaeology/evidence-projection/
├── test_evidence_projection_boundaries.py     # PROPOSED
├── test_projection_not_proof.py               # PROPOSED
├── test_evidenceref_not_bundle_closure.py     # PROPOSED
├── test_exact_location_not_public.py          # PROPOSED
├── test_missing_evidence_abstains.py          # PROPOSED
├── test_inaccessible_evidence_denies.py       # PROPOSED
├── test_review_ref_not_review_completion.py   # PROPOSED
├── test_catalog_projection_not_write.py       # PROPOSED
├── test_no_release_approval.py                # PROPOSED
└── test_root_boundary.py                      # PROPOSED
```

Fixtures should live in `fixtures/packages/domains/archaeology/evidence-projection/` unless a package-local convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not expose controlled archaeology locations, cultural context, collection-security detail, or other restricted material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the empty `packages/domains/archaeology/evidence-projection/README.md` file;
- identifies this path as shared evidence-projection helper-code space;
- keeps EvidenceBundle creation, doctrine, contracts, schemas, policy, lifecycle data, catalog/triplet records, review decisions, and release decisions in their authority roots;
- blocks projection helpers from becoming proof, site confirmation, exact-location disclosure, policy approval, lifecycle promotion, catalog/triplet truth, or release approval;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Archaeology sensitivity, cultural/steward review, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-ARCH-EP-001` | Which language/runtime owns `packages/domains/archaeology/evidence-projection/`? | UNKNOWN |
| `PKG-DOM-ARCH-EP-002` | Which EvidenceRef and EvidenceBundleRef shapes are canonical for Archaeology projection helpers? | NEEDS VERIFICATION |
| `PKG-DOM-ARCH-EP-003` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-ARCH-EP-004` | Which canonical schemas own citation, summary, review-ref, catalog projection, and triplet projection payloads? | NEEDS VERIFICATION |
| `PKG-DOM-ARCH-EP-005` | Which CI workflow validates projection-not-proof and exact-location-denial rules? | UNKNOWN |
| `PKG-DOM-ARCH-EP-006` | Should catalog/triplet projection helpers live here, in a catalog package, or in a governed API package? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this package helper-focused and subordinate to Archaeology evidence governance. Do not add EvidenceBundle writers, site-confirmation logic, exact-location publication, policy decisions, lifecycle writers, catalog/triplet writers, release decisions, public API routes, UI behavior, controlled-location examples, culturally sensitive examples, collection-security details, or generated truth claims here.

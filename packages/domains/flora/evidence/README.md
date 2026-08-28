<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-flora-evidence-readme
title: Flora Evidence Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <flora-domain-steward>
  - <schema-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-14
updated: 2026-06-14
policy_label: public
path: packages/domains/flora/evidence/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/flora/README.md
  - docs/domains/flora/README.md
  - pipelines/domains/flora/README.md
  - pipeline_specs/flora/README.md
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - tests/packages/domains/flora/evidence/
  - fixtures/packages/domains/flora/evidence/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, flora, evidence, evidence-ref, evidence-bundle, source-role, voucher, specimen, occurrence, governance]
notes:
  - "This README fills the empty flora evidence package file with a governed helper-package contract."
  - "evidence is a shared helper package for Flora evidence-reference support; it is not EvidenceBundle storage, evidence closure, proof authority, lifecycle authority, or release authority."
  - "Evidence helpers must preserve source roles, native identifiers, uncertainty, review refs, policy refs, and EvidenceRef links."
  - "When release or policy state is missing, helpers must return safe abstain or deny outcomes rather than substituting generated confidence."
  - "Concrete code exports, language runtime, package manifest, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Evidence Package

> Shared helper package for Flora evidence-reference support. It may normalize EvidenceRefs, preserve source-native support identifiers, prepare voucher/specimen support payloads, preserve caveats, and help build package fixtures. It must not create EvidenceBundles, decide proof closure, decide Flora truth, write lifecycle records, approve policy, or approve release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Fflora%2Fevidence%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20package-0a7ea4)
![evidence](https://img.shields.io/badge/evidence--ref-helper%20not%20proof-d62728)
![release](https://img.shields.io/badge/no%20release%20approval-d62728)

**Status:** Draft  
**Path:** `packages/domains/flora/evidence/README.md`  
**Parent package:** `packages/domains/flora/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/flora/`  
**Executable domain-pipeline root:** `pipelines/domains/flora/`  
**Declarative pipeline-spec root:** `pipeline_specs/flora/`  
**Contract/schema/policy roots:** `contracts/domains/flora/`, `schemas/contracts/v1/domains/flora/`, and `policy/domains/flora/`  
**Evidence proof root:** `data/proofs/evidence_bundle/`  
**Placement posture:** helper package for Flora EvidenceRef and support-metadata handling only. Runtime, exports, package manifest, active tests, and implementation are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Evidence helper boundary](#3-evidence-helper-boundary)
- [4. Policy and publication boundary](#4-policy-and-publication-boundary)
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

`packages/domains/flora/evidence/` may contain reusable helper code for Flora evidence references and support metadata without becoming an evidence authority root.

It may support:

- EvidenceRef parsing, formatting, and normalization helpers;
- source-native support identifier preservation helpers;
- voucher, specimen, collection, survey, plot, photo, observation, and vegetation-source support helpers;
- occurrence-support and specimen-support DTO adapters;
- source role, source time, valid time, limitation, caveat, uncertainty, access state, and review-ref preservation helpers;
- policy-ref, release-ref, and correction-ref preservation helpers;
- evidence-support completeness check helpers that do not close EvidenceBundles;
- schema-bound validation adapters and safe errors;
- no-network fixture builders for tests.

It does **not** create EvidenceBundles, decide proof closure, decide botanical truth, decide taxonomic authority, decide occurrence truth, decide policy, write lifecycle data, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/flora/`? | Evidence helpers are reusable Flora package code, not a proof or data root. | CONFIRMED parent root pattern / NEEDS VERIFICATION for implementation |
| Is this EvidenceBundle storage? | No. EvidenceBundles and proofs stay in proof homes such as `data/proofs/evidence_bundle/`. | CONFIRMED proof separation |
| Is this Flora doctrine? | No. Flora doctrine and scope belong under `docs/domains/flora/`. | CONFIRMED boundary posture |
| Can this decide proof closure? | No. It may validate reference shape and preserve support metadata only. | CONFIRMED evidence boundary |
| Can this decide policy, lifecycle, or release? | No. It may preserve refs, caveats, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> Evidence helper output is not proof. A normalized EvidenceRef, voucher reference, specimen reference, source-support payload, or completeness result remains downstream of EvidenceBundle creation, validation, review, policy, lifecycle, and release controls.

[⬆ Back to top](#top)

---

## 3. Evidence helper boundary

Allowed direction:

```text
source-native support id / EvidenceRef / voucher ref / specimen ref / review refs / policy refs
  -> flora evidence helper
  -> normalized reference payload, support metadata, caveat payload, or validation result
  -> governed proof/pipeline/review flow handles EvidenceBundle closure where authorized
```

Blocked direction:

```text
evidence helper
  -> EvidenceBundle creation
  -> proof closure
  -> botanical truth decision
  -> occurrence truth decision
  -> taxonomic authority decision
  -> lifecycle promotion
  -> policy approval
  -> release approval
```

Evidence helpers should be deterministic where practical, preserve source-native identifiers, and keep uncertainty, limitations, and caveats explicit. They should prefer review-ready support payloads over authoritative assertions.

[⬆ Back to top](#top)

---

## 4. Policy and publication boundary

This package must preserve these boundaries:

- helper output is not proof or release approval;
- normalized evidence-support payloads are not automatically releasable;
- policy and review refs must be preserved rather than discarded;
- missing or inaccessible EvidenceBundle, source support, review, policy, or release state should produce abstain/deny-safe outcomes, not fabricated evidence confidence;
- ReviewRecord, PolicyDecision, ReleaseManifest, correction path, and rollback posture remain outside this package.

[⬆ Back to top](#top)

---

## 5. Anti-collapse rules

Disallowed collapses:

```text
evidence helper -> EvidenceBundle authority
EvidenceRef normalizer -> EvidenceBundle closure
voucher reference -> specimen proof
specimen support -> occurrence truth
photo support -> botanical truth
completeness check -> validation pass
review ref -> review completion
policy ref -> policy approval
release ref -> release approval
successful package test -> lifecycle promotion
```

Required separations:

- evidence helper code stays under `packages/domains/flora/evidence/`;
- Flora doctrine stays under `docs/domains/flora/`;
- object meaning stays under `contracts/domains/flora/`;
- schemas stay under `schemas/contracts/v1/domains/flora/`;
- policy rules stay under `policy/domains/flora/`;
- lifecycle records and writes stay under governed data/pipeline roots;
- EvidenceBundles stay under `data/proofs/evidence_bundle/` and accepted proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 6. What belongs here

Appropriate source files include:

- EvidenceRef parsing and formatting helpers;
- source-native evidence id preservation helpers;
- voucher, specimen, collection, survey, plot, photo, and observation support reference helpers;
- occurrence-support and specimen-support DTO adapters;
- evidence-support completeness and shape-check helpers that do not close proof;
- review-ref, policy-ref, release-ref, correction-ref, and EvidenceRef preservation helpers;
- source-role, limitation, caveat, uncertainty, and access-state preservation helpers;
- schema-bound validation adapters and safe errors;
- synthetic or sanitized fixture builders.

A good placement test:

> If the file is reusable evidence-reference support code that preserves source/evidence/governance refs and does not create proof, decide truth, write lifecycle records, decide policy, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| EvidenceBundle storage or creation | `data/proofs/evidence_bundle/` and proof tooling |
| Validation reports and proof closure | validator/proof roots and accepted pipeline outputs |
| Flora doctrine and source scope docs | `docs/domains/flora/` |
| Flora object contracts | `contracts/domains/flora/` |
| Flora schemas | `schemas/contracts/v1/domains/flora/` |
| Flora policy decisions/rules | `policy/domains/flora/` |
| Executable evidence pipeline | `pipelines/domains/flora/` or accepted executable lane |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Review decisions | policy/review authority roots |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| Public map/UI rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/flora/evidence/` |
| Package fixtures | `fixtures/packages/domains/flora/evidence/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 8. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `evidence_ref` | EvidenceRef parsing, formatting, normalization, and echo helpers. | PROPOSED |
| `voucher` | Voucher/specimen/collection support reference helpers. | PROPOSED |
| `occurrence_support` | Occurrence evidence-support helper payloads. | PROPOSED |
| `source_support` | Source-native id, source-role, limitation, and caveat preservation. | PROPOSED |
| `review_refs` | Review, policy, release, correction, and rollback reference preservation. | PROPOSED |
| `completeness` | Completeness and shape-check helpers, not proof closure. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Synthetic/sanitized fixture builders. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/flora/evidence/` | Shared EvidenceRef/support helper code only. |
| Parent helper package | `packages/domains/flora/` | Domain helper parent. |
| Domain doctrine | `docs/domains/flora/` | Scope and sensitivity posture. |
| Domain contracts | `contracts/domains/flora/` | Meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/flora/` | Machine shape authority. |
| Domain policy | `policy/domains/flora/` | Admissibility authority. |
| Canonical lifecycle records | `data/<phase>/flora/` | Not written here as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/flora/evidence/` | Package validation. |
| Fixtures | `fixtures/packages/domains/flora/evidence/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 10. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.flora.evidence
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - evidence_bundle_creation
  - evidence_closure
  - occurrence_truth
  - specimen_truth
  - taxonomic_authority
  - flora_doctrine
  - policy_decision
  - lifecycle_write
  - release_decision
allowed_responsibilities:
  - EvidenceRef parsing and formatting
  - source-native support id preservation
  - voucher and specimen reference helpers
  - occurrence support payload helpers
  - review and policy reference preservation
  - completeness and shape-check helpers
  - schema-bound adapters
  - synthetic fixture builders
required_invariants:
  no_evidence_bundle_creation: true
  no_evidence_closure: true
  no_occurrence_truth_decision: true
  no_taxonomic_authority_decision: true
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_release_approval: true
  evidence_helper_output_is_not_proof: true
```

[⬆ Back to top](#top)

---

## 11. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/flora/evidence/
├── test_evidence_package_boundaries.py       # PROPOSED
├── test_evidence_ref_not_bundle_closure.py   # PROPOSED
├── test_voucher_ref_not_specimen_proof.py    # PROPOSED
├── test_occurrence_support_not_truth.py      # PROPOSED
├── test_completeness_not_validation_pass.py  # PROPOSED
├── test_no_hidden_lifecycle_writes.py        # PROPOSED
├── test_no_policy_or_release_decisions.py    # PROPOSED
├── test_no_evidence_fabrication.py           # PROPOSED
└── test_root_boundary.py                     # PROPOSED
```

Fixtures should live in `fixtures/packages/domains/flora/evidence/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the empty `packages/domains/flora/evidence/README.md` file;
- identifies this path as shared Flora evidence-reference helper-code space;
- keeps EvidenceBundles, proof closure, doctrine, contracts, schemas, policy, lifecycle data, review decisions, and release decisions in their authority roots;
- blocks evidence helpers from becoming proof, evidence closure, occurrence truth, policy approval, lifecycle promotion, EvidenceBundle creation, or release approval;
- defines expected helper families, policy posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Flora lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FLORA-EVD-001` | Which language/runtime owns `packages/domains/flora/evidence/`? | UNKNOWN |
| `PKG-DOM-FLORA-EVD-002` | Which canonical schema owns EvidenceRef payloads, voucher refs, occurrence-support refs, and support completeness checks? | NEEDS VERIFICATION |
| `PKG-DOM-FLORA-EVD-003` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-FLORA-EVD-004` | Which CI workflow validates evidence-helper-not-proof and no hidden lifecycle writes? | UNKNOWN |
| `PKG-DOM-FLORA-EVD-005` | Should proof-readiness checks live here, in validators, or in an executable pipeline lane? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-FLORA-EVD-006` | Which evidence-support vocabulary is canonical versus source-specific crosswalk input? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package helper-focused and subordinate to Flora evidence governance. Do not add EvidenceBundle writers, proof closure, validation pass decisions, occurrence truth decisions, taxonomic authority decisions, policy decisions, lifecycle writers, release decisions, public API routes, UI behavior, or generated truth claims here.

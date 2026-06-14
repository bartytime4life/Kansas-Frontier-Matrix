<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-citation-src-citation-readme
title: Citation Package Source Citation Module README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <citation-steward>
  - <evidence-steward>
  - <schema-steward>
  - <api-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/citation/src/citation/README.md
related:
  - packages/README.md
  - packages/citation/README.md
  - packages/api/README.md
  - docs/architecture/governed-api.md
  - data/proofs/evidence_bundle/
  - data/receipts/pipeline/
  - data/catalog/
  - release/manifests/
  - contracts/
  - schemas/contracts/v1/
  - policy/
  - tests/packages/citation/
  - fixtures/packages/citation/
tags: [kfm, packages, citation, src, citation-module, evidenceref, evidencebundle-ref, source-ref, receipt-ref, release-ref, limitations, validation, governance]
notes:
  - "This README fills the empty packages/citation/src/citation README with a governed source-module contract."
  - "packages/citation/src/citation/ may contain internal source code for shared citation helpers only; it must remain subordinate to packages/citation/."
  - "Citation module code may validate and preserve reference shapes. It cannot create EvidenceBundles, admit sources, decide policy, approve release, or make claims true."
  - "Concrete language runtime, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Citation Source Module

> Internal source-code module area for the `packages/citation/` shared library. This directory may hold reusable citation and reference helpers, but it must not become an EvidenceBundle store, source-admission tool, lifecycle writer, policy engine, release authority, or public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fcitation%2Fsrc%2Fcitation%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20module-0a7ea4)
![evidence](https://img.shields.io/badge/citation-pointer%20not%20proof-d62728)
![membrane](https://img.shields.io/badge/public%20path-governed%20API-d62728)

**Status:** Draft  
**Path:** `packages/citation/src/citation/README.md`  
**Parent package:** `packages/citation/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Evidence authority:** `data/proofs/evidence_bundle/` and accepted proof homes  
**Release authority:** `release/`  
**Public trust membrane:** `apps/governed-api/`  
**Placement posture:** source code for reusable citation helpers only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Module boundary](#3-module-boundary)
- [4. Anti-collapse rules](#4-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Expected module families](#7-expected-module-families)
- [8. Inputs and outputs](#8-inputs-and-outputs)
- [9. Minimal module contract shape](#9-minimal-module-contract-shape)
- [10. Tests and fixtures](#10-tests-and-fixtures)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`packages/citation/src/citation/` may hold internal source modules for the `packages/citation/` shared citation support library.

It may support reusable helpers for:

- Citation object normalization;
- EvidenceRef shape checks;
- EvidenceBundleRef preservation;
- SourceDescriptorRef preservation;
- RunReceiptRef preservation;
- PolicyDecisionRef, ReleaseManifestRef, CorrectionNoticeRef, and RollbackCardRef preservation;
- line, page, fragment, and anchor helpers;
- limitation, caveat, redaction, access-state, and source-role display helpers;
- safe missing-citation and inaccessible-evidence error helpers;
- no-network fixture builders for package tests.

It does **not** create EvidenceBundles, decide whether a claim is true, approve source admission, decide policy, approve release, or provide a public API surface.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/citation/`? | Parent package is the shared citation and EvidenceRef helper library. | CONFIRMED parent package contract |
| Why `src/citation/`? | This is a plausible internal module path for citation-specific package source. | PROPOSED / NEEDS VERIFICATION |
| Is this evidence storage? | No. EvidenceBundles belong under proof/data homes. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume schema/contract outputs, but authority stays in `schemas/` and `contracts/`. | CONFIRMED authority separation |
| Can this decide policy or release? | No. It may preserve refs and validation results only. | CONFIRMED policy/release separation |
| Can this be called directly by public clients as the trust membrane? | No. Public/client-facing behavior must go through governed API envelopes. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> Source modules here can help normalize, validate, and preserve citation-shaped references. They cannot turn references into proof, policy approval, release approval, or public truth.

[⬆ Back to top](#top)

---

## 3. Module boundary

Allowed direction:

```text
API / UI / pipeline / validator / test
  -> packages/citation/src/citation helper
  -> validated citation or reference shape
  -> governed API envelope, catalog record, report, or test fixture preserves the refs
```

Blocked direction:

```text
packages/citation/src/citation helper
  -> EvidenceBundle creation by reference alone
  -> source admission
  -> lifecycle write
  -> policy decision
  -> release approval
  -> generated claim becomes confirmed truth
```

The module should be pure or side-effect-minimal where practical. Any future IO capability requires explicit ownership, tests, receipts, and steward review.

[⬆ Back to top](#top)

---

## 4. Anti-collapse rules

Disallowed collapses:

```text
source module -> evidence authority
citation helper -> EvidenceBundle closure
EvidenceRef helper -> proof of truth
source reference -> source admission
line/page anchor -> full source context
citation display -> policy approval
citation display -> release approval
mock citation -> production evidence
successful module test -> claim validation
citation count -> confidence score
```

Required separations:

- reusable helper source stays under `packages/citation/src/citation/`;
- EvidenceBundles stay under proof/data homes;
- source descriptors stay under source registry homes;
- receipts stay under receipt homes;
- catalog records stay under catalog lifecycle homes;
- schemas and contracts stay under their authority roots;
- policy and release decisions stay under their authority roots;
- public clients consume governed API envelopes and released artifacts, not package internals.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source modules include helpers for:

- citation object construction from already-authorized inputs;
- citation normalization and validation;
- EvidenceRef and EvidenceBundleRef preservation;
- source, receipt, policy, release, correction, and rollback ref preservation;
- line/page/fragment/anchor normalization;
- limitation and caveat preservation;
- redaction/generalization and access-state labels;
- deterministic citation ids or digests;
- safe validation errors;
- package-only fixture builders.

A good placement test:

> If the module is reusable citation/reference helper code and does not create evidence, decide policy, change lifecycle state, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| EvidenceBundle storage or creation | `data/proofs/evidence_bundle/` and proof tooling |
| Source admission logic | source registry/admission workflow homes |
| Source descriptors | `data/registry/sources/` |
| Runtime receipts | `data/receipts/pipeline/` |
| Catalog records | `data/catalog/` |
| Triplet records | `data/triplets/` |
| Canonical schemas | `schemas/contracts/v1/` |
| Object contracts | `contracts/` |
| Policy decisions and rules | `policy/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| UI-only rendering components | `apps/explorer-web/` or accepted UI package roots |
| Executable pipeline code | `pipelines/` |
| Tests | `tests/packages/citation/` |
| Fixtures | `fixtures/packages/citation/` unless package-local convention is ADR-approved |

[⬆ Back to top](#top)

---

## 7. Expected module families

| Module family | Responsibility | Status |
|---|---|---|
| `citation` | Citation object helpers, normalization, and display payload shape. | PROPOSED |
| `evidence_ref` | EvidenceRef and EvidenceBundleRef reference helpers. | PROPOSED |
| `source_ref` | SourceDescriptorRef and source-role reference helpers. | PROPOSED |
| `receipt_ref` | RunReceiptRef and validation receipt ref helpers. | PROPOSED |
| `release_ref` | ReleaseManifestRef, CorrectionNoticeRef, and RollbackCardRef helpers. | PROPOSED |
| `limitations` | Caveat, limitation, redaction, generalization, and access-state helpers. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Package-only fixture builders, if accepted by package convention. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Module source | `packages/citation/src/citation/` | Shared helper source only. |
| Package entrypoint | `packages/citation/` | Language-specific entrypoint is not verified. |
| API envelope consumer | `apps/governed-api/`, `packages/api/` | Public/client-facing finite outcomes. |
| Evidence refs | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Source refs | `data/registry/sources/` | Referenced, not admitted. |
| Receipt refs | `data/receipts/pipeline/` | Referenced, not emitted. |
| Catalog records | `data/catalog/` | May preserve citations; module does not store records. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/citation/` | Package validation. |
| Fixtures | `fixtures/packages/citation/` | No-network package fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal module contract shape

```yaml
module_id: kfm.packages.citation.src.citation
status: draft
authority: package_source_module
not_authority_for:
  - evidence_bundle
  - source_admission
  - lifecycle_write
  - schema_home
  - contract_home
  - policy_decision
  - release_decision
allowed_responsibilities:
  - citation helpers
  - reference preservation helpers
  - limitation and caveat helpers
  - safe validation adapters
  - safe fixture builders
required_invariants:
  no_evidence_fabrication: true
  no_policy_bypass: true
  no_release_approval: true
  no_source_admission: true
  citation_pointer_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 10. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/citation/
├── test_citation_module_boundaries.py       # PROPOSED
├── test_citation_shape.py                   # PROPOSED
├── test_evidence_refs_preserved.py          # PROPOSED
├── test_source_refs_preserved.py            # PROPOSED
├── test_receipt_and_release_refs_preserved.py # PROPOSED
├── test_missing_citation_abstain_path.py    # PROPOSED
├── test_inaccessible_evidence_deny_path.py  # PROPOSED
├── test_no_evidence_fabrication.py          # PROPOSED
├── test_no_policy_or_release_decisions.py   # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

Fixture material should live in `fixtures/packages/citation/` unless a package-local fixture convention is explicitly accepted. Fixtures must not be mistaken for production evidence or production citations.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/citation/src/citation/README.md` file;
- identifies this directory as package source for shared citation helpers;
- keeps EvidenceBundles, receipts, source descriptors, policy decisions, release decisions, and public API behavior in their own authority roots;
- blocks helper modules from becoming EvidenceBundle creators, source-admission tools, lifecycle writers, policy engines, release approvers, schema authority, contract authority, or public trust membrane;
- defines expected module families, inputs/outputs, tests, fixtures, and open questions.

Future source files in this module are done only when they are schema-aligned, test-covered, deterministic where practical, and unable to bypass evidence, policy, release, and trust-membrane controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-CITATION-SRC-001` | Which language/runtime owns `packages/citation/src/citation/`? | UNKNOWN |
| `PKG-CITATION-SRC-002` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-CITATION-SRC-003` | Should fixture builders live in source, tests, or `fixtures/packages/citation/` only? | NEEDS VERIFICATION |
| `PKG-CITATION-SRC-004` | Which canonical schema owns Citation, EvidenceRef, and EvidenceBundleRef shapes? | NEEDS VERIFICATION |
| `PKG-CITATION-SRC-005` | Which CI workflow verifies helper determinism and no evidence/policy/release bypass? | UNKNOWN |
| `PKG-CITATION-SRC-006` | Should citation display helpers live here, in `packages/api/`, or in UI-specific packages? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this module small, deterministic, and subordinate to evidence and release governance. Do not add EvidenceBundle writers, source admission logic, lifecycle writers, schema authority, contract authority, policy decisions, release decisions, public API routes, UI-only rendering components, or generated truth claims here.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-citation-src-readme
title: Citation Package Source README
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
path: packages/citation/src/README.md
related:
  - packages/README.md
  - packages/citation/README.md
  - packages/citation/src/citation/README.md
  - packages/api/README.md
  - docs/architecture/governed-api.md
  - data/proofs/evidence_bundle/
  - data/receipts/pipeline/
  - data/catalog/
  - data/triplets/
  - release/manifests/
  - contracts/
  - schemas/contracts/v1/
  - policy/
  - tests/packages/citation/
  - fixtures/packages/citation/
tags: [kfm, packages, citation, src, shared-library, source-root, evidenceref, evidencebundle-ref, source-ref, receipt-ref, release-ref, limitations, validation, governance]
notes:
  - "This README fills the empty packages/citation/src README with a governed source-root contract."
  - "packages/citation/src/ may contain source code for the shared citation support package only; it must remain subordinate to packages/citation/."
  - "Citation source code may validate, normalize, and preserve reference shapes. It cannot create EvidenceBundles, admit sources, decide policy, approve release, or make claims true."
  - "packages/citation/src/citation/ is the citation-helper module lane for reusable citation/reference helpers."
  - "Concrete language runtime, package manifests, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Citation Package Source Root

> Source root for the `packages/citation/` shared citation support library. Code here may provide reusable citation helpers, reference validators, limitation preservation, safe error helpers, and internal module wiring, but it must not create EvidenceBundles, admit sources, write lifecycle records as hidden side effects, decide policy, approve release, or become a public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fcitation%2Fsrc%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20root-0a7ea4)
![evidence](https://img.shields.io/badge/citation-pointer%20not%20proof-d62728)
![membrane](https://img.shields.io/badge/public%20path-governed%20API-d62728)

**Status:** Draft  
**Path:** `packages/citation/src/README.md`  
**Parent package:** `packages/citation/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Citation helper module:** `packages/citation/src/citation/`  
**Evidence authority:** `data/proofs/evidence_bundle/` and accepted proof homes  
**Release authority:** `release/`  
**Public trust membrane:** `apps/governed-api/`  
**Placement posture:** source root for shared citation package code only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Source-root boundary](#3-source-root-boundary)
- [4. Anti-collapse rules](#4-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Expected module layout](#7-expected-module-layout)
- [8. Inputs and outputs](#8-inputs-and-outputs)
- [9. Minimal source-root contract shape](#9-minimal-source-root-contract-shape)
- [10. Tests and fixtures](#10-tests-and-fixtures)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`packages/citation/src/` may contain source code for the `packages/citation/` shared library.

It may include internal modules for:

- citation object helpers;
- EvidenceRef and EvidenceBundleRef helpers;
- SourceDescriptorRef helpers;
- RunReceiptRef helpers;
- ReleaseManifestRef, CorrectionNoticeRef, and RollbackCardRef helpers;
- line, page, fragment, anchor, and excerpt-boundary helpers;
- limitation, caveat, redaction, generalization, and access-state helpers;
- deterministic citation ids or digests;
- safe missing-citation and inaccessible-evidence errors;
- package entrypoints and internal exports.

It does **not** create EvidenceBundles, approve source admission, own lifecycle data, decide policy, approve release, or provide the public API trust membrane.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/citation/`? | Parent package is the shared citation and EvidenceRef helper library. | CONFIRMED parent package contract |
| Why `src/`? | This is a conventional source root for package implementation, but language/runtime are not yet verified. | PROPOSED / NEEDS VERIFICATION |
| Is this evidence storage? | No. EvidenceBundles belong under proof/data homes. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume schema/contract outputs, but authority stays in `schemas/` and `contracts/`. | CONFIRMED authority separation |
| Can this decide policy or release? | No. It may preserve refs and validation results only. | CONFIRMED policy/release separation |
| Can this be called directly by public clients as the trust membrane? | No. Public/client-facing behavior must go through governed API envelopes. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> Source code under this root can normalize, validate, preserve, and render citation-shaped references. It cannot turn references into proof, policy approval, release approval, or public truth.

[⬆ Back to top](#top)

---

## 3. Source-root boundary

Allowed direction:

```text
API / UI / pipeline / validator / test
  -> packages/citation/src module
  -> validated citation or reference shape
  -> governed API envelope, catalog record, report, or test fixture preserves the refs
```

Blocked direction:

```text
packages/citation/src module
  -> EvidenceBundle creation by reference alone
  -> source admission
  -> lifecycle write
  -> policy decision
  -> release approval
  -> generated claim becomes confirmed truth
```

The source root should favor pure, deterministic helpers. Any future IO capability must be explicit, reviewed, tested, receipt-producing, and owned by an executable pipeline, governed API, or approved tool lane.

[⬆ Back to top](#top)

---

## 4. Anti-collapse rules

Disallowed collapses:

```text
source root -> evidence authority
source module -> public trust membrane
citation helper -> EvidenceBundle closure
EvidenceRef helper -> proof of truth
source reference -> source admission
line/page anchor -> full source context
citation display -> policy approval
citation display -> release approval
mock citation -> production evidence
successful source-root test -> claim validation
citation count -> confidence score
```

Required separations:

- reusable source code stays under `packages/citation/src/`;
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

Appropriate source files include:

- package entrypoints and internal exports;
- citation object construction helpers;
- citation normalization and validation helpers;
- EvidenceRef and EvidenceBundleRef helpers;
- source, receipt, policy, release, correction, and rollback ref helpers;
- line/page/fragment/anchor helpers;
- limitation and caveat helpers;
- redaction/generalization and access-state label helpers;
- deterministic citation id or digest helpers;
- safe validation error helpers;
- package-local types generated from canonical schemas when generation provenance is recorded.

A good placement test:

> If the file is package source for reusable citation/reference support and does not create evidence, decide policy, change lifecycle state, or approve release, it may belong here.

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
| Declarative pipeline specs | `pipeline_specs/` |
| Package tests | `tests/packages/citation/` |
| Package fixtures | `fixtures/packages/citation/` unless package-local convention is ADR-approved |

[⬆ Back to top](#top)

---

## 7. Expected module layout

Current verified child module:

```text
packages/citation/src/
├── README.md
└── citation/
    └── README.md
```

Potential future layout:

```text
packages/citation/src/
├── index.*                    # PROPOSED
├── citation/
│   ├── citation.*             # PROPOSED
│   ├── evidence_ref.*         # PROPOSED
│   ├── source_ref.*           # PROPOSED
│   ├── receipt_ref.*          # PROPOSED
│   ├── release_ref.*          # PROPOSED
│   ├── limitations.*          # PROPOSED
│   └── validation.*           # PROPOSED
└── generated/                 # PROPOSED, only if generated from canonical schemas
```

Do not add parallel language layouts or generated output folders without package manifest evidence, generation provenance, tests, and a migration note.

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Source root | `packages/citation/src/` | Shared helper source only. |
| Citation helper module | `packages/citation/src/citation/` | Citation-specific helper module. |
| Package entrypoint | `packages/citation/` | Language-specific entrypoint is not verified. |
| API envelope consumer | `apps/governed-api/`, `packages/api/` | Public/client-facing finite outcomes. |
| Evidence refs | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Source refs | `data/registry/sources/` | Referenced, not admitted. |
| Receipt refs | `data/receipts/pipeline/` | Referenced, not emitted. |
| Catalog records | `data/catalog/` | May preserve citations; source root does not store records. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/citation/` | Package validation. |
| Fixtures | `fixtures/packages/citation/` | No-network package fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal source-root contract shape

```yaml
source_root_id: kfm.packages.citation.src
status: draft
authority: package_source_root
not_authority_for:
  - evidence_bundle
  - source_admission
  - lifecycle_write
  - schema_home
  - contract_home
  - policy_decision
  - release_decision
allowed_responsibilities:
  - package entrypoints
  - internal modules
  - citation helpers
  - reference preservation helpers
  - limitation and caveat helpers
  - safe validation adapters
  - deterministic id helpers
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
├── test_src_root_boundaries.py              # PROPOSED
├── test_citation_module_boundaries.py       # PROPOSED
├── test_exports_do_not_create_evidence.py   # PROPOSED
├── test_evidence_refs_preserved.py          # PROPOSED
├── test_source_refs_preserved.py            # PROPOSED
├── test_missing_citation_abstain_path.py    # PROPOSED
├── test_inaccessible_evidence_deny_path.py  # PROPOSED
├── test_no_policy_or_release_decisions.py   # PROPOSED
├── test_safe_validation_errors.py           # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

Fixture material should live in `fixtures/packages/citation/` unless a package-local fixture convention is explicitly accepted. Fixtures must not be mistaken for production evidence or production citations.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/citation/src/README.md` file;
- identifies this directory as the source root for shared citation package code;
- keeps EvidenceBundles, receipts, source descriptors, policy decisions, release decisions, and public API behavior in their own authority roots;
- blocks source modules from becoming EvidenceBundle creators, source-admission tools, lifecycle writers, policy engines, release approvers, schema authority, contract authority, or public trust membrane;
- defines expected module layout, inputs/outputs, tests, fixtures, and open questions.

Future source files under this root are done only when they are schema-aligned, test-covered, deterministic where practical, and unable to bypass evidence, policy, release, and trust-membrane controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-CITATION-SRC-ROOT-001` | Which language/runtime owns `packages/citation/src/`? | UNKNOWN |
| `PKG-CITATION-SRC-ROOT-002` | Which package manifest controls this source root? | UNKNOWN |
| `PKG-CITATION-SRC-ROOT-003` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-CITATION-SRC-ROOT-004` | Should generated types live under this source root, under `generated/`, or under a separate generated-code root? | NEEDS VERIFICATION / ADR |
| `PKG-CITATION-SRC-ROOT-005` | Which CI workflow verifies helper determinism and no evidence/policy/release bypass? | UNKNOWN |
| `PKG-CITATION-SRC-ROOT-006` | Should citation display helpers live here, in `packages/api/`, or in UI-specific packages? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this source root small, deterministic, and subordinate to evidence and release governance. Do not add EvidenceBundle writers, source admission logic, lifecycle writers, schema authority, contract authority, policy decisions, release decisions, public API routes, UI-only rendering components, or generated truth claims here.

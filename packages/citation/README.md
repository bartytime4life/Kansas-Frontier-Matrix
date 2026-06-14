<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-citation-readme
title: Citation Package README
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
path: packages/citation/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/governed-api.md
  - packages/README.md
  - packages/api/README.md
  - data/proofs/evidence_bundle/
  - data/receipts/pipeline/
  - data/catalog/
  - release/manifests/
  - contracts/
  - schemas/contracts/v1/
  - policy/
  - tests/packages/citation/
  - fixtures/packages/citation/
tags: [kfm, packages, citation, evidenceref, evidencebundle, citation-validation, reference-resolution, limitations, source-refs, governed-api, trust-membrane, governance]
notes:
  - "This README expands the packages/citation stub into a governed shared-package contract."
  - "packages/ contains shared libraries; packages/citation/ may contain reusable citation validation and EvidenceRef-resolution helpers only when subordinate to evidence, schema, contract, policy, lifecycle, and release roots."
  - "Citation helpers can check reference shape, preserve source/evidence/release refs, and build safe display payloads. They cannot create EvidenceBundles or make claims true."
  - "A citation is a pointer to evidence or source context, not proof by itself, not source admission, not policy approval, and not release approval."
  - "Concrete implementation, package exports, build scripts, validators, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Citation Package

> Shared library package for KFM citation support: citation validation, EvidenceRef resolution helpers, source/ref display helpers, limitation preservation, and safe reference utilities. EvidenceBundle storage remains under proof/data homes; policy and release decisions remain under their authority roots; public clients consume citations through governed API envelopes.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20library-0a7ea4)
![evidence](https://img.shields.io/badge/citation-pointer%20not%20proof-d62728)
![membrane](https://img.shields.io/badge/public%20path-governed%20API-d62728)

**Status:** Draft  
**Path:** `packages/citation/README.md`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Companion API package:** `packages/api/` — may carry citation/evidence-ref display helpers for governed envelopes  
**Evidence authority:** `data/proofs/evidence_bundle/` and accepted proof homes  
**Release authority:** `release/`  
**Placement posture:** `packages/citation/` may host reusable citation support code only when it remains deterministic, schema-aligned, and subordinate to evidence, policy, lifecycle, and release authority.  
**Public posture:** no independent public API, no EvidenceBundle fabrication, no source admission, no policy decision, no release approval, and no direct public-client trust membrane.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Citation responsibility boundary](#3-citation-responsibility-boundary)
- [4. Package anti-collapse rules](#4-package-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Package scope](#7-package-scope)
- [8. EvidenceRef and EvidenceBundle posture](#8-evidenceref-and-evidencebundle-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal package contract shape](#12-minimal-package-contract-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`packages/citation/` is a shared-library lane for citation and evidence-reference support code that can be reused by KFM applications, API helpers, pipelines, validators, tests, and documentation checks.

It may support:

- citation object validation;
- EvidenceRef shape helpers;
- EvidenceBundle reference resolution helpers;
- source descriptor reference helpers;
- line/page/fragment/anchor helper utilities;
- source role, claim scope, and limitation display helpers;
- safe citation rendering helpers for governed API envelopes;
- no-network fixture builders for citation tests;
- compatibility helpers for citation shape migrations.

It does **not** create EvidenceBundles, decide whether a claim is true, approve source admission, decide policy, or approve release.

Short rule:

```text
packages/citation/       = shared citation and EvidenceRef helper library
data/proofs/evidence_bundle/ = evidence proof home
schemas/                 = machine shape
contracts/               = object meaning
policy/                  = admissibility and exposure decisions
release/                 = release decisions and release control
apps/governed-api/       = public trust membrane
```

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/`? | This root owns shared libraries used by apps, workers, pipelines, and tools. | CONFIRMED root contract |
| Why `citation/` under packages? | Reusable citation helpers can support API, UI, tests, and pipeline validation without becoming proof or policy authority. | PROPOSED / NEEDS VERIFICATION |
| Is this an EvidenceBundle store? | No. EvidenceBundles belong under proof/data homes. | CONFIRMED boundary posture |
| Can this package define citation schema? | No. It may consume or mirror generated types, but schema authority lives under `schemas/`. | CONFIRMED authority separation |
| Can this package make policy or release decisions? | No. It may preserve refs and reason codes only. | CONFIRMED policy/release separation |
| Can public clients call this package as a trust membrane? | No. Public clients consume governed API envelopes, not package internals. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> A citation helper can validate and preserve a reference. It cannot make an uncited claim cited, turn a citation into evidence closure, or make a restricted claim publishable.

[⬆ Back to top](#top)

---

## 3. Citation responsibility boundary

KFM citations are traceability carriers. They point to evidence, source, receipt, catalog, or release context so users and systems can inspect claims. They are not sovereign truth.

Allowed direction:

```text
claim candidate + source refs + EvidenceRef refs + limitations
  -> packages/citation helper
  -> validated citation/reference shape
  -> governed API envelope or catalog record preserves the refs
  -> user can inspect evidence where authorized
```

Blocked direction:

```text
packages/citation helper
  -> EvidenceBundle creation by reference alone
  -> source admission
  -> policy decision
  -> release approval
  -> public display permission
  -> generated claim becomes confirmed truth
```

This package can make cite-or-abstain easier to implement. It cannot replace the evidence, review, policy, or release gates that make a response admissible.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
shared package -> evidence authority
citation helper -> EvidenceBundle closure
EvidenceRef helper -> proof of truth
source reference -> source admission
line/page anchor -> full source context
citation display -> policy approval
citation display -> release approval
mock citation -> production evidence
successful package test -> claim validation
citation count -> confidence score
```

Required separations:

- shared package code stays in `packages/citation/`;
- EvidenceBundles stay under proof/data homes;
- source descriptors stay in source registry homes;
- receipts stay under receipt homes;
- catalog records stay under catalog lifecycle homes;
- schemas stay in `schemas/`;
- contracts stay in `contracts/`;
- policy decisions stay in `policy/`;
- release decisions stay under `release/`;
- public clients consume governed API envelopes and released artifacts, not package-internal shortcuts.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include:

- citation validation helpers;
- EvidenceRef and EvidenceBundleRef helpers;
- source descriptor reference helpers;
- receipt reference helpers;
- release, correction, and rollback reference helpers;
- citation display models for governed envelopes;
- limitation and caveat preservation helpers;
- safe redaction/generalization labels associated with citations;
- deterministic citation key or digest helpers;
- schema-bound validators and validation adapters;
- fixture builders for no-network citation tests;
- compatibility helpers for citation-shape migrations.

A good placement test:

> If the file is reusable citation/reference support code that preserves traceability without creating evidence, deciding policy, or approving release, it may belong here. If it writes evidence, changes lifecycle state, or decides publication, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Runtime receipts | `data/receipts/pipeline/` |
| Source descriptors | `data/registry/sources/` |
| Catalog records | `data/catalog/` |
| Triplet records | `data/triplets/` |
| Canonical schemas | `schemas/contracts/v1/` |
| Object contracts | `contracts/` |
| Policy decisions and rules | `policy/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| Public UI rendering surfaces | `apps/explorer-web/` or accepted UI package roots |
| Executable pipeline code | `pipelines/` |
| Declarative pipeline specs | `pipeline_specs/` |
| Package tests | `tests/packages/citation/` |
| Package fixtures | `fixtures/packages/citation/` |

[⬆ Back to top](#top)

---

## 7. Package scope

`packages/citation/` may support citation-facing concerns such as:

- reference normalization;
- reference target shape checks;
- citation display DTO helpers;
- source role and authority label preservation;
- evidence limitation preservation;
- citation sorting and grouping helpers;
- deterministic ids for citation entries;
- safe missing-citation errors;
- abstain/deny helper reasons for uncited or inaccessible evidence;
- no-network fixture builders.

Implementation status for concrete modules, exports, package manager configuration, build steps, and CI remains `NEEDS VERIFICATION` unless backed by current repo evidence.

[⬆ Back to top](#top)

---

## 8. EvidenceRef and EvidenceBundle posture

| Term | Package posture | Must not collapse into |
|---|---|---|
| `Citation` | Display/reference carrier for a claim or response. | Evidence closure, policy approval, release approval. |
| `EvidenceRef` | Stable reference to evidence/proof context. | The EvidenceBundle itself. |
| `EvidenceBundleRef` | Pointer to proof package where evidence can be inspected if authorized. | Automatic truth or public display permission. |
| `SourceDescriptorRef` | Pointer to source metadata and source role. | Source admission or source authority by itself. |
| `RunReceiptRef` | Pointer to execution receipt. | Validation pass or release approval. |
| `ReleaseManifestRef` | Pointer to release decision context. | The decision itself unless resolved by release authority. |

Package helpers must preserve refs and limitations exactly. They must not silently drop inaccessible refs, turn missing refs into successful citations, or convert generated text into sourced truth.

[⬆ Back to top](#top)

---

## 9. Required gates

Before this package can be used by production callers, it should have:

1. **Schema gate** — generated or hand-written types reconciled with canonical schemas.
2. **Reference gate** — EvidenceRef, SourceDescriptorRef, RunReceiptRef, PolicyDecisionRef, ReleaseManifestRef, CorrectionNoticeRef, and RollbackCardRef shapes preserved.
3. **Limitations gate** — limitations, caveats, redaction/generalization state, and access state preserved.
4. **No-fabrication gate** — no helper can create proof by reference text alone.
5. **No-policy gate** — no helper can decide admissibility or sensitivity outcome.
6. **No-release gate** — no helper can decide publication or release state.
7. **Trust-membrane gate** — public/client-facing use happens through governed API envelopes.
8. **Error-safety gate** — safe missing-citation and inaccessible-evidence outcomes.
9. **Fixture gate** — no-network tests for citation/reference handling.
10. **Review gate** — citation, evidence, schema, and API steward review for trust-bearing changes.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
packages/citation/
├── README.md
├── package.json                 # NEEDS VERIFICATION / PROPOSED if JS package
├── pyproject.toml               # NEEDS VERIFICATION / PROPOSED if Python package
├── src/                         # PROPOSED
│   ├── index.*                  # PROPOSED
│   ├── citation.*               # PROPOSED
│   ├── evidence_ref.*           # PROPOSED
│   ├── source_ref.*             # PROPOSED
│   ├── receipt_ref.*            # PROPOSED
│   ├── release_ref.*            # PROPOSED
│   ├── limitations.*            # PROPOSED
│   └── validation.*             # PROPOSED
├── generated/                   # PROPOSED, only if generated from canonical schemas
└── README.md
```

The specific language/runtime is `UNKNOWN` from current evidence. Do not add parallel JS/Python package layouts without an implementation decision, package manifest, tests, and migration note.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/citation/` | Shared library only. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced; not created here. |
| Source descriptor | `data/registry/sources/` | Referenced; not admitted here. |
| Receipts | `data/receipts/pipeline/` | Referenced; not emitted here. |
| Catalog record | `data/catalog/` | May preserve citations; package does not store records. |
| API envelope | `apps/governed-api/` and `packages/api/` helpers | Public/client-facing finite outcomes. |
| Canonical schemas | `schemas/contracts/v1/` | Shape authority. |
| Object contracts | `contracts/` | Meaning authority. |
| Policy refs | `policy/` outputs/refs | Do not decide policy here. |
| Release refs | `release/` refs | Do not approve release here. |
| Tests | `tests/packages/citation/` | Package validation. |
| Fixtures | `fixtures/packages/citation/` | No-network package fixtures. |

[⬆ Back to top](#top)

---

## 12. Minimal package contract shape

```yaml
package_id: kfm.packages.citation
status: draft
authority: shared_library
not_authority_for:
  - evidence_bundle
  - source_admission
  - lifecycle_write
  - schema_home
  - contract_home
  - policy_decision
  - release_decision
allowed_exports:
  - Citation helpers
  - EvidenceRef helpers
  - EvidenceBundleRef helpers
  - SourceDescriptorRef helpers
  - RunReceiptRef helpers
  - limitation and caveat helpers
  - validation adapters
required_invariants:
  no_evidence_fabrication: true
  no_policy_bypass: true
  no_release_approval: true
  no_source_admission: true
  citation_pointer_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/packages/citation/
├── test_citation_shape.py                   # PROPOSED
├── test_evidence_refs_preserved.py          # PROPOSED
├── test_source_refs_preserved.py            # PROPOSED
├── test_receipt_and_release_refs_preserved.py # PROPOSED
├── test_missing_citation_abstain_path.py    # PROPOSED
├── test_inaccessible_evidence_deny_path.py  # PROPOSED
├── test_no_evidence_fabrication.py          # PROPOSED
├── test_no_policy_or_release_decisions.py   # PROPOSED
├── test_generated_types_match_schema.py     # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

A package change is not ready for production use until it has tests, fixtures, schema alignment, steward review, and proof that it cannot replace evidence closure, policy decisions, release decisions, or governed API finite outcomes.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- expands the short `packages/citation/README.md` stub;
- identifies `packages/citation/` as shared citation/EvidenceRef support, not proof authority;
- preserves EvidenceBundle, source registry, receipt, schema, contract, policy, release, and governed API boundaries;
- blocks the package from becoming source admission, lifecycle storage, EvidenceBundle closure, policy approval, release approval, or public truth authority;
- defines expected package scope, reference posture, root boundaries, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass evidence, policy, release, and trust-membrane controls.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-CITATION-001` | Is `packages/citation/` a JavaScript/TypeScript package, Python package, generated-helper home, or mixed-language home? | NEEDS VERIFICATION / ADR |
| `PKG-CITATION-002` | Which canonical schema owns Citation, EvidenceRef, and EvidenceBundleRef shapes? | NEEDS VERIFICATION |
| `PKG-CITATION-003` | Which CI workflow validates this package? | UNKNOWN |
| `PKG-CITATION-004` | Which package exports are active today? | UNKNOWN |
| `PKG-CITATION-005` | Should citation rendering helpers live here, in `packages/api/`, or in UI-specific packages? | NEEDS VERIFICATION / ADR |
| `PKG-CITATION-006` | Which missing/inaccessible evidence finite-outcome behavior is canonical across API, UI, and export surfaces? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package subordinate to evidence and release governance. Do not add EvidenceBundle writers, source admission logic, lifecycle writers, schema authority, contract authority, policy decisions, release decisions, public API routes, UI-only rendering behavior, secrets, credentials, or generated truth claims here. Put those concerns in their responsibility roots and reference them through governed contracts.

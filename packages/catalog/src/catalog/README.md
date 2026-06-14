<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-catalog-src-catalog-readme
title: Catalog Package Source Catalog Module README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <catalog-steward>
  - <schema-steward>
  - <evidence-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/catalog/src/catalog/README.md
related:
  - packages/README.md
  - packages/catalog/README.md
  - pipelines/catalog/README.md
  - pipeline_specs/README.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/standards/PROV.md
  - data/catalog/
  - data/triplets/
  - data/proofs/evidence_bundle/
  - data/receipts/pipeline/
  - release/manifests/
  - contracts/
  - schemas/contracts/v1/
  - policy/
  - tests/packages/catalog/
  - fixtures/packages/catalog/
tags: [kfm, packages, catalog, src, shared-library, catalog-module, stac, dcat, prov, builders, validators, metadata, evidence-ref, release-ref, governance]
notes:
  - "This README fills the empty packages/catalog/src/catalog README with a governed source-module contract."
  - "packages/catalog/src/catalog/ may contain internal source code for shared catalog helpers only; it must remain subordinate to packages/catalog/ and cannot become an executable pipeline or catalog data home."
  - "Catalog records are discovery/provenance carriers, not proof of truth, release approval, or public-display permission."
  - "Concrete modules, exports, language runtime, build scripts, and tests remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Source Module

> Internal source-code module area for the `packages/catalog/` shared library. This directory may hold reusable catalog helper modules, but it must not become an executable catalog pipeline, lifecycle data writer, schema authority, EvidenceBundle authority, policy authority, or release authority.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fcatalog%2Fsrc%2Fcatalog%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20module-0a7ea4)
![pipeline](https://img.shields.io/badge/executable-pipelines%2Fcatalog%2F-d62728)
![catalog](https://img.shields.io/badge/catalog-carrier%20not%20proof-d62728)

**Status:** Draft  
**Path:** `packages/catalog/src/catalog/README.md`  
**Parent package:** `packages/catalog/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Companion executable lane:** `pipelines/catalog/` — executable catalog-building and validation logic  
**Catalog data homes:** `data/catalog/` and `data/triplets/`  
**Release authority:** `release/`  
**Placement posture:** `packages/catalog/src/catalog/` is source code for reusable catalog helpers only. Implementation language, module names, exports, and CI coverage are `NEEDS VERIFICATION` until checked by current repo evidence.

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

`packages/catalog/src/catalog/` may hold internal source modules for the `packages/catalog/` shared catalog support library.

It may support reusable helpers for:

- STAC Item and Collection construction;
- DCAT Dataset and Distribution construction;
- PROV/PAV provenance embedding;
- catalog matrix assembly;
- deterministic catalog identifiers and digests;
- catalog metadata normalization;
- schema-bound catalog validation adapters;
- reference preservation for `EvidenceRef`, `RunReceiptRef`, `SourceDescriptorRef`, `PolicyDecisionRef`, `ReleaseManifestRef`, `CorrectionNoticeRef`, and `RollbackCardRef`;
- no-network fixture builders for package tests.

It does **not** run catalog pipelines or write catalog lifecycle records. Executable catalog behavior belongs under `pipelines/catalog/` or accepted domain catalog lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/catalog/`? | Parent package is the shared catalog support library. | CONFIRMED parent package contract |
| Why `src/catalog/`? | This is a plausible internal module path for catalog-specific package source. | PROPOSED / NEEDS VERIFICATION |
| Is this executable pipeline code? | No. Catalog execution belongs under `pipelines/catalog/`. | CONFIRMED boundary posture |
| Is this catalog data storage? | No. Catalog records belong under `data/catalog/`; graph/triplet records belong under `data/triplets/`. | CONFIRMED lifecycle posture |
| Can this define schemas or contracts? | No. It may consume schema/contract outputs, but authority stays in `schemas/` and `contracts/`. | CONFIRMED authority separation |
| Can this approve release or policy? | No. It may preserve refs only. | CONFIRMED release/policy separation |

> [!IMPORTANT]
> Source modules here can make catalog construction consistent. They cannot make catalog metadata evidence, publish data, promote lifecycle state, decide policy, or approve release.

[⬆ Back to top](#top)

---

## 3. Module boundary

Allowed direction:

```text
pipeline / tool / test
  -> packages/catalog/src/catalog helper
  -> validated catalog object shape or validation result
  -> executable pipeline writes governed outputs where authorized
```

Blocked direction:

```text
packages/catalog/src/catalog helper
  -> direct RAW / WORK / QUARANTINE promotion
  -> data/catalog lifecycle write as a hidden side effect
  -> EvidenceBundle fabrication
  -> PolicyDecision creation
  -> ReleaseManifest creation
  -> public display permission
```

The module should be pure or side-effect-minimal where practical. Any future write capability requires explicit executable pipeline ownership, tests, receipts, and review.

[⬆ Back to top](#top)

---

## 4. Anti-collapse rules

Disallowed collapses:

```text
source module -> executable catalog pipeline
builder helper -> lifecycle writer
catalog metadata -> EvidenceBundle
STAC helper -> proof of truth
DCAT helper -> source of truth
PROV helper -> full proof closure
validation helper -> promotion decision
reference helper -> policy decision
ReleaseManifest ref -> release approval
fixture builder -> production catalog
```

Required separations:

- reusable helper source stays under `packages/catalog/src/catalog/`;
- executable catalog orchestration stays under `pipelines/catalog/` or accepted domain catalog lanes;
- catalog lifecycle records stay under `data/catalog/`;
- graph/triplet records stay under `data/triplets/`;
- EvidenceBundles stay under proof homes;
- receipts stay under receipt homes;
- schemas and contracts stay under their authority roots;
- policy and release decisions stay under their authority roots.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source modules include helpers for:

- catalog object construction from already-authorized inputs;
- STAC/DCAT dispatch and builder utilities;
- PROV/PAV reference embedding utilities;
- KFM namespace handling;
- catalog matrix shape assembly;
- deterministic serialization and digest support;
- reference-preservation adapters;
- schema-bound validation adapters;
- safe validation errors;
- package-only fixture builders.

A good placement test:

> If the module is reusable catalog helper code and does not run a lifecycle transition, write catalog records as a side effect, evaluate policy, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Catalog pipeline runner/orchestrator | `pipelines/catalog/` |
| Domain catalog execution logic | `pipelines/domains/<domain>/catalog/` |
| Declarative catalog specs | `pipeline_specs/` |
| Catalog records | `data/catalog/` |
| Triplet records | `data/triplets/` |
| Runtime receipts | `data/receipts/pipeline/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Source descriptors | `data/registry/sources/` |
| Canonical schemas | `schemas/contracts/v1/` |
| Object contracts | `contracts/` |
| Policy decisions and rules | `policy/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| UI rendering code | `apps/explorer-web/` or package UI roots |
| Tests | `tests/packages/catalog/` |
| Fixtures | `fixtures/packages/catalog/` unless package-local convention is ADR-approved |

[⬆ Back to top](#top)

---

## 7. Expected module families

| Module family | Responsibility | Status |
|---|---|---|
| `stac` | STAC helper objects, field mappers, and validators. | PROPOSED |
| `dcat` | DCAT helper objects, distribution helpers, and validators. | PROPOSED |
| `prov` | PROV/PAV embedding and reference preservation. | PROPOSED |
| `matrix` | Catalog matrix assembly and cross-standard dispatch. | PROPOSED |
| `refs` | Evidence/source/receipt/policy/release reference helpers. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `digests` | Deterministic id, hash, and serialization helpers. | PROPOSED |
| `fixtures` | Package-only fixture builders, if accepted by package convention. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Module source | `packages/catalog/src/catalog/` | Shared helper source only. |
| Package entrypoint | `packages/catalog/` | Language-specific entrypoint is not verified. |
| Executable pipeline caller | `pipelines/catalog/` | Runs catalog lifecycle workflow. |
| Declarative spec caller | `pipeline_specs/` | Configures catalog work. |
| Catalog record output | `data/catalog/` | Written by governed execution, not hidden package side effects. |
| Triplet output | `data/triplets/` | Written by governed execution. |
| Receipts | `data/receipts/pipeline/` | Emitted by execution. |
| Evidence refs | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/catalog/` | Package validation. |
| Fixtures | `fixtures/packages/catalog/` | No-network package fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal module contract shape

```yaml
module_id: kfm.packages.catalog.src.catalog
status: draft
authority: package_source_module
not_authority_for:
  - executable_pipeline
  - lifecycle_writes
  - schema_home
  - contract_home
  - policy_decision
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - catalog helper types
  - catalog builders
  - standard dispatch helpers
  - reference preservation helpers
  - schema-bound validation adapters
  - safe fixture builders
required_invariants:
  no_hidden_lifecycle_writes: true
  no_evidence_fabrication: true
  no_policy_bypass: true
  no_release_approval: true
  catalog_metadata_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 10. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/catalog/
├── test_catalog_module_boundaries.py        # PROPOSED
├── test_stac_builder_preserves_refs.py      # PROPOSED
├── test_dcat_builder_preserves_refs.py      # PROPOSED
├── test_prov_helper_no_predicate_rename.py  # PROPOSED
├── test_catalog_metadata_not_evidence.py    # PROPOSED
├── test_no_hidden_lifecycle_writes.py        # PROPOSED
├── test_no_release_decisions.py             # PROPOSED
├── test_safe_validation_errors.py           # PROPOSED
└── test_deterministic_serialization.py      # PROPOSED
```

Fixture material should live in `fixtures/packages/catalog/` unless a package-local fixture convention is explicitly accepted. Fixtures must not be mistaken for production catalog records.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/catalog/src/catalog/README.md` file;
- identifies this directory as package source for shared catalog helpers;
- keeps executable catalog behavior under `pipelines/catalog/`;
- keeps catalog lifecycle records under `data/catalog/` and `data/triplets/`;
- blocks helper modules from becoming lifecycle writers, EvidenceBundle creators, policy engines, release approvers, schema authority, or contract authority;
- defines expected module families, inputs/outputs, tests, fixtures, and open questions.

Future source files in this module are done only when they are schema-aligned, test-covered, deterministic where practical, and unable to bypass catalog lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-CATALOG-SRC-001` | Which language/runtime owns `packages/catalog/src/catalog/`? | UNKNOWN |
| `PKG-CATALOG-SRC-002` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-CATALOG-SRC-003` | Should fixture builders live in source, tests, or `fixtures/packages/catalog/` only? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-004` | Which schema generator, if any, feeds generated catalog types into this module? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-005` | Which CI workflow verifies helper determinism and no hidden lifecycle writes? | UNKNOWN |
| `PKG-CATALOG-SRC-006` | Should deterministic JSON canonicalization live here, in a proof/signing package, or a shared serialization package? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this module small, deterministic, and subordinate to catalog lifecycle governance. Do not add pipeline runners, source clients, source descriptors, schema authority, contract authority, policy decisions, EvidenceBundle fabrication, release decisions, lifecycle writers, public API routes, secrets, credentials, or generated truth claims here.

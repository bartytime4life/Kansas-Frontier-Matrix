<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-catalog-readme
title: Catalog Package README
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
path: packages/catalog/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/standards/PROV.md
  - packages/README.md
  - pipelines/catalog/README.md
  - pipeline_specs/README.md
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
tags: [kfm, packages, catalog, shared-library, stac, dcat, prov, metadata, validator, catalog-matrix, evidence-ref, release-ref, governance]
notes:
  - "This README expands the packages/catalog stub into a governed shared-package contract."
  - "packages/ contains shared libraries; packages/catalog/ may contain reusable catalog builders, validators, type helpers, and fixture utilities only when subordinate to schemas, contracts, policy, evidence, lifecycle, and release roots."
  - "pipelines/catalog/ owns executable catalog-building logic. packages/catalog/ is shared library support and must not become a pipeline runner or publication authority."
  - "Catalog records are discovery/provenance carriers, not proof of truth, proof of release, or public-display permission."
  - "Concrete implementation, package exports, build scripts, validators, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Package

> Shared library package for KFM catalog support: STAC/DCAT/PROV helpers, catalog matrix builders, metadata validators, reference utilities, fixture builders, and deterministic serialization support. Executable catalog pipelines remain under `pipelines/catalog/`; catalog lifecycle records remain under `data/catalog/` and `data/triplets/`; release decisions remain under `release/`.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20library-0a7ea4)
![pipeline](https://img.shields.io/badge/executable-pipelines%2Fcatalog%2F-d62728)
![catalog](https://img.shields.io/badge/catalog-carrier%20not%20proof-d62728)

**Status:** Draft  
**Path:** `packages/catalog/README.md`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Companion executable lane:** `pipelines/catalog/` — executable catalog-building and validation logic  
**Catalog data homes:** `data/catalog/` and `data/triplets/`  
**Release authority:** `release/`  
**Placement posture:** `packages/catalog/` may host reusable catalog support code only when it remains non-deployable, deterministic, schema-aligned, and subordinate to catalog lifecycle and release authority.  
**Public posture:** no independent public catalog, no release approval, no EvidenceBundle fabrication, no policy bypass, and no direct public-client trust membrane.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Catalog responsibility boundary](#3-catalog-responsibility-boundary)
- [4. Package anti-collapse rules](#4-package-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Package scope](#7-package-scope)
- [8. STAC/DCAT/PROV posture](#8-stacdcatprov-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal package contract shape](#12-minimal-package-contract-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`packages/catalog/` is a shared-library lane for catalog-facing support code that can be reused by KFM applications, pipelines, tools, validators, tests, and documentation checks.

It may support:

- STAC helper types and builders;
- DCAT helper types and builders;
- PROV/PAV mapping helpers;
- KFM catalog matrix builder utilities;
- deterministic catalog identifier and hash helpers;
- EvidenceRef, EvidenceBundleRef, RunReceiptRef, PolicyDecisionRef, ReleaseManifestRef, CorrectionNoticeRef, and RollbackCardRef utilities;
- catalog validation helpers that consume canonical schemas;
- fixture builders for no-network tests;
- serialization/deserialization helpers;
- compatibility helpers for catalog profile migrations.

It does **not** implement the executable catalog pipeline. Catalog-building execution belongs under `pipelines/catalog/` or accepted domain catalog lanes.

Short rule:

```text
packages/catalog/  = shared catalog support library
pipelines/catalog/ = executable catalog-building logic
data/catalog/      = catalog lifecycle records
data/triplets/     = graph/triplet lifecycle records
schemas/           = machine shape
contracts/         = object meaning
policy/            = admissibility and exposure decisions
release/           = release decisions and release control
```

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/`? | This root owns shared libraries used by apps, workers, pipelines, and tools. | CONFIRMED root contract |
| Why `catalog/` under packages? | Reusable catalog helpers can support pipelines, tools, tests, and apps without becoming executable pipelines or data homes. | PROPOSED / NEEDS VERIFICATION |
| Is this the catalog pipeline? | No. Executable catalog pipeline logic belongs under `pipelines/catalog/`. | CONFIRMED boundary posture |
| Does this store catalog records? | No. Catalog records belong under `data/catalog/`; graph/triplet outputs belong under `data/triplets/` or accepted graph homes. | CONFIRMED lifecycle posture |
| Can this package define schemas or contracts? | No. It may consume or mirror generated types, but schema and contract authority live in their roots. | CONFIRMED authority separation |
| Can this package approve release or policy? | No. It may carry refs and validation helpers only. | CONFIRMED release/policy separation |

> [!IMPORTANT]
> A shared catalog package is not a pipeline runner, not a catalog data home, not schema authority, not contract authority, not EvidenceBundle authority, not policy authority, and not release authority.

[⬆ Back to top](#top)

---

## 3. Catalog responsibility boundary

KFM catalog records are discovery and provenance carriers. They help users and systems find and inspect released or candidate artifacts, but catalog metadata cannot replace evidence, policy, review, or release state.

Allowed direction:

```text
validated processed data + receipts + EvidenceBundle refs + policy/release refs
  -> pipelines/catalog/ executable build step
  -> packages/catalog shared helpers
  -> data/catalog/ candidate records + catalog receipts
  -> release review
  -> governed public access after ReleaseManifest
```

Blocked direction:

```text
packages/catalog helper
  -> raw/work/quarantine data promotion
  -> EvidenceBundle creation by metadata alone
  -> policy decision
  -> release approval
  -> public display permission
```

This package can make catalog construction and validation consistent. It cannot make a catalog record authoritative by itself.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
shared package -> executable catalog pipeline
builder helper -> catalog lifecycle writer
catalog metadata -> EvidenceBundle
catalog record -> release approval
catalog record -> public display permission
STAC item -> proof of truth
DCAT dataset -> source of truth
PROV fragment -> full EvidenceBundle closure
schema-generated type -> schema authority
successful package test -> catalog promotion
mock catalog -> production truth
```

Required separations:

- shared package code stays in `packages/catalog/`;
- executable catalog pipeline logic stays in `pipelines/catalog/` or accepted domain catalog lanes;
- catalog lifecycle records stay in `data/catalog/`;
- graph/triplet outputs stay in `data/triplets/` or accepted graph homes;
- schemas stay in `schemas/`;
- contracts stay in `contracts/`;
- policy decisions stay in `policy/`;
- EvidenceBundles stay in proof homes;
- release decisions stay under `release/`;
- public clients consume governed API envelopes and released artifacts, not package-internal shortcuts.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include:

- STAC Item and Collection helper types;
- DCAT Dataset and Distribution helper types;
- PROV/PAV mapping helpers;
- KFM namespace helper utilities;
- catalog matrix builder helpers;
- catalog identifier, digest, and deterministic serialization helpers;
- schema-bound validators and validation adapters;
- helper functions for EvidenceRef, RunReceiptRef, SourceDescriptorRef, PolicyDecisionRef, ReleaseManifestRef, CorrectionNoticeRef, and RollbackCardRef fields;
- catalog fixture builders for tests;
- no-network validator fixtures;
- compatibility helpers for catalog profile migrations.

A good placement test:

> If the file is reusable catalog support code that depends on canonical schemas/contracts and does not execute lifecycle transitions or write catalog records by itself, it may belong here. If it runs a pipeline, writes data, evaluates policy, or decides release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable catalog pipeline logic | `pipelines/catalog/` or accepted domain catalog lane |
| Declarative catalog specs | `pipeline_specs/` |
| Catalog lifecycle records | `data/catalog/` |
| Graph/triplet lifecycle records | `data/triplets/` or accepted graph homes |
| Runtime receipts | `data/receipts/pipeline/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Source descriptors | `data/registry/sources/` |
| Canonical schemas | `schemas/contracts/v1/` |
| Object contracts | `contracts/` |
| Policy decisions and rules | `policy/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API server routes | `apps/governed-api/` |
| Explorer/web UI code | `apps/explorer-web/` |
| Package tests | `tests/packages/catalog/` |
| Package fixtures | `fixtures/packages/catalog/` |
| Secrets or credentials | never in repo; use approved secret management |

[⬆ Back to top](#top)

---

## 7. Package scope

`packages/catalog/` may support catalog-facing concerns such as:

- catalog record construction helpers;
- STAC/DCAT dispatch helpers;
- PROV/PAV embedding helpers;
- catalog matrix validation helpers;
- source/evidence/release reference preservation;
- stable id and digest generation helpers;
- profile migration helpers;
- fixture and mock builders that cannot be mistaken for production catalog records;
- safe error helpers for catalog validation failures.

Implementation status for concrete modules, exports, package manager configuration, build steps, and CI remains `NEEDS VERIFICATION` unless backed by current repo evidence.

[⬆ Back to top](#top)

---

## 8. STAC/DCAT/PROV posture

KFM uses catalog standards with responsibility boundaries:

| Standard | KFM posture | Package responsibility |
|---|---|---|
| STAC | Spatiotemporal asset catalog envelope. | Help construct/validate STAC-shaped records without replacing EvidenceBundle or release state. |
| DCAT | Dataset-level metadata and non-spatial distribution carrier. | Help construct/validate DCAT-shaped records without making DCAT a truth source. |
| PROV/PAV | Provenance vocabulary and authoring/versioning layer. | Help embed and preserve provenance refs without claiming full proof closure. |

Package helpers must preserve standard conformance and KFM extension namespaces. They must not fork standards, rename PROV predicates, or silently drop KFM evidence, policy, review, release, limitation, or redaction fields.

[⬆ Back to top](#top)

---

## 9. Required gates

Before this package can be used by production catalog builders, it should have:

1. **Schema gate** — generated or hand-written types reconciled with canonical schemas.
2. **Standards gate** — STAC, DCAT, and PROV/PAV fields preserved according to KFM standards docs.
3. **Evidence gate** — EvidenceRef and EvidenceBundle references preserved without fabrication.
4. **Receipt gate** — RunReceipt and catalog-build receipt refs preserved.
5. **Policy gate** — PolicyDecision refs and sensitivity/redaction metadata preserved.
6. **Release gate** — ReleaseManifest, CorrectionNotice, and RollbackCard refs preserved.
7. **Lifecycle gate** — no direct promotion, publication, or lifecycle writes from package helpers.
8. **Determinism gate** — stable ids, digests, and serialization rules tested where practical.
9. **Fixture gate** — no-network tests for catalog helpers.
10. **Review gate** — catalog, schema, evidence, and release steward review for trust-bearing changes.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
packages/catalog/
├── README.md
├── package.json                 # NEEDS VERIFICATION / PROPOSED if JS package
├── pyproject.toml               # NEEDS VERIFICATION / PROPOSED if Python package
├── src/
│   ├── index.*                  # PROPOSED
│   ├── stac.*                   # PROPOSED
│   ├── dcat.*                   # PROPOSED
│   ├── prov.*                   # PROPOSED
│   ├── catalog_matrix.*         # PROPOSED
│   ├── refs.*                   # PROPOSED
│   ├── validation.*             # PROPOSED
│   └── fixtures.*               # PROPOSED
├── generated/                   # PROPOSED, only if generated from canonical schemas
└── README.md
```

The specific language/runtime is `UNKNOWN` from current evidence. Do not add parallel JS/Python package layouts without an implementation decision, package manifest, tests, and migration note.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/catalog/` | Shared library only. |
| Executable catalog pipeline | `pipelines/catalog/` | Runs catalog build/validation workflows. |
| Catalog specs | `pipeline_specs/` | Declarative inputs. |
| Catalog lifecycle records | `data/catalog/` | Package helpers do not store them directly. |
| Triplet lifecycle records | `data/triplets/` | Package helpers may support shape/refs, not lifecycle authority. |
| Runtime receipts | `data/receipts/pipeline/` | Referenced by catalog records. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced; not created by catalog metadata alone. |
| Canonical schemas | `schemas/contracts/v1/` | Schema authority. |
| Object contracts | `contracts/` | Meaning authority. |
| Policy refs | `policy/` outputs/refs | Do not decide policy here. |
| Release refs | `release/` refs | Do not approve release here. |
| Tests | `tests/packages/catalog/` | Package validation. |
| Fixtures | `fixtures/packages/catalog/` | No-network package fixtures. |

[⬆ Back to top](#top)

---

## 12. Minimal package contract shape

```yaml
package_id: kfm.packages.catalog
status: draft
authority: shared_library
not_authority_for:
  - executable_catalog_pipeline
  - catalog_lifecycle_storage
  - schema_home
  - contract_home
  - policy_decision
  - evidence_bundle
  - release_decision
allowed_exports:
  - STAC helpers
  - DCAT helpers
  - PROV/PAV helpers
  - catalog matrix helpers
  - reference preservation helpers
  - validation adapters
  - fixture builders
required_invariants:
  no_lifecycle_writes: true
  no_release_approval: true
  no_evidence_fabrication: true
  no_policy_bypass: true
  no_catalog_metadata_as_truth: true
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/packages/catalog/
├── test_stac_helpers.py                     # PROPOSED
├── test_dcat_helpers.py                     # PROPOSED
├── test_prov_helpers.py                     # PROPOSED
├── test_catalog_matrix_shape.py             # PROPOSED
├── test_evidence_refs_preserved.py          # PROPOSED
├── test_policy_release_refs_preserved.py    # PROPOSED
├── test_no_lifecycle_writes.py              # PROPOSED
├── test_generated_types_match_schema.py     # PROPOSED
├── test_deterministic_serialization.py      # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

A package change is not ready for production use until it has tests, fixtures, schema alignment, steward review, and proof that it cannot replace catalog pipeline execution, lifecycle storage, evidence closure, policy decisions, or release decisions.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- expands the short `packages/catalog/README.md` stub;
- identifies `packages/catalog/` as shared catalog support, not an executable catalog pipeline;
- preserves `pipelines/catalog/` as executable catalog-building logic;
- keeps `data/catalog/`, `data/triplets/`, `data/receipts/`, `data/proofs/`, and `release/` as authority roots for their respective artifacts and decisions;
- blocks the package from becoming schema, contract, policy, evidence, release, lifecycle, or public truth authority;
- defines expected package scope, standards posture, root boundaries, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass catalog lifecycle and release controls.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-CATALOG-001` | Is `packages/catalog/` a JavaScript/TypeScript package, Python package, generated-helper home, or mixed-language home? | NEEDS VERIFICATION / ADR |
| `PKG-CATALOG-002` | Which schema generator, if any, owns generated catalog types? | NEEDS VERIFICATION |
| `PKG-CATALOG-003` | Which CI workflow validates this package? | UNKNOWN |
| `PKG-CATALOG-004` | Which package exports are active today? | UNKNOWN |
| `PKG-CATALOG-005` | Which canonical catalog matrix shape should package helpers implement first? | NEEDS VERIFICATION |
| `PKG-CATALOG-006` | Should deterministic JSON canonicalization live here, in a shared proof package, or in a signing/provenance package? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this package subordinate to catalog lifecycle and release governance. Do not add executable pipeline runners, catalog lifecycle writers, source clients, source descriptors, schema authority, contract authority, policy decisions, EvidenceBundle fabrication, release decisions, public API routes, secrets, credentials, or generated claims here. Put those concerns in their responsibility roots and reference them through governed contracts.

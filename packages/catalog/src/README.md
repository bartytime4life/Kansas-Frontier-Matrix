<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-catalog-src-readme
title: Catalog Package Source README
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
path: packages/catalog/src/README.md
related:
  - packages/README.md
  - packages/catalog/README.md
  - packages/catalog/src/catalog/README.md
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
tags: [kfm, packages, catalog, src, shared-library, source-root, stac, dcat, prov, validators, builders, references, governance]
notes:
  - "This README fills the empty packages/catalog/src README with a governed source-root contract."
  - "packages/catalog/src/ may contain source code for the shared catalog support package only; it must remain subordinate to packages/catalog/."
  - "Catalog helper code must not become an executable catalog pipeline, catalog data home, proof authority, policy authority, or release authority."
  - "Catalog records are discovery/provenance carriers, not proof of truth, release approval, or public-display permission."
  - "Concrete language runtime, package manifests, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Package Source Root

> Source root for the `packages/catalog/` shared catalog support library. Code here may provide reusable catalog helpers, validators, references, serialization, and internal module wiring, but it must not execute catalog pipelines, write lifecycle records as hidden side effects, fabricate evidence, decide policy, or approve release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fcatalog%2Fsrc%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20root-0a7ea4)
![pipeline](https://img.shields.io/badge/executable-pipelines%2Fcatalog%2F-d62728)
![catalog](https://img.shields.io/badge/catalog-carrier%20not%20proof-d62728)

**Status:** Draft  
**Path:** `packages/catalog/src/README.md`  
**Parent package:** `packages/catalog/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Companion executable lane:** `pipelines/catalog/` — executable catalog-building and validation logic  
**Catalog helper module:** `packages/catalog/src/catalog/`  
**Catalog data homes:** `data/catalog/` and `data/triplets/`  
**Release authority:** `release/`  
**Placement posture:** source root for shared catalog package code only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.

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

`packages/catalog/src/` may contain source code for the `packages/catalog/` shared library.

It may include internal modules for:

- STAC helpers;
- DCAT helpers;
- PROV/PAV helpers;
- catalog matrix helpers;
- catalog reference helpers;
- deterministic id, digest, and serialization helpers;
- schema-bound validation adapters;
- safe validation error helpers;
- package entrypoints and internal exports;
- package-local adapters that do not own lifecycle transitions.

It does **not** run catalog pipelines or own catalog lifecycle state. Executable catalog behavior belongs under `pipelines/catalog/` or accepted domain catalog lanes, while catalog records belong under `data/catalog/` and graph/triplet records under `data/triplets/`.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/catalog/`? | Parent package is the shared catalog support library. | CONFIRMED parent package contract |
| Why `src/`? | This is a conventional source root for package implementation, but language/runtime are not yet verified. | PROPOSED / NEEDS VERIFICATION |
| Is this executable catalog pipeline logic? | No. Catalog execution belongs under `pipelines/catalog/`. | CONFIRMED boundary posture |
| Is this catalog data storage? | No. Catalog records belong under `data/catalog/`; graph/triplet records belong under `data/triplets/`. | CONFIRMED lifecycle posture |
| Can this define schemas or contracts? | No. It may consume schema/contract outputs, but authority stays in `schemas/` and `contracts/`. | CONFIRMED authority separation |
| Can this decide policy or release? | No. It may preserve refs and validate shape only. | CONFIRMED release/policy separation |

> [!IMPORTANT]
> Source code under this root can help construct, validate, and serialize catalog-shaped objects. It cannot make catalog metadata evidence, publish data, promote lifecycle state, decide policy, or approve release.

[⬆ Back to top](#top)

---

## 3. Source-root boundary

Allowed direction:

```text
pipeline / tool / test
  -> packages/catalog/src module
  -> validated catalog object shape, refs, digest, or validation result
  -> executable pipeline writes governed outputs where authorized
```

Blocked direction:

```text
packages/catalog/src module
  -> direct RAW / WORK / QUARANTINE promotion
  -> hidden data/catalog write
  -> hidden data/triplets write
  -> EvidenceBundle fabrication
  -> PolicyDecision creation
  -> ReleaseManifest creation
```

The source root should favor pure, deterministic helpers. Any future IO capability must be explicit, reviewed, tested, receipt-producing, and owned by an executable pipeline or tool lane.

[⬆ Back to top](#top)

---

## 4. Anti-collapse rules

Disallowed collapses:

```text
source root -> executable catalog pipeline
helper module -> lifecycle writer
catalog metadata -> EvidenceBundle
STAC helper -> proof of truth
DCAT helper -> source of truth
PROV helper -> full proof closure
validation helper -> promotion decision
reference helper -> policy decision
ReleaseManifest ref -> release approval
fixture builder -> production catalog
package export -> public trust membrane
```

Required separations:

- reusable source code stays under `packages/catalog/src/`;
- executable catalog orchestration stays under `pipelines/catalog/` or accepted domain catalog lanes;
- declarative catalog run profiles stay under `pipeline_specs/`;
- catalog lifecycle records stay under `data/catalog/`;
- graph/triplet records stay under `data/triplets/`;
- EvidenceBundles stay under proof homes;
- receipts stay under receipt homes;
- schemas and contracts stay under their authority roots;
- policy and release decisions stay under their authority roots;
- public clients consume governed API envelopes and released artifacts, not package internals.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source files include:

- package entrypoints and internal exports;
- catalog helper modules;
- STAC/DCAT/PROV/PAV builder modules;
- KFM namespace and profile helper modules;
- catalog matrix assembly modules;
- reference-preservation modules;
- schema-bound validation adapters;
- deterministic serialization and digest helpers;
- safe validation error helpers;
- package-local types generated from canonical schemas when generation provenance is recorded.

A good placement test:

> If the file is package source for reusable catalog support and does not run lifecycle transitions, write catalog records as a hidden side effect, evaluate policy, or approve release, it may belong here.

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
| Package tests | `tests/packages/catalog/` |
| Package fixtures | `fixtures/packages/catalog/` unless package-local convention is ADR-approved |

[⬆ Back to top](#top)

---

## 7. Expected module layout

Current verified child module:

```text
packages/catalog/src/
├── README.md
└── catalog/
    └── README.md
```

Potential future layout:

```text
packages/catalog/src/
├── index.*                    # PROPOSED
├── catalog/
│   ├── stac.*                 # PROPOSED
│   ├── dcat.*                 # PROPOSED
│   ├── prov.*                 # PROPOSED
│   ├── matrix.*               # PROPOSED
│   ├── refs.*                 # PROPOSED
│   ├── validation.*           # PROPOSED
│   └── digests.*              # PROPOSED
└── generated/                 # PROPOSED, only if generated from canonical schemas
```

Do not add parallel language layouts or generated output folders without package manifest evidence, generation provenance, tests, and a migration note.

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Source root | `packages/catalog/src/` | Shared helper source only. |
| Catalog helper module | `packages/catalog/src/catalog/` | Catalog-specific helper module. |
| Executable catalog pipeline | `pipelines/catalog/` | Runs catalog lifecycle workflow. |
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

## 9. Minimal source-root contract shape

```yaml
source_root_id: kfm.packages.catalog.src
status: draft
authority: package_source_root
not_authority_for:
  - executable_pipeline
  - lifecycle_writes
  - schema_home
  - contract_home
  - policy_decision
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - package entrypoints
  - internal modules
  - catalog helper types
  - catalog builders
  - standard dispatch helpers
  - reference preservation helpers
  - schema-bound validation adapters
  - deterministic serialization helpers
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
├── test_src_root_boundaries.py              # PROPOSED
├── test_catalog_module_boundaries.py        # PROPOSED
├── test_exports_do_not_run_pipelines.py     # PROPOSED
├── test_stac_dcat_prov_helpers.py           # PROPOSED
├── test_catalog_metadata_not_evidence.py    # PROPOSED
├── test_no_hidden_lifecycle_writes.py       # PROPOSED
├── test_no_policy_or_release_decisions.py   # PROPOSED
├── test_safe_validation_errors.py           # PROPOSED
└── test_deterministic_serialization.py      # PROPOSED
```

Fixture material should live in `fixtures/packages/catalog/` unless a package-local fixture convention is explicitly accepted. Fixtures must not be mistaken for production catalog records.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/catalog/src/README.md` file;
- identifies this directory as the source root for shared catalog package code;
- keeps executable catalog behavior under `pipelines/catalog/`;
- keeps catalog lifecycle records under `data/catalog/` and `data/triplets/`;
- blocks source modules from becoming lifecycle writers, EvidenceBundle creators, policy engines, release approvers, schema authority, contract authority, or public trust membrane;
- defines expected module layout, inputs/outputs, tests, fixtures, and open questions.

Future source files under this root are done only when they are schema-aligned, test-covered, deterministic where practical, and unable to bypass catalog lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-CATALOG-SRC-ROOT-001` | Which language/runtime owns `packages/catalog/src/`? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-002` | Which package manifest controls this source root? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-003` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-004` | Should generated types live under this source root, under `generated/`, or under a separate generated-code root? | NEEDS VERIFICATION / ADR |
| `PKG-CATALOG-SRC-ROOT-005` | Which CI workflow verifies helper determinism and no hidden lifecycle writes? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-006` | Should deterministic JSON canonicalization live here, in a proof/signing package, or a shared serialization package? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this source root small, deterministic, and subordinate to catalog lifecycle governance. Do not add pipeline runners, source clients, source descriptors, schema authority, contract authority, policy decisions, EvidenceBundle fabrication, release decisions, lifecycle writers, public API routes, or generated truth claims here.

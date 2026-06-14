<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-archaeology-src-readme
title: Archaeology Domain Package Source README
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
path: packages/domains/archaeology/src/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/archaeology/README.md
  - packages/domains/archaeology/src/archaeology/README.md
  - docs/domains/archaeology/README.md
  - pipelines/domains/archaeology/README.md
  - pipeline_specs/archaeology/README.md
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - tests/packages/domains/archaeology/
  - fixtures/packages/domains/archaeology/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, archaeology, src, source-root, shared-library, candidate-feature, survey, artifact, context, chronology, sensing, cultural-review, sensitivity-transform, governance]
notes:
  - "This README fills the empty packages/domains/archaeology/src README with a governed source-root contract."
  - "packages/domains/archaeology/src/ may contain source code for the shared Archaeology helper package only; it must remain subordinate to packages/domains/archaeology/."
  - "archaeology/ is the Archaeology helper module lane for reusable source-agnostic helpers."
  - "Archaeology source code may normalize, parse, map, generalize, preserve refs, and prepare review-friendly DTOs. It cannot confirm sites, write lifecycle data, decide policy, create EvidenceBundles, or approve release."
  - "Concrete language runtime, package manifests, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Package Source Root

> Source root for the `packages/domains/archaeology/` shared Archaeology helper library. Code here may provide reusable candidate, survey, artifact, context, chronology, sensing, review, sensitivity, validation, and fixture helpers, but it must not become Archaeology doctrine, schema authority, contract authority, policy authority, lifecycle writer, EvidenceBundle authority, release authority, or public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Farchaeology%2Fsrc%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20root-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Farchaeology%2F-d62728)
![sensitivity](https://img.shields.io/badge/restricted%20detail-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/archaeology/src/README.md`  
**Parent package:** `packages/domains/archaeology/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Archaeology helper module:** `packages/domains/archaeology/src/archaeology/`  
**Domain doctrine root:** `docs/domains/archaeology/`  
**Executable domain-pipeline root:** `pipelines/domains/archaeology/`  
**Declarative pipeline-spec root:** `pipeline_specs/archaeology/`  
**Contract/schema/policy roots:** `contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/`, and `policy/domains/archaeology/`  
**Placement posture:** source root for shared Archaeology helper code only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.

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

`packages/domains/archaeology/src/` may contain source code for the `packages/domains/archaeology/` shared helper package.

It may include internal modules for:

- candidate-feature and anomaly mapping;
- survey, artifact, feature, context, excavation-unit, stratigraphic-unit, and collection DTO adapters;
- LiDAR, remote-sensing, geophysics, and 3D-documentation parser helpers that preserve candidate status and uncertainty;
- chronology and cultural-temporal-period helper adapters;
- source role, source time, valid time, limitation, caveat, access state, and review-ref preservation helpers;
- cultural-review and steward-review reference helpers;
- sensitivity-transform, redaction, and generalization metadata helpers that do not approve publication;
- schema-bound validation adapters and safe errors;
- package entrypoints and internal exports.

It does **not** define Archaeology objects, confirm sites, decide cultural sensitivity, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/archaeology/`? | Parent package is the shared Archaeology helper-code lane. | CONFIRMED parent package contract |
| Why `src/`? | This is a conventional source root for package implementation, but language/runtime are not yet verified. | PROPOSED / NEEDS VERIFICATION |
| Is this Archaeology doctrine? | No. Archaeology doctrine and scope belong under `docs/domains/archaeology/`. | CONFIRMED boundary posture |
| Is this executable Archaeology pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/archaeology/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs and validation results only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Source code under this root can normalize, parse, map, and generalize. It cannot turn helper output into site confirmation, policy approval, EvidenceBundle closure, or release approval.

[⬆ Back to top](#top)

---

## 3. Source-root boundary

Allowed direction:

```text
domain app / pipeline / worker / validator / test
  -> packages/domains/archaeology/src module
  -> normalized identifiers, parsed observations, mapped DTOs, review inputs, or validation results
  -> governed pipeline/API/tool handles lifecycle, policy, evidence, review, and release where authorized
```

Blocked direction:

```text
packages/domains/archaeology/src module
  -> direct lifecycle writes
  -> site confirmation
  -> sensitivity decision
  -> policy decision
  -> EvidenceBundle creation
  -> release approval
  -> public trust membrane bypass
```

The source root should favor pure, deterministic, side-effect-minimal helpers. Any future IO capability must be explicit, bounded, test-covered, reviewable, and owned by an executable app, pipeline, worker, or approved tool lane.

[⬆ Back to top](#top)

---

## 4. Anti-collapse rules

Disallowed collapses:

```text
source root -> Archaeology doctrine
helper module -> site confirmation
candidate parser -> confirmed site
anomaly adapter -> site proof
context normalizer -> provenience truth
chronology helper -> chronology authority
sensing parser -> field confirmation
sensitivity helper -> public release approval
review ref -> review completion
successful source-root test -> lifecycle promotion
```

Required separations:

- reusable source code stays under `packages/domains/archaeology/src/`;
- Archaeology helper modules stay under `packages/domains/archaeology/src/archaeology/`;
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

- package entrypoints and internal exports;
- candidate-feature and anomaly mapping helpers;
- survey, artifact, feature, context, excavation-unit, stratigraphic-unit, and collection DTO adapters;
- LiDAR, remote-sensing, geophysics, and 3D-documentation parsing that retains candidate status;
- chronology and temporal-period helper adapters with caveats;
- cultural-review and steward-review reference preservation;
- sensitivity-transform and redaction/generalization helper utilities that do not approve publication;
- crosswalk helpers that preserve native classifications and source roles;
- schema-bound validation adapters and safe errors;
- deterministic helper ids when policy and schema allow;
- package-only fixture builders.

A good placement test:

> If the file is package source for reusable Archaeology helper code and does not confirm sites, write lifecycle data, decide policy, disclose restricted detail, or approve release, it may belong here.

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

## 7. Expected module layout

Current verified child module:

```text
packages/domains/archaeology/src/
├── README.md
└── archaeology/
    └── README.md
```

Potential future layout:

```text
packages/domains/archaeology/src/
├── index.*                    # PROPOSED
├── archaeology/
│   ├── candidate.*            # PROPOSED
│   ├── survey.*               # PROPOSED
│   ├── artifact.*             # PROPOSED
│   ├── context.*              # PROPOSED
│   ├── chronology.*           # PROPOSED
│   ├── sensing.*              # PROPOSED
│   ├── review.*               # PROPOSED
│   ├── sensitivity.*          # PROPOSED
│   ├── validation.*           # PROPOSED
│   └── fixtures.*             # PROPOSED
└── generated/                 # PROPOSED, only if generated from canonical schemas
```

Do not add parallel language layouts or generated output folders without package manifest evidence, generation provenance, tests, and a migration note.

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Source root | `packages/domains/archaeology/src/` | Shared helper source only. |
| Archaeology helper module | `packages/domains/archaeology/src/archaeology/` | Archaeology-specific helper module. |
| Package entrypoint | `packages/domains/archaeology/` | Language-specific entrypoint is not verified. |
| Domain doctrine | `docs/domains/archaeology/` | Scope, sensitivity, and human-facing control plane. |
| Domain contracts | `contracts/domains/archaeology/` | Object meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/archaeology/` | Machine shape authority. |
| Domain policy | `policy/domains/archaeology/` | Admissibility/exposure authority. |
| Executable pipeline | `pipelines/domains/archaeology/` | Runs transformations. |
| Declarative spec | `pipeline_specs/archaeology/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/archaeology/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/archaeology/` | Package validation. |
| Fixtures | `fixtures/packages/domains/archaeology/` | No-network synthetic or sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal source-root contract shape

```yaml
source_root_id: kfm.packages.domains.archaeology.src
status: draft
authority: package_source_root
not_authority_for:
  - archaeology_doctrine
  - site_confirmation
  - object_contract
  - schema_home
  - policy_decision
  - sensitivity_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - package entrypoints
  - internal modules
  - candidate mapping helpers
  - survey and artifact adapters
  - context and chronology parsers
  - remote-sensing helper adapters
  - cultural-review reference helpers
  - sensitivity-transform helper utilities
  - schema-bound adapters
  - safe fixture builders
required_invariants:
  no_site_confirmation: true
  no_restricted_detail_publication: true
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  helper_output_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 10. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/archaeology/
├── test_src_root_boundaries.py             # PROPOSED
├── test_archaeology_module_boundaries.py   # PROPOSED
├── test_exports_do_not_define_truth.py     # PROPOSED
├── test_candidate_not_site_confirmation.py # PROPOSED
├── test_context_preserves_source_role.py   # PROPOSED
├── test_sensing_preserves_uncertainty.py   # PROPOSED
├── test_sensitivity_helper_not_release.py  # PROPOSED
├── test_restricted_detail_not_public.py    # PROPOSED
├── test_no_hidden_lifecycle_writes.py      # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/archaeology/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain restricted archaeology detail unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/domains/archaeology/src/README.md` file;
- identifies this directory as the source root for shared Archaeology package code;
- keeps Archaeology doctrine, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, review decisions, and release in their own authority roots;
- blocks source modules from becoming doctrine, site confirmation, policy engine, lifecycle writer, EvidenceBundle creator, release approver, schema authority, contract authority, or public trust membrane;
- defines expected module layout, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future source files under this root are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Archaeology sensitivity, cultural/steward review, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-ARCH-SRC-ROOT-001` | Which language/runtime owns `packages/domains/archaeology/src/`? | UNKNOWN |
| `PKG-DOM-ARCH-SRC-ROOT-002` | Which package manifest controls this source root? | UNKNOWN |
| `PKG-DOM-ARCH-SRC-ROOT-003` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-DOM-ARCH-SRC-ROOT-004` | Should generated types live under this source root, under `generated/`, or under a separate generated-code root? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-ARCH-SRC-ROOT-005` | Which CI workflow validates helper determinism, sensitivity posture, and no hidden lifecycle writes? | UNKNOWN |
| `PKG-DOM-ARCH-SRC-ROOT-006` | Should sensitivity-transform helpers live here, in a policy package, or in a domain pipeline lane? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this source root helper-focused and subordinate to Archaeology governance. Do not add Archaeology doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, restricted archaeology examples, or generated truth claims here.

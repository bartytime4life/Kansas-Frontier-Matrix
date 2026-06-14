<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-agriculture-src-readme
title: Agriculture Domain Package Source README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <agriculture-domain-steward>
  - <schema-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/agriculture/src/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/agriculture/README.md
  - packages/domains/agriculture/src/agriculture/README.md
  - docs/domains/agriculture/README.md
  - pipelines/domains/agriculture/README.md
  - pipeline_specs/agriculture/README.md
  - contracts/domains/agriculture/
  - schemas/contracts/v1/domains/agriculture/
  - policy/domains/agriculture/
  - tests/packages/domains/agriculture/
  - fixtures/packages/domains/agriculture/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, agriculture, src, source-root, shared-library, crop, field-identity, yield, rotation, irrigation, suitability, aggregation, governance]
notes:
  - "This README fills the empty packages/domains/agriculture/src README with a governed source-root contract."
  - "packages/domains/agriculture/src/ may contain source code for the shared Agriculture helper package only; it must remain subordinate to packages/domains/agriculture/."
  - "agriculture/ is the Agriculture helper module lane for reusable source-agnostic helpers."
  - "Agriculture source code may normalize, parse, map, aggregate, and preserve refs. It cannot decide crop, yield, field, or producer-facing truth; write lifecycle data; decide policy; create EvidenceBundles; or approve release."
  - "Concrete language runtime, package manifests, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Package Source Root

> Source root for the `packages/domains/agriculture/` shared Agriculture helper library. Code here may provide reusable crop, yield, field, rotation, irrigation, suitability, aggregation, validation, and fixture helpers, but it must not become Agriculture doctrine, schema authority, contract authority, policy authority, lifecycle writer, EvidenceBundle authority, release authority, or public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Fagriculture%2Fsrc%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20root-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Fagriculture%2F-d62728)
![sensitivity](https://img.shields.io/badge/restricted%20detail-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/agriculture/src/README.md`  
**Parent package:** `packages/domains/agriculture/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Agriculture helper module:** `packages/domains/agriculture/src/agriculture/`  
**Domain doctrine root:** `docs/domains/agriculture/`  
**Executable domain-pipeline root:** `pipelines/domains/agriculture/`  
**Declarative pipeline-spec root:** `pipeline_specs/agriculture/`  
**Contract/schema/policy roots:** `contracts/domains/agriculture/`, `schemas/contracts/v1/domains/agriculture/`, and `policy/domains/agriculture/`  
**Placement posture:** source root for shared Agriculture helper code only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.

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

`packages/domains/agriculture/src/` may contain source code for the `packages/domains/agriculture/` shared helper package.

It may include internal modules for:

- crop observation mapping and normalization;
- crop code/name crosswalks that preserve native values;
- field or management-unit identity helpers that preserve uncertainty and provenance;
- yield, rotation, irrigation, stress, suitability, conservation, and economics DTO adapters;
- source role, source time, valid time, limitation, caveat, aggregation, and redaction helper fields;
- public-safe aggregation helper functions that do not approve publication;
- schema-bound validation adapters;
- safe validation error helpers;
- package entrypoints and internal exports.

It does **not** define Agriculture objects, decide crop/yield truth, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/agriculture/`? | Parent package is the shared Agriculture helper-code lane. | CONFIRMED parent package contract |
| Why `src/`? | This is a conventional source root for package implementation, but language/runtime are not yet verified. | PROPOSED / NEEDS VERIFICATION |
| Is this Agriculture doctrine? | No. Agriculture doctrine and scope belong under `docs/domains/agriculture/`. | CONFIRMED boundary posture |
| Is this executable Agriculture pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/agriculture/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, or release? | No. It may preserve refs and validation results only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Source code under this root can normalize, parse, map, and aggregate. It cannot turn helper output into crop truth, yield truth, field identity truth, policy approval, EvidenceBundle closure, or release approval.

[⬆ Back to top](#top)

---

## 3. Source-root boundary

Allowed direction:

```text
domain app / pipeline / worker / validator / test
  -> packages/domains/agriculture/src module
  -> normalized identifiers, parsed observations, mapped DTOs, aggregation inputs, or validation results
  -> governed pipeline/API/tool handles lifecycle, policy, evidence, and release where authorized
```

Blocked direction:

```text
packages/domains/agriculture/src module
  -> direct lifecycle writes
  -> crop or yield truth decision
  -> field identity authority
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
source root -> Agriculture doctrine
helper module -> crop truth
field identity helper -> field identity authority
yield adapter -> yield truth
rotation parser -> management history truth
irrigation helper -> water-right truth
suitability helper -> land-use decision authority
aggregation helper -> public release approval
successful source-root test -> validation pass or lifecycle promotion
```

Required separations:

- reusable source code stays under `packages/domains/agriculture/src/`;
- Agriculture helper modules stay under `packages/domains/agriculture/src/agriculture/`;
- Agriculture doctrine stays under `docs/domains/agriculture/`;
- Agriculture meaning stays under `contracts/domains/agriculture/`;
- Agriculture schemas stay under `schemas/contracts/v1/domains/agriculture/`;
- Agriculture policy stays under `policy/domains/agriculture/` and sensitivity/source policy roots;
- executable transformations stay under `pipelines/domains/agriculture/`;
- declarative run profiles stay under `pipeline_specs/agriculture/`;
- lifecycle records and receipts stay under `data/`;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source files include:

- package entrypoints and internal exports;
- crop/source mapping helpers;
- crop code/name normalization helpers;
- field identity normalization helpers that keep provenance and uncertainty explicit;
- yield, rotation, stress, irrigation, conservation, suitability, and economics DTO adapters;
- aggregation and redaction support that does not approve publication;
- crosswalk helpers that preserve native classifications and source roles;
- schema-bound validation adapters and safe errors;
- deterministic helper ids when policy and schema allow;
- package-only fixture builders.

A good placement test:

> If the file is package source for reusable Agriculture helper code and does not decide crop/yield/field truth, write lifecycle data, decide policy, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Agriculture doctrine and source scope docs | `docs/domains/agriculture/` |
| Agriculture object contracts | `contracts/domains/agriculture/` |
| Agriculture schemas | `schemas/contracts/v1/domains/agriculture/` |
| Agriculture policy decisions/rules | `policy/domains/agriculture/` and accepted policy roots |
| Executable Agriculture pipelines | `pipelines/domains/agriculture/` |
| Declarative Agriculture specs | `pipeline_specs/agriculture/` |
| Source descriptors | `data/registry/sources/agriculture/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Runtime receipts | `data/receipts/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| UI-only rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/agriculture/` |
| Package fixtures | `fixtures/packages/domains/agriculture/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Expected module layout

Current verified child module:

```text
packages/domains/agriculture/src/
├── README.md
└── agriculture/
    └── README.md
```

Potential future layout:

```text
packages/domains/agriculture/src/
├── index.*                    # PROPOSED
├── agriculture/
│   ├── crop.*                 # PROPOSED
│   ├── field_identity.*       # PROPOSED
│   ├── yield.*                # PROPOSED
│   ├── rotation.*             # PROPOSED
│   ├── irrigation.*           # PROPOSED
│   ├── suitability.*          # PROPOSED
│   ├── aggregation.*          # PROPOSED
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
| Source root | `packages/domains/agriculture/src/` | Shared helper source only. |
| Agriculture helper module | `packages/domains/agriculture/src/agriculture/` | Agriculture-specific helper module. |
| Package entrypoint | `packages/domains/agriculture/` | Language-specific entrypoint is not verified. |
| Domain doctrine | `docs/domains/agriculture/` | Scope, sensitivity, and human-facing control plane. |
| Domain contracts | `contracts/domains/agriculture/` | Object meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/agriculture/` | Machine shape authority. |
| Domain policy | `policy/domains/agriculture/` | Admissibility/exposure authority. |
| Executable pipeline | `pipelines/domains/agriculture/` | Runs transformations. |
| Declarative spec | `pipeline_specs/agriculture/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/agriculture/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/agriculture/` | Package validation. |
| Fixtures | `fixtures/packages/domains/agriculture/` | No-network synthetic or sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal source-root contract shape

```yaml
source_root_id: kfm.packages.domains.agriculture.src
status: draft
authority: package_source_root
not_authority_for:
  - agriculture_doctrine
  - crop_truth
  - field_identity_authority
  - yield_truth
  - object_contract
  - schema_home
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - package entrypoints
  - internal modules
  - crop mapping helpers
  - field identity normalizers
  - observation parsers
  - yield and suitability adapters
  - aggregation helper utilities
  - schema-bound adapters
  - safe fixture builders
required_invariants:
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  restricted_agriculture_public_denied_by_default: true
  helper_output_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 10. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/agriculture/
├── test_src_root_boundaries.py             # PROPOSED
├── test_agriculture_module_boundaries.py   # PROPOSED
├── test_exports_do_not_define_truth.py     # PROPOSED
├── test_crop_mapping_preserves_source.py   # PROPOSED
├── test_field_identity_uncertainty.py      # PROPOSED
├── test_yield_adapter_not_truth.py         # PROPOSED
├── test_aggregation_not_release.py         # PROPOSED
├── test_restricted_detail_not_public.py    # PROPOSED
├── test_no_hidden_lifecycle_writes.py      # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/agriculture/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain restricted field-level or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/domains/agriculture/src/README.md` file;
- identifies this directory as the source root for shared Agriculture package code;
- keeps Agriculture doctrine, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, and release in their own authority roots;
- blocks source modules from becoming doctrine, crop truth, yield truth, field identity authority, policy engine, lifecycle writer, EvidenceBundle creator, release approver, schema authority, contract authority, or public trust membrane;
- defines expected module layout, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future source files under this root are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Agriculture sensitivity, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-AG-SRC-ROOT-001` | Which language/runtime owns `packages/domains/agriculture/src/`? | UNKNOWN |
| `PKG-DOM-AG-SRC-ROOT-002` | Which package manifest controls this source root? | UNKNOWN |
| `PKG-DOM-AG-SRC-ROOT-003` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-DOM-AG-SRC-ROOT-004` | Should generated types live under this source root, under `generated/`, or under a separate generated-code root? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-AG-SRC-ROOT-005` | Which CI workflow validates helper determinism, sensitivity posture, and no hidden lifecycle writes? | UNKNOWN |
| `PKG-DOM-AG-SRC-ROOT-006` | Should field identity helpers live here, in a privacy package, or in a domain pipeline lane? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this source root helper-focused and subordinate to Agriculture governance. Do not add Agriculture doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, restricted field examples, or generated truth claims here.

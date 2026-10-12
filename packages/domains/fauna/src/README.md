<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-fauna-src-readme
title: Fauna Domain Package Source README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <fauna-domain-steward>
  - <sensitivity-steward>
  - <schema-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/fauna/src/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/fauna/README.md
  - packages/domains/fauna/src/fauna/README.md
  - docs/domains/fauna/README.md
  - pipelines/domains/fauna/README.md
  - pipeline_specs/fauna/README.md
  - contracts/domains/fauna/
  - schemas/contracts/v1/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - tests/packages/domains/fauna/
  - fixtures/packages/domains/fauna/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, fauna, src, source-root, shared-library, taxonomy, occurrence, monitoring, range, geoprivacy, sensitivity, validation, governance]
notes:
  - "This README fills the empty packages/domains/fauna/src README with a governed source-root contract."
  - "packages/domains/fauna/src/ may contain source code for the shared Fauna helper package only; it must remain subordinate to packages/domains/fauna/."
  - "fauna/ is the Fauna helper module lane for reusable source-agnostic helpers."
  - "Fauna source code may normalize, parse, map, aggregate, preserve refs, and prepare sensitivity-aware DTOs. It cannot decide occurrence truth, taxonomic authority, policy, lifecycle state, EvidenceBundle closure, or release approval."
  - "Concrete language runtime, package manifests, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Package Source Root

> Source root for the `packages/domains/fauna/` shared Fauna helper library. Code here may provide reusable taxonomy, occurrence, monitoring, range, status, geoprivacy, stewardship, health, validation, and fixture helpers, but it must not become Fauna doctrine, schema authority, contract authority, policy authority, lifecycle writer, EvidenceBundle authority, release authority, taxonomic authority, occurrence-truth authority, or public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Ffauna%2Fsrc%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20root-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Ffauna%2F-d62728)
![sensitivity](https://img.shields.io/badge/sensitive%20occurrence-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/fauna/src/README.md`  
**Parent package:** `packages/domains/fauna/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Fauna helper module:** `packages/domains/fauna/src/fauna/`  
**Domain doctrine root:** `docs/domains/fauna/`  
**Executable domain-pipeline root:** `pipelines/domains/fauna/`  
**Declarative pipeline-spec root:** `pipeline_specs/fauna/`  
**Contract/schema/policy roots:** `contracts/domains/fauna/`, `schemas/contracts/v1/domains/fauna/`, `policy/domains/fauna/`, and `policy/sensitivity/fauna/`  
**Placement posture:** source root for shared Fauna helper code only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.

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

`packages/domains/fauna/src/` may contain source code for the `packages/domains/fauna/` shared helper package.

It may include internal modules for:

- taxonomy and name normalization;
- source-native value and identifier preservation;
- occurrence and monitoring observation parsing;
- range, seasonal-range, movement, and habitat-relation DTO adaptation;
- conservation/legal-status crosswalk preparation that preserves source authority and caveats;
- geoprivacy and sensitivity-transform support that does not approve publication;
- mortality, disease, invasive-species, and stewardship-status helper adapters;
- public-safe aggregation metadata support;
- schema-bound validation adapters and safe errors;
- package entrypoints and internal exports.

It does **not** define Fauna objects, decide occurrence truth, decide taxonomic authority, decide conservation/legal status, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, expose restricted occurrence material, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/fauna/`? | Parent package is the shared Fauna helper-code lane. | CONFIRMED parent package contract |
| Why `src/`? | This is a conventional source root for package implementation, but language/runtime are not yet verified. | PROPOSED / NEEDS VERIFICATION |
| Is this Fauna doctrine? | No. Fauna doctrine and scope belong under `docs/domains/fauna/`. | CONFIRMED boundary posture |
| Is this executable Fauna pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/fauna/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, caveats, sensitivity tier, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> Source code under this root can normalize, parse, map, aggregate, and preserve sensitivity metadata. It cannot turn helper output into occurrence truth, taxonomic authority, policy approval, EvidenceBundle closure, or release approval.

[⬆ Back to top](#top)

---

## 3. Source-root boundary

Allowed direction:

```text
domain app / pipeline / worker / validator / test
  -> packages/domains/fauna/src module
  -> normalized identifiers, parsed observations, mapped DTOs, sensitivity metadata, or validation results
  -> governed pipeline/API/tool handles lifecycle, policy, evidence, geoprivacy, review, and release where authorized
```

Blocked direction:

```text
packages/domains/fauna/src module
  -> direct lifecycle writes
  -> occurrence truth decision
  -> taxonomic authority decision
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
source root -> Fauna doctrine
helper module -> occurrence truth
taxonomy helper -> taxonomic authority
occurrence parser -> occurrence truth
range adapter -> range truth
monitoring adapter -> monitoring truth
status crosswalk -> legal-status authority
geoprivacy helper -> public release approval
redaction metadata -> sensitivity decision
successful source-root test -> lifecycle promotion
```

Required separations:

- reusable source code stays under `packages/domains/fauna/src/`;
- Fauna helper modules stay under `packages/domains/fauna/src/fauna/`;
- Fauna doctrine stays under `docs/domains/fauna/`;
- Fauna meaning stays under `contracts/domains/fauna/`;
- Fauna schemas stay under `schemas/contracts/v1/domains/fauna/`;
- Fauna policy stays under `policy/domains/fauna/` and `policy/sensitivity/fauna/`;
- executable transformations stay under `pipelines/domains/fauna/`;
- declarative run profiles stay under `pipeline_specs/fauna/`;
- lifecycle records and receipts stay under `data/`;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source files include:

- package entrypoints and internal exports;
- taxonomy and name normalization helpers;
- source-native value and identifier preservation helpers;
- occurrence and monitoring observation parsers;
- range, seasonal-range, movement, and habitat-relation DTO adapters;
- conservation/legal-status crosswalk preparation that preserves source authority and caveats;
- geoprivacy and sensitivity-transform support that does not approve publication;
- mortality, disease, invasive-species, and stewardship-status helper adapters;
- public-safe aggregation metadata support;
- schema-bound validation adapters and safe errors;
- deterministic helper ids when policy and schema allow;
- package-only fixture builders.

A good placement test:

> If the file is package source for reusable Fauna helper code and does not decide occurrence truth, taxonomic authority, policy, lifecycle state, evidence closure, or release approval, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Fauna doctrine and source scope docs | `docs/domains/fauna/` |
| Fauna object contracts | `contracts/domains/fauna/` |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` |
| Fauna policy decisions/rules | `policy/domains/fauna/` and `policy/sensitivity/fauna/` |
| Executable Fauna pipelines | `pipelines/domains/fauna/` |
| Declarative Fauna specs | `pipeline_specs/fauna/` |
| Source descriptors | `data/registry/sources/fauna/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Runtime receipts | `data/receipts/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| UI-only rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/fauna/` |
| Package fixtures | `fixtures/packages/domains/fauna/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Expected module layout

Current verified child module:

```text
packages/domains/fauna/src/
├── README.md
└── fauna/
    └── README.md
```

Potential future layout:

```text
packages/domains/fauna/src/
├── index.*                    # PROPOSED
├── fauna/
│   ├── taxonomy.*             # PROPOSED
│   ├── occurrence.*           # PROPOSED
│   ├── monitoring.*           # PROPOSED
│   ├── range.*                # PROPOSED
│   ├── status.*               # PROPOSED
│   ├── geoprivacy.*           # PROPOSED
│   ├── stewardship.*          # PROPOSED
│   ├── health.*               # PROPOSED
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
| Source root | `packages/domains/fauna/src/` | Shared helper source only. |
| Fauna helper module | `packages/domains/fauna/src/fauna/` | Fauna-specific helper module. |
| Package entrypoint | `packages/domains/fauna/` | Language-specific entrypoint is not verified. |
| Domain doctrine | `docs/domains/fauna/` | Scope, sensitivity, and human-facing control plane. |
| Domain contracts | `contracts/domains/fauna/` | Object meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/fauna/` | Machine shape authority. |
| Domain policy | `policy/domains/fauna/`, `policy/sensitivity/fauna/` | Admissibility/geoprivacy authority. |
| Executable pipeline | `pipelines/domains/fauna/` | Runs transformations. |
| Declarative spec | `pipeline_specs/fauna/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/fauna/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/fauna/` | Package validation. |
| Fixtures | `fixtures/packages/domains/fauna/` | No-network synthetic or sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal source-root contract shape

```yaml
source_root_id: kfm.packages.domains.fauna.src
status: draft
authority: package_source_root
not_authority_for:
  - fauna_doctrine
  - taxonomic_authority
  - occurrence_truth
  - range_truth
  - legal_status_authority
  - object_contract
  - schema_home
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - package entrypoints
  - internal modules
  - taxonomy mapping helpers
  - occurrence parser helpers
  - monitoring adapters
  - range and movement adapters
  - status crosswalk helpers
  - geoprivacy helper utilities
  - stewardship reference helpers
  - schema-bound adapters
  - safe fixture builders
required_invariants:
  sensitive_occurrence_denied_by_default: true
  no_occurrence_truth_decision: true
  no_taxonomic_authority_decision: true
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
tests/packages/domains/fauna/
├── test_src_root_boundaries.py              # PROPOSED
├── test_fauna_module_boundaries.py          # PROPOSED
├── test_exports_do_not_define_truth.py      # PROPOSED
├── test_taxonomy_helper_not_authority.py    # PROPOSED
├── test_occurrence_parser_not_truth.py      # PROPOSED
├── test_sensitive_occurrence_not_public.py  # PROPOSED
├── test_geoprivacy_helper_not_release.py    # PROPOSED
├── test_no_hidden_lifecycle_writes.py       # PROPOSED
├── test_no_policy_or_release_decisions.py   # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/fauna/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain sensitive occurrence material, steward-controlled material, or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/domains/fauna/src/README.md` file;
- identifies this directory as the source root for shared Fauna package code;
- keeps Fauna doctrine, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, geoprivacy, review decisions, and release in their own authority roots;
- blocks source modules from becoming doctrine, taxonomic authority, occurrence truth, policy engine, lifecycle writer, EvidenceBundle creator, release approver, schema authority, contract authority, or public trust membrane;
- defines expected module layout, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future source files under this root are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Fauna sensitivity, geoprivacy, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FAUNA-SRC-ROOT-001` | Which language/runtime owns `packages/domains/fauna/src/`? | UNKNOWN |
| `PKG-DOM-FAUNA-SRC-ROOT-002` | Which package manifest controls this source root? | UNKNOWN |
| `PKG-DOM-FAUNA-SRC-ROOT-003` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-DOM-FAUNA-SRC-ROOT-004` | Should generated types live under this source root, under `generated/`, or under a separate generated-code root? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-FAUNA-SRC-ROOT-005` | Which CI workflow validates helper determinism, sensitive-occurrence denial, and no hidden lifecycle writes? | UNKNOWN |
| `PKG-DOM-FAUNA-SRC-ROOT-006` | Should geoprivacy helpers live here, in a policy/sensitivity package, or in a domain pipeline lane? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this source root helper-focused and subordinate to Fauna governance. Do not add Fauna doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive occurrence examples, steward-controlled examples, or generated truth claims here.

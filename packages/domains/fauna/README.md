<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-fauna-readme
title: Fauna Domain Package README
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
path: packages/domains/fauna/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/README.md
  - docs/domains/fauna/README.md
  - packages/README.md
  - packages/domains/README.md
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
tags: [kfm, packages, domains, fauna, biodiversity, wildlife, taxonomy, occurrence, range, monitoring, geoprivacy, sensitivity, shared-library, mapping-helpers, identity-normalizers, observation-parsers, governance]
notes:
  - "This README expands the short packages/domains/fauna scaffold into a governed domain-helper package contract."
  - "packages/domains/fauna/ may contain reusable Fauna helper code only; it is not Fauna doctrine, schema authority, contract authority, policy authority, lifecycle data, executable pipeline logic, evidence closure, or release approval."
  - "Sensitive taxa and sensitive occurrence detail fail closed for public use unless governed geoprivacy transform, review, policy, release, correction, and rollback controls are satisfied elsewhere."
  - "Fauna helper output must preserve source roles, uncertainty, sensitivity tier, geoprivacy transform refs, EvidenceRefs, and review state."
  - "Concrete modules, language runtime, package manifests, exports, build scripts, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Domain Package

> Shared helper-code lane for the Fauna domain: taxonomy helpers, occurrence and monitoring parsers, range and seasonal-range adapters, status crosswalks, geoprivacy helper utilities, sensitivity-aware DTO adapters, and fixture utilities. This package supports governed apps, pipelines, workers, tests, and tools, but it does not define Fauna truth, own schemas/contracts/policy, write lifecycle data, close EvidenceBundles, expose restricted occurrence detail, or approve public release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Ffauna%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20code-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Ffauna%2F-d62728)
![sensitivity](https://img.shields.io/badge/sensitive%20occurrence-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/fauna/README.md`  
**Parent package root:** `packages/domains/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/fauna/`  
**Executable domain-pipeline root:** `pipelines/domains/fauna/`  
**Declarative pipeline-spec root:** `pipeline_specs/fauna/`  
**Contract/schema/policy roots:** `contracts/domains/fauna/`, `schemas/contracts/v1/domains/fauna/`, `policy/domains/fauna/`, and `policy/sensitivity/fauna/`  
**Placement posture:** helper code only. Runtime, exports, package manifest, child modules, and active tests are `NEEDS VERIFICATION` until verified by repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Fauna sensitivity boundary](#3-fauna-sensitivity-boundary)
- [4. Package anti-collapse rules](#4-package-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Expected helper families](#7-expected-helper-families)
- [8. Inputs and outputs](#8-inputs-and-outputs)
- [9. Minimal package contract shape](#9-minimal-package-contract-shape)
- [10. Tests and fixtures](#10-tests-and-fixtures)
- [11. Definition of done](#11-definition-of-done)
- [12. Open questions](#12-open-questions)

---

## 1. Purpose

`packages/domains/fauna/` may contain reusable Fauna helper code that supports KFM domain processing without becoming an authority root.

It may support:

- taxonomic identity and name crosswalk helpers;
- occurrence, observation, monitoring, survey, mortality, disease, and invasive-species DTO adapters;
- range, seasonal-range, movement, and habitat-relation helper payloads;
- conservation and legal-status crosswalk helpers that preserve source role and caveats;
- geoprivacy, redaction, generalization, and sensitivity-transform metadata helpers that do not approve publication;
- source role, source time, valid time, limitation, caveat, sensitivity tier, access state, and review-ref preservation helpers;
- public-safe aggregation helper functions that do not approve release;
- schema-bound validation adapters that call canonical schema tooling;
- no-network fixture builders for tests.

It does **not** define Fauna objects, decide occurrence truth, decide taxonomic authority, decide conservation/legal status, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, expose restricted occurrence detail, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/domains/fauna/`? | Fauna helper code belongs under the packages root when reusable across apps, pipelines, workers, and tests. | CONFIRMED root pattern / NEEDS VERIFICATION for implementation |
| Is this Fauna doctrine? | No. Fauna doctrine and scope belong under `docs/domains/fauna/`. | CONFIRMED boundary posture |
| Is this executable pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/fauna/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, caveats, sensitivity tier, and validation results only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Fauna helper code can normalize, parse, map, aggregate, and preserve sensitivity metadata. It cannot make a fauna claim true, disclose restricted occurrence detail, bypass geoprivacy review, replace EvidenceBundle closure, or approve release.

[⬆ Back to top](#top)

---

## 3. Fauna sensitivity boundary

Fauna data can expose sensitive species, stewardship constraints, and vulnerable ecological contexts. Helper code must preserve these boundaries:

- sensitive taxa and sensitive occurrence detail are denied by default for public surfaces;
- nests, dens, roosts, hibernacula, spawning sites, stewardship-limited records, and exact sensitive occurrence geometry fail closed unless governed review and geoprivacy controls authorize release elsewhere;
- public products require approved redaction, generalization, or geoprivacy transforms outside this package;
- occurrence, range, monitoring, mortality, disease, and invasive-species helper output must preserve source role, uncertainty, sensitivity tier, caveats, and EvidenceRef links;
- habitat, flora, hydrology, hazards, agriculture, land, and archaeology context may inform Fauna but cannot replace Fauna evidence or policy gates;
- helper-derived values and generated interpretations are not evidence by themselves.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
fauna helper -> Fauna doctrine
taxonomy helper -> taxonomic authority
occurrence parser -> occurrence truth
range adapter -> range truth
monitoring adapter -> monitoring truth
status crosswalk -> legal-status authority
geoprivacy helper -> public release approval
redaction metadata -> sensitivity decision
validation helper -> validation pass
successful package test -> lifecycle promotion
```

Required separations:

- helper code stays under `packages/domains/fauna/`;
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

- taxonomy and name-normalization helpers;
- occurrence and monitoring observation parsers;
- range, seasonal-range, movement, and habitat-relation DTO adapters;
- conservation/legal-status crosswalk helpers that preserve source authority and caveats;
- geoprivacy and sensitivity-transform helper utilities that do not approve publication;
- mortality, disease, invasive-species, and stewardship-status helper adapters;
- aggregation helpers that preserve sensitivity and do not create release approval;
- crosswalk helpers that preserve native classifications and source roles;
- schema-generated adapters with generation provenance;
- safe fixture builders and mock helpers for package tests;
- compatibility helpers for Fauna helper migrations.

A good placement test:

> If the file is reusable Fauna helper code and does not decide occurrence truth, taxonomic authority, policy, lifecycle state, evidence closure, or release approval, it may belong here.

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

## 7. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `taxonomy` | Taxonomic name, rank, code, synonym, and source crosswalk helpers. | PROPOSED |
| `occurrence` | Occurrence and observation parsing helpers that preserve uncertainty. | PROPOSED |
| `monitoring` | Survey and monitoring-event DTO adapters. | PROPOSED |
| `range` | Range, seasonal range, and movement helper payloads. | PROPOSED |
| `status` | Conservation/legal-status crosswalk helpers, not status authority. | PROPOSED |
| `geoprivacy` | Redaction/generalization/sensitivity-transform support, not release approval. | PROPOSED |
| `stewardship` | Steward-controlled record reference helpers. | PROPOSED |
| `health` | Mortality, disease, and invasive-species context helpers. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Package-only fixture builders, if accepted by package convention. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/fauna/` | Shared helper source only. |
| Domain doctrine | `docs/domains/fauna/` | Scope, sensitivity, and human-facing control plane. |
| Domain contracts | `contracts/domains/fauna/` | Object meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/fauna/` | Machine shape authority. |
| Domain policy | `policy/domains/fauna/`, `policy/sensitivity/fauna/` | Admissibility/geoprivacy authority. |
| Executable domain pipeline | `pipelines/domains/fauna/` | Runs transformations. |
| Declarative domain spec | `pipeline_specs/fauna/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/fauna/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/fauna/` | Package validation. |
| Fixtures | `fixtures/packages/domains/fauna/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.fauna
status: draft
authority: shared_domain_helper_package
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
├── test_package_boundaries.py                 # PROPOSED
├── test_taxonomy_helper_not_authority.py      # PROPOSED
├── test_occurrence_parser_not_truth.py        # PROPOSED
├── test_sensitive_occurrence_not_public.py    # PROPOSED
├── test_geoprivacy_helper_not_release.py      # PROPOSED
├── test_status_crosswalk_not_authority.py     # PROPOSED
├── test_stewardship_ref_not_review_complete.py # PROPOSED
├── test_no_hidden_lifecycle_writes.py         # PROPOSED
├── test_no_policy_or_release_decisions.py     # PROPOSED
└── test_root_boundary.py                      # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/fauna/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain sensitive occurrence detail, steward-controlled material, or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- replaces the scaffold `packages/domains/fauna/README.md`;
- identifies this path as shared Fauna helper-code space;
- preserves docs, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, geoprivacy, and release roots as separate authorities;
- blocks Fauna helpers from becoming doctrine, schema, contract, policy, lifecycle, evidence, release, occurrence-truth, taxonomic-authority, status-authority, or public-trust authority;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Fauna sensitivity, geoprivacy, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FAUNA-001` | Which language/runtime owns `packages/domains/fauna/`? | UNKNOWN |
| `PKG-DOM-FAUNA-002` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-FAUNA-003` | Which helper modules are actually exported today? | UNKNOWN |
| `PKG-DOM-FAUNA-004` | Which canonical schemas own taxonomy, occurrence, monitoring, range, status, and geoprivacy helper shapes? | NEEDS VERIFICATION |
| `PKG-DOM-FAUNA-005` | Which CI workflow validates sensitive-occurrence denial and no hidden lifecycle writes? | UNKNOWN |
| `PKG-DOM-FAUNA-006` | Should geoprivacy helpers live here, in a policy/sensitivity package, or in a domain pipeline lane? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this package helper-focused and subordinate to Fauna governance. Do not add Fauna doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive occurrence examples, steward-controlled examples, or generated truth claims here.

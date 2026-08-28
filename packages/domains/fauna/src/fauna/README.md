<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-fauna-src-fauna-readme
title: Fauna Domain Package Source Module README
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
path: packages/domains/fauna/src/fauna/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/fauna/README.md
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
tags: [kfm, packages, domains, fauna, src, fauna-module, shared-library, taxonomy, occurrence, monitoring, range, geoprivacy, sensitivity, validation, governance]
notes:
  - "This README fills the empty packages/domains/fauna/src/fauna README with a governed source-module contract."
  - "packages/domains/fauna/src/fauna/ may contain internal source code for shared Fauna helpers only; it must remain subordinate to packages/domains/fauna/."
  - "Fauna source-module helpers can normalize, parse, map, aggregate, preserve refs, and prepare sensitivity-aware DTOs. They cannot decide occurrence truth, taxonomic authority, policy, lifecycle state, EvidenceBundle closure, or release approval."
  - "Sensitive occurrence material fails closed for public use unless governed geoprivacy, review, policy, release, correction, and rollback controls are satisfied elsewhere."
  - "Concrete language runtime, module exports, build scripts, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Source Module

> Internal source-code module area for the `packages/domains/fauna/` shared helper package. This directory may hold reusable Fauna helpers, but it must not become Fauna doctrine, taxonomic authority, occurrence-truth authority, schema authority, policy engine, lifecycle writer, EvidenceBundle authority, release authority, or public trust membrane.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Ffauna%2Fsrc%2Ffauna%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-package%20source%20module-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Ffauna%2F-d62728)
![sensitivity](https://img.shields.io/badge/sensitive%20occurrence-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/fauna/src/fauna/README.md`  
**Parent package:** `packages/domains/fauna/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/fauna/`  
**Executable domain-pipeline root:** `pipelines/domains/fauna/`  
**Declarative pipeline-spec root:** `pipeline_specs/fauna/`  
**Contract/schema/policy roots:** `contracts/domains/fauna/`, `schemas/contracts/v1/domains/fauna/`, `policy/domains/fauna/`, and `policy/sensitivity/fauna/`  
**Placement posture:** source code for reusable Fauna helpers only. Runtime, exports, package manifest, and active tests are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Fauna sensitivity boundary](#3-fauna-sensitivity-boundary)
- [4. Module anti-collapse rules](#4-module-anti-collapse-rules)
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

`packages/domains/fauna/src/fauna/` may hold internal source modules for the shared Fauna helper package.

It may support reusable helpers for:

- taxonomic identity, name, rank, code, synonym, and source crosswalks;
- occurrence, observation, monitoring-event, survey, mortality, disease, and invasive-species DTO adapters;
- range, seasonal-range, movement, and habitat-relation helper payloads;
- conservation and legal-status crosswalk helpers that preserve source role and caveats;
- geoprivacy, redaction, generalization, and sensitivity-transform metadata helpers that do not approve publication;
- source role, source time, valid time, limitation, caveat, sensitivity tier, access state, and review-ref preservation helpers;
- public-safe aggregation helper functions that do not approve release;
- schema-bound validation adapters and safe errors;
- no-network fixture builders for package tests.

It does **not** define Fauna objects, decide occurrence truth, decide taxonomic authority, decide conservation/legal status, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, expose restricted occurrence material, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/fauna/`? | Parent package is the shared Fauna helper-code lane. | CONFIRMED parent package contract |
| Why `src/fauna/`? | This is a plausible internal module path for Fauna-specific helper source. | PROPOSED / NEEDS VERIFICATION |
| Is this Fauna doctrine? | No. Fauna doctrine and scope belong under `docs/domains/fauna/`. | CONFIRMED boundary posture |
| Is this executable Fauna pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/fauna/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, caveats, sensitivity tier, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> Source modules here can normalize, parse, map, aggregate, and preserve sensitivity metadata. They cannot turn helper output into occurrence truth, taxonomic authority, policy approval, EvidenceBundle closure, or release approval.

[⬆ Back to top](#top)

---

## 3. Fauna sensitivity boundary

Fauna helper code must preserve the domain's deny-by-default posture for sensitive taxa and sensitive occurrence material:

- sensitive taxa and sensitive occurrence material are denied by default for public surfaces;
- nests, dens, roosts, hibernacula, spawning sites, stewardship-limited records, and exact sensitive occurrence geometry fail closed unless governed review and geoprivacy controls authorize release elsewhere;
- public products require approved redaction, generalization, or geoprivacy transforms outside this module;
- occurrence, range, monitoring, mortality, disease, and invasive-species helper output must preserve source role, uncertainty, sensitivity tier, caveats, and EvidenceRef links;
- habitat, flora, hydrology, hazards, agriculture, land, and archaeology context may inform Fauna but cannot replace Fauna evidence or policy gates;
- helper-derived values and generated interpretations are not evidence by themselves.

[⬆ Back to top](#top)

---

## 4. Module anti-collapse rules

Disallowed collapses:

```text
source module -> Fauna doctrine
taxonomy helper -> taxonomic authority
occurrence parser -> occurrence truth
range adapter -> range truth
monitoring adapter -> monitoring truth
status crosswalk -> legal-status authority
geoprivacy helper -> public release approval
redaction metadata -> sensitivity decision
validation helper -> validation pass
successful module test -> lifecycle promotion
```

Required separations:

- reusable helper source stays under `packages/domains/fauna/src/fauna/`;
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

Appropriate source modules include helpers for:

- taxonomy and name normalization;
- source-native value and identifier preservation;
- occurrence and monitoring observation parsing;
- range, seasonal-range, movement, and habitat-relation DTO adaptation;
- conservation/legal-status crosswalk preparation that preserves source authority and caveats;
- geoprivacy and sensitivity-transform support that does not approve publication;
- mortality, disease, invasive-species, and stewardship-status helper adapters;
- public-safe aggregation metadata support;
- schema-bound validation adapters and safe errors;
- deterministic helper ids when policy and schema allow;
- package-only fixture builders.

A good placement test:

> If the module is reusable Fauna helper code and does not decide occurrence truth, taxonomic authority, policy, lifecycle state, evidence closure, or release approval, it may belong here.

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
| Tests | `tests/packages/domains/fauna/` |
| Fixtures | `fixtures/packages/domains/fauna/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Expected module families

| Module family | Responsibility | Status |
|---|---|---|
| `taxonomy` | Taxonomic name, rank, code, synonym, and source crosswalk helpers. | PROPOSED |
| `occurrence` | Occurrence and observation parsing helpers that preserve uncertainty. | PROPOSED |
| `monitoring` | Survey and monitoring-event DTO adapters. | PROPOSED |
| `range` | Range, seasonal-range, and movement helper payloads. | PROPOSED |
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
| Module source | `packages/domains/fauna/src/fauna/` | Shared helper source only. |
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

## 9. Minimal module contract shape

```yaml
module_id: kfm.packages.domains.fauna.src.fauna
status: draft
authority: package_source_module
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
├── test_fauna_module_boundaries.py          # PROPOSED
├── test_taxonomy_helper_not_authority.py    # PROPOSED
├── test_occurrence_parser_not_truth.py      # PROPOSED
├── test_sensitive_occurrence_not_public.py  # PROPOSED
├── test_geoprivacy_helper_not_release.py    # PROPOSED
├── test_status_crosswalk_not_authority.py   # PROPOSED
├── test_no_hidden_lifecycle_writes.py       # PROPOSED
├── test_no_policy_or_release_decisions.py   # PROPOSED
├── test_no_evidence_fabrication.py          # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/fauna/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain sensitive occurrence material, steward-controlled material, or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- fills the empty `packages/domains/fauna/src/fauna/README.md` file;
- identifies this directory as package source for shared Fauna helpers;
- keeps Fauna doctrine, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, geoprivacy, review decisions, and release in their own authority roots;
- blocks helper modules from becoming doctrine, taxonomic authority, occurrence truth, policy engine, lifecycle writer, EvidenceBundle creator, release approver, schema authority, contract authority, or public trust membrane;
- defines expected module families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future source files in this module are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Fauna sensitivity, geoprivacy, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FAUNA-SRC-001` | Which language/runtime owns `packages/domains/fauna/src/fauna/`? | UNKNOWN |
| `PKG-DOM-FAUNA-SRC-002` | Which module names are actually exported by the package? | UNKNOWN |
| `PKG-DOM-FAUNA-SRC-003` | Should fixture builders live in source, tests, or `fixtures/packages/domains/fauna/` only? | NEEDS VERIFICATION |
| `PKG-DOM-FAUNA-SRC-004` | Which canonical schemas own taxonomy, occurrence, monitoring, range, status, and geoprivacy helper shapes? | NEEDS VERIFICATION |
| `PKG-DOM-FAUNA-SRC-005` | Which CI workflow validates helper determinism, sensitive-occurrence denial, and no hidden lifecycle writes? | UNKNOWN |
| `PKG-DOM-FAUNA-SRC-006` | Should geoprivacy helpers live here, in a policy/sensitivity package, or in a domain pipeline lane? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this module helper-focused and subordinate to Fauna governance. Do not add Fauna doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive occurrence examples, steward-controlled examples, or generated truth claims here.

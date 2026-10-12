<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-flora-readme
title: Flora Domain Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <flora-domain-steward>
  - <sensitivity-steward>
  - <schema-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/flora/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - packages/README.md
  - packages/domains/README.md
  - pipelines/domains/flora/README.md
  - pipeline_specs/flora/README.md
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - tests/packages/domains/flora/
  - fixtures/packages/domains/flora/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, flora, biodiversity, botany, plants, taxonomy, occurrence, specimen, vegetation, phenology, invasive-plants, geoprivacy, sensitivity, shared-library, mapping-helpers, normalizers, governance]
notes:
  - "This README expands the short packages/domains/flora scaffold into a governed domain-helper package contract."
  - "packages/domains/flora/ may contain reusable Flora helper code only; it is not Flora doctrine, schema authority, contract authority, policy authority, lifecycle data, executable pipeline logic, evidence closure, or release approval."
  - "Rare, protected, culturally sensitive, and steward-reviewed flora location material fails closed for public use unless governed geoprivacy transform, review, policy, release, correction, and rollback controls are satisfied elsewhere."
  - "Flora helper output must preserve source roles, uncertainty, sensitivity tier, geoprivacy transform refs, EvidenceRefs, and review state."
  - "Concrete modules, language runtime, package manifests, exports, build scripts, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Domain Package

> Shared helper-code lane for the Flora domain: plant taxonomy helpers, occurrence and specimen parsers, vegetation-community adapters, invasive-plant and phenology helpers, habitat-relation helpers, geoprivacy utilities, sensitivity-aware DTO adapters, and fixture utilities. This package supports governed apps, pipelines, workers, tests, and tools, but it does not define Flora truth, own schemas/contracts/policy, write lifecycle data, close EvidenceBundles, expose restricted plant-location material, or approve public release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Fflora%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20code-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Fflora%2F-d62728)
![sensitivity](https://img.shields.io/badge/rare%20plant%20geometry-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/flora/README.md`  
**Parent package root:** `packages/domains/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/flora/`  
**Executable domain-pipeline root:** `pipelines/domains/flora/`  
**Declarative pipeline-spec root:** `pipeline_specs/flora/`  
**Contract/schema/policy roots:** `contracts/domains/flora/`, `schemas/contracts/v1/domains/flora/`, `policy/domains/flora/`, and `policy/sensitivity/flora/`  
**Placement posture:** helper code only. Runtime, exports, package manifest, child modules, and active tests are `NEEDS VERIFICATION` until verified by repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Flora sensitivity boundary](#3-flora-sensitivity-boundary)
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

`packages/domains/flora/` may contain reusable Flora helper code that supports KFM domain processing without becoming an authority root.

It may support:

- plant taxonomic identity, name, rank, code, synonym, and source crosswalk helpers;
- occurrence, observation, specimen, plot, vegetation-community, phenology, restoration, and invasive-plant DTO adapters;
- range, distribution, habitat-association, and vegetation-surface helper payloads;
- rare/protected/culturally sensitive flora sensitivity metadata helpers that do not approve publication;
- source role, source time, valid time, limitation, caveat, sensitivity tier, access state, and review-ref preservation helpers;
- geoprivacy, redaction, generalization, and sensitivity-transform metadata helpers that do not approve release;
- public-safe aggregation helper functions that do not replace ReleaseManifest decisions;
- schema-bound validation adapters that call canonical schema tooling;
- no-network fixture builders for tests.

It does **not** define Flora objects, decide occurrence truth, decide taxonomic authority, decide conservation/legal status, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, expose restricted plant-location material, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/domains/flora/`? | Flora helper code belongs under the packages root when reusable across apps, pipelines, workers, and tests. | CONFIRMED root pattern / NEEDS VERIFICATION for implementation |
| Is this Flora doctrine? | No. Flora doctrine and scope belong under `docs/domains/flora/`. | CONFIRMED boundary posture |
| Is this executable pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/flora/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, caveats, sensitivity tier, and validation results only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Flora helper code can normalize, parse, map, aggregate, and preserve sensitivity metadata. It cannot make a botanical claim true, disclose restricted plant-location material, bypass geoprivacy review, replace EvidenceBundle closure, or approve release.

[⬆ Back to top](#top)

---

## 3. Flora sensitivity boundary

Flora data can expose rare, protected, culturally sensitive, steward-reviewed, and vulnerable botanical locations. Helper code must preserve these boundaries:

- rare, protected, culturally sensitive, and steward-reviewed flora material is denied by default for public surfaces when exact or sensitive location detail is involved;
- exact rare-plant geometry, sensitive population locations, seed-source detail, nursery/restoration-sensitive detail, and stewardship-limited records fail closed unless governed review and geoprivacy controls authorize release elsewhere;
- public products require approved redaction, generalization, or geoprivacy transforms outside this package;
- occurrence, specimen, vegetation, invasive-plant, phenology, and restoration helper output must preserve source role, uncertainty, sensitivity tier, caveats, and EvidenceRef links;
- habitat, fauna, soil, hydrology, agriculture, hazards, land, and archaeology context may inform Flora but cannot replace Flora evidence or policy gates;
- helper-derived values and generated interpretations are not evidence by themselves.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
flora helper -> Flora doctrine
taxonomy helper -> taxonomic authority
occurrence parser -> occurrence truth
specimen adapter -> specimen proof
vegetation adapter -> vegetation truth
status crosswalk -> legal-status authority
geoprivacy helper -> public release approval
redaction metadata -> sensitivity decision
validation helper -> validation pass
successful package test -> lifecycle promotion
```

Required separations:

- helper code stays under `packages/domains/flora/`;
- Flora doctrine stays under `docs/domains/flora/`;
- Flora meaning stays under `contracts/domains/flora/`;
- Flora schemas stay under `schemas/contracts/v1/domains/flora/`;
- Flora policy stays under `policy/domains/flora/` and `policy/sensitivity/flora/`;
- executable transformations stay under `pipelines/domains/flora/`;
- declarative run profiles stay under `pipeline_specs/flora/`;
- lifecycle records and receipts stay under `data/`;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate source files include:

- plant taxonomy and name-normalization helpers;
- occurrence, specimen, plot, and vegetation observation parsers;
- range, distribution, habitat-association, and vegetation-community DTO adapters;
- conservation/legal-status crosswalk helpers that preserve source authority and caveats;
- geoprivacy and sensitivity-transform helper utilities that do not approve publication;
- invasive-plant, phenology, restoration, seed-source, and stewardship-status helper adapters;
- aggregation helpers that preserve sensitivity and do not create release approval;
- crosswalk helpers that preserve native classifications and source roles;
- schema-generated adapters with generation provenance;
- safe fixture builders and mock helpers for package tests;
- compatibility helpers for Flora helper migrations.

A good placement test:

> If the file is reusable Flora helper code and does not decide occurrence truth, taxonomic authority, policy, lifecycle state, evidence closure, or release approval, it may belong here.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Flora doctrine and source scope docs | `docs/domains/flora/` |
| Flora object contracts | `contracts/domains/flora/` |
| Flora schemas | `schemas/contracts/v1/domains/flora/` |
| Flora policy decisions/rules | `policy/domains/flora/` and `policy/sensitivity/flora/` |
| Executable Flora pipelines | `pipelines/domains/flora/` |
| Declarative Flora specs | `pipeline_specs/flora/` |
| Source descriptors | `data/registry/sources/flora/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Runtime receipts | `data/receipts/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| UI-only rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/flora/` |
| Package fixtures | `fixtures/packages/domains/flora/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `taxonomy` | Plant taxonomic name, rank, code, synonym, and source crosswalk helpers. | PROPOSED |
| `occurrence` | Occurrence and observation parsing helpers that preserve uncertainty. | PROPOSED |
| `specimen` | Specimen, collection, and voucher DTO adapters. | PROPOSED |
| `vegetation` | Vegetation-community and surface helper payloads. | PROPOSED |
| `range` | Range, distribution, and habitat-association helper payloads. | PROPOSED |
| `status` | Conservation/legal-status crosswalk helpers, not status authority. | PROPOSED |
| `geoprivacy` | Redaction/generalization/sensitivity-transform support, not release approval. | PROPOSED |
| `phenology` | Phenology and seasonal-stage context helpers. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Package-only fixture builders, if accepted by package convention. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/flora/` | Shared helper source only. |
| Domain doctrine | `docs/domains/flora/` | Scope, sensitivity, and human-facing control plane. |
| Domain contracts | `contracts/domains/flora/` | Object meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/flora/` | Machine shape authority. |
| Domain policy | `policy/domains/flora/`, `policy/sensitivity/flora/` | Admissibility/geoprivacy authority. |
| Executable domain pipeline | `pipelines/domains/flora/` | Runs transformations. |
| Declarative domain spec | `pipeline_specs/flora/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/flora/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/flora/` | Package validation. |
| Fixtures | `fixtures/packages/domains/flora/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.flora
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - flora_doctrine
  - taxonomic_authority
  - occurrence_truth
  - specimen_truth
  - vegetation_truth
  - legal_status_authority
  - object_contract
  - schema_home
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - plant taxonomy mapping helpers
  - occurrence parser helpers
  - specimen adapters
  - vegetation community adapters
  - range and habitat association adapters
  - status crosswalk helpers
  - geoprivacy helper utilities
  - phenology helpers
  - schema-bound adapters
  - safe fixture builders
required_invariants:
  sensitive_flora_denied_by_default: true
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
tests/packages/domains/flora/
├── test_package_boundaries.py              # PROPOSED
├── test_taxonomy_helper_not_authority.py   # PROPOSED
├── test_occurrence_parser_not_truth.py     # PROPOSED
├── test_sensitive_flora_not_public.py      # PROPOSED
├── test_geoprivacy_helper_not_release.py   # PROPOSED
├── test_status_crosswalk_not_authority.py  # PROPOSED
├── test_specimen_adapter_not_proof.py      # PROPOSED
├── test_no_hidden_lifecycle_writes.py      # PROPOSED
├── test_no_policy_or_release_decisions.py  # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/flora/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain sensitive flora location material, steward-controlled material, culturally sensitive material, or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- replaces the scaffold `packages/domains/flora/README.md`;
- identifies this path as shared Flora helper-code space;
- preserves docs, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, geoprivacy, and release roots as separate authorities;
- blocks Flora helpers from becoming doctrine, schema, contract, policy, lifecycle, evidence, release, occurrence-truth, taxonomic-authority, status-authority, or public-trust authority;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Flora sensitivity, geoprivacy, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FLORA-001` | Which language/runtime owns `packages/domains/flora/`? | UNKNOWN |
| `PKG-DOM-FLORA-002` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-FLORA-003` | Which helper modules are actually exported today? | UNKNOWN |
| `PKG-DOM-FLORA-004` | Which canonical schemas own taxonomy, occurrence, specimen, vegetation, range, status, geoprivacy, and phenology helper shapes? | NEEDS VERIFICATION |
| `PKG-DOM-FLORA-005` | Which CI workflow validates rare-plant geometry denial and no hidden lifecycle writes? | UNKNOWN |
| `PKG-DOM-FLORA-006` | Should geoprivacy helpers live here, in a policy/sensitivity package, or in a domain pipeline lane? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this package helper-focused and subordinate to Flora governance. Do not add Flora doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive plant-location examples, steward-controlled examples, or generated truth claims here.

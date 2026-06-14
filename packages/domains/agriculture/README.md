<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-agriculture-readme
title: Agriculture Domain Package README
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
path: packages/domains/agriculture/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/README.md
  - docs/domains/agriculture/README.md
  - packages/README.md
  - packages/domains/README.md
  - pipelines/domains/agriculture/README.md
  - pipeline_specs/agriculture/README.md
  - contracts/domains/agriculture/
  - schemas/contracts/v1/domains/agriculture/
  - policy/domains/agriculture/
  - tests/packages/domains/agriculture/
  - fixtures/packages/domains/agriculture/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, agriculture, shared-library, mapping-helpers, identity-normalizers, observation-parsers, crop, field, yield, irrigation, conservation, privacy, governance]
notes:
  - "This README expands the short packages/domains/agriculture scaffold into a governed domain-helper package contract."
  - "packages/domains/agriculture/ may contain reusable Agriculture helper code only; it is not Agriculture doctrine, schema authority, contract authority, policy authority, lifecycle data, executable pipeline logic, evidence closure, or release approval."
  - "Field polygons, operator identities, private joins, source-rights-limited datasets, and field-level products are denied by default for public use unless explicit rights, sensitivity review, and release controls are satisfied."
  - "Crop/yield/suitability/stress/irrigation helpers preserve source roles and uncertainty; they do not make crop, yield, field, or operator claims true."
  - "Concrete modules, language runtime, package manifests, exports, build scripts, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Domain Package

> Shared helper-code lane for the Agriculture domain: mapping helpers, identity normalizers, observation parsers, crop/yield/field DTO adapters, aggregation helpers, suitability/stress helper types, and fixture utilities. This package supports governed apps, pipelines, workers, tests, and tools, but it does not define Agriculture truth, own schemas/contracts/policy, write lifecycle data, close EvidenceBundles, or approve public release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Fagriculture%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20code-0a7ea4)
![domain](https://img.shields.io/badge/domain-doctrine%20in%20docs%2Fdomains%2Fagriculture%2F-d62728)
![sensitivity](https://img.shields.io/badge/field%20%2F%20operator-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/agriculture/README.md`  
**Parent package root:** `packages/domains/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/agriculture/`  
**Executable domain-pipeline root:** `pipelines/domains/agriculture/`  
**Declarative pipeline-spec root:** `pipeline_specs/agriculture/`  
**Contract/schema/policy roots:** `contracts/domains/agriculture/`, `schemas/contracts/v1/domains/agriculture/`, and `policy/domains/agriculture/`  
**Placement posture:** helper code only. Runtime, exports, package manifest, child modules, and active tests are `NEEDS VERIFICATION` until verified by repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Agriculture sensitivity boundary](#3-agriculture-sensitivity-boundary)
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

`packages/domains/agriculture/` may contain reusable Agriculture helper code that supports KFM domain processing without becoming an authority root.

It may support:

- crop observation mapping helpers;
- field or management-unit identity normalization helpers that preserve uncertainty;
- yield, rotation, irrigation, stress, suitability, and conservation helper adapters;
- source-to-domain DTO mapping helpers;
- aggregation and public-safe representation helpers;
- source role, source time, valid time, and limitation preservation helpers;
- schema-bound validation adapters that call canonical schema tooling;
- no-network fixture builders for tests.

It does **not** define Agriculture objects, decide crop/yield truth, identify private operators for public surfaces, decide policy, create EvidenceBundles, write lifecycle data, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/domains/agriculture/`? | Agriculture helper code belongs under the packages root when reusable across apps, pipelines, workers, and tests. | CONFIRMED root pattern / NEEDS VERIFICATION for implementation |
| Is this Agriculture doctrine? | No. Agriculture doctrine and scope belong under `docs/domains/agriculture/`. | CONFIRMED boundary posture |
| Is this executable pipeline logic? | No. Executable domain transformation logic belongs under `pipelines/domains/agriculture/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, or release? | No. It may preserve refs and validation results only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Agriculture helper code can normalize, map, aggregate, and translate. It cannot turn a field-level observation into public truth, bypass rights review, publish operator-sensitive data, or replace EvidenceBundle closure.

[⬆ Back to top](#top)

---

## 3. Agriculture sensitivity boundary

Agriculture is rights- and privacy-sensitive. Helper code must preserve these boundaries:

- field polygons and field-level joins are not public by default;
- operator identities, private owner/operator joins, and source-rights-limited datasets are denied by default for public surfaces;
- public products should use approved aggregation/generalization thresholds;
- crop, yield, stress, suitability, irrigation, conservation, and economics helpers must preserve source role, source time, valid time, limitations, and confidence state;
- generated helper output is not evidence;
- public release requires evidence, policy, review, release manifest, correction path, and rollback posture outside this package.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
agriculture helper -> Agriculture doctrine
field normalizer -> field identity authority
crop parser -> crop truth
yield adapter -> yield truth
aggregation helper -> public release approval
suitability helper -> land-use decision authority
irrigation helper -> water-right truth
operator field -> public person/business disclosure
validation helper -> validation pass
successful package test -> lifecycle promotion
```

Required separations:

- helper code stays under `packages/domains/agriculture/`;
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

- crop/source mapping helpers;
- field identity normalization helpers that keep provenance and uncertainty explicit;
- yield, rotation, stress, irrigation, conservation, suitability, and economics DTO adapters;
- aggregation and redaction helper functions that do not approve publication;
- crosswalk helpers that preserve native classifications and source roles;
- schema-generated adapters with generation provenance;
- safe fixture builders and mock helpers for package tests;
- compatibility helpers for Agriculture helper migrations.

A good placement test:

> If the file is reusable Agriculture helper code and does not decide crop/yield/field/operator truth, write lifecycle data, decide policy, or approve release, it may belong here.

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

## 7. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `crop` | Crop code/name mapping and source-role-preserving crop observation helpers. | PROPOSED |
| `field_identity` | Field/management-unit identity helpers with uncertainty and provenance. | PROPOSED |
| `yield` | Yield DTO adapters and limitation preservation. | PROPOSED |
| `rotation` | Crop rotation and temporal sequence helpers. | PROPOSED |
| `irrigation` | Irrigation observation adapters, not water-right truth. | PROPOSED |
| `suitability` | Suitability/stress/conservation helper adapters with caveats. | PROPOSED |
| `aggregation` | Public-safe aggregation/redaction support, not publication approval. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Package-only fixture builders, if accepted by package convention. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 8. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/agriculture/` | Shared helper source only. |
| Domain doctrine | `docs/domains/agriculture/` | Scope, sensitivity, and human-facing control plane. |
| Domain contracts | `contracts/domains/agriculture/` | Object meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/agriculture/` | Machine shape authority. |
| Domain policy | `policy/domains/agriculture/` | Admissibility/exposure authority. |
| Executable domain pipeline | `pipelines/domains/agriculture/` | Runs transformations. |
| Declarative domain spec | `pipeline_specs/agriculture/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/agriculture/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/agriculture/` | Package validation. |
| Fixtures | `fixtures/packages/domains/agriculture/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 9. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.agriculture
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - agriculture_doctrine
  - object_contract
  - schema_home
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
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
  field_and_operator_public_denied_by_default: true
  helper_output_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 10. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/agriculture/
├── test_package_boundaries.py              # PROPOSED
├── test_crop_mapping_preserves_source.py   # PROPOSED
├── test_field_identity_uncertainty.py      # PROPOSED
├── test_yield_adapter_not_truth.py         # PROPOSED
├── test_aggregation_not_release.py         # PROPOSED
├── test_no_operator_public_disclosure.py   # PROPOSED
├── test_no_hidden_lifecycle_writes.py      # PROPOSED
├── test_no_policy_or_release_decisions.py  # PROPOSED
├── test_generated_types_match_schema.py    # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/agriculture/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain sensitive field-level, operator-level, private-property, or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 11. Definition of done

This README is done when it:

- expands the scaffold `packages/domains/agriculture/README.md`;
- identifies this path as shared Agriculture helper-code space;
- preserves docs, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, and release roots as separate authorities;
- blocks Agriculture helpers from becoming doctrine, schema, contract, policy, lifecycle, evidence, release, crop/yield truth, field identity authority, or public-trust authority;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Agriculture sensitivity, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-AG-001` | Which language/runtime owns `packages/domains/agriculture/`? | UNKNOWN |
| `PKG-DOM-AG-002` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-AG-003` | Which helper modules are actually exported today? | UNKNOWN |
| `PKG-DOM-AG-004` | Which canonical schemas own crop, field, yield, rotation, irrigation, suitability, and stress helper shapes? | NEEDS VERIFICATION |
| `PKG-DOM-AG-005` | Which CI workflow validates Agriculture helper packages and privacy boundaries? | UNKNOWN |
| `PKG-DOM-AG-006` | Should field identity helpers live here, in a privacy package, or in a domain pipeline lane? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this package helper-focused and subordinate to Agriculture governance. Do not add Agriculture doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive field/operator examples, private-property joins, or generated truth claims here.

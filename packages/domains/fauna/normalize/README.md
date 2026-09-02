<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-fauna-normalize-readme
title: Fauna Normalize Package README
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
path: packages/domains/fauna/normalize/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/fauna/README.md
  - packages/domains/fauna/identity/README.md
  - docs/domains/fauna/README.md
  - pipelines/domains/fauna/README.md
  - pipeline_specs/fauna/README.md
  - contracts/domains/fauna/
  - schemas/contracts/v1/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - tests/packages/domains/fauna/normalize/
  - fixtures/packages/domains/fauna/normalize/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, fauna, normalize, normalization, taxonomy, occurrence, monitoring, range, status, geoprivacy, sensitivity, crosswalk, validation, governance]
notes:
  - "This README fills the empty fauna normalize package file with a governed helper-package contract."
  - "normalize is a shared helper package for Fauna normalization support; it is not taxonomic authority, occurrence truth, schema authority, policy authority, or lifecycle authority."
  - "Normalization helpers must preserve source-native values, uncertainty, source role, sensitivity tier, geoprivacy transform refs, review refs, policy refs, and EvidenceRef links."
  - "Sensitive occurrence material fails closed for public use unless governed geoprivacy, review, policy, and release controls are satisfied elsewhere."
  - "Concrete code exports, language runtime, package manifest, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Normalize Package

> Shared helper package for Fauna normalization support: taxon-name normalization, source-native value preservation, occurrence and monitoring value normalization, status crosswalk preparation, unit and vocabulary adapters, sensitivity-aware normalization, and fixture utilities. It must not decide taxonomic authority, occurrence truth, legal-status authority, policy, lifecycle promotion, EvidenceBundle closure, or release approval.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Ffauna%2Fnormalize%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20package-0a7ea4)
![normalize](https://img.shields.io/badge/normalizer-not%20authority-d62728)
![sensitivity](https://img.shields.io/badge/sensitive%20occurrence-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/fauna/normalize/README.md`  
**Parent package:** `packages/domains/fauna/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/fauna/`  
**Executable domain-pipeline root:** `pipelines/domains/fauna/`  
**Declarative pipeline-spec root:** `pipeline_specs/fauna/`  
**Contract/schema/policy roots:** `contracts/domains/fauna/`, `schemas/contracts/v1/domains/fauna/`, `policy/domains/fauna/`, and `policy/sensitivity/fauna/`  
**Placement posture:** helper package for Fauna normalization only. Runtime, exports, package manifest, active tests, and implementation are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Normalization boundary](#3-normalization-boundary)
- [4. Sensitivity and publication boundary](#4-sensitivity-and-publication-boundary)
- [5. Anti-collapse rules](#5-anti-collapse-rules)
- [6. What belongs here](#6-what-belongs-here)
- [7. What does not belong here](#7-what-does-not-belong-here)
- [8. Expected helper families](#8-expected-helper-families)
- [9. Inputs and outputs](#9-inputs-and-outputs)
- [10. Minimal package contract shape](#10-minimal-package-contract-shape)
- [11. Tests and fixtures](#11-tests-and-fixtures)
- [12. Definition of done](#12-definition-of-done)
- [13. Open questions](#13-open-questions)

---

## 1. Purpose

`packages/domains/fauna/normalize/` may contain reusable helper code for normalizing Fauna values without becoming an authority root.

It may support:

- taxonomic name, rank, code, synonym, and source vocabulary normalization helpers;
- source-native value preservation helpers;
- occurrence, observation, monitoring-event, survey, range, seasonal-range, and movement value normalizers;
- units, counts, life stage, sex, behavior, observation method, evidence type, and confidence value normalization helpers;
- conservation/legal-status crosswalk preparation helpers that preserve source authority and caveats;
- geoprivacy, sensitivity tier, review, policy, and EvidenceRef preservation helpers;
- schema-bound validation adapters and safe errors;
- no-network fixture builders for tests.

It does **not** decide taxonomic authority, occurrence truth, range truth, legal-status authority, canonical identity, policy, EvidenceBundle creation, lifecycle writes, public release, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/fauna/`? | Normalization helpers are reusable Fauna package code, not a new authority root. | CONFIRMED parent root pattern / NEEDS VERIFICATION for implementation |
| Is this a taxonomic authority package? | No. It may normalize and crosswalk names while preserving source authority and uncertainty. | CONFIRMED boundary posture |
| Is this Fauna doctrine? | No. Fauna doctrine and scope belong under `docs/domains/fauna/`. | CONFIRMED boundary posture |
| Can this decide occurrence truth or status truth? | No. It may prepare normalized values and caveats only. | CONFIRMED normalization boundary |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, uncertainty, sensitivity tier, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> A normalized value is not a truth decision. Normalization may improve consistency, but source-native values, uncertainty, caveats, and EvidenceRef links must remain available for governed review.

[⬆ Back to top](#top)

---

## 3. Normalization boundary

Allowed direction:

```text
source-native value / taxon label / observation field / EvidenceRef / review refs / policy refs
  -> fauna normalize helper
  -> normalized value, source-native echo, caveat, confidence, and validation payload
  -> governed pipeline/review flow handles admissibility, identity, evidence, lifecycle, and release where authorized
```

Blocked direction:

```text
normalize helper
  -> taxonomic authority decision
  -> occurrence truth decision
  -> legal-status authority
  -> canonical identity registry write
  -> sensitive detail exposure
  -> policy decision
  -> EvidenceBundle creation
  -> lifecycle promotion
  -> release approval
```

Normalization helpers should be deterministic where practical, preserve source-native values, and keep uncertainty explicit. They should prefer review-ready normalized payloads over authoritative assertions.

[⬆ Back to top](#top)

---

## 4. Sensitivity and publication boundary

Fauna normalization has elevated exposure risk when sensitive taxa or sensitive occurrence context is involved. This package must preserve these boundaries:

- sensitive taxa and sensitive occurrence material are not public by default;
- normalized values must not expose restricted occurrence detail, steward-controlled context, or source-rights-limited detail;
- normalized candidate occurrence values remain candidate values unless confirmed through governed review and evidence;
- geoprivacy transform refs and sensitivity tiers must be preserved rather than discarded;
- missing or inaccessible EvidenceBundle, geoprivacy transform, review, policy, or release state should produce abstain/deny-safe outcomes, not fabricated confidence;
- RedactionReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, and rollback posture remain outside this package.

[⬆ Back to top](#top)

---

## 5. Anti-collapse rules

Disallowed collapses:

```text
normalizer -> authority
normalized taxon name -> accepted taxonomy
normalized occurrence value -> occurrence truth
normalized status -> legal-status authority
unit conversion -> measurement truth
crosswalk match -> source authority
sensitivity metadata -> policy approval
public-safe flag -> release approval
EvidenceRef -> EvidenceBundle closure
successful package test -> lifecycle promotion
```

Required separations:

- normalize helper code stays under `packages/domains/fauna/normalize/`;
- Fauna doctrine stays under `docs/domains/fauna/`;
- object meaning stays under `contracts/domains/fauna/`;
- schemas stay under `schemas/contracts/v1/domains/fauna/`;
- policy and sensitivity rules stay under `policy/domains/fauna/` and `policy/sensitivity/fauna/`;
- lifecycle records and writes stay under governed data/pipeline roots;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 6. What belongs here

Appropriate source files include:

- taxonomic name and code normalization helpers;
- source-native value preservation helpers;
- occurrence, observation, monitoring, survey, range, and movement normalizers;
- unit, count, life-stage, sex, behavior, method, evidence-type, and confidence value adapters;
- conservation/legal-status crosswalk preparation helpers that preserve source authority and caveats;
- geoprivacy-transform-ref, sensitivity-tier, review-ref, policy-ref, and EvidenceRef preservation helpers;
- schema-bound validation adapters and safe errors;
- deterministic helper ids when policy and schema allow;
- synthetic or sanitized fixture builders.

A good placement test:

> If the file is reusable normalization support code that preserves source/evidence/governance refs and does not decide taxonomy, occurrence truth, lifecycle state, policy, or release approval, it may belong here.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Taxonomic authority decisions | governed review/pipeline roots or accepted authority crosswalk roots |
| Canonical identity registry records | governed data/catalog/triplet roots or approved registry homes |
| EvidenceBundle storage or creation | `data/proofs/evidence_bundle/` and proof tooling |
| Fauna doctrine and source scope docs | `docs/domains/fauna/` |
| Fauna object contracts | `contracts/domains/fauna/` |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` |
| Fauna policy decisions/rules | `policy/domains/fauna/` and `policy/sensitivity/fauna/` |
| Executable normalization pipeline | `pipelines/domains/fauna/` or accepted executable lane |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Review decisions | policy/review authority roots |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| Public map/UI rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/fauna/normalize/` |
| Package fixtures | `fixtures/packages/domains/fauna/normalize/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 8. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `taxonomy` | Taxonomic name, rank, code, synonym, and source vocabulary normalization. | PROPOSED |
| `source_values` | Source-native value preservation and echo helpers. | PROPOSED |
| `occurrence` | Occurrence and observation value normalization. | PROPOSED |
| `monitoring` | Monitoring-event and survey value normalization. | PROPOSED |
| `range` | Range, seasonal-range, and movement value normalization. | PROPOSED |
| `status` | Conservation/legal-status crosswalk preparation, not authority. | PROPOSED |
| `units` | Unit and count normalization with caveats. | PROPOSED |
| `geoprivacy_refs` | Geoprivacy transform, review, policy, and sensitivity-ref preservation. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Synthetic/sanitized fixture builders. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/fauna/normalize/` | Shared normalization helper code only. |
| Parent helper package | `packages/domains/fauna/` | Domain helper parent. |
| Domain doctrine | `docs/domains/fauna/` | Scope and sensitivity posture. |
| Domain contracts | `contracts/domains/fauna/` | Meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/fauna/` | Machine shape authority. |
| Domain policy | `policy/domains/fauna/`, `policy/sensitivity/fauna/` | Admissibility/geoprivacy authority. |
| Canonical lifecycle records | `data/<phase>/fauna/` | Not written here as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/fauna/normalize/` | Package validation. |
| Fixtures | `fixtures/packages/domains/fauna/normalize/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 10. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.fauna.normalize
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - taxonomic_authority
  - occurrence_truth
  - legal_status_authority
  - canonical_identity_registry
  - fauna_doctrine
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - taxon name and code normalizers
  - source-native value preservation
  - occurrence value normalizers
  - monitoring and range value normalizers
  - status crosswalk preparation
  - unit and count adapters
  - geoprivacy and sensitivity reference helpers
  - schema-bound adapters
  - synthetic fixture builders
required_invariants:
  no_taxonomic_authority_decision: true
  no_occurrence_truth_decision: true
  no_legal_status_authority_decision: true
  source_native_values_preserved: true
  no_sensitive_detail_exposure: true
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  normalized_output_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 11. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/fauna/normalize/
├── test_normalize_package_boundaries.py       # PROPOSED
├── test_taxon_normalizer_not_authority.py     # PROPOSED
├── test_source_native_values_preserved.py     # PROPOSED
├── test_occurrence_normalizer_not_truth.py    # PROPOSED
├── test_status_crosswalk_not_authority.py     # PROPOSED
├── test_sensitive_occurrence_not_public.py    # PROPOSED
├── test_no_hidden_lifecycle_writes.py         # PROPOSED
├── test_no_evidence_fabrication.py            # PROPOSED
├── test_no_release_approval.py                # PROPOSED
└── test_root_boundary.py                      # PROPOSED
```

Fixtures should live in `fixtures/packages/domains/fauna/normalize/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not expose sensitive occurrence material, steward-controlled material, or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the empty `packages/domains/fauna/normalize/README.md` file;
- identifies this path as shared Fauna normalization helper-code space;
- keeps taxonomic decisions, occurrence truth, legal-status decisions, doctrine, contracts, schemas, policy, lifecycle data, evidence, review decisions, and release decisions in their authority roots;
- blocks normalizers from becoming taxonomic authority, occurrence truth, legal-status authority, policy approval, lifecycle promotion, EvidenceBundle creation, canonical identity write, or release approval;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Fauna sensitivity, geoprivacy, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FAUNA-NORM-001` | Which language/runtime owns `packages/domains/fauna/normalize/`? | UNKNOWN |
| `PKG-DOM-FAUNA-NORM-002` | Which canonical schema owns taxon labels, occurrence values, status crosswalk values, and normalization caveats? | NEEDS VERIFICATION |
| `PKG-DOM-FAUNA-NORM-003` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-FAUNA-NORM-004` | Which CI workflow validates normalizer-not-authority and sensitive-occurrence-denial rules? | UNKNOWN |
| `PKG-DOM-FAUNA-NORM-005` | Should canonical taxonomy resolution live in a domain pipeline, catalog package, or dedicated authority adapter? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-FAUNA-NORM-006` | Which source vocabularies and unit mappings are canonical versus source-specific crosswalk inputs? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package helper-focused and subordinate to Fauna normalization governance. Do not add taxonomic authority decisions, occurrence truth decisions, legal-status decisions, canonical identity registry writes, sensitive-detail publication, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive occurrence examples, steward-controlled examples, or generated truth claims here.

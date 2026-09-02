<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-fauna-identity-readme
title: Fauna Identity Package README
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
path: packages/domains/fauna/identity/README.md
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
  - tests/packages/domains/fauna/identity/
  - fixtures/packages/domains/fauna/identity/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, fauna, identity, taxonomy, occurrence-identity, monitoring-identity, range-identity, geoprivacy, sensitivity, deterministic-identity, governance]
notes:
  - "This README fills the empty fauna identity package file with a governed helper-package contract."
  - "identity is a shared helper package for Fauna identity-key and identity-normalization support; it is not taxonomic authority, occurrence truth, or canonical identity registry authority."
  - "Identity helpers must preserve uncertainty, source role, sensitivity tier, geoprivacy transform refs, review refs, policy refs, and EvidenceRef links."
  - "Sensitive occurrence material fails closed for public use unless governed geoprivacy, review, policy, and release controls are satisfied elsewhere."
  - "Concrete code exports, language runtime, package manifest, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Identity Package

> Shared helper package for Fauna identity support: taxonomy-key helpers, occurrence identity helpers, monitoring-event identity helpers, range and seasonal-range identity helpers, source crosswalk helpers, duplicate-candidate payloads, public-safe alias helpers, and fixture utilities. It must not decide taxonomic authority, occurrence truth, canonical identity, policy, lifecycle promotion, EvidenceBundle closure, or release approval.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Ffauna%2Fidentity%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20package-0a7ea4)
![identity](https://img.shields.io/badge/identity-helper%20not%20authority-d62728)
![sensitivity](https://img.shields.io/badge/sensitive%20occurrence-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/fauna/identity/README.md`  
**Parent package:** `packages/domains/fauna/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/fauna/`  
**Executable domain-pipeline root:** `pipelines/domains/fauna/`  
**Declarative pipeline-spec root:** `pipeline_specs/fauna/`  
**Contract/schema/policy roots:** `contracts/domains/fauna/`, `schemas/contracts/v1/domains/fauna/`, `policy/domains/fauna/`, and `policy/sensitivity/fauna/`  
**Placement posture:** helper package for Fauna identity normalization only. Runtime, exports, package manifest, active tests, and implementation are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Identity boundary](#3-identity-boundary)
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

`packages/domains/fauna/identity/` may contain reusable helper code for normalizing and comparing Fauna identity references without becoming an authority root.

It may support:

- taxonomic name, rank, code, synonym, and source crosswalk helper keys;
- occurrence, observation, monitoring-event, survey, range, seasonal-range, and movement identity helpers;
- source-native identifier preservation helpers;
- duplicate-candidate and review-candidate payload helpers;
- public-safe alias id helpers;
- sensitivity tier, geoprivacy transform, review, policy, and EvidenceRef preservation helpers;
- schema-bound validation adapters and safe errors;
- no-network fixture builders for tests.

It does **not** decide taxonomic authority, occurrence truth, range truth, legal-status authority, canonical identity, merge/split decisions, policy, EvidenceBundle creation, lifecycle writes, public release, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/fauna/`? | Identity helpers are reusable Fauna package code, not a new authority root. | CONFIRMED parent root pattern / NEEDS VERIFICATION for implementation |
| Is this the canonical identity registry? | No. It may produce helper keys and candidate payloads only; canonical registry and lifecycle authority stay outside this package. | CONFIRMED boundary posture |
| Is this Fauna doctrine? | No. Fauna doctrine and scope belong under `docs/domains/fauna/`. | CONFIRMED boundary posture |
| Can this decide occurrence truth or taxonomy? | No. It may suggest deterministic helper keys or identity candidates only. | CONFIRMED identity boundary |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, uncertainty, sensitivity tier, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> A Fauna identity helper is not identity authority. A deterministic key, normalized identifier, duplicate candidate, or public-safe alias remains downstream of source role, evidence, geoprivacy, review, policy, lifecycle, and release state.

[⬆ Back to top](#top)

---

## 3. Identity boundary

Allowed direction:

```text
source-native id / taxon id / occurrence id / EvidenceRef / review refs / policy refs
  -> fauna identity helper
  -> deterministic helper key, normalized id payload, duplicate candidate, or public-safe alias id
  -> governed pipeline/review flow handles canonical identity and lifecycle state where authorized
```

Blocked direction:

```text
identity helper
  -> taxonomic authority decision
  -> occurrence truth decision
  -> canonical identity registry write
  -> merge/split decision
  -> sensitive detail exposure
  -> policy decision
  -> EvidenceBundle creation
  -> lifecycle promotion
  -> release approval
```

Identity helpers should be deterministic where practical, preserve source-native identifiers, and keep uncertainty explicit. They should prefer review-ready identity candidates over authoritative assertions.

[⬆ Back to top](#top)

---

## 4. Sensitivity and publication boundary

Fauna identity handling has elevated exposure risk when sensitive taxa or sensitive occurrence context is involved. This package must preserve these boundaries:

- sensitive taxa and sensitive occurrence material are not public by default;
- identity keys must not expose sensitive biological context, steward-controlled context, or source-rights-limited detail;
- candidate occurrence identities remain candidate identities unless confirmed through governed review and evidence;
- public-safe alias ids must not reveal restricted internal identifiers without authorized context;
- missing or inaccessible EvidenceBundle, geoprivacy transform, review, policy, or release state should produce abstain/deny-safe outcomes, not fabricated identity confidence;
- geoprivacy transform, RedactionReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, and rollback posture remain outside this package.

[⬆ Back to top](#top)

---

## 5. Anti-collapse rules

Disallowed collapses:

```text
identity helper -> identity authority
taxonomy key -> taxonomic authority
normalized source id -> canonical KFM id
occurrence key -> occurrence truth
duplicate candidate -> merge decision
split candidate -> split decision
public-safe alias id -> release approval
review ref -> review completion
EvidenceRef -> EvidenceBundle closure
successful package test -> lifecycle promotion
```

Required separations:

- identity helper code stays under `packages/domains/fauna/identity/`;
- Fauna doctrine stays under `docs/domains/fauna/`;
- object meaning stays under `contracts/domains/fauna/`;
- schemas stay under `schemas/contracts/v1/domains/fauna/`;
- policy and sensitivity rules stay under `policy/domains/fauna/` and `policy/sensitivity/fauna/`;
- canonical lifecycle identities and record writes stay under governed data/pipeline roots;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 6. What belongs here

Appropriate source files include:

- deterministic helper-key utilities;
- taxonomic id and name normalization helpers;
- source-native id normalization helpers;
- occurrence, observation, monitoring-event, range, and movement identity-key helpers;
- identity crosswalk helpers that preserve native identifiers and uncertainty;
- duplicate-candidate helper payloads;
- merge/split proposal payload helpers that do not decide merges/splits;
- public-safe alias id helper utilities;
- review-ref, geoprivacy-transform-ref, sensitivity-tier, and EvidenceRef preservation helpers;
- schema-bound validation adapters and safe errors;
- synthetic or sanitized fixture builders.

A good placement test:

> If the file is reusable identity support code that preserves source/evidence/governance refs and does not decide taxonomy, occurrence truth, lifecycle state, policy, or release approval, it may belong here.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Canonical identity registry records | governed data/catalog/triplet roots or approved registry homes |
| Merge/split decision workflows | governed pipeline/review workflow roots |
| EvidenceBundle storage or creation | `data/proofs/evidence_bundle/` and proof tooling |
| Fauna doctrine and source scope docs | `docs/domains/fauna/` |
| Fauna object contracts | `contracts/domains/fauna/` |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` |
| Fauna policy decisions/rules | `policy/domains/fauna/` and `policy/sensitivity/fauna/` |
| Executable identity-resolution pipeline | `pipelines/domains/fauna/` or accepted executable lane |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Review decisions | policy/review authority roots |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| Public map/UI rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/fauna/identity/` |
| Package fixtures | `fixtures/packages/domains/fauna/identity/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 8. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `taxon_keys` | Deterministic helper keys for taxon references without becoming authority. | PROPOSED |
| `source_ids` | Source-native id normalization and preservation. | PROPOSED |
| `occurrence_ids` | Occurrence and observation identity helpers. | PROPOSED |
| `monitoring_ids` | Monitoring-event and survey identity helpers. | PROPOSED |
| `range_ids` | Range, seasonal-range, and movement identity helper payloads. | PROPOSED |
| `duplicates` | Duplicate-candidate helper payloads. | PROPOSED |
| `aliases` | Public-safe alias id helpers. | PROPOSED |
| `geoprivacy_refs` | Geoprivacy transform, review, policy, and sensitivity-ref preservation. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Synthetic/sanitized fixture builders. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/fauna/identity/` | Shared identity helper code only. |
| Parent helper package | `packages/domains/fauna/` | Domain helper parent. |
| Domain doctrine | `docs/domains/fauna/` | Scope and sensitivity posture. |
| Domain contracts | `contracts/domains/fauna/` | Meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/fauna/` | Machine shape authority. |
| Domain policy | `policy/domains/fauna/`, `policy/sensitivity/fauna/` | Admissibility/geoprivacy authority. |
| Canonical lifecycle records | `data/<phase>/fauna/` | Not written here as hidden behavior. |
| Catalog/triplet records | `data/catalog/`, `data/triplets/` | Not written here as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/fauna/identity/` | Package validation. |
| Fixtures | `fixtures/packages/domains/fauna/identity/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 10. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.fauna.identity
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - canonical_identity_registry
  - taxonomic_authority
  - occurrence_truth
  - merge_decision
  - split_decision
  - fauna_doctrine
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - deterministic helper-key utilities
  - taxon id and name normalizers
  - source-native id normalizers
  - occurrence identity helper payloads
  - monitoring and range identity helper payloads
  - duplicate-candidate helpers
  - public-safe alias id helpers
  - geoprivacy and sensitivity reference helpers
  - schema-bound adapters
  - synthetic fixture builders
required_invariants:
  no_taxonomic_authority_decision: true
  no_occurrence_truth_decision: true
  no_canonical_identity_write: true
  no_merge_or_split_decision: true
  no_sensitive_detail_exposure: true
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  identity_helper_output_is_not_authority: true
```

[⬆ Back to top](#top)

---

## 11. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/fauna/identity/
├── test_identity_package_boundaries.py       # PROPOSED
├── test_taxon_key_not_authority.py           # PROPOSED
├── test_source_id_not_canonical_id.py        # PROPOSED
├── test_occurrence_id_not_truth.py           # PROPOSED
├── test_duplicate_candidate_not_merge.py     # PROPOSED
├── test_alias_is_public_safe.py              # PROPOSED
├── test_sensitive_occurrence_not_public.py   # PROPOSED
├── test_no_hidden_lifecycle_writes.py        # PROPOSED
├── test_no_release_approval.py               # PROPOSED
└── test_root_boundary.py                     # PROPOSED
```

Fixtures should live in `fixtures/packages/domains/fauna/identity/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not expose sensitive occurrence material, steward-controlled material, or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the empty `packages/domains/fauna/identity/README.md` file;
- identifies this path as shared Fauna identity helper-code space;
- keeps canonical identity decisions, merge/split decisions, doctrine, contracts, schemas, policy, lifecycle data, evidence, review decisions, and release decisions in their authority roots;
- blocks identity helpers from becoming taxonomic authority, occurrence truth, policy approval, lifecycle promotion, EvidenceBundle creation, canonical identity write, merge/split decision, or release approval;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Fauna sensitivity, geoprivacy, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FAUNA-ID-001` | Which language/runtime owns `packages/domains/fauna/identity/`? | UNKNOWN |
| `PKG-DOM-FAUNA-ID-002` | Which canonical schema owns taxon ids, source-native ids, occurrence ids, duplicate candidates, and public-safe alias ids? | NEEDS VERIFICATION |
| `PKG-DOM-FAUNA-ID-003` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-FAUNA-ID-004` | Which CI workflow validates identity-helper-not-authority and sensitive-occurrence-denial rules? | UNKNOWN |
| `PKG-DOM-FAUNA-ID-005` | Should canonical identity resolution live in a domain pipeline, catalog package, or dedicated registry workflow? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-FAUNA-ID-006` | Which deterministic id strategy is canonical for public-safe alias ids versus restricted internal ids? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package helper-focused and subordinate to Fauna identity governance. Do not add canonical identity registry writes, taxonomic authority decisions, occurrence truth decisions, merge/split decisions, sensitive-detail publication, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive occurrence examples, steward-controlled examples, or generated truth claims here.

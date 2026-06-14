<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-archaeology-identity-readme
title: Archaeology Identity Package README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/archaeology/identity/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/archaeology/README.md
  - docs/domains/archaeology/README.md
  - pipelines/domains/archaeology/README.md
  - pipeline_specs/archaeology/README.md
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - data/proofs/evidence_bundle/
  - data/catalog/
  - data/triplets/
  - release/manifests/
  - tests/packages/domains/archaeology/identity/
  - fixtures/packages/domains/archaeology/identity/
tags: [kfm, packages, domains, archaeology, identity, deterministic-identity, candidate-identity, site-identity, artifact-identity, context-identity, provenance, sensitivity, governance]
notes:
  - "This README fills the empty archaeology identity package file with a governed helper-package contract."
  - "identity is a shared helper package for archaeology identity-key and identity-normalization support; it is not site confirmation authority, source authority, or canonical identity registry authority."
  - "Identity helpers must preserve uncertainty, candidate status, source role, provenance, review refs, policy refs, and EvidenceRef links."
  - "Restricted archaeology identity detail fails closed for public use unless governed review, transform, and release controls are satisfied elsewhere."
  - "Concrete code exports, language runtime, package manifest, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Identity Package

> Shared helper package for Archaeology identity support: deterministic id helpers, candidate/site/artifact/context identity-key helpers, source crosswalk helpers, merge-candidate payload helpers, uncertainty preservation, and fixture utilities. It must not confirm sites, become a canonical identity registry, disclose restricted detail, decide policy, write lifecycle records, create EvidenceBundles, or approve release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Farchaeology%2Fidentity%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20package-0a7ea4)
![identity](https://img.shields.io/badge/identity-helper%20not%20authority-d62728)
![sensitivity](https://img.shields.io/badge/restricted%20detail-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/archaeology/identity/README.md`  
**Parent package:** `packages/domains/archaeology/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/archaeology/`  
**Executable domain-pipeline root:** `pipelines/domains/archaeology/`  
**Contract/schema/policy roots:** `contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/`, and `policy/domains/archaeology/`  
**Placement posture:** helper package for archaeology identity normalization only. Runtime, exports, package manifest, active tests, and implementation are `NEEDS VERIFICATION` until checked by current repo evidence.

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

`packages/domains/archaeology/identity/` may contain reusable helper code for normalizing and comparing archaeology identity references without becoming an authority root.

It may support:

- deterministic id helper utilities for already-governed inputs;
- candidate-feature, site, survey, artifact, context, excavation-unit, collection, chronology, and sensing identity-key helpers;
- source-native identifier preservation helpers;
- source crosswalk helpers that retain native values and uncertainty;
- merge-candidate and split-candidate payload helpers;
- duplicate-detection helper structures;
- review queue identity helpers;
- public alias id helpers;
- schema-bound validation adapters;
- no-network fixture builders for tests.

It does **not** confirm archaeological sites, assign canonical identity by itself, merge or split lifecycle records, decide policy, create EvidenceBundles, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/archaeology/`? | Identity helpers are reusable Archaeology package code, not a new authority root. | CONFIRMED parent root pattern / NEEDS VERIFICATION for implementation |
| Is this the canonical identity registry? | No. It may produce helper keys and candidate payloads only; canonical registry and lifecycle authority stay outside this package. | CONFIRMED boundary posture |
| Is this Archaeology doctrine? | No. Doctrine and sensitivity posture belong under `docs/domains/archaeology/`. | CONFIRMED boundary posture |
| Can this confirm sites or merge records? | No. It may suggest deterministic keys or merge candidates only. | CONFIRMED identity boundary |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, uncertainty, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> An identity helper is not identity authority. A deterministic key, normalized identifier, or duplicate candidate remains downstream of source role, evidence, review, policy, lifecycle, and release state.

[⬆ Back to top](#top)

---

## 3. Identity boundary

Allowed direction:

```text
source-native id / candidate id / EvidenceRef / review refs / policy refs
  -> archaeology identity helper
  -> deterministic helper key, normalized id payload, duplicate candidate, or public alias id
  -> governed pipeline/review flow handles canonical identity and lifecycle state where authorized
```

Blocked direction:

```text
identity helper
  -> confirmed archaeological site
  -> canonical identity registry write
  -> merge/split decision
  -> restricted detail disclosure
  -> policy decision
  -> EvidenceBundle creation
  -> lifecycle promotion
  -> release approval
```

Identity helpers should be deterministic where practical, preserve source-native identifiers, and keep uncertainty explicit. They should prefer review-ready identity candidates over authoritative assertions.

[⬆ Back to top](#top)

---

## 4. Sensitivity and publication boundary

Archaeology identity handling has high exposure risk. This package must preserve these boundaries:

- restricted archaeology identity detail is not public by default;
- identity keys must not leak sensitive context or collection-security detail;
- candidate-feature identities remain candidate identities unless confirmed through governed review and evidence;
- public alias ids must not be reversible to restricted internal identifiers without authorized context;
- missing or inaccessible EvidenceBundle, review, policy, or release state should produce abstain/deny-safe outcomes, not fabricated identity confidence;
- cultural review, steward review, EvidenceBundle, SensitivityTransform, ReleaseManifest, correction path, and rollback posture remain outside this package.

[⬆ Back to top](#top)

---

## 5. Anti-collapse rules

Disallowed collapses:

```text
identity helper -> identity authority
deterministic key -> site confirmation
normalized source id -> canonical KFM id
duplicate candidate -> merge decision
split candidate -> split decision
public alias id -> public release approval
review ref -> review completion
EvidenceRef -> EvidenceBundle closure
successful package test -> lifecycle promotion
```

Required separations:

- identity helper code stays under `packages/domains/archaeology/identity/`;
- Archaeology doctrine stays under `docs/domains/archaeology/`;
- object meaning stays under `contracts/domains/archaeology/`;
- schemas stay under `schemas/contracts/v1/domains/archaeology/`;
- policy and sensitivity rules stay under `policy/domains/archaeology/` and accepted policy roots;
- canonical lifecycle identities and record writes stay under governed data/pipeline roots;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 6. What belongs here

Appropriate source files include:

- deterministic helper-key utilities;
- source-native id normalization helpers;
- candidate/site/artifact/context identity-key helpers;
- identity crosswalk helpers that preserve native identifiers and uncertainty;
- duplicate-candidate helper payloads;
- merge/split proposal payload helpers that do not decide merges/splits;
- public alias id helper utilities;
- review-ref and EvidenceRef preservation helpers;
- schema-bound validation adapters and safe errors;
- synthetic or sanitized fixture builders.

A good placement test:

> If the file is reusable identity support code that preserves source/evidence/governance refs and does not confirm sites, write lifecycle records, disclose restricted detail, decide policy, or approve release, it may belong here.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Canonical identity registry records | governed data/catalog/triplet roots or approved registry homes |
| Merge/split decision workflows | governed pipeline/review workflow roots |
| EvidenceBundle storage or creation | `data/proofs/evidence_bundle/` and proof tooling |
| Archaeology doctrine and scope docs | `docs/domains/archaeology/` |
| Archaeology object contracts | `contracts/domains/archaeology/` |
| Archaeology schemas | `schemas/contracts/v1/domains/archaeology/` |
| Archaeology policy decisions/rules | `policy/domains/archaeology/` and accepted policy roots |
| Executable identity-resolution pipeline | `pipelines/domains/archaeology/` or accepted executable lane |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Review decisions | cultural/steward review authority roots |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| Public map/UI rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/archaeology/identity/` |
| Package fixtures | `fixtures/packages/domains/archaeology/identity/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 8. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `keys` | Deterministic helper-key generation for governed inputs. | PROPOSED |
| `source_ids` | Source-native id normalization and preservation. | PROPOSED |
| `candidate_ids` | Candidate-feature and anomaly identity helpers. | PROPOSED |
| `site_ids` | Site identity helper keys, not confirmation. | PROPOSED |
| `artifact_ids` | Artifact and collection identity helper payloads. | PROPOSED |
| `context_ids` | Context/provenience identity helper payloads. | PROPOSED |
| `duplicates` | Duplicate-candidate helper payloads. | PROPOSED |
| `aliases` | Public alias id helpers that avoid restricted disclosure. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Synthetic/sanitized fixture builders. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/archaeology/identity/` | Shared identity helper code only. |
| Parent helper package | `packages/domains/archaeology/` | Domain helper parent. |
| Domain doctrine | `docs/domains/archaeology/` | Scope and sensitivity posture. |
| Domain contracts | `contracts/domains/archaeology/` | Meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/archaeology/` | Machine shape authority. |
| Domain policy | `policy/domains/archaeology/` | Admissibility/exposure authority. |
| Canonical lifecycle records | `data/<phase>/archaeology/` | Not written here as hidden behavior. |
| Catalog/triplet records | `data/catalog/`, `data/triplets/` | Not written here as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/archaeology/identity/` | Package validation. |
| Fixtures | `fixtures/packages/domains/archaeology/identity/` | No-network synthetic or sanitized fixtures. |

[⬆ Back to top](#top)

---

## 10. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.archaeology.identity
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - canonical_identity_registry
  - merge_decision
  - split_decision
  - archaeology_doctrine
  - site_confirmation
  - restricted_detail_release
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - deterministic helper-key utilities
  - source-native id normalizers
  - candidate identity helper payloads
  - site identity helper payloads
  - artifact and context identity helper payloads
  - duplicate-candidate helpers
  - public alias id helpers
  - schema-bound adapters
  - synthetic fixture builders
required_invariants:
  no_site_confirmation: true
  no_canonical_identity_write: true
  no_merge_or_split_decision: true
  no_restricted_detail_publication: true
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
tests/packages/domains/archaeology/identity/
├── test_identity_package_boundaries.py      # PROPOSED
├── test_key_not_site_confirmation.py        # PROPOSED
├── test_source_id_not_canonical_id.py       # PROPOSED
├── test_duplicate_candidate_not_merge.py    # PROPOSED
├── test_alias_not_detail_leak.py            # PROPOSED
├── test_restricted_detail_not_public.py     # PROPOSED
├── test_no_hidden_lifecycle_writes.py       # PROPOSED
├── test_no_evidence_fabrication.py          # PROPOSED
├── test_no_release_approval.py              # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

Fixtures should live in `fixtures/packages/domains/archaeology/identity/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not expose restricted archaeology identity material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the empty `packages/domains/archaeology/identity/README.md` file;
- identifies this path as shared identity helper-code space;
- keeps canonical identity decisions, merge/split decisions, doctrine, contracts, schemas, policy, lifecycle data, evidence, review decisions, and release decisions in their authority roots;
- blocks identity helpers from becoming site confirmation, restricted-detail disclosure, policy approval, lifecycle promotion, EvidenceBundle creation, canonical identity write, merge/split decision, or release approval;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Archaeology sensitivity, cultural/steward review, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-ARCH-ID-001` | Which language/runtime owns `packages/domains/archaeology/identity/`? | UNKNOWN |
| `PKG-DOM-ARCH-ID-002` | Which canonical schema owns source-native ids, candidate ids, site ids, duplicate candidates, and public alias ids? | NEEDS VERIFICATION |
| `PKG-DOM-ARCH-ID-003` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-ARCH-ID-004` | Which CI workflow validates identity-helper-not-authority and restricted-detail-denial rules? | UNKNOWN |
| `PKG-DOM-ARCH-ID-005` | Should canonical identity resolution live in a domain pipeline, catalog package, or dedicated registry workflow? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-ARCH-ID-006` | Which deterministic id strategy is canonical for public alias ids versus internal restricted ids? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package helper-focused and subordinate to Archaeology identity governance. Do not add canonical identity registry writes, merge/split decisions, site-confirmation logic, restricted-detail publication, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, restricted examples, or generated truth claims here.

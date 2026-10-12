<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-fauna-public-safe-readme
title: Fauna Public Safe Package README
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
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/fauna/public_safe/README.md
related:
  - packages/README.md
  - packages/domains/README.md
  - packages/domains/fauna/README.md
  - packages/domains/fauna/normalize/README.md
  - packages/domains/fauna/identity/README.md
  - docs/domains/fauna/README.md
  - pipelines/domains/fauna/README.md
  - pipeline_specs/fauna/README.md
  - contracts/domains/fauna/
  - schemas/contracts/v1/domains/fauna/
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - tests/packages/domains/fauna/public_safe/
  - fixtures/packages/domains/fauna/public_safe/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, fauna, public-safe, geoprivacy, generalization, redaction, aggregation, sensitivity, release-ref, governance]
notes:
  - "This README fills the empty fauna public_safe package file with a governed helper-package contract."
  - "public_safe is a shared helper package for preparing public-safe Fauna projection metadata; it is not policy authority, sensitivity authority, release authority, or public API authority."
  - "Public-safe helpers must preserve source roles, uncertainty, sensitivity tier, geoprivacy transform refs, review refs, policy refs, release refs, and EvidenceRef links."
  - "Sensitive occurrence material fails closed for public use unless governed geoprivacy, review, policy, release, correction, and rollback controls are satisfied elsewhere."
  - "Concrete code exports, language runtime, package manifest, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Public-Safe Package

> Shared helper package for Fauna public-safe projection support: geoprivacy metadata, redaction/generalization descriptors, aggregation hints, public display envelopes, caveat preservation, release-reference helpers, and fixture utilities. It must not decide policy, decide sensitivity, approve release, write lifecycle records, create EvidenceBundles, or make restricted occurrence material public.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Ffauna%2Fpublic__safe%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20helper%20package-0a7ea4)
![safe](https://img.shields.io/badge/public--safe-helper%20not%20release-d62728)
![sensitivity](https://img.shields.io/badge/sensitive%20occurrence-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `packages/domains/fauna/public_safe/README.md`  
**Parent package:** `packages/domains/fauna/`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/fauna/`  
**Executable domain-pipeline root:** `pipelines/domains/fauna/`  
**Declarative pipeline-spec root:** `pipeline_specs/fauna/`  
**Contract/schema/policy roots:** `contracts/domains/fauna/`, `schemas/contracts/v1/domains/fauna/`, `policy/domains/fauna/`, and `policy/sensitivity/fauna/`  
**Placement posture:** helper package for public-safe Fauna projection metadata only. Runtime, exports, package manifest, active tests, and implementation are `NEEDS VERIFICATION` until checked by current repo evidence.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Public-safe boundary](#3-public-safe-boundary)
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

`packages/domains/fauna/public_safe/` may contain reusable helper code for preparing public-safe Fauna projection metadata without becoming a release or policy authority.

It may support:

- geoprivacy transform reference helpers;
- redaction and generalization descriptor helpers;
- public-safe display envelope helpers;
- aggregation and binning metadata helpers;
- sensitivity tier and review-state preservation helpers;
- release-ref and correction-ref preservation helpers;
- EvidenceRef and source-role preservation helpers;
- safe absent/withheld/denied outcome helpers;
- schema-bound validation adapters and safe errors;
- no-network fixture builders for tests.

It does **not** decide that something is public, decide policy, decide sensitivity, approve geoprivacy sufficiency, create EvidenceBundles, write lifecycle data, publish artifacts, or approve release.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why under `packages/domains/fauna/`? | Public-safe helpers are reusable Fauna package code, not a new authority root. | CONFIRMED parent root pattern / NEEDS VERIFICATION for implementation |
| Is this the release authority? | No. It may prepare public-safe projection metadata only; release authority stays outside this package. | CONFIRMED release separation |
| Is this Fauna doctrine? | No. Fauna doctrine and scope belong under `docs/domains/fauna/`. | CONFIRMED boundary posture |
| Can this decide occurrence truth or taxonomy? | No. It may preserve already-governed refs, caveats, and transform metadata only. | CONFIRMED truth boundary |
| Can this decide policy, evidence, sensitivity, or release? | No. It may preserve refs, uncertainty, sensitivity tier, and validation results only. | CONFIRMED governance separation |

> [!IMPORTANT]
> A public-safe helper is not a release decision. A public-safe display envelope, aggregated descriptor, or withheld outcome remains downstream of geoprivacy, review, policy, EvidenceBundle, ReleaseManifest, correction path, and rollback posture.

[⬆ Back to top](#top)

---

## 3. Public-safe boundary

Allowed direction:

```text
EvidenceRef / source role / sensitivity tier / geoprivacy ref / review ref / policy ref / release ref
  -> fauna public_safe helper
  -> public-safe projection metadata, withheld outcome, display envelope, or aggregation descriptor
  -> governed API/release surface decides exposure where authorized
```

Blocked direction:

```text
public_safe helper
  -> policy decision
  -> sensitivity decision
  -> geoprivacy approval
  -> occurrence truth decision
  -> EvidenceBundle creation
  -> lifecycle promotion
  -> release approval
  -> public trust membrane bypass
```

Public-safe helpers should be deterministic where practical, preserve source-native and evidence refs, and fail safe when evidence, review, geoprivacy, policy, or release state is missing or inaccessible.

[⬆ Back to top](#top)

---

## 4. Sensitivity and publication boundary

Fauna public-safe projection has elevated exposure risk when sensitive taxa or sensitive occurrence context is involved. This package must preserve these boundaries:

- sensitive taxa and sensitive occurrence material are not public by default;
- public-safe outputs must not expose restricted occurrence detail, steward-controlled context, or source-rights-limited detail;
- generalized or aggregated outputs are not automatically releasable;
- geoprivacy transform refs and sensitivity tiers must be preserved rather than discarded;
- missing or inaccessible EvidenceBundle, geoprivacy transform, review, policy, or release state should produce abstain/deny-safe outcomes, not fallback exposure;
- RedactionReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, and rollback posture remain outside this package.

[⬆ Back to top](#top)

---

## 5. Anti-collapse rules

Disallowed collapses:

```text
public-safe helper -> release authority
public-safe flag -> ReleaseManifest
generalization descriptor -> geoprivacy approval
redaction metadata -> sensitivity decision
aggregation helper -> public release approval
withheld outcome -> evidence closure
EvidenceRef -> EvidenceBundle closure
review ref -> review completion
successful package test -> lifecycle promotion
```

Required separations:

- public-safe helper code stays under `packages/domains/fauna/public_safe/`;
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

- public-safe display envelope helpers;
- redaction and generalization descriptor helpers;
- geoprivacy-transform-ref preservation helpers;
- sensitivity-tier, review-ref, policy-ref, release-ref, correction-ref, and EvidenceRef preservation helpers;
- aggregation and binning metadata helpers;
- withheld/denied/abstain outcome helpers;
- source-role and caveat preservation helpers;
- schema-bound validation adapters and safe errors;
- deterministic helper ids when policy and schema allow;
- synthetic or sanitized fixture builders.

A good placement test:

> If the file is reusable public-safe projection support code that preserves source/evidence/governance refs and does not decide exposure, occurrence truth, lifecycle state, policy, or release approval, it may belong here.

[⬆ Back to top](#top)

---

## 7. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Release decisions and manifests | `release/` |
| Geoprivacy policy decisions | `policy/domains/fauna/` and `policy/sensitivity/fauna/` |
| EvidenceBundle storage or creation | `data/proofs/evidence_bundle/` and proof tooling |
| Fauna doctrine and source scope docs | `docs/domains/fauna/` |
| Fauna object contracts | `contracts/domains/fauna/` |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` |
| Executable public-safe projection pipeline | `pipelines/domains/fauna/` or accepted executable lane |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Review decisions | policy/review authority roots |
| Public API routes | `apps/governed-api/` |
| Public map/UI rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/fauna/public_safe/` |
| Package fixtures | `fixtures/packages/domains/fauna/public_safe/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 8. Expected helper families

| Helper family | Responsibility | Status |
|---|---|---|
| `display` | Public-safe display envelope helpers, not API routes. | PROPOSED |
| `geoprivacy_refs` | Geoprivacy transform and sensitivity-ref preservation. | PROPOSED |
| `redaction` | Redaction/generalization metadata helpers, not policy decisions. | PROPOSED |
| `aggregation` | Aggregation and binning metadata helpers, not release approval. | PROPOSED |
| `outcomes` | Withheld, denied, abstain, and inaccessible outcome helpers. | PROPOSED |
| `release_refs` | Release, correction, and rollback reference preservation. | PROPOSED |
| `evidence_refs` | EvidenceRef/source-role/caveat preservation. | PROPOSED |
| `validation` | Schema-bound validation adapters and safe errors. | PROPOSED |
| `fixtures` | Synthetic/sanitized fixture builders. | NEEDS VERIFICATION |

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/fauna/public_safe/` | Shared public-safe helper code only. |
| Parent helper package | `packages/domains/fauna/` | Domain helper parent. |
| Domain doctrine | `docs/domains/fauna/` | Scope and sensitivity posture. |
| Domain contracts | `contracts/domains/fauna/` | Meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/fauna/` | Machine shape authority. |
| Domain policy | `policy/domains/fauna/`, `policy/sensitivity/fauna/` | Admissibility/geoprivacy authority. |
| Canonical lifecycle records | `data/<phase>/fauna/` | Not written here as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/fauna/public_safe/` | Package validation. |
| Fixtures | `fixtures/packages/domains/fauna/public_safe/` | No-network synthetic/sanitized fixtures. |

[⬆ Back to top](#top)

---

## 10. Minimal package contract shape

```yaml
package_id: kfm.packages.domains.fauna.public_safe
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - release_decision
  - geoprivacy_policy_decision
  - sensitivity_decision
  - occurrence_truth
  - fauna_doctrine
  - lifecycle_write
  - evidence_bundle
allowed_responsibilities:
  - public-safe display envelope helpers
  - geoprivacy transform reference helpers
  - redaction and generalization metadata helpers
  - aggregation metadata helpers
  - withheld and denied outcome helpers
  - release/correction reference helpers
  - EvidenceRef and caveat preservation
  - schema-bound adapters
  - synthetic fixture builders
required_invariants:
  sensitive_occurrence_denied_by_default: true
  no_release_approval: true
  no_policy_bypass: true
  no_sensitivity_decision: true
  no_occurrence_truth_decision: true
  no_hidden_lifecycle_writes: true
  no_evidence_fabrication: true
  public_safe_output_is_not_release: true
```

[⬆ Back to top](#top)

---

## 11. Tests and fixtures

Recommended validation coverage:

```text
tests/packages/domains/fauna/public_safe/
├── test_public_safe_package_boundaries.py   # PROPOSED
├── test_public_safe_not_release.py          # PROPOSED
├── test_geoprivacy_ref_not_policy.py        # PROPOSED
├── test_redaction_not_sensitivity_decision.py # PROPOSED
├── test_aggregation_not_release.py          # PROPOSED
├── test_sensitive_occurrence_not_public.py  # PROPOSED
├── test_missing_release_ref_denies.py       # PROPOSED
├── test_no_hidden_lifecycle_writes.py       # PROPOSED
├── test_no_evidence_fabrication.py          # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

Fixtures should live in `fixtures/packages/domains/fauna/public_safe/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not expose sensitive occurrence material, steward-controlled material, or source-rights-limited material unless fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 12. Definition of done

This README is done when it:

- fills the empty `packages/domains/fauna/public_safe/README.md` file;
- identifies this path as shared public-safe projection helper-code space;
- keeps geoprivacy policy decisions, sensitivity decisions, doctrine, contracts, schemas, lifecycle data, evidence, review decisions, and release decisions in their authority roots;
- blocks public-safe helpers from becoming exposure approval, policy approval, lifecycle promotion, EvidenceBundle creation, or release approval;
- defines expected helper families, sensitivity posture, inputs/outputs, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass Fauna sensitivity, geoprivacy, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FAUNA-PS-001` | Which language/runtime owns `packages/domains/fauna/public_safe/`? | UNKNOWN |
| `PKG-DOM-FAUNA-PS-002` | Which canonical schema owns public-safe display envelopes, withheld outcomes, and geoprivacy transform refs? | NEEDS VERIFICATION |
| `PKG-DOM-FAUNA-PS-003` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-FAUNA-PS-004` | Which CI workflow validates public-safe-not-release and sensitive-occurrence-denial rules? | UNKNOWN |
| `PKG-DOM-FAUNA-PS-005` | Should public-safe projection helpers live here, in a policy package, or in a governed API package? | NEEDS VERIFICATION / ADR |
| `PKG-DOM-FAUNA-PS-006` | Which aggregation bands and withheld outcome vocabulary are canonical versus policy-configured? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package helper-focused and subordinate to Fauna public-safe release governance. Do not add exposure approvals, geoprivacy policy decisions, sensitivity decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive occurrence examples, steward-controlled examples, or generated truth claims here.

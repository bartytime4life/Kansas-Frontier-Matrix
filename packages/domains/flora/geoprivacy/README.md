<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-flora-geoprivacy-readme
title: Flora Geoprivacy Helper Package README
type: readme
version: v0.2
status: draft
owners:
  - <package-owner>
  - <flora-domain-steward>
  - <policy-steward>
  - <evidence-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-14
updated: 2026-06-14
policy_label: public
path: packages/domains/flora/geoprivacy/README.md
related:
  - packages/domains/flora/README.md
  - docs/domains/flora/README.md
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, flora, geoprivacy, access-state, evidence-ref, policy-ref, release-ref, governance]
notes:
  - "This package is helper-code space only. It is not doctrine, contract, schema, data, proof, API, or release authority."
  - "Helpers may preserve access-state, policy, evidence, review, and release references for governed callers."
  - "Helpers must not decide truth, policy, lifecycle, proof closure, public API behavior, or release state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Geoprivacy Helper Package

> Shared helper package for Flora access-state and projection metadata. Code here may prepare bounded helper DTOs and preserve governance references. It must not define Flora doctrine, create EvidenceBundles, decide proof closure, write lifecycle records, define policy, create public API routes, or approve release.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fdomains%2Fflora%2Fgeoprivacy%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-helper%20package-0a7ea4)
![release](https://img.shields.io/badge/no%20release%20approval-d62728)

**Status:** Draft  
**Path:** `packages/domains/flora/geoprivacy/README.md`  
**Parent package:** `packages/domains/flora/`  
**Responsibility root:** `packages/` — shared helper libraries  
**Domain doctrine root:** `docs/domains/flora/`  
**Contract/schema/policy roots:** `contracts/domains/flora/`, `schemas/contracts/v1/domains/flora/`, and `policy/domains/flora/`  
**Evidence proof root:** `data/proofs/evidence_bundle/`  
**Release root:** `release/`  
**Verification posture:** runtime, package manifest, exports, tests, and CI are `NEEDS VERIFICATION` until checked against repository evidence.

---

## 1. Purpose

`packages/domains/flora/geoprivacy/` may contain reusable helper code for Flora projection metadata.

Appropriate helpers include:

- access-state DTO helpers;
- bounded projection descriptor helpers;
- policy-ref, review-ref, release-ref, correction-ref, rollback-ref, and EvidenceRef preservation helpers;
- source-role, limitation, caveat, uncertainty, and access-state preservation helpers;
- schema-bound validation adapters and safe errors;
- synthetic fixture builders for package tests.

This package does not decide botanical truth, occurrence truth, policy, lifecycle state, proof closure, public API behavior, or release state.

[⬆ Back to top](#top)

---

## 2. Authority boundary

| Responsibility | Correct home |
|---|---|
| Flora doctrine | `docs/domains/flora/` |
| Flora object meaning | `contracts/domains/flora/` |
| Flora machine shapes | `schemas/contracts/v1/domains/flora/` |
| Flora policy | `policy/domains/flora/` |
| Flora executable pipelines | `pipelines/domains/flora/` |
| Lifecycle records | `data/` lifecycle roots |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions | `release/` |
| Public API routes | `apps/governed-api/` |

A helper result from this package is not an approval, proof, promotion, route, or release artifact.

[⬆ Back to top](#top)

---

## 3. Allowed flow

```text
EvidenceRef / source role / policy ref / review ref / release ref
  -> flora geoprivacy helper
  -> bounded metadata DTO or validation result
  -> governed caller handles policy, proof, lifecycle, API, and release controls
```

Blocked flow:

```text
flora geoprivacy helper
  -> policy decision
  -> EvidenceBundle creation
  -> proof closure
  -> lifecycle promotion
  -> release approval
  -> public trust membrane bypass
```

[⬆ Back to top](#top)

---

## 4. What belongs here

- DTO construction helpers;
- reference-preservation helpers;
- validation adapters that call canonical schemas;
- test fixture builders using synthetic or sanitized data;
- utility functions with no hidden lifecycle writes.

## 5. What does not belong here

- doctrine;
- contract definitions;
- schema definitions;
- policy decisions;
- lifecycle writers;
- EvidenceBundle writers;
- release decisions;
- public API routes;
- UI rendering components;
- generated truth claims.

---

## 6. Minimal package contract

```yaml
package_id: kfm.packages.domains.flora.geoprivacy
status: draft
authority: shared_domain_helper_package
not_authority_for:
  - policy_decision
  - evidence_bundle_creation
  - proof_closure
  - lifecycle_write
  - release_decision
  - public_api_route
allowed_responsibilities:
  - access_state_dto_helpers
  - projection_metadata_helpers
  - reference_preservation_helpers
  - validation_adapters
  - synthetic_fixture_builders
required_invariants:
  no_policy_decision: true
  no_evidence_bundle_creation: true
  no_hidden_lifecycle_writes: true
  no_release_approval: true
  no_public_trust_membrane_bypass: true
  helper_output_is_not_release: true
```

---

## 7. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOM-FLORA-GP-001` | Which language/runtime owns this package? | UNKNOWN |
| `PKG-DOM-FLORA-GP-002` | Which package manifest controls this package, if any? | UNKNOWN |
| `PKG-DOM-FLORA-GP-003` | Which tests validate helper boundaries? | UNKNOWN |
| `PKG-DOM-FLORA-GP-004` | Which schema owns bounded projection metadata? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this package helper-focused and subordinate to Flora governance. Do not add authority-bearing behavior here.

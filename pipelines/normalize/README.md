<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-normalize-readme
title: Normalize Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <normalization-steward>
  - <domain-stewards>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-normalization-receipt-and-lifecycle-gates
path: pipelines/normalize/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipeline_specs/normalize/
  - pipelines/domains/
  - tests/pipelines/normalize/
  - fixtures/normalize/
  - data/raw/
  - data/work/
  - data/quarantine/
  - data/processed/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
tags: [kfm, pipelines, normalize, transform-receipt, work-candidate, quarantine, evidence-bundle, policy, governance]
notes:
  - "This README replaces the greenfield stub at pipelines/normalize/README.md with a governed implementation-lane contract."
  - "The pipelines root is executable pipeline logic — the how — while pipeline_specs is declarative configuration — the what."
  - "This path is a shared normalization implementation lane, not a domain root, source connector, schema home, contract home, policy home, lifecycle data home, catalog home, proof store, or release authority."
  - "Domain-specific normalization remains under domain lanes such as pipelines/domains/<domain>/normalize/ unless an ADR or migration note says otherwise."
  - "Concrete executable behavior, CI coverage, fixture coverage, schema paths, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Normalize Pipelines

> Shared executable normalization lane for common KFM RAW/WORK-to-WORK shaping helpers, transform receipts, field mapping utilities, invariant checks, and domain-normalizer support — without owning source admission, domain truth, schemas, contracts, policy, catalog truth, EvidenceBundle truth, release decisions, or public API/UI behavior.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-shared%20normalization-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic%20only-0a7ea4)
![lifecycle](https://img.shields.io/badge/lifecycle-WORK%20candidate%20only-455a64)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/normalize/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared normalization helpers / cross-domain normalization support  
**Placement posture:** implementation sublane under `pipelines/`; exact long-term authority remains `NEEDS VERIFICATION / ADR` if this becomes a shared framework rather than a small helper lane  
**Public posture:** no direct publication; normalization outputs are WORK candidates, quarantine records, handoff refs, transform receipts, and blocker reports only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Normalize anti-collapse rules](#3-normalize-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Shared normalization scope](#6-shared-normalization-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal normalization receipt](#11-minimal-normalization-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/normalize/` is the shared executable lane for normalization support that is useful across multiple KFM domain pipelines.

It may support:

- common field-mapping helpers;
- original-field preservation helpers;
- unit, time, CRS, geometry, identity, and source-role normalization utilities;
- transform receipt builders;
- quarantine reason helpers;
- no-network fixture runners;
- shared adapters used by domain-specific normalizers;
- invariant checks that prove normalization does not collapse lifecycle, source-role, evidence, policy, catalog, or release boundaries.

This directory implements or will implement the **how** of shared normalization support. It does not own domain-specific normalization contracts, domain object meaning, source admission, source connectors, source descriptors, schemas, policy decisions, EvidenceBundles, catalog records, release decisions, or public API/map behavior.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Normalization helpers are executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why a shared `normalize/` lane? | It can hold reusable normalization utilities that should not be duplicated across domain lanes. | PROPOSED / NEEDS VERIFICATION |
| Does this replace domain normalizers? | No. Domain-owned behavior stays under `pipelines/domains/<domain>/normalize/`. | CONFIRMED boundary posture |
| Is this a schema or contract home? | No. Schemas and contracts remain in their own responsibility roots. | CONFIRMED authority separation |
| Does this write catalog or release outputs? | No. It may emit WORK candidates, quarantine records, receipts, and handoff refs only. | CONFIRMED governance posture |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> A normalized record is not validated truth, catalog truth, public truth, or release approval. Normalization makes data comparable, auditable, and ready for validation while preserving original source fields and receipts.

[⬆ Back to top](#top)

---

## 3. Normalize anti-collapse rules

Disallowed collapses:

```text
normalized record -> accepted public truth
normalization success -> validation pass
normalization receipt -> EvidenceBundle
source payload -> normalized truth without receipt
source role -> inferred domain truth
unit conversion -> silent edit
geometry transform -> public-safe representation
schema-shaped object -> policy-approved object
generated normalization summary -> evidence
pipeline run -> ReleaseManifest
```

Required distinctions:

- RAW capture, WORK candidate, QUARANTINE record, TransformReceipt, ValidationReport, EvidenceBundle, catalog record, triplet projection, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- original values, normalized values, methods, mappings, units, time facets, CRS, geometry transforms, source roles, and confidence/caveat fields remain auditable;
- domain-specific meaning remains with the domain lane;
- unresolved rights, source roles, evidence, policy, or representation questions fail closed;
- release-facing claims resolve EvidenceBundle support or abstain.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is reusable executable normalization support.

Appropriate contents include:

- shared normalization helper README files;
- fixture-only shared dry-run entrypoints;
- unit/time/CRS/geometry utility functions;
- source-role preservation helpers;
- original-field retention helpers;
- transform receipt builders;
- quarantine reason-code helpers;
- shared normalizer adapters used by domain lanes;
- no-network invariant tests or local helper wrappers;
- receipt hash helpers, if not already shared elsewhere.

A good placement test:

> If the code helps multiple domain normalizers shape data into auditable WORK candidates without owning domain truth, it may belong here. If it only belongs to one domain, place it in that domain's normalize lane. If it owns schemas, policy, source admission, catalog truth, release decisions, or public serving, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain-specific normalization workflows | `pipelines/domains/<domain>/normalize/` |
| Ingest/source admission | `pipelines/domains/<domain>/ingest/` or accepted ingest lane |
| Source fetchers and API clients | `connectors/<source_id>/` or accepted connector home |
| Source descriptors | `data/registry/sources/<domain>/` or accepted registry home |
| Domain doctrine | `docs/domains/<domain>/` |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts/object meaning | `contracts/...` accepted contract home |
| Policy | `policy/...` responsibility roots |
| Declarative normalize specs | `pipeline_specs/normalize/` or `pipeline_specs/<domain>/normalize.yaml` |
| Fixtures | `fixtures/normalize/` or domain fixture homes |
| Tests | `tests/pipelines/normalize/` or domain test homes |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Lifecycle outputs | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Shared normalization scope

| Scope area | Shared normalize responsibility | Failure behavior |
|---|---|---|
| Original fields | Preserve raw labels, values, source refs, payload hashes, and method refs. | Fail or route to QUARANTINE. |
| Units/time | Normalize only with explicit method, source unit, target unit, and receipt-ready metadata. | Hold on ambiguity. |
| Source role | Carry source role forward; do not invent authority. | Fail on collapse. |
| Geometry/CRS | Normalize CRS/geometry only with transform metadata and public-representation separation. | Hold on uncertainty. |
| Domain boundary | Delegate domain-specific meaning to the owning domain pipeline. | Fail if shared helper asserts domain truth. |
| Evidence | Preserve EvidenceRef candidates; do not build EvidenceBundles here. | Abstain if unresolved. |
| Receipts | Emit or support deterministic transform/run receipts. | Fail closed on missing hashes. |
| Handoff | Support validation-ready WORK candidates. | No direct catalog or publish. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every shared normalization helper must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, RAW, WORK, or QUARANTINE-remediation inputs only when a domain pipeline authorizes the call.
2. **Normalize** shared fields while preserving original fields, source refs, source roles, units, time facets, transforms, caveats, and evidence refs.
3. **Emit** normalized WORK candidate fragments, transform receipts, run receipts, or QUARANTINE reason inputs.
4. **Return** to the owning domain lane for validation, catalog, release, and public artifact decisions.
5. **Never publish, catalog, validate-as-pass, or decide release directly.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every shared normalization component must check or explicitly fail closed on:

1. **Caller ownership gate** — an owning domain pipeline or approved proof harness must provide scope.
2. **Input lifecycle gate** — input is fixture, RAW, WORK, or approved QUARANTINE remediation.
3. **Original-field gate** — original values remain recoverable.
4. **Method gate** — every transform records method, version, source fields, and target fields.
5. **Source-role gate** — source roles are preserved and not invented by shared code.
6. **Unit/time/geometry gate** — unit, temporal, and spatial transforms are explicit and receipt-ready.
7. **Evidence gate** — EvidenceRefs are carried forward; EvidenceBundles are not fabricated here.
8. **Policy gate** — unresolved rights/sensitivity/policy state remains unresolved and does not silently allow exposure.
9. **Receipt gate** — deterministic run or transform receipt metadata is produced where material.
10. **No-direct-validation gate** — normalization does not mark data as validated.
11. **No-direct-catalog gate** — normalization does not write catalog/triplet records.
12. **No-direct-publish gate** — normalization does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/normalize/
├── README.md
├── NORMALIZE_SHARED_CONTRACT.md       # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── normalize_units.py                 # PROPOSED
├── normalize_time.py                  # PROPOSED
├── normalize_crs_geometry.py          # PROPOSED
├── preserve_source_role.py            # PROPOSED
├── preserve_original_fields.py        # PROPOSED
├── build_transform_receipt.py         # PROPOSED
├── route_quarantine_reason.py         # PROPOSED
└── adapters/                          # PROPOSED domain/proof adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/normalize/<profile>.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/`, `data/quarantine/`, and `data/receipts/`, with domain-owned pipelines deciding the target domain lane.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Shared fixture | `fixtures/normalize/` or domain fixture home | Synthetic/public-safe by default. |
| Declarative spec | `pipeline_specs/normalize/` or domain spec home | The what, not executable logic. |
| Domain input | `data/raw/<domain>/`, `data/work/<domain>/`, or approved remediation refs | Read by stable refs only. |
| Normalized fragment | `data/work/<domain>/` | Owned by calling domain lane. |
| QUARANTINE reason | `data/quarantine/<domain>/` | Owned by calling domain lane. |
| Transform receipt | `data/receipts/pipeline/<domain>/normalize/` or accepted receipt home | Records method, refs, hashes, and outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here unless another accepted proof workflow owns it. |

[⬆ Back to top](#top)

---

## 11. Minimal normalization receipt

The final schema is not defined here. This example shows the minimum information a shared normalization receipt should preserve.

```yaml
schema_version: kfm.shared_normalize_receipt.v1
normalize_run_id: normalize_run_YYYYMMDDThhmmssZ
pipeline_id: normalize.<profile_id>
status: HELD
caller:
  owner_pipeline: pipelines/domains/<domain>/normalize
  domain: <domain>
  profile_ref: pipeline_specs/normalize/<profile_id>.yaml
inputs:
  source_refs: []
  input_lifecycle_state: WORK
  input_payload_hashes: []
transforms:
  original_fields_preserved: false
  source_role_preserved: false
  unit_transforms: []
  time_transforms: []
  geometry_transforms: []
checks:
  method_refs_resolved: false
  evidence_refs_carried_forward: false
  policy_state_preserved: false
  receipt_hashes_ready: false
anti_collapse:
  normalization_success_is_validation_pass: false
  transform_receipt_is_evidence_bundle: false
  shared_helper_owns_domain_truth: false
outputs:
  work_ref_candidates: []
  quarantine_reason_refs: []
  receipt_ref: data/receipts/pipeline/<domain>/normalize/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Recommended tests:

```text
tests/pipelines/normalize/
├── test_no_network_dry_run.py              # PROPOSED
├── test_caller_scope_required.py           # PROPOSED
├── test_original_fields_preserved.py       # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_unit_transform_receipts.py         # PROPOSED
├── test_time_transform_receipts.py         # PROPOSED
├── test_geometry_transform_receipts.py     # PROPOSED
├── test_evidence_refs_not_fabricated.py    # PROPOSED
├── test_policy_state_not_silently_allowed.py # PROPOSED
├── test_no_validation_pass_side_effect.py  # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, caller scope is required, original fields and source roles are preserved, unit/time/geometry transforms are receipt-ready, evidence refs are not fabricated, policy state is not silently allowed, receipts are deterministic, and no run writes directly to validation pass state, catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Shared normalization helpers may prepare normalized fragments, transform receipts, quarantine reasons, and validation handoff data. They do not publish.

Required chain:

```text
calling domain pipeline
  -> shared normalization helper
  -> normalized WORK fragment / quarantine reason / receipt
  -> domain validation
  -> EvidenceBundle closure
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- failed normalization helper runs remain auditable;
- receipts preserve input refs, method refs, transform refs, evidence refs, policy refs, and failure reasons;
- normalized outputs are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, transform refs, EvidenceBundle refs, policy refs, correction refs, or rollback refs drift;
- rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the greenfield stub at `pipelines/normalize/README.md`;
- identifies this directory as a shared executable normalization-support lane under `pipelines/`;
- prevents domain-specific logic, schemas, contracts, policy, source descriptors, lifecycle data, EvidenceBundles, release decisions, public API, UI, catalog, and publication authority from being placed here;
- preserves source-role, original-field, method, transform-receipt, EvidenceRef, policy, lifecycle, quarantine, correction, and rollback boundaries;
- blocks normalization-success-as-validation-pass, transform-receipt-as-EvidenceBundle, shared-helper-as-domain-truth, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this lane is done only when it has public-safe fixtures, no-network tests, caller-scope checks, original-field/source-role preservation tests, transform-receipt tests, evidence/policy preservation tests, deterministic receipts, CI coverage, domain-steward handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-NORM-001` | Is `pipelines/normalize/` the final accepted home for shared normalization helpers, or should this move under `packages/`, `tools/`, or domain lanes by ADR? | NEEDS VERIFICATION / ADR |
| `PIPE-NORM-002` | Which schema owns shared normalization receipts and transform receipt fragments? | NEEDS VERIFICATION |
| `PIPE-NORM-003` | Should every domain normalize sublane call shared helpers, or only use them for common unit/time/geometry transforms? | NEEDS VERIFICATION |
| `PIPE-NORM-004` | Which CI job owns shared normalization invariant tests? | UNKNOWN |
| `PIPE-NORM-005` | Which transform profiles belong in `pipeline_specs/normalize/` versus domain-specific specs? | NEEDS VERIFICATION |
| `PIPE-NORM-006` | Should shared normalization emit receipts directly, or only return receipt fragments to domain normalizers? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live source fetching, domain truth ownership, schema authority, policy authority, source-profile editing, validation-pass shortcuts, catalog writes, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller scope, source roles, original fields, transform methods, receipt hashes, EvidenceRef handling, policy state, deterministic receipts, and rollback expectations are proven.

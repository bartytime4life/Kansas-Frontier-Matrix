# `schemas/contracts/v1/domains/hazards/receipts/` — Hazards Receipts Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-hazards-receipts-readme
title: schemas/contracts/v1/domains/hazards/receipts/ — Hazards Receipts Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <hazards-domain-steward>
  - <receipt-steward>
  - <validation-steward>
  - <freshness-steward>
  - <policy-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, hazards, receipts, freshness, validation, run-receipt, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-hazards-red)
![family](https://img.shields.io/badge/family-receipts-blueviolet)
![posture](https://img.shields.io/badge/posture-schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/domains/hazards/receipts/` is a draft Hazards schema sublane for receipt-shaped Hazards objects.

This path should index machine-checkable schema shapes for Hazards receipt objects, such as intake, freshness, validation, transform, model-run, correction-support, rollback-support, and release-support receipts once those schema homes are confirmed.

This path must not store emitted receipt instances, proof records, EvidenceBundles, catalog records, release manifests, release decisions, policy decisions, source payloads, public layers, operational alerts, or life-safety instructions.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, lifecycle data, receipt data, proof output, emergency alert authority, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Hazards receipts schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/hazards/receipts/` |
| Status | Draft |
| Authority level | Schema-index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, receipt-family rules, policy rules, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Parent Hazards schema lane | `schemas/contracts/v1/domains/hazards/` exists as a PROPOSED greenfield scaffold. |
| Receipt schema inventory | NEEDS VERIFICATION. Current-session search did not confirm concrete receipt schemas under this path. |
| Related receipt instance lane | `data/receipts/hazards/` exists for Hazards process-memory receipts, not schema shape. |
| Hazards boundary | KFM Hazards is not an emergency alert system or life-safety authority. Official sources remain the authority for live safety action. |
| Receipt boundary | Schema shape belongs under `schemas/`; emitted receipt instances belong under governed `data/receipts/` lanes once confirmed. |
| Required reviewers | Schema steward, Hazards steward, receipt steward, validation steward, freshness steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms `schemas/contracts/v1/domains/hazards/README.md` exists as a PROPOSED Hazards domain schema scaffold. That parent file still needs expansion and does not by itself prove this receipts sublane is complete.

Current-session search found `data/receipts/hazards/README.md`, Hazards docs, and Hazards contracts. It did not confirm concrete receipt schemas under this requested path.

Current-session evidence from `data/receipts/hazards/README.md` confirms the receipt instance lane is process memory only; it is not proof, catalog, source registry, policy, release, public artifact, emergency alert, life-safety, or generated-answer authority.

Current-session evidence from ADR-0011 states the governance separation: receipt, proof, catalog, and publication are distinct families. This schema lane may define receipt shape, but it does not store or publish receipt instances.

Current-session Hazards architecture evidence confirms the Hazards lane governs historical, regulatory, modeled, and operational-context hazard information for analysis and resilience, while refusing to act as life-safety alerting.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── hazards/
                ├── README.md
                └── receipts/
                    └── README.md             # you are here

contracts/
└── domains/
    └── hazards/                              # semantic meaning; not schema shape

data/
└── receipts/
    └── hazards/                              # emitted process-memory receipts; not schema shape

docs/
└── domains/
    └── hazards/                              # human-facing doctrine; not schema shape

policy/                                       # allow/deny/restrict/abstain; not schema shape
fixtures/                                     # samples for tests; coverage NEEDS VERIFICATION
release/                                      # release decisions and records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/hazards/receipts/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `schemas/contracts/v1/domains/hazards/README.md` | Existing parent Hazards schema scaffold; status PROPOSED. |
| Search for Hazards receipt/schema surfaces | Found Hazards receipt instance lane and Hazards docs/contracts; did not confirm concrete receipt schemas here. |
| `data/receipts/hazards/README.md` | Hazards receipt process-memory lane; not proof, catalog, release, public, alert, or life-safety authority. |
| ADR-0011 | Proposed separation rule: receipt, proof, catalog, and publication are distinct families; schema homes remain governed by ADR-0001. |
| `docs/domains/hazards/ARCHITECTURE.md` | Hazards architecture; establishes the Hazards life-safety boundary. |

This README does not verify complete receipt schema fields, schema registry entries, fixture coverage, validator wiring, CI behavior, source-admission behavior, freshness enforcement, policy behavior, release integration, emitted receipt instance layout, runtime behavior, public API behavior, or map rendering behavior.

## Candidate receipt-shape families

Candidate Hazards receipt schemas should be introduced only after contract, fixture, validator, registry, freshness, policy, and steward support is clear.

| Candidate family | Status | Notes |
|---|---|---|
| Hazards source intake receipt | NEEDS VERIFICATION | Could describe process memory for admitted source intake. |
| Hazards freshness receipt | NEEDS VERIFICATION | Could describe freshness or expiry checks for time-sensitive context. |
| Hazards validation receipt | NEEDS VERIFICATION | Could describe validation process memory without becoming proof. |
| Hazards transform receipt | NEEDS VERIFICATION | Could describe normalization or transformation process memory. |
| Hazards model-run receipt | NEEDS VERIFICATION | Could describe model or materialization runs without proving hazard truth. |
| Hazards warning-context receipt | NEEDS VERIFICATION | Could describe context handling without becoming alert or safety authority. |
| Hazards correction receipt | NEEDS VERIFICATION | Could describe correction-support process memory without replacing CorrectionNotice. |
| Hazards rollback receipt | NEEDS VERIFICATION | Could describe rollback-support process memory without replacing RollbackCard or release records. |
| Hazards release-support receipt | NEEDS VERIFICATION | Could describe release-support process memory without becoming release authority. |

## Receipts-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Schema index | Track Hazards receipt schema candidates and accepted schema files. |
| Contract pairing | Link each receipt schema to a Hazards or shared receipt semantic contract when verified. |
| Instance separation | Keep emitted receipt records outside `schemas/`. |
| Family separation | Do not collapse receipts into proofs, catalog records, release manifests, policy decisions, correction notices, or rollback records. |
| Hazards boundary | Do not encode operational instructions, emergency directions, or life-safety authority. |
| Freshness discipline | Preserve source time, issue time, expiry time, retrieval time, release time, and correction time where schemas eventually require them. |
| Drift prevention | Prevent duplicate receipt schemas under conflicting Hazards, shared receipt, proof, or release paths. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Hazards-owned receipt schema files once placement is confirmed.
- Short schema-family index notes.
- Migration notes for receipt schema placement.
- Drift notes about duplicate or stale Hazards receipt schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, source-registry references, release references, correction references, rollback references, and tests.

## What does not belong here

- Emitted receipt instances.
- Proof records or EvidenceBundles.
- Catalog records.
- Registry records or SourceDescriptor instances.
- Release manifests or release decisions.
- Policy approvals or sensitivity decisions.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- Operational alert instructions or live safety guidance.
- Public API or map/UI behavior.
- Claims that a receipt schema is complete without fixtures, validators, registry records, and steward review support.

## Receipt schema status values

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate receipt schema locations. |
| `RECEIPT_SCHEMA_CANDIDATE` | The schema may become an accepted Hazards receipt schema. |
| `DRAFT_SCHEMA` | Schema exists but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `MIGRATE_TO_HAZARDS_ROOT` | Content belongs directly under `schemas/contracts/v1/domains/hazards/`. |
| `MIGRATE_TO_SHARED_RECEIPT` | Content belongs under a shared receipt schema family. |
| `DEPRECATED` | Content should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Review checklist

- [ ] Canonical receipt schema path is linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Receipt instance lane is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Receipt/proof/catalog/release/policy boundaries are preserved.
- [ ] Hazards life-safety boundary is preserved.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/hazards/receipts/`.
- [ ] Confirm whether Hazards receipt schemas belong in this sublane, the Hazards schema root, or a shared receipt family.
- [ ] Confirm paired Hazards contract paths.
- [ ] Confirm emitted receipt instance subtype lanes under `data/receipts/hazards/`.
- [ ] Confirm schema registry records.
- [ ] Confirm fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm freshness, policy, release, correction, and rollback references.
- [ ] Confirm whether `schemas/contracts/v1/domains/hazards/README.md` should index this receipts lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Receipt schema-home decision, new Hazards receipt schema, shared receipt migration note, validator update, fixture update, schema registry update, ADR update, Hazards receipt contract update, receipt instance lane update, or policy/release reference update |

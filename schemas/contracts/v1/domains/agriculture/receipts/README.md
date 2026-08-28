# `schemas/contracts/v1/domains/agriculture/receipts/` — Agriculture Receipts Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-agriculture-receipts-readme
title: schemas/contracts/v1/domains/agriculture/receipts/ — Agriculture Receipts Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <agriculture-domain-steward>
  - <receipt-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, agriculture, receipts, aggregation-receipt, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-agriculture-green)
![family](https://img.shields.io/badge/family-receipts-blueviolet)
![posture](https://img.shields.io/badge/posture-schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/domains/agriculture/receipts/` is a draft Agriculture schema sublane for receipt-shaped Agriculture objects.

This path should index machine-checkable schema shapes for Agriculture receipt objects. It must not store emitted receipt instances, proof records, catalog records, release manifests, release decisions, or publication artifacts.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, lifecycle data, receipt data, proof output, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Agriculture receipts schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/agriculture/receipts/` |
| Status | Draft |
| Authority level | Schema-index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, receipt-family rules, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Agriculture schema lane | `schemas/contracts/v1/domains/agriculture/` exists as a PROPOSED domain schema lane. |
| Confirmed related schema | `schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json` exists as a PROPOSED scaffold. |
| Paired contract | `contracts/domains/agriculture/aggregation-receipt.md` exists, but records a hyphen/underscore path conflict for the paired contract path. |
| Receipt boundary | Schema shape belongs under `schemas/`; emitted receipt instances belong in their governed data/receipt lane once confirmed. |
| Default posture | Do not add canonical receipt schemas here until paired contracts, fixtures, validators, registry records, and steward review are confirmed. |
| Required reviewers | Schema steward, Agriculture steward, receipt steward, contract steward, validation steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence confirms `schemas/contracts/v1/domains/agriculture/README.md` exists as a PROPOSED Agriculture domain schema lane.

Current-session search found `contracts/domains/agriculture/aggregation-receipt.md` as the Agriculture receipt semantic contract.

Current-session evidence confirms `schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json` exists as a PROPOSED scaffold with no required fields and `additionalProperties: true`.

Current-session evidence from ADR-0011 states the governance separation: receipt, proof, catalog, and publication are distinct families. This schema lane may define receipt shape, but it does not store or publish receipt instances.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── agriculture/
                ├── README.md
                ├── aggregation_receipt.schema.json      # confirmed PROPOSED scaffold
                └── receipts/
                    └── README.md                        # you are here

contracts/
└── domains/
    └── agriculture/
        └── aggregation-receipt.md                       # semantic contract; path conflict noted

data/
└── receipts/                                             # receipt instances; exact agriculture lane NEEDS VERIFICATION
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/agriculture/receipts/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `schemas/contracts/v1/domains/agriculture/README.md` | Existing Agriculture domain schema lane; status PROPOSED. |
| Search for agriculture receipt surfaces | Found `contracts/domains/agriculture/aggregation-receipt.md` and related Agriculture docs/policy surfaces. |
| `contracts/domains/agriculture/aggregation-receipt.md` | Semantic contract for `AggregationReceipt`; marks schema home and receipt-family path questions as NEEDS VERIFICATION. |
| `schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json` | Existing PROPOSED scaffold schema. |
| ADR-0011 | Proposed separation rule: receipt, proof, catalog, and publication are distinct families. |

This README does not verify complete schema fields, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, or emitted receipt instance layout.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `../aggregation_receipt.schema.json` | `contracts/domains/agriculture/aggregation-receipt.md` | PROPOSED / scaffold | Schema exists at the Agriculture domain schema root, not inside `receipts/`; contract records a hyphen/underscore path conflict and receipt-home questions. |

## Receipts-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Schema index | Track Agriculture receipt schema files and their placement status. |
| Contract pairing | Link each receipt schema to an Agriculture semantic contract when verified. |
| Instance separation | Keep emitted receipt records outside `schemas/`. |
| Family separation | Do not collapse receipts into proofs, catalog records, or release manifests. |
| Drift prevention | Prevent duplicate receipt schemas under conflicting Agriculture paths. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Agriculture-owned receipt schema files once placement is confirmed.
- Short schema-family index notes.
- Migration notes for receipt schema placement.
- Drift notes about duplicate or stale Agriculture receipt schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.
- Notes that preserve the receipt/proof/catalog/release separation.

## What does not belong here

- Emitted receipt instances.
- Proof records.
- Catalog records.
- Release manifests or release decisions.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- Registry records.
- Claims that a receipt schema is complete without fixtures, validators, registry records, and review support.

## Receipt schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate receipt schema locations. |
| `RECEIPT_SCHEMA_CANDIDATE` | The schema may become an accepted Agriculture receipt schema. |
| `DRAFT_SCHEMA` | Schema exists but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `MIGRATE_TO_AGRICULTURE_ROOT` | Content belongs directly under `schemas/contracts/v1/domains/agriculture/`. |
| `MIGRATE_TO_RECEIPTS` | Content belongs under this receipts sublane. |
| `DEPRECATED` | Content should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal receipt schema note

```markdown
# <agriculture-receipt-schema-note-id>

## Status
INDEX_ONLY / RECEIPT_SCHEMA_CANDIDATE / DRAFT_SCHEMA / ACTIVE_SCHEMA / MIGRATE_TO_AGRICULTURE_ROOT / MIGRATE_TO_RECEIPTS / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/agriculture/receipts/... or current schema path>

## Paired contract
<contract path or N/A>

## Receipt instance lane
<data receipt path or NEEDS VERIFICATION>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical receipt schema path is linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Receipt instance lane is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Receipt/proof/catalog/release boundaries are preserved.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/agriculture/receipts/`.
- [ ] Confirm whether Agriculture receipt schemas belong in this sublane or the Agriculture schema root.
- [ ] Resolve hyphen/underscore contract path conflict for `aggregation-receipt` / `aggregation_receipt`.
- [ ] Confirm paired Agriculture contract paths.
- [ ] Confirm receipt instance lane for Agriculture receipts.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/contracts/v1/domains/agriculture/README.md` should index this receipts lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Receipt schema-home decision, new Agriculture receipt schema, migration note, validator update, fixture update, schema registry update, ADR update, Agriculture receipt contract update, receipt instance lane update, or compatibility-lane decision |

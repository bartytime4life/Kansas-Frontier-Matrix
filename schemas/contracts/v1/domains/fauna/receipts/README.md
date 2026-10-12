# `schemas/contracts/v1/domains/fauna/receipts/` — Fauna Receipts Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-fauna-receipts-readme
title: schemas/contracts/v1/domains/fauna/receipts/ — Fauna Receipts Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <fauna-domain-steward>
  - <receipt-steward>
  - <redaction-steward>
  - <sensitivity-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, fauna, receipts, redaction-receipt, geoprivacy, sensitivity, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-fauna-green)
![family](https://img.shields.io/badge/family-receipts-blueviolet)
![posture](https://img.shields.io/badge/posture-schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)

## Purpose

`schemas/contracts/v1/domains/fauna/receipts/` is a draft Fauna schema sublane for receipt-shaped Fauna objects.

This path should index machine-checkable schema shapes for Fauna receipt objects, especially redaction and public-safe transformation receipts. It must not store emitted receipt instances, proof records, catalog records, release manifests, release decisions, policy decisions, sensitive coordinates, or public artifacts.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, lifecycle data, receipt data, proof output, sensitivity decision, redaction approval, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Fauna receipts schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/fauna/receipts/` |
| Status | Draft |
| Authority level | Schema-index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, receipt-family rules, sensitivity rules, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Fauna schema lane | `schemas/contracts/v1/domains/fauna/` exists as a PROPOSED greenfield scaffold. |
| Confirmed related schema | `schemas/contracts/v1/domains/fauna/redaction_receipt.schema.json` exists as a PROPOSED scaffold. |
| Confirmed related contract | `contracts/domains/fauna/redaction_receipt.md` exists and describes Fauna-specific redaction receipt semantics. |
| Placement posture | CONFLICTED / NEEDS VERIFICATION. The Fauna redaction receipt contract says the receipt schema home is open and may belong under a shared receipt/correction family pending ADR resolution. |
| Receipt boundary | Schema shape belongs under `schemas/`; emitted receipt instances belong in governed receipt/data lanes once confirmed. |
| Sensitivity posture | Fail closed. Do not encode sensitive location, re-identification details, or reversible redaction parameters in schema docs. |
| Required reviewers | Schema steward, Fauna steward, receipt steward, redaction steward, sensitivity steward, contract steward, validation steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms `schemas/contracts/v1/domains/fauna/README.md` exists as a PROPOSED Fauna domain schema scaffold.

Current-session evidence confirms `contracts/domains/fauna/redaction_receipt.md` exists and states that `RedactionReceipt` records a public-safe transformation or withholding action but does not decide policy approval, review sufficiency, rights clearance, release, or safety by itself.

Current-session evidence confirms `schemas/contracts/v1/domains/fauna/redaction_receipt.schema.json` exists as a PROPOSED scaffold with empty properties and `additionalProperties: true`.

Current-session evidence from ADR-0011 states the governance separation: receipt, proof, catalog, and publication are distinct families. This schema lane may define receipt shape, but it does not store or publish receipt instances.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── fauna/
                ├── README.md
                ├── redaction_receipt.schema.json       # confirmed PROPOSED scaffold
                └── receipts/
                    └── README.md                       # you are here

contracts/
└── domains/
    └── fauna/
        └── redaction_receipt.md                        # semantic contract; not schema shape

data/
├── receipts/                                            # emitted receipt instances; exact Fauna lane NEEDS VERIFICATION
├── proofs/fauna/                                        # proof objects; not receipt schemas
├── catalog/domain/fauna/                                # catalog records; not receipt schemas
└── registry/                                            # registry records; not receipt schemas

policy/
├── domains/fauna/                                       # policy decisions/rules; not schema shape
└── sensitivity/fauna/                                   # sensitivity posture; not schema shape

release/                                                 # release decisions and manifests; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/fauna/receipts/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes for receipts, proofs, registries, releases, and schemas require ADR review. |
| Search for Fauna receipt surfaces | Found `contracts/domains/fauna/redaction_receipt.md`, Fauna registry, proof, catalog, reports, processed, rollback, fixture, and source-registry surfaces. |
| `schemas/contracts/v1/domains/fauna/README.md` | Existing Fauna domain schema scaffold; status PROPOSED. |
| `contracts/domains/fauna/redaction_receipt.md` | Fauna redaction receipt semantic contract; placement is CONFLICTED / NEEDS VERIFICATION. |
| `schemas/contracts/v1/domains/fauna/redaction_receipt.schema.json` | Existing PROPOSED scaffold schema. |
| ADR-0011 | Proposed separation rule: receipt, proof, catalog, and publication are distinct families; schema homes remain governed by ADR-0001. |

This README does not verify complete receipt schema fields, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, emitted receipt instance layout, or runtime redaction behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `../redaction_receipt.schema.json` | `contracts/domains/fauna/redaction_receipt.md` | PROPOSED / scaffold / CONFLICTED placement | Schema exists at the Fauna domain schema root, not inside `receipts/`; contract says receipt schema home may need shared receipt/correction placement. |

## Candidate receipt-shape families

Candidate Fauna receipt schemas should be introduced only after contract, fixture, validator, registry, sensitivity-review, and steward support is clear.

| Candidate family | Status | Notes |
|---|---|---|
| Fauna redaction receipt | PROPOSED scaffold / NEEDS VERIFICATION | Existing schema scaffold and paired contract exist; field realization and home remain open. |
| Fauna public-safe transformation receipt | NEEDS VERIFICATION | Could describe public-safe transformation shape if accepted. |
| Fauna suppression / withholding receipt | NEEDS VERIFICATION | Could describe withholding action shape without leaking sensitive detail. |
| Fauna release-support receipt | NEEDS VERIFICATION | Could describe release-support process memory without becoming release authority. |
| Fauna correction / rollback receipt | NEEDS VERIFICATION | Could describe correction-support process memory without replacing CorrectionNotice or rollback records. |

## Receipts-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Schema index | Track Fauna receipt schema files and their placement status. |
| Contract pairing | Link each receipt schema to a Fauna or shared receipt semantic contract when verified. |
| Instance separation | Keep emitted receipt records outside `schemas/`. |
| Family separation | Do not collapse receipts into proofs, catalog records, release manifests, policy approvals, or correction notices. |
| Sensitivity discipline | Avoid encoding sensitive location, reversible redaction parameters, or re-identification details. |
| Drift prevention | Prevent duplicate receipt schemas under conflicting Fauna, correction, or shared receipt paths. |
| Fixture linkage | Point to valid, invalid, public-safe, and sensitivity-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Fauna-owned receipt schema files once placement is confirmed.
- Short schema-family index notes.
- Migration notes for receipt schema placement.
- Drift notes about duplicate or stale Fauna receipt schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, sensitivity references, release references, and tests.
- Public-safe notes that preserve the receipt/proof/catalog/release separation.

## What does not belong here

- Emitted receipt instances.
- Proof records.
- Catalog records.
- Registry records.
- Release manifests or release decisions.
- Policy approvals or sensitivity decisions.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- Sensitive coordinates, private-land joins, exact site details, telemetry details, reversible redaction parameters, or re-identification-enabling details.
- Public API or map/UI behavior.
- Claims that a receipt schema is complete without fixtures, validators, registry records, sensitivity review, and steward review support.

## Receipt schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate receipt schema locations. |
| `RECEIPT_SCHEMA_CANDIDATE` | The schema may become an accepted Fauna receipt schema. |
| `DRAFT_SCHEMA` | Schema exists but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, sensitivity posture, and review status. |
| `MIGRATE_TO_FAUNA_ROOT` | Content belongs directly under `schemas/contracts/v1/domains/fauna/`. |
| `MIGRATE_TO_RECEIPTS` | Content belongs under this receipts sublane. |
| `MIGRATE_TO_SHARED_RECEIPT` | Content belongs under a shared receipt schema family. |
| `MIGRATE_TO_CORRECTION` | Content belongs under a correction/correction-adjacent schema family. |
| `HELD_FOR_REVIEW` | Content requires schema, receipt, sensitivity, policy, or release review before use. |
| `DEPRECATED` | Content should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Minimal receipt schema note

```markdown
# <fauna-receipt-schema-note-id>

## Status
INDEX_ONLY / RECEIPT_SCHEMA_CANDIDATE / DRAFT_SCHEMA / ACTIVE_SCHEMA / MIGRATE_TO_FAUNA_ROOT / MIGRATE_TO_RECEIPTS / MIGRATE_TO_SHARED_RECEIPT / MIGRATE_TO_CORRECTION / HELD_FOR_REVIEW / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/fauna/receipts/... or current schema path>

## Paired contract
<contract path or N/A>

## Receipt instance lane
<data receipt path or NEEDS VERIFICATION>

## Sensitivity posture
<public-safe / generalized / withheld / held / denied / NEEDS VERIFICATION>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Notes
<short note grounded in repo evidence, without sensitive details>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical receipt schema path is linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Receipt instance lane is linked or marked NEEDS VERIFICATION.
- [ ] Sensitivity posture is explicit.
- [ ] Shared receipt/correction home conflict is resolved or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Public-safe or sensitivity-case fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Receipt/proof/catalog/release/policy boundaries are preserved.
- [ ] No sensitive location, private-land join, telemetry detail, or reversible redaction detail is stored here.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/fauna/receipts/`.
- [ ] Confirm whether Fauna receipt schemas belong in this sublane, the Fauna schema root, a shared receipt family, or a correction/correction-adjacent family.
- [ ] Resolve the redaction receipt schema-home conflict noted by the paired contract.
- [ ] Confirm paired Fauna contract paths.
- [ ] Confirm receipt instance lane for Fauna receipts.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe and sensitivity-case fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm sensitivity, policy, release, correction, and rollback references.
- [ ] Confirm whether `schemas/contracts/v1/domains/fauna/README.md` should index this receipts lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Receipt schema-home decision, new Fauna receipt schema, redaction-receipt migration note, validator update, fixture update, schema registry update, ADR update, Fauna receipt contract update, sensitivity-policy update, receipt instance lane update, or compatibility-lane decision |

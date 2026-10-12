# `schemas/contracts/v1/domains/fauna/` — Fauna Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-fauna-readme
title: schemas/contracts/v1/domains/fauna/ — Fauna Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <fauna-domain-steward>
  - <sensitivity-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, fauna, geoprivacy, sensitivity, receipts, redaction-receipt, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-fauna-green)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)

## Purpose

`schemas/contracts/v1/domains/fauna/` is the draft Fauna domain schema lane.

This path is for machine-checkable Fauna schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, sensitivity references, receipt references, correction references, rollback references, and release references.

This path is not a home for Fauna contract prose, policy rules, validator code, packages, pipelines, lifecycle data, source registry records, emitted receipts, proof outputs, catalog records, release records, review records, or public map/API artifacts.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, lifecycle data, registry data, proof output, receipt instance, source descriptor instance, sensitivity decision, redaction approval, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Fauna domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/fauna/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, sensitivity records, receipt records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED Fauna domain schema lane under ADR-0001. Implementation completeness remains NEEDS VERIFICATION. |
| Known child lanes | `receipts/` README exists and is a draft index. |
| Known schema file | `redaction_receipt.schema.json` exists as a PROPOSED scaffold, with placement conflict noted by its paired contract. |
| Sensitivity posture | Fail closed. Sensitive taxa, exact occurrence geometry, sensitive sites, telemetry, steward-controlled records, and private-land joins must not leak through schema docs. |
| Required reviewers | Schema steward, Fauna domain steward, sensitivity steward, contract steward, validation steward, policy steward where applicable, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms `docs/domains/fauna/README.md` identifies `schemas/contracts/v1/domains/fauna/` as the Fauna schema home and sets the Fauna lane's deny-by-default sensitivity posture.

Current-session evidence confirms `docs/domains/fauna/SCHEMAS.md` says the `.schema.json` files under this path are authoritative machine shapes, while the docs file is only a prose crosswalk.

Current-session evidence confirms `schemas/contracts/v1/domains/fauna/receipts/README.md` exists as a draft Fauna receipt schema index.

Current-session evidence confirms `schemas/contracts/v1/domains/fauna/redaction_receipt.schema.json` exists as a PROPOSED scaffold schema.

Current-session evidence confirms `contracts/domains/fauna/redaction_receipt.md` exists and marks the redaction receipt schema-home question as CONFLICTED / NEEDS VERIFICATION.

Current-session evidence confirms this path already had a greenfield scaffold. This update narrows the README to the actual `schemas/` responsibility: machine-checkable shape and schema-index support only.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── fauna/
                ├── README.md                         # you are here
                ├── redaction_receipt.schema.json     # confirmed PROPOSED scaffold
                └── receipts/
                    └── README.md

contracts/
└── domains/
    └── fauna/                                        # semantic meaning; not schema shape
        └── redaction_receipt.md

policy/
├── domains/fauna/                                    # admissibility/policy; not schema shape
└── sensitivity/fauna/                                # sensitivity policy; not schema shape

fixtures/
└── domains/fauna/                                    # test examples; coverage NEEDS VERIFICATION

data/                                                 # lifecycle, registry, proof, receipt roots; not schema home

release/                                              # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/fauna/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes for receipts, proofs, registries, releases, and schemas require ADR review. |
| `docs/domains/fauna/README.md` | Human-facing Fauna domain lane; confirms schema home and deny-by-default sensitivity posture. |
| `docs/domains/fauna/SCHEMAS.md` | Prose crosswalk; says authoritative shapes are `.schema.json` files under this path and flags receipt-schema-home questions. |
| `schemas/contracts/v1/domains/fauna/receipts/README.md` | Existing Fauna receipts schema index. |
| `contracts/domains/fauna/redaction_receipt.md` | Fauna redaction receipt semantic contract; placement is CONFLICTED / NEEDS VERIFICATION. |
| `schemas/contracts/v1/domains/fauna/redaction_receipt.schema.json` | Existing PROPOSED scaffold schema. |
| ADR-0011 | Proposed separation rule: receipt, proof, catalog, and publication are distinct families; schema homes remain governed by ADR-0001. |

This README does not verify complete Fauna schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, sensitivity-policy behavior, release integration, runtime behavior, or public API/UI behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `redaction_receipt.schema.json` | `contracts/domains/fauna/redaction_receipt.md` | PROPOSED / scaffold / CONFLICTED placement | Schema has `$schema`, `$id`, title, description, empty `properties`, `additionalProperties: true`, and `x-kfm.status: PROPOSED`; paired contract says receipt schema home may need shared receipt/correction placement. |

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| `receipts/` | Draft index | Fauna receipt schema index; must not store emitted receipt instances or collapse receipts with proofs, catalog records, policy decisions, correction notices, or release records. |

## Candidate schema inventory

Fauna schema candidates below come from current Fauna schema/docs evidence and require steward review, schema files, paired contracts, fixtures, validators, registry records, and CI support before promotion.

| Candidate schema | Status | Notes |
|---|---|---|
| `taxon.schema.json` | NEEDS VERIFICATION | Candidate animal taxonomic identity shape. |
| `taxon_crosswalk.schema.json` | NEEDS VERIFICATION | Candidate authority-taxonomy mapping shape. |
| `conservation_status.schema.json` | NEEDS VERIFICATION | Candidate conservation/legal status shape. |
| `occurrence_evidence.schema.json` | NEEDS VERIFICATION | Candidate evidence-bearing occurrence shape. |
| `occurrence_restricted.schema.json` | NEEDS VERIFICATION | Candidate restricted occurrence shape; sensitive by default. |
| `occurrence_public.schema.json` | NEEDS VERIFICATION | Candidate public-safe occurrence shape; must require generalization/redaction support where sensitive. |
| `range_polygon.schema.json` | NEEDS VERIFICATION | Candidate range geometry shape. |
| `seasonal_range.schema.json` | NEEDS VERIFICATION | Candidate seasonal range shape. |
| `migration_route.schema.json` | NEEDS VERIFICATION | Candidate migration route shape; sensitivity review may apply. |
| `monitoring_event.schema.json` | NEEDS VERIFICATION | Candidate monitoring-event shape. |
| `sensitive_site.schema.json` | NEEDS VERIFICATION | Candidate sensitive-site shape; fail-closed. |
| `mortality_observation.schema.json` | NEEDS VERIFICATION | Candidate mortality observation shape. |
| `disease_observation.schema.json` | NEEDS VERIFICATION | Candidate disease observation shape. |
| `invasive_species_record.schema.json` | NEEDS VERIFICATION | Candidate invasive-species record shape. |
| `redaction_receipt.schema.json` | PROPOSED scaffold / CONFLICTED placement | Existing scaffold; receipt-family home remains open. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Fauna schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/fauna/` or another verified contract lane. |
| Sensitivity discipline | Keep sensitive location, telemetry, steward-controlled details, and reversible redaction details out of README prose. |
| Receipt discipline | Keep `receipts/` as a scoped sublane with its own review status until receipt-home questions are resolved. |
| Boundary preservation | Keep policy, fixtures, validators, lifecycle data, source registry records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across domain root, child lanes, shared receipt/correction lanes, and cross-domain lanes. |
| Fixture linkage | Point to valid, invalid, public-safe, and sensitivity-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Fauna JSON Schema files.
- Fauna schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Fauna schema placement.
- Drift notes about duplicate or stale Fauna schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, sensitivity references, receipt references, release references, correction references, rollback references, and tests.
- Public-safe notes that preserve geoprivacy and do not expose sensitive details.

## What does not belong here

- Contract prose.
- Policy rules.
- Sensitivity decisions or review records.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipt instances.
- Proof outputs.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public API or map/UI behavior.
- Sensitive coordinates, private-land joins, exact site details, telemetry details, reversible redaction parameters, or re-identification-enabling details.
- Cross-domain schemas that belong under `schemas/contracts/v1/cross/` or another lowest-common responsibility root.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema is complete without fixtures, validators, registry records, sensitivity review, and steward review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, sensitivity posture, and review status. |
| `SENSITIVITY_HELD` | Schema or fixture work requires sensitivity/steward review before use. |
| `PUBLIC_SAFE_ALIAS` | Schema or fixture only exposes generalized/public-safe shape. |
| `EXTENSION_INDEX` | Child lane indexes extension schemas but has not accepted a concrete schema yet. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Minimal schema note

```markdown
# <fauna-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / SENSITIVITY_HELD / PUBLIC_SAFE_ALIAS / EXTENSION_INDEX / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/fauna/...>

## Paired contract
<contracts/domains/fauna/... or N/A>

## Child lane
<root / receipts / other / N/A>

## Sensitivity posture
<public-safe / generalized / restricted / held / denied / NEEDS VERIFICATION>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Policy references
<policy path or N/A>

## Receipt, correction, or rollback references
<data/release path or N/A>

## Release references
<release path or N/A>

## Notes
<short note grounded in repo evidence, without sensitive details>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Schema has a stable `$id`.
- [ ] Schema has `$schema` set to JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Sensitivity posture is explicit.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Public-safe or sensitivity-case fixtures are linked or marked NEEDS VERIFICATION where applicable.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Child-lane placement is justified when schema is not at the Fauna schema root.
- [ ] Receipt-home conflict is resolved or marked NEEDS VERIFICATION where receipt objects are involved.
- [ ] Policy, data, receipt-instance, registry-instance, proof, catalog, correction, rollback, and release records remain outside `schemas/`.
- [ ] No sensitive location, private-land join, telemetry detail, or reversible redaction detail is stored here.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
taxon.schema.json
taxon_crosswalk.schema.json
conservation_status.schema.json
occurrence_evidence.schema.json
occurrence_restricted.schema.json
occurrence_public.schema.json
range_polygon.schema.json
seasonal_range.schema.json
migration_route.schema.json
monitoring_event.schema.json
sensitive_site.schema.json
mortality_observation.schema.json
disease_observation.schema.json
invasive_species_record.schema.json
redaction_receipt.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. Do not encode sensitive locations, taxon-specific protected details, source-specific private joins, or reviewer details into filenames.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/fauna/`.
- [ ] Confirm complete Fauna schema inventory.
- [ ] Confirm which candidate schema files exist beyond `redaction_receipt.schema.json`.
- [ ] Confirm whether `redaction_receipt.schema.json` should remain at the Fauna schema root, move under `receipts/`, move to a shared receipt family, or move to a correction/correction-adjacent family.
- [ ] Resolve the redaction receipt schema-home conflict noted by `contracts/domains/fauna/redaction_receipt.md` and `docs/domains/fauna/SCHEMAS.md`.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe and sensitivity-case fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm sensitivity, policy, receipt, correction, rollback, proof, catalog, and release references for Fauna schemas.
- [ ] Confirm whether `schemas/README.md` should index this Fauna domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | New Fauna schema, child-lane decision, receipt-home decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Fauna contract update, sensitivity-policy update, receipt/correction/rollback reference update, release reference update, or compatibility-lane decision |

# `schemas/contracts/v1/domains/flora/` — Flora Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-flora-readme
title: schemas/contracts/v1/domains/flora/ — Flora Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <flora-domain-steward>
  - <sensitivity-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, flora, rare-plants, geoprivacy, sensitivity, redaction-receipt, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-flora-green)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)

## Purpose

`schemas/contracts/v1/domains/flora/` is the draft Flora domain schema lane.

This path is for machine-checkable Flora schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, sensitivity references, receipt references, correction references, rollback references, and release references.

This path is not a home for Flora contract prose, policy rules, validator code, packages, pipelines, lifecycle data, source registry records, emitted receipts, proof outputs, catalog records, release records, review records, or public map/API artifacts.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, lifecycle data, registry data, proof output, receipt instance, source descriptor instance, sensitivity decision, redaction approval, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Flora domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/flora/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, sensitivity records, receipt records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED Flora domain schema lane under ADR-0001. Implementation completeness remains NEEDS VERIFICATION. |
| Known schema file | `redaction_receipt.schema.json` exists as a PROPOSED scaffold. |
| Sensitivity posture | Fail closed. Rare/protected/culturally sensitive plants, exact sensitive occurrence geometry, steward-controlled records, and sensitive plant knowledge must not leak through schema docs. |
| Required reviewers | Schema steward, Flora domain steward, sensitivity steward, contract steward, validation steward, policy steward where applicable, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms `docs/domains/flora/README.md` identifies `schemas/contracts/v1/domains/flora/` as the Flora machine-shape lane and sets Flora sensitivity to deny-by-default for sensitive plant locations.

Current-session evidence confirms `docs/domains/flora/CANONICAL_PATHS.md` applies the responsibility-root lane pattern to Flora, records the schema-home path-segment conflict history, and follows Directory Rules plus ADR-0001 for `schemas/contracts/v1/domains/flora/`.

Current-session search found Flora semantic contracts for `flora_occurrence`, `redaction_receipt`, `rare_plant_record`, `occurrence_restricted`, `occurrence_public`, `specimen_record`, `vegetation_community`, `range_polygon`, `invasive_plant_record`, `restoration_planting`, and related domain objects.

Current-session evidence confirms `schemas/contracts/v1/domains/flora/redaction_receipt.schema.json` exists as a PROPOSED scaffold schema.

Current-session evidence confirms `contracts/domains/flora/redaction_receipt.md` exists and states the paired schema is a PROPOSED scaffold; the receipt records a protective transform but does not authorize publication or replace policy, review, validation, release, correction, or rollback authority.

Current-session evidence confirms this path already had a greenfield scaffold. This update narrows the README to the actual `schemas/` responsibility: machine-checkable shape and schema-index support only.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── flora/
                ├── README.md                         # you are here
                └── redaction_receipt.schema.json     # confirmed PROPOSED scaffold

contracts/
└── domains/
    └── flora/                                        # semantic meaning; not schema shape
        ├── flora_occurrence.md
        ├── rare_plant_record.md
        ├── occurrence_restricted.md
        ├── occurrence_public.md
        ├── specimen_record.md
        ├── vegetation_community.md
        ├── invasive_plant_record.md
        ├── range_polygon.md
        ├── restoration_planting.md
        └── redaction_receipt.md

policy/
├── domains/flora/                                    # admissibility/policy; not schema shape
└── sensitivity/flora/                                # sensitivity policy; not schema shape

fixtures/
└── domains/flora/                                    # test examples; coverage NEEDS VERIFICATION

data/                                                 # lifecycle, registry, proof, receipt roots; not schema home

release/                                              # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/flora/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes for receipts, proofs, registries, releases, and schemas require ADR review. |
| `docs/domains/flora/README.md` | Human-facing Flora domain lane; confirms schema lane and deny-by-default sensitivity posture. |
| `docs/domains/flora/CANONICAL_PATHS.md` | Flora canonical path register; confirms lane pattern and notes schema-home path-segment conflict history. |
| Search for Flora schema/contract surfaces | Found Flora contracts including occurrence, rare plant, invasive plant, vegetation, range, restoration, and redaction receipt surfaces. |
| `schemas/contracts/v1/domains/flora/redaction_receipt.schema.json` | Existing PROPOSED scaffold schema. |
| `contracts/domains/flora/redaction_receipt.md` | Flora redaction receipt semantic contract; paired schema is a scaffold and receipt is not release approval. |

This README does not verify complete Flora schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, sensitivity-policy behavior, release integration, runtime behavior, or public API/UI behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `redaction_receipt.schema.json` | `contracts/domains/flora/redaction_receipt.md` | PROPOSED / scaffold | Schema has `$schema`, `$id`, title, description, empty `properties`, `additionalProperties: true`, and `x-kfm.status: PROPOSED`; paired contract says field-level machine enforcement remains NEEDS VERIFICATION. |

## Candidate schema inventory

Flora schema candidates below come from current Flora docs/search evidence and require steward review, schema files, paired contracts, fixtures, validators, registry records, and CI support before promotion.

| Candidate schema | Status | Notes |
|---|---|---|
| `plant_taxon.schema.json` | NEEDS VERIFICATION | Candidate plant taxonomic identity shape. |
| `flora_taxon_crosswalk.schema.json` | NEEDS VERIFICATION | Candidate authority-taxonomy mapping shape. |
| `specimen_record.schema.json` | NEEDS VERIFICATION | Candidate specimen/evidence record shape. |
| `flora_occurrence.schema.json` | NEEDS VERIFICATION | Candidate Flora occurrence shape. |
| `occurrence_restricted.schema.json` | NEEDS VERIFICATION | Candidate restricted occurrence shape; rare/protected plants fail closed. |
| `occurrence_public.schema.json` | NEEDS VERIFICATION | Candidate public-safe occurrence shape; must preserve redaction/generalization support where sensitive. |
| `rare_plant_record.schema.json` | NEEDS VERIFICATION | Candidate rare/protected plant shape; fail-closed. |
| `phenology_observation.schema.json` | NEEDS VERIFICATION | Candidate phenology observation shape. |
| `vegetation_community.schema.json` | NEEDS VERIFICATION | Candidate vegetation-community shape. |
| `invasive_plant_record.schema.json` | NEEDS VERIFICATION | Candidate invasive-plant record shape. |
| `range_polygon.schema.json` | NEEDS VERIFICATION | Candidate range/distribution geometry shape. |
| `habitat_association.schema.json` | NEEDS VERIFICATION | Candidate Flora-owned habitat-association reference shape; Habitat-owned truth remains elsewhere. |
| `botanical_survey.schema.json` | NEEDS VERIFICATION | Candidate survey/event shape. |
| `restoration_planting.schema.json` | NEEDS VERIFICATION | Candidate restoration planting shape. |
| `domain_observation.schema.json` | NEEDS VERIFICATION | Candidate generic Flora domain observation shape. |
| `domain_feature_identity.schema.json` | NEEDS VERIFICATION | Candidate deterministic identity support shape. |
| `domain_validation_report.schema.json` | NEEDS VERIFICATION | Candidate validation-report shape; not proof or release authority. |
| `redaction_receipt.schema.json` | PROPOSED scaffold | Existing scaffold for protective transform receipt shape. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Flora schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/flora/` or another verified contract lane. |
| Sensitivity discipline | Keep sensitive location, steward-controlled details, culturally sensitive knowledge, and reversible redaction details out of README prose. |
| Receipt discipline | Keep redaction receipt shape separate from policy approval, release decisions, proofs, catalog records, and rollback records. |
| Boundary preservation | Keep policy, fixtures, validators, lifecycle data, source registry records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across domain root, shared receipt/correction lanes, and cross-domain lanes. |
| Fixture linkage | Point to valid, invalid, public-safe, and sensitivity-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Flora JSON Schema files.
- Flora schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Flora schema placement.
- Drift notes about duplicate or stale Flora schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, sensitivity references, receipt references, release references, correction references, rollback references, and tests.
- Public-safe notes that preserve geoprivacy and do not expose sensitive Flora details.

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
- Rare-plant exact locations, culturally sensitive plant knowledge, private-land joins, precise steward-controlled observations, reversible redaction parameters, or re-identification-enabling details.
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
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Minimal schema note

```markdown
# <flora-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / SENSITIVITY_HELD / PUBLIC_SAFE_ALIAS / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/flora/...>

## Paired contract
<contracts/domains/flora/... or N/A>

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
- [ ] Policy, data, receipt-instance, registry-instance, proof, catalog, correction, rollback, and release records remain outside `schemas/`.
- [ ] No rare-plant exact location, culturally sensitive plant knowledge, private-land join, or reversible redaction detail is stored here.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
plant_taxon.schema.json
flora_taxon_crosswalk.schema.json
specimen_record.schema.json
flora_occurrence.schema.json
occurrence_restricted.schema.json
occurrence_public.schema.json
rare_plant_record.schema.json
phenology_observation.schema.json
vegetation_community.schema.json
invasive_plant_record.schema.json
range_polygon.schema.json
habitat_association.schema.json
botanical_survey.schema.json
restoration_planting.schema.json
domain_observation.schema.json
domain_feature_identity.schema.json
domain_validation_report.schema.json
redaction_receipt.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. Do not encode sensitive locations, taxon-specific protected details, source-specific private joins, steward-controlled knowledge, or reviewer details into filenames.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/flora/`.
- [ ] Confirm complete Flora schema inventory.
- [ ] Confirm which candidate schema files exist beyond `redaction_receipt.schema.json`.
- [ ] Confirm whether `redaction_receipt.schema.json` should remain at the Flora schema root, move under a future `receipts/` sublane, move to a shared receipt family, or move to a correction/correction-adjacent family.
- [ ] Resolve any schema-home path-segment conflict noted by `docs/domains/flora/CANONICAL_PATHS.md`.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe and sensitivity-case fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm sensitivity, policy, receipt, correction, rollback, proof, catalog, and release references for Flora schemas.
- [ ] Confirm whether `schemas/README.md` should index this Flora domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | New Flora schema, schema-home decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Flora contract update, sensitivity-policy update, receipt/correction/rollback reference update, release reference update, or compatibility-lane decision |

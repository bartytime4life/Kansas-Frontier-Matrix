# `schemas/contracts/v1/domains/archaeology/` — Archaeology Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-archaeology-readme
title: schemas/contracts/v1/domains/archaeology/ — Archaeology Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, archaeology, cultural-heritage, sensitive-domain, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-archaeology-purple)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)

## Purpose

`schemas/contracts/v1/domains/archaeology/` is the draft Archaeology domain schema lane.

This path is for machine-checkable Archaeology and cultural-heritage schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, review references, and release references.

This path must not store sensitive site details, source payloads, exact geometry, candidate details, private-owner details, cultural-review records, emitted receipts, proof records, registry records, policy rules, or release records.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, lifecycle data, registry data, proof output, cultural-review record, receipt instance, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Archaeology domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/archaeology/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, cultural/steward review records, policy records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED Archaeology domain schema lane under ADR-0001. Implementation completeness remains NEEDS VERIFICATION. |
| Shorter alias lane | `schemas/contracts/v1/archaeology/` exists as a compatibility/index lane pointing toward this domain path. |
| Schema inventory | NEEDS VERIFICATION. Current-session search found Archaeology contract surfaces but did not confirm concrete schema files under this path. |
| Sensitivity posture | Fail closed. Schema work must not expose protected location or sensitive cultural details. |
| Required reviewers | Schema steward, Archaeology domain steward, cultural-review steward, contract steward, validation steward where applicable, policy steward where applicable, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence confirms `schemas/contracts/v1/archaeology/README.md` is a shorter Archaeology compatibility lane that points toward `schemas/contracts/v1/domains/archaeology/` as the candidate canonical domain schema home.

Current-session evidence from Archaeology domain documentation references `schemas/contracts/v1/domains/archaeology/` as a related implementation path and sets exact-location release to fail closed unless recorded review, transformation, evidence, release, and rollback support exist.

Current-session evidence confirms this path already had a greenfield scaffold. This update narrows the README to the actual `schemas/` responsibility: machine-checkable shape and schema-index support only.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── archaeology/                         # shorter compatibility/index lane
        └── domains/
            └── archaeology/
                └── README.md                    # you are here

contracts/
└── domains/
    └── archaeology/                             # semantic meaning; not schema shape

policy/
└── domains/
    └── archaeology/                             # admissibility/sensitivity policy; not schema shape

fixtures/
└── domains/
    ├── archaeology/                             # test examples; coverage NEEDS VERIFICATION
    └── archaeology-public-safe/                 # public-safe examples; coverage NEEDS VERIFICATION

data/                                            # lifecycle, registry, proof, and receipt roots; not schema home

release/                                         # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/archaeology/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `schemas/contracts/v1/archaeology/README.md` | Existing shorter compatibility index for Archaeology schema placement. |
| `docs/domains/archaeology/README.md` | Archaeology documentation references this schema path and states the domain's fail-closed exact-location posture. |
| Search for Archaeology schema/material surfaces | Found Archaeology contract and documentation surfaces; did not confirm concrete schema files under this path in this edit. |

This README does not verify complete Archaeology schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, cultural-review workflow behavior, policy behavior, release integration, runtime behavior, or public API/UI behavior.

## Candidate contract inventory

Current-session search found Archaeology semantic contracts that may require paired schemas after steward review:

| Contract surface | Status | Schema note |
|---|---|---|
| `contracts/domains/archaeology/site.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/archaeological_site.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/cultural_review.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/steward_review.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/sensitivity_transform.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/publication_transform_receipt.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/survey_project.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/lidar_candidate.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/remote_sensing_anomaly.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/provenience_context.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/excavation_unit.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/stratigraphic_unit.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/geophysics_observation.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/three_d_documentation.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/domain_layer_descriptor.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/domain_observation.md` | Found by search | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/archaeology/domain_validation_report.md` | Found by search | Paired schema NEEDS VERIFICATION. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Archaeology schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/archaeology/` or another verified contract lane. |
| Alias discipline | Keep `schemas/contracts/v1/archaeology/` as compatibility/index unless an ADR or migration note changes it. |
| Sensitivity discipline | Prevent sensitive locations, protected cultural details, or candidate details from being stored in schema docs. |
| Boundary preservation | Keep policy, fixtures, validators, data records, proofs, receipts, registry records, review records, and release records in their own responsibility roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across short alias, domain root, child lanes, and cross-domain lanes. |
| Fixture linkage | Point to valid, invalid, public-safe, and sensitivity-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Archaeology JSON Schema files after placement and sensitivity review.
- Archaeology schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Archaeology schema placement.
- Drift notes about duplicate or stale Archaeology schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, review references, release references, and tests.
- Public-safe notes that do not expose sensitive locations or protected cultural details.

## What does not belong here

- Contract prose.
- Policy rules.
- Cultural-review records.
- Steward-review records.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Registry records.
- Proof outputs.
- Emitted receipt instances.
- Release records, release manifests, or release decisions.
- Public API or map/UI behavior.
- Exact locations, candidate-location details, private-owner details, burial/sacred-site details, collection-security details, or other protected sensitive content.
- Cross-domain schemas that belong under `schemas/contracts/v1/cross/`.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema is complete without fixtures, validators, registry records, sensitivity review, and steward review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, sensitivity posture, and review status. |
| `PUBLIC_SAFE_ALIAS` | Schema or fixture only exposes generalized/public-safe shape. |
| `HELD_FOR_REVIEW` | Schema needs cultural, steward, policy, or sensitivity review before use. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Minimal schema note

```markdown
# <archaeology-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / PUBLIC_SAFE_ALIAS / HELD_FOR_REVIEW / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/archaeology/...>

## Paired contract
<contracts/domains/archaeology/... or N/A>

## Sensitivity posture
<public-safe / generalized / held / denied / NEEDS VERIFICATION>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Policy and review references
<policy/review path or N/A>

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
- [ ] Cultural/steward review need is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Public-safe fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Short alias path does not contain duplicate canonical schema definitions.
- [ ] Policy, data, proof, review, receipt-instance, and release records remain outside `schemas/`.
- [ ] No sensitive location or protected cultural detail is stored here.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
archaeological_site.schema.json
site.schema.json
survey_project.schema.json
cultural_review.schema.json
steward_review.schema.json
sensitivity_transform.schema.json
publication_transform_receipt.schema.json
remote_sensing_anomaly.schema.json
lidar_candidate.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. Do not encode sensitive location or source-specific detail into schema filenames.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/archaeology/`.
- [ ] Confirm complete Archaeology schema inventory.
- [ ] Confirm which contract object names are canonical when duplicate or colloquial names exist.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, cultural-review, steward-review, and release references for Archaeology schemas.
- [ ] Confirm whether `schemas/contracts/v1/archaeology/README.md` remains a compatibility/index lane.
- [ ] Confirm whether `schemas/README.md` should index this Archaeology domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | New Archaeology schema, schema-home migration, validator update, fixture update, schema registry update, ADR update, Archaeology contract update, policy/review update, release reference update, or compatibility-lane decision |

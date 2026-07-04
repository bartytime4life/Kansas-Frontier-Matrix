# `schemas/contracts/v1/domains/people-dna-land/` — People / DNA / Land Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-people-dna-land-readme
title: schemas/contracts/v1/domains/people-dna-land/ — People / DNA / Land Domain Schema Index
version: v1
status: draft; PROPOSED; restricted-review; sublane-drift-visible
policy_label: restricted-review
owners:
  - <schema-steward>
  - <people-dna-land-domain-steward>
  - <privacy-steward>
  - <consent-steward>
  - <policy-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, people-dna-land, people, dna, land, identity, consent, restricted-review]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-people--dna--land-purple)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)
![sensitivity](https://img.shields.io/badge/sensitivity-restricted--review-critical)

## Purpose

`schemas/contracts/v1/domains/people-dna-land/` is the draft People / DNA / Land domain schema lane.

This path is for machine-checkable schema shapes for People / DNA / Land object families once those shapes are accepted: JSON Schema files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, schema registry records, tests, policy references, source-registry references, consent references, correction references, rollback references, and release references.

This path is **not** a home for contract prose, policy rules, consent records, source registry records, lifecycle data, proof outputs, emitted receipts, catalog records, release records, public API behavior, public map behavior, identity stores, title authority, raw source material, or generated-answer authority.

This README is documentation only. It is not itself a schema file, contract, policy, consent record, source record, data payload, proof, receipt, release decision, person store, identity truth, title opinion, or publication authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | People / DNA / Land domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/people-dna-land/` |
| Status | Draft / PROPOSED / restricted-review |
| Authority level | Domain schema index guidance. Actual schema files, paired contracts, schema registry records, validators, fixtures, tests, ADRs, policy records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED domain schema lane under ADR-0001. Implementation completeness remains NEEDS VERIFICATION. |
| Concrete schema inventory | NEEDS VERIFICATION. Current-session search did not confirm concrete `.schema.json` files under this path. |
| Child path posture | `people/`, `genealogy/`, and `land-ownership/` READMEs exist but are marked CONFLICTED / TRANSITIONAL because People/DNA/Land sublane doctrine rejects mirroring sublane segments into schema roots without further governance. |
| Default posture | Restricted review. Unsafe or insufficiently supported identity, relationship, DNA-derived, consent-dependent, land-link, or title-like outputs fail closed. |
| Required reviewers | Schema steward, People/DNA/Land domain steward, privacy steward, consent steward, policy steward, validation steward, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while policy, release, source identity, rights, sensitivity, lifecycle data, registries, proofs, receipts, and other authority families remain separate responsibility roots.

Current-session evidence confirms this README previously claimed broadly that docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, and data lifecycle artifacts could belong here. This update corrects that boundary: this path is schema-shape only.

Current-session People/DNA/Land sublane doctrine says sublanes are documentation navigation only and should not be mirrored into schema roots without further governance. That makes the existing `people/`, `genealogy/`, and `land-ownership/` schema child READMEs transitional warning surfaces rather than canonical schema homes.

Current-session evidence confirms the `people/`, `genealogy/`, and `land-ownership/` child READMEs are already marked CONFLICTED / TRANSITIONAL and tell maintainers not to add schema files there merely because those folders exist.

Current-session search did not confirm concrete People / DNA / Land `.schema.json` files under this path.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── people-dna-land/
                ├── README.md                  # you are here
                ├── people/
                │   └── README.md              # CONFLICTED / transitional
                ├── genealogy/
                │   └── README.md              # CONFLICTED / transitional
                └── land-ownership/
                    └── README.md              # CONFLICTED / transitional

contracts/
└── domains/
    └── people-dna-land/                        # semantic meaning; not schema shape

docs/
└── domains/
    └── people-dna-land/                        # doctrine and documentation navigation

fixtures/
└── domains/
    └── people-dna-land/                        # synthetic examples; not schema shape

policy/                                         # access, consent, sensitivity, release posture; not schema shape
data/                                           # lifecycle, registry, proof, receipt roots; not schema home
release/                                        # release decisions and records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/people-dna-land/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms responsibility-root placement and separate homes for machine shape, policy, source identity, rights, sensitivity, and release decisions. |
| `docs/domains/people-dna-land/sublanes/people_genealogy.md` | Proposed sublane decision; rejects mirroring sublane segments into schema roots. |
| `schemas/contracts/v1/domains/people-dna-land/people/README.md` | Existing People child warning index; CONFLICTED / transitional. |
| `schemas/contracts/v1/domains/people-dna-land/genealogy/README.md` | Existing Genealogy child warning index; CONFLICTED / transitional. |
| `schemas/contracts/v1/domains/people-dna-land/land-ownership/README.md` | Existing Land Ownership child warning index; CONFLICTED / transitional. |
| Search for People / DNA / Land schema files | Did not confirm concrete `.schema.json` files under this path. |

This README does not verify complete schema coverage, schema registry entries, validator wiring, CI behavior, policy enforcement, consent enforcement, release integration, runtime behavior, public API behavior, or UI behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| No concrete `.schema.json` file confirmed in this edit | N/A | NEEDS VERIFICATION | Current-session search found docs/contracts but did not confirm concrete schema files under this parent path. |

## Current child lanes

| Child path | Status | Recommended action |
|---|---|---|
| `people/` | CONFLICTED / transitional | Do not add schema files here until schema-home decision resolves cross-root sublane mirroring. |
| `genealogy/` | CONFLICTED / transitional | Do not add schema files here until schema-home decision resolves cross-root sublane mirroring. |
| `land-ownership/` | CONFLICTED / transitional | Do not add schema files here until schema-home decision resolves cross-root sublane mirroring. |

## Candidate schema families

Candidate shapes below should be placed only after resolving whether they belong directly in this parent lane, in a shared/common family, or in a steward-approved transitional path.

| Candidate schema family | Status |
|---|---|
| `person_assertion.schema.json` | NEEDS VERIFICATION |
| `person_identity_candidate.schema.json` | NEEDS VERIFICATION |
| `person_canonical.schema.json` | NEEDS VERIFICATION |
| `name_assertion.schema.json` | NEEDS VERIFICATION |
| `life_event.schema.json` | NEEDS VERIFICATION |
| `residence_event.schema.json` | NEEDS VERIFICATION |
| `migration_event.schema.json` | NEEDS VERIFICATION |
| `genealogy_relationship.schema.json` | NEEDS VERIFICATION |
| `family_group.schema.json` | NEEDS VERIFICATION |
| `relationship_hypothesis.schema.json` | NEEDS VERIFICATION |
| `land_ownership_assertion.schema.json` | NEEDS VERIFICATION |
| `land_instrument.schema.json` | NEEDS VERIFICATION |
| `parcel_version.schema.json` | NEEDS VERIFICATION |
| `ownership_interval.schema.json` | NEEDS VERIFICATION |
| `domain_observation.schema.json` | NEEDS VERIFICATION |
| `domain_validation_report.schema.json` | NEEDS VERIFICATION |
| `public_safe_summary.schema.json` | NEEDS VERIFICATION |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List accepted People / DNA / Land schema files after schema-home review. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/people-dna-land/` or another verified contract lane. |
| Sublane drift control | Keep `people/`, `genealogy/`, and `land-ownership/` child folders marked CONFLICTED / TRANSITIONAL until the cross-root sublane issue is resolved. |
| Restricted-review discipline | Treat identity, consent, DNA-derived, land-link, and title-like surfaces as restricted-review by default. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, lifecycle data, source registry records, consent records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across this parent path, child paths, common schema paths, and cross-domain schema paths. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable People / DNA / Land JSON Schema files once placement is confirmed.
- Schema index notes.
- Migration notes for People / DNA / Land schema placement.
- Drift notes about duplicate, transitional, or stale schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, source-registry references, consent references, release references, correction references, rollback references, and tests.

## What does not belong here

- Contract prose.
- Policy rules or sensitivity decisions.
- Consent records.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Source registry records or source descriptors.
- Emitted receipt instances.
- Proof outputs.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public API, UI, map, Focus Mode, or generated-answer artifacts.
- Person stores, identity-truth stores, title opinions, legal determinations, or publication authority.
- Child sublane schema files unless placement is resolved by a steward decision, ADR, or migration note.
- Claims that a schema is complete without fixtures, validators, registry records, policy checks, consent checks, and steward review.

## Schema status values

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `PATH_CONFLICT` | Schema placement is blocked by unresolved child-sublane mirroring conflict. |
| `PROFILE` | Schema profiles a shared source, identity, consent, spatial, time, or common schema without creating duplicate authority. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, policy, consent, or CI support has not been verified. |

## Review checklist

- [ ] Complete schema inventory is confirmed.
- [ ] Accepted schema files live in the steward-approved schema home.
- [ ] Child-path conflict for `people/`, `genealogy/`, and `land-ownership/` is resolved or kept explicitly transitional.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION for each schema.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid synthetic fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid synthetic fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Policy, consent, sensitivity, release, correction, and rollback references are linked or marked NEEDS VERIFICATION where applicable.
- [ ] Pipeline, data, registry, proof, receipt, catalog, and release records remain outside `schemas/`.
- [ ] No restricted payload material is stored here.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern once placement is accepted:

```text
<object_name>.schema.json
```

Examples:

```text
person_assertion.schema.json
person_identity_candidate.schema.json
name_assertion.schema.json
life_event.schema.json
residence_event.schema.json
genealogy_relationship.schema.json
family_group.schema.json
land_ownership_assertion.schema.json
land_instrument.schema.json
parcel_version.schema.json
ownership_interval.schema.json
domain_observation.schema.json
domain_validation_report.schema.json
public_safe_summary.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. Do not silently create duplicate schemas across child subfolders, common schema paths, or cross-domain schema paths.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/people-dna-land/`.
- [ ] Confirm complete People / DNA / Land schema inventory.
- [ ] Resolve whether child schema paths should be retired, redirected, or accepted as transitional compatibility paths.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid synthetic fixture paths.
- [ ] Confirm invalid synthetic fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, consent, source-registry, release, correction, and rollback references for accepted schemas.
- [ ] Confirm whether `schemas/README.md` should index this domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | People/DNA/Land schema-home decision, child path decision, new schema addition, validator update, fixture update, schema registry update, policy/consent update, release reference update, or migration note |

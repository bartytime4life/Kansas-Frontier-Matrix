# `schemas/contracts/v1/domains/people/` — People Schema Bridge Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-people-readme
title: schemas/contracts/v1/domains/people/ — People Schema Bridge Index
version: v1
status: draft; PROPOSED; CONFLICTED; short-segment-bridge
policy_label: restricted-review
owners:
  - <schema-steward>
  - <people-domain-steward>
  - <people-dna-land-domain-steward>
  - <identity-resolution-steward>
  - <privacy-steward>
  - <consent-steward>
  - <policy-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, people, people-dna-land, identity, consent, restricted-review, bridge]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-people-purple)
![posture](https://img.shields.io/badge/posture-CONFLICTED%20%2F%20BRIDGE-orange)
![sensitivity](https://img.shields.io/badge/sensitivity-restricted--review-critical)

## Purpose

`schemas/contracts/v1/domains/people/` is a draft short-segment schema bridge for People-shaped schema work.

This path is **not confirmed canonical**. It exists to make the short `people` segment visible without silently replacing the broader `people-dna-land` domain schema lane.

This path may index future People schema candidates only after steward review decides whether accepted People schemas belong here, under `schemas/contracts/v1/domains/people-dna-land/`, under a shared/common schema family, or in another accepted schema home.

This README is documentation only. It is not a schema file, contract prose, policy, consent record, source registry record, lifecycle data, fixture, proof, release record, public API behavior, public map behavior, person store, identity truth, or publication authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | People schema bridge README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/people/` |
| Status | Draft / PROPOSED / CONFLICTED / short-segment bridge |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical posture | NEEDS VERIFICATION. ADR-0001 allows domain schemas under `schemas/contracts/v1/domains/<domain>/...`, but current evidence does not resolve whether the accepted domain segment should be short `people` or broader `people-dna-land`. |
| Broader domain schema lane | `schemas/contracts/v1/domains/people-dna-land/` exists as the broader People / DNA / Land schema index. |
| Known child lane | `dna/` exists as a CONFLICTED / TRANSITIONAL DNA schema bridge index. |
| Concrete schema inventory | NEEDS VERIFICATION. Current-session search did not confirm concrete `.schema.json` files under `schemas/contracts/v1/domains/people/`. |
| Default posture | Restricted review; assertion-first; evidence-bound; consent-aware; release-gated. |
| Required reviewers | Schema steward, People steward, People/DNA/Land steward, identity-resolution steward, privacy steward, consent steward, policy steward, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while policy, release, source identity, rights, sensitivity, lifecycle data, registries, proofs, receipts, and other authority families remain separate responsibility roots.

Current-session evidence confirms `contracts/domains/people/README.md` is a short-segment semantic-contract bridge. It explicitly says the short `people` segment is not proof that the segment is canonical and warns against creating duplicate schema, policy, lifecycle, or release lanes from that bridge alone.

Current-session evidence confirms `schemas/contracts/v1/domains/people-dna-land/README.md` exists as the broader People / DNA / Land schema index, with restricted-review posture and no confirmed concrete schema files.

Current-session People/DNA/Land sublane doctrine says sublanes are documentation navigation only and should not be mirrored into `schemas/`, `contracts/`, `policy`, `tests`, `fixtures`, `pipelines`, `data`, or `release` without further governance.

Current-session evidence confirms `schemas/contracts/v1/domains/people/dna/README.md` exists as a CONFLICTED / TRANSITIONAL child bridge and should not receive schema files until the segment question is resolved.

Current-session search did not confirm concrete People `.schema.json` files under this requested parent path.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            ├── people/
            │   ├── README.md                  # you are here; CONFLICTED / bridge
            │   └── dna/
            │       └── README.md              # CONFLICTED / transitional
            └── people-dna-land/
                └── README.md                  # broader domain schema index

contracts/
└── domains/
    ├── people/                                 # short-segment semantic bridge; not schema shape
    └── people-dna-land/                        # broader semantic-contract lane

docs/
└── domains/
    └── people-dna-land/                        # doctrine and documentation navigation

policy/                                         # access, consent, sensitivity, release posture; not schema shape
data/                                           # lifecycle, registry, proof, receipt roots; not schema home
release/                                        # release decisions and records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/people/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms responsibility-root placement and separate homes for machine shape, policy, source identity, rights, sensitivity, and release decisions. |
| `contracts/domains/people/README.md` | Short-segment semantic bridge; not proof of canonical schema segment. |
| `schemas/contracts/v1/domains/people-dna-land/README.md` | Broader People / DNA / Land schema index; restricted-review and no confirmed concrete schema files. |
| `schemas/contracts/v1/domains/people/dna/README.md` | DNA child bridge; CONFLICTED / transitional. |
| `docs/domains/people-dna-land/sublanes/people_genealogy.md` | Proposed sublane decision; rejects mirroring sublane segments into schema roots. |
| Search for People schema files | Did not confirm concrete `.schema.json` files under this path. |

This README does not verify complete schema coverage, schema registry entries, validator wiring, CI behavior, consent enforcement, policy enforcement, release integration, runtime behavior, public API behavior, or UI behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| No concrete `.schema.json` file confirmed in this edit | N/A | NEEDS VERIFICATION | Current-session search did not confirm concrete People schemas under this path. |

## Current child lanes

| Child path | Status | Recommended action |
|---|---|---|
| `dna/` | CONFLICTED / transitional | Do not add schema files here until the People vs People/DNA/Land schema-home question is resolved. |

## Candidate schema families

Candidate shapes should be placed only after resolving whether they belong in this short `people` parent, in `people-dna-land`, in a shared/common family, or in a steward-approved transitional path.

| Candidate schema family | Status |
|---|---|
| `person_assertion.schema.json` | NEEDS VERIFICATION |
| `person_identity_candidate.schema.json` | NEEDS VERIFICATION |
| `person_canonical.schema.json` | NEEDS VERIFICATION |
| `name_assertion.schema.json` | NEEDS VERIFICATION |
| `life_event.schema.json` | NEEDS VERIFICATION |
| `residence_event.schema.json` | NEEDS VERIFICATION |
| `migration_event.schema.json` | NEEDS VERIFICATION |
| `identity_resolution_record.schema.json` | NEEDS VERIFICATION |
| `public_safe_person_summary.schema.json` | NEEDS VERIFICATION |
| `dna/dna_match_evidence.schema.json` | NEEDS VERIFICATION |
| `dna/dna_segment.schema.json` | NEEDS VERIFICATION |
| `dna/dna_kit_token.schema.json` | NEEDS VERIFICATION |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Bridge index | Make the short `people` schema segment visible without canonicalizing it. |
| Contract pairing | Link each future schema to paired semantic contracts only after path review. |
| Segment drift control | Keep this path and `dna/` marked CONFLICTED / TRANSITIONAL until an ADR, migration note, or steward decision resolves the accepted home. |
| Restricted-review discipline | Treat identity, consent, DNA-derived, land-link, and relationship surfaces as restricted-review by default. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, lifecycle data, source registry records, consent records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across this short segment, `people-dna-land`, common schema paths, and cross-domain schema paths. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here while conflicted

- This README.
- Placement notes about why this path is CONFLICTED / bridge.
- Links to broader People/DNA/Land schema and doctrine, short-segment contract bridge notes, policy lanes, consent lanes, source-registry lanes, release references, correction references, and rollback references.
- Drift notes that help migrate future schema work to the accepted home.

## What does not belong here

- Sensitive or real-world personal payloads.
- Consent records.
- Source registry records.
- Lifecycle data payloads.
- Proof outputs.
- Policy decisions.
- Release records or release decisions.
- Public API, UI, map, Focus Mode, or generated-answer artifacts.
- Person stores, identity-truth stores, relationship truth stores, or public genealogy outputs.
- Contract prose beyond this path-boundary README.
- Schema files until placement is resolved by the appropriate steward or ADR.
- Claims that a People schema is complete without fixtures, validators, registry records, policy checks, consent checks, and steward review.

## Schema status values

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `PATH_CONFLICT` | Schema placement is blocked by unresolved short-segment vs broader-domain schema-home conflict. |
| `PROFILE` | Schema profiles a shared source, identity, consent, spatial, time, or common schema without creating duplicate authority. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, policy, consent, or CI support has not been verified. |

## Review checklist

- [ ] Resolve whether the short `people/` schema path should exist or be retired.
- [ ] Confirm whether accepted People schemas belong under `schemas/contracts/v1/domains/people-dna-land/` instead.
- [ ] Confirm whether the existing `dna/` child bridge should remain, move, or redirect.
- [ ] Confirm paired contract paths.
- [ ] Confirm schema registry records.
- [ ] Confirm valid synthetic fixture paths.
- [ ] Confirm invalid synthetic fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI/schema-test coverage.
- [ ] Confirm consent, policy, source-registry, release, correction, and rollback references.
- [ ] Confirm no restricted payload material is stored here.
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
migration_event.schema.json
identity_resolution_record.schema.json
public_safe_person_summary.schema.json
dna/dna_match_evidence.schema.json
dna/dna_segment.schema.json
dna/dna_kit_token.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. Do not silently create duplicate schemas across `people/`, `people-dna-land/`, common schema paths, or cross-domain schema paths.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/people/`.
- [ ] Confirm complete People schema inventory.
- [ ] Resolve whether this short `people` schema bridge is accepted, retired, or redirected.
- [ ] Confirm paired contract paths for all accepted People schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid synthetic fixture paths.
- [ ] Confirm invalid synthetic fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, consent, source-registry, release, correction, and rollback references for accepted schemas.
- [ ] Confirm whether `schemas/README.md` should index this short-segment bridge or only the broader People/DNA/Land lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank placeholder; CONFLICTED / short-segment bridge warning |
| Next review trigger | People schema-home decision, People/DNA/Land segment decision, child `dna/` decision, accepted People schema addition, validator update, fixture update, schema registry update, consent/policy update, release reference update, or migration note |

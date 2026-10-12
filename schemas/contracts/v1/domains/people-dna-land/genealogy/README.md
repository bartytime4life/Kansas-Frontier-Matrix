# `schemas/contracts/v1/domains/people-dna-land/genealogy/` — Genealogy Schema Sublane Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-people-dna-land-genealogy-readme
title: schemas/contracts/v1/domains/people-dna-land/genealogy/ — Genealogy Schema Sublane Index
version: v1
status: draft; PROPOSED; CONFLICTED; transitional-index
policy_label: restricted-review
owners:
  - <schema-steward>
  - <people-dna-land-domain-steward>
  - <genealogy-assertion-steward>
  - <privacy-steward>
  - <consent-steward>
  - <policy-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, people-dna-land, genealogy, restricted-review, assertion-first]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-people--dna--land-purple)
![lane](https://img.shields.io/badge/lane-genealogy-blueviolet)
![posture](https://img.shields.io/badge/posture-CONFLICTED%20%2F%20TRANSITIONAL-orange)
![sensitivity](https://img.shields.io/badge/sensitivity-restricted--review-critical)

## Purpose

`schemas/contracts/v1/domains/people-dna-land/genealogy/` is a draft, transitional README for a requested genealogy schema sublane.

This path is **not confirmed canonical**. Current-session evidence shows this README existed as a blank placeholder, but People/DNA/Land sublane doctrine says sublane folders are a `docs/` navigation device and should not be mirrored into `schemas/` without further governance.

Until schema and domain stewards resolve the placement conflict, this directory should remain an index-only warning surface. Do not add genealogy schema files here merely because this README exists.

This README is documentation only. It is not a schema file, contract prose, policy, consent record, source registry record, lifecycle data, fixture, proof, release record, public API behavior, public map behavior, or genealogy truth.

## Status & authority

| Field | Value |
|---|---|
| Document type | Genealogy schema sublane README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/people-dna-land/genealogy/` |
| Status | Draft / transitional / CONFLICTED |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical posture | NEEDS VERIFICATION. ADR-0001 allows domain schemas under `schemas/contracts/v1/domains/<domain>/...`, but People/DNA/Land sublane doctrine rejects mirroring sublane segments into `schemas/`. |
| Parent schema lane | `schemas/contracts/v1/domains/people-dna-land/` exists, but its README is still a greenfield scaffold. |
| Concrete schema inventory | NEEDS VERIFICATION. Current-session search did not confirm concrete genealogy `.schema.json` files under this path. |
| Paired contract lane | `contracts/domains/people-dna-land/genealogy/` exists as a genealogy semantic contract folder with PROPOSED / NEEDS VERIFICATION posture. |
| Fixture lane | `fixtures/domains/people-dna-land/genealogy/` exists for synthetic examples only, not schema authority. |
| Default posture | Restricted review and deny-by-default for unsafe or insufficiently supported outputs. |
| Required reviewers | Schema steward, People/DNA/Land steward, genealogy assertion steward, privacy steward, consent steward, policy steward, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while policy, release, source identity, rights, sensitivity, lifecycle data, registries, proofs, receipts, and other authority families remain separate responsibility roots.

Current-session evidence confirms the parent People/DNA/Land schema README is a greenfield scaffold and should not be treated as proof of complete schema coverage.

Current-session People/DNA/Land sublane doctrine says sublanes are documentation navigation only and should not be mirrored into schema roots without further governance.

Current-session genealogy contract evidence confirms genealogy is assertion-first, evidence-bound, consent-aware, privacy-aware, and restricted-review by default. It does not create schema, policy, source registry, lifecycle-data, release, consent, or publication authority.

Current-session fixture evidence confirms `fixtures/domains/people-dna-land/genealogy/` is for synthetic examples only and does not define schema, data, proof, consent, policy, or release authority.

Current-session search did not confirm concrete genealogy schema files under this requested path.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── people-dna-land/
                ├── README.md                  # parent schema lane; scaffold
                └── genealogy/
                    └── README.md              # you are here; CONFLICTED / transitional

contracts/
└── domains/
    └── people-dna-land/
        └── genealogy/                          # semantic meaning; not schema shape

docs/
└── domains/
    └── people-dna-land/
        └── sublanes/                           # documentation navigation only

fixtures/
└── domains/
    └── people-dna-land/
        └── genealogy/                          # synthetic examples only; not schema shape

policy/
data/
release/
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/people-dna-land/genealogy/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms responsibility-root placement and separate homes for machine shape, policy, source identity, rights, sensitivity, and release decisions. |
| `schemas/contracts/v1/domains/people-dna-land/README.md` | Existing parent schema scaffold. |
| `docs/domains/people-dna-land/sublanes/people_genealogy.md` | Proposed sublane decision; rejects mirroring sublane segments into schema roots. |
| `contracts/domains/people-dna-land/genealogy/README.md` | Genealogy semantic contract folder; restricted-review, evidence-bound, consent-aware, assertion-first. |
| `fixtures/domains/people-dna-land/genealogy/README.md` | Synthetic fixture lane only; not schema, data, proof, consent, policy, or release authority. |
| Search for genealogy schema files | Did not confirm concrete `.schema.json` files under this path. |

This README does not verify complete schema coverage, schema registry entries, validator wiring, CI behavior, policy enforcement, consent enforcement, release integration, runtime behavior, public API behavior, or UI behavior.

## Candidate schema families

Candidate shapes should be placed only after resolving whether they belong directly under `schemas/contracts/v1/domains/people-dna-land/`, under a shared schema family, or in a governed transitional path.

| Candidate schema family | Status |
|---|---|
| `person_assertion.schema.json` | NEEDS VERIFICATION |
| `name_assertion.schema.json` | NEEDS VERIFICATION |
| `life_event.schema.json` | NEEDS VERIFICATION |
| `residence_event.schema.json` | NEEDS VERIFICATION |
| `genealogy_relationship.schema.json` | NEEDS VERIFICATION |
| `family_group.schema.json` | NEEDS VERIFICATION |
| `relationship_hypothesis.schema.json` | NEEDS VERIFICATION |
| `genealogy_source_citation.schema.json` | NEEDS VERIFICATION |
| `public_safe_genealogy_summary.schema.json` | NEEDS VERIFICATION |

## What belongs here while conflicted

- This README.
- Placement notes about why this path is CONFLICTED / transitional.
- Links to paired contracts, parent schema lane, fixture lanes, policy lanes, source-registry lanes, release references, correction references, and rollback references.
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
- Contract prose beyond this path-boundary README.
- Schema files until placement is resolved by the appropriate steward or ADR.
- Claims that a genealogy schema is complete without fixtures, validators, registry records, policy checks, consent checks, and steward review.

## Review checklist

- [ ] Resolve whether this `genealogy/` schema sublane should exist or be retired.
- [ ] Confirm whether accepted genealogy schemas belong directly under `schemas/contracts/v1/domains/people-dna-land/`.
- [ ] Confirm paired contract paths.
- [ ] Confirm schema registry records.
- [ ] Confirm valid synthetic fixture paths.
- [ ] Confirm invalid synthetic fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI/schema-test coverage.
- [ ] Confirm consent, policy, source-registry, release, correction, and rollback references.
- [ ] Confirm no restricted payload material is stored here.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank placeholder; CONFLICTED / transitional path warning |
| Next review trigger | People/DNA/Land schema-home decision, genealogy sublane decision, parent schema README update, accepted genealogy schema addition, validator update, fixture update, schema registry update, consent/policy update, release reference update, or migration note |

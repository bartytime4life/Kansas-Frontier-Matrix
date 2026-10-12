# `schemas/contracts/v1/domains/people/dna/` — DNA Schema Bridge Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-people-dna-readme
title: schemas/contracts/v1/domains/people/dna/ — DNA Schema Bridge Index
version: v1
status: draft; PROPOSED; CONFLICTED; transitional-index
policy_label: restricted-review
owners:
  - <schema-steward>
  - <people-domain-steward>
  - <people-dna-land-domain-steward>
  - <dna-evidence-steward>
  - <privacy-steward>
  - <consent-steward>
  - <policy-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, people, dna, people-dna-land, consent, restricted-review, transitional]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![path](https://img.shields.io/badge/path-people%2Fdna-purple)
![posture](https://img.shields.io/badge/posture-CONFLICTED%20%2F%20TRANSITIONAL-orange)
![sensitivity](https://img.shields.io/badge/sensitivity-restricted--review-critical)

## Purpose

`schemas/contracts/v1/domains/people/dna/` is a draft, transitional README for a requested short-segment DNA schema path.

This path is **not confirmed canonical**. Current-session evidence shows this README existed as a blank placeholder, while the parent `schemas/contracts/v1/domains/people/README.md` was not present in this check. Current evidence also shows DNA doctrine is organized under the broader `people-dna-land` domain, and People/DNA/Land sublane doctrine rejects mirroring sublane segments into schema roots without further governance.

Until schema, People, and People/DNA/Land stewards resolve the segment question, this directory should remain an index-only warning surface. Do not add DNA schema files here merely because this README exists.

This README is documentation only. It is not a schema file, contract prose, policy, consent record, source registry record, lifecycle data, fixture, proof, release record, public API behavior, public map behavior, DNA evidence authority, relationship authority, person identity authority, or publication authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | DNA schema bridge README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/people/dna/` |
| Status | Draft / transitional / CONFLICTED |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Parent path posture | `schemas/contracts/v1/domains/people/README.md` was not present in this check, so the requested child path lacks a confirmed parent schema index. |
| Canonical posture | NEEDS VERIFICATION. ADR-0001 allows domain schemas under `schemas/contracts/v1/domains/<domain>/...`, but the accepted/reviewed domain segment for DNA-related people work remains unresolved in current evidence. |
| Broader active doctrine | DNA guidance is currently evidenced under `docs/domains/people-dna-land/sublanes/dna.md`. |
| Cross-root sublane warning | People/DNA/Land sublane doctrine says sublane folders are `docs/` navigation only and must not be mirrored into schema roots without governance. |
| Concrete schema inventory | NEEDS VERIFICATION. Current-session search did not confirm concrete DNA `.schema.json` files under this path. |
| Default posture | Restricted review; consent-gated; deny-by-default for unsafe or insufficiently supported outputs. |
| Required reviewers | Schema steward, People steward, People/DNA/Land steward, DNA evidence steward, privacy steward, consent steward, policy steward, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while policy, release, source identity, rights, sensitivity, lifecycle data, registries, proofs, receipts, and other authority families remain separate responsibility roots.

Current-session search found a `contracts/domains/people/README.md` bridge. That contract bridge says the short `people` segment is not proof that the people segment is canonical and warns against creating duplicate schema, policy, lifecycle, or release lanes from that bridge alone.

Current-session People/DNA/Land DNA doctrine confirms DNA work is restricted by default, consent-gated, and part of the People / DNA / Land bounded context.

Current-session People/DNA/Land sublane doctrine says sublanes are documentation navigation only and should not be mirrored into `schemas/`, `contracts/`, `policy`, `tests`, `fixtures`, `pipelines`, `data`, or `release` without further governance.

Current-session search did not confirm concrete DNA schema files under this requested path.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            ├── people/
            │   └── dna/
            │       └── README.md              # you are here; CONFLICTED / transitional
            └── people-dna-land/
                └── README.md                  # broader domain schema lane; PROPOSED

contracts/
├── domains/
│   ├── people/                                 # short-segment bridge; not schema shape
│   └── people-dna-land/                        # broader semantic-contract lane

docs/
└── domains/
    └── people-dna-land/
        └── sublanes/
            └── dna.md                          # DNA doctrine; docs navigation only

policy/                                         # access, consent, sensitivity, release posture; not schema shape
data/                                           # lifecycle, registry, proof, receipt roots; not schema home
release/                                        # release decisions and records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/people/dna/README.md` | Blank before this update. |
| `schemas/contracts/v1/domains/people/README.md` | Not present in this check; parent schema index remains NEEDS VERIFICATION. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms responsibility-root placement and separate homes for machine shape, policy, source identity, rights, sensitivity, and release decisions. |
| `contracts/domains/people/README.md` | Short-segment semantic contract bridge; not proof of canonical schema segment. |
| `docs/domains/people-dna-land/sublanes/dna.md` | DNA sublane doctrine; restricted by default and consent-gated. |
| `docs/domains/people-dna-land/sublanes/people_genealogy.md` | Proposed sublane decision; rejects mirroring sublane segments into schema roots. |
| Search for DNA schema files | Did not confirm concrete `.schema.json` files under this requested path. |

This README does not verify complete schema coverage, schema registry entries, validator wiring, CI behavior, consent enforcement, policy enforcement, release integration, runtime behavior, public API behavior, or UI behavior.

## Candidate schema families

Candidate shapes should be placed only after resolving whether they belong under `schemas/contracts/v1/domains/people/`, `schemas/contracts/v1/domains/people-dna-land/`, a shared consent/evidence family, or another accepted schema home.

| Candidate schema family | Status |
|---|---|
| `dna_match_evidence.schema.json` | NEEDS VERIFICATION |
| `dna_segment.schema.json` | NEEDS VERIFICATION |
| `dna_kit_token.schema.json` | NEEDS VERIFICATION |
| `dna_relationship_hint.schema.json` | NEEDS VERIFICATION |
| `relationship_hypothesis_dna_evidence.schema.json` | NEEDS VERIFICATION |
| `consent_grant_ref.schema.json` | NEEDS VERIFICATION |
| `revocation_receipt_ref.schema.json` | NEEDS VERIFICATION |
| `redacted_dna_aggregate.schema.json` | NEEDS VERIFICATION |
| `public_safe_dna_summary.schema.json` | NEEDS VERIFICATION |

## What belongs here while conflicted

- This README.
- Placement notes about why this path is CONFLICTED / transitional.
- Links to broader People/DNA/Land doctrine, short-segment bridge notes, policy lanes, consent lanes, source-registry lanes, release references, correction references, and rollback references.
- Drift notes that help migrate future schema work to the accepted home.

## What does not belong here

- DNA payloads, source exports, or vendor identifiers.
- Consent records or revocation records.
- Source registry records.
- Lifecycle data payloads.
- Proof outputs.
- Policy decisions.
- Release records or release decisions.
- Public API, UI, map, Focus Mode, or generated-answer artifacts.
- Person identity stores, relationship truth stores, or public genealogy outputs.
- Contract prose beyond this path-boundary README.
- Schema files until placement is resolved by the appropriate steward or ADR.
- Claims that a DNA schema is complete without fixtures, validators, registry records, policy checks, consent checks, and steward review.

## Review checklist

- [ ] Resolve whether the short `people/dna/` schema path should exist or be retired.
- [ ] Confirm whether accepted DNA schemas belong under `schemas/contracts/v1/domains/people-dna-land/` instead.
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
| Next review trigger | People schema-home decision, DNA schema-home decision, People/DNA/Land segment decision, parent schema README update, accepted DNA schema addition, validator update, fixture update, schema registry update, consent/policy update, release reference update, or migration note |

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/catalog-closure-packet
title: CatalogClosurePacket Contract
type: semantic-contract; data; catalog-closure; readiness; non-authoritative
version: v0.1.0
status: draft; PROPOSED; fixture-first
owners: OWNER_TBD — Catalog steward · Evidence steward · Validation steward · Policy steward · Release steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; data; catalog-closure; non-authoritative
related:
  - ./catalog_matrix.md
  - ../../schemas/contracts/v1/data/catalog_closure_packet.schema.json
  - ../../fixtures/data/catalog_closure_packet/
  - ../../tools/validators/catalog_closure/validate_catalog_closure.py
  - ../../tests/validators/test_validate_catalog_closure.py
  - ../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
notes:
  - "Implements a bounded closure-readiness packet without deciding the unresolved CatalogMatrix persistence/placement question."
  - "A PASS is readiness evidence for the next review gate, never proof closure, policy approval, promotion, release, or publication."
[/KFM_META_BLOCK_V2] -->

# `CatalogClosurePacket`

> A deterministic, immutable input packet for checking whether STAC, DCAT, and PROV catalog carriers agree on one artifact identity, digest, and release-candidate reference and whether their declared evidence, validation, policy, review, correction, and rollback dependencies are ready for the next governed gate.

## Purpose

The repository already separates catalog records, evidence/proofs, receipts, policy, review, release, and published artifacts. This contract supplies the missing **readiness-check packet** joining those references for one bounded validation run.

It does not create a `CatalogMatrix`, catalog record, `EvidenceBundle`, proof, receipt, policy decision, review approval, `ReleaseManifest`, rollback card, or published artifact. It does not settle the proposed ADR disagreement over where a persisted `CatalogMatrix` instance belongs.

## Directory Rules basis

The object meaning belongs under `contracts/data/`; machine shape belongs under `schemas/contracts/v1/data/`; synthetic examples belong under `fixtures/data/`; executable checks belong under `tools/validators/catalog_closure/`; enforceability belongs under `tests/validators/`; hosted orchestration belongs under `.github/workflows/`.

No new repository root or parallel catalog, proof, receipt, policy, release, or publication authority is introduced.

## Required relationships

A packet identifies one target artifact and carries three catalog-carrier records:

- one `STAC` record;
- one `DCAT` record; and
- one `PROV` record.

Each carrier must bind the same:

- `artifact_id`;
- `artifact_digest`; and
- `release_candidate_ref`, when a release review is requested.

The packet also carries canonical reference inventories for source descriptors, evidence, validation reports, policy/review state, run provenance, corrections, and rollback.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The packet is internally consistent and ready to be handed to the named next review gate. |
| `HOLD` | The packet is valid, but rights, sensitivity, or human review remains unresolved. |
| `DENY` | A recorded policy or review decision forbids the requested handoff. |
| `FAIL` | The packet violates schema or semantic closure invariants. |
| `ERROR` | The validator could not safely read or evaluate the input. |

`PASS` never means that evidence is true, policy is approved, review is complete beyond the declared packet, or release/publication is authorized.

## Deterministic hash profile

`kfm-fixture-json-v1` removes top-level `spec_hash`, serializes UTF-8 JSON with sorted keys and no insignificant whitespace, preserves array order, and computes SHA-256. This profile is local to the synthetic fixture/replay contract and is not a repository-wide hash-policy decision.

## Required invariants

- Catalog carriers are canonical and exactly cover `DCAT`, `PROV`, and `STAC`.
- Carrier artifact identity, digest, and release candidate agree with packet scope.
- All carrier records are declared resolved.
- Reference arrays are sorted, unique, and non-empty where required.
- `ALLOW` requires resolved rights and sensitivity plus a policy-decision reference.
- `APPROVED` review requires a review-record reference.
- `RELEASE_REVIEW` requires a release-candidate reference and rollback reference.
- Promotion, release, publication, and public-use authority flags remain false.
- A release-review packet may describe a candidate transition; it cannot authorize that transition.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_catalog_closure.py' \
  --verbose

python tools/validators/catalog_closure/validate_catalog_closure.py --fixtures
```

## Rollback

The slice is additive except for no existing authority surface. Rollback removes this contract, schema, synthetic fixtures, validator, tests, and workflow. No catalog record, proof, receipt, policy decision, release object, or published artifact requires restoration.

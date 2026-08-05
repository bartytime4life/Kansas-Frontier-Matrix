<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/evidence-custody-handoff
title: Evidence Custody Handoff and Reconciliation Candidate Contract
type: semantic-contract; fixture-first; no-network
version: v0.1.0
status: proposed; fixture-only; no-live-transfer
owners: OWNER_TBD — Evidence steward · Source steward · Contracts steward · Validation steward · Rights/sensitivity steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; evidence; custody; reconciliation; no-publish
related:
  - ./README.md
  - ../../schemas/contracts/v1/evidence/evidence_custody_handoff.schema.json
  - ../../fixtures/contracts/v1/evidence/evidence_custody_handoff/
  - ../../tools/validators/validate_evidence_custody_handoff.py
  - ../../tests/validators/test_validate_evidence_custody_handoff.py
  - ../../docs/intake/exploratory/new-ideas-4-23-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, evidence, custody, reconciliation, digest, partition, no-network]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Evidence Custody Handoff and Reconciliation Candidate Contract

> A fixture-first record that binds an exact sender manifest to one receiver disposition for every declared item. It proves synthetic accounting and byte-identity rules only; it is not an EvidenceBundle, PolicyDecision, promotion, release, publication, or live transfer.

## Source-derived gap

The governed source map for *New Ideas 4-23-26* identifies cross-boundary evidence custody as the first unresolved connective gap: existing receipts describe work inside lanes, but no common closed handoff binds sender bytes, receiver acceptance, duplicates, rejects, and unresolved items across responsibility or environment boundaries. This contract closes only that synthetic seam.

## Bounded context

| Candidate may describe | Candidate must not do |
|---|---|
| One digest-bound sender manifest | Carry source payload bytes or secrets |
| One receiver disposition per sender item | Omit, duplicate, or silently replace an item |
| Accepted, rejected, duplicate, and unresolved accounting | Treat a transfer as evidence closure or source truth |
| Same-stage custody or movement into quarantine | Advance lifecycle stage or write `PUBLISHED` |
| Exact sender/receiver digest and byte-count comparison | Treat integrity as rights, policy, review, or release approval |
| Open reconciliation when an item remains unresolved | Hide missing rights, sensitivity, identity, or digest support |

## Object surface

`EvidenceCustodyHandoff` contains:

1. **sender boundary** — authority class, lifecycle stage, send time, and a digest over the ordered item manifest;
2. **receiver boundary** — authority class, lifecycle stage, receive time, and a digest over the ordered disposition record;
3. **transfer metadata** — opaque receipt references and a deterministic transfer identity;
4. **items** — IDs, source/evidence references, media type, sender digest, byte count, classification, rights, and sensitivity posture;
5. **receiver dispositions** — exactly one `ACCEPTED`, `REJECTED`, `DUPLICATE`, or `UNRESOLVED` result for each item; and
6. **summary and governance** — exact counts, `OPEN`/`CLOSED` closure, and explicit non-effects.

## Reconciliation rules

- Items and dispositions are sorted by `item_id` and contain no duplicate IDs.
- Every sender item has exactly one receiver disposition; no unknown receiver item is permitted.
- `ACCEPTED` and `DUPLICATE` require byte count and digest equality with the sender.
- `DUPLICATE` also requires an existing governed item reference; it records idempotent reuse rather than a second copy.
- `REJECTED` carries no receiver artifact and requires at least one reason code.
- `UNRESOLVED` keeps the handoff `OPEN` and requires a reason code.
- Unknown rights or sensitivity must be `UNRESOLVED` and the receiver boundary must be `QUARANTINE`.
- The receiver may remain in the sender lifecycle stage or move into `QUARANTINE`; the handoff cannot advance trust or publication state.
- Summary counts must exactly match the disposition partition.

## Deterministic identity

```text
manifest_digest       = SHA-256(canonical ordered items)
reconciliation_digest = SHA-256(canonical ordered dispositions)
handoff_key           = SHA-256(sender boundary + receiver boundary + manifest_digest)
handoff_id            = kfm://candidate/evidence-custody/<handoff-key-hex>
transfer_id           = <handoff_id>/transfer/<revision>
spec_hash             = SHA-256(canonical record excluding spec_hash)
```

The profile uses recursively sorted, compact JSON for this bounded fixture identity. It does not claim to replace an accepted repository-wide canonicalization standard.

## Rights, sensitivity, and public boundary

Unknown rights or sensitivity never become accepted custody. Restricted material may be accounted for only inside non-public lifecycle stages and remains subject to later policy and steward review. The fixture carries no source bytes, coordinates, credentials, EvidenceBundle resolution, policy decision, lifecycle write, promotion, release, or publication authority.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. The artifact's authority owner is evidence semantics, so the dependency-closed slice uses existing responsibility roots:

- semantic meaning: `contracts/evidence/`;
- machine shape: `schemas/contracts/v1/evidence/`;
- synthetic examples: `fixtures/contracts/v1/evidence/`;
- executable validation: `tools/validators/`;
- enforceability: `tests/validators/`;
- hosted orchestration: `.github/workflows/`; and
- AI authoring provenance: `data/receipts/generated/`.

No new root, evidence store, receipt authority, policy home, release home, or publication path is created.

## Validation

```bash
python -m pytest -q -p no:cacheprovider \
  tests/validators/test_validate_evidence_custody_handoff.py

python tools/validators/validate_evidence_custody_handoff.py --fixtures
```

A green result proves only schema closure, deterministic synthetic identity, exact item/disposition accounting, byte-integrity comparison, fail-closed unknown posture, and lifecycle non-escalation.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an independently authorized merge, revert the contract/schema/fixtures/validator/tests/workflow/receipt slice. No source, payload, evidence store, lifecycle write, release, deployment, or published object requires cleanup.

[Back to top](#top)

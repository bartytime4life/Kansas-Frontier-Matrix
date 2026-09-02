<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/as-of-snapshot-disclosure-candidate
title: AsOfSnapshotDisclosureCandidate Semantic Contract
type: semantic-contract; fixture-profile; temporal-evidence
version: 1.0.0
status: proposed; inactive; fixture-only; NEEDS STEWARD REVIEW
owners: OWNER_TBD — Evidence steward · Temporal steward · Data steward · Review steward · Release steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public; evidence; temporal; as-of; reports; exports; non-authoritative
tags: [kfm, contract, evidence, temporal, as-of, snapshot, report, export, bitemporal, abstain]
related:
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../schemas/contracts/v1/evidence/as_of_snapshot_disclosure.schema.json
  - ./verification_state_history.md
notes:
  - "Implements a bounded candidate from Pass 18 card KFM-P18-INV-348."
  - "The profile discloses immutable references only; it does not create a snapshot, recompute a report, correct a source, release, or publish."
[/KFM_META_BLOCK_V2] -->

# AsOfSnapshotDisclosureCandidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This profile binds a report, export, table, map, or statistic candidate to the source and transaction/release state used to compute it. It creates no snapshot, evidence, truth, correction, policy, review, release, publication, or public-use authority.

## Purpose

Records may change after a report is produced. A claim period alone cannot explain why two outputs for the same period differ. `AsOfSnapshotDisclosureCandidate` therefore keeps two temporal axes distinct:

- `claim_valid_time` — the period the reported claim describes;
- `snapshot.as_of` — the transaction or release state available to the computation.

The object also binds each source version and digest, records which corrections were included, declares how later corrections are handled, and gives public candidates explicit valid-time and as-of labels.

## Object meaning

One candidate binds an immutable output digest, resolved claim scope, half-open valid-time interval, one declared snapshot mode, one or more source snapshots, correction posture, disclosure labels, evidence references, a conclusion, and an all-false authority block.

Snapshot modes are declarations:

| Mode | Required reference posture |
|---|---|
| `RELEASE_SNAPSHOT` | release-manifest reference only |
| `TRANSACTION_SNAPSHOT` | transaction-snapshot reference only |
| `BITEMPORAL_SNAPSHOT` | both release-manifest and transaction-snapshot references |

`profile_spec_hash` is the lowercase SHA-256 digest of this contract's exact bytes. The validator checks the binding without authenticating authorship or resolving any reference.

## Deterministic outcomes

| Outcome | Bounded meaning |
|---|---|
| `PASS` | Shape and hash bindings are valid; claim and source references resolve; time axes are coherent; source snapshots are canonical and not later than the declared as-of point; correction and public-disclosure requirements are complete; declaration is `READY_FOR_REVIEW`. |
| `ABSTAIN` | Claim scope, snapshot, source version, correction posture, or conclusion remains unresolved. |
| `DENY` | Axes are collapsed, time order is impossible, mode/reference binding conflicts, arrays are noncanonical, a source is later than the as-of point, public review/release disclosure is missing, or the declared conclusion conflicts with findings. |
| `ERROR` | JSON, schema, timestamp, source-card, profile-hash, or authority constraints fail. |

`PASS` means only that a deterministic disclosure candidate is eligible for separate human review.

## Fail-closed rules

- All timestamps must be explicit UTC values ending in `Z`.
- Valid-time `start` must precede `end`; its `[)` boundary is fixed by schema.
- Snapshot mode and release/transaction references must agree exactly.
- Claim scope, snapshot, and every source snapshot must resolve; otherwise the result is `ABSTAIN`.
- Source snapshots must be sorted and unique by `source_id`; each `source_as_of` must be no later than `snapshot.as_of`.
- `corrections.included_through` must be no later than the snapshot; `UNKNOWN` later-correction behavior produces `ABSTAIN`.
- Valid-time and as-of labels must remain visibly distinct.
- A public candidate requires a review reference and output release-manifest reference. When the snapshot itself names a release manifest, the disclosure must name the same reference.
- Evidence, correction, and review arrays must be sorted and unique.
- Every authority claim is literally `false` in the schema.

## Non-authority boundary

The validator does not query a database, execute a transaction, freeze source state, create or compare report bytes, resolve references, decide claim truth, apply a correction, write history, create review or policy decisions, issue a release, deploy, publish, or authorize public use.

## Rollback

Rollback is additive: remove the inactive packet and its path-scoped workflow. No data, report, snapshot, or runtime migration is required because this proposal wires no consumer.

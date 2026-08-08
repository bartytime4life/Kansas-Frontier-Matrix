<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/drift-summary
title: DriftSummary semantic contract
type: semantic-contract; source-drift; watcher-output; fixture-first
version: v0.1.0
status: proposed; inactive; fixture-first; no-network; non-publisher
owners: OWNER_TBD — Source steward · Contracts steward · Schema steward · Validation steward · Policy steward
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; source; drift; evidence-first; fail-closed; non-authoritative
related:
  - ./source_intake_record.md
  - ../../schemas/contracts/v1/source/drift_summary.schema.json
  - ../../fixtures/contracts/v1/source/source_intake_record/
  - ../../tools/validators/validate_source_intake_record.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, source, drift, watcher, contract, materiality, sensitivity, no-network]
notes:
  - "Source idea: KFM-P4-PROG-0001."
  - "This contract does not activate a source, decide truth, admit RAW, promote, release, or publish."
[/KFM_META_BLOCK_V2] -->

# DriftSummary semantic contract

`DriftSummary` is the bounded, source-role-preserving description of a comparison performed by a watcher or source-health process. It records **what changed**, **how material the change appears under the declared comparison profile**, and **whether the change may imply sensitivity or public-detail restrictions**.

It does not prove that an upstream claim is true, that a source is admissible, that a public layer should change, or that a release is authorized.

## Required meaning

A conforming summary carries:

- a stable `drift_id` and `source_descriptor_ref`;
- canonical observation time and an optional prior/current comparison window;
- one `drift_kind` and one `materiality` outcome;
- deterministic `change_codes` and `changed_fields`;
- a bounded public-safe `summary`;
- a `sensitive_implication` and explicit `public_detail_allowed` posture; and
- optional metrics and identity references that remain subordinate to the future object-family hash policy.

## Finite vocabulary

`drift_kind` is one of `NONE`, `METADATA`, `CONTENT`, `SCHEMA`, `TAXONOMY`, `GEOMETRY`, `RIGHTS`, `SENSITIVITY`, or `MULTIPLE`.

`materiality` is one of:

- `NONE` — no detected change;
- `BELOW_THRESHOLD` — a change exists but does not meet the declared review threshold;
- `REVIEW_REQUIRED` — a bounded work candidate may be proposed; or
- `BLOCKING` — the candidate must remain quarantined or otherwise fail closed.

`DriftSummary` never chooses a lifecycle transition. `SourceIntakeRecord` binds the summary to a candidate disposition.

## Invariants

1. `NONE` requires `materiality=NONE`, `change_codes=["NO_CHANGE"]`, and no changed fields.
2. Any non-`NONE` drift requires at least one changed field or declared metric.
3. `BLOCKING` or any sensitivity implication other than `NONE` requires `public_detail_allowed=false`.
4. Comparison time cannot run backward.
5. Change codes and field pointers are unique and canonically sorted.
6. Hash or identity references identify declared comparison inputs only; they do not establish evidence closure or publication truth.

## Authority split

- Semantic meaning: `contracts/source/drift_summary.md`.
- Machine shape: `schemas/contracts/v1/source/drift_summary.schema.json`.
- Candidate envelope: `contracts/source/source_intake_record.md`.
- Validation and fixture proof: `tools/validators/` and `fixtures/`.
- Rights, sensitivity, and publication decisions: `policy/`, review records, and release controls.

## Rollback

Before merge, close the draft pull request and delete only its feature branch. After merge, revert the implementation commit through a reviewed pull request. No source, lifecycle data, release, or public artifact migration is required because this slice is fixture-first and inactive.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy/thresholds-readme
title: policy/thresholds — Inactive Threshold Policy Candidates
type: readme
version: v0.1.0
status: draft; PROPOSED_INACTIVE; no-adopted-values
owners: OWNER_TBD — Policy steward · Domain stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: public; policy; thresholds; inactive; review-required
owning_root: policy/
responsibility: Bound the singular inactive threshold-policy candidate lane and forbid value adoption, consumer binding, or authority overclaim.
related:
  - ../README.md
  - ../../contracts/policy/threshold_policy_registry.md
  - ../../schemas/contracts/v1/policy/threshold_policy_registry.schema.json
  - ./registry.v1.json
truth_posture: CONFIRMED singular policy root and inactive-registry allowance / PROPOSED threshold candidate lane / UNKNOWN steward approval and any active value or consumer binding
[/KFM_META_BLOCK_V2] -->

# `policy/thresholds/`

This lane contains reviewable **inactive threshold-policy candidates**. Its first
registry records unresolved questions only; it adopts no values.

## Authority

`policy/` is the singular policy-source root under adopted Directory Rules.
This child lane may carry an inactive candidate registry, but it does not own
semantic definitions, JSON Schema, fixtures, validator code, emitted decisions,
source records, evidence, lifecycle state, release records, or public output.

## Allowed

- versioned inactive candidate registries;
- stable threshold identifiers and review posture;
- proposal-lineage and repository pressure references;
- explicit supersession notes after reviewed changes; and
- false-valued non-effect declarations.

## Forbidden

- live or illustrative values presented as adopted policy;
- endpoint, watcher, detector, renderer, or evaluator configuration;
- source activation, admission, promotion, release, or publication state;
- scientific or emergency conclusions inferred from registry membership;
- credentials, raw data, sensitive locations, or unreviewed decision records;
- a second threshold authority under another root.

## Review burden

Resolving a slot requires affected domain, policy, evidence, validation, and
consumer review plus explicit compatibility, correction, and rollback analysis.
Until then, entries remain `UNRESOLVED / UNBOUND / HOLD`.

## Rollback

Revert the additive candidate packet. No active rule, source, consumer, release,
or published artifact depends on this lane.

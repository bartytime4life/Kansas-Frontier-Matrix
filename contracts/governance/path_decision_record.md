<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/path-decision-record/v1
title: Path Decision Record Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-07
policy_label: public
related:
  - "../../docs/doctrine/directory-rules.md"
  - "../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "../../control_plane/root_registry.yaml"
  - "../../schemas/contracts/v1/governance/path_decision_record.schema.json"
  - "../../tools/validators/directory_governance/validate_path_decision_record.py"
tags: [kfm, governance, directory-rules, placement, path-decision, finite-outcome]
notes:
  - "A validated record documents a placement evaluation. It does not authorize a path, accept an ADR, move bytes, create authority, or grant release/publication status."
[/KFM_META_BLOCK_V2] -->

# Path Decision Record Contract

## Purpose

A `PathDecisionRecord` is the reviewable machine record required for structural KFM changes. It binds one proposed artifact or object family to:

- the adopted Directory Rules identity and digest;
- the exact root-registry projection and pinned repository base;
- a responsibility signature;
- evidence and rule references;
- one finite placement outcome: `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, or `DENY`.

The record makes placement reasoning inspectable and testable. It is not itself an authority decision.

## Responsibility signature

Each record carries the Directory Rules signature axes:

- artifact kind;
- exactly one claimed authority owner;
- lifecycle stage;
- execution role;
- scope kind and registered scope ID;
- exposure;
- mutability;
- retention;
- physical storage.

The producer of an artifact does not determine its home. The validator evaluates the stated path against the root registry, hard exclusions, lifecycle boundaries, and the declared outcome.

## Binding fields

A record includes:

- `decision_id`, version, evaluation time, and pinned `base_ref`;
- root-registry path, SHA-256, and registry base reference;
- adopted Directory Rules path, SHA-256, and `ADR-0029`;
- artifact identity, optional current path, proposed path, and responsibility signature;
- evidence refs, Directory Rules IDs, reason codes, and candidate roots;
- optional `canonical_source`, `consumer_refs`, and `split_targets`;
- one finite outcome.

## Outcome semantics

### `PLACE`

Use only when the proposed path resolves to one active canonical or platform root and the declared artifact kind is allowed there. Compatibility, deprecated, retired, and inactive conditional roots cannot receive `PLACE`.

### `SPLIT`

Use when the proposed artifact combines multiple authority owners. The record must provide at least two distinct `split_targets`; each target is later evaluated independently.

### `MIGRATE`

Use when an existing artifact has a known canonical destination. `current_path` and `proposed_path` must differ, the proposed root must be active and canonical/platform, and the record must cite migration and rollback evidence.

### `MIRROR`

Use only for a verified one-way compatibility consumer. The record must bind `canonical_source`, at least one `consumer_ref`, and an exit condition reason code. The target root must be compatibility-class.

### `HOLD`

Use when ownership, authority, identity, sensitivity, source evidence, or target evidence remains unresolved. A hold is fail-closed and cannot be used as implicit permission.

### `DENY`

Use when the proposed placement violates a hard invariant, exposes protected lifecycle state, creates parallel authority, or uses a non-authoritative carrier as a canonical home.

## Hard checks in the first validator slice

The validator denies inconsistent records, including:

- a registry or doctrine digest mismatch;
- unsafe or non-canonical paths;
- `PLACE` in compatibility, deprecated, retired, or inactive conditional roots;
- artifact kinds that are prohibited or not allowed by the target root;
- public exposure from `data/raw/`, `data/work/`, or `data/quarantine/`;
- trust-bearing contracts, schemas, policy, data, or release decisions under `artifacts/`;
- `MIGRATE` without a distinct current path;
- `MIRROR` without canonical source, consumer, and exit evidence;
- `SPLIT` without at least two targets;
- missing evidence, rule IDs, reason codes, or root-registry binding.

## Validation boundary

A `PASS` means the record is internally consistent with the pinned projection. It does not prove the underlying architectural choice is accepted, that a migration is safe, that consumers are closed, or that any data/release/publication gate passed.

## Rollback

Rollback removes this additive contract/schema/validator/fixture/test/workflow packet and restores the prior directory-governance validator README. It does not require data migration or public-state reversal.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/action-point-reference-check
title: ActionPointReferenceCheck Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Validation steward · Automation steward · Evidence steward
created: 2026-08-25
updated: 2026-08-25
policy_label: internal; validation; action-point; deterministic; fail-closed
owning_root: contracts/
responsibility: fixture-only comparison of an acted-on literal with a freshly dereferenced authoritative literal
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../schemas/contracts/v1/validation/action_point_reference_check.schema.json
  - ../../fixtures/contracts/v1/validation/action_point_reference_check/cases.json
  - ../../tools/generators/action_point_reference_check/build_action_point_reference_check.py
  - ../../tools/validators/validate_action_point_reference_check.py
  - ../../tests/validators/test_validate_action_point_reference_check.py
  - ../../docs/intake/exploratory/cairnwake-action-point-reference-check-source-map.md
tags: [kfm, validation, dereference, action-point, literal, fail-closed, fixture]
[/KFM_META_BLOCK_V2] -->

# ActionPointReferenceCheck Candidate Contract

ActionPointReferenceCheck records whether the literal actually used at a consequential action point equals the literal freshly read from its authoritative source. It turns an advisory memory rule into a deterministic gate declaration.

## Closed outcomes

- MATCH: preserved action residue equals the source literal byte-for-byte.
- MISMATCH: both literals exist and differ.
- BLOCKED: the action used an abbreviated opaque literal or the dereference occurred after the action.
- UNCLASSIFIABLE: the action residue did not survive.

Only MATCH is eligible for a downstream ready decision. Every other outcome is fail-closed. Validator PASS means the declaration and its reproduced outcome agree; it does not mean the action is authorized.

## Required evidence

The record binds the literal as acted on, action time, residue status, authoritative source reference, immutable source digest, source literal, dereference time, and a pointer whose kind is either FULL_LITERAL or DETERMINISTIC_COMMAND. Line-number-only pointers are not admitted because edits can make them stale while retaining a plausible shape.

For OPAQUE_IDENTIFIER values, three consecutive ASCII periods or a Unicode ellipsis are treated as abbreviation markers. A fresh dereference must occur no later than the action. Equality is exact and requires no narrative classification.

## Deterministic identity

The builder derives the report, hashes the complete candidate except check_id and spec_hash with repository RFC 8785 JCS plus SHA-256, and forms check_id from the digest payload. Validators reproduce both the outcome and identity.

## Authority boundary

The profile is fixture-only, no-network, and non-mutating. It does not open a source, execute a command, inspect a live tool call, authorize an agent operation, authenticate evidence, or create a review, merge, release, deployment, publication, or public-use decision.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive commit. No source, lifecycle, data, release, or public state is changed by this inactive slice.

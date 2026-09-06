<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/validation/action-point-reference-check
title: ActionPointReferenceCheck Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Validation steward · Automation steward · Evidence steward
created: 2026-08-25
updated: 2026-09-06
policy_label: internal; validation; action-point; deterministic; fail-closed
owning_root: contracts/
responsibility: fixture-only comparison of an acted-on literal with a freshly dereferenced authoritative literal
truth_posture: CONFIRMED synthetic fixture behavior and current-main packet placement / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution, live-source evidence, and consumer adoption
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

## Repository reconciliation (2026-09-06)

This contract was re-read against GitHub `main@eaae135d8f4508c0712e3c6e151d7168a46f54ab` on 2026-09-06. GitHub is the implementation authority for this snapshot; Notion and Google Drive remain coordination and lineage inputs. The semantic rules above remain inactive and unchanged by this currentness refresh.

The base snapshot contains the following bounded packet:

| Surface | Current-main evidence | Confirmed boundary |
|---|---|---|
| Contract meaning | this document, base blob `12cf0ad74353f152a0e7d11ae498c505c8026b50` | Owns the semantic profile; it does not authorize the action or any repository/lifecycle transition. |
| Machine shape | schema blob `06cf5b9ed4208602f87856c9a5a54c2e2dd561de` | Draft 2020-12, closed object; `PROPOSED_INACTIVE`, `FIXTURE_ONLY_NO_EXTERNAL_EFFECT`, and `authority: NONE`. |
| Fixture replay | manifest blob `d3c03f90eb28f73a4af9efda52116a236c87c132` | Eight synthetic cases: five valid finite-outcome reproductions and three fail-closed mutations. |
| Deterministic builder | builder blob `630da5a6f472a1062103aa205f80123ecad47b2d` | Builds `MATCH`, `MISMATCH`, `BLOCKED`, and `UNCLASSIFIABLE` documents and derives the report, spec hash, and check ID. |
| Static validator | validator blob `e164b0d4ac8ae764c03bbc7d951f79bffccce3d9` | Checks schema, derived report, spec hash, and check ID; fixture mode is local and non-mutating. |
| Focused tests | test blob `fb8d566b772ea88b70d9a67c84e1dc9eb7106e7c` | Covers schema, eight-case polarity, report/identity drift, pointer shape, no-network/write surface, symlink rejection, and deterministic CLIs. |
| Hosted workflow | workflow blob `358e691a8b142218a875698deb992959ab1f19e8` | Runs focused unittest, representative builder output, fixture replay, and generated-receipt integrity validation. |
| Source/lineage map | source-map blob `558242fc0fa5995fbe800a4aea21394a85e28651` | Treats the external Cairnwake report as an idea input, not KFM evidence or authority. |

The checked-in receipt `data/receipts/generated/genrec-cairnwake-action-point-reference-check-20260825.json` preserves authoring-time provenance. Its recorded gates mark focused JSON-schema tests and hosted exact-head CI as `SKIPPED`, and no matching action-point check run was identified for the current `main` commit. The receipt’s eight artifact hashes were stale against the current-main packet; the coupled receipt refresh updates those hashes and the contract binding only. It does not convert historical gates into current hosted proof or human approval.

## Current verification boundary

Confirmed from the repository snapshot:

- The contract, closed schema, eight-case synthetic manifest, deterministic builder, validator, focused tests, source map, workflow, and receipt are present at the paths named above.
- `PASS` means only that a generated declaration reproduces its finite report and deterministic identity. It does not prove that a real action occurred correctly or was authorized.
- The workflow is a command-bearing CI path, not proof that a run passed at the current `main` SHA. No matching action-point check run was identified for `main@eaae135d8f4508c0712e3c6e151d7168a46f54ab` during this reconciliation.
- The profile remains proposed, inactive, fixture-only, no-network, non-mutating, and non-authoritative.

Still open:

- steward ownership, human review, and hosted exact-head validation for any future change;
- live-source dereferencing, action execution, residue capture, and authenticated operational evidence;
- downstream consumer adoption and any policy, review, merge, release, deployment, publication, or public-use decision.

This update does not widen the evidence model, change the schema, alter fixture semantics, change the builder, change the validator, or authorize production use.

## Validation

```bash
python -m unittest tests.validators.test_validate_action_point_reference_check -v
python tools/generators/action_point_reference_check/build_action_point_reference_check.py --case valid-match
python tools/validators/validate_action_point_reference_check.py --fixtures
python tools/validators/validate_generated_receipt.py data/receipts/generated/genrec-cairnwake-action-point-reference-check-20260825.json --repo-root .
```

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive commit. No source, lifecycle, data, release, or public state is changed by this inactive slice.

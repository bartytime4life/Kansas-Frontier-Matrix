<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/issue-projection-receipt
title: IssueProjectionReceipt Contract
type: semantic-contract; process-receipt
version: v1.0.0
status: proposed; fixture-first; dry-run-only; non-authoritative
owners: OWNER_TBD — Governance steward · Repository-control steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal-control-plane; process-memory; no-repository-mutation; no-public-authority
related:
  - ./briefing_signal.md
  - ./issue_inventory_projection.md
  - ../../schemas/contracts/v1/governance/issue_projection_receipt.schema.json
  - ../../fixtures/contracts/v1/governance/issue_projection_receipt/README.md
  - ../../tools/validators/governance/validate_issue_projection_receipt.py
  - ../../tools/validators/governance/project_issue_receipts.py
  - ../../tests/governance/test_issue_projection_receipt.py
  - ../../docs/architecture/briefing-integration.md
tags: [kfm, briefing, issue-routing, receipt, idempotency, dry-run, no-network]
notes:
  - "The v1 profile records one dry-run issue-routing projection only."
  - "A future mutation-capable receipt requires separate authority, exact GitHub result binding, and a versioned successor profile."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# IssueProjectionReceipt Contract

> An `IssueProjectionReceipt` is deterministic process memory for one validated `BriefingSignal` issue-routing projection. It binds the signal, event cluster, router report digest, idempotency key, repository/ref context, read-only inventory input, proposed or held operation, target issue numbers, and finite reasons without attempting or authorizing a GitHub mutation.

## Authority boundary

| Concern | v1 posture |
|---|---|
| Execution mode | `DRY_RUN` only |
| Operation attempted | always `false` |
| Repository mutation permission | always `false` |
| Repository authority | none |
| Evidence, policy, review, proof, release, or publication authority | none |
| Public use | always `false` |
| Live GitHub state | not accepted by this fixture-first profile |
| Durable purpose | replayable process memory and review input |

The receipt records what the local router projected. It does not prove that the underlying signal is true, that an issue is currently open, that the operation is authorized, or that GitHub accepted a write.

## Required bindings

The profile binds:

- canonical repository identity, default branch, and exact 40-character branch-head SHA;
- one `signal_id` and one durable `event_cluster_id`;
- `kfm-briefing-routing-v1`;
- SHA-256 of the complete value-minimized router report;
- the signal's issue-operation idempotency key;
- either no inventory, a required-but-missing inventory, or one validated fixture `IssueInventoryProjection`;
- declared and projected operations;
- declared, effective, closed, and missing GitHub issue numbers;
- canonical finite reason codes;
- an explicit outcome; and
- content-derived receipt digest and ID.

Target issue numbers are GitHub identifiers only. Titles, bodies, comments, labels, assignees, permissions, reviews, merge state, and secret-bearing response metadata are outside this profile.

## Finite operations and outcomes

| Projected operation | Receipt outcome |
|---|---|
| `UPDATE_EXISTING_ISSUE` | `PROPOSED` |
| `OPEN_SOURCE_DISCOVERY_ISSUE` | `PROPOSED` |
| `OPEN_OBJECT_MODEL_ISSUE` | `PROPOSED` |
| `OPEN_CORRECTIVE_ISSUE` | `PROPOSED` |
| `HOLD_FOR_DEPENDENCY` | `HELD` |
| `REJECT_UNSAFE` | `REJECTED` |
| `NO_ACTION` | `NO_ACTION` |
| `ERROR` | `ERROR` |

A declared `UPDATE_EXISTING_ISSUE` may become projected `HOLD_FOR_DEPENDENCY` when inventory is missing, invalid, closed, missing the target, or ambiguous. No other declared/projected operation mismatch is admitted.

## Inventory profiles

| Kind | Meaning | Required state |
|---|---|---|
| `NOT_APPLICABLE` | The operation does not need existing-issue state. | null reference/digest; `NOT_REQUIRED` |
| `MISSING` | An update route required inventory but none was supplied. | null reference/digest; `REQUIRED` |
| `FIXTURE_PROJECTION` | One validated local `IssueInventoryProjection` supported or blocked the projection. | projection ID, digest, and finite inventory status |

The v1 profile deliberately excludes stored live-read receipts. The existing live-read router integration remains a separate reviewed boundary; extending this receipt to bind it requires a versioned successor or explicit compatible schema revision with freshness and receipt-resolution tests.

## Semantic invariants

- Issue-number arrays are sorted and unique.
- Effective targets, closed targets, and missing targets cannot overlap.
- Effective, closed, and missing issue numbers must come from the declared target set.
- A proposed update requires exactly one bound open target and `ISSUE_INVENTORY_OPEN_TARGET`.
- Proposed new-issue operations carry no existing issue number.
- A held update carries no effective target.
- Every receipt includes `ISSUE_PROJECTION_DRY_RUN`.
- Reason codes are sorted and unique.
- `recorded_at` is canonical UTC to the second.
- `receipt_digest` is SHA-256 over canonical JSON excluding only `receipt_id` and `receipt_digest`.
- `receipt_id` is the first 24 digest hex characters under `kfm:issue-projection-receipt:`.

## Builder boundary

`project_issue_receipts.py` accepts only a local router report that:

- reports `status=PASS`;
- contains no findings;
- has `authority_created=false`;
- has `repository_mutation_allowed=false`;
- contains signals sorted uniquely by `signal_id`; and
- uses the bounded routing shape emitted by `route_briefing_signals.py`.

It emits canonical JSON to standard output. It performs no network access, issue write, local lifecycle write, evidence creation, release action, or publication action.

## Anti-collapse rules

| Never collapse | Required distinction |
|---|---|
| Receipt → repository authorization | The receipt records a proposal; external repository-control evidence authorizes writes. |
| Receipt → GitHub mutation | `operation_attempted=false`; no write client exists in this slice. |
| Issue number → issue truth | A numeric target identifies a projected object; it does not authenticate title, state, body, or comments. |
| Router PASS → source/evidence truth | PASS proves bounded deterministic routing mechanics only. |
| Receipt → proof/release | Process memory remains separate from evidence, proof, review, promotion, and release objects. |
| Inventory fixture → live state | Fixture state is synthetic and always reports `live_state_verified=false`. |

## Directory Rules basis

The accepted Directory Governance Standard places semantic meaning in `contracts/governance/`, machine shape in `schemas/contracts/v1/governance/`, synthetic inputs in `fixtures/contracts/v1/governance/`, repository-wide validation and projection tools in `tools/validators/governance/`, enforceability in `tests/governance/`, CI orchestration in `.github/workflows/`, and generated authoring accountability in `data/receipts/generated/`.

No new root or parallel issue, source, evidence, receipt, proof, release, or publication authority is created.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q \
  tests/governance/test_issue_projection_receipt.py \
  --strict-config --strict-markers

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_issue_projection_receipt.py \
  fixtures/contracts/v1/governance/issue_projection_receipt/valid/*.json
```

Known-invalid fixtures must return nonzero.

## Graduation path

A future mutation-capable profile must separately bind:

- current repository-control authorization;
- exact attempted operation and request time;
- before-state and post-write read-back;
- GitHub request or GraphQL identifiers where available;
- authenticated result identity;
- failure and idempotent replay behavior;
- correction/rollback treatment for an incorrect issue mutation; and
- explicit separation from evidence, review, merge, release, and publication authority.

It must not silently reinterpret v1 dry-run receipts as executed operations.

## Rollback

Before merge, close the draft pull request and retire its branch through normal controls. After an authorized merge, revert the bounded implementation commit or merge commit. This profile creates no external issue mutation, lifecycle state, release, deployment, cache, or public state requiring operational cleanup.

[Back to top](#top)

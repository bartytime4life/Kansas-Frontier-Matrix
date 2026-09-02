<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/implementation-decision-record
title: ImplementationDecisionRecord Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Governance steward · Review steward · Contract steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; review-support; non-authoritative
related:
  - ../../schemas/contracts/v1/governance/implementation_decision_record.schema.json
  - ../../fixtures/contracts/v1/governance/implementation_decision_record/cases.json
  - ../../tools/validators/governance/validate_implementation_decision_record.py
  - ../../tests/validators/governance/test_implementation_decision_record.py
  - ../../docs/governance/DECISION_LOG.md
  - ./ReviewRecord.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, implementation-decision, rationale, alternatives, review, ai]
notes:
  - "Adapted from FluencyLoop's decision-journal and reviewer-view concepts without copying its runtime, private calibration profile, or branch-management behavior."
  - "This contract creates reviewer context only. It does not create evidence, policy, approval, mutation, promotion, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# ImplementationDecisionRecord

> A person-neutral, deterministic review-support record for the few implementation decisions that shaped a bounded change: what mechanism was chosen, why, which alternative was rejected or deferred, what evidence and validation support the choice, and how to roll it back.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `LOCAL_NO_NETWORK` |
| Authority created | `NONE` |
| Schema | `schemas/contracts/v1/governance/implementation_decision_record.schema.json` |
| Validator and renderer | `tools/validators/governance/validate_implementation_decision_record.py` |
| Public-use posture | Denied; review-support input only |

A conforming record makes implementation rationale easier to inspect. It does **not** prove that the choice is correct, that evidence was resolved, that a reviewer approved it, that policy allowed it, or that a repository mutation, merge, promotion, release, deployment, or publication is authorized.

## Why this object exists

KFM already distinguishes significant governance decisions, ADRs, review events, generated receipts, and pull-request intake. A smaller gap remains: routine but non-obvious implementation forks often exist only in an AI conversation or a long PR body. Those choices are too local for the significant `Decision Log`, yet they are useful to future reviewers and maintainers.

`ImplementationDecisionRecord` fills only that gap. It is deliberately narrower than:

- an ADR or `GovernanceDecision`, which establishes governance intent;
- a `ReviewRecord`, which records a review event and disposition;
- an `EvidenceBundle`, which supports claims;
- a `GENERATED_RECEIPT`, which records AI authorship and artifact hashes;
- a pull-request template, which remains the complete KFM review and coordination surface.

## Source adaptation

FluencyLoop records meaningful feature decisions with a code area, rationale, rejected alternative, and trust state, then assembles those records into a reviewer-facing view. KFM adopts the useful mechanism while changing the authority model:

| Upstream idea | KFM adaptation |
|---|---|
| Capture only real implementation forks | One record per load-bearing choice; no narration of every edit. |
| Record the chosen mechanism and rejected alternative | Required `decision.mechanism`, `decision.rationale`, and `decision.alternatives`. |
| Assemble a reviewer view deterministically | Validator can render sorted Markdown from one or more records. |
| Keep developer calibration private | No person profile, competence label, teaching score, or hidden reasoning is admitted. |
| Backfill skipped work | Allowed only as `DRAFT` or `NEEDS_VERIFICATION` until evidence and validation references are supplied. |
| Feature workflow is not a correctness gate | A rendered view never replaces KFM validation, human review, policy, or release gates. |

The implementation is original KFM code. No FluencyLoop scripts or templates are vendored.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. This record's semantic meaning belongs under `contracts/governance/`; its machine shape belongs under `schemas/contracts/v1/governance/`; synthetic examples belong under `fixtures/contracts/v1/governance/`; deterministic enforceability belongs under `tools/validators/governance/` and `tests/validators/governance/`; CI belongs under `.github/workflows/`; source adaptation belongs under `docs/intake/exploratory/`; AI authoring provenance belongs under `data/receipts/generated/`.

No new responsibility root or parallel decision, review, receipt, proof, policy, release, or publication home is created.

## Object meaning

An `ImplementationDecisionRecord` binds these concerns without collapsing their authority:

1. **Change identity** — the branch, pull request, issue, or commit range the decision explains.
2. **Scope** — stable repository paths, affected behavior, and named object families.
3. **Mechanism** — how the chosen implementation works.
4. **Rationale and alternatives** — why the option was chosen and why alternatives were rejected or deferred.
5. **Governance significance** — local, cross-component, or authority-significant, with ADR escalation when required.
6. **Support** — evidence and validation references, explicitly separate from the prose rationale.
7. **Rollback** — the strategy and target that make the change reversible.
8. **Non-effects** — all authority flags remain false.

## Finite outcomes

The validator returns one outcome:

- `READY` — internally conformant and marked `READY_FOR_REVIEW`, with validation support and no unresolved escalation;
- `HOLD` — well-formed, but still draft, unsupported, `UNKNOWN`, or missing a required ADR reference;
- `ERROR` — malformed, unsafe, contradictory, unsorted, over-authoritative, or otherwise nonconforming.

CLI exit codes are `0` for `READY`, `3` for `HOLD`, and `2` for `ERROR`. `HOLD` is a fail-closed review state, not an approval or a test success.

## Required semantics

- Repository paths are relative POSIX paths, sorted, unique, and bounded.
- Evidence references, validation references, and object-family names are sorted and unique.
- At least one alternative is recorded with `REJECTED` or `DEFERRED` disposition and a reason.
- `READY_FOR_REVIEW` requires at least one validation reference and cannot use truth label `UNKNOWN`.
- `AUTHORITY_SIGNIFICANT` requires an ADR reference; missing authority produces `HOLD`.
- `CROSS_COMPONENT` must span at least two top-level responsibility roots.
- Rollback strategy and target are required even when the change is documentation-only.
- No prompt body, hidden reasoning, competence profile, personal calibration, secret, credential, or restricted payload is part of the object.
- Every permission remains false and the exact `non_effects` list is preserved.

## Deterministic reviewer view

The renderer sorts records by `record_id` and emits only declared fields:

- title, outcome, change and scope;
- chosen mechanism and rationale;
- alternatives and reviewer questions;
- evidence and validation references;
- governance significance and escalation references;
- rollback strategy and target;
- an explicit non-authority boundary.

The renderer does not inspect a Git diff, infer decisions, create prose beyond fixed labels, or authenticate any reference. The existing KFM pull-request template remains authoritative for complete PR review context.

## Validation

```bash
python -m pytest -q \
  tests/validators/governance/test_implementation_decision_record.py

python tools/validators/governance/validate_implementation_decision_record.py \
  --cases
```

To render valid records:

```bash
python tools/validators/governance/validate_implementation_decision_record.py \
  --render path/to/decision-0001.json path/to/decision-0002.json
```

## Rollback

Revert the feature commit or close the draft pull request. No migration, reprocessing, source activation, release, deployment, cache invalidation, or publication rollback is required because this slice creates only an inactive contract, fixtures, deterministic tooling, tests, documentation, workflow validation, and authoring provenance.

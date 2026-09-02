<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/verification-backlog-item
title: VerificationBacklogItem Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — governance steward · research steward · validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/governance/verification_backlog_item.schema.json
  - ../../fixtures/contracts/v1/governance/verification_backlog_item/base.json
  - ../../fixtures/contracts/v1/governance/verification_backlog_item/cases_ready_hold.json
  - ../../fixtures/contracts/v1/governance/verification_backlog_item/cases_error.json
  - ../../tools/validators/governance/_verification_backlog_item_io.py
  - ../../tools/validators/governance/_verification_backlog_item_model.py
  - ../../tools/validators/governance/_verification_backlog_item_fixtures.py
  - ../../tools/validators/governance/validate_verification_backlog_item.py
  - ../../tests/validators/governance/test_verification_backlog_item.py
  - ../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, verification, backlog, research, evidence, uncertainty]
notes:
  - "Adapts the required research-item record from the KFM Comprehensive Research and Verification Agenda into an inactive fixture contract."
  - "This contract does not create or update a control-plane register. A machine register remains a projection of accepted authority and requires its own governed admission."
[/KFM_META_BLOCK_V2] -->

# VerificationBacklogItem

> A bounded, machine-checkable record of one uncertainty, the evidence and research modes capable of resolving it, the constraints that must fail closed, the affected KFM surfaces, and the acceptance, correction, and rollback conditions needed to close or supersede it.

## Status and non-authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.governance.verification-backlog-item.v1` |
| Status | `PROPOSED_INACTIVE` |
| Execution | `FIXTURE_ONLY_NO_NETWORK` |
| Authority | `NONE` |
| Finite validation outcomes | `READY`, `HOLD`, `ERROR` |
| Public-use posture | Denied; internal verification-planning record only |

A conforming item improves the inspectability of an uncertainty. It does **not** prove an answer, authenticate evidence, activate a source, make an architecture or steward decision, mutate the repository, approve review, promote lifecycle state, release, publish, or authorize public use.

## Why this object exists

KFM already has human-readable verification backlogs across the system and domain lanes. The Comprehensive Research and Verification Agenda adds a stronger requirement: every research item should record its question, bounded answer, primary evidence and locator, currentness risk, rights and sensitivity constraints, conflicts, KFM impact, owner role, acceptance evidence, validation, rollback or correction implication, residual unknowns, and next check.

`VerificationBacklogItem` makes that record testable without replacing:

- `docs/registers/VERIFICATION_BACKLOG.md`, the human-readable register;
- a future `control_plane/` verification projection, which may only project accepted governance;
- `EvidenceBundle`, which supports claims;
- `ReviewRecord`, which records a review event and disposition;
- an ADR or governance decision, which resolves authority;
- a source descriptor or activation decision;
- a validation report, release manifest, correction notice, or rollback card.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. The responsibility split is:

- object meaning under `contracts/governance/`;
- machine shape under `schemas/contracts/v1/governance/`;
- synthetic examples under `fixtures/contracts/v1/governance/`;
- deterministic validation under `tools/validators/governance/`;
- executable proof under `tests/validators/governance/`;
- CI under `.github/workflows/`;
- source adaptation under `docs/intake/exploratory/`;
- AI authoring provenance under `data/receipts/generated/`.

No `control_plane/` record is created in this slice. Directory Rules state that a control-plane register projects accepted authority and cannot self-authorize a new rule. Admission of a new live register class therefore remains separate governance work.

## Research modes

The record preserves the Agenda's separation of ways an uncertainty can be settled:

| Code | Mode | What can settle it |
|---|---|---|
| `EXT` | Authoritative external research | Official source, law, terms, standard, maintained technical documentation, or current primary-source fact. |
| `REPO` | Repository/runtime verification | Current branch, files, configuration, tests, workflows, emitted artifacts, settings, deployments, or observed runtime behavior. |
| `DEC` | Governance/architecture decision | Accepted ADR, ratified policy, or authorized steward decision. |
| `STW` | Domain/legal/sovereignty review | Qualified domain, legal, privacy, tribal/cultural, security, or release authority. |
| `TST` | Measured validation | Fixture, benchmark, replay, dry run, negative test, rollback drill, or correction drill. |

The validator requires every primary-evidence record's mode to be declared by the item. It never substitutes one mode for another: web research cannot prove repository state, a test cannot ratify policy, and technical preference cannot resolve a steward decision.

## Priority

| Priority | Meaning |
|---|---|
| `P0` | Blocks safe architecture, source activation, sensitive handling, or publication. |
| `P1` | Blocks the first proof slice or a credible user-facing surface. |
| `P2` | Blocks scale, performance, operational maturity, or broader domain coverage. |
| `P3` | Improves long-term breadth or optimization without displacing trust-critical work. |

Priority influences ordering only. It grants no authority and cannot convert an unresolved item into a decision.

## Deterministic identity

`item_id` is derived with the repository's RFC 8785 JCS plus SHA-256 implementation from the stable uncertainty projection:

- profile;
- priority;
- question;
- bounded scope and affected roots/object families/domain lanes;
- research modes; and
- basis references.

Mutable progress, evidence, answer, constraints, recommendation, acceptance, and lineage do not create a new uncertainty identity. `spec_hash` binds the complete current record except the `spec_hash` field itself.

## State and finite outcomes

### `READY`

A record is `READY` only when it is internally closed:

- `work_state` is `RESOLVED` with `resolution.status=CONFIRMED`, or it is properly `SUPERSEDED`;
- identity and record hashes match;
- primary evidence is present and canonically ordered;
- resolved items declare acceptance evidence and validation tests;
- residual unknowns are empty for a resolved item;
- rights, sensitivity, sovereignty, security, and public-use constraints are not `UNKNOWN` or `REVIEW_REQUIRED`;
- lineage is coherent.

`READY` means that the backlog record is internally consistent. It is not approval of the underlying decision or public use.

### `HOLD`

An item remains `HOLD` when it is open, in progress, or blocked, or when any of these remain unresolved:

- resolution is not confirmed;
- primary evidence is absent;
- acceptance evidence or validation is absent;
- residual unknowns remain;
- rights, sensitivity, sovereignty, security, or public-use review is still required.

This is the normal state for an honest backlog item.

### `ERROR`

`ERROR` means the record is malformed or contradicts itself, including:

- identity or spec-hash drift;
- noncanonical or duplicated arrays/evidence records;
- evidence using an undeclared research mode;
- a `RESOLVED` item without the evidence, validation, or cleared constraints it claims;
- a `SUPERSEDED` item without a target;
- a blocked item that declares no blocker;
- invalid temporal order or authority overreach.

## Constraints and fail-closed posture

The record carries explicit states for rights, sensitivity, sovereignty, security, and public use. `UNKNOWN` and `REVIEW_REQUIRED` preserve a hold. `RESTRICTED` may be a resolved result when the evidence and authorized decision support the restriction. The record stores only the constraint posture and bounded notes; it must not reveal protected locations, credentials, private data, or sensitive reasons beyond governance need.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q \
  tests/validators/governance/test_verification_backlog_item.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_verification_backlog_item.py \
  --cases
```

## Rollback

Before merge, close the draft pull request and abandon the feature branch. After an authorized merge, revert the feature commit or merge commit. The profile is additive, inactive, fixture-only, and no-network, so rollback requires no source deactivation, data migration, lifecycle cleanup, release withdrawal, cache invalidation, or public correction.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-promotion-gate-status-board
title: Pass 32 promotion gate status board - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; fixture-only; read-only
owners: OWNER_TBD - Governance steward; release steward; UI steward; validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; pass-32; non-authoritative
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0014 with current gate authorities and a bounded reviewer-facing Explorer projection
truth_posture: CONFIRMED source statement and repository gate foundations / PROPOSED app-local status board / NEEDS VERIFICATION hosted exact-head checks and human review
related:
  - ../../../contracts/governance/lifecycle_gate_closure_assessment.md
  - ../../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../../apps/explorer-web/src/features/promotion_gate_status_board/README.md
  - ../../../fixtures/ui/promotion_gate_status_board_projection/README.md
tags: [kfm, pass-32, promotion, gates, status-board, explorer, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Pass 32 promotion gate status board

## Source statement

Pass 32 card `KFM-P32-FEAT-0014` proposes that reviewers see source-monitor, scorecard, schema-validator, OPA-decision, attestation, and release-manifest-candidate states. Its atlas `spec_hash` is `sha256:1c69b3575f3f715d1eaea53a22846fa926cc575ea43e28e239769227f4517620`. The source frames the board as a visibility surface, not as policy, review, promotion, release, or publication authority.

## Current repository reconciliation

KFM already has lifecycle and promotion doctrine, a promotion-gate sequence ADR, gate-outcome mapping, and a fixture-first `LifecycleGateClosureAssessment`. Those objects remain authoritative for their responsibilities. This slice creates no new gate meaning and does not claim that the source card's six display components are a canonical gate sequence.

The bounded gap is a strict, app-local projection that can display the six source-named component states in one fixed order. Artifact references are opaque and unique. The board neither resolves those references nor treats a displayed pass as authenticated execution.

## Implemented boundary

The adapter enforces:

- exact `ANSWER / ABSTAIN / DENY / ERROR` reason pairing;
- canonical observation time and one opaque release-candidate reference;
- exactly six components in source-card order;
- exact component state/reason pairing;
- null artifact references only for `NOT_RUN`;
- unique non-null artifact references;
- recomputed pass/hold/deny/error/not-run counts;
- board state derived as `ERROR`, then `DENY`, then `HOLD`, otherwise `READY_FOR_REVIEW`; and
- fixed-false monitor execution, validator execution, policy evaluation, attestation verification, authenticated review, promotion, release, and publication flags.

`READY_FOR_REVIEW` means only that all six projected components display `PASS`. It does not authenticate a check or reviewer and does not approve a transition. The component is text-first, has no action controls, and invalid input renders nothing without echoing canary detail.

## Directory Rules basis

UI code remains under `apps/`; synthetic projections under `fixtures/ui/`; tests in the Explorer harness; source adaptation under `docs/intake/exploratory/`; and generated authoring accountability under `data/receipts/generated/`. Existing governance and release authorities are referenced rather than copied. These are existing responsibility roots under accepted ADR-0029; no parallel gate, policy, attestation, review, release, or publication home is introduced.

## Validation and non-effects

Validation consists of TypeScript compilation, deterministic fixture-resolution checks, Explorer unit tests, browser-fixture typecheck, Playwright checks, and generated-receipt byte binding. Hosted exact-head checks remain pending review evidence after the draft PR opens.

This slice executes no monitor, scorecard, validator, OPA policy, attestation verification, review authentication, release assembly, lifecycle transition, promotion, deployment, publication, repository setting, or external service.

## Rollback

Before merge, close the draft and abandon its branch. After an authorized merge, revert the additive commit. No lifecycle, policy, attestation, review, release, deployment, or public state requires restoration.

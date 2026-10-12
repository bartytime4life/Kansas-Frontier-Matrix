<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-layer-lineage-timeline-source-map
title: Pass 32 rollback and correction lineage timeline - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; non-authoritative
owners: OWNER_TBD - UI steward; release steward; provenance steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0020 with current repository authorities and the bounded Explorer implementation
truth_posture: CONFIRMED source statement and current-repository overlap / PROPOSED app-local implementation / UNKNOWN production integration and runtime proof
related: [../../../apps/explorer-web/src/features/layer_lineage_timeline/README.md, ../../architecture/publication/ROLLBACK.md, ../../architecture/publication/rollback-and-correction.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 rollback and correction lineage timeline - governed implementation source map

## Source statement

`KFM-P32-FEAT-0020` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes a timeline showing previous artifact digests, correction receipts, rollback targets, and release states for a promoted layer. The connected Drive atlas/seed-card corpus corroborates visible correction and rollback lineage but does not establish repository implementation.

## Current repository reconciliation

At inspected `main@149af17075f7f12d716aa14de439ea22ee6a343e`:

- publication doctrine already fixes the never-delete/always-supersede rule and distinguishes correction from rollback;
- `RollbackCard`, `CorrectionNotice`, release manifests, receipts, and release-plane decisions remain the governing objects;
- existing UI doctrine requires public lineage to remain visible without exposing mutation authority; and
- open pull requests `#2438` through `#2443`, plus drafts `#2446` and `#2447`, do not implement a rollback/correction timeline.

No new release, correction, rollback, evidence, receipt, policy, review, or proof object is justified. The bounded gap is an app-local public-safe chronological projection and read-only timeline.

## Implemented boundary

Only `ANSWER / LINEAGE_AVAILABLE` carries one to sixteen exact entries. Sequence numbers are contiguous, timestamps strictly increase, release and correction references are unique, and each transition closes over the preceding artifact digest. Corrections require a correction receipt and a changed digest. Rollbacks require an earlier release target whose digest equals the restored digest. Withdrawals retain the preceding digest and require a correction receipt or earlier rollback target. The final entry closes over the top-level current release and state.

Negative outcomes carry no layer, release, receipt, rollback, digest, timestamp, or free-form diagnostic detail. Unknown fields, noncanonical timestamps, malformed digests, wrong reference families, broken chronology, unresolved rollback targets, inconsistent transitions, and incomplete positive closure fail closed.

The component does not resolve manifests or receipts, execute rollback/correction, mutate lifecycle state, evaluate policy, authenticate review, authorize release, deploy, publish, or persist state. It renders no control capable of requesting a lifecycle action.

## Directory Rules basis

UI implementation remains under `apps/`; synthetic projections remain under `fixtures/ui/`; tests remain in the Explorer harness; this reconciliation remains under `docs/intake/exploratory/`; authoring accountability remains under `data/receipts/generated/`. Existing release-plane authorities are referenced rather than copied or amended.

## Validation and rollback

Validation is the Explorer unit suite, production typecheck/build, isolated browser-fixture typecheck, hosted Playwright coverage, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; it has no data, lifecycle, evidence, policy, review, release, deployment, or publication effect.

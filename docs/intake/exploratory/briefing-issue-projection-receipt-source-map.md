<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/briefing-issue-projection-receipt-source-map
title: Briefing IssueProjectionReceipt Adaptation Source Map
type: exploratory-intake; source-map
version: v1.0.0
status: proposed adaptation; no repository mutation
created: 2026-08-09
updated: 2026-08-09
[/KFM_META_BLOCK_V2] -->

# Briefing `IssueProjectionReceipt` adaptation

The supplied *KFM Briefing-to-System Integration Architecture* requires every
issue projection to carry an `IssueProjectionReceipt` with the idempotency key,
requested operation, result, and GitHub identifiers. The same source states
that receipts are process memory and remain separate from evidence, proof,
review, release, and publication.

Current repository evidence already provides deterministic `BriefingSignal`
routing, issue-operation idempotency keys, a fixture-backed
`IssueInventoryProjection`, a stored read-only GitHub issue inventory receipt,
and a no-network router. No repository object implementing
`IssueProjectionReceipt` was found on the inspected base.

This adaptation therefore implements only a fixture-first dry-run receipt. It
binds the local router result, repository/ref context, fixture inventory
identity, target issue numbers, finite reasons, and deterministic receipt
identity. It sets `operation_attempted=false` and every authority-bearing flag
to false.

A later mutation-capable successor remains separate. It requires current
repository-control authorization, actual GitHub result identity, post-write
read-back, replay behavior, and a correction path for an incorrect issue
mutation. This adaptation does not write an issue, read live GitHub state,
approve merge, construct evidence, release, deploy, or publish.

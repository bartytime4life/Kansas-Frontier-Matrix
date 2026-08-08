<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-live-issue-inventory-binding
title: Briefing Live Issue Inventory Binding
type: architecture; integration-boundary
version: v0.1.0
status: proposed; stacked-on-github-issue-inventory-read; non-authoritative
owners: OWNER_TBD — Governance steward · Architecture steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal-control-plane; read-only; no-public-authority; no-repository-mutation
related:
  - ../../contracts/governance/issue_inventory_projection.md
  - ../../contracts/governance/github_issue_inventory_read.md
  - ../../tools/validators/governance/route_briefing_signals.py
  - ../../tools/validators/governance/validate_github_issue_inventory_read.py
  - ../../tests/governance/test_briefing_signal_live_issue_inventory.py
tags: [kfm, governance, briefing, github, issue-inventory, read-only, freshness, routing]
[/KFM_META_BLOCK_V2] -->

# Briefing Live Issue Inventory Binding

This integration is **PROPOSED** and non-authoritative. It allows the existing BriefingSignal dry-run router to consume a previously captured `GitHubIssueInventoryRead` receipt in addition to the existing deterministic fixture `IssueInventoryProjection`.

The router itself remains no-network. Live GitHub retrieval is a separate diagnostic step. The captured receipt must pass its closed schema, deterministic digest and receipt-id checks, report outcome `FRESH`, and remain inside its explicit `retrieved_at..stale_at` window at a caller-supplied `--as-of` time.

## Fail-closed routing

```text
BriefingSignal
  -> deterministic declared route
  -> fixture IssueInventoryProjection
       OR
     stored GitHubIssueInventoryRead receipt
  -> freshness / identity / issue-set validation
  -> one open target => UPDATE_EXISTING_ISSUE proposal
  -> stale / invalid / ambiguous / absent => HOLD or FAIL
```

Fixture and live-read inventory inputs are mutually exclusive. A live receipt without an explicit `--as-of` is rejected so replay does not depend on wall-clock time.

A successful live binding adds `BOUND_OPEN_TARGET_LIVE_READ` and `ISSUE_INVENTORY_LIVE_READ_FRESH` to the dry-run report. These markers prove only that a valid fresh read receipt supported the routing proposal. They do not authorize an issue mutation.

## Trust boundary

This integration does not open, close, edit, label, assign, comment on, merge, or otherwise mutate GitHub objects. It creates no repository authority, EvidenceBundle, policy decision, review approval, lifecycle transition, release, deployment, publication, or public-use authority. The existing fixture profile remains the deterministic contract-test reference.

## Directory Rules basis

Integration documentation stays under `docs/architecture/`; reusable governance validators stay under `tools/validators/governance/`; synthetic proof inputs stay under `fixtures/contracts/v1/governance/`; enforceability stays under `tests/governance/`; CI orchestration stays under `.github/workflows/`. No new responsibility root is introduced.

## Rollback

Before merge, close the stacked draft PR. After an authorized merge, revert the bounded integration commit. No external GitHub mutation or KFM lifecycle/public state is created by this slice.

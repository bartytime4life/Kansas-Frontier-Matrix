<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-architecture-briefing-live-issue-inventory-binding
title: Briefing Live Issue Inventory Binding
type: architecture; integration-boundary
version: v0.2.0
status: proposed; current-main repair; non-authoritative
owners: OWNER_TBD — Governance steward · Architecture steward · Validation steward
created: 2026-08-08
updated: 2026-08-09
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

This integration is **PROPOSED** and non-authoritative. It allows the existing BriefingSignal dry-run router to consume a previously captured `GitHubIssueInventoryRead` receipt in addition to the deterministic fixture-backed `IssueInventoryProjection`.

The read-only adapter reached `main` through PR #2179. The dependent router binding from PR #2180 was merged into the already-merged parent branch rather than current `main`, so the integration bytes did not become part of the default branch. This bounded repair replays only the dependency-closed router, stored receipt fixture, validator, focused test, and this current-state note against current `main`.

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

The router performs no network access. Fixture and stored-read inputs are mutually exclusive. A stored receipt without an explicit `--as-of` is rejected so replay never depends on wall-clock time. The receipt must satisfy its closed schema, deterministic digest and receipt identity, report `FRESH`, and remain inside its declared retrieval window.

A successful binding adds `BOUND_OPEN_TARGET_LIVE_READ` and `ISSUE_INVENTORY_LIVE_READ_FRESH` to the dry-run report. These markers support a routing proposal only. They do not authorize a GitHub issue mutation.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q \
  tests/governance/test_briefing_signal_live_issue_inventory.py \
  tests/governance/test_briefing_signal_issue_inventory.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/route_briefing_signals.py \
  --github-issue-inventory-read \
  fixtures/contracts/v1/governance/github_issue_inventory_read/fresh_receipt_1647.json \
  --as-of 2026-08-08T02:31:00Z \
  examples/briefing_integration/*.json
```

## Trust boundary

This integration does not open, close, edit, label, assign, comment on, merge, or otherwise mutate GitHub objects. It creates no repository authority, `EvidenceBundle`, policy decision, review approval, lifecycle transition, release, deployment, publication, or public-use authority. The fixture profile remains the deterministic contract-test reference.

## Directory Rules basis

Integration documentation stays under `docs/architecture/`; reusable governance validators stay under `tools/validators/governance/`; synthetic proof inputs stay under `fixtures/contracts/v1/governance/`; and enforceability stays under `tests/governance/`. No new responsibility root, registry, lifecycle phase, policy home, release home, or proof home is introduced.

## Rollback

Before merge, close the draft pull request and abandon the branch. After an authorized merge, revert the bounded repair commit. No external GitHub mutation or KFM lifecycle/public state is created by this slice.

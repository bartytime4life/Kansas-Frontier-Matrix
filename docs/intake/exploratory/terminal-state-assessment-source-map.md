<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/terminal-state-assessment
title: Terminal-state divergence adaptation
status: proposed adaptation; fixture-only
type: exploratory-intake; source-map
created: 2026-08-08
updated: 2026-08-08
[/KFM_META_BLOCK_V2] -->

# Terminal-state divergence adaptation

## Goal

Implement the smallest no-network regression surface for the briefing architecture's P0 `TerminalStateDivergence` object family: compare an explicit `DRAFT_PR` or `READY_PR` ceiling to observed pull-request state and fail closed when the host advances beyond it.

## Evidence basis

**CONFIRMED source statement:** the briefing integration blueprint defines terminal-state divergence as incident evidence, calls for one-writer regression fixtures from prior unexpected merges, and states that mergeability is not authorization and draft state is not approval.

**CONFIRMED repository basis at authoring:** accepted ADR-0029 establishes responsibility-root placement; repository-control objects already live under governance lanes; no exact `TerminalStateDivergence` contract or validator was found on the inspected main revision.

## Added bounded result

The packet adds a proposed semantic contract, strict schema, fourteen exact fixtures, deterministic validator, focused tests, read-only workflow, and generated receipt. It performs no GitHub API request and changes no pull-request or repository state.

## Non-effects

No settings, permissions, branch protection, rulesets, draft state, review state, merge, release, deployment, or publication action is performed or authorized.

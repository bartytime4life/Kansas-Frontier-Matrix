# Source adaptation — InspectableClaimCarrierAssessment

## Goal

Turn KFM's repeated **inspectable claim / carriers are not truth** doctrine into one small fixture-only guard reusable across map, tile, graph, dashboard, export, story, AI, and 3D review work.

## Source basis

- KFM Components Pass 11: the durable public output is the inspectable claim and trust-visible negative states are part of the evidence contract.
- KFM MapLibre Operating Architecture: the renderer is downstream of trust and public surfaces must expose evidence, policy, release, stale, and correction state.
- KFM Connected-Dots / Unified Doctrine: maps, tiles, graph edges, dashboards, exports, scenes, and AI answers are carriers rather than sovereign truth.
- KFM Pipeline Living Manual: EvidenceBundle, policy, release, correction, and rollback remain separate object families and the governed loop cannot self-publish.

## Repository adaptation

The repository already has specialized carrier/readiness profiles, negative-state audits, EvidenceBundle families, release manifests, correction/rollback objects, and governed AI/map contracts. The missing cross-cutting check is a minimal declaration that a carrier retains the trust bindings needed to remain inspectable without claiming to validate those upstream objects.

This packet checks reference presence and negative-state visibility only. It deliberately does not dereference evidence, evaluate policy, verify release state, or authorize public use.

## Non-effects

No source activation, lifecycle write, EvidenceBundle creation, policy approval, review approval, promotion, release, deployment, publication, or public-route mutation occurs.

## Directory Rules basis

Accepted ADR-0029 routes semantic meaning, machine shape, fixtures, validation, tests, CI, and exploratory source adaptation to their existing responsibility roots. No parallel authority is introduced.

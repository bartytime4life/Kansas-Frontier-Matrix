<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-ssurgo-yearly-change-viewer-source-map
title: Pass 32 SSURGO yearly change viewer - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; fixture-only; non-authoritative
owners: OWNER_TBD - UI steward; soil steward; provenance steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0018 with current soil yearly-diff authorities and the bounded Explorer implementation
truth_posture: CONFIRMED source statement and current-repository overlap / PROPOSED app-local implementation / UNKNOWN production integration and hosted exact-head proof
related: [../../../apps/explorer-web/src/features/soil_yearly_change_viewer/README.md, ../../../contracts/domains/soil/ssurgo_yearly_diff_profile.md, ../../../tools/generators/build_soil_yearly_diff.py]
[/KFM_META_BLOCK_V2] -->

# Pass 32 SSURGO yearly change viewer - governed implementation source map

## Source statement

`KFM-P32-FEAT-0018` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes a viewer comparing year N and year N-1 soil layers with diff metrics and provenance anchors. The connected Drive atlas and Directory Rules corpus corroborates the idea and placement constraints but does not establish repository implementation.

## Current repository reconciliation

At inspected `main@457e4fba09ef641efbddc0639bd8127e4c464b5a`, `SoilYearlyDiffProfile`, its strict schema and validator, synthetic SSURGO snapshots, deterministic local builder, tests, and workflow already own the fixture-only year-pinned comparison semantics. No open pull request implements the viewer card, and the source-availability watchlist idea is separately covered by historical PR `#2263`.

No new soil source, snapshot, diff, STAC, PROV, receipt, evidence, policy, promotion, release, or publication object is justified. The bounded gap is an unmounted Explorer adapter plus read-only text-first viewer.

## Implemented boundary

Only an exact `ANSWER / DIFF_AVAILABLE` projection carries consecutive SSURGO snapshots, bounded added/removed/modified counts, canonical changed-property names, and explicit diff, STAC, PROV, source-snapshot, and validation anchors. It is fixed to `PROPOSED_INACTIVE`, `FIXTURE_ONLY`, the accepted SSURGO support role and descriptor, and `publication_authorized: false`.

Negative outcomes carry no source, snapshot, digest, receipt, STAC, or provenance detail. Unknown fields, wrong reason/outcome pairs, nonconsecutive years, identical snapshot digests, wrong reference families, noncanonical properties, count/property incoherence, source-role collapse, or publication overreach fail closed and render nothing.

The viewer does not fetch NRCS data, compare records, validate a real digest or STAC/PROV graph, interpret differences as soil change or materiality, mount a route, write lifecycle state, promote, release, deploy, or publish.

## Directory Rules basis

UI implementation remains under `apps/explorer-web/`; synthetic display projections remain under `fixtures/ui/`; tests remain in the Explorer harness; this reconciliation remains under `docs/intake/exploratory/`; and authoring accountability remains under `data/receipts/generated/`. Existing soil authorities are referenced rather than copied or amended.

## Validation and rollback

Validation is the targeted Explorer unit suite, full Explorer unit suite, production typecheck/build, isolated browser-fixture typecheck, hosted Playwright coverage, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; it has no source, data, lifecycle, evidence, policy, promotion, release, deployment, or publication effect.

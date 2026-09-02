<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-environmental-anomaly-scorecard-source-map
title: Pass 32 environmental anomaly scorecard - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; fixture-only; non-authoritative
owners: OWNER_TBD - UI steward; environmental data stewards; source-health steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0006 with current county environmental projections and the bounded Explorer implementation
truth_posture: CONFIRMED source statement and current-repository overlap / PROPOSED app-local implementation / UNKNOWN production integration and hosted exact-head proof
related: [../../../apps/explorer-web/src/features/environmental_anomaly_scorecard/README.md, ../../../contracts/data/county_environmental_recency_spine.md, pass-32-county-environmental-cadence-calendar-source-map.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 environmental anomaly scorecard - governed implementation source map

## Source statement

`KFM-P32-FEAT-0006` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes a county scorecard that summarizes vegetation, hydrology, air, soils, and biodiversity freshness and anomaly candidates. The card is sourced to `SRC-P32-002`, the connected Drive document *New Ideas 5-17-26*. Both sources describe a downstream candidate; neither establishes repository implementation, anomaly truth, or authority.

## Current repository reconciliation

At inspected `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a`, the county environmental recency spine, county cadence calendar, source-health references, and several domain-specific panels already provide bounded foundations. Repository and open-pull-request searches found no implementation for the exact environmental anomaly scorecard card.

No new source, probe, watcher, anomaly algorithm, model, evidence authority, policy decision, lifecycle object, promotion gate, release object, or publication object is justified. The smallest dependency-closed gap is an unmounted Explorer adapter, read-only table-first scorecard, synthetic projections, and focused tests.

## Implemented boundary

Only an exact `ANSWER / SCORECARD_AVAILABLE` projection carries one synthetic Kansas county scope, a canonical UTC assessment time, five ordered domain lanes, unique source-health and evidence references, and a derived `COMPLETE` or `HOLD` rollup. A `PROPOSED` candidate state is a pointer to a separately governed candidate, not a finding. Stale, missing, or errored lanes carry no evidence or candidate reference. Finite negative display outcomes carry no county, time, lane, health-assessment, evidence, or candidate detail.

The projection is fixed to `PROPOSED_INACTIVE`, `FIXTURE_ONLY`, and false interpretation, publication, and public-use authority. Unknown fields, wrong outcome/reason pairs, wrong lane order or set, reused references, impossible freshness/candidate/reason combinations, summary mismatch, noncanonical time, or authority overreach fail closed and render nothing.

The scorecard does not probe sources, author source health, compute an anomaly, interpret environmental conditions, mount a route, invoke a model, evaluate policy, write lifecycle state, promote, release, deploy, publish, or authorize public use.

## Directory Rules basis

UI implementation remains under `apps/explorer-web/`; synthetic display projections remain under `fixtures/ui/`; tests remain in the Explorer harness; this reconciliation remains under `docs/intake/exploratory/`; and authoring accountability remains under `data/receipts/generated/`. County is a composition scope rather than a new domain or repository root, and existing source-health and evidence authorities are referenced rather than copied.

## Validation and rollback

Validation is the targeted Explorer unit suite, full Explorer unit suite, production typecheck/build, isolated browser-fixture typecheck, hosted Playwright coverage, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; it has no source, data, lifecycle, evidence, policy, interpretation, promotion, release, deployment, publication, or public-use effect.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-county-environmental-cadence-calendar-source-map
title: Pass 32 county environmental cadence calendar - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; fixture-only; non-authoritative
owners: OWNER_TBD - UI steward; data steward; source steward; temporal steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0015 with the county environmental recency spine and the bounded Explorer implementation
truth_posture: CONFIRMED source statement and current-repository overlap / PROPOSED app-local implementation / UNKNOWN production integration and hosted exact-head proof
related: [../../../apps/explorer-web/src/features/county_environmental_cadence_calendar/README.md, ../../../contracts/data/county_environmental_recency_spine.md, pass-32-county-environmental-recency-source-map.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 county environmental cadence calendar - governed implementation source map

## Source statement

`KFM-P32-FEAT-0015` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes a weekly county calendar showing source-freshness status across vegetation, imagery, hydrology, air, soils, and biodiversity. The connected Drive atlas and Directory Rules corpus corroborates the idea and placement constraints but does not establish repository implementation.

## Current repository reconciliation

At inspected `main@457e4fba09ef641efbddc0639bd8127e4c464b5a`, `CountyEnvironmentalRecencySpineCandidate`, its strict schema and validator, synthetic six-lane cases, tests, and workflow already own the fixture-only county/week rollup semantics. The existing contract explicitly leaves a downstream UI surface out of that slice. No open pull request implements the cadence calendar card.

No new source, probe, watcher, source-health, temporal-support, material-change, evidence, policy, lifecycle, promotion, release, or publication object is justified. The bounded gap is an unmounted Explorer adapter plus read-only table-first calendar.

## Implemented boundary

Only an exact `ANSWER / CALENDAR_AVAILABLE` projection carries one synthetic Kansas county scope, one exact 168-hour UTC week, the six canonical lanes, unique source and health-assessment references, reproduced check/health/reason closure, and a coherent `COMPLETE` or `HOLD` rollup. The downstream `ANSWER` means only that the display packet is structurally available; `HOLD` retains the upstream non-interpretation posture.

The projection is fixed to `PROPOSED_INACTIVE`, `FIXTURE_ONLY`, and false interpretation, publication, and public-use authority. It excludes errored lanes because the upstream candidate reports them as `ERROR`; finite negative display outcomes carry no county, time, source, or lane detail. Unknown fields, wrong reason/outcome pairs, nonweekly time, wrong lane order/set, reused references, impossible check/health/reason combinations, summary mismatch, or authority overreach fail closed and render nothing.

The calendar does not probe sources, author source health, clear stale or missing status, interpret environmental conditions, mount a route, evaluate policy, write lifecycle state, promote, release, deploy, publish, or authorize public use.

## Directory Rules basis

UI implementation remains under `apps/explorer-web/`; synthetic display projections remain under `fixtures/ui/`; tests remain in the Explorer harness; this reconciliation remains under `docs/intake/exploratory/`; and authoring accountability remains under `data/receipts/generated/`. The county remains a composition scope, not a new domain or root, and existing data/source authorities are referenced rather than copied.

## Validation and rollback

Validation is the targeted Explorer unit suite, full Explorer unit suite, production typecheck/build, isolated browser-fixture typecheck, hosted Playwright coverage, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; it has no source, data, lifecycle, evidence, policy, interpretation, promotion, release, deployment, publication, or public-use effect.

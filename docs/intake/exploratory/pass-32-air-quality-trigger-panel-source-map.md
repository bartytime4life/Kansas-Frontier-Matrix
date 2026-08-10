<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-air-quality-trigger-panel-source-map
title: Pass 32 air-quality trigger panel - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; fixture-only; non-authoritative
owners: OWNER_TBD - UI steward; atmosphere steward; evidence steward; policy steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal
owning_root: docs/
responsibility: reconcile Pass 32 KFM-P32-FEAT-0007 with the PM2.5 trigger-candidate assessment and a bounded Explorer projection
truth_posture: CONFIRMED source statement and repository foundation / PROPOSED app-local implementation / UNKNOWN production integration and hosted exact-head proof
related: [../../../apps/explorer-web/src/features/air_quality_trigger_panel/README.md, ../../../contracts/domains/atmosphere/pm25_trigger_candidate_assessment.md, pass-32-pm25-trigger-candidate-source-map.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 air-quality trigger panel - governed implementation source map

## Source statement

`KFM-P32-FEAT-0007` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes a panel that distinguishes denied negative fixtures from positive evidence-backed PM2.5 trigger candidates. The related `KFM-P32-IDEA-0012` requires monitored-threshold, trailing-median, and source-evidence conditions to meet fail-closed positive-fixture criteria. The source is a downstream design candidate; it does not establish repository implementation, scientific validity, evidence closure, policy, an event, regulatory compliance, health advice, release, or publication.

## Current repository reconciliation

At inspected `main@7c69e025e2b274be4a19f49fa37e22401a2fe757`, `PM25_TRIGGER_CANDIDATE_ASSESSMENT_V1`, its closed schema, deterministic validator, synthetic positive/no-trigger/hold/error/denial cases, tests, workflow, and source map already own categorical candidate-assessment meaning. They expressly do not expose a UI or resolve evidence. Current open PRs implement a View Registry inspector and streamflow QC dashboard on disjoint paths; neither implements this card.

The smallest dependency-closed gap is an unmounted Explorer projection over categorical relations and digest-bound references. No source fetch, observation contract, numeric computation, detector, EvidenceBundle producer, policy pack, route, workflow, event, health/regulatory surface, or lifecycle writer is justified.

## Implemented boundary

The adapter accepts exact fixture-only packets. A proposed candidate requires the fixed `OBSERVED_SENSOR` knowledge character, both finite relations above their separately governed references, two or more distinct digest-bound EvidenceRefs, and immutable assessment/observation/baseline references. A no-candidate packet requires at least one at-or-below relation. Held, denied, and error outcomes carry no candidate or reference detail.

The source phrase “evidence-backed” is deliberately narrowed to `REFERENCED_NOT_RESOLVED` because this slice does not resolve EvidenceRefs to EvidenceBundles. All network, detector, event, regulatory, health, policy, review, promotion, release, publication, and public-use authority is fixed false. No raw concentration, numeric threshold, AQI value, coordinate, station identity, or health category enters the accepted shape.

## Directory Rules basis

Accepted ADR-0029 and Directory Rules route the user surface and app-local adapter to `apps/explorer-web/`, synthetic reusable display packets to `fixtures/ui/`, feature proof to the Explorer test harness, human source reconciliation to `docs/intake/exploratory/`, and authoring accountability to `data/receipts/generated/`. Existing Atmosphere contract, schema, validator, fixture, and workflow authority is consumed without duplication.

## Sources

- Consolidated atlas card `KFM-P32-FEAT-0007`, spec hash `sha256:63e16ecd2e3cd675b3b2efc5fb2e326acd9308dfe89dd6df65451463dc44c5d5`.
- Consolidated atlas card `KFM-P32-IDEA-0012`, spec hash `sha256:1a1b69f7617d949b015eb6e459a061b07789a7be4c5626113defeb43e00a0f88`.
- Connected Drive Pass 32 atlas: `https://drive.google.com/file/d/1nNpWLceYOifELgJDB3ihQHTtYfQUsvdN`.
- Repository foundation: `contracts/domains/atmosphere/pm25_trigger_candidate_assessment.md` and its paired schema, validator, fixtures, tests, and workflow.

## Validation and rollback

Validation covers targeted and full Explorer unit suites, production build, isolated browser-fixture typechecking and discovery, the existing PM2.5 candidate-assessment suite, metadata and link checks, strict JSON parsing, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; it creates no external, source, detector, event, evidence, policy, review, lifecycle, promotion, release, deployment, publication, or public-use state.

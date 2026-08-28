<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-forecast-product-source-map
title: Briefing ForecastProduct Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED adaptation; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; forecast; no-authority
owning_root: docs/
responsibility: Record the bounded adaptation from the briefing conditions framework into an inactive ForecastProduct profile and preserve the next conditions backlog.
truth_posture: "CONFIRMED current repository overlap check; PROPOSED adaptation; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/common/forecast_product.md
  - ../../../contracts/common/classification_release.md
  - ../../../contracts/common/condition_relation.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, briefing, forecast, conditions]
[/KFM_META_BLOCK_V2] -->

# Briefing ForecastProduct Source Map

## Source requirement

The briefing conditions framework identifies `ForecastProduct` as distinct from
`ObservationRecord`, `ClassificationRelease`, modeled surfaces, surveys, and
aggregates. It requires issue time, valid interval, model or forecaster
identity, method, geography, and uncertainty to remain explicit.

## Repository reconciliation

CONFIRMED against the implementation base:

- `ClassificationRelease`, `ConditionRelation`, common temporal envelopes, and
  domain-owned observations already exist;
- the repository has deterministic RFC 8785 JCS plus SHA-256 identity support;
- ADR-0029 accepts Directory Governance Standard v2;
- bounded searches found no existing `forecast_product` contract, schema,
  validator, fixture packet, or open pull request for the exact family.

## Adaptation

The smallest coherent slice is an inactive, fixture-only common contract with
closed shape, explicit forecast role, model/expert/hybrid method context,
uncertainty, source-lineage states, deterministic identity, focused tests, a
read-only workflow, and a byte-bound authoring receipt.

## Next sourced ideas

1. Conditions source-role crosswalk matrix for classification, observation,
   forecast, model, survey, aggregate, and contextual relation families.
2. `ModeledSurface` profile with model version, training/support limits,
   resolution, uncertainty, and derived-only authority.
3. `AggregateStatistic` profile with geography, weighting, denominator, and
   source release.
4. Forecast-to-observation `ConditionRelation` fixtures that preserve valid-time
   overlap and deny causality.
5. Public Conditions Explorer only after released, public-safe projections,
   evidence closure, correction, and rollback exist.

## Deliberate holds

No live forecast endpoint, source rights decision, advisory, alert, model
execution, public API, MapLibre layer, search index, Focus Mode answer, release,
or publication is introduced.

## Rollback

Discard the branch before merge or revert the additive packet afterward. No
live or public state is affected.

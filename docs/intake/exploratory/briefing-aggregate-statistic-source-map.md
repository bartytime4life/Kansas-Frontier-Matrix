<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-aggregate-statistic-source-map
title: Briefing AggregateStatistic Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED adaptation; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; aggregate; no-authority
owning_root: docs/
responsibility: Record the bounded adaptation from the briefing conditions framework into an inactive AggregateStatistic profile.
truth_posture: "CONFIRMED source and current repository overlap check; PROPOSED adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/aggregate_statistic.md
  - ../../../contracts/common/classification_release.md
  - ../../../contracts/common/condition_relation.md
  - ../../../contracts/common/forecast_product.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, briefing, aggregate-statistic, conditions]
[/KFM_META_BLOCK_V2] -->

# Briefing AggregateStatistic source map

## Source requirement

The Google Drive **KFM Briefing-to-System Integration Architecture** conditions
lane identifies `AggregateStatistic` as distinct from observations, modeled
surfaces, forecasts, classification releases, and survey products. It requires
aggregation geography, weighting, denominator, and source release to remain
explicit. The supplied consolidated atlas separately warns that aggregate
statistics must not become field/operator truth.

Both are design sources, not implementation or source-admission authority.

## Repository reconciliation

CONFIRMED at selection base `main@149af17075f7f12d716aa14de439ea22ee6a343e`:

- existing classification, forecast, relation, temporal, and domain-observation
  families preserve adjacent source roles;
- `ClassificationRelease` already carries unresolved aggregate-statistic
  references but does not define their meaning;
- repository RFC 8785 JCS plus SHA-256 hashing is available;
- ADR-0029 accepts Directory Governance Standard v2;
- exact repository and GitHub PR searches found no `AggregateStatistic`
  contract, schema, validator, fixture family, branch, or prior PR; and
- eight open PRs at selection time concern disjoint UI, runtime, evidence, and
  documentation work.

## Adaptation

The smallest dependency-closed slice is an inactive common contract, closed
schema, exact synthetic cases, deterministic no-network validator, focused
tests, read-only CI, and byte-bound authoring receipt. It binds geography,
weighting, numerator/denominator, missing-data treatment, source release, time,
uncertainty, lineage, identity, and all-false authority effects without
computing or publishing a statistic.

## Directory and authority decision

The artifact's authority owner is common semantic meaning, so the placement
outcome is `PLACE` under `contracts/common/` with paired responsibility roots.
No parallel statistics, data, source, evidence, policy, release, or public home
is created.

## Deliberate holds and rollback

No live source or real value, weighting or imputation execution, source-rights
decision, exact-local condition, EvidenceBundle resolution, public DTO, map, AI
answer, release, or publication is introduced.

Discard the branch before merge or revert the additive packet afterward. No
live or public state is affected.

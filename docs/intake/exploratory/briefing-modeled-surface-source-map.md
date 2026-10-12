<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-modeled-surface-source-map
title: Briefing ModeledSurface Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED adaptation; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; model; no-authority
owning_root: docs/
responsibility: Record the bounded adaptation from the briefing conditions framework into an inactive ModeledSurface profile.
truth_posture: "CONFIRMED source and current repository overlap check; PROPOSED adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/modeled_surface.md
  - ../../../contracts/common/classification_release.md
  - ../../../contracts/common/condition_relation.md
  - ../../../contracts/common/forecast_product.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, briefing, modeled-surface, conditions]
[/KFM_META_BLOCK_V2] -->

# Briefing ModeledSurface source map

## Source requirement

The Google Drive **KFM Briefing-to-System Integration Architecture** conditions
lane identifies `ModeledSurface` as distinct from observations, forecasts,
classification releases, survey products, and aggregate statistics. It requires
model version, training/support limits, spatial resolution, and uncertainty to
remain visible. The supplied consolidated atlas independently warns that
aggregate and satellite products must not become field/operator truth.

Both are design sources, not implementation or source-admission authority.

## Repository reconciliation

CONFIRMED at selection base `main@149af17075f7f12d716aa14de439ea22ee6a343e`:

- `ClassificationRelease`, `ForecastProduct`, `ConditionRelation`, temporal
  envelopes, and domain-owned observations already exist;
- repository RFC 8785 JCS plus SHA-256 hashing is available;
- ADR-0029 accepts Directory Governance Standard v2;
- exact repository and GitHub PR searches found no `ModeledSurface` contract,
  schema, validator, fixture family, branch, or prior PR; and
- eight open PRs at selection time concern disjoint UI, runtime, evidence, and
  documentation work.

## Adaptation

The smallest dependency-closed slice is an inactive common contract, closed
schema, exact synthetic cases, deterministic no-network validator, focused
tests, read-only CI, and byte-bound authoring receipt. It binds model/support,
space, resolution, time, uncertainty, lineage, identity, and all-false authority
effects without executing a model or making a factual claim.

## Directory and authority decision

The artifact's authority owner is common semantic meaning, so the placement
outcome is `PLACE` under `contracts/common/` with paired responsibility roots.
No parallel model, source, evidence, policy, release, or public home is created.

## Deliberate holds and rollback

No live model or source, real training data, inference, interpolation, rights or
sensitivity decision, field truth, EvidenceBundle resolution, public DTO, map,
AI answer, release, or publication is introduced.

Discard the branch before merge or revert the additive packet afterward. No
live or public state is affected.

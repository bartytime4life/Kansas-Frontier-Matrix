<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-20-frontier-definition-source-map
title: Pass 20 FrontierDefinition Source Map
type: exploratory-source-map
version: v0.1.0
status: complete-for-proposed-fixture-slice; human-review-pending
owners: OWNER_TBD - Analytics steward; Evidence steward; Geography steward; Policy steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-adaptation; no-network
owning_root: docs/
responsibility: Record how Pass 20 KFM-IDX-APP-008, current IndicatorDefinition semantics, and the draft GeographyVersion dependency were narrowed into one inactive fixture-only FrontierDefinition packet.
truth_posture: CONFIRMED source/repository comparison / PROPOSED implementation packet / NEEDS VERIFICATION human review and hosted exact-head checks
related:
  - ../../../contracts/evidence/frontier_definition.md
  - ../../../contracts/evidence/indicator_definition.md
  - ../../../contracts/common/geography_version.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-20, frontier-definition, county-year, criteria, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Pass 20 FrontierDefinition Source Map

## Source statement

Pass 20 card `KFM-IDX-APP-008` proposes a future frontier-demography and economy product built as a versioned county-year panel. It names `FrontierDefinition`, `GeographyVersion`, population/economic/agriculture/access observations, crosswalks, uncertainty, release manifests, and rollback cards. Its next-step guidance is definitions first, followed by synthetic fixtures, before any public analytical claim.

Related Pass 20 interpretation guidance requires indicators to declare assumptions, source choices, scale, uncertainty, and decision context. Time-modeling guidance distinguishes valid time, transaction time, publication time, retrieval time, and correction time.

These source statements are design evidence. They do not prove an accepted frontier rule, source admission, repository implementation, analytic correctness, policy approval, release, or publication.

## Repository reconciliation

At authoring base `main@18b5bba4bf53edcd5b9ac61779a0cccade35d186`:

- the merged `IndicatorDefinition` profile provides digest-addressable analytic-method declarations with denominator, missing-data, uncertainty, and geography-version discipline;
- draft PR #2502 proposes the shared fixture-only `GeographyVersion` dependency without geography or crosswalk resolution;
- bounded exact-path, pull-request, and branch probes found no `FrontierDefinition` contract, schema, fixture family, validator, test, open implementation pull request, or same-purpose branch;
- prior county-year work records geography-version and frontier-definition needs but does not implement this object family; and
- the implementation is therefore stacked on #2502 so it cannot imply a geography dependency that the target branch lacks.

Differently named or unindexed implementations remain possible. This packet claims a bounded checked-path gap, not universal absence.

## Implemented boundary

The packet declares one inactive county-scoped definition, valid interval, calendar-year support, geography-version dependency, indicator-definition dependencies, opaque threshold-policy references, combination rule, fail-closed missingness and uncertainty, result vocabulary, assumptions, evidence references, disclosure limits, and deterministic identity.

The validator:

- rejects empty or inverted valid intervals;
- requires sorted unique criteria and digest-bound dependencies;
- requires the criterion indicator-reference set to exactly match declared support dependencies;
- forbids inline thresholds, county identifiers, observations, scores, and classification results by closed schema;
- fixes unresolved inputs and indeterminate outcomes to abstention / `UNCLASSIFIED`; and
- fixes all operational, classification, policy, review, release, and publication authorities to false.

It does not resolve any reference, load source data, execute a formula or rule, compare an observation to a threshold, join a geography, classify a county, evaluate uncertainty or missingness, or change lifecycle state.

## Directory Rules basis

Accepted ADR-0029 and Directory Rules route interpretive claim semantics to `contracts/evidence/`, paired machine shape to `schemas/contracts/v1/evidence/`, synthetic replay to `fixtures/contracts/v1/evidence/`, reusable checks to `tools/validators/evidence/`, test evidence to `tests/validators/evidence/`, orchestration to `.github/workflows/`, human reconciliation to `docs/intake/exploratory/`, and generated authoring accountability to `data/receipts/generated/`.

No new root or parallel analytics, frontier, geography, schema, evidence, policy, source, registry, release, proof, or publication home is created.

## Source and evidence references

- Supplied Pass 20 corpus, card `KFM-IDX-APP-008`, local source digest `sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`.
- Current repository `contracts/evidence/indicator_definition.md` at the authoring base.
- Draft GeographyVersion dependency in PR #2502 at pinned head `db29374a0fdb61058d26f7a5c554a13679a3c64f`.
- Current repository `docs/doctrine/directory-rules.md` and accepted ADR-0029.
- Prior county-year candidate gap record in PR #1398.

Private connected-source identifiers and copied private prose are intentionally excluded from this public artifact.

## Validation and rollback

Validation covers schema meta-validation, exact fixture replay, dependency-set consistency, deterministic identity, safe input parsing, no-network behavior, payload non-reflection, workflow parsing, generated-receipt byte binding, and adjacent GeographyVersion / IndicatorDefinition suites. Hosted exact-head results and human review remain pending until the stacked draft pull request exists.

Rollback is a focused revert of this additive packet. It creates no live source, observation, geography join, threshold, classification, evidence, policy, review, lifecycle, release, deployment, or public state.

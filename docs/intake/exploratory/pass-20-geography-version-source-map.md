<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-20-geography-version-source-map
title: Pass 20 GeographyVersion Source Map
type: exploratory-source-map
version: v0.1.0
status: complete-for-proposed-fixture-slice; human-review-pending
owners: OWNER_TBD - Geography steward; Contract steward; Evidence steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-adaptation; no-network
owning_root: docs/
responsibility: Record how Pass 20 KFM-IDX-APP-008 and the current IndicatorDefinition dependency were narrowed into one inactive fixture-only GeographyVersion packet.
truth_posture: CONFIRMED source/repository comparison / PROPOSED implementation packet / NEEDS VERIFICATION human review and hosted exact-head checks
related:
  - ../../../contracts/common/geography_version.md
  - ../../../contracts/evidence/indicator_definition.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-20, geography-version, county-year, crosswalk, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Pass 20 GeographyVersion Source Map

## Source statement

Pass 20 card `KFM-IDX-APP-008` proposes a future frontier-demography and economy product built as a versioned county-year panel. It names `FrontierDefinition`, `GeographyVersion`, versioned observations, crosswalks, uncertainty, release manifests, and rollback cards as necessary foundations. The card recommends starting with definitions and synthetic fixtures before public analytical claims.

The source is design evidence. It does not prove repository implementation, a geography dataset, source admission, boundary authority, analytic correctness, policy approval, release, or publication.

## Repository reconciliation

At authoring base `main@18b5bba4bf53edcd5b9ac61779a0cccade35d186`:

- the merged `IndicatorDefinition` contract requires geography-version discipline for derived indicators;
- bounded exact-path probes found no `GeographyVersion` contract, schema, fixture family, validator, or test at the checked common, evidence, data, or spatial candidate paths;
- pull-request searches found no exact `GeographyVersion` implementation;
- a prior agriculture county-year candidate dossier records geography versioning as an unresolved release-candidate requirement, but it does not implement the shared object; and
- the two open pull requests concern claim-scope assessment and an Explorer NDVI panel, so their changed responsibilities do not overlap this common contract slice.

Differently named or unindexed implementations remain possible; this packet therefore claims a bounded checked-path gap, not universal absence.

## Implemented boundary

The packet declares one geography key, source role, source-valid interval, publication/retrieval times, referenced boundary artifact, CRS, version-local feature identity, predecessor/crosswalk posture, representation role, evidence references, disclosure limits, and deterministic identity.

The validator:

- rejects inverted valid intervals and retrieval before publication;
- requires sorted unique digest-bound evidence references;
- prevents cross-version identity or crosswalk inference;
- requires a transform receipt for generalized geometry;
- checks predecessor/crosswalk coherence; and
- fixes all operational and publication authorities to false.

It does not read geometry, resolve any reference, verify a source, compare boundary features, execute a join, evaluate rights or sensitivity, classify a county, or change lifecycle state.

## Directory Rules basis

Accepted ADR-0029 and Directory Rules route shared semantic meaning to `contracts/common/`, paired machine shape to `schemas/contracts/v1/common/`, synthetic replay to `fixtures/contracts/v1/common/`, reusable checks to `tools/validators/`, test evidence to `tests/validators/`, orchestration to `.github/workflows/`, human reconciliation to `docs/intake/exploratory/`, and generated authoring accountability to `data/receipts/generated/`.

No new root or parallel schema, evidence, geography, policy, source, registry, release, proof, or publication home is created.

## Source and evidence references

- Supplied Pass 20 corpus, card `KFM-IDX-APP-008`, local source digest `sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`.
- Current repository `contracts/evidence/indicator_definition.md` at the authoring base.
- Current repository `docs/doctrine/directory-rules.md` and accepted ADR-0029.
- Prior county-year candidate gap record in PR #1398.

Private connected-source identifiers and copied private prose are intentionally excluded from this public artifact.

## Validation and rollback

Validation covers schema meta-validation, exact fixture replay, deterministic identity, safe input parsing, no-network behavior, payload non-reflection, workflow parsing, generated-receipt byte binding, and the adjacent IndicatorDefinition suite. Hosted exact-head results and human review remain pending until the draft pull request exists.

Rollback is a focused revert of this additive packet. It creates no live geography, source, evidence, crosswalk, policy, review, lifecycle, release, deployment, or public state.

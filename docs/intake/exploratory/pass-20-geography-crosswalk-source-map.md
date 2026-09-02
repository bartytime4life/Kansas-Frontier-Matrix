<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-20-geography-crosswalk-source-map
title: Pass 20 GeographyCrosswalk Source Map
type: exploratory-source-map
version: v0.1.0
status: complete-for-proposed-fixture-slice; human-review-pending
owners: OWNER_TBD - Geography steward; Crosswalk steward; Contract steward; Evidence steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-adaptation; no-network
owning_root: docs/
responsibility: Record how Pass 20 KFM-IDX-APP-008, the consolidated Frontier Matrix atlas, and merged GeographyVersion semantics were narrowed into one inactive fixture-only GeographyCrosswalk packet.
truth_posture: CONFIRMED source/repository comparison / PROPOSED implementation packet / NEEDS VERIFICATION human review and hosted exact-head checks
related:
  - ../../../contracts/crosswalks/geography_crosswalk.md
  - ../../../contracts/common/geography_version.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-20, geography-crosswalk, county-year, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Pass 20 GeographyCrosswalk Source Map

## Source statement

Pass 20 card `KFM-IDX-APP-008` proposes a versioned county-year frontier-demography/economy panel with geography versions, crosswalks, uncertainty, and reproducible joins. The consolidated Frontier Matrix atlas separately names `Crosswalk` as an owned object family and proposes GeographyVersion/Crosswalk tests. Both sources retain implementation as proposed and require evidence, time, source role, and release-state discipline.

The sources are design evidence. They do not prove a geography dataset, mapping row, cross-version identity, source admission, evidence closure, review, release, or publication.

## Repository reconciliation

At authoring base `main@463381703bcd6eada8eea05e95c4a88912ed4b02`:

- merged `GeographyVersion` semantics require a separately reviewed crosswalk before a different-version join;
- its validator explicitly records crosswalk references as unresolved and performs no crosswalk resolution;
- `contracts/crosswalks/` and `schemas/contracts/v1/crosswalks/` already host semantic and machine-shape crosswalk families, including the fixture-first taxonomy lineage profile;
- bounded exact-path, object-name, pull-request, and branch probes found no checked-path `GeographyCrosswalk` contract, schema, fixture family, validator, test, workflow, or same-purpose open work; and
- the two open pull requests concern a duplicate claim-scope assessment and an Explorer NDVI panel, with no crosswalk paths.

Differently named or unindexed implementations remain possible. This packet claims a bounded checked-path gap, not universal absence.

## Implemented boundary

The packet declares one direction-specific pair of digest-bound `GeographyVersion` references, a pinned method, digest-only feature identities, exact/split/merge/partial/unmapped relations, integer-millionth weights, evidence references, disclosure limits, and deterministic identity.

The validator checks ordering, uniqueness, relation shape, weight closure, merge groups, finite time, source/target separation, required disclosures, and stored identity. It does not read coordinates, compare geometries, resolve a reference, run an overlay or join, infer reverse mappings, or evaluate evidence, rights, sensitivity, policy, review, release, or public use.

## Directory Rules basis

Accepted ADR-0029 and current repository evidence route mapping meaning to `contracts/crosswalks/`, paired shape to `schemas/contracts/v1/crosswalks/`, synthetic replay to `fixtures/contracts/v1/crosswalks/`, reusable checks to `tools/validators/`, test evidence to `tests/validators/`, orchestration to `.github/workflows/`, human reconciliation to `docs/intake/exploratory/`, and generated authoring accountability to `data/receipts/generated/`.

No new root or parallel geography, crosswalk registry, schema, evidence, source, policy, release, proof, or publication home is created.

## Source and evidence references

- Supplied Pass 20 corpus, card `KFM-IDX-APP-008`, local source digest `sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`.
- Supplied consolidated Frontier Matrix atlas, visually reviewed domain/object-family pages, local digest `sha256:020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639`.
- Current repository `contracts/common/geography_version.md`, Directory Rules, and accepted ADR-0029.

Private connected-source identifiers and copied private prose are intentionally excluded from this public artifact.

## Validation and rollback

Validation covers schema meta-validation, exact fixture replay, relation/weight coherence, deterministic identity, safe input parsing, no-network behavior, payload non-reflection, workflow parsing, generated-receipt byte binding, and the adjacent GeographyVersion suite. Hosted exact-head results and human review remain pending until the draft pull request exists.

Rollback is a focused revert of this additive packet. It creates no live geography, source, evidence, crosswalk registry, policy, review, lifecycle, release, deployment, or public state.

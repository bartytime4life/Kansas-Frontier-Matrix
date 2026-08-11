<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-20-county-year-panel-source-map
title: Pass 20 CountyYearPanel Source Map
type: exploratory-source-map
version: v0.1.0
status: complete-for-proposed-fixture-slice; human-review-pending
owners: OWNER_TBD - Frontier Matrix steward; Data steward; Evidence steward; Contract steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-adaptation; no-network
owning_root: docs/
responsibility: Record how Pass 20 KFM-IDX-APP-008, the consolidated Frontier Matrix atlas, and merged repository definition seams were narrowed into one inactive fixture-only CountyYearPanel packet.
truth_posture: CONFIRMED source/repository comparison / PROPOSED implementation packet / NEEDS VERIFICATION human review and hosted exact-head checks
related:
  - ../../../contracts/data/county_year_panel.md
  - ../../../contracts/common/geography_version.md
  - ../../../contracts/evidence/frontier_definition.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-20, county-year-panel, frontier-matrix, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Pass 20 CountyYearPanel Source Map

## Source statement

Pass 20 card `KFM-IDX-APP-008` proposes a versioned county-year frontier-demography/economy product across population, economic, agriculture, and access observations. It requires explicit frontier definitions, geography versions, crosswalks, uncertainty, release and rollback discipline, and recommends definitions plus synthetic fixtures before source harvesting. The consolidated Frontier Matrix atlas confirms `County-Year Panel`, `GeographyVersion`, observation families, and `Crosswalk` as vocabulary while retaining implementation as proposed.

The sources are design evidence. They do not prove a county observation, join, frontier classification, fitness assessment, evidence closure, review, release, or publication.

## Repository reconciliation

At authoring base `main@463381703bcd6eada8eea05e95c4a88912ed4b02`:

- merged `GeographyVersion` semantics provide a pinned geography seam and forbid silent different-version joins;
- merged `FrontierDefinition` semantics provide an inactive, fixture-only definition seam without classification authority;
- existing indicator-definition and source-role contracts provide opaque typed-reference seams without loading source data;
- current responsibility layout routes derived data-product declarations through `contracts/data/` and matching versioned support roots;
- bounded exact-name, path, pull-request, branch, and open-work probes found no checked-path `CountyYearPanel` contract, schema, fixture family, validator, test, workflow, or same-purpose active work; and
- older pull-request material mentioning county-year agriculture remained documentation-only and explicitly blocked implementation, while current open work concerns a duplicate claim-scope assessment and a separate Explorer NDVI panel.

Differently named or unindexed implementations remain possible. This packet claims a bounded checked-path gap, not universal absence.

## Implemented boundary

The packet declares a synthetic county digest and year, pinned definition references, exactly four typed observation slots, source-role preservation, explicit availability and geography-alignment states, uncertainty and evidence references, deterministic derived panel state, required interpretation limits, and content-addressed identity.

The validator checks declaration shape, slot completeness and order, reference pairing, alignment posture, availability posture, summary derivation, disclosure limits, deterministic identity, and safe input parsing. It does not load an observation or source, calculate a value, aggregate records, resolve geography or crosswalks, evaluate uncertainty or evidence, apply frontier thresholds, classify a county, approve policy, promote, release, publish, or deploy.

## Directory Rules basis

Accepted ADR-0029 and current repository evidence route data-product meaning to `contracts/data/`, paired shape to `schemas/contracts/v1/data/`, synthetic replay to `fixtures/contracts/v1/data/`, reusable checks to `tools/validators/data/`, test evidence to `tests/data/`, orchestration to `.github/workflows/`, human reconciliation to `docs/intake/exploratory/`, and generated authoring accountability to `data/receipts/generated/`.

No new root or parallel data, source, evidence, geography, crosswalk, policy, release, proof, API, map, or publication home is created.

## Source and evidence references

- Supplied Pass 20 corpus, card `KFM-IDX-APP-008`, local source digest `sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`.
- Supplied consolidated Frontier Matrix atlas, visually reviewed object-family and application-card pages, local digest `sha256:020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639`.
- Current repository `GeographyVersion`, `FrontierDefinition`, indicator-definition, source-role, Directory Rules, and accepted ADR-0029 materials.

Private connected-source identifiers and copied private prose are intentionally excluded from this public artifact.

## Validation and rollback

Validation covers schema meta-validation, exact positive/negative fixture replay, availability and alignment branches, deterministic summary and identity, safe input parsing, no-network behavior, payload non-reflection, workflow parsing, generated-receipt byte binding, and adjacent GeographyVersion, FrontierDefinition, and IndicatorDefinition suites. Hosted exact-head results and human review remain pending until the draft pull request exists.

Rollback is a focused revert of this additive packet. It creates no live observation, source, evidence, geography, crosswalk, policy, review, lifecycle, release, deployment, or public state.

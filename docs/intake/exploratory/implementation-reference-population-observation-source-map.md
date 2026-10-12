<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/implementation-reference-population-observation-source-map
title: Implementation Reference PopulationObservation Source Map
type: source-reconciliation; exploratory-design-record
version: v0.1.0
status: confirmed-source-reconciliation; proposed-inactive-implementation; review-required
owners: OWNER_TBD - Intake steward; Population statistics steward; Evidence steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; population; county-year; no-network
owning_root: docs/
responsibility: Reconcile the supplied population-observation proposal with current repository authority and record the bounded implementation decision.
truth_posture: CONFIRMED cited source and checked-path gap / PROPOSED inactive profile / NEEDS VERIFICATION steward review and hosted exact-head execution
related:
  - ../../../contracts/evidence/population_observation.md
  - ../../../schemas/contracts/v1/evidence/population_observation.schema.json
  - ../../../fixtures/contracts/v1/evidence/population_observation/cases.json
  - ../../../tools/validators/evidence/validate_population_observation.py
  - ../../../tests/validators/evidence/test_validate_population_observation.py
  - ../../../contracts/common/geography_version.md
  - ../../../contracts/evidence/frontier_definition.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, source-map, population-observation, county-year, frontier, fixture-only]
notes:
  - "Private Drive identifiers, URLs, and copied private prose are excluded from this public reconciliation."
  - "The supplied implementation reference is design lineage, not proof of repository maturity or factual Kansas population values."
[/KFM_META_BLOCK_V2] -->

# PopulationObservation Source Map

## Goal and status

Implement the smallest definitions-first successor to the merged `GeographyVersion` and `FrontierDefinition` profiles: one inactive `PopulationObservation` declaration for synthetic Kansas county-year fixtures.

| Claim | Status | Evidence |
|---|---|---|
| The implementation reference names `PopulationObservation` as a county-year schema family with geography, year/vintage, value, source table, and uncertainty support. | `CONFIRMED` | Supplied *Kansas Frontier Matrix Implementation Reference*, PDF pages 6-7, SHA-256 `d948332b6c5bfcdd956cf6264f7bcb88d6881ac00ca8afc2534a02d288d4b3c2`. |
| Pass 20 recommends definitions and a synthetic county-year fixture before public analytical claims. | `CONFIRMED` | Supplied Pass 20 Part 2 combined atlas, `KFM-IDX-APP-008`, SHA-256 `57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`. |
| The connected architecture brief treats a county-year frontier classification as an inspectable claim whose evidence, withholding, policy, and correction posture must remain reconstructable. | `CONFIRMED` | Connected Drive architecture brief inspected during authoring; private file identifiers are not reproduced. |
| `PopulationObservation` already existed at the checked contract, schema, fixture, validator, test, or workflow paths on `main@463381703bcd6eada8eea05e95c4a88912ed4b02`. | `CONFIRMED FALSE` | Direct current-main path probes returned not found. |
| A matching pull request or branch already existed at authoring time. | `CONFIRMED FALSE` | Exact `PopulationObservation` PR search and `population-observation` branch search returned no matches. |
| The profile should be activated or treated as factual Kansas population data. | `DENY` | No live source, source admission, evidence resolution, rights/sensitivity decision, policy review, or release closure is part of this packet. |

## Repository reconciliation

Current repository authority already provides:

- accepted directory governance through ADR-0029;
- `GeographyVersion` for version-bounded geography declaration;
- `IndicatorDefinition` and `FrontierDefinition` for analytic and classification method declarations;
- deterministic RFC 8785 JCS plus SHA-256 identity support; and
- generated-receipt validation.

This packet reuses those boundaries. It does not create a `frontier/`, `population/`, `census/`, or `economy/` repository root and does not alter an existing domain lane.

## Selected slice

The selected candidate carries exactly one aggregate total-resident-population state:

- `OBSERVED`, including an explicit zero;
- `SUPPRESSED`, preserving source suppression; or
- `MISSING`, preserving a bounded missing reason.

It binds version-local county identity, calendar-year support, source observation/release/retrieval/correction time, optional reported uncertainty, source lineage, evidence references, interpretation limits, and fixed false authority flags.

## Deliberate exclusions

The packet excludes:

- real Kansas population values or source payloads;
- person, household, address, race, ethnicity, age, or other subgroup records;
- geometry, coordinates, crosswalk execution, or cross-version identity inference;
- imputation, normalization, indicator computation, frontier classification, or causal interpretation;
- source activation, evidence resolution, rights or sensitivity evaluation;
- policy, review, promotion, release, deployment, publication, and public-use authority.

Subgroup observations, broader geography levels, and live source adapters remain separate future decisions because they add privacy, semantic, source, and policy burdens not needed to prove this object seam.

## Directory Rules decision

| Axis | Value |
|---|---|
| `artifact_kind` | Semantic contract packet with paired schema, synthetic fixture matrix, validator, tests, CI, reconciliation, and generated receipt |
| `authority_owner` | Cross-domain evidence-bearing observation semantics |
| `scope_kind` | Object family / cross-domain seam |
| `exposure` | Internal, fixture-only |
| `mutability` | Versioned candidate |
| `rules` | `DIR-SIGNATURE-001`, `DIR-PLACE-001`, `DIR-PLACE-005`, `DIR-PLACE-008` |
| `outcome` | `PLACE` across existing responsibility roots |

Meaning belongs under `contracts/evidence/` because the object is a cross-domain support record for a future interpretive claim and no accepted Frontier domain lane exists. Machine shape, fixtures, executable validation, tests, orchestration, reconciliation, and authoring accountability remain in their established roots.

## Validation and next work

The focused suite must prove schema validity, exact positive/negative fixture polarity, observed-zero preservation, suppression/missingness separation, uncertainty closure, correction lineage, parser hardening, no-network behavior, non-reflection, deterministic identity, and generated-receipt hash replay.

A later `EconomicObservation` profile may proceed independently. A `MatrixCell` or frontier-classification result must remain blocked until required observation families, geography alignment, evidence, policy, review, release, and rollback semantics are separately closed.

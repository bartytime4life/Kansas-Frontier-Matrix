<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/implementation-reference-economic-observation-source-map
title: Implementation Reference EconomicObservation Source Map
type: source-reconciliation; exploratory-design-record
version: v0.1.0
status: confirmed-source-reconciliation; proposed-inactive-implementation; review-required
owners: OWNER_TBD - Intake steward; Economic statistics steward; Evidence steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; economy; county-year; no-network
owning_root: docs/
responsibility: Reconcile the supplied economic-observation proposal with current repository authority and record the bounded implementation decision.
truth_posture: CONFIRMED cited source and checked-path gap / PROPOSED inactive profile / NEEDS VERIFICATION steward review and hosted exact-head execution
related:
  - ../../../contracts/evidence/economic_observation.md
  - ../../../schemas/contracts/v1/evidence/economic_observation.schema.json
  - ../../../fixtures/contracts/v1/evidence/economic_observation/cases.json
  - ../../../tools/validators/evidence/validate_economic_observation.py
  - ../../../tests/validators/evidence/test_validate_economic_observation.py
  - ../../../contracts/common/geography_version.md
  - ../../../contracts/evidence/frontier_definition.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, source-map, economic-observation, county-year, frontier, suppression, fixture-only]
notes:
  - "Private Drive identifiers, URLs, and copied private prose are excluded from this public reconciliation."
  - "The supplied implementation reference is design lineage, not proof of repository maturity or factual Kansas economic values."
[/KFM_META_BLOCK_V2] -->

# EconomicObservation Source Map

## Goal and status

Implement one inactive `EconomicObservation` declaration as the next independent observation-family seam for a future county-year frontier panel.

| Claim | Status | Evidence |
|---|---|---|
| The implementation reference names `EconomicObservation` with employment, wage, industry, GDP/income, and suppression semantics and calls it essential to the missing economy lane. | `CONFIRMED` | Supplied *Kansas Frontier Matrix Implementation Reference*, PDF page 6, SHA-256 `d948332b6c5bfcdd956cf6264f7bcb88d6881ac00ca8afc2534a02d288d4b3c2`. |
| Pass 20 names economic observations as part of a versioned county-year panel that must start with definitions and synthetic fixtures. | `CONFIRMED` | Supplied Pass 20 Part 2 combined atlas, `KFM-IDX-APP-008`, SHA-256 `57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`. |
| The connected Full Atlas places Population, Economic, Agriculture, and Access observations inside a proposed Frontier Matrix synthesis lane while preserving adjacent domain truth. | `CONFIRMED` | Connected Drive Full Atlas inspected during authoring; private file identifiers are not reproduced. |
| `EconomicObservation` already existed at the checked contract, schema, fixture, validator, test, or workflow paths on `main@463381703bcd6eada8eea05e95c4a88912ed4b02`. | `CONFIRMED FALSE` | Direct current-main path probes returned not found. |
| A matching pull request or branch already existed at authoring time. | `CONFIRMED FALSE` | Exact `EconomicObservation` PR search and `economic-observation` branch search returned no matches. |
| The profile should be activated or treated as factual Kansas economic data. | `DENY` | No live source, source admission, evidence resolution, confidentiality decision, policy review, or release closure is part of this packet. |

## Repository reconciliation

Current repository authority already provides accepted directory governance, version-bounded geography declarations, analytic/classification method declarations, deterministic identity, and generated-receipt validation. No accepted Economy or Frontier domain lane was established in the checked evidence.

This packet therefore uses an existing cross-domain contract family and does not create an `economy/`, `frontier/`, `labor/`, or `industry/` repository root.

## Selected slice

The selected candidate carries one aggregate county-year economic state with:

- a version-local county identity;
- an annual reference period and separate release, retrieval, and correction time;
- employment, wage, income, GDP, or industry-output family semantics;
- explicit unit, current/constant-dollar basis, price year, and seasonal posture;
- optional digest-bound industry-classification reference without translation;
- `OBSERVED`, `SUPPRESSED`, and `MISSING` states;
- source, table, variable, evidence, suppression-method, and correction references; and
- fixed false authority flags.

## Deliberate exclusions

The packet excludes:

- real Kansas economic values or source payloads;
- employer, establishment, person, household, address, or transaction records;
- geometry, coordinates, industry crosswalk execution, or cross-version identity inference;
- inflation conversion, seasonal adjustment, aggregation, imputation, normalization, indicator computation, or frontier classification;
- source activation, evidence resolution, confidentiality adjudication, rights or sensitivity evaluation;
- policy, review, promotion, release, deployment, publication, and public-use authority.

Live economic-source selection, source-specific quality flags, industry translation, and inflation methods remain separate decisions.

## Directory Rules decision

| Axis | Value |
|---|---|
| `artifact_kind` | Semantic contract packet with paired schema, synthetic fixture matrix, validator, tests, CI, reconciliation, and generated receipt |
| `authority_owner` | Cross-domain evidence-bearing economic observation semantics |
| `scope_kind` | Object family / cross-domain seam |
| `exposure` | Internal, fixture-only |
| `mutability` | Versioned candidate |
| `rules` | `DIR-SIGNATURE-001`, `DIR-PLACE-001`, `DIR-PLACE-005`, `DIR-PLACE-008` |
| `outcome` | `PLACE` across existing responsibility roots |

Meaning belongs under `contracts/evidence/`; machine shape, fixtures, executable validation, tests, orchestration, reconciliation, and authoring accountability remain in their established roots. No parallel schema, contract, policy, source, evidence, release, or publication home is created.

## Validation and next work

The focused suite must prove schema validity, exact fixture polarity, annual-period closure, source-time ordering, observed/suppressed/missing separation, price-basis and unit coherence, industry binding, correction lineage, parser hardening, no-network behavior, non-reflection, deterministic identity, and generated-receipt hash replay.

The population and economic profiles remain independent. A future county-year `MatrixCell` must not collapse their source roles or proceed until the remaining observation families, geography alignment, evidence, policy, review, release, and rollback semantics are separately closed.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/economic-observation
title: EconomicObservation Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD - Economic statistics steward; Evidence steward; Geography steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; evidence; economy; county-year; aggregate; no-network
owning_root: contracts/
responsibility: Define one aggregate county-year economic observation without resolving geography or evidence, exposing suppressed business information, activating sources, classifying frontier status, or changing policy or release state.
truth_posture: CONFIRMED source and checked-path repository gap / PROPOSED inactive profile / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ./frontier_definition.md
  - ../common/geography_version.md
  - ../../schemas/contracts/v1/evidence/economic_observation.schema.json
  - ../../fixtures/contracts/v1/evidence/economic_observation/cases.json
  - ../../tools/validators/evidence/validate_economic_observation.py
  - ../../tests/validators/evidence/test_validate_economic_observation.py
  - ../../docs/intake/exploratory/implementation-reference-economic-observation-source-map.md
tags: [kfm, evidence, economy, observation, county-year, suppression, price-basis, industry, deterministic, fixture-only]
notes:
  - "Implements the EconomicObservation object family named by the KFM Implementation Reference and Pass 20 KFM-IDX-APP-008."
  - "A passing fixture proves declaration coherence only; it does not prove an economic value, geography, evidence, classification, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# EconomicObservation Candidate

> A deterministic, fixture-only declaration of one aggregate economic measure for one Kansas county and one calendar-year reference period.

## Purpose

The implementation reference identifies `EconomicObservation` as essential to the missing economy lane for a future county-year frontier panel. This profile fills only the observation-declaration seam.

It records:

- one digest-bound `GeographyVersion` reference and one version-local county feature key;
- a bounded annual reference period with distinct source release, retrieval, and correction time;
- one employment, wage, income, GDP, or industry-output measure;
- unit, price-basis, constant-dollar year, seasonal-adjustment, and industry-classification posture;
- source suppression and missingness without inventing a value or exposing suppressed detail;
- digest-bound source, dataset-version, table, variable, suppression-method, correction, and evidence references; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

The object contains no employer, establishment, person, household, address, coordinate, geometry, source payload, frontier result, policy decision, or released artifact.

## Finite observation states

| `result_state` | Value | Suppression status | Required posture |
|---|---:|---|---|
| `OBSERVED` | Required; zero is valid | `NOT_SUPPRESSED` | No missing or suppression reason |
| `SUPPRESSED` | `null` | `SUPPRESSED` | `CONFIDENTIALITY` or `RELIABILITY`; digest-bound suppression method |
| `MISSING` | `null` | `MISSING` | Bounded source-missing reason; no suppression method |

A suppressed record remains suppressed. The validator does not infer a value, convert it to zero, or permit an establishment-level detail payload.

## Measure semantics

| Family | Unit | Price basis | Seasonal posture |
|---|---|---|---|
| `EMPLOYMENT` | `PERSONS` | `NOT_APPLICABLE` | `ADJUSTED` or `NOT_ADJUSTED` |
| `TOTAL_WAGES`, `PERSONAL_INCOME`, `GDP`, `INDUSTRY_OUTPUT` | `USD` | `CURRENT_DOLLARS` or `CONSTANT_DOLLARS` | `NOT_APPLICABLE` |
| `AVERAGE_ANNUAL_WAGE` | `USD_PER_JOB` | `CURRENT_DOLLARS` or `CONSTANT_DOLLARS` | `NOT_APPLICABLE` |
| `PER_CAPITA_INCOME` | `USD_PER_PERSON` | `CURRENT_DOLLARS` or `CONSTANT_DOLLARS` | `NOT_APPLICABLE` |

`CONSTANT_DOLLARS` requires a `price_year`; other price bases prohibit it. A specific-industry observation requires a digest-bound classification reference and a source-native industry code. An all-industries observation prohibits both. The validator does not translate classifications or approve a crosswalk.

## Geography, evidence, and authority boundary

The county feature key is version-local and unresolved. A join against a different `GeographyVersion` requires a separately reviewed crosswalk. Source and evidence references remain opaque. Rights, sensitivity, confidentiality, statistical fitness, and source currentness are not evaluated.

Required interpretation limits are:

- `AGGREGATE_ONLY`;
- `NO_BUSINESS_OR_INDIVIDUAL_INFERENCE`;
- `NO_CAUSAL_CLAIM`;
- `NO_PUBLICATION_AUTHORITY`;
- `PRICE_BASIS_DECLARED`;
- `SOURCE_ROLE_PRESERVED`;
- `SUPPRESSION_PRESERVED`; and
- `VERSION_BOUND`.

## Deterministic identity

The validator removes only `observation_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash       = SHA-256(JCS(identity subject))
observation_id  = kfm:economic-observation:<first 24 digest hex>
```

Evidence and interpretation-limit arrays are unique and lexical. Period, source-time, state, price, industry, suppression, correction, order, stored-identity, or authority drift fails closed.

## Directory Rules basis

This is a cross-domain evidence-bearing observation candidate, not a new Economy or Frontier domain root. Meaning belongs under the existing `contracts/evidence/` family alongside `IndicatorDefinition` and `FrontierDefinition`; machine shape belongs under `schemas/contracts/v1/evidence/`; synthetic replay under `fixtures/contracts/v1/evidence/`; validation under `tools/validators/evidence/`; tests under `tests/validators/evidence/`; read-only orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and generated-work accountability under `data/receipts/generated/`.

These existing responsibility roots are governed by accepted ADR-0029. The packet creates no economy data store, source registry, geography resolver, classification translator, frontier runtime, public API, release lane, or publication path.

## Validation

```bash
python -m unittest -v tests.validators.evidence.test_validate_economic_observation
python tools/validators/evidence/validate_economic_observation.py --fixtures
```

## Non-effects and rollback

A passing fixture does not prove that a source, dataset version, county, table, variable, classification, evidence item, suppression decision, correction, or value exists or is admissible. It does not classify a county, evaluate policy, approve review, promote, release, authorize public use, or publish.

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the additive packet. No live source, observation, policy, lifecycle, deployment, release, or public state requires restoration.

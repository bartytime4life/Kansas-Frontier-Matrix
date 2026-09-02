<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/population-observation
title: PopulationObservation Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD - Population statistics steward; Evidence steward; Geography steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; evidence; population; county-year; aggregate; no-network
owning_root: contracts/
responsibility: Define one aggregate county-year population observation without resolving geography or evidence, inferring individuals, activating sources, classifying frontier status, or changing policy or release state.
truth_posture: CONFIRMED source and checked-path repository gap / PROPOSED inactive profile / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ./frontier_definition.md
  - ../common/geography_version.md
  - ../../schemas/contracts/v1/evidence/population_observation.schema.json
  - ../../fixtures/contracts/v1/evidence/population_observation/cases.json
  - ../../tools/validators/evidence/validate_population_observation.py
  - ../../tests/validators/evidence/test_validate_population_observation.py
  - ../../docs/intake/exploratory/implementation-reference-population-observation-source-map.md
tags: [kfm, evidence, population, observation, county-year, uncertainty, suppression, deterministic, fixture-only]
notes:
  - "Implements the PopulationObservation object family named by the KFM Implementation Reference and Pass 20 KFM-IDX-APP-008."
  - "A passing fixture proves declaration coherence only; it does not prove a census value, geography, evidence, rights decision, classification, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# PopulationObservation Candidate

> A deterministic, fixture-only declaration of one aggregate population count for one Kansas county and one calendar-year reference period.

## Purpose

The implementation reference names `PopulationObservation` as one of the object families needed before a county-year frontier panel can be assembled. The merged `GeographyVersion` and `FrontierDefinition` profiles establish version and definition boundaries, but neither may carry an observation value.

This profile records:

- one digest-bound `GeographyVersion` reference and one version-local county feature key;
- one calendar-year reference period and a distinct source observation date;
- an aggregate total-resident-population count, including an explicit observed-zero state;
- source suppression or missingness without inventing a value;
- reported margin-of-error or standard-error disclosure when provided;
- digest-bound source, dataset-version, table, variable, uncertainty-method, correction, and evidence references;
- source release, retrieval, and correction time without collapsing them; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

The profile contains no person, household, address, coordinate, geometry, subgroup row, live source payload, frontier result, policy decision, or released artifact.

## Finite observation states

| `result_state` | Value | Missing reason | Uncertainty |
|---|---:|---|---|
| `OBSERVED` | Required; zero is valid | `NOT_APPLICABLE` | `REPORTED` or `NOT_REPORTED` |
| `SUPPRESSED` | `null` | `SOURCE_SUPPRESSED` | `NOT_APPLICABLE` |
| `MISSING` | `null` | `SOURCE_MISSING`, `NOT_COLLECTED`, or `NOT_AVAILABLE` | `NOT_APPLICABLE` |

A suppressed or missing record remains an observation-status record, not a zero. The validator never converts `null` to zero and never imputes a count.

## Geography and time boundary

The observation is county-scoped and references `kfm.geography-version.fixture.v1` through a digest-bound reference. The county feature key is version-local; this profile does not resolve it, inspect geometry, or authorize cross-version identity. A future join against a different geography version requires a separately reviewed crosswalk.

`reference_year`, `observation_date`, source release, retrieval, and correction time are separate. The observation date must fall within the declared calendar year. Retrieval may not precede source release.

## Evidence and uncertainty boundary

Every source and evidence reference remains opaque and unresolved. A reported uncertainty requires its kind, value, confidence level, and method reference. `NOT_REPORTED` means only that the synthetic source declaration carries no uncertainty value; it is not a claim of exactness.

Required interpretation limits are:

- `AGGREGATE_ONLY`;
- `NO_CAUSAL_CLAIM`;
- `NO_INDIVIDUAL_INFERENCE`;
- `NO_PUBLICATION_AUTHORITY`;
- `SOURCE_ROLE_PRESERVED`; and
- `VERSION_BOUND`.

## Deterministic identity

The validator removes only `observation_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash       = SHA-256(JCS(identity subject))
observation_id  = kfm:population-observation:<first 24 digest hex>
```

Evidence and interpretation-limit arrays are unique and lexical. Time, state, uncertainty, correction, order, stored-identity, or authority drift fails closed.

## Directory Rules basis

This is a cross-domain evidence-bearing observation candidate, not a new Frontier, Census, or Economy domain root. Meaning therefore belongs under the existing `contracts/evidence/` family alongside `IndicatorDefinition` and `FrontierDefinition`; machine shape belongs under `schemas/contracts/v1/evidence/`; synthetic replay under `fixtures/contracts/v1/evidence/`; validation under `tools/validators/evidence/`; tests under `tests/validators/evidence/`; read-only orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and generated-work accountability under `data/receipts/generated/`.

These are existing responsibility roots governed by accepted ADR-0029. The packet creates no population data store, source registry, geography resolver, frontier runtime, public API, release lane, or publication path.

## Validation

```bash
python -m unittest -v tests.validators.evidence.test_validate_population_observation
python tools/validators/evidence/validate_population_observation.py --fixtures
```

## Non-effects and rollback

A passing fixture does not prove that a referenced source, dataset version, county, table, variable, EvidenceBundle, uncertainty method, correction, or value exists or is admissible. It does not classify a county, evaluate policy, approve review, promote, release, authorize public use, or publish.

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the additive packet. No live source, observation, policy, lifecycle, deployment, release, or public state requires restoration.

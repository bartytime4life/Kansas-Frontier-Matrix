<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/frontier-definition
title: FrontierDefinition Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD - Analytics steward; Evidence steward; Geography steward; Policy steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; evidence; analytics; frontier; county-year; no-network
owning_root: contracts/
responsibility: Define one immutable frontier-classification method declaration without embedding thresholds, reading observations, resolving references, classifying a county, or changing policy or release state.
truth_posture: CONFIRMED source and bounded repository gap / PROPOSED inactive definition / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ./indicator_definition.md
  - ../common/geography_version.md
  - ../../schemas/contracts/v1/evidence/frontier_definition.schema.json
  - ../../fixtures/contracts/v1/evidence/frontier_definition/cases.json
  - ../../tools/validators/evidence/validate_frontier_definition.py
  - ../../tests/validators/evidence/test_validate_frontier_definition.py
  - ../../docs/intake/exploratory/pass-20-frontier-definition-source-map.md
tags: [kfm, evidence, analytics, frontier-definition, county-year, deterministic, fixture-only]
notes:
  - "Implements the definitions-first artifact proposed by Pass 20 KFM-IDX-APP-008 on top of the current IndicatorDefinition contract and draft GeographyVersion profile."
  - "A passing definition declares criteria only; it does not resolve thresholds, compute indicators, join geography, classify a county, evaluate policy, review, release, or publish."
[/KFM_META_BLOCK_V2] -->

# FrontierDefinition Candidate

> A deterministic, fixture-only declaration of how a future county-year frontier classification would be bounded, referenced, and disclosed.

## Purpose

Pass 20 card `KFM-IDX-APP-008` recommends starting the frontier-demography and economy lane with definitions and synthetic fixtures before data harvesting or public analytical claims. This packet implements only the first object in that sequence.

A `FrontierDefinition` records:

- a stable key, version, label, description, inactive lifecycle, county unit, jurisdiction, and intended use;
- an explicit valid-time interval and calendar-year support requirements;
- a digest-bound `GeographyVersion` reference and digest-bound `IndicatorDefinition` references;
- sorted criteria that point to opaque, digest-bound threshold-policy material instead of carrying inline thresholds;
- fixed `FRONTIER`, `NOT_FRONTIER`, and `UNCLASSIFIED` result semantics without producing a result;
- fail-closed missing-data and unresolved-uncertainty behavior;
- evidence, assumption, uncertainty, and interpretation-limit references; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

The object contains no county identifier, observation, population value, economic value, agriculture value, access value, geometry, coordinate, executable formula, threshold number, score, classification output, source payload, or released artifact.

## Classification declaration

| Concern | Required posture |
|---|---|
| Combination | `ALL_CRITERIA` or `ANY_CRITERION` |
| Criterion inputs | Digest-bound `IndicatorDefinition` references declared in `support` |
| Thresholds | Digest-bound policy references; never inline values |
| Missing input | `ABSTAIN` |
| Unresolved uncertainty | `ABSTAIN` |
| Satisfied result | `FRONTIER` |
| Unsatisfied result | `NOT_FRONTIER` |
| Indeterminate result | `UNCLASSIFIED` |
| Execution | `NOT_EXECUTED`; fixture validation only |

Criterion keys and all reference arrays are lexical and unique. The set of criterion indicator references must exactly match `support.indicator_definition_refs`. This prevents unused or undeclared analytic dependencies from being hidden in the declaration.

## Geography and time boundary

The definition is county-scoped and requires one digest-bound `GeographyVersion` reference using the `kfm.geography-version.fixture.v1` profile. This validator treats the reference as opaque. It neither resolves geography nor authorizes an observation join. Different geography versions require a separately reviewed crosswalk.

The valid interval names when this definition is intended to apply. It is not an observation time, retrieval time, transaction-time record, or proof that any county-year data exist. A calendar-year result would still need observation valid time and geography-valid-time alignment.

## Evidence and authority boundary

A passing fixture proves only local declaration coherence and deterministic identity. It does not prove:

- any referenced geography, indicator, threshold policy, evidence item, assumption, or uncertainty method exists or is admissible;
- a threshold is appropriate, lawful, approved, or resolved;
- source roles, observations, joins, uncertainty, or missingness have been evaluated;
- any county or year is `FRONTIER`, `NOT_FRONTIER`, or `UNCLASSIFIED`; or
- policy, review, promotion, release, public use, publication, or deployment is authorized.

## Deterministic identity

The validator removes only `definition_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash    = SHA-256(JCS(identity subject))
definition_id = kfm:frontier-definition:<first 24 digest hex>
```

Order, duplicate, temporal, reference-set, stored-identity, or authority drift fails closed.

## Directory Rules basis

Frontier classification meaning belongs under `contracts/evidence/` because it declares how a derived interpretive claim would be supported and limited. Machine shape belongs under `schemas/contracts/v1/evidence/`; synthetic replay under `fixtures/contracts/v1/evidence/`; reusable validation under `tools/validators/evidence/`; executable evidence under `tests/validators/evidence/`; read-only orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. The packet creates no frontier domain root, data store, source registry, threshold-policy home, computation runtime, public API, release lane, or publication path.

## Validation

```bash
python -m unittest -v tests.validators.evidence.test_validate_frontier_definition
python tools/validators/evidence/validate_frontier_definition.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the additive packet. Because the profile is inactive and fixture-only, no source, observation, classification, policy, review, lifecycle, deployment, release, or public state requires restoration.

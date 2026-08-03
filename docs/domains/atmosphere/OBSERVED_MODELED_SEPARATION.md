<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/atmosphere/observed-modeled-separation
title: Atmosphere Observed-Modeled Separation Profile
type: domain-profile
version: v0.1.0
status: draft; bounded executable profile; no source or release activation
owners:
  - OWNER_TBD - Atmosphere domain steward
  - OWNER_TBD - Schema steward
  - OWNER_TBD - Validation steward
  - OWNER_TBD - Evidence steward
created: 2026-08-03
updated: 2026-08-03
policy_label: public; synthetic-fixtures; no-network; not-life-safety
related:
  - ../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../schemas/contracts/v1/domains/atmosphere/air_observation.schema.json
  - ../../../schemas/contracts/v1/domains/atmosphere/forecast_context.schema.json
  - ../../../fixtures/domains/atmosphere/observed_modeled_separation/
  - ../../../tools/validators/domains/atmosphere/validate_observed_modeled_separation.py
  - ../../../tests/domains/atmosphere/test_observed_modeled_separation.py
[/KFM_META_BLOCK_V2] -->

# Atmosphere Observed-Modeled Separation Profile

> A bounded, synthetic, no-network profile that prevents an `AirObservation`
> and a modeled `ForecastContext` from becoming substitutable records.

## Status and evidence boundary

| Claim | Status | Evidence |
|---|---|---|
| Atmosphere semantic contracts distinguish observed sensor values from model fields. | CONFIRMED | `contracts/domains/atmosphere/README.md`, `AirObservation.md`, and `ForecastContext.md` at base `c4629bd9adddd2e322663149c6f3bc23a5224140`. |
| The lowercase AirObservation and ForecastContext schemas were permissive empty-property scaffolds. | CONFIRMED | Prior blobs `45a674eabb2739f61666690284cb44c3543899b6` and `32afc3a2aca48297c595da2584535f62d62ab51f`. |
| CamelCase and lowercase schema files coexisted. | CONFIRMED | Four schema paths were read at the same base. |
| `New Ideas 6.pdf` proposes separate observed and modeled air objects with explicit provenance. | CONFIRMED design evidence | Pages 3-5; attachment SHA-256 `723ad2a705caec0ff42e8f5ba1d8f16e835901655469520c1ec655c775203af2`. |
| This profile proves current Kansas air quality, model accuracy, source admissibility, or release readiness. | DENIED | The slice uses synthetic fixtures and performs no live retrieval, scientific assessment, policy decision, or release transition. |

The attached idea packet is treated as design evidence, not repository truth. Its
claims that broader pipelines are active or enforced are not adopted by this
profile.

## Responsibility-root placement

Directory Rules place each artifact by responsibility:

| Responsibility | Path |
|---|---|
| Human boundary and use guidance | `docs/domains/atmosphere/` |
| Existing object meaning | `contracts/domains/atmosphere/` |
| Machine-checkable shape | `schemas/contracts/v1/domains/atmosphere/` |
| Synthetic inputs | `fixtures/domains/atmosphere/observed_modeled_separation/` |
| Deterministic checker | `tools/validators/domains/atmosphere/` |
| Executable conformance proof | `tests/domains/atmosphere/` |
| Generated-work process memory | `data/receipts/generated/` |

No new root, lifecycle phase, source registry, policy home, proof home, release
home, public API, UI, connector, or pipeline is created.

## Profile contract

### AirObservation

An `AirObservation` in this profile must carry:

- the `OBSERVED_SENSOR` knowledge character;
- `observed` or `low_cost_sensor` source role;
- source-resolution state and a station reference;
- separate observed and retrieval times;
- parameter, finite value, unit, and averaging period;
- QA, evidence-resolution, rights, sensitivity, and non-release posture;
- a not-for-life-safety marker and explicit limitations.

It rejects model-run identity, model identity, generated/valid model times, and
model derivation fields. A low-cost-sensor record additionally requires a
caveat and confidence statement.

### ForecastContext

A `ForecastContext` in this profile must carry:

- the `ATMOSPHERIC_MODEL_FIELD` knowledge character and `modeled` source role;
- source and model-run references plus model name and version;
- separate generated, valid, and optional validity-end times;
- governed spatial support, parameter, finite value, and unit;
- explicit `DERIVED_FROM` lineage;
- uncertainty state and statement;
- evidence-resolution, rights, sensitivity, and non-release posture;
- `not_an_observation` and not-for-life-safety limitations.

It rejects station-observation fields, observed-time claims, observation QA
state, and observed-value aliases.

## Schema identity and compatibility

Lowercase snake_case files are the profile's canonical machine shapes:

- `air_observation.schema.json`
- `forecast_context.schema.json`

The pre-existing CamelCase paths remain as one-way `$ref` mirrors so existing
contract links continue to resolve. A mirror must not evolve independently.
This resolves the local casing duplication without deleting a compatibility
path or creating parallel schema meaning.

Both canonical schemas are closed shapes, use object-type and
knowledge-character discriminators, exclude `released` posture, and bind their
fixture, validator, profile-document, and semantic-contract paths in `x-kfm`.
Chronological comparison between separate timestamp fields remains an explicit
validator boundary because portable Draft 2020-12 JSON Schema does not compare
the values of sibling fields.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The candidate conforms to the bounded profile and its source, evidence, QA/uncertainty, and rights states are resolved enough for this validator scope. |
| `ABSTAIN` | Shape is usable, but source, evidence, QA, rights, or model uncertainty remains unresolved. No claim is inferred. |
| `DENY` | The candidate collapses object families, omits required provenance or units, reverses time, asserts release, or otherwise violates the profile. |
| `ERROR` | Bounded JSON parsing or file handling could not complete. |

These outcomes do not approve policy, evidence truth, promotion, release, or
publication.

## Fixture matrix

The profile contains three positive controls:

- bound observation -> `PASS`;
- bound modeled context -> `PASS`;
- shape-valid observation with unresolved source/evidence/QA/rights -> `ABSTAIN`.

Twelve exact-negative fixtures cover:

- model knowledge or model-run identity on an observation;
- missing station or unit;
- observation knowledge on a modeled field;
- missing model-run identity, `DERIVED_FROM` lineage, or uncertainty;
- observed-time claims on a model field;
- reversed model time;
- false `released` posture for either object family.

All fixtures are synthetic, declare no network requirement, carry no sensitive
data, and do not represent current air quality or model output.

## Validation

Run the focused standard-library suite:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 KFM_NO_NETWORK=1 \
  python -m unittest -v \
  tests.domains.atmosphere.test_observed_modeled_separation
```

Run the validator directly:

```bash
python tools/validators/domains/atmosphere/validate_observed_modeled_separation.py \
  fixtures/domains/atmosphere/observed_modeled_separation/valid/air_observation_bound.json \
  fixtures/domains/atmosphere/observed_modeled_separation/valid/forecast_context_bound.json
```

The repository `domain-atmosphere` workflow invokes the focused suite and
checks one positive, one abstaining, and two exact-negative CLI cases. The
shared `schema-validation` workflow separately parses and meta-schema checks
every `*.schema.json` file.

## Non-goals

This slice does not:

- activate OpenAQ, CAMS, NOAA, EPA, or another source;
- add a connector, schedule, endpoint, credential, or live fetch;
- determine air-quality health significance or model skill;
- create an AQI, advisory, emergency-alert, or life-safety surface;
- resolve EvidenceRefs against live EvidenceBundles;
- create policy, source admission, catalog, proof, promotion, release, or publication state;
- add public API, Explorer, MapLibre, tile, graph, or AI behavior.

## Rollback

Before merge, close the draft pull request or abandon the feature branch. After
merge, use a focused revert of this profile's schemas, mirrors, fixtures,
validator, tests, workflow wiring, documentation, and generated receipt. Do not
delete the prior CamelCase paths or rewrite shared history. Reverting this slice
restores their prior permissive scaffold bytes but also restores the known
observed/model schema gap.

## Evidence basis

- `New Ideas 6.pdf`, pp. 3-5, Air Modeling & Atmospheric Integration - design evidence only.
- `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`, pp. 80-86 - object-character and negative-test design evidence.
- `Unified Implementation Architecture Build Manual.md`, Atmosphere and validation sections - doctrine-grounded architecture guidance.
- Current repository base `c4629bd9adddd2e322663149c6f3bc23a5224140` - implementation evidence for existing contracts, scaffolds, validators, fixtures, tests, and workflows.

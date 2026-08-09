<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/forecast-product/v1
title: ForecastProduct Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; no-public-authority
owning_root: contracts/
responsibility: Define a source-issued forecast without collapsing prediction into observation, classification, model truth, advisory action, release, or public guidance.
truth_posture: "CONFIRMED source/repository boundary; PROPOSED candidate semantics; NEEDS VERIFICATION steward review and operational adoption"
related:
  - ../../schemas/contracts/v1/common/forecast_product.schema.json
  - ../../fixtures/contracts/v1/common/forecast_product/
  - ../../tools/validators/validate_forecast_product.py
  - ../../tests/validators/test_validate_forecast_product.py
  - ./classification_release.md
  - ./condition_relation.md
  - ./temporal_authority_envelope.md
  - ../source/official_source_snapshot_candidate.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, common, forecast, prediction, uncertainty, method, source-role, deterministic, fixture-only, no-network]
notes:
  - "Implements the ForecastProduct family named by the briefing-to-system conditions framework."
  - "A PASS proves bounded local shape and invariants only; no live source, advisory, release, or public guidance is created."
[/KFM_META_BLOCK_V2] -->

# ForecastProduct

## Purpose

`ForecastProduct` is a release-neutral candidate for a source-issued prediction
over a declared geography, variable, issue time, valid interval, method, and
uncertainty posture.

It is deliberately not:

- an observed measurement;
- a classification release;
- a model output treated as factual truth;
- an advisory instruction;
- an EvidenceBundle;
- a release manifest;
- public guidance.

The conditions framework keeps forecasts, observations, classifications,
modeled surfaces, survey products, and aggregates separate. This contract
realizes only the forecast carrier.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.common.forecast-product.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Schema | `schemas/contracts/v1/common/forecast_product.schema.json` |
| Validator | `tools/validators/validate_forecast_product.py` |
| Source access | None |
| Evidence resolution | Not performed |
| Release state | Semantically fixed to `UNRELEASED` |
| Public use | Semantically fixed to `false` |
| Guidance authority | None |

## Source-role boundary

| Concept | Source role | Support type |
|---|---|---|
| Forecast product | `FORECAST` | `PREDICTION` |
| Classification release | `CLASSIFICATION` | `DERIVED_CLASSIFICATION` |
| Domain observation | Domain-native observation role | Direct or domain-native measurement support |
| Modeled surface | `MODEL` | `MODELED_ESTIMATE` |

A forecast candidate claiming observation, classification, or model source role
is denied. Prediction support cannot silently become direct measurement.

## Time

The profile keeps distinct:

- source data cutoff;
- issuance;
- valid start and end;
- retrieval;
- correction;
- supersession;
- source-native timezone.

The validator denies cutoff after issuance, validity before issuance, inverted
validity, issuance after retrieval, and incoherent correction or supersession.

## Method

Finite method kinds are:

- `MODEL` — model reference and version required;
- `EXPERT` — forecaster reference required and model context absent;
- `HYBRID` — model, version, and forecaster all required.

Every candidate also names the method, variable, unit, and optional ensemble or
scenario. Method context is part of the forecast's meaning, not incidental
metadata.

## Uncertainty

Supported uncertainty kinds are probability, range, ensemble spread, category
confidence, or `NOT_PROVIDED`. A provided uncertainty kind requires a value
reference. `NOT_PROVIDED` requires a null reference and `UNKNOWN` confidence.
The profile denies confidence that is stronger than the declared uncertainty
support.

## Space and lineage

Resolved geometry requires a governed geography reference and digest.
Unresolved geometry cannot carry resolved location or confidence. Finite
source-lineage states are `CURRENT`, `CORRECTED`, `SUPERSEDED`, and
`CONFLICTED`; conflict requires at least two references and unresolved-safe
geometry.

## Identity

`spec_hash` uses the repository RFC 8785 JCS plus SHA-256 package.
`forecast_product_id` is derived from the first 24 hexadecimal characters of
that hash. Equivalent semantic input replays to the same identity.

## Finite outcomes

- `PASS` — bounded candidate accepted;
- `DENY` — semantic or authority boundary violated;
- `ERROR` — unsafe input, unavailable dependency, or identity corruption.

Diagnostics expose stable code/path pairs and do not echo forecast values.

## Authority non-effects

All source, evidence, policy, promotion, release, and publication effects remain
false. A release reference, public-use claim, true effect, or guidance authority
is denied.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. The packet uses
`contracts/common/` for meaning, `schemas/contracts/v1/common/` for shape,
`fixtures/contracts/v1/common/` for synthetic inputs, `tools/validators/` for
execution, `tests/validators/` for behavior, `.github/workflows/` for read-only
CI, `docs/intake/exploratory/` for adaptation, and
`data/receipts/generated/` for authoring accountability.

No new root, source connector, observation authority, model store, policy home,
release home, public API, map layer, or advisory path is created.

## Non-effects

This profile does not fetch a forecast, activate a source, issue advice, resolve
evidence, evaluate policy, write lifecycle state, promote, release, publish,
render a map, or answer with AI.

## Compatibility and next seams

`ClassificationRelease` and domain observation profiles retain their own
published language. `ConditionRelation` may later relate released objects while
preserving role, scale, time, uncertainty, and no-causality constraints.

The next bounded conditions work is a source-role crosswalk test across
classification, observation, forecast, modeled surface, survey product, and
aggregate statistic. Public conditions projections remain held behind evidence,
policy, review, release, correction, and rollback closure.

## Rollback

Close the draft pull request or abandon the branch before merge. After an
authorized merge, revert the additive packet. No live source, advisory,
release, deployment, or public artifact requires restoration.

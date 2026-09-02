<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/modeled-surface/v1
title: ModeledSurface Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; no-public-authority
owning_root: contracts/
responsibility: Define a derived modeled surface without collapsing model output into observation, forecast, classification, survey, aggregate, field truth, release, or publication authority.
truth_posture: "CONFIRMED source/repository boundary; PROPOSED candidate semantics; NEEDS VERIFICATION steward review and operational adoption"
related:
  - ../../schemas/contracts/v1/common/modeled_surface.schema.json
  - ../../fixtures/contracts/v1/common/modeled_surface/
  - ../../tools/validators/validate_modeled_surface.py
  - ../../tests/validators/test_validate_modeled_surface.py
  - ./classification_release.md
  - ./condition_relation.md
  - ./forecast_product.md
  - ./temporal_authority_envelope.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, common, modeled-surface, model, support-limits, resolution, uncertainty, deterministic, fixture-only, no-network]
notes:
  - "Implements the ModeledSurface family named by the briefing-to-system conditions framework."
  - "A PASS proves only bounded local shape and anti-collapse invariants; it creates no factual, field, policy, release, or public authority."
[/KFM_META_BLOCK_V2] -->

# ModeledSurface

## Purpose

`ModeledSurface` is a release-neutral candidate for a derived model output over
a declared variable, geography, resolution, valid interval, model version,
training/support boundary, and uncertainty posture.

It is deliberately not:

- a station, sensor, sample, or field observation;
- a source-issued forecast or classification release;
- a survey product;
- an aggregate statistic;
- field, parcel, or operator truth;
- an EvidenceBundle, policy decision, release manifest, or public map.

The briefing conditions framework keeps modeled surfaces distinct from
observations, forecasts, classifications, surveys, and aggregates. A source
example such as SoilGrids or a reviewed interpolation supplies design pressure,
not source admission or a factual dataset claim.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.common.modeled-surface.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Source role | Exactly `MODEL` |
| Support type | Exactly `MODELED_ESTIMATE` |
| Evidence resolution | Not performed |
| Release state | Semantically fixed to `UNRELEASED` |
| Public and field use | Semantically fixed to `false` |

A validator `PASS` means only that the synthetic candidate is internally
coherent for this profile. References remain unresolved and untrusted.

## Required boundaries

### Model and support

The candidate binds model identity and version, method, parameters, training
dataset references, training support summary, training extent and time, output
variable, unit, and extrapolation state. Missing support context is denied.

`INSIDE_SUPPORT`, `PARTIAL_EXTRAPOLATION`, `OUTSIDE_SUPPORT`, and `UNKNOWN`
remain explicit. Outside or unknown support cannot carry `CONFIRMED` or `HIGH`
uncertainty confidence.

### Space, time, and resolution

The profile preserves training-data cutoff, model-run time, modeled valid time,
retrieval time, correction/supersession time, geography, geometry role, CRS,
and positive spatial resolution. A grid without resolution or a model run after
retrieval is denied. Retrospective validity may predate the model run.

### Uncertainty and lineage

Uncertainty is a referenced standard error, interval, ensemble spread,
validation metric, or explicit `NOT_PROVIDED`. Source lineage remains one of
`CURRENT`, `CORRECTED`, `SUPERSEDED`, or `CONFLICTED`; history is never erased.

### Derived-only posture

`derived_only` is always `true`; `field_truth_allowed`, `public_use_allowed`,
and every source/evidence/policy/promotion/release/publication effect are always
`false`. Model integrity cannot silently become factual support or publication
authority.

## Deterministic identity and outcomes

The repository RFC 8785 JCS plus SHA-256 helper computes `spec_hash` over the
candidate with its identity fields removed. `modeled_surface_id` derives from
the first 24 digest hex characters.

Finite validator outcomes are `PASS`, `DENY`, and `ERROR`. Diagnostics expose
only stable code/path pairs and never echo modeled values or source payloads.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. Meaning, machine shape,
synthetic cases, executable validation, behavioral proof, read-only CI, source
adaptation, and authoring accountability remain under `contracts/`, `schemas/`,
`fixtures/`, `tools/`, `tests/`, `.github/`, `docs/intake/`, and
`data/receipts/generated/` respectively. No model store, source registry,
domain root, evidence home, policy home, release home, or publication path is
created.

## Non-effects and rollback

This profile performs no live fetch, training, inference, interpolation,
statistics, geometry processing, evidence resolution, policy/review action,
lifecycle write, promotion, release, deployment, mapping, or publication.

Before merge, close the draft PR or abandon its branch. After an authorized
merge, revert the additive packet. No live or public state requires restoration.

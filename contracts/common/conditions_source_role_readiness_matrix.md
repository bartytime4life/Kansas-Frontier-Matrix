<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/conditions-source-role-readiness-matrix/v1
title: Conditions Source-Role Readiness Matrix Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; no-public-authority
owning_root: contracts/
responsibility: Reconcile conditions-lane source roles against selected repository profiles without creating a shared observation authority or treating unbound roles as implemented.
truth_posture: "CONFIRMED repository profile inventory; PROPOSED compatibility matrix; NEEDS VERIFICATION steward review and future profile selection"
related:
  - ../../schemas/contracts/v1/common/conditions_source_role_readiness_matrix.schema.json
  - ../../fixtures/contracts/v1/common/conditions_source_role_readiness_matrix/
  - ../../tools/validators/validate_conditions_source_role_readiness_matrix.py
  - ../../tests/cross_domain/test_conditions_source_role_readiness_matrix.py
  - ./classification_release.md
  - ./forecast_product.md
  - ./condition_relation.md
  - ../domains/soil/domain_observation.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, common, conditions, source-role, readiness, cross-domain, fixture-only, no-network]
notes:
  - "Implements the conditions source-role crosswalk identified by the briefing-to-system architecture after the classification, observation, forecast, and relation foundations existed."
  - "The matrix references the domain-owned Soil observation profile; it does not create a competing shared ObservationRecord contract."
[/KFM_META_BLOCK_V2] -->

# Conditions Source-Role Readiness Matrix

## Purpose

`ConditionsSourceRoleReadinessMatrix` records which conditions-lane roles have
an explicitly selected repository profile and which remain held. It keeps
observation, classification, forecast, model, survey, and aggregate roles
distinct while avoiding a new common observation authority.

The first matrix binds three existing fixture-only profiles:

| Conditions role | Selected repository profile | Common role/support |
|---|---|---|
| Observation | Soil `DomainObservation` Mesonet-style fixture | `OBSERVATION` / `DIRECT_MEASUREMENT` |
| Classification | `ClassificationRelease` | `CLASSIFICATION` / `DERIVED_CLASSIFICATION` |
| Forecast | `ForecastProduct` | `FORECAST` / `PREDICTION` |

Model, survey, and aggregate remain `HOLD`. The repository contains related
domain objects, but this matrix does not silently choose one as the shared
interoperability profile.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.common.conditions-source-role-readiness-matrix.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Expected current outcome | `PARTIAL_READY` |
| Source access | None |
| Evidence resolution | None |
| Policy or review execution | None |
| Lifecycle, release, or publication writes | None |

A validator `PASS` proves only that the local matrix is internally coherent and
that selected repository paths exist. The packet's focused cross-domain tests
separately replay the three bound fixture profiles through their own validators.
Neither result accepts the matrix, activates a source, establishes scientific
compatibility, or authorizes a public product.

## Readiness semantics

Each of the six required roles appears exactly once in canonical role order.

- `BOUND` requires an existing semantic contract, schema, validator, and
  fixture path plus native and common source-role/support mappings.
- `HOLD` requires all binding paths and native mappings to remain null and at
  least one explicit reason code.
- Any held role makes the matrix `PARTIAL_READY`.
- `FULLY_READY` is permitted by the shape for a later version of the same
  profile, but only when every role is bound and separately validated.

The validator pins the intended common pairs:

| Role | Intended common support |
|---|---|
| `AGGREGATE` | `AGGREGATE_STATISTIC` |
| `CLASSIFICATION` | `DERIVED_CLASSIFICATION` |
| `FORECAST` | `PREDICTION` |
| `MODEL` | `MODELED_ESTIMATE` |
| `OBSERVATION` | `DIRECT_MEASUREMENT` |
| `SURVEY` | `SURVEY_PRODUCT` |

## Anti-collapse rules

1. A station observation cannot satisfy a classification, forecast, model,
   survey, or aggregate binding.
2. A classification release cannot claim direct measurement.
3. A forecast cannot claim observation or classification support.
4. A related domain object is not a selected interoperability profile until
   its exact contract, schema, validator, and fixtures are named and pass.
5. A `HOLD` cannot be hidden by the readiness of another role.
6. `ConditionRelation` may relate typed endpoints but does not replace any
   endpoint profile.

## Deterministic identity

`spec_hash` uses the repository RFC 8785 JCS plus SHA-256 implementation.
`matrix_id` is derived from the first 24 hexadecimal characters of that hash.
The identity subject excludes only `matrix_id` and `spec_hash`.

## Finite outcomes

- `PASS` - local matrix shape, role mapping, path presence, and fixture
  compatibility are coherent;
- `DENY` - a role is duplicated, collapsed, overclaimed, or bound without its
  dependency set;
- `ERROR` - input safety, schema availability, hashing, or identity failed.

Diagnostics contain stable code/path pairs and never echo source values.

## Directory Rules basis

ADR-0029 adopts Directory Governance Standard v2. The matrix meaning belongs
under `contracts/common/`; its machine shape under
`schemas/contracts/v1/common/`; synthetic cases under `fixtures/`; repository
validation under `tools/validators/`; cross-domain proof under
`tests/cross_domain/`; orchestration under `.github/workflows/`; source
reconciliation under `docs/intake/exploratory/`; and authoring provenance under
`data/receipts/generated/`.

The responsibility signature is one common semantic contract, no lifecycle
stage, repository-tool execution, cross-domain scope, internal exposure, and
versioned Git retention. No new root, domain, source, schema home, policy home,
observation authority, release object, or public surface is created.

## Non-effects

This profile does not fetch USDM, Mesonet, NWS, or another source; activate a
source; resolve evidence; evaluate scientific fitness, policy, or review;
create an observation, classification, forecast, relation, map, API response,
dashboard, or AI answer; write lifecycle state; promote; release; or publish.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, revert this additive packet. Existing domain and common
profiles remain unchanged, and no external or public state requires cleanup.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/condition-relation/v1
title: Condition Relation Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-07
policy_label: public
related:
  - ../../schemas/contracts/v1/common/condition_relation.schema.json
  - ../../tools/validators/validate_condition_relation.py
  - ../../fixtures/contracts/v1/common/condition_relation/
  - ../../tests/validators/test_validate_condition_relation.py
  - ./temporal_authority_envelope.md
tags: [kfm, common, condition, relation, source-role, scale, temporal, contextual]
notes:
  - "ConditionRelation links released or candidate references without collapsing observations, classifications, forecasts, advisories, models, or context into one truth type."
  - "The contract records contextual relation support only; causal requests are denied by design."
[/KFM_META_BLOCK_V2] -->

# Condition Relation

## Purpose

`ConditionRelation` is a common, cross-domain seam for recording a bounded contextual relation between two typed condition-bearing subjects. It supports the briefing-to-system architecture's requirement to connect observations, classifications, forecasts, advisories, models, and contextual records while preserving each source role, support type, spatial scale, and valid-time window.

The relation is deliberately narrower than a domain observation, forecast, classification, or advisory contract. It references those objects; it does not replace them.

## Anti-collapse rules

1. Every endpoint keeps an explicit `source_role` and the corresponding `support_type`.
2. `OBSERVATION` is never represented as `FORECAST`; `CLASSIFICATION` is never represented as direct measurement.
3. Cross-scale relations require an explicit weighting method or return `ABSTAIN`.
4. Endpoint evidence must be carried into the relation assessment.
5. Spatial and temporal uncertainty remain explicit. Unknown scale, time, or relation state does not silently clear.
6. A causal request is recorded as a denied request. `assessment.causal_claim` is always `false`.
7. A valid relation is not evidence closure, policy approval, release authorization, or publication authority.

## Source-role vocabulary

| Source role | Required support type |
|---|---|
| `OBSERVATION` | `DIRECT_MEASUREMENT` |
| `CLASSIFICATION` | `DERIVED_CLASSIFICATION` |
| `FORECAST` | `PREDICTION` |
| `ADVISORY` | `REGULATORY_STATUS` |
| `MODEL` | `MODELED_ESTIMATE` |
| `CONTEXT` | `CONTEXT_ONLY` |

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `ANSWER` | A contextual relation is supported with resolved space, time, scale, weighting, and evidence. |
| `ABSTAIN` | Space, time, scale compatibility, or required weighting is unresolved or incompatible. |
| `DENY` | The requested relation would assert causality or violate a source-role/sensitivity boundary. |
| `ERROR` | The local relation operation could not complete. |

`ANSWER` is not a causal statement. It means only that the explicitly named contextual relation is supported for the stated scopes.

## Scale and weighting

When endpoint scales differ, `scale_compatibility` cannot be `COMPATIBLE`. It must be `REQUIRES_WEIGHTING`, `INCOMPATIBLE`, or `UNKNOWN`.

A `REQUIRES_WEIGHTING` relation must name one of:

- `AREA_WEIGHTED`
- `DISTANCE_WEIGHTED`
- `STATION_ASSIGNMENT`

The validator does not execute spatial weighting. It only verifies that a reviewed relation packet makes the requirement explicit.

## Deterministic identity

The canonical projection removes `relation_id` and `spec_hash`, serializes the remaining packet as sorted compact UTF-8 JSON with non-finite values denied, and computes SHA-256.

- `spec_hash = sha256(canonical_projection)`
- `relation_id = condition-relation:<first-24-hex-of-spec_hash>`

Arrays used as sets are sorted and unique. Equal semantic inputs replay to equal identity.

## Validation boundary

The validator is deterministic and no-network. It checks bounded JSON safety, schema conformance, role-to-support mapping, time-window ordering, scale/weighting compatibility, evidence closure, finite outcome semantics, deterministic identity, and governance flags.

It does not fetch a source, calculate a spatial overlay, evaluate a model, infer causality, resolve policy, mutate lifecycle state, promote, release, deploy, or publish.

## Rollback

Rollback is removal of this additive contract/schema/validator/fixture/test package. Domain contracts and existing releases are unchanged because this slice creates no data instance and authorizes no public exposure.

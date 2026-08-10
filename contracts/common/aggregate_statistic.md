<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/aggregate-statistic/v1
title: AggregateStatistic Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; no-public-authority
owning_root: contracts/
responsibility: Define an aggregate statistic with explicit geography, weighting, denominator, missing-data treatment, and source release without collapsing it into observation, model, classification, exact-local truth, release, or publication authority.
truth_posture: "CONFIRMED source/repository boundary; PROPOSED candidate semantics; NEEDS VERIFICATION steward review and operational adoption"
related:
  - ../../schemas/contracts/v1/common/aggregate_statistic.schema.json
  - ../../fixtures/contracts/v1/common/aggregate_statistic/
  - ../../tools/validators/validate_aggregate_statistic.py
  - ../../tests/validators/test_validate_aggregate_statistic.py
  - ./classification_release.md
  - ./condition_relation.md
  - ./forecast_product.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, common, aggregate-statistic, geography, weighting, denominator, missing-data, source-release, deterministic, fixture-only, no-network]
notes:
  - "Implements the AggregateStatistic family named by the briefing-to-system conditions framework."
  - "A PASS proves only bounded local shape and anti-collapse invariants; it creates no source, statistical, policy, release, or public authority."
[/KFM_META_BLOCK_V2] -->

# AggregateStatistic

## Purpose

`AggregateStatistic` is a release-neutral candidate for a source-issued or
source-derived summary over an explicit aggregation geography, valid time,
method, weighting rule, numerator/denominator posture, missing-data treatment,
and source release.

It is deliberately not:

- an individual observation or field/operator record;
- a modeled surface, forecast, classification, or survey product;
- exact local geometry or parcel truth;
- proof that an aggregation method is scientifically fit;
- an EvidenceBundle, policy decision, KFM release, or public claim.

The briefing conditions framework uses a statewide percentage as an example
and explicitly forbids treating it as exact local condition. The example is
design pressure only; this packet contains synthetic references and no values.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.common.aggregate-statistic.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Source role | Exactly `AGGREGATE` |
| Support type | Exactly `AGGREGATE_STATISTIC` |
| Evidence resolution | Not performed |
| Release state | Semantically fixed to `UNRELEASED` |
| Local/public use | Semantically fixed to `false` |

## Required boundaries

### Geography and scale

Every candidate declares the aggregation geography and level. Resolved
geography carries a digest; unresolved geography cannot carry resolved
location evidence. `local_truth_allowed` and `exact_local_geometry_allowed`
are always false.

### Computation context

The packet binds a variable, value reference, unit, aggregation method,
weighting kind and reference, numerator/denominator kind and references,
method reference, source-release reference, and missing-data treatment.

Percentages and rates require numerator and denominator references. Weighted
methods require a weighting reference. A declared denominator cannot be
omitted, and missing-data treatment must remain bound to an inspectable
declaration. The validator checks declaration closure only; it does not
recompute a statistic or endorse a method.

### Time, uncertainty, and lineage

Source-data cutoff, source release, validity, retrieval, correction, and
supersession remain distinct. Uncertainty is referenced or explicitly marked
`NOT_PROVIDED`. Source lineage stays `CURRENT`, `CORRECTED`, `SUPERSEDED`, or
`CONFLICTED`; old versions remain addressable.

### Authority non-effects

`derived_only` is true. Local truth, exact-local geometry, public use, source
activation, evidence resolution, policy evaluation, promotion, release, and
publication are false. A source's release is not a KFM release.

## Deterministic identity and outcomes

The repository RFC 8785 JCS plus SHA-256 helper computes `spec_hash` after
removing identity fields. `aggregate_statistic_id` derives from the first 24
digest hex characters. Outcomes are `PASS`, `DENY`, and `ERROR`; diagnostics
contain stable code/path pairs and do not echo values.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. Meaning, shape, cases,
validation, tests, read-only CI, source adaptation, and authoring accountability
remain in their established responsibility roots. No statistical store, source
registry, data lane, evidence home, policy home, release home, or public path is
created.

## Non-effects and rollback

This profile performs no live fetch, aggregation, weighting, imputation,
geospatial calculation, evidence resolution, policy/review action, lifecycle
write, promotion, release, mapping, AI answer, or publication.

Before merge, close the draft PR or abandon its branch. After an authorized
merge, revert the additive packet. No live or public state requires restoration.

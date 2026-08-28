# GovernanceHealthProjection

Status: PROPOSED_INACTIVE  
Profile: `kfm.governance.health-projection.v1`

`GovernanceHealthProjection` is a deterministic, read-only projection of governance-health measurements from normalized references to existing receipt, manifest, decision, validation, and drift record families.

It is not a metric store, policy engine, release gate, health authority, or publication decision. It reports observed counts and ratios without applying target thresholds.

## Initial indicator subset

The first fixture-only profile computes eight indicators already named by the KFM Indicator Catalog:

1. `evidence_ref_resolution_rate`
2. `cite_or_abstain_compliance`
3. `release_with_rollback_rate`
4. `derivative_invalidation_coverage`
5. `sensitive_lane_fail_closed_rate`
6. `ai_receipt_presence_rate`
7. `adr_completeness`
8. `open_drift_count`

`max_open_drift_age_days` is emitted as supporting context, not a separate health judgment.

## Coverage state

- `COMPLETE`: all eight indicator families have at least one applicable input observation.
- `PARTIAL`: at least one but not all indicator families have applicable inputs.
- `EMPTY`: no applicable observations were supplied.
- `ERROR`: malformed, non-canonical, internally inconsistent, or authority-overreaching input/output.

## Schema closure

Before returning a projection, the compiler validates the complete emitted object against the Draft 2020-12 schema at `schemas/contracts/v1/governance/governance_health_projection.schema.json`. An unavailable or invalid schema, or a nonconforming generated object, fails closed without returning a partial projection. The command-line surface reports the existing finite `ERROR` / `INVALID_INPUT` outcome; library callers receive `ValueError`.

Schema conformance proves only the bounded machine shape. It does not make a projection authoritative, healthy, compliant, release-ready, or publishable.

## Non-authority boundary

The projection does not declare `GREEN`, `HEALTHY`, `SAFE`, `RELEASE_READY`, or similar conclusions. Dashboard thresholds remain documentation/policy concerns and require separate review. A ratio of `1.0` is only a measurement over the bounded supplied observations.

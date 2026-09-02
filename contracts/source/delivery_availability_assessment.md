<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/delivery-availability-assessment
title: Delivery Availability Assessment Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Source steward · Temporal steward · Contract steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: public; source; delivery; availability; freshness; no-network
owning_root: contracts/
responsibility: Define a bounded source-product assessment that keeps cadence, delivery latency, availability, retrieval, freshness, staleness, supersession, and evidenced outage clocks separate without probing a source or changing source expectations.
truth_posture: CONFIRMED synthetic validator behavior / PROPOSED inactive source profile / NEEDS VERIFICATION steward adoption, product-specific expectations, and hosted exact-head execution
related:
  - ./source_descriptor.md
  - ./source_health_assessment.md
  - ./source_availability_watchlist.md
  - ./source_polling_checkpoint.md
  - ../../schemas/contracts/v1/source/delivery_availability_assessment.schema.json
  - ../../fixtures/contracts/v1/source/delivery_availability_assessment/cases.json
  - ../../tools/validators/source/validate_delivery_availability_assessment.py
  - ../../tests/validators/test_validate_delivery_availability_assessment.py
  - ../../docs/intake/exploratory/delivery-availability-assessment-source-map.md
tags: [kfm, source, cadence, delivery-latency, availability, freshness, staleness, fixture-only]
notes:
  - "Implements the bounded KFM-TRIAD-049 and KFM-CAND-0147 gap from the Full Atlas."
  - "Every duration and timestamp in the fixtures is synthetic; none is an adopted source schedule, service-level objective, freshness rule, or outage policy."
[/KFM_META_BLOCK_V2] -->

# Delivery Availability Assessment Candidate

> A deterministic, fixture-only profile for distinguishing expected product lag from true lateness, staleness, missing delivery, supersession, and an evidenced source outage. It does not poll a source, change a descriptor, or authorize downstream use.

## Purpose

Observation cadence, product cadence, generation time, delivery window, actual availability, retrieval, validation, release, freshness, and staleness answer different questions. Collapsing them into a single `updated_at` field can mislabel a legitimately delayed product as stale or let an old product appear current merely because it was retrieved recently.

`DeliveryAvailabilityAssessment` binds one versioned synthetic `DeliveryExpectation`, one `AvailabilityObservation`, one derived decision, and one review-only learned-latency observation. Product-specific facts must be verified and placed in a separately governed source descriptor or expectation profile before activation.

## Object surface

The assessment records:

- source identity, exact descriptor reference, descriptor version, and assessment time;
- observation and product cadence as distinct durations;
- minimum and maximum delivery latency as a versioned expected window;
- separate freshness and stale thresholds;
- a tolerance-profile reference, optional calendar-exception profile, and outage-exception posture;
- observed, generated, expected-available, actually available, retrieved, validated, and optional released times;
- source revision, superseding revision, retrieval result, and optional outage evidence; and
- a mechanically derived state, freshness state, observed delivery latency, and deterministic identity.

The expected-availability bounds must equal generation time plus the declared minimum and maximum latency. The validator never learns or guesses a replacement bound.

## Finite states

| State | Validator result | Meaning |
|---|---|---|
| `ON_TIME` | `PASS` | A synthetic product became available within its declared delivery window. |
| `EXPECTED_LAG` | `PASS` | The product is not yet available, but the declared window remains open. |
| `LATE` | `PASS` | The product arrived after the delivery window but before the stale threshold. Review remains required. |
| `STALE` | `ABSTAIN` | The stale threshold elapsed; consequential use remains on hold. |
| `MISSING` | `ABSTAIN` | The delivery window closed without an available product and without an evidenced outage. |
| `SUPERSEDED` | `ABSTAIN` | A later source revision explicitly supersedes this revision. |
| `SOURCE_OUTAGE` | `ABSTAIN` | A failed retrieval is paired with explicit synthetic outage evidence and an allowed exception posture. |
| malformed or contradictory packet | `DENY` | Shape, identity, time order, retrieval state, expected-window, learned-latency, decision, or authority invariants failed. |
| `ERROR` or unreadable input | `ERROR` | The assessment or bounded validator could not complete safely. |

`PASS` proves local consistency only. Every coherent packet fixes `review_required=true` and `policy_change_candidate=false`.

## Anti-collapse and learning rules

1. Retrieval time never substitutes for observation, generation, or availability time.
2. Expected lag is not late; late is not necessarily stale; missing is not an outage without evidence.
3. A stale threshold is strictly later than the freshness window.
4. Supersession preserves both revision identities and never deletes history.
5. Observed delivery latency is recorded only when actual availability is known.
6. A learned latency is marked `REVIEW_REQUIRED`; it cannot mutate the expectation or authorize an update.
7. Synthetic durations are validator examples, not source facts, scheduler constants, or policy.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete candidate after removing only `assessment_id` and `spec_hash`.

```text
spec_hash      = SHA-256(JCS(identity subject))
assessment_id  = kfm:delivery-availability:<first 24 digest hex>
```

Descriptor and expectation versions, every clock, revision and outage reference, derived outputs, and fixed governance flags all participate in identity.

## Existing-family boundary

- `SourceDescriptor` remains the source identity, role, rights, sensitivity, cadence, and activation surface.
- `SourceHealthAssessment` remains the bounded probe/freshness-health result.
- `SourceAvailabilityWatchlist` remains the health-plus-materiality review projection.
- `SourcePollingCheckpoint` remains conditional-request state.

This profile owns only the missing product-delivery clock reconciliation. It replaces none of those families.

## Directory Rules basis

Source semantics belong under `contracts/source/`; machine shape under `schemas/contracts/v1/source/`; synthetic cases under `fixtures/contracts/v1/source/`; reusable validation under `tools/validators/source/`; executable evidence under `tests/validators/`; orchestration under `.github/workflows/`; exploratory adaptation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`. The packet creates no new root or parallel source, policy, evidence, receipt, proof, release, or publication authority.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_delivery_availability_assessment
python tools/validators/source/validate_delivery_availability_assessment.py --fixtures
```

## Rollback

Before merge, close the draft pull request and remove its branch. After an authorized merge, revert this additive contract/schema/fixture/validator/test/workflow/source-map/receipt packet. No live source, descriptor, scheduler, stored product, policy, release, cache, deployment, or publication requires operational rollback.

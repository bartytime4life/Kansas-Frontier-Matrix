# Seasonal Streamflow Tail-Event Assessment Contract

**Status:** PROPOSED implementation contract  
**Authority owner:** Hydrology domain  
**Artifact family:** `StreamflowTailEventAssessment`  
**Source basis:** *New Ideas 4-2-26(1).pdf* — USGS instantaneous-value checks against approved seasonal 5th/95th percentiles with recency, persistence, and qualifier gates  
**Directory Rules basis:** hydrology meaning belongs under `contracts/domains/hydrology/`; machine shape, fixture evaluation, fixtures, tests, and workflow live under their own responsibility roots.

## Purpose

Define a deterministic, fixture-only evaluator for deciding whether a streamflow tail condition is:

- `NO_EVENT`;
- `HOLD` because a single or short-lived excursion has not met persistence;
- `ANSWER_CANDIDATE` because an approved seasonal tail has persisted;
- `ABSTAIN` because the baseline is missing, the latest value is stale, qualifiers compromise interpretation, or regulated-river context makes the percentile comparison insufficient;
- `DENY` because the percentile authority is not approved or the input violates the public-safe fixture boundary;
- `ERROR` because the candidate is structurally unreadable.

`ANSWER_CANDIDATE` is deliberately not named `ALERT`. The evaluator does not issue warnings, replace USGS/NWS products, or authorize public release.

## Input boundary

The synthetic candidate carries:

- a stable site ID and generalized HUC12 support;
- a UTC evaluation time and ordered instantaneous-value readings;
- a seasonal baseline for the current day-of-year, or an explicit missing baseline;
- configurable recency, persistence-count, and persistence-window thresholds;
- source, evidence, and run-receipt references;
- a regulation-context label;
- fixture-only rights and not-released governance.

Precise coordinates and unpublished station geometry are denied.

## Deterministic rules

1. Missing percentile baseline -> `ABSTAIN / PERCENTILES_MISSING`.
2. Baseline status other than `approved_fixture` -> `DENY / PERCENTILES_NOT_APPROVED`.
3. Latest reading older than `recency_limit_hours` -> `ABSTAIN / DATA_STALE`.
4. Any latest-reading qualifier in `Ice`, `Eqp`, or `SensorError` -> `ABSTAIN / SENSOR_QUALIFIER_PRESENT`.
5. `regulation_context=regulated_context_limited` -> `ABSTAIN / REGULATED_CONTEXT_LIMITED`.
6. Latest value between p05 and p95, inclusive -> `NO_EVENT`.
7. Latest value is in a tail but fewer than `persistence_count` consecutive same-tail readings occur inside `persistence_window_hours` -> `HOLD / PERSISTENCE_NOT_MET`.
8. The required consecutive tail readings are present -> `ANSWER_CANDIDATE / PERSISTENT_LOW_FLOW` or `PERSISTENT_HIGH_FLOW`.

Readings are ordered oldest-to-newest and must not extend beyond the evaluation time. Percentiles must satisfy `0 <= p05 < p95`.

## Output

A successful evaluation emits a schema-valid assessment containing:

- latest discharge and age;
- p05/p95 when available;
- low/high/none candidate state;
- consecutive tail count;
- a finite decision and exact reason code;
- original source/evidence/receipt references;
- fixture-only, not-released governance state.

## Trust boundary

- No USGS or NWS network access.
- No operational alert, emergency advice, flood-stage claim, or public warning.
- No provisional-to-approved conversion.
- No lifecycle writes, EvidenceBundle creation, PolicyDecision, promotion, release, or publication.
- A future live adapter must separately verify current USGS APIs, source terms, qualifiers, approved statistic provenance, correction behavior, and official-alert boundaries.

## Rollback

Remove this contract and its paired schema, evaluator, fixtures, tests, workflow, and generated authoring receipt. No live hydrology state or published artifact is modified.

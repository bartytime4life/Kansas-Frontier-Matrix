<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-rolling-metric-window-disclosure
title: Pass 18 Rolling-Metric Window Disclosure Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Common contract steward · Analytics steward · Evidence steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; source-lineage; rolling-metric; window-frame
responsibility: Preserve exact source lineage and repository reconciliation for the bounded rolling-metric window disclosure adaptation without promoting proposal material into analytical, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription and inspected-repository comparison; PROPOSED bounded adaptation; UNKNOWN engine parity and consumers; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/rolling_metric_window_disclosure.md
  - ../../../contracts/common/aggregate_statistic.md
  - ../../../schemas/contracts/v1/common/rolling_metric_window_disclosure.schema.json
  - ../../../fixtures/contracts/v1/common/rolling_metric_window_disclosure/cases.json
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Rolling-Metric Window Disclosure Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 290 / printed page 287 | Card `KFM-P18-INV-479` proposes recording partition, ordering, and frame definitions for moving averages, ranks, and trend indicators; it notes that frame changes alter meaning and that database differences require parity tests. | `CONFIRMED` |
| `main@6b1c60d3814548acaedc7a365c90e0010573790e` | Exact searches found `AggregateStatistic`, indicator, measurement-scale, period-boundary, temporal, evidence, review, and release surfaces, but no rolling-metric window disclosure contract, schema, fixture family, validator, workflow, matching branch, or pull request. | `CONFIRMED` for the inspected snapshot |

The supplied card is proposal evidence, not repository or database instruction authority. Its source attribution to `Advanced-SQL-Concepts.pdf` is retained as card lineage; that upstream source was not independently admitted or revalidated in this slice.

## Reconciliation and selected increment

`AggregateStatistic` already owns aggregate geography, weighting, numerator/denominator, missing-data, source-release, and non-authority semantics. `MeasurementScaleOperationAssessmentCandidate` separately assesses which aggregation and ranking operations fit declared measurement-scale metadata. Release and review objects already own publication gates.

Changing those established profiles or adding execution logic would broaden compatibility and authority. The selected increment is therefore one standalone common disclosure profile that binds a metric by reference and makes its window semantics inspectable without calculating it.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Record partition definitions. | Explicit global/keyed mode and exact partition fields. | No query construction or source-field resolution. |
| Record ordering definitions. | Ordered fields, direction, null handling, time role, uniqueness declaration, and explicit tie breaker when needed. | No source uniqueness proof or sort execution. |
| Record frame definitions. | Closed `ROWS`, `RANGE`, and `GROUPS` vocabulary with inclusive bounds, offsets, units, and exclusions. | No claim of universal SQL syntax or engine behavior. |
| Make rolling metrics reproducible and auditable. | Deterministic candidate identity, time semantics, missing-data treatment, partial-window behavior, correction, rollback, and public labels. | No metric recomputation, scientific-fitness finding, or evidence resolution. |
| Test cross-engine parity. | Single-engine, synthetic-parity, unresolved, and mismatch states with fixture references. | No live database, generated SQL, or verified parity claim. |
| Keep public use downstream of governance. | Public candidates require review-record and release-manifest references while all authority effects remain false. | No review approval, release, deployment, publication, or public use. |

## Directory Rules basis

Reusable metric-window disclosure meaning is adjacent to `AggregateStatistic` under `contracts/common/`. Shape, synthetic inputs, validation, tests, workflow orchestration, source reconciliation, and generated receipt use their established responsibility roots. No topic root, database adapter, analytics runtime, policy authority, release lane, or public surface is introduced.

## Deferred questions

- Which accepted metrics and indicators actually use rolling windows or ranks?
- Which engine profiles and versions require parity fixtures, and what constitutes parity for nulls, peers, calendars, and numeric precision?
- Should a later accepted `AggregateStatistic` version carry a direct optional reference to this profile?
- Which review and release objects may expose the human-readable disclosure labels?
- How should open-ended, irregular, business-calendar, or event-count windows extend this closed v1 vocabulary?

## Validation and rollback

Focused validation covers closed shape, deterministic identity, partition consistency, ordering uniqueness and tie handling, all three frame units, offset and bound coherence, time-field binding, missing-data method requirements, late-arrival correction/rollback references, parity states, public review/release references, unresolved abstention, no-network replay, hash tampering, and unknown-field rejection.

Rollback is a focused revert of this additive packet. No metric, query, database object, evidence record, release, deployment, or public artifact is changed.

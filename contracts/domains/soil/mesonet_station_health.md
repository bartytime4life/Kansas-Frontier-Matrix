# Kansas Mesonet Station-Health Assessment Contract

**Status:** PROPOSED implementation contract  
**Authority owner:** Soil domain  
**Artifact family:** `MesonetStationHealthAssessment`  
**Source basis:** *New Ideas 4-2-26(1).pdf* — Kansas Mesonet roster freshness, coverage, and soil-moisture anomaly controls  
**Directory Rules basis:** semantic meaning belongs under `contracts/domains/soil/`; machine shape, executable evaluation, fixtures, and tests live in their own responsibility roots.

## Purpose

Define a deterministic, fixture-only assessment that turns a normalized Kansas Mesonet soil-moisture roster into an inspectable station-health candidate. The evaluator may classify freshness, roster degradation, and untriaged statistical anomalies. It does not fetch Mesonet, activate a source, issue an operational alert, resolve rights, approve policy, promote data, or publish a product.

## Input boundary

The synthetic batch preserves:

- station identity and generalized county support;
- one evaluation time and one expected reporting interval;
- the latest station report time;
- soil-moisture samples with caller-supplied z-score and relative-jump diagnostics;
- source descriptor, evidence, and run-receipt references;
- fixture-only rights, consent, and governance state.

Precise station coordinates are denied. Statistical diagnostics are treated as supplied fixture facts; this evaluator does not fit a model or manufacture a baseline.

## Deterministic rules

| Rule | Result |
|---|---|
| Station age is at least `expected_interval_minutes × degraded_after_multiplier` | Station is `DEGRADED` |
| Absolute z-score is greater than `z_score_abs_threshold` | Sample is anomalous |
| Relative jump is at least `relative_jump_fraction_threshold` | Sample is anomalous |
| An anomalous sample has `triage_state=UNTRIAGED` | Count as an untriaged anomaly |
| Degraded fraction is at least `maximum_degraded_fraction` | Batch outcome `HOLD` |
| Fresh-station coverage is below `minimum_coverage_fraction` | Batch outcome `HOLD` |
| Untriaged anomaly count exceeds `max_untriaged_anomalies` | Batch outcome `HOLD` |
| All checks pass | Batch outcome `HEALTHY_FIXTURE` |
| Rights, governance, evidence, support type, or public-safe geometry is invalid | `DENY` |
| The candidate is structurally unreadable | `ERROR` |

Threshold boundary operators are intentional: the source packet describes degradation at `>= 3×` the interval, a roster-loss trigger at `>= 10%`, z-score anomalies at `> 4`, and relative jumps at `>= 50%`.

## Output

A successful evaluation emits a schema-valid `MesonetStationHealthAssessment` containing:

- deterministic summary counts and fractions;
- one sorted station result per input station;
- station reason codes without raw coordinates;
- a finite `HEALTHY_FIXTURE` or `HOLD` decision;
- the original source, evidence, receipt, rights, and non-release governance references.

The assessment remains a candidate carrier. It is not an `EvidenceBundle`, `PolicyDecision`, `ReleaseManifest`, public alert, or published station-health layer.

## Trust boundary

- No network access.
- No RAW, WORK, QUARANTINE, PROCESSED, CATALOG, or PUBLISHED writes.
- No source activation or consent inference.
- No public station coordinates.
- No agronomic interpretation.
- No automatic issue, pull-request, promotion, release, or publication action.
- A future live adapter requires separate source-rights verification, policy review, evidence closure, and release controls.

## Rollback

Remove this contract and its paired schema, fixture evaluator, fixtures, tests, workflow, and generated authoring receipt. No live source or lifecycle state is modified by this slice.

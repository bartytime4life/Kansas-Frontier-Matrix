<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hydrology/adaptive-threshold-proposal
title: Drought-Context Adaptive Threshold Proposal
type: semantic-contract
version: v1
status: proposed
owners: [hydrology-domain-steward]
created: 2026-08-07
policy_label: internal
related:
  - schemas/contracts/v1/domains/hydrology/adaptive_threshold_proposal.schema.json
  - tools/validators/domains/hydrology/validate_adaptive_threshold_proposal.py
  - fixtures/contracts/v1/domains/hydrology/adaptive_threshold_proposal/
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
source_ideas:
  - KFM-P25-PROG-0004
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Drought-Context Adaptive Threshold Proposal

## Purpose

`AdaptiveThresholdProposal` records a **review recommendation** that a hydrologic detector
baseline should be kept, recomputed, or held after considering a version-pinned drought
classification. It implements `KFM-P25-PROG-0004`: refresh detector thresholds or seasonal
percentiles when drought extent and moisture signals remain material.

The object deliberately stops before configuration mutation. It can recommend a deterministic
recalibration dry run; it cannot choose a new threshold value, write detector configuration,
declare a hydrologic event, or publish a changed baseline.

## Authority boundary

- The detector baseline remains a versioned analytical configuration, not evidence.
- The drought input remains a `CLASSIFICATION` with
  `DERIVED_CLASSIFICATION` support; it does not become a streamflow observation.
- Materiality is supplied through a reviewed `materiality_rule_ref`; this validator does not
  invent or recalculate policy thresholds.
- `REVIEW_RECALIBRATION` means "run a governed calibration review," not "change production."
- Watchers are candidate producers and non-publishers.
- No exact recommended threshold is permitted by the schema.

## Required fields

| Field | Meaning |
|---|---|
| `proposal_id` | Deterministic ID from canonical JSON excluding `proposal_id` and `spec_hash`. |
| `schema_version` | `v1`. |
| `detector` | Detector reference, metric, baseline `spec_hash`, analysis window, and evidence references. |
| `drought_context` | Classification reference, valid window, spatial scope, source role, support type, and evidence. |
| `assessment` | Finite outcome, materiality, method recommendation, reason codes, and evidence closure. |
| `governance` | Explicit no-mutation and no-publication boundary. |
| `spec_hash` | Canonical packet digest. |

## Finite outcomes

| Outcome | Required semantics |
|---|---|
| `KEEP_BASELINE` | Materiality is `NOT_MATERIAL`, the baseline is pinned, and reason includes `DROUGHT_CONTEXT_NOT_MATERIAL`. |
| `REVIEW_RECALIBRATION` | Materiality is `MATERIAL`, the baseline is pinned, and method is `RECOMPUTE_SEASONAL_PERCENTILES` or `REVIEW_ADAPTIVE_THRESHOLD`. |
| `HOLD` | Materiality or baseline identity is unresolved; method is `HOLD`. |
| `ERROR` | Operational failure; materiality and method are `UNKNOWN`. |

## Recommended methods

- `NONE`
- `RECOMPUTE_SEASONAL_PERCENTILES`
- `REVIEW_ADAPTIVE_THRESHOLD`
- `HOLD`
- `UNKNOWN`

The contract never carries a replacement percentile or numerical trigger. A later reviewed
calibration artifact must own that decision.

## Deterministic validation

```bash
python tools/validators/domains/hydrology/validate_adaptive_threshold_proposal.py \
  fixtures/contracts/v1/domains/hydrology/adaptive_threshold_proposal/valid/review_recalibration.json

pytest -q tests/domains/hydrology/test_adaptive_threshold_proposal.py
```

## Non-goals

This contract does not:

- fetch the U.S. Drought Monitor or streamflow data;
- compute drought extent, percentiles, or a new threshold;
- mutate a detector, pipeline specification, model, or release;
- declare a drought or hydrologic event;
- evaluate policy, promotion, deployment, or publication.

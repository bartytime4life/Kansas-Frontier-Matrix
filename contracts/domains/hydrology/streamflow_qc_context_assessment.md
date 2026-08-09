<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hydrology/streamflow-qc-context-assessment
title: Streamflow QC Context Assessment
type: semantic-contract
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
created: 2026-08-09
policy_label: internal; hydrology; quality-review; candidate-only
source_ideas: [KFM-P32-IDEA-0002, KFM-P32-FEAT-0001]
related:
  - ./flow_observation.md
  - ./adaptive_threshold_proposal.md
  - ../../../schemas/contracts/v1/domains/hydrology/streamflow_qc_context_assessment.schema.json
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Streamflow QC Context Assessment

> **PROPOSED:** `STREAMFLOW_QC_CONTEXT_V1` records whether declared regional percentile, drought, adjacent-gauge, and ingest context supports a bounded quality-review priority for one low-flow signal. It never invalidates a sensor, declares a hydrologic event, recomputes a percentile, or authorizes publication.

## Source adaptation

Pass 32 card `KFM-P32-IDEA-0002` proposes using hydrologic percentile context as external evidence when distinguishing regional low-flow conditions from a local sensor or integration concern. This profile adapts that proposal without fetching WaterWatch, NWIS, drought, or gauge data and without inventing a numeric threshold.

The assessment consumes opaque references to already-produced observations, percentile context, drought context, and EvidenceRefs. It records classifications supplied by those upstream objects; it does not recalculate them.

## Finite assessment outcomes

| Outcome | Required local relationship | Meaning |
|---|---|---|
| `REGIONAL_LOW_FLOW_CONTEXT` | low-flow signal, adjacent gauges corroborate, drought context supports, integrity context is clear | Regional context supports treating the signal as a real-condition review candidate. |
| `LOCAL_SIGNAL_REVIEW` | low-flow signal lacks regional corroboration or carries an ingest/unit/cadence concern | Prioritize sensor or integration review; do not declare the sensor wrong. |
| `NO_QC_ESCALATION` | the supplied subject is not classified low-flow and integrity context is clear | No low-flow-driven QC escalation from this profile. |
| `HOLD` | required context is unknown or insufficient | Abstain pending evidence. |
| `ERROR` | the upstream assessment explicitly failed | Preserve operational failure. |

`priority` is limited to `ROUTINE`, `ELEVATED`, `HIGH`, or `NONE`. It is review routing, not policy, incident severity, release priority, or publication authority.

## Anti-collapse rules

- The observation source and percentile-context source remain distinct references.
- EvidenceRefs are required for the subject and for any claimed regional corroboration.
- `REGIONAL_LOW_FLOW_CONTEXT` cannot coexist with an ingest gap, unit conflict, late cadence, missing adjacent gauges, or unsupported drought context.
- `LOCAL_SIGNAL_REVIEW` cannot say a sensor is invalid; it only names a review priority.
- The profile carries no raw values, coordinates, numeric percentile thresholds, replacement baselines, or detector configuration.
- All authority-bearing flags are fixed false.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the packet excluding `assessment_id` and `spec_hash`.

```text
spec_hash    = SHA-256(JCS(identity subject))
assessment_id = "kfm:streamflow-qc-context:" + first 24 digest hex characters
```

## Validation outcomes

| Validator outcome | Meaning |
|---|---|
| `PASS` | A coherent regional, local-review, or no-escalation assessment. |
| `ABSTAIN` | A coherent `HOLD` assessment. |
| `DENY` | Shape, identity, evidence, temporal, reason, or authority invariants fail. |
| `ERROR` | A coherent upstream `ERROR` or input cannot be read safely. |

A green result proves local fixture consistency only. It does not resolve evidence, authenticate sources, decide policy, mutate a detector, promote, release, deploy, publish, or authorize public use.

## Directory Rules basis

Hydrology meaning remains in `contracts/domains/hydrology/`; machine shape in `schemas/contracts/v1/domains/hydrology/`; synthetic examples in `fixtures/contracts/v1/domains/hydrology/`; executable validation in `tools/validators/domains/hydrology/`; tests in `tests/domains/hydrology/`; CI in `.github/workflows/`; source adaptation in `docs/intake/exploratory/`; and generated authoring accountability in `data/receipts/generated/`. No new root or parallel evidence, policy, review, release, or publication authority is created.

## Rollback

Close the draft or revert the additive packet. The profile creates no live source, lifecycle write, detector change, release state, cache, deployment, or public artifact requiring operational rollback.

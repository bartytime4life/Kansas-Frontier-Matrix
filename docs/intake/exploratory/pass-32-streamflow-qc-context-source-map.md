# Pass 32 streamflow QC context source map

## Status

**PROPOSED / FIXTURE-ONLY.** This note maps source ideas to a bounded repository adaptation. It is not a source admission, hydrologic finding, sensor judgment, policy decision, release, or publication record.

## Source basis

| Source | Candidate | Adaptation |
|---|---|---|
| `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` | `KFM-P32-IDEA-0002`, hydrologic percentile context for sensor QC | Add a declared-context assessment with explicit source/evidence separation and finite review routing. |
| Same atlas | `KFM-P32-FEAT-0001`, streamflow QC prioritization dashboard | Implement only the non-UI contract precursor; no dashboard or route is claimed. |
| Current repository | `FlowObservation`, `AdaptiveThresholdProposal`, EvidenceRef conventions, repository hashing | Reuse existing hydrology and identity boundaries; do not create a new observation, evidence, or threshold authority. |

The source card says implementation status is unknown. Current `main@a98b631e637a481888d386efedae4625fa5a9341` contains no exact streamflow QC context assessment, validator, fixture family, or open PR for this candidate. The adjacent adaptive-threshold profile recommends later recalibration review but deliberately does not classify sensor/integration review context; this slice does not modify it.

## Deliberate narrowing

- No WaterWatch, NWIS, drought, or adjacent-gauge fetch.
- No numeric percentile threshold or raw flow value.
- No claim that regional context proves a hydrologic anomaly.
- No claim that local inconsistency proves sensor failure.
- No configuration mutation, policy, approval, promotion, release, deployment, or publication.

## Directory placement

Accepted ADR-0029 routes semantic meaning to `contracts/`, machine shape to `schemas/`, synthetic examples to `fixtures/`, reusable validation to `tools/validators/`, tests to `tests/`, CI to `.github/workflows/`, and authoring accountability to `data/receipts/generated/`. The packet uses existing hydrology lanes and introduces no root or parallel authority.

# Pass 32 PM2.5 trigger candidate source map

## Status

**PROPOSED / FIXTURE-ONLY.** This note maps candidate source cards to a bounded repository adaptation. It is not source admission, an air-quality finding, AQI or health advice, policy, release, or publication.

## Source basis

| Source | Candidate | Adaptation |
|---|---|---|
| `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` | `KFM-P32-IDEA-0012`, air-quality trigger fixtures as candidate gates | Require declared monitored-threshold and trailing-median relations, evidence, and fail-closed integrity state. |
| Same atlas | `KFM-P32-PROG-0009`, air trigger fixture suite | Add exact positive, no-trigger, hold, error, and denial fixtures with deterministic identity. |
| Current repository | Atmosphere PM2.5, knowledge-character, AirNow/AQS, low-cost-sensor, and observed/model separation profiles | Reuse Atmosphere ownership and anti-collapse boundaries without creating another observation, policy, or public-health authority. |

The atlas marks implementation status unknown. Current `main@73be9400ffecbc5908bf4aa127de83d79cd40864` has no exact PM2.5 trigger candidate assessment, validator, or fixture family. Existing Atmosphere profiles constrain observation meaning, provenance, calibration, and source reconciliation; none performs this categorical candidate check.

## Deliberate narrowing

- No live AirNow, AQS, PurpleAir, station, or API fetch.
- No raw concentration, numeric threshold, trailing-median value, AQI value, coordinates, or health category.
- No regulatory compliance, health guidance, event declaration, detector mutation, policy, approval, release, deployment, or publication.

## Directory placement

Accepted ADR-0029 routes semantic meaning to `contracts/`, machine shape to `schemas/`, synthetic cases to `fixtures/`, reusable validation to `tools/validators/`, tests to `tests/`, CI to `.github/workflows/`, and authoring accountability to `data/receipts/generated/`. The packet uses the existing Atmosphere domain lanes and introduces no new root.

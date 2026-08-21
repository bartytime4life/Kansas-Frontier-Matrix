<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/pm-sensor-trust-profile
title: PM Sensor Trust Profile Candidate
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Atmosphere steward · Air-quality steward · Evidence steward · Schema steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; atmosphere; pm-sensor; trust-dimensions; no-network; non-release
source_card: KFM-P30-PROG-0001
source_spec_hash: sha256:6fed794c95d89545865ee4faa472ee9dc5906a073d2af0e22145fe16610b7b4f
related:
  - ./AirStation.md
  - ./PM25Observation.md
  - ../../../docs/dashboards/domain/air/PM_SENSOR_CALIBRATION_REVIEW.md
  - ../../../schemas/contracts/v1/domains/atmosphere/pm_sensor_trust_profile.schema.json
  - ../../../fixtures/contracts/v1/domains/atmosphere/pm_sensor_trust_profile/cases.json
  - ../../../tools/validators/domains/atmosphere/validate_pm_sensor_trust_profile.py
  - ../../../tests/validators/domains/atmosphere/test_pm_sensor_trust_profile.py
tags: [kfm, atmosphere, pm25, sensor-trust, calibration, reference-anchor, fixture]
[/KFM_META_BLOCK_V2] -->

# PM Sensor Trust Profile Candidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This profile declares bounded synthetic trust dimensions for a PM sensor evaluation window. It does not evaluate a live sensor, prove scientific validity, establish reference-grade equivalence, admit a source, evaluate policy, approve review, promote, release, publish, or issue public-health guidance.

## Source-derived gap

Pass 30 card `KFM-P30-PROG-0001` calls for a PM sensor trust schema carrying accuracy, stability, responsiveness, consensus alignment, calibration version, and reference-anchor fields. Current repository contracts distinguish station identity from calibration proof, and existing low-cost-sensor fixtures preserve correction lineage and caveats. This additive profile supplies the missing reusable declaration shape without changing those authorities.

## Directory Rules basis

Atmosphere-specific semantic meaning belongs under `contracts/domains/atmosphere/`; machine shape belongs under `schemas/contracts/v1/domains/atmosphere/`; synthetic examples belong under `fixtures/contracts/v1/domains/atmosphere/`; and executable enforcement belongs under `tools/validators/` and `tests/`. No new root or competing station, observation, policy, evidence, release, or publication home is created.

## Required meaning

| Surface | Meaning | Fail-closed boundary |
|---|---|---|
| `evaluation_window` | Bounded synthetic observation and reference counts with explicit start and end times. | Reversed or empty time intervals fail. |
| `metrics` | Independent normalized declarations for accuracy, stability, responsiveness, and consensus alignment. | A measured metric requires a method and evidence; unresolved remains null. |
| `calibration` | Versioned correction context, model reference, application time, transferability state, and evidence. | `WITHIN_DECLARED_SCOPE` requires a model and time; it is not proof of scientific fitness. |
| `reference_anchor` | Reference-monitor or collocation-series declaration, or explicit unresolved state. | Peer consensus cannot substitute for a reference anchor, and no anchor grants authority. |
| `evidence_refs` | Exact closure over all nested metric, calibration, and anchor references. | Missing, additional, duplicated, or unsorted references fail. |
| `assessment` | Finite `QUALIFIED_CONTEXT`, `HOLD`, or `DENY` routing posture with no composite score. | Qualified context requires all dimensions measured, a resolved anchor, and bounded transferability. |
| `controls` | Fixed non-authority flags. | Every live-evaluation, source, policy, review, promotion, release, publication, health, and equivalence claim remains false. |

## Identity

`spec_hash` is RFC 8785/JCS SHA-256 over the complete record after removing `profile_id` and `spec_hash`. `profile_id` is `kfm:pm-sensor-trust:` followed by the first 24 hexadecimal digest characters. Set-like reference and reason arrays are sorted and duplicate-free.

## Relationship to existing Atmosphere objects

- `AirStation` remains station and network identity context; it does not prove calibration or observation quality.
- `PM25Observation` remains the observation family and preserves low-cost-sensor caveats, correction references, source roles, evidence, and release boundaries.
- Existing low-cost-sensor calibration fixtures remain correction-lineage proof surfaces. This profile does not replace or reinterpret them.
- The PM Sensor Calibration Review dashboard remains a proposed review specification; this profile does not activate a dashboard or define scientific thresholds.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/atmosphere \
  --pattern 'test_pm_sensor_trust_profile.py' \
  --verbose

python tools/validators/domains/atmosphere/validate_pm_sensor_trust_profile.py --fixtures
```

A passing result proves only the bounded synthetic shape, evidence-reference closure, posture consistency, and deterministic identity encoded here.

## Rollback

Revert this additive packet. It creates no live sensor evaluation, source state, policy decision, lifecycle transition, release, public guidance, or published artifact.

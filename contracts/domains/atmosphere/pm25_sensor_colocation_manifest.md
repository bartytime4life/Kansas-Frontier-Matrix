<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/pm25-sensor-colocation-manifest
title: PM2.5 Sensor Co-location Manifest Candidate
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Atmosphere steward · Air-quality steward · Evidence steward · Schema steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; atmosphere; pm25; co-location; calibration-context; no-network; non-release
source_card: KFM-P30-PROG-0003
source_spec_hash: sha256:7bc2ca941e28838e5e44f436ad3eaed4cdf2da041e36c506604e1a4ccb771285
related:
  - ./pm_sensor_trust_profile.md
  - ./AirStation.md
  - ./PM25Observation.md
  - ../../../schemas/contracts/v1/domains/atmosphere/pm25_sensor_colocation_manifest.schema.json
  - ../../../fixtures/contracts/v1/domains/atmosphere/pm25_sensor_colocation_manifest/cases.json
  - ../../../tools/validators/domains/atmosphere/validate_pm25_sensor_colocation_manifest.py
  - ../../../tests/validators/domains/atmosphere/test_pm25_sensor_colocation_manifest.py
tags: [kfm, atmosphere, pm25, sensor, colocation, calibration-context, fixture]
[/KFM_META_BLOCK_V2] -->

# PM2.5 Sensor Co-location Manifest Candidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This manifest declares synthetic co-location study context. It does not evaluate live sensor data, establish calibration validity, prove reference-grade equivalence, admit a source, evaluate policy, approve review, promote, release, publish, or issue public-health guidance.

## Source-derived gap

Pass 30 card `KFM-P30-PROG-0003` calls for sensor identifiers, a reference site, start and end times, data completeness, seasonal coverage, and a validation split. The existing PM sensor trust profile can cite calibration and reference context, but it does not own the study-design manifest that produced that context. This additive candidate supplies that bounded declaration without changing station, observation, evidence, review, or release authority.

## Directory Rules basis

Atmosphere-specific semantic meaning belongs under `contracts/domains/atmosphere/`; machine shape belongs under `schemas/contracts/v1/domains/atmosphere/`; synthetic cases belong under `fixtures/contracts/v1/domains/atmosphere/`; reusable enforcement belongs under `tools/validators/`; and validation evidence belongs under `tests/`. The packet creates no domain root and no parallel schema, policy, evidence, receipt, or publication home.

## Required meaning

| Surface | Meaning | Fail-closed boundary |
|---|---|---|
| `sensor_ids` | Sorted, duplicate-free synthetic sensor identities included in the declared study. | Completeness or split records may not introduce or omit sensors. |
| `reference_site` | Synthetic reference-site and source-descriptor bindings plus evidence references. | It is context only and never establishes regulatory or reference-grade equivalence. |
| `window` | UTC-bounded co-location interval. | Empty or reversed intervals fail. |
| `data_completeness` | Per-sensor expected and observed counts with a reproduced fraction. | Fractions must equal the declared counts; no scientific sufficiency threshold is inferred. |
| `seasonal_coverage` | Explicit meteorological-season labels and a finite coverage posture. | Labels are canonical and do not imply generalizability. |
| `validation_split` | Time-blocked or site-holdout partitions with evidence bindings. | A validation partition is mandatory; overlapping time blocks for a shared sensor fail. |
| `generalization_assumptions` | Sorted, explicit limits on transfer beyond the declared window and site. | Empty, duplicated, or unordered assumptions fail. |
| `evidence_refs` | Exact closure over reference-site, completeness, and split evidence. | Missing, additional, duplicated, or unordered references fail. |
| `controls` | Fixed non-authority flags. | Every live-data, scientific-validity, source, policy, review, promotion, release, publication, and health-authority effect remains false. |

## Identity

`spec_hash` is RFC 8785/JCS SHA-256 over the complete record after removing `manifest_id` and `spec_hash`. `manifest_id` is `kfm:pm25-colocation-manifest:` followed by the first 24 hexadecimal digest characters.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/atmosphere \
  --pattern 'test_pm25_sensor_colocation_manifest.py' \
  --verbose

python tools/validators/domains/atmosphere/validate_pm25_sensor_colocation_manifest.py --fixtures
```

A passing result proves only the bounded synthetic declaration, internal arithmetic and split consistency, evidence-reference closure, and deterministic identity encoded here.

## Rollback

Revert this additive packet and the explicit Atmosphere validator-inventory entry. No live sensor, source state, calibration model, policy decision, lifecycle transition, release, public guidance, or published artifact is created.

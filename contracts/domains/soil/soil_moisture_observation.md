<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/soil/soil-moisture-observation/v1
title: Soil Moisture Observation Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-06-23
updated: 2026-08-07
policy_label: public
related:
  - "../../../schemas/contracts/v1/domains/soil/soil_moisture_observation.schema.json"
  - "../../../tools/validators/domains/soil/validate_soil_moisture_observation.py"
  - "../../../fixtures/domains/soil/soil_moisture_observation/"
  - "../../../tests/domains/soil/test_soil_moisture_observation.py"
  - "./support_type_profile.md"
  - "./soil_time_caveat.md"
tags: [kfm, soil, soil-moisture, observation, station, satellite, depth, qc, support-type]
notes:
  - "Fixture-first and PROPOSED_INACTIVE. This contract creates no source, evidence, policy, promotion, release, or publication authority."
  - "Station, reference-station, satellite-grid, survey, profile, and derivative support remain distinct."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Moisture Observation Contract

`SoilMoistureObservation` records one source-scoped, time-aware soil-moisture assessment while preserving the support type, source role, depth or retrieval layer, normalized unit, QC, time axes, spatial support, evidence references, limitations, and finite outcome.

> [!IMPORTANT]
> This is a **fixture-first, deterministic, no-network contract profile**. The paired schema and validator establish bounded shape and semantic polarity for synthetic records only. They do not activate Kansas Mesonet, SCAN, USCRN, SMAP, or another source; resolve evidence; evaluate policy; promote data; approve release; or publish a map or answer.

## Purpose

The object prevents a numeric moisture value from losing the context that gives it meaning. It keeps these source-support families separate:

| Support type | Required role | Spatial support | Required depth posture |
|---|---|---|---|
| `station_soil_moisture` | `IN_SITU_OBSERVATION` | `POINT_STATION` | `SENSOR_DEPTH` with numeric `depth_cm` |
| `reference_station_soil_climate` | `REFERENCE_OBSERVATION` | `POINT_STATION` | `SENSOR_DEPTH` with numeric `depth_cm` |
| `satellite_soil_moisture_grid` | `SATELLITE_RETRIEVAL` | `GRID_CELL` | `SURFACE_LAYER` or `ROOT_ZONE_LAYER`; no synthetic station depth |

The broader Soil support vocabulary remains owned by the existing support-type profile. This object intentionally excludes authoritative static survey soil, gridded derivative soil, profile evidence, interpretations, and governed change evidence.

## Non-collapse rules

1. A station reading is not a satellite grid cell, survey polygon, gridded derivative, field-wide surface, or county-wide condition.
2. A satellite retrieval is not a station observation and may not invent a sensor depth.
3. Normalized volumetric water content uses `m3_m3`; a source-native value may be retained only with its source unit.
4. Material station/reference observations preserve a numeric sensor depth in centimeters.
5. QC flags, source timezone, cadence, observed time, retrieval time, support resolution, evidence, and limitations remain part of the record.
6. Exact coordinates are not carried in this profile. Location is a governed reference and public geometry is an explicit rule.
7. Operational or private sensor use returns `DENY` unless a separate policy/review path supports it.
8. `ANSWER` means only that the local synthetic record satisfies this profile. It is not public truth or release authority.

## Finite outcomes

| Outcome | Value posture | Meaning |
|---|---|---|
| `ANSWER` | Normalized value required | The observation is structurally and semantically supported for its stated source scope. |
| `ABSTAIN` | Value must be `null` | Evidence, freshness, or required context is insufficient. |
| `DENY` | Value must be `null` | Private/sensitive use or an unsafe support claim blocks use. |
| `ERROR` | Value must be `null` | The bounded evaluator could not complete safely. |

Reason codes are canonical, sorted, and explicit. No negative outcome may silently retain an answer value.

## Deterministic identity

The canonical projection removes `observation_id` and `spec_hash`, serializes the remaining object as sorted compact UTF-8 JSON with non-finite values denied, and computes SHA-256.

- `spec_hash = sha256:<64 lowercase hex>`
- `observation_id = soil-moisture:<first 24 hex characters of spec_hash>`

Arrays that behave as sets are sorted and unique. Replaying the same normalized input yields the same identity.

## Contract surface

The machine profile binds:

- source reference, role, native identifier, and native key family;
- subject reference, location reference, spatial support, public geometry rule, and resolution;
- normalized value/unit, measurement type, depth support, optional source-native value, and QC flags;
- observed, source-publication, retrieval, and valid-time fields plus source timezone and cadence;
- finite outcome, reason codes, evidence references, limitations, and optional `SoilTimeCaveat` reference;
- governance non-effects that remain false in this inactive profile.

## Validation boundary

The validator is deterministic and no-network. It checks:

- bounded UTF-8 JSON, duplicate-key and non-finite-number rejection;
- Draft 2020-12 schema conformance;
- deterministic identity and canonical set ordering;
- support-type/source-role/spatial-support/key-family parity;
- station depth and satellite retrieval-layer rules;
- UTC and temporal ordering;
- normalized unit/value bounds and answer/negative outcome polarity;
- evidence requirements and governance non-effects.

It does not verify live sensor accuracy, source authority, rights, scientific fitness, station metadata, product version, freshness against a live clock, EvidenceBundle closure, policy, review, release, correction propagation, rollback execution, or public suitability.

## Lifecycle and public boundary

A valid record may participate in RAW-to-WORK/QUARANTINE reconciliation and later PROCESSED validation. This contract does not move the record through lifecycle stages. A public map, API, Evidence Drawer, export, or Focus Mode answer requires separately verified EvidenceBundle, policy, review, release, correction, and rollback closure.

Public clients must not read RAW, WORK, QUARANTINE, private sensor stores, or direct model output.

## Directory Rules basis

Placement follows responsibility roots:

- semantic meaning: `contracts/domains/soil/`;
- machine shape: `schemas/contracts/v1/domains/soil/`;
- reusable synthetic fixtures: `fixtures/domains/soil/soil_moisture_observation/`;
- repository-wide executable validation: `tools/validators/domains/soil/`;
- conformance tests: `tests/domains/soil/`;
- read-only CI orchestration: `.github/workflows/`;
- AI authoring process memory: `data/receipts/generated/`.

No new root or parallel contract, schema, policy, source, proof, release, or publication home is introduced.

## Rollback

Revert the implementation commit or restore the prior contract blob. The schema, fixtures, validator, tests, workflow, and generated receipt are additive; rollback does not require source shutdown, data migration, release withdrawal, cache invalidation, or public correction because this profile activates and publishes nothing.

<p align="right"><a href="#top">Back to top</a></p>

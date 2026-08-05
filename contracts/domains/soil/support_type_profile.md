<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/soil/support-type-profile
title: Soil Support-Type Anti-Collapse Profile
type: semantic-contract; domain-profile; validation-profile
version: v0.1.0
status: proposed; inactive; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Soil steward · Contract steward · Source steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; soil; support-type; anti-collapse; non-publisher
related:
  - ./README.md
  - ../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../packages/domains/soil/README.md
  - ../../../schemas/contracts/v1/domains/soil/support_type_profile.schema.json
  - ../../../schemas/contracts/v1/domains/soil/support_type_candidate.schema.json
  - ../../../pipeline_specs/soil/support_type_profile.v1.json
  - ../../../tools/validators/domains/soil/support_type/validate_support_type_profile.py
tags: [kfm, soil, support-type, source-role, anti-collapse, fixture-first]
[/KFM_META_BLOCK_V2] -->

# Soil support-type anti-collapse profile

> This inactive, fixture-first profile proves that Soil support classes remain
> distinct across source family, source role, spatial support, and claim kind.
> It does not admit a source, resolve evidence, evaluate policy, authorize
> promotion, release a layer, or publish Soil truth.

## Goal

The Soil lane is a governed family rather than one all-purpose truth layer. The
profile records eight bounded support classes:

| Support type | Intended support | Primary anti-collapse rule |
|---|---|---|
| `authoritative_static_soil` | SSURGO/SDA map-unit survey support | Not a live station, satellite-grid, or management claim. |
| `gridded_derivative_soil` | gSSURGO/gNATSGO-style derived grids | Not source-of-record polygon or station truth. |
| `station_soil_moisture` | Kansas Mesonet-style point observations | Not countywide, satellite-grid, static-survey, or advisory truth. |
| `reference_station_soil_climate` | SCAN/USCRN reference observations | Not local Mesonet identity or countywide advice. |
| `satellite_soil_moisture_grid` | SMAP-style gridded context | Not a station reading, field verification, or survey map unit. |
| `profile_soil_evidence` | Pedon/profile/horizon evidence | Not map-unit or countywide truth without separate support. |
| `soil_interpretation` | Source or KFM-derived interpretations | Not legal, hazard, management, or engineering authority. |
| `governed_change_evidence` | Materiality/diff process memory | Not release authorization or publication state. |

The names are bound to this proposed profile version. They do not amend a
global vocabulary or activate live sources.

## Candidate boundary

`SoilSupportTypeCandidate` is a synthetic test object. It binds:

- profile identity, version, and digest;
- candidate content digest;
- one declared support type;
- source family and source role;
- spatial-support class and claim kind;
- source and evidence references;
- explicit `not_evaluated` policy and `not_released` release state;
- governance fields that are all false.

A schema-valid candidate can still fail the profile mapping. That distinction is
intentional: schema checks shape, while the validator checks profile coherence.

## Deterministic identity

`support_type_profile.v1.json` uses `kfm-canonical-json-v1`: remove the
top-level `spec_hash`, serialize sorted-key UTF-8 JSON without insignificant
whitespace, preserve array order, compute SHA-256, and prefix `sha256:`.

The validator also requires profile rule arrays and candidate reference arrays
to be sorted and unique so replay does not depend on incidental ordering.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, digest, profile binding, and support mapping are coherent. |
| `DENY` | The candidate collapses support types, requests public use, or violates the inactive governance boundary. |
| `ERROR` | The input, profile, or schema cannot be read or evaluated safely. |

`PASS` is a bounded test result. It is not `ANSWER`, policy approval, evidence
closure, release readiness, or publication permission.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. Placement follows one owning
responsibility per artifact:

- semantic meaning → `contracts/domains/soil/`;
- machine shape → `schemas/contracts/v1/domains/soil/`;
- inactive executable profile → `pipeline_specs/soil/`;
- validation logic → `tools/validators/domains/soil/support_type/`;
- synthetic cases → `fixtures/domains/soil/support_type/`;
- enforceability proof → `tests/validators/domains/soil/support_type/`;
- CI orchestration → `.github/workflows/`;
- AI authoring accountability → `data/receipts/generated/`.

No new root or parallel source, policy, evidence, proof, release, or published
home is created.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/soil/support_type \
  --pattern 'test_support_type_profile.py' \
  --verbose

python tools/validators/domains/soil/support_type/validate_support_type_profile.py \
  --fixtures
```

Both commands are deterministic and perform no network access.

## Rollback

Before merge, close the draft pull request and delete its branch. After an
authorized merge, revert the complete contract/schema/profile/validator/
fixture/test/workflow/receipt slice. No source, lifecycle object, release, or
public artifact is created.

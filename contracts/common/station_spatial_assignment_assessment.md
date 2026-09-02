<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/station-spatial-assignment-assessment
title: StationSpatialAssignmentAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Spatial foundation steward · Hydrology steward · Boundary steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; spatial-assignment; station; huc12; county
responsibility: Define a bounded deterministic assessment of synthetic station point assignments to versioned state, county, and HUC12 boundaries without live boundary access or canonical geography writes.
truth_posture: CONFIRMED connected-Drive source and current-repository gap / PROPOSED inactive assessment / NEEDS VERIFICATION human review and hosted exact-head CI
related:
  - ../../docs/intake/exploratory/pass-25-station-spatial-assignment-source-map.md
  - ../../schemas/contracts/v1/common/station_spatial_assignment_assessment.schema.json
  - ../../fixtures/contracts/v1/common/station_spatial_assignment_assessment/cases.json
  - ../../tools/validators/common/validate_station_spatial_assignment_assessment.py
  - ../../tests/validators/common/test_validate_station_spatial_assignment_assessment.py
tags: [kfm, common, station, spatial-join, huc12, county, fixture-only, no-network]
[/KFM_META_BLOCK_V2] -->

# StationSpatialAssignmentAssessment Candidate

This candidate makes a narrow cross-domain operation testable: given a synthetic station point and pinned synthetic boundary snapshots, derive one state FIPS, county GEOID, and HUC12 assignment with deterministic point-in-polygon behavior.

It adapts Pass 25 card `KFM-P25-IDEA-0014` and the connected `New Ideas 4-21-26` station workflow. It does not fetch SCAN, USCRN, Mesonet, AQS, AirNow, WBD, or TIGER data. It does not establish that a real station belongs to a real geography.

## Profile boundary

The v1 fixture profile accepts EPSG:4326 points and simple closed polygon rings. A point on a boundary abstains rather than selecting a side. A point outside every polygon abstains. Multiple containing polygons, relation contradictions, invalid rings, version-set contradictions, or identity/hash drift deny.

## Finite outcomes

- `PASS`: one resolved containing polygon exists at each required level and the declared context matches.
- `ABSTAIN`: a boundary snapshot is unresolved, a point lies on a boundary, or no unique containing geography exists.
- `DENY`: overlapping assignments or contradictory identity, geometry, relation, context, ordering, or hashes.
- `ERROR`: closed-schema or bounded-parser failure.

A green result is local synthetic geometry conformance only. It grants no source activation, canonical boundary authority, location publication, lifecycle transition, promotion, release, or public use.

## Directory Rules basis

Reusable cross-domain spatial-assignment meaning belongs under `contracts/common/`; machine shape under `schemas/contracts/v1/common/`; fixtures, validators, tests, workflow, source map, and authoring receipt remain in their existing responsibility roots. No new geography, hydrology, station, source, or publication root is created.

## Validation

```bash
python -m unittest tests.validators.common.test_validate_station_spatial_assignment_assessment -v
python tools/validators/common/validate_station_spatial_assignment_assessment.py --fixtures
```

## Rollback

Revert the additive packet. No station, source, boundary, lifecycle, release, deployment, cache, or public state requires restoration.

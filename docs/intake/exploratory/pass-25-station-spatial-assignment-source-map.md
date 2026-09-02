<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-25-station-spatial-assignment-source-map
title: Pass 25 Station Spatial Assignment Source Map
type: source-map
version: v1.0.0
status: proposed; implementation-source-map; review-pending
owners: OWNER_TBD — Intake steward · Spatial foundation steward · Hydrology steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; intake; pass-25; station; spatial-assignment
responsibility: Reconcile Pass 25 station-to-HUC12/county assignment material with current repository surfaces and bound the fixture-only adaptation.
truth_posture: CONFIRMED source and bounded repository search / PROPOSED adaptation / NEEDS VERIFICATION human review
related:
  - ../../../contracts/common/station_spatial_assignment_assessment.md
  - ../../../schemas/contracts/v1/common/station_spatial_assignment_assessment.schema.json
  - ../../../data/receipts/generated/genrec-pass25-station-spatial-assignment-20260811.json
tags: [kfm, pass-25, source-map, station, huc12, county, point-in-polygon]
[/KFM_META_BLOCK_V2] -->

# Pass 25 Station Spatial Assignment Source Map

## Source

Connected Google Drive document **New Ideas 4-21-26** proposes assigning SCAN, USCRN, Mesonet, AQS, and AirNow station points to versioned WBD HUC12 and Census county geographies through deterministic point-in-polygon joins. Pass 25 preserves that idea as `KFM-P25-IDEA-0014` and explicitly leaves implementation maturity unverified.

## Repository reconciliation

Current `main` contains station, boundary, join, hydrology, source, and temporal surfaces, but bounded exact searches found no closed `StationSpatialAssignmentAssessmentCandidate` packet and no matching pull request. The implementation therefore avoids creating a live join pipeline or authoritative crosswalk. Existing source and geography families remain separate.

## Adaptation decision

Implement one no-network synthetic assessment with three required levels: state, county, and HUC12. Pin each boundary snapshot by opaque source/version references and digest. Recompute relation from a simple closed polygon ring. Boundary and no-match cases abstain; overlap and contradiction deny.

## Deferred work

- live WBD/TIGER SourceDescriptor and rights/currentness review;
- robust production geometry engine, CRS transforms, antimeridian, holes, and invalid-polygon repair;
- canonical station registry integration;
- persisted crosswalks, correction propagation, and release use.

Those require separate repository, source, policy, and steward evidence.

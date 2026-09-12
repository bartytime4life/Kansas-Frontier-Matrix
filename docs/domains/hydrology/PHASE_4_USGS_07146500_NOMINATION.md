<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/hydrology/phase-4-usgs-07146500-nomination
title: "Phase 4 Living Waters — USGS 07146500 Candidate Nomination"
type: review-record
version: v1
status: proposed; human-selected; review-pending; fixture-only; no-network; non-authoritative
owners: ["@bartytime4life", "Hydrology steward — NEEDS VERIFICATION", "Source steward — NEEDS VERIFICATION"]
created: 2026-09-12
updated: 2026-09-12
policy_label: restricted-review
owning_root: docs/
responsibility: "Records one human-selected, review-only Phase 4 product-and-gauge nomination; it does not admit or activate a source, retrieve data, evaluate policy, release, deploy, publish, or create flood-warning authority."
truth_posture: "proposed; cite-or-abstain; external references are not resolved to an EvidenceBundle and no source response is retrieved"
related:
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/BOUNDARY.md
  - docs/domains/hydrology/SOURCE_REGISTRY.md
  - docs/sources/catalog/usgs/nwis-water.md
  - apps/explorer-web/src/features/living_atlas/living-waters-fixture.ts
  - apps/explorer-web/src/features/living_atlas/living-waters-product-selection.ts
  - apps/explorer-web/tests/living-waters-product-selection.test.ts
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3372
tags: [kfm, hydrology, phase-4, living-waters, usgs, continuous-values, discharge, review-only, no-network]
notes:
  - "A human selected the pair during the 2026-09-12 Phase 4 review. This record is a nomination, not a source descriptor, evidence bundle, retrieval record, policy decision, lifecycle transition, release, or publication artifact."
  - "No observation value, observation timestamp, station coordinate, source payload, source-health assertion, forecast, flood stage, flood category, or safety interpretation is carried by this record."
[/KFM_META_BLOCK_V2] -->

# Phase 4 Living Waters — USGS 07146500 candidate nomination

> **Status: `HUMAN_SELECTED_REVIEW_PENDING`.** This records the smallest
> product-and-gauge nomination for the next Living Waters proof. It is a
> review-only fixture boundary; it does not fetch, admit, activate, assess, or
> display live water data.

## Selected pair

| Field | Value |
|---|---|
| Publisher | U.S. Geological Survey (USGS) |
| Product | Water Data APIs — Continuous Values |
| Measurement | `00060` — discharge |
| Statistic semantics | instantaneous |
| Unit | `ft3/s` |
| Gauge | USGS `07146500` — Arkansas River at Arkansas City, KS |
| Decision state | `HUMAN_SELECTED_REVIEW_PENDING` |

The pair narrows the Phase 4 review to one public federal product, one Kansas
gauge identifier, and one already-established measurement semantic. It does
not select gage height, daily values, a flood stage, a forecast, a warning
threshold, or a derived condition.

## Evidence and implementation boundary

The selected product is referenced through the official USGS continuous-values
documentation and the official monitoring-location page for `USGS-07146500`.
Those links establish only the intended external references for a later review;
they do not resolve an `EvidenceRef` to an EvidenceBundle in this slice.

- [USGS Continuous Values API](https://api.waterdata.usgs.gov/ogcapi/v0/collections/continuous)
- [USGS monitoring location USGS-07146500](https://waterdata.usgs.gov/monitoring-location/USGS-07146500/)

The paired Explorer projection is deterministic and fixture-only. Its output
contains the product/gauge selection and reference URLs, but deliberately fixes
the observation to `NOT_RETRIEVED` with `value: null` and `observedAt: null`.
It has no network client or renderer binding.

## Fixed non-effects

All of the following are `false` in the fixture and enforced by the focused
unit test:

- source admission, activation, payload retrieval, and policy evaluation;
- lifecycle promotion, release, deployment, and publication;
- flood-warning, forecast, flood-stage, or life-safety authority;
- rendering a map layer or displaying a discharge observation.

In particular, this nomination must not be described as a working source
connection, a live gauge display, a data-quality or availability finding, or a
flood-warning product. USGS observations remain provisional when supplied as
such, and no observation is supplied here.

## What the existing synthetic proof still owns

The merged Living Waters fixture remains the semantic proof for instantaneous
discharge and finite `AVAILABLE`, `STALE`, `NO_RESULTS`, `UNAVAILABLE`, and
`ABSTAIN` presentation states. This nomination does not change that synthetic
packet, its schema, or its ownership. It adds no parallel schema lane.

## Gates before any later real-data use

1. Steward-confirm the source descriptor, rights, attribution, cadence, API
   lineage, site identity, and parameter/qualifier handling.
2. Capture any source response through the governed lifecycle with immutable
   receipt and provenance, rather than from the browser.
3. Preserve provisional/approved status, observation time, retrieval time,
   unit, qualifiers, and unavailable/ambiguous outcomes.
4. Resolve policy, sensitivity, evidence, correction, rollback, review, and
   release gates independently before any governed API or public surface could
   use the data.

Until those gates are independently satisfied, the only valid Phase 4 result is
this review-only nomination.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/stac-geoparquet-mirror-assessment-source-map
title: STAC GeoParquet Mirror Assessment - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Catalog steward · STAC steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; intake; data; stac; geoparquet; mirror; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from the supplied spatiotemporal modernization blueprint to one bounded STAC GeoParquet mirror-parity candidate without adopting an unstable specification or granting catalog, evidence, policy, review, release, or publication authority.
truth_posture: CONFIRMED Drive lineage, upstream file/blob inspection, and current-main collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION upstream release status, steward approval, byte-level validation, and later-main collisions
related:
  - ./spatiotemporal-modernization-blueprint-source-map.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../standards/STAC.md
  - ../../../contracts/data/stac_geoparquet_mirror_assessment.md
tags: [kfm, intake, stac, geoparquet, collection-mirror, parity]
notes:
  - "The upstream mapping document was fetched from its primary GitHub repository on 2026-08-10 and pinned by Git blob SHA dcef2113c42f505cffa8208af9f6525ec5122a69."
[/KFM_META_BLOCK_V2] -->

# STAC GeoParquet mirror assessment - source map

> **Outcome:** The Google Drive document *Kansas Frontier Matrix Improvements* contributes a bounded STAC GeoParquet bulk-mirror parity candidate. The packet checks declared synthetic projections only and does not open Parquet or promote the upstream mapping into KFM doctrine.

## Source lineage

| Source | Relevant pressure | Posture used here |
|---|---|---|
| Google Drive `Kansas Frontier Matrix Improvements` (`1qH0oVs3vQN0YXhk_vASnrwAmJORL_vQigOM0cfHJSDI`) | Represent STAC collections in GeoParquet for bulk analytical access. | Design pressure only; imperative performance and adoption claims are not carried forward. |
| Existing governed source map | Classifies STAC GeoParquet as a deferred profile candidate requiring a pinned revision, mapping rules, nested asset/link validation, and catalog closure. | Repository routing authority for the bounded next step. |
| Upstream `radiantearth/stac-geoparquet-spec` mapping document | One STAC Item per row; extensions, identity, geometry, bbox, links, assets, collection, flattened properties, native timestamps, metadata version, collections map, and collection-mirror asset role. | Primary technical lineage pinned to Git blob `dcef2113c42f505cffa8208af9f6525ec5122a69`; upstream stability is not inferred. |
| Directory Rules and accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules. | Placement authority. |

## Current-main collision review

The inspected tree at `main@7463ee1347326b72a6998e5331b20a3cae69604b` contains KFM STAC documentation, a fixture-first STAC Item catalog-health validator, catalog-closure responsibilities, GeoParquet carrier readiness, STAC asset projections, and several catalog trust extensions. No contract, schema, validator, fixture family, test, or workflow was found that compares a declared STAC Item set with a declared STAC GeoParquet collection-mirror row set and distinguishes full parity from partial-sample parity. This is **CONFIRMED for that inspected tree**, not a timeless repository claim.

## Bounded adaptation

The packet retains mapping fields needed to detect identity, geometry/bbox, link, asset, property, temporal, collection, omission, addition, and reserved-name conflicts. It pins the upstream mapping input, treats partial samples as `ABSTAIN`, and fixes every operational authority flag to false.

It excludes physical Parquet or Arrow validation, WKB/GeoArrow decoding, source fetches, remote collection validation, catalog mutation, evidence resolution, policy, review, release, correction, rollback, deployment, publication, and public use.

## Directory Rules placement

| Responsibility | Path |
|---|---|
| Catalog-data semantic meaning | `contracts/data/stac_geoparquet_mirror_assessment.md` |
| Canonical machine shape | `schemas/contracts/v1/data/stac_geoparquet_mirror_assessment.schema.json` |
| Reusable synthetic inputs | `fixtures/contracts/v1/data/stac_geoparquet_mirror_assessment/cases.json` |
| Catalog validator | `tools/validators/catalog/validate_stac_geoparquet_mirror_assessment.py` |
| Executable evidence | `tests/validators/test_validate_stac_geoparquet_mirror_assessment.py` |
| Hosted orchestration | `.github/workflows/stac-geoparquet-mirror-assessment.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

This follows Directory Rules: `contracts/` defines meaning, `schemas/` defines shape, `fixtures/` holds synthetic inputs, `tools/` validates, `tests/` proves behavior, and the existing workflow/receipt roots retain orchestration and provenance. No new root or parallel STAC, catalog, evidence, policy, release, receipt, proof, correction, rollback, or publication authority is created.

## Verification still required

Catalog and STAC stewards must decide whether and when to admit an upstream mapping revision, how actual STAC objects and Parquet bytes are resolved, how Arrow/Parquet types and geometries are validated, how collection metadata and extensions are validated, and how rights, sensitivity, correction, rollback, release, and catalog closure are enforced. An upstream pin change requires fresh primary-source review and fixture replay.

## Validation and rollback

Validation covers schema validity, exact finite outcomes, full versus partial scope, content conflict, key and collection integrity, property collision, temporal shape, deterministic identity, bounded hostile parsing, no-network behavior, workflow parsing, documentation metadata, and generated-receipt hashes.

Rollback is an ordinary revert of this additive packet. No STAC object, Parquet file, catalog record, evidence object, release, correction, rollback, deployment, or publication state is changed.

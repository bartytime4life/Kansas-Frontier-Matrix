<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/m24-geoparquet-pmtiles-cog-cross-engine-interoperability-source-map
title: M24 GeoParquet, PMTiles & COG Cross-Engine Interoperability - source map
type: exploratory-intake-source-map
version: v0.1.0
status: proposed; fixture-first; read-only
owners: OWNER_TBD — GeoParquet steward · PMTiles steward · COG steward · evidence steward
created: 2026-09-01
updated: 2026-09-01
policy_label: public; exploratory; m24; geoparquet; pmtiles; cog; evidence; non-authoritative
owning_root: docs/
responsibility: Record the current repository surfaces, overlap map, and the smallest reversible first slice for the M24 carrier-interoperability checkpoint without granting default, release, or publication authority.
truth_posture: CONFIRMED current-main pin / CONFIRMED overlap issue and PR review surface / PROPOSED GeoParquet-only first slice / NEEDS VERIFICATION broader cross-engine matrix, PMTiles, COG, DuckDB, and Sedona surfaces
related:
  - ../../../contracts/release/geoparquet_2_rc_pyarrow_carrier_probe.md
  - ../../../contracts/release/geoparquet_2_rc_gdal_consumer_probe.md
  - ../../../docs/standards/GEOPARQUET.md
  - ../../../docs/standards/PMTILES.md
  - ../../../docs/standards/COG.md
  - ../../../tests/release/test_geoparquet_2_rc_pyarrow_carriers.py
  - ../../../tests/release/test_geoparquet_2_rc_gdal_consumer_probe.py
  - ../../../tests/release/README.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, m24, geoparquet, pmtiles, cog, interoperability, inventory, overlap, source-map]
[/KFM_META_BLOCK_V2] -->

# M24 GeoParquet, PMTiles & COG Cross-Engine Interoperability

## Execution pin and overlap map

| Item | Current pin |
|---|---|
| Current main | `main@db23a8bfa9fa126e87009a41240576619ccaac02` |
| Overlap issue | `#2907` |
| Overlap PR | `#4084` |
| Accepted placement authority | ADR-0029 plus `docs/doctrine/directory-rules.md` |
| Adjacent README contract | `tests/release/README.md` |

## Current repository surface classification

| Surface | Status | Notes |
|---|---|---|
| `docs/standards/GEOPARQUET.md` | IMPLEMENTED | Repository standards boundary for GeoParquet 1.1 / 2.0-RC evidence. |
| `contracts/release/geoparquet_2_rc_pyarrow_carrier_probe.md` | PARTIAL | Exact PyArrow 25.0.0 carrier probe, still fixture-only. |
| `tests/release/test_geoparquet_2_rc_pyarrow_carriers.py` | PARTIAL | Generates the carrier pair and now includes one malformed-carrier negative test. |
| `contracts/release/geoparquet_2_rc_gdal_consumer_probe.md` | PARTIAL | PyArrow-to-GDAL read edge only; no producer route or broader matrix. |
| `tests/release/test_geoparquet_2_rc_gdal_consumer_probe.py` | PARTIAL | Bounded consumer probe with governed failure cases. |
| `docs/standards/PMTILES.md` | NOT_INSPECTED | Adjacent milestone surface not expanded in this slice. |
| `docs/standards/COG.md` | NOT_INSPECTED | Adjacent milestone surface not expanded in this slice. |
| DuckDB / Sedona lane declarations | ABSENT | No current repository byte evidence was added for this slice. |

## First slice contract

- Dependency: the existing PyArrow carrier generator/validator lane only.
- Validation: a truncated synthetic carrier must fail closed with `CARRIER_UNREADABLE`.
- Rollback: revert this doc and the focused test addition together.
- Forward-fix: broaden only after a separate reviewed slice adds the next carrier or engine lane.

## Unresolved items

- Cross-engine GeoParquet confirmation remains partial.
- PMTiles and COG proof surfaces remain outside this slice.
- DuckDB, SedonaSpark, and SedonaDB remain unauthenticated for this checkpoint.

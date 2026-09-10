<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-census-cartographic-boundary-files
title: Census 2025 County Cartographic Boundary Files — Kansas reference slice
type: source-documentation
version: v0.1.0
status: draft; HOLD; documentation-only; no source activation
owners: NEEDS VERIFICATION — Census source steward + geography steward + evidence/release stewards
created: 2026-09-10
updated: 2026-09-10
policy_label: public-review; cite-or-abstain; fail-closed
current_path: docs/sources/catalog/census/cartographic-boundary-files.md
owning_root: docs/
responsibility: bounded human-facing source documentation; no admission, evidence, release, publication, or runtime authority
truth_posture: "CONFIRMED exact upstream archive identity and bounded offline inspection facts / PROPOSED source descriptor, validator, and future transform gates / HOLD source activation, runtime binding, evidence authority, release, and publication / NEEDS VERIFICATION rights decision, accountable review, and release closure"
related:
  - ./README.md
  - ./tiger-line.md
  - ../../../../data/registry/sources/settlements-infrastructure/census_cartographic_boundary_counties_2025_500k.source.json
  - ../../../../tools/validators/source/census_cartographic_boundary_counties.py
  - ../../../doctrine/directory-rules.md
tags: [kfm, census, cartographic-boundary, county, kansas, geoid, geography-version, hold]
notes:
  - "This page records a bounded verification only; no Census payload, EvidenceBundle, release, or runtime binding is created here."
  - "Exact archive facts were reproduced from the caller-supplied ZIP by the no-network validator on 2026-09-10."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Census 2025 County Cartographic Boundary Files — Kansas reference slice

> Bounded source documentation for a possible first Kansas county reference-geometry slice from the U.S. Census Bureau's 2025 county-and-equivalent cartographic boundary archive.

> [!CAUTION]
> **HOLD — not admitted, released, or available to runtime.** The proposed `SourceDescriptor` is inactive, the connector is disabled, and `public_release.allowed` is `false`. No source payload, deterministic Kansas derivative, `EvidenceBundle`, `ReleaseManifest`, site layer, map binding, or governed API response is authorized by this page or by a passing offline inspection.

## Verified source identity

The following facts were reproduced by a bounded offline inspection on 2026-09-10. The exact archive is the identity boundary; the product page or a later annual vintage is not an interchangeable input.

| Field | Verified value |
|---|---|
| Publisher and product | U.S. Census Bureau, **2025 Cartographic Boundary File (SHP), County and Equivalent for United States, 1:500,000** |
| Vintage | **January 1, 2025** |
| Scale | **1:500,000**, generalized |
| Exact archive | [`cb_2025_us_county_500k.zip`](https://www2.census.gov/geo/tiger/GENZ2025/shp/cb_2025_us_county_500k.zip) |
| Archive bytes | **11,758,981** (`11758981`) |
| Archive SHA-256 | `aa976c00b181939755d0da757f4c7c2dc0103c3b3b4530fb2a91c2bb62fc777c` |
| Native CRS | **NAD83 / EPSG:4269** |
| National records | **3,235** county-and-equivalent features |
| Kansas selector | Exact DBF predicate `STATEFP == "20"` |
| Kansas records | **105**, with **105 unique `GEOID` values** |
| Kansas GEOID range | `20001` through `20209`; each `GEOID == STATEFP + COUNTYFP` |
| Kansas bbox | **`[-102.051744, 36.993016, -94.588413, 40.003162]`** in EPSG:4269, ordered west, south, east, north |
| Kansas identity projection SHA-256 | `ef0e2721bc98ee5542072e1f10e83c279551d73cd2db3e841f0a39da703d0e15` |
| Kansas shape-record SHA-256 | `bb466162a735f1c386a10b7d06b4538f16ffd2fc340ba369540a17d4a1b91197` |

The candidate machine-readable record is [`census_cartographic_boundary_counties_2025_500k.source.json`](../../../../data/registry/sources/settlements-infrastructure/census_cartographic_boundary_counties_2025_500k.source.json). It is the proposed descriptor home for identity, role, rights, cadence, limitations, and activation posture; this page does not supersede it.

## Role and limitations

Within the declared vintage and scale, this product may support:

- county and equivalent **reference identity** using Census `GEOID`;
- small-scale **thematic map display** after governed transformation and release; and
- **citation support** for the exact federal statistical geography product.

It does **not** establish cadastral, survey, parcel, title, municipal-status, navigation, geocoding, life-safety, or current legal-boundary truth. The geometry is intentionally generalized and is unsuitable for precise boundary analysis or for calculating authoritative area or perimeter. Preserve the source-reported `ALAND` and `AWATER` fields rather than recomputing them from this geometry. A spatial join inherits the limitations, sensitivity, and claim-role rules of every joined source; county membership does not turn an aggregate or candidate into a place-level fact.

The Census Bureau is authoritative for this federal statistical cartographic product and its identifiers within the declared role. Underlying legal boundary authority remains outside this source.

## Current HOLD posture

This slice currently has documentation and bounded inspection evidence only:

| Surface | Current state |
|---|---|
| Source registry | Proposed; `review_state: needs_review` |
| Connector / watcher | Disabled; no recurring or live fetch authorized |
| Source payload | Not committed and not admitted to RAW |
| Kansas transform | Not implemented or promoted |
| Evidence | No authoritative `EvidenceBundle` emitted |
| Release | `release_state: not_released`; public release denied |
| Site, map, API, runtime | No binding allowed; public consumers must omit the layer or render an explicit unavailable/HOLD state |

The official TIGERweb service is useful corroborating documentation, but the browser and map runtime must not query it as an unpublished fallback. Public surfaces may consume only a governed artifact named by an approved release manifest.

## Offline validation

Download the exact archive outside the validator, then run the bounded no-network check from the repository root:

```bash
python tools/validators/source/census_cartographic_boundary_counties.py \
  /absolute/path/to/cb_2025_us_county_500k.zip
```

The validator binds the caller-supplied ZIP to the proposed descriptor and checks archive safety limits, exact member set, byte length and SHA-256, embedded product metadata, CRS, Shapefile/DBF structure, national count, the deterministic Kansas predicate and GEOID set, bbox, and content digests. A successful result ends with `validation_outcome: "PASS"` and still means only **offline identity and structure passed**. It does not fetch, extract to the repository, write lifecycle state, admit the source, create evidence, approve policy, authorize release, or bind runtime.

## Gates before any deterministic Kansas derivative

A future transform remains fail-closed until all of these are implemented and reviewed:

1. Pin an immutable RAW capture to the exact URL, `11758981` bytes, and expected SHA-256; reject same-URL byte drift as a new review event.
2. Close source activation, rights, sensitivity, steward, and domain review without weakening the current HOLD posture by inference.
3. Select only `STATEFP == "20"`; require exactly 105 unique expected GEOIDs and preserve `STATEFP`, `COUNTYFP`, `COUNTYNS`, `GEOID`, `NAME`, `NAMELSAD`, `ALAND`, and `AWATER`.
4. Record `GeographyVersion` as January 1, 2025, scale `1:500,000`, native CRS EPSG:4269, and the verified Kansas bbox. Reject missing or conflicting vintage, CRS, axis order, count, or identity fields.
5. Define the target format, CRS, coordinate precision, feature ordering, geometry-validation/repair policy, and simplification policy. No implicit reprojection, geometry repair, or additional generalization is allowed.
6. Produce byte-stable output from the same input and pinned toolchain; record input/output digests, parameters, software versions, counts, bbox, and warnings in a `TransformReceipt` and `ValidationReport`.
7. Bind source and transform evidence, policy decision, review record, release manifest, correction path, and rollback target before any published asset, API route, or map layer can resolve.

A later Census vintage is a distinct candidate source version. It must not silently overwrite or supersede this archive.

## Correction and rollback

Any digest, length, member, count, GEOID, CRS, bbox, or metadata mismatch is a fail-closed condition: quarantine the candidate, keep the last approved release unchanged, and open a correction review. Never repair upstream bytes or mutate a published derivative in place.

If this slice is later released, a `CorrectionNotice` must identify the affected source and output digests, reason, discovery time, affected claims/layers, and replacement or retraction. Supersession must be explicit. Rollback selects the prior immutable artifact through its `ReleaseManifest` and rollback record, then verifies governed API and map cache behavior against that manifest. Because the present slice is HOLD and unreleased, today's rollback is only an ordinary reviewed Git reversion of candidate repository changes; there is no external release or runtime state to roll back.

## Official Census references and citation

- [2025 county-and-equivalent archive (exact distribution)](https://www2.census.gov/geo/tiger/GENZ2025/shp/cb_2025_us_county_500k.zip)
- [Census Cartographic Boundary Files overview](https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html)
- [Census Cartographic Boundary File description and naming](https://www.census.gov/programs-surveys/geography/technical-documentation/naming-convention/cartographic-boundary-file.html)
- [TIGERweb Generalized ACS 2025 Counties 500K layer](https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2025/State_County/MapServer/11)

Minimum citation:

> U.S. Census Bureau, *2025 Cartographic Boundary File (SHP), County and Equivalent for United States, 1:500,000*, January 1, 2025 vintage, exact archive URL and access date. Geometry generalized for thematic mapping.

[Back to top](#top)

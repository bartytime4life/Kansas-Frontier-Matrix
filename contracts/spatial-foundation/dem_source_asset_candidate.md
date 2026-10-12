<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/spatial-foundation/dem-source-asset-candidate
title: DEM Source Asset Candidate Contract
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED_INACTIVE; fixture-only; non-authoritative
owners: OWNER_TBD — Spatial foundation steward · Source steward · Contracts steward · Validation steward
created: 2026-09-09
updated: 2026-09-09
policy_label: public; contracts; spatial-foundation; elevation; dem; source-candidate; non-authoritative
owning_root: contracts/
responsibility: Define an exact, fixture-only DEM asset candidate and its unresolved admission blockers without creating source, lifecycle, evidence, runtime, release, deployment, or publication authority.
truth_posture: "CONFIRMED exact public USGS asset inspection; PROPOSED inactive contract; HOLD pending delivered-tile geoid, applicable vertical accuracy, and human review"
related:
  - ../../schemas/contracts/v1/spatial-foundation/dem_source_asset_candidate.schema.json
  - ../../fixtures/contracts/v1/spatial-foundation/dem_source_asset_candidate/cases.json
  - ../../tools/validators/validate_dem_source_asset_candidate.py
  - ../../tests/validators/test_validate_dem_source_asset_candidate.py
  - ../../docs/sources/catalog/usgs/3dep-elevation.md
notes:
  - "The fixture records identity and inspection facts only; it contains no GeoTIFF or ordinary source payload."
  - "Conformance leaves the candidate on HOLD and never admits or activates Terrain 3D."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `DemSourceAssetCandidate`

> A closed, fixture-only record for evaluating one exact DEM distribution asset before source admission or runtime use.

## Purpose

`USGS 3DEP`, `one-meter DEM`, or a mutable elevation service is not an adequate source identity for the first Terrain 3D slice. This contract binds one exact distribution tile to its authoritative metadata, byte digests, dates, footprint, coordinate reference, vertical reference, raster grid, nodata rule, accuracy disposition, source-work-unit lineage, and a minimized public-safe inspection sample.

The first fixture evaluates `USGS_1M_14_x56y429_KS_Statewide_2018_A18.tif`, a standard 1-meter bare-earth DEM tile intersecting the Ellsworth pilot area. The raster, metadata, 3DEP Index result, vertical-accuracy report, and Census TIGERweb state and county checks were inspected outside ordinary validation, then reduced to declared facts and SHA-256 identities. The repository stores neither the 297 MB GeoTIFF nor a live acquisition path.

## Exact identity and evidence separation

The candidate keeps these facts distinct:

- source-work-unit collection dates versus standard-tile publication date;
- the delivered tile CRS (`EPSG:26914`) versus the source-work-unit CRS (`EPSG:3744`);
- NAVD88, which the tile metadata declares, versus `GEOID12B`, which is established only for the sole intersecting source work unit;
- the 10 km nominal product footprint versus the GeoTIFF's 6 m storage border;
- author-time remote-response byte observations versus the content-addressed minimized projections retained for offline review;
- source Float32 elevation versus a fixture-only Terrarium representation; and
- display exaggeration versus the numeric source elevation returned to a caller.

The authoritative locators are:

- USGS GeoTIFF: `https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/KS_Statewide_2018_A18/TIFF/USGS_1M_14_x56y429_KS_Statewide_2018_A18.tif`
- USGS tile metadata: `https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/KS_Statewide_2018_A18/metadata/USGS_1M_14_x56y429_KS_Statewide_2018_A18.xml`
- USGS 3DEP Index layer: `https://index.nationalmap.gov/arcgis/rest/services/3DEPElevationIndex/MapServer/24`
- exact project-and-envelope query: `evidence_captures.three_dep_index_query.locator`
- USGS UTM 14 vertical-accuracy report: `https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/metadata/KS_Statewide_2018_A18/vertical_accuracy/USGS/14/USGS_USGS_KS_Statewide_2018_UTM14_VA.txt`
- Census TIGERweb States layer, January 1, 2026 vintage: `https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/0`
- exact public-point state query: `evidence_captures.census_state_point_query.locator`
- exact public-point county query: `evidence_captures.census_county_point_query.locator`

The envelope query returns exactly one intersecting source work unit, `KS_Statewide_B10_2018` (`workunit_id=209920`). That record establishes the source-work-unit collection interval, QL2 classification, source CRS, NAVD88, GEOID12B, and 1 m source DEM GSD. It does not establish a numeric vertical-accuracy statistic applicable to the delivered tile. Independent Census point-in-polygon queries return Kansas (`GEOID=20`, `STUSAB=KS`) and Ellsworth County (`GEOID=20053`, county code `053`) for the public-safe point; the 3DEP query is not used as administrative-boundary evidence.

Each query capture records an author-time observation of the remote response length and SHA-256 digest. Those raw responses are not stored, so the remote digests are not independently reproducible offline and do not prove the service's current response. The closed minimized projections are stored separately in `evidence-projection-snapshot.json`; its repository path, byte length, and SHA-256 digest are part of the candidate identity. The validator verifies that local snapshot and binds every projection to dependent candidate fields. Any comparison with a later service response requires a separate reviewed recapture.

The constraints-aware rights classification is bound to the exact, SHA-256-identified USGS tile metadata asset: `/metadata/idinfo/descript/abstract` establishes the public-domain statement, while `/metadata/idinfo/accconst` and `/metadata/idinfo/useconst` preserve the USGS disclaimer, no-accuracy-warranty, and no-endorsement caveats. It is not inferred from the candidate label or from an unbound general web page.

## Required fields

A conforming candidate records:

- exact organization, program, product family, project IDs, tile ID, source role, metadata-bound rights evidence, and sensitivity;
- exact HTTPS raster and XML metadata locators, filenames, byte lengths, retrieval times, and SHA-256 digests;
- one frozen UTC evidence-capture session whose remote-query retrieval times equal its completion time and do not postdate candidate freeze;
- source-work-unit observation interval separately from tile publication and XML temporal range;
- XML WGS84 bounds, nominal UTM product bounds, separate GeoTIFF storage bounds, a declared forward/inverse transform, authoritative Kansas and Ellsworth County point-in-polygon evidence, and a public-safe pilot point;
- complete delivered horizontal CRS identity and its realization status;
- vertical datum, units, delivered-tile geoid status, and the separately scoped source-work-unit geoid;
- cell size, dimensions, affine transform, data type, pixel interpretation, and source nodata value;
- an unresolved delivered-tile vertical-accuracy state plus the immutable, explicitly non-applicable project report;
- one minimized source pixel plus its fixture-only Terrarium encoding, quantization error, source nodata value, and validity-mask rule;
- exact unresolved blockers, `HOLD`, pending human review, and all authority effects fixed false; and
- deterministic content identity using repository JCS plus SHA-256.

## Fail-closed rules

Validation denies the candidate when identity, digest, date, coverage, CRS, vertical datum, units, resolution, nodata, lineage, or blocker closure is inconsistent. In particular:

- publication and collection dates may not be conflated;
- retrieval timestamps may not precede the corresponding HTTP Last-Modified timestamp;
- every numeric input must be finite and within the JSON canonicalization safe-integer domain before any arithmetic;
- every remote-query retrieval time must equal the frozen evidence-capture completion time, that completion must not postdate candidate freeze, and the Census vintage must not postdate the Census metadata retrieval;
- the delivered CRS must be the complete `EPSG:26914` identity and may not collapse to bare `NAD83`;
- projected coordinates must remain within the declared UTM domain, and transform arithmetic must fail closed;
- the XML footprint must reconcile with the nominal UTM bounds under the declared GRS80 UTM zone 14N null-datum approximation;
- the sample WGS84 coordinate must transform to its declared projected coordinate and raster cell;
- the content-addressed local 3DEP and Census projection snapshot must remain byte-identity consistent and cross-field closed;
- remote response digests must remain labeled as author-time observations and may not be presented as offline-reproducible captures;
- the public-domain claim must remain bound to the exact USGS metadata digest and extraction path;
- a source-work-unit geoid may not be relabeled as a delivered-tile geoid;
- a general program specification may not substitute for an applicable numeric accuracy result;
- missing accuracy remains an explicit blocker;
- the public-safe inspection point must fall inside the declared tile bounds;
- the fixture decoding error must remain within one Terrarium quantization step;
- nodata is carried by a source-comparison validity mask, never by a potentially colliding Terrarium RGB sentinel;
- the package-root decoder accepts only the hard-bound one-cell candidate fixture and optional display exaggeration; caller-supplied identity, digest, raster bytes, validity mask, grid, datum, and nodata remain confined to the package's internal conformance seam;
- omitted display exaggeration defaults to exactly `1.0`, while any supplied exaggeration remains display-only;
- the reported numeric sample is never exaggerated; and
- any activation, admission, runtime loading, EvidenceBundle resolution, lifecycle write, promotion, release, deployment, publication, or public-use effect is forbidden; and
- each closed authority/effect flag plus the `PROPOSED_INACTIVE`, `FIXTURE_ONLY`, `NONE`, and `HOLD` posture has an explicit fail-closed mutation fixture.

## Current disposition

The exact tile is a credible candidate, but it remains `HOLD`. A USGS UTM 14 project report records 708 NVA checkpoints with RMSEz `0.0864 m` and 95% accuracy `0.1694 m`, plus 492 VVA checkpoints with a 95th percentile of `0.2397 m`. Its inventory includes B10 source DEM inputs, but it is a multi-work-unit project result and does not explicitly bind those statistics to this delivered standard tile. The fixture therefore preserves the report and its digest while leaving tile-applicable accuracy unresolved. `GEOID12B` is likewise proven for the matched source work unit, not explicitly for the delivered tile. Human review is also pending.

A future review may resolve those blockers by citing immutable delivered-tile evidence and explicitly accepting the source-work-unit-to-tile vertical lineage. This v1 profile intentionally cannot represent a verified delivered-tile geoid or vertical-accuracy claim; resolution requires a separately reviewed contract revision. Editing this fixture or passing CI does not admit the source.

## Validation boundary

A passing fixture proves only closed shape, deterministic identity, internal consistency, content-addressed local projection closure, coordinate reconciliation, blocker closure, and fixture-only sampling invariants. Validation performs no network request, does not re-establish the author-time remote-response digests, does not inspect the remote GeoTIFF, XML, or query services, and does not write repository or lifecycle state.

It does not create a `SourceDescriptor`, connector, RAW capture, pipeline run, EvidenceBundle, catalog entry, MapLibre `raster-dem` source, `setTerrain` call, runtime sample authority, release, deployment, publication, engineering claim, survey claim, or legal-boundary claim.

## Correction and rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the dependency-closed contract, schema, fixture, validator, tests, workflow, sampling helper, and generated receipt. No data migration, cache purge, source shutdown, deployment rollback, or public correction is required because the slice creates no live or published state.

<p align="right"><a href="#top">Back to top</a></p>

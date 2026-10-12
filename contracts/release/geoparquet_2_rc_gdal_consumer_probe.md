# GeoParquet 2.0 RC GDAL Consumer Probe

Status: `PROPOSED_INACTIVE / PARTIAL_OR_HOLD / FIXTURE_ONLY`

Profile: `kfm.geoparquet-2-rc-gdal-consumer-probe.v1`

This bounded profile consumes the two actual synthetic carriers emitted by
`kfm.geoparquet-2-rc-pyarrow-carrier-probe.v1` with exact GDAL `3.13.2`
command-line bytes. It tests only this direction:

```text
PyArrow 25.0.0 producer -> GDAL 3.13.2 consumer
```

The two inputs remain:

1. the GeoParquet `1.1.0` WKB baseline; and
2. the GeoParquet `2.0.0-rc.1` `GEOMETRY` logical type over physical
   `BYTE_ARRAY` WKB.

GeoParquet `1.1.0` remains the KFM default. The profile cannot return
`INTEROPERABLE_CANDIDATE` and creates no adoption, ADR, migration, release,
deployment, publication, or public-use authority.

## Exact distribution boundary

The probe pulls the official OSGeo multi-architecture image
`ghcr.io/osgeo/gdal:alpine-normal-3.13.2` by immutable manifest-list digest:

```text
sha256:6960891693c3463b8e2b498a915c7c9b10eeb93f155d5be14c2e3ffbede9fbb1
```

The hosted lane selects `linux/amd64`; OSGeo records that platform manifest as:

```text
sha256:6611b649465826c623869861447be58cd75962da2312d8ab656a1f4e32acf98d
```

The corresponding selected source identity is the GDAL `v3.13.2` tag at commit
`b40672525acf3f5c4f29d8541aa7dcff1e18eb92`. The `alpine-normal` image is used
because the official image configuration includes the Parquet dependency; the
smaller image does not. The immutable image reference binds the selected
distribution and its layers, but does not authenticate a production deployment
or admit GDAL as a KFM runtime dependency.

## Executed checks

The repository runner:

- verifies the source manifest and both carrier digests before execution;
- pulls the exact image for `linux/amd64` and records the local image identity;
- verifies `GDAL 3.13.2` and the presence of the Parquet vector driver;
- executes with no network, a read-only container filesystem, no Linux
  capabilities, and a read-only fixture mount;
- translates each carrier to GeoJSON through `ogr2ogr` while requesting an
  OGC:CRS84-to-OGC:CRS84 transform; and
- compares row count, stable feature identity, non-geometry labels, Point
  coordinates, and null geometry behavior with the PyArrow producer manifest.

An empty Parquet `GEOMETRY` CRS parameter is the format default for geographic
longitude/latitude WGS84 and is therefore semantically compatible with the
fixture's optional inline OGC:CRS84 PROJJSON metadata. This profile tests that
single same-CRS case only; it does not prove projected-CRS or conflict behavior.

## Finite outcomes

- `PARTIAL` — both retained carriers are read with the expected bounded
  semantics. The wider engine matrix, GDAL producer route, and pruning proof
  remain incomplete.
- `HOLD` — the exact image runs, but the Parquet driver or one selected carrier
  is explicitly unavailable or unsupported. No substitute image or engine may
  be used.
- `FAIL` — GDAL reports success while returning a different row count, stable
  identity, label, geometry type, coordinate, or null-geometry result.
- `ERROR` — the packet, image identity, version, carrier binding, schema,
  declared outcome, or governance boundary is malformed or contradictory.

## Explicitly deferred

- GDAL production and write/read round trip;
- unknown Parquet metadata preservation through a GDAL rewrite;
- empty and mixed geometry-type cases beyond this retained null/Point fixture;
- projected CRS and intentional Parquet-versus-inline CRS conflict;
- Parquet-native geospatial statistics and row-group pruning;
- `GEOGRAPHY` logical-type behavior;
- DuckDB Spatial, SedonaSpark, and SedonaDB lanes;
- cross-platform image execution and independent human review; and
- adoption, migration, release, deployment, publication, or public use.

## Rollback

Before merge, close the draft pull request. After an authorized merge, revert
this profile, schema, runner, validator, focused tests, workflow wiring, and
generated authoring receipt as one dependency-closed packet. No source, data,
runtime, release, deployment, or publication cleanup is required.

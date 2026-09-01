# GeoParquet 2.0 RC PyArrow Carrier Probe

Status: `PROPOSED_INACTIVE / PARTIAL / FIXTURE_ONLY`

Profile: `kfm.geoparquet-2-rc-pyarrow-carrier-probe.v1`

This bounded execution profile creates and inspects two tiny, wholly synthetic
Parquet carriers with exact PyArrow `25.0.0` bytes:

1. a retained GeoParquet `1.1.0` WKB baseline; and
2. a GeoParquet `2.0.0-rc.1` carrier whose root `geometry` column uses the
   Parquet `GEOMETRY` logical type over physical `BYTE_ARRAY` WKB.

The profile proves only one producer/inspector lane. It does not claim GDAL,
DuckDB Spatial, SedonaSpark, SedonaDB, or production interoperability.

## Deterministic input

Four generated feature identities are used with three Point WKB values and one
null. Coordinates are synthetic fixture values and are not Kansas observations,
facilities, parcels, source records, or public claims. Both carriers use two row
groups, no compression, no dictionary encoding, and an inline OGC:CRS84
PROJJSON identity in optional `geo` metadata.

## Finite result

- `PARTIAL` — both actual carriers are generated, digest-bound, readable, retain
  stable feature identity and WKB, and the 2.0-RC footer exposes the expected
  native logical type; cross-engine and geospatial-pruning proof remain absent.
- `ERROR` — carrier bytes, digests, schema/footer, WKB, CRS, metadata,
  toolchain, declared result, or governance boundaries disagree.

`INTEROPERABLE_CANDIDATE` is not available to this profile.

## Exact package boundary

The execution workflow uses Python `3.12` and the PyPI manylinux x86-64 wheel
`pyarrow-25.0.0-cp312-cp312-manylinux_2_28_x86_64.whl` with SHA-256
`5d1dbf24e151042f2fa3c129563f65d66674128868496fb008c4272b16bdf778`.
The hash authenticates only that downloaded wheel in the declared hosted-runner
lane. It does not authenticate GDAL, DuckDB, Sedona, containers, or transitive
production artifacts.

## Explicit HOLDs

- GDAL producer/consumer execution;
- DuckDB Spatial extension integrity and query/pruning behavior;
- SedonaSpark and SedonaDB execution as distinct surfaces;
- Parquet-native geospatial row-group statistics and pruning correctness;
- projected/geographic CRS round trips beyond this one OGC:CRS84 fixture;
- GEOGRAPHY logical-type behavior;
- malformed/truncated carrier coverage beyond one focused negative test;
- independent human review; and
- adoption, migration, release, deployment, publication, or public use.

## Rollback

Before merge, close the draft pull request. After an authorized merge, revert
the carrier family, workflow, tests, lock, generated receipt, and committed
synthetic bytes. No source or external-system cleanup is required.

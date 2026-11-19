# Synthetic NLCD-style native-grid packets

`base.json` and `changed.json` contain 382-byte, self-contained classic GeoTIFFs
encoded as base64, with class-scheme candidates, fixed capture metadata, exact
source hashes, and golden observation candidates. They were generated in the
repository's locked imagery environment, without provider access.

Each grid has 12 cells at a synthetic 30-unit resolution in EPSG:5070, with three
nodata cells. The base has three valid cells for each code 11, 41 and 90. The
changed case replaces one code 11 cell with 41, giving counts 2, 4 and 3.
Labels are synthetic; no reviewed NLCD legend, land-cover condition, habitat
meaning, source admission or public-use permission is established.

Valid time is the synthetic 2021 calendar year; retrieval is fixed at
2026-11-19T00:00:00Z. No current provider data or current clock is required.
The [entrypoint](../../../../pipelines/domains/habitat/ingest_nlcd.py) compares
replay against the complete golden object. See the
[runbook](../../../../docs/runbooks/nlcd-fixture-ingest.md) for source, grid,
mask, identity, uncertainty and execution limits.

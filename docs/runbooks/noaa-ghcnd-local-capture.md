<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/noaa-ghcnd-local-capture
title: Bounded Kansas GHCN Daily local capture
type: runbook
version: v1.0
status: implemented; private capture; review pending
owners: ["@bartytime4life"]
created: 2026-10-07
updated: 2026-10-07
policy_label: public-documentation
owning_root: docs/
responsibility: Explain station selection, bounded acquisition, verification and recovery in the existing external KFM store.
truth_posture: Implementation and capture evidence are separate from source admission and map release.
[/KFM_META_BLOCK_V2] -->

# Kansas GHCN Daily on the local PC

The [NOAA directory](https://www.ncei.noaa.gov/pub/data/ghcn/daily/) provides
daily station observations useful for rainfall, temperature, snowfall, snow
depth and station-history context. Use each station's available elements and
dates; a state's overall time span is not continuous coverage at every station.
The [product description](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)
explains changing observations, real-time versus archive-quality updates, and
variable station coverage. Preserve source flags and retrieval times.

## Selection and storage

Select the exact `KS` state field in `ghcnd-stations.txt`, validate coordinates,
and join it to `by_station/`. The inspected directory lists **2,519 Kansas
stations / 184,215,541 compressed bytes**. These are complete available station
files, including all elements and years, not just recent observations.
`ghcnd-inventory.txt` records element-specific advertised periods; the capture
also measures dates and row counts from each downloaded file.

The source's [station format](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme-by_station.txt)
contains one station/date/element record per row, with the value, measurement,
quality and source flags, and observation time. Originals stay `.csv.gz`.
Nothing is expanded to disk. The parser checks gzip CRC, row shape, station ID
and calendar dates. It counts flags without removing flagged observations or
turning traces/missing values into zero. Units remain in the captured
[README](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt); normalization
is a separate future step.

Do not also acquire `all/`, the global tarball, or global `by_year/` files:
they duplicate selected station observations and increase storage. The site's
figures, papers, staging and temporary directories are not required payloads.
Existing local GHCNDEX climate-index archives are different products, not a
replacement for these daily observations; they remain untouched.

The operator enforces **384 MiB across all retained GHCNd runs**, including
metadata and receipts, and a **100 GiB minimum free-space reserve**. It reserves
16 MiB for reports, permits two concurrent requests, bounds individual station
objects to 8 MiB compressed / 128 MiB inspected in memory, and limits a capture
invocation to 30 minutes. No cron, unattended refresh, bulk world selection,
paid service, deletion or automatic eviction is installed. Repeat a partial run
to acquire only missing stations. A new revision is an explicit new capture;
it still shares the aggregate cap and cannot grow storage without limit.

## Run and verify

Use the existing initialized external store, not the repository or Site checkout.
Python 3.11+ is the documented operator environment; only the standard library
is needed by this command. Choose a unique run label (UTC-shaped for sorting);
actual retrieval timestamps are recorded separately in every source receipt.

```bash
python3 tools/local_data/noaa_ghcnd.py prepare \
  --root "$HOME/Projects/KFM-data" --run 20261007T182000Z
python3 tools/local_data/noaa_ghcnd.py capture \
  --root "$HOME/Projects/KFM-data" --run 20261007T182000Z
python3 tools/local_data/noaa_ghcnd.py verify \
  --root "$HOME/Projects/KFM-data" --run 20261007T182000Z
```

`prepare` captures eight bounded source metadata/documents, creates an explicit
Kansas plan, and checks expected storage. `capture` hashes originals and records
per-station receipts. `verify` independently rehashes and checks every compressed
stream, then writes a GeoJSON station-location/coverage index for local review.
All metadata snapshots are dated captures, not a promise that NOAA's mutable
directory remained globally atomic during the run. Listed sizes and actual
captured sizes are retained separately. Provider checksums are unavailable;
SHA-256 identifies local captured bytes and is not upstream digest verification.

Paths beneath the existing `KFM_DATA_ROOT`:

| Path | Responsibility |
|---|---|
| `data/raw/noaa-ghcnd/<run>/metadata/` | Immutable station/inventory/directory snapshots, version and field documentation |
| `data/raw/noaa-ghcnd/<run>/stations/<id>.csv.gz` | Immutable compressed source records |
| `data/work/noaa-ghcnd/<run>/plan.json` | Explicit station selection and capture limits |
| `data/work/noaa-ghcnd/<run>/station-index-<digest>.geojson` | Unreleased location/coverage inspection index; no climate-value interpolation |
| `data/receipts/ingest/noaa-ghcnd/<run>/` | Immutable source headers, hashes, inspections and attempt reports |

Placement follows accepted [Directory Rules](../doctrine/directory-rules.md)
DIR-EXEC-002/007, DIR-SOURCE-001, DIR-STORAGE-001 and the lifecycle/accountability
split. Source parsing/transport belongs in the existing
`connectors/noaa/src/noaa/` package; filesystem orchestration in
`tools/local_data/`; behavior tests in `tests/local_data/`; procedure in `docs/`.
This extends existing responsibility roots without introducing a competing
source registry, schema home, or release authority.

## Failure, recovery and downstream use

Rerunning the same plan rehashes existing completed objects before reuse. Network
failures leave the run `PARTIAL`, preserve completed files, and report missing
station IDs. A provider-size, CRC, date or format error never creates a successful
station receipt. A crash between RAW commit and receipt requires explicit
inspection; the tool does not overwrite that object. A killed process can leave
the existing `.local-data.lock`; establish that the writer ended before manual
lock cleanup. Symlink/special-file, hash, storage and reserve failures stop work.

The station index is WORK for inspection. Neither the browser nor the hosted
Site gets direct access to the private store. Captured originals are protected,
unreviewed candidates: source/rights/sensitivity review, element/unit and quality
policy, evidence binding, map projection and release remain open. No catalog
activation, D1/R2 import, new map layer or source admission is implied.
For a released layer, preserve observation date separately from retrieval time,
carry evidence references and flag semantics, and expose only the reviewed
projection through KFM's governed route.

Rollback reverts code; retain originals and receipts. No old data or existing
EE/PRISM/GHCNDEX assets need to be removed. Use focused tests:

```bash
python3 -m unittest tests.local_data.test_noaa_ghcnd -v
```

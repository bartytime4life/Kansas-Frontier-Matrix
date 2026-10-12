<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/noaa-nwm-local-capture
title: Bounded National Water Model capture for Kansas
type: runbook
version: v1
status: implementation-candidate; private-WORK-only
owners: ["@bartytime4life"]
created: 2026-10-07
updated: 2026-10-07
policy_label: public
owning_root: docs/
responsibility: Explain bounded source capture, local verification and recovery without model activation.
truth_posture: Verified capture and tests do not establish source admission, review or release.
[/KFM_META_BLOCK_V2] -->

# National Water Model data on the local PC

The [requested NOMADS directory](https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/)
is a rolling collection of model runs, not a durable historical climate archive.
It includes analysis/assimilation, short-, medium- and long-range forecasts,
ensembles, land/terrain grids, reservoirs, forcing, other regions and coastal
products. A recursive mirror would download large, frequently replaced and
overlapping products. The [NOAA model description](https://water.noaa.gov/about/nwm)
and [output dictionary](https://water.noaa.gov/about/output_file_contents)
explain the configurations and units.

## Selected useful subset

The operator captures one complete CONUS short-range **18-hour streamflow run**
and its same-filename-cycle `analysis_assim.channel_rt.tm00` snapshot: 19 NetCDF4
files. The parent listing and complete set of forecast filenames select the
cycle; exact HEAD byte sizes and Last-Modified values are then frozen in the
plan. The capture fails if those identities change. It never silently switches
to a later cycle or substitutes another product.

Channel files contain reach IDs without their map geometry. The accompanying
[NOAA reference flowlines](https://maps.water.noaa.gov/server/rest/services/reference/static_nwm_flowlines/FeatureServer/0)
query selects lines intersecting `[-102.052,36.993,-94.588,40.004]` in EPSG:4326.
This is a **Kansas envelope**, not an exact state-boundary clip: border reaches
and nearby out-of-state portions remain. The captured object-ID list fixes the
selection; 500-ID requests must return every requested ID without truncation.
No geometry simplification, invented centroid, interpolation or inferred river
topology is applied.

The NetCDF files are indivisible CONUS source objects (about 235 MB for the
initial selection). Private WORK projections contain only the selected reaches:
compressed GeoJSON flowlines and compressed CSV streamflow, velocity and
assimilation adjustment (`nudge`). All other original channel variables remain
available in the retained NetCDF files. Forcing, restart files, land/terrain
grids, reservoir outputs, other regions and additional forecast cycles are not
needed for this streamflow capture and are not selected.

## Limits and repeat runs

- **512 MiB aggregate** across all retained `noaa-nwm` RAW, WORK and receipt runs,
  measured using the greater of file size and allocated file blocks.
- **100 GiB minimum free-space reserve**, checked before every new write.
- 16 MiB per channel file, 4 MiB per reference page, 192 MiB of reference pages,
  64 MiB of compressed WORK outputs, 125,000 selected reaches and 30 minutes per
  capture invocation. Metadata and receipt overhead count toward the aggregate.
- Sequential bounded requests; no recursive downloader, background scheduler,
  deletion, eviction, paid service, credentials or public data serving.

`prepare` makes a small metadata capture, obtains model HEAD sizes and refuses
an over-budget plan before model transfer. `capture` preserves already receipted
files and downloads only missing objects. A second cycle still shares the same
512 MiB cap; the cap is not reset by changing the run label. A cap or free-space
failure leaves completed captures intact. Capacity changes require an explicit
operator decision; this tool has no automatic expansion or cleanup.

## Commands

Use Linux x86_64, Python 3.11 or 3.12, and the existing initialized private
external KFM store. Preparation and capture use the standard library. Binary
verification additionally needs the optional, hash-locked reader:

```bash
python -m pip install --require-hashes --only-binary=:all: -r tools/ci/python-nwm.lock
python tools/local_data/noaa_nwm.py prepare --root "$HOME/Projects/KFM-data" --run 20261007T180550Z
python tools/local_data/noaa_nwm.py capture --root "$HOME/Projects/KFM-data" --run 20261007T180550Z
python tools/local_data/noaa_nwm.py verify --root "$HOME/Projects/KFM-data" --run 20261007T180550Z
```

For a new capture choose a new UTC timestamp run label. Reuse the same label to
resume or verify an existing capture. NOMADS retention is short; a missing old
object is reported as unavailable, not replaced with a different cycle. No
automatic archive fallback is implemented. A killed writer may leave the store
lock; inspect that process before clearing a stale lock. A RAW file without its
receipt is held for inspection rather than overwritten or trusted on retry.

`verify` independently rehashes every source, checks NetCDF dimensions, reach-ID
uniqueness/join completeness, product, units, packing and both scalar and global
time metadata, then deterministically builds WORK projections. It preserves
packed values and flags missing/out-of-range values; those decoded CSV values
are blank, never zero-filled. Each variable's original packing and units are
retained in `subset-metadata.json`.

## Time and source integrity

Filename cycle, initialization/reference time, valid time and retrieval time
are distinct. In the initial 2026-10-07 16Z selection, the analysis initializes
at 13:00Z and is valid at 16:00Z; the forecast initializes at 16:00Z and is valid
hourly from 17:00Z through 10:00Z the following day. Never relabel the analysis
as initialized at the filename hour. Earlier planning metadata is retained
locally, with an append-only corrected plan binding this distinction.

The captured model declares `v3.1`, while the reference geometry's `nwm_vers`
attribute declares `3.0`. Both values remain visible. Successful ID joining is
necessary but does not establish geometry/version compatibility or source
review. Model guidance is neither observed discharge nor an official RFC river
forecast or emergency warning. The frozen capture becomes historical context
as time advances; it must not be displayed as live data.

No provider checksum was supplied by these responses. SHA-256 verifies local
captured-byte identity only. TLS source URL, size, Last-Modified, ETag when
available and retrieval timestamps are retained. Multiple reference queries
are dated captures, not a globally atomic snapshot of the mutable service.

## Placement and delivery boundary

Paths are relative to the existing external `KFM_DATA_ROOT`:

| Path | Responsibility |
|---|---|
| `data/raw/noaa-nwm/<run>/metadata/` | Original directory, documentation, geometry layer and ID snapshots |
| `data/raw/noaa-nwm/<run>/models/` | Original 19 CONUS NetCDF4 channel files |
| `data/raw/noaa-nwm/<run>/flowlines/` | Original NOAA Kansas-envelope reference-query responses |
| `data/work/noaa-nwm/<run>/plan-v2.json` | Frozen selection, byte bounds and filename-cycle expectations |
| `data/work/noaa-nwm/<run>/kansas-envelope-flowlines.geojson.gz` | Unreleased geometry projection keyed by `feature_id` |
| `data/work/noaa-nwm/<run>/kansas-envelope-streamflow.csv.gz` | Unreleased selected model values keyed by reach and time |
| `data/work/noaa-nwm/<run>/subset-metadata.json` | Source/model versions, time semantics, units, packing and limitations |
| `data/receipts/ingest/noaa-nwm/<run>/` | Per-object hashes/headers, capture bound to plan hash, verification |

Placement follows accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and [Directory Rules](../doctrine/directory-rules.md), especially
DIR-EXEC-002/007, DIR-DATA-004 and DIR-STORAGE-001. Source acquisition belongs
under existing `connectors/noaa/src/noaa/`; private filesystem orchestration
under `tools/local_data/`; deterministic model projection under the registered
`pipelines/domains/hydrology/` lane; tests under `tests/local_data/`; audit-only
delivery receipts under `data/receipts/generated/`. No parallel source registry,
schema authority or release home is created.

This does not modify the Site's existing NOAA reach API or authorize it to read
private RAW/WORK files. Later map use needs geometry/version review, source
admission, rights/sensitivity/validation checks and a governed released carrier.
Rollback consists of reverting the code changes and leaving immutable captured
sources and receipts available for audit; no service or scheduler needs to be
stopped. Removal of protected data is a separate explicit retention decision.

## Verified local capture

The [capture record](../../data/receipts/generated/noaa-nwm-kansas-capture-20261007.json)
records 101,599 reaches and 1,930,381 reach-time rows across 19 frames, with all
selected geometry IDs matched. Compressed outputs were independently rehashed,
read through gzip CRC validation, and counted. There are 19,950 missing
streamflow rows and 19,950 missing velocity rows; their sentinels/status remain
explicit, not converted to zero. The collection uses approximately 470 MB,
including source originals, WORK outputs, planning history and receipts.

## Validation

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_python_ci.py nwm-netcdf
make local-data-check
```

The existing local-data workflow installs the finite hash-locked NWM reader
profile and runs offline tests. Fixtures cover partial cycles, year rollover,
HTTP size/redirect handling, aggregate/free-space caps, corruption and resume,
geometry truncation/IDs/CRS, packed missing values, differing analysis time,
forecast time mismatch and deterministic compressed output. Passing these tests
does not establish source admission, map rendering, human review or release.

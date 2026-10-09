<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/raw-data-intake
title: Analyze raw data and route it to the right place
type: runbook
version: v1.0
status: implemented; local verification; owner acceptance pending
owners: ["@bartytime4life"]
created: 2026-10-09
updated: 2026-10-09
policy_label: public-documentation
owning_root: docs/
responsibility: Explain the intake pipeline, its loopback desk and Explorer summary, placement rules across local store, database, WORK lane, Git and GitHub releases, and the GitHub storage budget.
truth_posture: CONFIRMED synthetic local tests and a local browser run; NEEDS VERIFICATION native-PC acceptance on real holdings and owner review of the storage policy.
related:
  - docs/runbooks/local-pc-data-store.md
  - docs/runbooks/github-data-baseline.md
  - tools/local_data/README.md
  - tools/local_data/catalogs/github-storage-budget.json
[/KFM_META_BLOCK_V2] -->

# Analyze raw data and route it to the right place

The intake pipeline answers one question for every file already on this PC:
**what is it, and where does it belong?** It reads the private
`KFM_DATA_ROOT` store prepared by the [local-PC runbook](local-pc-data-store.md),
profiles each file by its content, recommends a placement, records everything in a
local SQLite index, and applies a placement only when you ask. It never downloads,
uploads, commits, deletes, admits a source, or turns a file into a map layer.

| Part | File | What it does |
|---|---|---|
| Analyzer | [`intake_profile.py`](../../tools/local_data/intake_profile.py) | Identifies format from magic bytes; reads extent, CRS, time coverage, structure and review hints with bounded reads |
| Projections | [`intake_crs.py`](../../tools/local_data/intake_crs.py) | Offline inverse projections for Kansas State Plane North/South (m and US ft), UTM 13–15N, CONUS Albers and Web Mercator |
| Router | [`intake_route.py`](../../tools/local_data/intake_route.py) | Deterministic placement rules and the GitHub storage guard |
| Pipeline & index | [`intake.py`](../../tools/local_data/intake.py) | Discover → profile → route → index → explicit apply; CLI |
| Backend & desk | [`intake_service.py`](../../tools/local_data/intake_service.py), [`intake_desk/`](../../tools/local_data/intake_desk/index.html) | Loopback JSON API and standalone GUI on `127.0.0.1:8771` |
| Explorer | [`intake-desk-summary.tsx`](../../apps/site/source/app/intake-desk-summary.tsx) | Read-only summary on **Data & downloads → My library** |
| Storage policy | [`github-storage-budget.json`](../../tools/local_data/catalogs/github-storage-budget.json) | GitHub limit, reserved interface room and committed usage |

Everything uses the Python 3.11+ standard library. GDAL, pyproj and network access
are not required.

## Quick start

```bash
export KFM_DATA_ROOT="$HOME/KFM-data"          # an initialized store (see local-pc-data-store.md)
python3 tools/local_data/intake.py budget      # GitHub storage summary; needs no store
python3 tools/local_data/intake.py analyze     # profile RAW and QUARANTINE files
python3 tools/local_data/intake_service.py --inbox "$HOME/Downloads/KFM"
```

Open <http://127.0.0.1:8771/> in a browser on the same computer. Use that exact
address; `localhost` is refused so a hostile web page cannot rebind a name to this
service. Press **Analyze store**, filter by status, lane, format, domain or text,
or drag a box on the Kansas map to find files by area. Select a file to see what
was found and where each part of it belongs.

When the local Explorer runs on port 4173, **Data & downloads → My library** shows
the same totals and GitHub budget with a link to the desk.

## What is analyzed

| Lane | Included | Notes |
|---|---|---|
| `data/raw/**` | Every regular file | Hashed up to `--hash-limit` (default 4 GiB) |
| `data/quarantine/<source>/objects/sha256/<digest>/payload` | Captured payloads | Declared source, dataset, version, rights and sensitivity come from the capture bindings |
| `--inbox DIR` | Downloads not yet captured | Read-only; always routed to **capture first** |

Hidden names, credential/config names and runtime folders are skipped, as in the
library scan. Symbolic links and special files are counted and skipped, never
followed. `data/work/intake/` (the desk's own output) is not rescanned. A rerun
reuses the stored profile of any file whose size and modification time are
unchanged. A file that disappears is marked missing; its history stays.

Recognized formats: GeoTIFF/TIFF and BigTIFF, zipped or loose shapefiles
(`.shp` header, `.prj`, `.dbf` fields), GeoPackage and SQLite (opened read-only,
immutable and defensive), GeoJSON, KML/KMZ, CSV with latitude/longitude columns,
GeoParquet, PMTiles v3, LAS point clouds, PDF and GeoPDF markers, PNG, JPEG with
EXIF GPS, and NetCDF/HDF5/GRIB/gzip/tar by signature only. Zip members are listed
and their headers read without extraction.

### Three clocks stay separate

| Field | Meaning |
|---|---|
| `content_start` / `content_end` | Dates found inside the data (date columns, KML `<when>`, EXIF capture time) |
| `file_metadata_time` | When the file says it was written (TIFF `DateTime`, PDF `CreationDate`) |
| `path_year_hint` | Years in the file name, such as `1997-1998` — a hint, not evidence |

### Extent and Kansas check

Native bounds are transformed to WGS84 by densifying the box edges, then compared
with the Kansas envelope as `inside`, `overlaps`, `outside` or `unknown`. NAD83 and
WGS84 are treated as coincident; NAD27 is flagged `datum_nad27_approximate`. The
formulas reproduce the EPSG Guidance Note 7-2 Lambert example and Snyder's Albers
example to centimetres. They are for screening, not survey work. Unsupported
systems are reported as `crs_not_transformable_offline`, never guessed.

## Where things go

Every file receives one decision with five placements:

| Placement | Rule |
|---|---|
| **Local PC store** | Always. Bulk bytes stay in `KFM_DATA_ROOT`. |
| **Intake database** | Always. Profile, decision and extent are indexed in `data/work/intake/index.sqlite`, with an R*Tree for map searches. |
| **WORK review lane** | *Stage copy* when the format is recognized and a domain is known. The copy goes to `data/work/intake/<domain>/<source>/<dataset>/`. Inbox files must be captured first. |
| **Git repository** | *Metadata card* only — never file bytes — and only for `redistribution: allowed`, `sensitivity: public`, no review flags. |
| **GitHub release** | *Candidate* only for public, redistributable, Kansas-relevant files that fit the budget. Files under 1 MiB are *bundled* with their collection; files over 1.8 GB are split into parts. |

The decision **status** is `ready` (nothing held), `review` (rights,
sensitivity, review flags, domain or capture to settle) or `blocked` (unsafe zip
paths or unreadable content). Review flags come from names and fields that
suggest cultural sites, living persons, rare species, critical infrastructure or
exact photo locations. They hold sharing; they do not delete anything.

Raw files have no declared rights, so they stay in `review` until captured.
Capture them with `manage.py describe`, set `rights` and `sensitivity` in the
reviewed manifest, then `plan` and `sync`, as in the
[local-PC runbook](local-pc-data-store.md). The next analysis picks up the
declarations from the quarantine bindings.

## GitHub storage budget

GitHub is limited to **100 GB** for this project. The policy file keeps
**20 GB permanently reserved for code, interface and feature work**, leaving an
80 GB data ceiling — the same ceiling the
[curated baseline release](github-data-baseline.md) already uses.

```bash
python3 tools/local_data/intake.py budget
```

At this commit the committed usage is 234,924,032 bytes of repository history plus
36,710,723,546 bytes in the `curated-data-20261008` release, leaving about
43.05 GB for new curated data. The loader checks the release figure against the
baseline manifest and reports `baseline_check: match` or `mismatch`. After
publishing a new release, add a `committed` entry with its exact asset bytes.
The desk warns at 85% of the data ceiling and denies candidates that would exceed it.

`release-plan` selects candidates greedily in domain/path order until the budget
is spent and lists the rest as deferred. It is a plan for owner review; nothing
is uploaded.

## Command reference

```bash
python3 tools/local_data/intake.py analyze [--inbox DIR] [--hash-limit BYTES]
python3 tools/local_data/intake.py overview
python3 tools/local_data/intake.py list [--status ready|review|blocked] [--lane raw|quarantine|inbox] \
    [--domain D] [--family F] [--text T] [--bbox=MINLON,MINLAT,MAXLON,MAXLAT] [--limit N] [--offset N]
python3 tools/local_data/intake.py show ITEM_ID
python3 tools/local_data/intake.py apply ITEM_ID stage     # verified WORK review copy + receipt
python3 tools/local_data/intake.py apply ITEM_ID card      # metadata card + receipt
python3 tools/local_data/intake.py release-plan
python3 tools/local_data/intake.py cards > ~/kfm-cards.json
python3 tools/local_data/intake.py budget
```

All commands print JSON. Errors go to standard error as
`{"outcome": "ERROR", "error": CODE}` with exit status 2.

### Loopback API

| Method and path | Purpose |
|---|---|
| `GET /` | The Intake Desk (session token embedded; strict CSP; no external resources) |
| `GET /api/status` | Job state; adds `sessionToken` only for allowlisted Explorer origins |
| `GET /api/overview` | Totals by status, domain, format and lane; GitHub budget |
| `GET /api/items?status=&lane=&domain=&family=&text=&bbox=&limit=&offset=` | Filtered list (max 500 per page) |
| `GET /api/items/{id}` | Full profile, decision and applied actions |
| `GET /api/extents?…` | GeoJSON boxes of matching files for the desk map |
| `GET /api/budget`, `GET /api/release-plan` | Storage state and plan |
| `POST /api/analyze {"includeInbox": bool}` | Start the background analysis |
| `POST /api/cancel {}` | Stop it after the current file |
| `POST /api/apply {"id", "action": "stage" or "card"}` | Apply one recommended placement |

The service binds `127.0.0.1` only and requires `Host: 127.0.0.1:8771`. A request
carrying an `Origin` must come from the desk itself, the local Explorer
(`http://127.0.0.1:4173`) or the owner's hosted Explorer. Every `POST` also needs
the per-process `X-KFM-Session` token, a JSON body under 4 KiB, and no chunked
encoding. The browser never chooses a file-system path; the inbox is fixed when
the service starts.

## Outputs and recovery

| Path under `KFM_DATA_ROOT` | Content |
|---|---|
| `data/work/intake/index.sqlite` | The intake database (WAL mode, private permissions) |
| `data/work/intake/<domain>/…` | Staged review copies (verified copies, never hard links) |
| `data/work/intake/cards/<id>.json` | Metadata cards for repository review |
| `data/receipts/intake/<id>/…json` | One immutable receipt per applied action |

The index can be rebuilt at any time: stop the service, move `index.sqlite` aside,
and run `analyze` again. Receipts, staged copies and cards are never overwritten. A
second writer waits for the first (`INTAKE_BUSY`). To undo a staged copy, remove
that copy after review; its receipt stays as history.

## Validation

```bash
make local-data-check                                     # includes tests/local_data/test_intake.py
cd apps/site/source && node --test tests/intake-desk.test.mjs
```

The Python tests build tiny synthetic files: GeoTIFFs, a shapefile zip, LAS,
PMTiles, an EXIF photo, GeoJSON, CSV, PDF and KML. With them they check:

- the projection worked examples
- every reader, plus the zip safety flags
- the routing and budget rules
- the full pipeline on a temporary store, including the single-writer lock and cancellation
- the HTTP handler in-process, as the no-network test environment requires

Passing tests do not establish source admission, scientific validity or acceptance
on a native Windows host.

## Limits and next steps

- NetCDF/HDF5/GRIB contents, LAS coordinate systems (stored in VLRs) and GeoPDF
  georeferencing are not parsed yet; they are reported as explicit gaps.
- Domain inference uses names and fields only. Declare the domain at capture when
  it matters.
- The desk does not edit manifests or rights. Use `manage.py` for capture
  declarations.
- Staged WORK copies are review material. Normalization, PROCESSED outputs,
  catalog entries, release and map activation remain separate governed steps.

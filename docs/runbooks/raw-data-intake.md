<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/raw-data-intake
title: Analyze raw data and route it to the right place
type: runbook
version: v1.1
status: implemented; local verification; owner acceptance pending
owners: ["@bartytime4life"]
created: 2026-10-09
updated: 2026-10-11
policy_label: public-documentation
owning_root: docs/
responsibility: Explain the intake pipeline, its loopback desk and Explorer summary, placement rules across local store, database, WORK lane, Git and GitHub releases, and the GitHub storage budget.
truth_posture: CONFIRMED base contracts and targeted local tests; NEEDS VERIFICATION real-holdings reanalysis, host installation and owner review.
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
uploads, commits, deletes, or admits a source. The optional local atlas offers
bounded private map previews while retaining review holds; it does not release
datasets or publish map layers.

| Part | File | What it does |
|---|---|---|
| Analyzer | [`intake_profile.py`](../../tools/local_data/intake_profile.py) | Identifies format from magic bytes; reads extent, CRS, time coverage, structure and review hints with bounded reads |
| Projections | [`intake_crs.py`](../../tools/local_data/intake_crs.py) | Offline inverse projections for Kansas State Plane North/South (m and US ft), UTM 13–15N, CONUS Albers and Web Mercator |
| Router | [`intake_route.py`](../../tools/local_data/intake_route.py) | Deterministic placement rules and the GitHub storage guard |
| Pipeline & index | [`intake.py`](../../tools/local_data/intake.py) | Discover → profile → route → index → explicit apply; CLI |
| Backend & desk | [`intake_service.py`](../../tools/local_data/intake_service.py), [`intake_desk/`](../../tools/local_data/intake_desk/index.html) | Loopback JSON API and standalone GUI on `127.0.0.1:8771` |
| Explorer | [`intake-desk-summary.tsx`](../../apps/site/source/app/intake-desk-summary.tsx) | Read-only summary on **Data & downloads → My library** |
| Storage policy | [`github-storage-budget.json`](../../tools/local_data/catalogs/github-storage-budget.json) | GitHub limit, reserved interface room and committed usage |

The base intake pipeline uses the Python 3.11+ standard library. GDAL, pyproj and
network access are not required for that path. Optional atlas raster/shapefile
previews require an explicitly selected trusted Python with rasterio, numpy and
pyshp; projection-grid networking remains disabled. See the
[consolidation runbook](kfm-projects-consolidation.md) for those bounded previews.

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
| `data/quarantine/<source>/objects/sha256/<digest>/payload` | Captured payloads | Declarations come only from bindings with the same source directory and digest; the declared source must match the directory |
| `--inbox DIR` | Downloads not yet captured | Read-only; always routed to **capture first** |

Hidden names, credential/config names and runtime folders are skipped, as in the
library scan. Symbolic links and special files are counted and skipped, never
followed. `data/work/intake/` (the desk's own output) is not rescanned. A rerun
reuses the stored profile of any file whose size, modification time and capture
declaration are unchanged. Changed declarations refresh source-derived domain,
filename and review hints too. Identical bytes captured by different sources
retain separate provenance, rights, sensitivity and binding counts. A payload
without a matching source binding has unknown rights and stays held for sharing.
A file that disappears is marked missing; its history stays.

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
sensitivity, review flags, domain or capture to settle), `reviewed` (operator
accepted this file for local use; sharing remains held), or `blocked` (unsafe zip
paths or unreadable content). Review flags come from names and fields that
suggest cultural sites, living persons, rare species, critical infrastructure or
exact photo locations. They hold sharing; they do not delete anything.

Raw files have no declared rights, so they initially stay in `review`. For a
capture declaration, use `manage.py describe`, set `rights` and `sensitivity` in
the reviewed manifest, then `plan` and `sync`, as in the
[local-PC runbook](local-pc-data-store.md). The next analysis picks up the
declarations from the quarantine bindings.

### Complete a review in the Working Data desk

Select a file and use **Review this file** in its details drawer. Enter your name
and a review note, choose a decision, confirm the file, and click **Save review**:

- **Reviewed — keep on this PC** removes it from the pending review queue and
  increments **Reviewed · local**. Unknown rights or sensitivity may remain
  unknown; Git and release routing stay on hold.
- **Approve for public routing** requires a domain, allowed redistribution,
  public sensitivity, and a rights reference or license. File blockers, sensitive
  content flags, explicit capture restrictions and routing holds still apply.
  This enables eligible metadata/routing plans; it does not upload or publish.
- **Reopen — needs review again**, under **Change or reopen review**, restores
  the original analyzer decision. Previous decisions remain in **Review history**.

Decisions apply to one indexed file and SHA-256, not a whole source or future
captures. They persist through reanalysis, but become inactive if file bytes or
the captured context/profile changes. The original capture declaration is not
rewritten. Each decision creates a private receipt in
`data/receipts/intake/<item_id>/review-<uuid>.json` and an append-only index history.
The imported archive catalog and read-only desks cannot save decisions.

## GitHub storage budget

The owner limits GitHub-hosted KFM material to **100 GB** for this project.
This includes Site source in Git history, release assets and recorded CI
artifacts/caches. It does not cap local PC storage and is not a GitHub platform
quota. The policy file keeps
**20 GB permanently reserved for code, interface and feature work**, leaving an
80 GB data ceiling. The archives from the
[curated baseline release](github-data-baseline.md) have been retired; its retained metadata remains accounted for.

```bash
python3 tools/local_data/intake.py budget
```

The ledger records 244,829,184 provider-reported repository bytes, 42,312 bytes
for the baseline release's three retained metadata assets, 6,150,059 artifact
bytes and 7,064,414,678 cache bytes. The total is 7,315,436,233 bytes, leaving
about 72.68 GB beneath the 80 GB working ceiling. The repository and CI entries
are historical estimates; CI storage is mutable and LFS needs separate
accounting if used. Re-read the ledger before an upload.

The loader checks the retired release's historical archive size against the
preserved baseline manifest and reports `baseline_check: retired` when they
match. A discrepancy reports `mismatch`; active releases continue to report
`match` or `mismatch`. After publishing a new release, add a `committed` entry
with its exact asset bytes. The desk warns at 85% of the data ceiling and denies
candidates that would exceed it.

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
| `GET /` | Public Intake Desk shell (no session token; strict CSP; no external resources) |
| `GET /api/status` | Authenticated job state; adds `sessionToken` only for authenticated Explorer origins |
| `GET /api/overview` | Totals by status, domain, format and lane; GitHub budget |
| `GET /api/items?status=&lane=&domain=&family=&text=&bbox=&limit=&offset=` | Filtered list (max 500 per page) |
| `GET /api/items/{id}` | Full profile, decision, applied actions and review history |
| `GET /api/extents?…` | GeoJSON boxes of matching files for the desk map |
| `GET /api/budget`, `GET /api/release-plan` | Storage state and plan |
| `POST /api/analyze {"includeInbox": bool}` | Start the background analysis |
| `POST /api/cancel {}` | Stop it after the current file |
| `POST /api/apply {"id", "action": "stage" or "card"}` | Apply one recommended placement |
| `POST /api/review` | Save a digest-bound operator decision with expected review revision, domain, rights, sensitivity, reference, reviewer, note and explicit confirmation; desk origin only |

The service binds `127.0.0.1` only and requires `Host: 127.0.0.1:8771`. A request
carrying an `Origin` must come from the desk itself, the local Explorer
(`http://127.0.0.1:4173`) or the owner's hosted Explorer. Every `POST` also needs
the per-process `X-KFM-Session` token, a JSON body under 4 KiB (16 KiB for review notes), and no chunked
encoding. The browser never chooses a file-system path; the inbox is fixed when
the service starts.

## Outputs and recovery

### Refresh indexes created before source-scoped bindings

Earlier Intake Desk versions matched quarantine declarations by digest alone.
Identical bytes captured under different sources could inherit another source's
provenance and permissions. This confirms a code defect, not that any particular
store or output was affected.

After updating the code, stop the old desk service and restart it with the updated
code. Choose **Analyze store** (or run `python3 tools/local_data/intake.py analyze`
with the correct `KFM_DATA_ROOT`). Existing indexes containing quarantine records
return `INTAKE_REANALYSIS_REQUIRED` for item views, overview, cards, release plans
and apply actions until a complete pass has refreshed their bindings. Cancelled
or failed passes leave this hold in place. Source bytes, existing cards, staged
copies and immutable receipts are preserved. Previously exported cards or plans
need regeneration and review before use; reanalysis does not validate or rewrite
those older outputs.

### Stored outputs

| Path under `KFM_DATA_ROOT` | Content |
|---|---|
| `data/work/intake/index.sqlite` | The intake database (WAL mode, private permissions) |
| `data/work/intake/<domain>/…` | Staged review copies (verified copies, never hard links) |
| `data/work/intake/cards/<id>.json` | Metadata cards for repository review |
| `data/receipts/intake/<id>/…json` | One immutable receipt per applied action |

The index can be rebuilt at any time: stop the service, move `index.sqlite` aside,
and run `analyze` again. Receipts, staged copies and cards are never overwritten. A
second writer is rejected with `INTAKE_BUSY` and may retry after the first
finishes. To undo a staged copy, remove
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

### Private browser connection

Each service start prints private connection links in its operator terminal.
Open the link for the browser origin you use. The `kfm-downloads`, `kfm-intake`,
or `kfm-basemap` URL fragment provisions that service's per-process capability;
the browser removes the fragment and keeps it in memory and tab-scoped session
storage. Fragments are not sent in HTTP requests. Open each service's link in
the same Explorer tab to connect multiple companions, and open the Intake Desk
link separately for its standalone UI. After a service restart, open its new
link. A bare URL does not provision authority.

Every private API GET and POST requires `X-KFM-Session`, including status and
catalog reads. The Intake Desk HTML/CSS/JS shell is public and contains no
capability. Host, Origin, CORS and PNA checks remain browser protections; they
do not identify an OS user. Keep terminal output and connection links private.
The capability does not isolate the service from code that can read the owner's
terminal or browser state. Earth Engine OAuth callbacks continue to use their
separate expiring, single-use state and PKCE checks.

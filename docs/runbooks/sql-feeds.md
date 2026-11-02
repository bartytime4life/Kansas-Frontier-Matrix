# SQL feeds on the pipeline PC

`tools/local_data/sql_feeds.py` keeps the pipeline PC's local SQL database
(`observations.sqlite`, beside the TIGER and NWM GeoPackages) growing from new
public source data.

The owner asked for this on 2026-11-01, approving four things:

- automatic review of the three hourly capture sources;
- backfills of IEM wind readings (2003–2026) and ASOS 5-minute data (2001–);
- PRISM at both 4 km and 800 m, keeping only Kansas;
- a private NetCDF reader, so NWM loads one run a day.

The public local-data API serves these tables. The feeds only add data.

## Rules every feed follows

- **Only new data.** Each feed fetches what is new since its recorded state
  (`kfm_feed_state`). It also re-fetches what the provider revises, as the
  table below says.
- **Kansas only.** Providers that serve national files are cut to Kansas at
  once:
  - PRISM grids are clipped to the Kansas window.
  - The GHCN daily update files, Storm Events files and NWM runs are cut to
    Kansas rows.

  The kept raw copy, under `data/raw/sql-feeds/<feed>/`, is the Kansas part. Its
  receipt, under `data/receipts/ingest/sql-feeds/<feed>/`, records the URL, the
  retrieval time, `Last-Modified`, and the full download's size and SHA-256
  (`"kept": false`).
- **One transaction per source file**, keyed by SHA-256 in `kfm_sql_sources`. A
  rerun skips what is loaded, an interrupted load leaves nothing behind, and an
  identical answer is never loaded twice.
- **The lock covers writes only.** Downloads run outside `run/pipeline.lock`;
  only database writes take it. Captures and backups are held for seconds, not
  for a download.
- **The ceilings still apply.** These are the original SQL build's 85 GB
  aggregate ceiling, less a 5 GB reserve, and its 100 GB free-space floor.
  Reaching one stops the feed with `CEILING_85GB_HEADROOM_STOP` or
  `FREE_SPACE_FLOOR_REACHED`.

## Feeds

| Feed | Source | What it adds | Revisions |
|---|---|---|---|
| `captures` | Hourly USGS streamflow, NWS alerts and USGS earthquake captures | Reviews new captures automatically, then loads features into `kfm_environmental_features` | — |
| `iem-wind` | IEM `asos.py` / `daily.py`, 68 Kansas stations | Readings to yesterday (31 days per request) and daily summaries; one backfill year of readings per run, 2003 → 2026-10-31 | — |
| `ghcnd` | NCEI `superghcnd_diff_*` daily update files | Kansas inserts, updates and deletes into `kfm_ghcnd_daily_revisions`; Kansas stations refreshed from `ghcnd-stations.txt` every 30 days | The API serves the newest revision over the archived station file |
| `storm-events` | NCEI Storm Events CSV files | A year whose details, locations or fatalities file is newer is reloaded | The newer file replaces that year's rows; the old source is marked `superseded`. Columns NCEI adds at the end are added as `TEXT` |
| `asos-5min` | NCEI TD-6401, KCNK KDDC KGLD KICT KTOP | One year per run from 2001 | NCEI's archive ends in 2022; afterwards the feed only checks for a newer folder |
| `prism` | PRISM `services.nacse.org` BIL grids, 9 variables, 4 km and 800 m | County cell-center summaries into `kfm_prism_grids` / `kfm_prism_county_stats` for each new day (up to 7 a run while catching up), month and year | Days are fetched again at 8 and 35 days, months at 3 months, years in July. A changed grid is stored as `…zip#sha256=<12 hex>`, and the API serves the newest |
| `nwm` | NWM 12Z analysis on `noaa-nwm-pds` | 101,599 Kansas reaches into `kfm_nwm_channel_rt`, up to 7 days a run | — |

**Captures review.** The automatic review applies the checks of the
2026-10-31 manual review:

- a matching capture receipt;
- SHA-256 and byte count;
- the GeoJSON structure.

It records reviewer `sql-feeds automatic capture policy`. A capture that fails a
check stays in review, and the feed reports why.

**PRISM counties.** County summaries use the cells whose centers fall in each
2025 TIGER county, with NODATA excluded. This reproduces the archived summaries'
cell counts for all 105 counties.

## Install and run

**Install:**

    pc-pipeline-data/run/install-sql-feeds.sh SOURCE_CHECKOUT

This copies the 14 modules and 2 budget catalogs the feeds need into
`pc-pipeline-data/runtime/releases/sql-feeds-<digest>/`, writes
`runtime/sql-feeds.env`, and enables these timers (local time):

| Feed | Runs |
|---|---|
| `captures` | hourly at :25 |
| `iem-wind` | 01:05 |
| `ghcnd` | 04:05 |
| `asos-5min` | 05:05 |
| `nwm` | 09:35 |
| `prism` | 13:05 |
| `storm-events` | Mondays at 04:35 |

None runs during the 02:30 backup.

**Run one feed by hand:**

    pc-pipeline-data/runtime/sql-feed.sh FEED

**Status of every feed:**

    python -m tools.local_data.sql_feeds --root STORE --db DB status

**Logs:**

    journalctl --user -u 'kfm-sql-feed@*'

The `nwm` feed runs with `~/.cache/kfm-nwm-venv/bin/python`. That environment
has binary wheels only:

- `netCDF4` 1.7.5.1.post1, its stable-ABI wheel, since dev runs Python 3.14 and
  the pinned 1.7.4 has no wheel for it;
- `numpy` 2.5.4.

Every other feed uses only the standard library.

## Backup

The per-file nightly backup would store a new full copy of a database that
changes every hour, and it never deletes old copies. So on 2026-11-01 the owner
chose a separate nightly copy of the database, keeping the newest two:

    pc-pipeline-data/runtime/sql-feed.sh snapshot DEST [--lock-held]
    pc-pipeline-data/runtime/sql-feed.sh snapshot-check DEST

`snapshot` (`tools/local_data/sql_snapshot.py`) works like this:

- It copies the database page by page with SQLite's backup API, while the
  pipeline lock keeps writers out, to `DEST` on another device. The copy is a
  standalone rollback-journal file.
- The copy must pass `PRAGMA quick_check` and match the source's
  `kfm_sql_sources` counts and page count. It is then renamed to
  `observations-<UTC time>-<first 12 hex of its SHA-256>.sqlite`, with a receipt
  in `DEST/receipts/`.
- Only then are copies older than the newest two deleted. Their receipts stay.
- A failed or interrupted copy deletes nothing, and the copy refuses to leave
  the backup volume under 20% free (`SNAPSHOT_SPACE_FLOOR`).
- An unchanged database is not copied twice, but only if the kept copy still
  has the bytes its receipt records. If it doesn't, the new copy is published
  and the command exits 1 with `SNAPSHOT_RETAINED_MISMATCH`, since the backup
  volume changed a kept copy.
- One snapshot or check runs at a time per destination (`.snapshot.lock`, held
  from cleanup to pruning); another gets `SNAPSHOT_BUSY`. Each run first removes
  what an interrupted one left: partial copies, and a renamed copy whose
  receipt was never published. Files with other names are never touched.

The 02:30 backup runs it with `--lock-held`, since `runtime/backup.sh` already
holds the lock; run by hand, it takes the lock itself.

The monthly restore test runs `snapshot-check`. It re-hashes the newest copy
against its receipt, runs `PRAGMA integrity_check`, and compares the counts.

The per-file backup leaves the database out because it is listed in the
pipeline config's `separateBackup`. That list, and the steps to restore from a
copy, are in the pipeline runbook, `docs/second-pc-pipeline.md` on the hosted
branch.

## Failure and recovery

A failed run logs `feed_failed` with a fixed reason. It changes no state, so the
next timer run retries. Common reasons:

- `HTTP_<code>`, `FETCH_FAILED`: the provider was unavailable.
- `STORM_COLUMNS_CHANGED`: NCEI removed or renamed a column.
- `RAW_OBJECT_CHANGED`: a provider's bytes changed under a name already kept.
- `PIPELINE_LOCK_BUSY`: the lock was held for more than 15 minutes.

Partial runs recover without stalling or skipping:

- **PRISM:** a grid not yet posted keeps its target in `retry`, and the next
  runs fetch it first. After 60 days it is given up and listed in `given_up`. An
  incomplete revision check is not marked, so it stays due.
- **NWM:** days gone from the bucket are recorded in `missing_days`, and the
  cursor moves past them.
- **Storm Events:** an NCEI re-release whose Kansas rows are unchanged is
  recorded in `seen`, so the year stops being due.

Raw copies and receipts are immutable, and a kept copy is byte-identical when
rebuilt from the same download. A load can be repeated from them by deleting its
`kfm_sql_sources` row and its data rows in one transaction.

## Verification

`tests/local_data/test_sql_feeds.py` runs the feeds against fake providers.
NWM's test runs when netCDF4 is installed.

The first run on dev, 2026-11-01:

| Feed | Result |
|---|---|
| `captures` | 72 waiting captures reviewed, 75 capture files loaded |
| `ghcnd` | 23 update files, 98,317 Kansas rows, current to Oct 31 |
| `iem-wind` | 2,470 daily summaries; 408,185 backfilled 2003 readings |
| `asos-5min` | 2001: 60 files, 465,161 readings |

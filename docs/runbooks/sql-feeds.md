# SQL feeds on the pipeline PC

## Record recovery evidence without running a feed

The [browser-local recovery desk](../../apps/review-console/recovery-desk.md) records IEM wind, USGS daily and Wikidata Kansas recovery evidence. Its PR #5751 baseline is a dated source snapshot, with historical journal and test totals labelled author-reported. Current installed identity, preserved database state and after-change outcomes require separate evidence. The desk never starts ingestion, installs a release, fetches a provider or connects to operational tables. Export/import moves local working notes and preserves history; imported claims need fresh review.

A merged source change, a passing client test and an accepted local reviewer note each have narrower scope than installed-machine or actual feed recovery. Follow the guide to record observations already obtained under separate owner authorization.

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
- **No size ceiling and no free-space floor.** The owner asked on 2026-11-02 to
  ignore all data caps and floors. A full disk surfaces as an ordinary write
  failure, so watch the volume's free space.

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

## Kansas sources added 2026-11-02

On 2026-11-02 the owner asked to "fatten the database with usable data on
Kansas" and chose these sources. They go into this database only; publishing
any of them on the website is a separate decision.

The same day the owner set the rule for them: "if it is public knowledge do not
stop from adding it to the KFM database." Public records are kept whole, names
included. For example, the KGS files keep lease names, operators and water-well
owners.

They follow the rules above. Two core helpers in `sql_feeds.py` serve them:

- **`download` and `temp_path`.** A file too large to hold in memory, such as
  NASS crops at 1.1 GB, is streamed to `tmp-sql-feeds/` in the store. That
  folder is outside `data/`, so the per-file backup never sees a half-written
  download. Temp files are deleted after each load.
- **`load_version`.** Some providers publish the same file again over time: a
  year's file, or a bulk export. Each new version loads under a stable key
  (`results/2024`, `qs.crops`). The version before is deleted and marked
  `superseded` in the same transaction. A new download with unchanged content
  keeps no second copy.

| Feed | Source | Tables | Each run, and revisions |
|---|---|---|---|
| `usgs-daily` | USGS Water Data OGC API (`api.waterdata.usgs.gov/ogcapi/v1`): `combined-metadata`, `daily` | `kfm_usgs_series`, `kfm_usgs_sites`, `kfm_usgs_daily_values` | Backfills up to 300 series records a run, within USGS's 1,000 requests an hour without a key. A statewide "modified since" window picks up new and revised values; there is one row per series and day, and a revision replaces it. Six records are re-read in full each run |
| `usgs-peaks` | OGC `peaks` | `kfm_usgs_peaks` | The statewide answer every 30 days, replacing the last |
| `usgs-groundwater` | OGC `field-measurements` | `kfm_usgs_field_measurements` | Year files, backfilled from 1860. Years with changed rows are fetched again, and every year once a year |
| `water-quality` | Water Quality Portal `Result` and `Station` | `kfm_wqp_results` (47 columns; the kept copy has all of them), `kfm_wqp_stations` | Year files, backfilled from 1901. The current and previous year are fetched weekly, the three before monthly, older years yearly |
| `climdiv` | NCEI nClimDiv | `kfm_climdiv_monthly`, `kfm_climdiv_normals`, `kfm_climdiv_county_divisions` | Each newer dated release of a file replaces it. Kansas is NCEI state 14; counties are stored by GEOID |
| `drought` | U.S. Drought Monitor statistics service | `kfm_usdm_county_stats`, `kfm_usdm_state_stats` | A key per year, fetched again when a weekly map is due |
| `air-quality` | EPA AirData daily files and `file_list.csv` | `kfm_aqs_daily`, `kfm_aqs_daily_aqi_county`, `kfm_aqs_sites`, `kfm_aqs_monitors` | A key per pollutant and year. The recent three years are fetched again when EPA's Created date advances; older years at most yearly |
| `nass` | USDA NASS Quick Stats bulk files | `kfm_nass_quickstats` | A kind is reloaded when NASS publishes a newer file, at most every 30 days. At most two kinds a run; crops runs alone |
| `kgs-oil-gas` | Kansas Geological Survey `PRS/Ora_Archive` | `kfm_kgs_wells`, `kfm_kgs_leases`, `kfm_kgs_tops`, `kfm_kgs_lease_production`, `kfm_kgs_wwc5_wells`, `kfm_kgs_wwc5_lithology` | Each file again when its listed time changes, at most every 28 days. Four files a run |
| `fema` | OpenFEMA | `kfm_fema_disaster_declarations`, `kfm_fema_nfip_claims`, `kfm_fema_nfip_policies`, `kfm_fema_pa_projects`, `kfm_fema_hma_subapplications` | The whole Kansas extract of a dataset when FEMA's refresh date changes. Pages by record id |
| `earthquakes` | USGS ComCat, the Kansas box | `kfm_usgs_earthquakes` (`county_geoid`, `in_kansas`) | One small "updated since" request. When anything changed, and every 30 days, the whole box is fetched and the changed years are replaced. Events just over the state line are kept with `in_kansas=0` |
| `tornadoes` | SPC `1950-YYYY_all_tornadoes.csv` | `kfm_spc_tornadoes` | When the file name changes or every 28 days. The "all" file is used because it includes state segments |
| `nws-warnings` | IEM VTEC events by state | `kfm_iem_vtec_events` | A key per year from 1986. The current year is fetched every run |
| `cdc-places` | CDC PLACES county and tract datasets | `kfm_cdc_places_county`, `kfm_cdc_places_tract` | Every 28 days. Each release is keyed by dataset id and year |
| `census-acs` | ACS 5-year table-based summary files on `www2.census.gov` | `kfm_census_acs_values`, `kfm_census_acs_geographies`, `kfm_census_acs_variables` | Each table's national file is cut to the 9,944 Kansas geographies, plus 704 ZCTAs with ZIP prefix 66 or 67. A file is loaded again when its listed time changes. At most 40 tables or 2 GB a run. `ACS_TABLES` holds 76 curated tables (`None` loads all 1,198); `ACS_VINTAGES` holds 2024 |
| `census-decennial` | 2020 Census: P.L. 94-171 and DHC Kansas files | `kfm_census_decennial_values`, `kfm_census_decennial_geographies`, `kfm_census_decennial_variables` | Loads state through block group, places and districts, 24 segments a run. Block values are left out, but the PL block rows are kept in the geography table. After loading it rechecks yearly |
| `eia-seds` | EIA State Energy Data System bulk file | `kfm_eia_seds_series`, `kfm_eia_seds_values`, `kfm_eia_seds_categories`, `kfm_eia_seds_category_series` | Loaded again when SEDS's `last_updated` changes, at most every 30 days. One key replaces all four tables at once |

**USGS services.** USGS retires all remaining legacy WaterServices and NWISWeb
pages between November 2026 and February 2027, so these feeds use only the OGC
API.

**Not available:**

- The Census API needs a key, so the census feeds use the Bureau's bulk files
  instead.
- BLS refuses requests that carry no contact email, and the owner chose to skip
  BLS.
- The Water Quality Portal's legacy profile has no USGS samples after March
  2024, when USGS moved to WQX 3.0.

**Backfill:** most feeds finish in one run.

| Feed | Runs |
|---|---|
| `usgs-daily` | about 6 |
| `usgs-groundwater` | about 3 |
| `water-quality` | about 5 |
| `air-quality` | about 6 |
| `kgs-oil-gas` | 4 |
| `nws-warnings` | 4 |
| `nass` | 3 |
| `drought` | 3 |
| `census-acs` | 3 |
| `census-decennial` | 2 |

## Feeds recovered after the November 3 PC rebuild

The 31 feeds below were reconstructed from the surviving kept downloads, receipt
keys, feed state and database schemas. They use the same source identities and
version keys, so an unchanged download does not reload existing rows. The
`newspaper-text-rebuild` command also restores retained OCR extracts without
network access; it is a repair command, not another scheduled feed.

| Feeds | Providers | Main table families |
|---|---|---|
| `airports`, `obstacles`, `dams`, `mines`, `grade-crossings`, `rail-lines` | FAA NASR/DOF, USACE NID, USGS/MSHA, FRA/BTS | `kfm_nasr_*`, `kfm_faa_*`, `kfm_nid_*`, `kfm_mrds_*`, `kfm_usmin_*`, `kfm_msha_*`, `kfm_fra_*`, `kfm_narn_*` |
| `gnis-names`, `post-offices`, `county-boundaries`, `ceded-lands`, `railroads-history`, `congress-kansas`, `nps-places`, `nrhp` | USGS GNIS, historical post-office and railroad collections, Newberry AHCB, USFS, unitedstates/congress-legislators, NPS | `kfm_gnis_*`, `kfm_post_*`, `kfm_ahcb_*`, `kfm_usfs_*`, `kfm_atack_*`, `kfm_congress_*`, `kfm_nps_*`, `kfm_nrhp_*` |
| `pbdb`, `macrostrat`, `radiocarbon`, `neotoma`, `idigbio-fossils` | Paleobiology Database, Macrostrat, p3k14c, Neotoma, iDigBio | `kfm_pbdb_*`, `kfm_macrostrat_*`, radiocarbon, `kfm_neotoma_*`, `kfm_idigbio_*` |
| `banks`, `exempt-orgs`, `museums-libraries`, `schools`, `historical-topo-maps`, `usgs-samples` | FDIC, IRS, IMLS, NCES/IPEDS, USGS topoView and Samples Data | `kfm_fdic_*`, IRS, `kfm_imls_*`, `kfm_nces_*`, `kfm_ipeds_*`, USGS maps and samples |
| `wikidata-kansas`, `plss-grid` | Wikidata Query Service and BLM public ArcGIS layers | `kfm_wikidata_*`, `kfm_blm_plss_*` |
| `bridges`, `epa-facilities`, `newspaper-text`, `osm-kansas` | FHWA NBI, EPA FRS, Library of Congress, Geofabrik/OpenStreetMap | `kfm_nbi_*`, `kfm_frs_*`, `kfm_newspaper_*`, `kfm_osm_*` in the separate bulk database |

The six `sql_feed_structures`, `sql_feed_places`, `sql_feed_deeptime`,
`sql_feed_institutions`, `sql_feed_wikidata_plss` and `sql_feed_bulk` module
headers describe each provider URL, refresh interval, pagination limit, license,
kept-file format and receipt key. A daily timer invokes each feed; its saved
state determines whether any download is due. Provider throttling or a schema
change stops the affected run and retains the previous completed version.

Bulk feeds require **both** `--db observations.sqlite` and
`--bulk-db bulk-sql/kfm-bulk.sqlite`, pointing to different files. Both databases need their own verified SQLite snapshots.
The full-copy snapshot implementation still reads and verifies the entire file;
this rebuild does not implement the previously proposed changed-chunk backup.

Recovery compatibility checks are in `test_sql_feed_rebuild.py` and the
schema-only `fixtures/recovered-feed-schema.json`. They cover 122 existing tables,
indexes, revision rollback, multi-table retirement, bulk routing, resumable
Wikidata groups, PLSS point widths, full-text indexes and quoted CSV newlines.
They contain no production rows. On the owner's PC, the separate recovery audit
also replays preserved raw files and compares counts and sampled values against
the read-only databases. It must pass before activating the rebuilt schedules.

The retained OSM layer manifests do not contain their geometries; they cannot be
used alone to rebuild the derived layer tables. The first approved refresh
re-downloads the monthly shapefile archive and may supersede these layers once
because the original manifest hash convention was not recovered. The retained
PBF remains independently replayable. Wikidata scalar coordinates use the first
provider coordinate; the full geometry preserves every point and county matching
can use another point. Date precision remains explicit: a year is not expanded
to an invented January 1 observation.

## Feeds added after the recovery

These three feeds are new designs. They live in `sql_feed_texts.py`, whose
header records the provider details.

| Feed | Source | Tables | Each run and revisions |
|---|---|---|---|
| `archive-texts` | Internet Archive Scrape, metadata and `_djvu.txt` (bulk database) | `kfm_ia_items`, `kfm_ia_texts`, `kfm_ia_texts_fts`, `kfm_ia_text_status` | Listing every 28 days; about 300 items a run, at least 1 s between requests; re-downloaded when the MD5 changes; items that stop qualifying are retired; 429/503 stops with `IA_RATE_LIMITED` |
| `newspaper-directory` | LOC Directory of U.S. Newspapers, Kansas facet | `kfm_loc_newspaper_directory` | Every 28 days; 70 pages at least 6 s apart; resumes from a spool; a changed directory replaces the old one |
| `towers` | FCC ASR weekly `r_tower.zip`, from FCC's web servers, which answer this pipeline 403 | `kfm_asr_registrations`, `_locations`, `_entities`, `_history`, `_remarks`, `_special_conditions` | Every 7 days; Kansas cut per record type; `FCC_BLOCKED` in state if no route serves it |

| `census-acs-full` | ACS 5-year table-based summary files on `www2.census.gov`, 2021-2024, every table (bulk database) | `kfm_census_acs_values`, `kfm_census_acs_geographies`, `kfm_census_acs_variables` | Each table's national file is cut to Kansas and loaded in transactions of at most 1M rows or 60 seconds, with the lock free between them. A run lasts about 45 minutes and resumes where the last stopped; about 40-70 runs. A file is loaded again when its listed time changes. Firewall-rejected tables are listed under `rejected` and retried |
| `census-decennial-full` | 2020 Census: P.L. 94-171 and DHC Kansas files, every table and iteration with block values (bulk database) | `kfm_census_decennial_values`, `kfm_census_decennial_geographies`, `kfm_census_decennial_variables` | Same short transactions and resume. About 20-60 runs. Continues the bulk database's `census-decennial` state; afterwards it rechecks yearly, and a changed zip reloads what changed |

| `gbif` | GBIF occurrence search and dataset registry (bulk database) | `kfm_gbif_occurrences`, `kfm_gbif_datasets`, `kfm_gbif_segments`, `kfm_gbif_dataset_queue` | Up to 400 requests and 30 minutes a run, 1 s apart. Plans segments of at most 10,000 records, then loads the smallest first, one `load_version` key each. Stops with `GBIF_RATE_LIMITED` on 429/403 and `GBIF_UNAVAILABLE` on 5xx, HTML or connection failure, keeping finished segments. After the backfill, segments with recent years are checked every 28 days and older ones every 365, re-fetched only if `lastInterpreted` shows changes; dataset records every 182 days |
| `loc-kansas` | loc.gov JSON API: photos, maps, HABS/HAER/HALS, Chronicling America titles and issues | `kfm_loc_items`, `kfm_loc_newspaper_titles` | Up to 50 pages a run, 6 s apart. Buckets every 28 days, title list every 7, a title's issues when its listing changes and every 182 days. Stops with `LOC_RATE_LIMITED` on 429, 403 or HTML; a segment that keeps failing waits for the next run (`LOC_UNAVAILABLE`). No images or OCR text |

`towers` has no timer and has loaded nothing. FCC's web servers refuse this
pipeline. An anonymous FTP server holds the file, but no FCC page we could read
names it as a route, so the feed does not use it. Add a timer if FCC stops
refusing the web routes or documents another one.

`archive-texts` runs daily at 23:45, with a second slot at 12:10 during the
backfill of about 30 to 40 runs. `newspaper-directory` runs on Thursdays at 17:15.
`gbif` runs at 00:10 and 12:30 and `loc-kansas` at 17:20. GBIF advises its
download API for long scripted pulls, but that needs a registered account, which
this feed does not use; a registered download could replace the search backfill.
About 364,000 GBIF records are CC BY-NC. Each row keeps its license, so check it
before publishing any of them.

During their backfills `census-decennial-full` runs at 05:15, 09:15, 13:15, 17:15
and 21:15, and `census-acs-full` at 07:15, 11:15, 15:15, 19:15 and 23:15. Drop each
to one daily run once its backfill finishes.

The two Census backfills take the bulk database to about 112 GB, so its full
snapshot would take 4.5 to 6.5 hours. On this PC it runs weekly, on Sundays at
03:15, through a `kfm-bulk-snapshot.timer.d` override. The raw-file backup stays
nightly.

## Install and run

**Install:**

    pc-pipeline-data/run/install-sql-feeds.sh SOURCE_CHECKOUT

This copies the 22 modules and 2 budget catalogs the feeds need into
`pc-pipeline-data/runtime/releases/sql-feeds-<digest>/`, writes
`runtime/sql-feeds.env`, and enables these timers (local time):

| Feed | Runs |
|---|---|
| `captures` | hourly at :25 |
| `iem-wind` | 01:05 |
| `usgs-groundwater` | 01:35 |
| `ghcnd` | 04:05 |
| `asos-5min` | 05:05 |
| `climdiv` | 05:35 |
| `usgs-daily` | 06:05 |
| `earthquakes` | 06:35 |
| `nws-warnings` | 06:50 |
| `air-quality` | 07:05 |
| `water-quality` | 08:05 |
| `nwm` | 09:35 |
| `fema` | 10:05 |
| `drought` | 10:35 |
| `prism` | 13:05 |
| `nass` | 14:05 |
| `kgs-oil-gas` | 15:05 |
| `census-acs` | 16:05 |
| `census-decennial` | 16:35 |
| `storm-events` | Mondays at 04:35 |
| `tornadoes` | Wednesdays at 11:05 |
| `cdc-places` | Thursdays at 11:35 |
| `eia-seds` | Fridays at 12:05 |
| `census-decennial` | 16:35 |
| `usgs-peaks` | Sundays at 17:05 |

None runs during the 02:30 backup. The large loads are spaced so that two
rarely overlap. On most days most feeds only read a listing; each feed decides
for itself what is due.

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

## Spatial sidecars

Every feed table with a `geometry_geojson` column, or the four `min_lon`,
`min_lat`, `max_lon`, `max_lat` columns the OSM tables carry, has an R-tree
sidecar `<table>_rtree(id, min_lon, max_lon, min_lat, max_lat)` whose `id` is
`file_id << 32 | row_number` (`tools/local_data/sql_spatial.py`). The website's
`near-observations` and `near-bulk` questions join it to the table for "what is
in this map area" without scanning: in development measurements on a database
copy, a bounding box over 2.26 million OSM elements took 11.7 s by scan and
0.01 s through the sidecar. This does not qualify an operational PC installation.

- `kfm_spatial_index` records the `file_id` values each sidecar covers and the
  table's greatest `file_id`. `sql_feeds.py run FEED` refreshes the written
  database's sidecars after a successful run: superseded files' entries are
  deleted by key range, new files' entries added. A failure is logged as
  `spatial_index_failed` and does not fail the feed.
- A reader treats a sidecar as stale when the table's greatest `file_id` differs
  from the record, and refuses the collection (`DATASET_NOT_READY`) until the
  next refresh.
- `sql_feeds.py … spatial build [--table T]` reconciles every sidecar under the
  pipeline lock (both databases when `--bulk-db` is given); `spatial check`
  reports each one as `current`, `stale` or `missing` read-only and exits 1
  when any is not current. The first build on a copy of the bulk database took
  45 s for the 2.26 million OSM elements (through their box columns), 888 thousand
  NBI bridges (through their GeoJSON) and the OSM places together.
- Every supplied database path must exist, including an explicitly supplied
  `--bulk-db`; a missing path fails before any build writes. With `--table T`,
  only databases containing that geometry table are built or checked. If both
  contain it, both must pass; if neither does, the command reports
  `SPATIAL_TABLE_UNKNOWN`. Omitting optional `--bulk-db` selects only `--db`.
- Rows with no geometry, unreadable or empty GeoJSON, a box outside the planet
  or inverted, or a `row_number` of 2^32 or more get no entry and are counted
  as `skipped`.

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

### The bulk database

The bulk database gets a different nightly job, because it is growing to about
112 GB and a full verified copy of that takes 4.5 to 6.5 hours. About 95% of that
time is `PRAGMA quick_check` walking the b-trees on a spinning disk: 1,192 of the
1,225 seconds for the 8.3 GB copy of 2026-11-03.

    python -m tools.local_data.sql_chunks snapshot --db kfm-bulk.sqlite --dest DEST [--keep 2]
    python -m tools.local_data.sql_chunks check --dest DEST [--level quick|integrity]
    python -m tools.local_data.sql_chunks restore --dest DEST --manifest NAME --to FILE [--level integrity|quick]

`snapshot` (`tools/local_data/sql_chunks.py`) works like this:

- It opens one read transaction and reads every page in file order through
  `sqlite_dbpage`, so it sees one commit, WAL frames included. It takes no pipeline
  lock, writes nothing to the database and never checkpoints its WAL. Feeds keep
  committing, and the WAL grows by what they commit until the read ends.
- It cuts the bytes into 4 MiB chunks and writes those the store lacks to
  `DEST/chunks/ab/<sha256>.z`, compressed. Stored chunks are not read again.
- After a `syncfs` of the backup volume it renames
  `DEST/manifests/<stem>-<UTC time>-<first 12 hex of its SHA-256>.json` into place.
  Only then are copies past the newest `--keep` removed, then the chunks nothing
  uses. The newest copy with a check receipt is also kept, whatever `--keep` says.
- A killed or failed run leaves the kept copies as they were. Every run starts by
  removing the chunks no manifest names, which is what such a run left behind.
- A database whose file and WAL have the same size and times as at the newest copy
  is not read at all.
- It does **not** run `quick_check`. Until the next `check`, a copy is known to hold
  the bytes that were read, not that they form a healthy database.

`check` rebuilds the newest copy in `DEST/staging/` (it needs the database's size
free), re-hashes every chunk and the whole file, runs `quick_check` and compares
the counts, then re-hashes the chunks only older kept copies use. It records a
receipt in `DEST/checks/`. A chunk that fails its hash moves to `DEST/quarantine/`,
the command exits 1 with `SNAPSHOT_CHUNK_DAMAGED`, and the next snapshot writes the
chunk again if the database still holds those bytes. `integrity_check` also
compares every index with its table, which at this size on a spinning disk is
for a restore you intend to use, not for the weekly job.

Measured on 2026-11-04, replaying the real Census and newspaper loaders on a
throwaway copy of the database (4 MiB chunks):

| Night | Size after | Old chunks changed | New chunks | Written, compressed |
| --- | --- | --- | --- | --- |
| First load of new tables (22.6 million rows, FTS5) | 11.2 GB | 0.2% | 26% of the file | about 0.5 GB |
| Backfill, 203 million rows | 34.1 GB | 28% | 67% | about 4 GB |
| Backfill, 204 million rows | 57.0 GB | 73% | 40% | 6.3 GB |
| Quiet: one archive-texts run | 57.2 GB | 0.2% | 0.2% | 0.09 GB |
| `VACUUM` (no feed runs it) | 14.1 GB | 100% | | the whole file |

The last two compressed figures were measured by this tool. The first two are
estimates from its measured ratio, about 6.3 to 1 for a whole file.

During a backfill most of the file is written again, because index inserts touch
pages all over it: 9.5% of pages changed, but those pages sit in 73% of the chunks.
There the job is cheap because of compression (7.6 to 1) and because it skips
`quick_check`, not because chunks repeat. Chunks repeat once the backfill ends.

`restore` rebuilds a named copy to a new file, runs `integrity_check` and gives the
file its name only if that passes. The file is a standalone rollback-journal
database. To put it back, stop the feeds and the local-data gateway, remove
`kfm-bulk.sqlite-wal` and `-shm`, and move it over `kfm-bulk.sqlite`; the feeds
switch it back to WAL on their next open.

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

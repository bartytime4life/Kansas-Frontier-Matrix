<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/local-data-integration-audit-20261008
title: Local data integration and integrity audit
type: report
version: v0.1
status: local-verification; repository-review-pending
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: public-documentation
owning_root: docs/
responsibility: Record workstation storage, connection, repair and verification scope without granting source admission.
truth_posture: CONFIRMED dated local measurements and bounded checks; NEEDS VERIFICATION source admission and hosted equivalence.
[/KFM_META_BLOCK_V2] -->

# Local data integration and integrity audit

The October 8 audit started from repository main
`ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe` and reconciled the same preserved
Site's saved version 185, source `ecc8921b715959095bafcd7bc201bc4f14b5b7c6`.
The primary PC checkout was clean and fast-forwarded from `ca790057d3` to that
main. The independent working branch preserves other worktrees.

## Storage decision and coverage

The canonical external store contained **58,902,183,552 bytes in 268,308 files**
at the detailed audit snapshot. Counts change as existing acquisition and the
repairs below progress. That exceeds the owner's **25,000,000,000-byte** condition,
so dataset payloads remain outside Git and have not been moved into the repo.
After archive recovery and the protected PRISM catalog backup, the October 8
16:03:51 UTC snapshot contained **66,236,349,588 bytes in 269,588 files**. The
existing PRISM acquisition can continue to change that dated count.
Recovery backups, references, active Site state and two separate candidate
stores were identified independently; they are not interchangeable data roots.

| Collection | Verified connection and present limits |
| --- | --- |
| Reviewed Earth Engine context | Five installed 2024 layers: CDL, CHIRPS, TerraClimate, Sentinel-2 and 3DEP. The active R2 manifest, indexes and 15,806 tiles match their recorded hashes. Other years/products are not inferred to be installed. |
| Basemap cache | The existing loopback cache uses the canonical data root and retains the 10 GB cache bound. All 480 cached objects matched their index hashes and accounted storage. |
| Local map PDFs | All 596 PDFs, totaling 1,617,135,252 bytes, match the current Site's metadata index. There are 185 with embedded controls awaiting review and 411 needing manual control; this is local discovery, not automatic georeferenced activation. |
| PRISM | Local rasters and county summaries feed review packages. Two derived numeric defects were corrected as described below. Two grids still lack source unit evidence. The prior held review snapshot is retained. |
| NOAA GHCN-Daily | 2,519 captured stations and 51,522,960 observations in the local candidate collection, with capture hashes verified. Site provider queries do not automatically consume this entire local archive. |
| NOAA National Water Model | The stored candidate has 101,599 reaches, 19 frames and 1,930,381 rows with verified raw/derived hashes. Its forecast ends October 8 at 10:00 UTC; model v3.1/geometry v3.0 compatibility remains under review. It is not observed discharge. |
| Census TIGER 2025 | 7,566 extracted/metadata files match the prior inventory. All 1,083 missing original ZIPs were recovered and passed exact SHA-256, size and CRC checks. Vintage boundaries remain source context. |
| NOAA FTP and airport winds | Historical source files and dated derived captures are retained. A missing duplicate NOAA archive is explained by the prior cleanup receipt and member identity proof. Dated captures are not live provider responses. |
| NOAA normals and USGS water pilot | Explicit separate candidate stores remain accounted for; folder presence does not grant release or serving authority. |
| References and recovery | Reference documents and immutable recovery copies are retained as references/backups, not map observations. |

Every local dataset is not automatically a rendered layer. Existing reviewed
display connections, metadata discovery, candidate processing and source-specific
review requirements are distinct. This audit does not admit, release, activate,
or publicly serve arbitrary RAW/WORK/QUARANTINE contents.

## Application and connection repairs

- Crop-CASMA requests now have a bounded body/deadline and cancellation. Missing,
  held or invalid data removes stale rendered/visible state; the selected control
  can still be turned off when its data becomes unavailable.
- Earth Engine rejects an active baseline pointer for the wrong year. Concurrent
  requests share validation of the same tile index, with bounded pending entries;
  settled results are evicted so later corruption/deletion is still detected.
  Individual tile digests remain checked.
- Restored the current saved Site's Earth Engine download/setup and Underground
  resource views while retaining newer repository storm, map lifecycle, timeline,
  soil, favicon and security fixes. The resource endpoint uses the Worker's
  supported manual redirect mode and rejects redirected provider responses.
- Restored the installed local Earth Engine operator, provider adapter, pinned
  requirements and runbook into source control. Existing canonical local-store
  helpers remain authoritative. The operator is reachable; Google project login
  remains an owner step and no account authorization was performed here.
- The installed PC basemap-cache service now matches the canonical local
  operator, including bounded gzip decoding and header validation. Companion
  code and tests stay in `tools/local_data` and `tests/local_data`; the Site
  calls the loopback service and does not package a filesystem operator.
- Reconciled lockfile metadata removes a malformed optional Sharp entry; the
  declared dependency versions and integrity pins are retained.

## Library and background download interface

The local `/downloads` page brings collection search, role filters, pagination,
reviewed display periods and persistent worker jobs into one view. It is linked
from the map's Data & downloads menu, the Earth Engine workspace and acquisition
receipts. A selected dataset still has its direct download action and size limit.

The existing loopback operator now scans collection metadata in the background.
The initial scan measured 40 collections in 0.56 seconds; it reads no dataset
payloads. The installed service's 16:11 UTC snapshot contained 263,131 eligible
files totaling 60,619,762,184 logical bytes. This subset covers RAW, WORK,
QUARANTINE and PROCESSED; recovery receipts, catalog backups, hidden entries,
credentials and runtimes are excluded. It is distinct from the full 66.24 GB
store measurement above. Scan dates and retained prior snapshots stay visible.

Only the established local Site origin connects automatically. Hosted pages
retain an explicit local connection action. Host, origin and session checks
remain in force. Scans have entry, collection, depth and time limits; unsafe,
changing or unreadable trees fail explicitly without replacing complete totals.

Jobs continue in the operator after navigation. Progress uses completed files
when a total is known, otherwise a labeled indeterminate bar; the selected byte
maximum is never presented as a completion percentage. Cancellation and partial
file retention remain visible. Polls have bounded bodies and deadlines, cannot
overlap within a view, pause in hidden tabs and refresh on return. Pointer styles
reflect enabled actions, editable text, disabled controls and busy actions while
preserving map and range gestures. Library discovery needs no Google login;
provider downloads still require the owner's project authorization.

## PRISM derived-data correction

The two out-of-range county means were reproducible float32 accumulation errors,
not changed raster pixels. Reapplying the exact original county masks with
float64 accumulation gives Allen County `0.09000000357627869` and Stanton County
`0.009999999776482582` hPa, equal to each row's minimum and maximum.

The repair checked original TIFF and boundary digests and full catalog row
preconditions, preserved a transactional SQLite backup, and updated exactly two
mean fields. Raster bytes, source digests, units and historical review receipts
were unchanged. The curator's single-line accumulator fix was installed; four
numerical integration tests and two application rehearsals passed.

The acquisition service was subsequently stopped under its existing lock for a
controlled recovery. Five original partial/metadata files (45,089,028 bytes) and
the exact affected catalog rows were preserved before retrying 15 existing
failures: two read timeouts and 13 DNS errors. All 15 recovered through the
original SHA-256, ZIP CRC, raster and transactional catalog checks. The retry
received 631,625,582 bytes within a 1 GiB limit; the 16:26:43 UTC snapshot showed
213,795 complete grids, 244,020 indexed grids and zero errors.

The service restarted at 16:26:29 UTC and completed its interrupted March 14,
2023 precipitation grid. Independent recalculation of all 105 county means
matched float64 exactly; two differed from the old float32 result, confirming
the live process loaded the fix. Recovery and verification records remain in
the private `runtime/prism-restart-20261008T162434Z/` directory. Two separate
missing-unit records remain `null` and held pending source evidence.

## Archive recovery

The prior source inventory retained all extracted TIGER components, but 1,083
original ZIP paths were absent before this audit. Two exact originals survive in
quarantine; the other 1,081 have recorded Census URLs, sizes and SHA-256 values.
Recovery downloaded **1,772,631,724 original payload bytes** and reused the two
retained originals, restoring **1,866,577,596 bytes across all 1,083 ZIPs**.
Each original passed exact size, SHA-256 and ZIP CRC before no-overwrite
installation. HTTP error/HTML/rate-limit responses were never accepted.

The transfer completed with **zero failed originals**. A separate final readback
rechecked all 1,083 original hashes, sizes and ZIP CRCs. The initial rate-limited
run's interruption receipt is retained alongside the successful throttled run
`20261008T155339Z-original-recovery-throttled` in the private source receipt lane.
Its final recovery receipt SHA-256 is
`7ec1deade5ab3069af6e95b395def91f3fe6a2cff20a0cf8255481a26dd23e36`.
The complete private audit is retained in
`data/catalog/local-data-audit-20261008/`; source admission and map activation are
unchanged.

## Local installation and verification

The reconciled application was installed as a new source directory behind the
existing stable Site alias. The physical v109 D1/R2 state and origin
`http://127.0.0.1:4173` were retained. A stopped-writer backup matched all
**18,410 state files / 917,505,475 bytes** before source cutover. The previous
source, service definition, cache script and backup remain available for recovery.
No hosted Site deployment or audience change is part of this local update.
The final download-center build and local operator were installed with their
own source backups, unchanged storage bindings and successful health readback.

Initial verified checks:

- 46,971 historical/package/receipt/display checksum comparisons passed;
  separately, all 596 current PDFs and all runtime R2 objects were checked.
- Ten SQLite databases passed structural integrity checks. One idle cache needed
  a stable, before/after-hashed copy because its read-only WAL open was unavailable.
- Production build, 662 Site tests, TypeScript and full Site lint passed;
  lint retains 45 warnings and zero errors.
- 224 local-data/governed-API Python tests and 44 subtests passed; eight standalone
  cache tests and 13 subtests passed.
- Three smoke-startup isolation tests, eight mirror tests, and 56 offline backend
  checks across 46 routes passed. Nine provider-only routes remain explicitly
  outside that offline smoke.
- The local browser rendered MapLibre and the reviewed-period controls. Its
  download connection showed the canonical local destination and the truthful
  Google project setup requirement. This is bounded browser smoke, not complete
  accessibility/device/WebGL or provider-service acceptance.

Final download-center checks:

- Production build and all **673 Site tests** passed. TypeScript passed; full
  lint has zero errors and the same 45 existing warnings.
- **192 local-data tests / 47 subtests**, **11 mirror/smoke-isolation tests** and
  the 56-check offline backend smoke passed. The real mirror receipt check
  separately retains `MIRROR_REVIEW_REQUIRED`.
- Independent browser evaluation passed at 1440, 768 and 375 pixels. Search,
  role filters, pagination, background refresh, visible scan dates, hover/busy/
  disabled/text cursors and keyboard focus handoff were exercised. Reduced-motion
  behavior is covered by the actual callback regression test. No browser errors
  were observed. The independent evaluator used the same provider because a
  second-provider tool was unavailable.
- No live Earth Engine login, download or cancellation was performed; those
  states have deterministic contract/callback coverage. The worker's job count
  is explicitly labeled Earth Engine and does not claim to monitor the separate
  PRISM acquisition service.
- Both new documentation metadata blocks are valid. The metadata workbench's
  overall result still fails on seven pre-existing structural findings in the
  unchanged document registry (duplicate keys and malformed/incomplete entries).
  The two new documents are review-only registry addition candidates; this audit
  does not rewrite the governed registry to obtain a passing result.
- Hosted topology validation caught duplicate basemap companion files inside
  the deployable Site mirror. They were removed in favor of the existing
  canonical operator/test locations; launch guidance was corrected. No topology
  rule or baseline was weakened. The installed cache service is unchanged.

Private file-level audit and recovery records remain under the owner's existing
external catalog/receipt/recovery lanes. No secrets, absolute personal inventory
or payloads are copied into this report. Historical `MIRROR_REVIEW_REQUIRED`
receipts remain unchanged; passing code checks does not clear that hold.

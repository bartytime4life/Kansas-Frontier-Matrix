<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/earth-engine-downloads
title: Selected Earth Engine downloads and local library
type: runbook
version: v1.0
status: implemented; local verification; provider authorization pending
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: public-documentation
owning_root: docs/
responsibility: Explain bounded local library inspection, selected provider downloads, authorization, storage and recovery.
truth_posture: CONFIRMED bounded local contracts; NEEDS VERIFICATION live provider authorization and source admission.
[/KFM_META_BLOCK_V2] -->

# Selected Earth Engine downloads

The Earth Engine workspace has **Sign in with Google Earth Engine** and a
dataset/year download control. It talks only to the owner-operated loopback
service on `127.0.0.1:8769`. The hosted Site cannot write arbitrary local files.

## Install once

Use Python 3.11 or newer. From a checkout containing this change:

```sh
python3 -m venv "$HOME/Projects/KFM-ee-runtime"
"$HOME/Projects/KFM-ee-runtime/bin/python" -m pip install -r connectors/google/earth_engine/requirements.txt
"$HOME/Projects/KFM-ee-runtime/bin/python" tools/local_data/earth_engine_downloads.py serve --root "$HOME/Projects/KFM-data"
```

The root must already be an initialized, owner-private KFM local store. Keep the
operator running, or install it as an owner user service. Both the local Site
(`http://127.0.0.1:4173`) and the existing private hosted KFM Site are allowlisted.
The browser may request local-network access. Other origins and Host values are
denied; writes also require the per-process in-memory session token.

## Link Google and download

Open **Data & downloads → Library & downloads** to search what is already stored,
refresh its dated inventory, inspect approved map periods and follow all recent
worker jobs. The established local Site connects automatically; hosted pages
offer an explicit local connection. Library inspection does not require Google
sign-in. From the center, **Choose data to download** opens the catalog below.

1. Open **Earth Engine datasets & recipes**, choose a dataset and year.
2. Enter the Google Cloud **project ID**, found in the account menu of the
   [Earth Engine Code Editor](https://code.earthengine.google.com/).
3. Press **Sign in with Google Earth Engine**, select the Google account, and
   approve Google's consent screen. If a popup is blocked, use **Continue with
   Google**. Return to KFM while it verifies access to the registered project.
4. Select a maximum size, then **Download [year] to KFM**. One job runs at a time.
   The page shows captured bytes, file progress, destination and failures.

The project must be registered for Earth Engine and the account must have access.
This does not enable billing, create a Cloud Storage bucket, or select a paid
fallback. Google manages login; no password is submitted to KFM. The OAuth flow
uses PKCE, a one-time state value and a ten-minute expiry. Refresh credentials
stay in the private local store; they are not sent to the Site or GitHub.

## Data paths and map handoff

Directory Rules and accepted ADR-0029 place provider capture in
`connectors/google/earth_engine`, local operation in `tools/local_data`, tests in
`tests/local_data` and this operator guide in `docs/runbooks`. Payloads remain
outside source checkouts, under the existing data lifecycle:

| Relative to the chosen KFM data root | Purpose |
| --- | --- |
| `data/raw/earth-engine/<dataset>/<year-or-fixed>/<job-id>/` | Immutable candidate GeoTIFF tiles, source inventory and capture metadata |
| `data/work/earth-engine-downloads/jobs/` | Mutable progress / failure states |
| `data/work/earth-engine-downloads/credentials.json` | Owner-private Google refresh credential; never commit or upload |
| `data/work/earth-engine-downloads/config.json` | Linked project ID |
| `data/receipts/ingest/earth-engine/<job-id>.json` | Stored-byte hashes, partial outcomes and unreviewed receipt |

Source IDs, date labels, processing choices, coordinate grid and file hashes
travel with each product. Hashes verify locally captured bytes, not an independent
provider checksum. **Downloaded is not map-ready:** coverage, processing, rights,
review and release must be completed before preparing a display set in the
existing Earth Engine map installer. This feature does not automatically promote
raw files, replace approved map tiles, change active mirror review, or fabricate
an EvidenceBundle. Existing `data/work/earth-engine/exports` remain untouched.

## Limits and recovery

The download center can inspect the local library without a Google account.
An authorized `GET /library` starts its first background scan; subsequent reads
return progress or the last complete snapshot. `POST /library/refresh` accepts
only `{}` and the existing session token. Concurrent refreshes share one scan.
The scan reads filesystem metadata under `data/raw`, `data/work`,
`data/quarantine`, and `data/processed`; it never reads payloads or credentials.
Only top-level collection labels, lifecycle lanes, file counts, and logical
file bytes are returned. Individual file names and paths are not returned.

Hidden entries, credentials/configuration files, runtime/environment directories,
and the download operator's job/credential directory are excluded. Other symlinks
and special files fail the scan without following them. Limits are 256
collections, 500,000 examined entries, 32 nested levels, and 30 seconds. Unreadable,
changed, unsafe, or excessive trees produce an explicit failed scan; partial
totals never replace the last complete snapshot. A missing scan timestamp means
the library has not yet been measured, even when its initial counters are zero.
Scanning is independent of job polling and requires no download or source
activation. These metadata totals are a dated inventory, not checksum verification,
an atomic filesystem snapshot, source coverage, or map readiness.

- The 17 catalog selections are supported, not the entire Earth Engine catalog.
  Annual map composites/summaries are exported, not every original source scene.
  MSS, ERA5 and ERA5-Land currently download source inventories only; selecting
  variables, processing and bounded raster products is still required.
- Kansas boundary: TIGER 2018, STATEFP 20. RGB/elevation use a 30 m EPSG:5070
  display grid; Dynamic World uses 10 m. Climate grids follow the selected recipe;
  PRISM checks its NAD83 grid. Categorical resampling stays nearest-neighbor.
- Each synchronous Earth Engine tile is at most 1024×1024 pixels and 32 MiB;
  maximum 4096 tiles, 4 billion pixels, 20,000 source IDs. The user chooses a total
  limit up to 500 GB and adequate free disk space is required. New RAW captures
  are protected candidates, separate from the existing replaceable 500 GB cache;
  they are never silently evicted and repeated captures consume additional space.
- Cancellation stops between bounded provider requests (up to 90 seconds each).
  Partial files remain inspectable. Worker restart marks unfinished jobs
  interrupted. There is no tile resume yet: a new download gets a new directory.
  Retry after an uncertain start reuses the request ID to avoid duplicate jobs.
- Google quotas and request/compute limits can still reject a large selection.
  Failure does not substitute another year, provider, product or paid service.
- To disconnect, stop the operator and remove only its private credential using
  the owner's normal credential-management process. Revoke Earth Engine access
  in the Google account when desired; deleting local credentials is not revocation.

## Verification

Deterministic tests cover bounds, caps, incomplete years, preserved partial
captures, idempotent job starts, OAuth state/expiry, origin/Host/session checks and
stored receipts. A real OAuth consent and authenticated raster capture require
the owner's account and registered project; simulated tests do not prove them.

References: [Google authentication](https://developers.google.com/earth-engine/guides/auth),
[download request limits](https://developers.google.com/earth-engine/apidocs/ee-image-getdownloadurl),
[export grids](https://developers.google.com/earth-engine/guides/exporting_images).


## Google account and local library update — 2026-10-09

Sign in with Google before choosing a project. The local operator exchanges a
one-time PKCE code, refreshes the grant and reports the account when Google
provides a verified email. Sign-in does not request project listing: Google
rejects the Cloud project list scope for the shared Earth Engine OAuth client
(403 `restricted_client`). Enter the Cloud project ID once; it is saved and
prefilled afterwards. Grants that still carry the scope from before this change
keep their project list. Nothing here creates projects, enables APIs or
billing, or grants IAM roles. Enter or choose the project and use
**Check download access**. A real Earth Engine scalar computation must succeed
before the download control becomes ready. Saved credentials are rechecked on
operator restart; a credential file alone does not establish access.

OAuth requests only the Earth Engine scope and email/OpenID. Tokens remain in
private local credential storage and never appear in status responses or Site
storage. Any grant can be checked with a manually entered project; a missing
email permission has an explicit fallback. Browser Google cookies alone are not an
Earth Engine grant. Google consent and live account/project acceptance require
the owner to complete sign-in.

**View downloaded data** opens My library directly. It lists recent completed
and partial transfers by source, with bytes and destination, plus the bounded
filesystem metadata scan of all existing collections. Earth Engine raw files
are grouped by dataset and period; empty directories are not downloaded data.
Transfer history does not prove a file still exists, and stored bytes do not
approve a dataset for map display. The existing refresh, stale-state, partial
capture, size-cap and source-review protections remain in effect.

References: [Google authentication](https://developers.google.com/earth-engine/guides/auth)
and [read-only project discovery](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/list).


### No-login Kansas catalog preference — 2026-10-09

Satellite & climate defaults to public publisher files. Google sign-in is an
optional Earth Engine export path. The initial public collection contains 20
USDA NASS national CDL ZIPs (2008–2025, including the 2024/2025 10 m and
resampled 30 m alternatives) and 44 CHIRPS v2 annual GeoTIFFs (1981–2024).
Every offered URL was found in the publisher's listing and checked anonymously
with a bounded byte-range read: file signature and total byte length matched.
No full datasets were fetched as part of curation. The exact URLs are pinned in
the local operator; redirect/query variants and arbitrary future URLs remain
denied. Publisher originals include Kansas but are national/global files, not
Kansas clips or byte-identical Earth Engine recipe outputs. Size and scope are
visible before an explicit download. They use the existing local transfer,
cancellation, history and library paths without Google credentials. The source
coverage remains a curated subset; geology refreshes retain its separate check
date and never mark it as a complete live Earth Engine catalog.

Public sources: [USDA files](https://www.nass.usda.gov/Research_and_Science/Cropland/Release/),
[CHIRPS annual files](https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/),
and [Earth Engine catalog](https://developers.google.com/earth-engine/datasets).

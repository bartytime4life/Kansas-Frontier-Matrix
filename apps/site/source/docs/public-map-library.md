# Public mine-map and geologic-map library

Open **Library & downloads → Mine maps & geologic maps** at
`/downloads#public-maps`. Search by title, publication, county, publisher, map
year or direct-file format. Select a record to inspect its source, scale,
dates and reuse terms. Metadata browsing requires no Google account.

Choose **Connect map downloads**, then **Refresh all Kansas records** to ask
the existing local operator for a fresh inventory. The established local Site
connects automatically. Each source reports its own completeness and last-check
time; retained reference records are counted separately from discovered rows.
A failed source keeps its prior records. Missing results never establish an
absence of mines or complete geological coverage.

The download catalog includes only records with verified direct files. Entries
with no files, unverified links, service-only access, archival requests or purchase
requirements are excluded from results, publisher/format choices and source
coverage. Archive-request links and non-download availability choices are removed.
The same rule applies to the offline seed and refreshed local catalogs. Existing
metadata snapshots, stored files, receipts and transfer history remain intact.

The October 9, 2026 local snapshot contains 1,695 metadata records; eight records
with twelve verified direct files are offered for download. Source coverage keeps
its original metadata-inventory counts and dates distinct from downloadable
record counts. Free original files can still carry reuse or redistribution holds.

A failed local catalog read preserves the last checked metadata and its warning.
The existing five-second status poll retries that read once the service responds;
only a successfully parsed catalog clears the warning. A successful refresh with
zero discovered points is a checked query result, distinct from unavailable
discovery, and still does not establish absence of mining or complete coverage.

For a **verified direct file**, select the original and enter a maximum in MiB
(1 MiB = 1,048,576 bytes), at least its known size. Then press **Download selected
original**. Follow confirmed job progress below. An uncertain response is not a
confirmed failure: reconnect and inspect jobs before requesting another copy.
**Cancel map download** preserves captured partial bytes. Public-map downloads
share the operator's single active-download boundary with Earth Engine jobs but
require no Earth Engine setup or authentication.

## What the catalog establishes

- The supplied NGMDB search is preserved verbatim as a reference. Discovery
  queries its public JSON counterpart for Kansas and reconciles all result IDs
  before retaining explicit USGS and KGS publisher subsets. The URL's publisher
  parameter alone is not relied on. A complete catalog means the query was
  reconciled, not that every publication has a downloadable or georeferenced map.
- The researched seed includes selected verified KGS M-118 and Bourbon M-97
  PDF/JPEG originals and four USGS Limon/Lamar GIS ZIP archives. The latter
  retain 1980/1976 map dates separately from their 2022 digital releases;
  publisher metadata and HEAD sizes verify the offered links, not extracted
  archive contents. Most discovered NGMDB records currently supply metadata
  links only and are excluded from download discovery. GeMS releases, services, and unverified asset links do not become
  downloadable simply because their publication appears in search results.
- Four CNGM version 2 national GeMS ZIPs are also selectable: Earth surface
  (3,492,433,165 bytes), Quaternary (2,971,732,596), Pre-Quaternary
  (3,067,729,423), and Precambrian (2,211,252,348). These are whole national
  archives, not pre-clipped Kansas subsets. Verified-TLS GET response headers
  confirmed exact offered links and lengths; HEAD attempts timed out, and no
  archive body was fetched during catalog preparation. Initial publication
  was 2025; version 2 was released September 3, 2026. The four products are
  thematic interpretations and do not form a continuous three-dimensional model.
- NMMR discovery uses the supplied ArcGIS experience's official mine-map point
  service within a Kansas bounding rectangle. Points are finding aids, not mine
  boundaries or current hazard assessments. Source confidence, archive status,
  scene identity and feet-per-inch scale remain explicit. Provider-derived JPEG
  scene URLs start **unverified**. Archival TIFF originals may require the
  repository's request process. Those request-only and unverified records are excluded from the download sources; no request is submitted by this feature.
- Metadata requests use verified TLS, fixed endpoints, 4 MiB per response and a
  64 MiB total budget. Limits or unavailable services produce explicit partial
  or unavailable coverage. The October 8, 2026 discovery reconciled 2,270 NGMDB
  Kansas result IDs, including 944 USGS and 741 KGS publications; NMMR remained
  unavailable because its service failed TLS verification. Those counts describe
  that snapshot, not all future inventories.

## Source previews and rights

**Open source map preview** provides opt-in, unsaved context for the KGS M-118
GeMS polygon service, four separate USGS CNGM v2 map-unit services, or NMMR index-point service. Pan and zoom within Kansas,
then choose **Load this map area**. Requests cover at most roughly 0.6 degrees
in each direction, read at most 4 MB, and display at most 200 validated features.
Rejected or excess features mark the response partial. Provider failure is not
an empty-area finding. Select a feature on the map or in its accessible list to
inspect source attributes.

M-118 is interpreted surface geology at 1:500,000; zooming adds no mapping
accuracy. NMMR points do not reconstruct mine workings. These previews neither
save data nor install a governed map layer. Downloaded PDFs/JPEGs are reference
originals until georeferencing is separately verified; a TIFF signature also
does not establish geographic alignment.

KGS rights holds remain in force. The owner's explicit selection permits
private candidate retrieval of offered public originals; capture does not clear
reuse, redistribution, source admission, display preparation or publication.
Every job has `mapReady: false`; every receipt remains `UNREVIEWED`,
`NOT_ADMITTED` and `NOT_RELEASED`. Existing active maps and mirror-review
receipts are unaffected.

## Operator, storage and recovery

Use the existing initialized, owner-private KFM data root and the loopback
operator documented in the repository's
`docs/runbooks/earth-engine-downloads.md`. From a complete source checkout:

```sh
python3 tools/local_data/earth_engine_downloads.py serve --root "$HOME/Projects/KFM-data"
```

The established Earth Engine runtime can run that command unchanged. For a
standalone metadata snapshot, choose a new output outside the source checkout:

```sh
python3 tools/local_data/public_map_catalog.py --output /tmp/kfm-public-map-catalog.json
```

The discovery command refuses an existing output. It downloads metadata only.
The browser's refresh action stores the current snapshot automatically.

| Relative to the KFM data root | Contents |
| --- | --- |
| `data/work/public-map-downloads/catalog.json` | Last saved catalog snapshot |
| `data/work/public-map-downloads/jobs/<id>.json` | Job progress and terminal state |
| `data/raw/public-maps/<record-id>/<id>/` | Selected original or retained `.part`, plus pinned `source.json` |
| `data/receipts/ingest/public-maps/<id>.json` | Immutable capture receipt and stored-file SHA-256 |

Each explicit transfer is capped by the selected maximum, up to 500 decimal GB,
with a 64 MiB free-space reserve. RAW files are protected from automatic eviction;
repeated captures use new directories and consume additional space. Streams
never overwrite existing paths or follow filesystem symlinks, and transfers
reject redirects, unexpected formats, changed known sizes and oversized bodies.
SHA-256 plus stored-byte readback verifies captured bytes; it is not an
independently published provider checksum. Cancellation waits for an in-progress
bounded network read; unfinished jobs become interrupted on restart. Missing
receipts are recovered without replacing an existing receipt. There is no
automatic retry, partial-file resume or extraction.

The service remains on `127.0.0.1:8769`. Read routes are
`GET /public-maps/catalog` and `GET /public-maps/status`; mutation routes are
`POST /public-maps/downloads`, `/public-maps/cancel` and `/public-maps/refresh`.
The existing Host/origin checks apply, with the session token additionally
required for mutations. The Site preview route is `GET /api/public-maps/preview`
and accepts only the six fixed source kinds and bounded Kansas extents.

An installed operator must retain the repository-relative layout for
`tools/local_data/public_map_catalog.py`, `public_map_downloads.py`, the updated
`earth_engine_downloads.py`, and their existing helper modules. It also requires
`apps/site/source/app/public-map-catalog.json` beneath that same source root,
even when a saved live snapshot exists. The Site build contains only the
researched metadata seed; live inventory and captured map bytes stay in the
external local store.

NMMR's supported future direct-file route is limited to its published
`https://mmr.osmre.gov/images/<document-and-scene>_web.jpg` naming rule. A URL
matching that rule still cannot download until its catalog availability has
been separately verified. TIFF-request endpoints and arbitrary URLs are denied.
ScienceBase transfers accept only the four pinned Limon/Lamar attachment URLs
and known original filenames. Other ScienceBase query tokens remain denied.
CNGM transfers likewise accept only the four pinned `gems_download.pl` queries.
Local descriptive filenames are used where a publisher filename was not
observed; the exact source URL remains pinned in each candidate's `source.json`.

## NMMR TLS investigation — October 8, 2026

The retained discovery receipt at
`tools/local_data/catalogs/public-maps/discovery-20261008.json` records
`CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate` for the
automated ArcGIS discovery host, `geodata.osmre.gov`. The official navigation
host is separately pinned as `mmr.osmre.gov`. The receipt does not distinguish
a missing provider intermediate certificate from a local trust-store problem.

Inspection of `tools/local_data/public_map_catalog.py` confirms fixed HTTPS
metadata endpoints, the standard-library verifying TLS context, disabled
redirects and bounded reads. A fresh fixed-endpoint count probe and a strict
`openssl s_client -verify_return_error` probe both failed DNS resolution in this
task environment before a certificate could be inspected. The runtime reports
OpenSSL 3.5.8 and an environment-specific CA-file default. Provider chain and
original-host trust-store diagnosis therefore remain **UNKNOWN**; the earlier
TLS failure has not been reproduced or declared repaired here.

No transport or trust-store change is justified by that evidence. On the original
operator host, the next diagnostic is to inspect the presented chain and the
configured CA bundle using normal verification. A provider-chain repair or an
authorized trust-store repair must be followed by a verified request to the same
fixed endpoint. Do not disable verification, trust a certificate retrieved from
the failing connection, follow redirects or substitute an unverified endpoint.
Focused offline tests cover default verifying TLS, a single failed request with
no insecure retry, retained unavailable metadata, subsequent checked zero/point
results, and denial of search/request URLs as metadata-transport destinations.


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

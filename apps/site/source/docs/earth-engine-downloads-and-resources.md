# Earth Engine downloads and underground resource context

The Earth Engine workspace now provides a Google sign-in button, project-ID
field, local connection status and a download action for its selected dataset
and year. A loopback operator installed from the main KFM repository owns Google
credentials and filesystem writes. Hosted code receives only job status, source
metadata and a transient local-control session token. Google credentials never
enter the Site, D1, R2, URL state or localStorage.

**Library & downloads** (`/downloads`) combines a searchable, paginated local
inventory with background job status and separately checked map periods. The
local Site connects automatically; hosted pages require an explicit connection.
Library scans run in the operator, return bounded metadata summaries, and retain
the previous dated result during refresh or failure. They exclude credentials,
hidden files, runtime directories and recovery/catalog lanes; their byte total
is not a whole-disk measurement or checksum verification.

Jobs survive page navigation. File progress is determinate only when the worker
knows its total; a selected transfer maximum is a limit, not estimated final size.
Hidden tabs pause status polling and refresh when visible again. Cancellation
outcomes and retained partial files stay visible. Buttons, fields, busy actions
and unavailable controls use their corresponding pointer styles.

Downloads capture Kansas recipe products into the external RAW candidate lane,
with source inventories, explicit grids, hashes and receipts. They remain
unreviewed until the existing display-set preparation/review/installer process.
MSS and ERA5 selections are inventories, not unqualified raster products. The
manual recipe/export controls remain available in a disclosure below downloads.
See the main repo `docs/runbooks/earth-engine-downloads.md` for setup and limits.

In Underground → selected area, **Water, oil, gas & minerals** opens a compact
resource selector. Water reuses the loaded WWC5 logs and their record-time
filter. Oil/gas and mines/minerals query official public services for the applied
frame, independently of the time slider. Each request is capped at 201 source
features / 1 MB / 18 seconds; at most 200 valid, unique positions are displayed.
Late responses from a previous frame are discarded. A closed or hidden resource
panel removes its overlay. No resource point is converted into an invented
subsurface trajectory, interval, reserve estimate or geological volume.

Oil/gas source: KGS Kansas GIS oilgas_general MapServer layer 0. Positions request
WGS84 output; raw NAD27 coordinate attributes are not reused. Reported total
depth is in feet with source-dependent reference, often Kelly bushing. Recorded
status is not a current production assertion.

Mines/minerals source: KGS-linked Quarries_and_Mines FeatureServer layer 0,
primarily KDHE inventory circa 2000. Active/abandoned descriptions are historical.
Service edit or retrieval dates do not become observation dates.

Source methods and limitations remain visible with record details. Results are
read-only display context, separate from governed source admission and released
evidence. Location details are withheld in redacted mode. Existing well/core,
aquifer, cutaway and map-time behavior are retained.

Placement follows the existing Site app/API/test roots within `apps/site/source`
when mirrored; no alternate registry, schema or source-admission home is created.


## Google account and local library update — 2026-10-09

Sign in with Google before choosing a project. The local operator exchanges a
one-time PKCE code, refreshes the grant and reports the account when Google
provides a verified email. Project discovery uses the read-only Cloud project
list scope; it does not create projects, enable APIs or billing, or grant IAM
roles. Choose a project (or enter its ID if listing is unavailable) and use
**Check download access**. A real Earth Engine scalar computation must succeed
before the download control becomes ready. Saved credentials are rechecked on
operator restart; a credential file alone does not establish access.

OAuth additionally requests email/OpenID and read-only project listing alongside
the existing Earth Engine scope. Tokens remain in private local credential
storage and never appear in status responses or Site storage. Legacy grants can
still be checked with a manually entered project; missing email/project-list
permissions have an explicit fallback. Browser Google cookies alone are not an
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

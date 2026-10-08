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

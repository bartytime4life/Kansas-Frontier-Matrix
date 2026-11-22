# Provider changes found by a route sweep (2026-11-22)

Every public data route was sent one valid request from outside the site. Two had stopped
working because their provider changed, and are repaired here. The Drought Monitor series was a
third and is covered in `category-maps.md`.

## Historical topographic maps: the USGS moved the sheet catalog

`/api/historical-topo` answered 502 for every search, so the historical map control found no
sheets.

- Former address: `ngmdb.usgs.gov/arcgis/rest/services/topoview/ustOverlay/MapServer/0/query`.
  It now answers `{"error":{"code":404,"message":"Service not found"}}`.
- Current address: `energy.usgs.gov/arcgis/rest/services/ustOverlay/MapServer/0/query`, the one
  topoView's own page reads. Same layer and fields. The route's query for a point at Topeka
  returned 24 sheets in 0.7 seconds.

`app/historical-topo.ts` names the new address and `energy.usgs.gov` joins the bounded fetch
allowlist. Links to the topoView viewer are unchanged; it is still at ngmdb.usgs.gov.

## Storm outlooks: an outlook with no risk area lost its issue time

When the Storm Prediction Center draws no risk area (for example the day 1 tornado outlook on a
quiet day) it sends one placeholder feature, "Less Than 2% All Areas", with no polygon. The
parser skipped that feature before reading its times, so the outlook showed no issue time or
valid period. The times are now read from the outlook's features before the placeholder is
set aside. Nothing is drawn for it and no Kansas risk is claimed.

## Found and not changed here

| Route | What was seen | Why it is left |
|---|---|---|
| `/api/cropland/point`, `/api/cropland/history` | 502, and every year "failed" | The CropScape point service (`nassgeodata.gmu.edu`) answered 503 on repeated tries. The provider is down; the map tiles from the same provider work |
| `/api/public-maps/preview?kind=osmre-nmmr` | 502 | The provider's server sends an incomplete certificate chain, so a verified connection cannot be made. The other five kinds work |
| `/api/hydrology/direction` | 200 after 13 to 35 seconds, elevation unavailable | The 3DEP elevation sampling service was slow and intermittently failing. The channel query itself took 2 seconds |
| `/api/local-data/[dataset]` | 503 on about one first request in four, 200 a minute later | The relay to the home computer, not the datasets |

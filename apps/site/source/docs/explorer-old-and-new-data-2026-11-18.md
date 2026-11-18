# Older and newer layers together — November 18, 2026

The November 13–16 changes added storm, rain, land-cover, outdoor-access, trail,
historic-place and bridge layers. The Explorer already had older aquifer,
seismic, survey, rail, lightning and river layers. Many of these were reachable
only through Map layers. This change makes both sets easier to find and use
together, and fixes reliability, performance and accessibility problems found
in the same review.

Every layer named here was already a registered public context source. No
provider, endpoint, dataset or release is added, and no record is admitted.

## Starters

The **Start with a purpose** menu has 20 starters, up from 12. They are grouped
by theme in the menu: Water & ground, Weather & hazards, History & routes,
Outdoors & ecology, Earth & survey, and Built & planning.

| New starter | Layers | Older layers it uses |
|---|---|---|
| Beneath the plains | High Plains aquifer, saturated thickness, depth to water, monitoring wells | KGS aquifer maps from 2022–2024 |
| Shaking ground | Recent earthquakes, Raspberry Shake stations, 3DEP hillshade | USGS and Raspberry Shake feeds |
| River & flood watch | NWPS forecast gauges, NWM 18-hour outlook, MRMS 24 h rainfall, 3DHP hydrography | NWPS and NWM |
| Survey lines & soils | PLSS townships and sections, SSURGO map units, counties | BLM PLSS |
| Roads & rails through time | 1918 roads, abandoned and active rail, current roads | KDOT transport references |
| Lightning & the sky | 15-minute lightning density, 1995–2014 flash average, radar loop, GOES imagery | Lightning and satellite layers |
| Wildlife & open country | KDWP wildlife areas, NLCD 2021, PAD-US, 3DHP hydrography | 3DHP |
| Bridges & crossings | State highway bridges, recorded closed bridges, roads, 3DHP hydrography | KDOT roads |

Every starter keeps the existing rules. It uses 3–4 public context layers and no
more than two JSON feeds. Held, failed and private sources are skipped. A
starter with a matching guide shows a **Read the guide →** link. The default
starter is looked up by id instead of by its position in the list.

NEW markers on layers and starters now stop showing on January 1, 2027
(`NEW_MARKER_UNTIL` in `app/kansas-discovery-layers.ts`). The KDWP wildlife-area and
walk-in layers, added on November 13, now carry NEW markers and legend chips.
Their map and legend colours come from one shared constant.

## Guides

`/explore` has 13 plain-language guides, up from 5:

- `storms-and-severe-weather`: SPC outlook, storm reports, NWS alerts, MRMS rainfall
- `fire-and-smoke`: SPC fire weather, FIRMS detections, NIFC reports, HMS smoke
- `aquifers-and-groundwater`: High Plains aquifer, saturated thickness, depth to water, about 1,400 measured wells
- `earthquakes-in-kansas`: USGS earthquakes, Raspberry Shake, hillshade
- `land-cover-and-public-lands`: NLCD 2021, PAD-US, watersheds
- `rivers-and-floods`: NWPS gauges, NWM outlook, MRMS rainfall, hydrography
- `roads-and-railroads`: 1918 roads, abandoned and active rail, highways
- `land-survey-and-soils`: PLSS townships and sections, SSURGO, counties

A guide page names the starter that opens related layers. The guide index
states how many guides there are, and each provider link tells screen-reader
users that it opens a new tab. `/sitemap.xml` lists the public entry pages and
guides. `/robots.txt` keeps API routes and owner workspaces out of indexes.

`/topics` links each subject to the guides whose lead layer belongs to it, has
a canonical URL, and marks internal links with → instead of the external ↗. The
Explorer's layer panel, the About page and the 404 page now link to the guides.
The root page description is now plain language.

Topic membership changes:

- The trail layers are also under **Transportation**.
- MRMS rainfall and the WPC rain forecast are also under **Hazards**.
- SSURGO soils are also under **Engineering**.

The hazard "held" notes now say that the reviewed storm reports and the CPC
drought outlook are available. They still list the full Storm Events archive,
the weekly Drought Monitor and algal-bloom advisories as held.

## Science lab

Each of the Observatory Science lab's 18 phenomena now has a **Map layers →**
link. The link opens the Explorer with that phenomenon's public context layers
selected, for example storm reports and the SPC outlook for tornadoes, or NLCD
and PAD-US for vegetation. The Observatory sources table shows the same link.
A link selects context only. It does not change a phenomenon's support label
and does not connect an archive.

## Reliability and performance

- Each layer row checks whether it is listed through a Set built once per
  render. Before, every row searched the whole list.
- Each row computes its discovery legend once.
- Topic membership and search text are computed once per source and reused for
  every filter keystroke.
- The GOES satellite refresh depends on its own layer only. Toggling another
  layer no longer refetches satellite frames or restarts their timer.
- The observed-lightning poll reads at most 2 MiB and pauses in a hidden tab
  after its first read. The reviewed-water minute poll also pauses in a hidden
  tab.
- Soil-moisture availability can be cancelled, times out after 20 s and reads at
  most 256 KiB. A newer check or unmount cancels an older one.
- Saving a fire-detection day times out after 45 s with a plain message, so the
  button is not left busy.
- Release-console status and actions time out, read bounded bodies and handle a
  non-JSON reply. Before, a non-JSON reply could leave "Loading…" on screen.
- Observatory side reads now have byte limits: coverage, context feeds, geology
  legend, resources, storm scans and storm availability. So does the NOAA radar
  frame manifest.
- KDWP paging shares a 25 s budget, so it answers before the browser's 30 s read
  limit. Pages that do not fit become a labeled partial response.
- The Balanced render budget treats a device as touch-first only for a coarse
  pointer, or a small viewport without hover. Before, a short laptop window
  (1366 × 700, for example) got the reduced touch budget.
- If a source's data does not match the layer it was requested for, the error
  now says so. Before, it reported "HTTP 200".
- `npm run measure:layers` runs the lifecycle measurement. The script now stops
  with an error when a `page.tsx` anchor it slices on is missing.
- A connection record's feed is taken from the source's `apiPath`. The five KDOT
  bridge connections now name their feeds.
- The NWS User-Agent contact string uses the shared `PUBLIC_SITE_ORIGIN`, which
  is unchanged.

## Accessibility

- A source toggle's accessible name no longer changes with its state. The
  checkbox state already announces whether the layer is on.
- The NEW badge is separated from the title and is announced as ", new layer".

## Knowledge pack

The curated vocabulary adds terms for the new layers: SPC outlook, local storm
report, MRMS, QPF, drought outlook, SSURGO, soil map unit, KDWP wildlife area,
WIHA, National Historic Trail and cattle trail. The generated pack was rebuilt,
and `--check` reports it current.

## Not changed

- No new provider, endpoint, dataset, or local download, and no data admission
  or release.
- The KDWP walk-in season label, the WIHA service name and every provider query
  are unchanged.
- Geometry clones still use a JSON round trip. That step also drops values that
  cannot be serialized.

## Follow-up corrections (after merge)

Automated review of the merged change found two regressions in the reliability
work above. Both are fixed in a follow-up change.

- **Release console.** An HTTP 200 reply whose body could not be read (stalled,
  truncated, oversized or not a JSON object) was treated as an empty status. The
  console then said no package was active and enabled **Activate package**
  while the real state was unknown.

  A successful reply must now be read in full. Otherwise status reports
  "unavailable", and an action reports that nothing is confirmed. Only refused
  (non-OK) replies with an unreadable body fall back to a generic reason.
- **KDWP paging.** When the shared 25 s budget shortened a later page and that
  page timed out, the whole feed failed and the pages already read were
  discarded.

  That timeout now ends paging, and the response returns the collected areas as
  a labeled partial result. A first-page failure, a full-length page timeout and
  any other upstream error still fail the feed.

## Second coverage pass (after merge)

A later pass gives starters or guides to layers that still had none.

| Addition | Layers |
|---|---|
| Starter and guide: Aquifers beyond the High Plains (`/explore/kansas-aquifers`) | KGS alluvial, Dakota, Glacial Drift and Ozark aquifer extents |
| Guide for the Lightning & the sky starter (`/explore/lightning-and-the-sky`) | 15-minute lightning density, 1995–2014 flash average, radar loop, GOES imagery |
| Starter: Bridges before 1950 (links the bridges guide) | KDOT local bridges built before 1950, historic-designated bridges, 1918 roads |
| Starter: Declared disasters & alerts | FEMA declaration counties, NWS alerts, SPC Day 1 outlook, NWM high-flow analysis |
| Starter: Federal mineral leases | BLM authorized and closed lease cases, PLSS townships, counties |

The menu now has 24 starters, and `/explore` has 15 guides. A few layers still
have neither:

- **Airflow:** a model canvas with no map layer for a starter to select.
- **Local road bridges:** about 19,300 points, too many for a starter to open.
- **Others:** slope, water-table elevation, FIRMS detection details and PLSS
  intersected divisions. All are still available in Map layers.

The selected-bridge record read is now size-bounded. The unused
`fetchBoundedJsonArray` helper in the live-context route was removed.

## Third coverage pass (after merge)

Six more layers gain a starter, and one gains a guide.

| Addition | Layers |
|---|---|
| Starter: Water table & wells (links the aquifers guide) | High Plains extent, water-table elevation, monitoring wells, watersheds |
| Starter: Eastern Kansas aquifers (links the Kansas aquifers guide) | KGS Osage, Flint Hills, Glacial Drift and Ozark aquifer extents |
| Starter and guide: Slopes & landforms (`/explore/terrain-and-slope`) | 3DEP hillshade and slope, watersheds, counties |
| Starter: Fire detections up close (links the fire guide) | Clickable NOAA-20 heat detections, the daily thermal-anomaly image, HMS smoke, NLCD 2021 |
| Starter: Survey divisions up close (links the survey guide) | PLSS sections and intersected divisions, SSURGO soils, counties |

The menu now has 29 starters, and `/explore` has 16 guides. The aquifer, fire
and survey guides each name their new starter. Each starter still follows the
3–4 layer, two-JSON-feed and public-context rules.

Two layers still have neither:

- **Airflow:** a model canvas with no map layer for a starter to select.
- **Local road bridges:** about 19,300 points. Use the bridges starters or Map
  layers instead.

## Validation

See the pull request for the full test run, type check and mirror receipt.

## Rollback

Revert the commit and its successor mirror receipt and selector together. No
saved-schema, data, route-contract or operational-store migration is involved.
The context-preference storage key is unchanged.

# Discovery layers, legend chips and themed starters — November 13, 2026

This note records nine new public context layers, five themed map starters, a
**Surprise me** starter, **NEW** markers and inline legend chips in the
repository Explorer (`apps/site/source`). Every new layer is external display
context (`EXTERNAL_CONTEXT_ONLY`). None creates a KFM EvidenceBundle, source
admission, review or release. No hosted deployment, browser acceptance or
public-website change is asserted by this note.

## What a visitor can do now

| Layer | Provider | Kind | Topics | Clock |
|---|---|---|---|---|
| Severe storm outlook · Day 1 | NOAA SPC | Provider image | Weather, Hazards, Science | Current Day 1 issuance |
| Fire-weather outlook · Day 1 | NOAA SPC | Provider image | Weather, Hazards, Science | Current Day 1 issuance |
| Storm reports · 72 h | NOAA NWS | Clickable points | Weather, Hazards, Science | Rolling 72 hours; each report keeps its own time |
| Rainfall · past 24 h | NOAA MRMS | Provider image | Weather, Water, Agriculture, Science | Rolling 24 hours to the latest hour |
| Rain forecast · 5 days | NOAA WPC | Provider image | Weather, Water, Agriculture, Science | Current 120-hour issuance |
| Drought outlook · seasonal | NOAA CPC | Provider image | Weather, Hazards, Agriculture, Water, Science | Current seasonal outlook |
| Land cover · NLCD 2021 | MRLC / USGS | Provider image | Ecology, Agriculture, Land, Science | Fixed 2021 edition |
| Public & protected lands | USGS PAD-US 4.0 | Provider image | Ecology, Land, Places | PAD-US 4.0 compilation |
| Historic places · National Register | National Park Service | Clickable points | History, Places | Current public NPS locations |

A live check on November 13, 2026 returned 1,331 listed Kansas National
Register properties and 20 Kansas local storm reports through the new adapter
paths. Counts change with the providers and are not a fixed inventory.

**Starters.** *Storm watch*, *Rain & drought*, *Fire season*, *Heritage trail*
and *Land cover & open lands* join the six existing starters and are labeled
"new" in the chooser. **Surprise me** applies a different starter at random and
announces what it selected and why. Starter limits remain in *Sources & limits*.

**Legend chips.** Each new layer shows compact color chips copied from the
provider legend (or, for the two point feeds, from the MapLibre paint
expression). Chips identify colors; they are not measurements, and the
*Provider legend* link remains authoritative.

## Source and safety boundaries

- **Outlooks and forecasts** (SPC, WPC, CPC) are not observations, watches or
  warnings. A blank image is never labeled safe, dry or drought-free.
- **Storm reports** are preliminary, relayed observations with approximate
  locations. They can be duplicated or revised; NCEI Storm Data is the final
  record. Zero reports is labeled *empty*, not an all-clear.
- **MRMS rainfall** is a radar-only estimate, not a gauge measurement.
- **NLCD** classes have mapping error and do not establish ownership, habitat
  or present land use. **PAD-US** inclusion does not grant access or title.
- **National Register** points are the NPS public, non-restricted service.
  NPS withholds sensitive and restricted locations; this adapter never requests
  or infers them. Records the service marks *Removed* are omitted. A listing
  that publishes several points keeps each point with its own map identity.
  National Archives links are kept only when they point to
  `catalog.archives.gov`.

## Implementation

| Area | Files |
|---|---|
| Layer definitions and legends | `app/kansas-discovery-layers.ts` |
| Registry, temporal support and MapLibre layers | `app/live-context.ts` |
| Bounded server adapters (`nps-nrhp-places`, `nws-storm-reports`) | `app/api/live-context/route.ts`, `app/api/source-download/route.ts` |
| Topics | `app/layer-workspaces.ts` |
| Inspection fields and text | `app/evidence-drawer-data.ts`, `app/page.tsx` |
| Feature, connection and download registries | `app/site-features.ts`, `app/site-connections.ts`, `app/source-downloads.ts` |
| Starters and Surprise me | `app/map-starters.ts`, `app/map-starters-control.tsx` |
| Styles | `app/map-layers.css`, `app/explorer-controls.css` |
| Tests | `tests/kansas-discovery-layers.test.mjs`, `tests/map-starters.test.mjs` and registry-count updates |

The adapters use fixed provider URLs and fixed queries (`State='KANSAS'`,
`state='KS'`), the existing 8 MiB bounded JSON reader, Kansas coordinate bounds
and record caps (2,000 listings, 500 reports). The People topic still contains
only aggregate Census population; National Register places are listed under
History and Places.

## Rollback

Revert the files above together. No database, storage binding, dataset or
deployment setting is changed, so rollback needs no data migration.

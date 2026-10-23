# Road and rail construction through time

**Implementation candidate, 2026-10-22.** The hosted Explorer has a browser-local construction study and original 3D equipment models. Statewide, source-qualified construction/closure history is **not connected**. The tool does not animate existing KDOT reference layers into an invented historical network.

In the Layer Catalog, choose **Roads, rail & movement**, then **Construction through time**. Open the equipment study to inspect the same metre-based road/rail models used on the map. This unlocated visual study does not represent a real project or rate. A compatible local JSON study can be loaded, fitted to the map, hidden or cleared. Clearing, changing topic, or leaving the page discards it; nothing uploads or persists.

## Dates and progress

Following map time uses its selected calendar day; a year-only frame uses January 1. A local date, keyboard-accessible traversal slider and finite playback can override that clock for the construction study alone. **Follow map time** restores linkage. Playback compresses calendar time; it does not measure machinery speed. It stops at the final work date, pauses in a hidden tab and is disabled under reduced motion. The selected construction day and per-route status remain visible.

Each route needs its oriented centerline, supplied corridor width, positional uncertainty, actual work interval, individual chainage observations and separate HTTPS source links for dates and geometry. `interpolate: false` holds at the latest observation through gaps. Explicit `true` permits linear visual interpolation and labels it accordingly. Interval averages are labelled averages, never daily measurements. Endpoint dates alone do not provide an intermediate build rate. The importer verifies structure, ranges and ordering; it **cannot verify source assertions** or establish a recorded history.

`build`, `reconstruct` and `remove` are distinct actions. Removal requires an explicit removal record. Closure and reopening dates are independent of completion; a completed project does not automatically reopen. Rewinding time reconstructs the requested frame without converting construction into demolition. Absence from a map, active/abandoned rail designation, bridge age, a proposed project, contract award or lane opening does not establish construction, closure, removal or whole-project completion.

## Map appearance and scale

The custom layer uses metre-based, original procedural meshes in the existing MapLibre WebGL context, loaded on demand. Road models include a crawler excavator with treads, rollers, hydraulic boom/stick/bucket, compactor, cones, materials and workers. Rail models include work equipment, flanged wheels, working heads, ballast, ties and rails. Generic dimensions, equipment choices, tie spacing and animation are **representative visual design**, not observed contractor assets or historically verified machinery. Early-date studies omit modern high-visibility equipment/clothing.

No model is inflated to meet a screen-pixel minimum. Worker detail drops before equipment, then an overview line remains. Positional uncertainty above 4 m, narrow corridors and tight curves retain line cues rather than false precision or off-route equipment. Up to four visible crews render. Removal retains route cues until removal-specific equipment staging is qualified. Models stay behind the supplied front; articulation does not advance historical progress. Terrain/globe retain route cues with an explicit limitation; detailed crew projection is held. This is not a qualified terrain-aware historical reconstruction.

Overview lines are cartographic cues (minimum 1.5 px), not physical-width measurements. At close scale, line width follows the supplied corridor width. The selected basemap remains a reference and may show modern roads independently of the study. Historical traces are not legal access, navigability, safe routing or current closure advice. Local records stay out of the Evidence Drawer, AI context, exports, saved workspaces and source registry.

## Local study format

The downloadable [`transport-construction-study-example.json`](../public/transport-construction-study-example.json) is explicitly **synthetic**: invented dates and geometry, no actual route, no real closure or build rate, and placeholder URLs. Downloading does not load it onto the map. Do not substitute its content into a factual catalog.

```json
{
  "version": 1,
  "synthetic": false,
  "routes": [{
    "id": "source-specific-segment",
    "title": "Unverified local study",
    "mode": "road",
    "action": "build",
    "coordinates": [[-98.5, 38.5], [-98.497, 38.5]],
    "widthM": 8,
    "positionAccuracyM": 1,
    "start": "2024-01-01",
    "end": "2024-01-11",
    "progress": [
      {"date": "2024-01-01", "chainageM": 0, "sourceUrl": "https://example.invalid/actual-start"},
      {"date": "2024-01-11", "chainageM": 261.06, "sourceUrl": "https://example.invalid/actual-completion"}
    ],
    "interpolate": false,
    "sourceUrl": "https://example.invalid/work-record",
    "geometrySourceUrl": "https://example.invalid/survey",
    "limitation": "Illustrative format only. Replace all assertions and links with independently reviewed records."
  }]
}
```

The inline example is explanatory and must not be treated as real data. The downloadable example provides the exact synthetic route length. Optional `closedFrom` and `reopenedAt` require ordered valid dates; a removal cannot assert reopening. Each route models one monotonic oriented front; multi-front projects need separately supported segments. A worksite observation and equipment detail require adequate line geometry, not merely a town or project point.

Bounds: 2 MB, 1–12 routes, 10,000 total vertices, 2–5,000 vertices per route, 80 m–500 km length, Kansas bounds, 2–40 m corridor width, 0.1–10,000 m supplied positional uncertainty, 2–400 individually sourced observations per route. Reject invalid calendar days, credentials in URLs, non-HTTPS links, unordered/contradictory observations and out-of-range chainage. Unknown properties and external asset definitions are discarded; links are never fetched by the importer or renderer. Structural validation is not sensitivity clearance: load only public-safe study content.

## Curated primary-source leads and open work

The application includes four bounded discovery notes, with original source links and explicit missing fields:

| Source | Supported discovery fact | Still needed before a factual advancing-front map |
|---|---|---|
| [Kansas Historical Society, I-70](https://www.kansashistory.gov/kansapedia/eisenhower-highway-interstate-70/16894) | Opening west of Topeka on 1956-11-14 | Exact segment geometry, work start and observed front progress |
| [KDOT 69Express pre-construction notice](https://www.ksdot.gov/Home/Components/News/News/2831/386) | Preparation and planned construction phases are separate | Actual per-segment dates, staging, geometry and chainage |
| [KDOT KC Metro updates](https://www.ksdot.gov/about/our-organization/districts/district-1-northeast-kansas/kc-metro-updates) | Express-lane opening in February 2026 is separate from remaining work | Actual final acceptance, work-location and progress records; mutable notice needs an immutable capture |
| [BNSF 2024-10-25 update](https://www.bnsf.com/news-media/customer-notifications/notification.page?notId=industrial-products-network-update-for-friday-october-25-2024) | Twelve miles of second mainline near Augusta completed that report week | Exact new-track alignment, work start, daily/segment progress and precise completion date |

Research also checked KDOT historical maps and Kansas Historical Society railroad engineering/right-of-way collections. Map-edition presence can bound an existence interval but cannot establish when crews started or how quickly they advanced. KanDrive is a current/planned-conditions lead, not a verified historical archive. KDOT's accessible contractor-status report is dated **1998**; its current web availability does not make it a current feed, and it is not wired into this tool.

Next data work is source-specific: acquire immutable public records through existing intake, resolve rights and sensitivity, georeference at defensible accuracy, crosswalk segment/project identities, separate actual/planned dates, validate chainage and direction, retain uncertainty/conflicts and missing intervals, then obtain the normal evidence/review/release decision. Neither this UI nor the local JSON format is a new canonical transport contract, ingestion pipeline or release authority. No SQL migration, PC storage change, bulk acquisition, automatic refresh or historical-data publication is included.

## Placement, validation and rollback

Existing standalone hosted composition: `app/` owns UI/rendering, `tests/` owns regression coverage, `public/` owns the explicitly synthetic format example, `docs/` owns this behavior guide, and `data/receipts/generated/` owns authoring provenance. Canonical Directory Rules §§9–11 and accepted ADR-0029 route these responsibilities; no root or source authority is introduced. The main monorepo mirror and original Sites identity remain separate and require their own reconciliation.

Focused checks cover bounded input, progress uncertainty, closures/removal, reverse seeking, distance/LOD, geometry/material lifecycle, MapLibre style validity and overlay teardown. Browser/WebGL qualification, physical-device performance, production source equivalence, real historical-data admission and independent review remain separate from tests. Revert this focused application/test/guide/example/receipt change together; no stored-data migration or operational source change needs rollback.

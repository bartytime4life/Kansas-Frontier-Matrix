# Historical Kansas road-map comparison: local study boundary

## Scope and source identities

The Site's `app/road-map-editions.ts` inventories 55 operator-held PDFs in `/home/bartytime/Projects/Kansas Road Maps` by exact filename, byte size, and SHA-256. This is source **discovery**, not admission. No PDF bytes, derived raster, or traced road geometry have been added to Git or the Site. The user supplied the [KDOT past published county-map index](https://www.ksdot.gov/about/our-organization/divisions/planning-and-development/kansas-maps-and-gis-resources/past-published-county-maps); the statewide sheets inspected in this collection correspond to KDOT's separate [historic state-map index](https://www.ksdot.gov/about/our-organization/divisions/planning-and-development/kansas-maps-and-gis-resources/historic-state-maps). Exact download URL and edition identity for each local PDF remain to be bound.

Current-session checks found image objects in 54 PDFs and one blank 977-byte `1967 Kansas.pdf`. Several filenames cover two-year editions. `1938 Kansas.pdf` and `1938 Kansas 2.pdf` are distinct local files; their publication months were not determined from filenames. A filename year or two-year range is a **map edition**, not a road opening, closure, realignment, or construction date. The maps are page imagery, not georeferenced road-centerline data. Visual inspection of 1918, 1941, 1984, and 2023-2024 pages confirmed changing cartographic design and legends; automatic pixel differences would mix style, labeling, scan, and geographic changes.

The project owner reports written permission for a Kansas 3D digital-twin use. The actual permission text and its derivative, repository, public Site, and redistribution scope have not yet been inspected. [KDOT's public site terms](https://www.ksdot.gov/about/publications-and-reports/kdot-website-terms-of-use) require explicit permission for reproduction or use. Keep PDF bytes and source-derived geometry in the private work lane until the permission record is checked and cited.

## What the Site can do now

In **Domains + live data → Historical roads → Compare road years**, the Map Workbench accepts up to four small road-only GeoJSON line files for browser-local visual study. To view changes rather than an entire road network, prepare each file with only candidate changed road segments for its edition comparison. The Site does not compute or verify those changes. Each tagged edition has an independent color, opacity, show/hide control, and removal. The files are never uploaded, persisted, added to the Layer Catalog, reported, exported, or released. Only line coordinates reach MapLibre; properties are discarded. A user-selected edition tag is unverified metadata. A road line drawn in an edition does not establish when the road first existed.

The app's year-by-year Time Sweep remains the governed atlas clock. Road study overlays are independent so that multiple map vintages can be compared at once; the Site does not fill years without a source edition or carry the last mapped road state forward. The Site has **no derived Kansas road lines from these PDFs yet**.

## Required path from a PDF to a road layer

1. Verify the written permission and exact source URL; bind edition ID, SHA-256, map side, legend, attribution, and scope.
2. Keep source bytes in the private RAW or QUARANTINE store according to source-admission and rights review. The existing repository's `data/raw/roads-rail-trade/` and `data/work/roads-rail-trade/` describe lifecycle responsibilities; the large PDFs should remain outside Git.
3. Georeference each sheet with reviewed control points and record residual error. Reject blank, wrong-side, or poorly registered sheets.
4. Trace road centerlines or obtain a source-native vector dataset, retain the legend's road class, and record method, uncertainty, source edition, and reviewer. A raster color mask alone is not a validated RoadSegment.
5. Compare matched roads across actual editions, recording an **interval** for first or last mapped appearance. Do not turn a 1950-1951 map or an edition gap into an exact event year. Review style and scale changes before labeling additions or removals.
6. Gate processed data through the Roads/Rail/Trade source, rights, sensitivity, evidence, validation, policy, review, release, correction, and rollback controls before using a public KFM layer. Only then bind a released artifact to the Site.

Rollback of this local Site change removes the comparison controls and inventory. Browser-local overlays disappear on reload; no source file or repository data is changed.

# Category maps

Each start-page category opens on a map built for its data. The category map
registry, `app/category-maps.ts`, gives every topic in `app/layer-workspaces.ts`
one map look:

| Field | Meaning |
|---|---|
| `name`, `lede` | The look's short name and one sentence on what the visitor will see. They are shown on the welcome card, the topic dialog and the map dock. |
| `basemap` | A `BASEMAPS` key in `app/map-runtime.ts`. |
| `scene` | `2d`, `terrain` (3D terrain) or `globe`. It is applied through the existing `activateMapRepresentation`. |
| `camera` | Center, zoom, pitch and bearing. Only 3D looks start tilted. |
| `starters` | Existing official provider-context ids that are switched **on**. They are never switched off. |
| `swatch` | Three colours used to sketch the basemap on the start card and the dock. |

Choosing a look is presentation and navigation only. Starters are the same
provider-context switches the Layers panel offers, with their own source clocks,
holds and limits. They are display context, not admitted evidence.

## How a visitor gets there

- **Welcome.** Opening a category shows its map look. **Open the {map look}**
  calls `openCategoryMap`. **Explore {category} sources** still opens only the
  Layers catalogue.
- **The map dock.** While a category's look is on screen, `CategoryMapDock`
  (`app/category-map-dock.tsx`) names it and offers:
  - 2D, 3D and Globe;
  - relief depth (3D only);
  - sun direction (not on the globe);
  - reset view and "Layers for this map".

  Every control reuses an existing handler: `activateMapRepresentation`,
  `changeTerrainDepth`, `changeStudioLight` and `openAtlasPanel`. The dock can
  be hidden. It returns the next time a category map is opened.
- **Shared URLs.** No new parameter is needed. `topic`, `base`, `proj` and
  `scene` already restore the category, basemap and renderer, and the dock
  follows the restored category when its basemap is on screen.

## Specialized basemaps

Both new styles live in `app/category-basemaps.ts`. They are built only from
carriers already listed in `app/external-context-sources.ts`:

- OpenFreeMap vector tiles and fonts (`openfreemap-liberty`);
- the Terrarium display DEM (`aws-mapzen-terrarium`), for relief;
- the bundled simplified Kansas outline and graticule.

Both carriers now disclose `aviation-chart` and `civic` in `activatesWhen`. No
sprite is requested: airport symbols are drawn as circles.

### Aviation chart (`aviation-chart`)

A reading of a VFR sectional chart:

- elevation bands at 1,000 ft steps (`AVIATION_TINT_BANDS`, a stepped
  `color-relief`), plus hillshade;
- yellow built-up areas, quiet blue water and magenta roads;
- a dashed state line and a dashed 1° graticule;
- OpenMapTiles `aeroway` runways, taxiways and aprons;
- `aerodrome_label` airports as circled symbols, coloured by class (military,
  private, other), with ICAO/IATA identifiers and, from zoom 10, the airport
  name.

It is display context. It is **not for navigation**, flight planning or drone
authorization, and it does not replace current FAA charts, NOTAMs or TFRs.

### Government & civic (`civic`)

A light reference map:

- state, county (`admin_level` 6) and municipal (`admin_level` 8) boundaries
  are the subject;
- land, water and roads recede, with a faint hillshade;
- place labels are sized by rank, and state capitals carry a star.

At statewide zoom the vector tiles thin out county lines, so the Government,
People and Places looks also switch on the Census county layer as a starter.
Boundaries are display geography, not legal descriptions.

### Shared behaviour

- **Fallback.** Both styles use the `openmaptiles` source id. If that carrier
  fails, the existing fallback swaps to the local Midnight style
  (`VECTOR_BASEMAPS`, `shouldFallbackStandardBasemap`).
- **Globe.** Vector basemaps stay on the globe. Raster ones still hand over to
  the standard style there.
- **Relief.** The 2D relief scene effect defers to a basemap that draws its own
  hillshade (`CATEGORY_BASEMAP_HILLSHADE_LAYER_ID`), so shading is never
  doubled.
- **Persistence.** Saved views, snapshots, report attribution and wind-arrow
  contrast all accept the new keys.

## Limits

- The visual result of the two vector styles was validated against the MapLibre
  style specification and by tests. It was not rendered against live
  OpenFreeMap tiles in the build container, which cannot reach that host.
- The aviation chart basemap draws airports from OpenStreetMap data, not the
  FAA NASR airport list, and carries no airspace itself. The Aviation look
  switches on the separate airspace layer (`overlays: ["aviation"]`, see
  `docs/aviation-layers.md`), which draws FAA NASR airspace as 3D volumes or a
  2D chart, airports, drone ceilings, TFRs, weather and live traffic.

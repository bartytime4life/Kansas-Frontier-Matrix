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
- **Layers panel.** When a category is chosen in the Layers catalogue, its
  topic guide shows the same map-look card: name, scene and what you'll see.
  **Open this map** applies the look, and once the look is on the card reads
  "on the map now".
- **Shared URLs.** No new parameter is needed. `topic`, `base`, `proj` and
  `scene` already restore the category, basemap and renderer, and the dock
  follows the restored category when its basemap is on screen.

## In the Evidence Drawer

A selected record now opens with the category it belongs to, then the same
three questions for every source (`app/evidence-summary.ts`):

- **What it is** is the record's own summary. A provider basemap record is
  labelled as the provider's mapped record.
- **Where & when** gives the spatial scope and display anchor, then the
  observation or source time, with the source update when it differs.
- **Source & limits** gives the organization, the evidence state (a basemap
  record stays "External context only · no KFM EvidenceBundle") and the
  recorded generalization and uncertainty.

  When no limitation is recorded, the drawer says so rather than implying
  none.

Categories come from the same source-identity rules as the Layers catalogue:
`officialSourceTopics` or `registryLayerTopics`. When that category's map look
is not already on screen, the drawer offers **Open the {map look}**. The
summary only restates fields the selection already carries; the existing
Data, Metadata, Trace and Focus tabs are unchanged.

## Specialized basemaps

Six category styles live in `app/category-basemaps.ts`, listed with their
picker title, network note and legend in `CATEGORY_BASEMAPS`. Their keys are in
the import-free `app/category-basemap-keys.ts`, which the allow-lists share.
They are built only from carriers already listed in
`app/external-context-sources.ts`:

- OpenFreeMap vector tiles and fonts (`openfreemap-liberty`);
- the Terrarium display DEM (`aws-mapzen-terrarium`), for relief;
- the bundled simplified Kansas outline and graticule.

Both carriers disclose every category key in `activatesWhen`. No sprite is
requested: symbols such as airport circles and peak triangles are drawn or set
in text.

| Key | Map look | Used by |
|---|---|---|
| `aviation-chart` | Aviation chart | Aviation |
| `civic` | Government & civic | Government, People, Places |
| `hydro` | River network | Water |
| `relief` | Relief model | Terrain, Geology |
| `storm` | Storm desk | Weather, Hazards |
| `network` | Network map | Transport, Engineering |

### Aviation chart (`aviation-chart`)

A reading of a VFR sectional chart:

- elevation bands at 1,000 ft steps (`AVIATION_TINT_BANDS`), drawn as a
  `color-relief` whose interpolate stops pair one metre apart for hard chart
  edges, plus hillshade;
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

### River network (`hydro`)

- deep-water ground with a lifted hillshade, so the drainage pattern reads even
  before vector tiles load;
- rivers, canals and streams scaled by class, each with a soft glow, canals
  dashed;
- lakes and wetlands;
- river names follow their courses, and towns are labelled quietly.

It shows display geography, not measured flow or watershed boundaries.

### Relief model (`relief`)

- a smooth hypsometric tint (`RELIEF_RAMP`, a `color-relief` from about 150 m
  to 2,500 m) under the strongest hillshade of the set;
- rivers, main roads, peaks and towns stay quiet.

It is mixed-source display elevation, not survey measurement.

### Storm desk (`storm`)

- a neutral charcoal ground; every colour in the style has low chroma, so
  radar, alert and fire colours stay distinguishable;
- county and state lines and town labels show where weather is hitting.

Weather layers keep their own clocks.

### Network map (`network`)

- road classes in colour (motorway, trunk, primary, secondary), white-cased,
  with darker casing on bridges;
- route numbers from `transportation_name`;
- classic dark rail with white ties, plus runways and county lines.

It is display context, not traffic, condition or access.

### Shared behaviour

- **Fallback.** All six styles use the `openmaptiles` source id. If that carrier
  fails, the existing fallback swaps to the local Midnight style
  (`VECTOR_BASEMAPS`, `shouldFallbackStandardBasemap`).
- **Globe.** Vector basemaps stay on the globe. Raster ones still hand over to
  the standard style there.
- **Relief.** Each style draws its own hillshade under
  `CATEGORY_BASEMAP_HILLSHADE_LAYER_ID`. The 2D relief scene effect defers to
  it, so shading is never doubled, and the overlay sync aims it at the scene's
  sun direction.
- **Contrast.** `LIGHT_CATEGORY_BASEMAPS` marks the light grounds, so wind
  arrows draw dark strokes there and light strokes on `hydro` and `storm`.
- **Persistence.** Saved views, snapshots, report attribution and wind-arrow
  contrast all accept the new keys.

## Limits

- The vector layers of all six styles were validated against the MapLibre
  style specification and by tests. Their relief, tint and outline layers were
  rendered in a browser. It was not rendered against live
  OpenFreeMap tiles in the build container, which cannot reach that host.
- The aviation chart basemap draws airports from OpenStreetMap data, not the
  FAA NASR airport list, and carries no airspace itself. The Aviation look
  switches on the separate airspace layer (`overlays: ["aviation"]`, see
  `docs/aviation-layers.md`), which draws FAA NASR airspace as 3D volumes or a
  2D chart, airports, drone ceilings, TFRs, weather and live traffic.

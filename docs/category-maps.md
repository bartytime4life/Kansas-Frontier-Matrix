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
| `starters` | Existing official provider-context ids that are switched **on**. Opening the map switches every other provider-context layer **off**, as a starter set does, so each map opens on its own subject. |
| `swatch` | Three colours used to sketch the basemap on the start card and the dock. |
| `light` | Optional scene recipe (`daylight`, `golden`, `blue`, `survey`) the look opens under. Only its atmosphere and sun azimuth are applied, through `changeStudioLight`, so the visitor's effect settings never change. Relief looks use a raking sun (Terrain golden, Geology/Engineering/Groundwater survey), weather and water a dark sky (`blue`), aviation `daylight`. **Reset view** restores it. While the visitor follows the real sun, the computed sun lights the map instead. |

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
  - **Use the real sun now**, which switches on the Scene studio's "Follow
    real sun" effect. While it is on, the sun slider gives way to a reading of
    the computed sun over the map center, such as "52° up, from SW · 4:00 PM
    CDT", because a hand-set direction would have no effect. **Set light by
    hand** switches it back off. Only the visitor changes this setting; a look
    never does;
  - **Time**, shown while following the real sun: a quarter-hour slider
    through today in Kansas that relights the map for the sun at that moment.
    Watching it sweep from sunrise to sunset across the Flint Hills or the
    Smoky Hills shows how slope and aspect take the light. The reading then
    says "Sun at" rather than "Real sun", and **Now** returns to the clock.
    The chosen instant is registered per map (`registerSunInstant`), so the
    sky, relief, glow, buildings and Scene studio all read the same moment.
    Turning the real sun off or on from any control (the dock, the Scene
    studio checkbox, a recipe or a look preset) ends the study. The last
    step is 11:45 PM, so the slider never picks tomorrow's midnight.
  - **Play the day**, next to **Set light by hand** while following the real
    sun: a time-lapse that steps the study forward one quarter hour every
    200 ms (`SUN_PLAY_STEP_MS`) and stops at 11:45 PM, about 15 seconds from
    5:00 AM. It starts from the time shown, or from 5:00 AM once the day has
    been played out. Moving Time, pressing **Now**, turning the real sun off, or
    anything that takes its controls off screen stops it: hiding the dock,
    clearing the category, opening the guide or switching to the globe
    (`sunControlsShown`). Under reduced motion the button is disabled and
    only the slider moves the sun; It is display lighting only; no
    source time, archive date or evidence clock changes;
  - **Draw a cross-section**, on the Terrain, Geology and Engineering looks
    (`tools: ["transect"]`). It starts the existing terrain investigation
    (`startTerrainInvestigation`): 3D terrain, the Scene panel with its "Terrain tools"
    section opened and scrolled to the investigation steps, and a distance
    line. Finish the line, then **Preview display profile** samples the
    display DEM along it without the 3D exaggeration. It waits for terrain,
    and the profile stays display context, not survey measurement;
  - **Show river flow**, on the Water look (`tools: ["flow"]`). It switches the
    Scene studio's "Flowing water" effect on or off through
    `updateSceneEffects`: rivers flow downstream where USGS 3DHP maps a
    direction, and a USGS gauge reading lights its own reach. While it is on,
    the dock shows the effect's own reading, for example how many reaches have
    a flow direction and how many a gauge lights, or that it is loading or needs
    a closer zoom. When the map is degraded or still starting, or with reduced
    motion, ambient motion off or an efficient render budget (the same rule the
    animation uses), the rivers are drawn still and the dock names which applies. The flow reaches
    are display context, not measured discharge;
  - **Explore underground**, on the Aquifer and Geology looks
    (`tools: ["underground"]`). It opens the existing Underground view of
    recorded well logs, cores and aquifer sections (`enterUnderground`, the
    same entry the guide's Underground action uses), which switches to the 2D
    map and takes focus. The dock steps aside while Underground is open and
    returns when it closes, if the look's basemap is still on;
  - **Show day and night**, on the Sky and Observation globes
    (`tools: ["daylight"]`). It switches the existing Daylight & twilight
    layer on or off through the layer card's own path
    (`toggleDaylightVisibility`): the calculated night side of the Earth and
    its civil, nautical and astronomical twilight bands. When the layer's
    chosen date range holds the current time, it opens at now
    (`showCategoryDaylight`); a past day chosen in the layer card keeps its own
    clock. While it is shown, the dock reads that clock in Kansas Central time
    and what it means at the look's center, for example "Kansas center: Sun 9°
    below the horizon · nautical twilight" (`daylightPhaseReading`, using the
    overlay's own band edges). **Play day and night** runs the layer's 60-second
    loop through the day; reduced motion disables it. It is calculated
    geometry, not observed brightness or cloud cover;
  - **Measure an area**, on the Field and Survey grid looks
    (`tools: ["area"]`). It starts the Map menu's own Polygon measurement
    (`beginMapMeasurement("area")`); pressed again while points are being
    added, it cancels. Click around a field or parcel and **Finish** in the
    measurement readout. Areas under one square mile read in acres (hectares
    in metric), larger ones in square miles with acres alongside
    (`formatMeasuredArea`), so a PLSS section reads "1.0 sq mi (640 acres)".
    The geometry stays in the browser and is an approximation, not a survey.
    While a measurement readout is on the map (from this tool or **Draw a
    cross-section**), the dock lifts above it; on a phone (760px or narrower)
    it steps aside instead, so the map can be tapped, and returns when the
    measurement is cleared;
  - **Watch the radar loop**, on the Storm desk (`tools: ["radar"]`). It
    turns radar on and opens its live loop controls (`watchRadarLoop`, shared
    with the radar layer card's "Watch live loop"); while they are open it
    reads **Close radar loop** (`closeLiveInstrument`). The live loop plays at
    the present map time, so the button waits until Time is at Present. Opening
    the Storm desk already starts the loop, so the button is mostly for closing
    and reopening it. While a radar or lightning loop panel is open the dock
    sits above it; the taller river and satellite-flash panels, and any loop
    panel on a phone, have the bottom of the map to themselves and the dock
    returns when they close;
  - reset view and "Layers for this map".

  Every control reuses an existing handler: `activateMapRepresentation`,
  `changeTerrainDepth`, `changeStudioLight`, `updateSceneEffects`,
  `startTerrainInvestigation` (through `startCategoryTransect`),
  `enterUnderground`, `toggleDaylightVisibility` (through
  `showCategoryDaylight`), `beginMapMeasurement`, `watchRadarLoop`,
  `closeLiveInstrument` and `openAtlasPanel`. Turning river flow on or off also goes through
  `updateSceneEffects`. The dock can
  be hidden. It returns the next time a category map is opened.
- **Layers panel.** When a category is chosen in the Layers catalogue, its
  topic guide shows the same map-look card: name, scene and what you'll see.
  **Open this map** applies the look, and once the look is on the card reads
  "on the map now".
- **Shared URLs.** No new parameter is needed. `topic`, `base`, `proj` and
  `scene` already restore the category, basemap and renderer, and the dock
  follows the restored category when its basemap is on screen.

## What is not on every map

County boundaries, USGS river gauges and the USGS 3DHP stream network are
**off by default**. They appear on the maps whose subject they are (the civic,
community and reference maps start with counties; the water map with its
gauges) or when a visitor turns them on. The county payload still loads once
in the background so **Find a county** works; loaded but hidden layers are not
drawn (`searchNeedsCounties`).

The category basemaps follow the same rule. County lines are drawn only on the
civic style; river lines only on the river network and, as chart landmarks, the
aviation chart. Lakes stay in every style as water fill.

## In the Evidence Drawer

A selected record now opens with the category it belongs to, then the same
three questions for every source (`app/evidence-summary.ts`):

- **What it is** is the record's own summary. A provider basemap record is
  labelled as the provider's mapped record.
- **Where & when** gives the spatial scope and display anchor, then the
  observation or source time. The second clause is labelled by what it is:
  "retrieved …" for an official feature's retrieval time, "listed freshness: …"
  when only the source's cadence is known, and "record updated …" for a
  registry record. A provider basemap record gets no update clause.
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

Seven category styles live in `app/category-basemaps.ts`, listed with their
picker title, network note and legend in `CATEGORY_BASEMAPS`. Their keys are in
the import-free `app/category-basemap-keys.ts`, which the allow-lists share.
They are built only from carriers already listed in
`app/external-context-sources.ts`:

- OpenFreeMap vector tiles and fonts (`openfreemap-liberty`);
- the Terrarium display DEM (`aws-mapzen-terrarium`), for relief;
- the bundled Census Kansas boundary (simplified for state-scale display) and graticule.

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
| `historic` | Historic atlas | History |

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

### Historic atlas (`historic`)

- a parchment ground with a sepia hillshade and the bundled 1° graticule;
- railroads are the subject: an ink line crossed by ties, the way atlases drew
  the lines that placed Kansas towns;
- county lines are dotted and the state line is dash-dot;
- modern roads, urban areas and water recede;
- city names are letter-spaced capitals, and river names follow their courses.

It is present-day OpenMapTiles geography drawn in an atlas style, not a
historical map. The History look adds the dated layers on top: the digitized
1918 road map and abandoned railroads, each with its own source limitation.
OpenFreeMap provides only Noto Sans, so the atlas feel comes from spacing,
case and colour rather than a serif face.

### Shared behaviour

- **Fallback.** All seven styles use the `openmaptiles` source id. If that carrier
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

- The vector layers of all seven styles were validated against the MapLibre
  style specification and by tests. Their relief, tint and outline layers were
  rendered in a browser. It was not rendered against live
  OpenFreeMap tiles in the build container, which cannot reach that host.
- The aviation chart basemap draws airports from OpenStreetMap data, not the
  FAA NASR airport list, and carries no airspace itself. The Aviation look
  switches on the separate airspace layer (`overlays: ["aviation"]`, see
  `docs/aviation-layers.md`), which draws FAA NASR airspace as 3D volumes or a
  2D chart, airports, drone ceilings, TFRs, weather and live traffic.

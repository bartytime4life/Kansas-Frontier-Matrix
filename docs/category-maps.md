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
  - **Show day and night**, on the Sky globe and the Satellite view
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

## Population in 3D (People)

The People map draws every Kansas county as a column (`app/population-prisms.ts`).
Each column is built from the same 2020 Census county record the Evidence
Drawer shows:

- **Height** is linear in density: 100 m for every person per square mile of
  land (`AREALAND`, water excluded). There is no logarithm and no exaggeration,
  so the metro counties stand as tall as their density says.
- **Colour** is the county's Kansas population density peer group, the KDHE
  classification: Frontier (under 6 people per square mile), Rural (6–19.9),
  Densely-settled rural (20–39.9), Semi-urban (40–149.9) and Urban (150 and
  over).
- The dock legend counts the counties in each group, and gives the statewide
  density (total people over total land, not an average of county ratios), from
  the loaded payload.
- A selected column opens its county record, which now carries
  `peoplePerSquareMile` and `densityGroup` beside the counts.
- The county layer's opacity slider fades the columns (as drawn at its
  default setting, gone at zero), and a shared link (`prisms=on`) reopens with
  them standing.

The columns replace the county outline while they stand, are hidden on the
globe, and appear in the start-page preview of the People map. Counts describe
areas, not people; a county's column says nothing about where in the county
people live.

## Soil moisture on the Field view (Agriculture)

The Field view opens on the 2024 Kansas aerial imagery at field scale. Its dock
adds **Show soil moisture**: NASA SMAP Level-4 (SPL4SMAU V008) modelled soil
moisture, through the Explorer's own soil-moisture control
(`app/soil-moisture-control.tsx`).

- SMAP cells are 9 km across; at field scale one cell would fill the screen and
  read as a per-field value it is not. Switching the tool on therefore pulls a
  closer view out to zoom 7.2, the region the cells describe.
- **Surface 0–5 cm** and **Root zone 0–100 cm** switch the modelled depth.
- The reading names the frame actually drawn (its UTC day and depth), or says
  plainly that NASA is unavailable and nothing is drawn; NASA's own colour scale
  sits beneath it.
- Soil moisture stays with the maps that offer it: opening another category map
  hides it.
- The control now checks NASA's available days whenever it is switched on from
  outside its own row (the dock, or a shared link that restores `soil=1`), not
  only from its switch.

## Saturated thickness on the Aquifer map (Groundwater)

The Aquifer map opens on the Kansas Geological Survey's 2022–2024 saturated
thickness of the High Plains aquifer: how many feet of the aquifer still hold
water. It is centred on western Kansas, where the aquifer is. Its dock switches
one KGS view at a time:

- **Thickness**, classes from under 50 to over 300 feet;
- **Depth to water**, from under 25 to over 350 feet below the land surface;
- **Extent**, where the aquifer is mapped.

The legend lists the KGS classes in feet with the colours the snapshots carry
(`GROUNDWATER_CLASS_LEGENDS`); `tests/aquifer-legend.test.mjs` keeps it equal to
the snapshot files in `public/data/groundwater/`. These are regional classified
estimates, not well measurements; Explore underground opens the recorded well
logs and cores.

## Reviewed snapshots from the site database

The River network, Storm desk and Hazard watch docks offer **Reviewed …
snapshots**: the hourly USGS discharge and NWS alert captures that the site's
publishing pipeline normalized, checked against their signed manifest and
committed to the site's MySQL database (`server/pipeline-*.mjs`), read through
`/api/curated/{source}` and its `/history` (up to 20 releases).

- Gauges are circles whose area grows with discharge: radius = 3 + 0.06·√Q px
  (Q in ft³/s), from a 3 px floor and capped at 62,500 ft³/s. Provisional USGS
  values carry an amber ring, approved values a white one; a gauge without a
  value is not drawn as zero. While a snapshot is drawn, the dock keys the
  scale at 100, 1,000, 10,000 and 62,500+ ft³/s at the sizes drawn, and the
  two rings (`REVIEWED_DISCHARGE_KEY` in `app/map-keys.ts`, which the gauge
  layer also reads). Reviewed alert snapshots share the live NWS severity key.
- Alert areas take their NWS severity colour; alerts that have expired leave
  the display, as on `/curated`.
- The scrubber runs oldest to newest; each step names the hour the capture is
  for, when it was published and how many features it holds, and says when it
  is older than two hours. Play steps forward and stops at the newest.
- A release is shown only while its publication approval holds: the history
  is read again every minute, so a release whose approval lapses or is revoked
  leaves the scrubber, and a shown release leaves the map the moment its own
  `approvalExpiresAt` passes. With no release picked, the newest is followed as
  new ones are published.
- A newly picked release reads as loading until it is drawn, and Play steps on
  only after each release has been drawn.
- When the pipeline is not switched on, has no approved release, or the
  database is unavailable, the dock says so and nothing is drawn.

The snapshots are drawn by the context renderer (`app/reviewed-snapshot-layers.ts`)
and are approved context releases, not admitted evidence.

## Map keys

A map whose starter layers encode a value shows a key for each one in its
dock, while that layer is on (`app/map-keys.ts`). The layer styles and the keys
read the same constants, so the two cannot drift apart:

- **Earthquake magnitude** (Landform relief): USGS magnitude; colour and
  circle size both rise with it. The key draws M 0, 2, 4 and 6+ at their
  statewide (zoom 4) sizes.
- **NWS alert severity** (Storm desk, Hazard watch): the alert's CAP severity,
  as one ordinal palette for live and reviewed alerts alike. It runs from pale
  yellow (Minor) through orange and red to magenta (Extreme, the Storm
  Prediction Center's colour for its highest risk), each step more salient on
  the dark storm base. An alert without a recognised severity is neutral grey,
  off the scale.

- **Satellite fire detections (VIIRS)** and **Reported fire incidents
  (NIFC)** (Hazard watch): a detection is a dot at its pixel centre coloured
  by detection confidence (with the dashed scan × track pixel close in); a
  reported incident is a ring coloured by incident type. The two datasets no
  longer share a symbol, and nothing animates (`docs/fire-close-zoom.md`).
- **KDOT roads and rail** (Network map) and **1918 roads and former rail**
  (Historic atlas): the lines KDOT's service draws with our symbols
  (`KDOT_LINE_SYMBOLS`), so the request and the key share them. Public roads
  are amber, active railroads teal, 1918 state highways brick red, and
  abandoned railroads violet and dashed; dashes mean former rail only. The
  KDOT colours had been chosen for the dark default map: on the Network map's
  near-white ground and the Historic atlas's parchment they reached only
  1.04–1.3:1, and the 1918 roads and abandoned rail were the same orange dash.
  Each colour now has at least 3:1 against both the light category grounds
  and the dark ones, and no two datasets share one. Lines of one map are
  keyed together under one title.
- **Elevation** (Relief model, Landform relief, Aviation chart): the basemaps
  that colour the ground by height show their ramp as a bar, first in the
  dock, while that basemap is drawn. The bar is built from the same stops the
  style uses (`RELIEF_RAMP`, `AVIATION_TINT_BANDS` in
  `app/category-basemaps.ts`). The relief key is continuous, in metres above
  sea level (200–1,300 m, ticks every 300 m). The aviation chart's key is
  stepped into its 1,000 ft bands and labelled in feet, as sectional charts
  are. Both notes give the state's span, 207 m (679 ft) where the Verdigris
  River leaves Kansas to 1,231 m (4,039 ft) at Mount Sunflower, so a reader
  can turn a colour into a height. The key is gone when the basemap is not
  (photo-real ground, or the local fallback style).

Radar keeps its dBZ legend in its own panel, and stream gauges keep theirs in
River Pulse.

## Earthquake record (Landform relief)

The Landform relief dock's **Earthquake record since 1973** replaces the rolling
30-day catalog with every USGS ComCat earthquake of magnitude 2.5 or more whose
epicentre lies inside Kansas, from 1 January 1973 to now
(`app/earthquake-record.ts`, served by `/api/earthquake-record`).

- **Source and clip.** One FDSN event query over the state's bounding box,
  oldest first, kept on the server for six hours. Events in the box but outside
  the Census state outline (northern Oklahoma, north-west Missouri) are dropped
  and counted; the outline is accurate to a few hundred metres, finer than the
  catalog's epicentre uncertainty. If the provider returns more than 6,000
  events the reading says the answer was cut short.
- **Symbols.** Size is magnitude, on the record's own scale (it holds far more
  events than 30 days). Colour is the year: 1973–2009 share one dark violet,
  when Kansas had few seismometers and few M2.5+ events, then the perceptually
  ordered "plasma" ramp runs from 2010 to the current year, so the rise in
  south-central Kansas after 2013 is read by colour as well as by place. Larger
  events draw on top.
- **Histogram.** The dock charts events per year in each year's map colour, so
  the chart is also the colour key. A bar, or the Year list, shows one year on
  the map; the reading gives the count and the busiest year.
- **Selection.** Selecting an event shows its magnitude and magnitude type,
  UTC time, USGS place, depth and review status in the dock, with a link to the
  USGS event page. The basemap beneath is not inspected.
- **Limits.** Detection improved as seismometers were added after 2013, so early
  decades miss some small events and counts across decades are not directly
  comparable. Locations, magnitudes and review status can be revised by USGS.
  Hiding the record brings the 30-day catalog back; leaving the map closes it.

## SPC convective outlook (Storm desk)

The Storm desk dock's **Show the SPC severe outlook** draws the NOAA Storm
Prediction Center's categorical convective outlook for Day 1, 2 or 3
(`app/spc-outlook.ts`, served by `/api/spc-outlook?day=`), beside radar and
alerts.

- **Source.** SPC's own `dayNotlk_cat.lyr.geojson`, kept ten minutes on the
  server and re-read in the browser once a shown day is a quarter-hour old,
  since SPC reissues Day 1 several times a day. Only SPC's six categories
  (TSTM, MRGL, SLGT, ENH, MDT, HIGH) with valid polygons are drawn; provider
  properties other than the category do not travel.
- **Symbols.** Outlines, not fills, so radar reflectivity keeps its colours, in
  SPC's own category fill colours, which stay legible on the dark storm base
  where SPC's darker stroke colours do not. Higher categories lie inside lower
  ones, as SPC layers them. The key lists the categories with SPC's numbering,
  1 Marginal to 5 High.
- **Reading.** The highest category reaching Kansas (tested every 0.1°, about
  10 km, inside the Census outline), with the outlook's issue time and valid
  period in UTC, and a link to SPC's outlook page.
- **Limits.** The outlook is a forecast of risk, not an observation, a watch or
  a warning; probabilistic tornado, wind and hail outlooks are not drawn.
  Leaving the map closes it.

## Photo-real 3D (Terrain)

The Relief model dock's **Photo-real 3D** drapes the photographed ground on the
measured one: the 2024 Kansas NG911 one-foot aerial (over Esri world imagery,
which carries oblique views past the state line) on the USGS 3DEP bare-earth DEM
(`/api/3dep-dem-tile`), at **true vertical scale** (1×), lit by the real sun at
the map centre, with OpenStreetMap buildings raised to the heights OpenMapTiles
records (`render_height`, from `render_min_height`). The style is the
`photoreal` basemap: no labels, painted shading or stylisation over the
photograph. The photograph carries the real light of its flight, so the DEM
hillshade is not drawn while it is loaded, and the USGS 3DEP hillshade, if
switched on, is switched off on entry and back on with "Back to relief
colours".

It flies to six real landscapes (`app/photoreal-landscapes.ts`), each captioned
with what the ground is: the Red Hills (Permian red beds capped by gypsum),
Monument Rocks and Little Jerusalem (Niobrara Chalk), Konza Prairie in the
Flint Hills (Permian limestone and chert under tallgrass prairie), the Arikaree
Breaks (canyons in loess), and downtown Wichita on the Arkansas River. The
reading always states the vertical scale: "True vertical scale (1×)" or the
exaggeration chosen with Relief. The status bar's DEM readout gives the 3DEP
height under the pointer. "Back to relief colours" restores the look's own map,
the Mapzen relief and the default depth.

## What is not on every map

County boundaries, USGS river gauges, the USGS 3DHP stream network and the fire
layers (NOAA-20 fire detections and NIFC fire reports) are **off by default**;
the plain Explorer starts with no provider layer. They appear on the maps whose
subject they are (the civic, community and reference maps start with counties;
the water map with its gauges; Hazard watch with alert areas, fire detections
and fire reports) or when a visitor turns them on. The county payload still loads once
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
- lakes, main roads, peaks and towns stay quiet.

It is mixed-source display elevation, not survey measurement.

### Storm desk (`storm`)

- a neutral charcoal ground; every colour in the style has low chroma, so
  radar, alert and fire colours stay distinguishable;
- the state line and town labels show where weather is hitting.

Weather layers keep their own clocks.

### Network map (`network`)

- road classes in colour (motorway, trunk, primary, secondary), white-cased,
  with darker casing on bridges;
- route numbers from `transportation_name`;
- classic dark rail with white ties, plus runways.

It is display context, not traffic, condition or access.

### Historic atlas (`historic`)

- a parchment ground with a sepia hillshade and the bundled 1° graticule;
- railroads are the subject: an ink line crossed by ties, the way atlases drew
  the lines that placed Kansas towns;
- the state line is dash-dot;
- modern roads, urban areas and water recede;
- city names are letter-spaced capitals.

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
  `CATEGORY_BASEMAP_HILLSHADE_LAYER_ID`. The 2D relief scene effect and, in
  3D, the terrain hillshade (`kfm-terrain-hillshade`) both defer to it, so
  shading is never doubled. The overlay sync lights it as the scene is lit:
  from the sun's direction and at its height (held between 12° and 60°), so
  the real sun lengthens and turns its shadows. The Relief model no longer
  starts with the USGS 3DEP hillshade, whose fixed multidirectional light
  would contradict the scene's sun; it stays in Layers for finer detail.
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

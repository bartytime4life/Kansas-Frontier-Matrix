import type { Feature, FeatureCollection, LineString, Point } from "geojson";

export type ScienceSupport = "connected" | "mixed" | "download" | "derived" | "reference" | "steward";
export type ScienceGeometry = "point" | "path" | "area" | "surface" | "network" | "aggregate" | "profile";
export type ScienceClock = "instant" | "interval" | "daily" | "annual" | "edition" | "paired" | "static";
export type ScienceTrackId = "radar" | "smoke" | "river" | "geology" | "flora" | "fauna" | "resources" | "counties" | "weather" | "earthquakes" | "shake";

export type ScienceEventSpec = Readonly<{
  id: string;
  title: string;
  glyph: string;
  color: string;
  geometry: ScienceGeometry;
  clockKind: ScienceClock;
  clock: string;
  representation: string;
  measurement: string;
  support: ScienceSupport;
  trackId?: ScienceTrackId;
  sourceLabel: string;
  sourceUrl: string;
  limitation: string;
}>;

export const SCIENCE_SUPPORT_LABELS: Readonly<Record<ScienceSupport, string>> = Object.freeze({
  connected: "CONNECTED",
  mixed: "PARTLY CONNECTED",
  download: "DOWNLOAD",
  derived: "DERIVE",
  reference: "REFERENCE",
  steward: "STEWARD DATA",
});

// This registry is a display contract, not a claim that every carrier is live.
// Each phenomenon keeps its own clock, visual grammar, metric and admission state.
export const SCIENCE_EVENTS: readonly ScienceEventSpec[] = Object.freeze([
  {
    id: "tornadoes", title: "Tornadoes", glyph: "↯", color: "#ef8f73", geometry: "path", clockKind: "interval",
    clock: "Recorded begin/end time; path survey edition",
    representation: "Reveal a tapered damage corridor between surveyed start/end points; show EF class by width and a hatched uncertainty halo.",
    measurement: "Path length, maximum width, EF rating, injuries/fatalities",
    support: "download", sourceLabel: "NOAA Storm Events bulk archive", sourceUrl: "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/",
    limitation: "Annual event files require parsing, spatial review and duplicate handling before a path can be admitted. A county event record is not a surveyed tornado track.",
  },
  {
    id: "floods", title: "Floods", glyph: "≋", color: "#58c8e4", geometry: "area", clockKind: "interval",
    clock: "Gauge sample time plus documented event/extent interval",
    representation: "Pair pulsing gauges and hydrographs with observed inundation outlines; use threshold bands only when a station datum supplies them.",
    measurement: "Discharge, stage, crest, duration and inundated area",
    support: "mixed", trackId: "river", sourceLabel: "USGS Water Data + NOAA Storm Events", sourceUrl: "https://api.waterdata.usgs.gov/",
    limitation: "The connected lane is discharge, not a flood classification or continuous inundation surface. Historical extents remain a separate reviewed input.",
  },
  {
    id: "history", title: "Historical landscape", glyph: "◫", color: "#d9bd82", geometry: "surface", clockKind: "edition",
    clock: "Map edition/publication date, kept separate from feature date",
    representation: "Use edition-stamped georeferenced sheets with swipe/A–B comparison and visible registration-error bounds.",
    measurement: "Edition, scale, control-point error and mapped change",
    support: "steward", sourceLabel: "USGS topoView", sourceUrl: "https://ngmdb.usgs.gov/topoview/",
    limitation: "Publication year does not date every road, town or boundary on a sheet. A scan needs reviewed georeferencing and rights metadata.",
  },
  {
    id: "erosion", title: "Erosion & deposition", glyph: "↘", color: "#e4a86e", geometry: "profile", clockKind: "paired",
    clock: "Two pinned acquisition epochs; never the shared cursor alone",
    representation: "Show a signed elevation-change surface, before/after transect and confidence mask: loss in warm tones, deposition in cool tones.",
    measurement: "Vertical change, volume balance, slope and uncertainty",
    support: "derived", sourceLabel: "USGS 3DEP elevation program", sourceUrl: "https://www.usgs.gov/3d-elevation-program",
    limitation: "Erosion cannot be inferred from one hillshade. It requires co-registered surfaces, error propagation and a documented change method.",
  },
  {
    id: "elevation", title: "Elevation & terrain", glyph: "△", color: "#d6c78f", geometry: "surface", clockKind: "edition",
    clock: "DEM acquisition/work-unit date; display date stays independent",
    representation: "Combine physical-scale 3D relief, hillshade, hypsometric color, contours and an unexaggerated transect profile.",
    measurement: "Elevation, relief, slope, aspect and profile distance",
    support: "reference", sourceLabel: "USGS 3DEP / LiDAR Explorer", sourceUrl: "https://apps.nationalmap.gov/lidar-explorer/",
    limitation: "Display terrain is not survey grade and does not reconstruct the surface on the selected historical day.",
  },
  {
    id: "cities", title: "Cities & settlements", glyph: "◆", color: "#f1d485", geometry: "point", clockKind: "edition",
    clock: "Gazetteer/Census vintage or documented founding/active interval",
    representation: "Use proportional population circles with a vintage ring; historical settlement labels fade only outside a documented active interval.",
    measurement: "Population, housing, incorporated area and vintage",
    support: "reference", trackId: "counties", sourceLabel: "U.S. Census TIGER/Line", sourceUrl: "https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html",
    limitation: "The connected Census county baseline is not a historical city boundary reconstruction. Place vintages must remain explicit.",
  },
  {
    id: "roads", title: "Roads", glyph: "━", color: "#b9c9c3", geometry: "network", clockKind: "edition",
    clock: "Network edition/year; construction and closure dates when known",
    representation: "Draw class-weighted lines with edition badges; A/B mode highlights additions, removals and unchanged segments separately.",
    measurement: "Length, class, connectivity, travel distance and edition change",
    support: "reference", sourceLabel: "U.S. Census TIGER/Line", sourceUrl: "https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html",
    limitation: "The present basemap is modern reference context. It must never be treated as the road network for a historical event date.",
  },
  {
    id: "trade-routes", title: "Trade routes", glyph: "⇢", color: "#dd9fd0", geometry: "path", clockKind: "interval",
    clock: "Documented operating interval and source-map edition",
    representation: "Use directional corridors, documented stops and a translucent route-confidence band rather than a falsely precise centerline.",
    measurement: "Route distance, documented stops, operating span and confidence",
    support: "steward", sourceLabel: "Library of Congress Kansas maps", sourceUrl: "https://www.loc.gov/maps/?fa=location:kansas",
    limitation: "A traced historical route is an interpretation. Provenance, scale, georeferencing error and competing route hypotheses must remain visible.",
  },
  {
    id: "snow", title: "Snow", glyph: "✦", color: "#d9f2ff", geometry: "surface", clockKind: "daily",
    clock: "Observation day or event begin/end; no invented hourly change",
    representation: "Combine station snow-depth/accumulation glyphs with a separately sourced gridded surface and unit-aware stepped legend.",
    measurement: "Snowfall, snow depth, water equivalent and duration",
    support: "mixed", trackId: "weather", sourceLabel: "NOAA GHCN-D + Storm Events", sourceUrl: "https://www.ncei.noaa.gov/pub/data/ghcn/daily/",
    limitation: "The connected weather lane currently maps temperature and precipitation summaries, not a statewide snow field.",
  },
  {
    id: "ice", title: "Ice", glyph: "◇", color: "#9fd7ef", geometry: "area", clockKind: "interval",
    clock: "Event begin/end or daily observation",
    representation: "Use a diagonal hatch for affected areas, point observations for measured accretion and a distinct road-impact overlay.",
    measurement: "Accretion, duration, temperature and reported impacts",
    support: "download", sourceLabel: "NOAA Storm Events bulk archive", sourceUrl: "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/",
    limitation: "Narrative event areas and point measurements have different precision. Neither should be rendered as a continuous thickness surface without a method.",
  },
  {
    id: "foliage", title: "Foliage & vegetation", glyph: "✣", color: "#9ed878", geometry: "aggregate", clockKind: "annual",
    clock: "Occurrence year; future phenology imagery uses acquisition date",
    representation: "Show generalized flora-record hexagons now; reserve seasonal color ramps for a separately named vegetation/phenology product.",
    measurement: "Occurrence density now; vegetation index and phenophase only from future qualified data",
    support: "mixed", trackId: "flora", sourceLabel: "GBIF Maps API", sourceUrl: "https://techdocs.gbif.org/en/openapi/v2/maps",
    limitation: "Plant occurrence density is not foliage cover, greenness, abundance or absence and is strongly affected by sampling effort.",
  },
  {
    id: "fauna", title: "Fauna", glyph: "◉", color: "#cdb2f2", geometry: "aggregate", clockKind: "annual",
    clock: "Occurrence year; exact record dates remain provider metadata",
    representation: "Use coarse annual hex density with taxon filters; never animate movement between unrelated occurrence records.",
    measurement: "Generalized occurrence density and taxonomic richness",
    support: "connected", trackId: "fauna", sourceLabel: "GBIF Maps API", sourceUrl: "https://techdocs.gbif.org/en/openapi/v2/maps",
    limitation: "Records are not abundance, migration tracks, habitat suitability or proof of absence. Sensitive locations remain generalized.",
  },
  {
    id: "smoke", title: "Smoke", glyph: "≈", color: "#dda16b", geometry: "area", clockKind: "interval",
    clock: "NOAA analysis Start ≤ cursor < End",
    representation: "Draw categorical satellite-analysis footprints with stable edges between source intervals and density-specific fill patterns.",
    measurement: "Column-density category, footprint area and supported duration",
    support: "connected", trackId: "smoke", sourceLabel: "NOAA HMS", sourceUrl: "https://www.ospo.noaa.gov/products/land/hms.html",
    limitation: "HMS is not surface PM2.5, plume height or measured transport. No decorative wind particles or interpolated polygon motion.",
  },
  {
    id: "water-levels", title: "Water levels & flow", glyph: "●", color: "#6fd7e5", geometry: "profile", clockKind: "instant",
    clock: "Exact station sample; connected discharge held ≤30 minutes",
    representation: "Use station pulses keyed to trend, a gap-aware hydrograph and separate stage/flood-threshold bands when that datum is available.",
    measurement: "Discharge, stage, trend, sample age and qualifiers",
    support: "mixed", trackId: "river", sourceLabel: "USGS Water Data APIs", sourceUrl: "https://api.waterdata.usgs.gov/",
    limitation: "Current map values are discharge parameter 00060. Radius is log-scaled display, not channel width, stage or flood extent.",
  },
  {
    id: "earthquakes", title: "Earthquakes", glyph: "✹", color: "#ee9e88", geometry: "point", clockKind: "instant",
    clock: "USGS catalog origin time; points accumulate to the cursor",
    representation: "Scale rings by magnitude, encode depth by tone and expose catalog time, depth and review status on selection.",
    measurement: "Magnitude, depth, origin time and distance/bearing",
    support: "connected", trackId: "earthquakes", sourceLabel: "USGS FDSN event service", sourceUrl: "https://earthquake.usgs.gov/fdsnws/event/1/",
    limitation: "Catalog completeness changes across time. No returned event is not proof of no earthquake, and a sensor is not an event.",
  },
  {
    id: "radar", title: "Radar & severe weather context", glyph: "◌", color: "#71d8b8", geometry: "surface", clockKind: "instant",
    clock: "Exact listed five-minute mosaic validity slot",
    representation: "Render source reflectivity colors one exact mosaic at a time; use event paths as separate overlays, never inferred from radar color alone.",
    measurement: "Reflectivity class, valid time and archive coverage",
    support: "connected", trackId: "radar", sourceLabel: "NOAA/NWS-derived IEM mosaics", sourceUrl: "https://mesonet.agron.iastate.edu/docs/nexrad_composites/",
    limitation: "A mosaic is not a simultaneous scan and does not by itself prove a tornado, hail report or surface precipitation amount.",
  },
  {
    id: "geology", title: "Geology", glyph: "▧", color: "#cfabd9", geometry: "area", clockKind: "static",
    clock: "Mapped-geology edition, independent of event time",
    representation: "Use unit polygons/colors with an inspectable stratigraphic legend; pin rock age separately from map publication date.",
    measurement: "Map unit, geologic age, area and source scale",
    support: "reference", trackId: "geology", sourceLabel: "Kansas Geological Survey", sourceUrl: "https://kgs.ku.edu/geology-and-mineral-resources",
    limitation: "The current cached carrier has an unconfirmed edition and does not supply a subsurface volume or deep-time reconstruction.",
  },
  {
    id: "resources", title: "Mapped resources", glyph: "⬡", color: "#e3c269", geometry: "aggregate", clockKind: "edition",
    clock: "Pinned topographic-map edition",
    representation: "Use county-shaded counts with an edition control and inspectable symbol totals; preserve gaps instead of implying zero resources.",
    measurement: "Mapped symbol count by county and edition",
    support: "connected", trackId: "resources", sourceLabel: "USGS topographic mine symbols", sourceUrl: "https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/USGS_Topographic_Mine_Symbols/FeatureServer/8",
    limitation: "Counts are historical map symbols, not unique mines, operating dates, reserves, ownership or economic potential.",
  },
]);

export type ScienceCoordinate = readonly [longitude: number, latitude: number];

const radians = (degrees: number) => degrees * Math.PI / 180;
const degrees = (value: number) => value * 180 / Math.PI;

export function scienceMeasurement(points: readonly ScienceCoordinate[]) {
  if (points.length < 2) return null;
  const [[longitude1, latitude1], [longitude2, latitude2]] = points;
  const latitudeDelta = radians(latitude2 - latitude1);
  const longitudeDelta = radians(longitude2 - longitude1);
  const a = Math.sin(latitudeDelta / 2) ** 2
    + Math.cos(radians(latitude1)) * Math.cos(radians(latitude2)) * Math.sin(longitudeDelta / 2) ** 2;
  const arc = Math.max(0, Math.min(1, a));
  const kilometers = 6371.0088 * 2 * Math.atan2(Math.sqrt(arc), Math.sqrt(1 - arc));
  const y = Math.sin(longitudeDelta) * Math.cos(radians(latitude2));
  const x = Math.cos(radians(latitude1)) * Math.sin(radians(latitude2))
    - Math.sin(radians(latitude1)) * Math.cos(radians(latitude2)) * Math.cos(longitudeDelta);
  return Object.freeze({ kilometers, miles: kilometers * 0.6213711922, bearing: (degrees(Math.atan2(y, x)) + 360) % 360 });
}

export function scienceProbeGeoJSON(points: readonly ScienceCoordinate[]): FeatureCollection<LineString | Point, { kind: "line" | "vertex"; sequence?: number }> {
  const coordinates = points.slice(0, 2).map(([longitude, latitude]) => [longitude, latitude]);
  const features: Feature<LineString | Point, { kind: "line" | "vertex"; sequence?: number }>[] = [];
  if (coordinates.length === 2) features.push({ type: "Feature", properties: { kind: "line" }, geometry: { type: "LineString", coordinates } });
  coordinates.forEach((coordinate, index) => features.push({ type: "Feature", properties: { kind: "vertex", sequence: index + 1 }, geometry: { type: "Point", coordinates: coordinate } }));
  return { type: "FeatureCollection", features };
}

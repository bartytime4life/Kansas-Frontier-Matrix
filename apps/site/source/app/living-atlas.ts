import type { MapViewProfile } from "./map-interface";

export type LivingAtlasViewStatus = "REAL_BASELINE";

export type LivingAtlasView = Readonly<{
  id: string;
  title: string;
  question: string;
  scope: string;
  domains: readonly string[];
  display: "2D" | "Terrain 3D" | "Globe" | "Story";
  time: string;
  sourcePosture: string;
  motion: string;
  report: string;
  status: LivingAtlasViewStatus;
  profileId?: MapViewProfile["id"];
  story?: boolean;
  camera?: Readonly<{
    center: readonly [number, number];
    zoom: number;
    bearing: number;
    pitch: number;
  }>;
  note: string;
}>;

const camera = (
  center: readonly [number, number],
  zoom: number,
  bearing = 0,
  pitch = 0,
) => Object.freeze({ center, zoom, bearing, pitch });

/**
 * Map starting views use provider-backed context only. Proposed views without
 * real source bindings stay out of the selectable map library.
 */
export const LIVING_ATLAS_VIEWS: readonly LivingAtlasView[] = Object.freeze([
  Object.freeze({
    id: "kansas-overview",
    title: "Kansas Overview",
    question: "Where should I begin?",
    scope: "Kansas statewide",
    domains: ["places", "water", "movement"],
    display: "2D",
    time: "Today’s observations + pinned Census edition",
    sourcePosture: "Census county baseline + USGS water sources",
    motion: "Paused; camera only",
    report: "Statewide orientation + report starter",
    status: "REAL_BASELINE",
    profileId: "overview",
    camera: camera([-98.38, 38.48], 5.45),
    note: "Opens on all 105 real county boundaries, decennial population/housing counts, stream observations and mapped hydrography. No synthetic overlay starts enabled.",
  }),
  Object.freeze({
    id: "county-atlas",
    title: "County Atlas",
    question: "What is present, changing, or missing here?",
    scope: "Choose a county; Ellsworth is the pilot focus",
    domains: ["places", "water", "coverage"],
    display: "2D",
    time: "2020 Census baseline; 2010 comparison available",
    sourcePosture: "105 Census county boundaries and counts",
    motion: "Step declared catalog time",
    report: "County dossier + coverage table",
    status: "REAL_BASELINE",
    profileId: "overview",
    camera: camera([-98.45, 38.56], 8.1),
    note: "Click a real county boundary to inspect its population, housing and land/water area. Use the archive for independently dated 2010 and 2020 baseline editions.",
  }),
  Object.freeze({
    id: "terrain-landforms",
    title: "Terrain & Landforms",
    question: "How does the land rise and shape a route?",
    scope: "Kansas landform regions",
    domains: ["geology", "hydrology"],
    display: "Terrain 3D",
    time: "Provider-published elevation mosaic",
    sourcePosture: "USGS 3DEP hillshade and reference terrain",
    motion: "Optional orbit; no data clock",
    report: "Elevation concept + limitations",
    status: "REAL_BASELINE",
    profileId: "elevation",
    camera: camera([-96.55, 38.55], 7.85, -22, 48),
    note: "Shows actual published elevation-derived terrain context. The layer retains its source limitations and makes no acquisition-date or accuracy claim for an individual pixel.",
  }),
  Object.freeze({
    id: "living-waters",
    title: "Living Waters",
    question: "What connects this river, basin, and place?",
    scope: "Kansas river corridors",
    domains: ["hydrology", "habitat"],
    display: "2D",
    time: "Exact USGS samples + provider-current GIS",
    sourcePosture: "USGS observations, hydrography and NOAA context",
    motion: "Exact gauge frames; gaps break paths",
    report: "USGS and NOAA source clocks",
    status: "REAL_BASELINE",
    profileId: "water",
    camera: camera([-96.75, 39.0], 7.35, 12, 42),
    note: "Start with real observations and mapped waterways. Explore each station’s declared record span and daily or continuous samples in the archive. No gauge value is generalized to a reach or basin.",
  }),
  Object.freeze({
    id: "smoke-transport",
    title: "Smoke Transport",
    question: "How should smoke context be inspected without overclaiming it?",
    scope: "Kansas plus regional context",
    domains: ["smoke", "fire", "hazards"],
    display: "2D",
    time: "NOAA analysis intervals and observed radar times",
    sourcePosture: "NOAA HMS polygons and radar images",
    motion: "Presentation effect; no forecast",
    report: "Smoke context + boundary notes",
    status: "REAL_BASELINE",
    profileId: "smoke",
    camera: camera([-99.0, 38.7], 6.4, 8, 18),
    note: "Actual smoke footprints and observed radar frames retain their provider times. This layer does not infer smoke movement, surface concentration, or exposure.",
  }),
]);

export const livingAtlasStatusLabel = (_status: LivingAtlasViewStatus) => "REAL SOURCE BASELINE";

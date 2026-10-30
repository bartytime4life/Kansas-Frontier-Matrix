"use client";

import type { CSSProperties } from "react";
import type { CategoryMap, CategoryScene } from "./category-maps";
import type { SceneLight } from "./scene-effects";
import type { KansasDensityGroup } from "./population-prisms";
import type { PhotorealLandscape } from "./photoreal-landscapes";
import type { MapKey } from "./map-keys";
import type { DepthSection, EarthquakeRecordEvent, MagnitudeFrequency, YearCount } from "./earthquake-record";
import type { FloodGauge, FloodHydrograph } from "./flood-forecast";
import type { FemaYear, HAZARD_FAMILIES, HazardFamilyId } from "./fema-record";
import type { RainfallKind } from "./mrms-rainfall";
import type { TornadoYear } from "./tornado-record";
import type { WellPlot } from "./well-levels";
import type { SunChart } from "./sun-chart";
import type { MoonStrip } from "./moon";
import type { CropFamily, RotationPattern } from "./crop-history";
import type { OutlookDay, OutlookProduct } from "./spc-outlook";
import type { ReportDay, StormReport } from "./storm-reports";

export type AquiferView = "kgs-saturated-thickness" | "kgs-depth-to-water" | "kgs-aquifer-high-plains";
const AQUIFER_VIEWS: readonly (readonly [AquiferView, string, string])[] = [
  ["kgs-saturated-thickness", "Thickness", "Saturated thickness: how much of the aquifer still holds water, in feet"],
  ["kgs-depth-to-water", "Depth to water", "Depth from the land surface down to the water table, in feet"],
  ["kgs-aquifer-high-plains", "Extent", "Where the High Plains aquifer is mapped"],
];

const MODES: readonly (readonly [CategoryScene, string, string])[] = [
  ["2d", "2D", "Flat map, straight down"],
  ["terrain", "3D", "Tilted 3D terrain"],
  ["globe", "Globe", "Whole-Earth globe"],
];

/** Compass label for a light azimuth (the direction the light comes from). */
export function azimuthLabel(degrees: number): string {
  const names = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"];
  return names[Math.round((((degrees % 360) + 360) % 360) / 45) % 8];
}

/**
 * Quarter-hour steps through the day for the time-of-day study. The last step
 * is 11:45 PM: a full fraction would be tomorrow's midnight, outside the day
 * the slider measures against.
 */
export const SUN_TIME_STEPS = 96;
/** Play the day restarts here once it has reached the end: 5:00 AM, before sunrise in every Kansas season. */
export const SUN_PLAY_RESTART_STEP = 20;

/** The day fraction of the next quarter-hour step, or null once the last step (11:45 PM) is reached. */
export function nextSunStep(dayFraction: number): number | null {
  const step = Math.min(SUN_TIME_STEPS - 1, Math.max(0, Math.floor((Number.isFinite(dayFraction) ? dayFraction : 0) * SUN_TIME_STEPS + 1e-9)));
  return step >= SUN_TIME_STEPS - 1 ? null : (step + 1) / SUN_TIME_STEPS;
}
const SUN_CLOCK = new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", hour: "numeric", minute: "2-digit", timeZoneName: "short" });

/** Plain reading of the computed sun over the map center, at the time it was computed. */
export function sunReading(light: SceneLight, at: number): string {
  const time = Number.isFinite(at) ? ` · ${SUN_CLOCK.format(at)}` : "";
  return light.source === "sun"
    ? `${Math.round(light.solarElevation ?? light.altitude)}° up, from ${azimuthLabel(light.azimuth)}${time}`
    : `Below the horizon · night fill${time}`;
}

/**
 * The category map's own instrument panel: which map look is on, and the few
 * controls most explorations need. Every action reuses an existing Explorer
 * handler; the dock holds no map state of its own.
 */
/** A collapsible list of map features as buttons, for picking one by keyboard or screen reader. */
/** "40 of 89" when a list holds fewer than all, else just the count. */
const shownOf = (shown: number, total: number) => total > shown ? `${shown} of ${total.toLocaleString("en-US")}` : String(shown);

function PickList({ summary, label, items, selected, onPick }: Readonly<{ summary: string; label: string; items: readonly Readonly<{ id: string; label: string }>[]; selected: string | null; onPick: (id: string) => void }>) {
  return <details className="category-map-dock-context">
    <summary>{summary}</summary>
    <ul className="category-map-dock-picklist" aria-label={label}>
      {items.map(item => <li key={item.id}><button type="button" aria-pressed={selected === item.id} onClick={() => onPick(item.id)}>{item.label}</button></li>)}
    </ul>
  </details>;
}

const OUTLOOK_PRODUCT_CHOICES: readonly (readonly [OutlookProduct, string, string])[] = [
  ["cat", "Risk", "SPC's categorical risk, General thunderstorms to 5 High"],
  ["torn", "Tornado", "Probability of a tornado within 25 miles of a point, with SPC's intensity areas"],
  ["wind", "Wind", "Probability of damaging gusts (50 kt+) within 25 miles of a point, with SPC's intensity areas"],
  ["hail", "Hail", "Probability of hail 1 inch or larger within 25 miles of a point, with SPC's intensity areas"],
];

export function CategoryMapDock({ onReviewedDate, civic, onCivicPick, onCivicCongress, onCivicPresent, onCivicRetry, look, mode, depth, azimuth, sun, sunAvailable = true, terrainAvailable, onMode, onDepth, onAzimuth, onRealSun, onSunTime, sunPlaying, motionAllowed, onSunPlay, onTransect, onUnderground, daylight, onDaylight, onDaylightPlay, sunYear, onSunYear, onSunYearCentre, onSunYearPlace, measuringArea, onMeasureArea, population, onPopulation, populationChange, onPopulationChange, onPopulationChangePick, onPopulationChangeClear, quakes, onQuakes, onQuakeYear, onQuakeClear, onQuakePick, outlook, onOutlook, onOutlookProduct, reports, onReports, onReportPick, onReportClear, soil, onSoil, onSoilDepth, drought, onDrought, onDroughtWeek, onDroughtPlay, onDroughtChange, onDroughtCounty, onDroughtCountyClear, aquifer, onAquiferView, surface, onSurface, onSurfacePick, onSurfaceClear, history, surveySoil, degreeDays, wells, onWells, onWellPick, onWellClear, reviewed, onReviewed, onReviewedClear, onReviewedPick, onReviewedIndex, onReviewedPlay, photoreal, onPhotoreal, radar, onRadar, flow, onFlow, flood, onFlood, onFloodPick, onFloodClear, fema, onFema, onFemaYear, onFemaFamily, onFemaEmergencies, onFemaCounty, onFemaCountyClear, rainfall, onRainfall, onRainfallKind, onRainfallHours, flora, onFlora, onFloraYear, onFloraOpacity, onFloraRetry, landCover, onLandCover, crops, onCrops, onCropsYear, legislature, onLegislature, onLegislaturePick, onLegislatureClear, tornadoes, onTornadoes, onTornadoYear, onTornadoRating, onTornadoPick, onTornadoClear, layerVisibility, onLayer, keys, onReset, onLayers, onClose }: Readonly<{
  civic?: Readonly<{ visible: boolean; state: string; day?: string | null; congress?: number | null; options?: readonly Readonly<{ value: number; label: string }>[]; items: readonly Readonly<{ id: string; label: string }>[] }>;
  onCivicCongress?: (congress: number) => void;
  onCivicPresent?: () => void;
  onCivicRetry?: () => void;
  onCivicPick?: (id: string, returnElement: HTMLElement) => void;
  look: CategoryMap;
  mode: CategoryScene;
  depth: number;
  azimuth: number;
  /**
   * The computed sun when the scene follows it; the hand-set light is then
   * ignored. `dayFraction` places `at` in its Kansas day; `live` is false while
   * the visitor studies another time of day.
   */
  sun: Readonly<{ light: SceneLight; at: number; dayFraction: number; live: boolean }> | null;
  /**
   * Whether the light changes this map: 3D terrain, or a category basemap with
   * its shaded relief. Flat imagery, topo and the standard base have none, so
   * the sun controls stay off the dock there.
   */
  sunAvailable?: boolean;
  terrainAvailable: boolean;
  onMode: (mode: CategoryScene) => void;
  onDepth: (value: number) => void;
  onAzimuth: (value: number) => void;
  onRealSun: (on: boolean) => void;
  /** A time of day as a fraction of today in Kansas, or null to follow the clock again. */
  onSunTime: (dayFraction: number | null) => void;
  /** Whether Play the day is sweeping the sun, and whether motion is allowed at all. */
  sunPlaying: boolean;
  motionAllowed: boolean;
  onSunPlay: (on: boolean) => void;
  /** Starts the terrain investigation for looks that offer the transect tool. */
  onTransect?: () => void;
  /** Opens the Underground view for looks that offer the underground tool. */
  onUnderground?: () => void;
  /**
   * The calculated day-and-night layer, for looks that offer the daylight
   * tool: whether it is shown and playing, its clock, and what that clock
   * means at the look's center.
   */
  daylight?: Readonly<{ on: boolean; playing: boolean; time: string; reading: string }>;
  /**
   * Daylight through the year at one Kansas place: shown or not, the place,
   * a click outside Kansas, the day's line, the year chart and a time-zone note.
   */
  sunYear?: Readonly<{ on: boolean; place: string | null; outside: boolean; reading: string | null; chart: SunChart | null; note: string | null; atCentre: boolean; coordinates?: Readonly<{ lon: number; lat: number }>;
    /** The Moon at the same place: tonight's line, the next principal phases, and the next 30 evenings as discs. */
    moon?: Readonly<{ reading: string; phases: string; strip: MoonStrip }> | null }>;
  onSunYear?: (on: boolean) => void;
  onSunYearCentre?: () => void;
  onSunYearPlace?: (lon: number, lat: number) => void;
  onDaylight?: (on: boolean) => void;
  onDaylightPlay?: (on: boolean) => void;
  /** Whether a polygon measurement is taking points, and the handler that starts or cancels one. */
  measuringArea?: boolean;
  onMeasureArea?: () => void;
  /**
   * The live radar loop, for looks that offer the radar tool: whether its
   * controls are on the map, and whether the map time allows a live loop.
   */
  radar?: Readonly<{ watching: boolean; available: boolean }>;
  onRadar?: (watch: boolean) => void;
  layerVisibility?: Readonly<Record<string, boolean>>;
  onLayer?: (id: CategoryMap["starters"][number], visible: boolean) => void;
  /**
   * The flowing-water effect and its reading, for looks that offer the flow
   * tool. `still` names why the rivers are not moving, if they are not.
   */
  flow?: Readonly<{ on: boolean; reading: string | null; still: string | null }>;
  /**
   * NWS river flood forecasts, for looks that offer the flood tool: the NOAA
   * NWPS gauges by flood category, a list most severe first, and the picked
   * gauge's stage hydrograph (observed, then the official forecast).
   */
  flood?: Readonly<{
    on: boolean;
    /** The network: loading, failed, or held outside the present map time. */
    state: "loading" | "failed" | "held" | "ready";
    summary: string | null;
    list: readonly Readonly<{ id: string; label: string }>[];
    picked: string | null;
    gauge: FloodGauge | null;
    plot: FloodHydrograph | null;
    reading: string | null;
    gaugeLoading: boolean;
    gaugeFailed: boolean;
    url: string | null;
  }>;
  /**
   * The FEMA disaster record since 1953, for looks that offer it: declarations
   * per year by hazard family, counties shaded by how many designated them,
   * and the picked county's declarations.
   */
  fema?: Readonly<{
    on: boolean;
    loading: boolean;
    failed: boolean;
    reading: string | null;
    families: typeof HAZARD_FAMILIES;
    years: readonly FemaYear[] | null;
    year: number | null;
    family: HazardFamilyId | null;
    emergencies: boolean;
    counties: Readonly<{ list: readonly Readonly<{ id: string; label: string }>[]; picked: string | null; reading: string | null;
      declarations: readonly Readonly<{ id: string; label: string }>[] }> | null;
  }>;
  /**
   * Rainfall, for looks that offer it, as the NWS renders it with the
   * service's own key: observed (the MRMS radar estimate of the past 1–72
   * hours) or forecast (the WPC forecast for the next 6 hours to 7 days).
   */
  rainfall?: Readonly<{
    on: boolean;
    held: boolean;
    kind: RainfallKind;
    hours: number;
    windows: readonly Readonly<{ hours: number; label: string; title: string }>[];
    reading: string;
    legend: readonly Readonly<{ label: string; image: string }>[] | null;
    legendFailed: boolean;
  }>;
  /** The SPC tornado record since 1950, for looks that offer it: tracks by rating, the years stacked by rating, and the strongest and deadliest. */
  tornadoes?: Readonly<{
    on: boolean;
    loading: boolean;
    failed: boolean;
    reading: string | null;
    series: readonly Readonly<{ name: string; color: string }>[];
    years: readonly TornadoYear[] | null;
    year: number | null;
    minRating: number;
    list: readonly Readonly<{ id: string; label: string }>[];
    picked: Readonly<{ id: string; detail: string }> | null;
  }>;
  onTornadoes?: (on: boolean) => void;
  onTornadoYear?: (year: number | null) => void;
  onTornadoRating?: (minRating: number) => void;
  onTornadoPick?: (id: string) => void;
  onTornadoClear?: () => void;
  /** Kansas Senate or House districts, for looks that offer them, in place of the U.S. House districts while shown. */
  legislature?: Readonly<{ chamber: "senate" | "house" | null; loading: boolean; failed: boolean; reading: string | null;
    list: readonly Readonly<{ id: string; label: string }>[]; picked: string | null }>;
  onLegislature?: (chamber: "senate" | "house" | null) => void;
  onLegislaturePick?: (id: string) => void;
  onLegislatureClear?: () => void;
  /** The USDA Cropland Data Layer, for looks that offer it: a year, and the crop at the point last clicked with CropScape's colour for it. */
  crops?: Readonly<{ on: boolean; year: number; years: readonly number[]; reading: string; swatch: string | null }>;
  /**
   * The crop history at the point last clicked: loading or failed, or the
   * year-by-year bars, the pattern read from them and its line.
   */
  degreeDays?: Readonly<{ state: "loading" | "failed" | "ready" | "none"; year: number; line: string | null; rain: string | null }> | null;
  surveySoil?: Readonly<{ state: "loading" | "failed" | "ready" | "none"; mapUnit: string | null; water: string | null; lines: readonly Readonly<{ name: string; detail: string }>[] }> | null;
  history?: Readonly<{ state: "loading" | "partial" | "failed" | "ready"; bars: readonly Readonly<{ year: number; family: CropFamily | null; state: "ready" | "none" | "failed"; label: string }>[];
    pattern: RotationPattern | null; reading: string | null }> | null;
  onCrops?: (on: boolean) => void;
  onCropsYear?: (year: number) => void;
  /** USGS NLCD 2021 land cover, for looks that offer it, with the class at the point last clicked. */
  flora?: Readonly<{ on: boolean; year: number; years: readonly number[]; opacity: number; failed: boolean; reading: string }>;
  onFlora?: (on: boolean) => void;
  onFloraYear?: (year: number) => void;
  onFloraOpacity?: (opacity: number) => void;
  onFloraRetry?: () => void;
  landCover?: Readonly<{ on: boolean; reading: string }>;
  onLandCover?: (on: boolean) => void;
  onRainfall?: (on: boolean) => void;
  onRainfallKind?: (kind: RainfallKind) => void;
  onRainfallHours?: (hours: number) => void;
  onFema?: (on: boolean) => void;
  onFemaYear?: (year: number | null) => void;
  onFemaFamily?: (family: HazardFamilyId | null) => void;
  onFemaEmergencies?: (on: boolean) => void;
  onFemaCounty?: (geoid: string) => void;
  onFemaCountyClear?: () => void;
  onFlood?: (on: boolean) => void;
  onFloodPick?: (lid: string) => void;
  onFloodClear?: () => void;
  onFlow?: (on: boolean) => void;
  /**
   * The county population prisms, for looks that offer the population tool:
   * whether they are drawn, how many counties fall in each Kansas density
   * group, the statewide density, all from the loaded 2020 county payload,
   * and the height scale.
   */
  population?: Readonly<{ on: boolean; groups: readonly (KansasDensityGroup & { count: number })[]; counties: number; statewide: number | null; metresPerPerson: number }>;
  onPopulation?: (on: boolean) => void;
  /**
   * Population change by county between the 2010 and 2020 Census counts: the
   * statewide line, every county as a bar from largest gain to largest loss in
   * its class colour, the same counties as a list, and the picked county.
   */
  populationChange?: Readonly<{ on: boolean; loading: boolean; failed: boolean; reading: string | null;
    bars: readonly Readonly<{ id: string; name: string; percent: number; color: string }>[] | null;
    list: readonly Readonly<{ id: string; label: string }>[]; picked: string | null; county: string | null }>;
  onPopulationChange?: (on: boolean) => void;
  onPopulationChangePick?: (geoid: string) => void;
  onPopulationChangeClear?: () => void;
  /**
   * The Kansas earthquake record since 1973, for looks that offer the quakes
   * tool: whether it is shown and read, the events per year, the one year
   * drawn (null for all), and the event a visitor selected on the map.
   */
  quakes?: Readonly<{
    on: boolean; loading: boolean; failed: boolean; counts: readonly (YearCount & { color: string })[] | null; total: number; startYear: number; endYear: number;
    minMagnitude: number; truncated: boolean; year: number | null; selected: EarthquakeRecordEvent | null; selectedUrl: string | null;
    /** The chosen year's events newest first, or the largest across all years, so an event can be picked without the map. */
    list?: readonly Readonly<{ id: string; label: string }>[];
    /** The record (or the chosen year) as a west–east depth section and a magnitude–frequency distribution. */
    plots?: Readonly<{ section: DepthSection; frequency: MagnitudeFrequency }> | null;
  }>;
  onQuakePick?: (id: string) => void;
  onQuakes?: (on: boolean) => void;
  onQuakeYear?: (year: number | null) => void;
  onQuakeClear?: () => void;
  /**
   * The SPC convective outlook, for looks that offer the outlook tool: the day
   * shown (null when off), the product shown (categorical, or the tornado, wind
   * or hail probabilities) and those the day offers, whether it is being read
   * or failed, and what it says for Kansas with its issue and valid times.
   */
  outlook?: Readonly<{ day: OutlookDay | null; product?: OutlookProduct; products?: readonly OutlookProduct[]; loading: boolean; failed: boolean; reading: string | null; url: string }>;
  onOutlook?: (day: OutlookDay | null) => void;
  onOutlookProduct?: (product: OutlookProduct) => void;
  /**
   * SPC's preliminary storm reports, for looks that offer the reports tool: the
   * convective day shown (null when off), whether it is being read or failed,
   * what it says for Kansas, and the report selected on the map with its
   * magnitude, time and place already worded.
   */
  reports?: Readonly<{ day: ReportDay | null; loading: boolean; failed: boolean; reading: string | null; url: string;
    /** Today's reports against the Day 1 outlook shown, when both are on the map. */
    verification?: string | null;
    selected: Readonly<{ report: StormReport; title: string; when: string | null }> | null;
    /** Kansas reports, newest first, so a report can be picked without the map. */
    kansas?: readonly Readonly<{ id: string; label: string }>[] }>;
  onReports?: (day: ReportDay | null) => void;
  onReportPick?: (id: string) => void;
  onReportClear?: () => void;
  /**
   * NASA SMAP L4 soil moisture, for looks that offer the soil tool: whether it
   * is drawn, at which depth, what the map shows now (the exact day drawn, or
   * why none is), and NASA's own colour scale.
   */
  soil?: Readonly<{ on: boolean; depth: "surface" | "root"; reading: string; legendUrl: string }>;
  onSoil?: (on: boolean) => void;
  onSoilDepth?: (depth: "surface" | "root") => void;
  /**
   * The U.S. Drought Monitor, for looks that offer the drought tool: the week
   * shown (its label, and the weeks before and after it, `next` null at the
   * newest), what it says for Kansas, the categories in the colours drawn,
   * and Kansas's weekly shares since 2000 when the USDM statistics answered.
   */
  drought?: Readonly<{
    on: boolean; loading: boolean; failed: boolean; reading: string | null; url: string;
    date: string | null; label: string | null; previous: string | null; next: string | null; newest: boolean;
    categories: readonly Readonly<{ id: string; name: string; color: string }>[];
    weeks: readonly DroughtChartWeek[] | null; seriesFailed: boolean;
    /** Whether Play is stepping through the weeks, and whether motion is allowed at all. */
    playing?: boolean; motionAllowed?: boolean;
    /** The change view: 0 for the categories, or the weeks the change is measured over, with what it says for Kansas. */
    /** start: the first week with a whole interval behind it, when the week shown comes before it. */
    change?: Readonly<{ weeks: 0 | 4 | 12; reading: string | null; start?: string | null; loading: boolean; failed: boolean }>;
    /** Kansas counties on the shown week, once the Census counties are in hand: how many each category reaches, the list most severe first, and the picked county's shares. */
    counties?: Readonly<{ summary: string; list: readonly Readonly<{ id: string; label: string }>[]; picked: string | null; reading: string | null }> | null;
  }>;
  onDroughtPlay?: (on: boolean) => void;
  onDroughtChange?: (weeks: 0 | 4 | 12) => void;
  onDroughtCounty?: (geoid: string) => void;
  onDroughtCountyClear?: () => void;
  onDrought?: (on: boolean) => void;
  /** A week to show ("YYYYMMDD"), or null for the newest. */
  onDroughtWeek?: (date: string | null) => void;
  /**
   * The High Plains aquifer view, for looks that offer the aquifer tool: which
   * KGS map is drawn (or none), and that map's classes in feet, in order.
   */
  aquifer?: Readonly<{ view: AquiferView | null; legend: readonly Readonly<{ label: string; color: string }>[] | null }>;
  onAquiferView?: (view: AquiferView) => void;
  /**
   * Measured depth to water at the KGS monitoring wells: whether picking is on,
   * the wells nearest the map centre, and the picked well's name, links, line
   * and hydrograph (null until read, or with too few measurements to plot).
   */
  wells?: Readonly<{ on: boolean; list: readonly Readonly<{ id: string; label: string }>[]; picked: string | null; name: string | null;
    loading: boolean; failed: boolean; reading: string | null; plot: WellPlot | null; usgsUrl: string | null; kgsUrl: string | null }>;
  onWells?: (on: boolean) => void;
  /**
   * Surface observations on the Storm desk: the station plots' state (held away
   * from the present map time), the statewide line, the stations as a list,
   * and the picked station decoded, with its raw METAR.
   */
  surface?: Readonly<{ on: boolean; state: "held" | "loading" | "failed" | "ready"; reading: string | null; list: readonly Readonly<{ id: string; label: string }>[];
    picked: string | null; detail: string | null; raw: string | null }>;
  onSurface?: (on: boolean) => void;
  onSurfacePick?: (station: string) => void;
  onSurfaceClear?: () => void;
  onWellPick?: (site: string) => void;
  onWellClear?: () => void;
  /**
   * Reviewed snapshots from the site database, for looks that offer them:
   * which source, whether shown, the release list and the one drawn, or the
   * plain reason none is.
   */
  reviewed?: Readonly<{
    source: string; on: boolean; loading: boolean; reason: string | null; effectiveDay?: string; historical?: boolean;
    count: number; index: number; publishedAt: string | null; capturedFor: string | null;
    features: number | null; freshness: string | null; playing: boolean; motionAllowed: boolean;
    /** The feature picked on the map, in its source's terms, with the release it belongs to and that release's signed download. */
    selected?: Readonly<{ title: string; lines: readonly string[]; link: Readonly<{ href: string; label: string }> | null; release: string; download: string }> | null;
    /** The shown release's most significant features, so one can be picked without the map. */
    list?: readonly Readonly<{ id: string; label: string }>[];
    /** The id of the picked feature, marked in the list. */
    pick?: string | null;
  }>;
  onReviewedDate?: (day: string) => void;
  onReviewedPick?: (id: string) => void;
  onReviewed?: (on: boolean) => void;
  onReviewedClear?: () => void;
  onReviewedIndex?: (index: number) => void;
  onReviewedPlay?: (on: boolean) => void;
  /**
   * The photo-real 3D view, for looks that offer it: whether it is on, the
   * landscapes it flies to, which one is framed, and the vertical scale in use.
   */
  photoreal?: Readonly<{ on: boolean; landscapes: readonly PhotorealLandscape[]; place: string | null; depth: number }>;
  /** A landscape id flies there in photo-real 3D; null returns to the look's own map. */
  onPhotoreal?: (landscape: string | null) => void;
  onReset: () => void;
  onLayers: () => void;
  /** Keys for the shown starter layers whose symbols encode a value (map-keys.ts). */
  keys?: readonly MapKey[];
  onClose: () => void;
}>) {
  const swatch = { "--m0": look.swatch[0], "--m1": look.swatch[1], "--m2": look.swatch[2] } as CSSProperties;
  return <section className="category-map-dock" aria-label={`${look.name} controls`} data-mode={mode} style={swatch}>
    <header>
      <span className="category-map-dock-swatch" aria-hidden="true" />
      <div><strong>{look.name}</strong><small>{mode === "terrain" ? "3D terrain" : mode === "globe" ? "Globe" : "2D map"} · display context</small></div>
      <button type="button" className="category-map-dock-close" aria-label={`Hide ${look.name} controls`} onClick={onClose}>×</button>
    </header>
    {look.topic === "government" && civic && <section className="category-map-dock-layer-set" aria-label="Kansas congressional districts">
      <strong>U.S. House · {civic.congress ? `Congress ${civic.congress}` : "history"}</strong>
      <small>{civic.day ? `${civic.day} · congressional term, not election date` : "Choose a Congress or a supported calendar date"}</small>
      {civic.options && onCivicCongress && <label>Congress<select aria-label="Choose Congress" value={civic.congress ?? ""} onChange={event => { const value = Number(event.target.value); if (civic.options?.some(option => option.value === value)) onCivicCongress(value); }}>
        <option value="" disabled>Choose a Congress</option>{civic.options.map(option => <option key={option.value} value={option.value}>{option.label}</option>)}
      </select></label>}
      {onCivicPresent && <button type="button" className="category-map-dock-tool" onClick={onCivicPresent}>Return to Present</button>}
      {onLayer && <button type="button" className="category-map-dock-tool" aria-pressed={civic.visible} onClick={() => onLayer("census-congress-119", !civic.visible)}>Show district areas</button>}
      <p className="category-map-dock-reading" role="status">{!civic.visible ? "District layer hidden." : civic.state === "held" ? "No checked plan for this map date. Choose a Congress; year-only frames use January 1." : civic.state === "ready" ? `${civic.items.length} source constituencies loaded. Choose one to inspect its source record; shapes do not count seats.` : civic.state === "error" ? "District source unavailable. Open Layers for this map to retry." : "Loading the selected congressional plan…"}</p>
      {civic.visible && civic.state === "error" && onCivicRetry && <button type="button" className="category-map-dock-tool" onClick={onCivicRetry}>Retry selected plan</button>}
      {civic.visible && civic.state === "ready" && onCivicPick && <ul className="category-map-dock-picklist" aria-label="Inspect a Kansas U.S. House district">
        {civic.items.map(item => <li key={item.id}><button type="button" onClick={event => onCivicPick(item.id, event.currentTarget)}>{item.label}</button></li>)}
      </ul>}
      <small>Colors identify district numbers, not parties. At-large constituencies can overlap numbered districts and elect multiple members. Boundaries do not determine your ballot.</small>
      {civic.visible && civic.state === "ready" && civic.day && <a href={`/api/live-context?feed=census-congress-119&day=${encodeURIComponent(civic.day)}`} download>Download selected plan (GeoJSON)</a>}
      <small>Coverage: statehood, January 29, 1861, through the 119th Congress. Earlier territorial delegate geometry is unverified. Historical plans are scholarly reconstructions; Present uses Census geography.</small>
      <a href="https://www.archives.gov/legislative/features/kansas" target="_blank" rel="noreferrer">Kansas statehood record ↗</a>
      <a href="https://cdmaps.polisci.ucla.edu/" target="_blank" rel="noreferrer">Historical boundary sources ↗</a>
      <a href="/civic-history-license.txt" target="_blank" rel="noreferrer">Historical data license ↗</a>
      <a href="https://www.sos.ks.gov/elections/district-maps.html" target="_blank" rel="noreferrer">Official Kansas district maps ↗</a>
      {onLayer && layerVisibility && <button type="button" className="category-map-dock-tool" aria-pressed={Boolean(layerVisibility["census-counties"])} onClick={() => onLayer("census-counties", !layerVisibility["census-counties"])}>Compare Census counties</button>}
    </section>}
    {look.contextLayers && onLayer && layerVisibility && <div className="category-map-dock-layer-set">
      {look.starters.length > 0 && <>
      <strong>Starting layers</strong>
      {look.starters.map(id => <button key={id} type="button" className="category-map-dock-tool" aria-pressed={Boolean(layerVisibility[id])}
        onClick={() => onLayer(id, !layerVisibility[id])}>{id === "nws-radar" ? "Latest NOAA radar" : "Active NWS alerts"}</button>)}
      <small>Latest scan first · playback on demand. Each source keeps its own clock.</small>
      </>}
      <details className="category-map-dock-context"><summary>Add related context</summary>
        <p>Off at start. Add only what helps this view.</p>
        {look.contextLayers.map(layer => <div key={layer.id}>
          <button type="button" className="category-map-dock-tool" aria-pressed={Boolean(layerVisibility[layer.id])}
            onClick={() => onLayer(layer.id, !layerVisibility[layer.id])}>{layer.title}</button>
          <small>{layer.note}</small>
        </div>)}
      </details>
    </div>}
    <div className="category-map-dock-modes" role="group" aria-label="View">
      {MODES.map(([value, label, title]) => <button key={value} type="button" aria-pressed={mode === value} title={title}
        disabled={value === "terrain" && !terrainAvailable} onClick={() => onMode(value)}>{label}</button>)}
    </div>
    {mode === "terrain" && <label className="category-map-dock-range"><span>Relief</span>
      <input type="range" min={0.5} max={3} step={0.1} value={depth} aria-valuetext={`${depth.toFixed(1)} times vertical exaggeration`} onChange={event => onDepth(Number(event.target.value))} />
      <output>{depth.toFixed(1)}×</output></label>}
    {mode !== "globe" && sunAvailable && (sun
      ? <>
        <p className="category-map-dock-sun-reading" aria-live="polite"><span>{sun.live ? "Real sun" : "Sun at"}</span><output>{sunReading(sun.light, sun.at)}</output></p>
        <div className="category-map-dock-range category-map-dock-sun-time"><span id="category-map-dock-sun-time">Time</span>
          <input type="range" min={0} max={SUN_TIME_STEPS - 1} step={1} value={Math.min(SUN_TIME_STEPS - 1, Math.round(sun.dayFraction * SUN_TIME_STEPS))} aria-labelledby="category-map-dock-sun-time"
            aria-valuetext={sunReading(sun.light, sun.at)} onChange={event => onSunTime(Number(event.target.value) / SUN_TIME_STEPS)} />
          <button type="button" disabled={sun.live} onClick={() => onSunTime(null)} title="Follow the clock again">Now</button></div>
      </>
      : <label className="category-map-dock-range"><span>Sun from</span>
        <input type="range" min={0} max={355} step={5} value={Math.round(azimuth) % 360} aria-valuetext={`Light from ${azimuthLabel(azimuth)}, ${Math.round(azimuth)} degrees`} onChange={event => onAzimuth(Number(event.target.value))} />
        <output>{azimuthLabel(azimuth)}</output></label>)}
    {mode !== "globe" && sunAvailable && (sun
      ? <div className="category-map-dock-sun-actions">
        <button type="button" className="category-map-dock-sun" aria-pressed={sunPlaying && motionAllowed} disabled={!motionAllowed} onClick={() => onSunPlay(!sunPlaying)}
          title={motionAllowed ? "Sweep the sun through the rest of today in quarter-hour steps" : "Reduced motion is on; move Time by hand"}>{sunPlaying && motionAllowed ? "Pause" : "Play the day"}</button>
        <button type="button" className="category-map-dock-sun" aria-pressed={true} onClick={() => onRealSun(false)} title="Set the light direction by hand">Set light by hand</button>
      </div>
      : <button type="button" className="category-map-dock-sun" aria-pressed={false} onClick={() => onRealSun(true)} title="Light the map from where the sun is now over the map center">Use the real sun now</button>)}
    {look.tools?.includes("flow") && flow && onFlow && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={flow.on} onClick={() => onFlow(!flow.on)}
        title="Rivers flow downstream where USGS 3DHP maps a direction; a USGS gauge reading lights its own reach">{flow.on ? "Hide river flow" : "Show river flow"}</button>
      {flow.on && <p className="category-map-dock-reading" aria-live="polite">{flow.reading ?? "Starting river flow…"}{flow.still ? ` · drawn still: ${flow.still}` : ""}</p>}
    </>}
    {look.tools?.includes("sunyear") && sunYear && onSunYear && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={sunYear.on} onClick={() => onSunYear(!sunYear.on)}
        title="Sunrise, sunset and twilight for every day of the year at a Kansas place, with the Moon's phases, rising and setting, all calculated">{sunYear.on ? "Hide daylight through the year" : "Daylight through the year"}</button>
      {sunYear.on && <div className="category-map-dock-quakes">
        <p className="category-map-dock-reading" aria-live="polite">{`At ${sunYear.place ?? "–"} · ${sunYear.outside ? "the chart is for places in Kansas: choose coordinates or click inside the state" : "click the map in Kansas for another place"}`}</p>
        {sunYear.coordinates && onSunYearPlace && <form className="category-map-dock-sun-location" key={`${sunYear.coordinates.lon},${sunYear.coordinates.lat}`} onSubmit={event => {
          event.preventDefault();
          const fields = event.currentTarget.elements;
          onSunYearPlace((fields.namedItem("longitude") as HTMLInputElement).valueAsNumber, (fields.namedItem("latitude") as HTMLInputElement).valueAsNumber);
        }}>
          <label>Latitude<input name="latitude" type="number" min={-90} max={90} step="any" required defaultValue={sunYear.coordinates.lat} /></label>
          <label>Longitude<input name="longitude" type="number" min={-180} max={180} step="any" required defaultValue={sunYear.coordinates.lon} /></label>
          <button type="submit">Chart location</button>
          <small>Decimal degrees; Kansas longitudes are negative. Or click the map.</small>
        </form>}
        {sunYear.chart && <SunYearChart chart={sunYear.chart} place={sunYear.place ?? ""} />}
        {sunYear.reading && <p className="category-map-dock-reading">{sunYear.reading}</p>}
        {sunYear.note && <p className="category-map-dock-reading">{sunYear.note}</p>}
        {sunYear.moon && <>
          <p className="category-map-dock-reading">{sunYear.moon.reading}</p>
          <MoonPhaseStrip strip={sunYear.moon.strip} />
          <p className="category-map-dock-reading">{sunYear.moon.phases}</p>
        </>}
        {!sunYear.atCentre && onSunYearCentre && <div><button type="button" onClick={onSunYearCentre}>Back to the centre of Kansas</button></div>}
      </div>}
    </>}
    {look.tools?.includes("daylight") && daylight && onDaylight && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={daylight.on} onClick={() => onDaylight(!daylight.on)}
        title="Shade the night side of the Earth and its civil, nautical and astronomical twilight, calculated from the Sun's position">{daylight.on ? "Hide day and night" : "Show day and night"}</button>
      {daylight.on && <>
        <p className="category-map-dock-reading" aria-live={daylight.playing ? "off" : "polite"}>{daylight.time}<br />{daylight.reading}</p>
        {onDaylightPlay && <button type="button" className="category-map-dock-sun" aria-pressed={daylight.playing && motionAllowed} disabled={!motionAllowed} onClick={() => onDaylightPlay(!daylight.playing)}
          title={motionAllowed ? "Run the calculated day through 24 hours in a 60-second loop" : "Reduced motion is on; set the time in the Daylight & twilight layer"}>{daylight.playing && motionAllowed ? "Pause day and night" : "Play day and night"}</button>}
      </>}
    </>}
    {look.tools?.includes("radar") && radar && onRadar && <button type="button" className="category-map-dock-tool" aria-pressed={radar.watching} disabled={!radar.watching && !radar.available} onClick={() => onRadar(!radar.watching)}
      title={radar.watching ? "Close the radar loop controls" : radar.available ? "Play the latest NOAA radar scans on the map at their observation times" : "The live loop plays at the present map time; return to Present in Time"}>{radar.watching ? "Close radar loop" : "Watch the radar loop"}</button>}
    {look.tools?.includes("outlook") && outlook && onOutlook && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={outlook.day !== null} onClick={() => onOutlook(outlook.day === null ? 1 : null)}
        title="NOAA Storm Prediction Center convective outlooks: the categorical severe risk, and tornado, wind and hail probabilities, drawn as outlines">{outlook.day === null ? "Show the SPC severe outlook" : "Hide the SPC outlook"}</button>
      {outlook.day !== null && <>
        <div className="category-map-dock-modes" role="group" aria-label="Outlook day">
          {([1, 2, 3] as const).map(day => <button key={day} type="button" aria-pressed={outlook.day === day} onClick={() => onOutlook(day)}>Day {day}</button>)}
        </div>
        {onOutlookProduct && outlook.products && <div className="category-map-dock-modes category-map-dock-products" role="group" aria-label="Outlook product">
          {OUTLOOK_PRODUCT_CHOICES.map(([product, label, title]) => {
            const offered = outlook.products!.includes(product);
            return <button key={product} type="button" aria-pressed={outlook.product === product} disabled={!offered} onClick={() => onOutlookProduct(product)}
              title={offered ? title : "SPC issues tornado, wind and hail probabilities for days 1 and 2"}>{label}</button>;
          })}
        </div>}
        <p className="category-map-dock-reading" aria-live="polite">{outlook.loading ? "Reading the SPC outlook…"
          : outlook.failed ? "The SPC outlook did not answer. Try again, or another day."
          : outlook.reading}</p>
        <p className="category-map-dock-reading"><a href={outlook.url} target="_blank" rel="noreferrer">SPC outlook page ↗</a> · forecast risk, not a warning</p>
      </>}
    </>}
    {look.tools?.includes("reports") && reports && onReports && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={reports.day !== null} onClick={() => onReports(reports.day === null ? "today" : null)}
        title="Preliminary tornado, wind and hail reports collected by the NOAA Storm Prediction Center for the convective day">{reports.day === null ? "Show SPC storm reports" : "Hide storm reports"}</button>
      {reports.day !== null && <>
        <div className="category-map-dock-modes category-map-dock-depth" role="group" aria-label="Report day">
          {([["today", "Today"], ["yesterday", "Yesterday"]] as const).map(([day, label]) => <button key={day} type="button" aria-pressed={reports.day === day} onClick={() => onReports(day)}>{label}</button>)}
        </div>
        <p className="category-map-dock-reading" aria-live="polite">{reports.loading ? "Reading the SPC storm reports…"
          : reports.failed ? "The SPC storm reports did not answer. Try again, or the other day."
          : reports.reading}</p>
        {reports.verification && !reports.loading && !reports.failed && <p className="category-map-dock-reading category-map-dock-verification" aria-live="polite"
          title="Reports made since the outlook's valid start, placed against its areas, as SPC verifies its outlooks; preliminary reports">{reports.verification}</p>}
        {onReportPick && reports.kansas && reports.kansas.length > 0 && <PickList summary={`Kansas reports (${reports.kansas.length})`} label="Kansas storm reports, newest first"
          items={reports.kansas} selected={reports.selected?.report.id ?? null} onPick={onReportPick} />}
        {reports.selected && <div className="category-map-dock-quake-event" aria-live="polite">
          <p><b>{reports.selected.title}</b>{reports.selected.when ? ` · ${reports.selected.when}` : ""}<br />
            {[reports.selected.report.location, reports.selected.report.county && `${reports.selected.report.county} Co.`, reports.selected.report.state].filter(Boolean).join(", ")}
            {reports.selected.report.comments && <><br />{reports.selected.report.comments}</>}</p>
          <div><button type="button" onClick={onReportClear} aria-label="Clear the selected storm report">Clear</button></div>
        </div>}
        <p className="category-map-dock-reading"><a href={reports.url} target="_blank" rel="noreferrer">SPC storm reports ↗</a> · preliminary, unverified</p>
      </>}
    </>}
    {look.tools?.includes("population") && population && onPopulation && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={population.on} onClick={() => onPopulation(!population.on)}
        title="Raise each county by its 2020 Census people per square mile of land">{population.on ? "Flatten the counties" : "Show population in 3D"}</button>
      {population.on && <div className="category-map-dock-legend" aria-label="Kansas density groups, people per square mile of land">
        <ul>{population.groups.map(group => <li key={group.id}><span className="category-map-dock-chip" style={{ background: group.color }} aria-hidden="true" />
          <span>{group.label}<small>{group.range}</small></span><b>{population.counties ? `${group.count} ${group.count === 1 ? "county" : "counties"}` : "…"}</b></li>)}</ul>
        <p className="category-map-dock-reading">Height: {population.metresPerPerson} m per person per sq mi of land{population.statewide !== null ? ` · Kansas overall ${population.statewide.toFixed(1)}` : ""} · 2020 Census</p>
      </div>}
      {populationChange && onPopulationChange && <>
        <button type="button" className="category-map-dock-tool" aria-pressed={populationChange.on} onClick={() => onPopulationChange(!populationChange.on)}
          title="Shade each county by its change in people between the 2010 and 2020 Census counts">{populationChange.on ? "Hide the 2010–2020 change" : "Show change since 2010"}</button>
        {populationChange.on && <div className="category-map-dock-quakes">
          <p className="category-map-dock-reading" aria-live="polite">{populationChange.loading ? "Reading the 2010 and 2020 Census counts…"
            : populationChange.failed ? "The Census Bureau did not answer for both years; no change is shown. Try again." : populationChange.reading}</p>
          {populationChange.bars && <PopulationChangeChart bars={populationChange.bars} picked={populationChange.picked} onPick={onPopulationChangePick} />}
          {onPopulationChangePick && populationChange.list.length > 0 && <PickList summary={`Counties, largest gain first (${populationChange.list.length})`}
            label="Kansas counties by percent change in people, 2010–2020, largest gain first" items={populationChange.list} selected={populationChange.picked} onPick={onPopulationChangePick} />}
          {populationChange.county && <div className="category-map-dock-quake-event" aria-live="polite">
            <p>{populationChange.county}</p>
            <div><button type="button" onClick={onPopulationChangeClear} aria-label="Clear the selected county">Clear</button></div>
          </div>}
        </div>}
      </>}
    </>}
    {look.tools?.includes("surface") && surface && onSurface && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={surface.on} onClick={() => onSurface(!surface.on)}
        title="Kansas airport observations as station plots: sky cover, wind barb, temperature and dew point">{surface.on ? "Hide surface observations" : "Show surface observations"}</button>
      {surface.on && <div className="category-map-dock-quakes">
        <p className="category-map-dock-reading" aria-live="polite">{surface.state === "held" ? "Observations are current only: return the map to the present to plot them."
          : surface.state === "loading" ? "Reading the latest METARs…" : surface.state === "failed" ? "The Aviation Weather Center did not answer; no conditions are inferred. Try again shortly." : surface.reading}</p>
        {surface.state === "ready" && onSurfacePick && surface.list.length > 0 && <PickList summary={`Stations (${surface.list.length})`} label="Kansas-area weather stations, by identifier"
          items={surface.list} selected={surface.picked} onPick={onSurfacePick} />}
        {surface.state === "ready" && surface.detail && <div className="category-map-dock-quake-event" aria-live="polite">
          <p>{surface.detail}</p>
          {surface.raw && <p><code>{surface.raw}</code></p>}
          <div><button type="button" onClick={onSurfaceClear} aria-label="Clear the selected station">Clear</button></div>
        </div>}
      </div>}
    </>}
    {look.tools?.includes("tornadoes") && tornadoes && onTornadoes && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={tornadoes.on} onClick={() => onTornadoes(!tornadoes.on)}
        title="Every Kansas tornado in the SPC severe weather database since 1950, as tracks coloured by F/EF rating">{tornadoes.on ? "Hide the tornado record" : "Tornado record since 1950"}</button>
      {tornadoes.on && <div className="category-map-dock-quakes">
        <p className="category-map-dock-reading" aria-live="polite">{tornadoes.loading ? "Reading the SPC tornado database…"
          : tornadoes.failed ? "The SPC tornado database did not answer. Try the record again." : tornadoes.reading}</p>
        {tornadoes.years && <TornadoHistory years={tornadoes.years} year={tornadoes.year} series={tornadoes.series} onYear={onTornadoYear} />}
        {tornadoes.years && <div className="category-map-dock-fema-filters">
          <label className="category-map-dock-range"><span>Year</span>
            <select value={tornadoes.year ?? ""} onChange={event => onTornadoYear?.(event.target.value ? Number(event.target.value) : null)}>
              <option value="">All years</option>
              {tornadoes.years.filter(entry => entry.total > 0 || entry.year === tornadoes.year).map(entry => <option key={entry.year} value={entry.year}>{entry.year} · {entry.total}</option>)}
            </select></label>
          <label className="category-map-dock-range"><span>Rating</span>
            <select value={tornadoes.minRating} onChange={event => onTornadoRating?.(Number(event.target.value))}>
              <option value={0}>All tornadoes</option>
              {[1, 2, 3, 4, 5].map(r => <option key={r} value={r}>F/EF{r} or stronger</option>)}
            </select></label>
        </div>}
        {onTornadoPick && tornadoes.list.length > 0 && <PickList summary={`Strongest and deadliest (${tornadoes.list.length})`} label="Kansas tornadoes, strongest first, then deadliest"
          items={tornadoes.list} selected={tornadoes.picked?.id ?? null} onPick={onTornadoPick} />}
        {tornadoes.picked && <div className="category-map-dock-quake-event" aria-live="polite">
          <p>{tornadoes.picked.detail}</p>
          <div><button type="button" onClick={onTornadoClear} aria-label="Clear the selected tornado">Clear</button></div>
        </div>}
      </div>}
    </>}
    {look.tools?.includes("legislature") && legislature && onLegislature && <>
      <div className="category-map-dock-modes" role="group" aria-label="District plan">
        {([[null, "U.S. House", "Kansas's U.S. House districts, Congress by Congress"], ["senate", "Kansas Senate", "The 40 Kansas Senate districts, 2024 plan"], ["house", "Kansas House", "The 125 Kansas House districts, 2024 plan"]] as const).map(([chamber, label, title]) =>
          <button key={label} type="button" aria-pressed={legislature.chamber === chamber} title={title} onClick={() => onLegislature(chamber)}>{label}</button>)}
      </div>
      {legislature.chamber && <div className="category-map-dock-quakes">
        <p className="category-map-dock-reading" aria-live="polite">{legislature.loading ? "Reading the Census legislative districts…"
          : legislature.failed ? "The Census legislative districts did not answer; nothing is drawn from part of a plan." : legislature.reading}</p>
        {onLegislaturePick && legislature.list.length > 0 && <PickList summary={`Districts (${legislature.list.length})`} label={`${legislature.chamber === "senate" ? "Kansas Senate" : "Kansas House"} districts`}
          items={legislature.list} selected={legislature.picked} onPick={onLegislaturePick} />}
        {legislature.picked && <div><button type="button" onClick={onLegislatureClear} aria-label="Clear the selected district">Clear</button></div>}
      </div>}
    </>}
    {look.tools?.includes("crops") && crops && onCrops && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={crops.on} onClick={() => onCrops(!crops.on)}
        title="USDA NASS Cropland Data Layer: what was planted in each 30 m cell, year by year since 2008">{crops.on ? "Hide crops" : "Show crops (USDA CDL)"}</button>
      {crops.on && <div className="category-map-dock-quakes">
        <label className="category-map-dock-range category-map-dock-quake-year"><span>Year</span>
          <select value={crops.year} onChange={event => onCropsYear?.(Number(event.target.value))}>
            {crops.years.map(year => <option key={year} value={year}>{year}</option>)}
          </select></label>
        <p className="category-map-dock-reading" aria-live="polite">{crops.swatch && <i className="category-map-dock-crop-swatch" style={{ background: crops.swatch }} aria-hidden="true" />}{crops.reading}</p>
        {history && <div className="category-map-dock-crop-history" aria-live="polite">
          {history.state === "loading" && <p className="category-map-dock-reading">Reading every CDL year at this point…</p>}
          {history.state === "failed" && <p className="category-map-dock-reading">CropScape did not answer for this point. No pattern is read; click the point again to retry.</p>}
          {(history.state === "ready" || history.state === "partial") && history.bars.length > 0 && <>
            <CropHistoryTimeline bars={history.bars} />
            {history.state === "partial" && <p className="category-map-dock-reading">CropScape did not answer for {history.bars.filter(b => b.state === "failed").length} year{history.bars.filter(b => b.state === "failed").length === 1 ? "" : "s"} (dashed). No pattern is read from a partial history; click the point again to retry.</p>}
            {history.reading && <p className="category-map-dock-reading">{history.reading}</p>}
          </>}
        </div>}
        {surveySoil && <div className="category-map-dock-crop-history" aria-live="polite">
          <p className="category-map-dock-reading">Soil survey at this point (SSURGO){surveySoil.mapUnit ? ` · ${surveySoil.mapUnit}` : ""}</p>
          {surveySoil.state === "loading" && <p className="category-map-dock-reading">Reading the soil-map unit…</p>}
          {surveySoil.state === "failed" && <p className="category-map-dock-reading">USDA Soil Data Access did not answer for this point. No soil is inferred; click the point again to retry.</p>}
          {surveySoil.state === "none" && <p className="category-map-dock-reading">No SSURGO soil-map unit covers this point.</p>}
          {surveySoil.state === "ready" && <>
            {surveySoil.water && <p className="category-map-dock-reading">Map-unit average: {surveySoil.water}</p>}
            <ul className="category-map-dock-reading">{surveySoil.lines.map((line, index) => <li key={`${index}-${line.name}`}><strong>{line.name}</strong>: {line.detail}</li>)}</ul>
            <p className="category-map-dock-reading">Components are alternatives within the mapped area, each with its share of it. They are not the soil at the point.</p>
          </>}
        </div>}
        {degreeDays && <div className="category-map-dock-crop-history" aria-live="polite">
          <p className="category-map-dock-reading">Growing degree days, {degreeDays.year} (click the point again for another year)</p>
          {degreeDays.state === "loading" && <p className="category-map-dock-reading">Reading the season at the nearest Kansas station…</p>}
          {degreeDays.state === "failed" && <p className="category-map-dock-reading">The Iowa Environmental Mesonet did not answer for this point. No growing degree days are inferred; click the point again to retry.</p>}
          {degreeDays.state === "none" && <p className="category-map-dock-reading">No Kansas airport station is within 150 km of this point, or it has no readings for the season.</p>}
          {degreeDays.state === "ready" && degreeDays.line && <p className="category-map-dock-reading">{degreeDays.line}</p>}
          {degreeDays.state === "ready" && degreeDays.rain && <p className="category-map-dock-reading">{degreeDays.rain}</p>}
          {degreeDays.state === "ready" && <p className="category-map-dock-reading">A station reading, not the field. Degree days vary across a county, and an airport station records its own weather.</p>}
        </div>}
      </div>}
    </>}
    {look.tools?.includes("plants") && flora && onFlora && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={flora.on} onClick={() => onFlora(!flora.on)}>{flora.on ? "Hide plant records" : "Show plant records (GBIF)"}</button>
      {flora.on && <div className="category-map-dock-quakes">
        <label className="category-map-dock-flora-control">Plant record year
          <select value={flora.year} onChange={event => onFloraYear?.(Number(event.target.value))}>
            {flora.years.map(year => <option key={year} value={year}>{year}</option>)}
          </select>
        </label>
        <label className="category-map-dock-flora-control">Plant layer opacity · {Math.round(flora.opacity * 100)}%
          <input type="range" min="0.1" max="1" step="0.05" value={flora.opacity} onChange={event => onFloraOpacity?.(Number(event.target.value))} />
        </label>
        <p className="category-map-dock-reading" aria-live="polite">{flora.reading}</p>
        {flora.failed && <button type="button" className="category-map-dock-tool" onClick={onFloraRetry}>Retry plant records</button>}
        <p className="category-map-dock-reading">Annual records, including specimens, in coarse hexagons. This year is independent of the map calendar; NLCD stays at 2021. Shading is not plant abundance or a species inventory.</p>
      </div>}
      <details className="category-map-dock-context"><summary>Flora data &amp; limits</summary>
        <p>NLCD 2021 classifies 30 m land-cover cells. GBIF summarizes Plantae records by event year, 1995–2025; this is the selector range, not a guarantee of coverage. Crop classes use their own USDA year. Border hexagons can include records from neighboring states.</p>
        <p>Exact plant locations are not requested. These are external context layers; reviewed Flora evidence, species checklists and conservation status are not connected. Empty records do not prove absence.</p>
        <p><a href="https://www.usgs.gov/centers/eros/science/national-land-cover-database" target="_blank" rel="noreferrer">USGS land cover</a> · <a href="/observatory/sources#ecology">GBIF source notes</a> · <a href="https://www.gbif.org/terms/data-user" target="_blank" rel="noreferrer">GBIF data terms</a></p>
      </details>
    </>}
    {look.tools?.includes("landcover") && landCover && onLandCover && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={landCover.on} onClick={() => onLandCover(!landCover.on)}
        title="USGS National Land Cover Database 2021: land cover classified from Landsat at 30 m, in NLCD's own colours">{landCover.on ? "Hide land cover" : "Show land cover (NLCD 2021)"}</button>
      {landCover.on && <p className="category-map-dock-reading" aria-live="polite">{landCover.reading}</p>}
    </>}
    {look.tools?.includes("rainfall") && rainfall && onRainfall && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={rainfall.on} onClick={() => onRainfall(!rainfall.on)}
        title="Observed rain (the NWS MRMS radar estimate of the past 1 to 72 hours) and forecast rain (the NWS WPC forecast for the next 6 hours to 7 days)">{rainfall.on ? "Hide rainfall" : "Show rainfall"}</button>
      {rainfall.on && <div className="category-map-dock-quakes">
        {rainfall.held ? <p className="category-map-dock-reading" aria-live="polite">Rainfall shows only at the present map time.</p> : <>
          {onRainfallKind && <div className="category-map-dock-modes category-map-dock-rain-kinds" role="group" aria-label="Rainfall observed or forecast">
            {([["observed", "Observed (MRMS)", "The NWS MRMS radar estimate of the rain that fell"], ["forecast", "Forecast (WPC)", "The NWS Weather Prediction Center forecast of the rain to come"]] as const).map(([kind, label, title]) =>
              <button key={kind} type="button" aria-pressed={rainfall.kind === kind} title={title} onClick={() => onRainfallKind(kind)}>{label}</button>)}
          </div>}
          <div className="category-map-dock-modes category-map-dock-rain-windows" role="group" aria-label="Rainfall window" style={{ gridTemplateColumns: `repeat(${rainfall.windows.length},minmax(0,1fr))` }}>
            {rainfall.windows.map(window => <button key={window.hours} type="button" aria-pressed={rainfall.hours === window.hours} title={window.title}
              onClick={() => onRainfallHours?.(window.hours)}>{window.label}</button>)}
          </div>
          <p className="category-map-dock-reading" aria-live="polite">{rainfall.reading}</p>
          {rainfall.legend ? <ul className="category-map-dock-rain-key" aria-label={rainfall.kind === "forecast" ? "Forecast precipitation, inches" : `Rain in the past ${rainfall.hours} hours, inches`}>
            {rainfall.legend.map(item => <li key={item.label}><i style={{ backgroundImage: `url("${item.image}")` }} aria-hidden="true" />{item.label}</li>)}
          </ul> : <p className="category-map-dock-scale-note">{rainfall.legendFailed ? "The NWS legend did not answer; the colours on the map are the NWS's own." : "Reading the NWS legend…"}</p>}
        </>}
      </div>}
    </>}
    {look.tools?.includes("fema") && fema && onFema && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={fema.on} onClick={() => onFema(!fema.on)}
        title="Every FEMA disaster declaration for Kansas since 1953: counties shaded by how many designated them, and the record year by year">{fema.on ? "Back to current hazards" : "FEMA disaster record since 1953"}</button>
      {fema.on && <div className="category-map-dock-quakes">
        <p className="category-map-dock-reading" aria-live="polite">{fema.loading ? "Reading the OpenFEMA declarations…"
          : fema.failed ? "OpenFEMA did not answer. Try the record again, or go back to current hazards." : fema.reading}</p>
        {fema.years && <FemaHistory years={fema.years} year={fema.year} families={fema.families} onYear={onFemaYear} />}
        {fema.years && <div className="category-map-dock-fema-filters">
          <label className="category-map-dock-range"><span>Year</span>
            <select value={fema.year ?? ""} onChange={event => onFemaYear?.(event.target.value ? Number(event.target.value) : null)}>
              <option value="">All years</option>
              {fema.years.filter(entry => entry.total > 0 || entry.year === fema.year).map(entry => <option key={entry.year} value={entry.year}>{entry.year} · {entry.total}</option>)}
            </select></label>
          <label className="category-map-dock-range"><span>Hazard</span>
            <select value={fema.family ?? ""} onChange={event => onFemaFamily?.(event.target.value ? event.target.value as HazardFamilyId : null)}>
              <option value="">All hazards</option>
              {fema.families.map(family => <option key={family.id} value={family.id}>{family.name}</option>)}
            </select></label>
          <label className="category-map-dock-check"><input type="checkbox" checked={fema.emergencies} onChange={event => onFemaEmergencies?.(event.target.checked)} />
            <span>Include emergency and fire-management declarations</span></label>
        </div>}
        {onFemaCounty && fema.counties && <PickList summary={`Counties, most declarations first (${fema.counties.list.length})`} label="Kansas counties by FEMA declarations, most first"
          items={fema.counties.list} selected={fema.counties.picked} onPick={onFemaCounty} />}
        {fema.counties?.picked && <div className="category-map-dock-quake-event" aria-live="polite">
          <p>{fema.counties.reading}</p>
          {fema.counties.declarations.length > 0 && <ul className="category-map-dock-fema-list" aria-label="Declarations designating this county, newest first">
            {fema.counties.declarations.map(item => <li key={item.id}><a href={`https://www.fema.gov/disaster/${item.id}`} target="_blank" rel="noreferrer">{item.label}</a></li>)}
          </ul>}
          <div><button type="button" onClick={onFemaCountyClear} aria-label="Clear the selected county">Clear</button></div>
        </div>}
      </div>}
    </>}
    {look.tools?.includes("flood") && flood && onFlood && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={flood.on} onClick={() => onFlood(!flood.on)}
        title="NOAA NWPS river gauges coloured by NWS flood category, each with its stage hydrograph and the official NWS forecast">{flood.on ? "Hide flood forecasts" : "Show flood forecasts"}</button>
      {flood.on && <div className="category-map-dock-quakes">
        <p className="category-map-dock-reading" aria-live="polite">{flood.state === "loading" ? "Reading the NWS river gauges…"
          : flood.state === "failed" ? "The NWS gauge network did not answer; no flood state is inferred. Try again from Layers."
          : flood.state === "held" ? "NWS gauges show only at the present map time." : flood.summary}</p>
        {onFloodPick && flood.list.length > 0 && <PickList summary={`Gauges, most severe first (${flood.list.length})`} label="Kansas NWS river gauges, most severe flood category first"
          items={flood.list} selected={flood.picked} onPick={onFloodPick} />}
        {flood.picked && <div className="category-map-dock-quake-event" aria-live="polite">
          {flood.gauge ? <>
            <p><b>{flood.gauge.name}</b> · {flood.gauge.lid}{flood.gauge.usgsId ? ` · USGS ${flood.gauge.usgsId}` : ""}</p>
            {flood.plot && <FloodHydrographChart gauge={flood.gauge} plot={flood.plot} reading={flood.reading} />}
            <p>{flood.reading}</p>
          </> : <p>{flood.gaugeFailed ? "The NWS did not answer for this gauge; its category on the map stands." : flood.gaugeLoading ? "Reading the NWS hydrograph…" : null}</p>}
          <div>{flood.url && <a href={flood.url} target="_blank" rel="noreferrer">NWS gauge page ↗</a>}
            <button type="button" onClick={onFloodClear} aria-label="Clear the selected gauge">Clear</button></div>
        </div>}
      </div>}
    </>}
    {look.tools?.includes("quakes") && quakes && onQuakes && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={quakes.on} onClick={() => onQuakes(!quakes.on)}
        title={`Every USGS-catalogued Kansas earthquake of magnitude ${quakes.minMagnitude} or more since ${quakes.startYear}, coloured by year`}>{quakes.on ? "Back to the past 30 days" : `Earthquake record since ${quakes.startYear}`}</button>
      {quakes.on && <div className="category-map-dock-quakes">
        {quakes.counts && <QuakeHistogram counts={quakes.counts} year={quakes.year} onYear={onQuakeYear} />}
        {quakes.counts && <label className="category-map-dock-range category-map-dock-quake-year"><span>Year</span>
          <select value={quakes.year ?? ""} onChange={event => onQuakeYear?.(event.target.value ? Number(event.target.value) : null)}>
            <option value="">All years</option>
            {quakes.counts.filter(entry => entry.count > 0).map(entry => <option key={entry.year} value={entry.year}>{entry.year} · {entry.count}</option>)}
          </select></label>}
        <p className="category-map-dock-reading" aria-live="polite">{quakeReading(quakes)}</p>
        {quakes.plots && quakes.plots.section.points.length > 0 && <QuakeDepthSection section={quakes.plots.section} selected={quakes.selected?.id ?? null} onPick={onQuakePick} />}
        {quakes.plots && <QuakeMagnitudeFrequency frequency={quakes.plots.frequency} />}
        {onQuakePick && quakes.list && quakes.list.length > 0 && <PickList summary={`${quakes.year === null ? "Largest events" : `Events in ${quakes.year}`} (${shownOf(quakes.list.length, quakes.year === null ? quakes.total : quakes.counts?.find(entry => entry.year === quakes.year)?.count ?? 0)})`}
          label={quakes.year === null ? "Largest earthquakes in the record" : `Earthquakes in ${quakes.year}, newest first`} items={quakes.list} selected={quakes.selected?.id ?? null} onPick={onQuakePick} />}
        {quakes.selected && <div className="category-map-dock-quake-event" aria-live="polite">
          <p><b>M {quakes.selected.magnitude.toFixed(1)}{quakes.selected.magnitudeType ? ` ${quakes.selected.magnitudeType}` : ""}</b> · {quakes.selected.time.slice(0, 16).replace("T", " ")} UTC<br />
            {quakes.selected.place ?? "Kansas"}{quakes.selected.depthKilometers !== null ? ` · depth ${quakes.selected.depthKilometers} km` : ""}{quakes.selected.status ? ` · ${quakes.selected.status}` : ""}</p>
          <div>{quakes.selectedUrl && <a href={quakes.selectedUrl} target="_blank" rel="noreferrer">USGS event page ↗</a>}
            <button type="button" onClick={onQuakeClear} aria-label="Clear the selected earthquake">Clear</button></div>
        </div>}
      </div>}
    </>}
    {look.tools?.includes("photoreal") && photoreal && onPhotoreal && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={photoreal.on} onClick={() => onPhotoreal(photoreal.on ? null : photoreal.place ?? photoreal.landscapes[0].id)}
        title="The 2024 one-foot Kansas aerial on the USGS 3DEP bare-earth DEM at true vertical scale, lit by the real sun">{photoreal.on ? "Back to relief colours" : "Photo-real 3D"}</button>
      {photoreal.on && <div className="category-map-dock-places" role="group" aria-label="Kansas landscapes">
        {photoreal.landscapes.map(landscape => <button key={landscape.id} type="button" aria-pressed={photoreal.place === landscape.id} onClick={() => onPhotoreal(landscape.id)}>{landscape.name}</button>)}
      </div>}
      {photoreal.on && <p className="category-map-dock-reading" aria-live="polite">{photoreal.landscapes.find(landscape => landscape.id === photoreal.place)?.caption}{" "}
        <span className="category-map-dock-scale-note">{Math.abs(photoreal.depth - 1) < 0.05 ? "True vertical scale (1×)" : `Vertical ×${photoreal.depth.toFixed(1)}`} · USGS 3DEP bare earth · Kansas aerial 2024, 1 ft</span></p>}
    </>}
    {look.tools?.includes("reviewed") && reviewed && onReviewed && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={reviewed.on} onClick={() => onReviewed(!reviewed.on)}
        title={reviewed.effectiveDay ? "Approved historical source snapshots, each at its own boundary date" : "Snapshots the site's publishing pipeline reviewed and stored, each at its own source time"}>{reviewed.on ? "Hide reviewed snapshots" : `Reviewed ${reviewed.source} snapshots`}</button>
      {reviewed.on && <div className="category-map-dock-reviewed">
        {reviewed.count > 1 && <div className="category-map-dock-range"><span id="category-map-dock-reviewed">Snapshot</span>
          <input type="range" min={0} max={reviewed.count - 1} step={1} value={Math.max(0, reviewed.index)} aria-labelledby="category-map-dock-reviewed"
            aria-valuetext={reviewed.effectiveDay ?? reviewed.publishedAt ?? "no snapshot"} onChange={event => { onReviewedPlay?.(false); onReviewedIndex?.(Number(event.target.value)); }} />
          <button type="button" aria-pressed={reviewed.playing && reviewed.motionAllowed} disabled={!reviewed.motionAllowed || Boolean(reviewed.effectiveDay)} onClick={() => onReviewedPlay?.(!reviewed.playing)}
            title={reviewed.motionAllowed ? "Step through the stored snapshots, oldest to newest" : "Reduced motion is on; move Snapshot by hand"}>{reviewed.playing && reviewed.motionAllowed ? "Pause" : "Play"}</button></div>}
        <p className="category-map-dock-reading" aria-live={reviewed.playing ? "off" : "polite"}>{reviewed.loading ? "Reading the site database…"
          : reviewed.reason ? reviewed.reason
          : `Snapshot ${reviewed.index + 1} of ${reviewed.count} · ${reviewed.effectiveDay ? "boundary date " + reviewed.effectiveDay : "captured for " + reviewed.capturedFor} · published ${reviewed.publishedAt} · ${reviewed.features} ${reviewed.features === 1 ? "feature" : "features"}${reviewed.freshness === "stale" ? " · older than two hours" : ""}`}</p>
        {reviewed.effectiveDay && onReviewedDate && <button type="button" className="category-map-dock-tool" onClick={() => onReviewedDate(reviewed.effectiveDay!)}>Set map to {reviewed.effectiveDay}</button>}
        {reviewed.historical && <small>Only approved snapshots are listed. Each is one exact date; missing dates and the 1873–1874 disputed coverage stay unavailable. Source areas are not counts of organized counties.</small>}
        {onReviewedPick && reviewed.list && reviewed.list.length > 0 && <PickList summary={`Features in this snapshot (${shownOf(reviewed.list.length, reviewed.features ?? 0)})`}
          label={reviewed.effectiveDay ? "Historical source areas, by name" : "Snapshot features, most significant first"} items={reviewed.list} selected={reviewed.pick ?? null} onPick={onReviewedPick} />}
        {reviewed.selected && <div className="category-map-dock-quake-event" aria-live="polite">
          <p><b>{reviewed.selected.title}</b>{reviewed.selected.lines.map(line => <span key={line}><br />{line}</span>)}
            <br /><span className="category-map-dock-release">Release {reviewed.selected.release.slice(0, 12)}… · external context, not evidence</span></p>
          <div>{reviewed.selected.link && <a href={reviewed.selected.link.href} target="_blank" rel="noreferrer">{reviewed.selected.link.label}</a>}
            <a href={reviewed.selected.download} download>Release JSON</a>
            <button type="button" onClick={onReviewedClear} aria-label="Clear the selected snapshot feature">Clear</button></div>
        </div>}
      </div>}
    </>}
    {look.tools?.includes("drought") && drought && onDrought && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={drought.on} onClick={() => onDrought(!drought.on)}
        title="The weekly U.S. Drought Monitor over Kansas, D0 abnormally dry to D4 exceptional drought, with Kansas's share in each since 2000">{drought.on ? "Hide the Drought Monitor" : "Show the Drought Monitor"}</button>
      {drought.on && <div className="category-map-dock-drought">
        {drought.weeks && drought.weeks.length > 1 && <DroughtChart weeks={drought.weeks} date={drought.date} categories={drought.categories} onWeek={onDroughtWeek} />}
        {drought.weeks && drought.weeks.length > 1 && (() => {
          const weeks = drought.weeks, index = drought.date ? weeks.findIndex(week => week.date === drought.date) : weeks.length - 1;
          return <div className="category-map-dock-range"><span id="category-map-dock-drought-week">Week</span>
            <input type="range" min={0} max={weeks.length - 1} step={1} value={index < 0 ? weeks.length - 1 : index} aria-labelledby="category-map-dock-drought-week"
              aria-valuetext={drought.label ?? weeks[weeks.length - 1].label} onChange={event => onDroughtWeek?.(Number(event.target.value) === weeks.length - 1 ? null : weeks[Number(event.target.value)].date)} />
          </div>;
        })()}
        <div className="category-map-dock-modes category-map-dock-drought-steps" role="group" aria-label="Drought Monitor week">
          <button type="button" aria-label="Week before" disabled={!drought.previous} onClick={() => drought.previous && onDroughtWeek?.(drought.previous)}>◀ Week</button>
          <button type="button" aria-pressed={drought.newest} onClick={() => onDroughtWeek?.(null)}>Newest</button>
          <button type="button" aria-label="Week after" disabled={!drought.next} onClick={() => drought.next && onDroughtWeek?.(drought.next)}>Week ▶</button>
          {onDroughtPlay && <button type="button" aria-pressed={Boolean(drought.playing && drought.motionAllowed)} disabled={drought.motionAllowed === false} onClick={() => onDroughtPlay(!drought.playing)}
            title={drought.motionAllowed === false ? "Reduced motion is on; step the weeks by hand" : drought.newest ? "Play the past year, a week at a time" : "Play forward a week at a time to the newest"}>{drought.playing && drought.motionAllowed !== false ? "Pause" : "Play"}</button>}
        </div>
        <p className="category-map-dock-reading" aria-live={drought.playing ? "off" : "polite"}>{drought.failed ? <>The Drought Monitor did not answer for this week. <a href={drought.url} target="_blank" rel="noreferrer">USDM ↗</a></>
          : drought.loading ? `Reading the Drought Monitor${drought.label ? ` for ${drought.label}` : ""}…` : drought.reading}</p>
        {drought.seriesFailed && <p className="category-map-dock-scale-note">The USDM statistics did not answer; the shares are measured on the map.</p>}
        {onDroughtChange && drought.change && <>
          <div className="category-map-dock-modes" role="group" aria-label="Drought map view">
            {([[0, "Categories", "The USDM categories, D0 to D4"], [4, "4-week change", "Each county's change in drought over the 4 weeks before the week shown"], [12, "12-week change", "Each county's change in drought over the 12 weeks before the week shown"]] as const).map(([weeks, label, title]) =>
              <button key={weeks} type="button" aria-pressed={drought.change!.weeks === weeks} title={title} onClick={() => onDroughtChange(weeks)}>{label}</button>)}
          </div>
          {drought.change.weeks > 0 && <p className="category-map-dock-reading" aria-live={drought.playing ? "off" : "polite"}>{drought.change.start ? `The Drought Monitor begins Jan 4, 2000, so a ${drought.change.weeks}-week change starts with the week of ${drought.change.start}; the categories stay on the map.`
            : drought.change.failed ? "The earlier week did not answer; the categories stay on the map."
            : drought.change.loading || !drought.change.reading ? `Reading the week ${drought.change.weeks} weeks before…` : drought.change.reading}</p>}
        </>}
        {drought.counties && !drought.loading && !drought.failed && <>
          <p className="category-map-dock-scale-note">{drought.counties.summary}</p>
          {onDroughtCounty && (drought.change?.weeks ?? 0) > 0 && drought.change?.reading
            ? <PickList summary={`Counties, most worsened first (${drought.counties.list.length})`} label={`Kansas counties by drought change over ${drought.change.weeks} weeks, most worsened first`}
              items={drought.counties.list} selected={drought.counties.picked} onPick={onDroughtCounty} />
            : onDroughtCounty && <PickList summary={`Counties, most severe first (${drought.counties.list.length})`} label="Kansas counties by drought, most severe first"
              items={drought.counties.list} selected={drought.counties.picked} onPick={onDroughtCounty} />}
          {drought.counties.reading && <div className="category-map-dock-quake-event" aria-live={drought.playing ? "off" : "polite"}>
            <p>{drought.counties.reading}</p>
            <div><button type="button" onClick={onDroughtCountyClear} aria-label="Clear the selected county">Clear</button></div>
          </div>}
        </>}
      </div>}
    </>}
    {look.tools?.includes("aquifer") && aquifer && onAquiferView && <>
      <div className="category-map-dock-modes" role="group" aria-label="Aquifer map">
        {AQUIFER_VIEWS.map(([view, label, title]) => <button key={view} type="button" aria-pressed={aquifer.view === view} title={title} onClick={() => onAquiferView(view)}>{label}</button>)}
      </div>
      {aquifer.legend && <div className="category-map-dock-legend" aria-label={aquifer.view === "kgs-depth-to-water" ? "Depth to water, feet" : "Saturated thickness, feet"}>
        <ul className="category-map-dock-ramp">{aquifer.legend.map(entry => <li key={entry.label}><span className="category-map-dock-chip" style={{ background: entry.color }} aria-hidden="true" /><span>{entry.label}</span></li>)}</ul>
        <p className="category-map-dock-reading">{aquifer.view === "kgs-depth-to-water" ? "Depth to water" : "Saturated thickness"}, feet · KGS High Plains Atlas, 2022–2024 classes, not well measurements</p>
      </div>}
    </>}
    {look.tools?.includes("wells") && wells && onWells && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={wells.on} onClick={() => onWells(!wells.on)}
        title="The KGS monitoring wells: pick one for its measured depth to water over the years, from USGS Water Data">{wells.on ? "Hide well water levels" : "Water levels at wells"}</button>
      {wells.on && <div className="category-map-dock-quakes">
        {!wells.picked && <p className="category-map-dock-reading" aria-live="polite">Pick a monitoring well on the map, or from the list, for its measured depth to water over the years.</p>}
        {onWellPick && wells.list.length > 0 && <PickList summary={`Wells nearest the map centre (${wells.list.length})`} label="KGS monitoring wells nearest the map centre"
          items={wells.list} selected={wells.picked} onPick={onWellPick} />}
        {wells.picked && <div className="category-map-dock-quake-event" aria-live="polite">
          <p>{`${wells.name ?? wells.picked} · USGS ${wells.picked}`}</p>
          <p>{wells.loading ? "Reading the USGS measurements…" : wells.failed ? "USGS Water Data did not answer for this well; no level is inferred. Try it again, or open its KGS record." : wells.reading}</p>
          {wells.plot && <WellHydrographChart plot={wells.plot} name={wells.name ?? wells.picked} />}
          <div>
            {wells.usgsUrl && <a href={wells.usgsUrl} target="_blank" rel="noreferrer">USGS record ↗</a>}
            {wells.kgsUrl && <a href={wells.kgsUrl} target="_blank" rel="noreferrer">KGS WIZARD ↗</a>}
            <button type="button" onClick={onWellClear} aria-label="Clear the selected well">Clear</button>
          </div>
        </div>}
      </div>}
    </>}
    {look.tools?.includes("soil") && soil && onSoil && <>
      <button type="button" className="category-map-dock-tool" aria-pressed={soil.on} onClick={() => onSoil(!soil.on)}
        title="NASA SMAP L4 modelled soil moisture in 9 km cells; a field-scale view pulls out to the region the cells describe">{soil.on ? "Hide soil moisture" : "Show soil moisture"}</button>
      {soil.on && <>
        <div className="category-map-dock-modes category-map-dock-depth" role="group" aria-label="Soil depth">
          {([["surface", "Surface 0–5 cm"], ["root", "Root zone 0–100 cm"]] as const).map(([depth, label]) =>
            <button key={depth} type="button" aria-pressed={soil.depth === depth} onClick={() => onSoilDepth?.(depth)}>{label}</button>)}
        </div>
        <p className="category-map-dock-reading" aria-live="polite">{soil.reading}</p>
        <img className="category-map-dock-scale" src={soil.legendUrl} alt="NASA colour scale for soil moisture" loading="lazy" />
      </>}
    </>}
    {look.tools?.includes("area") && onMeasureArea && <button type="button" className="category-map-dock-tool" aria-pressed={Boolean(measuringArea)} onClick={onMeasureArea}
      title={measuringArea ? "Cancel the outline in progress" : "Click around a field or parcel, then Finish, for its approximate area; not a survey"}>{measuringArea ? "Cancel area" : "Measure an area"}</button>}
    {look.tools?.includes("transect") && onTransect && <button type="button" className="category-map-dock-tool" disabled={!terrainAvailable} onClick={onTransect}
      title="Draw a line across the relief, then preview its elevation profile without the 3D exaggeration">Draw a cross-section</button>}
    {look.tools?.includes("underground") && onUnderground && <button type="button" className="category-map-dock-tool" onClick={onUnderground}
      title="Open recorded well logs, cores and aquifer sections beneath the map, on the 2D map">Explore underground</button>}
    {keys?.map(key => <section className="category-map-dock-legend category-map-dock-key" key={key.id} aria-label={`Key: ${key.title}`}>
      <strong>{key.title}</strong>
      {key.ramp && <div className="category-map-dock-key-ramp">
        <span className="category-map-dock-key-ramp-bar" aria-hidden="true" style={{ background: key.ramp.css }} />
        <span className="category-map-dock-key-ramp-ticks">{key.ramp.ticks.map(tick => <span key={tick.label} style={{ left: `${tick.at}%` }}>{tick.label}</span>)}</span>
      </div>}
      {key.items.length > 0 && <ul>{key.items.map(item => <li key={item.label}><span className={`category-map-dock-key-${item.shape}`} aria-hidden="true"
        data-dashed={item.dashed ? "true" : undefined}
        style={{ "--key": item.color, ...(item.size ? { "--size": `${item.size}px` } : {}), ...(item.stroke ? { "--stroke": item.stroke } : {}) } as CSSProperties} /><span>{item.label}</span></li>)}</ul>}
      <small>{key.note}</small>
    </section>)}
    <p className="category-map-dock-lede">{look.lede}</p>
    <div className="category-map-dock-actions">
      <button type="button" onClick={onReset}>Reset view</button>
      <button type="button" onClick={onLayers}>Layers for this map</button>
    </div>
  </section>;
}

type QuakeDockState = NonNullable<Parameters<typeof CategoryMapDock>[0]["quakes"]>;

/** What the record shows now, or why it shows nothing. */
export function quakeReading(quakes: Pick<QuakeDockState, "loading" | "failed" | "counts" | "total" | "startYear" | "endYear" | "minMagnitude" | "truncated" | "year">): string {
  if (quakes.loading) return "Reading the USGS earthquake catalog…";
  if (quakes.failed || !quakes.counts) return "The USGS catalog did not answer. Go back to the past 30 days, or try the record again.";
  const cut = quakes.truncated ? " · the catalog answer was cut short" : "";
  if (quakes.year !== null) {
    const count = quakes.counts.find(entry => entry.year === quakes.year)?.count ?? 0;
    return `${count.toLocaleString("en-US")} ${count === 1 ? "earthquake" : "earthquakes"} M${quakes.minMagnitude}+ in ${quakes.year} · choose All years to see the record${cut}`;
  }
  const peak = quakes.counts.reduce((best, entry) => entry.count > best.count ? entry : best, { year: quakes.startYear, count: 0 });
  return `${quakes.total.toLocaleString("en-US")} earthquakes M${quakes.minMagnitude}+ inside Kansas, ${quakes.startYear}–${quakes.endYear}${peak.count ? ` · most in ${peak.year} (${peak.count})` : ""}${cut}`;
}

/**
 * Events per year as bars in each year's map colour, so the chart is also the
 * colour key. A bar selects its year; the select beside it does the same from
 * the keyboard.
 */
export type DroughtChartWeek = Readonly<{ date: string; label: string; /** Percent of Kansas in D0 or worse … D4. */ shares: readonly number[] }>;
/**
 * Kansas's weekly share of area in each Drought Monitor category or worse,
 * drawn as the USDM draws its time series: each category's area over the
 * milder ones, 0–100% of the state. A click picks the week under it.
 */
export function DroughtChart({ weeks, date, categories, onWeek }: Readonly<{ weeks: readonly DroughtChartWeek[]; date: string | null; categories: readonly Readonly<{ id: string; color: string }>[]; onWeek?: (date: string | null) => void }>) {
  const height = 50, last = weeks.length - 1;
  const y = (share: number) => (height - share / 100 * height).toFixed(2);
  const index = date ? weeks.findIndex(week => week.date === date) : last;
  let peak = weeks[0];
  for (const week of weeks) if (week.shares[1] > peak.shares[1]) peak = week;
  const first = weeks[0].date.slice(0, 4), end = weeks[last].date.slice(0, 4);
  return <figure className="category-map-dock-drought-chart" aria-label={`Share of Kansas in each Drought Monitor category, weekly, ${first}–${end}; drought (D1–D4) peaked at ${Math.round(peak.shares[1])}% in the week of ${peak.label}`}>
    <svg viewBox={`0 0 ${Math.max(1, last)} ${height}`} preserveAspectRatio="none" aria-hidden="true"
      onClick={event => {
        const box = event.currentTarget.getBoundingClientRect();
        const i = Math.min(last, Math.max(0, Math.round((event.clientX - box.left) / Math.max(1, box.width) * last)));
        onWeek?.(i === last ? null : weeks[i].date);
      }}>
      {categories.map((category, k) => <path key={category.id} fill={category.color} d={`M0,${height} ${weeks.map((week, i) => `L${i},${y(week.shares[k])}`).join(" ")} L${last},${height} Z`} />)}
      {[25, 50, 75].map(share => <line key={share} x1={0} x2={last} y1={y(share)} y2={y(share)} stroke="#e6eff2" strokeOpacity={0.25} strokeWidth={0.6} vectorEffect="non-scaling-stroke" />)}
      {index >= 0 && <line x1={index} x2={index} y1={0} y2={height} stroke="#e6eff2" strokeWidth={1.4} vectorEffect="non-scaling-stroke" />}
    </svg>
    <figcaption><span>{first}</span><span>% of Kansas · gridlines 25, 50, 75</span><span>{end}</span></figcaption>
  </figure>;
}

/**
 * A stage hydrograph as the NWS draws it: the gauge's flood categories as
 * coloured bands from each stage up, the observed stage as a solid line, the
 * official forecast dashed with its points, and a line at now.
 */
export function FloodHydrographChart({ gauge, plot, reading }: Readonly<{ gauge: FloodGauge; plot: FloodHydrograph; reading: string | null }>) {
  const width = 260, height = 150, left = 22, right = 3, top = 4, bottom = 14;
  const x = (time: number) => left + (time - plot.start) / Math.max(1, plot.end - plot.start) * (width - left - right);
  const y = (value: number) => top + (plot.high - value) / Math.max(1e-6, plot.high - plot.low) * (height - top - bottom);
  const path = (points: FloodHydrograph["observed"]) => points.map((point, i) => `${i ? "L" : "M"}${x(point.time).toFixed(1)},${y(point.value).toFixed(1)}`).join(" ");
  const joined = plot.observed.length && plot.forecast.length ? [plot.observed[plot.observed.length - 1], ...plot.forecast] : plot.forecast;
  // A day label every day for a short plot, every other (or third) day for a long one.
  const stride = Math.max(1, Math.ceil(plot.days.length / 6));
  return <figure className="category-map-dock-section category-map-dock-hydrograph" aria-label={`${gauge.label} hydrograph for ${gauge.name}${reading ? `: ${reading}` : ""}`}>
    <svg viewBox={`0 0 ${width} ${height}`} aria-hidden="true">
      {plot.bands.map(band => <g key={band.id}>
        <rect x={left} width={width - left - right} y={y(band.to).toFixed(1)} height={Math.max(0, y(band.from) - y(band.to)).toFixed(1)} fill={band.color} fillOpacity={0.16} />
        {band.value >= plot.low && <>
          <line x1={left} x2={width - right} y1={y(band.value).toFixed(1)} y2={y(band.value).toFixed(1)} stroke={band.color} strokeWidth={1} />
          <text x={left + 3} y={(y(band.value) - 2.5).toFixed(1)} fontSize={8} fill={band.color}>{`${band.short} ${band.value.toFixed(1)}`}</text>
        </>}
      </g>)}
      {plot.ticks.map(value => <g key={value}>
        <line x1={left} x2={width - right} y1={y(value).toFixed(1)} y2={y(value).toFixed(1)} stroke="#e6eff2" strokeOpacity={0.12} strokeWidth={0.5} />
        <text x={left - 3} y={(y(value) + 2.8).toFixed(1)} fontSize={8} fill="#cfe2ea" textAnchor="end">{value}</text>
      </g>)}
      {plot.days.map((day, i) => <g key={day.time}>
        <line x1={x(day.time).toFixed(1)} x2={x(day.time).toFixed(1)} y1={top} y2={height - bottom} stroke="#e6eff2" strokeOpacity={0.1} strokeWidth={0.5} />
        {i % stride === 0 && <text x={x(day.time).toFixed(1)} y={height - 3} fontSize={8} fill="#cfe2ea" textAnchor="middle">{day.label}</text>}
      </g>)}
      {plot.now >= plot.start && plot.now <= plot.end && <line x1={x(plot.now).toFixed(1)} x2={x(plot.now).toFixed(1)} y1={top} y2={height - bottom} stroke="#ffffff" strokeOpacity={0.7} strokeWidth={0.8} strokeDasharray="2 2" />}
      {plot.observed.length > 1 && <path d={path(plot.observed)} fill="none" stroke="#5cc8ff" strokeWidth={1.6} strokeLinejoin="round" />}
      {joined.length > 1 && <path d={path(joined)} fill="none" stroke="#d58cff" strokeWidth={1.5} strokeDasharray="4 2" strokeLinejoin="round" />}
      {plot.forecast.map(point => <circle key={point.time} cx={x(point.time).toFixed(1)} cy={y(point.value).toFixed(1)} r={1.4} fill="#d58cff" />)}
      {plot.crest && <circle cx={x(plot.crest.time).toFixed(1)} cy={y(plot.crest.value).toFixed(1)} r={3.2} fill="none" stroke="#ffffff" strokeWidth={1} />}
    </svg>
    <figcaption><span>{`${gauge.label}${gauge.units ? `, ${gauge.units}` : ""} · Central time`}</span><span><span style={{ color: "#5cc8ff" }}>━ observed</span> <span style={{ color: "#d58cff" }}>╍ forecast</span></span></figcaption>
  </figure>;
}

/**
 * The year's daylight at a place: days across, Central clock time up, gold
 * between sunrise and sunset, twilights in deepening blues, solar noon dashed,
 * and today marked.
 */
export function SunYearChart({ chart, place }: Readonly<{ chart: SunChart; place: string }>) {
  const { width, height, left, top, plotWidth, plotHeight } = chart;
  const names: Record<string, string> = { day: "Day", civil: "Civil twilight", nautical: "Nautical", astronomical: "Astronomical", night: "Night" };
  return <figure className="category-map-dock-section category-map-dock-hydrograph" aria-label={`Sunrise, sunset and twilight through the year at ${place}, in Central clock time`}>
    <svg viewBox={`0 0 ${width} ${height}`} aria-hidden="true">
      <rect x={left} y={top} width={plotWidth} height={plotHeight} fill={chart.night} />
      {chart.bands.map(band => <path key={band.id} data-band={band.id} d={band.d} fill={band.color} />)}
      <path d={chart.noon} fill="none" stroke="#7a5a12" strokeWidth={0.8} strokeDasharray="3 2" />
      {chart.hours.map(h => <g key={h.y}>
        <line x1={left} x2={left + plotWidth} y1={h.y.toFixed(1)} y2={h.y.toFixed(1)} stroke="#e6eff2" strokeOpacity={0.15} strokeWidth={0.5} />
        <text x={left - 3} y={(h.y + 2.8).toFixed(1)} fontSize={8} fill="#cfe2ea" textAnchor="end">{h.label}</text>
      </g>)}
      {chart.months.map(m => <text key={m.x} x={m.x.toFixed(1)} y={height - 3} fontSize={7} fill="#cfe2ea">{m.label}</text>)}
      {chart.today !== null && <line data-today="" x1={chart.today.toFixed(1)} x2={chart.today.toFixed(1)} y1={top} y2={top + plotHeight} stroke="#ffffff" strokeWidth={0.9} />}
    </svg>
    <figcaption><span>Central clock time; the steps are the clock changing</span></figcaption>
    <p className="category-map-dock-fema-families">{[...chart.bands].reverse().map(band => <span key={band.id}><i style={{ background: band.color }} aria-hidden="true" />{names[band.id]}</span>)}
      <span><i style={{ background: chart.night, outline: "1px solid #3b4f8f" }} aria-hidden="true" />{names.night}</span></p>
  </figure>;
}

/**
 * A point's crop history as one bar a year, coloured by crop family; a grey
 * outline marks a year CropScape did not answer for, and a faint tick a year with no class.
 */
export function CropHistoryTimeline({ bars }: Readonly<{ bars: readonly Readonly<{ year: number; family: CropFamily | null; state: "ready" | "none" | "failed"; label: string }>[] }>) {
  const width = 260, height = 56, top = 4, bottom = 14, plot = height - top - bottom, step = width / bars.length;
  const families = [...new Set(bars.map(b => b.family).filter((f): f is CropFamily => f !== null))];
  return <figure className="category-map-dock-section category-map-dock-hydrograph" aria-label={`Crop history, ${bars[0]?.year} to ${bars[bars.length - 1]?.year}: ${bars.map(b => `${b.year} ${b.label}`).join('; ')}`}>
    <svg viewBox={`0 0 ${width} ${height}`} aria-hidden="true">
      {bars.map((bar, i) => <g key={bar.year} data-year={bar.year}>
        {bar.family && <rect x={(i * step + 0.6).toFixed(2)} y={top} width={(step - 1.2).toFixed(2)} height={plot} fill={CROP_FAMILY_COLORS[bar.family]} />}
        {bar.state === "failed" && <rect x={(i * step + 0.6).toFixed(2)} y={top} width={(step - 1.2).toFixed(2)} height={plot} fill="none" stroke="#9aa3ab" strokeWidth={0.6} strokeDasharray="2 1.5" />}
        {bar.state === "none" && <line x1={(i * step + step / 2).toFixed(2)} x2={(i * step + step / 2).toFixed(2)} y1={top + plot - 3} y2={top + plot} stroke="#5b6670" strokeWidth={0.8} />}
      </g>)}
      {bars.length > 0 && <>
        <text x={0} y={height - 3} fontSize={8} fill="#cfe2ea">{bars[0].year}</text>
        <text x={width} y={height - 3} fontSize={8} fill="#cfe2ea" textAnchor="end">{bars[bars.length - 1].year}</text>
      </>}
    </svg>
    <figcaption><span>Crop family by year</span></figcaption>
    <p className="category-map-dock-fema-families">{families.map(f => <span key={f}><i style={{ background: CROP_FAMILY_COLORS[f] }} aria-hidden="true" />{CROP_FAMILY_LABELS[f]}</span>)}</p>
  </figure>;
}
const CROP_FAMILY_COLORS: Readonly<Record<CropFamily, string>> = { corn: "#ffd300", sorghum: "#ff9e0b", soybeans: "#267000", sunflower: "#ffff00", wheat: "#a87000", "double-crop": "#707000", hay: "#ffa5e2", fallow: "#bfbf77", grass: "#e8ffbf", other: "#8a8a8a" };
const CROP_FAMILY_LABELS: Readonly<Record<CropFamily, string>> = { corn: "Corn", sorghum: "Sorghum", soybeans: "Soybeans", sunflower: "Sunflower", wheat: "Winter wheat", "double-crop": "Double crop", hay: "Alfalfa or hay", fallow: "Fallow", grass: "Grass or pasture", other: "Other" };

/**
 * The next 30 evenings' Moon, each a disc lit as it will be at 9 PM (the lit
 * limb on the right while waxing, as seen from Kansas), today first.
 */
export function MoonPhaseStrip({ strip }: Readonly<{ strip: MoonStrip }>) {
  // The fullest evening is picked on the unrounded fraction: two evenings can both round to the same percentage.
  const first = strip.discs[0], full = strip.discs.reduce((a, b) => b.fraction > a.fraction ? b : a);
  return <figure className="category-map-dock-section" aria-label={`The Moon over the next ${strip.discs.length} evenings, from ${first?.percent}% lit tonight; fullest ${full?.date}, ${full?.percent}% lit`}>
    <svg viewBox={`0 0 ${strip.width} ${strip.height}`} aria-hidden="true">
      {strip.discs.map(disc => <g key={disc.date} data-date={disc.date}>
        <circle cx={disc.cx.toFixed(2)} cy={disc.cy} r={strip.r} fill="#1a2238" stroke="#3b4f8f" strokeWidth={0.6} />
        {disc.d && <path d={disc.d} fill="#f0ead6" />}
      </g>)}
    </svg>
    <figcaption><span>{`Tonight first, ${strip.discs.length} evenings at 9 PM, left to right`}</span></figcaption>
  </figure>;
}

/**
 * A well's hydrograph as hydrogeologists draw it: depth to water increasing
 * downward, so a falling water level runs down the chart. Each measurement is
 * a dot (hollow while provisional), joined in time, with the record's
 * least-squares trend dashed across it.
 */
export function WellHydrographChart({ plot, name }: Readonly<{ plot: WellPlot; name: string }>) {
  const width = 260, height = 150, left = 26, right = 4, top = 4, bottom = 14;
  const x = (time: number) => left + (time - plot.start) / Math.max(1, plot.end - plot.start) * (width - left - right);
  const y = (depth: number) => top + (depth - plot.low) / Math.max(1e-6, plot.high - plot.low) * (height - top - bottom);
  const line = plot.points.map((p, i) => `${i ? "L" : "M"}${x(p.time).toFixed(1)},${y(p.depth).toFixed(1)}`).join(" ");
  const first = plot.points[0], last = plot.points[plot.points.length - 1];
  return <figure className="category-map-dock-section category-map-dock-hydrograph" aria-label={`Depth to water at ${name}, ${plot.points.length} measurements from ${plot.firstLabel} to ${plot.lastLabel}, ${first.depth.toFixed(1)} to ${last.depth.toFixed(1)} feet below land surface`}>
    <svg viewBox={`0 0 ${width} ${height}`} aria-hidden="true">
      {plot.ticks.map(value => <g key={value}>
        <line x1={left} x2={width - right} y1={y(value).toFixed(1)} y2={y(value).toFixed(1)} stroke="#e6eff2" strokeOpacity={0.12} strokeWidth={0.5} />
        <text x={left - 3} y={(y(value) + 2.8).toFixed(1)} fontSize={8} fill="#cfe2ea" textAnchor="end">{value}</text>
      </g>)}
      {plot.years.map(tick => <g key={tick.time}>
        <line x1={x(tick.time).toFixed(1)} x2={x(tick.time).toFixed(1)} y1={top} y2={height - bottom} stroke="#e6eff2" strokeOpacity={0.1} strokeWidth={0.5} />
        <text x={x(tick.time).toFixed(1)} y={height - 3} fontSize={8} fill="#cfe2ea" textAnchor="middle">{tick.label}</text>
      </g>)}
      {plot.trend && <line x1={x(plot.trend.from.time).toFixed(1)} y1={y(plot.trend.from.depth).toFixed(1)} x2={x(plot.trend.to.time).toFixed(1)} y2={y(plot.trend.to.depth).toFixed(1)}
        stroke="#f2b86b" strokeWidth={1.1} strokeDasharray="4 2" />}
      <path d={line} fill="none" stroke="#5cc8ff" strokeOpacity={0.7} strokeWidth={1} strokeLinejoin="round" />
      {plot.points.map(p => <g key={`${p.time}-${p.depth}`}>
        {p.span && <line data-span={p.precision} x1={x(p.span[0]).toFixed(1)} x2={x(p.span[1]).toFixed(1)} y1={y(p.depth).toFixed(1)} y2={y(p.depth).toFixed(1)} stroke="#5cc8ff" strokeOpacity={0.8} strokeWidth={0.8} />}
        <circle cx={x(p.time).toFixed(1)} cy={y(p.depth).toFixed(1)} r={1.7} fill={p.provisional ? "none" : "#5cc8ff"} stroke="#5cc8ff" strokeWidth={0.7} />
      </g>)}
    </svg>
    <figcaption><span>Depth to water, ft below land surface</span><span><span style={{ color: "#5cc8ff" }}>● measured{plot.points.some(p => p.span) ? " (bar: month or year only)" : ""}</span> <span style={{ color: "#f2b86b" }}>╍ trend</span></span></figcaption>
  </figure>;
}

/**
 * Tornadoes per year as bars stacked by rating, weakest at the base, in the
 * ratings' colours. A bar picks its year; the year select does the same.
 */
export function TornadoHistory({ years, year, series, onYear }: Readonly<{ years: readonly TornadoYear[]; year: number | null; series: readonly Readonly<{ name: string; color: string }>[]; onYear?: (year: number | null) => void }>) {
  const max = Math.max(1, ...years.map(entry => entry.total));
  const width = years.length * 4, height = 48;
  return <figure className="category-map-dock-histogram" aria-label={`Kansas tornadoes per year, ${years[0]?.year}–${years[years.length - 1]?.year}, by rating; the most in one year is ${max}`}>
    <svg viewBox={`0 0 ${width} ${height}`} preserveAspectRatio="none" aria-hidden="true">
      {years.map((entry, i) => {
        let base = height;
        return <g key={entry.year} data-year={entry.year} onClick={() => entry.total && onYear?.(year === entry.year ? null : entry.year)} opacity={year === null || year === entry.year ? 1 : 0.3}>
          <rect x={i * 4} y={0} width={4} height={height} fill="transparent" />
          {series.map((part, k) => {
            const n = entry.byRating[k];
            if (!n) return null;
            const h = n / max * (height - 2);
            base -= h;
            return <rect key={part.name} x={i * 4 + 0.4} y={base} width={3.2} height={h} fill={part.color} />;
          })}
        </g>;
      })}
    </svg>
    <figcaption><span>{years[0]?.year}</span><span>{max} in the busiest year</span><span>{years[years.length - 1]?.year}</span></figcaption>
  </figure>;
}

/**
 * Declarations per year as bars stacked by hazard family, in the families'
 * colours, so the chart is also their key. A bar picks its year; the year
 * select does the same from the keyboard.
 */
export function FemaHistory({ years, year, families, onYear }: Readonly<{ years: readonly FemaYear[]; year: number | null; families: typeof HAZARD_FAMILIES; onYear?: (year: number | null) => void }>) {
  const max = Math.max(1, ...years.map(entry => entry.total));
  const width = years.length * 4, height = 48;
  const shown = families.filter((_, k) => years.some(entry => entry.byFamily[k] > 0));
  return <figure className="category-map-dock-histogram" aria-label={`FEMA declarations per year, ${years[0]?.year}–${years[years.length - 1]?.year}, by hazard; the most in one year is ${max}`}>
    <svg viewBox={`0 0 ${width} ${height}`} preserveAspectRatio="none" aria-hidden="true">
      {years.map((entry, i) => {
        let base = height;
        return <g key={entry.year} data-year={entry.year} onClick={() => entry.total && onYear?.(year === entry.year ? null : entry.year)} opacity={year === null || year === entry.year ? 1 : 0.3}>
          <rect x={i * 4} y={0} width={4} height={height} fill="transparent" />
          {families.map((family, k) => {
            const n = entry.byFamily[k];
            if (!n) return null;
            const h = n / max * (height - 2);
            base -= h;
            return <rect key={family.id} x={i * 4 + 0.4} y={base} width={3.2} height={h} fill={family.color} />;
          })}
        </g>;
      })}
    </svg>
    <figcaption><span>{years[0]?.year}</span><span>{max} in the busiest year</span><span>{years[years.length - 1]?.year}</span></figcaption>
    <p className="category-map-dock-fema-families">{shown.map(family => <span key={family.id}><i style={{ background: family.color }} aria-hidden="true" />{family.name}</span>)}</p>
  </figure>;
}

const signedShare = (p: number) => `${p > 0 ? "+" : p < 0 ? "−" : ""}${Math.abs(p).toFixed(1)}%`;

/**
 * Every county's percent change as a bar from the zero line, largest gain on
 * the left to largest loss on the right, in its class colour: the shape of the
 * decade at a glance. A bar picks its county; the list does the same by keyboard.
 */
export function PopulationChangeChart({ bars, picked, onPick }: Readonly<{ bars: readonly Readonly<{ id: string; name: string; percent: number; color: string }>[]; picked: string | null; onPick?: (geoid: string) => void }>) {
  const up = Math.max(0, ...bars.map(bar => bar.percent)), down = Math.max(0, ...bars.map(bar => -bar.percent));
  const width = bars.length * 4, height = 64, span = up + down || 1, zero = height * up / span;
  const first = bars[0], last = bars[bars.length - 1];
  const losing = bars.filter(bar => bar.percent < 0).length;
  const at = picked === null ? -1 : bars.findIndex(bar => bar.id === picked);
  return <figure className="category-map-dock-histogram" aria-label={`Percent change in people, 2010–2020, for ${bars.length} Kansas counties from ${first?.name} (${signedShare(first?.percent ?? 0)}) to ${last?.name} (${signedShare(last?.percent ?? 0)}); ${losing} below zero`}>
    <svg viewBox={`0 0 ${width} ${height}`} preserveAspectRatio="none" aria-hidden="true">
      {bars.map((bar, i) => {
        const h = Math.abs(bar.percent) / span * height;
        return <g key={bar.id} data-county={bar.id} onClick={() => onPick?.(bar.id)} opacity={picked === null || picked === bar.id ? 1 : 0.5}>
          <rect x={i * 4} y={0} width={4} height={height} fill="transparent" />
          <rect x={i * 4 + 0.4} y={bar.percent >= 0 ? zero - h : zero} width={3.2} height={Math.max(h, 0.6)} fill={bar.color} stroke={picked === bar.id ? "#111111" : "none"} strokeWidth={0.6} />
        </g>;
      })}
      <line x1={0} x2={width} y1={zero} y2={zero} stroke="#5b5650" strokeWidth={0.5} />
      {at >= 0 && <line data-picked={picked} x1={at * 4 + 2} x2={at * 4 + 2} y1={0} y2={height} stroke="#f0e6c8" strokeWidth={0.8} strokeDasharray="2 1.5" />}
    </svg>
    <figcaption><span>{`${first?.name} ${signedShare(first?.percent ?? 0)}`}</span><span>{`0% line · ${bars.length} counties`}</span><span>{`${last?.name} ${signedShare(last?.percent ?? 0)}`}</span></figcaption>
  </figure>;
}
const SECTION_WEST = -102.05, SECTION_EAST = -94.59;
/**
 * The record as a west–east cross-section of Kansas: each event at its
 * longitude and depth, sized by magnitude and coloured by year as on the
 * map; the selected event is ringed and drawn last. A click picks an event.
 */
export function QuakeDepthSection({ section, selected, onPick }: Readonly<{ section: DepthSection; selected: string | null; onPick?: (id: string) => void }>) {
  const width = 300, height = 112, top = 6, bottom = 4;
  const x = (longitude: number) => (longitude - SECTION_WEST) / (SECTION_EAST - SECTION_WEST) * width;
  const y = (depth: number) => top + depth / section.maxDepth * (height - top - bottom);
  const ticks = Array.from({ length: section.maxDepth / 5 + 1 }, (_, i) => i * 5);
  const points = [...section.points.filter(point => point.id !== selected), ...section.points.filter(point => point.id === selected)];
  const notes = [section.atSetDepth ? `${section.atSetDepth} at exactly 5 or 10 km, often a set depth` : null, section.withoutDepth ? `${section.withoutDepth} without a depth` : null].filter(Boolean).join(" · ");
  return <figure className="category-map-dock-section" aria-label={`Depth section west to east across Kansas: ${section.points.length} events with a USGS depth, to ${section.maxDepth} km${notes ? `; ${notes}` : ""}`}>
    <svg viewBox={`0 0 ${width} ${height}`} aria-hidden="true">
      {ticks.map(depth => <g key={depth}>
        <line x1={0} x2={width} y1={y(depth)} y2={y(depth)} stroke="#e6eff2" strokeOpacity={depth === 0 ? 0.55 : 0.16} strokeWidth={0.6} />
        {depth > 0 && <text x={2} y={y(depth) - 1.5} fontSize={7} fill="#cfe2ea">{depth} km</text>}
      </g>)}
      {points.map(point => <circle key={point.id} data-id={point.id} cx={x(point.longitude).toFixed(1)} cy={y(point.depth).toFixed(1)} r={(1.2 + (point.magnitude - 2.5) * 1.3).toFixed(2)}
        fill={point.color} fillOpacity={0.82} stroke={point.id === selected ? "#ffffff" : "#140a1c"} strokeWidth={point.id === selected ? 1.4 : 0.4} onClick={() => onPick?.(point.id)} />)}
    </svg>
    <figcaption><span>102.05°W</span><span>west → east · depth below the surface</span><span>94.59°W</span></figcaption>
    {notes && <p className="category-map-dock-scale-note">{notes}</p>}
  </figure>;
}

/** The b-value line for the dock: the estimate and its error, or why there is none. */
export function bValueReading(frequency: MagnitudeFrequency): string {
  if (frequency.b === null || frequency.bError === null) return `${frequency.count} events of M${frequency.completeness}+; a b-value needs at least 50`;
  return `b = ${frequency.b.toFixed(2)} ± ${frequency.bError.toFixed(2)} (Aki–Utsu, M ≥ ${frequency.completeness}, n = ${frequency.count.toLocaleString("en-US")}) · magnitude types mixed`;
}
/**
 * The Gutenberg–Richter plot: how many events were of each magnitude or
 * larger, on a log scale, with the maximum-likelihood line log10 N = a − bM.
 */
export function QuakeMagnitudeFrequency({ frequency }: Readonly<{ frequency: MagnitudeFrequency }>) {
  const bins = frequency.bins.filter(bin => bin.count > 0);
  if (bins.length < 2) return null;
  const width = 300, height = 112, left = 22, right = 6, top = 6, bottom = 12;
  const low = frequency.completeness, high = Math.max(low + 0.5, bins[bins.length - 1].magnitude);
  const decades = Math.max(1, Math.ceil(Math.log10(bins[0].count)));
  const x = (m: number) => left + (m - low) / (high - low) * (width - left - right);
  const y = (n: number) => top + (1 - Math.log10(n) / decades) * (height - top - bottom);
  const fit = frequency.a !== null && frequency.b !== null ? (() => {
    const end = Math.min(high, frequency.a / frequency.b);
    return { x1: x(low), y1: y(10 ** (frequency.a - frequency.b * low)), x2: x(end), y2: y(10 ** (frequency.a - frequency.b * end)) };
  })() : null;
  return <figure className="category-map-dock-section" aria-label={`Magnitude–frequency: ${bValueReading(frequency)}`}>
    <svg viewBox={`0 0 ${width} ${height}`} aria-hidden="true">
      {Array.from({ length: decades + 1 }, (_, k) => <g key={k}>
        <line x1={left} x2={width - right} y1={y(10 ** k)} y2={y(10 ** k)} stroke="#e6eff2" strokeOpacity={0.16} strokeWidth={0.6} />
        <text x={left - 3} y={y(10 ** k) + 2.5} fontSize={7} fill="#cfe2ea" textAnchor="end">{(10 ** k).toLocaleString("en-US")}</text>
      </g>)}
      {fit && <line {...fit} stroke="#f89540" strokeWidth={1.2} strokeDasharray="4 2" />}
      {bins.map(bin => <rect key={bin.magnitude} x={(x(bin.magnitude) - 1.6).toFixed(1)} y={(y(bin.count) - 1.6).toFixed(1)} width={3.2} height={3.2} fill="#e6eff2" />)}
      {[low, high].map(m => <text key={m} x={x(m)} y={height - 2} fontSize={7} fill="#cfe2ea" textAnchor={m === low ? "start" : "end"}>M {m.toFixed(1)}</text>)}
    </svg>
    <figcaption><span>{bValueReading(frequency)}</span></figcaption>
  </figure>;
}

function QuakeHistogram({ counts, year, onYear }: Readonly<{ counts: readonly (YearCount & { color: string })[]; year: number | null; onYear?: (year: number | null) => void }>) {
  const max = Math.max(1, ...counts.map(entry => entry.count));
  const width = counts.length * 4, height = 44;
  return <figure className="category-map-dock-histogram" aria-label={`Earthquakes per year, ${counts[0]?.year}–${counts[counts.length - 1]?.year}; the most in one year is ${max}`}>
    <svg viewBox={`0 0 ${width} ${height}`} preserveAspectRatio="none" aria-hidden="true">
      {counts.map((entry, i) => {
        const h = entry.count ? Math.max(1.2, entry.count / max * (height - 2)) : 0;
        return <g key={entry.year} onClick={() => entry.count && onYear?.(year === entry.year ? null : entry.year)} data-year={entry.year}>
          <rect x={i * 4} y={0} width={4} height={height} fill="transparent" />
          {h > 0 && <rect x={i * 4 + 0.4} y={height - h} width={3.2} height={h} fill={entry.color} stroke="#e6eff2" strokeOpacity={0.45} strokeWidth={0.6} vectorEffect="non-scaling-stroke" opacity={year === null || year === entry.year ? 1 : 0.3} />}
        </g>;
      })}
    </svg>
    <figcaption><span>{counts[0]?.year}</span><span>{max} in the busiest year</span><span>{counts[counts.length - 1]?.year}</span></figcaption>
  </figure>;
}

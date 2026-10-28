import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { Feature, FeatureCollection, Point } from "geojson";
import type { MapKey } from "./map-keys";

/**
 * The Storm Prediction Center's preliminary local storm reports: tornadoes,
 * damaging wind and hail reported to the National Weather Service for one
 * convective day (12:00 UTC to 11:59 UTC the next day), as SPC collects them
 * to verify its outlooks. Drawn on the Storm desk beside the outlook, so the
 * forecast and what was reported can be read together. They are preliminary,
 * unverified reports, never a damage survey or the Storm Data record.
 */
export type ReportDay = "today" | "yesterday";
export const REPORT_DAYS: readonly ReportDay[] = Object.freeze(["today", "yesterday"]);
export type ReportKind = "torn" | "wind" | "hail";
export const STORM_REPORTS_SOURCE_ID = "kfm-storm-reports";
export const STORM_REPORTS_LAYER_ID = "kfm-storm-reports-points";
export const STORM_REPORTS_SELECTED_LAYER_ID = "kfm-storm-reports-selected";
/** SPC's filtered reports (duplicates near in time and place removed) for the current or previous convective day. */
export const stormReportsProviderUrl = (day: ReportDay): string => `https://www.spc.noaa.gov/climo/reports/${day}_filtered.csv`;
export const STORM_REPORTS_PAGE = "https://www.spc.noaa.gov/climo/reports/";

/**
 * SPC's report-map colours (tornado red, wind blue, hail green), set to read
 * on the dark storm base. Significant reports, SPC's thresholds of an EF2 or
 * stronger tornado, a gust of 65 kt (75 mph) or more and hail 2 inches or
 * larger, are drawn larger with a white ring.
 */
export const REPORT_KINDS = Object.freeze([
  Object.freeze({ id: "torn", name: "Tornado", plural: "tornado", color: "#ff4d4d" }),
  Object.freeze({ id: "wind", name: "Wind damage or gust", plural: "wind", color: "#4f8dff" }),
  Object.freeze({ id: "hail", name: "Hail", plural: "hail", color: "#3fcf5f" }),
] as const);
const KIND = new Map<string, (typeof REPORT_KINDS)[number]>(REPORT_KINDS.map(kind => [kind.id, kind]));
export const SIGNIFICANT_COLOR = "#ffffff";
const SIGNIFICANT = Object.freeze({ torn: 2, wind: 75, hail: 2 });

export type StormReport = Readonly<{
  id: string; kind: ReportKind;
  /** The report time, ISO UTC, placed in the convective day; null when SPC gives none. */
  time: string | null;
  /** EF rating for a tornado, mph for wind, inches for hail; null when unknown. */
  magnitude: number | null;
  significant: boolean;
  location: string; county: string; state: string;
  longitude: number; latitude: number;
  comments: string;
}>;
export type StormReports = Readonly<{
  day: ReportDay;
  /** The convective day the reports cover, ISO UTC: 12:00 to 11:59 the next day. */
  from: string; until: string;
  reports: readonly StormReport[];
  retrievedAt: string; source: string;
}>;

/** The convective day an SPC report file covers: "today" began at the most recent 12:00 UTC. */
export function convectiveDay(day: ReportDay, now: Date): { from: Date; until: Date } {
  const from = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate(), 12));
  if (now.getUTCHours() < 12) from.setUTCDate(from.getUTCDate() - 1);
  if (day === "yesterday") from.setUTCDate(from.getUTCDate() - 1);
  return { from, until: new Date(from.getTime() + 24 * 3_600_000 - 60_000) };
}

const unquote = (value: string) => value.trim().replace(/^"(.*)"$/s, "$1").replace(/""/g, "\"").trim();
/** SPC writes coordinates as decimals; older and raw files write hundredths with west longitude positive. */
function coordinate(value: string, longitude: boolean): number | null {
  let number = Number(unquote(value));
  if (!Number.isFinite(number) || number === 0) return null;
  if (Math.abs(number) > (longitude ? 180 : 90)) number /= 100;
  if (longitude && number > 0) number = -number;
  return longitude ? number >= -180 && number <= -60 ? Math.round(number * 1e4) / 1e4 : null
    : number >= 15 && number <= 72 ? Math.round(number * 1e4) / 1e4 : null;
}
function magnitudeOf(kind: ReportKind, raw: string): number | null {
  const value = unquote(raw).toUpperCase();
  if (kind === "torn") { const rating = /^E?F([0-5])$/.exec(value); return rating ? Number(rating[1]) : null; }
  const number = Number(value);
  if (!value || !Number.isFinite(number) || number <= 0) return null;
  // Hail is in hundredths of an inch.
  return kind === "hail" ? Math.round(number) / 100 : Math.round(number);
}
/** Which section a header row opens: SPC names the second column F_Scale (or leaves it blank), Speed or Size. */
function sectionOf(cells: readonly string[]): ReportKind | null {
  if (unquote(cells[0] ?? "").toLowerCase() !== "time") return null;
  const second = unquote(cells[1] ?? "").toLowerCase();
  return second === "speed" ? "wind" : second === "size" ? "hail" : second === "f_scale" || second === "" || second === "ef_scale" ? "torn" : null;
}

/**
 * SPC's report CSV to the reports drawn: three sections (tornado, wind, hail),
 * each opened by its own header row; comments may hold commas, so everything
 * after the seventh column is the comment. Rows without a usable position are
 * left out.
 */
export function parseStormReports(raw: string, day: ReportDay, now: Date, source: string): StormReports {
  if (typeof raw !== "string") throw new Error("The SPC storm reports were not text.");
  const { from, until } = convectiveDay(day, now);
  const reports: StormReport[] = [];
  let kind: ReportKind | null = null, sections = 0;
  for (const line of raw.split(/\r?\n/)) {
    if (!line.trim()) continue;
    const cells = line.split(",");
    const opened = sectionOf(cells);
    if (opened) { kind = opened; sections++; continue; }
    if (!kind || cells.length < 7) continue;
    const latitude = coordinate(cells[5], false), longitude = coordinate(cells[6], true);
    if (latitude === null || longitude === null) continue;
    const clock = /^(\d{1,2})(\d{2})$/.exec(unquote(cells[0]));
    let time: string | null = null;
    if (clock && +clock[1] < 24 && +clock[2] < 60) {
      // Reports before 12:00 UTC belong to the morning that ends the convective day.
      const at = new Date(from);
      if (+clock[1] < 12) at.setUTCDate(at.getUTCDate() + 1);
      at.setUTCHours(+clock[1], +clock[2]);
      time = at.toISOString();
    }
    const magnitude = magnitudeOf(kind, cells[1]);
    reports.push(Object.freeze({
      id: `${kind}-${reports.length}`, kind, time, magnitude,
      significant: magnitude !== null && magnitude >= SIGNIFICANT[kind],
      location: unquote(cells[2]).slice(0, 120), county: unquote(cells[3]).slice(0, 80), state: unquote(cells[4]).toUpperCase().slice(0, 2),
      longitude, latitude, comments: unquote(cells.slice(7).join(",")).slice(0, 600),
    }));
  }
  if (!sections) throw new Error("The SPC storm reports had no report sections.");
  return Object.freeze({ day, from: from.toISOString(), until: until.toISOString(), reports: Object.freeze(reports), retrievedAt: now.toISOString(), source });
}

const record = (value: unknown): Record<string, unknown> | null => value && typeof value === "object" && !Array.isArray(value) ? value as Record<string, unknown> : null;
export function validStormReports(value: unknown): value is StormReports {
  const candidate = record(value);
  return Boolean(candidate && REPORT_DAYS.includes(candidate.day as ReportDay) && typeof candidate.from === "string" && typeof candidate.until === "string"
    && typeof candidate.retrievedAt === "string" && Array.isArray(candidate.reports)
    && candidate.reports.every(item => {
      const r = record(item);
      return r && typeof r.id === "string" && KIND.has(r.kind as string) && typeof r.longitude === "number" && typeof r.latitude === "number"
        && Number.isFinite(r.longitude) && Number.isFinite(r.latitude) && (r.magnitude === null || typeof r.magnitude === "number")
        && (r.time === null || typeof r.time === "string") && typeof r.significant === "boolean"
        && typeof r.location === "string" && typeof r.county === "string" && typeof r.state === "string" && typeof r.comments === "string";
    }));
}

/** A report's magnitude as SPC states it. */
export function reportMagnitude(report: StormReport): string {
  if (report.magnitude === null) return report.kind === "torn" ? "EF rating not yet known" : report.kind === "wind" ? "speed not measured" : "size unknown";
  return report.kind === "torn" ? `EF${report.magnitude}` : report.kind === "wind" ? `${report.magnitude} mph` : `${report.magnitude.toFixed(2)} in`;
}

const CLOCK = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit", hourCycle: "h23" });
export const reportClock = (iso: string): string => `${CLOCK.format(new Date(iso))} UTC`;

/** The reports for Kansas by kind, with the national total and the convective day. */
export function stormReportsReading(reports: StormReports): string {
  const kansas = reports.reports.filter(report => report.state === "KS");
  const counts = REPORT_KINDS.map(kind => [kind, kansas.filter(report => report.kind === kind.id).length] as const).filter(([, n]) => n > 0);
  const significant = kansas.filter(report => report.significant).length;
  const window = ` · ${reportClock(reports.from)} to ${reportClock(reports.until)}`;
  if (!reports.reports.length) return `No reports yet this convective day${window}`;
  const local = counts.length ? `Kansas: ${counts.map(([kind, n]) => `${n} ${kind.plural}`).join(", ")} report${kansas.length === 1 ? "" : "s"}${significant ? ` (${significant} significant)` : ""}` : "No reports in Kansas";
  return `${local} · ${reports.reports.length} across the US${window}`;
}

export function stormReportsKey(day: ReportDay): MapKey {
  return Object.freeze({
    id: "storm-reports", title: `SPC storm reports · ${day === "today" ? "Today" : "Yesterday"}`,
    items: Object.freeze([
      ...REPORT_KINDS.map(kind => Object.freeze({ label: kind.name, color: kind.color, shape: "dot" as const })),
      Object.freeze({ label: "Significant: EF2+, 75 mph+, 2 in+ hail", color: "#9aa5ad", shape: "dot" as const, size: 12, stroke: SIGNIFICANT_COLOR }),
    ]),
    note: "Preliminary reports to the National Weather Service for the convective day, 12:00 to 11:59 UTC; duplicates filtered by SPC. Unverified, may change, and placed at the reported location.",
  });
}

const geojson = (reports: readonly StormReport[]): FeatureCollection<Point, { id: string; kind: ReportKind; significant: boolean; rank: number }> => ({
  type: "FeatureCollection",
  // Tornadoes over wind over hail; significant reports over the rest.
  features: reports.map((report): Feature<Point, { id: string; kind: ReportKind; significant: boolean; rank: number }> => ({
    type: "Feature", geometry: { type: "Point", coordinates: [report.longitude, report.latitude] },
    properties: { id: report.id, kind: report.kind, significant: report.significant, rank: (report.kind === "torn" ? 20 : report.kind === "wind" ? 10 : 0) + (report.significant ? 5 : 0) },
  })),
});
const colors = ["match", ["get", "kind"], ...REPORT_KINDS.flatMap(kind => [kind.id, kind.color]), "#9aa5ad"];
/** Zoom is the outer input; the stops read the report, as MapLibre requires. */
const radius = (extra = 0) => ["interpolate", ["linear"], ["zoom"], 4, ["case", ["get", "significant"], 5.5 + extra, 3.6 + extra], 9, ["case", ["get", "significant"], 9 + extra, 6 + extra]];
const shown = new WeakMap<MapLibreMap, readonly StormReport[]>();

/** Draws the reports (or removes them, for null) and rings the selected one. Safe to call on every style load. */
export function syncStormReports(map: MapLibreMap, reports: StormReports | null, selectedId: string | null): void {
  if (!reports) {
    for (const id of [STORM_REPORTS_SELECTED_LAYER_ID, STORM_REPORTS_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(STORM_REPORTS_SOURCE_ID)) map.removeSource(STORM_REPORTS_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const source = map.getSource(STORM_REPORTS_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(STORM_REPORTS_SOURCE_ID, { type: "geojson", data: geojson(reports.reports) });
  else if (shown.get(map) !== reports.reports) source.setData(geojson(reports.reports));
  shown.set(map, reports.reports);
  // Above the outlook lines and provider layers, under the site's own overlays and labels.
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background"
    && !layer.id.startsWith(STORM_REPORTS_SOURCE_ID) && !layer.id.startsWith("kfm-spc-outlook"))?.id;
  if (!map.getLayer(STORM_REPORTS_LAYER_ID)) map.addLayer({ id: STORM_REPORTS_LAYER_ID, type: "circle", source: STORM_REPORTS_SOURCE_ID,
    layout: { "circle-sort-key": ["get", "rank"] as never },
    paint: { "circle-color": colors as never, "circle-radius": radius() as never, "circle-opacity": 0.92,
      "circle-stroke-color": ["case", ["get", "significant"], SIGNIFICANT_COLOR, "#0b1418"] as never,
      "circle-stroke-width": ["case", ["get", "significant"], 1.8, 0.8] as never } }, before);
  if (!map.getLayer(STORM_REPORTS_SELECTED_LAYER_ID)) map.addLayer({ id: STORM_REPORTS_SELECTED_LAYER_ID, type: "circle", source: STORM_REPORTS_SOURCE_ID,
    paint: { "circle-color": "rgba(0,0,0,0)", "circle-radius": radius(3.5) as never, "circle-stroke-color": "#ffe9a8", "circle-stroke-width": 2 } }, before);
  map.setFilter(STORM_REPORTS_SELECTED_LAYER_ID, ["==", ["get", "id"], selectedId ?? ""]);
}

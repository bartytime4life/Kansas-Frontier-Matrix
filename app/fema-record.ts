import type { Feature, FeatureCollection, Geometry } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";

/**
 * Every FEMA disaster declaration for Kansas since the first in 1953, from
 * OpenFEMA's Disaster Declarations Summaries: one entry per declaration with
 * the counties it designated. A county designation names a county as eligible
 * for assistance; it is not a footprint of the damage.
 */

export const FEMA_RECORD_SOURCE = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries";
export const FEMA_RECORD_PAGE_SIZE = 1000;
export const FEMA_RECORD_MAX_PAGES = 12;
export const femaDisasterPage = (number: number) => `https://www.fema.gov/disaster/${number}`;

export type FemaDeclarationType = "DR" | "EM" | "FM";
export const FEMA_DECLARATION_TYPES: Readonly<Record<FemaDeclarationType, string>> = Object.freeze({
  DR: "Major disaster", EM: "Emergency", FM: "Fire management",
});

export type HazardFamilyId = "storm" | "flood" | "winter" | "fire" | "drought" | "biological" | "other";
/** Incident types gathered into hazard families, each with one colour on the history chart. */
export const HAZARD_FAMILIES: readonly Readonly<{ id: HazardFamilyId; name: string; color: string; incidents: readonly string[] }>[] = Object.freeze([
  { id: "storm", name: "Severe storms & tornadoes", color: "#6a51a3", incidents: ["severe storm", "severe storm(s)", "tornado", "straight-line winds", "hurricane", "tropical storm", "coastal storm", "typhoon"] },
  { id: "flood", name: "Floods", color: "#2171b5", incidents: ["flood", "dam/levee break", "mud/landslide"] },
  { id: "winter", name: "Winter storms", color: "#41b6c4", incidents: ["snowstorm", "severe ice storm", "winter storm", "freezing"] },
  { id: "fire", name: "Fire", color: "#e6550d", incidents: ["fire"] },
  { id: "drought", name: "Drought", color: "#bf9b30", incidents: ["drought"] },
  { id: "biological", name: "Biological", color: "#9e9e9e", incidents: ["biological"] },
  { id: "other", name: "Other", color: "#d9d9d9", incidents: [] },
]);
export const hazardFamily = (incident: string | null): HazardFamilyId =>
  HAZARD_FAMILIES.find(family => family.incidents.includes((incident ?? "").trim().toLowerCase()))?.id ?? "other";

export type FemaDisaster = Readonly<{
  number: number;
  type: FemaDeclarationType;
  incident: string;
  family: HazardFamilyId;
  title: string;
  /** Declaration date, YYYY-MM-DD (UTC). */
  declared: string;
  year: number;
  begin: string | null;
  end: string | null;
  /** 2020 county GEOIDs designated; a statewide designation lists none and sets statewide. */
  counties: readonly string[];
  statewide: boolean;
}>;

export type FemaRecord = Readonly<{
  retrievedAt: string;
  source: string;
  disasters: readonly FemaDisaster[];
  firstYear: number;
  lastYear: number;
  rows: number;
  skipped: number;
  truncated: boolean;
}>;

type Row = Record<string, unknown>;
const isRow = (value: unknown): value is Row => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const text = (value: unknown, max = 200) => typeof value === "string" && value.trim() && value.length <= max ? value.trim() : null;
const day = (value: unknown) => {
  const candidate = text(value, 40);
  return candidate && /^\d{4}-\d\d-\d\dT/.test(candidate) && Number.isFinite(Date.parse(candidate)) ? candidate.slice(0, 10) : null;
};

/** One page of the OpenFEMA query: Kansas rows, the fields the record uses, in a stable order. */
export function femaRecordPageUrl(page: number): string {
  const url = new URL(FEMA_RECORD_SOURCE);
  url.searchParams.set("$filter", "state eq 'KS'");
  url.searchParams.set("$select", "id,disasterNumber,declarationType,declarationDate,incidentType,declarationTitle,incidentBeginDate,incidentEndDate,fipsStateCode,fipsCountyCode,designatedArea");
  url.searchParams.set("$orderby", "id");
  url.searchParams.set("$top", String(FEMA_RECORD_PAGE_SIZE));
  url.searchParams.set("$skip", String(page * FEMA_RECORD_PAGE_SIZE));
  return url.toString();
}

/**
 * Rows to declarations. A row designates one area of one declaration; rows
 * for the same disaster number are gathered. A Kansas county code (odd, 001–
 * 209) designates that county; "000" with a statewide area designates the
 * state; anything else (a tribal area, say) is counted as skipped.
 */
export function parseFemaRecord(rows: readonly unknown[], retrievedAt: string, source: string, truncated = false): FemaRecord {
  // A declaration's date is its earliest row's; its counties are all its rows'.
  const byNumber = new Map<number, { disaster: Omit<FemaDisaster, "counties" | "statewide">; counties: Set<string>; statewide: boolean }>();
  let skipped = 0;
  const seen = new Set<string>();
  for (const row of rows) {
    if (!isRow(row)) { skipped++; continue; }
    const id = text(row.id, 100);
    const number = row.disasterNumber;
    const type = row.declarationType;
    const declared = day(row.declarationDate);
    const county = text(row.fipsCountyCode, 3);
    if (!id || seen.has(id) || typeof number !== "number" || !Number.isInteger(number) || number <= 0 || number >= 100_000
      || (type !== "DR" && type !== "EM" && type !== "FM") || !declared || (row.fipsStateCode !== undefined && row.fipsStateCode !== "20" && row.fipsStateCode !== 20)) { skipped++; continue; }
    const area = text(row.designatedArea) ?? "";
    const statewide = county === "000" && /statewide/i.test(area);
    const countyCode = county && /^\d{3}$/.test(county) && Number(county) % 2 === 1 && Number(county) <= 209 ? county : null;
    if (!statewide && !countyCode) { skipped++; continue; }
    seen.add(id);
    let entry = byNumber.get(number);
    if (!entry) {
      const incident = text(row.incidentType, 80) ?? "Other";
      entry = { disaster: { number, type, incident, family: hazardFamily(incident), title: text(row.declarationTitle) ?? incident,
        declared, year: Number(declared.slice(0, 4)), begin: day(row.incidentBeginDate), end: day(row.incidentEndDate) }, counties: new Set(), statewide: false };
      byNumber.set(number, entry);
    } else if (declared < entry.disaster.declared) entry.disaster = { ...entry.disaster, declared, year: Number(declared.slice(0, 4)) };
    if (statewide) entry.statewide = true;
    else entry.counties.add(`20${countyCode}`);
  }
  const disasters = [...byNumber.values()].map(entry => Object.freeze({ ...entry.disaster, counties: Object.freeze([...entry.counties].sort()), statewide: entry.statewide }))
    .sort((a, b) => a.declared.localeCompare(b.declared) || a.number - b.number);
  const years = disasters.map(disaster => disaster.year);
  return Object.freeze({ retrievedAt, source, disasters: Object.freeze(disasters), firstYear: years.length ? Math.min(...years) : 1953,
    lastYear: years.length ? Math.max(...years) : new Date(retrievedAt).getUTCFullYear(), rows: rows.length, skipped, truncated });
}

export function validFemaRecord(value: unknown): value is FemaRecord {
  return isRow(value) && Array.isArray(value.disasters) && typeof value.firstYear === "number" && typeof value.lastYear === "number"
    && typeof value.retrievedAt === "string" && value.disasters.every(d => isRow(d) && typeof d.number === "number" && typeof d.year === "number"
      && Array.isArray(d.counties) && typeof d.family === "string" && typeof d.declared === "string");
}

export type FemaFilter = Readonly<{ family: HazardFamilyId | null; emergencies: boolean; year: number | null }>;
export const FEMA_DEFAULT_FILTER: FemaFilter = Object.freeze({ family: null, emergencies: false, year: null });

/** The declarations a view counts: major disasters only unless emergencies are included, of one family or all, in one year or all. */
export function femaSelect(record: Pick<FemaRecord, "disasters">, filter: FemaFilter): FemaDisaster[] {
  return record.disasters.filter(d => (filter.emergencies || d.type === "DR") && (!filter.family || d.family === filter.family) && (filter.year === null || d.year === filter.year));
}

export type FemaYear = Readonly<{ year: number; total: number; byFamily: readonly number[] }>;
/** Declarations per year, by family in HAZARD_FAMILIES order, every year of the record (the year filter is not applied). */
export function femaYears(record: FemaRecord, filter: FemaFilter): FemaYear[] {
  const chosen = femaSelect(record, { ...filter, year: null });
  return Array.from({ length: record.lastYear - record.firstYear + 1 }, (_, i) => {
    const year = record.firstYear + i;
    const byFamily = HAZARD_FAMILIES.map(family => chosen.filter(d => d.year === year && d.family === family.id).length);
    return { year, total: byFamily.reduce((a, b) => a + b, 0), byFamily };
  });
}

/** How many of the declarations designated each county; a statewide one counts for every county. */
export function femaCountyCounts(disasters: readonly FemaDisaster[], geoids: readonly string[]): Map<string, number> {
  const counts = new Map(geoids.map(geoid => [geoid, 0]));
  for (const disaster of disasters) {
    for (const geoid of disaster.statewide ? geoids : disaster.counties) if (counts.has(geoid)) counts.set(geoid, (counts.get(geoid) ?? 0) + 1);
  }
  return counts;
}

const ORANGES = ["#fdd0a2", "#fdae6b", "#f16913", "#d94801", "#8c2d04"];
export const FEMA_NONE_COLOR = "#f2efe6";
/** Five equal classes of a round width from 1 up to the largest count; 0 has its own pale colour. */
export function femaClasses(max: number): { from: number; to: number; color: string }[] {
  if (max <= 0) return [];
  const raw = max / 5;
  const power = 10 ** Math.floor(Math.log10(Math.max(raw, 1)));
  const width = Math.max(1, [1, 2, 5, 10].map(m => m * power).find(w => w >= raw) ?? 10 * power);
  const classes: { from: number; to: number; color: string }[] = [];
  for (let k = 0; k < 5 && k * width + 1 <= max; k++) classes.push({ from: k * width + 1, to: (k + 1) * width, color: ORANGES[k] });
  return classes;
}
export const femaCountColor = (count: number, classes: ReturnType<typeof femaClasses>) =>
  count <= 0 ? FEMA_NONE_COLOR : (classes.find(c => count >= c.from && count <= c.to) ?? classes[classes.length - 1]).color;

/** The county outlines carrying each count and its class colour, for the choropleth. */
export function femaCountyCollection(counties: FeatureCollection, counts: Map<string, number>): FeatureCollection {
  const classes = femaClasses(Math.max(0, ...counts.values()));
  return { type: "FeatureCollection", features: counties.features.flatMap((feature): Feature<Geometry>[] => {
    const geoid = String(feature.properties?.geoid ?? "");
    if (!feature.geometry || !counts.has(geoid)) return [];
    const count = counts.get(geoid) ?? 0;
    return [{ type: "Feature", geometry: feature.geometry, properties: { geoid, name: String(feature.properties?.name ?? geoid), count, color: femaCountColor(count, classes) } }];
  }) };
}

export function femaCountyList(counts: Map<string, number>, names: Map<string, string>): { id: string; label: string }[] {
  return [...counts].sort((a, b) => b[1] - a[1] || (names.get(a[0]) ?? a[0]).localeCompare(names.get(b[0]) ?? b[0]))
    .map(([geoid, count]) => ({ id: geoid, label: `${names.get(geoid) ?? geoid} · ${count}` }));
}

const MONTH = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", year: "numeric" });
const monthOf = (date: string) => MONTH.format(Date.parse(`${date}T00:00:00Z`));
const familyName = (id: HazardFamilyId) => HAZARD_FAMILIES.find(f => f.id === id)?.name ?? "Other";
const plural = (n: number, one: string, many: string) => `${n.toLocaleString("en-US")} ${n === 1 ? one : many}`;
const kindOf = (filter: FemaFilter) => filter.emergencies ? ["declaration", "declarations"] as const : ["major disaster declaration", "major disaster declarations"] as const;

/** One county's declarations in the view, newest first, for its list. */
export function femaCountyDisasters(disasters: readonly FemaDisaster[], geoid: string): { id: string; label: string }[] {
  return disasters.filter(d => d.statewide || d.counties.includes(geoid)).slice().reverse()
    .map(d => ({ id: String(d.number), label: `${d.type}-${d.number} · ${d.title} · ${monthOf(d.declared)}` }));
}

/** The statewide line: how many declarations the view counts, over which years, and the busiest year. */
export function femaReading(record: FemaRecord, filter: FemaFilter, years: readonly FemaYear[]): string {
  const [one, many] = kindOf(filter);
  const family = filter.family ? ` · ${familyName(filter.family).toLowerCase()}` : "";
  const cut = record.truncated ? " · the OpenFEMA answer was cut short" : "";
  if (filter.year !== null) {
    const n = years.find(y => y.year === filter.year)?.total ?? 0;
    return `${plural(n, one, many)} in Kansas in ${filter.year}${family} · choose All years for the record${cut}`;
  }
  const total = years.reduce((a, y) => a + y.total, 0);
  const peak = years.reduce((best, y) => y.total > best.total ? y : best, { year: record.firstYear, total: 0, byFamily: [] } as FemaYear);
  return `${plural(total, one, many)} in Kansas, ${record.firstYear}–${record.lastYear}${family}${peak.total ? ` · most in ${peak.year} (${peak.total})` : ""}${cut}`;
}

/** The picked county's line: its count in the view, its most frequent family, and its latest declaration. */
export function femaCountyReading(name: string, geoid: string, disasters: readonly FemaDisaster[], filter: FemaFilter, firstYear: number): string {
  const mine = disasters.filter(d => d.statewide || d.counties.includes(geoid));
  const [one, many] = kindOf(filter);
  const span = filter.year !== null ? `in ${filter.year}` : `since ${firstYear}`;
  if (!mine.length) return `${name} County: no ${many} ${span}${filter.family ? ` for ${familyName(filter.family).toLowerCase()}` : ""}`;
  const byFamily = HAZARD_FAMILIES.map(f => ({ f, n: mine.filter(d => d.family === f.id).length })).sort((a, b) => b.n - a.n);
  const latest = mine[mine.length - 1];
  return `${name} County: ${plural(mine.length, one, many)} ${span}${!filter.family && byFamily[0].n ? ` · most often ${byFamily[0].f.name.toLowerCase()} (${byFamily[0].n})` : ""} · latest ${latest.type}-${latest.number}, declared ${monthOf(latest.declared)}`;
}

export function femaKey(classes: ReturnType<typeof femaClasses>, filter: FemaFilter, firstYear: number, lastYear: number): MapKey {
  const [, many] = kindOf(filter);
  return Object.freeze({
    id: "fema-record",
    title: `FEMA ${many} per county · ${filter.year ?? `${firstYear}–${lastYear}`}${filter.family ? ` · ${familyName(filter.family)}` : ""}`,
    items: Object.freeze([{ label: "None", color: FEMA_NONE_COLOR, shape: "area" as const },
      ...classes.map(c => ({ label: c.from === c.to ? `${c.from}` : `${c.from}–${c.to}`, color: c.color, shape: "area" as const }))]),
    note: "OpenFEMA county designations: a county named eligible for assistance, not a map of the damage. A statewide declaration counts for every county. Tribal designations are not drawn.",
  });
}

export const FEMA_RECORD_SOURCE_ID = "kfm-fema-record";
export const FEMA_RECORD_FILL_LAYER_ID = "kfm-fema-record-fill";
export const FEMA_RECORD_LINE_LAYER_ID = "kfm-fema-record-line";
export const FEMA_RECORD_SELECTED_LAYER_ID = "kfm-fema-record-selected";
const shown = new WeakMap<MapLibreMap, FeatureCollection>();

/** The county choropleth (or nothing, for null), under the site's own overlays and labels, with the picked county outlined. */
export function syncFemaRecord(map: MapLibreMap, collection: FeatureCollection | null, selected: string | null = null): void {
  if (!collection) {
    for (const id of [FEMA_RECORD_SELECTED_LAYER_ID, FEMA_RECORD_LINE_LAYER_ID, FEMA_RECORD_FILL_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(FEMA_RECORD_SOURCE_ID)) map.removeSource(FEMA_RECORD_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const source = map.getSource(FEMA_RECORD_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(FEMA_RECORD_SOURCE_ID, { type: "geojson", data: collection });
  else if (shown.get(map) !== collection) source.setData(collection);
  shown.set(map, collection);
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(FEMA_RECORD_SOURCE_ID))?.id;
  if (!map.getLayer(FEMA_RECORD_FILL_LAYER_ID)) map.addLayer({ id: FEMA_RECORD_FILL_LAYER_ID, type: "fill", source: FEMA_RECORD_SOURCE_ID,
    paint: { "fill-color": ["get", "color"] as never, "fill-opacity": 0.86 } }, before);
  if (!map.getLayer(FEMA_RECORD_LINE_LAYER_ID)) map.addLayer({ id: FEMA_RECORD_LINE_LAYER_ID, type: "line", source: FEMA_RECORD_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#4a3a28", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 0.5, 9, 1.2] as never, "line-opacity": 0.6 } }, before);
  if (!map.getLayer(FEMA_RECORD_SELECTED_LAYER_ID)) map.addLayer({ id: FEMA_RECORD_SELECTED_LAYER_ID, type: "line", source: FEMA_RECORD_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#111111", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 2.4, 9, 3.8] as never } }, before);
  map.setFilter(FEMA_RECORD_SELECTED_LAYER_ID, ["==", ["get", "geoid"], selected ?? ""] as never);
}

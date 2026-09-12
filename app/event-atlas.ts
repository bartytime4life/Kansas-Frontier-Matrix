import type { FeatureCollection, Polygon } from "geojson";

export const EVENT_BOUNDS = [-102.2, 36.8, -94.4, 40.2] as const;
export const EVENT_EARLIEST_DAY = "1800-01-01";
export const EVENT_MAX_HOURS = 24;
export const RADAR_STEP_MS = 300_000;
export type RadarProduct = "n0r" | "n0q";
export type RadarScan = { time: string; product: RadarProduct; artifact: string };
export type SmokeProperties = { start: string; end: string; startMs: number; endMs: number; density: "Light" | "Medium" | "Heavy" | "NA"; satellite: string; artifact: string; featureId?: string };
export type SmokeCollection = FeatureCollection<Polygon, SmokeProperties>;
export type EventManifest = {
  format: "kfm-event-atlas-v1"; start: string; end: string; retrievedAt: string;
  radar: { state: string; scans: RadarScan[]; gaps: string[]; message: string };
  smoke: { state: string; data: SmokeCollection; gaps: string[]; message: string };
  imagery: { dates: string[]; message: string };
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
};
export type EventHourSlot = Readonly<{ hour: number; start: string; end: string }>;
export type EventHourAvailability = EventHourSlot & Readonly<{
  radar: boolean;
  smoke: boolean;
  river: boolean;
  supported: boolean;
}>;

export function exactUtc(value: string): string | null {
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.000)?Z$/.test(value)) return null;
  const ms = Date.parse(value);
  if (!Number.isFinite(ms)) return null;
  const iso = new Date(ms).toISOString();
  return iso.replace(".000Z", "Z") === value.replace(".000Z", "Z") ? iso : null;
}

/** Accept only a real UTC calendar day.  Date-only values are deliberately
 * kept separate from local-time parsing so a calendar selection cannot drift
 * across a daylight-saving transition. */
export function eventDay(value: string): string | null {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return null;
  const timestamp = `${value}T00:00:00.000Z`;
  const ms = Date.parse(timestamp);
  if (!Number.isFinite(ms) || new Date(ms).toISOString().slice(0, 10) !== value) return null;
  return value;
}

export function eventDayStart(value: string): string | null {
  const day = eventDay(value);
  return day ? `${day}T00:00:00.000Z` : null;
}

export function advanceEventDay(value: string, days: number): string | null {
  const start = eventDayStart(value);
  if (!start || !Number.isInteger(days)) return null;
  return new Date(Date.parse(start) + days * 86_400_000).toISOString().slice(0, 10);
}

/** Sunday-through-Saturday UTC week containing the requested calendar day. */
export function eventWeekDays(value: string): readonly string[] {
  const start = eventDayStart(value);
  if (!start) return Object.freeze([]);
  const startMs = Date.parse(start);
  const weekStart = startMs - new Date(startMs).getUTCDay() * 86_400_000;
  return Object.freeze(Array.from({ length: 7 }, (_, offset) => (
    new Date(weekStart + offset * 86_400_000).toISOString().slice(0, 10)
  )));
}

/** Always returns every hour in a valid UTC day.  A data gap never removes a
 * slot from the calendar; availability is resolved separately. */
export function eventDayHours(value: string): readonly EventHourSlot[] {
  const start = eventDayStart(value);
  if (!start) return Object.freeze([]);
  const startMs = Date.parse(start);
  return Object.freeze(Array.from({ length: EVENT_MAX_HOURS }, (_, hour) => Object.freeze({
    hour,
    start: new Date(startMs + hour * 3_600_000).toISOString(),
    end: new Date(startMs + (hour + 1) * 3_600_000).toISOString(),
  })));
}

export function eventInterval(start: string, hours: number, now = Date.now()) {
  const from = exactUtc(start);
  if (!from || ![1, 6, 24].includes(hours) || Date.parse(from) < Date.parse(`${EVENT_EARLIEST_DAY}T00:00:00Z`) || Date.parse(from) >= now) throw new Error("Choose a valid UTC start since 1800 and a 1, 6, or 24 hour interval, not in the future.");
  const end = new Date(Math.min(Date.parse(from) + hours * 3_600_000, now)).toISOString();
  if (Date.parse(end) <= Date.parse(from)) throw new Error("The interval must contain past time.");
  return { start: from, end };
}

export function intervalDays(start: string, end: string): string[] {
  const days: string[] = [];
  for (let t = Date.parse(start.slice(0, 10) + "T00:00:00Z"); t < Date.parse(end); t += 86_400_000) days.push(new Date(t).toISOString().slice(0, 10));
  return days;
}

export function radarProduct(time: string): RadarProduct { return time < "2011-02-16" ? "n0r" : "n0q"; }
export function radarDirectory(day: string): string { return `https://mesonet.agron.iastate.edu/archive/data/${day.replaceAll("-", "/")}/GIS/uscomp/`; }

// The radar.py list service can synthesize scheduled times. Admit only actual
// timestamped artifact names found in the source archive directory instead.
export function parseRadarDirectory(html: string, day: string, start: string, end: string): RadarScan[] {
  const matches = html.matchAll(/href=["'](n0[rq]_(\d{12})\.png)["']/g);
  const scans = new Map<string, RadarScan>();
  for (const match of matches) {
    const stamp = match[2];
    const time = exactUtc(`${stamp.slice(0,4)}-${stamp.slice(4,6)}-${stamp.slice(6,8)}T${stamp.slice(8,10)}:${stamp.slice(10,12)}:00Z`);
    if (!time || !time.startsWith(day) || time < start || time >= end || new Date(time).getUTCMinutes() % 5 !== 0) continue;
    const product = match[1].slice(0, 3) as RadarProduct;
    if (product !== radarProduct(time)) continue;
    scans.set(time, { time, product, artifact: radarDirectory(day) + match[1] });
  }
  return [...scans.values()].sort((a,b) => a.time.localeCompare(b.time));
}

export function radarAt(scans: readonly RadarScan[], cursor: string): RadarScan | null {
  const ms = Date.parse(cursor);
  return [...scans].reverse().find((scan) => Date.parse(scan.time) <= ms && ms < Date.parse(scan.time) + RADAR_STEP_MS) ?? null;
}

export function hmsTime(value: string): string | null {
  const match = value.match(/^(\d{4})(\d{3}) (\d{2})(\d{2})(?:UTC)?$/);
  if (!match) return null;
  const [, y, day, hour, minute] = match;
  const year = Number(y), ordinal = Number(day);
  const days = (Date.UTC(year + 1,0,1) - Date.UTC(year,0,1)) / 86_400_000;
  if (ordinal < 1 || ordinal > days || Number(hour) > 23 || Number(minute) > 59) return null;
  return new Date(Date.UTC(year,0,ordinal,Number(hour),Number(minute))).toISOString();
}

export function smokeUrl(day: string): string { return `https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/KML/${day.slice(0,4)}/${day.slice(5,7)}/hms_smoke${day.replaceAll("-", "")}.kml`; }

// Deliberately not a general KML renderer. Never execute description HTML,
// external styles, NetworkLinks, icons, or overlays from upstream KML.
export function parseSmokeKml(kml: string, artifact: string): SmokeCollection {
  if (!/<kml[\s>]/i.test(kml) || /<!DOCTYPE|<!ENTITY/i.test(kml)) throw new Error("Unrecognized NOAA smoke file.");
  const data: SmokeCollection = { type: "FeatureCollection", features: [] };
  let vertices = 0, records = 0;
  for (const match of kml.matchAll(/<Placemark\b[^>]*>([\s\S]*?)<\/Placemark>/g)) {
    if (++records > 2000) throw new Error("Smoke file exceeds the polygon budget.");
    const block = match[1];
    const start = hmsTime(block.match(/Start Time:\s*(\d{7} \d{4})(?:UTC)?/)?.[1] ?? "");
    const end = hmsTime(block.match(/End Time:\s*(\d{7} \d{4})(?:UTC)?/)?.[1] ?? "");
    const density = block.match(/Density:\s*(Light|Medium|Heavy|NA)(?:<|\s)/)?.[1] as SmokeProperties["density"] | undefined;
    if (!start || !end || end <= start || !density) throw new Error("A NOAA smoke record lacks a valid observation interval or density category.");
    const satellite = (block.match(/Satellite:\s*([^<\r\n]{1,80})/)?.[1] ?? "Not supplied").trim();
    const rings: number[][][] = [];
    for (const coordinates of block.matchAll(/<coordinates\b[^>]*>([\s\S]*?)<\/coordinates>/g)) {
      const ring = coordinates[1].trim().split(/\s+/).map((tuple) => {
        const [lng, lat] = tuple.split(",").map(Number);
        if (!Number.isFinite(lng) || !Number.isFinite(lat) || lng < -180 || lng > 180 || lat < -90 || lat > 90) throw new Error("Invalid smoke geometry.");
        if (++vertices > 100_000) throw new Error("Smoke file exceeds the vertex budget.");
        return [lng, lat];
      });
      if (ring.length < 4 || ring[0][0] !== ring.at(-1)![0] || ring[0][1] !== ring.at(-1)![1]) throw new Error("Smoke polygon is not closed.");
      rings.push(ring);
    }
    if (!rings.length || (block.match(/<Polygon\b/g)?.length ?? 0) !== 1) throw new Error("Unsupported smoke geometry.");
    const bounds = rings[0].reduce((b,p) => [Math.min(b[0],p[0]),Math.min(b[1],p[1]),Math.max(b[2],p[0]),Math.max(b[3],p[1])], [Infinity,Infinity,-Infinity,-Infinity]);
    if (bounds[2] < EVENT_BOUNDS[0] || bounds[0] > EVENT_BOUNDS[2] || bounds[3] < EVENT_BOUNDS[1] || bounds[1] > EVENT_BOUNDS[3]) continue;
    data.features.push({ type: "Feature", geometry: { type: "Polygon", coordinates: rings }, properties: { start, end, startMs: Date.parse(start), endMs: Date.parse(end), density, satellite, artifact } });
  }
  return data;
}

export function smokeAt(data: SmokeCollection, cursor: string): SmokeCollection {
  const ms = Date.parse(cursor);
  return { type: "FeatureCollection", features: data.features.filter((f) => f.properties.startMs <= ms && ms < f.properties.endMs) };
}

export function eventFrames(manifest: EventManifest, observations: readonly { observedAt: string }[] = []): string[] {
  const times = new Set([manifest.start, ...manifest.radar.scans.flatMap((scan) => [scan.time, new Date(Date.parse(scan.time) + RADAR_STEP_MS).toISOString()]), ...manifest.smoke.data.features.flatMap((f) => [f.properties.start, f.properties.end]), ...observations.flatMap((o) => [o.observedAt, new Date(Date.parse(o.observedAt) + 30 * 60_000 + 1000).toISOString()])]);
  // Keep every hour navigable even when no provider has a record for it.
  for (let time = Date.parse(manifest.start); time < Date.parse(manifest.end); time += 3_600_000) times.add(new Date(time).toISOString());
  return [...times].filter((t) => t >= manifest.start && t < manifest.end).sort();
}

/**
 * Resolves one full day's calendar ledger from the exact artifacts already
 * admitted into an EventManifest.  It is intentionally a coverage view, not
 * an interpolation: any hour without an overlapping observation stays a gap.
 */
export function eventHourAvailability(
  manifest: Pick<EventManifest, "start" | "end" | "radar" | "smoke">,
  observations: readonly { observedAt: string; value?: number | null }[] = [],
  day = manifest.start.slice(0, 10),
): readonly EventHourAvailability[] {
  const manifestStart = Date.parse(manifest.start);
  const manifestEnd = Date.parse(manifest.end);
  if (!Number.isFinite(manifestStart) || !Number.isFinite(manifestEnd) || manifestEnd <= manifestStart) return Object.freeze([]);
  return Object.freeze(eventDayHours(day).map((slot) => {
    const slotStart = Math.max(Date.parse(slot.start), manifestStart);
    const slotEnd = Math.min(Date.parse(slot.end), manifestEnd);
    const intersectsQuery = slotStart < manifestEnd && slotEnd > manifestStart;
    const radar = intersectsQuery && manifest.radar.scans.some((scan) => {
      const scanStart = Date.parse(scan.time);
      return Number.isFinite(scanStart) && scanStart < slotEnd && scanStart + RADAR_STEP_MS > slotStart;
    });
    const smoke = intersectsQuery && manifest.smoke.data.features.some((feature) => (
      feature.properties.startMs < slotEnd && feature.properties.endMs > slotStart
    ));
    const river = intersectsQuery && observations.some((observation) => {
      const observationStart = Date.parse(observation.observedAt);
      return typeof observation.value === "number" && Number.isFinite(observation.value)
        && Number.isFinite(observationStart)
        && observationStart < slotEnd
        && observationStart + 30 * 60_000 > slotStart;
    });
    return Object.freeze({ ...slot, radar, smoke, river, supported: radar || smoke || river });
  }));
}

export const GIBS_LAYER = "MODIS_Terra_CorrectedReflectance_TrueColor";
export function imageryTiles(day: string) { return `https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/${GIBS_LAYER}/default/${day}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpeg`; }
export function imageryDomainUrl(day: string) { return `https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/1.0.0/${GIBS_LAYER}/default/GoogleMapsCompatible_Level9/all/${day}--${day}.xml`; }
export function domainIncludes(xml: string, day: string): boolean {
  const domain = xml.match(/<(?:\w+:)?Domain\b[^>]*>([\s\S]*?)<\/(?:\w+:)?Domain>/)?.[1] ?? "";
  return domain.trim().split(",").some((value) => {
    const [start, end, step] = value.trim().split("/");
    return end ? step === "P1D" && start <= day && day <= end : start === day;
  });
}

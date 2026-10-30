import { boundedFetch } from "./api/event-atlas/upstream";
import { validDate, type Station } from "./growing-degree-days";

const STATIONS_URL = "https://mesonet.agron.iastate.edu/geojson/network/KS_ASOS.geojson";
const DAY_MS = 86_400_000;
let stationList: { at: number; stations: Station[] } | null = null;
let pending: Promise<Station[]> | null = null;

/** Validate IEM's network identity, geometry, archive bounds and station timezone. */
export function parseKansasStations(data: unknown): Station[] {
  if (!data || typeof data !== "object") throw new Error("Invalid station network.");
  const collection = data as { type?: unknown; features?: unknown };
  if (collection.type !== "FeatureCollection" || !Array.isArray(collection.features)) throw new Error("Invalid station network.");
  const stations: Station[] = [], ids = new Set<string>();
  for (const feature of collection.features) {
    if (!feature || typeof feature !== "object") continue;
    const f = feature as { properties?: Record<string, unknown>; geometry?: { type?: unknown; coordinates?: unknown } };
    const props = f.properties, coords = f.geometry?.coordinates;
    if (!props || f.geometry?.type !== "Point" || !Array.isArray(coords)) continue;
    const [lon, lat] = coords, id = props.sid;
    if (typeof id !== "string" || !/^[A-Z0-9]{3,5}$/.test(id) || props.network !== "KS_ASOS" || props.state !== "KS"
      || typeof lon !== "number" || !Number.isFinite(lon) || lon < -103 || lon > -94
      || typeof lat !== "number" || !Number.isFinite(lat) || lat < 36 || lat > 41
      || !validDate(props.archive_begin) || !(props.archive_end === null || validDate(props.archive_end))
      || (props.archive_end !== null && props.archive_end < props.archive_begin)
      || !["America/Chicago", "America/Denver"].includes(String(props.tzname))) continue;
    if (ids.has(id)) throw new Error("Duplicate station identifier.");
    ids.add(id);
    stations.push({ id, name: typeof props.sname === "string" ? props.sname : id, lon, lat, tzname: String(props.tzname), archiveBegin: props.archive_begin, archiveEnd: props.archive_end as string | null });
  }
  if (stations.length === 0) throw new Error("No valid stations in the network.");
  return stations;
}

/** Cache the catalog, not a year-filtered projection. Closed stations remain valid for historical years. */
export async function kansasStations(start = "0000-01-01", end = "9999-12-31"): Promise<Station[]> {
  if (!stationList || Date.now() - stationList.at >= DAY_MS) {
    if (!pending) pending = boundedFetch(STATIONS_URL, 512 * 1024, { timeoutMs: 15_000 })
      .then(response => parseKansasStations(JSON.parse(response.text())))
      .then(stations => { stationList = { at: Date.now(), stations }; return stations; })
      .finally(() => { pending = null; });
    await pending;
  }
  return stationList!.stations.filter(station => station.archiveBegin! <= end && (station.archiveEnd === null || station.archiveEnd! >= start));
}

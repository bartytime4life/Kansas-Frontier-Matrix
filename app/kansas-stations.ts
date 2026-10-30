import { boundedFetch } from "./api/event-atlas/upstream";
import type { Station } from "./growing-degree-days";

/** The Kansas ASOS stations of the Iowa Environmental Mesonet network, with their identifiers and positions, kept a day. */
const STATIONS_URL = "https://mesonet.agron.iastate.edu/geojson/network/KS_ASOS.geojson";
const MAX_BYTES = 512 * 1024;
const DAY_MS = 24 * 60 * 60 * 1000;
let stationList: { at: number; stations: Station[] } | null = null;

export async function kansasStations(): Promise<Station[]> {
  if (stationList && Date.now() - stationList.at < DAY_MS) return stationList.stations;
  const data = JSON.parse((await boundedFetch(STATIONS_URL, MAX_BYTES, { timeoutMs: 15_000 })).text()) as { features?: unknown };
  const stations: Station[] = [];
  for (const feature of Array.isArray(data.features) ? data.features : []) {
    const f = feature as { properties?: { sid?: unknown; sname?: unknown }; geometry?: { coordinates?: unknown } };
    const [lon, lat] = Array.isArray(f.geometry?.coordinates) ? f.geometry.coordinates : [];
    const id = f.properties?.sid;
    if (typeof id !== "string" || !/^[A-Za-z0-9]{3,5}$/.test(id) || typeof lon !== "number" || typeof lat !== "number") continue;
    stations.push({ id, name: typeof f.properties?.sname === "string" ? f.properties.sname : id, lon, lat });
  }
  if (stations.length === 0) throw new Error("No stations in the network.");
  stationList = { at: Date.now(), stations };
  return stations;
}

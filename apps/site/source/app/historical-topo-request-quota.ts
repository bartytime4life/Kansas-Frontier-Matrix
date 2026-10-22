import { topoOverlayPrefix } from "./historical-topo-overlay";
import { topoBucket, topoCatalogSheet, topoJson, TopoOverlayError } from "./historical-topo-overlay-server";

// Every acquisition, including failed lookups, retains its slot for the UTC day.
// Cached successful IDs can be retried without another acquisition or charge.
const DAILY_REQUEST_LIMIT = 10;
type RequestRecord = { version: 1; id: number; scanId: number; name: string; year: number; scale: number; state: "KS"; footprint: number[][][]; requestedAt: string };
type Entry = { id: number; token: string; record?: RequestRecord };
type Quota = { count: number; requests: Entry[] };
const invalid = () => new TopoOverlayError("Historical map request accounting is unavailable.", 503);
const integer = (value: unknown, min: number, max: number): value is number => typeof value === "number" && Number.isInteger(value) && value >= min && value <= max;

function validRecord(value: unknown, id: number): value is RequestRecord {
  if (!value || typeof value !== "object") return false;
  const r = value as Partial<RequestRecord>, ring = r.footprint?.[0];
  return r.version === 1 && r.id === id && integer(r.scanId, 1, 1e10) && r.state === "KS"
    && typeof r.name === "string" && r.name.length > 0 && r.name.length <= 120
    && integer(r.year, 1800, 2100) && integer(r.scale, 1, 1e7)
    && typeof r.requestedAt === "string" && Number.isFinite(Date.parse(r.requestedAt))
    && Array.isArray(r.footprint) && r.footprint.length === 1 && Array.isArray(ring) && ring.length === 5
    && ring.every(p => Array.isArray(p) && p.length === 2 && Number.isFinite(p[0]) && Math.abs(p[0]) <= 180 && Number.isFinite(p[1]) && Math.abs(p[1]) <= 90)
    && ring[0][0] === ring[4][0] && ring[0][1] === ring[4][1];
}

function parseQuota(value: unknown): Quota {
  if (!value || typeof value !== "object" || Array.isArray(value)) throw invalid();
  const q = value as Partial<Quota>;
  // Existing count-only records keep their consumed capacity; never reset them.
  if (!integer(q.count, 0, DAILY_REQUEST_LIMIT) || (q.requests !== undefined && !Array.isArray(q.requests))) throw invalid();
  const requests = q.requests ?? [];
  if (requests.length > q.count || new Set(requests.map(e => e?.id)).size !== requests.length
    || requests.some(e => !e || !integer(e.id, 1, 1e10) || typeof e.token !== "string" || !/^[0-9a-f-]{36}$/.test(e.token)
      || (e.record !== undefined && !validRecord(e.record, e.id)))) throw invalid();
  return { count: q.count, requests };
}

async function changeQuota<T>(key: string, change: (quota: Quota) => { value: T; write: boolean }): Promise<T> {
  const bucket = topoBucket();
  // Bound contention work as well as provider work. Failed CAS never authorizes a lookup.
  for (let attempt = 0; attempt < 32; attempt++) {
    const stored = await bucket.get(key);
    let quota: Quota = { count: 0, requests: [] };
    if (stored) {
      if (!integer(stored.size, 1, 16_384) || typeof stored.etag !== "string" || !stored.etag) throw invalid();
      const bytes = await stored.arrayBuffer();
      if (bytes.byteLength !== stored.size) throw invalid();
      quota = parseQuota(topoJson(bytes));
    }
    const result = change(quota);
    if (!result.write) return result.value;
    const written = await bucket.put(key, new TextEncoder().encode(JSON.stringify(quota)).buffer as ArrayBuffer, {
      httpMetadata: { contentType: "application/json" },
      onlyIf: stored ? { etagMatches: stored.etag } : { etagDoesNotMatch: "*" },
    });
    if (written) return result.value;
  }
  throw new TopoOverlayError("Historical map requests are busy. Please retry shortly.", 429);
}

export async function topoCatalogRequest(requester: string, id: number): Promise<RequestRecord> {
  if (!integer(id, 1, 1e10)) throw new TopoOverlayError("Invalid historical sheet ID.");
  const key = `${topoOverlayPrefix}/requesters/${requester}/${new Date().toISOString().slice(0, 10)}.json`;
  const token = crypto.randomUUID();
  const cached = await changeQuota<RequestRecord | undefined>(key, quota => {
    const entry = quota.requests.find(e => e.id === id);
    if (entry?.record) return { value: entry.record, write: false };
    if (entry) throw new TopoOverlayError("This historical map request is in progress. Please retry shortly.", 429);
    if (quota.count >= DAILY_REQUEST_LIMIT) throw new TopoOverlayError("Daily historical map request limit reached. Try again tomorrow.", 429);
    quota.count++;
    quota.requests.push({ id, token });
    return { value: undefined, write: true };
  });
  if (cached) return cached;
  try {
    const sheet = await topoCatalogSheet(id);
    const points = sheet.footprint.geometry.coordinates.flat();
    const west = Math.min(...points.map(p => p[0])), east = Math.max(...points.map(p => p[0]));
    const south = Math.min(...points.map(p => p[1])), north = Math.max(...points.map(p => p[1]));
    const record: RequestRecord = { version: 1, id: sheet.id, scanId: sheet.scanId, name: sheet.name, year: sheet.year, scale: sheet.scale,
      state: "KS", footprint: [[[west, south], [east, south], [east, north], [west, north], [west, south]]], requestedAt: new Date().toISOString() };
    if (!validRecord(record, id)) throw invalid();
    // Cache the immutable request before queue creation, so an uncertain queue
    // write can be retried without repeating USGS work or changing requestedAt.
    await changeQuota(key, quota => {
      const entry = quota.requests.find(e => e.id === id && e.token === token);
      if (!entry) throw invalid();
      entry.record = record;
      return { value: undefined, write: true };
    });
    return record;
  } finally {
    try {
      await changeQuota(key, quota => {
        const index = quota.requests.findIndex(e => e.id === id && e.token === token && !e.record);
        if (index < 0) return { value: undefined, write: false };
        quota.requests.splice(index, 1);
        return { value: undefined, write: true };
      });
    } catch {
      // An interrupted/uncertain reservation remains charged and fails closed.
      console.error("KFM_HISTORICAL_TOPO_RESERVATION_HELD");
    }
  }
}

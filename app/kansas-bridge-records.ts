/** Site-only external context. These reads do not acquire or release a KFM dataset. */
export const BRIDGE_FILTERS = {
  "kdot-bridges-state": { service: "State_Bridges", where: "1=1" },
  "kdot-bridges-local": { service: "Non_State_Bridges", where: "1=1" },
  "kdot-bridges-historic": { service: "Non_State_Bridges", where: "HISTSIGN IN ('Br eligible for NRHP','Br on Natl Reg Hist Place')" },
  "kdot-bridges-old": { service: "Non_State_Bridges", where: "YEARBUILT >= 1800 AND YEARBUILT < 1950" },
  "kdot-bridges-closed": { service: "Non_State_Bridges", where: "OPPOSTCL='Closed to all traffic'" },
} as const;
export type BridgeLayerId = keyof typeof BRIDGE_FILTERS;
export function isBridgeLayer(value: string): value is BridgeLayerId { return Object.hasOwn(BRIDGE_FILTERS, value); }
export type BridgeSearch = { layer: BridgeLayerId; longitude: number; latitude: number; radius: number };
export type BridgeRecord = {
  objectId: number; name: string; coordinates: [number, number]; distanceMeters: number;
  facility: string | null; crossing: string | null; location: string | null; county: string | null;
  builtYear: number | null; reconstructedYear: number | null; recordedStatus: string | null;
  historicDesignation: string | null; inspectionDate: string | null; previousInspectionDate: string | null;
  modifiedDate: string | null; sourceUrl: string;
};
export type BridgeResult = {
  state: "ready" | "partial" | "empty"; records: BridgeRecord[]; query: BridgeSearch;
  retrievedAt: string; partial: boolean; omittedRecords: number; sourceUrl: string;
  providerCount?: number; pagesRead?: number;
  role: "EXTERNAL_CONTEXT_ONLY";
};
export const BRIDGE_RECORD_LIMIT = 50;
export const BRIDGE_PAGE_LIMIT = 5;
export const BRIDGE_TOTAL_LIMIT = BRIDGE_RECORD_LIMIT * BRIDGE_PAGE_LIMIT;
const STRUCTURES = "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures";
export function bridgeLayerUrl(layer: BridgeLayerId): string { return `${STRUCTURES}/${BRIDGE_FILTERS[layer].service}/MapServer/0`; }
function inKansasView(lng: number, lat: number) { return Number.isFinite(lng) && Number.isFinite(lat) && lng >= -102.06 && lng <= -94.58 && lat >= 36.99 && lat <= 40.01; }
export function parseBridgeSearch(url: string): BridgeSearch {
  const p = new URL(url).searchParams;
  if ([...p.keys()].some(k => !["layer", "longitude", "latitude", "radius"].includes(k)) || [...p.keys()].some(k => p.getAll(k).length !== 1)) throw new Error("Invalid query.");
  const layer = p.get("layer") ?? "", longitude = Number(p.get("longitude")), latitude = Number(p.get("latitude")), radius = Number(p.get("radius"));
  if (!isBridgeLayer(layer) || !inKansasView(longitude, latitude) || ![100, 500, 1000].includes(radius)) throw new Error("Choose a Kansas map center and bounded radius.");
  return { layer, longitude, latitude, radius };
}
export function bridgeProviderUrl(query: BridgeSearch, offset = 0): string {
  if (!Number.isInteger(offset) || offset < 0 || offset >= BRIDGE_TOTAL_LIMIT || offset % BRIDGE_RECORD_LIMIT !== 0) throw new Error("Invalid bridge page.");
  const state = query.layer === "kdot-bridges-state";
  const fields = state ? "OBJECTID,STR_NAME,FACILITY,FEATINT,LOCATION,COUNTYNAME,BUILT_DATE,OPPOSTCL,MODIFIED_DATE" : "OBJECTID,BRKEY,STRUCT_NUM,FIPS_STATE,FACILITY,FEATINT,LOCATION,COUNTY,YEARBUILT,YEARRECON,INSPDATE,LASTINSP,OPPOSTCL,HISTSIGN";
  const url = new URL(`${bridgeLayerUrl(query.layer)}/query`);
  url.search = new URLSearchParams({ f: "json", where: BRIDGE_FILTERS[query.layer].where,
    geometry: JSON.stringify({ x: query.longitude, y: query.latitude, spatialReference: { wkid: 4326 } }),
    geometryType: "esriGeometryPoint", inSR: "4326", outSR: "4326", spatialRel: "esriSpatialRelIntersects",
    distance: String(query.radius), units: "esriSRUnit_Meter", returnGeometry: "true",
    outFields: fields, orderByFields: "OBJECTID", resultRecordCount: String(BRIDGE_RECORD_LIMIT), resultOffset: String(offset),
  }).toString();
  return url.href;
}
export function bridgeProviderCountUrl(query: BridgeSearch): string {
  const url = new URL(bridgeProviderUrl(query));
  for (const key of ["outFields", "orderByFields", "resultRecordCount", "resultOffset"]) url.searchParams.delete(key);
  url.searchParams.set("returnGeometry", "false");
  url.searchParams.set("returnCountOnly", "true");
  return url.href;
}
export function parseBridgeCount(raw: unknown): number {
  if (!raw || typeof raw !== "object" || "error" in raw) throw new Error("Invalid provider count.");
  const count = (raw as { count?: unknown }).count;
  if (!Number.isSafeInteger(count) || (count as number) < 0) throw new Error("Invalid provider count.");
  return count as number;
}
const text = (value: unknown) => typeof value === "string" && value.trim() && value.length <= 250 ? value.trim() : null;
const year = (value: unknown) => typeof value === "number" && Number.isInteger(value) && value >= 1800 && value <= new Date().getUTCFullYear() ? value : null;
const date = (value: unknown) => typeof value === "number" && Number.isFinite(value) && value >= Date.UTC(1900, 0, 1) && value <= Date.now() ? new Date(value).toISOString().slice(0, 10) : null;
export function bridgeDistance(lng: number, lat: number, query: BridgeSearch): number {
  const rad = Math.PI / 180, dLat = (lat - query.latitude) * rad, dLng = (lng - query.longitude) * rad;
  const a = Math.sin(dLat / 2) ** 2 + Math.cos(lat * rad) * Math.cos(query.latitude * rad) * Math.sin(dLng / 2) ** 2;
  return 6371008.8 * 2 * Math.asin(Math.min(1, Math.sqrt(a)));
}
export function parseBridgeRecords(raw: unknown, query: BridgeSearch): BridgeResult {
  if (!raw || typeof raw !== "object") throw new Error("Invalid provider response.");
  const body = raw as { error?: unknown; features?: unknown[]; geometryType?: string; spatialReference?: { wkid?: number; latestWkid?: number }; exceededTransferLimit?: unknown };
  if (body.error || !Array.isArray(body.features) || body.features.length > BRIDGE_RECORD_LIMIT || body.geometryType !== "esriGeometryPoint" || (body.spatialReference?.latestWkid ?? body.spatialReference?.wkid) !== 4326 || (body.exceededTransferLimit !== undefined && typeof body.exceededTransferLimit !== "boolean")) throw new Error("Invalid provider response.");
  const records: BridgeRecord[] = [], ids = new Set<number>(); let omittedRecords = 0;
  for (const feature of body.features) {
    const f = feature as { attributes?: Record<string, unknown>; geometry?: { x?: number; y?: number } } | null;
    const a = f?.attributes, x = f?.geometry?.x, y = f?.geometry?.y;
    if (!a || typeof a.OBJECTID !== "number" || !Number.isSafeInteger(a.OBJECTID) || a.OBJECTID < 0 || typeof x !== "number" || typeof y !== "number" || !inKansasView(x, y)) { omittedRecords++; continue; }
    if (ids.has(a.OBJECTID)) throw new Error("Duplicate provider identity.");
    ids.add(a.OBJECTID);
    const state = query.layer === "kdot-bridges-state", distance = bridgeDistance(x, y, query);
    const builtYear = year(state ? a.BUILT_DATE : a.YEARBUILT);
    if (distance > query.radius + 2 || (!state && a.FIPS_STATE !== "KANSAS") ||
        (query.layer === "kdot-bridges-old" && (builtYear === null || builtYear >= 1950)) ||
        (query.layer === "kdot-bridges-closed" && a.OPPOSTCL !== "Closed to all traffic") ||
        (query.layer === "kdot-bridges-historic" && !["Br eligible for NRHP", "Br on Natl Reg Hist Place"].includes(String(a.HISTSIGN)))) { omittedRecords++; continue; }
    records.push({ objectId: a.OBJECTID, name: text(state ? a.STR_NAME : a.BRKEY) ?? `KDOT object ${a.OBJECTID}`,
      coordinates: [x, y], distanceMeters: Math.round(distance), facility: text(a.FACILITY), crossing: text(a.FEATINT), location: text(a.LOCATION),
      county: text(state ? a.COUNTYNAME : a.COUNTY), builtYear, reconstructedYear: state ? null : year(a.YEARRECON),
      recordedStatus: text(a.OPPOSTCL), historicDesignation: state ? null : text(a.HISTSIGN),
      inspectionDate: state ? null : date(a.INSPDATE), previousInspectionDate: state ? null : date(a.LASTINSP),
      modifiedDate: state ? text(a.MODIFIED_DATE) : null, sourceUrl: `${bridgeLayerUrl(query.layer)}/query?objectIds=${a.OBJECTID}&outFields=*&returnGeometry=false&f=pjson` });
  }
  records.sort((a, b) => a.distanceMeters - b.distanceMeters || a.objectId - b.objectId);
  const partial = body.exceededTransferLimit === true || body.features.length === BRIDGE_RECORD_LIMIT || omittedRecords > 0;
  return { state: partial ? "partial" : records.length ? "ready" : "empty", records, query, retrievedAt: new Date().toISOString(), partial, omittedRecords, sourceUrl: bridgeLayerUrl(query.layer), role: "EXTERNAL_CONTEXT_ONLY" };
}

/** Combine ordered provider pages without presenting an incomplete capture as complete. */
export function assembleBridgePages(rawPages: unknown[], query: BridgeSearch, providerCount: number): BridgeResult {
  if (!Number.isSafeInteger(providerCount) || providerCount < 0 || rawPages.length > BRIDGE_PAGE_LIMIT ||
      (providerCount > 0 && rawPages.length === 0) || (providerCount === 0 && rawPages.length !== 0)) throw new Error("Invalid bridge page set.");
  let lastId = -1, observed = 0, omittedRecords = 0;
  const records: BridgeRecord[] = [];
  for (const raw of rawPages) {
    const body = raw as { features?: unknown[]; exceededTransferLimit?: boolean };
    const page = parseBridgeRecords(raw, query);
    if (!body.features?.length || observed + body.features.length > BRIDGE_TOTAL_LIMIT) throw new Error("Invalid bridge page set.");
    for (const feature of body.features) {
      const id = (feature as { attributes?: { OBJECTID?: unknown } } | null)?.attributes?.OBJECTID;
      if (!Number.isSafeInteger(id) || (id as number) <= lastId) throw new Error("Bridge pages changed or overlapped.");
      lastId = id as number;
    }
    observed += body.features.length;
    omittedRecords += page.omittedRecords;
    records.push(...page.records);
    if (body.exceededTransferLimit === true && body.features.length < BRIDGE_RECORD_LIMIT) throw new Error("Provider page was truncated.");
  }
  if (observed > providerCount) throw new Error("Bridge count changed during paging.");
  records.sort((a, b) => a.distanceMeters - b.distanceMeters || a.objectId - b.objectId);
  const partial = observed !== providerCount || omittedRecords > 0;
  return { state: partial ? "partial" : records.length ? "ready" : "empty", records, query,
    retrievedAt: new Date().toISOString(), partial, omittedRecords, sourceUrl: bridgeLayerUrl(query.layer),
    providerCount, pagesRead: rawPages.length, role: "EXTERNAL_CONTEXT_ONLY" };
}

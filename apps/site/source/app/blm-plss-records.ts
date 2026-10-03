/** Bounded Site inspection of provider-current PLSS attributes, not land title. */
export const BLM_PLSS_LAYERS = {
  "blm-plss-townships": { layer: 1, where: "STATEABBR='KS'", fields: "OBJECTID,STATEABBR,PLSSID,TWNSHPLAB,PRINMER,SOURCEDATE,SOURCEREF" },
  "blm-plss-sections": { layer: 2, where: "PLSSID LIKE 'KS%'", fields: "OBJECTID,PLSSID,FRSTDIVID,FRSTDIVTXT,FRSTDIVLAB,SOURCEDATE,SOURCEREF" },
  "blm-plss-intersected": { layer: 3, where: "STATEABBR='KS'", fields: "OBJECTID,STATEABBR,PLSSID,FRSTDIVID,FRSTDIVLAB,SECDIVID,SECDIVTXT,SECDIVLAB,SOURCEDATE,SOURCEREF,REVISEDDATE" },
} as const;
export type BlmPlssLayerId = keyof typeof BLM_PLSS_LAYERS;
export const BLM_PLSS_LIMIT = 10;
const SERVICE = "https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer";
export function isBlmPlssLayer(value: string): value is BlmPlssLayerId { return Object.hasOwn(BLM_PLSS_LAYERS, value); }
export function blmPlssLayerUrl(layer: BlmPlssLayerId): string { return `${SERVICE}/${BLM_PLSS_LAYERS[layer].layer}`; }
export type BlmPlssQuery = { layer: BlmPlssLayerId; longitude: number; latitude: number };
export type BlmPlssRecord = {
  objectId: number; plssId: string; townshipLabel: string | null; principalMeridian: string | null;
  firstDivisionId: string | null; firstDivisionLabel: string | null; firstDivisionType: string | null;
  secondDivisionId: string | null; secondDivisionLabel: string | null; secondDivisionType: string | null;
  sourceDocumentDate: string | null; revisedDate: string | null; sourceReference: string | null;
  officialRecordUrl: string;
};
export type BlmPlssResult = {
  state: "ready" | "partial" | "empty"; query: BlmPlssQuery; records: BlmPlssRecord[];
  providerCount: number; omittedRecords: number; partial: boolean; retrievedAt: string;
  sourceUrl: string; role: "EXTERNAL_CONTEXT_ONLY";
};
/** Manual GLO handoff only: a survey feature is not a matched land record. */
export function gloSearchReference(record: BlmPlssRecord, query: BlmPlssQuery): string | null {
  if (typeof record?.plssId !== "string" || !/^KS[A-Z0-9]{13,14}$/.test(record.plssId) ||
      !inKansas(query?.longitude, query?.latitude)) return null;
  const parts = ["Kansas", `BLM PLSS township ID: ${record.plssId}`];
  if (typeof record.townshipLabel === "string" && /^T\d{1,3}[NS] R\d{1,3}[EW]$/.test(record.townshipLabel))
    parts.push(`BLM township label: ${record.townshipLabel}`);
  if (typeof record.principalMeridian === "string" && /^[A-Za-z0-9 .'-]{1,80}$/.test(record.principalMeridian))
    parts.push(`Principal meridian: ${record.principalMeridian}`);
  if (record.firstDivisionType === "Section" && typeof record.firstDivisionLabel === "string" &&
      /^(?:[1-9]|[12]\d|3[0-6])$/.test(record.firstDivisionLabel))
    parts.push(`BLM section: ${record.firstDivisionLabel}`);
  parts.push(`Map center: ${query.latitude.toFixed(5)}, ${query.longitude.toFixed(5)}`);
  return parts.join(" | ");
}
function inKansas(lng: number, lat: number): boolean {
  return Number.isFinite(lng) && Number.isFinite(lat) && lng >= -102.06 && lng <= -94.58 && lat >= 36.99 && lat <= 40.01;
}
export function parseBlmPlssQuery(url: string): BlmPlssQuery {
  const params = new URL(url).searchParams;
  if ([...params.keys()].some(k => !["layer", "longitude", "latitude"].includes(k) || params.getAll(k).length !== 1)) throw new Error("Invalid PLSS query.");
  const layer = params.get("layer") ?? "", longitude = Number(params.get("longitude")), latitude = Number(params.get("latitude"));
  if (!isBlmPlssLayer(layer) || !inKansas(longitude, latitude)) throw new Error("Choose a Kansas map center and PLSS layer.");
  return { layer, longitude, latitude };
}
export function blmPlssProviderUrl(query: BlmPlssQuery, countOnly = false): string {
  const profile = BLM_PLSS_LAYERS[query.layer], url = new URL(`${blmPlssLayerUrl(query.layer)}/query`);
  url.search = new URLSearchParams({ f: "json", where: profile.where,
    geometry: JSON.stringify({ x: query.longitude, y: query.latitude, spatialReference: { wkid: 4326 } }),
    geometryType: "esriGeometryPoint", inSR: "4326", spatialRel: "esriSpatialRelIntersects",
    returnGeometry: "false", ...(countOnly ? { returnCountOnly: "true" } : {
      outFields: profile.fields, orderByFields: "OBJECTID", resultRecordCount: String(BLM_PLSS_LIMIT), resultOffset: "0",
    }),
  }).toString();
  return url.href;
}
const label = (value: unknown): string | null => typeof value === "string" && value.trim().length > 0 && value.length <= 250 ? value.trim() : null;
const date = (value: unknown): string | null => typeof value === "number" && Number.isSafeInteger(value) && value >= Date.UTC(1800, 0, 1) && value <= Date.now() ? new Date(value).toISOString().slice(0, 10) : null;
export function parseBlmPlssCount(raw: unknown): number {
  if (!raw || typeof raw !== "object" || "error" in raw) throw new Error("Invalid BLM count.");
  const value = (raw as { count?: unknown }).count;
  if (!Number.isSafeInteger(value) || (value as number) < 0) throw new Error("Invalid BLM count.");
  return value as number;
}
export function parseBlmPlssRecords(raw: unknown, query: BlmPlssQuery, providerCount: number): BlmPlssResult {
  if (!Number.isSafeInteger(providerCount) || providerCount < 0 || !raw || typeof raw !== "object") throw new Error("Invalid BLM response.");
  const body = raw as { error?: unknown; features?: unknown[]; exceededTransferLimit?: unknown; geometryType?: string };
  if (body.error || !Array.isArray(body.features) || body.features.length > BLM_PLSS_LIMIT ||
      (body.exceededTransferLimit !== undefined && typeof body.exceededTransferLimit !== "boolean") ||
      (body.geometryType !== undefined && body.geometryType !== "esriGeometryPolygon")) throw new Error("Invalid BLM response.");
  const records: BlmPlssRecord[] = [];
  let lastId = -1, omittedRecords = 0;
  for (const feature of body.features) {
    const attributes = (feature as { attributes?: Record<string, unknown> } | null)?.attributes;
    const objectId = attributes?.OBJECTID, plssId = label(attributes?.PLSSID);
    if (!Number.isSafeInteger(objectId) || (objectId as number) <= lastId) throw new Error("BLM identities were missing or unordered.");
    lastId = objectId as number;
    if (!plssId?.startsWith("KS") || (query.layer !== "blm-plss-sections" && attributes?.STATEABBR !== "KS")) { omittedRecords++; continue; }
    records.push({ objectId: objectId as number, plssId,
      townshipLabel: label(attributes?.TWNSHPLAB), principalMeridian: label(attributes?.PRINMER),
      firstDivisionId: label(attributes?.FRSTDIVID), firstDivisionLabel: label(attributes?.FRSTDIVLAB), firstDivisionType: label(attributes?.FRSTDIVTXT),
      secondDivisionId: label(attributes?.SECDIVID), secondDivisionLabel: label(attributes?.SECDIVLAB), secondDivisionType: label(attributes?.SECDIVTXT),
      sourceDocumentDate: date(attributes?.SOURCEDATE), revisedDate: date(attributes?.REVISEDDATE), sourceReference: label(attributes?.SOURCEREF),
      officialRecordUrl: `${blmPlssLayerUrl(query.layer)}/query?objectIds=${objectId}&outFields=*&returnGeometry=false&f=pjson`,
    });
  }
  if (body.features.length > providerCount || (body.exceededTransferLimit === true && body.features.length < BLM_PLSS_LIMIT)) throw new Error("BLM count or page changed.");
  const partial = body.features.length !== providerCount || omittedRecords > 0 || body.exceededTransferLimit === true;
  return { state: partial ? "partial" : records.length ? "ready" : "empty", query, records, providerCount, omittedRecords, partial,
    retrievedAt: new Date().toISOString(), sourceUrl: blmPlssLayerUrl(query.layer), role: "EXTERNAL_CONTEXT_ONLY" };
}

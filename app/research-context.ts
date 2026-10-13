/** Browser research context. This is a display projection, never an EvidenceBundle. */
export const RESEARCH_RADII = [25, 50, 100, 200] as const;
export type ResearchRadius = typeof RESEARCH_RADII[number];
export type ResearchRecord = Readonly<{
  kind: "registry" | "provider";
  sourceId: string;
  featureId: string;
  title: string;
  coordinates: readonly [number, number];
  sourceTitle: string;
  sourceUrl: string | null;
  sourceTime: string;
  retrievedAt: string | null;
  evidenceLabel: string;
  limitation: string;
}>;
export type ResearchNeighbor = ResearchRecord & Readonly<{ distanceMiles: number }>;
export type ResearchCoverage = Readonly<{
  sourceId: string;
  title: string;
  state: "ready" | "partial" | "empty" | "loading" | "held" | "unavailable" | "not-spatial";
  retrievedAt: string | null;
  limitation: string;
}>;
export type ResearchContext = Readonly<{
  version: 1;
  capturedAt: string;
  anchor: ResearchRecord;
  radiusMiles: ResearchRadius;
  mapTime: string;
  total: number;
  records: readonly ResearchNeighbor[];
  coverage: readonly ResearchCoverage[];
}>;

const object = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const text = (value: unknown, max: number): value is string => typeof value === "string" && value.length > 0 && value.length <= max && !/[\u0000-\u001f\u007f]/.test(value);
const date = (value: unknown): value is string => text(value, 40) && /^\d{4}-\d{2}-\d{2}T/.test(value) && Number.isFinite(Date.parse(value));
const keys = (value: Record<string, unknown>, allowed: string[]) => Object.keys(value).every(key => allowed.includes(key));
export const researchCoordinates = (value: unknown): value is readonly [number, number] => Array.isArray(value) && value.length === 2
  && value.every(item => typeof item === "number" && Number.isFinite(item)) && Math.abs(value[0]) <= 180 && Math.abs(value[1]) <= 90;
export const researchSourceUrl = (value: unknown): string | null => {
  if (typeof value !== "string" || value.length > 2048) return null;
  try { const url = new URL(value); return url.protocol === "https:" && !url.username && !url.password ? url.href : null; } catch { return null; }
};
export const researchIdentity = (record: Pick<ResearchRecord, "kind" | "sourceId" | "featureId">) => JSON.stringify([record.kind, record.sourceId, record.featureId]);
export function chooseResearchAnchor(current: ResearchRecord | null, selected: ResearchRecord | null, startNew = false): ResearchRecord | null {
  const candidate = startNew || !current ? selected : current;
  return validResearchRecord(candidate) ? candidate : null;
}

/** A superseded or canceled renderer read must never replace the current inventory. */
export async function readResearchInventory<T>(load: () => Promise<T>, signal: AbortSignal, accept: (value: T) => void): Promise<void> {
  try { const value = await load(); if (!signal.aborted) accept(value); } catch { /* Missing inventory stays unavailable. */ }
}
export function validResearchRecord(value: unknown): value is ResearchRecord {
  return object(value) && keys(value, ["kind", "sourceId", "featureId", "title", "coordinates", "sourceTitle", "sourceUrl", "sourceTime", "retrievedAt", "evidenceLabel", "limitation", "distanceMiles"]) && ["registry", "provider"].includes(String(value.kind)) && text(value.sourceId, 160) && text(value.featureId, 240)
    && text(value.title, 240) && researchCoordinates(value.coordinates) && text(value.sourceTitle, 240)
    && (value.sourceUrl === null || researchSourceUrl(value.sourceUrl) === value.sourceUrl)
    && text(value.sourceTime, 600) && (value.retrievedAt === null || date(value.retrievedAt))
    && text(value.evidenceLabel, 120) && (value.kind === "provider" ? value.evidenceLabel === "EXTERNAL_CONTEXT_ONLY" : ["ANSWER", "CORRECTED", "GENERALIZED_GEOMETRY"].includes(value.evidenceLabel))
    && (value.distanceMiles === undefined || typeof value.distanceMiles === "number" && Number.isFinite(value.distanceMiles) && value.distanceMiles >= 0)
    && text(value.limitation, 2000);
}
export function validResearchContext(value: unknown): value is ResearchContext {
  if (!object(value) || !keys(value, ["version", "capturedAt", "anchor", "radiusMiles", "mapTime", "total", "records", "coverage"]) || value.version !== 1 || !date(value.capturedAt) || !validResearchRecord(value.anchor)
    || Object.hasOwn(value.anchor, "distanceMiles")
    || !RESEARCH_RADII.includes(value.radiusMiles as ResearchRadius) || !text(value.mapTime, 240)
    || !Number.isSafeInteger(value.total) || Number(value.total) < 0 || Number(value.total) > 100_000
    || !Array.isArray(value.records) || value.records.length > 50 || value.records.length > Number(value.total)
    || !Array.isArray(value.coverage) || value.coverage.length > 100) return false;
  const ids = new Set<string>();
  for (const row of value.records) {
    const distance = object(row) ? row.distanceMiles : undefined;
    if (!validResearchRecord(row) || typeof distance !== "number" || !Number.isFinite(distance)
      || distance < 0 || distance > Number(value.radiusMiles) + 1e-9 || Math.abs(distance - researchDistanceMiles(value.anchor.coordinates, row.coordinates)) > 1e-8
      || researchIdentity(row) === researchIdentity(value.anchor)
      || ids.has(researchIdentity(row))) return false;
    ids.add(researchIdentity(row));
  }
  return value.coverage.every(item => object(item) && keys(item, ["sourceId", "title", "state", "retrievedAt", "limitation"]) && text(item.sourceId, 160) && text(item.title, 240)
    && ["ready", "partial", "empty", "loading", "held", "unavailable", "not-spatial"].includes(String(item.state))
    && (item.retrievedAt === null || date(item.retrievedAt)) && text(item.limitation, 2000));
}

export function researchDistanceMiles(left: readonly [number, number], right: readonly [number, number]): number {
  const radians = Math.PI / 180;
  const a = Math.sin((right[1] - left[1]) * radians / 2) ** 2
    + Math.cos(left[1] * radians) * Math.cos(right[1] * radians) * Math.sin((right[0] - left[0]) * radians / 2) ** 2;
  const bounded = Math.max(0, Math.min(1, a));
  return 3958.8 * 2 * Math.atan2(Math.sqrt(bounded), Math.sqrt(1 - bounded));
}

/** Call with already eligible records from the active time and selected sources. */
export function nearbyResearch(anchor: ResearchRecord, candidates: readonly ResearchRecord[], radiusMiles: ResearchRadius) {
  if (!validResearchRecord(anchor) || !RESEARCH_RADII.includes(radiusMiles)) return { records: [], total: 0 };
  const unique = new Map<string, ResearchNeighbor>();
  for (const candidate of candidates) {
    if (!validResearchRecord(candidate)) continue;
    const key = researchIdentity(candidate);
    if (key === researchIdentity(anchor)) continue;
    const distanceMiles = researchDistanceMiles(anchor.coordinates, candidate.coordinates);
    if (distanceMiles > radiusMiles + 1e-9) continue;
    const previous = unique.get(key);
    // Repeated provider IDs are one record; prefer the newest response deterministically.
    const timestamp = (record: ResearchRecord) => record.retrievedAt ? Date.parse(record.retrievedAt) : 0;
    const tie = (record: ResearchRecord) => JSON.stringify([record.coordinates, record.title, record.sourceTitle, record.sourceUrl, record.sourceTime, record.evidenceLabel, record.limitation]);
    if (!previous || timestamp(candidate) > timestamp(previous)
      || timestamp(candidate) === timestamp(previous) && tie(candidate) < tie(previous)) unique.set(key, { ...candidate, distanceMiles });
  }
  const rows = [...unique.values()].sort((a, b) => a.distanceMiles - b.distanceMiles || (researchIdentity(a) < researchIdentity(b) ? -1 : 1));
  return { records: rows.slice(0, 50), total: rows.length };
}

/** Project only supplied point geometry and stable provider identity; no centroid fallback. */
export function providerResearchPoints(source: { id: string; title: string; url: string; time: string; limitation: string }, payload: unknown,
  eligible: boolean, expectedDay?: string, sourceTime?: (properties: Record<string, unknown>) => string): ResearchRecord[] {
  if (!eligible || !object(payload) || payload.feed !== source.id || !["ready", "partial", "empty"].includes(String(payload.state))
    || !date(payload.retrievedAt) || expectedDay !== undefined && payload.sourceDay !== expectedDay
    || !object(payload.data) || payload.data.type !== "FeatureCollection" || !Array.isArray(payload.data.features)) return [];
  return payload.data.features.flatMap(feature => {
    if (!object(feature) || !object(feature.geometry) || feature.geometry.type !== "Point" || !Array.isArray(feature.geometry.coordinates)
      || !researchCoordinates(feature.geometry.coordinates.slice(0, 2)) || !object(feature.properties)) return [];
    const properties = feature.properties;
    const id = properties.featureId ?? feature.id;
    if (typeof id !== "string" && (typeof id !== "number" || !Number.isFinite(id))) return [];
    const title = [properties.name, properties.name_en, properties.title, properties.place, properties.monitoringLocationId, properties.stationId].find(value => text(value, 240));
    const record: ResearchRecord = {
      kind: "provider", sourceId: source.id, featureId: String(id), title: typeof title === "string" ? title : `${source.title} · ${id}`,
      coordinates: feature.geometry.coordinates.slice(0, 2) as [number, number], sourceTitle: source.title,
      sourceUrl: researchSourceUrl(source.url), sourceTime: sourceTime?.(properties) ?? source.time,
      retrievedAt: payload.retrievedAt as string, evidenceLabel: "EXTERNAL_CONTEXT_ONLY", limitation: source.limitation,
    };
    return validResearchRecord(record) ? [record] : [];
  });
}

/** Never persist a dossier which could reveal the browser-location-derived area. */
export function persistableResearch(context: ResearchContext | null, locationRedacted: boolean, settingsOnly = false): ResearchContext | undefined {
  if (locationRedacted || !validResearchContext(context)) return undefined;
  return JSON.parse(JSON.stringify(settingsOnly ? { ...context, records: [], total: 0 } : context)) as ResearchContext;
}

/** Plain Markdown export: escape provider prose so it cannot introduce HTML or links. */
const md = (value: string) => value.replace(/[&<>]/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" })[char]!).replace(/[\\`*_{}\[\]()#!|]/g, "\\$&");
export function researchMarkdown(context: ResearchContext): string {
  if (!validResearchContext(context)) return "Research context unavailable.";
  return [
    "## Near here · captured research context",
    `Anchor: ${md(context.anchor.title)} · ${context.radiusMiles} miles · captured ${context.capturedAt}`,
    `Map time: ${md(context.mapTime)}. Showing ${context.records.length} of ${context.total} eligible loaded records.`,
    "Provider context is not admitted KFM evidence. Proximity does not establish a relationship or complete coverage.",
    `Anchor source: ${md(context.anchor.sourceTitle)} · ${context.anchor.sourceUrl ? md(context.anchor.sourceUrl) : "No source link supplied"}`,
    ...context.records.map(row => `- ${md(row.title)} · ${row.distanceMiles.toFixed(1)} mi (${row.kind === "registry" ? "registry anchor" : "provider point"}); ${md(row.evidenceLabel)}. Source: ${md(row.sourceTitle)}; ${row.sourceUrl ? md(row.sourceUrl) : "no source link"}. Source time: ${md(row.sourceTime)}. Retrieved: ${row.retrievedAt ?? "not supplied"}. ${md(row.limitation)}`),
    "### Coverage at capture",
    ...context.coverage.map(row => `- ${md(row.title)}: ${row.state}; retrieved ${row.retrievedAt ?? "not supplied"}. ${md(row.limitation)}`),
  ].join("\n\n");
}

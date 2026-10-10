import { readBoundedJson } from "./bounded-json";

export const HISTORY_RESEARCH_MAX_BYTES = 3 * 1024 * 1024;
export const HISTORY_RESEARCH_PAGE_SIZE = 30;
export const HISTORY_RESEARCH_PATH = "/history/people-events.json";
export const HISTORY_RESEARCH_KINDS = ["person", "event", "topic", "organization", "fictional"] as const;
export type HistoryResearchKind = typeof HISTORY_RESEARCH_KINDS[number];
export type HistoryResearchSource = {
  id: string; title: string; publisher: string; url: string;
  access: "readable" | "partial" | "blocked"; accessNote: string; coverage: string;
  rights: string; recordCount: number; completeness: string; checkedAt: string;
};
export type HistoryResearchRecord = {
  id: string; sourceId: string; kind: HistoryResearchKind; title: string; category: string;
  date: string | null; place: string | null; relation: string; sourceUrl: string;
  targetUrl: string; reviewNote: string; themes: string[];
};
export type HistoryResearchCatalog = {
  schemaVersion: 1; checkedAt: string; scope: string; attribution: string;
  lifecycle: { sourceAdmission: "NOT_ADMITTED"; review: "PENDING"; mapActivation: "NONE" };
  sources: HistoryResearchSource[]; records: HistoryResearchRecord[];
};

const object = (value: unknown): value is Record<string, unknown> => !!value && typeof value === "object" && !Array.isArray(value);
const text = (value: unknown, maximum = 6000): value is string => typeof value === "string" && value.trim().length > 0 && value.length <= maximum;
const identifier = (value: unknown): value is string => typeof value === "string" && /^[a-zA-Z0-9][a-zA-Z0-9._:-]{0,199}$/.test(value);
const optionalText = (value: unknown): value is string | null => value === null || text(value, 1000);

/** Links are navigation only. No provider content is fetched or embedded by this browser. */
export function historyResearchUrl(value: unknown): value is string {
  if (!text(value, 4096) || /[\s\\\u0000-\u001f\u007f]/.test(value)) return false;
  try {
    const url = new URL(value);
    const host = url.hostname.toLowerCase().replace(/\.$/, "");
    return (url.protocol === "https:" || url.protocol === "http:") && !url.username && !url.password
      && (!url.port || url.port === "80" || url.port === "443")
      && /^[a-z0-9-]+(?:\.[a-z0-9-]+)+$/.test(host) && !/^\d+(?:\.\d+){3}$/.test(host)
      && !/(?:^|\.)(?:localhost|local|internal|test|invalid|example)$/.test(host);
  } catch { return false; }
}

/** Reject the whole catalogue on a broken reference rather than silently losing attribution. */
export function parseHistoryResearchCatalog(value: unknown): HistoryResearchCatalog | null {
  if (!object(value) || value.schemaVersion !== 1 || !text(value.checkedAt, 100)
    || !text(value.scope) || !text(value.attribution) || !object(value.lifecycle)
    || value.lifecycle.sourceAdmission !== "NOT_ADMITTED" || value.lifecycle.review !== "PENDING" || value.lifecycle.mapActivation !== "NONE"
    || !Array.isArray(value.sources) || !value.sources.length || value.sources.length > 100
    || !Array.isArray(value.records) || value.records.length > 10000) return null;
  const sources: HistoryResearchSource[] = [];
  const sourceIds = new Set<string>();
  for (const source of value.sources) {
    if (!object(source) || !identifier(source.id) || sourceIds.has(source.id) || !text(source.title, 1000)
      || !text(source.publisher, 1000) || !historyResearchUrl(source.url)
      || (source.access !== "readable" && source.access !== "partial" && source.access !== "blocked") || !text(source.accessNote)
      || !text(source.coverage) || !text(source.rights) || !text(source.completeness) || !text(source.checkedAt, 100)
      || !Number.isSafeInteger(source.recordCount) || (source.recordCount as number) < 0) return null;
    sourceIds.add(source.id);
    sources.push(source as HistoryResearchSource);
  }
  const recordIds = new Set<string>();
  const counts = new Map<string, number>();
  const records: HistoryResearchRecord[] = [];
  for (const record of value.records) {
    if (!object(record) || !identifier(record.id) || recordIds.has(record.id) || !identifier(record.sourceId)
      || !sourceIds.has(record.sourceId) || !HISTORY_RESEARCH_KINDS.includes(record.kind as HistoryResearchKind)
      || !text(record.title, 1000) || !text(record.category, 1000) || !optionalText(record.date) || !optionalText(record.place)
      || !text(record.relation) || !historyResearchUrl(record.sourceUrl) || !historyResearchUrl(record.targetUrl)
      || !text(record.reviewNote) || !Array.isArray(record.themes) || record.themes.length > 40
      || !record.themes.every(theme => text(theme, 300))) return null;
    recordIds.add(record.id);
    counts.set(record.sourceId, (counts.get(record.sourceId) ?? 0) + 1);
    records.push(record as HistoryResearchRecord);
  }
  if (sources.some(source => source.recordCount !== (counts.get(source.id) ?? 0))) return null;
  return { schemaVersion: 1, checkedAt: value.checkedAt, scope: value.scope, attribution: value.attribution,
    lifecycle: { sourceAdmission: "NOT_ADMITTED", review: "PENDING", mapActivation: "NONE" }, sources, records };
}

export async function readHistoryResearchCatalog(response: Response, signal?: AbortSignal): Promise<HistoryResearchCatalog> {
  if (!response.ok) throw new Error("The research catalogue is unavailable. Try loading it again.");
  const catalog = parseHistoryResearchCatalog(await readBoundedJson(response, HISTORY_RESEARCH_MAX_BYTES, signal));
  if (!catalog) throw new Error("The research catalogue could not be validated. No entries have been displayed.");
  return catalog;
}

export async function loadHistoryResearchCatalog(signal: AbortSignal): Promise<HistoryResearchCatalog> {
  const response = await fetch(HISTORY_RESEARCH_PATH, { signal, mode: "same-origin", credentials: "same-origin", redirect: "error" });
  return readHistoryResearchCatalog(response, signal);
}

export function filterHistoryResearch(catalog: HistoryResearchCatalog, query: string, sourceId: string, kind: string): HistoryResearchRecord[] {
  const words = query.toLocaleLowerCase("en-US").trim().split(/\s+/).filter(Boolean);
  const sources = new Map(catalog.sources.map(source => [source.id, `${source.title} ${source.publisher}`]));
  return catalog.records.filter(record => (sourceId === "all" || record.sourceId === sourceId)
    && (kind === "all" || record.kind === kind)
    && words.every(word => `${record.title} ${record.category} ${record.date ?? ""} ${record.place ?? ""} ${record.relation} ${record.reviewNote} ${record.themes.join(" ")} ${sources.get(record.sourceId)}`.toLocaleLowerCase("en-US").includes(word)));
}

export function historyResearchKnowledgeLink(title: string): string {
  return `/knowledge?term=${encodeURIComponent(title.slice(0, 80))}`;
}

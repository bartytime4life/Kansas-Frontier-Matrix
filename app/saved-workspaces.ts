export type SavedWorkspaceParseResult = Readonly<{
  records: readonly Record<string, unknown>[];
  rejected: boolean;
}>;

const record = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const text = (value: unknown, limit = 240): value is string => typeof value === "string" && value.length > 0 && value.length <= limit;
const finite = (value: unknown): value is number => typeof value === "number" && Number.isFinite(value);
const stringList = (value: unknown, limit: number): value is string[] => Array.isArray(value) && value.length <= limit && value.every(item => text(item, 160));
const scalarMap = (value: unknown, kind: "boolean" | "number") => record(value)
  && Object.keys(value).length <= 100
  && Object.entries(value).every(([key, item]) => text(key, 160) && (kind === "boolean" ? typeof item === "boolean" : finite(item)));

/** Validate the minimum complete device-local workspace shape before React sees it. */
export const validSavedWorkspaceRecord = (value: unknown): value is Record<string, unknown> => {
  if (!record(value) || !text(value.id) || !text(value.name) || !text(value.savedAt) || !Number.isFinite(Date.parse(value.savedAt))) return false;
  if (!record(value.view) || !Array.isArray(value.view.center) || value.view.center.length !== 2 || !value.view.center.every(finite)
    || !finite(value.view.zoom) || !finite(value.view.bearing) || !finite(value.view.pitch)) return false;
  if (!scalarMap(value.visibility, "boolean") || !scalarMap(value.opacity, "number") || !stringList(value.layerOrder, 100) || !finite(value.year)) return false;
  if (!["standard", "imagery", "midnight", "prairie", "streets", "topo"].includes(String(value.basemap)) || !["mercator", "globe"].includes(String(value.projection))) return false;
  if (!record(value.report) || !text(value.report.title, 180) || !["VIEWPORT", "ANALYSIS_AREA", "VISIBLE_LAYERS", "SELECTION"].includes(String(value.report.scope))
    || !["EXECUTIVE", "STANDARD", "TECHNICAL"].includes(String(value.report.detail)) || !stringList(value.report.layerIds, 100)
    || !record(value.report.sections) || typeof value.report.query !== "string" || value.report.query.length > 500) return false;
  if (value.selection !== null && value.selection !== undefined && (!record(value.selection) || !text(value.selection.layerId, 160) || !text(value.selection.featureId, 240))) return false;
  return true;
};

export const parseSavedWorkspaceList = (raw: string | null, maxItems: number, maxBytes = 2_000_000): SavedWorkspaceParseResult => {
  if (!raw) return { records: Object.freeze([]), rejected: false };
  if (raw.length > maxBytes || !Number.isInteger(maxItems) || maxItems < 1 || maxItems > 100) return { records: Object.freeze([]), rejected: true };
  try {
    const value: unknown = JSON.parse(raw);
    if (!Array.isArray(value)) return { records: Object.freeze([]), rejected: true };
    const bounded = value.slice(0, maxItems);
    const records = bounded.filter(validSavedWorkspaceRecord);
    return { records: Object.freeze(records), rejected: records.length !== value.length };
  } catch {
    return { records: Object.freeze([]), rejected: true };
  }
};

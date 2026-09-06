const MAX_SAVED_WORKSPACES = 8;
const MAX_SERIALIZED_BYTES = 512_000;
const MAX_MAP_ENTRIES = 128;
const MAX_ID_LENGTH = 128;
const MAX_NAME_LENGTH = 50;
const MAX_TEXT_LENGTH = 2_000;
const MAX_KEY_LENGTH = 128;
const KANSAS_CONTEXT_BOUNDS = Object.freeze({
  west: -104.8,
  south: 34.8,
  east: -92,
  north: 42.2,
});
const PROTOTYPE_KEYS = new Set(["__proto__", "constructor", "prototype"]);
const SCENE_PRESETS = new Set([
  "overview-2d",
  "globe-overview",
  "water-systems",
  "smoke-context",
  "elevation-3d",
  "tile-grid",
]);
const ATMOSPHERES = new Set(["night", "dusk", "clear"]);
const REPORT_SCOPES = new Set(["VIEWPORT", "ANALYSIS_AREA", "VISIBLE_LAYERS", "SELECTION"]);
const REPORT_DETAILS = new Set(["EXECUTIVE", "STANDARD", "TECHNICAL"]);
const EVIDENCE_FILTERS = new Set([
  "ALL",
  "ANSWER",
  "MISSING_EVIDENCE",
  "SOURCE_STALE",
  "GENERALIZED_GEOMETRY",
  "RESTRICTED_ACCESS",
  "DENIED_BY_POLICY",
  "CORRECTED",
  "SUPERSEDED",
  "ERROR",
]);

const isRecord = (value: unknown): value is Record<string, unknown> => (
  typeof value === "object" && value !== null && !Array.isArray(value)
);

const hasOwn = (value: Record<string, unknown>, key: string) => Object.prototype.hasOwnProperty.call(value, key);

const isSafeString = (value: unknown, maximum: number, allowEmpty = false): value is string => (
  typeof value === "string"
  && value.length <= maximum
  && (allowEmpty || value.length > 0)
  && !value.includes("\u0000")
);

const isSafeKey = (value: string) => (
  value.length > 0
  && value.length <= MAX_KEY_LENGTH
  && !PROTOTYPE_KEYS.has(value)
  && /^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(value)
);

const isFiniteNumber = (value: unknown): value is number => typeof value === "number" && Number.isFinite(value);

const isSafeInteger = (value: unknown): value is number => typeof value === "number" && Number.isSafeInteger(value);

const isBoundedNumber = (value: unknown, minimum: number, maximum: number): value is number => (
  isFiniteNumber(value) && value >= minimum && value <= maximum
);

const isStringArray = (value: unknown, maximum = MAX_MAP_ENTRIES): value is string[] => (
  Array.isArray(value)
  && value.length <= maximum
  && value.every((entry) => isSafeString(entry, MAX_KEY_LENGTH) && isSafeKey(entry))
);

const isSafeRecord = (
  value: unknown,
  predicate: (entry: unknown) => boolean,
  maximum = MAX_MAP_ENTRIES,
): value is Record<string, unknown> => (
  isRecord(value)
  && Object.keys(value).length <= maximum
  && Object.entries(value).every(([key, entry]) => isSafeKey(key) && predicate(entry))
);

const isValidView = (value: unknown): boolean => {
  if (!isRecord(value) || !hasOwn(value, "center") || !hasOwn(value, "zoom") || !hasOwn(value, "bearing") || !hasOwn(value, "pitch")) return false;
  const center = value.center;
  return Array.isArray(center)
    && center.length === 2
    && isBoundedNumber(center[0], KANSAS_CONTEXT_BOUNDS.west, KANSAS_CONTEXT_BOUNDS.east)
    && isBoundedNumber(center[1], KANSAS_CONTEXT_BOUNDS.south, KANSAS_CONTEXT_BOUNDS.north)
    && isBoundedNumber(value.zoom, 0, 24)
    && isBoundedNumber(value.bearing, -360, 360)
    && isBoundedNumber(value.pitch, 0, 85);
};

const isValidBounds = (value: unknown): boolean => {
  if (!isRecord(value) || !hasOwn(value, "west") || !hasOwn(value, "south") || !hasOwn(value, "east") || !hasOwn(value, "north")) return false;
  return isBoundedNumber(value.west, KANSAS_CONTEXT_BOUNDS.west, KANSAS_CONTEXT_BOUNDS.east)
    && isBoundedNumber(value.south, KANSAS_CONTEXT_BOUNDS.south, KANSAS_CONTEXT_BOUNDS.north)
    && isBoundedNumber(value.east, KANSAS_CONTEXT_BOUNDS.west, KANSAS_CONTEXT_BOUNDS.east)
    && isBoundedNumber(value.north, KANSAS_CONTEXT_BOUNDS.south, KANSAS_CONTEXT_BOUNDS.north)
    && value.west < value.east
    && value.south < value.north;
};

const isValidScene = (value: unknown): boolean => {
  if (!isRecord(value)) return false;
  return hasOwn(value, "preset")
    && typeof value.preset === "string"
    && SCENE_PRESETS.has(value.preset)
    && hasOwn(value, "verticalExaggeration")
    && isBoundedNumber(value.verticalExaggeration, 0, 2)
    && hasOwn(value, "atmosphere")
    && typeof value.atmosphere === "string"
    && ATMOSPHERES.has(value.atmosphere)
    && hasOwn(value, "lightAzimuth")
    && isBoundedNumber(value.lightAzimuth, 0, 359)
    && hasOwn(value, "fieldOfView")
    && isBoundedNumber(value.fieldOfView, 20, 60);
};

const isValidReport = (value: unknown): boolean => {
  if (!isRecord(value)) return false;
  if (hasOwn(value, "title") && !isSafeString(value.title, MAX_TEXT_LENGTH, true)) return false;
  if (hasOwn(value, "scope") && (typeof value.scope !== "string" || !REPORT_SCOPES.has(value.scope))) return false;
  if (hasOwn(value, "detail") && (typeof value.detail !== "string" || !REPORT_DETAILS.has(value.detail))) return false;
  if (hasOwn(value, "layerIds") && !isStringArray(value.layerIds)) return false;
  if (hasOwn(value, "sections") && !isSafeRecord(value.sections, (entry) => typeof entry === "boolean", 16)) return false;
  if (hasOwn(value, "query") && !isSafeString(value.query, MAX_TEXT_LENGTH, true)) return false;
  if (hasOwn(value, "evidenceFilter") && (typeof value.evidenceFilter !== "string" || !EVIDENCE_FILTERS.has(value.evidenceFilter))) return false;
  return true;
};

const isValidSelection = (value: unknown): boolean => (
  value === null
  || value === undefined
  || (
    isRecord(value)
    && hasOwn(value, "layerId")
    && hasOwn(value, "featureId")
    && isSafeString(value.layerId, MAX_ID_LENGTH)
    && isSafeString(value.featureId, MAX_ID_LENGTH)
    && isSafeKey(value.layerId)
    && isSafeKey(value.featureId)
  )
);

const isValidSnapshot = (value: unknown): value is Record<string, unknown> => {
  if (!isRecord(value)) return false;
  if (!hasOwn(value, "id") || !isSafeString(value.id, MAX_ID_LENGTH) || !isSafeKey(value.id)) return false;
  if (!hasOwn(value, "name") || !isSafeString(value.name, MAX_NAME_LENGTH)) return false;
  if (!hasOwn(value, "savedAt") || !isSafeString(value.savedAt, 64) || !Number.isFinite(Date.parse(value.savedAt))) return false;
  if (!hasOwn(value, "view") || !isValidView(value.view)) return false;
  if (!hasOwn(value, "visibility") || !isSafeRecord(value.visibility, (entry) => typeof entry === "boolean")) return false;
  if (!hasOwn(value, "opacity") || !isSafeRecord(value.opacity, (entry) => isBoundedNumber(entry, 0, 1))) return false;
  if (!hasOwn(value, "layerOrder") || !isStringArray(value.layerOrder)) return false;
  if (!hasOwn(value, "year") || !isSafeInteger(value.year)) return false;
  if (!hasOwn(value, "basemap") || (value.basemap !== "midnight" && value.basemap !== "prairie")) return false;
  if (!hasOwn(value, "projection") || (value.projection !== "mercator" && value.projection !== "globe")) return false;
  if (hasOwn(value, "locationCameraRedacted") && typeof value.locationCameraRedacted !== "boolean") return false;
  if (hasOwn(value, "scene") && !isValidScene(value.scene)) return false;
  if (hasOwn(value, "analysisArea") && value.analysisArea !== null && !isValidBounds(value.analysisArea)) return false;
  if (hasOwn(value, "temporalComparison")) {
    if (!isRecord(value.temporalComparison)
      || !hasOwn(value.temporalComparison, "timeA")
      || !hasOwn(value.temporalComparison, "timeB")
      || !isSafeInteger(value.temporalComparison.timeA)
      || !isSafeInteger(value.temporalComparison.timeB)) return false;
  }
  if (hasOwn(value, "report") && !isValidReport(value.report)) return false;
  if (hasOwn(value, "selection") && !isValidSelection(value.selection)) return false;
  return true;
};

export const parseSavedWorkspaces = (raw: string | null): unknown[] => {
  if (typeof raw !== "string" || raw.length === 0 || raw.length > MAX_SERIALIZED_BYTES) return [];
  let parsed: unknown;
  try {
    parsed = JSON.parse(raw);
  } catch {
    return [];
  }
  if (!Array.isArray(parsed)) return [];

  const seenIds = new Set<string>();
  const restored: Record<string, unknown>[] = [];
  for (const candidate of parsed) {
    if (!isValidSnapshot(candidate)) continue;
    const candidateId = candidate.id;
    if (typeof candidateId !== "string" || seenIds.has(candidateId)) continue;
    seenIds.add(candidateId);
    restored.push(candidate);
    if (restored.length === MAX_SAVED_WORKSPACES) break;
  }
  return restored;
};

export { MAX_SAVED_WORKSPACES, MAX_SERIALIZED_BYTES };

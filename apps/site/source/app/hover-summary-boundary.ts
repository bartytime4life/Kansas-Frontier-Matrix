type HoverLocalRecord = Readonly<{
  title: string;
  evidenceState: string;
  releaseState: string;
}>;

const WITHHELD = "Protected feature";

export function localHoverTitle(record: HoverLocalRecord, layerPublicStatus?: string): string {
  if (layerPublicStatus === "RESTRICTED" || record.releaseState === "RESTRICTED"
    || record.evidenceState === "RESTRICTED_ACCESS" || record.evidenceState === "DENIED_BY_POLICY") {
    return WITHHELD;
  }
  return record.title;
}

// External map properties are untrusted display labels, never evidence. Bound
// their text before retaining it in hover state or presenting it on screen.
export function externalHoverTitle(value: unknown): string {
  if (typeof value !== "string" && typeof value !== "number") return "Basemap feature";
  const normalized = String(value).replace(/[\u0000-\u001f\u007f]/g, " ").replace(/\s+/g, " ").trim();
  return normalized ? normalized.slice(0, 90) : "Basemap feature";
}

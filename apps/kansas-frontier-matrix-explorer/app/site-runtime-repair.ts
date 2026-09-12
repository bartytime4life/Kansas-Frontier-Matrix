export type ExplorerLayerOpacity = Readonly<{
  id: string;
  defaultOpacity: number;
}>;

export type DegradedGuidanceStep = Readonly<{
  id: string;
  state: "SUPPORTED" | "CORRECTED" | "SUPERSEDED" | "DENY";
  title: string;
  summary: string;
  layerId: string;
  featureId: string;
  year: number;
}>;

export const PRIVATE_CAMERA_VISIBLE_LABEL = "Private camera · coordinates redacted";
export const PRIVATE_CAMERA_ASSISTIVE_LABEL = "private camera, coordinates redacted";
export const LOCATION_CAMERA_REDACTION_VALUE = "location-camera-redacted";

const OPACITY_EPSILON = 0.005;
const TRUST_SCOPED_PARAMS = Object.freeze([
  "f",
  "panel",
  "drawer",
  "focusStage",
  "focusIntent",
]);

export const DEGRADED_GUIDANCE_STEPS: readonly DegradedGuidanceStep[] = Object.freeze([
  Object.freeze({
    id: "supported",
    state: "SUPPORTED",
    title: "Topeka · 2026",
    summary: "Open a synthetic observation with a matching demonstration evidence reference.",
    layerId: "atmosphere-observations",
    featureId: "atmo-topeka-2026",
    year: 2026,
  }),
  Object.freeze({
    id: "corrected",
    state: "CORRECTED",
    title: "Hays · 2024",
    summary: "Inspect a corrected record without hiding its earlier state.",
    layerId: "atmosphere-observations",
    featureId: "atmo-hays-2024",
    year: 2024,
  }),
  Object.freeze({
    id: "superseded",
    state: "SUPERSEDED",
    title: "Historical route · 1910",
    summary: "Inspect lineage retained for history without treating it as current support.",
    layerId: "historical-context",
    featureId: "history-route-1910",
    year: 1910,
  }),
  Object.freeze({
    id: "withheld",
    state: "DENY",
    title: "Protected context",
    summary: "See why precise detail remains unavailable instead of being inferred.",
    layerId: "public-safe-planning",
    featureId: "planning-generalized-envelope",
    year: 2026,
  }),
]);

const parseOpacityPairs = (value: string | null): Map<string, number> => {
  const parsed = new Map<string, number>();
  if (value === null || value.trim() === "") return parsed;

  for (const entry of value.split(",")) {
    const separator = entry.lastIndexOf(":");
    if (separator <= 0 || separator === entry.length - 1) continue;
    const id = entry.slice(0, separator);
    const numericValue = Number(entry.slice(separator + 1));
    if (!Number.isFinite(numericValue)) continue;
    parsed.set(id, Math.min(1, Math.max(0, numericValue)));
  }
  return parsed;
};

export function canonicalizeExplorerUrl(
  input: string | URL,
  layers: readonly ExplorerLayerOpacity[],
  featureExists: (featureId: string) => boolean,
): URL {
  const next = input instanceof URL ? new URL(input.toString()) : new URL(input);
  const parsedOpacity = parseOpacityPairs(next.searchParams.get("o"));
  const opacityOverrides = layers.flatMap((layer) => {
    const value = parsedOpacity.get(layer.id);
    if (value === undefined || Math.abs(value - layer.defaultOpacity) < OPACITY_EPSILON) return [];
    return [`${layer.id}:${value.toFixed(2)}`];
  });

  if (opacityOverrides.length > 0) next.searchParams.set("o", opacityOverrides.join(","));
  else next.searchParams.delete("o");

  const activeContextIds = (next.searchParams.get("ctx") ?? "").split(",").filter(Boolean);
  const parsedContextOpacity = parseOpacityPairs(next.searchParams.get("ctxo"));
  const contextOpacityOverrides = activeContextIds.flatMap((id) => {
    const value = parsedContextOpacity.get(id);
    return value === undefined ? [] : [`${id}:${value.toFixed(2)}`];
  });
  if (contextOpacityOverrides.length > 0) next.searchParams.set("ctxo", contextOpacityOverrides.join(","));
  else next.searchParams.delete("ctxo");

  if (next.searchParams.get("ws") === "trust") {
    const featureId = next.searchParams.get("f");
    if (featureId === null || !featureExists(featureId)) {
      next.searchParams.set("ws", "explore");
      for (const parameter of TRUST_SCOPED_PARAMS) next.searchParams.delete(parameter);
    }
  }

  return next;
}

export function relativeExplorerUrl(url: URL): string {
  return `${url.pathname}${url.search}${url.hash}`;
}

export function redactScreenReaderStatus(status: string): string {
  return status.replace(
    /Map center .*?\. (?=\d+ layers visible\.)/s,
    `Map center ${PRIVATE_CAMERA_ASSISTIVE_LABEL}. `,
  );
}

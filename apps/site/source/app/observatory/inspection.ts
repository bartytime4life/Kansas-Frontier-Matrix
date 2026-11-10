import type { FeatureCollection } from "geojson";

type InspectionTrack = "weather" | "river" | "counties" | "earthquakes" | "shake" | "storms";
export type InspectionSelection = { track: string; properties: Record<string, unknown> };
export type InspectionFrame = { time: string; data: Readonly<Record<InspectionTrack, FeatureCollection>> };

function identity(track: string, properties: Record<string, unknown>): string | null {
  const field = track === "weather" ? "station" : track === "river" ? "stationId"
    : track === "counties" ? "geoid" : track === "earthquakes" || track === "shake" ? "featureId" : null;
  if (field) {
    const value = properties[field];
    return typeof value === "string" && value !== "" ? JSON.stringify([track, value]) : null;
  }
  if (track !== "storms" || typeof properties.radar !== "string" || !properties.radar) return null;
  if (properties.kind === "radar") return JSON.stringify(["radar", properties.radar]);
  if (!["cell", "rotation"].includes(String(properties.kind)) || typeof properties.volumeTime !== "string" || !properties.volumeTime) return null;
  // A storm ID can be reused in a later volume. Keep this exact scan identity;
  // ambiguous unassociated rotations are withheld rather than guessed.
  return JSON.stringify([properties.kind, properties.radar, properties.stormId ?? null, properties.volumeTime]);
}

/** Resolve against the records that actually passed the map's frame commit.
 * The clicked properties supply identity only, never a fallback reading. */
export function committedInspection(
  selection: InspectionSelection | null,
  frame: InspectionFrame | null,
  scope: { requested: string | null; committed: string | null; ready: boolean; visible: boolean },
): InspectionSelection | null {
  if (!selection || !frame || !scope.ready || !scope.visible || !scope.committed
    || frame.time !== scope.committed || scope.requested !== scope.committed || !Object.hasOwn(frame.data, selection.track)) return null;
  const key = identity(selection.track, selection.properties);
  if (!key) return null;
  const matches = frame.data[selection.track as InspectionTrack].features.filter((feature) => feature.properties
    && identity(selection.track, feature.properties) === key
    && (selection.track !== "river" || feature.properties.missing === false));
  return matches.length === 1 ? { track: selection.track, properties: matches[0].properties! } : null;
}

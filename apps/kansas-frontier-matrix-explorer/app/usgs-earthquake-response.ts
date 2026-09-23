import { readBoundedJson } from "./bounded-json";

type JsonRecord = Record<string, unknown>;
const isRecord = (value: unknown): value is JsonRecord => (
  value !== null && typeof value === "object" && !Array.isArray(value)
);

/**
 * Decode only a response from the fixed USGS FDSN event query adapter.
 * USGS documents 204 as its default no-data response. It has no JSON body.
 * Normalizing that provider-defined result does not create an observation.
 *
 * Do not use this no-data policy for radar, smoke, alerts, or arbitrary URLs.
 * Redirect rejection, request timeout, and the host allowlist remain at the
 * caller. Other non-200 responses and malformed 200 bodies still fail closed.
 */
export async function readUsgsEarthquakeResponse(
  response: Response,
  maxBytes: number,
): Promise<JsonRecord> {
  if (response.status === 204) {
    return {
      type: "FeatureCollection",
      metadata: { count: 0 },
      features: [],
    };
  }
  if (response.status !== 200) {
    throw new Error(`USGS earthquake upstream returned HTTP ${response.status}.`);
  }

  const payload = await readBoundedJson(response, maxBytes);
  if (!isRecord(payload)
    || payload.type !== "FeatureCollection"
    || !Array.isArray(payload.features)
    || !payload.features.every((feature) => isRecord(feature) && feature.type === "Feature")) {
    throw new SyntaxError("USGS earthquake upstream returned an invalid GeoJSON FeatureCollection.");
  }
  // Coordinates, event time, feature identity, and query-window filtering
  // remain the responsibility of the existing recentEarthquakes adapter.
  return payload;
}

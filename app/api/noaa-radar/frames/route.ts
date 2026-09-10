import { NextResponse } from "next/server";
import {
  buildNoaaRadarManifest,
  NOAA_RADAR_CAPABILITIES_URL,
} from "../../../noaa-radar";

export const dynamic = "force-dynamic";

const NOAA_USER_AGENT = "KansasFrontierMatrixExplorer/1.0 (https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)";
const MAX_CAPABILITIES_BYTES = 512 * 1024;
const REQUEST_TIMEOUT_MS = 12_000;

class RadarUpstreamError extends Error {
  constructor(message: string, readonly timeout = false) {
    super(message);
  }
}

const fetchCapabilities = async (): Promise<string> => {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  try {
    const response = await fetch(NOAA_RADAR_CAPABILITIES_URL, {
      cache: "no-store",
      signal: controller.signal,
      headers: { Accept: "application/xml,text/xml;q=0.9", "User-Agent": NOAA_USER_AGENT },
    });
    if (!response.ok) throw new RadarUpstreamError(`NOAA nowCOAST returned HTTP ${response.status}.`);
    const contentType = response.headers.get("content-type")?.toLowerCase() ?? "";
    if (!contentType.includes("xml")) throw new RadarUpstreamError("NOAA radar capabilities returned an unexpected media type.");
    const declaredLength = Number(response.headers.get("content-length") ?? "0");
    if (declaredLength > MAX_CAPABILITIES_BYTES) throw new RadarUpstreamError("NOAA radar capabilities exceeded the bounded adapter limit.");
    const body = await response.arrayBuffer();
    if (body.byteLength > MAX_CAPABILITIES_BYTES) throw new RadarUpstreamError("NOAA radar capabilities exceeded the bounded adapter limit.");
    const xml = new TextDecoder().decode(body);
    if (!xml.includes("WMS_Capabilities") || !xml.includes("conus_base_reflectivity_mosaic")) {
      throw new RadarUpstreamError("NOAA radar capabilities did not match the fixed WMS contract.");
    }
    return xml;
  } catch (error) {
    if (error instanceof RadarUpstreamError) throw error;
    if (error instanceof Error && error.name === "AbortError") throw new RadarUpstreamError("NOAA radar capabilities request timed out.", true);
    throw new RadarUpstreamError(error instanceof Error ? error.message : "NOAA radar capabilities request failed.");
  } finally {
    clearTimeout(timeout);
  }
};

export async function GET() {
  try {
    const retrievedAt = new Date().toISOString();
    const manifest = buildNoaaRadarManifest(await fetchCapabilities(), retrievedAt);
    return NextResponse.json(manifest, {
      status: 200,
      headers: {
        "Cache-Control": "public, max-age=120, stale-while-revalidate=120",
        "X-Content-Type-Options": "nosniff",
      },
    });
  } catch (error) {
    const timeout = error instanceof RadarUpstreamError && error.timeout;
    return NextResponse.json({
      state: "error",
      code: timeout ? "NOAA_RADAR_TIMEOUT" : "NOAA_RADAR_UNAVAILABLE",
      message: "NOAA radar frames are temporarily unavailable. No synthetic or untimed fallback was used.",
      evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    }, {
      status: timeout ? 504 : 502,
      headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" },
    });
  }
}

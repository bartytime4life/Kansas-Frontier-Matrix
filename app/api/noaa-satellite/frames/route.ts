import { readBoundedJson } from "../../../bounded-json";
import { NextResponse } from "next/server";
import { buildNoaaSatelliteManifest, NOAA_SATELLITE_MAX_FRAMES, NOAA_SATELLITE_SERVICE_URL } from "../../../noaa-satellite";

export const dynamic = "force-dynamic";

export async function GET() {
  const retrievedAt = new Date().toISOString();
  const url = new URL(`${NOAA_SATELLITE_SERVICE_URL}/query`);
  url.searchParams.set("where", "start_time IS NOT NULL");
  url.searchParams.set("outFields", "objectid,name,start_time,end_time");
  url.searchParams.set("returnGeometry", "false");
  url.searchParams.set("orderByFields", "start_time DESC");
  url.searchParams.set("resultRecordCount", String(NOAA_SATELLITE_MAX_FRAMES + 1));
  url.searchParams.set("time", `${Date.parse(retrievedAt) - 24 * 60 * 60 * 1000},${Date.parse(retrievedAt)}`);
  url.searchParams.set("f", "json");
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 12_000);
  try {
    const response = await fetch(url.toString(), { cache: "no-store", redirect: "manual", signal: controller.signal, headers: { Accept: "application/json" } });
    if (!response.ok || response.redirected || !response.headers.get("content-type")?.toLowerCase().includes("json")) throw new Error("NOAA satellite catalog was unavailable.");
    const data = await readBoundedJson(response, 1024 * 1024);
    const manifest = buildNoaaSatelliteManifest(data, retrievedAt);
    return NextResponse.json(manifest, { headers: { "Cache-Control": "public, max-age=0, s-maxage=120", "X-Content-Type-Options": "nosniff" } });
  } catch {
    return NextResponse.json({ state: "error", message: "NOAA satellite frames are unavailable; no undated imagery was substituted." }, { status: controller.signal.aborted ? 504 : 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  } finally {
    clearTimeout(timeout);
  }
}

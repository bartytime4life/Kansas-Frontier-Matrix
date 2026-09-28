import { NextRequest } from "next/server";
import { GET as contextData } from "../live-context/route";
import { GET as streamflowData } from "../hydrology/streamflow/route";
import { eventDay } from "../../event-atlas";
export const dynamic = "force-dynamic";
const sources = new Set(["census-counties", "usgs-streamflow", "usgs-earthquakes", "noaa-hms-smoke", "nasa-gibs-fire-points", "nifc-fire-reports", "raspberry-shake-stations", "nws-alerts"]);
const archiveSources = new Set(["usgs-earthquakes", "noaa-hms-smoke", "nasa-gibs-fire-points", "raspberry-shake-stations"]);
export async function GET(request: Request) {
  const url = new URL(request.url); const source = url.searchParams.get("source") ?? "";
  const day = url.searchParams.get("day");
  if (!sources.has(source) || [...url.searchParams.keys()].some((k) => !["source", "day"].includes(k) || url.searchParams.getAll(k).length !== 1)
    || (url.searchParams.has("day") && (!archiveSources.has(source) || !day || !eventDay(day)
      || day < (source === "nasa-gibs-fire-points" ? "2018-01-01" : source === "noaa-hms-smoke" ? "2005-08-05" : "1800-01-01")
      || day > new Date().toISOString().slice(0, 10)))) return Response.json({ error: "Choose a supported source download and exact UTC day." }, { status: 400 });
  const path = source === "usgs-streamflow" ? "/api/hydrology/streamflow?mode=network&range=24h" : `/api/live-context?feed=${source}${day ? `&day=${encodeURIComponent(day)}` : ""}`;
  const forwarded = new NextRequest(new URL(path, url));
  const response = await (source === "usgs-streamflow" ? streamflowData(forwarded) : contextData(forwarded));
  if (!response.ok) return response;
  const headers = new Headers(response.headers);
  const json = await response.json();
  const extension = source === "usgs-streamflow" ? "json" : "geojson";
  if (extension === "geojson" && (json?.data?.type !== "FeatureCollection" || !Array.isArray(json.data.features))) return Response.json({ error: "The source did not return a valid feature collection." }, { status: 502, headers: { "Cache-Control": "no-store" } });
  const imageDay = source === "nasa-gibs-fire-points" ? json.sourceDay : null;
  if (source === "nasa-gibs-fire-points" && (typeof imageDay !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(imageDay))) return Response.json({ error: "The fire source did not provide a valid image day." }, { status: 502, headers: { "Cache-Control": "no-store" } });
  const result = source === "usgs-streamflow" ? json : { ...json.data, kfm: { source: json.source, requestedDay: day ?? undefined, sourceDay: imageDay ?? undefined, retrievedAt: json.retrievedAt, sourceTime: json.upstreamUpdatedAt, state: json.state, limitation: json.limitation } };
  // The downloaded body differs from the upstream envelope; remove its body metadata.
  for (const name of ["Content-Length", "Content-Encoding", "ETag"]) headers.delete(name);
  headers.set("Content-Disposition", `attachment; filename="kfm-${source}-${imageDay ?? day ?? new Date().toISOString().slice(0,10)}.${extension}"`);
  headers.set("Content-Type", extension === "geojson" ? "application/geo+json; charset=utf-8" : "application/json; charset=utf-8");
  headers.set("X-Content-Type-Options", "nosniff");
  return new Response(JSON.stringify(result), { status: response.status, headers });
}

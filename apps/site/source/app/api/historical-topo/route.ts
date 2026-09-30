import { boundedFetch } from "../event-atlas/upstream";
import { parseTopoCatalog, parseTopoSearch, topoProviderUrl } from "../../historical-topo";

export const dynamic = "force-dynamic";
export async function GET(request: Request) {
  let search;
  try { search = parseTopoSearch(request.url); }
  catch { return Response.json({ state: "error", message: "Choose a valid U.S. map center and filters." }, { status: 400, headers: { "Cache-Control": "no-store" } }); }
  const source = topoProviderUrl(search);
  try {
    const response = await boundedFetch(source, 512 * 1024, { timeoutMs: 12000 });
    const parsed = parseTopoCatalog(JSON.parse(response.text()) as unknown);
    return Response.json({ state: "available", ...parsed, query: search, retrievedAt: new Date().toISOString(), source, role: "EXTERNAL_CONTEXT_ONLY",
      note: "Catalog footprints and sheet editions only. A map publication year does not date every feature. No scanned raster is displayed here." },
    { headers: { "Cache-Control": "public, max-age=300", "X-Content-Type-Options": "nosniff" } });
  } catch {
    return Response.json({ state: "unavailable", sheets: [], message: "USGS historical map catalog is unavailable. Try again or open TopoView directly." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}

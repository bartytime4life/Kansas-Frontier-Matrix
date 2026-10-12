import { readBoundedJson } from "../../../bounded-json";
/** Read-only public USDA display context. The query contains only validated numeric coordinates. */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const lon = Number(params.get("lon")), lat = Number(params.get("lat"));
  if (!params.has("lon") || !params.has("lat") || !Number.isFinite(lon) || !Number.isFinite(lat) || lon < -102.1 || lon > -94.5 || lat < 36.9 || lat > 40.1) {
    return Response.json({ error: "A Kansas coordinate is required." }, { status: 400 });
  }
  const query = `SELECT TOP 100 mu.mukey,mu.musym,mu.muname,c.cokey,c.compname,c.comppct_r,c.majcompflag,h.chkey,h.hzname,h.hzdept_r,h.hzdepb_r,h.sandtotal_r,h.silttotal_r,h.claytotal_r FROM mapunit mu JOIN component c ON c.mukey=mu.mukey JOIN chorizon h ON h.cokey=c.cokey WHERE mu.mukey IN (SELECT mukey FROM SDA_Get_Mukey_from_intersection_with_WktWgs84('POINT(${lon.toFixed(6)} ${lat.toFixed(6)})')) ORDER BY c.comppct_r DESC,c.cokey,h.hzdept_r,h.chkey`;
  const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 18000);
  const cancel = () => controller.abort(); request.signal.addEventListener("abort", cancel, { once: true });
  try {
    const response = await fetch("https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ format: "JSON+COLUMNNAME", query }), signal: controller.signal });
    if (!response.ok) throw new Error("USDA unavailable");
    const data = await readBoundedJson(response, 300000, controller.signal);
    const table = data && typeof data === "object" && "Table" in data ? data.Table : [];
    if (!Array.isArray(table) || table.length > 101 || table.some(row => !Array.isArray(row) || row.length !== 14 || row.some(cell => cell !== null && typeof cell !== "string" && typeof cell !== "number"))) throw new Error("Unrecognized USDA response");
    return Response.json({ columns: table[0] ?? [], rows: table.slice(1), partial: table.length === 101, retrievedAt: new Date().toISOString(), sourceUrl: "https://sdmdataaccess.nrcs.usda.gov/", depthUnit: "cm", depthReference: "soil surface", limitation: "Soil-map components are alternative descriptions with map-unit proportions, not observations at this pointer. Survey editions vary; no historical reconstruction. At most 100 horizons returned." }, { headers: { "Cache-Control": "private, max-age=3600" } });
  } catch { return Response.json({ error: "Soil source is unavailable. No soil conditions are inferred." }, { status: 502 }); }
  finally { clearTimeout(timer); request.signal.removeEventListener("abort", cancel); }
}

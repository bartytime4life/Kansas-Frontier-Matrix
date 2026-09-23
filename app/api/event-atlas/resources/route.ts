import { boundedFetch, jsonHeaders } from "../upstream";
export const dynamic = "force-dynamic";
const ROOT = "https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/USGS_Topographic_Mine_Symbols/FeatureServer/8/query";
const COUNTIES = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/1/query?where=STATE%3D%2720%27&outFields=GEOID%2CBASENAME&returnGeometry=true&outSR=4326&geometryPrecision=3&maxAllowableOffset=0.01&f=geojson";
export async function GET(request: Request) {
  try {
    const p = new URL(request.url).searchParams, edition = p.get("edition") ?? "1984";
    if ([...p.keys()].some((key) => key !== "edition") || p.getAll("edition").length > 1 || !/^\d{4}$/.test(edition) || Number(edition) < 1934 || Number(edition) > 1996) return Response.json({ message: "Choose a map edition year from 1934–1996." }, { status: 400 });
    const url = new URL(ROOT);
    for (const [key,value] of Object.entries({ where: `State='KS' AND Topo_Date='${edition}'`, outStatistics: JSON.stringify([{ statisticType: "count", onStatisticField: "OBJECTID", outStatisticFieldName: "symbol_count" }]), groupByFieldsForStatistics: "County", returnGeometry: "false", f: "json" })) url.searchParams.set(key,value);
    const [countBody, countyBody] = await Promise.all([boundedFetch(url.toString(), 500_000), boundedFetch(COUNTIES, 3_000_000)]);
    const counts = JSON.parse(countBody.text()), counties = JSON.parse(countyBody.text());
    if (counts.error || !Array.isArray(counts.features) || counts.exceededTransferLimit || counties.type !== "FeatureCollection" || !Array.isArray(counties.features) || counties.features.length !== 105) throw new Error("Incomplete resource join.");
    const byCounty = new Map<string,number>();
    for (const row of counts.features) {
      const { County, symbol_count: count } = row.attributes ?? {};
      if (typeof County !== "string" || !Number.isInteger(count) || count < 0 || byCounty.has(County)) throw new Error("Invalid county summary.");
      byCounty.set(County,count);
    }
    const features = counties.features.map((county: { properties: { GEOID: string; BASENAME: string }; geometry: unknown }) => {
      const name = county.properties.BASENAME;
      const count = byCounty.get(name) ?? 0; byCounty.delete(name);
      return { type: "Feature", geometry: county.geometry, properties: { county: name, geoid: county.properties.GEOID, symbols: count, edition, evidenceRole: "EXTERNAL_CONTEXT_ONLY" } };
    });
    if (byCounty.size) throw new Error("Unmatched county names were withheld.");
    return Response.json({ type: "FeatureCollection", features, edition, retrievedAt: new Date().toISOString(), source: ROOT, limitation: "Historical USGS 1:24,000 topographic mine symbols, grouped before delivery by modern Census county. Counts are map symbols, not unique mines, operations, production, reserves, or economic resource estimates. This older compilation is not the latest complete USMIN release." }, { headers: jsonHeaders });
  } catch { return Response.json({ message: "Regional resource context is unavailable; no precise site locations were delivered." }, { status: 502, headers: { "Cache-Control": "no-store" } }); }
}

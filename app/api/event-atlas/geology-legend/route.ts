import { boundedFetch, jsonHeaders } from "../upstream";
export const dynamic = "force-dynamic";
const SOURCE = "https://tiles.arcgis.com/tiles/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Kansas_geology/MapServer/legend?f=pjson";
export async function GET(request: Request) {
  if (new URL(request.url).search) return Response.json({ message: "No parameters supported." }, { status: 400 });
  try {
    const body = await boundedFetch(SOURCE, 1024 * 1024), data = JSON.parse(body.text());
    if (!Array.isArray(data.layers) || data.error) throw new Error("Legend unavailable.");
    const items = data.layers.flatMap((layer: { legend?: unknown[] }) => layer.legend ?? []).filter((item: { label?: unknown; contentType?: unknown; imageData?: unknown }) => typeof item.label === "string" && item.label.length < 300 && item.contentType === "image/png" && typeof item.imageData === "string" && item.imageData.length < 20_000 && /^[A-Za-z0-9+/]+=*$/.test(item.imageData)).map((item: { label: string; imageData: string }) => ({ label: item.label, image: `data:image/png;base64,${item.imageData}` }));
    if (!items.length || items.length > 100) throw new Error("Legend outside budget.");
    return Response.json({ source: SOURCE, items }, { headers: jsonHeaders });
  } catch { return Response.json({ message: "The KGS unit legend is unavailable." }, { status: 502 }); }
}

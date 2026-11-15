import { kdotBridges } from "../live-context/kdot-bridges";

export const dynamic = "force-dynamic";
const headers = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
const BRIDGE_ID = /^kdot-(?:state|local)-\d{1,9}$/;

/** The full KDOT inventory record for one bridge already shown on the map. The only input is
 * a bridge id from the map feed; the record comes from the same shared inventory read. */
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams, id = params.get("id") ?? "";
  if ([...params.keys()].some(key => key !== "id") || params.getAll("id").length !== 1 || !BRIDGE_ID.test(id)) {
    return Response.json({ state: "error", message: "Choose a bridge from the map." }, { status: 400, headers });
  }
  try {
    const detail = await kdotBridges.detail(id);
    if (!detail) return Response.json({ state: "missing", message: "That bridge is not in the current KDOT inventory." }, { status: 404, headers });
    return Response.json({ state: "ready", id, retrievedAt: detail.retrievedAt, properties: detail.properties, role: "EXTERNAL_CONTEXT_ONLY" }, { headers });
  } catch (error) {
    return Response.json({ state: "unavailable", message: error instanceof Error ? error.message : "KDOT bridge records are unavailable." }, { status: 503, headers });
  }
}

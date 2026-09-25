import { earthEngineFailure, earthEngineOwner, earthEnginePrivateHeaders, earthEngineTile } from "../../../../../earth-engine-context-server";

export async function GET(_request: Request, context: { params: Promise<{ setId: string; layerId: string; tile: string[] }> }) {
  try {
    await earthEngineOwner();
    const { setId, layerId, tile } = await context.params;
    if (!Array.isArray(tile) || tile.length !== 3) return new Response(null, { status: 404, headers: earthEnginePrivateHeaders });
    const image = await earthEngineTile(setId, layerId, tile[0], tile[1], tile[2]);
    if (!image) return new Response(null, { status: 404, headers: earthEnginePrivateHeaders });
    return new Response(image, { headers: { ...earthEnginePrivateHeaders, "Content-Type": "image/png" } });
  } catch (error) { return earthEngineFailure(error); }
}

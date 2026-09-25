import { activeEarthEngineManifest, earthEngineFailure, earthEngineOwner, earthEnginePrivateHeaders } from "../../../earth-engine-context-server";

export async function GET() {
  try {
    await earthEngineOwner();
    const manifest = await activeEarthEngineManifest();
    return Response.json({ available: Boolean(manifest), manifest }, { headers: earthEnginePrivateHeaders });
  } catch (error) { return earthEngineFailure(error); }
}

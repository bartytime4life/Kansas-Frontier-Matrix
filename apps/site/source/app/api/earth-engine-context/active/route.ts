import { activeEarthEngineManifest, earthEngineFailure, earthEngineReader, earthEnginePrivateHeaders } from "../../../earth-engine-context-server";

export async function GET(request: Request) {
  try {
    await earthEngineReader(request);
    const manifest = await activeEarthEngineManifest();
    return Response.json({ available: Boolean(manifest), manifest }, { headers: earthEnginePrivateHeaders });
  } catch (error) { return earthEngineFailure(error); }
}

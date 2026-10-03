import { activeEarthEngineCatalog, earthEngineFailure, earthEngineReader, earthEnginePrivateHeaders } from "../../../earth-engine-context-server";

export async function GET(request: Request) {
  try {
    await earthEngineReader(request);
    return Response.json({ manifests: await activeEarthEngineCatalog() }, { headers: earthEnginePrivateHeaders });
  } catch (error) { return earthEngineFailure(error); }
}

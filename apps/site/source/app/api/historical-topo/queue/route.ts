import { topoActiveKey, topoOverlayPrefix } from "../../../historical-topo-overlay";
import { topoBucket, topoBytes, topoFailure, topoJson, topoWorker, TopoOverlayError } from "../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  try {
    topoWorker(request);
    const bucket = topoBucket();
    const listed = await bucket.list({ prefix: `${topoOverlayPrefix}/requests/`, limit: 100 });
    if (listed.truncated) throw new TopoOverlayError("Historical map queue exceeds its bounded page; narrow or drain it.", 503);
    const requests = [];
    for (const object of listed.objects) {
      const raw = await topoBytes(object.key, 4096);
      if (!raw) continue;
      const item = topoJson(raw) as { version?: number; id?: number; scanId?: number; state?: string };
      if (item.version !== 1 || item.state !== "KS" || !Number.isInteger(item.id) || !Number.isInteger(item.scanId)) continue;
      if (await topoBytes(topoActiveKey(item.scanId!), 2048)) continue;
      requests.push(item);
    }
    return Response.json({ requests }, { headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  } catch (error) { return topoFailure(error); }
}

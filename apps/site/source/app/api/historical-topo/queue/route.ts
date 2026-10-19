import { topoActiveKey, topoOverlayPrefix } from "../../../historical-topo-overlay";
import { topoBucket, topoBytes, topoFailure, topoJson, topoWorker } from "../../../historical-topo-overlay-server";
export const dynamic = "force-dynamic";

// Request records stay in storage after their sheet is activated, so the queue
// pages past them (and past any malformed records) instead of failing closed
// once more than one listing page exists. Both bounds keep storage reads finite.
const QUEUE_PAGE = 100, QUEUE_SCAN_LIMIT = 500, QUEUE_RETURN_LIMIT = 25;

export async function GET(request: Request) {
  try {
    topoWorker(request);
    const bucket = topoBucket();
    const requests = [];
    let cursor: string | undefined, scanned = 0, truncated = false;
    while (requests.length < QUEUE_RETURN_LIMIT) {
      if (scanned >= QUEUE_SCAN_LIMIT) { truncated = true; break; }
      const listed = await bucket.list({ prefix: `${topoOverlayPrefix}/requests/`, limit: QUEUE_PAGE, ...(cursor ? { cursor } : {}) });
      for (const object of listed.objects) {
        if (requests.length >= QUEUE_RETURN_LIMIT) { truncated = true; break; }
        scanned++;
        const raw = await topoBytes(object.key, 4096);
        if (!raw) continue;
        const item = topoJson(raw) as { version?: number; id?: number; scanId?: number; state?: string };
        if (item.version !== 1 || item.state !== "KS" || !Number.isInteger(item.id) || !Number.isInteger(item.scanId)) continue;
        if (await topoBytes(topoActiveKey(item.scanId!), 2048)) continue;
        requests.push(item);
      }
      if (!listed.truncated || !listed.cursor) break;
      cursor = listed.cursor;
    }
    return Response.json({ requests, truncated }, { headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  } catch (error) { return topoFailure(error); }
}

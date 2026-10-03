import { boundedFetch } from "../event-atlas/upstream";
import { assembleBridgePages, bridgeProviderCountUrl, bridgeProviderUrl, BRIDGE_PAGE_LIMIT, BRIDGE_RECORD_LIMIT, parseBridgeCount, parseBridgeSearch } from "../../kansas-bridge-records";

export const dynamic = "force-dynamic";
const headers = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
export async function GET(request: Request) {
  let query;
  try { query = parseBridgeSearch(request.url); }
  catch { return Response.json({ state: "error", message: "Choose a Kansas map center and a 100, 500, or 1000 metre radius." }, { status: 400, headers }); }
  const controller = new AbortController();
  const cancel = () => controller.abort(request.signal.reason);
  request.signal.addEventListener("abort", cancel, { once: true });
  const timer = setTimeout(() => controller.abort(new Error("Bridge search deadline exceeded.")), 12000);
  try {
    controller.signal.throwIfAborted();
    const countResponse = await boundedFetch(bridgeProviderCountUrl(query), 4096, { timeoutMs: 12000, signal: controller.signal });
    const count = parseBridgeCount(JSON.parse(countResponse.text()));
    const pages: unknown[] = [];
    for (let page = 0; page < BRIDGE_PAGE_LIMIT && page * BRIDGE_RECORD_LIMIT < count; page++) {
      controller.signal.throwIfAborted();
      const response = await boundedFetch(bridgeProviderUrl(query, page * BRIDGE_RECORD_LIMIT), 128 * 1024, { timeoutMs: 12000, signal: controller.signal });
      const body = JSON.parse(response.text()) as { features?: unknown[] };
      pages.push(body);
      if (!Array.isArray(body.features) || body.features.length < BRIDGE_RECORD_LIMIT) break;
    }
    controller.signal.throwIfAborted();
    return Response.json(assembleBridgePages(pages, query, count), { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "KDOT bridge records could not be verified. Retry or inspect the official service." }, { status: 502, headers });
  } finally {
    clearTimeout(timer);
    request.signal.removeEventListener("abort", cancel);
  }
}

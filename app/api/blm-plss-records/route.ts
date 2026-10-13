import { boundedFetch } from "../event-atlas/upstream";
import { blmPlssProviderUrl, parseBlmPlssCount, parseBlmPlssQuery, parseBlmPlssRecords } from "../../blm-plss-records";

export const dynamic = "force-dynamic";
const headers = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
export async function GET(request: Request) {
  let query;
  try { query = parseBlmPlssQuery(request.url); }
  catch { return Response.json({ state: "error", message: "Choose a Kansas map center and PLSS layer." }, { status: 400, headers }); }
  const controller = new AbortController();
  const cancel = () => controller.abort(request.signal.reason);
  request.signal.addEventListener("abort", cancel, { once: true });
  const timer = setTimeout(() => controller.abort(new Error("PLSS inspection timed out.")), 12000);
  try {
    controller.signal.throwIfAborted();
    const countResponse = await boundedFetch(blmPlssProviderUrl(query, true), 4096, { timeoutMs: 12000, signal: controller.signal });
    const count = parseBlmPlssCount(JSON.parse(countResponse.text()));
    if (count === 0) return Response.json(parseBlmPlssRecords({ features: [] }, query, 0), { headers });
    controller.signal.throwIfAborted();
    const featuresResponse = await boundedFetch(blmPlssProviderUrl(query), 64 * 1024, { timeoutMs: 12000, signal: controller.signal });
    controller.signal.throwIfAborted();
    return Response.json(parseBlmPlssRecords(JSON.parse(featuresResponse.text()), query, count), { headers });
  } catch {
    return Response.json({ state: "unavailable", message: "BLM survey records could not be verified. Retry or inspect the official service." }, { status: 502, headers });
  } finally {
    clearTimeout(timer);
    request.signal.removeEventListener("abort", cancel);
  }
}

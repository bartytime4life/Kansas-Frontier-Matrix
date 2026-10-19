import { getIngestionStore } from "../../../../server/ingestion-store.mjs";
import { clearIngestionStatusCache } from "../../../../server/ingestion-runner.mjs";
import { workerAuthorized, json } from "../../../../server/capture-worker-access.mjs";
export const dynamic = "force-dynamic";
export async function POST(request: Request) {
  if (!workerAuthorized(request)) return json({ error: "Capture worker authorization required." }, 401);
  const params = new URL(request.url).searchParams;
  const action = params.get("action");
  if (params.size !== 1 || !["pause", "resume"].includes(action ?? "")) return json({ error: "Choose pause or resume." }, 400);
  try {
    await (await getIngestionStore()).setPaused(action === "pause", "capture-worker");
    clearIngestionStatusCache();
    return json({ state: action === "pause" ? "paused" : "scheduled" });
  } catch { return json({ error: "Capture control held; storage is unavailable." }, 503); }
}

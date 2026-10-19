import { runIngestion, clearIngestionStatusCache } from "../../../../server/ingestion-runner.mjs";
import { workerAuthorized, json } from "../../../../server/capture-worker-access.mjs";
export const dynamic = "force-dynamic";
export async function POST(request: Request) {
  if (!workerAuthorized(request)) return json({ error: "Capture worker authorization required." }, 401);
  try { const result = await runIngestion({ actor: "capture-worker" }); clearIngestionStatusCache(); return json(result, result.state === "configuration-required" ? 409 : result.state === "partial" ? 503 : 200); }
  catch { return json({ error: "Capture held; storage is unavailable." }, 503); }
}

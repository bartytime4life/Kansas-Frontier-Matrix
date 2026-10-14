import { runIngestion, clearIngestionStatusCache } from "../../../../server/ingestion-runner.mjs";
import { authenticateOwner, sameOrigin, workerAuthorized, json } from "../../../../server/owner-auth.mjs";
import { OWNER_GITHUB_ID } from "../../../../server/ingestion-config.mjs";
export const dynamic = "force-dynamic";
export async function POST(request: Request) {
  const worker = workerAuthorized(request);
  if (!(worker || sameOrigin(request) && await authenticateOwner(request))) return json({ error: "Owner or capture-worker sign-in required." }, 401);
  try { const result = await runIngestion({ actor: worker ? "capture-worker" : `github:${OWNER_GITHUB_ID}` }); clearIngestionStatusCache(); return json(result, result.state === "configuration-required" ? 409 : result.state === "partial" ? 503 : 200); }
  catch { return json({ error: "Capture held; storage is unavailable." }, 503); }
}

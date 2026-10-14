import { ingestionConfig, OWNER_GITHUB_ID } from "../../../../server/ingestion-config.mjs";
import { getIngestionStore } from "../../../../server/ingestion-store.mjs";
import { clearIngestionStatusCache } from "../../../../server/ingestion-runner.mjs";
import { authenticateOwner, sameOrigin, json } from "../../../../server/owner-auth.mjs";
export const dynamic = "force-dynamic";
export async function POST(request: Request) {
  if (!sameOrigin(request) || !await authenticateOwner(request)) return json({ error: "Owner sign-in required." }, 401);
  // Fixed operations in query; no unbounded bodies, arbitrary URL, release or delete command.
  const params = new URL(request.url).searchParams;
  const action = params.get("action");
  if (params.size !== 1 || !["pause", "resume"].includes(action ?? "")) return json({ error: "Choose pause or resume." }, 400);
  if (action === "resume" && !ingestionConfig().ready) return json({ error: "Storage, identity, published runtime and capacity confirmation are required." }, 409);
  try { await (await getIngestionStore()).setPaused(action === "pause", `github:${OWNER_GITHUB_ID}`); clearIngestionStatusCache(); return json({ state: action === "pause" ? "paused" : "scheduled" }); }
  catch { return json({ error: "Storage is unavailable." }, 503); }
}

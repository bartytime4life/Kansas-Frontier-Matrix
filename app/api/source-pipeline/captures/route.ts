import { getIngestionStore } from "../../../../server/ingestion-store.mjs";
import { authenticateOwner, json } from "../../../../server/owner-auth.mjs";
export const dynamic = "force-dynamic";
export async function GET(request: Request) {
  if (!await authenticateOwner(request)) return json({ error: "Owner sign-in required." }, 401);
  try {
    const params = new URL(request.url).searchParams;
    if (!params.size) return json({ captures: await (await getIngestionStore()).list(), releaseState: "unreleased" });
    if (params.size !== 1 || params.getAll("id").length !== 1 || !/^[a-f0-9]{64}$/.test(params.get("id") ?? "")) return json({ error: "Choose one capture." }, 400);
    const id = params.get("id")!; const { bytes } = await (await getIngestionStore()).read(id);
    return new Response(bytes, { headers: { "Content-Type": "application/octet-stream", "Content-Disposition": `attachment; filename="kfm-quarantine-${id}.json"`, "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff", "Content-Security-Policy": "sandbox" } });
  } catch { return json({ error: "Capture unavailable or integrity check failed." }, 503); }
}

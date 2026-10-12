import { env } from "cloudflare:workers";
import { NextRequest } from "next/server";
import { getRawDb } from "../../../db";
import { archiveFeed } from "../../daily-archive";
import { ArchiveError, archiveHeaders, archiveCatalog, captureArchive, readArchiveCapture, reviewArchive, type ArchiveBucket } from "../../daily-archive-store";
import { GET as liveContext } from "../live-context/route";

export const dynamic = "force-dynamic";
const store = () => {
  const bucket = env.BUCKET as ArchiveBucket | undefined;
  if (!bucket) throw new ArchiveError("Archive storage is unavailable.", 503);
  return { db: getRawDb(), bucket };
};
const fail = (error: unknown) => Response.json({ error: error instanceof ArchiveError ? error.message : "Archive operation failed. Check storage and capture status before retrying." }, { status: error instanceof ArchiveError ? error.status : 503, headers: archiveHeaders });
function query(request: NextRequest) {
  const params = request.nextUrl.searchParams;
  if ([...params.keys()].some(key => !["day", "id", "action", "feed"].includes(key) || params.getAll(key).length !== 1)) throw new ArchiveError("Unsupported archive query.");
  return params;
}
export async function GET(request: NextRequest) {
  try {
    const p = query(request); const { db, bucket } = store();
    if (p.has("id")) {
      const result = await readArchiveCapture(db, bucket, p.get("id")!, p.get("action") === "download");
      if (p.get("action") === "download") return new Response(result.bytes as Uint8Array<ArrayBuffer>, { headers: { ...archiveHeaders, "Content-Type": "application/json", "Content-Disposition": `attachment; filename="${result.entry.day}-${result.entry.feed}-${result.entry.id}.json"` } });
      const reviews = (await db.prepare("SELECT state,note,reviewed_at FROM daily_archive_reviews WHERE capture_id=? ORDER BY reviewed_at DESC,id DESC").bind(result.entry.id).all()).results;
      return Response.json({ entry: result.entry, payload: result.payload, reviews }, { headers: archiveHeaders });
    }
    return Response.json(await archiveCatalog(db, p.get("day") ?? new Date().toISOString().slice(0, 10)), { headers: archiveHeaders });
  } catch (error) { return fail(error); }
}

/** Shared archive only, protected by this Site's owner-private dispatch boundary.
 * Local runtime rejects forged Host/edge identity. The custom header plus same-
 * origin check prevents browser cross-origin writes; there is no CORS grant.
 * Do not expose this writer if the Site audience becomes public/shared. */
export async function POST(request: NextRequest) {
  try {
    const origin = request.headers.get("origin");
    if (request.headers.get("x-kfm-archive-writer") !== "daily-v1" || (origin && origin !== request.nextUrl.origin) || request.headers.get("sec-fetch-site") === "cross-site") throw new ArchiveError("Archive writer authority rejected.", 403);
    const p = query(request); const { db, bucket } = store(); const action = p.get("action");
    if (action === "capture") {
      if (p.has("day") || p.has("id")) throw new ArchiveError("Captures use the actual UTC retrieval day; past days cannot be fabricated.");
      const feed = p.get("feed") ?? "";
      if (!archiveFeed(feed)) throw new ArchiveError("Choose a supported feed.");
      const result = await captureArchive(db, bucket, feed, () => liveContext(new NextRequest(new URL(`/api/live-context?feed=${feed}`, request.url), { signal: request.signal })));
      return Response.json(result, { headers: archiveHeaders });
    }
    if (!request.headers.get("content-type")?.startsWith("application/json")) throw new ArchiveError("JSON input required.");
    const reader = request.body?.getReader(); let text = ""; let size = 0; const decoder = new TextDecoder();
    if (!reader) throw new ArchiveError("Input required.");
    for (;;) { const {done,value} = await reader.read(); if(done) break; size += value.length; if(size > 4096) { await reader.cancel(); throw new ArchiveError("Input too large.",413); } text += decoder.decode(value,{stream:true}); } text += decoder.decode();
    const body = JSON.parse(text);
    if (action === "review") return Response.json(await reviewArchive(db, body.id, body.state, body.note), { headers: archiveHeaders });
    if (action === "settings") {
      if (!Number.isSafeInteger(body.budget) || body.budget < 16777216 || body.budget > 1_000_000_000_000 || typeof body.paused !== "boolean") throw new ArchiveError("Choose a storage budget between 16,777,216 bytes and 1 TB and a pause setting.");
      await db.prepare("INSERT INTO daily_archive_settings(id,budget,paused) VALUES(1,?,?) ON CONFLICT(id) DO UPDATE SET budget=excluded.budget,paused=excluded.paused").bind(body.budget, body.paused ? 1 : 0).run();
      return Response.json({ budget: body.budget, paused: body.paused }, { headers: archiveHeaders });
    }
    throw new ArchiveError("Unknown archive action.");
  } catch (error) { return fail(error); }
}

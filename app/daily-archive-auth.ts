import { env } from "cloudflare:workers";
import { ArchiveError } from "./daily-archive-store";

function matchesToken(request: Request, expected: unknown) {
  if (typeof expected !== "string" || !/^[A-Za-z0-9_-]{43,128}$/.test(expected)) return false;
  const actual = request.headers.get("authorization") ?? "";
  const value = `Bearer ${expected}`;
  let difference = actual.length ^ value.length;
  for (let i = 0; i < value.length; i++) difference |= value.charCodeAt(i) ^ (actual.charCodeAt(i) || 0);
  return difference === 0;
}

/** No browser identity is provided by this public application. A separately
 * configured loopback machine capability remains available to local tooling. */
export async function archiveOwner(request: Request) {
  if (env.KFM_ARCHIVE_LOCAL_OWNER_TOKEN !== env.KFM_ARCHIVE_WORKER_TOKEN && new URL(request.url).hostname === "127.0.0.1" && matchesToken(request, env.KFM_ARCHIVE_LOCAL_OWNER_TOKEN)) return;
  throw new ArchiveError("Private archive access is unavailable in this application.", 401);
}

export function archiveWorker(request: Request) {
  return matchesToken(request, env.KFM_ARCHIVE_WORKER_TOKEN);
}

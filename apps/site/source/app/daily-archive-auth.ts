import { env } from "cloudflare:workers";
import { getChatGPTUser } from "./chatgpt-auth";
import { ArchiveError } from "./daily-archive-store";

function matchesToken(request: Request, expected: unknown) {
  if (typeof expected !== "string" || !/^[A-Za-z0-9_-]{43,128}$/.test(expected)) return false;
  const actual = request.headers.get("authorization") ?? "";
  const value = `Bearer ${expected}`;
  let difference = actual.length ^ value.length;
  for (let i = 0; i < value.length; i++) difference |= value.charCodeAt(i) ^ (actual.charCodeAt(i) || 0);
  return difference === 0;
}

/** Hosted identity comes from Sites dispatch; the local wrapper rejects forged
 * identity headers and explicitly supplies a separate owner capability. */
export async function archiveOwner(request: Request) {
  if (env.KFM_ARCHIVE_LOCAL_OWNER_TOKEN !== env.KFM_ARCHIVE_WORKER_TOKEN && new URL(request.url).hostname === "127.0.0.1" && matchesToken(request, env.KFM_ARCHIVE_LOCAL_OWNER_TOKEN)) return;
  const user = await getChatGPTUser();
  if (!user) throw new ArchiveError("Sign in as an archive owner or supply local archive access.", 401);
  const ids = String(env.KFM_ARCHIVE_OWNER_IDS ?? "").split(",").map(value => value.trim()).filter(Boolean);
  const emails = String(env.KFM_ARCHIVE_OWNER_EMAILS ?? "").split(",").map(value => value.trim().toLowerCase()).filter(Boolean);
  if (!ids.length && !emails.length) throw new ArchiveError("Archive owner access is not configured.", 503);
  if (!(user.id && ids.includes(user.id)) && !emails.includes(user.email.toLowerCase())) throw new ArchiveError("Archive owner access required.", 403);
}

export function archiveWorker(request: Request) {
  return matchesToken(request, env.KFM_ARCHIVE_WORKER_TOKEN);
}

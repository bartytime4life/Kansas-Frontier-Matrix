import { env } from "cloudflare:workers";
import { getRawDb } from "../db";
import { getChatGPTUser } from "./chatgpt-auth";
import { WaterAdminError, type WaterAdminBucket, type WaterAdminDb, type WaterAdminStore } from "./governed-water-admin";

export const waterAdminHeaders = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" };

export function waterAdminStore(): WaterAdminStore {
  const bucket = env.BUCKET as WaterAdminBucket | undefined;
  if (!bucket) throw new WaterAdminError("STORAGE_UNAVAILABLE", 503);
  return { db: getRawDb() as unknown as WaterAdminDb, bucket };
}

export function waterSameOrigin(request: Request) {
  if (request.headers.get("origin") !== new URL(request.url).origin || request.headers.get("sec-fetch-site") === "cross-site") throw new WaterAdminError("SAME_ORIGIN_REQUIRED", 403);
}

// Owner allowlist, configured in Sites runtime settings. Missing configuration keeps activation closed.
export async function waterOwner() {
  const user = await getChatGPTUser();
  if (!user) throw new WaterAdminError("SIGN_IN_REQUIRED", 401);
  const ids = String(env.KFM_WATER_OWNER_IDS ?? "").split(",").map((x) => x.trim()).filter(Boolean);
  const emails = String(env.KFM_WATER_OWNER_EMAILS ?? "").split(",").map((x) => x.trim().toLowerCase()).filter(Boolean);
  if (!ids.length && !emails.length) throw new WaterAdminError("WATER_RELEASE_NOT_CONFIGURED", 503);
  if (!(user.id && ids.includes(user.id)) && !emails.includes(user.email.toLowerCase())) throw new WaterAdminError("OWNER_REQUIRED", 403);
  return user;
}

// Staging token for the owner's local release tool. It can store packages but never activate them.
export function waterWorker(request: Request) {
  const expected = String(env.KFM_WATER_WORKER_TOKEN ?? "");
  const actual = request.headers.get("authorization")?.replace(/^Bearer /, "") ?? "";
  if (expected.length < 32) throw new WaterAdminError("WATER_STAGING_NOT_CONFIGURED", 503);
  const a = new TextEncoder().encode(expected), b = new TextEncoder().encode(actual);
  let difference = a.length ^ b.length;
  for (let index = 0; index < a.length; index++) difference |= a[index] ^ (b[index] ?? 0);
  if (difference !== 0) throw new WaterAdminError("STAGING_TOKEN_REQUIRED", 403);
}

export async function waterActor(user: { id: string | null; email: string }) {
  const bytes = new TextEncoder().encode(user.id ? `id:${user.id}` : `email:${user.email.toLowerCase()}`);
  const hash = await crypto.subtle.digest("SHA-256", bytes);
  return "owner:" + [...new Uint8Array(hash)].map((n) => n.toString(16).padStart(2, "0")).join("").slice(0, 32);
}

export function waterAdminFailure(error: unknown): Response {
  const known = error instanceof WaterAdminError;
  if (!known) console.error(JSON.stringify({ event: "water_admin_error", component: "site-water" }));
  return Response.json({ outcome: "ERROR", reason_code: known ? error.message : "WATER_ADMIN_UNAVAILABLE" }, { status: known ? error.status : 503, headers: waterAdminHeaders });
}

export async function readBoundedText(request: Request, limit: number): Promise<string> {
  if (Number(request.headers.get("content-length") ?? 0) > limit) throw new WaterAdminError("REQUEST_TOO_LARGE", 413);
  const raw = await request.arrayBuffer();
  if (raw.byteLength > limit) throw new WaterAdminError("REQUEST_TOO_LARGE", 413);
  try { return new TextDecoder("utf-8", { fatal: true }).decode(raw); } catch { throw new WaterAdminError("REQUEST_NOT_UTF8", 400); }
}

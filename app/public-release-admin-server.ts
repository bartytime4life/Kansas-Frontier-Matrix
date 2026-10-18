import { env } from "cloudflare:workers";
import { getRawDb } from "../db";
import { waterActor, waterOwner, waterSameOrigin, waterWorker, waterAdminHeaders } from "./governed-water-admin-server";
import { WaterAdminError } from "./governed-water-admin";
import { parseWaterJson } from "./governed-water";
import { PUBLIC_ASSET_FAMILIES, activatePublicDelivery, withdrawPublicDelivery, publicAuthorizationStatus, publicPinnedEntry } from "./public-release-server";
import { PublicReleaseError, PUBLIC_ARTIFACT_LIMIT, readPublicArtifact, publicReleaseGate, assertPublicRequestTarget, type PublicBucket, type PublicFamily } from "./public-release";

const familyCheck = (family: string) => {
  if (!PUBLIC_ASSET_FAMILIES.includes(family as typeof PUBLIC_ASSET_FAMILIES[number])) throw new PublicReleaseError("PUBLIC_FAMILY_UNAVAILABLE", 404);
  return family as PublicFamily;
};
const failure = (error: unknown) => Response.json({ outcome: "ERROR", reason_code: error instanceof PublicReleaseError || error instanceof WaterAdminError ? error.message : "PUBLIC_ADMIN_UNAVAILABLE" }, { status: error instanceof PublicReleaseError || error instanceof WaterAdminError ? error.status : 503, headers: waterAdminHeaders });
async function boundedBytes(request: Request, limit: number) {
  if (!Number.isSafeInteger(limit) || limit < 1 || limit > PUBLIC_ARTIFACT_LIMIT || Number(request.headers.get("content-length") ?? 0) > limit) throw new PublicReleaseError("REQUEST_TOO_LARGE", 413);
  const reader = request.body?.getReader(); if (!reader) throw new PublicReleaseError("REQUEST_REQUIRED", 400);
  const chunks: Uint8Array[] = []; let total = 0;
  for (;;) { const { done, value } = await reader.read(); if (done) break; total += value.length;
    if (total > limit) { await reader.cancel(); throw new PublicReleaseError("REQUEST_TOO_LARGE", 413); } chunks.push(value); }
  const bytes = new Uint8Array(total); let offset = 0; for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  return bytes;
}
async function body(request: Request) {
  if (!request.headers.get("content-type")?.startsWith("application/json")) throw new PublicReleaseError("JSON_REQUIRED", 415);
  let value;
  try { value = parseWaterJson(new TextDecoder("utf-8", { fatal: true }).decode(await boundedBytes(request, 4096))); } catch (error) { if (error instanceof PublicReleaseError) throw error; throw new PublicReleaseError("PUBLIC_ADMIN_REQUEST_INVALID", 400); }
  if (!value || typeof value !== "object" || Array.isArray(value)) throw new PublicReleaseError("PUBLIC_ADMIN_REQUEST_INVALID", 400);
  return value as Record<string, unknown>;
}
export async function publicDeliveryStatus(request: Request, family: string) {
  try {
    const selected = familyCheck(family);
    if (request.headers.has("authorization")) waterWorker(request); else await waterOwner();
    if (new URL(request.url).search) throw new PublicReleaseError("INVALID_QUERY", 400);
    const authorization = await publicAuthorizationStatus(selected), authorized = authorization.authorized_packages;
    const active = await getRawDb().prepare("SELECT package_id,previous_package_id,revision,state FROM public_delivery_active WHERE family=?").bind(selected).first<{ package_id: string; previous_package_id: string | null; revision: number; state: string }>();
    return Response.json({ active_package_id: active?.package_id ?? null, previous_package_id: active?.previous_package_id ?? null, revision: active?.revision ?? 0,
      state: active?.state ?? "INACTIVE", decision_expires_at: authorized.find(item => item.package_id === active?.package_id)?.expires_at ?? null, ...authorization }, { headers: waterAdminHeaders });
  } catch (error) { return failure(error); }
}
export async function publicDeliveryStage(request: Request, family: string) {
  try {
    const selected = familyCheck(family); waterWorker(request);
    const origin = request.headers.get("origin");
    if (origin && origin !== new URL(request.url).origin || request.headers.get("sec-fetch-site") === "cross-site") throw new PublicReleaseError("SAME_ORIGIN_REQUIRED", 403);
    if (request.headers.get("content-type") !== "application/octet-stream") throw new PublicReleaseError("OCTET_STREAM_REQUIRED", 415);
    const params = new URL(request.url).searchParams;
    if ([...params.keys()].some(key => !["package_id", "name"].includes(key) || params.getAll(key).length !== 1) || !params.has("package_id") || !params.has("name")) throw new PublicReleaseError("PUBLIC_STAGE_QUERY_INVALID", 400);
    const entry = await publicPinnedEntry(selected, params.get("package_id")!), artifact = entry.artifacts.find(item => item.name === params.get("name"));
    assertPublicRequestTarget(entry, request);
    if (!artifact) throw new PublicReleaseError("PUBLIC_ARTIFACT_UNAVAILABLE", 404);
    const bytes = await boundedBytes(request, artifact.bytes);
    const actual = "sha256:" + [...new Uint8Array(await crypto.subtle.digest("SHA-256", bytes))].map(value => value.toString(16).padStart(2, "0")).join("");
    if (bytes.length !== artifact.bytes || actual !== artifact.sha256) throw new PublicReleaseError("PUBLIC_ARTIFACT_INTEGRITY_HOLD", 400);
    const bucket = (env as unknown as { BUCKET?: PublicBucket & { put(key: string, value: Uint8Array<ArrayBuffer>, options?: unknown): Promise<unknown> } }).BUCKET;
    if (!bucket) throw new PublicReleaseError("PUBLIC_RELEASE_STORE_UNAVAILABLE");
    const existing = await bucket.get(artifact.object_key);
    if (existing) await readPublicArtifact(bucket, entry, artifact.name, async () => true);
    else {
      const now = publicReleaseGate(entry, new Date().toISOString()); if (now !== "ELIGIBLE") throw new PublicReleaseError(now, 404);
      await bucket.put(artifact.object_key, bytes, { httpMetadata: { contentType: artifact.media_type } });
    }
    await getRawDb().prepare("INSERT OR IGNORE INTO public_delivery_staging_events(family,package_id,artifact_name,artifact_sha256,bytes,staged_at,actor) VALUES(?,?,?,?,?,?,'staging-token')")
      .bind(selected, entry.package_id, artifact.name, artifact.sha256, artifact.bytes, new Date().toISOString()).run();
    return Response.json({ package_id: entry.package_id, name: artifact.name, state: "ARTIFACT_STORED", activated: false }, { headers: waterAdminHeaders });
  } catch (error) { return failure(error); }
}
export async function publicDeliveryActivate(request: Request, family: string) {
  try {
    const selected = familyCheck(family); waterSameOrigin(request); const owner = await waterOwner();
    if (new URL(request.url).search) throw new PublicReleaseError("INVALID_QUERY", 400);
    const requestBody = await body(request);
    if (Object.keys(requestBody).some(key => !["package_id", "expected_active", "rollback"].includes(key)) || typeof requestBody.package_id !== "string" || !("expected_active" in requestBody) || !(requestBody.expected_active === null || typeof requestBody.expected_active === "string") || requestBody.rollback !== undefined && typeof requestBody.rollback !== "boolean") throw new PublicReleaseError("PUBLIC_ACTIVATION_INVALID", 400);
    assertPublicRequestTarget(await publicPinnedEntry(selected, requestBody.package_id), request);
    return Response.json(await activatePublicDelivery(selected, requestBody.package_id, requestBody.expected_active, await waterActor(owner), requestBody.rollback === true), { headers: waterAdminHeaders });
  } catch (error) { return failure(error); }
}
export async function publicDeliveryWithdraw(request: Request, family: string) {
  try {
    const selected = familyCheck(family); waterSameOrigin(request); const owner = await waterOwner();
    if (new URL(request.url).search) throw new PublicReleaseError("INVALID_QUERY", 400);
    const requestBody = await body(request);
    if (Object.keys(requestBody).sort().join("|") !== "expected_active|package_id" || typeof requestBody.package_id !== "string" || requestBody.package_id !== requestBody.expected_active) throw new PublicReleaseError("PUBLIC_WITHDRAW_INVALID", 400);
    return Response.json(await withdrawPublicDelivery(selected, requestBody.package_id, await waterActor(owner)), { headers: waterAdminHeaders });
  } catch (error) { return failure(error); }
}

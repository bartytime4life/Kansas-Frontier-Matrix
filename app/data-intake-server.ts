import { env } from "cloudflare:workers";
import { getRawDb } from "../db";
import { getChatGPTUser } from "./chatgpt-auth";
import { MAX_UPLOAD_BYTES, type Review, type Submission } from "./data-intake";

type StoredObject = { body: ReadableStream; size: number };
type IntakeBucket = { put(key: string, value: ArrayBuffer, options?: unknown): Promise<unknown>; get(key: string): Promise<StoredObject | null>; delete(key: string): Promise<unknown> };
export class IntakeError extends Error { constructor(message: string, readonly status = 400) { super(message); } }
export async function intakeUser() {
  const user = await getChatGPTUser();
  if (!user) throw new IntakeError("Sign in with ChatGPT to use data submissions.", 401);
  // Older dispatch deployments forward email without a site-scoped user id.
  // Use only dispatch-authenticated identity, never a form field or URL role.
  const key = await sha256(new TextEncoder().encode(user.id ? `id:${user.id}` : `email:${user.email.toLowerCase()}`).buffer as ArrayBuffer);
  const ids = String(env.KFM_STEWARD_USER_IDS ?? "").split(",").map((v) => v.trim()).filter(Boolean);
  const emails = String(env.KFM_STEWARD_EMAILS ?? "").split(",").map((v) => v.trim().toLowerCase()).filter(Boolean);
  return { key, name: user.displayName, steward: Boolean(user.id && ids.includes(user.id)) || emails.includes(user.email.toLowerCase()) };
}
export function intakeStore() {
  const db = getRawDb();
  const bucket = env.BUCKET as IntakeBucket | undefined;
  if (!bucket) throw new IntakeError("Data storage is temporarily unavailable. Your form has been kept; please retry.", 503);
  return { db, bucket };
}
export const intakeHeaders = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" };
export function sameOrigin(request: Request) {
  if (request.headers.get("origin") !== new URL(request.url).origin || request.headers.get("sec-fetch-site") === "cross-site") throw new IntakeError("Open the submission form on this Site and try again.", 403);
}
export async function boundedForm(request: Request) {
  const limit = MAX_UPLOAD_BYTES + 64 * 1024;
  if (!request.headers.get("content-type")?.startsWith("multipart/form-data;") || Number(request.headers.get("content-length")) > limit || !request.body) throw new IntakeError("Choose a file of 10 MB or smaller.", 413);
  const reader = request.body.getReader(); const chunks: Uint8Array[] = []; let length = 0;
  for (;;) { const { done, value } = await reader.read(); if (done) break; length += value.length; if (length > limit) { await reader.cancel(); throw new IntakeError("Choose a file of 10 MB or smaller.", 413); } chunks.push(value); }
  const bytes = new Uint8Array(length); let offset = 0; for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  try { return await new Response(bytes, { headers: { "Content-Type": request.headers.get("content-type")! } }).formData(); }
  catch { throw new IntakeError("The upload could not be read. Choose the file again."); }
}
export async function sha256(bytes: ArrayBuffer) { return Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", bytes)), (b) => b.toString(16).padStart(2,"0")).join(""); }
export function intakeFailure(error: unknown) {
  if (error instanceof IntakeError) return Response.json({ error: error.message }, { status: error.status, headers: intakeHeaders });
  console.error("KFM_INTAKE_STORAGE_FAILED", error instanceof Error ? error.name : "Unknown error");
  return Response.json({ error: "Data storage is temporarily unavailable. Your input has been kept; please retry." }, { status: 503, headers: intakeHeaders });
}
export const submissionColumns = `id, owner_name AS ownerName, title, source_id AS sourceId, source_url AS sourceUrl, description, license, sensitivity, start_date AS startDate, end_date AS endDate, file_name AS fileName, file_bytes AS fileBytes, file_sha256 AS fileSha256, status, version, created_at AS createdAt, updated_at AS updatedAt`;
export async function ownedSubmission(id: string, user: Awaited<ReturnType<typeof intakeUser>>) {
  if (!/^[0-9a-f-]{36}$/.test(id)) throw new IntakeError("Submission not found.", 404);
  const { db } = intakeStore();
  const row = await db.prepare(`SELECT ${submissionColumns}, owner_key AS ownerKey, object_key AS objectKey FROM data_submissions WHERE id = ?`).bind(id).first<Submission & { ownerKey: string; objectKey: string }>();
  if (!row || !user.steward && row.ownerKey !== user.key) throw new IntakeError("Submission not found.", 404);
  return row;
}
export async function submissionReviews(id: string) {
  return (await intakeStore().db.prepare("SELECT id, reviewer_name AS reviewerName, previous_status AS previousStatus, status, note, version, created_at AS createdAt FROM data_submission_reviews WHERE submission_id = ? ORDER BY version").bind(id).all<Review>()).results;
}

import { validateSubmission, validateUpload } from "../../data-intake";
import { boundedForm, intakeFailure, intakeHeaders, IntakeError, intakeStore, intakeUser, sameOrigin, sha256, submissionColumns } from "../../data-intake-server";
export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  try {
    const user = await intakeUser(); const { db } = intakeStore();
    const params = new URL(request.url).searchParams;
    const queue = params.get("scope") === "review";
    if (queue && !user.steward) throw new IntakeError("This review queue is available to assigned stewards.", 403);
    const cursor = params.get("before");
    if (cursor && !/^\d{4}-\d\d-\d\dT[\d:.]+Z\|[0-9a-f-]{36}$/.test(cursor)) throw new IntakeError("Invalid page cursor.");
    const [createdAt, id] = cursor?.split("|") ?? [];
    const predicates = [queue ? "1=1" : "owner_key = ?", ...(cursor ? ["(created_at < ? OR (created_at = ? AND id < ?))"] : [])];
    const args = [...(queue ? [] : [user.key]), ...(cursor ? [createdAt, createdAt, id] : [])];
    const rows = (await db.prepare(`SELECT ${submissionColumns} FROM data_submissions WHERE ${predicates.join(" AND ")} ORDER BY created_at DESC, id DESC LIMIT 31`).bind(...args).all()).results;
    const items = rows.slice(0,30); const last = items.at(-1);
    return Response.json({ user: { name: user.name, steward: user.steward }, items, nextCursor: rows.length > 30 && last ? `${last.createdAt}|${last.id}` : null }, { headers: intakeHeaders });
  } catch (error) { return intakeFailure(error); }
}

export async function POST(request: Request) {
  try {
    sameOrigin(request); const user = await intakeUser(); const { db, bucket } = intakeStore();
    const today = new Date(Date.now() - 86_400_000).toISOString();
    const count = await db.prepare("SELECT COUNT(*) AS n FROM data_submissions WHERE owner_key = ? AND created_at >= ?").bind(user.key, today).first<{ n: number }>();
    if ((count?.n ?? 0) >= 20) throw new IntakeError("You have submitted 20 files in the last 24 hours. Please try tomorrow.", 429);
    const form = await boundedForm(request);
    if ([...form.keys()].some((key) => form.getAll(key).length !== 1)) throw new IntakeError("Each submission field must appear once.");
    let fields; try { fields = validateSubmission(Object.fromEntries(form)); } catch (error) { throw new IntakeError((error as Error).message); }
    if (form.get("permission") !== "yes") throw new IntakeError("Confirm that you are allowed to share this file for steward review.");
    const file = form.get("file");
    if (!file || typeof file === "string") throw new IntakeError("Choose a data file to submit.");
    try { validateUpload(file.name, file.size); } catch (error) { throw new IntakeError((error as Error).message); }
    const bytes = await file.arrayBuffer(); const hash = await sha256(bytes); const id = crypto.randomUUID();
    const objectKey = `quarantine/${user.key}/${id}`; const now = new Date().toISOString();
    await bucket.put(objectKey, bytes, { httpMetadata: { contentType: "application/octet-stream" } });
    try {
      await db.prepare("INSERT INTO data_submissions (id, owner_key, owner_name, title, source_id, source_url, description, license, sensitivity, start_date, end_date, file_name, file_bytes, file_sha256, object_key, status, version, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'submitted', 1, ?, ?)").bind(id, user.key, user.name, fields.title, fields.sourceId, fields.sourceUrl, fields.description, fields.license, fields.sensitivity, fields.startDate, fields.endDate, file.name, file.size, hash, objectKey, now, now).run();
    } catch (error) { await bucket.delete(objectKey).catch(() => undefined); throw error; }
    return Response.json({ id, status: "submitted", fileSha256: hash }, { status: 201, headers: intakeHeaders });
  } catch (error) { return intakeFailure(error); }
}

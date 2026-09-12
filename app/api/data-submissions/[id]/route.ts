import { validateReview } from "../../../data-intake";
import { intakeFailure, intakeHeaders, IntakeError, intakeStore, intakeUser, ownedSubmission, sameOrigin, submissionReviews } from "../../../data-intake-server";
export const dynamic = "force-dynamic";
type Context = { params: Promise<{ id: string }> };

export async function GET(request: Request, context: Context) {
  try {
    const user = await intakeUser(); const { id } = await context.params; const row = await ownedSubmission(id, user);
    if (new URL(request.url).searchParams.get("download") === "1") {
      const object = await intakeStore().bucket.get(row.objectKey);
      if (!object) throw new IntakeError("The uploaded file is temporarily unavailable. Please contact a steward.", 503);
      return new Response(object.body, { headers: { ...intakeHeaders, "Content-Type": "application/octet-stream", "Content-Length": String(object.size), "Content-Disposition": `attachment; filename="kfm-${id}.${row.fileName.split(".").pop()?.replace(/[^a-z0-9]/gi, "")}"; filename*=UTF-8''${encodeURIComponent(row.fileName).replace(/['()]/g, escape)}`, "Content-Security-Policy": "sandbox; default-src 'none'" } });
    }
    const { ownerKey: _owner, objectKey: _object, ...submission } = row;
    return Response.json({ submission, reviews: await submissionReviews(id), canReview: user.steward }, { headers: intakeHeaders });
  } catch (error) { return intakeFailure(error); }
}

export async function PATCH(request: Request, context: Context) {
  try {
    sameOrigin(request); const user = await intakeUser();
    if (!user.steward) throw new IntakeError("Only assigned stewards can record a review.", 403);
    const { id } = await context.params; const row = await ownedSubmission(id, user);
    if (Number(request.headers.get("content-length")) > 16_384) throw new IntakeError("Review note is too long.", 413);
    const bodyText = await request.text(); if (bodyText.length > 16_384) throw new IntakeError("Review note is too long.", 413);
    let body; try { body = JSON.parse(bodyText); } catch { throw new IntakeError("The review could not be read."); }
    if (!body || !Number.isInteger(body.version) || body.version !== row.version) throw new IntakeError("Another steward updated this submission. Reload it before reviewing.", 409);
    let review; try { review = validateReview(row, body.status, body.note); } catch (error) { throw new IntakeError((error as Error).message); }
    const now = new Date().toISOString(); const reviewId = crypto.randomUUID(); const { db } = intakeStore();
    // Conditional update and audit insert are one D1 transaction. The insert is
    // gated by changes(), so a losing concurrent reviewer cannot append a note.
    const result = await db.batch([
      db.prepare("UPDATE data_submissions SET status = ?, version = version + 1, updated_at = ? WHERE id = ? AND version = ?").bind(review.status, now, id, row.version),
      db.prepare("INSERT INTO data_submission_reviews (id, submission_id, reviewer_key, reviewer_name, previous_status, status, note, version, created_at) SELECT ?, ?, ?, ?, ?, ?, ?, ?, ? WHERE changes() = 1").bind(reviewId, id, user.key, user.name, row.status, review.status, review.note, row.version + 1, now),
    ]);
    if (result[0].meta.changes !== 1) throw new IntakeError("Another steward updated this submission. Reload it before reviewing.", 409);
    return Response.json({ status: review.status, version: row.version + 1 }, { headers: intakeHeaders });
  } catch (error) { return intakeFailure(error); }
}

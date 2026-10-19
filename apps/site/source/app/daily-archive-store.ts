import { ARCHIVE_ATTEMPTS, ARCHIVE_DEFAULT_BUDGET, ARCHIVE_MAX_PAYLOAD, DAILY_FEEDS, archiveDay, archiveFeed, validateArchivePayload, type ArchiveEntry, type DailyFeed } from "./daily-archive";

type Statement = { bind(...values: unknown[]): Statement; first<T>(): Promise<T | null>; all<T>(): Promise<{ results: T[] }>; run(): Promise<unknown> };
export type ArchiveDb = { prepare(sql: string): Statement; batch(statements: Statement[]): Promise<Array<{ meta?: { changes?: number } }>> };
export type ArchiveBucket = { put(key: string, value: Uint8Array, options?: unknown): Promise<unknown>; get(key: string): Promise<{ size: number; arrayBuffer(): Promise<ArrayBuffer> } | null> };
export class ArchiveError extends Error { constructor(message: string, readonly status = 400) { super(message); } }
export const archiveHeaders = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff" };
export const archiveHash = async (bytes: Uint8Array) => Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", bytes as Uint8Array<ArrayBuffer>)), b => b.toString(16).padStart(2, "0")).join("");
const fields = `c.*, COALESCE((SELECT state FROM daily_archive_reviews r WHERE r.capture_id=c.id ORDER BY reviewed_at DESC, id DESC LIMIT 1),'pending') AS review, (SELECT note FROM daily_archive_reviews r WHERE r.capture_id=c.id ORDER BY reviewed_at DESC, id DESC LIMIT 1) AS review_note`;

export async function archiveStorage(db: ArchiveDb) {
  const settings = await db.prepare("SELECT budget, paused FROM daily_archive_settings WHERE id=1").first<{ budget: number; paused: number }>();
  const usage = await db.prepare("SELECT COALESCE(SUM(bytes),0) AS used FROM daily_archive_captures").first<{ used: number }>();
  return { used: usage?.used ?? 0, budget: settings?.budget ?? ARCHIVE_DEFAULT_BUDGET, paused: Boolean(settings?.paused) };
}

export async function archiveCatalog(db: ArchiveDb, day: string) {
  if (!archiveDay(day)) throw new ArchiveError("Choose an exact UTC calendar day.");
  const [entries, days, span, storage] = await Promise.all([
    db.prepare(`SELECT ${fields} FROM daily_archive_captures c WHERE day=? ORDER BY feed, attempt DESC`).bind(day).all<ArchiveEntry>(),
    db.prepare("SELECT day, COUNT(*) AS captures FROM daily_archive_captures WHERE status IN ('ready','empty','partial') GROUP BY day ORDER BY day DESC LIMIT 366").all<{ day: string; captures: number }>(),
    db.prepare("SELECT MIN(day) AS earliestDay, MAX(day) AS latestDay FROM daily_archive_captures").first<{ earliestDay: string | null; latestDay: string | null }>(),
    archiveStorage(db),
  ]);
  return { day, entries: entries.results, days: days.results, feeds: DAILY_FEEDS, storage, ...span };
}

export async function boundedArchiveBytes(response: Response) {
  if (!response.body || Number(response.headers.get("content-length")) > ARCHIVE_MAX_PAYLOAD) throw new ArchiveError("CAPTURE_TOO_LARGE", 413);
  const reader = response.body.getReader(); const chunks: Uint8Array[] = []; let length = 0;
  for (;;) { const { done, value } = await reader.read(); if (done) break; length += value.length; if (length > ARCHIVE_MAX_PAYLOAD) { await reader.cancel(); throw new ArchiveError("CAPTURE_TOO_LARGE", 413); } chunks.push(value); }
  const bytes = new Uint8Array(length); let offset = 0; for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  return bytes;
}

/** One globally leased writer keeps budget reservations and per-day attempts serial.
 * Bytes remain reserved after a crash: no unindexed object can evade the budget.
 * R2 is written and read back before an entry becomes displayable in D1. */
export async function captureArchive(db: ArchiveDb, bucket: ArchiveBucket, feed: DailyFeed, acquire: () => Promise<Response>, now = new Date()) {
  if (!archiveFeed(feed)) throw new ArchiveError("Unknown capture source.");
  const started = now.toISOString(); const day = started.slice(0, 10); const token = crypto.randomUUID();
  const expires = new Date(now.getTime() + 10 * 60_000).toISOString();
  const lock = await db.batch([db.prepare("INSERT INTO daily_archive_lock(id,token,expires_at) VALUES(1,?,?) ON CONFLICT(id) DO UPDATE SET token=excluded.token,expires_at=excluded.expires_at WHERE expires_at < ?").bind(token, expires, started)]);
  if (lock[0].meta?.changes !== 1) throw new ArchiveError("Another capture is running. Retry after it finishes.", 409);
  let reserved = false; let objectStarted = false;
  try {
    // Interrupted attempts remain inspectable and retain a conservative byte reservation.
    await db.prepare("UPDATE daily_archive_captures SET status='failed',finished_at=?,message='INTERRUPTED_CAPTURE: reserved bytes retained for recovery' WHERE status='running' AND started_at < ?").bind(started, new Date(now.getTime() - 10 * 60_000).toISOString()).run();
    const prior = await db.prepare("SELECT * FROM daily_archive_captures WHERE day=? AND feed=? ORDER BY attempt DESC").bind(day, feed).all<ArchiveEntry>();
    const complete = prior.results.find(entry => entry.status === "ready" || entry.status === "empty");
    if (complete) return { outcome: "already-captured", id: complete.id, day, feed };
    if (prior.results.length >= ARCHIVE_ATTEMPTS) throw new ArchiveError("Daily retry limit reached; previous attempts are preserved.", 409);
    const storage = await archiveStorage(db);
    if (storage.paused) throw new ArchiveError("Daily capture is paused.", 409);
    if (storage.used + ARCHIVE_MAX_PAYLOAD > storage.budget) throw new ArchiveError("Storage budget reached. Existing history is preserved; increase the budget to continue.", 507);
    await db.prepare("INSERT INTO daily_archive_captures(id,day,feed,attempt,status,started_at,bytes) VALUES(?,?,?,?,'running',?,?)").bind(token, day, feed, prior.results.length + 1, started, ARCHIVE_MAX_PAYLOAD).run();
    reserved = true;
    const response = await acquire();
    if (!response.ok) throw new ArchiveError(`UPSTREAM_HTTP_${response.status}`, 502);
    const bytes = await boundedArchiveBytes(response);
    const payload = validateArchivePayload(JSON.parse(new TextDecoder().decode(bytes)), feed);
    const hash = await archiveHash(bytes); const key = `daily-archive/v1/${day}/${feed}/${token}/${hash}.json`;
    const stillOwns = await db.prepare("SELECT token FROM daily_archive_lock WHERE id=1 AND token=? AND expires_at > ?").bind(token, new Date().toISOString()).first();
    if (!stillOwns) throw new ArchiveError("CAPTURE_LEASE_EXPIRED", 409);
    // Record the object identity before putting it, so interrupted writes can be reconciled.
    await db.prepare("UPDATE daily_archive_captures SET bytes=?,sha256=?,object_key=? WHERE id=?").bind(bytes.length, hash, key, token).run();
    objectStarted = true;
    await bucket.put(key, bytes, { httpMetadata: { contentType: "application/json" } });
    const stored = await bucket.get(key);
    if (!stored || stored.size !== bytes.length || await archiveHash(new Uint8Array(await stored.arrayBuffer())) !== hash) throw new ArchiveError("CAPTURE_READBACK_FAILED", 503);
    const status = payload.truncated ? "partial" : payload.state;
    await db.prepare("UPDATE daily_archive_captures SET status=?,finished_at=?,feature_count=?,source_time=?,source_day=?,message=? WHERE id=?").bind(status, new Date().toISOString(), payload.featureCount, payload.upstreamUpdatedAt, payload.sourceDay ?? null, payload.limitation, token).run();
    return { outcome: "captured", id: token, day, feed, status, bytes: bytes.length, sha256: hash };
  } catch (error) {
    if (reserved) await db.prepare("UPDATE daily_archive_captures SET status='failed',finished_at=?,bytes=CASE WHEN ? THEN bytes ELSE 0 END,message=? WHERE id=?").bind(new Date().toISOString(), objectStarted ? 1 : 0, error instanceof ArchiveError ? error.message : "CAPTURE_VALIDATION_OR_STORAGE_FAILED", token).run();
    throw error;
  } finally {
    await db.prepare("DELETE FROM daily_archive_lock WHERE id=1 AND token=?").bind(token).run();
  }
}

export async function readArchiveCapture(db: ArchiveDb, bucket: ArchiveBucket, id: string, inspectHeld = false) {
  if (!/^[0-9a-f-]{36}$/.test(id)) throw new ArchiveError("Capture not found.", 404);
  const entry = await db.prepare(`SELECT ${fields} FROM daily_archive_captures c WHERE id=?`).bind(id).first<ArchiveEntry>();
  if (!entry || !["ready", "empty", "partial"].includes(entry.status) || !entry.object_key || !entry.sha256) throw new ArchiveError("No stored capture is available.", 404);
  if (entry.review === "held" && !inspectHeld) throw new ArchiveError("This capture is held for review and hidden from the map.", 409);
  const object = await bucket.get(entry.object_key);
  if (!object || object.size !== entry.bytes || object.size > ARCHIVE_MAX_PAYLOAD) throw new ArchiveError("Stored capture is missing or has changed.", 503);
  const bytes = new Uint8Array(await object.arrayBuffer());
  if (await archiveHash(bytes) !== entry.sha256) throw new ArchiveError("Stored capture failed its checksum.", 503);
  const payload = validateArchivePayload(JSON.parse(new TextDecoder().decode(bytes)), entry.feed);
  return { entry, payload, bytes };
}

export async function reviewArchive(db: ArchiveDb, id: string, state: string, note: string) {
  if (!/^[0-9a-f-]{36}$/.test(id) || !["pending", "reviewed", "held"].includes(state) || typeof note !== "string" || !note.trim() || note.length > 1000) throw new ArchiveError("Choose a review state and enter a note (up to 1,000 characters).");
  const entry = await db.prepare("SELECT id FROM daily_archive_captures WHERE id=? AND status IN ('ready','empty','partial')").bind(id).first();
  if (!entry) throw new ArchiveError("Capture not found.", 404);
  await db.prepare("INSERT INTO daily_archive_reviews(id,capture_id,state,note,reviewed_at) VALUES(?,?,?,?,?)").bind(crypto.randomUUID(), id, state, note.trim(), new Date().toISOString()).run();
  return { id, state, note: note.trim(), boundary: "Archive review only; no source admission or release." };
}

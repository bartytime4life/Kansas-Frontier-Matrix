// Hosted water release steps. Staging stores a validated package and never activates it;
// activation needs a decision that passes the same serving gate as reads (ADR-0044).
import { parseWaterJson, parseWaterPackage, projectWater, object, WATER_PACKAGE_LIMIT } from "./governed-water";

type Statement = { bind(...values: unknown[]): Statement; first<T>(): Promise<T | null>; run(): Promise<unknown> };
export type WaterAdminDb = { prepare(query: string): Statement; batch(statements: Statement[]): Promise<Array<{ meta?: { changes?: number } }>> };
export type WaterAdminBucket = {
  get(key: string): Promise<{ size: number; text(): Promise<string> } | null>;
  put(key: string, value: string, options?: { httpMetadata?: { contentType: string } }): Promise<unknown>;
};
export type WaterAdminStore = { db: WaterAdminDb; bucket: WaterAdminBucket };
export class WaterAdminError extends Error { constructor(message: string, readonly status = 409) { super(message); } }

const DIGEST = /^sha256:[a-f0-9]{64}$/;
const requestObject = (value: unknown, reason: string) => { try { return object(value); } catch { throw new WaterAdminError(reason, 400); } };
export const waterObjectKey = (packageId: string) => `governed-water/v1/objects/${packageId.slice(7)}.json`;

async function storedPackage(store: WaterAdminStore, packageId: string) {
  const stored = await store.bucket.get(waterObjectKey(packageId));
  if (!stored || !Number.isInteger(stored.size) || stored.size < 1 || stored.size > WATER_PACKAGE_LIMIT) throw new WaterAdminError("PACKAGE_UNAVAILABLE", 404);
  const text = await stored.text();
  return { text, pkg: await parseWaterPackage(text) };
}

export async function stageWaterPackage(store: WaterAdminStore, text: string, actor: string, now: string) {
  if (new TextEncoder().encode(text).length > WATER_PACKAGE_LIMIT) throw new WaterAdminError("PACKAGE_TOO_LARGE", 413);
  let pkg;
  try { pkg = await parseWaterPackage(text); } catch { throw new WaterAdminError("PACKAGE_INVALID", 400); }
  const packageId = pkg.manifest.package_id, key = waterObjectKey(packageId);
  const existing = await store.bucket.get(key);
  if (existing) {
    if (await existing.text() !== text) throw new WaterAdminError("IMMUTABLE_OBJECT_CONFLICT");
  } else {
    await store.bucket.put(key, text, { httpMetadata: { contentType: "application/json" } });
  }
  await store.db.prepare("INSERT OR IGNORE INTO water_packages (package_id, object_key, staged_at, staged_by, state) VALUES (?, ?, ?, ?, 'STAGED')").bind(packageId, key, now, actor).run();
  const row = await store.db.prepare("SELECT state FROM water_packages WHERE package_id = ?").bind(packageId).first<{ state: string }>();
  return { package_id: packageId, state: row?.state ?? "UNKNOWN", activated: false };
}

type Active = { package_id: string; previous_package_id: string | null; revision: number };
const currentActive = (store: WaterAdminStore) =>
  store.db.prepare("SELECT package_id, previous_package_id, revision FROM water_active WHERE singleton = 1").first<Active>();

export async function activateWaterPackage(store: WaterAdminStore, body: unknown, now: string) {
  const request = requestObject(body, "ACTIVATION_REQUEST_INVALID");
  const { package_id: packageId, expected_active: expected, rollback = false } = request;
  if (typeof packageId !== "string" || !DIGEST.test(packageId) || !(expected === null || typeof expected === "string" && DIGEST.test(expected)) || typeof rollback !== "boolean") throw new WaterAdminError("ACTIVATION_REQUEST_INVALID", 400);
  const decision = requestObject(request.decision, "ACTIVATION_REQUEST_INVALID");
  const decisionJson = JSON.stringify(decision);
  if (decisionJson.length > 8192 || decision.package_id !== packageId) throw new WaterAdminError("ACTIVATION_BINDING_MISMATCH", 400);
  const staged = await store.db.prepare("SELECT state FROM water_packages WHERE package_id = ?").bind(packageId).first<{ state: string }>();
  if (staged?.state !== "STAGED") throw new WaterAdminError("PACKAGE_NOT_STAGED");
  const { pkg } = await storedPackage(store, packageId);
  if (pkg.manifest.package_id !== packageId) throw new WaterAdminError("ACTIVATION_BINDING_MISMATCH");
  const projected = await projectWater(pkg, object(parseWaterJson(decisionJson)), "layers", now);
  if (projected.envelope.outcome !== "ANSWER") throw new WaterAdminError(String(projected.envelope.reason_code));
  const current = await currentActive(store);
  if ((current?.package_id ?? null) !== expected) throw new WaterAdminError("ACTIVATION_CONFLICT");
  if (rollback && (!current || current.previous_package_id !== packageId)) throw new WaterAdminError("ROLLBACK_TARGET_MISMATCH");
  if (!rollback && pkg.manifest.rollback_target !== expected) throw new WaterAdminError("ROLLBACK_BINDING_MISMATCH");
  const revision = (current?.revision ?? 0) + 1, eventId = "water:" + crypto.randomUUID().replaceAll("-", "");
  // Compare-and-swap: the pointer write matches only the expected current row; the event row is written
  // only if that pointer write took effect. D1 runs a batch as one transaction.
  const write = current
    ? store.db.prepare("UPDATE water_active SET package_id = ?, decision_json = ?, previous_package_id = ?, revision = ? WHERE singleton = 1 AND package_id = ? AND revision = ?").bind(packageId, decisionJson, expected, revision, current.package_id, current.revision)
    : store.db.prepare("INSERT INTO water_active (singleton, package_id, decision_json, previous_package_id, revision) VALUES (1, ?, ?, NULL, 1) ON CONFLICT(singleton) DO NOTHING").bind(packageId, decisionJson);
  // changes() is the row count of the pointer write just before it in this batch, so a losing
  // concurrent request (same package, same new revision) records no event.
  const event = store.db.prepare("INSERT INTO water_activation_events (event_id, package_id, previous_package_id, decision_json, occurred_at, action) SELECT ?, ?, ?, ?, ?, ? WHERE changes() = 1")
    .bind(eventId, packageId, expected, decisionJson, now, rollback ? "ROLLBACK" : "ACTIVATE");
  const [written] = await store.db.batch([write, event]);
  if (written?.meta?.changes !== 1) throw new WaterAdminError("ACTIVATION_CONFLICT");
  return { event_id: eventId, package_id: packageId, previous_package_id: expected, revision, outcome: rollback ? "ROLLED_BACK" : "ACTIVATED" };
}

export async function withdrawWaterPackage(store: WaterAdminStore, body: unknown, now: string) {
  const request = requestObject(body, "WITHDRAW_REQUEST_INVALID");
  const { package_id: packageId, expected_active: expected } = request;
  if (typeof packageId !== "string" || !DIGEST.test(packageId) || !("expected_active" in request)
    || !(expected === null || typeof expected === "string" && DIGEST.test(expected))) throw new WaterAdminError("WITHDRAW_REQUEST_INVALID", 400);
  const eventId = "water:" + crypto.randomUUID().replaceAll("-", "");
  // The withdrawal applies only while the active pointer is still the one the caller saw.
  const [changed] = await store.db.batch([
    store.db.prepare("UPDATE water_packages SET state = 'WITHDRAWN' WHERE package_id = ? AND state = 'STAGED' AND (SELECT package_id FROM water_active WHERE singleton = 1) IS ?").bind(packageId, expected),
    store.db.prepare("INSERT INTO water_activation_events (event_id, package_id, previous_package_id, decision_json, occurred_at, action) SELECT ?, ?, NULL, '{}', ?, 'WITHDRAW' WHERE changes() = 1").bind(eventId, packageId, now),
  ]);
  if (changed?.meta?.changes !== 1) {
    const active = await currentActive(store);
    throw new WaterAdminError((active?.package_id ?? null) !== expected ? "WITHDRAW_CONFLICT" : "PACKAGE_NOT_STAGED");
  }
  return { event_id: eventId, package_id: packageId, outcome: "WITHDRAWN" };
}

export async function waterAdminStatus(store: WaterAdminStore) {
  const active = await currentActive(store);
  return { active_package_id: active?.package_id ?? null, previous_package_id: active?.previous_package_id ?? null, revision: active?.revision ?? 0 };
}

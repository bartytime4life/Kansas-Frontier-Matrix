/// <reference types="vite/client" />
import { env } from "cloudflare:workers";
import { getRawDb } from "../db";
import rawCatalog from "./public-release-catalog.json?raw";
import { IS_PUBLIC_COPY } from "./public-profile";
import { SITE_IDENTITY } from "./site-identity";
import { canonical, digest, parseWaterJson } from "./governed-water";
import { PUBLIC_FAMILIES, PublicReleaseError, parsePinnedPublicManifest, publicEntry, publicReleaseGate, publicReleaseExpiresAt, readPublicArtifact, assertPublicImplementationBinding, assertPublicRequestTarget, publicRequestTargetAllowed, type PublicDeliveryManifest, type PublicFamily, type PublicReleaseEntry, type PublicBucket } from "./public-release";

export const PUBLIC_READ_HEADERS = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
const settings = () => env as unknown as Record<string, unknown>;
const familyTables: Partial<Record<PublicFamily, { active: string; packages: string }>> = {
  water: { active: "water_active", packages: "water_packages" }, weather: { active: "weather_active", packages: "weather_packages" },
  soil: { active: "soil_active", packages: "soil_packages" }, "storm-events": { active: "storm_events_active", packages: "storm_events_packages" },
  earthquakes: { active: "earthquakes_active", packages: "earthquakes_packages" },
};
export const PUBLIC_ASSET_FAMILIES = ["subsurface", "groundwater", "archive"] as const;
export async function publicManifest(): Promise<PublicDeliveryManifest> {
  if (!IS_PUBLIC_COPY) throw new PublicReleaseError("PUBLIC_PROFILE_REQUIRED", 404);
  const manifest = await parsePinnedPublicManifest(rawCatalog, settings().KFM_PUBLIC_DELIVERY_SHA256);
  assertPublicImplementationBinding(manifest, SITE_IDENTITY.projectId, settings().KFM_PUBLIC_IMPLEMENTATION_REF);
  return manifest;
}
export async function publicPinnedEntry(family: PublicFamily, packageId: string): Promise<PublicReleaseEntry> {
  return publicEntry(await publicManifest(), family, packageId, new Date().toISOString());
}
export async function publicAuthorizedPackages(family: PublicFamily) {
  return (await publicAuthorizationStatus(family)).authorized_packages;
}
export async function publicAuthorizationStatus(family: PublicFamily): Promise<{ authorized_packages: { package_id: string; expires_at: string }[]; release_hold: string | null }> {
  if (!IS_PUBLIC_COPY) return { authorized_packages: [], release_hold: null };
  try {
    const manifest = await publicManifest(), now = new Date().toISOString(), candidates = manifest.entries.filter(entry => entry.family === family);
    let eligible = candidates.filter(entry => publicReleaseGate(entry, now) === "ELIGIBLE");
    if (!eligible.length) return { authorized_packages: [], release_hold: candidates.length ? publicReleaseGate(candidates[0], now) : "NO_APPROVED_PUBLIC_RELEASE" };
    const legacy = familyTables[family], placeholders = eligible.map(() => "?").join(",");
    const query = legacy
      ? `SELECT package_id FROM ${legacy.packages} WHERE state='WITHDRAWN' AND package_id IN (${placeholders})`
      : `SELECT DISTINCT package_id FROM public_delivery_events WHERE family=? AND action='WITHDRAW' AND package_id IN (${placeholders})`;
    const bindings = [...(!legacy ? [family] : []), ...eligible.map(entry => entry.package_id)];
    const withdrawn = new Set((await getRawDb().prepare(query).bind(...bindings).all<{ package_id: string }>()).results.map(row => row.package_id));
    eligible = eligible.filter(entry => !withdrawn.has(entry.package_id));
    return { authorized_packages: eligible.map(entry => ({ package_id: entry.package_id, expires_at: publicReleaseExpiresAt(entry) })), release_hold: eligible.length ? null : "PUBLIC_RELEASE_WITHDRAWN" };
  } catch (error) {
    // Read-only operator status and withdrawal must survive an invalid grant.
    return { authorized_packages: [], release_hold: error instanceof PublicReleaseError ? error.message : "PUBLIC_AUTHORIZATION_UNAVAILABLE" };
  }
}
export async function publicStageAuthorization(family: PublicFamily, packageText: string, request: Request): Promise<PublicReleaseEntry | null> {
  if (!IS_PUBLIC_COPY) return null;
  let packageId: unknown;
  try { packageId = (parseWaterJson(packageText) as { manifest?: { package_id?: unknown } })?.manifest?.package_id; } catch { throw new PublicReleaseError("PUBLIC_PACKAGE_BINDING_MISMATCH", 400); }
  if (typeof packageId !== "string") throw new PublicReleaseError("PUBLIC_PACKAGE_BINDING_MISMATCH", 400);
  const entry = await publicPinnedEntry(family, packageId);
  assertPublicRequestTarget(entry, request);
  if (await digest(packageText) !== entry.package_sha256) throw new PublicReleaseError("PUBLIC_PACKAGE_BINDING_MISMATCH", 400);
  const after = publicReleaseGate(entry, new Date().toISOString()); if (after !== "ELIGIBLE") throw new PublicReleaseError(after, 404);
  return entry;
}
export async function publicDecisionForActivation(family: PublicFamily, packageId: string, request: Request): Promise<Record<string, unknown>> {
  const entry = await publicPinnedEntry(family, packageId);
  assertPublicRequestTarget(entry, request);
  if (!entry.release_decision) throw new PublicReleaseError("PUBLIC_DECISION_BINDING_MISMATCH", 400);
  return entry.release_decision;
}
export async function publicActiveEntry(manifest: PublicDeliveryManifest, family: PublicFamily, now = new Date().toISOString()): Promise<PublicReleaseEntry | null> {
  const legacy = familyTables[family];
  if (legacy) {
    const row = await getRawDb().prepare(`SELECT a.package_id, a.decision_json, p.state FROM ${legacy.active} a LEFT JOIN ${legacy.packages} p ON p.package_id = a.package_id WHERE a.singleton = 1`).first<{ package_id: string; decision_json: string; state: string }>();
    if (!row || row.state !== "STAGED") return null;
    const entry = publicEntry(manifest, family, row.package_id, now);
    if (typeof row.decision_json !== "string" || row.decision_json.length > 8192 || canonical(parseWaterJson(row.decision_json)) !== canonical(entry.release_decision)) throw new PublicReleaseError("PUBLIC_DECISION_BINDING_MISMATCH");
    return entry;
  }
  const row = await getRawDb().prepare("SELECT family, package_id, manifest_sha256, state FROM public_delivery_active WHERE family = ?").bind(family).first<{ family: string; package_id: string; manifest_sha256: string; state: string }>();
  if (!row || row.state !== "ACTIVE") return null;
  if (row.manifest_sha256 !== settings().KFM_PUBLIC_DELIVERY_SHA256) throw new PublicReleaseError("PUBLIC_MANIFEST_PIN_MISMATCH");
  return publicEntry(manifest, family, row.package_id, now);
}
export async function publicFamilyAuthorization(family: PublicFamily, packageId: string, packageText: string, storedDecision: unknown, request: Request) {
  if (!IS_PUBLIC_COPY) return null;
  const manifest = await publicManifest(), entry = await publicActiveEntry(manifest, family);
  if (!entry || entry.package_id !== packageId) throw new PublicReleaseError("NO_APPROVED_PUBLIC_RELEASE", 404);
  assertPublicRequestTarget(entry, request);
  if (canonical(storedDecision) !== canonical(entry.release_decision) || await digest(packageText) !== entry.package_sha256) throw new PublicReleaseError("PUBLIC_PACKAGE_BINDING_MISMATCH");
  const after = publicReleaseGate(entry, new Date().toISOString()); if (after !== "ELIGIBLE") throw new PublicReleaseError(after, 404);
  if ((await publicActiveEntry(manifest, family))?.package_id !== entry.package_id) throw new PublicReleaseError("PUBLIC_RELEASE_WITHDRAWN", 404);
  return entry;
}

/** Caller must authenticate an operator and enforce same-origin before mutation.
 * The request chooses an already pinned package; it cannot submit approvals. */
export async function activatePublicDelivery(family: string, packageId: string, expectedActive: string | null, actor: string, rollback = false) {
  if (!PUBLIC_ASSET_FAMILIES.includes(family as typeof PUBLIC_ASSET_FAMILIES[number]) || !/^sha256:[a-f0-9]{64}$/.test(packageId) || !(expectedActive === null || /^sha256:[a-f0-9]{64}$/.test(expectedActive)) || !/^owner:[a-f0-9]{32}$/.test(actor) || typeof rollback !== "boolean") throw new PublicReleaseError("PUBLIC_ACTIVATION_INVALID", 400);
  const manifest = await publicManifest(), now = new Date().toISOString(), entry = publicEntry(manifest, family as PublicFamily, packageId, now);
  const db = getRawDb();
  const withdrawn = await db.prepare("SELECT event_id FROM public_delivery_events WHERE family=? AND package_id=? AND action='WITHDRAW' LIMIT 1").bind(family, packageId).first<{ event_id: string }>();
  if (withdrawn) throw new PublicReleaseError("PUBLIC_RELEASE_WITHDRAWN", 409);
  const bucket = settings().BUCKET as PublicBucket | undefined;
  if (!bucket) throw new PublicReleaseError("PUBLIC_RELEASE_STORE_UNAVAILABLE");
  // Verify every bounded artifact before changing the active pointer. This does
  // not review or approve bytes; the deployment pin already selects reviewed bytes.
  for (const artifact of entry.artifacts) await readPublicArtifact(bucket, entry, artifact.name, async () => true);
  const current = await db.prepare("SELECT package_id, previous_package_id, revision, state FROM public_delivery_active WHERE family = ?").bind(family).first<{ package_id: string; previous_package_id: string | null; revision: number; state: string }>();
  if (current?.package_id === packageId && current.state === "WITHDRAWN") throw new PublicReleaseError("PUBLIC_RELEASE_WITHDRAWN", 409);
  if ((current?.package_id ?? null) !== expectedActive || rollback && current?.previous_package_id !== packageId) throw new PublicReleaseError("PUBLIC_ACTIVATION_CONFLICT", 409);
  const revision = (current?.revision ?? 0) + 1, eventId = crypto.randomUUID(), pin = settings().KFM_PUBLIC_DELIVERY_SHA256;
  const write = current
    ? db.prepare("UPDATE public_delivery_active SET package_id=?, manifest_sha256=?, previous_package_id=?, state='ACTIVE', revision=? WHERE family=? AND package_id=? AND revision=? AND NOT EXISTS(SELECT 1 FROM public_delivery_events WHERE family=? AND package_id=? AND action='WITHDRAW')").bind(packageId, pin, expectedActive, revision, family, current.package_id, current.revision, family, packageId)
    : db.prepare("INSERT INTO public_delivery_active(family,package_id,manifest_sha256,previous_package_id,state,revision) SELECT ?,?,?,NULL,'ACTIVE',1 WHERE NOT EXISTS(SELECT 1 FROM public_delivery_events WHERE family=? AND package_id=? AND action='WITHDRAW') ON CONFLICT(family) DO NOTHING").bind(family, packageId, pin, family, packageId);
  const event = db.prepare("INSERT INTO public_delivery_events(event_id,family,package_id,previous_package_id,manifest_sha256,occurred_at,actor,action) SELECT ?,?,?,?,?,?,?,? WHERE changes()=1").bind(eventId, family, packageId, expectedActive, pin, new Date().toISOString(), actor, rollback ? "ROLLBACK" : "ACTIVATE");
  const beforeWrite = publicReleaseGate(entry, new Date().toISOString()); if (beforeWrite !== "ELIGIBLE") throw new PublicReleaseError(beforeWrite, 404);
  const [written] = await db.batch([write, event]);
  if (written?.meta?.changes !== 1) throw new PublicReleaseError("PUBLIC_ACTIVATION_CONFLICT", 409);
  return { outcome: rollback ? "ROLLED_BACK" : "ACTIVATED", family, package_id: packageId, revision, event_id: eventId };
}
export async function withdrawPublicDelivery(family: string, expectedActive: string, actor: string) {
  if (!PUBLIC_ASSET_FAMILIES.includes(family as typeof PUBLIC_ASSET_FAMILIES[number]) || !/^sha256:[a-f0-9]{64}$/.test(expectedActive) || !/^owner:[a-f0-9]{32}$/.test(actor)) throw new PublicReleaseError("PUBLIC_WITHDRAW_INVALID", 400);
  const db = getRawDb(), eventId = crypto.randomUUID();
  const [changed] = await db.batch([
    db.prepare("UPDATE public_delivery_active SET state='WITHDRAWN',revision=revision+1 WHERE family=? AND package_id=? AND state='ACTIVE'").bind(family, expectedActive),
    db.prepare("INSERT INTO public_delivery_events(event_id,family,package_id,previous_package_id,manifest_sha256,occurred_at,actor,action) SELECT ?,family,package_id,previous_package_id,manifest_sha256,?,?,'WITHDRAW' FROM public_delivery_active WHERE family=? AND changes()=1").bind(eventId, new Date().toISOString(), actor, family),
  ]);
  if (changed?.meta?.changes !== 1) throw new PublicReleaseError("PUBLIC_WITHDRAW_CONFLICT", 409);
  return { outcome: "WITHDRAWN", family, package_id: expectedActive, event_id: eventId };
}

function failure(error: unknown, asset = false) {
  const reason = error instanceof PublicReleaseError ? error.message : "PUBLIC_RELEASE_STORE_UNAVAILABLE";
  const held = ["PUBLIC_RELEASE_UNBOUND", "PUBLIC_IMPLEMENTATION_UNBOUND", "PUBLIC_HOST_NOT_AUTHORIZED", "NO_APPROVED_PUBLIC_RELEASE", "PUBLIC_RELEASE_EXPIRED", "PUBLIC_CORRECTION_HOLD", "PUBLIC_RELEASE_WITHDRAWN", "PUBLIC_ARTIFACT_UNAVAILABLE", "PUBLIC_PROFILE_REQUIRED"].includes(reason);
  return Response.json({ envelope: { outcome: held ? "ABSTAIN" : "ERROR", reason_code: reason, evidence_refs: [] } }, { status: held ? asset || reason === "PUBLIC_HOST_NOT_AUTHORIZED" || reason === "PUBLIC_PROFILE_REQUIRED" ? 404 : 200 : error instanceof PublicReleaseError ? error.status : 503, headers: PUBLIC_READ_HEADERS });
}
export async function publicCatalogRead(request: Request) {
  try {
    if (new URL(request.url).search) throw new PublicReleaseError("INVALID_QUERY", 400);
    const manifest = await publicManifest(), entries = [];
    const requestEntries = manifest.entries.filter(entry => publicRequestTargetAllowed(entry, request));
    if (manifest.entries.length && !requestEntries.length) throw new PublicReleaseError("PUBLIC_HOST_NOT_AUTHORIZED", 404);
    const families = PUBLIC_FAMILIES.filter(family => requestEntries.some(entry => entry.family === family));
    if (!families.length) throw new PublicReleaseError("NO_APPROVED_PUBLIC_RELEASE", 404);
    const selects = families.map(family => {
      const legacy = familyTables[family];
      return legacy
        ? `SELECT '${family}' AS family,a.package_id,a.decision_json,p.state,NULL AS manifest_sha256 FROM ${legacy.active} a LEFT JOIN ${legacy.packages} p ON p.package_id=a.package_id WHERE a.singleton=1`
        : `SELECT family,package_id,NULL AS decision_json,state,manifest_sha256 FROM public_delivery_active WHERE family='${family}'`;
    });
    // One statement gives one consistent active-pointer snapshot. No later
    // awaits may let an earlier selection go stale during other family reads.
    const rows = (await getRawDb().prepare(selects.join(" UNION ALL ")).all<{ family: PublicFamily; package_id: string; decision_json: string | null; state: string; manifest_sha256: string | null }>()).results;
    const now = new Date().toISOString();
    for (const row of rows) {
      const legacy = familyTables[row.family];
      if (row.state !== (legacy ? "STAGED" : "ACTIVE")) continue;
      const entry = requestEntries.find(item => item.family === row.family && item.package_id === row.package_id);
      if (!entry || publicReleaseGate(entry, now) !== "ELIGIBLE") continue;
      if (legacy) {
        if (typeof row.decision_json !== "string" || row.decision_json.length > 8192 || canonical(parseWaterJson(row.decision_json)) !== canonical(entry.release_decision)) throw new PublicReleaseError("PUBLIC_DECISION_BINDING_MISMATCH");
      } else if (row.manifest_sha256 !== settings().KFM_PUBLIC_DELIVERY_SHA256) throw new PublicReleaseError("PUBLIC_MANIFEST_PIN_MISMATCH");
      entries.push({ family: entry.family, package_id: entry.package_id, title: entry.title, expires_at: publicReleaseExpiresAt(entry),
        date_coverage: entry.date_coverage, available_dates: entry.available_dates, source_versions: entry.source_versions,
        attribution: entry.rights.attribution, geometry_precision: entry.sensitivity.geometry_precision,
        assets: entry.artifacts.map(artifact => ({ name: artifact.name, url: `/api/governed/public/assets/${entry.family}/${encodeURIComponent(artifact.name)}`, media_type: artifact.media_type, bytes: artifact.bytes })) });
    }
    if (!entries.length) throw new PublicReleaseError("NO_APPROVED_PUBLIC_RELEASE", 404);
    return Response.json({ envelope: { outcome: "ANSWER", reason_code: "APPROVED_PUBLIC_RELEASES", evidence_refs: [] }, data: { entries } }, { headers: PUBLIC_READ_HEADERS });
  } catch (error) { return failure(error); }
}
export async function publicAssetRead(request: Request, family: string, name: string) {
  try {
    if (new URL(request.url).search || !PUBLIC_ASSET_FAMILIES.includes(family as typeof PUBLIC_ASSET_FAMILIES[number]) || !/^[a-zA-Z0-9][a-zA-Z0-9._-]{0,159}$/.test(name) || name.includes("..")) throw new PublicReleaseError("PUBLIC_ARTIFACT_UNAVAILABLE", 404);
    const manifest = await publicManifest(), entry = await publicActiveEntry(manifest, family as PublicFamily);
    if (!entry) throw new PublicReleaseError("NO_APPROVED_PUBLIC_RELEASE", 404);
    assertPublicRequestTarget(entry, request);
    const bucket = settings().BUCKET as PublicBucket | undefined;
    if (!bucket || typeof bucket.get !== "function") throw new PublicReleaseError("PUBLIC_RELEASE_STORE_UNAVAILABLE");
    const current = async () => (await publicActiveEntry(manifest, family as PublicFamily))?.package_id === entry.package_id;
    const { bytes, artifact } = await readPublicArtifact(bucket, entry, name, current);
    return new Response(bytes as Uint8Array<ArrayBuffer>, { headers: { ...PUBLIC_READ_HEADERS, "Content-Type": artifact.media_type,
      "X-KFM-Public-Expires-At": entry.publication.expires_at, "X-KFM-Public-Release-ID": entry.package_id } });
  } catch (error) { return failure(error, true); }
}

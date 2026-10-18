import { canonical, digest, parseWaterJson } from "./governed-water";

// This delivery projection is downstream of accountable authorization. A schema,
// digest, compiler result or uploaded package cannot create that authorization.
export const PUBLIC_DELIVERY_PROFILE = "kfm.public-delivery/v1";
export const PUBLIC_MANIFEST_LIMIT = 2 * 1024 * 1024;
export const PUBLIC_ARTIFACT_LIMIT = 64 * 1024 * 1024;
export const PUBLIC_FAMILIES = ["water", "weather", "soil", "storm-events", "earthquakes", "subsurface", "groundwater", "archive"] as const;
export type PublicFamily = typeof PUBLIC_FAMILIES[number];
export const PUBLIC_AUTHORITY_ROLES = ["source_admission", "rights", "sensitivity", "policy", "review", "release", "publication"] as const;
export type PublicAuthorityRole = typeof PUBLIC_AUTHORITY_ROLES[number];
export type PublicAuthorityRef = { ref: string; sha256: string };
export type PublicArtifact = { name: string; object_key: string; sha256: string; bytes: number; media_type: string; public_fields: string[] };
export type PublicSourceVersion = { source_id: string; version: string; sha256: string; role: "observation" | "interpretation" | "display_context"; citation: string; url: string };
export type PublicPublicationTarget = { site_project_id: string; hostnames: string[]; implementation_ref: string };
export type PublicReleaseEntry = {
  family: PublicFamily; package_id: string; package_sha256: string; title: string;
  publication: { decision: "APPROVED"; audience: "PUBLIC"; authorized_by: string; authorized_at: string; expires_at: string; target: PublicPublicationTarget };
  refs: Record<PublicAuthorityRole, PublicAuthorityRef>;
  rights: { license: string; attribution: string; redistribution_allowed: true };
  sensitivity: { level: "public"; geometry_precision: "NONE" | "GENERALIZED" | "SOURCE_PRECISION" };
  correction_state: "ACTIVE" | "CORRECTED" | "SUPERSEDED" | "WITHDRAWN";
  rollback_ref: string; source_versions: PublicSourceVersion[];
  date_coverage: { start: string; end: string; time_kind: "observation_instant" | "observation_day" | "record_date" | "source_edition" | "retrieval_day" };
  available_dates: string[]; artifacts: PublicArtifact[];
  release_decision: Record<string, unknown> | null;
};
export type PublicDeliveryManifest = { profile: typeof PUBLIC_DELIVERY_PROFILE; entries: PublicReleaseEntry[] };
export class PublicReleaseError extends Error { constructor(reason: string, readonly status = 503) { super(reason); } }
const HEX = /^sha256:[a-f0-9]{64}$/;
const REF = /^kfm:\/\/[A-Za-z0-9._~:/-]{1,240}$/;
const NAME = /^[a-zA-Z0-9][a-zA-Z0-9._-]{0,159}$/;
const SITE_PROJECT = /^appgprj_[a-f0-9]{32}$/;
const IMPLEMENTATION_REF = /^kfm:\/\/receipt\/implementation\/sha256\/[a-f0-9]{64}$/;
const MEDIA = ["application/json", "application/gzip", "image/png", "image/jpeg", "text/plain", "text/csv"];
const object = (value: unknown): value is Record<string, unknown> => !!value && typeof value === "object" && !Array.isArray(value);
const text = (value: unknown, limit = 4000): value is string => typeof value === "string" && value.length > 0 && value.length <= limit && !/[\u0000-\u001f\u007f]/.test(value);
const keys = (value: Record<string, unknown>, expected: string[]) => Object.keys(value).sort().join("|") === expected.sort().join("|");
const timestamp = (value: unknown): value is string => typeof value === "string" && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?Z$/.test(value) && Number.isFinite(Date.parse(value)) && new Date(Date.parse(value)).toISOString().slice(0, 19) === value.slice(0, 19);
const day = (value: unknown): value is string => typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value) && Number.isFinite(Date.parse(value)) && new Date(value).toISOString().slice(0, 10) === value;
const uniqueStrings = (value: unknown, maximum: number, check: (v: unknown) => boolean) => Array.isArray(value) && value.length <= maximum && value.every(check) && new Set(value).size === value.length;
const https = (value: unknown) => { if (!text(value, 2000)) return false; try { const url = new URL(value); return url.protocol === "https:" && !url.username && !url.password; } catch { return false; } };
export function publicHostname(value: unknown): value is string {
  return typeof value === "string" && value.length <= 253 && value === value.toLowerCase()
    && value.split(".").length >= 2 && /[a-z]/.test(value.split(".").at(-1) ?? "")
    && value.split(".").every(label => /^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/.test(label));
}
function invalid(): never { throw new PublicReleaseError("PUBLIC_MANIFEST_INVALID"); }

export function publicObjectKey(family: PublicFamily, packageId: string, name: string): string {
  if (!PUBLIC_FAMILIES.includes(family) || !HEX.test(packageId) || !NAME.test(name) || name.includes("..")) throw new PublicReleaseError("PUBLIC_ARTIFACT_INVALID", 400);
  return `public-delivery/v1/${family}/${packageId.slice(7)}/${name}`;
}

export function parsePublicManifest(raw: string): PublicDeliveryManifest {
  if (new TextEncoder().encode(raw).length > PUBLIC_MANIFEST_LIMIT) invalid();
  let parsed: unknown;
  try { parsed = parseWaterJson(raw); } catch { invalid(); }
  if (!object(parsed) || !keys(parsed, ["profile", "entries"]) || parsed.profile !== PUBLIC_DELIVERY_PROFILE || !Array.isArray(parsed.entries) || parsed.entries.length > 128) invalid();
  const identities = new Set<string>();
  for (const candidate of parsed.entries) {
    if (!object(candidate) || !keys(candidate, ["family", "package_id", "package_sha256", "title", "publication", "refs", "rights", "sensitivity", "correction_state", "rollback_ref", "source_versions", "date_coverage", "available_dates", "artifacts", "release_decision"])) invalid();
    const entry = candidate as unknown as PublicReleaseEntry;
    if (!PUBLIC_FAMILIES.includes(entry.family) || !HEX.test(entry.package_id) || !HEX.test(entry.package_sha256) || !text(entry.title, 240)) invalid();
    const identity = `${entry.family}:${entry.package_id}`;
    if (identities.has(identity)) invalid(); identities.add(identity);
    if (!object(entry.publication) || !keys(entry.publication, ["decision", "audience", "authorized_by", "authorized_at", "expires_at", "target"]) || entry.publication.decision !== "APPROVED" || entry.publication.audience !== "PUBLIC" || !text(entry.publication.authorized_by, 128) || !timestamp(entry.publication.authorized_at) || !timestamp(entry.publication.expires_at) || Date.parse(entry.publication.authorized_at) >= Date.parse(entry.publication.expires_at)) invalid();
    const target = entry.publication.target;
    if (!object(target) || !keys(target, ["site_project_id", "hostnames", "implementation_ref"]) || !SITE_PROJECT.test(target.site_project_id) || !uniqueStrings(target.hostnames, 16, publicHostname) || !target.hostnames.length || !IMPLEMENTATION_REF.test(target.implementation_ref)) invalid();
    if (!object(entry.refs) || !keys(entry.refs, [...PUBLIC_AUTHORITY_ROLES])) invalid();
    const refs = new Set<string>();
    for (const role of PUBLIC_AUTHORITY_ROLES) {
      const item = entry.refs[role];
      if (!object(item) || !keys(item, ["ref", "sha256"]) || !REF.test(item.ref) || !HEX.test(item.sha256) || refs.has(item.ref)) invalid();
      refs.add(item.ref);
    }
    if (!object(entry.rights) || !keys(entry.rights, ["license", "attribution", "redistribution_allowed"]) || !text(entry.rights.license) || !text(entry.rights.attribution) || entry.rights.redistribution_allowed !== true || /review required|unknown|unresolved/i.test(entry.rights.license)) invalid();
    if (!object(entry.sensitivity) || !keys(entry.sensitivity, ["level", "geometry_precision"]) || entry.sensitivity.level !== "public" || !["NONE", "GENERALIZED", "SOURCE_PRECISION"].includes(entry.sensitivity.geometry_precision)) invalid();
    if (!["ACTIVE", "CORRECTED", "SUPERSEDED", "WITHDRAWN"].includes(entry.correction_state) || !REF.test(entry.rollback_ref)) invalid();
    if (!Array.isArray(entry.source_versions) || !entry.source_versions.length || entry.source_versions.length > 32) invalid();
    const sources = new Set<string>();
    for (const source of entry.source_versions) {
      if (!object(source) || !keys(source, ["source_id", "version", "sha256", "role", "citation", "url"]) || !text(source.source_id, 160) || !text(source.version, 160) || !HEX.test(source.sha256) || !["observation", "interpretation", "display_context"].includes(source.role) || !text(source.citation) || !https(source.url) || sources.has(source.source_id)) invalid();
      sources.add(source.source_id);
    }
    if (!object(entry.date_coverage) || !keys(entry.date_coverage, ["start", "end", "time_kind"]) || !["observation_instant", "observation_day", "record_date", "source_edition", "retrieval_day"].includes(entry.date_coverage.time_kind)) invalid();
    const dates = entry.date_coverage.time_kind === "observation_instant" ? timestamp : day;
    if (!dates(entry.date_coverage.start) || !dates(entry.date_coverage.end) || Date.parse(entry.date_coverage.start) > Date.parse(entry.date_coverage.end) || !uniqueStrings(entry.available_dates, 80000, day) || entry.available_dates.some(value => value < entry.date_coverage.start.slice(0, 10) || value > entry.date_coverage.end.slice(0, 10))) invalid();
    if (!Array.isArray(entry.artifacts) || entry.artifacts.length > 2000) invalid();
    const names = new Set<string>();
    for (const artifact of entry.artifacts) {
      if (!object(artifact) || !keys(artifact, ["name", "object_key", "sha256", "bytes", "media_type", "public_fields"]) || !NAME.test(artifact.name) || artifact.name.includes("..") || names.has(artifact.name) || artifact.object_key !== publicObjectKey(entry.family, entry.package_id, artifact.name) || !HEX.test(artifact.sha256) || !Number.isSafeInteger(artifact.bytes) || artifact.bytes < 1 || artifact.bytes > PUBLIC_ARTIFACT_LIMIT || !MEDIA.includes(artifact.media_type) || !uniqueStrings(artifact.public_fields, 256, value => text(value, 160)) || !artifact.public_fields.length) invalid();
      if (artifact.name.endsWith(".json") && artifact.media_type !== "application/json" || artifact.name.endsWith(".json.gz") && artifact.media_type !== "application/gzip") invalid();
      names.add(artifact.name);
    }
    const familyProfiles: Record<string, string> = { water: "kfm.water-release-decision/v1", weather: "kfm.weather-release-decision/v1", soil: "kfm.soil-release-decision/v1", "storm-events": "kfm.storm-events-release-decision/v1", earthquakes: "kfm.earthquake-release-decision/v1" };
    if (entry.family in familyProfiles) {
      if (!object(entry.release_decision) || entry.release_decision.profile !== familyProfiles[entry.family] || entry.release_decision.package_id !== entry.package_id || entry.release_decision.decision !== "APPROVED") invalid();
      for (const role of PUBLIC_AUTHORITY_ROLES.filter(role => role !== "publication")) if (entry.release_decision[`${role}_ref`] !== entry.refs[role].ref) invalid();
      if (!["reviewed_at", "released_at", "expires_at"].every(key => timestamp(entry.release_decision![key])) || Date.parse(String(entry.release_decision.reviewed_at)) > Date.parse(String(entry.release_decision.released_at)) || Date.parse(String(entry.release_decision.released_at)) > Date.parse(entry.publication.authorized_at)) invalid();
    } else if (entry.release_decision !== null || !entry.artifacts.length) invalid();
  }
  return parsed as unknown as PublicDeliveryManifest;
}

export async function parsePinnedPublicManifest(raw: string, trustedPin: unknown): Promise<PublicDeliveryManifest> {
  if (typeof trustedPin !== "string" || !HEX.test(trustedPin)) throw new PublicReleaseError("PUBLIC_RELEASE_UNBOUND");
  if (new TextEncoder().encode(raw).length > PUBLIC_MANIFEST_LIMIT || await digest(raw) !== trustedPin) throw new PublicReleaseError("PUBLIC_MANIFEST_PIN_MISMATCH");
  return parsePublicManifest(raw);
}

export function assertPublicImplementationBinding(manifest: PublicDeliveryManifest, siteProjectId: unknown, trustedImplementationRef: unknown) {
  // Empty catalogs authorize nothing, including in an unconfigured preview.
  if (!manifest.entries.length) return;
  if (typeof trustedImplementationRef !== "string" || !IMPLEMENTATION_REF.test(trustedImplementationRef)) throw new PublicReleaseError("PUBLIC_IMPLEMENTATION_UNBOUND");
  if (typeof siteProjectId !== "string" || !SITE_PROJECT.test(siteProjectId)) throw new PublicReleaseError("PUBLIC_TARGET_SITE_MISMATCH");
  for (const entry of manifest.entries) {
    if (entry.publication.target.site_project_id !== siteProjectId) throw new PublicReleaseError("PUBLIC_TARGET_SITE_MISMATCH");
    if (entry.publication.target.implementation_ref !== trustedImplementationRef) throw new PublicReleaseError("PUBLIC_IMPLEMENTATION_MISMATCH");
  }
}
export function publicRequestTargetAllowed(entry: PublicReleaseEntry, request: Request): boolean {
  const url = new URL(request.url);
  return url.protocol === "https:" && !url.port && !url.username && !url.password
    && entry.publication.target.hostnames.includes(url.hostname);
}
export function assertPublicRequestTarget(entry: PublicReleaseEntry, request: Request) {
  if (!publicRequestTargetAllowed(entry, request)) throw new PublicReleaseError("PUBLIC_HOST_NOT_AUTHORIZED", 404);
}

export function publicReleaseGate(entry: PublicReleaseEntry, now: string): string {
  if (!timestamp(now)) return "PUBLIC_TIME_INVALID";
  if (entry.correction_state !== "ACTIVE") return "PUBLIC_CORRECTION_HOLD";
  if (entry.publication.decision !== "APPROVED" || entry.publication.audience !== "PUBLIC" || entry.sensitivity.level !== "public" || !entry.rights.redistribution_allowed) return "PUBLIC_RELEASE_NOT_APPROVED";
  if (!(Date.parse(entry.publication.authorized_at) <= Date.parse(now) && Date.parse(now) < Date.parse(entry.publication.expires_at))) return "PUBLIC_RELEASE_EXPIRED";
  if (entry.release_decision?.correction_state !== undefined && entry.release_decision.correction_state !== "ACTIVE") return "PUBLIC_CORRECTION_HOLD";
  if (entry.release_decision && (entry.release_decision.correction_ref !== null || !(Date.parse(String(entry.release_decision.released_at)) <= Date.parse(now) && Date.parse(now) < Date.parse(String(entry.release_decision.expires_at))))) return "PUBLIC_RELEASE_EXPIRED";
  return "ELIGIBLE";
}
export function publicReleaseExpiresAt(entry: PublicReleaseEntry): string {
  return entry.release_decision
    ? new Date(Math.min(Date.parse(entry.publication.expires_at), Date.parse(String(entry.release_decision.expires_at)))).toISOString()
    : entry.publication.expires_at;
}

export function publicEntry(manifest: PublicDeliveryManifest, family: PublicFamily, packageId: string, now: string): PublicReleaseEntry {
  const entry = manifest.entries.find(item => item.family === family && item.package_id === packageId);
  if (!entry) throw new PublicReleaseError("NO_APPROVED_PUBLIC_RELEASE", 404);
  const reason = publicReleaseGate(entry, now); if (reason !== "ELIGIBLE") throw new PublicReleaseError(reason, 404);
  return entry;
}

export type PublicBucket = { get(key: string): Promise<{ size: number; arrayBuffer(): Promise<ArrayBuffer> } | null> };
export async function readPublicArtifact(bucket: PublicBucket, entry: PublicReleaseEntry, name: string, current: () => Promise<boolean>, clock = () => new Date().toISOString()) {
  const reason = publicReleaseGate(entry, clock()); if (reason !== "ELIGIBLE") throw new PublicReleaseError(reason, 404);
  if (!await current()) throw new PublicReleaseError("PUBLIC_RELEASE_WITHDRAWN", 404);
  const artifact = entry.artifacts.find(item => item.name === name);
  if (!artifact || artifact.object_key !== publicObjectKey(entry.family, entry.package_id, name)) throw new PublicReleaseError("PUBLIC_ARTIFACT_UNAVAILABLE", 404);
  const stored = await bucket.get(artifact.object_key);
  if (!stored || stored.size !== artifact.bytes || stored.size > PUBLIC_ARTIFACT_LIMIT) throw new PublicReleaseError("PUBLIC_ARTIFACT_INTEGRITY_HOLD");
  const bytes = new Uint8Array(await stored.arrayBuffer());
  const actual = "sha256:" + [...new Uint8Array(await crypto.subtle.digest("SHA-256", bytes))].map(value => value.toString(16).padStart(2, "0")).join("");
  if (bytes.byteLength !== artifact.bytes || actual !== artifact.sha256) throw new PublicReleaseError("PUBLIC_ARTIFACT_INTEGRITY_HOLD");
  const after = publicReleaseGate(entry, clock()); if (after !== "ELIGIBLE") throw new PublicReleaseError(after, 404);
  if (!await current()) throw new PublicReleaseError("PUBLIC_RELEASE_WITHDRAWN", 404);
  return { bytes, artifact };
}

// Offline validation only: the resolver supplies already-reviewed owning bytes.
// Resolving/hash-checking them never authenticates a reviewer or approves a release.
export async function compilePublicReleaseCatalog(raw: string, resolve: (ref: string) => Promise<string | Uint8Array | null>) {
  const manifest = parsePublicManifest(raw);
  const checkBytes = async (key: string, expected: string, size?: number) => {
    const value = await resolve(key);
    if (value === null) throw new PublicReleaseError("PUBLIC_REFERENCE_UNRESOLVED");
    const bytes = typeof value === "string" ? new TextEncoder().encode(value) : value;
    if (size !== undefined && bytes.length !== size) throw new PublicReleaseError("PUBLIC_ARTIFACT_INTEGRITY_HOLD");
    const actual = "sha256:" + [...new Uint8Array(await crypto.subtle.digest("SHA-256", new Uint8Array(bytes)))].map(value => value.toString(16).padStart(2, "0")).join("");
    if (actual !== expected) throw new PublicReleaseError("PUBLIC_REFERENCE_DIGEST_MISMATCH");
    return bytes;
  };
  for (const entry of manifest.entries) {
    const implementationRef = entry.publication.target.implementation_ref;
    const implementationBytes = await checkBytes(implementationRef, "sha256:" + implementationRef.split("/").at(-1));
    let implementation: unknown;
    try { implementation = parseWaterJson(new TextDecoder("utf-8", { fatal: true }).decode(implementationBytes)); } catch { throw new PublicReleaseError("PUBLIC_IMPLEMENTATION_REVIEW_INVALID"); }
    if (!object(implementation) || !keys(implementation, ["profile", "decision", "site_project_id", "source_commit", "reviewed_by", "reviewed_at"])
      || implementation.profile !== "kfm.public-implementation-review/v1" || implementation.decision !== "APPROVED"
      || implementation.site_project_id !== entry.publication.target.site_project_id || typeof implementation.source_commit !== "string" || !/^[a-f0-9]{40}$/.test(implementation.source_commit)
      || !text(implementation.reviewed_by, 128) || !timestamp(implementation.reviewed_at) || Date.parse(implementation.reviewed_at) > Date.parse(entry.publication.authorized_at)) throw new PublicReleaseError("PUBLIC_IMPLEMENTATION_REVIEW_INVALID");
    for (const role of PUBLIC_AUTHORITY_ROLES) {
      const reference = entry.refs[role], bytes = await resolve(reference.ref);
      if (bytes === null) throw new PublicReleaseError("PUBLIC_REFERENCE_UNRESOLVED");
      const content = typeof bytes === "string" ? new TextEncoder().encode(bytes) : bytes;
      const actual = "sha256:" + [...new Uint8Array(await crypto.subtle.digest("SHA-256", new Uint8Array(content)))].map(value => value.toString(16).padStart(2, "0")).join("");
      if (actual !== reference.sha256) throw new PublicReleaseError("PUBLIC_REFERENCE_DIGEST_MISMATCH");
    }
    const rollback = await resolve(entry.rollback_ref);
    if (rollback === null) throw new PublicReleaseError("PUBLIC_ROLLBACK_UNRESOLVED");
    await checkBytes(`${entry.family}:${entry.package_id}`, entry.package_sha256);
    for (const source of entry.source_versions) await checkBytes(`${source.source_id}@${source.version}`, source.sha256);
    for (const artifact of entry.artifacts) {
      const bytes = await checkBytes(artifact.object_key, artifact.sha256, artifact.bytes);
      if (["application/json", "application/gzip"].includes(artifact.media_type)) {
        let jsonBytes = bytes;
        if (artifact.media_type === "application/gzip") {
          const reader = new Blob([bytes as Uint8Array<ArrayBuffer>]).stream().pipeThrough(new DecompressionStream("gzip")).getReader();
          const chunks: Uint8Array[] = []; let total = 0;
          for (;;) {
            const { done, value } = await reader.read(); if (done) break;
            total += value.length;
            if (total > 25_000_000) { await reader.cancel(); throw new PublicReleaseError("PUBLIC_EXPANDED_ARTIFACT_TOO_LARGE"); }
            chunks.push(value);
          }
          jsonBytes = new Uint8Array(total); let offset = 0;
          for (const chunk of chunks) { jsonBytes.set(chunk, offset); offset += chunk.length; }
        }
        let value: unknown;
        try { value = parseWaterJson(new TextDecoder("utf-8", { fatal: true }).decode(jsonBytes)); } catch { throw new PublicReleaseError("PUBLIC_ARTIFACT_JSON_INVALID"); }
        const fields = new Set<string>();
        const visit = (item: unknown, prefix: string, depth: number) => {
          if (depth > 64) throw new PublicReleaseError("PUBLIC_ARTIFACT_JSON_INVALID");
          if (Array.isArray(item)) { for (const child of item) visit(child, prefix + "[]", depth + 1); }
          else if (object(item)) for (const [key, child] of Object.entries(item)) {
            const path = prefix ? `${prefix}.${key}` : key; fields.add(path); visit(child, path, depth + 1);
          }
        };
        visit(value, "", 0);
        if ([...fields].some(field => !artifact.public_fields.includes(field))) throw new PublicReleaseError("PUBLIC_FIELD_NOT_APPROVED");
      }
    }
  }
  const output = canonical(manifest) + "\n";
  return { text: output, sha256: await digest(output), authority: "VALIDATION_ONLY" as const };
}

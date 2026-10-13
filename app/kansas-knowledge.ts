/** Read-only, reviewed Kansas knowledge projection. Source capture and approval live upstream. */
export const KNOWLEDGE_PACKAGE_LIMIT = 4 * 1024 * 1024;
const DIGEST = /^sha256:[0-9a-f]{64}$/;
const REF = /^kfm:\/\/[A-Za-z0-9._~:/-]{1,240}$/;
const ID = /^[a-z0-9][a-z0-9._:-]{0,119}$/;
const KINDS = new Set(["place", "fact", "person", "event", "story"]);
const SOURCE_HOSTS = new Set(["www.usgs.gov", "www.blm.gov", "glorecords.blm.gov", "www.loc.gov", "loc.gov"]);
const ROW_KEYS = ["record_id", "release_id", "kind", "title", "summary", "location_label", "geometry_role", "time_start", "time_end", "source_ref", "source_url", "evidence_ref", "rights_ref", "sensitivity_ref", "review_ref", "correction_state", "public_state", "assertions_json"].sort().join(",");

export type KnowledgeRow = {
  record_id: string; release_id: string; kind: string; title: string; summary: string;
  location_label: string; geometry_role: string; time_start: string | null; time_end: string | null;
  source_ref: string; source_url: string; evidence_ref: string; rights_ref: string;
  sensitivity_ref: string; review_ref: string; correction_state: string;
  public_state: string; assertions_json: string;
};
export type KnowledgeRecord = Omit<KnowledgeRow, "assertions_json"> & {
  assertions: { text: string; source_ref: string; evidence_ref: string; status: "documented" | "conflicting" | "narrative" }[];
};
export type KnowledgeQuery = { kind: "search"; term: string } | { kind: "record"; id: string };

export function knowledgeQuery(url: string): KnowledgeQuery {
  const parsed = new URL(url);
  if (parsed.search.length > 160) throw new Error("INVALID_QUERY");
  const fields = [...parsed.searchParams.entries()];
  if (fields.some(([key]) => key !== "term" && key !== "id") || fields.length > 1) throw new Error("INVALID_QUERY");
  const id = parsed.searchParams.get("id");
  if (id !== null) {
    if (!ID.test(id)) throw new Error("INVALID_QUERY");
    return { kind: "record", id };
  }
  const term = (parsed.searchParams.get("term") ?? "").trim();
  if (term.length > 80 || /[\u0000-\u001f\u007f]/.test(term)) throw new Error("INVALID_QUERY");
  return { kind: "search", term };
}

export function canonicalKnowledge(value: unknown): string {
  if (value === null || typeof value === "string" || typeof value === "boolean" || typeof value === "number" && Number.isFinite(value)) return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(canonicalKnowledge).join(",")}]`;
  if (!value || typeof value !== "object") throw new Error("INVALID_PACKAGE");
  const obj = value as Record<string, unknown>;
  return `{${Object.keys(obj).sort().map(key => `${JSON.stringify(key)}:${canonicalKnowledge(obj[key])}`).join(",")}}`;
}

export async function knowledgeDigest(bytes: Uint8Array): Promise<string> {
  return "sha256:" + Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", Uint8Array.from(bytes).buffer)), b => b.toString(16).padStart(2, "0")).join("");
}

export function validKnowledgeRelease(row: Record<string, unknown> | null, now = Date.now()): boolean {
  if (!row || row.state !== "APPROVED" || row.release_id !== row.package_sha256 ||
      typeof row.release_id !== "string" || !DIGEST.test(row.release_id) ||
      row.package_key !== `kansas-knowledge/v1/objects/${row.release_id.slice(7)}.json` ||
      typeof row.reviewer_key !== "string" || typeof row.releaser_key !== "string" ||
      !row.reviewer_key || !row.releaser_key || row.reviewer_key === row.releaser_key) return false;
  for (const key of ["source_admission_ref", "rights_ref", "sensitivity_ref", "policy_ref", "review_ref", "release_ref"]) {
    if (typeof row[key] !== "string" || !REF.test(row[key])) return false;
  }
  const reviewed = Date.parse(String(row.reviewed_at));
  const released = Date.parse(String(row.released_at));
  return Number.isFinite(reviewed) && Number.isFinite(released) && reviewed <= released && released <= now;
}

const text = (value: unknown, max: number) => typeof value === "string" && value.length > 0 && value.length <= max && !/[\u0000-\u001f\u007f]/.test(value);
export function publicKnowledgeRecord(row: KnowledgeRow): KnowledgeRecord {
  if (!row || Object.keys(row).sort().join(",") !== ROW_KEYS || !ID.test(row.record_id) || !DIGEST.test(row.release_id) || !KINDS.has(row.kind) ||
      !text(row.title, 200) || !text(row.summary, 2000) || !text(row.location_label, 160) ||
      !["named place", "county-level", "statewide", "no mapped location"].includes(row.geometry_role) ||
      row.public_state !== "PUBLIC_SAFE" || row.correction_state !== "ACTIVE" ||
      ![row.source_ref, row.evidence_ref, row.rights_ref, row.sensitivity_ref, row.review_ref].every(value => typeof value === "string" && REF.test(value))) throw new Error("RECORD_WITHHELD");
  let source: URL;
  try { source = new URL(row.source_url); } catch { throw new Error("SOURCE_LINK_INVALID"); }
  if (source.protocol !== "https:" || !SOURCE_HOSTS.has(source.hostname) || source.username || source.password || source.hash) throw new Error("SOURCE_LINK_INVALID");
  for (const day of [row.time_start, row.time_end]) if (day !== null) {
    if (typeof day !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(day) || !Number.isFinite(Date.parse(day + "T00:00:00Z")) || new Date(day + "T00:00:00Z").toISOString().slice(0, 10) !== day) throw new Error("TIME_INVALID");
  }
  if (row.time_start && row.time_end && row.time_start > row.time_end) throw new Error("TIME_INVALID");
  if (row.assertions_json.length > 12_000) throw new Error("ASSERTIONS_INVALID");
  let assertions: unknown;
  try { assertions = JSON.parse(row.assertions_json); } catch { throw new Error("ASSERTIONS_INVALID"); }
  if (!Array.isArray(assertions) || assertions.length < 1 || assertions.length > 20 || assertions.some(value => {
    if (!value || typeof value !== "object" || Array.isArray(value)) return true;
    const item = value as Record<string, unknown>;
    return Object.keys(item).sort().join(",") !== "evidence_ref,source_ref,status,text" ||
      !text(item.text, 800) || typeof item.source_ref !== "string" || !REF.test(item.source_ref) ||
      typeof item.evidence_ref !== "string" || !REF.test(item.evidence_ref) ||
      !["documented", "conflicting", "narrative"].includes(String(item.status));
  })) throw new Error("ASSERTIONS_INVALID");
  const { assertions_json: _internal, ...safe } = row;
  return { ...safe, assertions: assertions as KnowledgeRecord["assertions"] };
}

export function parseKnowledgePackage(bytes: Uint8Array, releaseId: string): Map<string, KnowledgeRecord> {
  if (bytes.length < 2 || bytes.length > KNOWLEDGE_PACKAGE_LIMIT) throw new Error("PACKAGE_LIMIT");
  let body: unknown;
  try { body = JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(bytes)); } catch { throw new Error("PACKAGE_INVALID"); }
  if (!body || typeof body !== "object" || Array.isArray(body)) throw new Error("PACKAGE_INVALID");
  const pkg = body as Record<string, unknown>;
  if (Object.keys(pkg).sort().join(",") !== "profile,records" || pkg.profile !== "kfm.kansas-knowledge/v1" ||
      !Array.isArray(pkg.records) || pkg.records.length > 1000) throw new Error("PACKAGE_INVALID");
  const records = new Map<string, KnowledgeRecord>();
  for (const value of pkg.records) {
    if (!value || typeof value !== "object" || Array.isArray(value) || "release_id" in value) throw new Error("PACKAGE_INVALID");
    const record = publicKnowledgeRecord({ ...(value as Omit<KnowledgeRow, "release_id">), release_id: releaseId });
    if (records.has(record.record_id)) throw new Error("PACKAGE_INVALID");
    records.set(record.record_id, record);
  }
  return records;
}

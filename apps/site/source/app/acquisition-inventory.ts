// A Site projection of tools/local_data acquisition receipts, not a source registry.
export const ACQUISITION_MAX_BYTES = 1_048_576;
export const ACQUISITION_CACHE_LIMIT = 500_000_000_000;
export type AcquisitionJob = {
  job_id: string; source_id: string; dataset_id: string; label: string;
  state: "planned" | "blocked" | "running" | "complete" | "captured" | "failed";
  reason: string; expected_bytes: number | null; approved_max_bytes?: number | null; downloaded_bytes: number; protected?: boolean;
  sha256: string | null; checksum_verified: boolean;
  checksum_basis?: "provider-expected" | "capture-readback"; provider_digest?: string | null; bytes_received?: number;
  intended_destination?: "local-pc";
  temporal_start: string | null; temporal_end: string | null;
  storage: "provider-remote" | "local-replaceable-cache" | "local-protected-candidate";
  source_url: string; updated_at: string; scope: "kansas" | "global";
  estimate_basis: "provider" | "calculated" | "unknown"; rights_url?: string;
};
export type AcquisitionInventory = {
  schema_version: "kfm-acquisition-inventory-v1"; generated_at: string; lifecycle: "candidate-only";
  cache: { limit_bytes: number; used_bytes: number; temporary_bytes: number; replaceable_bytes: number; inspected?: boolean; budget_scope?: "new-cache-transfers" };
  jobs: AcquisitionJob[];
};
const record = (v: unknown): v is Record<string, unknown> => Boolean(v && typeof v === "object" && !Array.isArray(v));
const text = (v: unknown, max = 300): v is string => typeof v === "string" && v.length > 0 && v.length <= max && !/[\x00-\x1f\x7f]/.test(v);
const digest = (v: unknown): v is string => typeof v === "string" && /^[a-f0-9]{64}$/.test(v);
const bytes = (v: unknown): v is number => Number.isSafeInteger(v) && Number(v) >= 0;
const byteBound = (v: unknown, maximum = Number.MAX_SAFE_INTEGER): v is number => bytes(v) && v > 0 && v <= maximum;
const calendarDay = (v: string): boolean => {
  const parsed = Date.parse(`${v}T00:00:00Z`);
  return /^\d{4}-\d{2}-\d{2}$/.test(v) && Number.isFinite(parsed) && new Date(parsed).toISOString().slice(0, 10) === v;
};
const stamp = (v: unknown): v is string => text(v, 40) && /^\d{4}-\d{2}-\d{2}T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d{1,6})?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)$/.test(v) && calendarDay(v.slice(0, 10)) && Number.isFinite(Date.parse(v));
const date = (v: unknown): v is string | null => v === null || (text(v, 40) && (/^\d{4}$/.test(v) || /^\d{4}-(?:0[1-9]|1[0-2])$/.test(v) || calendarDay(v) || stamp(v)));
// Links are references only: the Site never fetches these or treats them as transport permission.
function sourceUrl(v: unknown): v is string {
  if (!text(v, 1200)) return false;
  try { const url = new URL(v); return url.protocol === "https:" && !url.username && !url.password && !url.search && !url.hash && !["localhost", "127.0.0.1", "[::1]"].includes(url.hostname); }
  catch { return false; }
}
export function parseAcquisitionInventory(value: unknown): AcquisitionInventory | null {
  if (!record(value) || value.schema_version !== "kfm-acquisition-inventory-v1" || value.lifecycle !== "candidate-only" || !stamp(value.generated_at)
    || !record(value.cache) || !Array.isArray(value.jobs) || value.jobs.length > 2000) return null;
  const cache = value.cache;
  const recordedLimit = cache.limit_bytes;
  if (!byteBound(recordedLimit) || cache.budget_scope !== undefined && cache.budget_scope !== "new-cache-transfers") return null;
  const jobLimit = cache.budget_scope === "new-cache-transfers" ? Number.MAX_SAFE_INTEGER : recordedLimit;
  if (![cache.used_bytes, cache.temporary_bytes, cache.replaceable_bytes].every(bytes)) return null;
  if (cache.inspected !== undefined && typeof cache.inspected !== "boolean") return null;
  if (Number(cache.temporary_bytes) > Number(cache.used_bytes) || Number(cache.replaceable_bytes) > Number(cache.used_bytes) - Number(cache.temporary_bytes)) return null;
  const jobs: AcquisitionJob[] = [];
  const ids = new Set<string>();
  for (const item of value.jobs) {
    if (!record(item) || !text(item.job_id) || ids.has(item.job_id) || !text(item.source_id) || !text(item.dataset_id) || !text(item.label)
      || !["planned", "blocked", "running", "complete", "captured", "failed"].includes(String(item.state))
      || !(item.reason === null || (typeof item.reason === "string" && item.reason.length <= 1200 && !/[\x00-\x1f\x7f]/.test(item.reason)))
      || !(item.expected_bytes === null || byteBound(item.expected_bytes, jobLimit)) || !bytes(item.downloaded_bytes)
      || !(item.approved_max_bytes === undefined || item.approved_max_bytes === null || byteBound(item.approved_max_bytes, jobLimit))
      || (item.protected !== undefined && typeof item.protected !== "boolean")
      || !(item.sha256 === null || digest(item.sha256))
      || (item.checksum_basis !== undefined && !["provider-expected", "capture-readback"].includes(String(item.checksum_basis)))
      || (item.provider_digest !== undefined && item.provider_digest !== null && !digest(item.provider_digest))
      || (item.bytes_received !== undefined && (!bytes(item.bytes_received) || item.bytes_received !== item.downloaded_bytes))
      || (item.intended_destination !== undefined && item.intended_destination !== "local-pc")
      || typeof item.checksum_verified !== "boolean" || !date(item.temporal_start) || !date(item.temporal_end)
      || !["provider-remote", "local-replaceable-cache", "local-protected-candidate"].includes(String(item.storage)) || !sourceUrl(item.source_url)
      || !stamp(item.updated_at) || !["kansas", "global"].includes(String(item.scope))
      || !["provider", "calculated", "unknown"].includes(String(item.estimate_basis))
      || (item.rights_url !== undefined && item.rights_url !== null && !sourceUrl(item.rights_url))) return null;
    if (item.temporal_start && item.temporal_end && Date.parse(item.temporal_start) > Date.parse(item.temporal_end)) return null;
    if (item.expected_bytes !== null && item.downloaded_bytes > item.expected_bytes) return null;
    if (typeof item.approved_max_bytes === "number" && (item.downloaded_bytes > item.approved_max_bytes || (item.expected_bytes !== null && item.expected_bytes > item.approved_max_bytes))) return null;
    // Capture-readback is a separate protected candidate, never expected-provider verification.
    if (item.state === "captured" && (item.checksum_basis !== "capture-readback" || item.provider_digest !== null
      || !digest(item.sha256) || item.checksum_verified !== false || !byteBound(item.bytes_received, jobLimit)
      || item.storage !== "local-protected-candidate" || item.protected !== true || item.intended_destination !== "local-pc"
      || (item.expected_bytes === null && typeof item.approved_max_bytes !== "number"))) return null;
    if (item.checksum_basis === "capture-readback" && item.state !== "captured") return null;
    if (item.storage === "local-protected-candidate" && item.state !== "captured") return null;
    if (item.provider_digest !== undefined && item.provider_digest !== null && item.provider_digest !== item.sha256) return null;
    if (item.checksum_basis === "provider-expected" && item.provider_digest === null) return null;
    if (item.checksum_verified && (!item.sha256 || item.state !== "complete")) return null;
    if (item.state === "complete" && (!item.checksum_verified || !item.sha256 || item.downloaded_bytes <= 0 || item.storage !== "local-replaceable-cache"
      || (item.expected_bytes !== null ? item.expected_bytes !== item.downloaded_bytes : typeof item.approved_max_bytes !== "number"))) return null;
    if (item.expected_bytes === null && item.estimate_basis !== "unknown") return null;
    ids.add(item.job_id);
    jobs.push({ job_id: item.job_id, source_id: item.source_id, dataset_id: item.dataset_id, label: item.label,
      state: item.state as AcquisitionJob["state"], reason: item.reason ?? "", expected_bytes: item.expected_bytes, downloaded_bytes: item.downloaded_bytes,
      ...(item.approved_max_bytes !== undefined ? { approved_max_bytes: item.approved_max_bytes } : {}), ...(item.protected !== undefined ? { protected: item.protected } : {}),
      sha256: item.sha256, checksum_verified: item.checksum_verified,
      ...(item.checksum_basis !== undefined ? { checksum_basis: item.checksum_basis as AcquisitionJob["checksum_basis"] } : {}),
      ...(item.provider_digest !== undefined ? { provider_digest: item.provider_digest as string | null } : {}),
      ...(item.bytes_received !== undefined ? { bytes_received: item.bytes_received } : {}),
      ...(item.intended_destination !== undefined ? { intended_destination: item.intended_destination } : {}), temporal_start: item.temporal_start, temporal_end: item.temporal_end,
      storage: item.storage as AcquisitionJob["storage"], source_url: item.source_url, updated_at: item.updated_at, scope: item.scope as AcquisitionJob["scope"],
      estimate_basis: item.estimate_basis as AcquisitionJob["estimate_basis"], ...(item.rights_url ? {rights_url: item.rights_url} : {}) });
  }
  return { schema_version: "kfm-acquisition-inventory-v1", lifecycle: "candidate-only", generated_at: value.generated_at,
    cache: { limit_bytes: recordedLimit, used_bytes: cache.used_bytes as number, temporary_bytes: cache.temporary_bytes as number, replaceable_bytes: cache.replaceable_bytes as number, ...(cache.inspected !== undefined ? { inspected: cache.inspected } : {}), ...(cache.budget_scope === "new-cache-transfers" ? { budget_scope: cache.budget_scope } : {}) }, jobs };
}
export function formatAcquisitionBytes(value: number | null) {
  if (value === null) return "Unknown — selection required";
  if (value < 1024) return `${value} B`;
  const index = Math.min(4, Math.floor(Math.log(value) / Math.log(1024)));
  return `${(value / 1024 ** index).toFixed(1)} ${["B", "KiB", "MiB", "GiB", "TiB"][index]}`;
}

/** Labels describe the retained receipt's assertions, never Site-side payload verification. */
export function acquisitionJobLabels(job: AcquisitionJob) {
  return {
    status: job.state === "captured" ? "Captured locally · not reviewed or admitted" : job.state === "complete" ? "Captured · expected checksum verified" : job.state,
    checksum: job.state === "captured" ? "Stored-file hash checked; provider checksum unavailable" : null,
    digest: job.state === "captured" ? "Stored-file SHA-256" : "Expected SHA-256",
    storage: job.storage === "local-protected-candidate" ? "Protected local candidate · outside replaceable cache" : job.storage === "provider-remote" ? "Provider-hosted archive" : job.protected ? "Protected local cache" : "Replaceable local cache",
  };
}

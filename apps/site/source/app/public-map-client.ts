import { readBoundedJson } from "./bounded-json";
import { PUBLIC_MAP_MAX_BYTES, publicMapCount, publicMapStamp, publicMapText } from "./public-map-catalog";

export type PublicMapJob = {
  id: string; assetId: string; title: string;
  state: "queued" | "downloading" | "downloaded" | "failed" | "cancelled" | "interrupted";
  bytes: number; expectedBytes: number | null; maxBytes: number; sha256: string | null;
  destination: string; reason: string | null; mapReady: false; createdAt: string; updatedAt: string;
};
export type PublicMapAssetState = { assetId: string; state: PublicMapJob["state"] | "partial" | "missing" | "outdated" };
export type PublicMapStatus = {
  schema: "kfm-public-map-download-control/v1"; sessionToken: string; jobs: PublicMapJob[];
  active: string | null; limitBytes: number; refresh: { state: "idle" | "running" | "complete" | "failed"; reason?: string };
  /** Files waiting behind the active one; absent from operators without a queue. */
  queued?: number;
  /** Complete tracked history; completed copies passed a local presence/size check. */
  assetStates?: PublicMapAssetState[];
};
const object = (v: unknown): v is Record<string, unknown> => !!v && typeof v === "object" && !Array.isArray(v);
const id = (v: unknown): v is string => typeof v === "string" && /^[a-f0-9]{32}$/.test(v);
const hash = (v: unknown) => typeof v === "string" && /^[a-f0-9]{64}$/.test(v);
export function parsePublicMapStatus(value: unknown): PublicMapStatus | null {
  if (!object(value) || value.schema !== "kfm-public-map-download-control/v1" || typeof value.sessionToken !== "string" || !/^[-_A-Za-z0-9]{43}$/.test(value.sessionToken)
    || !(value.active === null || id(value.active)) || !publicMapCount(value.limitBytes) || value.limitBytes < 1 || value.limitBytes > Number.MAX_SAFE_INTEGER
    || !Array.isArray(value.jobs) || value.jobs.length > 100 || !object(value.refresh) || !["idle", "running", "complete", "failed"].includes(String(value.refresh.state))
    || value.refresh.reason !== undefined && !publicMapText(value.refresh.reason, 200)
    || value.queued !== undefined && (!publicMapCount(value.queued) || value.queued > 300 || value.queued > 0 && value.active === null)) return null;
  const seen = new Set<string>();
  for (const job of value.jobs) {
    if (!object(job) || !id(job.id) || seen.has(job.id) || !publicMapText(job.assetId, 500) || !job.assetId || !publicMapText(job.title, 2000)
      || !["queued", "downloading", "downloaded", "failed", "cancelled", "interrupted"].includes(String(job.state))
      || !publicMapCount(job.bytes) || !publicMapCount(job.maxBytes) || job.maxBytes < 1 || job.bytes > job.maxBytes
      || !(job.expectedBytes === null || publicMapCount(job.expectedBytes) && job.expectedBytes > 0)
      || !(job.sha256 === null || hash(job.sha256)) || !publicMapText(job.destination, 2000)
      || !(job.reason === null || job.reason === undefined || publicMapText(job.reason, 300)) || job.mapReady !== false
      || !publicMapStamp(job.createdAt) || !publicMapStamp(job.updatedAt)
      || job.state === "downloaded" && (!hash(job.sha256) || job.bytes < 1 || job.expectedBytes !== null && job.bytes !== job.expectedBytes)) return null;
    seen.add(job.id);
  }
  if (value.active !== null && !seen.has(value.active)) return null;
  if (value.assetStates !== undefined) {
    if (!Array.isArray(value.assetStates) || value.assetStates.length > 1000) return null;
    const assets = new Set<string>();
    for (const item of value.assetStates) {
      if (!object(item) || !publicMapText(item.assetId, 500) || !item.assetId || assets.has(item.assetId)
        || !["queued", "downloading", "downloaded", "failed", "cancelled", "interrupted", "partial", "missing", "outdated"].includes(String(item.state))) return null;
      assets.add(item.assetId);
    }
  }
  return value as unknown as PublicMapStatus;
}
export type PublicMapEndpoint = "/catalog" | "/status" | "/downloads" | "/cancel" | "/refresh" | "/queue" | "/queue/cancel";
const endpoints = new Set<PublicMapEndpoint>(["/catalog", "/status", "/downloads", "/cancel", "/refresh", "/queue", "/queue/cancel"]);
/** Fixed existing local worker; reference links never become request destinations. */
export async function publicMapRequest(path: PublicMapEndpoint, signal: AbortSignal, payload?: unknown, sessionToken?: string) {
  if (!endpoints.has(path) || payload !== undefined && (!sessionToken || !/^[-_A-Za-z0-9]{43}$/.test(sessionToken))) throw new Error("Connect to local map downloads first.");
  const combined = AbortSignal.any([signal, AbortSignal.timeout(path === "/catalog" ? 20_000 : 10_000)]);
  combined.throwIfAborted();
  const response = await fetch(`http://127.0.0.1:8769/public-maps${path}`, { signal: combined, credentials: "omit", cache: "no-store", redirect: "error",
    ...(payload === undefined ? {} : { method: "POST", headers: { "Content-Type": "application/json", "X-KFM-Session": sessionToken! }, body: JSON.stringify(payload) }) });
  const body = await readBoundedJson(response, path === "/catalog" ? PUBLIC_MAP_MAX_BYTES : path === "/status" ? 2_000_000 : 256_000, combined);
  combined.throwIfAborted();
  return { response, body };
}
export const publicMapJobLabels: Record<PublicMapJob["state"], string> = {
  queued: "Queued", downloading: "Downloading", downloaded: "Stored candidate · awaiting review", failed: "Download failed",
  cancelled: "Cancelled · partial files retained", interrupted: "Interrupted · partial files retained",
};
export const publicMapReason = (reason: string) => ({
  CACHE_BUDGET_EXCEEDED: "The selected maximum exceeds your saved local cache budget. Update Local cache budget or select a smaller maximum.",
  SELECTED_LIMIT_TOO_SMALL: "The selected maximum is below the file size.", INSUFFICIENT_FREE_SPACE_FOR_LIMIT: "The selected maximum exceeds available disk capacity.",
  DOWNLOAD_ALREADY_RUNNING: "A file is already downloading. Wait or cancel before starting another.", CANCELLED: "Any captured bytes remain for inspection.",
  SIZE_LIMIT_EXCEEDED: "The response exceeded the selected byte maximum.", WORKER_RESTARTED: "The local worker restarted; retained files need inspection.",
  ASSET_NOT_DOWNLOADABLE: "This source offers metadata or a request route, not a verified direct download.",
  ASSET_FORMAT_MISMATCH: "The provider returned something other than the expected file type.", JOB_HISTORY_LIMIT: "The local download history is full; no more files can be queued.",
  ASSET_EXCEEDS_SELECTED_LIMIT: "A file is larger than the selected maximum per file.",
} as Record<string, string>)[reason] ?? "The local service could not finish this request. Reconnect to check its current state before retrying.";

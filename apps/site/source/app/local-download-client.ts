import { readBoundedJson } from "./bounded-json";

export const LOCAL_DOWNLOAD_ORIGIN = "http://127.0.0.1:8769";
export const automaticLocalConnection = (origin: string) => origin === "http://127.0.0.1:4173";
export type DownloadJob = { id: string; selection: { dataset: string; year: number | null; maxBytes: number }; state: "queued" | "preparing" | "downloading" | "downloaded" | "failed" | "cancelled" | "interrupted"; bytes: number; completed: number; total: number; destination: string; reason?: string; mapReady: false; createdAt: string };
export type DownloadStatus = { schema: "kfm-ee-download-control/v1"; configured: boolean; project?: string | null; authentication?: string; signedIn?: boolean; accountEmail?: string | null; projects?: string[]; projectDiscovery?: "idle" | "complete" | "limited" | "unavailable"; authError?: string | null; destination: string; sessionToken: string; active: string | null; limitBytes?: number; jobs: DownloadJob[] };
export type LibraryEntry = { id: string; label: string; lane: "raw" | "work" | "quarantine" | "processed"; files: number; bytes: number; role: "stored-candidate" | "archive-context" | "review-material"; dataset?: string; period?: string };
export type LocalLibrary = { schema: "kfm-local-library/v1"; state: "idle" | "scanning" | "complete" | "failed"; scannedFiles: number; generatedAt: string | null; entries: LibraryEntry[]; totalBytes: number; totalFiles: number; error: string | null };
const object = (v: unknown): v is Record<string, unknown> => Boolean(v && typeof v === "object" && !Array.isArray(v));
const text = (v: unknown, max = 1000): v is string => typeof v === "string" && v.length <= max && !/[\x00-\x1f\x7f]/.test(v);
const count = (v: unknown): v is number => Number.isSafeInteger(v) && Number(v) >= 0;
const stamp = (v: unknown): v is string => typeof v === "string" && /^\d{4}-\d{2}-\d{2}T/.test(v) && Number.isFinite(Date.parse(v));
export function parseDownloadStatus(value: unknown): DownloadStatus | null {
  if (!object(value) || value.schema !== "kfm-ee-download-control/v1" || typeof value.configured !== "boolean" || !text(value.destination)
    || !(value.active === null || typeof value.active === "string" && /^[a-f0-9]{32}$/.test(value.active))
    || typeof value.sessionToken !== "string" || !/^[-_A-Za-z0-9]{43}$/.test(value.sessionToken)
    || !Array.isArray(value.jobs) || value.jobs.length > 100 || value.project !== undefined && value.project !== null && !text(value.project, 100)
    || value.authentication !== undefined && !text(value.authentication, 40)) return null;
  if (value.signedIn !== undefined && typeof value.signedIn !== "boolean"
    || value.accountEmail !== undefined && value.accountEmail !== null && !text(value.accountEmail, 254)
    || value.projects !== undefined && (!Array.isArray(value.projects) || value.projects.length > 100 || !value.projects.every(p => typeof p === "string" && /^[a-z][a-z0-9-]{4,61}[a-z0-9]$/.test(p)))
    || value.projectDiscovery !== undefined && !["idle", "complete", "limited", "unavailable"].includes(String(value.projectDiscovery))
    || value.authError !== undefined && value.authError !== null && !["GOOGLE_SIGN_IN_FAILED", "GOOGLE_SIGN_IN_REQUIRED", "PROJECT_ACCESS_REQUIRED"].includes(String(value.authError))) return null;
  if (value.limitBytes !== undefined && (!count(value.limitBytes) || value.limitBytes < 1)) return null;
  const ids = new Set<string>();
  for (const job of value.jobs) {
    if (!object(job) || typeof job.id !== "string" || !/^[a-f0-9]{32}$/.test(job.id) || ids.has(job.id) || !object(job.selection)
      || !text(job.selection.dataset, 100) || !(job.selection.year === null || Number.isInteger(job.selection.year) && Number(job.selection.year) >= 1800 && Number(job.selection.year) <= 2200)
      || !count(job.selection.maxBytes) || job.selection.maxBytes === 0
      || !count(job.bytes) || !text(job.destination, 1200) || job.mapReady !== false || !count(job.completed) || !count(job.total) || job.total < job.completed
      || !text(job.createdAt, 50) || !Number.isFinite(Date.parse(job.createdAt)) || job.reason !== undefined && !text(job.reason, 200)
      || !["queued", "preparing", "downloading", "downloaded", "failed", "cancelled", "interrupted"].includes(String(job.state))) return null;
    ids.add(job.id);
  }
  if (value.active !== null && !ids.has(value.active)) return null;
  return value as unknown as DownloadStatus;
}

export function parseLocalLibrary(value: unknown): LocalLibrary | null {
  if (!object(value) || value.schema !== "kfm-local-library/v1" || !["idle", "scanning", "complete", "failed"].includes(String(value.state))
    || !count(value.scannedFiles) || !(value.generatedAt === null || stamp(value.generatedAt)) || !Array.isArray(value.entries) || value.entries.length > 256
    || !count(value.totalFiles) || !count(value.totalBytes) || !(value.error === null || ["LIBRARY_SCAN_LIMIT", "LIBRARY_SCAN_FAILED", "LIBRARY_SCAN_UNSAFE", "LIBRARY_SCAN_CHANGED"].includes(String(value.error)))) return null;
  if (value.limitBytes !== undefined && (!count(value.limitBytes) || value.limitBytes < 1)) return null;
  const ids = new Set<string>();
  let files = 0, bytes = 0;
  for (const entry of value.entries) {
    if (!object(entry) || typeof entry.id !== "string" || !/^[a-f0-9]{64}$/.test(entry.id) || ids.has(entry.id) || !text(entry.label, 300) || !entry.label
      || !["raw", "work", "quarantine", "processed"].includes(String(entry.lane)) || !["stored-candidate", "archive-context", "review-material"].includes(String(entry.role)) || !count(entry.files) || !count(entry.bytes)) return null;
    if (entry.dataset !== undefined && (!text(entry.dataset, 100) || !/^ee-[a-z0-9-]+$/.test(entry.dataset)) || entry.period !== undefined && (!text(entry.period, 10) || !/^(?:[0-9]{4}|fixed)$/.test(entry.period))) return null;
    ids.add(entry.id); files += entry.files; bytes += entry.bytes;
  }
  if (!Number.isSafeInteger(files) || !Number.isSafeInteger(bytes) || files !== value.totalFiles || bytes !== value.totalBytes
    || value.generatedAt === null && (value.entries.length > 0 || value.totalFiles !== 0 || value.totalBytes !== 0)
    || value.state === "complete" && value.generatedAt === null) return null;
  return value as unknown as LocalLibrary;
}

export type DownloadEndpoint = "/status" | "/library" | "/library/refresh" | "/downloads" | "/cancel" | "/auth/start" | "/auth/check" | "/cache-budget";
/** The complete response, including a stalled body, shares one deadline and caller cancellation. */
export async function localDownloadRequest(path: DownloadEndpoint, signal: AbortSignal, payload?: unknown, sessionToken?: string) {
  const combined = AbortSignal.any([signal, AbortSignal.timeout(path === "/downloads" ? 10_000 : 8_000)]);
  combined.throwIfAborted();
  const response = await fetch(`${LOCAL_DOWNLOAD_ORIGIN}${path}`, { signal: combined, credentials: "omit", cache: "no-store",
    ...(payload === undefined ? {} : { method: "POST", headers: { "Content-Type": "application/json", "X-KFM-Session": sessionToken ?? "" }, body: JSON.stringify(payload) }) });
  const body = await readBoundedJson(response, path === "/status" || path === "/library" || path === "/library/refresh" ? 256_000 : 64_000, combined);
  combined.throwIfAborted();
  return { response, body };
}
export function formatDownloadBytes(value: number) {
  if (value >= 1e9) return `${(value / 1e9).toFixed(2)} GB`;
  if (value >= 1e6) return `${(value / 1e6).toFixed(1)} MB`;
  if (value >= 1e3) return `${(value / 1e3).toFixed(1)} kB`;
  return `${value} B`;
}
export const libraryRoleLabels: Record<LibraryEntry["role"], string> = { "stored-candidate": "Private candidate", "archive-context": "Archive context", "review-material": "Review material" };
export const jobStateLabels: Record<DownloadJob["state"], string> = { queued: "Queued", preparing: "Preparing source selection", downloading: "Downloading", downloaded: "Downloaded · awaiting map review", failed: "Download failed", cancelled: "Cancelled · partial files retained", interrupted: "Interrupted · partial files retained" };
export const downloadReasons: Record<string, string> = {
  CACHE_BUDGET_EXCEEDED: "The selected maximum exceeds your saved local cache budget. Change it in Data & downloads → Local cache budget.",
  EARTH_ENGINE_SETUP_REQUIRED: "Link your Earth Engine project on this computer.", SELECTED_LIMIT_BELOW_GRID_ESTIMATE: "The chosen maximum is below the product’s grid estimate. Choose a larger maximum for a new download.",
  INSUFFICIENT_FREE_SPACE_FOR_LIMIT: "The selected maximum exceeds available disk capacity.", SOURCE_PERIOD_INCOMPLETE: "The source period is incomplete or duplicated. No substitute period was used.",
  NO_DATA_OR_SOURCE_LIMIT: "No source data was found, or the selection exceeds the source inventory limit.", EARTH_ENGINE_REQUEST_FAILED: "Check Earth Engine project access and quota, then retry.",
  DOWNLOAD_ALREADY_RUNNING: "A download is already running. Let it finish or cancel it first.", CANCELLED: "Captured files remain available for inspection.", WORKER_RESTARTED: "The worker restarted. Captured files remain available; a new download can retry this selection.",
};

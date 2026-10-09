import type { DownloadJob, DownloadStatus } from "./local-download-client";
import type { PublicMapJob, PublicMapStatus } from "./public-map-client";

export const terminalDownloadState = (state: string) => ["downloaded", "failed", "cancelled", "interrupted"].includes(state);
type ActivityBase = {
  key: string; nativeId: string; provider: string; label: string; title: string;
  state: DownloadJob["state"]; createdAt: string; active: boolean; bytes: number; maxBytes: number;
  progress: { unit: "files" | "bytes" | "unknown"; value: number | null; total: number | null };
};
export type ActivityItem = ActivityBase & ({ kind: "earth-engine"; job: DownloadJob } | { kind: "public-map"; job: PublicMapJob });

/** Native progress units stay distinct; a selected stop limit is never a total. */
export function normalizeDownloadActivity(local: DownloadStatus | null, maps: PublicMapStatus | null): ActivityItem[] {
  const rows: ActivityItem[] = [
    ...(local?.jobs ?? []).map((job): ActivityItem => ({ key: `earth-engine:${job.id}`, kind: "earth-engine", nativeId: job.id,
      provider: "Earth Engine", label: "Satellite & climate", title: `${job.selection.dataset} · ${job.selection.year ?? "fixed period"}`,
      state: job.state, createdAt: job.createdAt, active: job.id === local?.active, bytes: job.bytes, maxBytes: job.selection.maxBytes,
      progress: job.total > 0 ? { unit: "files", value: job.completed, total: job.total } : { unit: "unknown", value: null, total: null }, job })),
    ...(maps?.jobs ?? []).map((job): ActivityItem => ({ key: `public-map:${job.id}`, kind: "public-map", nativeId: job.id,
      provider: "Public maps", label: "Maps & geology", title: job.title, state: job.state, createdAt: job.createdAt,
      active: job.id === maps?.active, bytes: job.bytes, maxBytes: job.maxBytes,
      progress: job.expectedBytes !== null && job.expectedBytes > 0 ? { unit: "bytes", value: job.bytes, total: job.expectedBytes }
        : { unit: "unknown", value: null, total: null }, job })),
  ];
  return rows.sort((a, b) => Number(b.active) - Number(a.active) || b.createdAt.localeCompare(a.createdAt) || a.key.localeCompare(b.key));
}

/** Seed from the initial snapshot; only later terminal observations trigger work. */
export function observeDownloadTransitions(previous: Map<string, string> | null, jobs: { id: string; state: string }[]) {
  const next = new Map(previous ?? []), changed: typeof jobs = [], terminal: typeof jobs = [];
  for (const job of jobs) {
    const prior = previous?.get(job.id);
    if (previous && prior !== job.state) {
      changed.push(job);
      if (terminalDownloadState(job.state) && (prior === undefined || !terminalDownloadState(prior))) terminal.push(job);
    }
    next.set(job.id, job.state);
  }
  return { next, changed, terminal };
}

import { isEmbeddedSiteRuntime } from "./embed-runtime";

const archiveBounds = { "usgs-earthquakes": "0001-01-01", "noaa-hms-smoke": "2005-08-05", "nasa-gibs-fire-points": "2018-01-01", "raspberry-shake-stations": "0001-01-01" } as const;
export type ArchiveViewFeed = keyof typeof archiveBounds;
export const restoreArchiveViewDays = (value: string | null, today: string): Partial<Record<ArchiveViewFeed, string>> => {
  const days: Partial<Record<ArchiveViewFeed, string>> = {};
  for (const pair of (value ?? "").slice(0, 512).split(",")) {
    const [id, day] = pair.split(":");
    if (!Object.hasOwn(archiveBounds, id) || !/^\d{4}-\d{2}-\d{2}$/.test(day ?? "") || day > today || day < archiveBounds[id as ArchiveViewFeed]) continue;
    const instant = Date.parse(`${day}T00:00:00Z`);
    if (Number.isFinite(instant) && new Date(instant).toISOString().slice(0, 10) === day) days[id as ArchiveViewFeed] = day;
  }
  return days;
};

export const explorerHistoryParams = (search: string, state: unknown): URLSearchParams => {
  const saved = state && typeof state === "object" && "kfmExplorerView" in state ? state.kfmExplorerView : null;
  return new URLSearchParams(typeof saved === "string" && saved.length <= 12000 ? saved : search);
};

/** Retain this tab's context without changing its URL or the embedded host's history. */
export const saveExplorerHistoryView = (params: URLSearchParams, history: Pick<History, "state" | "replaceState">, embedded = isEmbeddedSiteRuntime()): boolean => {
  if (embedded) return false;
  try {
    const saved = params.toString();
    if (saved.length > 12000) return false;
    history.replaceState({ ...history.state, kfmExplorerView: saved }, "");
    return true;
  } catch { return false; }
};

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

export const explorerHistoryWelcome = (state: unknown): boolean | null =>
  state && typeof state === "object" && "kfmExplorerWelcome" in state && typeof state.kfmExplorerWelcome === "boolean"
    ? state.kfmExplorerWelcome : null;

export const explorerHistoryEntryKey = (state: unknown): string | null => {
  const key = state && typeof state === "object" && "kfmExplorerEntry" in state ? state.kfmExplorerEntry : null;
  return typeof key === "string" && key.length > 0 && key.length <= 128 ? key : null;
};

/** Identify this native entry without adding a step or changing the route. */
export const ensureExplorerHistoryEntry = (history: Pick<History, "state" | "replaceState">, embedded = isEmbeddedSiteRuntime()): string | null => {
  if (embedded) return null;
  try {
    const key = explorerHistoryEntryKey(history.state) ?? crypto.randomUUID();
    if (explorerHistoryEntryKey(history.state) !== key) history.replaceState({ ...history.state, kfmExplorerEntry: key }, "");
    return key;
  } catch { return null; }
};

/** Deliberate navigation adds a step; camera changes update that step. Never alter the embedded host. */
export const saveExplorerHistoryView = (params: URLSearchParams, history: Pick<History, "state" | "replaceState"> & Partial<Pick<History, "pushState">>, embedded = isEmbeddedSiteRuntime(), options: { navigation?: boolean; welcome?: boolean; expectedEntry?: string } = {}): boolean => {
  if (embedded) return false;
  try {
    const saved = params.toString();
    if (saved.length > 12000) return false;
    const previous = history.state;
    // Traversal selects its destination before popstate/React passive effects
    // settle. A save from the old render must not overwrite that destination.
    if (options.expectedEntry !== undefined && explorerHistoryEntryKey(previous) !== options.expectedEntry) return false;
    const changed = previous?.kfmExplorerView !== saved || (options.welcome !== undefined && previous?.kfmExplorerWelcome !== options.welcome);
    const push = options.navigation && typeof previous?.kfmExplorerView === "string" && changed && history.pushState;
    const key = push ? crypto.randomUUID() : explorerHistoryEntryKey(previous) ?? crypto.randomUUID();
    const next = { ...previous, kfmExplorerEntry: key, kfmExplorerView: saved, ...(options.welcome === undefined ? {} : { kfmExplorerWelcome: options.welcome }) };
    if (push) history.pushState!(next, "");
    else history.replaceState(next, "");
    return true;
  } catch { return false; }
};

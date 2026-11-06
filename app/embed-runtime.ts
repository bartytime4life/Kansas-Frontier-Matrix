type HistoryLike = Pick<History, "replaceState"> & Partial<Pick<History, "state">>;

/**
 * Embedded Sites panels own their outer navigation. Updating the iframe history
 * on every Explorer state change can make the host discard the frame, so only a
 * top-level window may mirror state into its address bar.
 */
export const isEmbeddedSiteRuntime = (): boolean => {
  if (typeof window === "undefined") return false;
  try { return window.self !== window.top; } catch { return true; }
};

export const replaceExplorerHistory = (
  path: string,
  embedded = isEmbeddedSiteRuntime(),
  history: HistoryLike | undefined = typeof window === "undefined" ? undefined : window.history,
): boolean => {
  if (embedded || !history) return false;
  try {
    // Sharing updates this entry's URL. Its router and Explorer ownership
    // still belong to the same native entry and must survive the replacement.
    history.replaceState(history.state ?? null, "", path);
    return true;
  } catch {
    return false;
  }
};

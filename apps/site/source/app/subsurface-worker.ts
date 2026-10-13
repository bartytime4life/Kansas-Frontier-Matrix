type Query = { id: number; kind: "probe" | "search" | "area" | "prepare" };
const scope = self as unknown as { onmessage: ((event: MessageEvent<Query>) => void) | null; postMessage: (message: unknown) => void };

// Exact records remain withheld even if an older manifest survives in a cache.
// Re-enabling delivery requires a separately reviewed public-safe release path.
scope.onmessage = event => {
  if (event.origin && event.origin !== self.location.origin) return;
  scope.postMessage({ id: event.data.id, ...(event.data.kind === "prepare" ? { prepared: true } : {}), manifest: { version: 1, capturedAt: "2026-10-13T00:00:00Z", sources: [], tiles: [], counties: [], totals: { wellCount: 0, coreCount: 0 } }, columns: [], ...(event.data.kind === "search" ? { matches: [] } : {}), error: "Underground records are withheld pending rights, sensitivity and release review." });
};

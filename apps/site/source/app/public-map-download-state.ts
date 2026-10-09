import type { PublicMapStatus } from "./public-map-client";

export type CardDownloadState = {
  state: "downloaded" | "not-downloaded" | "partial" | "downloading" | "queued" | "missing" | "failed" | "cancelled" | "interrupted" | "unknown";
  label: string; detail: string; downloaded: number; total: number;
};

/** Exact asset identity, never title/year matching or the truncated Activity list. */
export function publicMapDownloadState(assetIds: readonly string[], status: PublicMapStatus | null, connection: string): CardDownloadState {
  const total = new Set(assetIds).size;
  const result = (state: CardDownloadState["state"], label: string, detail: string, downloaded = 0): CardDownloadState => ({ state, label, detail, downloaded, total });
  if (connection !== "connected" || !status) return result("unknown", connection === "connecting" ? "Checking downloads…" : "Status unknown", "Connect to this computer to check its downloads.");
  if (!status.assetStates || !total) return result("unknown", "Status unavailable", "The local service needs a download-status update. Recent activity alone cannot establish whether this file is stored.");
  const index = new Map(status.assetStates.map(item => [item.assetId, item.state]));
  const states = [...new Set(assetIds)].map(id => index.get(id));
  const downloaded = states.filter(state => state === "downloaded").length;
  const count = `${downloaded} of ${total} files downloaded`;
  const complete = "Completed by KFM; the recorded file is present at its captured size. This is not a fresh checksum or map approval.";
  if (downloaded === total) return result("downloaded", "Downloaded", total > 1 ? `${count}. ${complete}` : complete, downloaded);
  if (states.includes("downloading")) return result("downloading", "Downloading", total > 1 ? `${count} · a file is downloading.` : "Downloading to this computer.", downloaded);
  if (states.includes("queued")) return result("queued", "Queued", total > 1 ? `${count} · more files are queued.` : "Waiting in this computer’s download queue.", downloaded);
  if (downloaded || states.includes("partial")) return result("partial", downloaded ? `${downloaded} of ${total} downloaded` : "Partially downloaded", downloaded ? `${count}. Select this card to see each file’s status.` : "An incomplete transfer was recorded. A complete download is still needed.", downloaded);
  if (states.includes("missing")) return result("missing", "Check local file", "A completed download was recorded, but its local file could not be confirmed at the captured size.");
  for (const state of ["failed", "interrupted", "cancelled"] as const) {
    if (states.includes(state)) return result(state, "Not downloaded", `The previous transfer ${state === "failed" ? "failed" : `was ${state}`}; no complete copy is confirmed.`);
  }
  return result("not-downloaded", "Not downloaded", "No completed download is recorded by KFM on this computer. Files saved outside KFM are not tracked.");
}

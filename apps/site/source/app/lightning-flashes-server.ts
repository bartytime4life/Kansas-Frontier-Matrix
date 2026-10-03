import { GLM_FLASH_LIMIT, GLM_FLASH_SOURCE, parseGlmFlashSnapshot, type GlmFlashSnapshot, type GlmFlashWindow } from "./lightning-flashes";

const MAX_BYTES = 4 * 1024 * 1024;
const cache = new Map<GlmFlashWindow, { value: GlmFlashSnapshot; expires: number }>();
const pending = new Map<GlmFlashWindow, Promise<GlmFlashSnapshot>>();

export async function getGlmFlashSnapshot(windowMinutes: GlmFlashWindow): Promise<GlmFlashSnapshot> {
  const hit = cache.get(windowMinutes);
  if (hit && hit.expires > Date.now()) return hit.value;
  const inFlight = pending.get(windowMinutes);
  if (inFlight) return inFlight;
  const task = (async () => {
    const url = new URL(GLM_FLASH_SOURCE);
    url.search = new URLSearchParams({ state: "KS", minutes: String(windowMinutes), limit: String(GLM_FLASH_LIMIT) }).toString();
    const response = await fetch(url, { cache: "no-store", redirect: "manual", signal: AbortSignal.timeout(12_000), headers: { Accept: "application/json", "User-Agent": "KansasFrontierMatrixExplorer/1.0" } });
    if (!response.ok || !/application\/json/i.test(response.headers.get("content-type") ?? "") || !response.body) throw new Error(`GLM mirror unavailable (HTTP ${response.status}).`);
    if (Number(response.headers.get("content-length")) > MAX_BYTES) throw new Error("GLM mirror response exceeded the byte limit.");
    const reader = response.body.getReader();
    const parts: Uint8Array[] = [];
    let size = 0;
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      size += value.byteLength;
      if (size > MAX_BYTES) { await reader.cancel(); throw new Error("GLM mirror response exceeded the byte limit."); }
      parts.push(value);
    }
    const bytes = new Uint8Array(size);
    let offset = 0;
    for (const part of parts) { bytes.set(part, offset); offset += part.byteLength; }
    const snapshot = parseGlmFlashSnapshot(JSON.parse(new TextDecoder().decode(bytes)), windowMinutes);
    if (snapshot.state !== "stale") cache.set(windowMinutes, { value: snapshot, expires: Date.now() + 20_000 });
    return snapshot;
  })();
  pending.set(windowMinutes, task);
  try { return await task; } finally { pending.delete(windowMinutes); }
}

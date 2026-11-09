import { readBoundedText } from "./bounded-json";
import { NOAA_LIGHTNING_CAPABILITIES_URL, parseLightningCapabilities, type LightningManifest } from "./lightning-data";

const CAPABILITIES_LIMIT = 512 * 1024;
const IMAGE_LIMIT = 1024 * 1024;
const NOAA_USER_AGENT = "KansasFrontierMatrixExplorer/1.0 (https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)";
let cached: { manifest: LightningManifest; expires: number } | null = null;
let pending: Promise<LightningManifest> | null = null;

export async function getLightningManifest(): Promise<LightningManifest> {
  if (cached && cached.expires > Date.now()) return cached.manifest;
  if (pending) return pending;
  pending = (async () => {
    const response = await fetch(NOAA_LIGHTNING_CAPABILITIES_URL, {
      cache: "no-store", redirect: "manual", signal: AbortSignal.timeout(12_000),
      headers: { Accept: "application/xml,text/xml;q=0.9", "User-Agent": NOAA_USER_AGENT },
    });
    if (!response.ok || !/xml/i.test(response.headers.get("content-type") ?? "")) throw new Error(`NOAA lightning capabilities HTTP ${response.status}, content-type ${response.headers.get("content-type") ?? "missing"}.`);
    const xml = await readBoundedText(response, CAPABILITIES_LIMIT);
    if (!xml.includes("WMS_Capabilities")) throw new Error("NOAA lightning capabilities did not match WMS.");
    const manifest = parseLightningCapabilities(xml);
    cached = { manifest, expires: Date.now() + 120_000 };
    return manifest;
  })();
  try { return await pending; } finally { pending = null; }
}

export async function fetchLightningPng(url: string, signal?: AbortSignal): Promise<Uint8Array> {
  signal?.throwIfAborted();
  const controller = new AbortController();
  const abort = () => controller.abort(signal?.reason);
  signal?.addEventListener("abort", abort, { once: true });
  let response: Response | undefined;
  let reader: ReadableStreamDefaultReader<Uint8Array> | undefined;
  let complete = false;
  const cancelRead = () => { void reader?.cancel(controller.signal.reason).catch(() => undefined); };
  controller.signal.addEventListener("abort", cancelRead, { once: true });
  const timer = setTimeout(() => controller.abort(new DOMException("NOAA lightning image request timed out.", "TimeoutError")), 15_000);
  try {
    response = await fetch(url, { cache: "no-store", redirect: "manual", signal: controller.signal, headers: { Accept: "image/png", "User-Agent": NOAA_USER_AGENT } });
    controller.signal.throwIfAborted();
    if (!response.ok || !/image\/png/i.test(response.headers.get("content-type") ?? "")) throw new Error(`NOAA lightning image HTTP ${response.status}, content-type ${response.headers.get("content-type") ?? "missing"}.`);
    const announced = Number(response.headers.get("content-length"));
    if (announced > IMAGE_LIMIT) throw new Error("NOAA lightning image exceeds the limit.");
    if (!response.body) throw new Error("NOAA lightning response is not a bounded PNG.");
    reader = response.body.getReader();
    const chunks: Uint8Array[] = []; let length = 0;
    for (;;) {
      controller.signal.throwIfAborted();
      const { done, value } = await reader.read();
      controller.signal.throwIfAborted();
      if (done) break;
      length += value.byteLength;
      if (length > IMAGE_LIMIT) throw new Error("NOAA lightning image exceeds the limit.");
      chunks.push(value);
    }
    const bytes = new Uint8Array(length); let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
    if (bytes.length < 64 || ![137, 80, 78, 71, 13, 10, 26, 10].every((byte, index) => bytes[index] === byte)) throw new Error("NOAA lightning response is not a bounded PNG.");
    complete = true;
    return bytes;
  } finally {
    clearTimeout(timer);
    signal?.removeEventListener("abort", abort);
    if (!complete) {
      controller.abort();
      if (!reader) void response?.body?.cancel().catch(() => undefined);
    }
    controller.signal.removeEventListener("abort", cancelRead);
    reader?.releaseLock();
  }
}

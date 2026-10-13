import { readBoundedText } from "./bounded-json";
import { NOAA_LIGHTNING_CAPABILITIES_URL, parseLightningCapabilities, type LightningManifest } from "./lightning-data";

const CAPABILITIES_LIMIT = 512 * 1024;
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

export async function fetchLightningPng(url: string): Promise<Uint8Array> {
  const response = await fetch(url, { cache: "no-store", redirect: "manual", signal: AbortSignal.timeout(15_000), headers: { Accept: "image/png", "User-Agent": NOAA_USER_AGENT } });
  if (!response.ok || !/image\/png/i.test(response.headers.get("content-type") ?? "")) throw new Error(`NOAA lightning image HTTP ${response.status}, content-type ${response.headers.get("content-type") ?? "missing"}.`);
  const announced = Number(response.headers.get("content-length"));
  if (announced > 1024 * 1024) throw new Error("NOAA lightning image exceeds the limit.");
  const bytes = new Uint8Array(await response.arrayBuffer());
  if (bytes.length < 64 || bytes.length > 1024 * 1024 || ![137, 80, 78, 71, 13, 10, 26, 10].every((byte, index) => bytes[index] === byte)) throw new Error("NOAA lightning response is not a bounded PNG.");
  return bytes;
}

import { eventDay, exactUtc, type EventManifest, type RadarScan } from "./event-atlas";
import type { OfficialContextPayload } from "./live-context";

const ROOT = "KFM-map-display-context";
const FIRE_LIMIT = 8 * 1024 * 1024;
const RADAR_FRAME_LIMIT = 4 * 1024 * 1024;
export const RADAR_DOWNLOAD_MAX_BYTES = 500 * 1024 * 1024;

async function directory(parts: string[], create: boolean): Promise<FileSystemDirectoryHandle> {
  if (!navigator.storage?.getDirectory) throw new Error("Private browser file storage is unavailable here.");
  let node = await navigator.storage.getDirectory();
  for (const part of [ROOT, ...parts]) node = await node.getDirectoryHandle(part, { create });
  return node;
}

async function readFile(parts: string[], name: string): Promise<File | null> {
  try { return await (await (await directory(parts, false)).getFileHandle(name)).getFile(); }
  catch (error) { if (error instanceof DOMException && error.name === "NotFoundError") return null; throw error; }
}

async function writeFile(parts: string[], name: string, body: Blob | string) {
  const handle = await (await directory(parts, true)).getFileHandle(name, { create: true });
  const stream = await handle.createWritable();
  try { await stream.write(body); await stream.close(); }
  catch (error) { await stream.abort().catch(() => undefined); throw error; }
}

export function mapCachePath(kind: "radar" | "fire", day: string) {
  if (!eventDay(day)) throw new Error("Choose an exact UTC day.");
  return `${ROOT}/${kind === "radar" ? "radar" : "fire-detections"}/${day}`;
}

export function validFireCachePayload(day: string, value: unknown): value is OfficialContextPayload {
  if (!eventDay(day) || !value || typeof value !== "object") return false;
  const data = value as Partial<OfficialContextPayload>;
  return data.feed === "nasa-gibs-fire-points" && data.sourceDay === day
    && (data.state === "ready" || data.state === "empty" || data.state === "partial")
    && data.data?.type === "FeatureCollection" && Array.isArray(data.data.features)
    && data.featureCount === data.data.features.length && typeof data.retrievedAt === "string"
    && Number.isFinite(Date.parse(data.retrievedAt));
}

export async function saveFireDay(day: string, payload: unknown): Promise<number> {
  if (!validFireCachePayload(day, payload)) throw new Error("The NASA response does not match the selected UTC day.");
  const body = JSON.stringify(payload);
  const bytes = new Blob([body]).size;
  if (bytes > FIRE_LIMIT) throw new Error("The selected fire response exceeds the 8 MiB browser map limit.");
  await writeFile(["fire-detections"], `${day}.json`, body);
  return bytes;
}

export async function readFireDay(day: string): Promise<OfficialContextPayload | null> {
  if (!eventDay(day)) return null;
  const file = await readFile(["fire-detections"], `${day}.json`).catch(() => null);
  if (!file || file.size > FIRE_LIMIT) return null;
  try { const value: unknown = JSON.parse(await file.text()); return validFireCachePayload(day, value) ? value : null; }
  catch { return null; }
}

const radarName = (time: string) => {
  const exact = exactUtc(time);
  if (!exact || new Date(exact).getUTCMinutes() % 5 || new Date(exact).getUTCSeconds()) throw new Error("Invalid exact radar frame time.");
  return `${exact.slice(11, 16).replace(":", "")}.png`;
};

export async function saveRadarFrame(time: string, image: Blob): Promise<void> {
  if (!image.size || image.size > RADAR_FRAME_LIMIT || image.type !== "image/png") throw new Error("Radar frame exceeds the 4 MiB PNG limit.");
  await writeFile(["radar", time.slice(0, 10)], radarName(time), image);
}

export async function readRadarFrame(time: string): Promise<Blob | null> {
  let name: string;
  try { name = radarName(time); } catch { return null; }
  const index = await readRadarIndex(time.slice(0, 10));
  if (!index?.scans.some((scan) => scan.time === time)) return null;
  const file = await readFile(["radar", time.slice(0, 10)], name).catch(() => null);
  return file && file.size > 0 && file.size <= RADAR_FRAME_LIMIT ? file : null;
}

export type RadarCacheIndex = {
  format: "kfm-radar-map-cache-v1"; day: string; start: string; end: string;
  retrievedAt: string; savedAt: string; bytes: number; partial: boolean; scans: RadarScan[];
};

export function validRadarCacheIndex(value: unknown): value is RadarCacheIndex {
  if (!value || typeof value !== "object") return false;
  const index = value as Partial<RadarCacheIndex>;
  return index.format === "kfm-radar-map-cache-v1" && !!index.day && !!eventDay(index.day)
    && !!index.start && !!exactUtc(index.start) && !!index.end && !!exactUtc(index.end)
    && index.start.slice(0, 10) === index.day && index.start < index.end
    && !!index.retrievedAt && Number.isFinite(Date.parse(index.retrievedAt))
    && !!index.savedAt && Number.isFinite(Date.parse(index.savedAt))
    && typeof index.bytes === "number" && index.bytes >= 0 && index.bytes <= RADAR_DOWNLOAD_MAX_BYTES
    && typeof index.partial === "boolean" && Array.isArray(index.scans)
    && index.scans.length <= 288 && index.scans.every((scan) =>
      !!exactUtc(scan.time) && scan.time >= index.start! && scan.time < index.end!
      && scan.time.slice(0, 10) === index.day && ["n0r", "n0q"].includes(scan.product)
      && scan.artifact.startsWith("https://mesonet.agron.iastate.edu/archive/data/"));
}

export async function saveRadarIndex(index: RadarCacheIndex) {
  if (!validRadarCacheIndex(index)) throw new Error("Radar cache index does not match the selected interval.");
  await writeFile(["radar", index.day], "index.json", JSON.stringify(index));
}

export async function readRadarIndex(day: string): Promise<RadarCacheIndex | null> {
  if (!eventDay(day)) return null;
  const file = await readFile(["radar", day], "index.json").catch(() => null);
  if (!file || file.size > 100_000) return null;
  try { const value: unknown = JSON.parse(await file.text()); return validRadarCacheIndex(value) && value.day === day ? value : null; }
  catch { return null; }
}

export function radarManifestFromCache(index: RadarCacheIndex, start: string, end: string): EventManifest | null {
  if (!validRadarCacheIndex(index) || !exactUtc(start) || !exactUtc(end) || start < index.start || end > index.end) return null;
  const scans = index.scans.filter((scan) => scan.time >= start && scan.time < end);
  return {
    format: "kfm-event-atlas-v1", start, end, retrievedAt: index.retrievedAt,
    radar: { state: "partial", scans, gaps: ["Cached selection only; provider coverage was not rechecked."], message: "Private browser map cache. Missing frames remain unavailable." },
    smoke: { state: "empty", data: { type: "FeatureCollection", features: [] }, gaps: ["Not checked while using the radar cache."], message: "Other dynamic sources were not checked." },
    imagery: { dates: [], message: "Imagery was not checked while using the radar cache." },
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  };
}

import { archiveInterval, archiveLocation, parseArchiveListing, selectArchiveFiles, GLM_ARCHIVE_BATCH, type GlmArchiveQuery, type GlmArchiveManifest } from "./lightning-archive";

const manifests = new Map<string, { value: GlmArchiveManifest; expires: number }>();
async function noaaBytes(url: URL, limit: number, signal: AbortSignal) {
  if (!["https://noaa-goes16.s3.amazonaws.com", "https://noaa-goes19.s3.amazonaws.com"].includes(url.origin)) throw new Error("Unexpected NOAA host.");
  const response = await fetch(url, { redirect: "manual", signal, headers: { Accept: "*/*" } });
  if (!response.ok || !response.body || Number(response.headers.get("content-length")) > limit) throw new Error("NOAA archive unavailable or too large.");
  const reader = response.body.getReader(), chunks: Uint8Array[] = [];
  let length = 0;
  try {
    while (true) {
      signal.throwIfAborted();
      const { value, done } = await reader.read(); if (done) break;
      length += value.length;
      if (length > limit) throw new Error("NOAA archive exceeded its size limit.");
      chunks.push(value);
    }
  } catch (error) { await reader.cancel().catch(() => {}); throw error; }
  finally { reader.releaseLock(); }
  const bytes = new Uint8Array(length); let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  return bytes;
}

export async function getArchiveManifest(query: GlmArchiveQuery, signal: AbortSignal): Promise<GlmArchiveManifest> {
  const { start, end } = archiveInterval(query), key = JSON.stringify(query);
  const cached = manifests.get(key);
  if (cached && cached.expires > Date.now()) return cached.value;
  const locations = [archiveLocation(start), archiveLocation(end)];
  const unique = locations.filter((location, i) => i === 0 || location.prefix !== locations[0].prefix || location.satellite !== locations[0].satellite);
  const lists = await Promise.all(unique.map(async location => {
    const url = new URL(`https://noaa-goes${location.satellite}.s3.amazonaws.com/`);
    url.search = new URLSearchParams({ "list-type": "2", prefix: location.prefix, "max-keys": "200" }).toString();
    const bytes = await noaaBytes(url, 128 * 1024, signal);
    return parseArchiveListing(new TextDecoder().decode(bytes), location);
  }));
  const files = selectArchiveFiles(lists.flat(), start, end), expectedFiles = query.duration * 3 + 1;
  if (!files.length) throw new Error("No NOAA files are available for the selected interval.");
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(JSON.stringify({ query, files })));
  const id = Array.from(new Uint8Array(digest), b => b.toString(16).padStart(2, "0")).join("");
  const value: GlmArchiveManifest = { id, query, start: new Date(start).toISOString(), end: new Date(end).toISOString(), files, expectedFiles, missingFiles: expectedFiles - files.length, parts: Math.ceil(files.length / GLM_ARCHIVE_BATCH) };
  manifests.delete(key); manifests.set(key, { value, expires: Date.now() + 10 * 60_000 });
  while (manifests.size > 8) manifests.delete(manifests.keys().next().value!);
  return value;
}

export async function getArchivePart(manifest: GlmArchiveManifest, part: number, signal: AbortSignal) {
  if (!Number.isInteger(part) || part < 0 || part >= manifest.files.length) throw new Error("Invalid archive file.");
  const file = manifest.files[part];
  const bytes = await noaaBytes(new URL(`https://noaa-goes${file.satellite}.s3.amazonaws.com/${file.key}`), 4 * 1024 * 1024, signal);
  if (bytes.length !== file.size) throw new Error("NOAA file changed; reload its manifest.");
  return bytes;
}

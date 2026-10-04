/** Calendar selection and fixed NOAA GOES-East archive identities. */
export const GLM_ARCHIVE_FIRST_DAY = "2017-07-05";
export type GlmArchiveQuery = { day: string; hour: number; minute: number; duration: 15 | 30 | 60 };
export type GlmArchiveFile = { satellite: 16 | 19; key: string; start: number; end: number; size: number };
export type GlmArchiveManifest = {
  id: string; query: GlmArchiveQuery; start: string; end: string;
  files: GlmArchiveFile[]; expectedFiles: number; missingFiles: number; parts: number;
};
export const GLM_ARCHIVE_BATCH = 1;
export const GLM_ARCHIVE_FLASH_LIMIT = 50_000;

export function archiveInterval(query: GlmArchiveQuery, now = Date.now()) {
  const { day, hour, minute, duration } = query;
  const midnight = Date.parse(`${day}T00:00:00Z`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(day) || !Number.isFinite(midnight) || new Date(midnight).toISOString().slice(0, 10) !== day
    || day < GLM_ARCHIVE_FIRST_DAY || !Number.isInteger(hour) || hour < 0 || hour > 23
    || ![15, 30, 60].includes(duration) || !Number.isInteger(minute) || minute < 0 || minute + duration > 60 || minute % duration !== 0) throw new Error("Choose a valid archive date and completed interval.");
  const start = midnight + (hour * 60 + minute) * 60_000, end = start + duration * 60_000;
  if (end > now) throw new Error("This interval has not finished yet. Choose an earlier time.");
  return { start, end };
}

export function archiveLocation(ms: number) {
  const date = new Date(ms), year = date.getUTCFullYear();
  const ordinal = Math.floor((Date.UTC(year, date.getUTCMonth(), date.getUTCDate()) - Date.UTC(year, 0, 1)) / 86400000) + 1;
  const satellite = ms < Date.parse("2025-04-04T15:00:00Z") ? 16 : 19;
  return { satellite: satellite as 16 | 19, prefix: `GLM-L2-LCFA/${year}/${String(ordinal).padStart(3, "0")}/${String(date.getUTCHours()).padStart(2, "0")}/` };
}

export function archiveKeyTime(stamp: string) {
  if (!/^\d{14}$/.test(stamp)) throw new Error("Invalid NOAA file timestamp.");
  const year = +stamp.slice(0, 4), ordinal = +stamp.slice(4, 7), hour = +stamp.slice(7, 9), minute = +stamp.slice(9, 11), second = +stamp.slice(11, 13);
  const days = (Date.UTC(year + 1, 0, 1) - Date.UTC(year, 0, 1)) / 86400000;
  if (ordinal < 1 || ordinal > days || hour > 23 || minute > 59 || second > 59) throw new Error("Invalid NOAA file timestamp.");
  return Date.UTC(year, 0, ordinal, hour, minute, second, +stamp.slice(13) * 100);
}

export function parseArchiveListing(xml: string, location: ReturnType<typeof archiveLocation>): GlmArchiveFile[] {
  if (!/<ListBucketResult\b/.test(xml) || !/<IsTruncated>false<\/IsTruncated>/.test(xml) || /<!DOCTYPE|<!ENTITY/.test(xml)) throw new Error("NOAA archive listing is incomplete.");
  const files: GlmArchiveFile[] = [];
  for (const match of xml.matchAll(/<Contents>([\s\S]*?)<\/Contents>/g)) {
    if (files.length >= 200) throw new Error("NOAA archive listing exceeded its limit.");
    const key = match[1].match(/<Key>([^<]+)<\/Key>/)?.[1] ?? "";
    const size = Number(match[1].match(/<Size>(\d+)<\/Size>/)?.[1]);
    const name = key.slice(location.prefix.length).match(/^OR_GLM-L2-LCFA_G(16|19)_s(\d{14})_e(\d{14})_c\d{14}\.nc$/);
    if (!key.startsWith(location.prefix) || !name || +name[1] !== location.satellite || !Number.isSafeInteger(size) || size <= 0 || size > 4 * 1024 * 1024) throw new Error("Unexpected NOAA archive file.");
    const start = archiveKeyTime(name[2]), end = archiveKeyTime(name[3]);
    if (end <= start || end - start > 21_000) throw new Error("Unexpected NOAA observation interval.");
    files.push({ satellite: location.satellite, key, start, end, size });
  }
  return files;
}

export function selectArchiveFiles(files: GlmArchiveFile[], start: number, end: number) {
  // Include the following file: its completed flashes can begin before this interval ends.
  const byStart = new Map<number, GlmArchiveFile>();
  for (const file of files) if (file.start >= start && file.start <= end) {
    if (file.start % 20_000 !== 0 || byStart.has(file.start)) throw new Error("Ambiguous NOAA observation coverage.");
    byStart.set(file.start, file);
  }
  return [...byStart.values()].sort((a, b) => a.start - b.start);
}

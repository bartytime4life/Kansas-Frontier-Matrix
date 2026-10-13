import { GLM_ARCHIVE_FIRST_DAY, type GlmArchiveQuery } from "./lightning-archive";

export const LIGHTNING_HOUR = 3_600_000;
export const LIGHTNING_DAY = 24 * LIGHTNING_HOUR;
export type LightningYearRange = { start: number; end: number; hours: number; partial: boolean };

/** Only completed UTC hours within the archive's published date range. */
export function lightningYearRange(year: number, now = Date.now()): LightningYearRange {
  if (!Number.isInteger(year) || year < 2017 || year > new Date(now).getUTCFullYear()) throw new Error("Choose an available archive year.");
  const calendarStart = Date.UTC(year, 0, 1), calendarEnd = Date.UTC(year + 1, 0, 1);
  const start = Math.max(calendarStart, Date.parse(`${GLM_ARCHIVE_FIRST_DAY}T00:00:00Z`));
  const end = Math.min(calendarEnd, Math.floor(now / LIGHTNING_HOUR) * LIGHTNING_HOUR);
  if (end <= start) throw new Error("No completed archive hours in this year yet.");
  return { start, end, hours: (end - start) / LIGHTNING_HOUR, partial: start !== calendarStart || end !== calendarEnd };
}

export function lightningYearHour(ms: number, range: LightningYearRange) {
  if (!Number.isFinite(ms)) throw new Error("Invalid calendar position.");
  return Math.max(range.start, Math.min(range.end - LIGHTNING_HOUR, Math.floor(ms / LIGHTNING_HOUR) * LIGHTNING_HOUR));
}

export function lightningYearQuery(ms: number): GlmArchiveQuery {
  if (!Number.isFinite(ms) || ms % LIGHTNING_HOUR !== 0) throw new Error("Invalid archive hour.");
  const date = new Date(ms);
  return { day: date.toISOString().slice(0, 10), hour: date.getUTCHours(), minute: 0, duration: 60 };
}

export function nextLightningYearHour(ms: number, range: LightningYearRange, loop: boolean): number | null {
  if (ms !== lightningYearHour(ms, range)) throw new Error("Archive hour is outside the selected year.");
  return ms + LIGHTNING_HOUR < range.end ? ms + LIGHTNING_HOUR : loop ? range.start : null;
}

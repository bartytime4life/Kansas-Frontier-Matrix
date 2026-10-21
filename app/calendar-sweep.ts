export type CalendarStep = "years" | "months" | "days";
export type CalendarSweepView = Readonly<{
  day: string; start: string; end: string; step: CalendarStep;
  before: string | null; showing: "A" | "B";
}>;
export type CalendarFrameOutcome = Readonly<{
  state: "ready" | "partial" | "empty" | "error" | "reference";
  message: string;
}>;
export const CALENDAR_ARCHIVE_BOUNDS = Object.freeze({
  "usgs-earthquakes": "1800-01-01",
  "noaa-hms-smoke": "2005-08-05",
  "nasa-gibs-fire-points": "2018-01-01",
  "raspberry-shake-stations": "1800-01-01",
});
export type CalendarArchiveFeed = keyof typeof CALENDAR_ARCHIVE_BOUNDS;
const DAY = 86_400_000;
export const validCalendarDay = (value: unknown, today: string): value is string => {
  if (typeof value !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(value) || value < "1800-01-01" || value > today) return false;
  const ms = Date.parse(value + "T00:00:00.000Z");
  return Number.isFinite(ms) && new Date(ms).toISOString().slice(0, 10) === value;
};
export const calendarFrameDay = (view: CalendarSweepView) => view.showing === "A" && view.before ? view.before : view.day;
/** Calendar arithmetic uses UTC and clamps the day within the chosen month.
 * Every generated frame is an exact date, never a monthly/yearly average. */
export const calendarDateParts = (year: number, month: number, day: number): string => {
  const last = new Date(Date.UTC(year, month, 0)).getUTCDate();
  return String(year).padStart(4, "0") + "-" + String(month).padStart(2, "0") + "-" + String(Math.min(Math.max(1, day), last)).padStart(2, "0");
};
export const replaceCalendarPart = (date: string, part: "year" | "month" | "day", value: number, today: string): string => {
  const [year, month, day] = date.split("-").map(Number);
  if (!Number.isInteger(value)) return date;
  const y = part === "year" ? value : year, m = part === "month" ? value : month, d = part === "day" ? value : day;
  if (y < 1800 || y > Number(today.slice(0, 4)) || m < 1 || m > 12 || d < 1 || d > 31) return date;
  const next = calendarDateParts(y, m, d);
  return next > today ? today : next;
};
export const defaultCalendarSweep = (year: number, today: string): CalendarSweepView => {
  const safeYear = Number.isInteger(year) && year >= 1800 && year <= Number(today.slice(0, 4)) ? year : Number(today.slice(0, 4));
  const day = safeYear === Number(today.slice(0, 4)) ? today : String(safeYear) + "-01-01";
  return { day, start: String(Math.max(1800, safeYear - 5)) + "-01-01", end: safeYear === Number(today.slice(0, 4)) ? today : String(safeYear) + "-12-31", step: "years", before: null, showing: "B" };
};
export const calendarFrames = (start: string, end: string, step: CalendarStep): readonly string[] => {
  if (!validCalendarDay(start, end) || !validCalendarDay(end, end)) return [];
  const [year, month, day] = start.split("-").map(Number);
  const frames: string[] = [];
  // UTC dates in the supported 1800..9999 range have fewer than 3M days.
  const span = Math.floor((Date.parse(end + "T00:00:00Z") - Date.parse(start + "T00:00:00Z")) / DAY);
  const count = step === "days" ? span + 1 : step === "years" ? Number(end.slice(0, 4)) - year + 1 : (Number(end.slice(0, 4)) - year) * 12 + Number(end.slice(5, 7)) - month + 1;
  for (let i = 0; i < count; i++) {
    const next = step === "days" ? new Date(Date.parse(start + "T00:00:00Z") + i * DAY).toISOString().slice(0, 10)
      : step === "years" ? calendarDateParts(year + i, month, day)
      : calendarDateParts(year + Math.floor((month - 1 + i) / 12), (month - 1 + i) % 12 + 1, day);
    if (next <= end) frames.push(next);
  }
  if (frames.at(-1) !== end) frames.push(end);
  return frames;
};
export const calendarFrameIndex = (frames: readonly string[], day: string): number => {
  let lo = 0, hi = frames.length - 1;
  while (lo <= hi) { const mid = (lo + hi) >>> 1; if (frames[mid] <= day) lo = mid + 1; else hi = mid - 1; }
  return Math.max(0, hi);
};
export const calendarDayInRange = (view: CalendarSweepView, day: string): CalendarSweepView => ({
  ...view, day, start: day < view.start ? day : view.start, end: day > view.end ? day : view.end, showing: "B",
});
export const readCalendarSweep = (raw: string | null, today: string): CalendarSweepView | null => {
  if (!raw || raw.length > 512) return null;
  try {
    const view = JSON.parse(raw);
    if (!view || typeof view !== "object" || !validCalendarDay(view.day, today) || !validCalendarDay(view.start, today) || !validCalendarDay(view.end, today)
      || view.start > view.day || view.day > view.end || !["years", "months", "days"].includes(view.step)
      || view.before !== null && !validCalendarDay(view.before, today) || !["A", "B"].includes(view.showing) || view.showing === "A" && !view.before) return null;
    return { day: view.day, start: view.start, end: view.end, step: view.step, before: view.before, showing: view.showing };
  } catch { return null; }
};
export const calendarArchiveFeeds = (visibility: Readonly<Record<string, boolean>>, day: string): CalendarArchiveFeed[] =>
  (Object.keys(CALENDAR_ARCHIVE_BOUNDS) as CalendarArchiveFeed[]).filter(id => visibility[id] && day >= CALENDAR_ARCHIVE_BOUNDS[id]);
/** Only an exact checked archive day may override an operational-present gate.
 * A calendar request is not proof of coverage. Current-only carriers stay held. */
export const calendarVisibility = <T extends string>(
  base: Record<T, boolean>, selected: Readonly<Record<T, boolean>>, day: string | null, frame: number,
  today: string, checkedDays: Readonly<Partial<Record<T, string>>>, currentOnly: readonly T[], buildCurrent: boolean,
): Record<T, boolean> => {
  if (!day) return base;
  const next = { ...base };
  if (!validCalendarDay(day, today) || Number(day.slice(0, 4)) !== frame || !buildCurrent) {
    for (const id of currentOnly) next[id] = false;
    return next;
  }
  for (const id of currentOnly) if (day !== today) next[id] = false;
  for (const feed of Object.keys(CALENDAR_ARCHIVE_BOUNDS) as CalendarArchiveFeed[]) {
    const id = feed as T;
    next[id] = selected[id] === true && day >= CALENDAR_ARCHIVE_BOUNDS[feed] && checkedDays[id] === day;
  }
  return next;
};

export const PERIOD = Object.freeze({ from: '2020-01-01', to: '2025-12-31' });
export const YEARS = Object.freeze([2020, 2021, 2022, 2023, 2024, 2025]);
export const iso = day => day.toISOString().slice(0, 10);
export function calendar(from, to, step = 1) {
  const out = [];
  for (let day = new Date(`${from}T00:00:00Z`); iso(day) <= to; day.setUTCDate(day.getUTCDate() + step)) out.push(iso(day));
  return out;
}
export function samePeriod(period) { return period?.from === PERIOD.from && period?.to === PERIOD.to; }
export function sameSource(a, b) {
  return a && b && Object.keys(a).length === Object.keys(b).length && Object.keys(a).every(key => a[key] === b[key]);
}
export function validSource(source) {
  return source && YEARS.includes(source.year) && /^[a-f0-9]{64}$/.test(source.sha256) && Number.isInteger(source.bytes) && source.bytes > 0 &&
    /^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$/.test(source.capturedAt);
}
export function yearSource(sources, day) { return sources.find(source => source.year === Number(day.slice(0, 4))); }
export function csv(rows) {
  const cell = value => value === null || value === undefined ? '' : `"${String(value).replaceAll('"', '""')}"`;
  return rows.map(row => row.map(cell).join(',')).join('\r\n') + '\r\n';
}

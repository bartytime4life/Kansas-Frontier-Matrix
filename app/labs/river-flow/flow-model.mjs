const DAY_MS = 86_400_000;

export const FLOW_SITES = [
  { id: '06892350', name: 'Kansas River at De Soto', short: 'Kansas at De Soto', center: [-94.9646893, 38.9833375] },
  { id: '07144300', name: 'Arkansas River at Wichita', short: 'Arkansas at Wichita', center: [-97.3351944, 37.6433222] },
  { id: '06887000', name: 'Big Blue River near Manhattan', short: 'Big Blue near Manhattan', center: [-96.5713918, 39.2372186] },
];

const BASELINE = { id: 'baseline', label: '2020–2025 combined', from: '2020-01-01', to: '2025-12-31' };
const siteIds = new Set(FLOW_SITES.map(site => site.id));

export function flowSettings(query = {}) {
  const first = siteIds.has(query.first) ? query.first : FLOW_SITES[0].id;
  const second = siteIds.has(query.second) && query.second !== first
    ? query.second
    : FLOW_SITES.find(site => site.id !== first).id;
  const frequency = typeof query.frequency === 'string' ? Number(query.frequency) : NaN;
  const threshold = typeof query.threshold === 'string' && query.threshold.trim() ? Number(query.threshold) : NaN;
  return {
    first,
    second,
    period: typeof query.period === 'string' && /^20\d{2}$/.test(query.period) ? query.period : BASELINE.id,
    frequency: Number.isInteger(frequency) && frequency >= 1 && frequency <= 100 ? frequency : 50,
    threshold: Number.isFinite(threshold) && threshold >= 0 ? threshold : 1000,
    scale: query.scale === 'linear' ? 'linear' : 'compressed',
  };
}

export function flowPeriods(records) {
  let first = '', last = '';
  for (const row of records) {
    if (!siteIds.has(row.siteCode) || !/^20\d{2}-\d{2}-\d{2}$/.test(row.date)) continue;
    if (!first || row.date < first) first = row.date;
    if (row.date > last) last = row.date;
  }
  const periods = [BASELINE];
  if (!first) return periods;

  const firstYear = Number(first.slice(0, 4)), lastYear = Number(last.slice(0, 4));
  for (let year = lastYear; year >= firstYear; year--) {
    const start = `${year}-01-01`, end = `${year}-12-31`;
    const from = first > start ? first : start, to = last < end ? last : end;
    const label = from !== start || to !== end ? `${year} (partial year)` : String(year);
    periods.push({ id: String(year), label, from, to });
  }
  return periods;
}

function readFlow(row) {
  return Number.isFinite(row?.discharge) && row.discharge >= 0 ? row.discharge : null;
}

function durationCurve(values) {
  const sorted = values.sort((a, b) => b - a);
  const curve = [];
  sorted.forEach((value, index) => {
    if (value !== sorted[index + 1]) curve.push({ value, count: index + 1 });
  });
  return curve;
}

export function buildFlowComparison(records, period, first, second) {
  const lookup = new Map([[first, new Map()], [second, new Map()]]);
  for (const row of records) {
    if (row.date >= period.from && row.date <= period.to) lookup.get(row.siteCode)?.set(row.date, row);
  }

  const days = [], values = [[], []], missing = [0, 0];
  for (let time = Date.parse(period.from); time <= Date.parse(period.to); time += DAY_MS) {
    const date = new Date(time).toISOString().slice(0, 10);
    const rows = [lookup.get(first).get(date), lookup.get(second).get(date)];
    const readings = rows.map(row => ({ value: readFlow(row), qualifiers: row?.qualifiers || '' }));
    const included = readings.every(reading => reading.value !== null);
    readings.forEach(({ value }, index) => {
      if (value === null) missing[index]++;
      if (included) values[index].push(value);
    });
    days.push({ date, readings, included });
  }

  return { days, count: values[0].length, curves: values.map(durationCurve), missing };
}

export function flowAtFrequency(curve, total, frequency) {
  if (!total) return null;
  const rank = Math.ceil(frequency * total / 100);
  return curve.find(point => point.count >= rank);
}

export function daysAtFlow(curve, threshold) {
  let count = 0;
  for (const point of curve) {
    if (point.value < threshold) break;
    count = point.count;
  }
  return count;
}

export function gaugeHref(site) {
  return `https://waterdata.usgs.gov/monitoring-location/USGS-${site.id}/`;
}

export function watershedHref(site) {
  return `/?ctx=usgs-streamflow,usgs-wbd-watersheds&c=${site.center.join(',')}&z=9&base=civic&panel=layers&motion=off`;
}

export function flowCsvRows(days, first, second) {
  return [
    ['date', `${first}_daily_mean_cfs`, `${first}_USGS_qualifiers`, `${second}_daily_mean_cfs`, `${second}_USGS_qualifiers`, 'included_in_comparison'],
    ...days.map(day => [day.date, ...day.readings.flatMap(reading => [reading.value, reading.qualifiers]), day.included]),
  ];
}

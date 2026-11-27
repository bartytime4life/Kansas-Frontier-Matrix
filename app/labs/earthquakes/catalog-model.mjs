const FIRST_YEAR = 2010;
const YEARS_PER_PERIOD = 4;
const STARTS = [2010, 2014, 2018, 2022];

export const PERIODS = STARTS.map(start => ({
  id: String(start),
  start,
  end: start + YEARS_PER_PERIOD - 1,
  label: `${start}–${start + YEARS_PER_PERIOD - 1}`,
}));

export const MAGNITUDE_STEPS = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5];
export const CATALOG_BOUNDS = [-102.1, 36.8, -94.5, 40.1];

export function catalogSettings(query = {}) {
  const first = PERIODS.find(period => period.id === query.first) ?? PERIODS[1];
  const second = PERIODS.find(period => period.id === query.second && period !== first) ??
    PERIODS.findLast(period => period !== first);
  const magnitude = typeof query.mag === 'string' && query.mag.trim() ? Number(query.mag) : NaN;
  return {
    first: first.id,
    second: second.id,
    mag: Number.isFinite(magnitude) && magnitude >= 1 && magnitude <= 5 ? Math.round(magnitude * 10) / 10 : 2.5,
  };
}

export function catalogWindow(sourceUrl) {
  if (typeof sourceUrl !== 'string') return null;
  try {
    const params = new URL(sourceUrl).searchParams;
    const start = params.get('starttime');
    const end = params.get('endtime');
    return /^\d{4}-\d{2}-\d{2}$/.test(start) && /^\d{4}-\d{2}-\d{2}$/.test(end) ? { start, end } : null;
  } catch {
    return null;
  }
}

function isEvent(row) {
  return Number.isFinite(row.magnitude) && row.magnitude >= 1 && Number.isInteger(row.year) &&
    row.year >= FIRST_YEAR && Number.isFinite(row.longitude) && Number.isFinite(row.latitude);
}

export function compareCatalog(records, periods, threshold, window) {
  const events = records.filter(isEvent);
  return periods.map(period => {
    // USGS interprets a date-only bound as midnight UTC. Require the query
    // to span the whole period, regardless of the last recorded event date.
    const from = `${period.start}-01-01`;
    const to = `${period.end + 1}-01-01`;
    if (!window || window.start > from || window.end < to) return null;
    const within = events.filter(row => row.year >= period.start && row.year <= period.end);
    const selected = within.filter(row => row.magnitude >= threshold);
    const years = Array.from({ length: YEARS_PER_PERIOD }, (_, index) => ({
      year: period.start + index,
      count: selected.filter(row => row.year === period.start + index).length,
    }));
    const curve = MAGNITUDE_STEPS.map(mag => ({
      mag,
      perYear: within.filter(row => row.magnitude >= mag).length / YEARS_PER_PERIOD,
    }));
    const depths = selected.map(row => row.depth).filter(Number.isFinite).sort((a, b) => a - b);
    const mid = Math.floor(depths.length / 2);
    const medianDepth = !depths.length ? null : depths.length % 2 ? depths[mid] : (depths[mid - 1] + depths[mid]) / 2;
    return {
      period,
      years,
      curve,
      selected,
      perYear: selected.length / YEARS_PER_PERIOD,
      medianDepth,
      depthCount: depths.length,
    };
  });
}

export function catalogCsv(comparison) {
  const rows = comparison.flatMap(result => result.selected.map(row => [
    result.period.label, row.id, row.date, row.name, row.magnitude, row.magnitudeType,
    row.depth, row.latitude, row.longitude, row.status, row.url,
  ]));
  return [['period', 'event_id', 'time_utc', 'place', 'magnitude', 'magnitude_type', 'depth_km', 'latitude', 'longitude', 'review_status', 'usgs_url'], ...rows];
}

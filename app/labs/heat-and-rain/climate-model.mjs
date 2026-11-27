// NOAA station-day provider context. No interpolation, forecast or admission.
export const ELEMENTS = Object.freeze(['tmax', 'tmin', 'prcp']);
const DAY = 86400000;
const PERIOD = Object.freeze({ from: '2020-01-01', to: '2025-12-31' });
const SOURCE_FLAGS = new Set('01267AaBbCDdEFGHIKMf mNQRrSsTUuWXZz'.replaceAll(' ', ''));
const TEMPERATURE_FLAGS = new Set(['', 'H', 'L']);
const DAILY_PRECIPITATION_FLAGS = new Set(['', 'B', 'D', 'F', 'G']);
const PARTIAL_PRECIPITATION_FLAGS = new Set(['A', 'C', 'E']);
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const finite = value => typeof value === 'number' && Number.isFinite(value);

export function climateReading(tuple, element) {
  if (!ELEMENTS.includes(element)) throw new Error('Unknown climate element.');
  if (tuple === null) return { raw: null, value: null, state: 'missing', measurementFlag: '', qualityFlag: '', sourceFlag: '' };
  if (!Array.isArray(tuple) || tuple.length !== 4 || !Number.isInteger(tuple[0]) || tuple[0] < -9999 || tuple[0] > 99999 ||
      tuple.slice(1).some(flag => typeof flag !== 'string' || !/^[A-Za-z0-9]?$/.test(flag))) throw new Error('Invalid NOAA reading.');
  const [raw, measurementFlag, qualityFlag, sourceFlag] = tuple;
  const result = { raw, value: null, state: 'unqualified', measurementFlag, qualityFlag, sourceFlag };
  if (raw === -9999) result.state = 'missing';
  else if (qualityFlag) result.state = 'quality-withheld';
  else if (!SOURCE_FLAGS.has(sourceFlag)) result.state = 'unqualified';
  else if (measurementFlag === 'P') result.state = 'missing-presumed-zero';
  else if (element === 'prcp' && measurementFlag === 'H') result.state = 'precipitation-noted';
  else if (element === 'prcp' && measurementFlag === 'I') result.state = 'precipitation-not-reported';
  else if (element === 'prcp' && measurementFlag === 'T' && raw === 0) result.state = 'trace';
  // GHCN .dly flags A, C and E describe 6-, 18- and 12-hour totals.
  else if (element === 'prcp' && raw >= 0 && PARTIAL_PRECIPITATION_FLAGS.has(measurementFlag)) result.state = 'partial-period';
  else if ((element === 'prcp' ? DAILY_PRECIPITATION_FLAGS : TEMPERATURE_FLAGS).has(measurementFlag) && (element !== 'prcp' || raw >= 0)) {
    result.state = 'reported'; result.value = raw / 10;
  }
  return result;
}

export function validateSnapshot(snapshot, expected) {
  if (!snapshot || snapshot.schema !== 'kfm.daily-climate/v1' || !same(snapshot.period, PERIOD) ||
      !snapshot.station || !expected || ['id', 'name', 'latitude', 'longitude', 'elevationM'].some(key => snapshot.station[key] !== expected[key]) ||
      !/^US[CW]\d{8}$/.test(snapshot.station.id) || !finite(snapshot.station.latitude) || !finite(snapshot.station.longitude) ||
      snapshot.station.latitude < 36.9 || snapshot.station.latitude > 40.1 || snapshot.station.longitude < -102.1 || snapshot.station.longitude > -94.5 ||
      !same(snapshot.source, expected.source) || snapshot.source.url !== `https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/${snapshot.station.id}.dly` ||
      !/^[a-f0-9]{64}$/.test(snapshot.source.sha256) || !Number.isInteger(snapshot.source.bytes) || snapshot.source.bytes < 1 ||
      !Number.isFinite(Date.parse(snapshot.source.capturedAt)) || !Array.isArray(snapshot.records)) throw new Error('Snapshot does not match its station and source manifest.');
  const count = (Date.parse(PERIOD.to) - Date.parse(PERIOD.from)) / DAY + 1;
  if (snapshot.records.length !== count || expected.records !== count) throw new Error('Incomplete snapshot calendar.');
  snapshot.records.forEach((row, index) => {
    if (!row || row.date !== new Date(Date.parse(PERIOD.from) + index * DAY).toISOString().slice(0, 10) ||
        Object.keys(row).sort().join(',') !== 'date,prcp,tmax,tmin') throw new Error('Duplicate, missing or out-of-order station date.');
    for (const element of ELEMENTS) climateReading(row[element], element);
  });
  return snapshot;
}

function dayReadings(row) {
  const day = { date: row.date, ...Object.fromEntries(ELEMENTS.map(element => [element, climateReading(row[element], element)])) };
  if (day.tmax.value !== null && day.tmin.value !== null && day.tmin.value > day.tmax.value) {
    day.tmax = { ...day.tmax, value: null, state: 'inconsistent-temperatures' };
    day.tmin = { ...day.tmin, value: null, state: 'inconsistent-temperatures' };
  }
  return day;
}

function summary(days, heatC, wetMm) {
  const valid = Object.fromEntries(ELEMENTS.map(element => [element, days.filter(day => day[element].state === 'reported').length]));
  const temperatures = days.flatMap(day => [day.tmax.value, day.tmin.value]).filter(finite);
  return { expected: days.length, valid, excluded: Object.fromEntries(ELEMENTS.map(element => [element, days.length - valid[element]])),
    hotDays: days.filter(day => day.tmax.value !== null && day.tmax.value >= heatC).length,
    frostDays: days.filter(day => day.tmin.value !== null && day.tmin.value <= 0).length,
    wetDays: days.filter(day => day.prcp.value !== null && day.prcp.value >= wetMm).length,
    rainMm: valid.prcp ? days.reduce((sum, day) => sum + (day.prcp.state === 'reported' ? day.prcp.raw : 0), 0) / 10 : null,
    traceDays: days.filter(day => day.prcp.state === 'trace').length,
    partialPrecipitationDays: days.filter(day => day.prcp.state === 'partial-period').length,
    maxC: temperatures.length ? Math.max(...temperatures) : null,
    minC: temperatures.length ? Math.min(...temperatures) : null };
}

export function analyseClimate(snapshot, { year = 2025, month = 0, heatC = 32.2, wetMm = 1 } = {}) {
  if (!Number.isInteger(year) || year < 2020 || year > 2025 || !Number.isInteger(month) || month < 0 || month > 12 ||
      !finite(heatC) || heatC < -60 || heatC > 60 || !finite(wetMm) || wetMm < 0.1 || wetMm > 500) throw new Error('Choose a supported year, month and threshold.');
  const yearDays = snapshot.records.filter(row => row.date.startsWith(`${year}-`)).map(dayReadings);
  const expectedYear = (Date.UTC(year + 1, 0, 1) - Date.UTC(year, 0, 1)) / DAY;
  if (yearDays.length !== expectedYear || new Set(yearDays.map(day => day.date)).size !== expectedYear) throw new Error('The selected calendar is incomplete.');
  const days = month ? yearDays.filter(day => Number(day.date.slice(5, 7)) === month) : yearDays;
  const monthly = Array.from({ length: 12 }, (_, index) => ({ month: index + 1, ...summary(yearDays.filter(day => Number(day.date.slice(5, 7)) === index + 1), heatC, wetMm) }));
  return { station: snapshot.station, source: snapshot.source, period: snapshot.period, year, month, heatC, wetMm,
    days, monthly, ...summary(days, heatC, wetMm) };
}

export const CORN_HEAT_METHOD = Object.freeze({
  id: 'kfm.corn-growing-degree-days/v1',
  baseC: 10,
  capC: 30,
  documentation: 'https://mesonet.k-state.edu/agriculture/degreedays/',
});

export function validCornWindow(year, from, to) {
  if (!Number.isInteger(year) || year < 2020 || year > 2025) return false;
  const isDate = (value) => {
    if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value) || !value.startsWith(`${year}-`)) return false;
    const time = Date.parse(value);
    return Number.isFinite(time) && new Date(time).toISOString().slice(0, 10) === value;
  };
  return isDate(from) && isDate(to) && from <= to;
}

export function analyseCornHeat(snapshot, { year, from, to }) {
  if (!validCornWindow(year, from, to)) throw new Error('Choose a valid start and end date in the selected year.');
  const { baseC, capC } = CORN_HEAT_METHOD;
  const floor = baseC * 10, cap = capC * 10;
  const clamp = (reading) => Math.min(cap, Math.max(floor, reading.raw));
  const days = [];
  const months = new Map();
  let paired = 0, sum = 0;
  for (const row of snapshot.records) {
    if (row.date < from || row.date > to) continue;
    const { date, tmax, tmin } = dayReadings(row);
    // Keep integer half-tenths of a degree day until the final conversion.
    const amount = tmax.value !== null && tmin.value !== null ? clamp(tmax) + clamp(tmin) - 2 * floor : null;
    const month = date.slice(0, 7);
    const group = months.get(month) ?? { month, expected: 0, paired: 0, sum: 0 };
    group.expected++;
    if (amount !== null) {
      group.paired++;
      group.sum += amount;
      paired++;
      sum += amount;
    }
    months.set(month, group);
    days.push({ date, tmax, tmin, degreeDaysC: amount === null ? null : amount / 20 });
  }
  const firstDay = Date.parse(from);
  const expected = (Date.parse(to) - firstDay) / DAY + 1;
  if (days.length !== expected || days.some(({ date }, index) => Date.parse(date) !== firstDay + index * DAY)) {
    throw new Error('The corn heat calendar is incomplete.');
  }
  return { station: snapshot.station, source: snapshot.source, year, from, to, expected, paired, degreeDaysC: paired ? sum / 20 : null, days,
    monthly: Array.from(months.values(), ({ month, expected, paired, sum }) => ({ month, expected, paired, degreeDaysC: paired ? sum / 20 : null })) };
}

const STATES = Object.freeze({ missing: 'Missing', trace: 'Trace (unquantified)', 'quality-withheld': 'Withheld: NOAA quality flag',
  'missing-presumed-zero': 'Missing, presumed zero', 'precipitation-noted': 'Precipitation noted, amount unresolved',
  'precipitation-not-reported': 'Precipitation not reported', 'partial-period': 'Withheld: partial precipitation period', unqualified: 'Unqualified reading',
  'inconsistent-temperatures': 'Withheld: minimum exceeds maximum' });

export function readingLabel(reading, element, units = 'metric') {
  if (!ELEMENTS.includes(element) || !['metric', 'imperial'].includes(units)) throw new Error('Unknown element or units.');
  if (reading.state !== 'reported') return STATES[reading.state] ?? 'Unavailable';
  const temperature = element !== 'prcp';
  const value = units === 'imperial' ? (temperature ? reading.value * 9 / 5 + 32 : reading.value / 25.4) : reading.value;
  return `${value.toFixed(temperature || units === 'metric' ? 1 : 2)} ${temperature ? (units === 'metric' ? '°C' : '°F') : (units === 'metric' ? 'mm' : 'in')}`;
}

function csvCell(value) {
  const text = value === null || value === undefined ? '' : String(value);
  // Station/source text is provider controlled; do not create spreadsheet formulas.
  const safe = /^[=+@\t\r]/.test(text) || /^-(?!\d)/.test(text) ? `'${text}` : text;
  return /[",\r\n]/.test(safe) ? `"${safe.replaceAll('"', '""')}"` : safe;
}

export function climateCsv(analysis, units = 'metric') {
  if (!['metric', 'imperial'].includes(units)) throw new Error('Unknown units.');
  const names = ['station_id', 'station_name', 'date', 'year', 'month_filter', 'heat_threshold_C', 'wet_threshold_mm', 'display_units',
    ...ELEMENTS.flatMap(element => [`${element}_${element === 'prcp' ? (units === 'metric' ? 'mm' : 'in') : (units === 'metric' ? 'C' : 'F')}`, `${element}_state`, `${element}_raw_tenths`, `${element}_mflag`, `${element}_qflag`, `${element}_sflag`]),
    'source_url', 'source_sha256', 'captured_at', 'interpretation'];
  const rows = analysis.days.map(day => [analysis.station.id, analysis.station.name, day.date, analysis.year, analysis.month || 'all', analysis.heatC, analysis.wetMm, units,
    ...ELEMENTS.flatMap(element => { const reading = day[element]; const converted = reading.value === null ? null : units === 'metric' ? reading.value : element === 'prcp' ? reading.value / 25.4 : reading.value * 9 / 5 + 32;
      return [converted === null ? null : Number(converted.toFixed(8)), reading.state, reading.raw, reading.measurementFlag, reading.qualityFlag, reading.sourceFlag]; }),
    analysis.source.url, analysis.source.sha256, analysis.source.capturedAt, 'Station observation-day provider context; PRCP is liquid-equivalent precipitation; trace unquantified; partial periods withheld; no filled days']);
  return [names, ...rows].map(row => row.map(csvCell).join(',')).join('\r\n') + '\r\n';
}

export function cornHeatCsv(analysis, descriptor) {
  if (descriptor.id !== analysis.station.id || !same(descriptor.source, analysis.source)) throw new Error('The export must match the current station.');
  const { id, baseC, capC, documentation } = CORN_HEAT_METHOD;
  const columns = ['station_id', 'station_name', 'date', 'window_from', 'window_to',
    ...['tmax', 'tmin'].flatMap(element => ['C', 'state', 'raw_tenths', 'mflag', 'qflag', 'sflag'].map(field => `${element}_${field}`)),
    'corn_degree_days_C', 'corn_degree_days_F',
    'method_id', 'base_C', 'cap_C', 'method_url', 'source_url', 'source_sha256', 'captured_at', 'snapshot_url', 'snapshot_sha256'];
  const rows = analysis.days.map(({ date, tmax, tmin, degreeDaysC }) => [
    analysis.station.id, analysis.station.name, date, analysis.from, analysis.to,
    ...[tmax, tmin].flatMap(reading => [reading.value, reading.state, reading.raw, reading.measurementFlag, reading.qualityFlag, reading.sourceFlag]),
    degreeDaysC, degreeDaysC === null ? null : Number((degreeDaysC * 9 / 5).toFixed(3)),
    id, baseC, capC, documentation, analysis.source.url, analysis.source.sha256, analysis.source.capturedAt, descriptor.url, descriptor.sha256,
  ]);
  return [columns, ...rows].map(row => row.map(csvCell).join(',')).join('\r\n') + '\r\n';
}

export function climateReceipt(analysis, descriptor, units = 'metric') {
  if (!['metric', 'imperial'].includes(units) || descriptor.id !== analysis.station.id || !same(descriptor.source, analysis.source)) throw new Error('Receipt must match the current station.');
  return { schema: 'kfm.daily-climate-analysis/v1', scope: 'provider-context', station: analysis.station,
    selection: { year: analysis.year, month: analysis.month, heatC: analysis.heatC, wetMm: analysis.wetMm, displayUnits: units },
    support: { expectedDays: analysis.expected, quantifiedDays: analysis.valid, excludedDays: analysis.excluded, traceDays: analysis.traceDays, partialPrecipitationDays: analysis.partialPrecipitationDays },
    metrics: { hotDays: analysis.hotDays, frostDays: analysis.frostDays, wetDays: analysis.wetDays, quantifiedRainMm: analysis.rainMm },
    source: analysis.source, snapshot: { url: descriptor.url, sha256: descriptor.sha256, bytes: descriptor.bytes },
    method: 'TMAX >= heatC; TMIN <= 0 C; quantified PRCP >= wetMm. Each denominator is independent. Sum only qualified daily liquid-equivalent precipitation, which can include melted snow. GHCN .dly flags A, C and E are partial periods and excluded. Trace has no assigned amount. No missing values filled.',
    limitations: ['Station observation days, not hourly, field or county estimates.', 'The daily minimum does not establish the time of freezing temperatures or the occurrence of frost.', 'Trace precipitation is excluded from the quantified sum; missing and withheld readings remain excluded.',
      'A six-year sample is not a climate normal, trend attribution, drought index or forecast.', 'Captured source SHA256 establishes local byte identity, not a provider-issued checksum or KFM source admission.'],
    documentation: 'https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt' };
}

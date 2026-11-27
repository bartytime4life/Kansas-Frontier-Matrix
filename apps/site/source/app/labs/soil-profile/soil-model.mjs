import { PERIOD, YEARS, calendar, csv, samePeriod, sameSource, validSource, yearSource } from '../../science/science-model.mjs';

export const DEPTHS_CM = Object.freeze([5, 10, 20, 50, 100]);
const RANGES = { moisture: [0, 1], temperature: [-50, 60] };
const TOKENS = { moisture: /^-?\d{1,2}\.\d{3}$/, temperature: /^-?\d{1,4}\.\d$/ };
const SENTINELS = { moisture: '-99.000', temperature: '-9999.0' };
export function soilReading(raw, variable) {
  if (!Object.hasOwn(RANGES, variable)) throw new Error('Unknown soil variable.');
  if (raw === null) return { raw, value: null, state: 'absent' };
  if (typeof raw !== 'string' || !TOKENS[variable].test(raw)) throw new Error('Invalid soil source token.');
  if (raw === SENTINELS[variable]) return { raw, value: null, state: 'missing' };
  const value = Number(raw);
  const [low, high] = RANGES[variable];
  return value < low || value > high ? { raw, value: null, state: 'out-of-range' } : { raw, value, state: 'reported' };
}
export function soilReadingLabel(reading, variable) {
  if (reading.state !== 'reported') return reading.state === 'missing' ? 'Missing at source' : reading.state === 'absent' ? 'No source record' : 'Withheld: outside display range';
  return variable === 'moisture' ? `${reading.value.toFixed(3)} m³/m³` : `${reading.value.toFixed(1)} °C`;
}
export function validateSoilSnapshot(snapshot, descriptor) {
  const fail = () => { throw new Error('The soil profile snapshot has an invalid schema or coverage.'); };
  if (!snapshot || snapshot.schema !== 'kfm.soil-profile/v1' || !samePeriod(snapshot.period) ||
      !['53974', '03067'].includes(snapshot.station?.id) || !descriptor ||
      !['id', 'name', 'latitude', 'longitude', 'utcOffsetHours'].every(key => snapshot.station[key] === descriptor[key]) ||
      !Number.isFinite(snapshot.station.latitude) || snapshot.station.latitude < 36.9 || snapshot.station.latitude > 40.1 ||
      !Number.isFinite(snapshot.station.longitude) || snapshot.station.longitude < -102.2 || snapshot.station.longitude > -94.4 ||
      snapshot.station.utcOffsetHours !== -6 || JSON.stringify(snapshot.depthsCm) !== JSON.stringify(DEPTHS_CM)) fail();
  const name = snapshot.station.id === '53974' ? 'KS_Manhattan_6_SSW' : 'KS_Oakley_19_SSW';
  if (!Array.isArray(snapshot.sources) || snapshot.sources.length !== 6 || !Array.isArray(descriptor.sources) ||
      !snapshot.sources.every((source, index) => validSource(source) && source.year === YEARS[index] && sameSource(source, descriptor.sources[index]) &&
        source.url === `https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/${source.year}/CRND0103-${source.year}-${name}.txt`)) fail();
  const expected = calendar(PERIOD.from, PERIOD.to);
  if (!Array.isArray(snapshot.records) || snapshot.records.length !== expected.length || descriptor.records !== expected.length) fail();
  for (let index = 0; index < expected.length; index++) {
    const record = snapshot.records[index];
    if (!record || record.date !== expected[index] || typeof record.version !== 'string' || !/^(?:\d{1,2}\.\d{1,3}|-9\.000)$/.test(record.version)) fail();
    for (const variable of ['moisture', 'temperature']) {
      if (!Array.isArray(record[variable]) || record[variable].length !== 5) fail();
      for (const token of record[variable]) if (typeof token !== 'string' || !TOKENS[variable].test(token)) fail();
    }
  }
  return snapshot;
}

function median(values) {
  const sorted = values.toSorted((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length ? sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2 : null;
}
export function analyseSoil(snapshot, { year = 2025, month = 0, depth = 20, variable = 'moisture' } = {}) {
  if (!YEARS.includes(year) || !Number.isInteger(month) || month < 0 || month > 12 || !DEPTHS_CM.includes(depth) || !Object.hasOwn(RANGES, variable)) {
    throw new Error('Choose a valid soil year, month, depth and variable.');
  }
  const first = month ? `${year}-${String(month).padStart(2, '0')}-01` : `${year}-01-01`;
  const last = month ? new Date(Date.UTC(year, month, 0)).toISOString().slice(0, 10) : `${year}-12-31`;
  const records = new Map(snapshot.records.map(record => [record.date, record]));
  const days = calendar(first, last).map(day => {
    const record = records.get(day);
    return { date: day, version: record?.version ?? null,
      moisture: DEPTHS_CM.map((_, index) => soilReading(record?.moisture[index] ?? null, 'moisture')),
      temperature: DEPTHS_CM.map((_, index) => soilReading(record?.temperature[index] ?? null, 'temperature')) };
  });
  const depths = DEPTHS_CM.map((depthCm, index) => {
    const values = days.map(day => day[variable][index].value).filter(value => value !== null);
    const temperatures = days.map(day => day.temperature[index].value).filter(value => value !== null);
    return { depthCm, valid: values.length, missing: days.length - values.length,
      min: values.length ? Math.min(...values) : null, median: median(values), max: values.length ? Math.max(...values) : null,
      temperatureValid: temperatures.length, meanColdDays: temperatures.filter(value => value <= 0).length };
  });
  const selected = depths.find(item => item.depthCm === depth);
  return { station: snapshot.station, period: { from: first, to: last }, settings: { year, month, depth, variable }, expected: days.length,
    valid: selected.valid, missing: selected.missing, min: selected.min, median: selected.median, max: selected.max,
    meanColdDays: selected.meanColdDays, temperatureValid: selected.temperatureValid, depths, days, sources: snapshot.sources };
}
export function soilCsv(analysis, citation) {
  const s = analysis.settings;
  const rows = [['station_wban', 'station_name', 'latitude', 'longitude', 'local_standard_date', 'utc_offset_hours', 'depth_cm', 'moisture_source_token',
    'moisture_m3_m3', 'moisture_state', 'temperature_source_token', 'temperature_c', 'temperature_state', 'datalogger_version',
    'selected_year', 'selected_month_0_is_all', 'selected_variable', 'selected_depth_cm', 'source_url', 'source_sha256',
    'source_captured_at', 'source_bytes', 'source_citation']];
  for (const day of analysis.days) for (const [index, depth] of DEPTHS_CM.entries()) {
    const source = yearSource(analysis.sources, day.date);
    const m = day.moisture[index];
    const t = day.temperature[index];
    rows.push([analysis.station.id, analysis.station.name, analysis.station.latitude, analysis.station.longitude, day.date, analysis.station.utcOffsetHours, depth,
      m.raw, m.value, m.state, t.raw, t.value, t.state, day.version, s.year, s.month, s.variable, s.depth, source.url, source.sha256,
      source.capturedAt, source.bytes, citation]);
  }
  return csv(rows);
}
export function soilReceipt(analysis, descriptor, citation) {
  if (descriptor?.id !== analysis.station.id || !Array.isArray(descriptor.sources) ||
      !analysis.sources.every((source, index) => sameSource(source, descriptor.sources[index]))) throw new Error('Soil receipt station identity mismatch.');
  return { schema: 'kfm.soil-profile-analysis/v1', scope: 'provider-context', station: analysis.station, settings: analysis.settings, period: analysis.period,
    expectedDays: analysis.expected, depths: analysis.depths,
    displaySnapshot: { url: descriptor.url, sha256: descriptor.sha256, bytes: descriptor.bytes }, sources: analysis.sources, citation,
    method: 'Separate daily-mean point measurements at 5,10,20,50,100 cm, local standard time UTC−6. Moisture m³/m³, temperature °C. No interpolation or depth average. Sentinels and out-of-range values withheld; missing never means zero. Median uses observed days only. Daily-mean temperature ≤0°C counts do not identify all freezing events.',
    displayRanges: { moisture: [0, 1], temperature: [-50, 60] }, reviewState: 'PENDING', sourceAdmission: 'PENDING', releaseState: 'UNRELEASED' };
}

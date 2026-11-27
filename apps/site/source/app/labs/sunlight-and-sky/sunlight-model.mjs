// Satellite-derived/modelled horizontal solar energy. No interpolation or yield model.
export const SUNLIGHT_PERIOD = Object.freeze({ from: '2020-01-01', to: '2025-12-31' });
export const SUNLIGHT_POINTS = Object.freeze([
  Object.freeze({ id: 'dodge-city', name: 'Dodge City area', latitude: 37.7608, longitude: -99.9689 }),
  Object.freeze({ id: 'wichita', name: 'Wichita area', latitude: 37.6544, longitude: -97.4431 }),
  Object.freeze({ id: 'topeka', name: 'Topeka area', latitude: 39.0725, longitude: -95.6261 }),
]);
export const SUNLIGHT_PARAMETERS = Object.freeze({
  ALLSKY_SFC_SW_DWN: Object.freeze({ units: 'kW-hr/m^2/day', longname: 'All Sky Surface Shortwave Downward Irradiance' }),
  CLRSKY_SFC_SW_DWN: Object.freeze({ units: 'kW-hr/m^2/day', longname: 'Clear Sky Surface Shortwave Downward Irradiance' }),
});
const DAY = 86400000;
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const finite = value => typeof value === 'number' && Number.isFinite(value);
const validated = new WeakMap();
const analyses = new WeakSet();
const dates = Object.freeze(Array.from({ length: 2192 }, (_, index) => new Date(Date.parse(SUNLIGHT_PERIOD.from) + index * DAY).toISOString().slice(0, 10)));
function freeze(value) {
  if (value && typeof value === 'object' && !Object.isFrozen(value)) {
    for (const item of Object.values(value)) freeze(item);
    Object.freeze(value);
  }
  return value;
}

export function sunlightSourceUrl(point) {
  return `https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN,CLRSKY_SFC_SW_DWN&community=RE&longitude=${point.longitude}&latitude=${point.latitude}&start=20200101&end=20251231&format=JSON&time-standard=LST`;
}

export function sunlightReading(raw) {
  if (!finite(raw) || (raw !== -999 && (raw < 0 || raw > 30))) throw new Error('Invalid NASA solar energy value.');
  return { raw, value: raw === -999 ? null : raw, state: raw === -999 ? 'missing' : 'modeled' };
}

export function validateSunlightSnapshot(snapshot, descriptor) {
  const point = SUNLIGHT_POINTS.find(value => value.id === descriptor?.id);
  const source = descriptor?.source;
  const provider = descriptor?.provider;
  const coordinates = provider?.returnedCoordinates;
  if (!point || Object.keys(point).some(key => descriptor[key] !== point[key]) ||
      !/^[a-f0-9]{64}$/.test(descriptor.sha256 ?? '') || !Number.isInteger(descriptor.bytes) || descriptor.bytes < 1 || descriptor.bytes > 1024 * 1024 ||
      descriptor.url !== `/science-data/sunlight/${point.id}-${descriptor.sha256.slice(0, 16)}.json` || descriptor.records !== dates.length ||
      !source || source.url !== sunlightSourceUrl(point) || !/^[a-f0-9]{64}$/.test(source.sha256 ?? '') ||
      !Number.isInteger(source.bytes) || source.bytes < 1 || source.bytes > 1024 * 1024 ||
      typeof source.capturedAt !== 'string' || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$/.test(source.capturedAt) || !Number.isFinite(Date.parse(source.capturedAt)) ||
      (source.lastModified !== null && (typeof source.lastModified !== 'string' || source.lastModified.length > 128)) ||
      provider?.api?.name !== 'POWER Daily API' || !/^v2\.\d{1,3}\.\d{1,3}$/.test(provider?.api?.version ?? '') ||
      !same(provider.sources, ['SYN1DEG']) || provider.fillValue !== -999 || provider.timeStandard !== 'LST' ||
      !Array.isArray(coordinates) || coordinates.length !== 3 || coordinates.some(value => !finite(value)) ||
      Math.abs(coordinates[0] - point.longitude) > 0.001 || Math.abs(coordinates[1] - point.latitude) > 0.001 || coordinates[2] < -500 || coordinates[2] > 9000) {
    throw new Error('Invalid sunlight source manifest.');
  }
  if (!snapshot || snapshot.schema !== 'kfm.sunlight/v1' || snapshot.scope !== 'provider-context' ||
      !same(snapshot.point, point) || !same(snapshot.period, SUNLIGHT_PERIOD) || !same(snapshot.source, source) ||
      !same(snapshot.provider, provider) || !same(snapshot.parameters, SUNLIGHT_PARAMETERS) ||
      !Array.isArray(snapshot.records) || snapshot.records.length !== dates.length) throw new Error('Sunlight snapshot does not match its point, product and source.');
  snapshot.records.forEach((row, index) => {
    if (!row || row.date !== dates[index] || Object.keys(row).sort().join(',') !== 'allSky,clearSky,date') throw new Error('Invalid sunlight calendar.');
    sunlightReading(row.allSky);
    sunlightReading(row.clearSky);
  });
  // Keep receipt identity tied to the validated asset and prevent later edits
  // from changing statistics behind that identity.
  validated.set(snapshot, freeze(structuredClone(descriptor)));
  return freeze(snapshot);
}

function seriesSummary(days, side) {
  const values = days.filter(day => day[side].allSky.value !== null);
  const sum = values.length ? values.reduce((total, day) => total + day[side].allSky.value, 0) : null;
  const peak = values.reduce((current, day) => current === null || day[side].allSky.value > current.value ? { date: day.date, value: day[side].allSky.value } : current, null);
  return { validDays: values.length, missingDays: days.length - values.length, sum,
    mean: values.length ? sum / values.length : null, peak };
}

function summarize(days) {
  const pairs = days.filter(day => day.primary.allSky.value !== null && day.comparison.allSky.value !== null);
  const clear = days.filter(day => day.primary.allSky.value !== null && day.primary.clearSky.value !== null);
  const mean = (values, read) => values.length ? values.reduce((sum, day) => sum + read(day), 0) / values.length : null;
  return { expected: days.length, primary: seriesSummary(days, 'primary'), comparison: seriesSummary(days, 'comparison'),
    paired: { days: pairs.length, primaryMean: mean(pairs, day => day.primary.allSky.value), comparisonMean: mean(pairs, day => day.comparison.allSky.value),
      meanDifference: mean(pairs, day => day.primary.allSky.value - day.comparison.allSky.value) },
    clearSky: { days: clear.length, allSkyMean: mean(clear, day => day.primary.allSky.value), clearSkyMean: mean(clear, day => day.primary.clearSky.value),
      meanDifference: mean(clear, day => day.primary.allSky.value - day.primary.clearSky.value) } };
}

export function analyseSunlight(primary, comparison, { year = 2025, month = 0 } = {}) {
  const primaryDescriptor = validated.get(primary);
  const comparisonDescriptor = validated.get(comparison);
  if (!primaryDescriptor || !comparisonDescriptor) throw new Error('Validate both sunlight snapshots before analysis.');
  if (!Number.isInteger(year) || year < 2020 || year > 2025 || !Number.isInteger(month) || month < 0 || month > 12) throw new Error('Choose a captured year and month.');
  const yearDays = primary.records.flatMap((row, index) => row.date.startsWith(`${year}-`) ? [{ date: row.date, sourceKey: row.date.replaceAll('-', ''),
    primary: { allSky: sunlightReading(row.allSky), clearSky: sunlightReading(row.clearSky) },
    comparison: { allSky: sunlightReading(comparison.records[index].allSky), clearSky: sunlightReading(comparison.records[index].clearSky) } }] : []);
  const days = month ? yearDays.filter(day => Number(day.date.slice(5, 7)) === month) : yearDays;
  const analysis = freeze({ point: primary.point, comparisonPoint: comparison.point, period: SUNLIGHT_PERIOD, timeStandard: 'LST', year, month,
    expected: days.length, days, summary: summarize(days),
    monthly: Array.from({ length: 12 }, (_, index) => ({ month: index + 1, ...summarize(yearDays.filter(day => Number(day.date.slice(5, 7)) === index + 1)) })),
    sources: { primary: primary.source, comparison: comparison.source }, descriptors: { primary: primaryDescriptor, comparison: comparisonDescriptor } });
  analyses.add(analysis);
  return analysis;
}

function requireAnalysis(analysis) {
  if (!analyses.has(analysis)) throw new Error('Export requires the current source-bound sunlight analysis.');
}
function csvCell(value) {
  const text = value === null || value === undefined ? '' : String(value);
  const safe = /^[=+@\t\r]/.test(text) || /^-(?!\d)/.test(text) ? `'${text}` : text;
  return /[",\r\n]/.test(safe) ? `"${safe.replaceAll('"', '""')}"` : safe;
}

export function sunlightCsv(analysis) {
  requireAnalysis(analysis);
  const sides = ['primary', 'comparison'];
  const fields = ['allSky', 'clearSky'];
  const headers = ['date', 'source_json_date_key', 'selected_year', 'selected_month', 'time_standard', 'units',
    ...sides.flatMap(side => [`${side}_point_id`, `${side}_query_latitude`, `${side}_query_longitude`,
      ...fields.flatMap(field => [`${side}_${field}_kWh_m2_day`, `${side}_${field}_state`, `${side}_${field}_raw`]),
      `${side}_source_url`, `${side}_source_sha256`, `${side}_captured_at`, `${side}_snapshot_sha256`, `${side}_api_version`, `${side}_product`]), 'interpretation'];
  const rows = analysis.days.map(day => [day.date, day.sourceKey, analysis.year, analysis.month || 'all', 'NASA Local Solar Time', 'kWh/m2/day',
    ...sides.flatMap(side => { const descriptor = analysis.descriptors[side]; return [descriptor.id, descriptor.latitude, descriptor.longitude,
      ...fields.flatMap(field => [day[side][field].value, day[side][field].state, day[side][field].raw]),
      descriptor.source.url, descriptor.source.sha256, descriptor.source.capturedAt, descriptor.sha256, descriptor.provider.api.version, descriptor.provider.sources.join(';')]; }),
    'Satellite-derived/modelled incoming horizontal shortwave energy; nominal 1-degree grid; no missing-day filling; not panel output']);
  return [headers, ...rows].map(row => row.map(csvCell).join(',')).join('\r\n') + '\r\n';
}

export function sunlightReceipt(analysis) {
  requireAnalysis(analysis);
  return { schema: 'kfm.sunlight-analysis/v1', scope: 'provider-context', review: 'PENDING', admission: 'PENDING', release: 'UNRELEASED',
    selection: { primary: analysis.point, comparison: analysis.comparisonPoint, year: analysis.year, month: analysis.month,
      from: analysis.days[0].date, to: analysis.days.at(-1).date, timeStandard: 'NASA Local Solar Time' },
    units: { daily: 'kWh/m2/day', sum: 'kWh/m2' }, grid: { latitudeDegrees: 1, longitudeDegrees: 1 },
    metrics: structuredClone(analysis.summary), monthly: structuredClone(analysis.monthly),
    sources: structuredClone(analysis.descriptors), parameters: SUNLIGHT_PARAMETERS,
    method: 'Per-area all-sky means and sums use valid modeled days. Primary minus comparison means use only dates with both all-sky values. Primary all-sky minus clear-sky uses only paired primary values. Missing sentinel -999 is excluded without filling; zero is valid; values above clear-sky are retained.',
    limitations: ['Satellite-derived radiative-transfer model estimates; not ground-station measurements or field/county estimates.',
      'Nominal primary CERES SYN1deg radiation grid is 1 degree by 1 degree. Returned point-query metadata is not a verified cell center or boundary.',
      'Incoming horizontal shortwave energy is not panel yield, electricity, sunlight hours or a forecast.',
      'Clear-sky difference does not establish cloud-only causation; no values are clipped to the reference.',
      'NASA Local Solar Time uses 15-degree longitude swaths, not civil CST/CDT.',
      'Six years do not establish a climate normal or trend. Sources may be revised.',
      'Captured source SHA256 establishes local byte identity, not a provider checksum, scientific validation or KFM admission.'],
    documentation: 'https://power.larc.nasa.gov/docs/services/api/temporal/daily/',
    methodology: 'https://power.larc.nasa.gov/docs/methodology/data/sources_fluxes/',
    acknowledgment: 'Source: NASA Langley Research Center POWER project, funded by NASA Earth Science Division; POWER Daily API version and access date are recorded for each source.' };
}

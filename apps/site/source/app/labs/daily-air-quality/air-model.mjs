import { YEARS, PERIOD, calendar, csv, samePeriod, sameSource, yearSource } from '../../science/science-model.mjs';

export { YEARS };
export const CATEGORIES = Object.freeze(['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous']);
export const POLLUTANTS = Object.freeze(['CO', 'NO2', 'Ozone', 'PM10', 'PM2.5', 'SO2']);
const BASE = 'https://aqs.epa.gov/aqsweb/airdata/';
const MAX_SOURCE = 8 * 1024 * 1024;
const expectedDates = calendar(PERIOD.from, PERIOD.to);
const verifiedSnapshots = new WeakMap();
const analysisDisplays = new WeakMap();
const plain = value => value !== null && typeof value === 'object' && !Array.isArray(value);
const realDate = value => typeof value === 'string' && /^\d{4}-\d\d-\d\d$/.test(value) && Number.isFinite(Date.parse(`${value}T00:00:00Z`)) && new Date(`${value}T00:00:00Z`).toISOString().slice(0, 10) === value;
const validId = value => typeof value === 'string' && /^20\d{3}$/.test(value) && Number(value.slice(2)) >= 1 && Number(value.slice(2)) <= 209 && Number(value.slice(2)) % 2 === 1;

export function categoryForAqi(value) {
  if (!Number.isInteger(value) || value < 0 || value > 10000) throw new Error('Choose a nonnegative reported AQI integer.');
  const index = [50, 100, 150, 200, 300].findIndex(boundary => value <= boundary);
  return CATEGORIES[index === -1 ? 5 : index];
}

function validSource(source, index) {
  if (!plain(source) || source.year !== YEARS[index] || source.url !== `${BASE}daily_aqi_by_county_${YEARS[index]}.zip` ||
      typeof source.sha256 !== 'string' || !/^[a-f0-9]{64}$/.test(source.sha256) || !Number.isInteger(source.bytes) || source.bytes < 1 || source.bytes > MAX_SOURCE ||
      !Number.isInteger(source.providerRows) || source.providerRows < 1 || source.providerRows > 1500000 || !realDate(source.providerCreated) ||
      !['utf-8-sig', 'latin-1'].includes(source.encoding) || typeof source.capturedAt !== 'string' ||
      !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$/.test(source.capturedAt) || !Number.isFinite(Date.parse(source.capturedAt)) ||
      new Date(source.capturedAt).toISOString().replace('.000Z', 'Z') !== source.capturedAt ||
      (source.lastModified !== null && (typeof source.lastModified !== 'string' || source.lastModified.length > 100))) return false;
  return Object.keys(source).length === 9;
}

function validDisplay(descriptor) {
  return plain(descriptor) && descriptor.id === 'kansas' && typeof descriptor.sha256 === 'string' && /^[a-f0-9]{64}$/.test(descriptor.sha256) &&
    descriptor.url === `/science-data/daily-air-quality/kansas-${descriptor.sha256.slice(0, 16)}.json` && Number.isInteger(descriptor.bytes) && descriptor.bytes > 0 && descriptor.bytes <= 6 * 1024 * 1024 &&
    descriptor.calendarDates === expectedDates.length && Number.isInteger(descriptor.records) && descriptor.records > 0;
}

export function validateAirSnapshot(snapshot, manifest) {
  const fail = () => { throw new Error('The daily air quality snapshot has an invalid schema or coverage.'); };
  if (!plain(snapshot) || !plain(manifest) || snapshot.schema !== 'kfm.daily-air-quality/v1' || manifest.schema !== 'kfm.daily-air-quality-manifest/v1' ||
      snapshot.provider !== 'U.S. EPA AirData AQS' || manifest.provider !== snapshot.provider || snapshot.scope !== 'provider-context' || manifest.scope !== snapshot.scope ||
      manifest.review !== 'PENDING' || manifest.admission !== 'PENDING' || manifest.release !== 'UNRELEASED' ||
      !samePeriod(snapshot.period) || !samePeriod(manifest.period) || !validDisplay(manifest.snapshot)) fail();
  if (!Array.isArray(snapshot.dates) || snapshot.dates.length !== expectedDates.length || !snapshot.dates.every((day, i) => day === expectedDates[i]) ||
      !Array.isArray(snapshot.sources) || snapshot.sources.length !== 6 || !Array.isArray(manifest.sources) || manifest.sources.length !== 6 ||
      !snapshot.sources.every((source, index) => validSource(source, index) && plain(manifest.sources[index]) && sameSource(source, manifest.sources[index]))) fail();
  if (!Array.isArray(snapshot.counties) || snapshot.counties.length < 1 || snapshot.counties.length > 105 || !Array.isArray(manifest.counties) || manifest.counties.length !== snapshot.counties.length ||
      !plain(manifest.coverageByYear) || Object.keys(manifest.coverageByYear).length !== 6) fail();
  const rowsSeen = YEARS.map(() => new Set());
  const coverage = Object.fromEntries(YEARS.map(year => [year, { reportedCountyDays: 0, counties: new Set() }]));
  let previous = '', total = 0;
  for (let countyIndex = 0; countyIndex < snapshot.counties.length; countyIndex++) {
    const county = snapshot.counties[countyIndex];
    const descriptor = manifest.counties[countyIndex];
    if (!plain(county) || !plain(descriptor) || !validId(county.id) || county.id <= previous || descriptor.id !== county.id || descriptor.name !== county.name ||
        typeof county.name !== 'string' || !/^[A-Za-z][A-Za-z .'-]{0,50} County$/.test(county.name) || !Array.isArray(county.values) || county.values.length !== expectedDates.length ||
        !Number.isInteger(descriptor.reportedDays) || descriptor.reportedDays < 1 || descriptor.reportedDays > expectedDates.length) fail();
    previous = county.id;
    let reported = 0;
    for (let index = 0; index < county.values.length; index++) {
      const row = county.values[index];
      if (row === null) continue;
      const sourceIndex = Number(expectedDates[index].slice(0, 4)) - YEARS[0];
      const source = snapshot.sources[sourceIndex];
      if (!Array.isArray(row) || row.length !== 6 || typeof row[0] !== 'string' || !/^\d{1,5}$/.test(row[0]) || Number(row[0]) > 10000 || row[1] !== categoryForAqi(Number(row[0])) ||
          !POLLUTANTS.includes(row[2]) || typeof row[3] !== 'string' || row[3].length < 1 || row[3].length > 256 || /[\x00-\x1f\x7f]/.test(row[3]) ||
          !/^\d{2}-\d{3}-\d{4}(?:[,;| /]+\d{2}-\d{3}-\d{4})*$/.test(row[3]) || row[3].match(/\d{2}-\d{3}-\d{4}/g).some(site => site.slice(0, 2) + site.slice(3, 6) !== county.id) ||
          typeof row[4] !== 'string' || !/^\d{1,4}$/.test(row[4]) || Number(row[4]) < 1 || Number(row[4]) > 1000 ||
          !Number.isInteger(row[5]) || row[5] < 2 || row[5] > source.providerRows + 1 || rowsSeen[sourceIndex].has(row[5])) fail();
      rowsSeen[sourceIndex].add(row[5]);
      reported++;
      coverage[source.year].reportedCountyDays++;
      coverage[source.year].counties.add(county.id);
    }
    if (reported !== descriptor.reportedDays) fail();
    total += reported;
  }
  if (total !== manifest.snapshot.records || !YEARS.every(year => {
    const value = manifest.coverageByYear[year];
    return plain(value) && value.reportedCountyDays === coverage[year].reportedCountyDays && value.reportingCounties === coverage[year].counties.size;
  })) fail();
  verifiedSnapshots.set(snapshot, { ...manifest.snapshot });
  return snapshot;
}

const median = values => {
  if (!values.length) return null;
  const sorted = [...values].sort((a, b) => a - b), middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[middle] : (sorted[middle - 1] + sorted[middle]) / 2;
};
function summary(days) {
  const observed = days.filter(day => !day.missing);
  const thresholdDays = observed.filter(day => day.meets).length;
  return { expected: days.length, reported: observed.length, missing: days.length - observed.length, thresholdDays,
    thresholdPct: observed.length ? 100 * thresholdDays / observed.length : null, medianAqi: median(observed.map(day => day.aqi)),
    maxAqi: observed.length ? Math.max(...observed.map(day => day.aqi)) : null };
}
function longestRun(days) {
  let start = null;
  let best = { count: 0, from: null, to: null, leftBoundary: null, rightBoundary: null };
  for (let index = 0; index <= days.length; index++) {
    if (index < days.length && days[index].meets === true) { if (start === null) start = index; continue; }
    if (start !== null) {
      const count = index - start;
      if (count > best.count) best = { count, from: days[start].date, to: days[index - 1].date,
        leftBoundary: start === 0 ? 'window' : days[start - 1].missing ? 'missing' : null,
        rightBoundary: index === days.length ? 'window' : days[index].missing ? 'missing' : null };
      start = null;
    }
  }
  return best;
}

export function analyseAir(snapshot, { countyId = '20173', year = 2023, month = 0, threshold = 101 } = {}) {
  const display = plain(snapshot) ? verifiedSnapshots.get(snapshot) : null;
  if (!display) throw new Error('Load and verify the daily air quality snapshot first.');
  if (!validId(countyId) || !YEARS.includes(year) || !Number.isInteger(month) || month < 0 || month > 12 || !Number.isInteger(threshold) || threshold < 0 || threshold > 500) {
    throw new Error('Choose a reporting county, year, month and integer AQI threshold (0–500).');
  }
  const county = snapshot.counties.find(value => value.id === countyId);
  if (!county) throw new Error('Choose a reporting Kansas county from the snapshot.');
  const settings = { countyId, year, month, threshold };
  const source = yearSource(snapshot.sources, `${year}-01-01`);
  const days = snapshot.dates.flatMap((day, index) => {
    if (Number(day.slice(0, 4)) !== year || (month && Number(day.slice(5, 7)) !== month)) return [];
    const row = county.values[index];
    return [{ date: day, missing: row === null, aqi: row ? Number(row[0]) : null, rawAqi: row?.[0] ?? null,
      category: row?.[1] ?? null, parameter: row?.[2] ?? null, site: row?.[3] ?? null,
      sites: row ? Number(row[4]) : null, rawSites: row?.[4] ?? null, sourceRow: row?.[5] ?? null,
      meets: row ? Number(row[0]) >= threshold : null, source }];
  });
  const observed = days.filter(day => !day.missing);
  const totals = summary(days);
  const peak = observed.find(day => day.aqi === totals.maxAqi) ?? null;
  const months = [...new Set(days.map(day => Number(day.date.slice(5, 7))))].map(monthNumber => ({ month: monthNumber,
    label: new Intl.DateTimeFormat('en-US', { month: 'long', timeZone: 'UTC' }).format(new Date(`${year}-${String(monthNumber).padStart(2, '0')}-01T00:00:00Z`)),
    ...summary(days.filter(day => Number(day.date.slice(5, 7)) === monthNumber)) }));
  const analysis = { settings, period: { from: days[0].date, to: days.at(-1).date }, county: { id: county.id, name: county.name },
    ...totals, days, months, peak, longestRun: longestRun(days),
    categoryCounts: CATEGORIES.map(category => ({ category, count: observed.filter(day => day.category === category).length })),
    pollutantCounts: POLLUTANTS.map(parameter => ({ parameter, count: observed.filter(day => day.parameter === parameter).length })),
    siteCountRange: { min: observed.length ? Math.min(...observed.map(day => day.sites)) : null, max: observed.length ? Math.max(...observed.map(day => day.sites)) : null },
    sources: [source], provider: snapshot.provider, scope: snapshot.scope };
  analysisDisplays.set(analysis, display);
  return analysis;
}

export function airCsv(analysis) {
  if (!plain(analysis) || !analysisDisplays.has(analysis)) throw new Error('Export a verified daily air quality analysis.');
  const s = analysis.settings;
  const rows = [['county_fips', 'county_name', 'date', 'state', 'source_aqi', 'source_category', 'source_defining_parameter', 'source_defining_site', 'source_reporting_site_count',
    'source_csv_row_including_header', 'aqi_threshold_inclusive', 'meets_threshold', 'selected_year', 'selected_month_0_all', 'source_zip_url', 'source_zip_sha256', 'source_provider_created',
    'source_captured_at', 'scope']];
  for (const day of analysis.days) rows.push([analysis.county.id, analysis.county.name, day.date, day.missing ? 'missing' : 'reported',
    day.rawAqi, day.category, day.parameter, day.site, day.rawSites, day.sourceRow, s.threshold, day.meets, s.year, s.month,
    day.source.url, day.source.sha256, day.source.providerCreated, day.source.capturedAt, analysis.scope]);
  return csv(rows);
}

export function airReceipt(analysis, descriptor, { inspectedDate = null } = {}) {
  const display = plain(analysis) ? analysisDisplays.get(analysis) : null;
  if (!display || !validDisplay(descriptor) || !sameSource(display, descriptor)) throw new Error('The analysis receipt requires its matching verified display identity.');
  if (inspectedDate !== null && (!realDate(inspectedDate) || !analysis.days.some(day => day.date === inspectedDate))) throw new Error('Inspect a date within the selected calendar window.');
  const { months, categoryCounts, pollutantCounts, sources } = analysis;
  const stats = analysis;
  return { schema: 'kfm.daily-air-quality-analysis/v1', scope: 'provider-context', provider: analysis.provider,
    review: 'PENDING', admission: 'PENDING', release: 'UNRELEASED', selection: { ...analysis.settings, inspectedDate },
    period: analysis.period, county: analysis.county, summary: { expected: stats.expected, reported: stats.reported, missing: stats.missing,
      thresholdDays: stats.thresholdDays, thresholdPct: stats.thresholdPct, medianAqi: stats.medianAqi, peak: stats.peak, longestRun: stats.longestRun, siteCountRange: stats.siteCountRange },
    months, categoryCounts, pollutantCounts, inspectedRecord: inspectedDate === null ? null : analysis.days.find(day => day.date === inspectedDate),
    display: { ...display }, sources,
    methods: { aqi: 'EPA-provided county daily AQI, category, defining pollutant/site and reporting-site count; AQI is not recomputed from concentrations.',
      countySupport: 'Highest reported qualifying monitor AQI in the county for that date; not a county average, personal exposure or population coverage.',
      threshold: 'Reported AQI >= selected inclusive integer threshold. Missing dates are not zero or below-threshold days.',
      percentage: '100 * thresholdDays / reportedDays; null when no day is reported. Calendar coverage is reported/expected.',
      median: 'Median of reported daily county AQI values; midpoint of the two middle values for an even count.',
      runs: 'Consecutive calendar dates meeting threshold. Missing dates break runs; window/missing boundaries are censored. Earliest longest run wins ties.',
      peak: 'Highest reported daily AQI in the selected window; earliest date wins ties.',
      definingPollutant: 'Counts only days when the named pollutant defined the county AQI. Does not identify concentrations, regulatory violations or an event cause.',
      revisions: 'Historical AQS files can be revised, including AQI breakpoint treatment. Values and provider file creation/capture identities are retained as published.',
      missing: 'No county daily AQI row in this captured source; reason is not inferred. Counties without records are not represented as clean air.',
      sourceRows: 'Original national CSV record number with header at row 1; raw AQI and site-count tokens preserved in CSV.' },
    limitations: ['Historical county-monitor summaries for 2020–2025; no live conditions, forecast, individual exposure or health outcome.',
      'Reporting pollutants, monitor networks and sampled dates vary; six years do not establish a climate normal or trend.',
      'Scientific review, source admission and dataset release are separate from a successful display or export.'] };
}

import { YEARS, calendar, csv, iso, samePeriod, sameSource, validSource, yearSource } from '../../science/science-model.mjs';

export function assessmentDates(fromYear = 2020, toYear = 2025) {
  const first = new Date(`${fromYear}-01-01T00:00:00Z`);
  first.setUTCDate(first.getUTCDate() + (9 - first.getUTCDay()) % 7);
  return calendar(iso(first), `${toYear}-12-31`, 7);
}
const round = value => Math.round(value * 100) / 100;
export function droughtCategories(values) {
  if (values === null) return null;
  return [values[0], ...values.slice(1, -1).map((value, index) => round(value - values[index + 2])), values[5]];
}
export function validateDroughtSnapshot(snapshot, manifest) {
  const fail = () => { throw new Error('The county drought snapshot has an invalid schema or coverage.'); };
  if (!snapshot || snapshot.schema !== 'kfm.county-drought/v1' || manifest?.schema !== 'kfm.county-drought-manifest/v1' ||
      !samePeriod(snapshot.period) || !samePeriod(manifest.period) || snapshot.statisticsType !== 1 ||
      typeof snapshot.attribution !== 'string' || snapshot.attribution !== manifest.attribution) fail();
  const expected = assessmentDates();
  if (!Array.isArray(snapshot.weeks) || snapshot.weeks.length !== expected.length ||
      !snapshot.weeks.every((value, index) => value === expected[index]) || manifest.snapshot.weeks !== expected.length) fail();
  if (!Array.isArray(snapshot.sources) || snapshot.sources.length !== 6 || !Array.isArray(manifest.sources) ||
      !snapshot.sources.every((source, index) => validSource(source) && source.year === YEARS[index] && sameSource(source, manifest.sources[index]) &&
        source.url.startsWith('https://usdmdataservices.unl.edu/api/CountyStatistics/GetDroughtSeverityStatisticsByAreaPercent?'))) fail();
  const ids = new Set();
  let records = 0;
  if (!Array.isArray(snapshot.counties) || snapshot.counties.length !== 105 || !Array.isArray(manifest.counties) || manifest.counties.length !== 105) fail();
  for (const county of snapshot.counties) {
    const ordinal = Number(county?.id?.slice(2));
    const descriptor = manifest.counties.find(value => value.id === county?.id);
    if (!/^20\d{3}$/.test(county?.id) || ordinal < 1 || ordinal > 209 || ordinal % 2 !== 1 || ids.has(county.id) ||
        !descriptor || descriptor.name !== county.name || !/^[A-Za-z][A-Za-z .'-]{0,50} County$/.test(county.name) ||
        !Array.isArray(county.values) || county.values.length !== expected.length) fail();
    ids.add(county.id);
    for (const values of county.values) {
      if (values === null) continue;
      if (!Array.isArray(values) || values.length !== 6 || values.some(value => !Number.isFinite(value) || value < 0 || value > 100) ||
          Math.abs(values[0] + values[1] - 100) > 0.011 || values.slice(1, -1).some((value, index) => value < values[index + 2])) fail();
      records++;
    }
  }
  if (records !== manifest.snapshot.records) fail();
  return snapshot;
}

function countySummary(county, dates, indexes, settings) {
  const weeks = indexes.map(index => {
    const values = county.values[index];
    // The source parser checks that each reported row's ValidEnd is ValidStart plus six days.
    const through = values ? iso(new Date(Date.parse(`${dates[index]}T00:00:00Z`) + 6 * 86400000)) : null;
    return { date: dates[index], through, none: values?.[0] ?? null, shares: values?.slice(1) ?? null,
      categories: droughtCategories(values), dsci: values ? round(values.slice(1).reduce((a, b) => a + b, 0)) : null,
      share: values?.[settings.level + 1] ?? null, meets: values ? values[settings.level + 1] >= settings.threshold : null, missing: !values };
  });
  const observed = weeks.filter(week => !week.missing);
  let start = null;
  let longestRun = { count: 0, from: null, to: null, leftBoundary: null, rightBoundary: null };
  for (let index = 0; index <= weeks.length; index++) {
    if (index < weeks.length && weeks[index].meets) { if (start === null) start = index; continue; }
    if (start !== null) {
      const count = index - start;
      if (count > longestRun.count) longestRun = { count, from: weeks[start].date, to: weeks[index - 1].date,
        leftBoundary: start === 0 ? 'window' : weeks[start - 1].missing ? 'missing' : null,
        rightBoundary: index === weeks.length ? 'window' : weeks[index].missing ? 'missing' : null };
      start = null;
    }
  }
  return { id: county.id, name: county.name, weeks, expected: weeks.length, valid: observed.length, missing: weeks.length - observed.length,
    thresholdWeeks: observed.filter(week => week.meets).length, longestRun,
    peakShare: observed.length ? Math.max(...observed.map(week => week.share)) : null,
    meanDsci: observed.length ? observed.reduce((sum, week) => sum + week.dsci, 0) / observed.length : null };
}

export function analyseDrought(snapshot, { countyId = '20055', compareId = '20161', fromYear = 2020, toYear = 2025, level = 2, threshold = 50 } = {}) {
  if (!YEARS.includes(fromYear) || !YEARS.includes(toYear) || fromYear > toYear || ![1, 2, 3, 4].includes(level) ||
      !Number.isFinite(threshold) || threshold < 0.01 || threshold > 100 || threshold !== Math.round(threshold * 100) / 100) {
    throw new Error('Choose a valid year range, severity and area threshold (0.01–100%, in 0.01% steps).');
  }
  const settings = { countyId, compareId, fromYear, toYear, level, threshold };
  const indexes = snapshot.weeks.flatMap((day, index) => Number(day.slice(0, 4)) >= fromYear && Number(day.slice(0, 4)) <= toYear ? [index] : []);
  const summaries = snapshot.counties.map(county => countySummary(county, snapshot.weeks, indexes, settings));
  const primary = summaries.find(county => county.id === countyId);
  const comparison = summaries.find(county => county.id === compareId);
  if (!primary || !comparison) throw new Error('Choose a Kansas county from the snapshot.');
  const ranking = summaries.map(({ weeks: _weeks, ...summary }) => summary).sort((a, b) => b.thresholdWeeks - a.thresholdWeeks ||
    (b.peakShare ?? -1) - (a.peakShare ?? -1) || a.name.localeCompare(b.name));
  return { settings, period: { from: snapshot.weeks[indexes[0]], to: snapshot.weeks[indexes.at(-1)] }, expected: indexes.length,
    primary, comparison, ranking, sources: snapshot.sources, attribution: snapshot.attribution };
}

export const WINTER_WHEAT_HARVEST_YEARS = Object.freeze(YEARS.slice(1));
export const WINTER_WHEAT_MONTHS = Object.freeze([
  'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
]);

export function winterWheatSeason(snapshot, countyId, harvestYear) {
  const county = snapshot.counties.find(({ id }) => id === countyId);
  if (!county || !WINTER_WHEAT_HARVEST_YEARS.includes(harvestYear)) {
    throw new Error('Choose a Kansas county and a harvest year with full calendar coverage.');
  }

  const from = `${harvestYear - 1}-09-01`;
  const through = `${harvestYear}-07-31`;
  const indexes = snapshot.weeks.flatMap((date, index) => date >= from && date <= through ? [index] : []);
  const summary = countySummary(county, snapshot.weeks, indexes, { level: 2, threshold: 50 });
  const months = WINTER_WHEAT_MONTHS.map((label, index) => {
    const month = String((index + 8) % 12 + 1).padStart(2, '0');
    const weeks = summary.weeks.filter((week) => week.date.slice(5, 7) === month);
    const reported = weeks.filter((week) => !week.missing);
    return {
      label,
      reported: reported.length,
      expected: weeks.length,
      thresholdWeeks: reported.length ? reported.filter((week) => week.meets).length : null,
    };
  });

  return {
    harvestYear,
    from,
    through,
    reported: summary.valid,
    expected: summary.expected,
    thresholdWeeks: summary.valid ? summary.thresholdWeeks : null,
    peakShare: summary.peakShare,
    months,
  };
}

export function droughtCsv(analysis) {
  const s = analysis.settings;
  const rows = [['county_fips', 'county_name', 'assessment_date', 'valid_through', 'state', 'none_percent', 'd0_plus_percent', 'd1_plus_percent', 'd2_plus_percent', 'd3_plus_percent', 'd4_percent',
    'only_none_percent', 'only_d0_percent', 'only_d1_percent', 'only_d2_percent', 'only_d3_percent', 'only_d4_percent', 'dsci_points', 'selected_level', 'area_threshold_percent', 'meets_threshold',
    'from_year', 'to_year', 'comparison_fips', 'source_url', 'source_sha256', 'statistics_type', 'source_captured_at', 'source_bytes', 'source_attribution']];
  for (const county of [analysis.primary, analysis.comparison]) for (const week of county.weeks) {
    const source = yearSource(analysis.sources, week.date);
    rows.push([county.id, county.name, week.date, week.through, week.missing ? 'missing' : 'reported', week.none,
      ...(week.shares ?? Array(5).fill(null)), ...(week.categories ?? Array(6).fill(null)), week.dsci, s.level === 4 ? 'D4' : `D${s.level}+`, s.threshold, week.meets,
      s.fromYear, s.toYear, s.compareId, source.url, source.sha256, 1, source.capturedAt, source.bytes, analysis.attribution]);
  }
  return csv(rows);
}
export function droughtReceipt(analysis, descriptor) {
  if (descriptor?.id !== 'kansas' || !/^[a-f0-9]{64}$/.test(descriptor.sha256)) throw new Error('Drought receipt snapshot identity mismatch.');
  const summary = ({ weeks: _weeks, ...rest }) => rest;
  return { schema: 'kfm.county-drought-analysis/v1', scope: 'provider-context', settings: analysis.settings, period: analysis.period,
    primary: summary(analysis.primary), comparison: summary(analysis.comparison), ranking: analysis.ranking,
    displaySnapshot: { url: descriptor.url, sha256: descriptor.sha256, bytes: descriptor.bytes }, sources: analysis.sources,
    attribution: analysis.attribution, method: 'Cumulative county-area percentages; DSCI=sum(D0..D4), 0–500. Threshold counts are Tuesday assessments, not physical drought days. Missing assessments break runs; window and missing boundaries censor observed runs.',
    csvDateConvention: 'For reported assessments, assessment_date and valid_through are the provider validity interval start (Tuesday) and end (Monday). The interval does not specify publication time or physical drought duration. Missing assessments have no valid_through value.',
    reviewState: 'PENDING', sourceAdmission: 'PENDING', releaseState: 'UNRELEASED' };
}

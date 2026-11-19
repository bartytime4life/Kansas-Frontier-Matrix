import { relationship, scientificSummary } from '../living-welcome/stories/science-model.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from './public-snapshots.mjs';
const finite = value => typeof value === 'number' && Number.isFinite(value);
const yearOf = value => Number(String(value ?? '').slice(0, 4));
const daysInYear = year => (Date.UTC(year + 1, 0, 1) - Date.UTC(year, 0, 1)) / 86400000;
const annualRows = bundle => bundle?.data?.records || [];
const lastCompleteYear = bundle => Number.isFinite(yearOf(bundle?.built_at)) && yearOf(bundle?.built_at) > 1900 ? yearOf(bundle.built_at) - 1 : 2025;

export function signalCatalog(bundles = {}) {
  const entries = [], add = (story, id, label, family, unit, spec, method) => {
    const series = annualSignal(bundles[story], spec);
    if (!series.rows.length) return;
    entries.push({ id, label, family, story, spec, unit, from: series.rows[0].year, to: series.rows.at(-1).year, method });
  };
  const climate = bundles['climate-stripes'];
  for (const area of climate?.data?.areas || []) for (const [element, meta] of Object.entries(climate.data.elements || {})) add('climate-stripes', `climate:${area.id}:${element}`, `${area.name} · ${meta.label}`, 'Climate', meta.unit, { kind: 'climate', area: area.id, element }, element === 'pcpn' ? 'Sum of 12 complete monthly precipitation values.' : 'Mean of 12 complete monthly values.');
  const energy = new Map(annualRows(bundles['energy-shift']).map(row => [row.seriesId, row]));
  for (const [series, row] of energy) add('energy-shift', `energy:${series}`, row.name, 'Energy', row.unit, { kind: 'energy', series }, 'Source-reported annual EIA SEDS series; overlapping accounting series are not additive.');
  const sites = new Map(annualRows(bundles['river-memory']).map(row => [row.siteCode, row.name]));
  for (const [site, name] of sites) add('river-memory', `river:${site}`, name, 'Rivers', 'ft³/s', { kind: 'river', site }, 'Unweighted mean of daily discharge; completed calendar years with at least 90% of calendar days.');
  for (const [key, label, unit] of [['count', 'Kansas tornado records', 'records'], ['fatalities', 'Kansas tornado fatalities', 'people'], ['injuries', 'Kansas tornado injuries', 'people'], ['maxLength', 'Kansas longest tornado track', 'mi']]) add('tornado-tracks', `tornado:${key}`, label, 'Tornadoes', unit, { kind: 'tornado', measure: key }, key === 'count' ? 'Annual count of source track records within the published catalog coverage.' : 'Annual source-reported impact or maximum track length; unknown values are not zero.');
  for (const [key, label, unit] of [['count', 'Kansas + border M≥1 earthquake records', 'events'], ['count3', 'Kansas + border M≥3 earthquake records', 'events'], ['maxMagnitude', 'Kansas + border largest earthquake', 'magnitude']]) add('shaking-ground', `quake:${key}`, label, 'Earthquakes', unit, { kind: 'quake', measure: key }, 'Complete calendar years within the declared USGS catalog coverage; changing detection and magnitude types limit comparisons.');
  return entries;
}

export function annualSignal(bundle, spec = {}) {
  const rows = [], excluded = [], records = annualRows(bundle);
  let method = '', unit = '';
  if (!bundle) return { rows, excluded, method, unit };
  if (spec.kind === 'climate') {
    const data = bundle.data || {}, meta = data.elements?.[spec.element] || {}, values = data.values?.[spec.element]?.[spec.area] || [], scale = finite(meta.scale) && meta.scale > 0 ? meta.scale : 1;
    method = spec.element === 'pcpn' ? '12-month sum' : '12-month mean'; unit = meta.unit;
    (data.years || []).forEach((year, index) => {
      const months = values.slice(index * 12, index * 12 + 12), count = months.filter(finite).length;
      if (months.length !== 12 || count !== 12) { excluded.push({ year, reason: 'Incomplete monthly year', count, expected: 12 }); return; }
      const value = months.reduce((sum, month) => sum + month, 0) / scale / (spec.element === 'pcpn' || meta.annual === 'sum' ? 1 : 12);
      rows.push({ year, value, count: 12, expected: 12, coverage: 1 });
    });
  } else if (spec.kind === 'energy') {
    method = 'Source-reported annual value';
    const groups = new Map(); for (const record of records.filter(row => row.seriesId === spec.series)) { if (!groups.has(record.year)) groups.set(record.year, []); groups.get(record.year).push(record); }
    for (const [year, values] of groups) {
      unit = values[0].unit;
      if (values.length !== 1 || !finite(values[0].value)) excluded.push({ year, reason: values.length > 1 ? 'Duplicate annual observations' : 'Missing annual value', count: 0, expected: 1 });
      else rows.push({ year, value: values[0].value, count: 1, expected: 1, coverage: 1 });
    }
  } else if (spec.kind === 'river') {
    method = 'Mean daily discharge; ≥90% calendar-day coverage'; unit = 'ft³/s';
    const groups = new Map();
    for (const row of records.filter(record => record.siteCode === spec.site)) {
      if (!/^\d{4}-\d{2}-\d{2}$/.test(row.date || '')) continue;
      const year = yearOf(row.date); if (!groups.has(year)) groups.set(year, new Map());
      const days = groups.get(year);
      // Conflicting duplicate daily observations make that day unavailable.
      if (days.has(row.date) && days.get(row.date) !== row.discharge) days.set(row.date, null); else if (!days.has(row.date)) days.set(row.date, row.discharge);
    }
    for (const [year, days] of groups) {
      const values = [...days.values()].filter(finite), count = values.length, expected = daysInYear(year);
      if (year > lastCompleteYear(bundle) || count / expected < .9) excluded.push({ year, reason: year > lastCompleteYear(bundle) ? 'Calendar year still in progress at retrieval' : 'Below 90% calendar-day coverage', count, expected });
      else rows.push({ year, value: values.reduce((sum, value) => sum + value, 0) / count, count, expected, coverage: count / expected });
    }
  } else if (spec.kind === 'tornado' || spec.kind === 'quake') {
    method = 'Annual event catalog aggregate'; unit = spec.measure?.startsWith('count') ? 'events' : spec.measure === 'maxLength' ? 'mi' : spec.measure === 'maxMagnitude' ? 'magnitude' : 'people';
    const first = yearOf(bundle.observed?.from), last = Math.min(yearOf(bundle.observed?.to), lastCompleteYear(bundle));
    if (!Number.isInteger(first) || !Number.isInteger(last) || first < 1800 || last - first > 250) return { rows, excluded, method, unit };
    for (let year = first; year <= last; year++) {
      const events = records.filter(record => record.year === year); let value = null;
      if (spec.measure === 'count') value = events.length;
      else if (spec.measure === 'count3') {
        if (events.every(row => finite(row.magnitude))) value = events.filter(row => row.magnitude >= 3).length;
      } else {
        const key = spec.measure === 'maxLength' ? 'length' : spec.measure === 'maxMagnitude' ? 'magnitude' : spec.measure, values = events.map(row => row[key]);
        if (values.length && values.every(finite)) value = spec.measure.startsWith('max') ? Math.max(...values) : values.reduce((sum, number) => sum + number, 0);
        else if (!values.length && ['injuries', 'fatalities'].includes(spec.measure)) value = 0;
      }
      if (value === null) excluded.push({ year, reason: events.length ? 'Missing source measurement in annual aggregate' : 'No events: maximum is undefined', count: 0, expected: events.length });
      else rows.push({ year, value, count: events.length, expected: events.length, coverage: 1 });
    }
    const observedLast = yearOf(bundle.observed?.to);
    if (observedLast > last) excluded.push({ year: observedLast, reason: 'Calendar year still in progress at retrieval', count: records.filter(row => row.year === observedLast).length, expected: null });
  }
  rows.sort((a, b) => a.year - b.year); excluded.sort((a, b) => a.year - b.year);
  return { rows, excluded, method, unit };
}

function transformedPairs(xRows, yRows, { from, to, lag, transform }) {
  const ys = new Map(yRows.map(row => [row.year, row.value]));
  let pairs = xRows.filter(row => row.year >= from && row.year <= to && row.year + lag >= from && row.year + lag <= to && ys.has(row.year + lag)).map(row => ({ year: row.year, xYear: row.year, yYear: row.year + lag, rawX: row.value, rawY: ys.get(row.year + lag), x: row.value, y: ys.get(row.year + lag) }));
  if (transform === 'difference') pairs = pairs.flatMap((pair, index) => { const previous = pairs[index - 1]; return previous && pair.xYear === previous.xYear + 1 && pair.yYear === previous.yYear + 1 ? [{ ...pair, x: pair.rawX - previous.rawX, y: pair.rawY - previous.rawY }] : []; });
  if (transform === 'detrended' && pairs.length >= 3) {
    for (const key of ['x', 'y']) {
      const summary = scientificSummary(pairs, key), meanYear = pairs.reduce((sum, pair) => sum + pair.year, 0) / pairs.length;
      const xx = pairs.reduce((sum, pair) => sum + (pair.year - meanYear) ** 2, 0), xy = pairs.reduce((sum, pair) => sum + (pair.year - meanYear) * (pair[key] - summary.mean), 0), slope = xx ? xy / xx : 0;
      // Round numerical noise for a perfectly linear sequence to exactly zero.
      pairs = pairs.map(pair => { const residual = pair[key] - (summary.mean + slope * (pair.year - meanYear)); return { ...pair, [key]: Math.abs(residual) <= 1e-12 * Math.max(1, Math.abs(pair[key])) ? 0 : residual }; });
    }
  } else if (transform === 'detrended') pairs = [];
  const x = scientificSummary(pairs, 'x'), y = scientificSummary(pairs, 'y');
  return pairs.map(pair => ({ ...pair, zX: x.standardDeviation ? (pair.x - x.mean) / x.standardDeviation : null, zY: y.standardDeviation ? (pair.y - y.mean) / y.standardDeviation : null }));
}

export function analyzeSignals(bundles = {}, controls = {}) {
  const catalog = signalCatalog(bundles), x = catalog.find(entry => entry.id === controls.x) || null, y = catalog.find(entry => entry.id === controls.y) || null;
  const numericYear = (value, fallback) => value !== '' && value !== null && Number.isInteger(Number(value)) ? Math.min(2100, Math.max(1800, Number(value))) : fallback;
  const from = numericYear(controls.from, Math.max(x?.from || 1960, y?.from || 1960)), to = numericYear(controls.to, Math.min(x?.to || 2025, y?.to || 2025));
  const lag = Number.isInteger(Number(controls.lag)) ? Math.max(-5, Math.min(5, Number(controls.lag))) : 0, transform = ['raw', 'difference', 'detrended'].includes(controls.transform) ? controls.transform : 'raw';
  const a = annualSignal(x && bundles[x.story], x?.spec), b = annualSignal(y && bundles[y.story], y?.spec), params = { from, to, lag, transform };
  const pairs = transformedPairs(a.rows, b.rows, params), stats = relationship(pairs, 'x', 'y');
  const coverage = series => ({ eligible: series.rows.filter(row => row.year >= from && row.year <= to).length, excluded: series.excluded.filter(row => row.year >= from && row.year <= to), missingYears: from <= to ? Array.from({ length: to - from + 1 }, (_, index) => from + index).filter(year => !series.rows.some(row => row.year === year)) : [], method: series.method });
  const sources = [...new Set([x?.story, y?.story].filter(Boolean))];
  return { x, y, pairs, count: pairs.length, excluded: Math.max(0, to - from + 1 - pairs.length), pearson: stats.pearson, spearman: stats.spearman, rSquared: stats.rSquared, slope: stats.slope, intercept: stats.intercept, reason: !x || !y ? 'Choose two available signals.' : from > to ? 'Start year must be no later than end year.' : stats.reason,
    lagProfile: Array.from({ length: 11 }, (_, index) => { const lag = index - 5, rows = transformedPairs(a.rows, b.rows, { ...params, lag }), fit = relationship(rows, 'x', 'y'); return { lag, count: rows.length, pearson: fit.pearson, spearman: fit.spearman }; }), coverage: { x: coverage(a), y: coverage(b) }, bounds: { from, to }, sources, bindings: Object.fromEntries(sources.filter(story => PUBLIC_LAB_SNAPSHOTS[story]).map(story => [story, PUBLIC_LAB_SNAPSHOTS[story].sha256])) };
}

export const SIGNAL_PRESETS = Object.freeze([
  { id: 'rain-and-tornadoes', title: 'Rain & tornado records', description: 'Compare precipitation and recorded Kansas tornadoes across the same complete years.', controls: { x: 'climate:20:pcpn', y: 'tornado:count', from: 1950, to: 2025, lag: 0, transform: 'raw' } },
  { id: 'energy-transition', title: 'Wind & coal', description: 'Explore the annual energy transition, then remove the shared passage of time.', controls: { x: 'energy:SEDS.WYPRB.KS.A', y: 'energy:SEDS.CLTCB.KS.A', from: 1990, to: 2024, lag: 0, transform: 'raw' } },
  { id: 'warmth-and-energy', title: 'Temperature & home energy', description: 'Compare annual changes in statewide temperature and residential energy use.', controls: { x: 'climate:20:tmpc', y: 'energy:SEDS.TERCB.KS.A', from: 1960, to: 2024, lag: 0, transform: 'difference' } },
  { id: 'rain-and-river', title: 'Rain & the Kansas River', description: 'A short modern record: inspect complete-year coverage and each paired year.', controls: { x: 'climate:20:pcpn', y: 'river:06892350', from: 2020, to: 2025, lag: 0, transform: 'raw' } },
  { id: 'quake-thresholds', title: 'Earthquake thresholds', description: 'Compare recorded M≥1 and M≥3 events across Kansas and the immediate border region.', controls: { x: 'quake:count', y: 'quake:count3', from: 2010, to: 2025, lag: 0, transform: 'raw' } },
]);

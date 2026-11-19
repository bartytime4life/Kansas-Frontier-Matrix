// Descriptive statistics for the exact selected source rows. No imputation or inference.
import { numeric } from './record-model.mjs';

export function scienceMetrics(model) {
  return model.metrics.filter(column => column.analysis !== false && !/(?:flag|code|identifier|^id$)/i.test(column.key));
}

/** R type 7: interpolate at (n - 1) p in the ascending observations. */
export function quantile(values, probability) {
  const sorted = values.filter(value => numeric(value) !== null).toSorted((a, b) => a - b);
  if (!sorted.length || !Number.isFinite(probability) || probability < 0 || probability > 1) return null;
  const index = (sorted.length - 1) * probability, lower = Math.floor(index), fraction = index - lower;
  return sorted[lower] + (sorted[Math.ceil(index)] - sorted[lower]) * fraction;
}

export function scientificSummary(records, key) {
  const values = records.map(record => numeric(record[key])).filter(value => value !== null);
  let mean = 0, squared = 0;
  values.forEach((value, index) => { const delta = value - mean; mean += delta / (index + 1); squared += delta * (value - mean); });
  return { total: records.length, count: values.length, missing: records.length - values.length,
    min: values.length ? Math.min(...values) : null, max: values.length ? Math.max(...values) : null,
    mean: values.length ? mean : null, median: quantile(values, .5), q1: quantile(values, .25), q3: quantile(values, .75),
    standardDeviation: values.length > 1 ? Math.sqrt(Math.max(0, squared / (values.length - 1))) : null };
}

function averageRanks(values) {
  const sorted = values.map((value, index) => ({ value, index })).toSorted((a, b) => a.value - b.value), ranks = Array(values.length);
  for (let start = 0; start < sorted.length;) {
    let end = start + 1;
    while (end < sorted.length && sorted[end].value === sorted[start].value) end++;
    const rank = (start + 1 + end) / 2;
    for (let index = start; index < end; index++) ranks[sorted[index].index] = rank;
    start = end;
  }
  return ranks;
}

function centeredFit(xs, ys) {
  const n = xs.length;
  if (n < 3) return { reason: 'At least three complete pairs are needed.' };
  const meanX = xs.reduce((sum, value) => sum + value, 0) / n, meanY = ys.reduce((sum, value) => sum + value, 0) / n;
  let xx = 0, yy = 0, xy = 0;
  for (let index = 0; index < n; index++) { const x = xs[index] - meanX, y = ys[index] - meanY; xx += x * x; yy += y * y; xy += x * y; }
  if (!xx || !yy) return { reason: 'Both measures need variation; a constant axis has no correlation.' };
  const r = Math.max(-1, Math.min(1, xy / Math.sqrt(xx * yy))), slope = xy / xx;
  return { r, rSquared: r * r, slope, intercept: meanY - slope * meanX, reason: null };
}

export function relationship(records, xKey, yKey) {
  const pairs = records.flatMap(record => {
    const x = numeric(record[xKey]), y = numeric(record[yKey]);
    return x === null || y === null ? [] : [{ record, x, y }];
  });
  const xs = pairs.map(pair => pair.x), ys = pairs.map(pair => pair.y), fit = centeredFit(xs, ys);
  const ranked = fit.reason ? null : centeredFit(averageRanks(xs), averageRanks(ys));
  return { pairs, total: records.length, count: pairs.length, excluded: records.length - pairs.length,
    pearson: fit.r ?? null, spearman: ranked?.r ?? null, rSquared: fit.rSquared ?? null,
    slope: fit.slope ?? null, intercept: fit.intercept ?? null, reason: fit.reason,
    minX: xs.length ? Math.min(...xs) : null, maxX: xs.length ? Math.max(...xs) : null,
    minY: ys.length ? Math.min(...ys) : null, maxY: ys.length ? Math.max(...ys) : null };
}

/** Bounded deterministic mark sample; all analytical summaries still use all pairs. */
export function sampledPairs(pairs, maximum = 1800) {
  if (!Number.isInteger(maximum) || maximum < 1) return [];
  if (pairs.length <= maximum) return pairs;
  return Array.from({ length: maximum }, (_, index) => pairs[Math.floor(index * pairs.length / maximum)]);
}

export function rankRecords(records, key, direction = 'desc', limit = 12) {
  return records.filter(record => numeric(record[key]) !== null).toSorted((a, b) => (a[key] - b[key]) * (direction === 'asc' ? 1 : -1)).slice(0, limit);
}

export function groupSummaries(records, key, field) {
  const groups = new Map();
  for (const record of records) {
    const label = record[field] === null || record[field] === undefined || record[field] === '' ? 'Not recorded' : String(record[field]);
    if (!groups.has(label)) groups.set(label, []);
    groups.get(label).push(record);
  }
  return [...groups].map(([label, rows]) => ({ label, ...scientificSummary(rows, key) })).toSorted((a, b) => b.total - a.total || a.label.localeCompare(b.label));
}

export function yearlySeries(records, yearField, valueField, categoryField) {
  const groups = new Map();
  for (const row of records) {
    const year = numeric(row[yearField]);
    if (year === null) continue;
    const category = String(row[categoryField] ?? 'Unclassified'), key = `${category}\u0000${year}`;
    if (!groups.has(key)) groups.set(key, { year, timestamp: year, date: String(year), category, values: [], missing: 0 });
    const group = groups.get(key), value = numeric(row[valueField]);
    if (value === null) group.missing++; else group.values.push(value);
  }
  return [...groups.values()].toSorted((a, b) => a.year - b.year).map(({ values, ...group }) => ({ ...group, count: values.length, mean: values.length ? values.reduce((sum, value) => sum + value, 0) / values.length : null }));
}

/** Annual values require all 12 months; partial years never enter the fit or extremes. */
export function climateAnnualAnalysis(bundle, { element = 'tmpc', area = '20', baseline = '1901-2000', from = null, to = null } = {}) {
  const data = bundle?.data || {}, values = data.values?.[element]?.[area] || [], normal = data.normals?.[baseline]?.[element]?.[area];
  const scale = numeric(data.elements?.[element]?.scale) || 1;
  const annualSum = data.elements?.[element]?.annual === 'sum' || element === 'pcpn', normalValue = normal?.length === 12 ? normal.reduce((sum, value) => sum + value, 0) / (annualSum ? 1 : 12) / scale : null;
  const inPeriod = value => value !== '' && value !== null && value !== undefined && Number.isFinite(Number(value)) ? Number(value) : null;
  const lower = inPeriod(from), upper = inPeriod(to);
  let incomplete = 0;
  const rows = (data.years || []).flatMap((year, index) => {
    if ((lower !== null && year < lower) || (upper !== null && year > upper)) return [];
    const months = values.slice(index * 12, index * 12 + 12);
    if (months.length !== 12 || months.some(value => numeric(value) === null)) { incomplete++; return []; }
    const value = months.reduce((sum, month) => sum + month, 0) / (annualSum ? 1 : 12) / scale;
    return [{ id: String(year), year, value, anomaly: normalValue === null ? null : value - normalValue }];
  });
  const fit = relationship(rows, 'year', 'value'), sorted = rows.toSorted((a, b) => a.value - b.value || a.year - b.year);
  return { rows, count: rows.length, incomplete, slopePerDecade: fit.slope === null ? null : fit.slope * 10,
    rSquared: fit.rSquared, reason: fit.reason, lowest: sorted[0] || null, highest: sorted.at(-1) || null };
}

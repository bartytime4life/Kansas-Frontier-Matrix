// Reproducible descriptive investigations over the already verified county model.
export const HISTORY_METRICS = Object.freeze(['medianIncome', 'povertyPct', 'educationPct', 'medianAge', 'unemploymentPct', 'ownerOccupiedPct', 'vacancyPct', 'medianHomeValue', 'medianRent']);
const finite = value => typeof value === 'number' && Number.isFinite(value);
const measured = value => finite(value) ? value : null;
const records = (model, id) => model.bundles?.[id]?.data?.records || [];
const HISTORY_METHOD = 'Population uses July 1 estimates from one Census vintage. ACS points are nonoverlapping five-year periods with published or derived 90% margins of error. Dollar values use each vintage’s dollars and are not inflation-adjusted. Missing observations remain gaps; this comparison does not test statistical significance.';

export function countyHistory(model, { fipsA, fipsB, metric = 'medianIncome' } = {}) {
  const a = model.rows?.find(row => row.fips === fipsA), b = model.rows?.find(row => row.fips === fipsB);
  const descriptor = model.metrics?.find(item => item.key === metric);
  const result = { counties: { a: a ? { fips: a.fips, name: a.name } : null, b: b ? { fips: b.fips, name: b.name } : null }, metric: descriptor ? { ...descriptor, unit: metric === 'medianRent' ? 'vintage-year dollars/month' : ['medianIncome', 'medianHomeValue'].includes(metric) ? 'vintage-year dollars' : descriptor.unit } : null, population: [], conditions: [], sources: (model.sourceBindings || []).filter(item => ['census-mosaic', 'county-conditions'].includes(item.id)), method: HISTORY_METHOD, reason: null };
  if (!a || !b || !HISTORY_METRICS.includes(metric) || !descriptor) return { ...result, reason: 'Choose two Kansas counties and a supported ACS history measure.' };
  for (const [id, field] of [['census-mosaic', 'population'], ['county-conditions', metric]]) {
    const source = records(model, id), index = new Map();
    for (const row of source) {
      if (![fipsA, fipsB].includes(row.fips) || !Number.isInteger(row.year)) continue;
      const key = `${row.fips}/${row.year}`;
      if (index.has(key)) return { ...result, population: [], conditions: [], reason: `Duplicate county/year in ${id}: ${key}. History is unavailable until the source is reconciled.` };
      index.set(key, row);
    }
    const years = [...new Set(source.filter(row => Number.isInteger(row.year)).map(row => row.year))].sort((x, y) => x - y);
    const rows = years.map(year => {
      const rowA = index.get(`${fipsA}/${year}`), rowB = index.get(`${fipsB}/${year}`);
      return { year, period: id === 'census-mosaic' ? `July 1, ${year}` : `${year - 4}–${year}`, valueA: measured(rowA?.[field]), valueB: measured(rowB?.[field]), ...(id === 'county-conditions' ? { moeA: measured(rowA?.[field + 'Moe']), moeB: measured(rowB?.[field + 'Moe']), unit: descriptor.unit.includes('dollars') ? `${year} ${metric === 'medianRent' ? 'dollars/month' : 'dollars'}` : descriptor.unit } : {}) };
    });
    result[id === 'census-mosaic' ? 'population' : 'conditions'] = rows;
  }
  return result;
}

const PEER_METHOD = 'A common complete-case cohort is ranked separately on each selected measure, using average ranks for ties. Percentile = 100 × (average rank − 1) / (cohort size − 1). Distance is the equal-weight root mean square of percentile-point gaps on varying measures. Constant measures are reported and omitted. No missing values are imputed. This descriptive comparison is not a risk score, causal finding, or assessment of individuals.';
export function findCountyPeers(model, { fips, keys = [], limit = 6 } = {}) {
  const anchor = model.rows?.find(row => row.fips === fips), dimensions = Array.isArray(keys) ? keys.map(key => model.metrics?.find(item => item.key === key)) : [];
  const result = { anchor: anchor ? { fips: anchor.fips, name: anchor.name } : null, peers: [], dimensions: dimensions.filter(Boolean), cohortCount: null, excludedCount: null, varyingCount: null, constantKeys: [], reason: null, method: PEER_METHOD };
  if (!anchor || !Array.isArray(keys) || keys.length < 2 || keys.length > 5 || new Set(keys).size !== keys.length || dimensions.some(item => !item)) return { ...result, reason: 'Choose a Kansas county and two to five distinct numeric measures.' };
  const identities = new Set();
  for (const row of model.rows) { if (identities.has(row.fips)) return { ...result, reason: 'Duplicate county identifiers prevent a reproducible cohort.' }; identities.add(row.fips); }
  const cohort = model.rows.filter(row => keys.every(key => finite(row[key])));
  result.cohortCount = cohort.length; result.excludedCount = model.rows.length - cohort.length;
  if (!cohort.some(row => row.fips === fips)) return { ...result, reason: 'County A has missing values in the selected measures. Choose other measures or a county with complete observations.' };
  if (cohort.length < 3) return { ...result, reason: 'At least three complete counties are required for comparison.' };
  const ranks = new Map();
  for (const key of keys) {
    const sorted = [...cohort].sort((a, b) => a[key] - b[key] || a.fips.localeCompare(b.fips));
    if (sorted[0][key] === sorted.at(-1)[key]) { result.constantKeys.push(key); continue; }
    const values = new Map();
    for (let start = 0; start < sorted.length;) {
      let end = start + 1;
      while (end < sorted.length && sorted[end][key] === sorted[start][key]) end++;
      const percentile = 100 * ((start + end - 1) / 2) / (sorted.length - 1);
      for (let index = start; index < end; index++) values.set(sorted[index].fips, percentile);
      start = end;
    }
    ranks.set(key, values);
  }
  result.varyingCount = ranks.size;
  if (ranks.size < 2) return { ...result, reason: 'At least two selected measures must vary across the complete-case cohort.' };
  const count = Number.isInteger(limit) ? Math.max(1, Math.min(10, limit)) : 6;
  result.peers = cohort.filter(row => row.fips !== fips).map(row => {
    const contributions = result.dimensions.filter(item => ranks.has(item.key)).map(item => {
      const anchorPercentile = ranks.get(item.key).get(fips), percentile = ranks.get(item.key).get(row.fips), gap = percentile - anchorPercentile;
      return { key: item.key, label: item.label, unit: item.unit, period: item.period, anchorValue: anchor[item.key], value: row[item.key], anchorPercentile, percentile, gap, squaredGap: gap ** 2 };
    });
    return { fips: row.fips, name: row.name, distance: Math.sqrt(contributions.reduce((sum, item) => sum + item.squaredGap, 0) / contributions.length), contributions };
  }).sort((a, b) => a.distance - b.distance || a.fips.localeCompare(b.fips)).slice(0, count);
  return result;
}

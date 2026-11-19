// Pure FIPS joins over the closed public Labs bundles. No network or private DB.
import { quantile } from '../living-welcome/stories/science-model.mjs';

// Census Kansas county reference, verified against all three ACS vintage files.
const NAMES = 'Allen|Anderson|Atchison|Barber|Barton|Bourbon|Brown|Butler|Chase|Chautauqua|Cherokee|Cheyenne|Clark|Clay|Cloud|Coffey|Comanche|Cowley|Crawford|Decatur|Dickinson|Doniphan|Douglas|Edwards|Elk|Ellis|Ellsworth|Finney|Ford|Franklin|Geary|Gove|Graham|Grant|Gray|Greeley|Greenwood|Hamilton|Harper|Harvey|Haskell|Hodgeman|Jackson|Jefferson|Jewell|Johnson|Kearny|Kingman|Kiowa|Labette|Lane|Leavenworth|Lincoln|Linn|Logan|Lyon|McPherson|Marion|Marshall|Meade|Miami|Mitchell|Montgomery|Morris|Morton|Nemaha|Neosho|Ness|Norton|Osage|Osborne|Ottawa|Pawnee|Phillips|Pottawatomie|Pratt|Rawlins|Reno|Republic|Rice|Riley|Rooks|Rush|Russell|Saline|Scott|Sedgwick|Seward|Shawnee|Sheridan|Sherman|Smith|Stafford|Stanton|Stevens|Sumner|Thomas|Trego|Wabaunsee|Wallace|Washington|Wichita|Wilson|Woodson|Wyandotte'.split('|');
export const KANSAS_COUNTIES = Object.freeze(NAMES.map((name, index) => Object.freeze({ fips: `20${String(index * 2 + 1).padStart(3, '0')}`, name: `${name} County` })));
const SOURCE_IDS = ['census-mosaic', 'county-conditions', 'built-kansas', 'air-and-health'];
const finite = value => typeof value === 'number' && Number.isFinite(value) ? value : null;
const rowsOf = bundle => bundle?.data?.kind === 'records' && Array.isArray(bundle.data.records) ? bundle.data.records : [];
const asBundle = value => value?.bundle || value;
const validFips = value => typeof value === 'string' && /^20\d{3}$/.test(value) ? value : null;
const YEARS = rows => [...new Set(rows.map(row => finite(row.year)).filter(value => Number.isInteger(value)))].sort((a, b) => a - b);
const mean = values => values.length ? values.reduce((sum, value) => sum + value, 0) / values.length : null;
export const normalizeCountyName = value => typeof value === 'string' ? value.trim().replace(/\s+County(?:,\s*Kansas)?$/i, '').toLocaleLowerCase('en-US') : '';

function exactIndex(rows, year, known, sourceId) {
  const index = new Map();
  for (const row of rows) {
    if (row.year !== year) continue;
    const fips = validFips(row.fips);
    if (!fips || !known.has(fips)) continue;
    if (index.has(fips)) throw new Error(`Duplicate county/year in ${sourceId}: ${fips}/${year}`);
    index.set(fips, row);
  }
  return index;
}

const ACS_METRICS = [
  ['medianIncome', 'Median household income', 'dollars', 'estimate', 'Households; vintage-year dollars, not a common inflation-adjusted series.'],
  ['povertyPct', 'People below poverty level', '%', 'rate', 'Population for whom poverty status is determined.'],
  ['educationPct', "Age 25+ with bachelor's degree or higher", '%', 'rate', 'Population age 25 and over.'],
  ['medianAge', 'Median age', 'years', 'estimate', 'ACS five-year total population.'],
  ['unemploymentPct', 'Civilian unemployment rate, age 16+', '%', 'rate', 'Civilian labor force age 16 and over.'],
  ['ownerOccupiedPct', 'Owner-occupied share', '%', 'rate', 'Occupied housing units.'],
  ['vacancyPct', 'Vacant housing share', '%', 'rate', 'All housing units; vacancy includes seasonal and other vacant units.'],
  ['medianHomeValue', 'Median owner-occupied home value', 'dollars', 'estimate', 'Owner-occupied housing units; vintage-year dollars.'],
  ['medianRent', 'Median monthly gross rent', 'dollars/month', 'estimate', 'Occupied rental units paying cash rent; vintage-year dollars.'],
];
const ACS_RATES = {
  povertyPct: ['belowPoverty', 'povertyPopulation'], educationPct: ['bachelorsOrHigher', 'adult25Population'],
  unemploymentPct: ['unemployed', 'civilianLaborForce'], ownerOccupiedPct: ['ownerUnits', 'occupiedUnits'], vacancyPct: ['vacantUnits', 'housingUnits'],
};

/**
 * bundles is keyed by public story ID; options.snapshots can provide the exact
 * verified loader manifest for receipts. Selected source years are independent.
 * Unsupported requested years stay unavailable, never silently substituted.
 */
export function buildCountyModel(input = {}, options = {}) {
  const bundles = Object.fromEntries(SOURCE_IDS.map(id => [id, asBundle(input[id])]));
  const populationRows = rowsOf(bundles['census-mosaic']), acsRows = rowsOf(bundles['county-conditions']);
  const bridgeRows = rowsOf(bundles['built-kansas']), airRows = rowsOf(bundles['air-and-health']);
  const available = { populationYears: YEARS(populationRows), acsYears: YEARS(acsRows), aqiYears: YEARS(airRows) };
  const select = (key, years, fallback) => options[key] === undefined ? years.at(-1) ?? fallback : Number(options[key]);
  const populationYear = select('populationYear', available.populationYears, 2025), acsYear = select('acsYear', available.acsYears, 2024), aqiYear = select('aqiYear', available.aqiYears, 2025);
  const inventoryAsOf = bundles['built-kansas']?.data?.inventoryAsOf || null;
  const inventoryYear = typeof inventoryAsOf === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(inventoryAsOf) ? Number(inventoryAsOf.slice(0, 4)) : null;
  const known = new Set(KANSAS_COUNTIES.map(county => county.fips));
  const names = new Map(KANSAS_COUNTIES.map(county => [normalizeCountyName(county.name), county.fips]));
  const populations = exactIndex(populationRows, populationYear, known, 'census-mosaic');
  const baselines = exactIndex(populationRows, 2020, known, 'census-mosaic');
  const conditions = exactIndex(acsRows, acsYear, known, 'county-conditions');
  const air = exactIndex(airRows, aqiYear, known, 'air-and-health');
  const geometries = new Map();
  for (const row of [...populationRows, ...acsRows]) if (known.has(row.fips) && row.geometry && !geometries.has(row.fips)) geometries.set(row.fips, row.geometry);
  const grouped = new Map(KANSAS_COUNTIES.map(county => [county.fips, []]));
  const unmatched = new Map(), identities = new Map();
  let matched = 0;
  for (const row of bridgeRows) {
    // Exact normalized official county labels only. Coordinates never choose a county.
    const fips = names.get(normalizeCountyName(row.county));
    if (!fips) { const label = typeof row.county === 'string' && row.county.trim() ? row.county : '(missing county label)'; unmatched.set(label, (unmatched.get(label) || 0) + 1); continue; }
    grouped.get(fips).push(row);
    matched++;
    if (typeof row.structure === 'string' && row.structure) {
      const identity = `${fips}\u0000${row.network || ''}\u0000${row.structure}`;
      identities.set(identity, (identities.get(identity) || 0) + 1);
    }
  }
  const bridgeAvailable = !!bundles['built-kansas']?.data && bundles['built-kansas'].data.kind === 'records';
  const periods = {
    population: `July 1, ${populationYear} population estimate`, populationChange: `July 1, 2020 to July 1, ${populationYear}`,
    acs: `${acsYear - 4}–${acsYear} ACS five-year period`, aqi: `${aqiYear} annual monitored AQI`,
    bridges: inventoryAsOf ? `KDOT inventory snapshot ${inventoryAsOf}` : 'Inventory observation date unavailable',
    bridgeAge: inventoryAsOf ? `Age in ${inventoryYear}, from inventory ${inventoryAsOf}` : 'Inventory age unavailable',
  };
  const sourceBindings = SOURCE_IDS.map(id => {
    const bundle = bundles[id], binding = options.snapshots?.[id] || input[id]?.snapshot || bundle?.snapshotBinding || {};
    return { id, story: id, loaded: !!bundle?.data, sha256: binding.sha256 || null, bytes: binding.bytes || null, path: binding.path || null,
      observed: bundle?.observed || binding.observed || null, retrievedAt: binding.retrievedAt || bundle?.built_at || null,
      records: rowsOf(bundle).length, urls: (bundle?.sources || []).map(source => source.url), sources: bundle?.sources || [],
      sourceSnapshots: bundle?.data?.sourceSnapshots || [], limits: bundle?.data?.limits || [] };
  });
  const rows = KANSAS_COUNTIES.map(county => {
    const p = populations.get(county.fips), a = conditions.get(county.fips), e = air.get(county.fips), bridges = grouped.get(county.fips);
    const population = finite(p?.population), population2020 = finite(baselines.get(county.fips)?.population);
    const changeAllowed = populationYear >= 2020 && populationYear <= 2025;
    const populationChange = changeAllowed && population !== null && population2020 !== null ? population - population2020 : null;
    const scores = bridges.map(row => finite(row.sufficiency)).filter(value => value !== null && value >= 0 && value <= 100);
    const ages = inventoryYear === null ? [] : bridges.flatMap(row => Number.isInteger(row.year) && row.year > 0 && row.year <= inventoryYear ? [inventoryYear - row.year] : []);
    const traffic = bridges.flatMap(row => finite(row.traffic) !== null && row.traffic >= 0 ? [row] : []);
    const trafficYears = traffic.flatMap(row => Number.isInteger(row.trafficYear) && row.trafficYear >= 1900 && inventoryYear !== null && row.trafficYear <= inventoryYear ? [row.trafficYear] : []);
    const row = { ...county, id: county.fips, geometry: geometries.get(county.fips) || null, populationYear, acsYear, aqiYear, inventoryAsOf,
      population, population2020, populationChange, populationChangePct: populationChange !== null && population2020 > 0 ? 100 * populationChange / population2020 : null,
      births: finite(p?.births), deaths: finite(p?.deaths), netMigration: finite(p?.netMigration), naturalChange: finite(p?.naturalChange),
      acsPeriod: `${acsYear - 4}–${acsYear}`, acsSourceFlags: a?.sourceFlags || {}, acsMoeMethods: a?.moeMethods || {},
      bridgeRecords: bridgeAvailable ? bridges.length : null, bridgeScoreMean: mean(scores), bridgeScoreCount: scores.length,
      bridgeMedianAge: quantile(ages, .5), bridgeAgeCount: ages.length, bridgeAgeMissing: bridgeAvailable ? bridges.length - ages.length : null,
      bridgeTrafficMedian: quantile(traffic.map(record => record.traffic), .5), bridgeTrafficCount: traffic.length,
      bridgeTrafficDatedCount: trafficYears.length, bridgeTrafficUndatedCount: traffic.length - trafficYears.length,
      bridgeTrafficFirstYear: trafficYears.length ? Math.min(...trafficYears) : null, bridgeTrafficLastYear: trafficYears.length ? Math.max(...trafficYears) : null,
      aqi90th: finite(e?.aqi90th), aqiMedian: finite(e?.medianAqi), aqiMax: finite(e?.maxAqi), aqiMonitoredDays: finite(e?.daysWithAqi),
      aqiCoveragePct: finite(e?.coveragePct), aqiAbove100Days: finite(e?.daysAbove100), aqiAbove100Pct: finite(e?.above100Pct), aqiGoodPct: finite(e?.goodPct),
      calendarDays: new Date(Date.UTC(aqiYear + 1, 0, 1)).getTime() - new Date(Date.UTC(aqiYear, 0, 1)).getTime(),
      availableSources: { population: !!p, acs: !!a, bridges: bridgeAvailable, aqi: !!e } };
    for (const key of [...ACS_METRICS.map(metric => metric[0]), 'povertyPopulation', 'belowPoverty', 'adult25Population', 'bachelorsOrHigher', 'bachelors', 'masters', 'professional', 'doctorate', 'civilianLaborForce', 'unemployed', 'occupiedUnits', 'ownerUnits', 'housingUnits', 'vacantUnits']) {
      row[key] = finite(a?.[key]); row[key + 'Moe'] = finite(a?.[key + 'Moe']);
    }
    row.calendarDays /= 86_400_000;
    row.bridgeRecordsPer10k = row.bridgeRecords !== null && population > 0 ? row.bridgeRecords * 10000 / population : null;
    return row;
  });
  const descriptor = (key, label, unit, sourceId, period, kind, note, extra = {}) => ({ key, label, unit, sourceId, period, kind, note, ...extra });
  const metrics = [
    descriptor('population', 'Population', 'people', 'census-mosaic', periods.population, 'count', 'Annual Census Population Estimates Program estimate.'),
    descriptor('populationChange', 'Population change since 2020', 'people', 'census-mosaic', periods.populationChange, 'count', 'Same population-estimate vintage at both endpoints.'),
    descriptor('populationChangePct', 'Population change since 2020', '%', 'census-mosaic', periods.populationChange, 'rate', 'Difference divided by the July 1, 2020 population estimate.', { rate: { numerator: 'populationChange', denominator: 'population2020', scale: 100, denominatorPeriod: 'July 1, 2020' } }),
    ...ACS_METRICS.map(([key, label, unit, kind, note]) => descriptor(key, label, unit.startsWith('dollars') ? `${acsYear} ${unit}` : unit, 'county-conditions', periods.acs, kind, note,
      { moeKey: key + 'Moe', confidenceLevel: .90, moeMethod: ACS_RATES[key] ? 'Census approximate derived proportion MOE' : 'Published source MOE',
        ...(ACS_RATES[key] ? { rate: { numerator: ACS_RATES[key][0], denominator: ACS_RATES[key][1], scale: 100, denominatorPeriod: periods.acs } } : {}) })),
    descriptor('bridgeRecords', 'Bridge inventory records', 'inventory records', 'built-kansas', periods.bridges, 'count', 'Counts returned inventory records; repeated structure identities remain. Not a unique physical bridge count.'),
    descriptor('bridgeRecordsPer10k', 'Bridge records per 10,000 residents', 'records/10,000 people', 'built-kansas', `${periods.bridges}; denominator ${periods.population}`, 'rate', 'Different source periods are explicit. This ratio does not establish demand, exposure, safety or service capacity.', { sourceIds: ['built-kansas', 'census-mosaic'], rate: { numerator: 'bridgeRecords', denominator: 'population', scale: 10000, denominatorPeriod: periods.population } }),
    descriptor('bridgeScoreMean', 'Mean source sufficiency score', 'source score (0–100)', 'built-kansas', periods.bridges, 'index', 'Unweighted arithmetic mean of records with valid source scores, including repeated inventory records. Not a safety assessment.'),
    descriptor('bridgeMedianAge', 'Median recorded bridge age', 'years', 'built-kansas', periods.bridgeAge, 'estimate', 'Inventory observation year minus valid recorded built year; missing or future years excluded. Not historical construction rates.'),
    descriptor('bridgeTrafficMedian', 'Median recorded average daily traffic', 'vehicles/day', 'built-kansas', 'Mixed traffic-count years; inspect county coverage', 'estimate', 'Median of available source record traffic counts. Undated counts remain undated; counts can have different years. Not road capacity, present-day traffic or unique vehicle demand.'),
    descriptor('aqi90th', '90th percentile daily AQI', 'AQI', 'air-and-health', periods.aqi, 'index', 'EPA annual county summary over monitored days only; no value for unmonitored counties.'),
    descriptor('aqiMedian', 'Median daily AQI', 'AQI', 'air-and-health', periods.aqi, 'index', 'EPA supplied annual median across monitored daily AQI values.'),
    descriptor('aqiAbove100Pct', 'Monitored days with AQI above 100', '%', 'air-and-health', periods.aqi, 'rate', 'Days AQI 101+ divided by days with AQI; not a health outcome or annual exposure estimate.', { rate: { numerator: 'aqiAbove100Days', denominator: 'aqiMonitoredDays', scale: 100, denominatorPeriod: periods.aqi } }),
    descriptor('aqiCoveragePct', 'Calendar days with AQI observations', '%', 'air-and-health', periods.aqi, 'rate', 'Monitored days divided by calendar days in the selected year.', { rate: { numerator: 'aqiMonitoredDays', denominator: 'calendarDays', scale: 100, denominatorPeriod: String(aqiYear) } }),
  ];
  const diagnostics = { countyCount: rows.length, populationMatched: populations.size, acsMatched: conditions.size, aqiMatched: air.size,
    bridgeTotalRecords: bridgeRows.length, bridgeMatchedRecords: matched, bridgeUnmatchedRecords: bridgeRows.length - matched,
    bridgeUnmatchedCountyLabels: [...unmatched].map(([label, records]) => ({ label, records })),
    bridgeRepeatedStructureIdentities: [...identities.values()].filter(count => count > 1).length,
    bridgeRepeatedIdentityExtraRecords: [...identities.values()].reduce((sum, count) => sum + Math.max(0, count - 1), 0),
    bridgeJoin: 'Exact normalized county names to verified county FIPS; no point-in-polygon or nearest-county assignment.',
    missingGeometry: rows.filter(row => !row.geometry).length,
    warnings: options.inventoryYear !== undefined && Number(options.inventoryYear) !== inventoryYear ? ['The present inventory is fixed to its source observation date; a requested inventory year cannot reconstruct an earlier inventory.'] : [] };
  return { rows, metrics, periods, sourceBindings, diagnostics, selection: { populationYear, acsYear, aqiYear, inventoryYear, inventoryAsOf },
    options: available, bundles, method: 'County measures are joined by exact county FIPS or exact normalized official county label. Source periods are selected independently; descriptive association does not establish cause.' };
}

export const countyMetric = (model, key) => model.metrics.find(metric => metric.key === key) || null;

export function populationChange(model, fips, from = 2020, to = model.selection.populationYear) {
  if (!Number.isInteger(from) || !Number.isInteger(to) || from < 2020 || to > 2025 || from > to) return { from, to, difference: null, percent: null, reason: 'Select annual population estimate years within 2020–2025.' };
  const records = rowsOf(model.bundles['census-mosaic']).filter(row => row.fips === fips);
  const start = finite(records.find(row => row.year === from)?.population), end = finite(records.find(row => row.year === to)?.population);
  return { from, to, start, end, difference: start !== null && end !== null ? end - start : null,
    percent: start > 0 && end !== null ? 100 * (end - start) / start : null, reason: start === null || end === null ? 'An endpoint population estimate is unavailable.' : null };
}

export function describeCounty(model, fips) {
  const row = model.rows.find(county => county.fips === fips);
  if (!row) return null;
  const populationHistory = rowsOf(model.bundles['census-mosaic']).filter(record => record.fips === fips).toSorted((a, b) => a.year - b.year);
  const acsHistory = rowsOf(model.bundles['county-conditions']).filter(record => record.fips === fips).toSorted((a, b) => a.year - b.year);
  const aqiHistory = rowsOf(model.bundles['air-and-health']).filter(record => record.fips === fips).toSorted((a, b) => a.year - b.year);
  return { ...row, row, populationChange: populationChange(model, fips), periods: model.periods, sourceBindings: model.sourceBindings,
    populationHistory, acsHistory, aqiHistory, metrics: model.metrics.map(metric => ({ ...metric, value: row[metric.key], moe: metric.moeKey ? row[metric.moeKey] : null,
      available: finite(row[metric.key]) !== null })),
    notes: [model.method, 'ACS MOEs describe sampling uncertainty at 90%; derived rate MOEs use a documented approximation. Different source periods are not simultaneous observations.',
      'Bridge counts retain source record duplicates, sufficiency scores are unweighted, and recorded age is calculated only at the inventory snapshot date.',
      'Traffic count years differ and some are unavailable. Air-quality missingness reflects monitored coverage; no missing county is assigned a clean-air score.'] };
}

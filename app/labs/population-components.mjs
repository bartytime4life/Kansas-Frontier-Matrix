/** Descriptive accounting over the existing public Census Vintage 2025 snapshot. No I/O. */
export const COMPONENT_YEARS = Object.freeze([2021, 2022, 2023, 2024, 2025]);
const METHOD_ID = 'kfm.population-components/v1';
const isRow = value => !!value && typeof value === 'object' && !Array.isArray(value);
const integer = value => typeof value === 'number' && Number.isSafeInteger(value);
const validFips = value => typeof value === 'string' && /^20\d{3}$/.test(value) &&
  Number(value.slice(2)) >= 1 && Number(value.slice(2)) <= 209 && Number(value.slice(2)) % 2 === 1;
const selectionYear = value => integer(value) && value >= 1900 && value <= 2100 ? value : null;
const validName = value => typeof value === 'string' && value.trim().length > 0 && value.length <= 120 && !/[\x00-\x1f\x7f]/.test(value);
const METHOD = Object.freeze({
  id: METHOD_ID,
  description: 'Reconcile the change between two July 1 population estimates with the intervening births, deaths and net migration. The remaining difference is calculated from the retained fields.',
  balanceFormula: 'change = endPopulation − beginPopulation; remainder = change − births + deaths − netMigration',
  rateFormula: 'meanPopulation = (beginPopulation + endPopulation) / 2; normalized contribution = people × 1000 / meanPopulation',
  denominatorLabel: 'Mean of beginning and ending July 1 estimated populations',
  unit: 'people',
  rateUnit: 'people per 1,000 mean estimated residents',
  documentation: [{ title: 'Census Vintage 2025 county file layout and rate definitions', href: 'https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/CO-EST2025-ALLDATA.pdf' }],
  limits: [
    'One fixed Census Population Estimates vintage, not a census count or an individual record. Later vintages may revise earlier estimates.',
    'Component periods run from July 1 of the preceding year through June 30 of the selected year. The endpoints are July 1 population estimates.',
    '2020 components cover a partial year and this snapshot has no 2019 endpoint. Only complete 2021–2025 intervals are reconciled.',
    'The calculated balance remainder is derived from retained fields. It is not an independently captured Census residual, a demographic measurement or a causal explanation.',
    'Net migration is a signed balance, not arrivals or departures. This snapshot does not separate domestic and international migration.',
    'Per-1,000 values are KFM calculated normalizations using the mean of the two population endpoints, not downloaded provider rates. Missing or inconsistent inputs remain unavailable.',
    'Births minus deaths is natural change. It is a subtotal, not an additional contribution to add to births and deaths.',
    'Displayed normalized values may be rounded independently; CSV retains full calculation precision. Rounded displayed contributions can sum slightly differently from a rounded displayed total.',
  ],
});

function emptyBalance(selection) {
  const year = selectionYear(selection?.year), fips = validFips(selection?.fips) ? selection.fips : null;
  const supported = COMPONENT_YEARS.includes(year);
  return {
    status: 'unavailable', reason: null, reasonCode: null, fips, name: null, year,
    beginDate: supported ? `${year - 1}-07-01` : null,
    endDate: supported ? `${year}-07-01` : null,
    componentFrom: supported ? `${year - 1}-07-01` : null,
    componentTo: supported ? `${year}-06-30` : null,
    beginPopulation: null, endPopulation: null, change: null,
    births: null, deaths: null, naturalChange: null, netMigration: null, remainder: null,
    meanPopulation: null, changePer1000: null, naturalChangePer1000: null,
    netMigrationPer1000: null, remainderPer1000: null, contributions: [],
  };
}
const unavailable = (result, reasonCode, reason) => ({ ...result, status: 'unavailable', reasonCode, reason });

/** Values must already have the source schema's types; do not coerce strings or fill gaps. */
export function populationBalance(records, selection = {}) {
  const result = emptyBalance(selection);
  if (!isRow(selection) || !result.fips) return unavailable(result, 'INVALID_FIPS', 'Choose a valid Kansas county FIPS identifier.');
  if (Array.isArray(records)) {
    const names = new Set(records.filter(row => isRow(row) && row.fips === result.fips && validName(row.name)).map(row => row.name));
    if (names.size === 1) result.name = [...names][0];
  }
  if (!COMPONENT_YEARS.includes(result.year)) return unavailable(result, 'UNSUPPORTED_YEAR', 'Choose a complete interval ending in 2021–2025. The 2020 components cover a partial year and lack a preceding endpoint here.');
  if (!Array.isArray(records) || records.some(row => !isRow(row))) return unavailable(result, 'INVALID_RECORDS', 'The county source records are unavailable or malformed.');
  const before = records.filter(row => row.fips === result.fips && row.year === result.year - 1);
  const after = records.filter(row => row.fips === result.fips && row.year === result.year);
  if (before.length > 1 || after.length > 1) return unavailable(result, 'DUPLICATE_ENDPOINT', 'Duplicate county/year records prevent an unambiguous population balance.');
  if (before.length !== 1 || after.length !== 1) return unavailable(result, 'MISSING_ENDPOINT', 'Both July 1 population endpoints and the selected interval’s components are required.');
  const first = before[0], last = after[0];
  if (!validName(last.name)) return unavailable(result, 'INVALID_NAME', 'The selected county record has no usable name.');
  result.name = last.name;
  if (!integer(first.population) || !integer(last.population) || first.population < 0 || last.population < 0) {
    return unavailable(result, 'INVALID_POPULATION', 'Both endpoint populations must be recorded nonnegative integer estimates.');
  }
  if (!['births', 'deaths', 'naturalChange', 'netMigration'].every(key => integer(last[key]))) {
    return unavailable(result, 'INVALID_COMPONENT', 'Births, deaths, natural change and net migration must all have recorded integer values.');
  }
  if (last.births < 0 || last.deaths < 0) return unavailable(result, 'NEGATIVE_COUNT', 'Birth and death counts cannot be negative; signed contributions are calculated separately.');
  if (last.naturalChange !== last.births - last.deaths) return unavailable(result, 'INCONSISTENT_NATURAL_CHANGE', 'Recorded natural change does not equal births minus deaths. The balance is unavailable until the source is reconciled.');
  const beginPopulation = first.population, endPopulation = last.population;
  const meanPopulation = beginPopulation / 2 + endPopulation / 2;
  if (!(meanPopulation > 0) || !Number.isFinite(meanPopulation)) return unavailable(result, 'INVALID_DENOMINATOR', 'The mean of the beginning and ending population estimates must be positive.');
  const change = endPopulation - beginPopulation;
  const afterNaturalChange = change - last.naturalChange;
  const remainder = afterNaturalChange - last.netMigration;
  const signedCounts = [last.births, last.deaths === 0 ? 0 : -last.deaths, last.netMigration, remainder];
  const cumulative = signedCounts.reduce((values, value) => [...values, values.at(-1) + value], [0]);
  if (![change, afterNaturalChange, remainder, ...cumulative].every(integer)) return unavailable(result, 'UNSAFE_ARITHMETIC', 'The balance or an intermediate contribution sum exceeds exact integer arithmetic.');
  const per1000 = people => people / meanPopulation * 1000;
  return {
    ...result, status: 'ready', reason: null, reasonCode: null,
    beginPopulation, endPopulation, change,
    births: last.births, deaths: last.deaths, naturalChange: last.naturalChange,
    netMigration: last.netMigration, remainder, meanPopulation,
    changePer1000: per1000(change), naturalChangePer1000: per1000(last.naturalChange),
    netMigrationPer1000: per1000(last.netMigration), remainderPer1000: per1000(remainder),
    contributions: [
      { key: 'births', label: 'Births', people: last.births },
      { key: 'deaths', label: 'Deaths', people: last.deaths === 0 ? 0 : -last.deaths },
      { key: 'netMigration', label: 'Net migration', people: last.netMigration },
      { key: 'remainder', label: 'Calculated balance remainder', people: remainder },
    ].map(component => ({ ...component, per1000: per1000(component.people) })),
  };
}

const sourceText = value => typeof value === 'string' && value.length <= 500 && !/[\x00-\x1f\x7f]/.test(value) ? value : null;
function publicCapture(value) {
  if (!isRow(value)) return null;
  let url = null;
  try {
    const parsed = new URL(value.url);
    if (parsed.protocol === 'https:' && !parsed.username && !parsed.password && sourceText(value.url)) url = parsed.href;
  } catch { /* An invalid capture URL remains unavailable. */ }
  return {
    url,
    rawBytes: integer(value.rawBytes) && value.rawBytes > 0 ? value.rawBytes : null,
    rawSha256: typeof value.rawSha256 === 'string' && /^[a-f0-9]{64}$/.test(value.rawSha256) ? value.rawSha256 : null,
    retrievedAt: sourceText(value.retrievedAt) && Number.isFinite(Date.parse(value.retrievedAt)) ? value.retrievedAt : null,
    lastModified: sourceText(value.lastModified),
  };
}

/** The third argument is the census-mosaic ENTRY from PUBLIC_LAB_SNAPSHOTS. */
export function populationBalanceReport(bundle, selection = {}, snapshotManifest = {}) {
  const selected = isRow(selection) ? selection : {};
  const settings = { fipsA: validFips(selected.fipsA) ? selected.fipsA : null, fipsB: validFips(selected.fipsB) ? selected.fipsB : null, year: selectionYear(selected.year) };
  const validBundle = isRow(bundle) && bundle.story === 'census-mosaic' && bundle.format === 'kfm-story-bundle-v1' && isRow(bundle.data);
  const manifest = isRow(snapshotManifest) ? snapshotManifest : {};
  const balance = (fips, year) => validBundle ? populationBalance(bundle.data.records, { fips, year }) :
    unavailable(emptyBalance({ fips, year }), 'INVALID_BUNDLE', 'The public Census county snapshot is unavailable.');
  const primaryCapture = validBundle ? publicCapture(bundle.data.sourceSnapshot) : null;
  const source = {
    id: 'census-mosaic', name: 'U.S. Census Population Estimates, Vintage 2025',
    snapshotPath: typeof manifest.path === 'string' && /^\/labs-data\/census-mosaic-[a-f0-9]{16}\.json$/.test(manifest.path) ? manifest.path : null,
    sha256: typeof manifest.sha256 === 'string' && /^[a-f0-9]{64}$/.test(manifest.sha256) ? manifest.sha256 : null,
    bytes: integer(manifest.bytes) && manifest.bytes > 0 ? manifest.bytes : null,
    capturedAt: primaryCapture?.retrievedAt ?? null,
    preparedAt: validBundle && typeof bundle.built_at === 'string' ? bundle.built_at : null,
    observed: validBundle && isRow(bundle.observed) ? { from: bundle.observed.from, to: bundle.observed.to } : null,
    sources: validBundle && Array.isArray(bundle.sources) ? bundle.sources.map(item => ({ ...item })) : [],
    limits: validBundle && Array.isArray(bundle.data.limits) ? [...bundle.data.limits] : [],
    sourceSnapshot: primaryCapture,
    sourceSnapshots: validBundle && Array.isArray(bundle.data.sourceSnapshots) ? bundle.data.sourceSnapshots.map(publicCapture).filter(Boolean) : [],
  };
  return {
    schema: METHOD_ID, source,
    method: { ...METHOD, documentation: METHOD.documentation.map(item => ({ ...item })), limits: [...METHOD.limits] },
    selection: settings,
    countyA: balance(settings.fipsA, settings.year), countyB: balance(settings.fipsB, settings.year),
    history: {
      a: COMPONENT_YEARS.map(year => balance(settings.fipsA, year)),
      b: COMPONENT_YEARS.map(year => balance(settings.fipsB, year)),
    },
  };
}

const csvText = value => typeof value === 'string' && /^[=+@\-\t\r\n]/.test(value) ? "'" + value : value ?? '';
/** Tidy interval rows retain both histories, units, dates and the exact public snapshot identity. */
export function populationBalanceCsv(report) {
  if (!isRow(report) || report.schema !== METHOD_ID || !isRow(report.history) ||
      !Array.isArray(report.history.a) || !Array.isArray(report.history.b)) throw new Error('Population balance report unavailable.');
  const header = ['county_slot', 'county_fips', 'county_name', 'year', 'selected_year', 'selected_interval', 'status', 'reason_code', 'reason',
    'population_begin_date', 'population_end_date', 'components_from', 'components_to',
    'begin_population_people', 'end_population_people', 'change_people', 'births_people', 'deaths_people', 'deaths_contribution_people',
    'natural_change_people', 'net_migration_people', 'calculated_balance_remainder_people', 'mean_estimated_residents',
    'change_per_1000_mean_residents', 'births_per_1000_mean_residents', 'deaths_contribution_per_1000_mean_residents',
    'natural_change_per_1000_mean_residents', 'net_migration_per_1000_mean_residents', 'remainder_per_1000_mean_residents',
    'normalization_denominator', 'people_unit', 'normalized_unit', 'source_snapshot_path', 'source_snapshot_sha256', 'source_snapshot_bytes',
    'source_captured_at', 'public_snapshot_prepared_at', 'method_id', 'source_urls', 'raw_source_url', 'raw_source_sha256', 'raw_source_bytes',
    'raw_source_retrieved_at', 'raw_source_last_modified', 'raw_source_snapshots_json'];
  const rows = ['a', 'b'].flatMap(slot => report.history[slot].map(balance => {
    const component = key => balance.contributions.find(item => item.key === key);
    return [slot.toUpperCase(), balance.fips, balance.name, balance.year, report.selection.year, balance.year === report.selection.year,
      balance.status, balance.reasonCode, balance.reason, balance.beginDate, balance.endDate, balance.componentFrom, balance.componentTo,
      balance.beginPopulation, balance.endPopulation, balance.change, balance.births, balance.deaths, component('deaths')?.people,
      balance.naturalChange, balance.netMigration, balance.remainder, balance.meanPopulation,
      balance.changePer1000, component('births')?.per1000, component('deaths')?.per1000, balance.naturalChangePer1000,
      balance.netMigrationPer1000, balance.remainderPer1000, report.method.denominatorLabel, report.method.unit, report.method.rateUnit,
      report.source.snapshotPath, report.source.sha256, report.source.bytes, report.source.capturedAt, report.source.preparedAt, report.method.id,
      report.source.sources.map(item => item.url).join(' | '), report.source.sourceSnapshot?.url, report.source.sourceSnapshot?.rawSha256,
      report.source.sourceSnapshot?.rawBytes, report.source.sourceSnapshot?.retrievedAt, report.source.sourceSnapshot?.lastModified,
      JSON.stringify(report.source.sourceSnapshots)].map(csvText);
  }));
  return [header, ...rows];
}

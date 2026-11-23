// Builds the small table the county landing pages read (app/county-facts.generated.json) from three bundles
// the labs already ship: Census survey estimates, Census population estimates and the KDOT bridge inventory.
// No network: the bundles are in public/.
// Run after scripts/prepare-labs-county-data.py changes the bundle: node scripts/prepare-county-pages.mjs
import { readFile, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { COUNTY_LAB_SNAPSHOTS } from '../app/labs/county-snapshots.mjs';
import { BASE_LAB_SNAPSHOTS } from '../app/labs/base-snapshots.mjs';
import { BRIDGE_LAB_SNAPSHOTS } from '../app/labs/bridge-snapshots.mjs';
import { KANSAS_COUNTIES } from '../app/labs/county-model.mjs';

const round = (value, places) => typeof value === 'number' && Number.isFinite(value) ? Math.round(value * 10 ** places) / 10 ** places : null;
// Preserve the bundle's precision for comparisons. The page rounds for display.
function pair(record, key) {
  const value = record[key], margin = record[`${key}Moe`];
  if (!Number.isFinite(value) || !Number.isFinite(margin) || margin < 0) {
    throw new Error(`COUNTY_ESTIMATE_INCOMPLETE ${record.fips} ${record.year} ${key}`);
  }
  return [value, margin];
}
export const countySlug = name => name.replace(/\s+County$/, '').toLowerCase().replace(/[^a-z]+/g, '-').replace(/^-|-$/g, '');

function center(geometry) {
  const rings = geometry.type === 'Polygon' ? geometry.coordinates : geometry.coordinates.flat();
  let west = Infinity, south = Infinity, east = -Infinity, north = -Infinity;
  for (const ring of rings) for (const [lon, lat] of ring) { west = Math.min(west, lon); east = Math.max(east, lon); south = Math.min(south, lat); north = Math.max(north, lat); }
  return [round((west + east) / 2, 3), round((south + north) / 2, 3)];
}

const CLOSED = new Set(['Closed to all traffic', 'Closed']);
const ON_REGISTER = 'Br on Natl Reg Hist Place';

// July 1 population estimates: the newest year beside the first year of the same vintage.
function populations(bundle) {
  const records = bundle.data.records, years = [...new Set(records.map(record => record.year))].sort((a, b) => a - b);
  const year = years.at(-1), baseYear = years[0], byFips = new Map();
  for (const record of records) {
    if (record.year !== year && record.year !== baseYear) continue;
    const entry = byFips.get(record.fips) ?? {};
    entry[record.year === year ? 'value' : 'baseValue'] = record.population;
    byFips.set(record.fips, entry);
  }
  return fips => {
    const entry = byFips.get(fips);
    if (!entry || !Number.isInteger(entry.value) || !Number.isInteger(entry.baseValue)) throw new Error(`COUNTY_POPULATION_INCOMPLETE ${fips}`);
    return { year, value: entry.value, baseYear, baseValue: entry.baseValue };
  };
}

// The KDOT inventory names a county in capitals for state highways and in title case for local roads.
function bridges(bundle) {
  const byName = new Map();
  for (const record of bundle.data.records) {
    const key = String(record.county ?? '').trim().toLowerCase();
    const entry = byName.get(key) ?? { records: 0, state: 0, local: 0, closed: 0, register: 0, oldestYear: null, longestFt: null };
    entry.records += 1;
    if (record.network === 'State highway') entry.state += 1; else if (record.network === 'Local road') entry.local += 1;
    if (CLOSED.has(record.status)) entry.closed += 1;
    if (record.historic === ON_REGISTER) entry.register += 1;
    if (Number.isInteger(record.year) && (entry.oldestYear === null || record.year < entry.oldestYear)) entry.oldestYear = record.year;
    if (typeof record.length === 'number' && Number.isFinite(record.length) && (entry.longestFt === null || record.length > entry.longestFt)) entry.longestFt = record.length;
    byName.set(key, entry);
  }
  const used = new Set();
  const read = name => {
    const key = name.replace(/\s+County$/, '').toLowerCase(), entry = byName.get(key);
    if (!entry || entry.state + entry.local !== entry.records) throw new Error(`COUNTY_BRIDGES_INCOMPLETE ${name}`);
    used.add(key);
    return { ...entry, longestFt: round(entry.longestFt, 0) };
  };
  // Every inventory record must belong to one of the 105 counties, or the totals would silently drop some.
  read.complete = () => { if (used.size !== byName.size) throw new Error('COUNTY_BRIDGES_UNMATCHED'); };
  return read;
}

export function buildCountyFacts(bundle, populationBundle, bridgeBundle, snapshot = COUNTY_LAB_SNAPSHOTS['county-conditions']) {
  const population = populations(populationBundle), bridgeCounts = bridges(bridgeBundle);
  const records = bundle.data.records;
  const years = [...new Set(records.map(record => record.year))].sort((a, b) => a - b);
  const latestYear = years.at(-1), earlierYear = years[0];
  const counties = KANSAS_COUNTIES.map(({ fips, name }) => {
    const latest = records.find(record => record.fips === fips && record.year === latestYear);
    const earlier = records.find(record => record.fips === fips && record.year === earlierYear);
    if (!latest || !earlier || latest.name !== name) throw new Error(`COUNTY_FACTS_INCOMPLETE ${fips}`);
    return {
      fips, name, slug: countySlug(name), center: center(latest.geometry), population: population(fips), bridges: bridgeCounts(name),
      latest: {
        period: latest.period, medianIncome: pair(latest, 'medianIncome'), medianAge: pair(latest, 'medianAge'),
        medianHomeValue: pair(latest, 'medianHomeValue'), medianRent: pair(latest, 'medianRent'),
        educationPct: pair(latest, 'educationPct'), povertyPct: pair(latest, 'povertyPct'),
        ownerOccupiedPct: pair(latest, 'ownerOccupiedPct'), housingUnits: pair(latest, 'housingUnits'),
      },
      earlier: {
        period: earlier.period, medianAge: pair(earlier, 'medianAge'), educationPct: pair(earlier, 'educationPct'),
        povertyPct: pair(earlier, 'povertyPct'), housingUnits: pair(earlier, 'housingUnits'),
      },
    };
  });
  if (new Set(counties.map(county => county.slug)).size !== counties.length) throw new Error('COUNTY_SLUG_COLLISION');
  bridgeCounts.complete();
  const populationSnapshot = BASE_LAB_SNAPSHOTS['census-mosaic'], bridgeSnapshot = BRIDGE_LAB_SNAPSHOTS['built-kansas'];
  return {
    source: { path: snapshot.path, sha256: snapshot.sha256, retrievedAt: snapshot.retrievedAt },
    sources: {
      population: { path: populationSnapshot.path, sha256: populationSnapshot.sha256 },
      bridges: { path: bridgeSnapshot.path, sha256: bridgeSnapshot.sha256, inventoryAsOf: bridgeBundle.data.inventoryAsOf },
    },
    counties,
  };
}

const bundle = async (root, path) => JSON.parse(await readFile(resolve(root, 'public', path.replace(/^\//, '')), 'utf8'));
export const readCountyBundle = (root = process.cwd()) => bundle(root, COUNTY_LAB_SNAPSHOTS['county-conditions'].path);
export const readPopulationBundle = (root = process.cwd()) => bundle(root, BASE_LAB_SNAPSHOTS['census-mosaic'].path);
export const readBridgeBundle = (root = process.cwd()) => bundle(root, BRIDGE_LAB_SNAPSHOTS['built-kansas'].path);

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const facts = buildCountyFacts(await readCountyBundle(), await readPopulationBundle(), await readBridgeBundle());
  await writeFile('app/county-facts.generated.json', JSON.stringify(facts, null, 1) + '\n');
  console.log(`County facts: ${facts.counties.length} counties from ${facts.source.path}`);
}

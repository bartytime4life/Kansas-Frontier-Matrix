// Builds the small table the county landing pages read (app/county-facts.generated.json) from the
// Census county bundle the County Conditions lab already ships. No network: the bundle is in public/.
// Run after scripts/prepare-labs-county-data.py changes the bundle: node scripts/prepare-county-pages.mjs
import { readFile, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { COUNTY_LAB_SNAPSHOTS } from '../app/labs/county-snapshots.mjs';
import { KANSAS_COUNTIES } from '../app/labs/county-model.mjs';

const round = (value, places) => typeof value === 'number' && Number.isFinite(value) ? Math.round(value * 10 ** places) / 10 ** places : null;
// Estimate and its published or derived 90% margin of error, as [value, margin].
const pair = (record, key, places) => [round(record[key], places), round(record[`${key}Moe`], places)];
export const countySlug = name => name.replace(/\s+County$/, '').toLowerCase().replace(/[^a-z]+/g, '-').replace(/^-|-$/g, '');

function center(geometry) {
  const rings = geometry.type === 'Polygon' ? geometry.coordinates : geometry.coordinates.flat();
  let west = Infinity, south = Infinity, east = -Infinity, north = -Infinity;
  for (const ring of rings) for (const [lon, lat] of ring) { west = Math.min(west, lon); east = Math.max(east, lon); south = Math.min(south, lat); north = Math.max(north, lat); }
  return [round((west + east) / 2, 3), round((south + north) / 2, 3)];
}

export function buildCountyFacts(bundle, snapshot = COUNTY_LAB_SNAPSHOTS['county-conditions']) {
  const records = bundle.data.records;
  const years = [...new Set(records.map(record => record.year))].sort((a, b) => a - b);
  const latestYear = years.at(-1), earlierYear = years[0];
  const counties = KANSAS_COUNTIES.map(({ fips, name }) => {
    const latest = records.find(record => record.fips === fips && record.year === latestYear);
    const earlier = records.find(record => record.fips === fips && record.year === earlierYear);
    if (!latest || !earlier || latest.name !== name) throw new Error(`COUNTY_FACTS_INCOMPLETE ${fips}`);
    return {
      fips, name, slug: countySlug(name), center: center(latest.geometry),
      latest: {
        period: latest.period, medianIncome: pair(latest, 'medianIncome', 0), medianAge: pair(latest, 'medianAge', 1),
        medianHomeValue: pair(latest, 'medianHomeValue', 0), medianRent: pair(latest, 'medianRent', 0),
        educationPct: pair(latest, 'educationPct', 1), povertyPct: pair(latest, 'povertyPct', 1),
        ownerOccupiedPct: pair(latest, 'ownerOccupiedPct', 1), housingUnits: pair(latest, 'housingUnits', 0),
      },
      earlier: { period: earlier.period, medianAge: round(earlier.medianAge, 1), educationPct: round(earlier.educationPct, 1), povertyPct: round(earlier.povertyPct, 1), housingUnits: round(earlier.housingUnits, 0) },
    };
  });
  if (new Set(counties.map(county => county.slug)).size !== counties.length) throw new Error('COUNTY_SLUG_COLLISION');
  return { source: { path: snapshot.path, sha256: snapshot.sha256, retrievedAt: snapshot.retrievedAt }, counties };
}

export async function readCountyBundle(root = process.cwd()) {
  return JSON.parse(await readFile(resolve(root, 'public', COUNTY_LAB_SNAPSHOTS['county-conditions'].path.replace(/^\//, '')), 'utf8'));
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const facts = buildCountyFacts(await readCountyBundle());
  await writeFile('app/county-facts.generated.json', JSON.stringify(facts, null, 1) + '\n');
  console.log(`County facts: ${facts.counties.length} counties from ${facts.source.path}`);
}

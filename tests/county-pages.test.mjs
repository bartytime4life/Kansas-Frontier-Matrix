import test from 'node:test';
import assert from 'node:assert/strict';
import { access, readFile } from 'node:fs/promises';
import ts from 'typescript';
import { buildCountyFacts, countySlug, readBridgeBundle, readCountyBundle, readPopulationBundle } from '../scripts/prepare-county-pages.mjs';

const compile = async (path, modules = {}) => { const exports = {}; new Function('exports', 'require', ts.transpileModule(await readFile(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, esModuleInterop: true } }).outputText)(exports, name => { if (name in modules) return modules[name]; throw new Error(`Unexpected import: ${name}`); }); return exports; };
const facts = JSON.parse(await readFile('app/county-facts.generated.json', 'utf8'));
const pages = await compile('app/county-pages.ts', { './county-facts.generated.json': { __esModule: true, default: facts } });

test('the county table is exactly what the generator makes from the shipped bundles', async () => {
  assert.deepEqual(facts, JSON.parse(JSON.stringify(buildCountyFacts(await readCountyBundle(), await readPopulationBundle(), await readBridgeBundle()))), 'run node scripts/prepare-county-pages.mjs after a bundle changes');
  assert.match(facts.source.path, /^\/labs-data-observatory\/county-conditions-[a-f0-9]{16}\.json$/);
  assert.match(facts.sources.population.path, /^\/labs-data\/census-mosaic-[a-f0-9]{16}\.json$/);
  assert.match(facts.sources.bridges.path, /^\/labs-data-bridges\/built-kansas-[a-f0-9]{16}\.json$/);
  assert.match(facts.sources.bridges.inventoryAsOf, /^\d{4}-\d{2}-\d{2}$/);
});

test('all 105 counties have a page address, a place on the map and complete estimates', () => {
  assert.equal(pages.COUNTY_PAGES.length, 105);
  assert.equal(new Set(pages.COUNTY_PAGES.map(county => county.slug)).size, 105);
  assert.equal(new Set(pages.COUNTY_PAGES.map(county => county.fips)).size, 105);
  for (const county of pages.COUNTY_PAGES) {
    assert.match(county.slug, /^[a-z]+(?:-[a-z]+)*$/, county.name);
    assert.equal(county.slug, countySlug(county.name));
    assert.match(county.fips, /^20\d{3}$/); assert.match(county.name, / County$/);
    const [lon, lat] = county.center;
    assert.ok(lon > -102.06 && lon < -94.58 && lat > 36.99 && lat < 40.01, `${county.name} is inside Kansas`);
    assert.equal(county.latest.period, '2020–2024'); assert.equal(county.earlier.period, '2010–2014');
    for (const key of ['medianIncome', 'medianAge', 'medianHomeValue', 'medianRent', 'educationPct', 'povertyPct', 'ownerOccupiedPct', 'housingUnits']) {
      const [value, margin] = county.latest[key];
      assert.ok(Number.isFinite(value) && value > 0 && Number.isFinite(margin) && margin >= 0, `${county.name} ${key}`);
    }
    for (const key of ['medianAge', 'educationPct', 'povertyPct', 'housingUnits']) {
      const [value, margin] = county.earlier[key];
      assert.ok(Number.isFinite(value) && value > 0 && Number.isFinite(margin) && margin >= 0, `${county.name} earlier ${key}`);
    }
    assert.equal(pages.countyPage(county.slug), county);
    assert.equal(new URL(pages.countyObservatoryHref(county), 'https://example.test').searchParams.get('county'), county.fips);
  }
  assert.equal(pages.countyPage('nowhere'), undefined); assert.equal(pages.countyPage('Allen'), undefined);
  const sedgwick = pages.countyPage('sedgwick');
  assert.equal(sedgwick.fips, '20173'); assert.equal(pages.countyPath(sedgwick), '/counties/sedgwick');
  assert.match(pages.countyMapHref(sedgwick), /^\/\?ctx=census-counties&c=-97\.\d+,37\.\d+&z=8\.5$/);
});

test('county change labels use both margins at 90% confidence and retain the input precision', () => {
  assert.equal(pages.dollars([69365, 1409]), '$69,365 (±$1,409)');
  assert.equal(pages.percent([13.9, 0.8]), '13.9% (±0.8)');
  assert.equal(pages.years([36, 0.2]), '36.0 years (±0.2)');
  assert.equal(pages.count([227638, 171]), '227,638 (±171)');
  const period = '2020–2024';
  assert.equal(pages.comparedWith([13.9, 0.8], [15.1, 0.7], period), 'Lower in 2020–2024');
  assert.equal(pages.comparedWith([32.1, 0.7], [29.4, 1.8], period), 'Higher in 2020–2024');
  assert.equal(pages.comparedWith([32.1, 0.7], [29.4, 3.0], period), 'Difference uncertain');
  assert.equal(pages.comparedWith([12, 3], [7, 4], period), 'Difference uncertain', 'exactly the combined margin');
  assert.equal(pages.comparedWith([12.001, 3], [7, 4], period), 'Higher in 2020–2024');

  const anderson = pages.countyPage('anderson');
  assert.equal(pages.comparedWith(anderson.latest.educationPct, anderson.earlier.educationPct, period), 'Difference uncertain');
  assert.equal(pages.percent(anderson.earlier.educationPct), '17.5% (±3.3)');
});

test('the pages say where the numbers come from and never compare dollars across periods', async () => {
  const page = await readFile('app/counties/county-page.tsx', 'utf8');
  assert.match(page, /alternates: \{ canonical: url \}/);
  assert.match(page, /American Community Survey 5-year estimates/); assert.match(page, /90% margin of error/);
  assert.match(page, /Dollar amounts use each period/);
  assert.match(page, /countyObservatoryHref\(county\)/);
  for (const dollarsField of ['medianIncome', 'medianHomeValue', 'medianRent']) assert.ok(!new RegExp(`comparedWith\\(latest\\.${dollarsField}`).test(page), dollarsField);
  assert.ok(!facts.counties.some(county => 'medianIncome' in county.earlier || 'medianHomeValue' in county.earlier || 'medianRent' in county.earlier), 'earlier dollar amounts are not even carried');
  assert.match(page, /not Kansas Frontier Matrix evidence/);
  const route = await readFile('app/counties/[slug]/page.tsx', 'utf8');
  assert.match(route, /export function generateStaticParams\(\) \{ return COUNTY_PAGES\.map\(county => \(\{ slug: county\.slug \}\)\); \}/);
  assert.match(route, /countyMetadata\(\(await params\)\.slug\)/);
  const index = await readFile('app/counties/page.tsx', 'utf8');
  assert.match(index, /canonical: `\$\{PUBLIC_SITE_ORIGIN\}\/counties`/);
});

test('the sitemap lists every county and the public reading pages that were missing, and nothing robots.txt disallows', async () => {
  const guides = [{ slug: 'kansas-bridges' }, { slug: 'frontier-trails' }];
  const discovery = await compile('app/crawler-discovery.ts', { './county-pages': pages, './landing-guides': { LANDING_GUIDES: guides } });
  const locs = [...discovery.SITEMAP_XML.matchAll(/<loc>([^<]+)<\/loc>/g)].map(match => match[1].replace(discovery.PUBLIC_SITE_ORIGIN, ''));
  assert.equal(locs.length, 4 + guides.length + 1 + 105 + discovery.PUBLIC_PAGES.length);
  assert.equal(new Set(locs).size, locs.length, 'no address twice');
  assert.ok(locs.includes('/counties')); assert.ok(locs.includes('/counties/sedgwick')); assert.ok(locs.includes('/counties/wyandotte'));
  const disallowed = [...discovery.ROBOTS_TEXT.matchAll(/^Disallow: (\/[a-z/-]+)$/gm)].map(match => match[1]);
  assert.ok(disallowed.includes('/acquisition'));
  for (const path of locs) assert.ok(!disallowed.some(prefix => path === prefix || path.startsWith(prefix.endsWith('/') ? prefix : prefix + '/')), path);
  for (const path of discovery.PUBLIC_PAGES) {
    const found = await Promise.any([access(`app${path}/page.tsx`), access(`app${path}/page.jsx`)]).then(() => true, () => false);
    assert.ok(found, `${path} is a page in this application`);
  }
  assert.ok(!discovery.PUBLIC_PAGES.includes('/knowledge'), 'the Knowledge search is left out while its store is not provisioned');
});

test('population is two Census estimates side by side, and every bridge inventory record is counted in one county', async () => {
  const bridgeBundle = await readBridgeBundle();
  assert.equal(pages.COUNTY_PAGES.reduce((sum, county) => sum + county.bridges.records, 0), bridgeBundle.data.records.length, 'no inventory record is dropped or counted twice');
  for (const county of pages.COUNTY_PAGES) {
    const { population, bridges } = county;
    assert.ok(population.year > population.baseYear && Number.isInteger(population.value) && population.value > 0 && Number.isInteger(population.baseValue) && population.baseValue > 0, county.name);
    assert.equal(bridges.state + bridges.local, bridges.records, county.name);
    assert.ok(bridges.records > 0 && bridges.closed <= bridges.records && bridges.register <= bridges.local, county.name);
    assert.ok(bridges.oldestYear === null || bridges.oldestYear >= 1850 && bridges.oldestYear <= 2026, county.name);
    assert.ok(bridges.longestFt === null || bridges.longestFt > 0, county.name);
  }
  // The inventory names Sedgwick County in capitals for state highways and in title case for local roads.
  const sedgwick = pages.countyPage('sedgwick');
  const named = bridgeBundle.data.records.filter(record => String(record.county).toLowerCase() === 'sedgwick');
  assert.ok(named.some(record => record.county === 'SEDGWICK') && named.some(record => record.county === 'Sedgwick'));
  assert.equal(sedgwick.bridges.records, named.length);
  assert.equal(sedgwick.bridges.closed, named.filter(record => record.status === 'Closed to all traffic' || record.status === 'Closed').length);
  assert.match(pages.countyBridgesHref(sedgwick), /^\/\?ctx=census-counties,kdot-bridges-state,kdot-bridges-local&c=-97\.\d+,37\.\d+&z=9\.5$/);
  assert.deepEqual(pages.populationChange({ year: 2025, value: 538433, baseYear: 2020, baseValue: 524831 }), ['13,602 more than', 'up 2.6%']);
  assert.deepEqual(pages.populationChange({ year: 2025, value: 12302, baseYear: 2020, baseValue: 12533 }), ['231 fewer than', 'down 1.8%']);
  assert.deepEqual(pages.populationChange({ year: 2025, value: 5000, baseYear: 2020, baseValue: 5000 }), ['the same as', null]);
  assert.deepEqual(pages.populationChange({ year: 2025, value: 500001, baseYear: 2020, baseValue: 500000 }), ['1 more than', 'up less than 0.1%']);
  const page = await readFile('app/counties/county-page.tsx', 'utf8');
  assert.match(page, /These are inventory records, which are not always one physical bridge each\./);
  assert.match(page, /not a current safety assessment or permission to enter a structure/);
  assert.match(page, /A later release can revise earlier years, and the page gives the two estimates without saying why they differ\./);
  assert.match(page, /Inventory as of \{COUNTY_FACTS_SOURCES\.bridges\.inventoryAsOf\}/);
});

import test from 'node:test';
import assert from 'node:assert/strict';
import { access, readFile } from 'node:fs/promises';
import ts from 'typescript';
import { buildCountyFacts, countySlug, readCountyBundle } from '../scripts/prepare-county-pages.mjs';

const compile = async (path, modules = {}) => { const exports = {}; new Function('exports', 'require', ts.transpileModule(await readFile(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, esModuleInterop: true } }).outputText)(exports, name => { if (name in modules) return modules[name]; throw new Error(`Unexpected import: ${name}`); }); return exports; };
const facts = JSON.parse(await readFile('app/county-facts.generated.json', 'utf8'));
const pages = await compile('app/county-pages.ts', { './county-facts.generated.json': { __esModule: true, default: facts } });

test('the county table is exactly what the generator makes from the shipped Census bundle', async () => {
  assert.deepEqual(facts, JSON.parse(JSON.stringify(buildCountyFacts(await readCountyBundle()))), 'run node scripts/prepare-county-pages.mjs after the bundle changes');
  assert.match(facts.source.path, /^\/labs-data-observatory\/county-conditions-[a-f0-9]{16}\.json$/);
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
    assert.equal(pages.countyPage(county.slug), county);
  }
  assert.equal(pages.countyPage('nowhere'), undefined); assert.equal(pages.countyPage('Allen'), undefined);
  const sedgwick = pages.countyPage('sedgwick');
  assert.equal(sedgwick.fips, '20173'); assert.equal(pages.countyPath(sedgwick), '/counties/sedgwick');
  assert.match(pages.countyMapHref(sedgwick), /^\/\?ctx=census-counties&c=-97\.\d+,37\.\d+&z=8\.5$/);
});

test('figures carry their margin of error, and a change is named only when it is larger than that margin', () => {
  assert.equal(pages.dollars([69365, 1409]), '$69,365 (±$1,409)');
  assert.equal(pages.percent([13.9, 0.8]), '13.9% (±0.8)');
  assert.equal(pages.years([36, 0.2]), '36.0 years (±0.2)');
  assert.equal(pages.count([227638, 171]), '227,638 (±171)');
  assert.equal(pages.comparedWith([13.9, 0.8], 15.1, '%'), 'down from 15.1%');
  assert.equal(pages.comparedWith([32.1, 0.7], 29.4, '%'), 'up from 29.4%');
  assert.equal(pages.comparedWith([41.2, 0.6], 41.3, ' years'), 'about the same as 41.3 years');
  assert.equal(pages.comparedWith([9.9, 2.3], 12.2, '%'), 'about the same as 12.2%', 'a difference equal to the margin is not a change');
});

test('the pages say where the numbers come from and never compare dollars across periods', async () => {
  const page = await readFile('app/counties/county-page.tsx', 'utf8');
  assert.match(page, /alternates: \{ canonical: url \}/);
  assert.match(page, /American Community Survey 5-year estimates/); assert.match(page, /90% margins of error/);
  assert.match(page, /not adjusted for inflation, so this page does not compare them across periods/);
  for (const dollarsField of ['medianIncome', 'medianHomeValue', 'medianRent']) assert.ok(!new RegExp(`comparedWith\\(latest\\.${dollarsField}`).test(page), dollarsField);
  assert.ok(!facts.counties.some(county => 'medianIncome' in county.earlier || 'medianHomeValue' in county.earlier || 'medianRent' in county.earlier), 'earlier dollar amounts are not even carried');
  assert.match(page, /not Kansas Frontier Matrix evidence/);
  const route = await readFile('app/counties/[slug]/page.tsx', 'utf8');
  assert.match(route, /export function generateStaticParams\(\) \{ return COUNTY_PAGES\.map\(county => \(\{ slug: county\.slug \}\)\); \}/);
  assert.match(route, /countyMetadata\(\(await params\)\.slug\)/);
  const index = await readFile('app/counties/page.tsx', 'utf8');
  assert.match(index, /canonical: `\$\{PUBLIC_SITE_ORIGIN\}\/counties`/); assert.match(index, /COUNTY_PAGES\.map\(county => <li key=\{county\.fips\}><Link href=\{countyPath\(county\)\}>/);
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

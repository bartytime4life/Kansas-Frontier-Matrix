import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { buildKansasRecords, readRecordBundles } from '../scripts/prepare-kansas-records.mjs';

const generated = JSON.parse(await readFile('app/kansas-records.generated.json', 'utf8'));
const bundles = await readRecordBundles();
const section = id => generated.sections.find(entry => entry.id === id);
const item = (id, label) => section(id).items.find(entry => entry.label === label);

test('the records table is exactly what the generator makes from the shipped bundles', () => {
  assert.deepEqual(generated, JSON.parse(JSON.stringify(buildKansasRecords(bundles))), 'run node scripts/prepare-kansas-records.mjs after a bundle changes');
  assert.deepEqual(generated.sections.map(entry => entry.id), ['people', 'survey', 'bridges', 'tornadoes']);
  for (const entry of generated.sections) {
    assert.ok(entry.source.length > 20 && entry.caution.length > 20, `${entry.id} names its source and a limit`);
    for (const record of entry.items) {
      assert.ok(record.label && record.value && record.where, `${entry.id}: ${record.label}`);
      if (record.href) assert.match(record.href, /^\/counties\/[a-z]+(?:-[a-z]+)*$|^\/\?ctx=kdot-bridges-state,kdot-bridges-local&c=-\d+\.\d+,\d+\.\d+&z=14$/);
    }
  }
});

test('each record is the true extreme of its dataset, checked against the bundle directly', () => {
  const people = bundles.population.data.records.filter(record => record.year === 2025);
  const most = people.reduce((a, b) => b.population > a.population ? b : a), fewest = people.reduce((a, b) => b.population < a.population ? b : a);
  assert.equal(item('people', 'Most people').where, `${most.name}, Kansas`);
  assert.equal(item('people', 'Most people').value, most.population.toLocaleString('en-US'));
  assert.equal(item('people', 'Fewest people').where, `${fewest.name}, Kansas`);

  const tracks = bundles.tornadoes.data.records;
  assert.equal(item('tornadoes', 'Tornadoes in the record').value, tracks.length.toLocaleString('en-US'));
  assert.equal(item('tornadoes', 'Longest path').value, `${Math.max(...tracks.map(track => track.length ?? 0)).toFixed(1)} miles`);
  assert.equal(item('tornadoes', 'Most reported deaths').value, `${Math.max(...tracks.map(track => track.fatalities ?? 0))} deaths`);
  assert.equal(item('tornadoes', 'Rated F5 or EF5').value, `${tracks.filter(track => track.rating === 'F/EF5').length} tornadoes`);
  assert.match(item('tornadoes', 'Most reported deaths').note, /whole track, which can extend outside Kansas/);

  const inventory = bundles.bridges.data.records;
  assert.equal(item('bridges', 'Oldest recorded built year').value, String(Math.min(...inventory.filter(record => Number.isInteger(record.year)).map(record => record.year))));
  assert.equal(item('bridges', 'Longest structure').value, `${Math.round(Math.max(...inventory.map(record => record.length ?? 0))).toLocaleString('en-US')} feet`);
  assert.match(item('bridges', 'Longest structure').where, /^Recorded as “[^”]+” over “[^”]+”, [A-Z][a-z]+(?: [A-Z][a-z]+)* County$/, 'the inventory wording is quoted, not tidied');

  const survey = bundles.conditions.data.records.filter(record => record.year === 2024);
  const richest = survey.reduce((a, b) => b.medianIncome > a.medianIncome ? b : a);
  assert.equal(item('survey', 'Highest median household income').where, `${richest.name}, Kansas`);
  assert.match(item('survey', 'Highest median household income').value, /^\$[\d,]+ \(±\$[\d,]+\)$/, 'a survey estimate carries its margin of error');
});

test('a tie is reported as a tie, and a missing value is never treated as a record', () => {
  const tied = structuredClone(bundles);
  const rows = tied.population.data.records.filter(record => record.year === 2025);
  const top = Math.max(...rows.map(record => record.population));
  rows.find(record => record.name === 'Allen County').population = top;
  const people = buildKansasRecords(tied).sections.find(entry => entry.id === 'people').items.find(entry => entry.label === 'Most people');
  assert.equal(people.where, 'Allen County, Kansas'); assert.match(people.note, /^Shared by 2 counties; the first alphabetically is shown\.$/);
  const undated = structuredClone(bundles);
  for (const record of undated.bridges.data.records) if (record.year === 1870) record.year = null;
  assert.notEqual(buildKansasRecords(undated).sections.find(entry => entry.id === 'bridges').items[0].value, 'null');
  const short = structuredClone(bundles); short.population.data.records = short.population.data.records.filter(record => record.fips !== '20001');
  assert.throws(() => buildKansasRecords(short), /KANSAS_RECORDS_POPULATION_INCOMPLETE/);
});

test('the page states what a record here is, links each group to its source and limits, and is in the sitemap', async () => {
  const page = await readFile('app/records/page.tsx', 'utf8');
  assert.match(page, /alternates: \{ canonical: url \}/);
  assert.match(page, /It is a record of that dataset, for the years it covers, and nothing more/);
  assert.match(page, /Source: \{section\.source\}\. \{section\.caution\}/);
  assert.match(page, /not Kansas Frontier Matrix evidence/);
  assert.match(await readFile('app/crawler-discovery.ts', 'utf8'), /PUBLIC_PAGES = Object\.freeze\(\["\/records", /);
  assert.match(await readFile('app/counties/page.tsx', 'utf8'), /<Link href="\/records">/);
  assert.match(await readFile('app/explore/page.tsx', 'utf8'), /<Link href="\/records">/);
});

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { historyCsvCell, historyResearchCsv } from '../scripts/export-history-research.mjs';

const data = JSON.parse(await readFile('public/history/people-events.json', 'utf8'));
const supplied = [
  'https://www.ffa.org/ffa-history/',
  'https://www.ksnt.com/news/top-stories/famous-actors-from-kansas/',
  'https://kansasreflector.com/2023/10/08/voices-on-the-wind-the-uncomfortable-history-of-kansas-and-first-peoples-of-the-plains/',
  'https://www.history.com/articles/kansas',
  'https://www.onthisday.com/countries/usa/kansas',
  'http://www.kansashistory.us/',
  'https://ksoralhistory.org/collections/notable-kansans-2/',
  'https://en.wikipedia.org/wiki/List_of_people_from_Kansas',
  'https://www.findagrave.com/geographic/4?state=18',
  'https://www.ebsco.com/research-starters/history/history-kansas/',
  'https://indiansinkansashistory.com/',
  'https://www.ranker.com/list/famous-people-from-kansas/reference',
  'https://www.travelks.com/things-to-do/history-and-culture/famous-kansans/',
  'https://www.kansashistory.gov/kansapedia/notable-kansans/16875',
  'https://legendsofkansas.com/historic-people-of-kansas/',
];

test('supplied URLs remain exact and recovered index counts match observed coverage', () => {
  assert.deepEqual(data.sources.map(source => source.url), supplied);
  assert.equal(data.records.length, 2886);
  assert.ok(data.sources.every(source => source.access === 'readable'));
  for (const source of data.sources.filter(source => source.access === 'blocked')) {
    assert.equal(source.recordCount, 0);
    assert.ok(!data.records.some(record => record.sourceId === source.id));
  }
  const ranker = data.sources.find(source => source.id === 'ranker');
  assert.equal(ranker.access, 'readable');
  assert.equal(ranker.recordCount, 583);
  assert.equal(ranker.provenance.completeness.publisherDeclaredTotal, 583);
  assert.deepEqual(ranker.provenance.completeness.recordsPerPage, [120, 120, 120, 120, 103]);
  assert.equal(data.records.filter(record => record.sourceId === 'ksnt').length, 25);
  const memorials = data.records.filter(record => record.sourceId === 'findagrave');
  assert.equal(memorials.length, 405);
  assert.equal(new Set(memorials.map(record => record.targetUrl)).size, 405);
  assert.deepEqual(memorials.filter(record => record.kind === 'topic').map(record => record.title).sort(), ['Chief', 'Comanche', 'Insco', 'Lawrin']);
  assert.equal(memorials.filter(record => record.details.cenotaphLabelPresent).length, 6);
  assert.ok(memorials.every(record => record.details.burialStatus === 'not_verified'));
  assert.equal(data.sources.find(source => source.id === 'onthisday').recordCount, 218);
  assert.equal(data.sources.find(source => source.id === 'kansashistory').recordCount, 213);
});

test('conflicts, fictional entries and regional geography retain their distinct source roles', () => {
  const bighorn = data.records.find(record => record.id === 'reflector-011');
  assert.equal(bighorn.date, '1867-06-25');
  assert.equal(bighorn.details.correctionEvidence.date, '1876-06-25/1876-06-26');
  assert.match(bighorn.reviewNote, /1876/);
  const westport = data.records.find(record => record.id === 'history-017');
  assert.match(westport.details.correctionEvidence.place, /Missouri/);
  assert.match(westport.relation, /outside kansas/);
  const fiction = data.records.filter(record => record.kind === 'fictional');
  assert.equal(fiction.length, 24);
  assert.ok(fiction.every(record => record.date === null && record.place === null));
  assert.ok(data.records.filter(record => record.sourceId === 'ffa' && record.details.type === 'timeline_index').every(record => /^\d{4}$/.test(record.date)));
  assert.equal(data.integration.canonicalIdentityResolution, false);
  assert.equal(data.integration.geocoding, false);
  assert.deepEqual(data.lifecycle, { sourceAdmission: 'NOT_ADMITTED', review: 'PENDING', mapActivation: 'NONE' });
});

test('CSV is a reproducible projection and spreadsheet formulas remain inert', async () => {
  assert.equal(await readFile('public/history/people-events.csv', 'utf8'), historyResearchCsv(data.records));
  for (const value of ['=1+1', '+cmd', '-2+3', '@SUM(A1)', ' \t=HYPERLINK("x")', '\tplain']) {
    assert.ok(historyCsvCell(value).startsWith('"\''));
  }
  assert.equal(historyCsvCell('A,"B"\nC'), '"A,""B""\nC"');
  assert.equal(historyCsvCell(null), '""');
});

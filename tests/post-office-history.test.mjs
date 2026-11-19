import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import {
  continuityText, locationText, mapOfficeGroups, officesInView, postalCSV, postalMap,
  postalTimeline, readPostalView, recordedEvents,
} from '../app/labs/ghost-towns/post-office-model.mjs';

const snapshot = JSON.parse(await readFile(new URL('../app/labs/ghost-towns/post-office-snapshot.json', import.meta.url), 'utf8'));
const { boundary, records, scope, source } = snapshot;
const timeline = postalTimeline(records);

test('the postal snapshot pins the original coordinate edition and Douglas County cohort', async () => {
  assert.equal(scope.fips, '20045');
  assert.equal(records.length, 59);
  assert.equal(new Set(records.map(record => record.id)).size, records.length);
  assert.ok(records.every(record => record.counties.includes('DOUGLAS')));
  assert.equal(records.filter(record => record.location).length, 45);
  assert.equal(records.filter(record => record.continuous === false).length, 1);
  assert.equal(source.license, 'CC0 1.0');
  assert.match(source.url, /4491713\?format=original$/);
  assert.equal(source.sha256, 'b860791be2542d9da6224c4fc91801e1fbe2236fbf98cd0f22751e9c7ae83499');
  const countyBundle = await readFile(new URL('../public/labs-data/census-mosaic-a3c82ebd5d89619c.json', import.meta.url));
  assert.equal(boundary.bundleSha256, createHash('sha256').update(countyBundle).digest('hex'));
  const county = JSON.parse(countyBundle).data.records.find(record => record.fips === scope.fips);
  assert.deepEqual(boundary.ring, county.geometry.coordinates[0]);
});

test('the timeline counts actual source dates, leaves gaps empty, and never infers an active office', () => {
  assert.deepEqual([timeline.min, timeline.max, timeline.busiest], [1855, 1956, 1855]);
  assert.equal(timeline.years.reduce((sum, entry) => sum + entry.established, 0), 58);
  assert.equal(timeline.years.reduce((sum, entry) => sum + entry.discontinued, 0), 55);
  const emptyYear = timeline.years.find(entry => !entry.established && !entry.discontinued).year;
  assert.equal(officesInView(records, emptyYear, 'events').length, 0);
  const bothDates = { established: 1890, discontinued: 1890 };
  assert.deepEqual(recordedEvents(bothDates, 1890), ['Established', 'Discontinued']);
  assert.deepEqual(officesInView([bothDates], 1890, 'events'), [bothDates]);
});

test('unknown locations and undated noncontinuous records remain inspectable', () => {
  const baldwin = records.find(record => record.name === 'BALDWIN CITY');
  assert.deepEqual([baldwin.established, baldwin.discontinued, baldwin.continuous], [null, null, false]);
  assert.match(continuityText(baldwin), /Marked noncontinuous/);
  assert.equal(officesInView(records, 1900, 'events').includes(baldwin), false);
  assert.ok(officesInView(records, 1900, 'all').includes(baldwin));
  assert.equal(locationText(records.find(record => !record.location)), 'No matched coordinates');
  const projection = postalMap(boundary.ring, records);
  const groups = mapOfficeGroups(records, projection.project);
  assert.ok(groups.length < 45);
  assert.equal(groups.reduce((sum, group) => sum + group.records.length, 0), 45);
  assert.ok(groups.every(group => group.x > 0 && group.x < 100 && group.y > 0 && group.y < 100));
});

test('view links accept only known years, modes and record IDs in the visible selection', () => {
  const event = officesInView(records, 1900, 'events')[0];
  assert.deepEqual(readPostalView({ year: '1900', office: event.id }, timeline, records), { year: 1900, view: 'events', office: event.id });
  assert.deepEqual(readPostalView({ year: ['1900'], view: 'other', office: '../../anything' }, timeline, records),
    { year: timeline.busiest, view: 'events', office: null });
  const undated = records.find(record => record.established === null && record.discontinued === null);
  assert.equal(readPostalView({ year: '1900', view: 'all', office: undated.id }, timeline, records).office, undated.id);
  assert.equal(readPostalView({ year: '1900', office: undated.id }, timeline, records).office, null);
});

test('CSV identifies the exact view and carries original source provenance on each record', () => {
  const visible = officesInView(records, 1900, 'events');
  const [headers, ...rows] = postalCSV(visible, 1900, 'events', source);
  assert.equal(rows.length, visible.length);
  for (const row of rows) {
    assert.equal(row.length, headers.length);
    assert.equal(row[headers.indexOf('Selected year')], 1900);
    assert.equal(row[headers.indexOf('Source SHA-256')], source.sha256);
    assert.equal(row[headers.indexOf('Source URL')], source.url);
  }
});

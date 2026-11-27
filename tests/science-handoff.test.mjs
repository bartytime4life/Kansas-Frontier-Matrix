import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import {
  SCIENCE_TOOLS, SCIENCE_YEARS, SERVICE_OPTIONS, INQUIRY_CONTACT, INQUIRY_LIMITS,
  scienceToolPath, scienceSelectionPath, safeScienceContext,
  serviceInquiryPath, readInquirySelection, inquiryDraft,
} from '../app/science/science-handoff.mjs';

test('every quick start uses the target tool native clock window and distinct comparison years', () => {
  for (const tool of SCIENCE_TOOLS) for (const year of SCIENCE_YEARS) {
    const path = scienceToolPath(tool.id, year);
    assert.equal(safeScienceContext(path), path);
    const url = new URL(path, 'https://example.test');
    assert.equal(url.pathname, tool.path);
    if (tool.id === 'drought') {
      assert.equal(url.searchParams.get('from'), String(year));
      assert.equal(url.searchParams.get('to'), String(year));
    } else {
      assert.equal(url.searchParams.get('year'), String(year));
      if (tool.id === 'comparison') assert.notEqual(url.searchParams.get('compare'), String(year));
    }
    for (const geographic of ['station', 'county', 'primary']) assert.equal(url.searchParams.has(geographic), false, 'no invented shared location');
  }
  for (const args of [['missing', 2025], ['weather', '2024'], ['soil', 2026], ['air', NaN]]) assert.throws(() => scienceToolPath(...args));
});

test('handoff retains normalized thresholds, depths, dates, two-place selections and comparison years', () => {
  const cases = [
    ['weather', { station: 'USW00013996', year: 2024, month: 2, units: 'imperial', heat: 32.2, wet: 1 }, '/labs/heat-and-rain?station=USW00013996&year=2024&month=2&units=imperial&heat=32.2&wet=1'],
    ['drought', { countyId: '20177', compareId: '20055', fromYear: 2020, toYear: 2024, level: 3, threshold: 25.5 }, '/labs/county-drought?county=20177&compare=20055&from=2020&to=2024&level=3&threshold=25.5'],
    ['soil', { station: '53974', year: 2024, month: 2, depth: 100, variable: 'temperature', date: '2024-02-29' }, '/labs/soil-profile?station=53974&year=2024&month=2&depth=100&variable=temperature&date=2024-02-29'],
    ['air', { county: '20177', year: 2024, month: 2, threshold: 101, date: '2024-02-29' }, '/labs/daily-air-quality?county=20177&year=2024&month=2&threshold=101&date=2024-02-29'],
    ['sunlight', { primary: 'wichita', comparison: 'wichita', year: 2024, month: 0, date: '2024-02-29' }, '/labs/sunlight-and-sky?primary=wichita&comparison=wichita&year=2024&month=0&date=2024-02-29'],
    ['comparison', { year: 2021, compareYear: 2023 }, '/science/compare?year=2021&compare=2023'],
  ];
  for (const [tool, selection, expected] of cases) {
    const path = scienceSelectionPath(tool, { ...selection, token: 'must-not-propagate', lat: 39 });
    assert.equal(path, expected);
    const inquiry = readInquirySelection(new URL(serviceInquiryPath(path, 'data'), 'https://example.test').search);
    assert.deepEqual(inquiry, { service: 'data', context: path });
    const draft = inquiryDraft({ ...inquiry, question: 'Compare these source records.' });
    assert.match(draft.text, new RegExp(expected.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')));
  }
  assert.throws(() => scienceSelectionPath('weather', null));
  assert.throws(() => scienceSelectionPath('drought', { countyId: '20177', compareId: '20177' }));
});

test('current manifest coverage is accepted without broadening source coverage', async () => {
  const root = new URL('../app/labs/', import.meta.url);
  const manifest = async id => JSON.parse(await readFile(new URL(`${id}/snapshot-manifest.json`, root), 'utf8'));
  for (const station of (await manifest('heat-and-rain')).stations) assert.ok(safeScienceContext(`/labs/heat-and-rain?station=${station.id}`));
  for (const station of (await manifest('soil-profile')).stations) assert.ok(safeScienceContext(`/labs/soil-profile?station=${station.id}`));
  for (const county of (await manifest('county-drought')).counties) assert.ok(safeScienceContext(`/labs/county-drought?county=${county.id}`));
  for (const county of (await manifest('daily-air-quality')).counties) assert.ok(safeScienceContext(`/labs/daily-air-quality?county=${county.id}`));
  for (const point of (await manifest('sunlight-and-sky')).points) assert.ok(safeScienceContext(`/labs/sunlight-and-sky?primary=${point.id}`));
  assert.equal(safeScienceContext('/labs/daily-air-quality?county=20055'), null, 'no EPA display snapshot for Ford County');
  assert.equal(safeScienceContext('/labs/soil-profile?station=topeka'), null, 'no invented Topeka soil station');
});

test('inquiry context rejects foreign routes, credentials, arbitrary text, repeated selectors and incoherent dates', () => {
  const invalid = [null, {}, [], 5, '', 'https://kansasfrontiermatrix.com/science/compare', '//evil.test/science/compare',
    '/\\evil.test/science/compare', '/science/compare#private', '/science/../science/compare', '/science/%63ompare',
    '/science/services?email=person@example.test', '/api/local-data?token=private',
    '/labs/heat-and-rain?lat=39&lon=-96', '/labs/heat-and-rain?year=2020&year=2021',
    '/labs/heat-and-rain?year=2025e0', '/labs/heat-and-rain?station=USW00000000', '/labs/heat-and-rain?heat=Infinity',
    '/labs/county-drought?county=20000', '/labs/county-drought?county=20002', '/labs/county-drought?county=20211',
    '/labs/county-drought?from=2025&to=2020', '/labs/county-drought?level=0', '/labs/county-drought?threshold=1.234',
    '/labs/daily-air-quality?threshold=501', '/labs/soil-profile?depth=30',
    '/labs/sunlight-and-sky?date=2023-02-29', '/labs/sunlight-and-sky?date=2024-02-29', '/labs/sunlight-and-sky?year=2025&date=2024-02-29',
    '/labs/sunlight-and-sky?month=3&date=2024-02-29', '/science/compare?year=2024&compare=2024',
    '/labs/daily-air-quality?county=20177%0Asecret', `/science/compare?${'a'.repeat(1201)}`];
  for (const path of invalid) assert.equal(safeScienceContext(path), null, String(path));
  assert.equal(safeScienceContext('/science/compare?compare=2021&year=2024'), '/science/compare?year=2024&compare=2021');
  assert.equal(safeScienceContext('/labs/soil-profile?year=2024&month=0&date=2024-02-29'), '/labs/soil-profile?year=2024&month=0&date=2024-02-29');
});

test('service selectors cannot reflect untrusted or duplicate context into a draft', () => {
  assert.deepEqual(readInquirySelection('?service=walkthrough'), { service: 'walkthrough', context: null });
  assert.deepEqual(readInquirySelection('?service=brief&service=data&context=%2Fapi%2Fprivate'), { service: 'brief', context: null });
  assert.deepEqual(readInquirySelection('?context=%2Fscience%2Fcompare&context=%2Flabs%2Fsoil-profile'), { service: 'brief', context: null });
  assert.deepEqual(readInquirySelection({ toString() { throw new Error('never coerce'); } }), { service: 'brief', context: null });
  assert.equal(serviceInquiryPath('https://evil.test/?token=private', 'bogus'), '/science/services');
  const draft = inquiryDraft({ context: '/labs/soil-profile?token=private' });
  assert.equal(draft.context, null);
  assert.doesNotMatch(draft.text, /token|private/);
});

test('project drafts preserve user text as body only and remain explicitly unsent, unpriced inquiries', () => {
  for (const option of SERVICE_OPTIONS) {
    const question = 'Compare February & March.\nInclude “wet days” and units?';
    const draft = inquiryDraft({ service: option.id, question, area: '  Shawnee County  ', timing: 'Next month' });
    assert.ok(Object.isFrozen(draft));
    assert.equal(draft.canEmail, true);
    assert.match(draft.text, /General area: Shawnee County/);
    assert.ok(draft.text.includes(question));
    assert.match(draft.text, /quote before any work begins/);
    assert.match(draft.text, /remain free/);
    const mail = new URL(draft.mailto);
    assert.equal(mail.protocol, 'mailto:');
    assert.equal(mail.pathname, INQUIRY_CONTACT);
    assert.equal(mail.searchParams.get('body'), draft.text);
    assert.deepEqual([...mail.searchParams.keys()], ['subject', 'body']);
    assert.match(draft.filename, /^kfm-(?:brief|data|walkthrough)-project-inquiry\.txt$/);
  }
  assert.equal(inquiryDraft({ question: '   ' }).canEmail, false);
  assert.throws(() => inquiryDraft({ service: 'instant-certification' }));
  for (const [key, maximum] of Object.entries(INQUIRY_LIMITS)) {
    assert.throws(() => inquiryDraft({ [key]: 'a'.repeat(maximum + 1) }), /field/);
    assert.throws(() => inquiryDraft({ [key]: {} }), /field/);
    assert.throws(() => inquiryDraft({ [key]: '\u0000' }), /field/);
  }
});

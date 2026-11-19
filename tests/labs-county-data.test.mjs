import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { COUNTY_LAB_SNAPSHOTS } from '../app/labs/county-snapshots.mjs';
import { KANSAS_COUNTIES } from '../app/labs/county-model.mjs';
import { validStoryBundle, STORY_BUNDLE_BYTES } from '../app/living-welcome/stories/story-bundle.mjs';
import { recordModel, filterRecords } from '../app/living-welcome/stories/record-model.mjs';

const entry = COUNTY_LAB_SNAPSHOTS['county-conditions'];
const raw = await readFile(new URL('../public' + entry.path, import.meta.url));
const bundle = JSON.parse(raw), d = bundle.data;

test('County Conditions is a bounded exact-byte public bundle covering all three non-overlapping ACS periods', () => {
  assert.equal(raw.length, entry.bytes);
  assert.ok(raw.length < STORY_BUNDLE_BYTES);
  assert.equal(createHash('sha256').update(raw).digest('hex'), entry.sha256);
  assert.equal(validStoryBundle(bundle, 'county-conditions'), true);
  assert.equal(d.records.length, 315);
  assert.equal(new Set(d.records.map(row => row.id)).size, 315);
  assert.equal(d.temporalMode, 'snapshot');
  assert.equal(d.confidenceLevel, .9);
  const model = recordModel(bundle);
  for (const year of [2014, 2019, 2024]) {
    const selected = filterRecords(model, { time: year });
    assert.equal(selected.length, 105);
    assert.deepEqual(selected.map(row => [row.fips, row.name]), KANSAS_COUNTIES.map(row => [row.fips, row.name]));
    assert.ok(selected.every(row => row.period === `${year - 4}–${year}` && row.geometry && row.id === `${row.fips}/${year}`));
  }
  assert.deepEqual(bundle.observed, { from: '2010', to: '2024' });
  assert.ok(d.columns.length <= 60);
  assert.ok(d.limits.some(limit => /not been adjusted to a common price year/.test(limit)));
});

test('public ACS acquisition receipts distinguish complete ZIPs from independently verified national-table byte prefixes', () => {
  assert.equal(d.sourceSnapshots.length, 28);
  const prefixes = d.sourceSnapshots.filter(source => source.httpStatus === 206);
  assert.equal(prefixes.length, 9);
  for (const receipt of d.sourceSnapshots) {
    assert.equal(new URL(receipt.url).protocol, 'https:');
    assert.match(new URL(receipt.url).hostname, /(?:^|\.)census\.gov$/);
    assert.equal(new URL(receipt.url).searchParams.has('key'), false);
    assert.match(receipt.rawSha256, /^[a-f0-9]{64}$/);
    assert.ok(receipt.rawBytes > 0 && receipt.rawBytes <= 16_000_000);
    assert.ok(Date.parse(receipt.retrievedAt));
    if (receipt.httpStatus === 206) {
      assert.equal(receipt.requestRange, 'bytes=0-2097151');
      const match = /^bytes 0-(\d+)\/(\d+)$/.exec(receipt.contentRange);
      assert.ok(match);
      assert.equal(Number(match[1]) + 1, receipt.rawBytes);
      assert.ok(Number(match[2]) > receipt.rawBytes);
      assert.match(receipt.hashScope, /not entire national table/);
    } else {
      assert.equal(receipt.httpStatus, 200);
      assert.equal(receipt.requestRange, null);
      assert.equal(receipt.hashScope, 'entire response');
    }
  }
  assert.ok(d.limits.some(limit => /exactly the same 105 Kansas county FIPS/.test(limit)));
});

test('derived county percentages retain their source denominators and documented approximate 90% MOEs', () => {
  for (const row of d.records) {
    const degreeKeys = ['bachelors', 'masters', 'professional', 'doctorate'];
    assert.equal(row.bachelorsOrHigher, degreeKeys.reduce((sum, key) => sum + row[key], 0));
    assert.ok(Math.abs(row.bachelorsOrHigherMoe - Math.sqrt(degreeKeys.reduce((sum, key) => sum + row[key + 'Moe'] ** 2, 0))) < 1e-8);
    for (const [key, { numerator, denominator }] of Object.entries(d.derivedFields)) {
      const p = row[numerator] / row[denominator];
      assert.ok(p >= 0 && p <= 1);
      assert.ok(Math.abs(row[key] - p * 100) < 1e-10);
      const subtraction = row[numerator + 'Moe'] ** 2 - p ** 2 * row[denominator + 'Moe'] ** 2;
      const radicand = subtraction < 0 ? row[numerator + 'Moe'] ** 2 + p ** 2 * row[denominator + 'Moe'] ** 2 : subtraction;
      assert.ok(Math.abs(row[key + 'Moe'] - 100 * Math.sqrt(radicand) / row[denominator]) < 1e-9);
      assert.ok(row.moeMethods[key].includes(subtraction < 0 ? 'fallback' : 'subset'));
    }
    for (const key of ['medianIncome', 'medianAge', 'medianHomeValue', 'medianRent']) assert.ok(row[key + 'Moe'] >= 0);
  }
  assert.ok(bundle.sources.some(source => source.url.endsWith('2023_ACS_Accuracy_Document_Worked_Examples.pdf')));
  assert.ok(d.limits.some(limit => /omit unavailable covariance/.test(limit)));
  const johnson = d.records.find(row => row.year === 2024 && row.fips === '20091');
  assert.equal(johnson.medianIncome, 109208, 'official 2020–2024 Johnson County median household income');
  assert.equal(johnson.medianIncomeMoe, 1170);
  assert.equal(johnson.civilianLaborForce, 352618);
  assert.equal(johnson.unemployed, 11298);
  assert.equal(d.sourceDefinitions['2024'].civilianLaborForce.estimate, 'B23025_003E');
  assert.equal(d.sourceDefinitions['2014'].medianIncome.estimate, 'B19013_001E');
});

test('ACS parsers retain missing sentinels as null and calculate documented MOE fallbacks without fake precision', () => {
  const script = new URL('../scripts/prepare-labs-county-data.py', import.meta.url);
  const result = spawnSync('python3', ['-c', `
import importlib.util, math, sys
sys.dont_write_bytecode = True
spec=importlib.util.spec_from_file_location('county',sys.argv[1]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
for value in ['-666666666','-888888888','-555555555','','.','(X)','**']:
 assert m.numeric(value) is None,value
assert m.numeric('0')==0
for value in ['-1','nan','inf','unknown']:
 try:m.numeric(value)
 except ValueError:pass
 else:raise AssertionError(value)
estimate,moe,method=m.proportion(50,100,1,10)
assert estimate==50 and abs(moe-math.sqrt(26))<1e-12 and 'fallback' in method
estimate,moe,method=m.proportion(20,100,5,10)
assert estimate==20 and abs(moe-math.sqrt(21))<1e-12 and 'subset' in method
assert m.proportion(0,0,1,1)[:2]==(None,None)
assert m.proportion(None,100,1,1)[:2]==(None,None)
assert m.proportion(20,100,None,1)[:2]==(20,None)
try:m.proportion(101,100,1,1)
except ValueError:pass
else:raise AssertionError('invalid subset accepted')
`, script.pathname], { encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr || result.stdout);
});

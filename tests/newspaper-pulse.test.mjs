import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import {
  compareIssues, comparisonReceipt, MAX_INDEXED_PAGES, normalizeWord, pageWords,
} from '../app/labs/newspaper-pulse/cohort.mjs';

const cohort = JSON.parse(readFileSync(new URL('../app/labs/newspaper-pulse/reflector-cohort.json', import.meta.url), 'utf8'));

test('the OCR index uses distinct whole words and the two input words must differ', () => {
  assert.deepEqual([...pageWords('Wheat, wheat! Rail-road; ﬁeld. ⅳ. 1890')], ['wheat', 'rail', 'road', 'field', 'iv', '1890']);
  assert.equal(normalizeWord(' ＲＡＩＬ '), 'rail');
  for (const input of ['', 'rail road', 'rail*', 'rail-road', 'a'.repeat(41), null]) {
    assert.equal(normalizeWord(input), null);
  }
  assert.equal(compareIssues(cohort, 'Railroad', ' railroad '), null);
  assert.equal(compareIssues(cohort, 'railroad', ''), null);
});

test('the source snapshot binds all pages of each selected edition and no extras', () => {
  assert.equal(cohort.format, 'kfm-newspaper-pulse-cohort-v1');
  assert.equal(cohort.lccn, 'sn84029386');
  assert.equal(cohort.source.url, 'https://www.loc.gov/item/sn84029386/');
  assert.equal(cohort.source.digitizedBy, 'Kansas State Historical Society, Topeka, Kansas');
  assert.ok(Number.isFinite(Date.parse(cohort.retrievedAt)));
  assert.deepEqual(cohort.issues.map(issue => [issue.date, issue.edition, issue.pageCount]), [
    ['1890-01-02', 1, 8], ['1900-01-04', 1, 12],
  ]);
  const pages = [];
  for (const { date, issueUrl, inventoryUrl, inventorySha256, pageCount, pages: issuePages } of cohort.issues) {
    const path = `sn84029386/${date}/ed-1/`;
    assert.equal(issueUrl, `https://www.loc.gov/item/${path}`);
    assert.equal(inventoryUrl, `https://www.loc.gov/resource/${path}?fo=json&c=25`);
    assert.match(inventorySha256, /^[a-f0-9]{64}$/);
    assert.deepEqual(issuePages.map(page => page.number), Array.from({ length: pageCount }, (_, index) => index + 1));
    for (const { number, url, ocrUrl, ocrSha256 } of issuePages) {
      assert.equal(url, `https://www.loc.gov/resource/${path}?sp=${number}`);
      const ocr = new URL(ocrUrl);
      assert.equal(ocr.origin, 'https://tile.loc.gov');
      assert.equal(ocr.pathname, '/text-services/word-coordinates-service');
      assert.match(ocr.searchParams.get('segment'), /\/sn84029386\/.+\.xml$/);
      assert.equal(ocr.searchParams.get('full_text'), '1');
      assert.match(ocrSha256, /^[a-f0-9]{64}$/);
      pages.push(url);
    }
  }
  assert.equal(new Set(pages).size, pages.length);
  assert.ok(pages.length <= MAX_INDEXED_PAGES);
  const lastMask = 2 ** pages.length - 1;
  let indexed = 0;
  for (const [word, mask] of Object.entries(cohort.index)) {
    assert.equal(normalizeWord(word), word);
    assert.ok(Number.isSafeInteger(mask) && mask > 0 && mask <= lastMask);
    indexed |= mask;
  }
  assert.equal(indexed, lastMask, 'every inventoried page has searchable OCR');
});

test('two words use the same full denominators with exact source-page drilldown', () => {
  const comparison = compareIssues(cohort, 'Railroad', 'Wheat');
  assert.deepEqual(comparison.terms, ['railroad', 'wheat']);
  assert.deepEqual(comparison.issues.map(issue => [issue.pageCount, issue.totals, issue.shares]), [
    [8, [7, 4], [7 / 8, 4 / 8]], [12, [4, 5], [4 / 12, 5 / 12]],
  ]);
  for (const issue of comparison.issues) {
    assert.equal(issue.pages.length, issue.pageCount);
    assert.deepEqual(issue.totals, comparison.terms.map((_, index) => issue.pages.filter(page => page.matches[index]).length));
    assert.ok(issue.pages.some(page => page.matches.every(Boolean)), 'a page can match both words');
  }
  const zero = compareIssues(cohort, 'nevergoingtomatch', 'railroad');
  assert.ok(zero.issues.every(issue => issue.totals[0] === 0 && issue.shares[0] === 0));

  const receipt = comparisonReceipt(cohort, comparison);
  assert.equal(receipt.format, 'kfm-newspaper-pulse-comparison-v1');
  assert.deepEqual(receipt.source, cohort.source);
  assert.deepEqual(receipt.issues, comparison.issues);
  assert.ok(!Object.hasOwn(receipt, 'index'));
});

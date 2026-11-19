import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { rename, writeFile } from 'node:fs/promises';
import { setTimeout as delay } from 'node:timers/promises';
import { MAX_INDEXED_PAGES, pageWords } from '../app/labs/newspaper-pulse/cohort.mjs';

// Review candidate using the full digitized page inventory of two named editions.
// These are a fixed cohort, with earlier/later editions chosen one decade apart.
const TITLE = 'Abilene Weekly Reflector';
const LCCN = 'sn84029386';
const EDITION = 1;
const DATES = ['1890-01-02', '1900-01-04'];
const LIMIT_BYTES = 2_000_000;
const output = new URL('../app/labs/newspaper-pulse/reflector-cohort.json', import.meta.url);
const temporary = new URL('../app/labs/newspaper-pulse/reflector-cohort.json.tmp', import.meta.url);
const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');

async function getJson(url) {
  const response = await fetch(url, {
    headers: { Accept: 'application/json', 'User-Agent': 'KansasFrontierMatrix/1.0 (bounded source verification)' },
    redirect: 'error',
    signal: AbortSignal.timeout(15_000),
  });
  if (!response.ok || !response.headers.get('content-type')?.includes('application/json')) {
    throw new Error(`Library of Congress response unavailable (${response.status}) for ${url}`);
  }
  const reader = response.body.getReader();
  const chunks = [];
  let size = 0;
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      size += value.byteLength;
      if (size > LIMIT_BYTES) throw new Error(`Library of Congress response too large for ${url}`);
      chunks.push(value);
    }
  } finally {
    await reader.cancel().catch(() => {});
  }
  const bytes = Buffer.concat(chunks);
  return { data: JSON.parse(bytes.toString('utf8')), sha256: sha256(bytes) };
}

const issues = [];
const index = new Map();
let offset = 0;
for (const date of DATES) {
  const path = `/${LCCN}/${date}/ed-${EDITION}/`;
  const issueUrl = `https://www.loc.gov/item${path}`;
  const resource = `https://www.loc.gov/resource${path}`;
  const inventoryUrl = `${resource}?fo=json&c=25`;
  const { data: inventory, sha256: inventorySha256 } = await getJson(inventoryUrl);
  const segments = [...inventory.segments].sort((a, b) => a.index - b.index);
  const expectedPages = inventory.resources[0].segment_count;
  assert.equal(inventory.item.date, date);
  assert.deepEqual(inventory.item.number_lccn, [LCCN]);
  assert.ok(Number.isInteger(expectedPages) && expectedPages > 0 && offset + expectedPages <= MAX_INDEXED_PAGES);
  assert.equal(inventory.viewer_pagination.of, expectedPages);
  assert.equal(inventory.viewer_pagination.next, null);
  assert.equal(segments.length, expectedPages);

  const pages = [];
  for (const [position, segment] of segments.entries()) {
    const number = position + 1;
    const url = `${resource}?sp=${number}`;
    assert.equal(segment.index, number);
    assert.equal(segment.url, url);
    assert.equal(segment.digitized, true);
    assert.deepEqual(segment.number_lccn, [LCCN]);
    assert.deepEqual(segment.number_edition, [String(EDITION)]);
    assert.equal(segment.date, date);
    assert.ok(segment.contributor.includes('kansas state historical society; topeka, ks'));
    const ocr = new URL(segment.image_url.at(-1));
    assert.equal(ocr.origin, 'https://tile.loc.gov');
    assert.equal(ocr.pathname, '/text-services/word-coordinates-service');
    const key = ocr.searchParams.get('segment');
    assert.ok(key?.startsWith('/service/ndnp/') && key.includes(`/${LCCN}/`) && key.endsWith('.xml'));
    ocr.search = new URLSearchParams({ segment: key, format: 'alto_xml', full_text: '1' }).toString();

    // A single request at a time, well below the provider's Text Services limit.
    await delay(500);
    const { data, sha256: ocrSha256 } = await getJson(ocr.href);
    const text = data[key]?.full_text;
    assert.ok(typeof text === 'string' && text.trim(), `OCR is missing for ${url}`);
    const words = pageWords(text);
    assert.ok(words.size > 0, `OCR contains no searchable tokens for ${url}`);
    const bit = 2 ** offset++;
    for (const word of words) index.set(word, (index.get(word) ?? 0) | bit);
    pages.push({ number, url, ocrUrl: ocr.href, ocrSha256 });
  }
  issues.push({ date, edition: EDITION, issueUrl, inventoryUrl, inventorySha256, pageCount: expectedPages, pages });
}
const cohort = {
  format: 'kfm-newspaper-pulse-cohort-v1',
  title: TITLE,
  lccn: LCCN,
  source: {
    provider: 'Library of Congress, Chronicling America',
    digitizedBy: 'Kansas State Historical Society, Topeka, Kansas',
    url: `https://www.loc.gov/item/${LCCN}/`,
    rightsUrl: 'https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/',
  },
  retrievedAt: new Date().toISOString(),
  issues,
  index: Object.fromEntries([...index].sort(([a], [b]) => a < b ? -1 : a === b ? 0 : 1)),
};
await writeFile(temporary, `${JSON.stringify(cohort)}\n`, { flag: 'wx' });
await rename(temporary, output);
process.stdout.write(`Saved ${offset} OCR pages across ${issues.length} editions and ${index.size} searchable words.\n`);

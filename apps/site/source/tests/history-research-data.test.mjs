import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, rmSync, symlinkSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { brotliCompressSync, gzipSync } from 'node:zlib';
import { validateHistoryPublic } from '../scripts/validate-history-public.mjs';

function temporary(t) {
  const root = mkdtempSync(path.join(tmpdir(), 'kfm-history-hold-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  return root;
}
const record = { id: 'synthetic', sourceId: 'synthetic-source', kind: 'person', title: 'Synthetic Person', date: '2000-01-01', place: 'Synthetic place', relation: 'Synthetic only', reviewNote: 'Pending synthetic review' };
const catalog = { schemaVersion: 1, lifecycle: { sourceAdmission: 'NOT_ADMITTED', review: 'PENDING', mapActivation: 'NONE' }, sources: [], records: [record] };
const csv = '"id","sourceId","kind","title","category","date","place","relation","sourceUrl","targetUrl","reviewNote","themes"\r\n"synthetic","synthetic-source","person","Synthetic Person","","2000-01-01","Synthetic place","Synthetic only","","","Pending synthetic review",""\r\n';

test('public tree has no held research assets and retains ordinary history source metadata', () => {
  assert.deepEqual(validateHistoryPublic(path.resolve('public')), []);
  for (const name of ['people-events.json', 'people-events.csv']) {
    assert.throws(() => readFileSync(path.join('public/history', name)), { code: 'ENOENT' });
  }
  assert.equal(JSON.parse(readFileSync('public/history/sources.json')).sources.length, 17);
});

test('reserved history paths reject JSON, CSV, compressed and nested files even with approval labels', t => {
  const root = temporary(t); mkdirSync(path.join(root, 'history'));
  for (const name of ['people-events.json', 'people-events.csv', 'people-events.json.gz', 'people-events.csv.br']) {
    const file = path.join(root, 'history', name);
    writeFileSync(file, '{}');
    assert.ok(validateHistoryPublic(root).length, name);
    rmSync(file);
  }
  mkdirSync(path.join(root, 'history/people-events'));
  assert.ok(validateHistoryPublic(root).length);
});

test('renaming, wrapping, extracting records and changing lifecycle labels cannot release the research profile', t => {
  const root = temporary(t), file = path.join(root, 'alias.dat');
  for (const value of [catalog, { envelope: catalog }, [record], { ...catalog, records: [] },
    { ...catalog, lifecycle: { sourceAdmission: 'ADMITTED', review: 'APPROVED', release: 'PUBLIC_SAFE' } }]) {
    for (const encode of [value => Buffer.from(JSON.stringify(value)), value => gzipSync(JSON.stringify(value))]) {
      writeFileSync(file, encode(value));
      assert.ok(validateHistoryPublic(root).length);
    }
  }
  writeFileSync(path.join(root, 'alias.json.br'), brotliCompressSync(JSON.stringify(catalog)));
  assert.ok(validateHistoryPublic(root).length);
});

test('renamed CSV and compressed or reordered/BOM headers are denied', t => {
  const root = temporary(t);
  for (const [name, bytes] of [['alias.txt', csv], ['alias.bin', gzipSync(csv)], ['alias.csv.br', brotliCompressSync(csv)],
    ['reordered.csv', '\uFEFF"reviewNote","title","kind","relation","sourceId"\r\n']]) {
    const file = path.join(root, name); writeFileSync(file, bytes);
    assert.ok(validateHistoryPublic(root).length, name); rmSync(file);
  }
});

test('malformed carriers and symlink aliases fail closed; unrelated sources, text and CSV remain usable', t => {
  const root = temporary(t), file = path.join(root, 'alias');
  for (const [name, bytes] of [['bad.json', '{'], ['bad.json.gz', gzipSync('{')], ['bad.br', 'invalid brotli']]) {
    const target = path.join(root, name); writeFileSync(target, bytes);
    assert.ok(validateHistoryPublic(root).length); rmSync(target);
  }
  writeFileSync(file, JSON.stringify({ sources: [{ title: 'Synthetic archive' }] }));
  writeFileSync(path.join(root, 'book.txt'), 'Synthetic historical text.');
  writeFileSync(path.join(root, 'unrelated.csv'), 'year,count\r\n1909,1\r\n');
  assert.deepEqual(validateHistoryPublic(root), []);
  symlinkSync(file, path.join(root, 'linked.json'));
  assert.ok(validateHistoryPublic(root).length);
});

test('shared build/start gate rejects a stale built history carrier and accepts an ordinary static tree', t => {
  const root = temporary(t);
  const run = () => spawnSync(process.execPath, ['scripts/validate-subsurface-public.mjs', root], { encoding: 'utf8' });
  assert.equal(run().status, 0);
  writeFileSync(path.join(root, 'stale.csv'), csv);
  const result = run();
  assert.equal(result.status, 1); assert.match(result.stderr, /history research CSV delivery is held/);
});

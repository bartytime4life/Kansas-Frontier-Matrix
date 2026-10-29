// Offline qualification of exact provider bytes; inputs are never added to application assets.
// node scripts/verify-civic-history.mjs /path/to/retrieved/provider/files
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { basename, resolve } from 'node:path';
import { createHash } from 'node:crypto';
import ts from 'typescript';
const sourceDir = process.argv[2];
if (!sourceDir) throw new Error('Provide a directory of the 18 pinned source files; this verifier does not download or publish data.');
async function compile(file, deps = {}) {
  const exports = {};
  new Function('exports', 'require', ts.transpileModule(await readFile(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText)(exports, name => {
    if (!(name in deps)) throw new Error(`Unexpected import ${name}`); return deps[name];
  }); return exports;
}
const civic = await compile('app/civic-districts.ts');
const history = await compile('app/civic-history.ts', { './civic-districts': civic });
const bounded = await compile('app/bounded-json.ts');
const reader = await compile('app/api/live-context/civic-history.ts', { '../../bounded-json': bounded, '../../civic-history': history, './civic-districts': {} });
const bytes = new Map(), receipts = [];
for (const plan of history.CIVIC_HISTORY_PLANS) {
  const raw = await readFile(resolve(sourceDir, basename(plan.file)));
  assert.equal(createHash('sha256').update(raw).digest('hex'), plan.sha256, `Digest mismatch: ${plan.file}`);
  bytes.set(history.civicHistoryRawUrl(plan), raw);
  const payload = history.parseCivicHistory(JSON.parse(raw), history.civicTermStart(plan.first));
  assert.deepEqual(payload.data.features.map(f => f.properties.district), plan.districts);
  receipts.push({ file: plan.file, revision: plan.commit, sha256: plan.sha256, bytes: raw.length, constituencies: payload.featureCount });
}
let now = Date.parse('2026-10-29T00:00:00Z'), calls = 0, fail = false;
const read = reader.createCivicHistoryReader(async (url, options) => {
  calls++; assert.equal(options.redirect, 'manual'); assert.equal(options.cache, 'no-store');
  if (fail) throw new Error('private upstream failure');
  assert.ok(bytes.has(url), 'Only pinned source URLs may be requested');
  return new Response(bytes.get(url));
}, () => now, async () => { throw new Error('Census is outside this historical-file qualification'); });
let terms = 0;
for (let congress = 36; congress < 119; congress++) {
  const day = history.civicTermStart(congress);
  const values = await Promise.all(Array.from({ length: 12 }, () => read(day)));
  for (const payload of values) {
    assert.equal(payload.sourceDay, day);
    assert.ok(payload.data.features.every(f => f.properties.congressNumber === congress));
    assert.deepEqual(payload.data.features.map(f => f.properties.district), history.civicHistoryPlan(congress).districts);
  }
  terms++;
}
assert.equal(calls, 18, 'One acquisition per plan despite concurrent reads and repeated Congresses');
now += 24 * 60 * 60_000; fail = true;
await assert.rejects(read('2023-01-03'), /unavailable/);
const afterFailure = calls;
await assert.rejects(read('2023-01-03'), /unavailable/);
assert.equal(calls, afterFailure, 'Failure cooldown prevents repeated acquisitions');
now += 60_000; fail = false;
assert.equal((await read('2023-01-03')).featureCount, 4);
console.log(JSON.stringify({ status: 'passed', plans: receipts.length, congressionalTerms: terms, sourceReadsForTerms: 18, concurrentCallersPerTerm: 12, cacheExpiryAndCooldown: 'passed', receipts }, null, 2));

import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const compile = async path => ts.transpileModule(await readFile(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const url = value => `data:text/javascript;base64,${Buffer.from(value).toString('base64')}`;
const bounded = url(await compile('app/bounded-json.ts'));
const client = await import(url((await compile('app/intake-desk-client.ts')).replace('"./bounded-json"', JSON.stringify(bounded))));

const budget = patch => ({ github_limit_bytes: 100e9, reserved_for_code_and_interface_bytes: 20e9, data_ceiling_bytes: 80e9, committed_bytes: 36945647578,
  planned_bytes: 0, available_for_new_data_bytes: 43054352422, level: 'ok', committed: [], ...patch });
const overview = patch => ({ schema: 'kfm-intake-overview/v1', files: 21, bytes: 6190, by_status: { ready: { files: 1, bytes: 342 }, review: { files: 20, bytes: 5848 } },
  by_domain: {}, by_family: {}, by_lane: {}, last_run: { finished_at: '2026-10-09T18:42:06Z', state: 'complete' }, running_run: null,
  budget: budget(), release_plan_bytes: 0, ...patch });

test('intake overview parser keeps only shown, internally consistent fields', () => {
  const parsed = client.parseIntakeOverview(overview());
  assert.deepEqual([parsed.files, parsed.ready, parsed.review, parsed.blocked, parsed.running], [21, 1, 20, 0, false]);
  assert.equal(parsed.budget.available_for_new_data_bytes, 43054352422);
  assert.equal(parsed.lastRunFinishedAt, '2026-10-09T18:42:06Z');
  assert.equal('committed' in parsed.budget, false);
  assert.equal(client.parseIntakeOverview(overview({ running_run: 'intake-run', last_run: null })).running, true);
});

test('intake overview parser rejects malformed, inconsistent or unexpected shapes', () => {
  for (const patch of [
    { schema: 'kfm-local-library/v1' }, { files: -1 }, { files: 1.5 }, { by_status: [] }, { by_status: { ready: { files: 'x' } } },
    { by_status: { ready: { files: 30 } } }, { budget: budget({ level: 'fine' }) }, { budget: budget({ committed_bytes: -5 }) },
    { budget: budget({ data_ceiling_bytes: 90e9 }) }, { release_plan_bytes: undefined }, { running_run: 7 },
  ]) assert.equal(client.parseIntakeOverview(overview(patch)), null, JSON.stringify(patch));
  assert.equal(client.parseIntakeOverview(null), null);
});

test('intake desk is a fixed loopback origin and the client sends no credentials', async () => {
  assert.equal(client.INTAKE_DESK_ORIGIN, 'http://127.0.0.1:8771');
  const original = globalThis.fetch;
  let seen;
  globalThis.fetch = async (input, init) => { seen = { input, init }; return new Response(JSON.stringify(overview()), { status: 200, headers: { 'content-type': 'application/json' } }); };
  try {
    const result = await client.intakeOverviewRequest(new AbortController().signal);
    assert.equal(result.files, 21);
    assert.equal(seen.input, 'http://127.0.0.1:8771/api/overview');
    assert.deepEqual([seen.init.credentials, seen.init.cache, seen.init.redirect], ['omit', 'no-store', 'error']);
    globalThis.fetch = async () => new Response(JSON.stringify({ error: 'ORIGIN_REJECTED' }), { status: 403 });
    assert.equal(await client.intakeOverviewRequest(new AbortController().signal), null);
  } finally { globalThis.fetch = original; }
});

test('the library view mounts the read-only intake summary and the feature is registered', async () => {
  const workspace = await readFile('app/downloads/workspace.tsx', 'utf8');
  assert.match(workspace, /<div id="download-library"[^>]*><IntakeDeskSummary \/>/);
  const summary = await readFile('app/intake-desk-summary.tsx', 'utf8');
  assert.doesNotMatch(summary, /method:\s*"POST"|X-KFM-Session/);
  const features = await readFile('app/site-features.ts', 'utf8');
  assert.match(features, /id: "local-intake-desk"/);
});

import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const code = ts.transpileModule(await readFile('app/data-status/model.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
const model = await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);
const capacity = (extra = {}) => ({ format: 'kfm-database-capacity-v1', scope: 'visible-hosted-sql-tables', checkedAt: '2026-10-31T21:00:00Z', state: 'measured', targetBytes: 85e9, tables: 2, usedBytes: 1024, estimatedRows: 5, ...extra });
const local = () => ({ format: 'kfm-local-data-status-v1', scope: 'selected-local-catalogs', checkedAt: '2026-10-31T20:00:00Z',
  sql: { state: 'measured', targetBytes: 85e9, catalogCount: 2, usedBytes: 3000, journalBytes: 12 },
  intake: { state: 'measured', files: 3, counts: { ready: 0, reviewed: 2, review: 1, blocked: 0, other: 0 }, holds: [{ code: 'REVIEWED_LOCAL_ONLY', files: 2 }, { code: 'RIGHTS_UNKNOWN', files: 1 }] } });
const text = node => node == null || typeof node === 'boolean' ? '' : typeof node !== 'object' ? String(node) : [node.props?.children].flat(Infinity).map(text).join(' ').replace(/\s+/g, ' ');
test('status contracts preserve unknowns and reject inconsistent reports', () => {
  assert.equal(model.parseCapacity(capacity({ usedBytes: null })).usedBytes, null);
  assert.equal(model.parseCapacity(capacity({ usedBytes: 0 })).usedBytes, 0);
  assert.deepEqual(model.parseLocalReport(local()), local());
  for (const change of [{ usedBytes: -1 }, { state: 'unavailable' }, { targetBytes: 0 }, { checkedAt: 'invalid' }, { usedBytes: Number.MAX_SAFE_INTEGER + 1 }]) assert.throws(() => model.parseCapacity(capacity(change)));
  for (const mutate of [r => r.intake.files++, r => r.sql.journalBytes = 4000, r => r.intake.holds.push({ code: 'private message', files: 1 }), r => r.sql.state = 'unavailable']) {
    const report = local(); mutate(report); assert.throws(() => model.parseLocalReport(report));
  }
});
async function fixture(t) {
  const calls = [];
  const h = await componentHarness('app/data-status/dashboard.tsx', {
    'next/link': { default: 'a' }, '../hosted-source-status': { HostedSourceStatus: 'archive-status' }, './model': model,
    './dashboard.module.css': { default: {} }, '../browser-json-request': { browserJsonRequest: (url, options) => new Promise((resolve, reject) => calls.push({ url, options, resolve, reject })) },
  }, { fetch: () => assert.fail('local reports must never be uploaded') });
  t.after(() => h.dispose());
  const render = () => { const tree = h.render(h.exports.default, {}); h.commit(); return tree; };
  const reply = async (i, body) => { calls[i].resolve({ response: { ok: true }, body }); await settle(); };
  render(); return { h, calls, render, reply };
}
test('hosted failure keeps measurements unknown or explicitly stale and a later check recovers', async t => {
  const f = await fixture(t); assert.equal(f.calls[0].url, '/api/database-capacity'); assert.equal(f.calls[0].options.maxBytes, 16384);
  await f.reply(0, capacity());
  const refresh = () => findNode(f.render(), n => n.type === 'button' && text(n).includes('Refresh database')).props.onClick();
  refresh(); f.calls[1].reject(new Error('private credentials')); await settle();
  assert.match(text(f.render()), /Current measurement unknown/); assert.match(text(f.render()), /Previous check/);
  assert.doesNotMatch(text(f.render()), /private credentials/);
  refresh(); await f.reply(2, capacity({ state: 'unavailable', tables: null, usedBytes: null, estimatedRows: null }));
  assert.match(text(f.render()), /Database usage unknown/);
  assert.equal(findNode(f.render(), n => n.props?.label === 'Estimated hosted table and index usage').props.used, null);
});
test('local reports stay in memory, retain their dates and holds, and cannot arrive after Clear or unmount', async t => {
  const f = await fixture(t);
  const input = () => findNode(f.render(), n => n.type === 'input' && n.props.type === 'file');
  input().props.onChange({ target: { files: [{ size: 1000, text: async () => JSON.stringify(local()) }], value: 'report' } }); await settle();
  const output = text(f.render()); assert.match(output, /2026-10-31T20:00:00Z/); assert.match(output, /Local review is complete; sharing is still held/); assert.equal(f.calls.length, 1);
  input().props.onChange({ target: { files: [{ size: 65537, text: () => assert.fail('oversize reports must not be read') }], value: 'report' } }); await settle();
  assert.match(text(f.render()), /not a supported status report/); assert.match(text(f.render()), /2026-10-31T20:00:00Z/);
  let finish;
  input().props.onChange({ target: { files: [{ size: 100, text: () => new Promise(resolve => { finish = resolve; }) }], value: 'report' } });
  findNode(f.render(), n => n.type === 'button' && text(n) === 'Clear local report').props.onClick();
  finish(JSON.stringify(local())); await settle(); assert.match(text(f.render()), /unknown until a report is opened/);
  f.h.dispose(); assert.equal(f.calls[0].options.signal.aborted, true);
});

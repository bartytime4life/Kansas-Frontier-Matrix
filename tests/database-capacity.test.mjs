import test from 'node:test';
import assert from 'node:assert/strict';
import { createCapacityCheck } from '../server/database-capacity.mjs';

test('capacity reads only fixed aggregate metadata and closes the connection', async () => {
  const calls = []; let closed = 0;
  const check = createCapacityCheck({ options: async () => ({ options: { password: 'private-password' } }), connect: async () => ({
    query: async q => { calls.push(q); return [[{ tables_count: '13', allocated_bytes: '4703490048', estimated_rows: '101121013', private: 'secret' }]]; },
    destroy: () => closed++,
  }) });
  const result = await check();
  assert.equal(result.usedBytes, 4703490048); assert.equal(result.estimatedRows, 101121013); assert.equal(result.tables, 13);
  assert.equal(result.targetBytes, 85e9); assert.equal(result.scope, 'visible-hosted-sql-tables'); assert.equal(closed, 1);
  assert.equal(calls.length, 1); assert.equal(calls[0].timeout, 2000);
  assert.match(calls[0].sql, /FROM information_schema.TABLES WHERE TABLE_SCHEMA = DATABASE\(\)/);
  assert.doesNotMatch(calls[0].sql, /\b(?:INSERT|UPDATE|DELETE|ANALYZE|CREATE|DROP)\b/i);
  assert.doesNotMatch(JSON.stringify(result), /private|secret/);
});

test('metadata absence and failure remain unknown, while measured zeros stay zero', async () => {
  for (const [row, state, bytes, rows] of [
    [{ tables_count: 0, allocated_bytes: 0, estimated_rows: 0 }, 'measured', 0, 0],
    [{ tables_count: 1, allocated_bytes: null, estimated_rows: null }, 'measured', null, null],
    [{ tables_count: 1, allocated_bytes: '9007199254740993', estimated_rows: 7 }, 'unavailable', null, null],
    [{ tables_count: 1, allocated_bytes: -1, estimated_rows: 7 }, 'unavailable', null, null],
  ]) {
    const check = createCapacityCheck({ options: async () => ({ options: {} }), connect: async () => ({ query: async () => [[row]], destroy() {} }) });
    const result = await check(); assert.equal(result.state, state); assert.equal(result.usedBytes, bytes); assert.equal(result.estimatedRows, rows);
  }
  const check = createCapacityCheck({ environment: () => ({}), connect: async () => assert.fail('missing configuration must not connect') });
  assert.equal((await check()).reason, 'configuration-missing');
});

test('concurrent reads share failures and retry after the cache expires without driver details', async () => {
  let calls = 0, closed = 0, time = Date.now();
  const check = createCapacityCheck({ now: () => time, options: async () => ({ options: {} }), connect: async () => {
    calls++; return { query: async () => { throw new Error('private schema and password'); }, destroy: () => closed++ };
  } });
  const results = await Promise.all(Array.from({ length: 12 }, () => check()));
  assert.equal(calls, 1); assert.equal(closed, 1); assert.ok(results.every(r => r.usedBytes === null));
  assert.doesNotMatch(JSON.stringify(results), /private schema|password/);
  time += 59999; await check(); assert.equal(calls, 1);
  time += 2; await check(); assert.equal(calls, 2);
});

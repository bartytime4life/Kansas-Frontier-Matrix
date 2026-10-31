import test from 'node:test';
import assert from 'node:assert/strict';
import { DatabaseSync } from 'node:sqlite';
import { mkdtemp, rm, stat, link, writeFile, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { localDataStatus } from '../scripts/pc-pipeline/data-status.mjs';
const run = promisify(execFile);
async function fixture(t) {
  const root = await mkdtemp(join(tmpdir(), 'kfm-private-status-')); t.after(() => rm(root, { recursive: true, force: true }));
  const intake = join(root, 'private-source-index.sqlite');
  const db = new DatabaseSync(intake);
  db.exec('CREATE TABLE items(id TEXT, present INTEGER, status TEXT, decision_json TEXT)');
  const insert = db.prepare('INSERT INTO items VALUES (?,1,?,?)');
  insert.run('private-file-one', 'reviewed', JSON.stringify({ holds: ['REVIEWED_LOCAL_ONLY'] }));
  insert.run('private-file-two', 'review', JSON.stringify({ holds: ['RIGHTS_UNKNOWN', '/private/path-one', '/private/path-two'] }));
  insert.run('private-file-three', 'blocked', JSON.stringify({ holds: ['REVIEW_FLAGS'] }));
  db.exec("INSERT INTO items VALUES ('absent',0,'review','{}')"); db.close();
  return { root, intake };
}
test('private report measures selected files, deduplicates aliases and retains review/sharing distinctions', async t => {
  const { root, intake } = await fixture(t), alias = join(root, 'alias.sqlite');
  await link(intake, alias); await writeFile(intake + '-journal', Buffer.alloc(32));
  // The harmless test sidecar is measured; intake readback uses its own clean fixture.
  const queue = join(root, 'queue.sqlite'); await writeFile(queue, await readFile(intake));
  const report = await localDataStatus({ catalogs: [intake, alias], intake: queue });
  assert.equal(report.sql.catalogCount, 1); assert.equal(report.sql.journalBytes, 32);
  assert.equal(report.sql.usedBytes, (await stat(intake)).size + 32);
  assert.equal(report.sql.targetBytes, 85e9); assert.equal(report.intake.files, 3);
  assert.deepEqual(report.intake.counts, { ready: 0, reviewed: 1, review: 1, blocked: 1, other: 0 });
  assert.equal(report.intake.holds.find(r => r.code === 'OTHER').files, 1, 'two unknown holds on one file count once');
  assert.doesNotMatch(JSON.stringify(report), /private-file|private-source|private\/path|alias\.sqlite/);
});
test('an unreadable selected catalog never produces a misleading partial total', async t => {
  const { root, intake } = await fixture(t);
  const report = await localDataStatus({ catalogs: [intake, join(root, 'missing.sqlite')], intake });
  assert.equal(report.sql.state, 'unavailable'); assert.equal(report.sql.usedBytes, null); assert.equal(report.sql.catalogCount, null);
  assert.equal(report.intake.state, 'measured');
  const absent = await localDataStatus({ catalogs: [intake], intake: join(root, 'absent.sqlite') });
  assert.equal(absent.intake.files, null); assert.equal(absent.sql.state, 'measured');
});
test('report generation is read-only and the CLI creates a private file without replacing an existing report', async t => {
  const { root, intake } = await fixture(t), before = await readFile(intake), output = join(root, 'report.json');
  await run(process.execPath, ['scripts/pc-pipeline/data-status.mjs', '--catalog', intake, '--intake', intake, '--output', output]);
  const first = await readFile(output);
  assert.equal(JSON.parse(first).intake.files, 3); assert.equal((await stat(output)).mode & 0o777, 0o600);
  await assert.rejects(run(process.execPath, ['scripts/pc-pipeline/data-status.mjs', '--catalog', intake, '--intake', intake, '--output', output]));
  assert.deepEqual(await readFile(output), first); assert.deepEqual(await readFile(intake), before);
});

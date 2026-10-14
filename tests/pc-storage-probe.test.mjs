import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, symlink, stat, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { qualifyPcStorage } from '../server/pc-storage-probe.mjs';

test('cross-process lock, abrupt transaction death, integrity, and sentinel continuity', async () => {
  const root = await mkdtemp(join(tmpdir(),'kfm-pc-probe-'));
  try {
    const first = await qualifyPcStorage(root);
    assert.equal(first.crossProcessWriterLock,true);
    assert.equal(first.crashRollback,true);
    assert.equal(first.priorSentinelPresent,false);
    const second = await qualifyPcStorage(root);
    assert.equal(second.boots,2);
    assert.equal(second.priorSentinelPresent,true);
    assert.equal(second.persistenceAcrossRestart,'NEEDS_HOSTED_RESTART_AND_REDEPLOY');
    assert.equal((await stat(join(root,'kfm-pc-storage-probe-20261014','probe.sqlite'))).mode & 0o777,0o600);
  } finally { await rm(root,{recursive:true,force:true}); }
});
test('refuses symlink storage root', async () => {
  const root = await mkdtemp(join(tmpdir(),'kfm-pc-probe-'));
  try {
    await symlink(root,join(root,'link'));
    await assert.rejects(qualifyPcStorage(join(root,'link')),/ROOT_UNSAFE/);
  } finally { await rm(root,{recursive:true,force:true}); }
});

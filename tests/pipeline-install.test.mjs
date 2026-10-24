import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, writeFile, rm } from 'node:fs/promises';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { copyKit } from '../scripts/pc-pipeline/bundle.mjs';
const run = promisify(execFile);

test('installed kit loads worker and runs capture-only planner without checkout dependencies', async t => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-installed-kit-'));
  t.after(() => rm(root, { recursive: true, force: true }));
  await copyKit(root);
  const cli = resolve(root, 'scripts/pc-pipeline/cli.mjs');
  const config = resolve(root, 'config.json');
  await writeFile(config, JSON.stringify({ format: 'kfm-pc-pipeline-config-v1', root: '/srv/kfm-data/store', mount: '/srv/kfm-data',
    storeId: 'a'.repeat(32), device: 123, sources: ['nws-alerts','usgs-streamflow'], publish: false, approvalDirectory: '/etc/kfm-pipeline/approvals' }));
  const { stdout } = await run(process.execPath, [cli, 'plan', config], { cwd: root, timeout: 10000 });
  const plan = JSON.parse(stdout);
  assert.equal(plan.publicationEnabled, false);
  assert.equal(plan.capacity, 'unverified');
  const worker = pathToFileURL(resolve(root, 'scripts/pc-pipeline/worker.mjs')).href;
  const result = await run(process.execPath, ['--input-type=module', '-e', `const { tick } = await import(${JSON.stringify(worker)}); if (typeof tick !== 'function') process.exit(1);`], { cwd: root, timeout: 10000 });
  assert.equal(result.stdout, '');
});

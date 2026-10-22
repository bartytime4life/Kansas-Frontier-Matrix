import test from 'node:test';
import assert from 'node:assert/strict';
import { spawn, execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { mkdtemp } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
const run = promisify(execFile);
test('kernel operation lock excludes another writer and releases after a killed process', { skip: process.platform !== 'linux' }, async t => {
  const root = await mkdtemp(join(tmpdir(), 'kfm-operation-lock-')); const lock = join(root, 'operation.lock');
  const child = spawn('flock', ['--no-fork','--exclusive',lock,process.execPath,'-e',"process.stdout.write('LOCKED');setInterval(()=>{},1000)"], { stdio: ['ignore','pipe','pipe'] });
  t.after(() => child.kill('SIGKILL'));
  await new Promise((accept, reject) => {
    const timer = setTimeout(() => reject(new Error('LOCK_START_TIMEOUT')), 5000);
    child.on('error', reject); child.on('exit', () => reject(new Error('LOCK_PROCESS_EXITED')));
    child.stdout.once('data', data => { clearTimeout(timer); assert.match(data.toString(), /LOCKED/); accept(); });
  });
  await assert.rejects(run('flock', ['--exclusive','--nonblock','--conflict-exit-code=75',lock,process.execPath,'-e','']), e => e.code === 75);
  const exited = new Promise(accept => child.once('exit', accept)); child.kill('SIGKILL'); await exited;
  await run('flock', ['--exclusive','--nonblock','--conflict-exit-code=75',lock,process.execPath,'-e','']);
});

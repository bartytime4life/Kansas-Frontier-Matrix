import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, mkdir, readFile, readdir, lstat, symlink } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { EventEmitter } from 'node:events';
import { parseMemoryLimit, parseCpuQuota, readResourceLimits, runBoundedChild, qualifyHostedOllama, startHostedOllamaProbe } from '../server/hosted-ollama-probe.mjs';

test('memory capacity remains unknown for unlimited, absent, or malformed values', () => {
  for (const value of [undefined, null, '', 'max', '-1', '0', '4GB', 'Infinity', '9007199254740993']) {
    assert.equal(parseMemoryLimit(value), null, String(value));
  }
  assert.equal(parseMemoryLimit('4294967296\n'), 4294967296);
});

test('CPU quota uses quota/period; unlimited and malformed values remain unknown', () => {
  assert.equal(parseCpuQuota('200000 100000\n'), 2);
  assert.equal(parseCpuQuota('50000 100000'), 0.5);
  for (const value of ['max 100000', '0 100000', '-1 100000', '100 0', '', 'one two']) assert.equal(parseCpuQuota(value), null);
});

test('resource reader uses only fixed cgroup v2 paths and does not invent limits', async () => {
  const paths = [];
  const resources = await readResourceLimits(async path => {
    paths.push(path);
    if (path.endsWith('memory.max')) return 'max';
    if (path.endsWith('memory.current')) return '123456';
    throw new Error('missing');
  });
  assert.deepEqual(paths.sort(), ['/sys/fs/cgroup/cpu.max', '/sys/fs/cgroup/memory.current', '/sys/fs/cgroup/memory.max']);
  assert.equal(resources.cgroupV2MemoryMaxBytes, null);
  assert.equal(resources.cgroupV2MemoryCurrentBytes, 123456);
  assert.equal(resources.cgroupV2CpuQuotaCores, null);
});

test('resource reader rejects unexpectedly large filesystem content', async () => {
  const resources = await readResourceLimits(async () => '1'.repeat(5000));
  assert.equal(resources.cgroupV2MemoryMaxBytes, null);
});

function fakeSpawn(event) {
  return (executable, args, options) => {
    assert.equal(executable, '/fixed/verified-binary');
    assert.deepEqual(args, ['fixed-argument']);
    assert.equal(options.shell, false);
    assert.deepEqual(options.stdio, ['ignore', 'pipe', 'ignore']);
    const child = new EventEmitter();
    child.stdout = new EventEmitter();
    child.kill = () => true;
    queueMicrotask(() => event(child));
    return child;
  };
}

test('fixed child success requires its exact marker and zero exit', async () => {
  const result = await runBoundedChild('/fixed/verified-binary', ['fixed-argument'], 'marker', fakeSpawn(child => {
    child.stdout.emit('data', Buffer.from('marker')); child.emit('close', 0);
  }));
  assert.equal(result.status, 'PASS');
});

test('child execution denial is a finite failure without error text or stderr', async () => {
  const result = await runBoundedChild('/fixed/verified-binary', ['fixed-argument'], '', fakeSpawn(child => {
    child.emit('error', Object.assign(new Error('secret/path must not escape'), { code: 'EACCES' }));
  }));
  assert.deepEqual(result, { status: 'UNAVAILABLE', reason: 'EACCES' });
});

test('nonzero exit and wrong marker cannot become execution passes', async () => {
  for (const [code, output] of [[1, 'marker'], [0, 'different']]) {
    const result = await runBoundedChild('/fixed/verified-binary', ['fixed-argument'], 'marker', fakeSpawn(child => {
      child.stdout.emit('data', Buffer.from(output)); child.emit('close', code);
    }));
    assert.equal(result.status, 'UNAVAILABLE');
  }
});

test('child output is capped', async () => {
  const result = await runBoundedChild('/fixed/verified-binary', ['fixed-argument'], '', fakeSpawn(child => {
    child.stdout.emit('data', Buffer.from('x'.repeat(1025))); child.emit('close', 0);
  }));
  assert.equal(result.reason, 'CHILD_OUTPUT_LIMIT');
});

test('private receipt has restricted permissions, no model activation, and one retained attempt', async () => {
  const root = await mkdtemp(join(tmpdir(), 'kfm-ollama-probe-test-'));
  const calls = [];
  const receipt = await qualifyHostedOllama({ root,
    childRunner: async (file, args) => { calls.push({ file, args }); return { status: 'PASS' }; },
    loopback: async () => ({ status: 'PASS' }),
  });
  // These checks are injected primitives, not hosted Ollama execution evidence.
  assert.equal(receipt.status, 'BASELINE_PRIMITIVES_PASS');
  assert.equal(receipt.ollamaInstallation, 'NOT_ATTEMPTED');
  assert.equal(receipt.modelExecution, 'NOT_ATTEMPTED');
  assert.equal(calls.length, 2);
  assert.equal(calls[0].file, process.execPath);
  assert.deepEqual(calls[1].args, []);
  const directory = join(root, 'kfm-hosted-ollama-probe-20261016');
  const names = await readdir(directory);
  assert.equal(names.length, 3);
  assert.equal((await lstat(directory)).mode & 0o777, 0o700);
  const receiptFile = names.find(name => name.startsWith('receipt-'));
  assert.equal((await lstat(join(directory, receiptFile))).mode & 0o777, 0o600);
  assert.deepEqual(JSON.parse(await readFile(join(directory, receiptFile), 'utf8')), receipt);
  const script = names.find(name => name.startsWith('exec-'));
  assert.equal(await readFile(join(directory, script), 'utf8'), '#!/bin/sh\nexit 0\n');
  await assert.rejects(qualifyHostedOllama({ root }), { code: 'PROBE_ALREADY_ATTEMPTED' });
  assert.equal((await readdir(directory)).length, 3);
});

test('a primitive failure remains limited even when other primitives pass', async () => {
  const root = await mkdtemp(join(tmpdir(), 'kfm-ollama-probe-failure-'));
  const receipt = await qualifyHostedOllama({ root,
    childRunner: async () => ({ status: 'PASS' }),
    loopback: async () => { throw Object.assign(new Error('socket blocked'), { code: 'EPERM' }); },
  });
  assert.equal(receipt.status, 'BASELINE_LIMITED');
  assert.deepEqual(receipt.checks.loopback, { status: 'UNAVAILABLE', reason: 'EPERM' });
});

test('symlinked private root is rejected before writing', async () => {
  const parent = await mkdtemp(join(tmpdir(), 'kfm-ollama-probe-link-'));
  await mkdir(join(parent, 'real'));
  await symlink(join(parent, 'real'), join(parent, 'alias'));
  await assert.rejects(qualifyHostedOllama({ root: join(parent, 'alias') }), { code: 'PROBE_ROOT_UNSAFE' });
  assert.deepEqual(await readdir(join(parent, 'real')), []);
});

test('symlinked probe directory is rejected before writing', async () => {
  const root = await mkdtemp(join(tmpdir(), 'kfm-ollama-probe-child-link-'));
  await mkdir(join(root, 'real'));
  await symlink(join(root, 'real'), join(root, 'kfm-hosted-ollama-probe-20261016'));
  await assert.rejects(qualifyHostedOllama({ root }), { code: 'PROBE_DIRECTORY_UNSAFE' });
  assert.deepEqual(await readdir(join(root, 'real')), []);
});

test('default disabled entrypoint performs no qualification', async () => {
  let calls = 0;
  assert.deepEqual(await startHostedOllamaProbe(false, async () => { calls++; }), { status: 'DISABLED' });
  assert.equal(calls, 0);
});

test('startup qualification errors are contained and a process runs only one attempt', async () => {
  let calls = 0;
  const qualify = async () => { calls++; throw Object.assign(new Error('must not log secret text'), { code: 'EPERM' }); };
  assert.deepEqual(await startHostedOllamaProbe(true, qualify), { status: 'UNAVAILABLE', reason: 'EPERM' });
  assert.deepEqual(await startHostedOllamaProbe(true, qualify), { status: 'UNAVAILABLE', reason: 'EPERM' });
  assert.equal(calls, 1);
});

// Opt-in runtime qualification only: no model, download, credentials, or public route.
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { randomUUID } from 'node:crypto';
import { mkdir, lstat, chmod, writeFile, readFile, readdir, statfs } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { freemem, totalmem } from 'node:os';

const safeReason = error => /^[A-Z][A-Z0-9_]{0,63}$/.test(error?.code ?? '') ? error.code : 'CHECK_UNAVAILABLE';
const unavailable = error => ({ status: 'UNAVAILABLE', reason: safeReason(error) });

export function parseMemoryLimit(text) {
  const value = String(text ?? '').trim();
  if (!/^[1-9][0-9]{0,15}$/.test(value)) return null;
  const number = Number(value);
  return Number.isSafeInteger(number) && number < 2 ** 52 ? number : null;
}

export function parseCpuQuota(text) {
  const match = /^([1-9][0-9]{0,11}) ([1-9][0-9]{0,11})$/.exec(String(text ?? '').trim());
  if (!match) return null;
  const value = Number(match[1]) / Number(match[2]);
  return Number.isFinite(value) && value > 0 ? value : null;
}

export async function readResourceLimits(readText = path => readFile(path, 'utf8')) {
  const boundedRead = async path => {
    try { const text = await readText(path); return typeof text === 'string' && text.length <= 4096 ? text : null; }
    catch { return null; }
  };
  const [memory, current, cpu] = await Promise.all([
    boundedRead('/sys/fs/cgroup/memory.max'),
    boundedRead('/sys/fs/cgroup/memory.current'),
    boundedRead('/sys/fs/cgroup/cpu.max'),
  ]);
  return {
    cgroupV2MemoryMaxBytes: parseMemoryLimit(memory),
    cgroupV2MemoryCurrentBytes: parseMemoryLimit(current),
    cgroupV2CpuQuotaCores: parseCpuQuota(cpu),
    quotaInterpretation: 'Mounted cgroup v2 values only; unavailable/unlimited is not capacity confirmation. Ancestor limits and provider quotas require separate verification.',
  };
}

// Fixed argv, no shell, bounded lifetime/output. Failure never exposes stderr.
export function runBoundedChild(executable, args, expectedOutput = '', spawnChild = spawn) {
  return new Promise(resolveChild => {
    let child, output = '', settled = false, timer;
    const finish = result => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      resolveChild(result);
    };
    try {
      child = spawnChild(executable, args, { stdio: ['ignore', 'pipe', 'ignore'], shell: false });
      timer = setTimeout(() => { child.kill('SIGKILL'); finish({ status: 'UNAVAILABLE', reason: 'CHILD_TIMEOUT' }); }, 3000);
      child.stdout.on('data', chunk => {
        output += chunk.toString('utf8');
        if (output.length > 1024) { child.kill('SIGKILL'); finish({ status: 'UNAVAILABLE', reason: 'CHILD_OUTPUT_LIMIT' }); }
      });
      child.once('error', error => finish(unavailable(error)));
      child.once('close', code => finish(code === 0 && output === expectedOutput
        ? { status: 'PASS' } : { status: 'UNAVAILABLE', reason: 'CHILD_CHECK_FAILED' }));
    } catch (error) { finish(unavailable(error)); }
  });
}

export async function checkLoopback() {
  const marker = randomUUID();
  const server = createServer((_request, response) => {
    response.writeHead(200, { 'Content-Type': 'text/plain', 'Cache-Control': 'no-store' });
    response.end(marker);
  });
  try {
    await new Promise((resolveListen, reject) => {
      server.once('error', reject);
      server.listen({ host: '127.0.0.1', port: 0 }, resolveListen);
    });
    const address = server.address();
    const response = await fetch(`http://127.0.0.1:${address.port}/`, {
      redirect: 'error', signal: AbortSignal.timeout(2000),
    });
    const text = await response.text();
    return response.status === 200 && text === marker
      ? { status: 'PASS' } : { status: 'UNAVAILABLE', reason: 'LOOPBACK_CHECK_FAILED' };
  } catch (error) { return unavailable(error); }
  finally {
    server.closeAllConnections();
    if (server.listening) await new Promise(resolveClose => server.close(resolveClose));
  }
}

export async function qualifyHostedOllama({ root = '/private', childRunner = runBoundedChild, loopback = checkLoopback } = {}) {
  const absoluteRoot = resolve(root);
  const rootInfo = await lstat(absoluteRoot);
  if (!rootInfo.isDirectory() || rootInfo.isSymbolicLink()) throw Object.assign(new Error('Unsafe root'), { code: 'PROBE_ROOT_UNSAFE' });
  const directory = join(absoluteRoot, 'kfm-hosted-ollama-probe-20261016');
  try { await mkdir(directory, { mode: 0o700 }); } catch (error) { if (error.code !== 'EEXIST') throw error; }
  const directoryInfo = await lstat(directory);
  if (!directoryInfo.isDirectory() || directoryInfo.isSymbolicLink() || directoryInfo.uid !== process.getuid()) {
    throw Object.assign(new Error('Unsafe probe directory'), { code: 'PROBE_DIRECTORY_UNSAFE' });
  }
  await chmod(directory, 0o700);
  // One retained attempt per directory, fenced across processes. Preserve any
  // interrupted attempt for inspection instead of retrying or accumulating files.
  if ((await readdir(directory)).length !== 0) throw Object.assign(new Error('Probe already attempted'), { code: 'PROBE_ALREADY_ATTEMPTED' });
  try { await writeFile(join(directory, '.attempt'), 'kfm.hosted-ollama-baseline/20261016/v1\n', { mode: 0o600, flag: 'wx' }); }
  catch (error) {
    if (error.code === 'EEXIST') throw Object.assign(new Error('Probe already attempted'), { code: 'PROBE_ALREADY_ATTEMPTED' });
    throw error;
  }
  const runId = randomUUID();
  const executable = join(directory, `exec-${runId}.sh`);
  // Its fixed body exits immediately. There is no user-supplied command or argument.
  await writeFile(executable, '#!/bin/sh\nexit 0\n', { mode: 0o700, flag: 'wx' });
  const [nodeChild, privateExecution, loopbackResult, resources, filesystem] = await Promise.all([
    childRunner(process.execPath, ['-e', "process.stdout.write('kfm-hosted-probe-ok')"], 'kfm-hosted-probe-ok'),
    childRunner(executable, []),
    loopback().catch(unavailable),
    readResourceLimits(),
    statfs(absoluteRoot).then(info => ({ status: 'OBSERVED', filesystemType: info.type,
      availableBytes: info.bavail * info.bsize,
      interpretation: 'Filesystem observation only; not a provider storage quota.' })).catch(unavailable),
  ]);
  const receipt = {
    profile: 'kfm.hosted-ollama-baseline/20261016/v1', runId,
    observedAt: new Date().toISOString(),
    status: [nodeChild, privateExecution, loopbackResult].every(check => check.status === 'PASS')
      ? 'BASELINE_PRIMITIVES_PASS' : 'BASELINE_LIMITED',
    node: process.versions.node, platform: process.platform, arch: process.arch,
    processRssBytes: process.memoryUsage().rss,
    hostReportedTotalMemoryBytes: totalmem(), hostReportedFreeMemoryBytes: freemem(),
    hostMemoryInterpretation: 'Host-reported values are not proof of this app allocation.',
    checks: { nodeChild, privateExecution, loopback: loopbackResult }, resources, filesystem,
    limits: { maximumRetainedAttempts: 1, outputBytesPerChild: 1024, childTimeoutMilliseconds: 3000 },
    ollamaInstallation: 'NOT_ATTEMPTED', modelExecution: 'NOT_ATTEMPTED',
    sensitivity: 'No credentials, environment values, account/job data, prompts, or datasets are collected.',
    nextGate: 'Verify effective app RAM/disk allocation, native Ollama load and supervision, pinned model identity/license, bounded CPU/RAM/latency, and governed evidence integration before activation.',
  };
  await writeFile(join(directory, `receipt-${runId}.json`), JSON.stringify(receipt, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
  return receipt;
}

let startupCheck;
export function startHostedOllamaProbe(enabled = process.env.KFM_OLLAMA_BASELINE_PROBE === '1', qualify = qualifyHostedOllama) {
  if (!enabled) return Promise.resolve({ status: 'DISABLED' });
  if (!startupCheck) startupCheck = qualify().then(receipt => {
    console.info(`KFM hosted Ollama baseline: ${receipt.status}; private receipt saved; no model installed.`);
    return receipt;
  }).catch(error => {
    const result = unavailable(error);
    console.info(`KFM hosted Ollama baseline: ${result.reason}; map startup remains independent.`);
    return result;
  });
  return startupCheck;
}

// Disposable, non-secret storage qualification. Never touches application data.
import { DatabaseSync } from 'node:sqlite';
import { mkdir, lstat, chmod, statfs } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { join, resolve } from 'node:path';

const marker = 'kfm.pc-storage-probe/20261014/v1';
const modulePath = fileURLToPath(import.meta.url);
const child = (args, killOnReady = false) => new Promise((resolveChild, reject) => {
  const processChild = spawn(process.execPath, [modulePath, ...args], { stdio: ['ignore', 'pipe', 'pipe'] });
  let output = '', errors = '';
  const timer = setTimeout(() => { processChild.kill('SIGKILL'); reject(new Error('PROBE_CHILD_TIMEOUT')); }, 7000);
  processChild.stdout.on('data', chunk => {
    output += chunk.toString();
    if (killOnReady && output.includes('ready')) processChild.kill('SIGKILL');
  });
  processChild.stderr.on('data', chunk => { errors += chunk.toString(); });
  processChild.on('error', error => { clearTimeout(timer); reject(error); });
  processChild.on('exit', (code, signal) => {
    clearTimeout(timer);
    if (killOnReady && signal === 'SIGKILL' && output.includes('ready')) resolveChild(true);
    else if (code === 0) resolveChild(true);
    else reject(new Error(`PROBE_CHILD_FAILED:${code}:${errors.slice(0,200)}`));
  });
});

export async function qualifyPcStorage(root = '/private') {
  const rootInfo = await lstat(root);
  if (!rootInfo.isDirectory() || rootInfo.isSymbolicLink()) throw new Error('PROBE_ROOT_UNSAFE');
  const directory = join(resolve(root), 'kfm-pc-storage-probe-20261014');
  try { await mkdir(directory, { mode: 0o700 }); } catch (error) { if (error.code !== 'EEXIST') throw error; }
  const directoryInfo = await lstat(directory);
  if (!directoryInfo.isDirectory() || directoryInfo.isSymbolicLink() || directoryInfo.uid !== process.getuid()) throw new Error('PROBE_DIRECTORY_UNSAFE');
  await chmod(directory, 0o700);
  const file = join(directory, 'probe.sqlite');
  try {
    const info = await lstat(file);
    if (!info.isFile() || info.isSymbolicLink() || info.nlink !== 1 || info.uid !== process.getuid() || info.size > 1024 * 1024) throw new Error('PROBE_FILE_UNSAFE');
  } catch (error) { if (error.code !== 'ENOENT') throw error; }
  const db = new DatabaseSync(file);
  try {
    await chmod(file, 0o600);
    db.exec('PRAGMA busy_timeout=1000; PRAGMA journal_mode=DELETE; PRAGMA synchronous=FULL;');
    db.exec('CREATE TABLE IF NOT EXISTS probe (id INTEGER PRIMARY KEY CHECK(id=1), marker TEXT NOT NULL, boots INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS disposable (value TEXT NOT NULL);');
    const prior = db.prepare('SELECT marker, boots FROM probe WHERE id=1').get();
    if (prior && prior.marker !== marker) throw new Error('PROBE_IDENTITY_CONFLICT');
    db.prepare('INSERT INTO probe VALUES (1,?,1) ON CONFLICT(id) DO UPDATE SET boots=boots+1').run(marker);
    db.exec('BEGIN IMMEDIATE');
    try { await child(['lock', file]); } finally { db.exec('ROLLBACK'); }
    await child(['crash', file], true);
    if (db.prepare('SELECT COUNT(*) AS n FROM disposable').get().n !== 0) throw new Error('PROBE_CRASH_ROLLBACK_FAILED');
    if (db.prepare('PRAGMA integrity_check').get().integrity_check !== 'ok') throw new Error('PROBE_INTEGRITY_FAILED');
    const fs = await statfs(root);
    return { profile: marker, status: 'LOCAL_STORAGE_CHECKS_PASS', boots: Number(prior?.boots ?? 0)+1,
      priorSentinelPresent: Boolean(prior), crossProcessWriterLock: true, crashRollback: true,
      integrity: 'ok', filesystemType: fs.type, freeBytes: fs.bavail * fs.bsize,
      persistenceAcrossRestart: 'NEEDS_HOSTED_RESTART_AND_REDEPLOY', multiReplicaTopology: 'NEEDS_PROVIDER_VERIFICATION',
      node: process.versions.node };
  } finally { db.close(); }
}

if (process.argv[1] === modulePath && ['lock','crash'].includes(process.argv[2])) {
  const db = new DatabaseSync(process.argv[3]);
  db.exec('PRAGMA busy_timeout=250; PRAGMA journal_mode=DELETE; PRAGMA synchronous=FULL');
  if (process.argv[2] === 'lock') {
    try { db.exec('BEGIN IMMEDIATE'); db.exec('ROLLBACK'); process.exitCode=1; }
    catch (error) { if (!/locked|busy/i.test(error.message)) throw error; }
    db.close();
  } else {
    db.exec("BEGIN IMMEDIATE; INSERT INTO disposable VALUES ('uncommitted non-secret test');");
    process.stdout.write('ready\n');
    setInterval(() => {},1000);
  }
}

#!/usr/bin/env node
/** Called under the existing kernel lock; retains tick's stdout and exit contract. */
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { randomUUID } from 'node:crypto';
import { writeFile, rename, unlink, lstat } from 'node:fs/promises';
import { loadConfig, tick } from './worker.mjs';
import { operatorHealth, operatorState } from './health.mjs';
import { directory, storageGuard } from '../../server/pipeline-files.mjs';
export async function writeOperatorReport(config, configPath, runDirectory, { guard = storageGuard, readHealth = operatorHealth, lastTick } = {}) {
  // Never write a fallback directory when the expected data mount is absent.
  await guard(config);
  const report = await readHealth(configPath, runDirectory);
  if (lastTick) {
    report.lastTick = { state: lastTick.state === 'held' ? 'held' : 'complete', finishedAt: new Date().toISOString(),
      reason: /^[A-Z][A-Z_]{1,63}$/.test(lastTick.reason ?? '') ? lastTick.reason : null };
    report.state = operatorState(report);
  }
  const parent = resolve(config.root, 'data/work'); await directory(parent, true);
  const target = resolve(parent, 'pipeline-health.json');
  try { const info = await lstat(target); if (!info.isFile() || info.isSymbolicLink()) throw new Error('HEALTH_TARGET_UNSAFE'); }
  catch (error) { if (error.code !== 'ENOENT') throw error; }
  const temp = resolve(parent, '.pipeline-health-' + randomUUID() + '.tmp');
  try { await writeFile(temp, JSON.stringify(report), { flag: 'wx', mode: 0o600 }); await rename(temp, target); }
  finally { await unlink(temp).catch(error => { if (error.code !== 'ENOENT') throw error; }); }
  return report;
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const safe = error => /^[A-Z][A-Z_]{1,63}$/.test(error?.message ?? '') ? error.message : 'PIPELINE_OPERATION_FAILED';
  let config, lastTick;
  try {
    config = await loadConfig(resolve(process.argv[2]));
    const result = await tick(config); console.log(JSON.stringify(result));
    lastTick = result.outcomes.some(outcome => outcome.state === 'held') ? { state: 'held', reason: 'SOURCE_JOB_HELD' } : { state: 'complete' };
  }
  catch (error) { lastTick = { state: 'held', reason: safe(error) }; console.error(JSON.stringify(lastTick)); process.exitCode = 1; }
  if (config) try { await writeOperatorReport(config, resolve(process.argv[2]), resolve(process.argv[3]), { lastTick }); }
  catch (error) { console.error(JSON.stringify({ state: 'diagnostic-held', reason: safe(error) })); }
}

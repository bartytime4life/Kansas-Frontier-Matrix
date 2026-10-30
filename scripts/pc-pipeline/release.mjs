#!/usr/bin/env node
// Builds a commit-named copy of the PC kit for the user-level units, so checkout edits never change running code.
import { execFileSync } from 'node:child_process';
import { lstat, mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { KIT_FILES, copyKit } from './bundle.mjs';
import { canonical, fail } from '../../server/pipeline-contract.mjs';
import { hashFile } from '../../server/pipeline-files.mjs';

const checkout = fileURLToPath(new URL('../..', import.meta.url));
const git = (...args) => execFileSync('git', args, { cwd: checkout, encoding: 'utf8' });

export async function buildRelease(releasesRoot, { run = git, copy = copyKit } = {}) {
  if (!releasesRoot?.startsWith('/')) fail('ABSOLUTE_ROOT_REQUIRED');
  const commit = run('rev-parse', 'HEAD').trim(); if (!/^[a-f0-9]{40}$/.test(commit)) fail('COMMIT_INVALID');
  // Only committed bytes may run: a modified or untracked kit file would make the commit name false.
  if (run('status', '--porcelain', '--untracked-files=all', '--', ...KIT_FILES).trim()) fail('KIT_CHECKOUT_MODIFIED');
  const target = resolve(releasesRoot, commit);
  try { await lstat(target); fail('RELEASE_EXISTS'); } catch (error) { if (error.code !== 'ENOENT') throw error; }
  await mkdir(target, { recursive: true, mode: 0o700 });
  await copy(target);
  const files = {};
  for (const name of KIT_FILES) files[name] = (await hashFile(resolve(target, name))).sha256;
  // A release copy never carries credentials or enables publication; the active config decides that.
  const record = { sourceCommit: commit, publicationEnabled: false, files };
  await writeFile(resolve(target, 'release.json'), canonical(record), { flag: 'wx', mode: 0o600 });
  return { state: 'built', path: target, ...record };
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { console.log(canonical(await buildRelease(process.argv[2]))); }
  catch (error) { console.error(canonical({ state: 'held', reason: /^[A-Z][A-Z_]{1,63}$/.test(error.message ?? '') ? error.message : 'RELEASE_BUILD_FAILED' })); process.exitCode = 1; }
}

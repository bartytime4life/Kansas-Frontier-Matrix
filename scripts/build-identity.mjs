import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { lstat, readdir, readFile, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

// Only application inputs. No environment, persisted stores, model cache, Git
// credentials, build outputs, or generated browser assets enter this digest.
const roots = ['app', 'server', 'scripts', 'public', 'vendor', 'worker', 'db', 'drizzle'];
const files = ['package.json', 'package-lock.json', 'godaddy-source.json', 'next.config.ts', 'vite.config.ts', 'tsconfig.json', 'postcss.config.mjs'];
const excluded = new Set(['app/build-info.generated.json', 'public/assets', 'public/maplibre', 'public/vendor/h5wasm']);
export const BUILD_PROFILE = 'kfm.godaddy-application-inputs/v1';
export const BUILD_APPLICATION = 'urdng3v1vk';

function isApplicationFile(path) {
  const parts = path.split('/');
  return (files.includes(path) || roots.some(root => path.startsWith(root + '/'))) &&
    !parts.some(part => part.startsWith('.')) &&
    !parts.slice(0, -1).includes('__pycache__') &&
    ![...excluded].some(entry => path === entry || path.startsWith(entry + '/'));
}

// Counts only. /api/build is public, so no path or file name from the host's
// checkout is published; the counts say which kind of entry Git reports.
function worktreeChangeCounts(status) {
  const counts = { trackedInputs: 0, trackedOther: 0, untrackedInputs: 0, untrackedOther: 0 };
  const records = status.split('\0');
  for (let index = 0; index < records.length; index += 1) {
    const record = records[index];
    if (record.length < 4) continue;
    const state = record.slice(0, 2);
    // A rename or copy is followed by its original path as a separate record.
    if (/[RC]/.test(state)) index += 1;
    const kind = state === '??' ? 'untracked' : 'tracked';
    counts[kind + (isApplicationFile(record.slice(3).replace(/\/$/, '')) ? 'Inputs' : 'Other')] += 1;
  }
  return counts;
}

export async function applicationIdentity(root = process.cwd()) {
  const entries = [];
  const blobHashes = new Map();
  async function visit(path, optional = false) {
    if (excluded.has(path)) return;
    let stat;
    try { stat = await lstat(resolve(root, path)); }
    catch (error) { if (optional && error.code === 'ENOENT') return; throw error; }
    if (stat.isSymbolicLink()) throw new Error('SOURCE_SYMLINK_HELD');
    if (stat.isDirectory()) {
      // Python bytecode caches are generated outputs, even under source roots.
      if (path.split('/').at(-1) === '__pycache__') return;
      for (const name of (await readdir(resolve(root, path))).sort()) {
        if (!name.startsWith('.')) await visit(`${path}/${name}`);
      }
    } else if (stat.isFile()) {
      const bytes = await readFile(resolve(root, path));
      entries.push([path, createHash('sha256').update(bytes).digest('hex')]);
      // Hash the same observed bytes as a Git blob; status/index flags and
      // clean filters must not substitute different bytes for this comparison.
      blobHashes.set(path, createHash('sha1').update(`blob ${bytes.length}\0`).update(bytes).digest('hex'));
    } else throw new Error('SOURCE_FILE_TYPE_HELD');
  }
  for (const path of files) await visit(path);
  for (const path of roots) await visit(path, true);
  entries.sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0);
  const sourceDigest = 'sha256:' + createHash('sha256').update(JSON.stringify(entries)).digest('hex');
  let sourceCommit = null;
  let commitState = 'GIT_UNAVAILABLE';
  let worktreeChanges = null;
  try {
    const options = { cwd: root, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'], timeout: 5000 };
    if (resolve(execFileSync('git', ['rev-parse', '--show-toplevel'], options).trim()) !== resolve(root)) throw new Error('NOT_THIS_CHECKOUT');
    const commit = execFileSync('git', ['rev-parse', 'HEAD'], options).trim();
    const status = execFileSync('git', ['status', '--porcelain', '-z', '--untracked-files=normal'], options);
    if (/^[a-f0-9]{40}$/.test(commit) && status === '') {
      // One immutable tree read verifies paths and bytes against the commit,
      // including edits/deletions hidden by assume-unchanged or skip-worktree.
      const committed = new Map();
      const tree = execFileSync('git', ['ls-tree', '-r', '-z', '--full-tree', commit], options);
      for (const record of tree.split('\0').filter(Boolean)) {
        const separator = record.indexOf('\t');
        const [mode, type, hash] = record.slice(0, separator).split(' ');
        const path = record.slice(separator + 1);
        if (isApplicationFile(path)) committed.set(path, type === 'blob' && /^100(?:644|755)$/.test(mode) ? hash : null);
      }
      if (entries.some(([path]) => !committed.has(path))) commitState = 'UNTRACKED_APPLICATION_INPUTS';
      else if ([...committed].some(([path, hash]) => !hash || blobHashes.get(path) !== hash)) commitState = 'WORKTREE_MODIFIED';
      else { sourceCommit = commit; commitState = 'CLEAN_CHECKOUT'; }
    } else {
      commitState = 'WORKTREE_MODIFIED';
      if (status !== '') worktreeChanges = worktreeChangeCounts(status);
    }
  } catch { /* Archive builds still have an independently comparable digest. */ }
  return { profile: BUILD_PROFILE, application: BUILD_APPLICATION, sourceDigest,
    sourceFileCount: entries.length, sourceCommit, commitState,
    ...(worktreeChanges ? { worktreeChanges } : {}),
    scope: 'Application source inputs only; excludes build bytes, live data, settings, models, and release authority.' };
}

// Every browser file a build has staged stays in public/assets, so that a page opened before a publish can
// still load its scripts after it, and the build refuses to finish once that folder passes a fixed number
// of entries or bytes. Nothing outside the host can list the folder, so the build records how much of each
// limit was used when it started. Counts only: no file name is published.
// This file runs on its own in a fresh tree, so it states the two limits itself; a test holds them equal to
// the ones scripts/stage-public-client-assets.mjs enforces.
const CLIENT_ASSET_ENTRY_LIMIT = 4096, CLIENT_ASSET_BYTE_LIMIT = 256 * 1024 * 1024;
export async function retainedClientAssets(root = process.cwd()) {
  let entries = 0, bytes = 0;
  try {
    const folder = resolve(root, 'public/assets');
    for (const entry of await readdir(folder, { withFileTypes: true })) {
      entries += 1;
      if (entry.isFile()) bytes += (await lstat(resolve(folder, entry.name))).size;
    }
  } catch { return null; }
  return entries ? { entries, bytes, entryLimit: CLIENT_ASSET_ENTRY_LIMIT, byteLimit: CLIENT_ASSET_BYTE_LIMIT } : null;
}

export async function verifyHostedIdentity(expected, origin, fetcher = fetch) {
  const url = new URL(origin);
  if (url.username || url.password || url.search || url.hash || url.pathname !== '/' ||
      !(url.protocol === 'https:' || (url.protocol === 'http:' && ['127.0.0.1', 'localhost', '[::1]'].includes(url.hostname)))) {
    throw new Error('INVALID_VERIFICATION_ORIGIN');
  }
  url.pathname = '/api/build';
  const response = await fetcher(url, { cache: 'no-store', redirect: 'error', signal: AbortSignal.timeout(10000) });
  if (!response.ok || !response.headers.get('content-type')?.includes('application/json')) throw new Error('HOSTED_IDENTITY_UNAVAILABLE');
  const reader = response.body.getReader();
  const chunks = [];
  let size = 0;
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      size += value.byteLength;
      if (size > 4096) throw new Error('HOSTED_IDENTITY_INVALID');
      chunks.push(value);
    }
  } finally { await reader.cancel(); }
  let actual;
  try { actual = JSON.parse(Buffer.concat(chunks).toString('utf8')); }
  catch { throw new Error('HOSTED_IDENTITY_INVALID'); }
  if (actual?.profile !== BUILD_PROFILE || actual.application !== expected.application ||
      !/^sha256:[a-f0-9]{64}$/.test(actual.sourceDigest) || !Number.isSafeInteger(actual.sourceFileCount) || actual.sourceFileCount < 1) {
    throw new Error('HOSTED_IDENTITY_INVALID');
  }
  const matches = actual.sourceDigest === expected.sourceDigest && actual.sourceFileCount === expected.sourceFileCount;
  return { outcome: matches ? 'APPLICATION_INPUTS_MATCH' : 'APPLICATION_INPUTS_DIFFER',
    origin: url.origin, expectedDigest: expected.sourceDigest, observedDigest: actual.sourceDigest,
    scope: expected.scope };
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  try {
    const identity = await applicationIdentity();
    if (process.argv[2] === '--verify' && process.argv.length === 4) {
      const result = await verifyHostedIdentity(identity, process.argv[3]);
      console.log(JSON.stringify(result));
      if (result.outcome !== 'APPLICATION_INPUTS_MATCH') process.exitCode = 1;
    } else if (process.argv[2] === '--print' && process.argv.length === 3) console.log(JSON.stringify(identity));
    else if (process.argv.length === 2) {
      // Recorded for this build only; --print and --verify compare application inputs and leave it out.
      const retained = await retainedClientAssets();
      await writeFile('app/build-info.generated.json', JSON.stringify({ ...identity, ...(retained ? { retainedClientAssets: retained } : {}) }, null, 2) + '\n');
      console.log('Application identity: ' + identity.sourceDigest + ' (' + identity.commitState + ')');
      if (identity.worktreeChanges) console.log('Checkout entries Git reports as changed: ' + JSON.stringify(identity.worktreeChanges));
      if (retained) console.log('Browser files kept from earlier builds: ' + retained.entries + ' of ' + retained.entryLimit + ' entries, ' + Math.round(retained.bytes / 1048576) + ' of ' + Math.round(retained.byteLimit / 1048576) + ' MB');
    } else throw new Error('USAGE: node scripts/build-identity.mjs [--print | --verify ORIGIN]');
  } catch (error) { console.error(error.message); process.exitCode = 1; }
}

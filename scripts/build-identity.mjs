import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { lstat, readdir, readFile, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

// Only application inputs. No environment, persisted stores, model cache, Git
// credentials, build outputs, or generated browser assets enter this digest.
const roots = ['app', 'build', 'scripts', 'public', 'vendor', 'worker', 'db', 'drizzle'];
const files = ['package.json', 'package-lock.json', '.openai/hosting.json', 'next.config.ts', 'vite.config.ts', 'tsconfig.json', 'postcss.config.mjs'];
const excluded = new Set(['app/build-info.generated.json', 'public/maplibre', 'public/vendor/h5wasm']);
export const BUILD_PROFILE = 'kfm.sites-application-inputs/v1';

export async function applicationIdentity(root = process.cwd()) {
  const entries = [];
  async function visit(path, optional = false) {
    if (excluded.has(path)) return;
    let stat;
    try { stat = await lstat(resolve(root, path)); }
    catch (error) { if (optional && error.code === 'ENOENT') return; throw error; }
    if (stat.isSymbolicLink()) throw new Error('SOURCE_SYMLINK_HELD');
    if (stat.isDirectory()) {
      for (const name of (await readdir(resolve(root, path))).sort()) {
        if (!name.startsWith('.')) await visit(`${path}/${name}`);
      }
    } else if (stat.isFile()) {
      entries.push([path, createHash('sha256').update(await readFile(resolve(root, path))).digest('hex')]);
    } else throw new Error('SOURCE_FILE_TYPE_HELD');
  }
  for (const path of files) await visit(path);
  for (const path of roots) await visit(path, true);
  entries.sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0);
  const sourceDigest = 'sha256:' + createHash('sha256').update(JSON.stringify(entries)).digest('hex');
  let sourceCommit = null;
  let commitState = 'GIT_UNAVAILABLE';
  try {
    const options = { cwd: root, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'], timeout: 5000 };
    if (resolve(execFileSync('git', ['rev-parse', '--show-toplevel'], options).trim()) !== resolve(root)) throw new Error('NOT_THIS_CHECKOUT');
    const commit = execFileSync('git', ['rev-parse', 'HEAD'], options).trim();
    const status = execFileSync('git', ['status', '--porcelain', '--untracked-files=normal'], options).trim();
    if (/^[a-f0-9]{40}$/.test(commit) && status === '') { sourceCommit = commit; commitState = 'CLEAN_CHECKOUT'; }
    else commitState = 'WORKTREE_MODIFIED';
  } catch { /* Archive builds still have an independently comparable digest. */ }
  return { profile: BUILD_PROFILE, application: 'appgprj_6acd1aafe0d88191a4306ea2ab44ed91', sourceDigest,
    sourceFileCount: entries.length, sourceCommit, commitState,
    scope: 'Application source inputs only; excludes build bytes, live data, settings, models, and release authority.' };
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
      await writeFile('app/build-info.generated.json', JSON.stringify(identity, null, 2) + '\n');
      console.log('Application identity: ' + identity.sourceDigest + ' (' + identity.commitState + ')');
    } else throw new Error('USAGE: node scripts/build-identity.mjs [--print | --verify ORIGIN]');
  } catch (error) { console.error(error.message); process.exitCode = 1; }
}

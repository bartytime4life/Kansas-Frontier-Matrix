/** GHSA-67mh-4wv8-2f99: lockfile guards; optional synthetic loopback probes. */
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { mkdtemp, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import { realpathSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import test from 'node:test';

const app = fileURLToPath(new URL('../', import.meta.url));
const root = path.resolve(app, '../..');
const fixed = '0.28.2';
const read = (p) => readFile(p, 'utf8');
const json = async (p) => JSON.parse(await read(p));
const runtime = process.env.KFM_ESBUILD_RUNTIME_PROBE === '1';

function isPatched(version) {
  const match = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/.exec(version ?? '');
  if (!match) return false; // Unknown, ranges, and prereleases are not accepted.
  const [major, minor] = match.slice(1).map(Number);
  return major > 0 || minor >= 25;
}

function npmEsbuild(lock) {
  assert.equal(lock.lockfileVersion, 3);
  assert.ok(lock.packages && typeof lock.packages === 'object');
  const entries = Object.entries(lock.packages).filter(([p]) =>
    /(?:^|\/)node_modules\/(?:esbuild|@esbuild\/[^/]+)$/.test(p));
  assert.ok(entries.some(([p]) => /(?:^|\/)node_modules\/esbuild$/.test(p)), 'esbuild must be inventoried');
  return entries;
}

function pnpmEsbuild(text) {
  assert.match(text, /^lockfileVersion: ['"]9\.0['"]$/m);
  const entries = [...text.matchAll(/^  ['"]?(esbuild@[^\s:'"]+)['"]?:/gm)].map((m) => m[1]);
  assert.ok(entries.length > 0, 'esbuild package/snapshot keys must be inventoried');
  return entries;
}

test('security floor rejects vulnerable, malformed, and prerelease versions', () => {
  for (const v of ['0.18.20', '0.24.2', '0.24.99', '0.25.0-beta.1', '^0.28.2', '', null]) {
    assert.equal(isPatched(v), false, String(v));
  }
  for (const v of ['0.25.0', '0.25.12', '0.28.2', '1.0.0']) assert.equal(isPatched(v), true);
  assert.throws(() => npmEsbuild({ lockfileVersion: 3, packages: {} }));
  assert.throws(() => pnpmEsbuild("lockfileVersion: '9.0'\n"));
});

test('standalone npm lock contains no affected esbuild or platform binary', async () => {
  for (const [p, entry] of npmEsbuild(await json(path.join(app, 'package-lock.json')))) {
    assert.ok(isPatched(entry.version), `${p}: ${entry.version}`);
  }
});

test('workspace pnpm lock contains no affected esbuild package or snapshot', async () => {
  for (const entry of pnpmEsbuild(await read(path.join(root, 'pnpm-lock.yaml')))) {
    assert.ok(isPatched(entry.slice('esbuild@'.length)), entry);
  }
});

test('npm and pnpm retain the same parent-scoped remediation', async () => {
  const manifest = await json(path.join(app, 'package.json'));
  assert.deepEqual(manifest.overrides?.['@esbuild-kit/core-utils@3.3.2'], { esbuild: fixed });
  const workspace = await read(path.join(root, 'pnpm-workspace.yaml'));
  assert.match(workspace, /^overrides:\n  "@esbuild-kit\/core-utils@3\.3\.2>esbuild": "0\.28\.2"$/m);
  // Supply-chain permissions are intentionally not widened by a version override.
  for (const [name, allowed] of Object.entries({
    'esbuild@0.18.20': false, 'esbuild@0.25.12': false,
    'esbuild@0.28.1': false, 'esbuild@0.28.2': true,
    'unrs-resolver@1.12.2': false, 'workerd@1.20260828.1': false,
  })) assert.ok(workspace.includes(`  "${name}": ${allowed}\n`), name);
});

test('resolved legacy loader uses the patched esbuild; cross-origin reads are not granted',
  { skip: !runtime, timeout: 20000 }, async () => {
    const kit = createRequire(path.join(realpathSync(path.join(app, 'node_modules/drizzle-kit')), 'package.json'));
    const loader = createRequire(kit.resolve('@esbuild-kit/esm-loader'));
    const core = createRequire(loader.resolve('@esbuild-kit/core-utils'));
    const esbuild = core('esbuild');
    assert.equal(esbuild.version, fixed);
    assert.match(esbuild.transformSync('const n: number = 63;', { loader: 'ts' }).code, /n = 63/);
    const dir = await mkdtemp(path.join(tmpdir(), 'kfm-esbuild-'));
    let ctx;
    try {
      await writeFile(path.join(dir, 'input.ts'), 'export const securityProbe: number = 63;\n');
      ctx = await esbuild.context({ entryPoints: [path.join(dir, 'input.ts')],
        bundle: true, sourcemap: true, outdir: path.join(dir, 'out'), logLevel: 'silent' });
      const server = await ctx.serve({ host: '127.0.0.1', port: 0, servedir: path.join(dir, 'out') });
      for (const resource of ['/input.js', '/input.js.map']) {
        const url = `http://127.0.0.1:${server.port}${resource}`;
        const normal = await fetch(url, { signal: AbortSignal.timeout(5000) });
        assert.equal(normal.status, 200);
        assert.ok((await normal.text()).length > 0);
        const foreign = await fetch(url, { headers: { Origin: 'https://untrusted.example' }, signal: AbortSignal.timeout(5000) });
        assert.equal(foreign.headers.get('access-control-allow-origin'), null);
        await foreign.arrayBuffer();
      }
    } finally {
      if (ctx) await ctx.dispose();
      await rm(dir, { recursive: true, force: true });
    }
  });

test('Drizzle still generates SQL from synthetic TypeScript without a database',
  { skip: !runtime, timeout: 45000 }, async () => {
    const dir = await mkdtemp(path.join(app, '.kfm-esbuild-probe-'));
    try {
      await writeFile(path.join(dir, 'schema.ts'), "import { sqliteTable, text } from 'drizzle-orm/sqlite-core';\nexport const probe = sqliteTable('kfm_security_probe', { id: text('id').primaryKey() });\n");
      await writeFile(path.join(dir, 'config.ts'), `export default ${JSON.stringify({ dialect: 'sqlite', schema: path.join(dir, 'schema.ts'), out: path.join(dir, 'out') })};\n`);
      const result = spawnSync(path.join(app, 'node_modules/.bin/drizzle-kit'),
        ['generate', '--config', path.join(dir, 'config.ts')], { cwd: app, encoding: 'utf8', timeout: 30000 });
      assert.equal(result.status, 0, result.error?.message || result.stderr || result.stdout);
      const files = (await readdir(path.join(dir, 'out'))).filter((p) => p.endsWith('.sql'));
      assert.equal(files.length, 1);
      assert.match(await read(path.join(dir, 'out', files[0])), /CREATE TABLE.*kfm_security_probe/s);
    } finally { await rm(dir, { recursive: true, force: true }); }
  });

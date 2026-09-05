/** GHSA-px8p-9vwx-vf98: both installed graphs must carry the 0.7.5 backport.
 * No remote requests. The malformed ZIP64 fixture is synthetic and 176 bytes.
 * See ../docs/esbuild-security-remediation.md for the alert-53 reconciliation.
 */
import assert from 'node:assert/strict';
import { existsSync, readFileSync, realpathSync } from 'node:fs';
import { createRequire } from 'node:module';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const app = fileURLToPath(new URL('../', import.meta.url));
const root = path.resolve(app, '../..');
const runtime = process.env.KFM_ESBUILD_RUNTIME_PROBE === '1';
const inWorkspace = process.env.KFM_ESBUILD_REQUIRE_WORKSPACE === '1'
  || existsSync(path.join(root, '.git')) || existsSync(path.join(root, 'pnpm-workspace.yaml'));
const workspaceOnly = { skip: inWorkspace ? false : 'standalone app; workspace parity runs in monorepo CI' };
const read = (p) => readFileSync(p, 'utf8');

function patched(version) {
  const match = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/.exec(version ?? '');
  if (!match) return false;
  const [major, minor, patch] = match.slice(1).map(Number);
  // Deliberately bound to the two supported lines used by this dependency lane.
  // A new major/minor line needs a reviewed compatibility/advisory decision.
  return major === 0 && ((minor === 7 && patch >= 5) || (minor === 8 && patch >= 3));
}

function lockedVersions(lock) {
  assert.equal(lock.lockfileVersion, 3);
  assert.ok(lock.packages && typeof lock.packages === 'object');
  const entries = Object.entries(lock.packages).filter(([p]) => /(?:^|\/)node_modules\/fflate$/.test(p));
  assert.ok(entries.length, 'fflate must be inventoried');
  return entries;
}

// ZIP64 central entry with a sentinel compressed size and no ZIP64 extra field.
// Valid record/locator/EOCD structure ensures the ZIP64 parsing path is reached.
function malformedZip64() {
  const b = Buffer.alloc(176);
  b.writeUInt32LE(0x04034b50, 0); b.writeUInt16LE(45, 4);
  b.writeUInt16LE(1, 26); b[30] = 120;
  const c = 31;
  b.writeUInt32LE(0x02014b50, c); b.writeUInt16LE(45, c + 6);
  b.writeUInt32LE(0xffffffff, c + 20); b.writeUInt16LE(1, c + 28); b[c + 46] = 120;
  const z = 78;
  b.writeUInt32LE(0x06064b50, z); b.writeBigUInt64LE(44n, z + 4);
  b.writeUInt16LE(45, z + 12); b.writeUInt16LE(45, z + 14);
  b.writeBigUInt64LE(1n, z + 24); b.writeBigUInt64LE(1n, z + 32);
  b.writeBigUInt64LE(47n, z + 40); b.writeBigUInt64LE(31n, z + 48);
  const l = 134;
  b.writeUInt32LE(0x07064b50, l); b.writeBigUInt64LE(78n, l + 8); b.writeUInt32LE(1, l + 16);
  const e = 154;
  b.writeUInt32LE(0x06054b50, e); b.writeUInt16LE(0xffff, e + 8); b.writeUInt16LE(0xffff, e + 10);
  b.writeUInt32LE(47, e + 12); b.writeUInt32LE(0xffffffff, e + 16);
  return b;
}

function installedFflate() {
  let req = createRequire(path.join(realpathSync(path.join(app, 'node_modules/vinext')), 'package.json'));
  for (const dep of ['@vercel/og', 'satori', '@shuding/opentype.js']) req = createRequire(req.resolve(dep));
  return { req, entry: req.resolve('fflate') };
}

test('fflate version guard rejects vulnerable, unknown and prerelease versions', () => {
  for (const v of ['0.7.4', '0.8.2', '^0.7.5', '0.7.5-beta.1', '0.9.0', '', null]) assert.equal(patched(v), false, String(v));
  for (const v of ['0.7.5', '0.7.6', '0.8.3']) assert.equal(patched(v), true);
  assert.throws(() => lockedVersions({ lockfileVersion: 3, packages: {} }));
  assert.equal(malformedZip64().length, 176);
});

test('npm lock retains a patched fflate and the compatible parent range', () => {
  const lock = JSON.parse(read(path.join(app, 'package-lock.json')));
  for (const [p, entry] of lockedVersions(lock)) assert.ok(patched(entry.version), `${p}: ${entry.version}`);
  assert.equal(lock.packages['node_modules/@shuding/opentype.js'].dependencies.fflate, '^0.7.3');
  assert.equal(lock.packages['node_modules/fflate'].version, '0.7.5');
});

test('pnpm graph retains the existing patched fflate backport', workspaceOnly, () => {
  const text = read(path.join(root, 'pnpm-lock.yaml'));
  const versions = [...text.matchAll(/^  fflate@([^\s:]+):/gm)].map((m) => m[1]);
  assert.equal(versions.length, 2, 'one package and one snapshot expected');
  assert.ok(versions.every((v) => v === '0.7.5'));
});

test('resolved fflate preserves normal compression and rejects malformed ZIP64 finitely',
  { skip: !runtime, timeout: 10000 }, () => {
    const { req, entry } = installedFflate();
    const zip = req('fflate');
    const plain = zip.strToU8('KFM synthetic security fixture');
    assert.deepEqual(zip.decompressSync(zip.compressSync(plain)), plain);
    assert.deepEqual(zip.unzipSync(zip.zipSync({ 'probe.txt': plain }))['probe.txt'], plain);
    const child = spawnSync(process.execPath, ['-e', `
      const assert = require('node:assert/strict');
      const fflate = require(process.argv[1]);
      const input = new Uint8Array(Buffer.from(process.argv[2], 'base64'));
      assert.throws(() => fflate.unzipSync(input), (e) => e.code === 13);
      console.log('ZIP64_REJECTED');
    `, entry, malformedZip64().toString('base64')], {
      encoding: 'utf8', timeout: 3000, killSignal: 'SIGKILL', maxBuffer: 65536,
    });
    assert.equal(child.status, 0, child.error?.message || child.stderr);
    assert.equal(child.stdout.trim(), 'ZIP64_REJECTED');
  });

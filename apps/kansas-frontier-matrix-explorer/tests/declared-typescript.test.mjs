import assert from 'node:assert/strict';
import { test } from 'node:test';
import { mkdtempSync, mkdirSync, writeFileSync, rmSync, symlinkSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { resolveDeclaredTypeScript } from './declared-typescript.mjs';

function fixture(t, alias = true) {
  const root = mkdtempSync(join(tmpdir(), 'kfm compiler contract '));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const key = alias ? '@typescript/native' : 'typescript';
  const declaration = alias ? 'npm:typescript@7.0.2' : '7.0.2';
  const directory = join(root, 'node_modules', key);
  mkdirSync(join(directory, 'bin'), { recursive: true });
  const manifest = { devDependencies: { [key]: declaration } };
  if (alias) manifest.devDependencies.typescript = 'npm:@typescript/typescript6@6.0.2';
  const installed = { name: 'typescript', version: '7.0.2', bin: { tsc: 'bin/tsc' } };
  const lock = { packages: { '': { devDependencies: { ...manifest.devDependencies } },
    [`node_modules/${key}`]: { ...installed, bin: { ...installed.bin }, integrity: 'sha512-synthetic-contract-fixture' } } };
  const write = () => {
    writeFileSync(join(root, 'package.json'), JSON.stringify(manifest));
    writeFileSync(join(root, 'package-lock.json'), JSON.stringify(lock));
    writeFileSync(join(directory, 'package.json'), JSON.stringify(installed));
  };
  writeFileSync(join(directory, 'bin/tsc'), '// non-executable resolver fixture\n');
  write();
  return { root, key, directory, manifest, lock, installed, write };
}
for (const alias of [false, true]) {
  test(`resolves exact ${alias ? 'native alias' : 'plain'} CLI with paths containing spaces`, t => {
    const f = fixture(t, alias); const result = resolveDeclaredTypeScript(f.root);
    assert.equal(result.compiler, join(f.directory, 'bin/tsc'));
    assert.equal(result.compilerVersion, '7.0.2'); assert.ok(Object.isFrozen(result));
  });
}
for (const [name, change] of [
  ['range declaration', f => { f.manifest.devDependencies[f.key] = 'npm:typescript@^7.0.2'; }],
  ['classic API as CLI', f => { f.manifest.devDependencies[f.key] = 'npm:@typescript/typescript6@6.0.2'; }],
  ['lock importer mismatch', f => { f.lock.packages[''].devDependencies[f.key] = '7.0.2'; }],
  ['lock version mismatch', f => { f.lock.packages[`node_modules/${f.key}`].version = '7.0.1'; }],
  ['lock package mismatch', f => { f.lock.packages[`node_modules/${f.key}`].name = 'other'; }],
  ['missing lock integrity', f => { delete f.lock.packages[`node_modules/${f.key}`].integrity; }],
  ['installed version mismatch', f => { f.installed.version = '6.0.3'; }],
  ['installed package mismatch', f => { f.installed.name = '@typescript/typescript6'; }],
  ['installed bin mismatch', f => { f.installed.bin.tsc = 'bin/other'; }],
]) {
  test(`rejects ${name} rather than choosing an ambient compiler`, t => {
    const f = fixture(t); change(f); f.write(); assert.throws(() => resolveDeclaredTypeScript(f.root));
  });
}
test('missing declared installation does not fall back to classic API or NODE_PATH', t => {
  const f = fixture(t); rmSync(f.directory, { recursive: true, force: true });
  assert.throws(() => resolveDeclaredTypeScript(f.root));
});
test('even a lock-matching bin cannot escape the package through a symlink', t => {
  const f = fixture(t); const bin = join(f.directory, 'bin/tsc');
  const outside = join(f.root, 'outside'); writeFileSync(outside, '// external');
  rmSync(bin); symlinkSync(outside, bin);
  assert.throws(() => resolveDeclaredTypeScript(f.root), /escapes/);
});
for (const [installedBin, lockedBin] of [['./bin/tsc', 'bin/tsc'], ['bin/tsc', './bin/tsc']]) {
  test(`equivalent entrypoint spellings select one confined file: ${installedBin} / ${lockedBin}`, t => {
    const f = fixture(t);
    // These are independent package/lock objects, not a shared fixture alias.
    f.installed.bin = { tsc: installedBin };
    f.lock.packages[`node_modules/${f.key}`].bin = { tsc: lockedBin };
    f.write();
    assert.equal(resolveDeclaredTypeScript(f.root).compiler, join(f.directory, 'bin/tsc'));
  });
}
test('absolute lock entrypoints fail even when the installed relative path targets the same file', t => {
  const f = fixture(t);
  f.lock.packages[`node_modules/${f.key}`].bin = { tsc: join(f.directory, 'bin/tsc') };
  f.write();
  assert.throws(() => resolveDeclaredTypeScript(f.root), /does not match/);
});
test('different existing entrypoints are rejected rather than merely checked for existence', t => {
  const f = fixture(t);
  writeFileSync(join(f.directory, 'bin/other'), '// different installed program');
  f.installed.bin = { tsc: 'bin/other' };
  f.write();
  assert.throws(() => resolveDeclaredTypeScript(f.root), /does not match/);
});

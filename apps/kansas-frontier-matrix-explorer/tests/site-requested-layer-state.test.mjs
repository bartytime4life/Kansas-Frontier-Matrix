import assert from 'node:assert/strict';
import { test, after } from 'node:test';
import { mkdtempSync, rmSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, resolve, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');
const require = createRequire(import.meta.url);
const app = join(root, 'apps/kansas-frontier-matrix-explorer');
// NODE_PATH may resolve an ambient global compiler. Resolution alone is not a lock check.
let compiler;
let compilerVersion;
let compilerMode = 'DECLARED_VERSION_MATCH';
try {
  const manifest = JSON.parse(readFileSync(join(app, 'package.json'), 'utf8'));
  const lock = JSON.parse(readFileSync(join(app, 'package-lock.json'), 'utf8'));
  const expected = manifest.devDependencies?.typescript;
  if (!/^\d+\.\d+\.\d+$/.test(expected ?? '')
      || lock.packages?.['node_modules/typescript']?.version !== expected) {
    throw new Error('TypeScript declaration and app lock do not agree');
  }
  for (const directory of [app, root]) {
    const candidate = join(directory, 'node_modules/typescript/bin/tsc');
    if (!existsSync(candidate)) continue;
    const installed = JSON.parse(readFileSync(join(directory, 'node_modules/typescript/package.json'), 'utf8'));
    if (installed.version === expected) { compiler = candidate; compilerVersion = installed.version; break; }
  }
} catch { /* No implicit ambient/global fallback. */ }
if (!compiler) {
  if (process.env.KFM_ALLOW_GLOBAL_TSC !== '1') {
    throw new Error('Declared TypeScript unavailable or app lock mismatch. Install the repository lock; an ambient diagnostic requires KFM_ALLOW_GLOBAL_TSC=1.');
  }
  compiler = require.resolve('typescript/bin/tsc');
  compilerVersion = require('typescript/package.json').version;
  compilerMode = 'AMBIENT_DIAGNOSTIC_NOT_LOCK_NATIVE';
}
console.log(JSON.stringify({ compilerMode, compilerVersion, compiler,
  installedByteIntegrity: 'NOT_VERIFIED_BY_THIS_TEST' }));
const output = mkdtempSync(join(tmpdir(), 'kfm-requested-state-unit-'));
after(()=>rmSync(output,{recursive:true,force:true}));
writeFileSync(join(output, 'package.json'), '{"type":"module"}');
const files = ['apps/kansas-frontier-matrix-explorer/app/site-requested-layer-state.ts'];
const args = ['--target','ES2022','--module','ES2022','--moduleResolution','bundler','--strict',
  '--lib','ES2022,DOM,DOM.Iterable','--rootDir',root,'--outDir',output,...files.map(x=>join(root,x))];
const build = spawnSync(process.execPath,[compiler,...args],{encoding:'utf8'});
assert.equal(build.status,0,build.stdout+build.stderr);
const { createRequestedLayerStore } = await import(pathToFileURL(join(output, 'apps/kansas-frontier-matrix-explorer/app/site-requested-layer-state.js')).href);
const initial = () => ({ visibility: { a: false, b: false, legacy: true }, opacity: { a: 1, b: .7, legacy: .2 }, layerOrder: ['a', 'legacy', 'b'] });
const store = () => createRequestedLayerStore(initial(), ['a', 'b']);
const patch = (a, opacity = .4) => ({ visibility: { a }, opacity: { a: opacity } });
test('Library CAS publishes both maps once and preserves unrelated legacy state and order', () => {
  const s = store(); const seen = []; s.subscribe(() => seen.push(s.getSnapshot()));
  assert.equal(s.compareAndSet(patch(true), patch(false, 1)), true);
  assert.equal(seen.length, 1); assert.equal(seen[0].visibility.a, true); assert.equal(seen[0].opacity.a, .4);
  assert.equal(seen[0].visibility.legacy, true); assert.equal(seen[0].opacity.legacy, .2);
  assert.deepEqual(seen[0].layerOrder, initial().layerOrder);
});
test('a stale Library expectation cannot overwrite a later legacy writer', () => {
  const s = store(); s.setOpacity((v) => ({ ...v, a: .8 })); const before = s.getSnapshot();
  assert.equal(s.compareAndSet(patch(true), patch(false, 1)), false); assert.equal(s.getSnapshot(), before);
});
test('fast consecutive functional writers read the current owner before any React paint', () => {
  const s = store(); s.setVisibility((v) => ({ ...v, a: !v.a })); s.setVisibility((v) => ({ ...v, b: !v.b }));
  s.setOpacity((v) => ({ ...v, a: .5 }));
  assert.deepEqual(s.getSnapshot().visibility, { a: true, b: true, legacy: true });
  assert.equal(s.compareAndSet(patch(false, .3), patch(true, .5)), true);
});
test('unrelated changes do not cause a false conflict or get clobbered', () => {
  const s = store(); s.setVisibility((v) => ({ ...v, b: true }));
  assert.equal(s.compareAndSet(patch(true), patch(false, 1)), true); assert.equal(s.getSnapshot().visibility.b, true);
});
test('unknown and legacy-only IDs are refused by the Library path', () => {
  for (const id of ['unknown', 'legacy', '__proto__', 'constructor']) {
    const s = store(); const before = s.getSnapshot();
    assert.equal(s.compareAndSet({ visibility: { [id]: false }, opacity: { [id]: .5 } },
      { visibility: { [id]: before.visibility[id] }, opacity: { [id]: before.opacity[id] } }), false);
    assert.equal(s.getSnapshot(), before);
  }
});
test('invalid or partial expected values do not mutate or notify', () => {
  const s = store(); let count = 0; s.subscribe(() => count++);
  for (const value of [NaN, Infinity, -.1, 1.1, '0']) assert.equal(s.compareAndSet(patch(true, value), patch(false, 1)), false);
  assert.equal(s.compareAndSet(patch(true), { visibility: { a: false }, opacity: {} }), false);
  assert.equal(s.compareAndSet({ visibility: {}, opacity: {} }, { visibility: {}, opacity: {} }), false);
  assert.equal(count, 0);
});
test('zero opacity is a real value, not a missing/default value', () => {
  const s = store(); assert.equal(s.compareAndSet(patch(true, 0), patch(false, 1)), true);
  assert.equal(s.getSnapshot().opacity.a, 0);
});
test('snapshots are detached immutable values and server snapshot identity is stable', () => {
  const source = initial(); const s = createRequestedLayerStore(source, ['a', 'b']); const first = s.getSnapshot();
  source.visibility.a = true; source.opacity.a = .01; source.layerOrder.push('evil');
  assert.equal(first.visibility.a, false); assert.equal(first.opacity.a, 1);
  assert.throws(() => { first.visibility.a = true; }); assert.throws(() => first.layerOrder.push('bad'));
  s.setOpacity((v) => ({ ...v, a: .8 })); assert.equal(s.getServerSnapshot(), first); assert.notEqual(s.getSnapshot(), first);
});
test('reset/restore is one atomic replace and advances only transient membership epoch', () => {
  const s = store(); const observed = []; s.subscribe(() => observed.push(s.getSnapshot()));
  s.replace({ ...initial(), visibility: { a: true, b: true, legacy: false }, opacity: { a: 0, b: .3, legacy: .4 } });
  assert.equal(observed.length, 1); assert.equal(observed[0].membershipEpoch, 1);
  assert.equal(observed[0].opacity.a, 0); assert.equal(observed[0].visibility.legacy, false);
  s.replace(initial()); assert.equal(s.getSnapshot().membershipEpoch, 2);
});
test('invalid replace, missing keys and duplicate order leave the previous owner intact', () => {
  const s = store(); const before = s.getSnapshot();
  assert.throws(() => s.replace({ ...initial(), layerOrder: ['a', 'a', 'b'] }));
  assert.throws(() => s.setVisibility({ a: true })); assert.throws(() => s.setOpacity({ ...initial().opacity, a: NaN }));
  assert.equal(s.getSnapshot(), before);
});
test('a writer callback failure cannot partially update either map', () => {
  const s = store(); const before = s.getSnapshot(); assert.throws(() => s.setVisibility(() => { throw Error('test-only'); }));
  assert.equal(s.getSnapshot(), before);
});
test('unsubscribe ends observation without disabling state ownership', () => {
  const s = store(); let calls = 0; const off = s.subscribe(() => calls++);
  s.setOpacity((v) => ({ ...v, a: .6 })); off(); s.setOpacity((v) => ({ ...v, a: .5 }));
  assert.equal(calls, 1); assert.equal(s.getSnapshot().opacity.a, .5);
});

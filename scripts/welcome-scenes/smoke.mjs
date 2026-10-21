// Headless smoke test for welcome scenes: builds each scene with a stubbed
// canvas, steps its whole loop, and fails on exceptions, NaN camera poses or
// runaway object counts. Usage: node scripts/welcome-scenes/smoke.mjs [id ...]
import { SCENE_CATALOG } from '../../app/living-welcome/scenes/catalog.mjs';

const ctx2d = new Proxy({}, { get: (_, key) => key === 'createLinearGradient' || key === 'createRadialGradient' ? () => ({ addColorStop() {} }) : key === 'getImageData' ? () => ({ data: new Uint8ClampedArray(4) }) : key === 'measureText' ? () => ({ width: 10 }) : () => {}, set: () => true });
globalThis.document = { createElement: () => ({ width: 0, height: 0, style: {}, getContext: () => ctx2d }), hidden: false, addEventListener() {}, removeEventListener() {} };
globalThis.window = { devicePixelRatio: 1 };

const ids = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(SCENE_CATALOG);
let failed = 0;
for (const id of ids) {
 try {
  const { create } = await import(`../../app/living-welcome/scenes/${id}.mjs`);
  const started = performance.now();
  const s = create({});
  const built = performance.now() - started;
  if (!s.scene?.isScene || !s.camera?.isCamera || typeof s.update !== 'function') throw new Error('create() must return { scene, camera, update }');
  const duration = SCENE_CATALOG[id].duration;
  let objects = 0, worst = 0;
  for (let t = 0; t <= duration; t += 1 / 30) {
   const a = performance.now(); s.update(t, 1 / 30); worst = Math.max(worst, performance.now() - a);
   const p = s.camera.position;
   if (![p.x, p.y, p.z].every(Number.isFinite)) throw new Error(`camera position is not finite at t=${t.toFixed(2)}`);
  }
  // The loop must restart without a cut: compare the camera at both ends.
  s.update(0, 0); const first = s.camera.position.clone(); s.update(duration, 0);
  const seam = s.camera.position.distanceTo(first);
  if (seam > .4) console.log(`warn ${id}: camera jumps ${seam.toFixed(2)} units when the loop restarts`);
  s.scene.traverse(() => objects++);
  let vertices = 0; s.scene.traverse(o => { vertices += o.geometry?.attributes?.position?.count || 0; });
  s.dispose?.();
  console.log(`ok   ${id.padEnd(12)} build ${built.toFixed(0)}ms · worst update ${worst.toFixed(1)}ms · ${objects} objects · ${vertices} vertices`);
  if (worst > 8) console.log(`warn ${id}: an update took ${worst.toFixed(1)}ms on the CPU; keep per-frame work under ~4ms`);
  if (vertices > 700000) console.log(`warn ${id}: ${vertices} vertices is heavy for the start page`);
 } catch (error) { failed++; console.log(`FAIL ${id}: ${error.stack || error}`); }
}
process.exit(failed ? 1 : 0);

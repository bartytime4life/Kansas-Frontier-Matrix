import assert from 'node:assert/strict';
import test from 'node:test';
import { create } from '../app/living-welcome/scenes/transport.mjs';
import { disposeTree } from '../app/living-welcome/scenes/kit.mjs';

// Only the point-sprite texture needs a canvas while constructing geometry.
// This harness does not render or claim GPU/browser acceptance.
test('the full transport loop keeps measured vehicles in lanes and preserves spacing through era changes', () => {
 const prior = globalThis.document;
 globalThis.document = { createElement: () => ({ getContext: () => ({ createRadialGradient: () => ({ addColorStop() {} }), fillRect() {} }) }) };
 let world;
 try { world = create(); } finally { globalThis.document = prior; }
 let headwayChecks = 0, waitFrames = 0;
 try {
  for (const vehicle of world.trafficSnapshot()) {
   assert.ok(vehicle.lane + vehicle.halfWidth < vehicle.width / 2, `${vehicle.route}: wheels stay inside the shoulder`);
   if (vehicle.lane) assert.ok(vehicle.lane > vehicle.halfWidth, `${vehicle.route}: opposing lanes stay separate`);
  }
  for (let i = 0; i <= 36 * 60; i++) {
   world.update(i / 60);
   const moving = world.trafficSnapshot().filter(v => v.admitted && v.s >= 0 && v.s <= v.length);
   for (const a of moving) {
    waitFrames += Number(a.waiting);
    for (const b of moving) {
     if (a === b || a.physical !== b.physical || a.dir !== b.dir) continue;
     const gap = ((b.s - a.s) % a.cycle + a.cycle) % a.cycle - b.rear - a.front;
     assert.ok(gap >= .099, `headway at ${i / 60}s on ${a.physical}: ${gap}`);
     headwayChecks++;
    }
   }
   assert.ok(world.camera.position.toArray().every(Number.isFinite));
  }
  assert.ok(headwayChecks > 10000); assert.ok(waitFrames > 100);
  world.update(24); const first = world.trafficSnapshot();
  world.update(24); assert.deepEqual(world.trafficSnapshot(), first, 'pause is stable');
  world.update(0); world.update(24); assert.deepEqual(world.trafficSnapshot(), first, 'rewind reconstructs the same scene');
  const bridges = world.scene.children.filter(n => n.name.startsWith('bridge-'));
  assert.ok(bridges.length >= 4);
  assert.ok(bridges.every(b => b.children.length <= 2 && b.children.every(m => m.isInstancedMesh)), 'bridge detail stays batched');
 } finally { world.dispose(); disposeTree(world.scene); }
});

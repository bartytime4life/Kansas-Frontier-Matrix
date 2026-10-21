import { THREE, HALF, terrain, blockSides, riverWater, ribbon, surfacePath, mainRiver, riverZ, TRIBUTARIES, tributaryPoint, heroCamera, stage, orbit, glowPoints, gridSampler, smooth, window01, lerp, clamp, rng } from './kit.mjs';
// Water & watersheds: stream gauges report, their readings give the drawn flow
// its direction and speed, then a rising upstream reading travels downstream as
// a surge, each gauge responding as it passes.

const IDLE = new THREE.Color('#58798a'), FLOWING = new THREE.Color('#8fe6ff'), SURGE = new THREE.Color('#fff0c2');
const GAUGE_X = [-4.3, -1.4, 1.6, 4.4], TRAIL = 3, SURGE_START = 11.2, SURGE_SPEED = 2.6;

/** Arc-length table for a channel so particles move at even speed. */
function channel(points) {
 const lengths = [0];
 for (let i = 1; i < points.length; i++) lengths.push(lengths[i - 1] + points[i].distanceTo(points[i - 1]));
 const total = lengths[lengths.length - 1];
 function at(s, out) {
  const d = clamp(s) * total;
  let lo = 0, hi = lengths.length - 1;
  while (hi - lo > 1) { const mid = (lo + hi) >> 1; if (lengths[mid] < d) lo = mid; else hi = mid; }
  const f = (d - lengths[lo]) / Math.max(1e-6, lengths[hi] - lengths[lo]);
  return out.copy(points[lo]).lerp(points[hi], f);
 }
 return { points, total, at };
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .02 });
 const land = terrain({ segments: 220 }), sample = gridSampler(land);
 scene.add(land.mesh, blockSides(sample), riverWater(sample, { width: .3 }));
 land.mesh.material.color = new THREE.Color('#c9d2c6'); // soften the land so water reads first

 const main = channel(surfacePath(s => mainRiver(s), sample, 240, .05));
 const tribs = TRIBUTARIES.map(trib => channel(surfacePath(s => tributaryPoint(trib, s), sample, 120, .05)));
 for (const c of tribs) { const r = ribbon(c.points, { width: .12, color: '#3f86a6', opacity: .85 }); scene.add(r); }

 // Flow particles: each is a short comet (head + fading trail) so direction
 // reads even in a still frame.
 const random = rng(11), particles = [];
 const add = (c, count, delay, reach) => { for (let i = 0; i < count; i++) particles.push({ c, s0: random(), lane: (random() - .5) * (c === main ? .2 : .08), speed: .7 + random() * .5, delay, reach }); };
 add(main, 760, 0, 'main');
 tribs.forEach((c, i) => add(c, 150, .5 + i * .35, 'trib'));
 const flow = glowPoints(particles.length * TRAIL, { size: .4, color: '#8fe6ff' });
 scene.add(flow);

 // Gauges: a mast, a sensor light, a reading bar and a report ring.
 const gauges = GAUGE_X.map((x, i) => {
  const z = riverZ(x) + .34, y = sample(x, z), reading = .55 + .3 * Math.sin(i * 2.1 + 1);
  const mast = new THREE.Mesh(new THREE.CylinderGeometry(.018, .018, .7, 8), new THREE.MeshStandardMaterial({ color: '#cbd6dc', metalness: .6, roughness: .4 }));
  mast.position.set(x, y + .35, z);
  const bar = new THREE.Mesh(new THREE.BoxGeometry(.1, 1, .1), new THREE.MeshStandardMaterial({ color: '#0d3446', emissive: '#3fb8e0', emissiveIntensity: .8, transparent: true, opacity: .92 }));
  const ring = new THREE.Mesh(new THREE.RingGeometry(.9, 1, 64), new THREE.MeshBasicMaterial({ color: '#8fe6ff', transparent: true, opacity: 0, depthWrite: false, side: THREE.DoubleSide, blending: THREE.AdditiveBlending }));
  ring.rotation.x = -Math.PI / 2; ring.position.set(x, sample(x, riverZ(x)) + .07, riverZ(x));
  const light = glowPoints(1, { size: 1.1, color: '#ffd98f' }); light.positions.set([x, y + .74, z]); light.commit();
  const beam = new THREE.Mesh(new THREE.PlaneGeometry(.06, 3.2), new THREE.MeshBasicMaterial({ color: '#8fe6ff', transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide }));
  beam.position.set(x, y + 2.3, z);
  scene.add(mast, bar, ring, light, beam);
  return { x, z, y, reading, bar, ring, light, beam, report: .7 + i * 1.05 };
 });
 const tmp = new THREE.Vector3(), color = new THREE.Color();
 const surgeFront = t => (t - SURGE_START) * SURGE_SPEED - HALF; // world x of the surge front

 function update(t) {
  const fade = 1 - smooth(15.2, 16, t);
  // Beat 1: gauges report in sequence (ring, uplink beam, bar rises).
  for (const g of gauges) {
   const up = smooth(g.report, g.report + .8, t) * fade, pulse = (t - g.report) % 5.5;
   const passed = smooth(-.2, .5, surgeFront(t) - g.x) * (1 - smooth(14.6, 15.6, t));
   const level = g.reading * up * (1 + .7 * passed);
   g.bar.scale.y = Math.max(.001, level * 1.4); g.bar.position.set(g.x + .14, g.y + level * .7, g.z);
   g.bar.material.emissive.copy(FLOWING).lerp(SURGE, passed);
   g.ring.scale.setScalar(.15 + clamp(pulse / 1.6) * .9); g.ring.material.opacity = t >= g.report ? (1 - clamp(pulse / 1.6)) * .8 * fade : 0;
   g.beam.material.opacity = window01(t, g.report, g.report + 1.4, .3) * .7 + passed * .25 * window01(t, SURGE_START, 15, .4);
   g.light.alphas[0] = .4 + .6 * up; g.light.commit();
  }
  // Beat 2: readings arrive reach by reach downstream; particles take their
  // direction and speed from them. Beat 3: the surge brightens and quickens.
  const front = surgeFront(t);
  particles.forEach((p, i) => {
   const ref = p.reach === 'main' ? lerp(-HALF, HALF, p.s0) : -HALF + 4 + p.delay * 2;
   const start = 5.6 + (ref + HALF) / (2 * HALF) * 2.2 + p.delay, live = smooth(start, start + 1, t) * fade;
   const travel = Math.max(0, t - start - .5) * .05 * p.speed;
   const s = (p.s0 + travel / (p.c.total / 12)) % 1;
   const head = p.c.at(s, tmp);
   const surge = p.reach === 'main' ? smooth(.9, 0, Math.abs(head.x - front + .45)) * (t > SURGE_START ? 1 : 0) * fade : 0;
   for (let k = 0; k < TRAIL; k++) {
    const pos = k ? p.c.at(Math.max(0, s - k * .006 * (.4 + live)), tmp) : head, n = i * TRAIL + k;
    flow.positions.set([pos.x, pos.y + .02, pos.z + p.lane], n * 3);
    color.copy(IDLE).lerp(FLOWING, live).lerp(SURGE, surge);
    flow.colors.set([color.r, color.g, color.b], n * 3);
    flow.alphas[n] = (.35 + .65 * live) * (1 - k / TRAIL) * (.5 + .5 * fade);
    flow.sizes[n] = (.3 + .14 * live + .34 * surge) * (1 - k * .22);
   }
  });
  flow.commit();
  orbit(camera, t, { radius: 18.5, height: 10.5, target: [0, -.7, 0], start: -.75 + .26 * Math.sin(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update };
}

import { THREE, HALF, terrain, liveSurface, blockSides, heroCamera, stage, orbit, glowPoints, ribbon, surfacePath, smooth, window01, lerp, rng } from './kit.mjs';
import { SCENE_CATALOG } from './catalog.mjs';
// Government & civic: the state line and a county grid draw in, county seats
// rise as beacons, then one jurisdiction lifts out of the map to show that
// a place is governed by a stack of offices, not one line on the ground.

const T = SCENE_CATALOG.government.duration;
const COLS = 6, ROWS = 4, IN = HALF - .25;
const LIFTED = [3, 1]; // the county that lifts in beat 3

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022, background: '#0d1022' });
 const land = terrain({ segments: 200 });
 const u = liveSurface(land);
 u.tint.value.set('#2a2147');
 scene.add(land.mesh, blockSides(land.sample));
 const r = rng(17);

 // County grid: near-straight surveyed lines, the outer edge as the state line.
 const xs = Array.from({ length: COLS + 1 }, (_, i) => lerp(-IN, IN, i / COLS) + (i % COLS ? (r() - .5) * .3 : 0));
 const zs = Array.from({ length: ROWS + 1 }, (_, j) => lerp(-IN * .72, IN * .72, j / ROWS) + (j % ROWS ? (r() - .5) * .22 : 0));
 const lines = [];
 xs.forEach((x, i) => lines.push({ edge: i === 0 || i === COLS, mesh: ribbon(surfacePath(s => [x, lerp(zs[0], zs[ROWS], s)], land.sample, 90, .04), { width: i === 0 || i === COLS ? .12 : .055, color: i === 0 || i === COLS ? '#e3d4ff' : '#a58be0', additive: true }), order: i / COLS }));
 zs.forEach((z, j) => lines.push({ edge: j === 0 || j === ROWS, mesh: ribbon(surfacePath(s => [lerp(xs[0], xs[COLS], s), z], land.sample, 120, .04), { width: j === 0 || j === ROWS ? .12 : .055, color: j === 0 || j === ROWS ? '#e3d4ff' : '#a58be0', additive: true }), order: j / ROWS }));
 for (const line of lines) scene.add(line.mesh);

 // County seats: one per cell, offset from centre, with a beam that rises in beat 2.
 const seats = [];
 for (let j = 0; j < ROWS; j++) for (let i = 0; i < COLS; i++) {
  const x = lerp(xs[i], xs[i + 1], .35 + r() * .3), z = lerp(zs[j], zs[j + 1], .35 + r() * .3);
  seats.push({ i, j, x, z, y: land.sample(x, z), delay: (i + j) * .18 + r() * .2 });
 }
 const beams = seats.map(seat => {
  const beam = new THREE.Mesh(new THREE.CylinderGeometry(.025, .05, 1, 10, 1, true), new THREE.MeshBasicMaterial({ color: '#f2d27a', transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending }));
  beam.position.set(seat.x, seat.y, seat.z); beam.scale.y = .001; scene.add(beam);
  return beam;
 });
 const glow = glowPoints(seats.length, { size: .95, color: '#f2d27a' });
 scene.add(glow);

 // The lifted jurisdiction: a translucent prism with stacked tiers for its offices.
 const [li, lj] = LIFTED, w = xs[li + 1] - xs[li], d = zs[lj + 1] - zs[lj];
 const cx = (xs[li] + xs[li + 1]) / 2, cz = (zs[lj] + zs[lj + 1]) / 2, ground = land.sample(cx, cz);
 const stack = new THREE.Group(); stack.position.set(cx, ground, cz); scene.add(stack);
 const slabs = ['#b69cf0', '#8fd6ee', '#f2d27a'].map((color, k) => {
  const slab = new THREE.Mesh(new THREE.BoxGeometry(w * (1 - k * .16), .16, d * (1 - k * .16)), new THREE.MeshStandardMaterial({ color, emissive: color, emissiveIntensity: .45, transparent: true, opacity: 0, roughness: .4 }));
  const edges = new THREE.LineSegments(new THREE.EdgesGeometry(slab.geometry), new THREE.LineBasicMaterial({ color: '#ffffff', transparent: true, opacity: 0 }));
  slab.add(edges); stack.add(slab);
  return { slab, edges, k };
 });

 function update(t) {
  const out = 1 - smooth(T - .9, T, t);
  u.tintMix.value = .42 * smooth(0, 1.2, t) * out;
  // Beat 1 (0–5.5 s): the state line, then the county grid, draw across the land.
  for (const line of lines) {
   const start = line.edge ? .2 : 1.2 + line.order * 2.2, p = smooth(start, start + 1.6, t);
   line.mesh.reveal(p); line.mesh.material.opacity = (line.edge ? .95 : .7) * smooth(start, start + .2, t) * out * lerp(1, .55, smooth(11, 12, t));
  }
  // Beat 2 (5.5–11 s): county seats rise as beacons, west to east.
  seats.forEach((seat, k) => {
   const p = smooth(5.6 + seat.delay, 6.8 + seat.delay, t), isLifted = seat.i === li && seat.j === lj;
   const dim = isLifted ? 1 : lerp(1, .35, smooth(11, 12, t));
   beams[k].scale.y = Math.max(.001, p * (1.1 + .4 * Math.sin(k * 1.7)));
   beams[k].position.y = seat.y + beams[k].scale.y / 2;
   beams[k].material.opacity = p * .55 * dim * out;
   glow.positions.set([seat.x, seat.y + beams[k].scale.y + .05, seat.z], k * 3);
   glow.alphas[k] = p * dim * out * (.75 + .25 * Math.sin(t * 2.2 + k));
  });
  glow.commit();
  // Beat 3 (11–16 s): one county lifts as a stack of governing tiers.
  slabs.forEach(({ slab, edges, k }) => {
   const p = smooth(11.2 + k * .5, 12.6 + k * .5, t) * out;
   slab.position.y = .1 + p * (1.1 + k * .55);
   slab.material.opacity = p * .55; edges.material.opacity = p * .9;
  });
  orbit(camera, t, { radius: lerp(21, 19, window01(t, 10.5, T, 1.5)), height: lerp(11.5, 10, smooth(4, 10, t)), target: [0, -.4, 0], start: -1 + .28 * Math.sin(t / T * Math.PI * 2), speed: 0 });
 }
 update(0);
 return { scene, camera, update, dispose() {} };
}

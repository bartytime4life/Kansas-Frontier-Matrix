import { THREE, HALF, terrain, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, gridSampler, strataColor, smooth, lerp, clamp, easeInOut, rng } from './kit.mjs';
// Aquifers & groundwater: cuts open the block (east, then south, then a corner
// notch) so live cross-sections reveal soil, loess, the saturated aquifer under
// its water table, shale and bedrock; monitoring wells then sample the aquifer.

const FLOOR = -2.4, OFF = -100, CLOSED = HALF + .2;
const wobble = (x, z) => .05 * Math.sin(x * 1.3 + z * .7) + .03 * Math.sin(x * 3.7 - z * 2.1); // matches kit strata
const waterTable = (x, z) => .64 + 2 * wobble(x, z) + .05 * Math.sin(x * .5 - z * .3);
const aquiferBase = (x, z) => 1.21 + 3.6 * wobble(x, z);
const WET = new THREE.Color('#2a95c4');
function groundColor(depth, x, z, out) {
 strataColor(depth, x, z, out);
 if (depth > waterTable(x, z) && depth < aquiferBase(x, z)) out.lerp(WET, .62);
 return out;
}

/** A vertical cross-section face that follows a moving cut. */
function section(sample, axis, steps = 120, rows = 44) {
 const count = (steps + 1) * (rows + 1), positions = new Float32Array(count * 3), colors = new Float32Array(count * 3), normals = new Float32Array(count * 3), index = [];
 for (let i = 0; i < count; i++) normals.set(axis === 'x' ? [1, 0, 0] : [0, 0, 1], i * 3);
 for (let i = 0; i < steps; i++) for (let j = 0; j < rows; j++) { const a = i * (rows + 1) + j, b = a + rows + 1; index.push(a, b, a + 1, b, b + 1, a + 1); }
 const geometry = new THREE.BufferGeometry();
 geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3).setUsage(THREE.DynamicDrawUsage));
 geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3).setUsage(THREE.DynamicDrawUsage));
 geometry.setAttribute('normal', new THREE.BufferAttribute(normals, 3));
 geometry.setIndex(index);
 const mesh = new THREE.Mesh(geometry, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .9, side: THREE.DoubleSide, emissive: '#0b2a38', emissiveIntensity: .35 }));
 // The cut line on the surface: a hot gold edge.
 const edgeGeo = new THREE.BufferGeometry(), edgePos = new Float32Array((steps + 1) * 3);
 edgeGeo.setAttribute('position', new THREE.BufferAttribute(edgePos, 3).setUsage(THREE.DynamicDrawUsage));
 const edge = new THREE.Line(edgeGeo, new THREE.LineBasicMaterial({ color: '#ffd98f', transparent: true, opacity: .95 }));
 const tmp = new THREE.Color();
 let key = '';
 function set(fixed, from, to) {
  const next = `${fixed.toFixed(3)}:${from.toFixed(3)}:${to.toFixed(3)}`;
  mesh.visible = edge.visible = fixed > -HALF && fixed < HALF && to - from > .01;
  if (!mesh.visible || next === key) return;
  key = next;
  for (let i = 0; i <= steps; i++) {
   const c = lerp(from, to, i / steps), x = axis === 'x' ? fixed : c, z = axis === 'x' ? c : fixed, top = sample(x, z);
   edgePos.set([x, top + .012, z], i * 3);
   for (let j = 0; j <= rows; j++) {
    const k = j / rows, y = lerp(top, FLOOR, k * k * .55 + k * .45); // denser rows near the surface
    const v = i * (rows + 1) + j;
    positions.set([x, y, z], v * 3);
    groundColor(top - y, x, z, tmp); colors.set([tmp.r, tmp.g, tmp.b], v * 3);
   }
  }
  geometry.attributes.position.needsUpdate = geometry.attributes.color.needsUpdate = true;
  edgeGeo.attributes.position.needsUpdate = true;
  geometry.computeBoundingSphere(); edgeGeo.computeBoundingSphere();
 }
 return { mesh, edge, set };
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .018 });
 // Soft fill from the south-east so south-facing sections read as clearly as east ones.
 const fill = new THREE.DirectionalLight('#d4ecf7', 1.1); fill.position.set(5, 6, 10); scene.add(fill);
 const land = terrain({ segments: 220 }), sample = gridSampler(land);
 const sides = blockSides(sample, { floor: FLOOR, color: groundColor });
 const water = riverWater(sample);
 scene.add(land.mesh, sides, water);

 // Two clip planes, intersected: x > cutX AND z > cutZ is removed. An unused
 // plane sits at OFF so its half-space covers everything and the other cut acts alone.
 const planeX = new THREE.Plane(new THREE.Vector3(-1, 0, 0), OFF), planeZ = new THREE.Plane(new THREE.Vector3(0, 0, -1), OFF);
 const clipped = [land.mesh.material, water.material];
 sides.traverse(o => { if (o.material) clipped.push(o.material); });
 for (const m of clipped) { m.clippingPlanes = [planeX, planeZ]; m.clipIntersection = true; }

 const faceX = section(sample, 'x'), faceZ = section(sample, 'z');
 scene.add(faceX.mesh, faceX.edge, faceZ.mesh, faceZ.edge);

 // Groundwater drifting through the saturated zone on each open face.
 const FLOW = 240, flow = glowPoints(FLOW * 2, { size: .17, color: '#b4ecff' }), seeds = [], random = rng(5);
 for (let i = 0; i < FLOW * 2; i++) seeds.push([random(), random(), .4 + random() * .6]);
 scene.add(flow);
 // A glowing water-table trace along each face.
 const tableX = glowPoints(120, { size: .14, color: '#8fe0ff' }), tableZ = glowPoints(120, { size: .14, color: '#8fe0ff' });
 scene.add(tableX, tableZ);

 // Monitoring wells drilled just in front of the final notch faces.
 const wells = [[2.5, .36], [4.3, .36], [1.26, 2.3], [1.26, 4.5]].map(([x, z], i) => {
  const top = sample(x, z), bottom = top - aquiferBase(x, z) + .05, wt = top - waterTable(x, z);
  const casing = new THREE.Mesh(new THREE.CylinderGeometry(.032, .032, 1, 12), new THREE.MeshStandardMaterial({ color: '#c9d3d8', metalness: .7, roughness: .35 }));
  const screen = new THREE.Mesh(new THREE.CylinderGeometry(.04, .04, 1, 12), new THREE.MeshBasicMaterial({ color: '#8fe6ff', transparent: true, opacity: .9 }));
  const head = glowPoints(1, { size: .9, color: '#ffd98f' }), level = glowPoints(1, { size: .7, color: '#8fe6ff' });
  head.positions.set([x, top + .16, z]); level.positions.set([x, wt, z]); head.commit(); level.commit();
  scene.add(casing, screen, head, level);
  return { x, z, top, bottom, wt, casing, screen, head, level, delay: i * .55 };
 });

 let cutX = OFF, cutZ = OFF;
 function update(t) {
  // Beat 1 (0–6 s): an east cut sweeps in.  Beat 2 (6–12 s): it heals and a
  // south cut opens.  Beat 3 (12–18 s): the west closes into a corner notch.
  const east = easeInOut(smooth(.4, 4.6, t)), heal = easeInOut(smooth(6, 7.6, t));
  const south = easeInOut(smooth(7.4, 10.8, t)), notch = easeInOut(smooth(12, 14.6, t)), close = easeInOut(smooth(16.3, 17.8, t));
  // Each cut is a number or null (unused). Removed: x > xCut AND z > zCut.
  let xCut = null, zCut = null;
  if (t < 7.6) xCut = lerp(CLOSED, .9, east * (1 - heal));
  else if (t < 12) zCut = lerp(CLOSED, .3, south);
  else { xCut = lerp(lerp(-HALF - .2, 1.2, notch), CLOSED, close); zCut = .3; }
  if (xCut !== null && xCut >= HALF) { xCut = null; if (t >= 12) zCut = null; }
  if (zCut !== null && zCut >= HALF) zCut = null;
  // An unused plane covers everything so the other acts alone; with no cut at
  // all, park X beyond the block so nothing is removed.
  planeX.constant = xCut ?? (zCut === null ? CLOSED : OFF);
  planeZ.constant = zCut ?? OFF;
  cutX = xCut ?? OFF; cutZ = zCut ?? OFF;
  const xActive = xCut !== null && xCut > -HALF, zActive = zCut !== null;
  faceX.set(xActive ? xCut : OFF, zActive ? zCut : -HALF, HALF);
  faceZ.set(zActive ? zCut : OFF, xActive ? xCut : -HALF, HALF);

  // Flow particles ride the saturated band of whichever faces are open.
  const faces = [[faceX.mesh.visible, 'x', cutX, zActive ? cutZ : -HALF], [faceZ.mesh.visible, 'z', cutZ, xActive ? cutX : -HALF]];
  faces.forEach(([open, axis, fixed, from], f) => {
   for (let i = 0; i < FLOW; i++) {
    const n = f * FLOW + i, [u0, d, speed] = seeds[n];
    const u = (u0 + t * .018 * speed) % 1, c = lerp(from, HALF, u);
    const x = axis === 'x' ? fixed + .02 : c, z = axis === 'x' ? c : fixed + .02;
    const top = sample(x, z), wt = waterTable(x, z), base = aquiferBase(x, z);
    flow.positions.set([x, top - lerp(wt + .03, base - .03, d), z], n * 3);
    flow.alphas[n] = open ? (.35 + .65 * Math.sin(u * Math.PI)) * clamp(1.6 - Math.abs(2 * d - 1) * 1.2) : 0;
   }
  });
  flow.commit();
  [[tableX, faceX, 'x', cutX, zActive ? cutZ : -HALF], [tableZ, faceZ, 'z', cutZ, xActive ? cutX : -HALF]].forEach(([pts, face, axis, fixed, from]) => {
   for (let i = 0; i < 120; i++) {
    const c = lerp(from, HALF, i / 119), x = axis === 'x' ? fixed + .025 : c, z = axis === 'x' ? c : fixed + .025;
    pts.positions.set([x, sample(x, z) - waterTable(x, z), z], i * 3);
    pts.alphas[i] = face.mesh.visible ? .55 + .45 * Math.sin(i * .7 - t * 3) : 0;
   }
   pts.commit();
  });

  // Beat 3: wells drill down, the screened interval lights, the level pulses.
  for (const w of wells) {
   const drill = easeInOut(smooth(12.6 + w.delay, 14.2 + w.delay, t)) * (1 - smooth(16.2, 17, t));
   const len = (w.top + .14 - w.bottom) * drill;
   w.casing.visible = w.screen.visible = drill > .01;
   w.casing.scale.y = Math.max(.001, len); w.casing.position.set(w.x, w.top + .14 - len / 2, w.z);
   const screenTop = Math.min(w.wt - .04, w.top + .14 - len), screenLen = Math.max(.001, screenTop - Math.max(w.bottom, w.top + .14 - len));
   w.screen.scale.y = screenLen; w.screen.position.set(w.x, screenTop - screenLen / 2, w.z);
   w.screen.visible = drill > .7;
   w.head.alphas[0] = drill; w.head.commit();
   w.level.alphas[0] = drill > .9 ? .5 + .5 * Math.sin(t * 5 + w.delay * 3) : 0; w.level.sizes[0] = .5 + .35 * (.5 + .5 * Math.sin(t * 5 + w.delay * 3)); w.level.commit();
  }

  const a = .55 - .45 * smooth(0, 5, t) + 1.15 * smooth(6.2, 10.5, t) - .55 * smooth(12, 15, t) - .15 * smooth(16.5, 18, t);
  orbit(camera, t, { radius: lerp(17.5, 19.5, smooth(12, 15, t) * (1 - smooth(16.5, 18, t))), height: 8.2, target: [0, -.8, 0], start: a, speed: 0, bob: .2 });
 }
 update(0);
 return { scene, camera, update, dispose() { for (const f of [faceX, faceZ]) { f.edge.geometry.dispose(); } } };
}

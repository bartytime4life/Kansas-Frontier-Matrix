import { THREE, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, smooth, window01, lerp, clamp } from './kit.mjs';
import { SCENE_CATALOG } from './catalog.mjs';
// Aviation & airspace: the land reads as a chart (banded tint and contours),
// runways and circled airport symbols surface, controlled airspace rises in
// tiers over each field, then a departure climbs out through the layers.

const T = SCENE_CATALOG.aviation.duration;
// Two fields: a towered Class C airport with a shelf, and a smaller Class D.
const FIELDS = [
 { x: -1.4, z: .8, heading: .32, length: 2.3, color: '#c0408c', tiers: [[0, 1.9, 0, 2.5], [1.9, 3.6, 1.15, 2.5]] },
 { x: 3.7, z: -2.3, heading: -.7, length: 1.3, color: '#3f7fd8', tiers: [[0, 1.25, 0, 1.6]] },
];
const RISE = [[6.2, 8.6], [7.4, 9.6]]; // airspace rise windows per field

function circle(radius, y, color) {
 const points = Array.from({ length: 129 }, (_, i) => { const a = i / 128 * Math.PI * 2; return new THREE.Vector3(Math.cos(a) * radius, y, Math.sin(a) * radius); });
 return new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), new THREE.LineBasicMaterial({ color, transparent: true, opacity: 0, depthWrite: false }));
}

/** One airspace tier: inner/outer radius, floor and ceiling above the field. Walls, a faint lid and bright rims. */
function tier([inner, outer, floor, ceiling], color) {
 const group = new THREE.Group(), height = ceiling - floor, fills = [], rims = [];
 const wallMaterial = () => new THREE.MeshBasicMaterial({ color, transparent: true, opacity: 0, side: THREE.DoubleSide, depthWrite: false, blending: THREE.AdditiveBlending });
 const wall = new THREE.Mesh(new THREE.CylinderGeometry(outer, outer, height, 96, 1, true), wallMaterial());
 wall.position.y = floor + height / 2; fills.push([wall.material, .12]); group.add(wall);
 const lid = new THREE.Mesh(new THREE.RingGeometry(inner, outer, 96), wallMaterial());
 lid.rotation.x = -Math.PI / 2; lid.position.y = ceiling; fills.push([lid.material, .09]); group.add(lid);
 if (floor > 0) {
  const base = new THREE.Mesh(new THREE.RingGeometry(inner, outer, 96), wallMaterial());
  base.rotation.x = -Math.PI / 2; base.position.y = floor; fills.push([base.material, .06]); group.add(base);
  const under = circle(inner, floor, color); rims.push(under.material); group.add(under);
 }
 for (const y of [floor, ceiling]) { const rim = circle(outer, y, color); rims.push(rim.material); group.add(rim); }
 return { group, fills, rims };
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .02, background: '#071722' });
 const land = terrain({ segments: 220 });
 const u = liveSurface(land);
 u.contourColor.value.set('#6b5a3a'); u.contourStep.value = 9;
 scene.add(land.mesh, blockSides(land.sample), riverWater(land.sample));

 const fields = FIELDS.map(field => {
  const ground = land.sample(field.x, field.z), root = new THREE.Group();
  root.position.set(field.x, ground, field.z); root.rotation.y = field.heading;
  // Runway, centreline dashes and the chart's circled airport symbol.
  const runway = new THREE.Mesh(new THREE.BoxGeometry(field.length, .03, .16), new THREE.MeshStandardMaterial({ color: '#1b2c55', emissive: '#14306a', emissiveIntensity: .6, transparent: true, opacity: 0 }));
  runway.position.y = .04;
  const dashes = new THREE.Group();
  for (let k = -4; k <= 4; k++) { const d = new THREE.Mesh(new THREE.BoxGeometry(field.length / 14, .035, .018), new THREE.MeshBasicMaterial({ color: '#f4f1e2', transparent: true, opacity: 0 })); d.position.set(k * field.length / 10, .045, 0); dashes.add(d); }
  const symbol = new THREE.Mesh(new THREE.RingGeometry(field.length * .58, field.length * .58 + .07, 96), new THREE.MeshBasicMaterial({ color: field.color, transparent: true, opacity: 0, side: THREE.DoubleSide, depthWrite: false }));
  symbol.rotation.x = -Math.PI / 2; symbol.position.y = .06;
  const airspace = new THREE.Group(), tiers = field.tiers.map(spec => tier(spec, field.color));
  for (const t of tiers) airspace.add(t.group);
  root.add(runway, dashes, symbol);
  airspace.position.set(field.x, ground, field.z);
  scene.add(root, airspace);
  return { field, ground, runway, dashes, symbol, airspace, tiers };
 });

 // A departure from the Class C runway: rolls, rotates, climbs through the core and over the shelf.
 const c = fields[0], dir = new THREE.Vector3(Math.cos(c.field.heading), 0, -Math.sin(c.field.heading));
 const at = (along, side, y) => new THREE.Vector3(c.field.x + dir.x * along - dir.z * side, c.ground + y, c.field.z + dir.z * along + dir.x * side);
 const route = new THREE.CatmullRomCurve3([at(-1.1, 0, .1), at(.4, 0, .12), at(1.6, 0, .55), at(2.8, .5, 1.3), at(3.6, 1.9, 2.1), at(3.2, 3.3, 2.8), at(1.9, 3.9, 3.2)], false, 'centripetal');
 const TRAIL = 46, plane = glowPoints(TRAIL + 1, { size: .34, color: '#ffe7a8', depthTest: false });
 plane.sizes[0] = 1.35;
 scene.add(plane);

 function update(t) {
  const out = 1 - smooth(T - .9, T, t);
  // Beat 1 (0–6 s): the land takes the chart's banded tint and contours; runways and symbols surface.
  u.hypso.value = smooth(.2, 2.4, t) * .85;
  u.contour.value = smooth(1.2, 3.2, t) * .55 * out;
  fields.forEach(({ runway, dashes, symbol }, i) => {
   const show = smooth(1.4 + i * .6, 2.6 + i * .6, t) * out;
   runway.material.opacity = show; dashes.children.forEach(d => { d.material.opacity = show * .9; });
   symbol.material.opacity = show * .85;
  });
  // Beat 2 (6–12 s): each field's airspace rises tier by tier as translucent volumes.
  fields.forEach(({ airspace, tiers }, i) => {
   const rise = smooth(RISE[i][0], RISE[i][1], t);
   airspace.scale.y = Math.max(.001, rise); airspace.visible = rise > .001;
   const glow = rise * out * (1 + .25 * window01(t, 9.6, 12.4, 1));
   for (const { fills, rims } of tiers) { for (const [m, o] of fills) m.opacity = o * glow; for (const m of rims) m.opacity = .85 * glow; }
  });
  // Beat 3 (12–18 s): the departure and its fading trail.
  const s = smooth(12, 17.2, t), flying = window01(t, 11.8, 17.9, .5);
  for (let k = 0; k <= TRAIL; k++) {
   const p = route.getPoint(clamp(s - k * .012));
   plane.positions.set([p.x, p.y, p.z], k * 3);
   plane.alphas[k] = flying * (k ? (1 - k / TRAIL) * .7 : 1) * (s - k * .012 > 0 ? 1 : 0);
  }
  plane.commit();
  orbit(camera, t, { radius: lerp(20.5, 18.5, smooth(5, 11, t)), height: lerp(9.8, 11.2, smooth(10, 15, t)), target: [.6, .2, -.4], start: -1.05 + .3 * Math.sin(t / T * Math.PI * 2), speed: 0 });
 }
 update(0);
 return { scene, camera, update, dispose() {} };
}

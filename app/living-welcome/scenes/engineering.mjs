import { THREE, HALF, WORLD, RELIEF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, ribbon, surfacePath, riverZ, smooth, window01, lerp, clamp } from './kit.mjs';
// Engineering: truss bridges assemble where mapped roads cross the river, a
// survey line measures distance and grade with a profile curtain, then
// flow-accumulation paths grow from the ridges down to the river.

const ROADS = [-4.3, -1.7, 1.2, 3.6]; // north–south roads, each crossing the river once
const roadX = (x0, z) => x0 + .25 * Math.sin(z * .5 + x0);
const SPAN = 1.6, TRUSS = .26, DECK_W = .22, BAR = .026;
const SURVEY_A = [-3.4, -4.9], SURVEY_B = [3.5, 4.7], DATUM = 1.95;

/** Equal-arc-length path over the surface, with horizontal side vectors for offsets. */
function arcPath(fn, sample, { step = .04, lift = .03 } = {}) {
 const raw = surfacePath(fn, sample, 300, lift), cum = [0];
 for (let i = 1; i < raw.length; i++) cum.push(cum[i - 1] + raw[i].distanceTo(raw[i - 1]));
 const len = cum[cum.length - 1], n = Math.max(2, Math.ceil(len / step) + 1), pts = [];
 for (let i = 0, j = 0; i < n; i++) {
  const d = len * i / (n - 1);
  while (j < raw.length - 2 && cum[j + 1] < d) j++;
  pts.push(raw[j].clone().lerp(raw[j + 1], clamp((d - cum[j]) / (cum[j + 1] - cum[j] || 1))));
 }
 const sides = pts.map((_, i) => { const a = pts[Math.max(0, i - 1)], b = pts[Math.min(n - 1, i + 1)]; return new THREE.Vector3(-(b.z - a.z), 0, b.x - a.x).normalize(); });
 return { pts, sides, len, ds: len / (n - 1) };
}

/** A flat strip along `path` carrying distance-along and across coordinates for shader patterns. */
function strip(path, width) {
 const { pts, sides, ds } = path, n = pts.length, pos = new Float32Array(n * 6), along = new Float32Array(n * 2), across = new Float32Array(n * 2), index = [];
 for (let i = 0; i < n; i++) {
  const p = pts[i], s = sides[i], w = width / 2;
  pos.set([p.x + s.x * w, p.y, p.z + s.z * w, p.x - s.x * w, p.y, p.z - s.z * w], i * 6);
  along[i * 2] = along[i * 2 + 1] = i * ds; across[i * 2] = 1; across[i * 2 + 1] = -1;
  if (i < n - 1) { const a = i * 2; index.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
 }
 const geometry = new THREE.BufferGeometry();
 geometry.setAttribute('position', new THREE.BufferAttribute(pos, 3));
 geometry.setAttribute('aAlong', new THREE.BufferAttribute(along, 1));
 geometry.setAttribute('aAcross', new THREE.BufferAttribute(across, 1));
 geometry.setIndex(index);
 return geometry;
}

const LINE_VERT = `attribute float aAlong; attribute float aAcross; attribute float aV; attribute vec3 aTint;
 varying float vAlong; varying float vAcross; varying float vV; varying vec3 vTint;
 void main() { vAlong = aAlong; vAcross = aAcross; vV = aV; vTint = aTint; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`;
const OUT = '#include <tonemapping_fragment>\n#include <colorspace_fragment>';
function lineMaterial(fragment, uniforms) {
 return new THREE.ShaderMaterial({ uniforms, vertexShader: LINE_VERT, fragmentShader: `${fragment.replace('}%', `\n${OUT}\n}`)}`, transparent: true, depthWrite: false, side: THREE.DoubleSide, blending: THREE.AdditiveBlending });
}

/** One steel member between two local points, built from a shared unit box. */
const X_AXIS = new THREE.Vector3(1, 0, 0);
function member(geometry, material, a, b, thick) {
 const mesh = new THREE.Mesh(geometry, material), dir = new THREE.Vector3().subVectors(b, a), len = dir.length();
 mesh.position.copy(a).add(b).multiplyScalar(.5);
 mesh.quaternion.setFromUnitVectors(X_AXIS, dir.normalize());
 mesh.scale.set(len, thick, thick);
 mesh.userData.rest = { y: mesh.position.y, sx: len };
 return mesh;
}

/** A small Pratt truss in local space (x along the span), with piers down to the valley floor. */
function truss(unit, steel, concrete, groundAt) {
 const group = new THREE.Group(), parts = [], L = SPAN, H = TRUSS, W = DECK_W, V = (x, y, z) => new THREE.Vector3(x, y, z);
 const xs = Array.from({ length: 7 }, (_, i) => -L / 2 + i * L / 6);
 const add = (mesh, order) => { mesh.userData.order = order; parts.push(mesh); group.add(mesh); };
 const deck = new THREE.Mesh(unit, concrete); deck.scale.set(L + .1, .035, W + .04); deck.userData.rest = { y: 0, sx: L + .1 };
 add(deck, 0);
 for (const px of [-L / 4, L / 4]) {
  const drop = Math.max(.12, -groundAt(px) + .02), pier = new THREE.Mesh(unit, concrete);
  pier.scale.set(.07, drop, W * .9); pier.position.set(px, -drop / 2, 0); pier.userData.rest = { y: -drop / 2, sx: .07 };
  add(pier, 0);
 }
 for (const z of [-W / 2, W / 2]) {
  add(member(unit, steel, V(xs[0], .02, z), V(xs[6], .02, z), BAR), 1);
  for (let i = 1; i <= 5; i++) add(member(unit, steel, V(xs[i], .02, z), V(xs[i], H, z), BAR * .8), 2 + i * .15);
  add(member(unit, steel, V(xs[0], .02, z), V(xs[1], H, z), BAR), 3);
  add(member(unit, steel, V(xs[6], .02, z), V(xs[5], H, z), BAR), 3);
  add(member(unit, steel, V(xs[1], H, z), V(xs[5], H, z), BAR), 3.5);
  for (const [a, b] of [[1, 2], [2, 3], [5, 4], [4, 3]]) add(member(unit, steel, V(xs[a], H, z), V(xs[b], .02, z), BAR * .7), 4 + Math.abs(3 - b) * .2);
 }
 for (let i = 1; i <= 5; i++) add(member(unit, steel, V(xs[i], H, -W / 2), V(xs[i], H, W / 2), BAR * .7), 5 + i * .1);
 const nodes = xs.slice(1, 6).flatMap(x => [V(x, H, -W / 2), V(x, H, W / 2)]);
 return { group, parts, nodes };
}

/** D8 flow directions and accumulation on a coarse grid of the synthetic surface. */
function drainage(land, G = 84) {
 const cell = WORLD / G, n = G * G, h = new Float32Array(n), at = i => -HALF + (i + .5) * cell;
 for (let j = 0; j < G; j++) for (let i = 0; i < G; i++) h[j * G + i] = land.height(at(i), at(j));
 const down = new Int32Array(n).fill(-1), step = new Float32Array(n);
 for (let j = 0; j < G; j++) for (let i = 0; i < G; i++) {
  const c = j * G + i;
  let best = 0;
  for (let dj = -1; dj <= 1; dj++) for (let di = -1; di <= 1; di++) {
   const ii = i + di, jj = j + dj;
   if ((!di && !dj) || ii < 0 || jj < 0 || ii >= G || jj >= G) continue;
   const len = Math.hypot(di, dj), drop = (h[c] - h[jj * G + ii]) / len;
   if (drop > best) { best = drop; down[c] = jj * G + ii; step[c] = len * cell; }
  }
 }
 const order = [...Array(n).keys()].sort((a, b) => h[b] - h[a]), acc = new Float32Array(n).fill(1), reach = new Float32Array(n);
 for (const c of order) { const d = down[c]; if (d >= 0) { acc[d] += acc[c]; reach[d] = Math.max(reach[d], reach[c] + step[c]); } }
 const xy = c => [at(c % G), at(Math.floor(c / G))];
 return { G, n, down, step, acc, reach, xy };
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022 });
 const land = terrain({ segments: 220 });
 const u = liveSurface(land);
 u.tint.value.set('#0f2a36');
 const sides = blockSides(land.sample), water = riverWater(land.sample);
 scene.add(land.mesh, sides, water);

 // Roads: each half draws from the block edge toward its mapped crossing.
 const unit = new THREE.BoxGeometry(1, 1, 1);
 const steel = new THREE.MeshStandardMaterial({ color: '#d2b98a', metalness: .55, roughness: .35, emissive: '#e8c37c', emissiveIntensity: .15 });
 const concrete = new THREE.MeshStandardMaterial({ color: '#a7a397', roughness: .8, emissive: '#3a3226', emissiveIntensity: .3 });
 const roads = [], bridges = [];
 const nodeGlow = glowPoints(ROADS.length * 12, { size: .26, color: '#f3d38e' });
 const markGeo = new THREE.RingGeometry(.2, .26, 48); markGeo.rotateX(-Math.PI / 2);
 for (const [b, x0] of ROADS.entries()) {
  let zc = riverZ(x0);
  for (let k = 0; k < 6; k++) zc = riverZ(roadX(x0, zc));
  const xc = roadX(x0, zc), zN = zc - SPAN / 2, zS = zc + SPAN / 2;
  const deckY = Math.max(land.sample(roadX(x0, zN), zN), land.sample(roadX(x0, zS), zS)) + .05;
  for (const [from, to] of [[-HALF, zN], [HALF, zS]]) {
   const mesh = ribbon(surfacePath(s => { const z = lerp(from, to, s); return [roadX(x0, z), z]; }, land.sample, 90, .025), { width: .075, color: '#e3dccb', opacity: .9 });
   roads.push(mesh); scene.add(mesh);
  }
  // Orient local +x along the road at the crossing.
  const dx = roadX(x0, zS) - roadX(x0, zN), dz = zS - zN, theta = Math.atan2(-dz, dx);
  const groundAt = lx => land.sample(xc + Math.cos(theta) * lx, zc - Math.sin(theta) * lx) - deckY;
  const tr = truss(unit, steel, concrete, groundAt);
  tr.group.position.set(xc, deckY, zc); tr.group.rotation.y = theta;
  scene.add(tr.group);
  tr.group.updateMatrixWorld(true);
  tr.nodes.forEach((p, i) => { const w = p.clone().applyMatrix4(tr.group.matrixWorld); nodeGlow.positions.set([w.x, w.y, w.z], (b * 12 + i) * 3); });
  for (const [i, lx] of [[10, -SPAN / 2], [11, SPAN / 2]]) nodeGlow.positions.set([xc + Math.cos(theta) * lx, deckY + .05, zc - Math.sin(theta) * lx], (b * 12 + i) * 3);
  const mark = new THREE.Mesh(markGeo, new THREE.MeshBasicMaterial({ color: '#f3d38e', transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide }));
  mark.position.set(xc, land.sample(xc, zc) + .04, zc);
  scene.add(mark);
  bridges.push({ ...tr, mark, start: 1.3 + b * .6 });
 }
 scene.add(nodeGlow);

 // Survey: a dashed line with ticks, and a grade profile standing on a datum above it.
 const survey = arcPath(s => [lerp(SURVEY_A[0], SURVEY_B[0], s), lerp(SURVEY_A[1], SURVEY_B[1], s)], land.sample, { step: .05, lift: .04 });
 const su = { uReveal: { value: 0 }, uOp: { value: 0 }, uColor: { value: new THREE.Color('#f3d38e') } };
 const surveyLine = new THREE.Mesh(strip(survey, .065), lineMaterial(`uniform float uReveal; uniform float uOp; uniform vec3 uColor; varying float vAlong; varying float vAcross;
  void main() { if (vAlong > uReveal) discard; float dash = step(.45, fract(vAlong * 3.2)); float head = exp(-pow((uReveal - vAlong) / .2, 2.0));
  gl_FragColor = vec4(uColor * (1.0 + head * 2.0), uOp * max(dash, head) * (1.0 - smoothstep(.6, 1.0, abs(vAcross))));
  }%`, su));
 surveyLine.renderOrder = 3;
 const n = survey.pts.length, grade = new Float32Array(n), tints = [], color = new THREE.Color();
 const flat = new THREE.Color('#7fd3ea'), mid = new THREE.Color('#f3d38e'), steep = new THREE.Color('#ff9a5a');
 for (let i = 0; i < n; i++) {
  const a = survey.pts[Math.max(0, i - 3)], b = survey.pts[Math.min(n - 1, i + 3)];
  grade[i] = Math.abs(b.y - a.y) / Math.hypot(b.x - a.x, b.z - a.z);
  color.copy(flat).lerp(mid, smooth(.03, .14, grade[i])).lerp(steep, smooth(.16, .32, grade[i]));
  tints.push(color.r, color.g, color.b);
 }
 const profileY = i => DATUM + .18 + (survey.pts[i].y - .04) / RELIEF * 1.05;
 // Curtain between datum and profile, plus a bright edge band along the profile itself.
 function curtain(bottom, top) {
  const pos = [], along = [], v = [], tint = [], index = [];
  for (let i = 0; i < n; i++) {
   const p = survey.pts[i];
   pos.push(p.x, bottom(i), p.z, p.x, top(i), p.z); along.push(i * survey.ds, i * survey.ds); v.push(0, 1);
   tint.push(...tints.slice(i * 3, i * 3 + 3), ...tints.slice(i * 3, i * 3 + 3));
   if (i < n - 1) { const a = i * 2; index.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('aAlong', new THREE.Float32BufferAttribute(along, 1));
  g.setAttribute('aAcross', new THREE.Float32BufferAttribute(new Array(n * 2).fill(0), 1));
  g.setAttribute('aV', new THREE.Float32BufferAttribute(v, 1));
  g.setAttribute('aTint', new THREE.Float32BufferAttribute(tint, 3));
  g.setIndex(index);
  return g;
 }
 const pu = { uReveal: su.uReveal, uOp: { value: 0 } };
 const fill = new THREE.Mesh(curtain(() => DATUM, profileY), lineMaterial(`uniform float uReveal; uniform float uOp; varying float vAlong; varying float vV; varying vec3 vTint;
  void main() { if (vAlong > uReveal) discard; float grid = step(.9, fract(vAlong * 2.0)) * .25;
  gl_FragColor = vec4(vTint, uOp * (.07 + .42 * pow(vV, 1.6) + grid * vV)); }%`, pu));
 const edge = new THREE.Mesh(curtain(i => profileY(i) - .05, i => profileY(i) + .01), lineMaterial(`uniform float uReveal; uniform float uOp; varying float vAlong; varying float vV; varying vec3 vTint;
  void main() { if (vAlong > uReveal) discard; float head = exp(-pow((uReveal - vAlong) / .25, 2.0));
  gl_FragColor = vec4(vTint * (1.2 + head * 2.0), uOp * (.35 + .65 * vV)); }%`, pu));
 const datum = new THREE.Mesh(curtain(() => DATUM - .008, () => DATUM + .008), lineMaterial(`uniform float uReveal; uniform float uOp; varying float vAlong;
  void main() { if (vAlong > uReveal) discard; gl_FragColor = vec4(.5, .83, .92, uOp * .55 * step(.4, fract(vAlong * 6.0))); }%`, pu));
 fill.renderOrder = edge.renderOrder = datum.renderOrder = 4;
 scene.add(surveyLine, fill, edge, datum);
 // Ticks every unit of distance: a post on the ground and a faint drop line up to the datum.
 const tickMat = new THREE.MeshBasicMaterial({ color: '#f3d38e', transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending });
 const dropMat = new THREE.MeshBasicMaterial({ color: '#8fd6ee', transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending });
 const ticks = [];
 for (let d = 0; d <= survey.len + 1e-3; d += 1) {
  const i = Math.min(n - 1, Math.round(d / survey.ds)), p = survey.pts[i];
  const post = new THREE.Mesh(unit, tickMat); post.position.set(p.x, p.y + .09, p.z); post.scale.set(.025, .18, .025);
  const cross = new THREE.Mesh(unit, tickMat); cross.position.set(p.x, p.y + .005, p.z); cross.scale.set(.03, .01, .24); cross.rotation.y = Math.atan2(survey.sides[i].x, survey.sides[i].z);
  const drop = new THREE.Mesh(unit, dropMat), hgt = profileY(i) - p.y - .2; drop.position.set(p.x, p.y + .2 + hgt / 2, p.z); drop.scale.set(.008, hgt, .008);
  scene.add(post, cross, drop);
  ticks.push({ d, post, cross, drop });
 }
 // Tripods at both ends and a cursor riding the reveal front, tied up to its point on the profile.
 const survMarks = glowPoints(4, { size: .5, color: '#f3d38e' });
 const legGeo = new THREE.CylinderGeometry(.008, .012, .42, 5), legMat = new THREE.MeshStandardMaterial({ color: '#d8c7a0', metalness: .3, roughness: .5 });
 const tripods = [SURVEY_A, SURVEY_B].map(([x, z], i) => {
  const g = new THREE.Group(), y = land.sample(x, z);
  for (let k = 0; k < 3; k++) { const leg = new THREE.Mesh(legGeo, legMat), a = k * 2.1 + .3; leg.position.set(Math.cos(a) * .07, .19, Math.sin(a) * .07); leg.rotation.set(Math.sin(a) * .35, 0, -Math.cos(a) * .35); g.add(leg); }
  g.position.set(x, y, z); scene.add(g);
  survMarks.positions.set([x, y + .44, z], i * 3);
  return g;
 });
 const cursorLine = new THREE.Mesh(unit, new THREE.MeshBasicMaterial({ color: '#f3d38e', transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending }));
 scene.add(survMarks, cursorLine);

 // Drainage: flow segments revealed by how far upstream water has travelled to reach them.
 const flow = drainage(land), segs = { pos: [], along: [], across: [], acc: [] }, index = [];
 const MIN_ACC = 9, p0 = new THREE.Vector3(), p1 = new THREE.Vector3(), side = new THREE.Vector3();
 let reachMax = 0;
 for (let c = 0; c < flow.n; c++) {
  const d = flow.down[c];
  if (d < 0 || flow.acc[c] < MIN_ACC) continue;
  const [x0, z0] = flow.xy(c), [x1, z1] = flow.xy(d);
  if (Math.abs(z0 - riverZ(x0)) < .2 && Math.abs(z1 - riverZ(x1)) < .2) continue; // the river itself is drawn as water
  p0.set(x0, land.sample(x0, z0) + .035, z0); p1.set(x1, land.sample(x1, z1) + .035, z1);
  const w = clamp(.012 + .009 * Math.log2(flow.acc[c]), .014, .075) / 2;
  side.set(-(p1.z - p0.z), 0, p1.x - p0.x).normalize().multiplyScalar(w);
  const a = segs.pos.length / 3, r0 = flow.reach[c], r1 = r0 + flow.step[c], lg = Math.log2(flow.acc[c]);
  segs.pos.push(p0.x + side.x, p0.y, p0.z + side.z, p0.x - side.x, p0.y, p0.z - side.z, p1.x + side.x, p1.y, p1.z + side.z, p1.x - side.x, p1.y, p1.z - side.z);
  segs.along.push(r0, r0, r1, r1); segs.across.push(1, -1, 1, -1); segs.acc.push(lg, lg, lg, lg);
  index.push(a, a + 1, a + 2, a + 1, a + 3, a + 2);
  reachMax = Math.max(reachMax, r1);
 }
 const flowGeo = new THREE.BufferGeometry();
 flowGeo.setAttribute('position', new THREE.Float32BufferAttribute(segs.pos, 3));
 flowGeo.setAttribute('aAlong', new THREE.Float32BufferAttribute(segs.along, 1));
 flowGeo.setAttribute('aAcross', new THREE.Float32BufferAttribute(segs.across, 1));
 flowGeo.setAttribute('aV', new THREE.Float32BufferAttribute(segs.acc, 1));
 flowGeo.setAttribute('aTint', new THREE.Float32BufferAttribute(new Array(segs.along.length * 3).fill(0), 3));
 flowGeo.setIndex(index);
 const fu = { uReveal: { value: 0 }, uOp: { value: 0 }, uColor: { value: new THREE.Color('#4fb6e6') } };
 const flowMesh = new THREE.Mesh(flowGeo, lineMaterial(`uniform float uReveal; uniform float uOp; uniform vec3 uColor; varying float vAlong; varying float vAcross; varying float vV;
  void main() { if (vAlong > uReveal) discard; float head = exp(-pow((uReveal - vAlong) / .3, 2.0)); float strength = .3 + .7 * clamp((vV - 3.0) / 6.0, 0.0, 1.0);
  gl_FragColor = vec4(uColor * (1.0 + head * 1.5), uOp * (strength + head) * (1.0 - smoothstep(.4, 1.0, abs(vAcross)))); }%`, fu));
 flowMesh.renderOrder = 3;
 scene.add(flowMesh);
 // Droplets riding the larger channels down to the river once the network has grown.
 const starts = [];
 for (let c = 0; c < flow.n; c++) if (flow.acc[c] >= 14 && flow.acc[c] < 40 && flow.reach[c] > 1.4) starts.push(c);
 const paths = [];
 for (let k = 0; k < starts.length && paths.length < 36; k += Math.max(1, Math.floor(starts.length / 36))) {
  const pts = [];
  for (let c = starts[k], guard = 0; c >= 0 && guard < 120; c = flow.down[c], guard++) {
   const [x, z] = flow.xy(c);
   pts.push(new THREE.Vector3(x, land.sample(x, z) + .05, z));
   if (Math.abs(z - riverZ(x)) < .2) break;
  }
  if (pts.length > 4) paths.push(pts);
 }
 const DROPS = 4, drops = glowPoints(paths.length * DROPS, { size: .16, color: '#bff0ff' });
 scene.add(drops);

 function update(t) {
  // Beat 1 (0–5.5 s): roads reach each crossing, the crossing pings, and the truss assembles member by member.
  // (Roads dim in beat 3 so the drainage network reads.)
  const out = 1 - smooth(15, 15.8, t);
  roads.forEach((r, i) => { const b = bridges[i >> 1]; r.reveal(smooth(.2, b.start, t)); r.material.opacity = lerp(.9, .5, smooth(10.8, 11.8, t)) * out; });
  let lit = 0;
  for (const [b, br] of bridges.entries()) {
   const ping = clamp((t - br.start + .5) / 1.2);
   br.mark.scale.setScalar(1 + ping * 1.6); br.mark.material.opacity = ping > 0 && ping < 1 ? (1 - ping) * .9 : 0;
   for (const m of br.parts) {
    const k = smooth(br.start + m.userData.order * .3, br.start + m.userData.order * .3 + .35, t) * (1 - smooth(15 - b * .1, 15.6 - b * .1, t));
    m.visible = k > .01;
    m.scale.x = m.userData.rest.sx * Math.max(.01, k);
    m.position.y = m.userData.rest.y + (1 - k) * .3;
   }
   const done = smooth(br.start + 1.8, br.start + 2.1, t), flare = Math.exp(-Math.max(0, t - br.start - 2) * 1.6) * done;
   for (let i = 0; i < 12; i++) { nodeGlow.alphas[b * 12 + i] = (done * (.35 + .2 * Math.sin(t * 2 + i)) + flare) * out; nodeGlow.sizes[b * 12 + i] = .26 + flare * .4; }
   lit += flare;
  }
  nodeGlow.commit();
  steel.emissiveIntensity = (.2 + .6 * Math.min(1, lit)) * out + .12;

  // Beat 2 (5.5–11 s): the survey line draws, ticks pop as it passes, and the grade profile rises above it.
  const sv = window01(t, 5.5, 11.6, .6), reveal = lerp(0, survey.len, smooth(6, 9.2, t));
  su.uReveal.value = reveal; su.uOp.value = sv; pu.uOp.value = sv * smooth(6.2, 7, t);
  for (const tk of ticks) {
   const k = smooth(tk.d, tk.d + .3, reveal) * sv;
   tk.post.visible = tk.cross.visible = tk.drop.visible = k > .01;
   tk.post.scale.y = .18 * Math.max(.01, k);
  }
  tickMat.opacity = sv; dropMat.opacity = sv * .35;
  tripods.forEach(g => { g.visible = sv > .01; g.scale.setScalar(Math.max(.01, sv)); });
  survMarks.alphas[0] = survMarks.alphas[1] = sv * (.7 + .3 * Math.sin(t * 5));
  const ci = Math.min(n - 1, Math.round(reveal / survey.ds)), cp = survey.pts[ci], cy = profileY(ci), drawing = sv * window01(t, 6, 9.4, .3);
  survMarks.positions.set([cp.x, cp.y + .02, cp.z, cp.x, cy, cp.z], 6); survMarks.alphas[2] = survMarks.alphas[3] = drawing; survMarks.sizes[2] = .4; survMarks.sizes[3] = .55;
  survMarks.commit();
  cursorLine.position.set(cp.x, (cp.y + cy) / 2, cp.z); cursorLine.scale.set(.012, Math.max(.01, cy - cp.y), .012); cursorLine.material.opacity = drawing * .8;

  // Beat 3 (11–16 s): flow paths grow from the headwaters downstream and droplets run to the river.
  const dr = smooth(10.8, 11.6, t) * out;
  fu.uReveal.value = lerp(0, reachMax * 1.02, smooth(11.1, 14.6, t)); fu.uOp.value = dr;
  u.tintMix.value = .32 * dr; u.grey.value = .12 * dr;
  const flowing = window01(t, 13.2, 15.7, .7);
  paths.forEach((pts, p) => {
   for (let k = 0; k < DROPS; k++) {
    const f = ((t * .5 + k / DROPS + p * .137) % 1) * (pts.length - 1), i = Math.floor(f), w = f - i, j = (p * DROPS + k) * 3;
    const a = pts[i], b = pts[Math.min(pts.length - 1, i + 1)];
    drops.positions[j] = lerp(a.x, b.x, w); drops.positions[j + 1] = lerp(a.y, b.y, w); drops.positions[j + 2] = lerp(a.z, b.z, w);
    drops.alphas[p * DROPS + k] = flowing * Math.sin(Math.PI * f / (pts.length - 1));
   }
  });
  drops.commit();

  orbit(camera, t, { radius: 22, height: 10.8 - 1.2 * window01(t, 5, 16, 4), target: [0, -.4, 0], start: -.6 - .3 * Math.cos(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update, dispose() {} };
}

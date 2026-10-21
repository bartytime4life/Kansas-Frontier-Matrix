import { THREE, HALF, WORLD, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, riverZ, TRIBUTARIES, tributaryPoint, rng, noise2, smooth, window01, lerp, easeInOut } from './kit.mjs';
// Evidence & provenance: the composite map lifts apart into its source layers,
// features thread up to citation cards, and date/limit tags ride back down.

const D = 16, TAU = Math.PI * 2, PX = 512;
// Seamless sway instead of a one-way orbit, so t = D matches t = 0.
const shoot = (camera, t) => orbit(camera, 8 + 4.5 * Math.sin(TAU * t / D), { radius: 28, height: 10, target: [0, .3, 0], start: -1.21, speed: .045 });
const ARC = -.85 + Math.PI; // citation arc sits opposite the camera's mean azimuth, behind the stack
const toPx = v => (v + HALF) / WORLD * PX;

// Source layers, bottom → top: rest height (collapsed composite) and exploded height.
const LAYERS = [
 { color: '#7fd3ea', rest: 1.98, up: 2.2 }, // hydrography
 { color: '#e8c37c', rest: 2.02, up: 2.75 }, // boundaries
 { color: '#a8ecc8', rest: 2.06, up: 3.3 }, // point sites
];

function canvas2d(w, h) { const c = document.createElement('canvas'); c.width = w; c.height = h; return [c, c.getContext('2d')]; }
function roundRect(g, x, y, w, h, r) {
 g.beginPath(); g.moveTo(x + r, y);
 g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r);
 g.closePath();
}
const texture = c => { const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t; };
function polyline(g, pts) { g.beginPath(); pts.forEach(([x, z], i) => i ? g.lineTo(toPx(x), toPx(z)) : g.moveTo(toPx(x), toPx(z))); g.stroke(); }
function glowLine(g, color, width, pts, blur = 10) { g.strokeStyle = color; g.lineWidth = width; g.shadowColor = color; g.shadowBlur = blur; polyline(g, pts); g.shadowBlur = 0; }

/** A glass map sheet: faint fill and graticule, then the layer's own linework. */
function sheet(draw) {
 const [c, g] = canvas2d(PX, PX);
 g.fillStyle = 'rgba(150,215,235,.05)'; g.fillRect(0, 0, PX, PX);
 g.strokeStyle = 'rgba(160,220,240,.08)'; g.lineWidth = 1;
 for (let i = 32; i < PX; i += 32) { g.beginPath(); g.moveTo(i, 0); g.lineTo(i, PX); g.moveTo(0, i); g.lineTo(PX, i); g.stroke(); }
 g.lineCap = g.lineJoin = 'round';
 draw(g);
 return texture(c);
}

function hydroSheet() {
 const random = rng(23);
 return sheet(g => {
  const main = Array.from({ length: 241 }, (_, i) => { const x = -HALF + i * .05; return [x, riverZ(x)]; });
  glowLine(g, '#7fd3ea', 6, main, 12); glowLine(g, '#e6f8ff', 1.6, main, 0);
  for (const trib of TRIBUTARIES) {
   const pts = Array.from({ length: 61 }, (_, i) => tributaryPoint(trib, i / 60));
   glowLine(g, '#7fd3ea', 3.4, pts, 8);
   for (const s0 of [.3, .62]) { // small headwater streams feeding each tributary
    const [x0, z0] = tributaryPoint(trib, s0), dir = random() < .5 ? -1 : 1, rill = [];
    for (let k = 0; k <= 16; k++) rill.push([x0 + dir * k * .07, z0 + trib.side * k * .045 + .08 * Math.sin(k * .9 + s0 * 7)]);
    glowLine(g, 'rgba(127,211,234,.8)', 1.6, rill, 4);
   }
  }
  for (const [x, z, rx, rz] of [[-4.6, 3.6, .38, .22], [3.3, -3.9, .3, .2]]) { // two small reservoirs
   g.fillStyle = 'rgba(127,211,234,.32)'; g.strokeStyle = '#7fd3ea'; g.lineWidth = 2;
   g.beginPath(); g.ellipse(toPx(x), toPx(z), rx / WORLD * PX, rz / WORLD * PX, .4, 0, TAU); g.fill(); g.stroke();
  }
 });
}

// Synthetic administrative units: a jittered 5×5 vertex net with wandering edges.
function unitNet() {
 const random = rng(31), V = [];
 for (let i = 0; i <= 4; i++) {
  V.push([]);
  for (let j = 0; j <= 4; j++) {
   const edgeX = i === 0 || i === 4, edgeZ = j === 0 || j === 4;
   V[i].push([-HALF + 3 * i + (edgeX ? 0 : (random() - .5) * 1.3), -HALF + 3 * j + (edgeZ ? 0 : (random() - .5) * 1.3)]);
  }
 }
 return V;
}
function boundarySheet(V) {
 const wander = noise2(37);
 const edge = (a, b, k) => Array.from({ length: 25 }, (_, s) => {
  const f = s / 24, x = lerp(a[0], b[0], f), z = lerp(a[1], b[1], f), dx = b[0] - a[0], dz = b[1] - a[1], len = Math.hypot(dx, dz) || 1;
  const off = .22 * Math.sin(Math.PI * f) * wander(x * .9 + k, z * .9 - k);
  return [x - dz / len * off, z + dx / len * off];
 });
 return sheet(g => {
  for (let i = 0; i <= 4; i++) for (let j = 0; j <= 4; j++) {
   const outer = (a, b) => (a === 0 || a === 4) && (b === 0 || b === 4);
   if (i < 4) { const o = (j === 0 || j === 4); glowLine(g, '#e8c37c', o ? 4.5 : 3, o ? [V[i][j], V[i + 1][j]] : edge(V[i][j], V[i + 1][j], i + j * 5), 8); }
   if (j < 4) { const o = (i === 0 || i === 4); glowLine(g, '#e8c37c', o ? 4.5 : 3, o ? [V[i][j], V[i][j + 1]] : edge(V[i][j], V[i][j + 1], i * 3 + j + 40), 8); }
   if (i > 0 && i < 4 && j > 0 && j < 4 && !outer(i, j)) { // vertex markers
    g.fillStyle = '#f3d38e'; g.beginPath(); g.arc(toPx(V[i][j][0]), toPx(V[i][j][1]), 4, 0, TAU); g.fill();
   }
  }
  g.setLineDash([7, 7]); // finer, subordinate subdivisions
  for (const [i, j] of [[0, 1], [1, 2], [2, 0], [3, 3], [2, 2]]) {
   const a = V[i][j], b = V[i + 1][j + 1];
   glowLine(g, 'rgba(232,195,124,.55)', 1.6, [[lerp(a[0], b[0], .5), a[1]], [lerp(a[0], b[0], .5), b[1]]], 0);
  }
  g.setLineDash([]);
 });
}

function pointSheet(sites) {
 return sheet(g => sites.forEach(([x, z], i) => {
  const px = toPx(x), pz = toPx(z);
  g.shadowColor = '#a8ecc8'; g.shadowBlur = 8; g.strokeStyle = '#bff2dc'; g.lineWidth = 2.2; g.fillStyle = '#ffffff';
  if (i % 5 === 4) { g.strokeRect(px - 6, pz - 6, 12, 12); g.fillRect(px - 2, pz - 2, 4, 4); } // a second kind of site
  else { g.beginPath(); g.arc(px, pz, 6.5, 0, TAU); g.stroke(); g.beginPath(); g.arc(px, pz, 2.6, 0, TAU); g.fill(); }
  g.shadowBlur = 0;
 }));
}

let bandCanvas = null;
/** Glowing frame around a plate: four soft strips, brightest along the plate edge. */
function edgeFrame(color, width = .2) {
 if (!bandCanvas) {
  const [c, g] = canvas2d(4, 64), grd = g.createLinearGradient(0, 0, 0, 64);
  grd.addColorStop(0, 'rgba(255,255,255,0)'); grd.addColorStop(.5, 'rgba(255,255,255,1)'); grd.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = grd; g.fillRect(0, 0, 4, 64); bandCanvas = c;
 }
 const h = HALF, w = width / 2, pos = [], uv = [], index = [];
 const sides = [[[-h - w, -h], [h + w, -h], [0, 1]], [[-h - w, h], [h + w, h], [0, 1]], [[-h, -h - w], [-h, h + w], [1, 0]], [[h, -h - w], [h, h + w], [1, 0]]];
 sides.forEach(([a, b, [nx, nz]], k) => {
  for (const [p, s] of [[a, -1], [a, 1], [b, -1], [b, 1]]) { pos.push(p[0] + nx * w * s, 0, p[1] + nz * w * s); uv.push(0, s < 0 ? 0 : 1); }
  const o = k * 4; index.push(o, o + 2, o + 1, o + 1, o + 2, o + 3);
 });
 const geometry = new THREE.BufferGeometry();
 geometry.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
 geometry.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
 geometry.setIndex(index);
 return new THREE.Mesh(geometry, new THREE.MeshBasicMaterial({ map: texture(bandCanvas), color, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide }));
}

/** Two citation-card variants side by side: light rounded sheets with stripe "lines", no text. */
function cardAtlas() {
 const [c, g] = canvas2d(512, 320);
 const rows = [.86, .92, .7, .88, .6, .9, .8, .5, .74];
 for (let k = 0; k < 2; k++) {
  const x0 = k * 256 + 14, y0 = 14, w = 228, h = 292;
  g.shadowColor = 'rgba(143,214,238,.9)'; g.shadowBlur = 12;
  g.fillStyle = 'rgba(236,243,244,.96)'; roundRect(g, x0, y0, w, h, 18); g.fill(); g.shadowBlur = 0;
  g.fillStyle = '#e8c37c'; roundRect(g, x0 + 18, y0 + 20, 74, 11, 5.5); g.fill();
  g.fillStyle = 'rgba(40,70,82,.24)';
  for (let i = 0; i < 9; i++) {
   if (k && i >= 4 && i <= 6) continue;
   roundRect(g, x0 + 18, y0 + 54 + i * 24, (w - 36) * rows[(i + k * 3) % 9], 8, 4); g.fill();
  }
  if (k) { g.fillStyle = 'rgba(127,211,234,.4)'; roundRect(g, x0 + 18, y0 + 148, w - 36, 62, 8); g.fill(); }
  g.strokeStyle = 'rgba(40,70,82,.18)'; g.lineWidth = 2; roundRect(g, x0 + 1, y0 + 1, w - 2, h - 2, 17); g.stroke();
 }
 return texture(c);
}

/** Date-and-limits tag: a gold pill carrying a clock glyph and a bracketed range bar. */
function tagTexture() {
 const [c, g] = canvas2d(160, 64);
 g.shadowColor = 'rgba(243,211,142,.9)'; g.shadowBlur = 10;
 g.fillStyle = '#f0cd85'; roundRect(g, 6, 8, 148, 48, 24); g.fill(); g.shadowBlur = 0;
 g.strokeStyle = '#0b2a36'; g.fillStyle = '#0b2a36'; g.lineWidth = 4; g.lineCap = 'round';
 g.beginPath(); g.arc(34, 32, 14, 0, TAU); g.stroke();
 g.beginPath(); g.moveTo(34, 32); g.lineTo(34, 23); g.moveTo(34, 32); g.lineTo(41, 35); g.stroke();
 g.beginPath(); g.moveTo(64, 32); g.lineTo(136, 32); g.moveTo(64, 22); g.lineTo(64, 42); g.moveTo(136, 22); g.lineTo(136, 42); g.stroke();
 g.beginPath(); g.arc(98, 32, 6, 0, TAU); g.fill();
 return texture(c);
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .02 });
 const land = terrain({ segments: 220 });
 const u = liveSurface(land);
 const sides = blockSides(land.sample);
 const water = riverWater(land.sample);
 scene.add(land.mesh, sides, water);

 // Source plates with their features.
 const V = unitNet(), random = rng(53), sites = [[1.8, 3.6], [-4.2, 2.4]];
 while (sites.length < 46) { const p = [lerp(-5.5, 5.5, random()), lerp(-5.5, 5.5, random())]; if (sites.every(([x, z]) => Math.hypot(x - p[0], z - p[1]) > .7)) sites.push(p); }
 const maps = [hydroSheet(), boundarySheet(V), pointSheet(sites)];
 const plates = LAYERS.map((layer, i) => {
  const group = new THREE.Group();
  const geo = new THREE.PlaneGeometry(WORLD, WORLD); geo.rotateX(-Math.PI / 2);
  const glass = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ map: maps[i], transparent: true, blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide }));
  const frame = edgeFrame(layer.color);
  glass.renderOrder = 3 + i; frame.renderOrder = 3 + i;
  group.add(glass, frame);
  scene.add(group);
  return { ...layer, group, glass, frame };
 });
 const corners = glowPoints(12, { size: .55, color: '#ffffff' });
 plates.forEach((p, i) => { const c = new THREE.Color(p.color); for (let k = 0; k < 4; k++) corners.colors.set([c.r, c.g, c.b], (i * 4 + k) * 3); });
 scene.add(corners);

 // Highlighted features, each with a ring on its plate; cards are assigned in
 // azimuth order around the arc so the threads fan out without crossing.
 const features = [
  { plate: 0, at: [-.6, riverZ(-.6)] }, { plate: 0, at: [-3.8, riverZ(-3.8)] },
  { plate: 1, at: V[2][3] }, { plate: 2, at: sites[0] }, { plate: 2, at: sites[1] },
 ];
 const wrap = a => Math.atan2(Math.sin(a - ARC), Math.cos(a - ARC));
 features.sort((a, b) => wrap(Math.atan2(a.at[1], a.at[0])) - wrap(Math.atan2(b.at[1], b.at[0])));
 const N = features.length;
 const atlas = cardAtlas(), tagMap = tagTexture();
 const cardGlow = glowPoints(N, { size: 4.2, color: '#7fd3ea' }), cores = glowPoints(N, { size: .6 }), heads = glowPoints(N, { size: .55, color: '#fff1c8' });
 const pulses = glowPoints(N * 3, { size: .32, color: '#f3d38e' });
 const p0 = new THREE.Vector3(), p1 = new THREE.Vector3(), p2 = new THREE.Vector3(), p3 = new THREE.Vector3();
 features.forEach((f, i) => {
  const plate = plates[f.plate], color = new THREE.Color(plate.color);
  f.ring = new THREE.Mesh(new THREE.RingGeometry(.16, .21, 48), new THREE.MeshBasicMaterial({ color, transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide }));
  f.ring.rotation.x = -Math.PI / 2; f.ring.position.set(f.at[0], .012, f.at[1]); f.ring.renderOrder = 7;
  plate.group.add(f.ring);
  cores.colors.set([lerp(color.r, 1, .5), lerp(color.g, 1, .5), lerp(color.b, 1, .5)], i * 3);

  const a = ARC + (i - (N - 1) / 2) * .42;
  const card = new THREE.Mesh(new THREE.PlaneGeometry(.95, 1.24), new THREE.MeshBasicMaterial({ map: atlas, transparent: true, depthWrite: false, side: THREE.DoubleSide }));
  const uv = card.geometry.attributes.uv, half = i % 2 * .5;
  for (let k = 0; k < uv.count; k++) uv.setX(k, half + uv.getX(k) * .5);
  card.home = new THREE.Vector3(Math.cos(a) * 9.2, 2.6, Math.sin(a) * 9.2);
  card.position.copy(card.home); card.lookAt(0, 2.6, 0); card.renderOrder = 8;
  scene.add(card);
  f.card = card;

  // Thread: rises off the feature, arcs over the stack and enters the card from the front.
  const inward = new THREE.Vector3(-card.home.x, 0, -card.home.z).normalize();
  p0.set(f.at[0], plate.up + .02, f.at[1]); p3.copy(card.home).addScaledVector(inward, .05).setY(card.home.y - .4);
  p1.copy(p0).setY(p0.y + .95); p2.copy(p3).addScaledVector(inward, 1.8).setY(p3.y + .35);
  f.curve = new THREE.CubicBezierCurve3(p0.clone(), p1.clone(), p2.clone(), p3.clone());
  f.thread = new THREE.Mesh(new THREE.TubeGeometry(f.curve, 72, .014, 5, false), new THREE.MeshBasicMaterial({ color: '#f3d38e', transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false }));
  f.thread.renderOrder = 6;
  scene.add(f.thread);

  f.tag = new THREE.Sprite(new THREE.SpriteMaterial({ map: tagMap, transparent: true, opacity: 0, depthWrite: false }));
  f.tag.scale.set(.62, .25, 1); f.tag.renderOrder = 9;
  scene.add(f.tag);
 });
 scene.add(cardGlow, cores, heads, pulses);

 const q = new THREE.Vector3();
 function update(t) {
  // Beat 1 (0–5.5 s): the composite separates into an exploded stack, edges brightening.
  plates.forEach((p, i) => {
   const e = easeInOut(smooth(.6 + i * .35, 3.4 + i * .35, t)) * (1 - easeInOut(smooth(14.3 + (2 - i) * .2, 15.8, t)));
   p.e = e; p.y = lerp(p.rest, p.up, e);
   p.group.position.y = p.y;
   const moving = Math.sin(Math.PI * e);
   p.glass.material.opacity = .55 + .45 * e;
   p.frame.material.opacity = .3 + .55 * e + .35 * moving;
   for (let k = 0; k < 4; k++) { corners.positions.set([(k & 1 ? 1 : -1) * HALF, p.y, (k & 2 ? 1 : -1) * HALF], (i * 4 + k) * 3); corners.alphas[i * 4 + k] = .25 + .75 * e; }
  });
  corners.commit();
  u.tint.value.set('#0a2330'); u.tintMix.value = .32 * window01(t, 3.5, 15.6, 1.6);

  for (let i = 0; i < N; i++) {
   const f = features[i], plate = plates[f.plate], stagger = i * .26;
   // Beat 2 (5.5–11 s): features light up, cards arrive, threads draw feature → card.
   const lit = smooth(5.6 + stagger, 6.3 + stagger, t) * (1 - smooth(14.6, 15.4, t));
   const card = smooth(6 + stagger, 6.9 + stagger, t) * (1 - smooth(14.1, 14.8, t));
   const draw = easeInOut(smooth(6.5 + stagger, 8.1 + stagger, t));
   const linked = 8.1 + stagger, arrive = 11.4 + i * .28 + 1.5;
   f.card.position.copy(f.card.home).setY(f.card.home.y - .35 * (1 - card));
   f.card.scale.setScalar(.85 + .15 * card);
   f.card.material.opacity = card; f.card.visible = card > .005;
   cardGlow.positions.set([f.card.home.x * 1.02, f.card.position.y, f.card.home.z * 1.02], i * 3);
   cardGlow.alphas[i] = card * (.28 + .5 * window01(t, linked - .1, linked + .8, .25));
   f.thread.geometry.setDrawRange(0, Math.floor(draw * 72) * 30);
   f.thread.material.opacity = .9 * (1 - smooth(14, 14.6, t)); f.thread.visible = draw > 0 && t < 14.6;
   f.curve.getPointAt(Math.min(draw, 1), q);
   heads.positions.set([q.x, q.y, q.z], i * 3); heads.alphas[i] = Math.sin(Math.PI * draw);
   for (let j = 0; j < 3; j++) { // citation pulses travel up the finished thread
    const k = (t - 8.4) * .45 + j / 3 + i * .13;
    f.curve.getPointAt(k - Math.floor(k), q);
    pulses.positions.set([q.x, q.y, q.z], (i * 3 + j) * 3);
    pulses.alphas[i * 3 + j] = window01(t, 8.6 + stagger, 11.3, .45);
   }
   // Beat 3 (11–16 s): a date/limits tag slides down each thread and stays with its feature.
   const slide = easeInOut(smooth(arrive - 1.5, arrive, t)), s = 1 - slide;
   if (s > 0) f.curve.getPointAt(s, q).setY(q.y + .22 * slide);
   else q.set(f.at[0], plate.y + .22, f.at[1]);
   f.tag.position.copy(q);
   f.tag.material.opacity = smooth(11 + i * .28, 11.4 + i * .28, t) * (1 - smooth(15, 15.6, t));
   f.tag.visible = f.tag.material.opacity > .005;
   const ping = window01(t, arrive - .1, arrive + .9, .2);
   f.ring.material.opacity = lit * (.75 + .25 * Math.sin(t * 3 + i));
   f.ring.scale.setScalar(1 + .12 * Math.sin(t * 3 + i) + 1.4 * ping * smooth(arrive - .1, arrive + .9, t));
   cores.positions.set([f.at[0], plate.y + .03, f.at[1]], i * 3); cores.alphas[i] = lit * (.7 + .6 * ping);
  }
  cardGlow.commit(); cores.commit(); heads.commit(); pulses.commit();
  shoot(camera, t);
 }
 update(0);
 return { scene, camera, update, dispose() { bandCanvas = null; } };
}

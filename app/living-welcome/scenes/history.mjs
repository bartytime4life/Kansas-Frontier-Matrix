import { THREE, HALF, WORLD, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, surfacePath, riverZ, TRIBUTARIES, tributaryPoint, rng, smooth, window01, lerp, clamp, easeInOut } from './kit.mjs';
// History: an early survey sheet develops out of the dark as a sepia,
// hand-ruled map on the land, wagon trails draw across it by lantern light,
// then dated editions slide into registration and the land turns modern.

const LOW = .45; // map-like relief while the archival sheet is showing
const TRAILS = [
 s => { const x = lerp(HALF, -HALF, s); return [x, lerp(riverZ(x) + .95, -3.6, smooth(.45, 1, s)) + .2 * Math.sin(s * 11)]; },
 s => { const x = lerp(2.4, -HALF, s); return [x, lerp(riverZ(2.4) + .95, 5.2, s) + .3 * Math.sin(s * 7)]; },
 s => [4.6 + .5 * Math.sin(s * 4), lerp(HALF, riverZ(4.6) + .95, s)],
];
const SHEETS = [{ from: [-1.2, 2.6, -.8], turn: .14, scale: 1.08, start: 11, end: 12.7 }, { from: [1.4, 3, .9], turn: -.1, scale: .94, start: 11.4, end: 13.2 }];

/**
 * Archival sheet as data: R = paper tone, G = ruled grid and neatline, B = drawn
 * features. Shaders decode the channels, so the grid and features can ink in separately.
 */
function parchment(height) {
 const S = 512, c = document.createElement('canvas'); c.width = c.height = S;
 const g = c.getContext('2d'), random = rng(1861), px = x => (x + HALF) / WORLD * S;
 g.fillStyle = 'rgb(188,0,0)'; g.fillRect(0, 0, S, S);
 for (let i = 0; i < 150; i++) { // foxing and stains
  const x = random() * S, y = random() * S, r = 10 + random() * 60, grd = g.createRadialGradient(x, y, 0, x, y, r), v = 110 + random() * 145 | 0;
  grd.addColorStop(0, `rgba(${v},0,0,${.18 + random() * .3})`); grd.addColorStop(1, `rgba(${v},0,0,0)`);
  g.fillStyle = grd; g.fillRect(x - r, y - r, r * 2, r * 2);
 }
 g.lineWidth = 1;
 for (let i = 0; i < 500; i++) { const x = random() * S, y = random() * S, a = random() * Math.PI; g.strokeStyle = `rgba(${random() > .5 ? 240 : 150},0,0,.12)`; g.beginPath(); g.moveTo(x, y); g.lineTo(x + Math.cos(a) * 9, y + Math.sin(a) * 9); g.stroke(); }
 const edge = g.createRadialGradient(S / 2, S / 2, S * .3, S / 2, S / 2, S * .75);
 edge.addColorStop(0, 'rgba(90,0,0,0)'); edge.addColorStop(1, 'rgba(90,0,0,.65)');
 g.fillStyle = edge; g.fillRect(0, 0, S, S);

 g.globalCompositeOperation = 'lighter'; g.lineCap = 'round';
 // A wobbling pen line reads as hand-ruled rather than plotted.
 const pen = (pts, width, style) => { g.lineWidth = width; g.strokeStyle = style; g.beginPath(); pts.forEach(([x, y], i) => (i ? g.lineTo(x, y) : g.moveTo(x, y))); g.stroke(); };
 const ruled = (x0, y0, x1, y1) => Array.from({ length: 25 }, (_, i) => [lerp(x0, x1, i / 24) + (random() - .5) * 1.4, lerp(y0, y1, i / 24) + (random() - .5) * 1.4]);
 for (let k = 1; k < 12; k++) {
  const p = k * S / 12, w = k % 3 ? 1.1 : 2;
  pen(ruled(p, 14, p, S - 14), w, 'rgba(0,220,0,.85)'); pen(ruled(14, p, S - 14, p), w, 'rgba(0,220,0,.85)');
 }
 for (const [inset, w] of [[8, 2.4], [14, 1]]) pen([[inset, inset], [S - inset, inset], [S - inset, S - inset], [inset, S - inset], [inset, inset]], w, 'rgba(0,255,0,1)');
 for (const [x, y] of [[30, 30], [S - 30, 30], [S - 30, S - 30], [30, S - 30]]) { // registration marks
  g.lineWidth = 1.4; g.strokeStyle = 'rgba(0,255,0,1)'; g.beginPath(); g.arc(x, y, 8, 0, Math.PI * 2); g.moveTo(x - 13, y); g.lineTo(x + 13, y); g.moveTo(x, y - 13); g.lineTo(x, y + 13); g.stroke();
 }
 const river = Array.from({ length: 120 }, (_, i) => { const x = lerp(-HALF, HALF, i / 119); return [px(x), px(riverZ(x))]; });
 pen(river, 4.5, 'rgba(0,0,255,.95)'); pen(river.map(([x, y]) => [x, y + 4]), 1, 'rgba(0,0,255,.5)');
 for (const trib of TRIBUTARIES) pen(Array.from({ length: 40 }, (_, i) => { const [x, z] = tributaryPoint(trib, i / 39); return [px(x), px(z)]; }), 1.8, 'rgba(0,0,255,.85)');
 g.lineWidth = 1; g.strokeStyle = 'rgba(0,0,255,.6)';
 g.beginPath();
 for (let i = 0; i < 2600; i++) { // hachures: short strokes down the steeper slopes
  const x = lerp(-HALF, HALF, random()), z = lerp(-HALF, HALF, random()), e = .04;
  const gx = (height(x + e, z) - height(x - e, z)) / (2 * e), gz = (height(x, z + e) - height(x, z - e)) / (2 * e), m = Math.hypot(gx, gz);
  if (m < .32) continue;
  const len = Math.min(8, 2 + m * 5);
  g.moveTo(px(x), px(z)); g.lineTo(px(x) - gx / m * len, px(z) - gz / m * len);
 }
 g.stroke();
 for (let i = 0; i < 7; i++) { const x = 40 + random() * 430, y = 40 + random() * 430; g.lineWidth = 1.3; g.strokeStyle = 'rgba(0,0,255,.9)'; g.beginPath(); g.arc(x, y, 4, 0, Math.PI * 2); g.stroke(); g.fillStyle = 'rgba(0,0,255,.9)'; g.fillRect(x - 1, y - 1, 2, 2); }
 g.lineWidth = 1.2; g.strokeStyle = 'rgba(0,0,255,.9)'; g.beginPath(); // compass star
 for (let k = 0; k < 8; k++) { const a = k * Math.PI / 4, r = k % 2 ? 9 : 20; g.moveTo(462, 60); g.lineTo(462 + Math.cos(a) * r, 60 + Math.sin(a) * r); }
 g.stroke();
 return new THREE.CanvasTexture(c);
}

/** Equal-arc-length path over the surface (at full relief) with horizontal side vectors. */
function arcPath(fn, sample, { step = .04, lift = .05 } = {}) {
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
// Two dotted wheel ruts, ink on the old sheet and gold on today's map.
const TRAIL_VERT = `attribute float aAlong; attribute float aAcross; varying float vAlong; varying float vAcross;
 void main() { vAlong = aAlong; vAcross = aAcross; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`;
const TRAIL_FRAG = `uniform float uReveal; uniform float uOp; uniform float uMod; uniform vec3 uInk; uniform vec3 uGold; varying float vAlong; varying float vAcross;
 void main() {
  if (vAlong > uReveal) discard;
  float a = abs(vAcross), f = fract(vAlong / .1) - .5;
  float rut = 1.0 - smoothstep(.55, .9, length(vec2(f * 2.0, (a - .55) * 3.0)));
  float head = exp(-pow((uReveal - vAlong) / .3, 2.0));
  gl_FragColor = vec4(mix(uInk, uGold, uMod) + uGold * head * 1.5, clamp(rut * .95 + head * .5 * (1.0 - a), 0.0, 1.0) * uOp);
  #include <tonemapping_fragment>
  #include <colorspace_fragment>
 }`;

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022 });
 const block = new THREE.Group();
 scene.add(block);
 const land = terrain({ segments: 220 });
 const u = liveSurface(land);
 u.tint.value.set('#020a0e');
 const sides = blockSides(land.sample), water = riverWater(land.sample);
 const sideMats = [];
 sides.traverse(o => { if (o.material) { o.material.transparent = true; sideMats.push(o.material); } });
 block.add(land.mesh, sides, water);

 const parch = parchment(land.height);
 const hu = {
  uParch: { value: parch }, uSepia: { value: 1 }, uEmerge: { value: 0 }, uGridFront: { value: -7 }, uFeat: { value: 0 }, uFlash: { value: 0 },
  uPaperDark: { value: new THREE.Color('#5a3b1f') }, uPaperLight: { value: new THREE.Color('#e4cd9c') }, uInk: { value: new THREE.Color('#3b2412') },
  uGold: { value: new THREE.Color('#e8c37c') }, uDark: { value: new THREE.Color('#020a0e') },
 };
 const mat = land.mesh.material, live = mat.onBeforeCompile;
 mat.onBeforeCompile = (shader, renderer) => {
  live.call(mat, shader, renderer);
  Object.assign(shader.uniforms, hu);
  shader.vertexShader = shader.vertexShader.replace('#include <common>', '#include <common>\n varying vec2 vPUv; varying vec3 vHPos;')
   .replace('#include <project_vertex>', 'vPUv = vec2((position.x + 6.0) / 12.0, 1.0 - (position.z + 6.0) / 12.0); vHPos = position;\n #include <project_vertex>');
  shader.fragmentShader = shader.fragmentShader.replace('#include <common>', `#include <common>
    uniform sampler2D uParch; uniform float uSepia; uniform float uEmerge; uniform float uGridFront; uniform float uFeat; uniform float uFlash;
    uniform vec3 uPaperDark; uniform vec3 uPaperLight; uniform vec3 uInk; uniform vec3 uGold; uniform vec3 uDark; varying vec2 vPUv; varying vec3 vHPos;`)
   .replace('#include <color_fragment>', `#include <color_fragment>
    vec4 px = texture2D(uParch, vPUv);
    float ink = clamp(px.g * smoothstep(vHPos.x - .6, vHPos.x, uGridFront) + px.b * uFeat, 0.0, 1.0);
    diffuseColor.rgb = mix(diffuseColor.rgb, mix(mix(uPaperDark, uPaperLight, px.r), uInk, ink * .85), uSepia);
    // The sheet develops out of the dark from the centre, with a ragged, paper-driven edge.
    float em = smoothstep(0.0, .2, uEmerge - (length(vHPos.xz) / 8.5 + .3 * (1.0 - px.r)));
    diffuseColor.rgb = mix(uDark, diffuseColor.rgb, em);`)
   .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>
    totalEmissiveRadiance += uGold * (em * (1.0 - em) * 2.4 + uFlash * (.12 + ink * 1.1));`);
 };
 mat.customProgramCacheKey = () => 'kfm-history-surface';

 // Trails: built at full relief inside a group that scales with the surface relief.
 const trailGroup = new THREE.Group();
 block.add(trailGroup);
 const tu = { uOp: { value: 0 }, uMod: { value: 0 }, uInk: { value: new THREE.Color('#2e1a0b') }, uGold: { value: new THREE.Color('#f3d38e') } };
 const trails = TRAILS.map((fn, i) => {
  const path = arcPath(fn, land.sample), uniforms = { ...tu, uReveal: { value: 0 } };
  const mesh = new THREE.Mesh(strip(path, .18), new THREE.ShaderMaterial({ uniforms, vertexShader: TRAIL_VERT, fragmentShader: TRAIL_FRAG, transparent: true, depthWrite: false, side: THREE.DoubleSide }));
  mesh.renderOrder = 3; trailGroup.add(mesh);
  return { path, uniforms, start: 5.6 + i * .7 };
 });
 const WAGONS = 3, LAMPS = 3;
 const lanterns = glowPoints(TRAILS.length * WAGONS * LAMPS * 2 + 4, { size: .2, color: '#ffcf7a' });
 for (let i = 0; i < TRAILS.length * WAGONS * LAMPS; i++) lanterns.sizes[i * 2 + 1] = .75;
 block.add(lanterns);

 // Dated editions: ink-only sheets that slide in misregistered and settle onto the land.
 const sheetGeo = new THREE.PlaneGeometry(WORLD, WORLD, 64, 64);
 sheetGeo.rotateX(-Math.PI / 2);
 const sp = sheetGeo.attributes.position, tops = new Float32Array(sp.count);
 for (let i = 0; i < sp.count; i++) tops[i] = land.sample(sp.getX(i), sp.getZ(i));
 sheetGeo.setAttribute('aTop', new THREE.BufferAttribute(tops, 1));
 const relief = { value: LOW };
 const sheets = SHEETS.map(spec => {
  const su = { uSettle: { value: 0 }, uRelief: relief, uFlashS: { value: 0 }, uSheetInk: { value: new THREE.Color('#4a2c14') }, uPaper: { value: new THREE.Color('#d9c193') }, uGlow: { value: new THREE.Color('#ffe2a8') } };
  const m = new THREE.MeshBasicMaterial({ map: parch, transparent: true, opacity: 0, depthWrite: false, side: THREE.DoubleSide });
  m.onBeforeCompile = shader => {
   Object.assign(shader.uniforms, su);
   shader.vertexShader = shader.vertexShader.replace('#include <common>', '#include <common>\n attribute float aTop; uniform float uSettle; uniform float uRelief;')
    .replace('#include <begin_vertex>', '#include <begin_vertex>\n transformed.y = aTop * uRelief * uSettle + .04;');
   shader.fragmentShader = shader.fragmentShader.replace('#include <common>', '#include <common>\n uniform float uFlashS; uniform vec3 uSheetInk; uniform vec3 uPaper; uniform vec3 uGlow;')
    .replace('#include <map_fragment>', `vec4 px = texture2D(map, vMapUv);
     float ink = clamp(px.g + px.b, 0.0, 1.0);
     float edge = 1.0 - smoothstep(0.0, .01, min(min(vMapUv.x, 1.0 - vMapUv.x), min(vMapUv.y, 1.0 - vMapUv.y)));
     diffuseColor.rgb = mix(mix(uPaper, uSheetInk, ink), uGlow * 1.6, clamp(uFlashS * (ink + edge), 0.0, 1.0));
     diffuseColor.a *= clamp(.16 * px.r + ink * .9 + edge * (.4 + uFlashS), 0.0, 1.0);`);
  };
  m.customProgramCacheKey = () => 'kfm-history-sheet';
  const mesh = new THREE.Mesh(sheetGeo, m);
  mesh.renderOrder = 4; block.add(mesh);
  return { ...spec, mesh, su };
 });
 const corners = [[-HALF + .7, -HALF + .7], [HALF - .7, -HALF + .7], [HALF - .7, HALF - .7], [-HALF + .7, HALF - .7]];
 const sepiaWall = new THREE.Color('#e0c08e'), WHITE = new THREE.Color(1, 1, 1);
 const lampColor = new THREE.Color('#ffcf7a'), flashColor = new THREE.Color('#fff0c8'), cornerBase = TRAILS.length * WAGONS * LAMPS * 2;
 for (let i = 0; i < 4; i++) { lanterns.colors.set([flashColor.r, flashColor.g, flashColor.b], (cornerBase + i) * 3); lanterns.sizes[cornerBase + i] = 1.4; }

 function update(t) {
  // Seam: the loop ends dark, flat and sepia, exactly how it begins.
  const dark = smooth(15, 15.8, t), reset = smooth(15.8, 15.95, t);
  const k = lerp(LOW, 1, smooth(12.6, 14.2, t) * (1 - reset));
  u.relief.value = relief.value = k;
  hu.uSepia.value = 1 - smooth(13, 14.6, t) * (1 - reset);
  sides.scale.y = water.scale.y = trailGroup.scale.y = k;
  block.position.y = lerp(-.6, 0, easeInOut(smooth(0, 3.2, t))) * (1 - reset) + -.6 * reset;

  // Beat 1 (0–5.5 s): the sheet develops from the dark, the grid is ruled west → east, then features ink in.
  hu.uEmerge.value = lerp(0, 1.6, smooth(.2, 3, t));
  hu.uGridFront.value = lerp(-7, 7, smooth(1.2, 4.2, t));
  hu.uFeat.value = smooth(2.6, 4.6, t);
  u.tintMix.value = dark;
  const sideOp = smooth(.8, 2.4, t) * (1 - dark);
  for (const m of sideMats) { m.opacity = sideOp; m.color.copy(sepiaWall).lerp(WHITE, 1 - hu.uSepia.value); }
  sides.visible = sideOp > .01;

  // Beat 2 (5.5–11 s): trails draw as dotted wheel ruts; lantern-lit wagons follow the drawn track.
  tu.uOp.value = smooth(5.4, 6, t) * (1 - dark);
  let j = 0;
  for (const [ti, tr] of trails.entries()) {
   const shown = tr.path.len * smooth(tr.start, tr.start + 3.4, t);
   tr.uniforms.uReveal.value = shown;
   for (let w = 0; w < WAGONS; w++) for (let l = 0; l < LAMPS; l++, j++) {
    const d = ((t - tr.start) * .42 + w * tr.path.len / WAGONS - l * .07 + tr.path.len) % tr.path.len, f = d / tr.path.ds, i = Math.min(tr.path.pts.length - 2, Math.floor(f)), wgt = f - i;
    const a = tr.path.pts[i], b = tr.path.pts[i + 1];
    const x = lerp(a.x, b.x, wgt), y = lerp(a.y, b.y, wgt) * k + .06, z = lerp(a.z, b.z, wgt);
    const on = (d < shown ? 1 : 0) * window01(t, tr.start + .6, 15.6, .8), flicker = .85 + .15 * Math.sin(t * 13 + j * 2.7);
    lanterns.positions.set([x, y, z, x, y, z], j * 6);
    lanterns.alphas[j * 2] = on * flicker; lanterns.alphas[j * 2 + 1] = on * .3 * flicker;
    lanterns.colors.set([lampColor.r, lampColor.g, lampColor.b, lampColor.r, lampColor.g, lampColor.b], j * 6);
   }
   if (ti === 0) tu.uMod.value = smooth(13.2, 14.6, t);
  }

  // Beat 3 (11–16 s): two dated editions slide into registration, flash, and the land crossfades to today.
  let flash = 0;
  for (const s of sheets) {
   const p = easeInOut(smooth(s.start, s.end, t)), f = t > s.end ? Math.exp(-(t - s.end) * 2.6) : 0;
   s.mesh.position.set(lerp(s.from[0], 0, p), lerp(s.from[1], 0, p), lerp(s.from[2], 0, p));
   s.mesh.rotation.y = lerp(s.turn, 0, p); s.mesh.scale.setScalar(lerp(s.scale, 1, p));
   s.su.uSettle.value = smooth(.55, 1, p); s.su.uFlashS.value = f;
   s.mesh.material.opacity = smooth(s.start - .3, s.start + .4, t) * (1 - smooth(13.6, 14.6, t));
   s.mesh.visible = s.mesh.material.opacity > .01;
   flash = Math.max(flash, f);
  }
  hu.uFlash.value = flash * .8;
  water.material.opacity = .93 * smooth(13.2, 14.4, t) * (1 - smooth(15, 15.6, t));
  corners.forEach(([x, z], i) => { lanterns.positions.set([x, land.sample(x, z) * k + .1, z], (cornerBase + i) * 3); lanterns.alphas[cornerBase + i] = flash; });
  lanterns.commit();

  orbit(camera, t, { radius: 21.5, height: 10.8 - 1.2 * window01(t, 4, 16, 4), target: [0, -.7, 0], start: -.6 - .3 * Math.cos(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update, dispose() { parch.dispose(); } };
}

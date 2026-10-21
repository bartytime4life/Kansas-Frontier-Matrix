import { THREE, HALF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, smooth, window01, lerp, clamp, rng, noise2, riverZ, TRIBUTARIES, tributaryPoint, mainRiver } from './kit.mjs';
import { SCENE_CATALOG } from './catalog.mjs';
// Places & boundaries: county lines trace the state in gold, watershed divides
// follow the high ground between drainages in cool blue, then saved places pin
// down an investigation joined by a dashed path.

const T = SCENE_CATALOG.places.duration;
const COLS = 6, ROWS = 5;
const PINS = [[-3.8, -2.6], [-1, 2.6], [1.6, -1.2], [3.9, 2.2]];
const PIN_AT = PINS.map((_, i) => 11.2 + i * .62); // landing starts

/**
 * Draped polylines merged into one glowing ribbon mesh (one draw call).
 * Each line is a list of [x, z, order]; `reveal` (0..1) traces up to that order,
 * `dash` > 0 breaks it into dashes of that world length that drift with `flow`.
 */
function traceLines(lines, sample, { width = .08, color = '#8fd6ee', lift = .035, opacity = 1, tip = .03, dash = 0 } = {}) {
 const pos = [], ord = [], side = [], arc = [], index = [];
 for (const line of lines) {
  let s = 0;
  for (let i = 0; i < line.length; i++) {
   const [x, z, o] = line[i], a = line[Math.max(0, i - 1)], b = line[Math.min(line.length - 1, i + 1)];
   const l = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1, nx = -(b[1] - a[1]) / l * width / 2, nz = (b[0] - a[0]) / l * width / 2, v = pos.length / 3;
   if (i) s += Math.hypot(x - line[i - 1][0], z - line[i - 1][1]);
   for (const k of [1, -1]) { const px = x + nx * k, pz = z + nz * k; pos.push(px, sample(clamp(px, -HALF, HALF), clamp(pz, -HALF, HALF)) + lift, pz); ord.push(o); side.push(k); arc.push(s); }
   if (i < line.length - 1) index.push(v, v + 1, v + 2, v + 1, v + 3, v + 2);
  }
 }
 const geometry = new THREE.BufferGeometry();
 geometry.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
 geometry.setAttribute('aT', new THREE.Float32BufferAttribute(ord, 1));
 geometry.setAttribute('aSide', new THREE.Float32BufferAttribute(side, 1));
 geometry.setAttribute('aS', new THREE.Float32BufferAttribute(arc, 1));
 geometry.setIndex(index);
 const uniforms = { color: { value: new THREE.Color(color) }, opacity: { value: opacity }, reveal: { value: 1 }, tip: { value: tip }, dash: { value: dash }, flow: { value: 0 } };
 const material = new THREE.ShaderMaterial({
  uniforms, transparent: true, depthWrite: false, side: THREE.DoubleSide, blending: THREE.AdditiveBlending,
  vertexShader: `attribute float aT; attribute float aSide; attribute float aS; varying float vT; varying float vSide; varying float vS;
   void main() { vT = aT; vSide = aSide; vS = aS; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`,
  fragmentShader: `uniform vec3 color; uniform float opacity, reveal, tip, dash, flow; varying float vT; varying float vSide; varying float vS;
   void main() {
    float e = 1.0 - abs(vSide);
    float shown = 1.0 - smoothstep(reveal - 0.004, reveal, vT);
    float head = smoothstep(reveal - tip, reveal, vT) * shown;
    float f = fract(vS / max(dash, 1e-3) - flow);
    float d = dash > 0.0 ? smoothstep(0.0, 0.08, f) * (1.0 - smoothstep(0.5, 0.58, f)) : 1.0;
    float a = (smoothstep(0.45, 0.85, e) + e * e * 0.35) * shown * d * opacity;
    gl_FragColor = vec4(color * (1.0 + head * 3.0), a);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
   }`,
 });
 const mesh = new THREE.Mesh(geometry, material);
 mesh.renderOrder = 3; mesh.frustumCulled = false; mesh.uniforms = uniforms;
 return mesh;
}

/** Chain a fragment overlay onto liveSurface's shader; `vXZ` is world x/z, `glow` adds emissive light. */
function overlay(material, uniforms, head, body, key) {
 const prev = material.onBeforeCompile;
 material.onBeforeCompile = (shader, renderer) => {
  prev?.(shader, renderer);
  Object.assign(shader.uniforms, uniforms);
  shader.vertexShader = shader.vertexShader
   .replace('#include <common>', '#include <common>\nvarying vec2 vXZ;')
   .replace('#include <begin_vertex>', '#include <begin_vertex>\nvXZ = (modelMatrix * vec4(position, 1.0)).xz;');
  shader.fragmentShader = shader.fragmentShader
   .replace('#include <common>', `#include <common>\nvarying vec2 vXZ;\n${head}`)
   .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>\n{ vec3 glow = vec3(0.0);\n${body}\n totalEmissiveRadiance += glow; }`);
 };
 material.customProgramCacheKey = () => key;
}
// Pin landings ripple on the ground itself (draped exactly) with a soft pool of light.
const HEAD = `uniform vec4 rings[4]; uniform vec4 pools[4]; uniform vec3 cRing;`;
const BODY = `
 float aw = max(fwidth(vXZ.x), 1e-4);
 for (int i = 0; i < 4; i++) {
  vec4 r = rings[i]; vec4 p = pools[i];
  float d = length(vXZ - r.xy);
  float ring = 1.0 - smoothstep(0.014, 0.014 + aw * 1.5, abs(d - r.z));
  float ring2 = 1.0 - smoothstep(0.01, 0.01 + aw * 1.5, abs(d - r.z * 0.6));
  glow += cRing * ((ring + ring2 * 0.6) * r.w + exp(-d * d / 0.05) * p.x * 0.35);
 }`;

/** Follow high ground from the block edge down to the river: a synthetic drainage divide. */
function divide(sample, x0, side) {
 const pts = [];
 let x = x0, z = side * (HALF - .06);
 while (Math.abs(z - riverZ(x)) > .3 && pts.length < 200) {
  pts.push([x, z]);
  z -= side * .1;
  let best = x, top = -Infinity;
  for (let k = -5; k <= 5; k++) {
   const cx = clamp(x + k * .05, x0 - .9, x0 + .9), h = sample(cx, z) - .6 * (cx - x0) ** 2;
   if (h > top) { top = h; best = cx; }
  }
  x = best;
 }
 pts.push([x, riverZ(x) + side * .2]); // the divide closes at a pour point on the main stem
 for (let pass = 0; pass < 3; pass++) for (let i = 1; i < pts.length - 1; i++) pts[i][0] = (pts[i - 1][0] + pts[i][0] * 2 + pts[i + 1][0]) / 4;
 return pts;
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022 });
 const land = terrain({ segments: 256 });
 const u = liveSurface(land);
 u.tint.value.set('#0b2830');
 scene.add(land.mesh, blockSides(land.sample), riverWater(land.sample));
 const r = rng(41), wob = noise2(53);

 // Counties: a near-regular grid with surveyed-straight jitter, traced outward from the west.
 const IN = HALF - .06, V = [];
 for (let j = 0; j <= ROWS; j++) for (let i = 0; i <= COLS; i++) {
  const ex = i === 0 || i === COLS, ez = j === 0 || j === ROWS;
  V.push([lerp(-IN, IN, i / COLS) + (ex ? 0 : (r() - .5) * .36), lerp(-IN, IN, j / ROWS) + (ez ? 0 : (r() - .5) * .3)]);
 }
 const vid = (i, j) => j * (COLS + 1) + i, O = [-HALF, 0], dist = p => Math.hypot(p[0] - O[0], p[1] - O[1]);
 const edges = [];
 for (let j = 0; j <= ROWS; j++) for (let i = 0; i < COLS; i++) edges.push([vid(i, j), vid(i + 1, j), j === 0 || j === ROWS]);
 for (let j = 0; j < ROWS; j++) for (let i = 0; i <= COLS; i++) edges.push([vid(i, j), vid(i, j + 1), i === 0 || i === COLS]);
 let maxD = 0;
 const countyLines = edges.map(([a, b, outer], e) => {
  let A = V[a], B = V[b];
  if (dist(B) < dist(A)) [A, B] = [B, A];
  const len = Math.hypot(B[0] - A[0], B[1] - A[1]), n = Math.ceil(len / .07), nx = -(B[1] - A[1]) / len, nz = (B[0] - A[0]) / len;
  maxD = Math.max(maxD, dist(A) + len);
  return Array.from({ length: n + 1 }, (_, k) => {
   const s = k / n, off = outer ? 0 : .05 * wob(e * 2.7, s * 2) * Math.sin(s * Math.PI);
   return [lerp(A[0], B[0], s) + nx * off, lerp(A[1], B[1], s) + nz * off, dist(A) + s * len];
  });
 });
 for (const line of countyLines) for (const p of line) p[2] /= maxD;
 const counties = traceLines(countyLines, land.sample, { width: .075, color: '#d9a548', opacity: .8, tip: .05 });
 scene.add(counties);

 // Watersheds: divides on the high ground between tributaries, each closing at the river.
 const divides = [[-5.2, -1], [-.6, -1], [4.8, -1], [-3.2, 1], [1.8, 1]].map(([x0, side]) => divide(land.sample, x0, side));
 const shedLines = divides.map((pts, k) => pts.map(([x, z], i) => [x, z, k * .07 + i / (pts.length - 1) * .65]));
 const sheds = traceLines(shedLines, land.sample, { width: .2, color: '#2fa8e0', lift: .045, tip: .06 });
 scene.add(sheds);
 const streams = traceLines(TRIBUTARIES.map(trib => Array.from({ length: 81 }, (_, i) => [...tributaryPoint(trib, i / 80), i / 80])), land.sample, { width: .05, color: '#3f9fc6', lift: .02, opacity: 0 });
 scene.add(streams);

 // Drainage: sparks flowing down each tributary and on along the main stem.
 const paths = [...TRIBUTARIES.map(trib => s => tributaryPoint(trib, s)), s => mainRiver(s)].map(fn => Array.from({ length: 161 }, (_, i) => { const [x, z] = fn(i / 160); return [x, land.sample(x, z) + .06, z]; }));
 const sparks = [];
 paths.forEach((path, p) => { const n = p === paths.length - 1 ? 34 : 12; for (let k = 0; k < n; k++) sparks.push({ path, s0: k / n + r() * .03, v: (p === paths.length - 1 ? 2 : 3) / T }); });
 const pour = divides.map(pts => pts[pts.length - 1]);

 // Saved-place pins: gold heads on slim stems, dropped from above.
 const headGeo = new THREE.SphereGeometry(.2, 24, 16).translate(0, .78, 0), stemGeo = new THREE.ConeGeometry(.075, .66, 16).rotateX(Math.PI).translate(0, .33, 0);
 const pins = PINS.map(([x, z]) => {
  const mat = new THREE.MeshStandardMaterial({ color: '#f3d38e', emissive: '#c8902f', emissiveIntensity: 1.1, roughness: .3, metalness: .2, transparent: true });
  const group = new THREE.Group();
  group.add(new THREE.Mesh(headGeo, mat), new THREE.Mesh(stemGeo, mat));
  group.position.set(x, land.sample(x, z), z); group.userData.ground = group.position.y; group.userData.mat = mat;
  scene.add(group);
  return group;
 });

 const G0 = sparks.length, Q0 = G0 + pour.length;
 const glow = glowPoints(Q0 + PINS.length, { size: .24, color: '#8fd6ee' });
 pour.forEach(([x, z], i) => { glow.positions.set([x, land.sample(x, z) + .08, z], (G0 + i) * 3); glow.sizes[G0 + i] = .5; });
 PINS.forEach((_, i) => { glow.colors.set([1, .85, .55], (Q0 + i) * 3); glow.sizes[Q0 + i] = .9; });
 scene.add(glow);

 // Investigation path: a dashed line through the pins, drawn as each one lands.
 const curve = new THREE.CatmullRomCurve3(PINS.map(([x, z]) => new THREE.Vector3(x, 0, z)), false, 'centripetal');
 const trail = traceLines([Array.from({ length: 241 }, (_, i) => { const p = curve.getPoint(i / 240); return [p.x, p.z, i / 240]; })], land.sample, { width: .09, color: '#f3d38e', lift: .06, dash: .2, tip: .02 });
 scene.add(trail);

 const rings = PINS.map(([x, z]) => new THREE.Vector4(x, z, 0, 0)), pools = PINS.map(() => new THREE.Vector4());
 overlay(land.mesh.material, { rings: { value: rings }, pools: { value: pools }, cRing: { value: new THREE.Color('#f3d38e') } }, HEAD, BODY, 'kfm-places-pins');

 function update(t) {
  const out = 1 - smooth(14.8, 15.8, t);

  // Beat 1 (0–5.5 s): county boundaries trace across the state, west to east.
  counties.uniforms.reveal.value = lerp(0, 1.02, smooth(.2, 4.8, t));
  counties.uniforms.opacity.value = .8 * smooth(0, .3, t) * lerp(1, .35, smooth(5.5, 6.6, t)) * out;
  u.tintMix.value = .25 * smooth(0, 1, t) * out;

  // Beat 2 (5.5–11 s): divides climb down from the ridges; streams and sparks show the drainage they part.
  sheds.uniforms.reveal.value = lerp(0, 1.02, smooth(5.7, 8.8, t));
  sheds.uniforms.opacity.value = smooth(5.6, 6, t) * lerp(1, .55, smooth(11, 12, t)) * out;
  streams.uniforms.opacity.value = window01(t, 6.2, 12.4, 1) * .9;
  const flow = window01(t, 6.6, 11.8, 1);
  sparks.forEach((sp, i) => {
   const s = (sp.s0 + t * sp.v) % 1, f = s * 160, k = Math.min(159, Math.floor(f)), a = sp.path[k], b = sp.path[k + 1], w = f - k;
   glow.positions.set([lerp(a[0], b[0], w), lerp(a[1], b[1], w), lerp(a[2], b[2], w)], i * 3);
   glow.alphas[i] = flow * smooth(0, .08, s) * (1 - smooth(.92, 1, s));
  });
  pour.forEach((_, i) => { glow.alphas[G0 + i] = smooth(8.2 + i * .1, 8.9 + i * .1, t) * (1 - smooth(11, 12, t)) * (.7 + .3 * Math.sin(t * 3 + i)); });

  // Beat 3 (11–16 s): pins drop with a soft bounce, ripple on landing, and the path links them.
  let reached = 0;
  pins.forEach((pin, i) => {
   const p = clamp((t - PIN_AT[i]) / .9), fall = p < .5 ? 1 - (p / .5) ** 2 : .14 * Math.abs(Math.sin((p - .5) / .5 * Math.PI * 2)) * (1 - (p - .5) / .5);
   const shown = (t >= PIN_AT[i] ? 1 : 0) * out;
   pin.position.y = pin.userData.ground + fall * 2.6;
   pin.visible = shown > .001; pin.userData.mat.opacity = shown;
   pin.scale.setScalar(1 + .12 * Math.exp(-Math.pow((p - .5) * 14, 2)));
   const land0 = PIN_AT[i] + .45, q = clamp((t - land0) / 1.5);
   rings[i].z = .05 + .85 * Math.sqrt(q); rings[i].w = (t > land0 ? 1 - q : 0) * out;
   pools[i].x = smooth(land0, land0 + .4, t) * out;
   glow.positions.set([pin.position.x, pin.position.y + .78, pin.position.z], (Q0 + i) * 3);
   glow.alphas[Q0 + i] = shown * (.45 + .2 * Math.sin(t * 2.5 + i));
   if (i) reached = Math.max(reached, lerp((i - 1) / 3, i / 3, smooth(land0, land0 + .7, t)));
  });
  glow.commit();
  trail.uniforms.reveal.value = reached + .004;
  trail.uniforms.opacity.value = .85 * out * (t > PIN_AT[1] ? 1 : 0);
  trail.uniforms.flow.value = t * .8;

  orbit(camera, 4.5 * (1 - Math.cos(t / T * Math.PI * 2)), {
   radius: lerp(21.5, 19.5, window01(t, 10.6, 16, 1.5)), height: lerp(10.5, 9.5, window01(t, 5.2, 11, 1.5)), target: [0, -.6, 0], start: -.95, speed: .045,
  });
 }
 update(0);
 return { scene, camera, update, dispose() { headGeo.dispose(); stemGeo.dispose(); } };
}

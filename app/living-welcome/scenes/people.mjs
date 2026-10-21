import { THREE, HALF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, smooth, window01, lerp, clamp, rng, noise2, riverZ } from './kit.mjs';
import { SCENE_CATALOG } from './catalog.mjs';
// People & communities: county outlines trace on the land, aggregate counts
// rise as glass columns per county, then dusk falls and communities glow along
// the river and travel corridors. Aggregates only; never individual people.

const T = SCENE_CATALOG.people.duration;
const COLS = 5, ROWS = 4; // twenty county-like cells

/**
 * Draped polylines merged into one glowing ribbon mesh (one draw call).
 * Each line is a list of [x, z, order]; uniform `reveal` (0..1) traces up to that order.
 */
function traceLines(lines, sample, { width = .08, color = '#8fd6ee', lift = .035, opacity = 1, tip = .03 } = {}) {
 const pos = [], ord = [], side = [], index = [];
 for (const line of lines) {
  for (let i = 0; i < line.length; i++) {
   const [x, z, o] = line[i], a = line[Math.max(0, i - 1)], b = line[Math.min(line.length - 1, i + 1)];
   const l = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1, nx = -(b[1] - a[1]) / l * width / 2, nz = (b[0] - a[0]) / l * width / 2, v = pos.length / 3;
   for (const k of [1, -1]) { const px = x + nx * k, pz = z + nz * k; pos.push(px, sample(clamp(px, -HALF, HALF), clamp(pz, -HALF, HALF)) + lift, pz); ord.push(o); side.push(k); }
   if (i < line.length - 1) index.push(v, v + 1, v + 2, v + 1, v + 3, v + 2);
  }
 }
 const geometry = new THREE.BufferGeometry();
 geometry.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
 geometry.setAttribute('aT', new THREE.Float32BufferAttribute(ord, 1));
 geometry.setAttribute('aSide', new THREE.Float32BufferAttribute(side, 1));
 geometry.setIndex(index);
 const uniforms = { color: { value: new THREE.Color(color) }, opacity: { value: opacity }, reveal: { value: 1 }, tip: { value: tip } };
 const material = new THREE.ShaderMaterial({
  uniforms, transparent: true, depthWrite: false, side: THREE.DoubleSide, blending: THREE.AdditiveBlending,
  vertexShader: `attribute float aT; attribute float aSide; varying float vT; varying float vSide;
   void main() { vT = aT; vSide = aSide; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`,
  fragmentShader: `uniform vec3 color; uniform float opacity, reveal, tip; varying float vT; varying float vSide;
   void main() {
    float e = 1.0 - abs(vSide);
    float shown = 1.0 - smoothstep(reveal - 0.004, reveal, vT);
    float head = smoothstep(reveal - tip, reveal, vT) * shown;
    float a = (smoothstep(0.45, 0.85, e) + e * e * 0.35) * shown * opacity;
    gl_FragColor = vec4(color * (1.0 + head * 3.0), a);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
   }`,
 });
 const mesh = new THREE.Mesh(geometry, material);
 mesh.renderOrder = 3; mesh.frustumCulled = false; mesh.uniforms = uniforms;
 return mesh;
}

/** Glass column: fresnel body, brighter toward the top, a glowing rim and cap. */
function glassMaterial() {
 return new THREE.ShaderMaterial({
  uniforms: { glass: { value: new THREE.Color('#8fd6ee') }, cap: { value: new THREE.Color('#f3d38e') }, opacity: { value: 1 } },
  transparent: true, depthWrite: false, side: THREE.DoubleSide, blending: THREE.AdditiveBlending,
  vertexShader: `varying vec3 vN; varying vec3 vView; varying float vY; varying float vTop; varying float vFromTop;
   void main() {
    mat4 m = modelMatrix * instanceMatrix;
    vec4 wp = m * vec4(position, 1.0);
    vN = normalize(mat3(m) * normal); vView = cameraPosition - wp.xyz;
    vY = position.y; vTop = step(0.99, normal.y); vFromTop = (1.0 - position.y) * instanceMatrix[1][1];
    gl_Position = projectionMatrix * viewMatrix * wp;
   }`,
  fragmentShader: `uniform vec3 glass, cap; uniform float opacity; varying vec3 vN; varying vec3 vView; varying float vY; varying float vTop; varying float vFromTop;
   void main() {
    float f = pow(1.0 - abs(dot(normalize(vN), normalize(vView))), 2.2);
    float grad = mix(0.2, 1.0, vY);
    float rim = 1.0 - smoothstep(0.0, 0.07, vFromTop);
    vec3 c = glass * (0.3 + 1.1 * f) * grad + cap * (rim * 0.9 + vTop * 0.35);
    float a = (0.1 + 0.55 * f) * grad + rim * 0.6 + vTop * 0.3;
    gl_FragColor = vec4(c, a * opacity);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
   }`,
 });
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 const bg = new THREE.Color('#061a24'), dusk = new THREE.Color('#050f1a');
 const { key, hemi, rim } = stage(scene, { fog: .022 });
 const land = terrain({ segments: 256 });
 const u = liveSurface(land);
 const water = riverWater(land.sample);
 scene.add(land.mesh, blockSides(land.sample), water);
 u.tint.value.set('#0b1c2c');
 const r = rng(23), wob = noise2(31);

 // County lattice: jittered interior corners, gently wobbling shared edges, a straight outer line.
 const IN = HALF - .06;
 const V = [];
 for (let j = 0; j <= ROWS; j++) for (let i = 0; i <= COLS; i++) {
  const ex = i === 0 || i === COLS, ez = j === 0 || j === ROWS;
  V.push([lerp(-IN, IN, i / COLS) + (ex ? 0 : (r() - .5) * .9), lerp(-IN, IN, j / ROWS) + (ez ? 0 : (r() - .5) * .8)]);
 }
 const vid = (i, j) => j * (COLS + 1) + i, O = [-HALF, -1];
 const edges = [];
 for (let j = 0; j <= ROWS; j++) for (let i = 0; i < COLS; i++) edges.push([vid(i, j), vid(i + 1, j), j === 0 || j === ROWS]);
 for (let j = 0; j < ROWS; j++) for (let i = 0; i <= COLS; i++) edges.push([vid(i, j), vid(i, j + 1), i === 0 || i === COLS]);
 const dist = p => Math.hypot(p[0] - O[0], p[1] - O[1]);
 let maxD = 0;
 const raw = edges.map(([a, b, outer], e) => {
  let A = V[a], B = V[b];
  if (dist(B) < dist(A)) [A, B] = [B, A]; // trace outward from the west
  const len = Math.hypot(B[0] - A[0], B[1] - A[1]), n = Math.ceil(len / .07), nx = -(B[1] - A[1]) / len, nz = (B[0] - A[0]) / len;
  const pts = [];
  for (let k = 0; k <= n; k++) {
   const s = k / n, off = outer ? 0 : .12 * wob(e * 3.1, s * 2.4) * Math.sin(s * Math.PI);
   pts.push([lerp(A[0], B[0], s) + nx * off, lerp(A[1], B[1], s) + nz * off, dist(A) + s * len]);
  }
  maxD = Math.max(maxD, dist(A) + len);
  return pts;
 });
 for (const pts of raw) for (const p of pts) p[2] /= maxD;
 const counties = traceLines(raw, land.sample, { width: .09, color: '#8fd6ee', tip: .05 });
 scene.add(counties);

 // One aggregate per county: centroid, a seeded count (taller east and near the river), and when its outline closes.
 const cells = [];
 for (let j = 0; j < ROWS; j++) for (let i = 0; i < COLS; i++) {
  const c = [vid(i, j), vid(i + 1, j), vid(i, j + 1), vid(i + 1, j + 1)].map(k => V[k]);
  const x = c.reduce((s, p) => s + p[0], 0) / 4, z = c.reduce((s, p) => s + p[1], 0) / 4;
  const d = z - riverZ(x), h = clamp(.3 + 2.1 * Math.pow(r(), 2.3) + .35 * (x / HALF + 1) + .7 * Math.exp(-d * d / 1.5), .25, 3.1);
  cells.push({ x, z, y: land.sample(x, z), h, closed: Math.max(...c.map(dist)) / maxD, delay: r() * 1.3 });
 }
 const glass = new THREE.InstancedMesh(new THREE.CylinderGeometry(.26, .26, 1, 32, 1).translate(0, .5, 0), glassMaterial(), cells.length);
 glass.frustumCulled = false; glass.renderOrder = 4;
 scene.add(glass);
 const m4 = new THREE.Matrix4();

 // Dusk communities: warm clusters on the river banks and two travel corridors, plus each town's halo.
 const corridorA = x => -3.3 + .3 * Math.sin(x * .6 + 1), corridorB = z => 1.9 + .25 * Math.sin(z * .8);
 const towns = [
  ...[[-4.6, -1, .5], [-2.7, 1, .7], [-.8, -1, .45], [1.9, 1, 1], [3.4, -1, .6], [5.2, 1, .8]].map(([x, s, w]) => [x, riverZ(x) + s * .34, w]),
  ...[[-4.2, .35], [-1.4, .4], [1.9, .65], [4.4, .4]].map(([x, w]) => [x, corridorA(x), w]),
  [corridorB(3.6), 3.6, .45], [corridorB(-5.1), -5.1, .25],
 ];
 const lights = [];
 const keepDry = (x, z) => { const d = z - riverZ(x); return Math.abs(d) < .2 ? riverZ(x) + Math.sign(d || 1) * .2 : z; };
 const gauss = () => Math.sqrt(-2 * Math.log(1 - r())) * Math.cos(2 * Math.PI * r());
 for (const [tx, tz, w] of towns) {
  const n = Math.round(190 * w), sigma = .07 + .2 * w;
  for (let k = 0; k < n; k++) {
   const x = clamp(tx + gauss() * sigma, -5.85, 5.85), z = clamp(keepDry(x, tz + gauss() * sigma * .8), -5.85, 5.85);
   lights.push({ x, z, s: .09 + .15 * r() * r(), a: .6 + .4 * r(), warm: r() });
  }
 }
 for (let k = 0; k < 220; k++) { // a thin string of lights along each corridor
  const v = lerp(-5.8, 5.8, r()), onA = k % 2 === 0, x = onA ? v : corridorB(v) + gauss() * .05, z = onA ? corridorA(v) + gauss() * .05 : v;
  lights.push({ x, z: keepDry(x, z), s: .07 + .05 * r(), a: .35 + .4 * r(), warm: r() });
 }
 const L0 = cells.length, H0 = L0 + lights.length;
 const glow = glowPoints(H0 + towns.length, { size: .5, color: '#f3d38e' });
 const warmA = new THREE.Color('#ffd08a'), warmB = new THREE.Color('#ff9e57'), white = new THREE.Color('#fff1d6'), tmp = new THREE.Color();
 lights.forEach((p, k) => {
  const i = L0 + k;
  glow.positions.set([p.x, land.sample(p.x, p.z) + .04, p.z], i * 3);
  tmp.copy(warmA).lerp(p.warm > .85 ? white : warmB, p.warm > .85 ? .8 : p.warm * .7);
  glow.colors.set([tmp.r, tmp.g, tmp.b], i * 3); glow.sizes[i] = p.s;
  p.on = 11.1 + 1.6 * (p.x + HALF) / (2 * HALF) + .4 * r(); p.f = 1.5 + 3 * r(); p.ph = r() * 6.28;
 });
 towns.forEach(([x, z, w], k) => {
  const i = H0 + k;
  glow.positions.set([x, land.sample(x, z) + .1, z], i * 3); glow.sizes[i] = 1.1 + 2.2 * w;
  glow.colors.set([1, .62, .3], i * 3);
 });
 scene.add(glow);
 const corridors = traceLines([
  Array.from({ length: 121 }, (_, k) => { const x = lerp(-5.9, 5.9, k / 120); return [x, corridorA(x), k / 120]; }),
  Array.from({ length: 121 }, (_, k) => { const z = lerp(-5.9, 5.9, k / 120); return [corridorB(z), z, k / 120]; }),
 ], land.sample, { width: .06, color: '#ffb36b', opacity: .35 });
 scene.add(corridors);

 const sunDay = new THREE.Vector3(6, 9, 4), sunDusk = new THREE.Vector3(-11, 2.4, 3);
 const dayKey = new THREE.Color('#ffe2b8'), duskKey = new THREE.Color('#ff9a5c');

 function update(t) {
  const out = 1 - smooth(14.9, 15.9, t);

  // Beat 1 (0–5.5 s): outlines trace outward from the west; each closed county seeds a count.
  counties.uniforms.reveal.value = lerp(0, 1.02, smooth(.2, 4.6, t));
  counties.uniforms.opacity.value = smooth(0, .3, t) * lerp(1, .5, smooth(5.5, 7, t)) * lerp(1, .55, smooth(11, 12.5, t)) * out;

  // Beat 2 (5.5–11 s): glass columns rise from each county's centre, overshooting a touch.
  // Beat 3 (11–16 s): columns settle away as dusk falls and the communities light up.
  const sink = smooth(10.9, 12.4, t);
  cells.forEach((c, i) => {
   const p = clamp((t - 5.6 - c.delay) / 1.7), rise = p === 0 ? 0 : 1 + 2.4 * Math.pow(p - 1, 3) + 1.4 * Math.pow(p - 1, 2);
   const h = Math.max(.001, (c.h * rise + .15) * (1 - sink) * (p > 0 ? 1 : 0));
   m4.makeScale(1, h, 1).setPosition(c.x, c.y - .15, c.z);
   glass.setMatrixAt(i, m4);
   const seed = smooth(c.closed * 4.4 + .4, c.closed * 4.4 + .9, t);
   glow.positions.set([c.x, Math.max(c.y + .06, c.y - .15 + h + .02), c.z], i * 3);
   glow.alphas[i] = seed * (1 - sink) * (.5 + .2 * Math.sin(t * 2 + i));
   glow.sizes[i] = lerp(.35, .7, smooth(5.6, 7, t));
  });
  glass.instanceMatrix.needsUpdate = true;
  glass.material.uniforms.opacity.value = smooth(5.5, 6.2, t) * (1 - sink);
  glass.visible = glass.material.uniforms.opacity.value > .002;

  const night = smooth(10.8, 12.6, t) * out;
  lights.forEach((p, k) => { glow.alphas[L0 + k] = p.a * smooth(p.on, p.on + .6, t) * out * (.78 + .22 * Math.sin(t * p.f + p.ph)); });
  towns.forEach(([x], k) => { glow.alphas[H0 + k] = .38 * smooth(11.3 + 1.6 * (x + HALF) / (2 * HALF), 12.6 + 1.6 * (x + HALF) / (2 * HALF), t) * out; });
  glow.commit();
  corridors.uniforms.reveal.value = lerp(0, 1.02, smooth(11, 12.8, t));
  corridors.uniforms.opacity.value = .5 * night;

  // Dusk: low warm sun from the west, dimmer sky fill, a deeper background.
  key.position.copy(sunDay).lerp(sunDusk, night);
  key.color.copy(dayKey).lerp(duskKey, night);
  key.intensity = lerp(2.4, 1.6, night);
  hemi.intensity = lerp(.9, .42, night); rim.intensity = lerp(.55, .3, night);
  scene.background.copy(bg).lerp(dusk, night); scene.fog.color.copy(scene.background);
  u.tintMix.value = .22 * night;

  orbit(camera, 4.5 * (1 - Math.cos(t / T * Math.PI * 2)), {
   radius: 21.5, height: lerp(10.5, 8.8, window01(t, 5.2, 11.5, 1.6)), target: [0, -.4, 0], start: -.95, speed: .045,
  });
 }
 update(0);
 return { scene, camera, update, dispose() {} };
}

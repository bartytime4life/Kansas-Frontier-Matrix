import { THREE, HALF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, surfacePath, riverZ, smooth, window01, lerp, clamp, rng } from './kit.mjs';
// Transport: highway and rail corridors draw across a night-toned block,
// long-exposure traffic trails stream along them, then abandoned branch
// lines fade to dashed historic traces while the active network carries on.

const HIGHWAYS = [
 s => { const x = lerp(-HALF, HALF, s); return [x, -2.7 + .35 * Math.sin(x * .38 + 1)]; },
 s => { const x = lerp(HALF, -HALF, s); return [x, 3.5 + .3 * Math.sin(x * .5 - .4)]; },
 s => [lerp(5.9, -2.2, s) + .3 * Math.sin(s * 5), lerp(-HALF, HALF, s)],
 s => { const z = lerp(HALF, -HALF, s); return [-3.6 + .12 * Math.sin(z * .8), z]; },
];
const RAILS = [
 s => { const x = lerp(-HALF, HALF, s); return [x, riverZ(x) - .7]; }, // the valley line follows the river's north bank
 s => [lerp(-HALF, HALF, s), lerp(-4.8, 5.2, s) + .4 * Math.sin(s * 4)],
 s => { const z = lerp(-HALF, HALF, s); return [2.4 + .2 * Math.sin(z * .6), z]; },
];
const ABANDONED = [
 s => [lerp(-1.4, -HALF, s), lerp(riverZ(-1.4) - .7, 5.4, s) + .45 * Math.sin(s * Math.PI)],
 s => [lerp(2.4 + .2 * Math.sin(-.3), HALF, s), lerp(-.5, -4.4, s) - .3 * Math.sin(s * Math.PI)],
];
const CARS = 30, TRAIL = 9, TRAIN = 18;

/** Equal-arc-length path over the surface, with horizontal side vectors for lane offsets. */
function arcPath(fn, sample, { step = .04, lift = .035 } = {}) {
 const raw = surfacePath(fn, sample, 300, lift), cum = [0];
 for (let i = 1; i < raw.length; i++) cum.push(cum[i - 1] + raw[i].distanceTo(raw[i - 1]));
 const len = cum[cum.length - 1], n = Math.max(2, Math.ceil(len / step) + 1), pts = [];
 for (let i = 0, j = 0; i < n; i++) {
  const d = len * i / (n - 1);
  while (j < raw.length - 2 && cum[j + 1] < d) j++;
  pts.push(raw[j].clone().lerp(raw[j + 1], clamp((d - cum[j]) / (cum[j + 1] - cum[j] || 1))));
 }
 const sides = pts.map((_, i) => { const a = pts[Math.max(0, i - 1)], b = pts[Math.min(n - 1, i + 1)]; return new THREE.Vector3(-(b.z - a.z), 0, b.x - a.x).normalize(); });
 const ds = len / (n - 1);
 // Point at distance d, offset sideways by `off`, written into a flat array.
 const write = (d, off, out, k) => {
  const f = clamp(d, 0, len) / ds, i = Math.min(n - 2, Math.floor(f)), w = f - i, a = pts[i], b = pts[i + 1], s = sides[i];
  out[k] = a.x + (b.x - a.x) * w + s.x * off; out[k + 1] = a.y + (b.y - a.y) * w + .02; out[k + 2] = a.z + (b.z - a.z) * w + s.z * off;
 };
 return { pts, sides, len, ds, write };
}

/** A flat strip along a path carrying distance-along and across coordinates. */
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

const VERT = `attribute float aAlong; attribute float aAcross; varying float vAlong; varying float vAcross;
 void main() { vAlong = aAlong; vAcross = aAcross; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`;
// kind 0 highway (gold edges, warm core), 1 rail (steel line with cross-ties), 2 soft highway glow.
const FRAG = `uniform float uReveal; uniform float uOp; uniform float uKind; uniform float uFront; uniform float uHist;
 uniform vec3 uA; uniform vec3 uB; uniform vec3 uHistCol; varying float vAlong; varying float vAcross;
 void main() {
  if (vAlong > uReveal) discard;
  float a = abs(vAcross), head = exp(-pow((uReveal - vAlong) / .25, 2.0)), alpha; vec3 col;
  if (uKind < .5) {
   float edge = smoothstep(.5, .75, a);
   col = mix(uB, uA, edge); alpha = (.65 + .35 * edge) * (1.0 - smoothstep(.88, 1.0, a));
  } else if (uKind < 1.5) {
   float rail = 1.0 - smoothstep(.14, .3, a), tie = step(fract(vAlong * 7.0), .3) * (1.0 - smoothstep(.8, 1.0, a));
   col = mix(uB, uA, rail); alpha = max(rail, tie * .85);
   // Behind the fade front the line becomes a sparse dashed trace in archival sepia.
   float h = clamp((uFront - vAlong) / 1.2, 0.0, 1.0) * uHist, ember = exp(-pow((uFront - vAlong) / .35, 2.0)) * uHist;
   float dash = step(fract(vAlong * 2.4), .5) * (1.0 - smoothstep(.25, .5, a));
   col = mix(col, uHistCol, h) + uHistCol * ember * 1.5; alpha = mix(alpha, dash * .7, h) + ember * .4 * (1.0 - a);
  } else {
   col = uA; alpha = pow(1.0 - a, 2.0) * .3;
  }
  gl_FragColor = vec4(col * (1.0 + head * 2.0), clamp(alpha + head * .6 * (1.0 - a), 0.0, 1.0) * uOp);
  #include <tonemapping_fragment>
  #include <colorspace_fragment>
 }`;

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022, sunIntensity: 1.7 });
 const land = terrain({ segments: 220 });
 const u = liveSurface(land);
 u.tint.value.set('#0a1f2a');
 const sides = blockSides(land.sample), water = riverWater(land.sample);
 sides.traverse(o => { if (o.material) o.material.color = new THREE.Color('#a4adb2'); }); // cool the walls to match the night map
 scene.add(land.mesh, sides, water);

 const gold = new THREE.Color('#f3d38e'), warm = new THREE.Color('#fff4dc'), steel = new THREE.Color('#bcd3dc'), tie = new THREE.Color('#a08a6c'), sepia = new THREE.Color('#c79a62');
 const lines = [];
 function addLine(fn, kind, width, start, extra = {}) {
  const path = arcPath(fn, land.sample), uniforms = {
   uReveal: { value: 0 }, uOp: { value: 1 }, uKind: { value: kind }, uFront: { value: -2 }, uHist: { value: 0 },
   uA: { value: kind === 1 ? steel : gold }, uB: { value: kind === 1 ? tie : warm }, uHistCol: { value: sepia },
  };
  const mesh = new THREE.Mesh(strip(path, width), new THREE.ShaderMaterial({ uniforms, vertexShader: VERT, fragmentShader: FRAG, transparent: true, depthWrite: false, side: THREE.DoubleSide, blending: kind === 2 ? THREE.AdditiveBlending : THREE.NormalBlending }));
  mesh.renderOrder = kind === 2 ? 2 : 3;
  scene.add(mesh);
  const line = { path, uniforms, start, ...extra };
  lines.push(line);
  return line;
 }
 const highways = HIGHWAYS.map((fn, i) => { addLine(fn, 2, .5, .2 + i * .3); return addLine(fn, 0, .085, .2 + i * .3); });
 const rails = RAILS.map((fn, i) => addLine(fn, 1, .12, 1 + i * .35));
 const abandoned = ABANDONED.map((fn, i) => addLine(fn, 1, .12, 1.6 + i * .4, { abandoned: true }));
 const drawn = lines.filter(l => l.uniforms.uKind.value !== 2);

 // Towns sit on the corridors and glow as the network reaches them.
 const TOWNS = [[0, .2], [0, .55], [0, .86], [1, .3], [1, .72], [2, .48], [3, .4], [4, .38], [5, .7]];
 const towns = glowPoints(TOWNS.length * 2, { size: .5, color: '#ffd89a' });
 TOWNS.forEach(([l, s], i) => {
  const line = drawn[l], p = line.path;
  p.write(s * p.len, 0, towns.positions, i * 6); p.write(s * p.len, 0, towns.positions, i * 6 + 3);
  towns.sizes[i * 2] = .35; towns.sizes[i * 2 + 1] = 1.3;
 });
 scene.add(towns);

 // Traffic: long-exposure streaks, headlights one way and taillights the other.
 const random = rng(41), cars = [];
 highways.forEach((line, h) => { for (const dir of [1, -1]) for (let c = 0; c < CARS; c++) cars.push({ line, dir, d0: random() * line.path.len, v: .75 + random() * .45, h }); });
 const traffic = glowPoints(cars.length * TRAIL + rails.length * TRAIN, { size: .14 });
 const head = new THREE.Color('#fff1d0'), tail = new THREE.Color('#ff4a2e'), amber = new THREE.Color('#ffc46b');
 cars.forEach((car, c) => { const col = car.dir > 0 ? head : tail; for (let k = 0; k < TRAIL; k++) { const i = c * TRAIL + k; traffic.colors.set([col.r, col.g, col.b], i * 3); traffic.sizes[i] = k ? .2 : .28; } });
 for (let i = cars.length * TRAIL; i < traffic.alphas.length; i++) traffic.colors.set([amber.r, amber.g, amber.b], i * 3);
 scene.add(traffic);

 function update(t) {
  const out = 1 - smooth(15.2, 15.95, t);
  // Beat 1 (0–5.5 s): highways, then rail, draw corridor by corridor with a bright leading head.
  // Highways step down while traffic runs so the light trails, not the pavement, carry the corridors.
  const calm = lerp(1, .5, window01(t, 5.2, 16.5, 1));
  for (const l of lines) { l.uniforms.uReveal.value = l.path.len * smooth(l.start, l.start + 2.4, t) + (t > l.start + 2.4 ? 1 : 0); l.uniforms.uOp.value = out * (l.uniforms.uKind.value === 1 ? 1 : calm); }
  TOWNS.forEach(([l, s], i) => {
   const line = drawn[l], k = smooth(s * line.path.len - .2, s * line.path.len + .4, line.uniforms.uReveal.value) * out;
   towns.alphas[i * 2] = k; towns.alphas[i * 2 + 1] = k * (.22 + .05 * Math.sin(t * 1.7 + i));
  });
  // Beat 3 (11–16 s): abandoned branches lose their ties and fade to a dashed sepia trace, end to end.
  for (const l of abandoned) {
   l.uniforms.uHist.value = smooth(10.9, 11.3, t);
   l.uniforms.uFront.value = lerp(-1, l.path.len + 1.4, smooth(11.2, 13.8, t));
   l.uniforms.uOp.value = out * lerp(1, .8, smooth(12.5, 14, t));
  }
  towns.commit();

  // Beat 2 (5.5–11 s, continuing): traffic streams both ways; trains run the active rail only.
  const flow = window01(t, 5.4, 15.8, .9);
  cars.forEach((car, c) => {
   const len = car.line.path.len, base = ((car.d0 + car.v * t) % len + len) % len;
   for (let k = 0; k < TRAIL; k++) {
    const i = c * TRAIL + k, d = car.dir > 0 ? base - k * .065 : len - base + k * .065;
    car.line.path.write(d, car.dir * .022, traffic.positions, i * 3);
    traffic.alphas[i] = flow * Math.pow(1 - k / TRAIL, 1.6) * (d > .05 && d < len - .05 ? 1 : 0);
   }
  });
  rails.forEach((line, r) => {
   const len = line.path.len, front = ((r * 3.1 + t * .7) % (len + 2)) - 1;
   for (let k = 0; k < TRAIN; k++) {
    const i = cars.length * TRAIL + r * TRAIN + k, d = front - k * .05;
    line.path.write(d, 0, traffic.positions, i * 3);
    traffic.alphas[i] = flow * (d > 0 && d < len ? (k ? .7 : 1) : 0);
    traffic.sizes[i] = k ? .2 : .32;
   }
  });
  traffic.commit();

  // Keep the land dim so the lit network reads as the subject.
  u.tintMix.value = .5; u.grey.value = .2;
  orbit(camera, t, { radius: 22, height: 11 - 1.4 * window01(t, 4, 16, 4), target: [0, -.5, 0], start: -.6 - .3 * Math.cos(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update, dispose() {} };
}

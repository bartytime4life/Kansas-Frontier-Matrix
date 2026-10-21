import { THREE, HALF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, gridSampler, riverZ, smooth, window01, lerp, clamp, rng } from './kit.mjs';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
// Transport through time: an era clock runs 1860 → 2025 in five-year steps.
// Trails give way to rail, section-line roads, paved highways and the interstate;
// each era's wagons, trains, cars, trucks and aircraft travel only the network
// that exists in that era, and towns light up as a line first reaches them.

const D = 36, TAU = Math.PI * 2;
// Vehicles are modelled near true proportion, then enlarged so each era's types read at hero distance.
const GS = 1.45, TS = 1.3, AS = 1.25, CS = 1.6;
// Catalog-aligned keyframes (beat start → year), a hold on today, then a rewind to 1860.
const KEYS = [[0, 1860], [5, 1880], [10.5, 1910], [15.5, 1930], [21.5, 1955], [27.5, 1990], [32.4, 2025]];
function eraYear(t) {
 if (t >= 32.4) return lerp(2025, 1860, smooth(34.2, 35.5, t));
 for (let i = 1; i < KEYS.length; i++) if (t <= KEYS[i][0]) { const [t0, y0] = KEYS[i - 1], [t1, y1] = KEYS[i]; return lerp(y0, y1, (t - t0) / (t1 - t0)); }
 return 2025;
}

// ---------------------------------------------------------------- network
// kind: 0 wagon trail, 1 cattle trail, 2 rail, 3 section-line dirt road, 4 paved highway, 5 interstate, 6 ramp
const R1z = x => riverZ(x) - .8, R2z = x => 2.6 + .35 * Math.sin(x * .55 + .3);
const EW = z => s => [lerp(HALF, -HALF, s), z], NS = x => s => [x, lerp(-HALF, HALF, s)];
const SECTION = [-4.5, -1.5, 1.5, 4.5], HUB = [3.4, -2.6];
const NET = [
 { id: 'trail', kind: 0, w: .12, y: [1850, 1850], fn: s => [lerp(HALF, -HALF, s), lerp(-1.6, 4, s) + .45 * Math.sin(s * 7)] },
 { id: 'cattle', kind: 1, w: .3, y: [1866, 1869], fn: s => [lerp(.3, 1, s) + .3 * Math.sin(s * 9) * (1 - s), lerp(HALF, R1z(1), s)] },
 ...SECTION.flatMap((v, i) => [
  { id: `ns${i}`, kind: 3, w: .06, y: [1897 + i * 2.6, 1902 + i * 2.6], fn: NS(v) },
  { id: `ew${i}`, kind: 3, w: .06, y: [1898.3 + i * 2.6, 1903.3 + i * 2.6], fn: EW(v) },
 ]),
 { id: 'H1', kind: 4, w: .17, y: [1926, 1934], fn: EW(-4.5) },
 { id: 'H2', kind: 4, w: .17, y: [1929, 1938], fn: NS(-1.5) },
 { id: 'H3', kind: 4, w: .17, y: [1933, 1942], fn: EW(4.5) },
 { id: 'H4', kind: 4, w: .17, y: [1935, 1941], fn: EW(-1.5) }, // paved over a section road beside the main line
 { id: 'R1', kind: 2, w: .11, y: [1863, 1872], fn: s => { const x = lerp(HALF, -HALF, s); return [x, R1z(x)]; } },
 { id: 'R1b', kind: 2, w: .11, y: [1968, 1973], fn: s => { const x = lerp(-HALF, HALF, s); return [x, R1z(x) - .15]; } },
 { id: 'R2', kind: 2, w: .11, y: [1869, 1880], fn: s => { const x = lerp(HALF, -HALF, s); return [x, R2z(x)]; } },
 { id: 'B1', kind: 2, w: .11, y: [1886, 1890], gone: 1958, fn: s => [lerp(-2.6, -3.1, s) + .25 * Math.sin(s * 3), lerp(R1z(-2.6), -5.4, s)] },
 { id: 'B2', kind: 2, w: .11, y: [1881, 1885], fn: s => [lerp(4.3, 5.2, s) + .2 * Math.sin(s * Math.PI), lerp(R1z(4.3), -5.3, s)] },
 { id: 'B3', kind: 2, w: .11, y: [1887, 1891], gone: 1978, fn: s => [lerp(-4.3, -4.8, s) + .15 * Math.sin(s * Math.PI), lerp(R1z(-4.3), R2z(-4.8), s)] },
 { id: 'B4', kind: 2, w: .11, y: [1890, 1894], fn: s => [lerp(4.2, 4.9, s), lerp(R2z(4.2), 5.5, s)] },
 { id: 'B5', kind: 2, w: .11, y: [1897, 1902], gone: 1985, fn: s => [lerp(1, .4, s) - .25 * Math.sin(s * Math.PI), lerp(R1z(1), -5.4, s)] },
 { id: 'I1', kind: 5, w: .44, y: [1957, 1967], fn: EW(HUB[1]) },
 { id: 'I2', kind: 5, w: .44, y: [1960, 1970], fn: NS(HUB[0]) },
 // Cloverleaf: four 300° loops in the quadrants of the interstate crossing.
 ...[[1, 1], [-1, 1], [-1, -1], [1, -1]].map(([sx, sz], i) => {
  const cx = HUB[0] + sx * .46, cz = HUB[1] + sz * .46, a0 = Math.atan2(-sz, -sx) + .59;
  return { id: `ramp${i}`, kind: 6, w: .07, y: [1962 + i * .4, 1963.4 + i * .4], fn: s => [cx + .3 * Math.cos(a0 + s * 5.1), cz + .3 * Math.sin(a0 + s * 5.1)] };
 }),
];
// Draw order inside the merged network: older, humbler surfaces underneath.
const ORDER = [0, 1, 3, 4, 2, 6, 5];

// Towns [x, z, size]; access years are measured from the network, not listed.
const TOWNS = [
 [4.3, R1z(4.3), 1], [1, R1z(1), 2], [-2.6, R1z(-2.6), 1], [-5, R1z(-5), 0], [2.6, R2z(2.6), 0], [-1.5, R2z(-1.5), 1],
 [-3.07, -5.4, 0], [5.2, -5.3, 0], [-4.43, .42, 0], [4.9, 5.5, 0], [.4, -5.4, 0], [-1.5, 4.5, 0], [-3.3, -2.6, 0], [3.4, 5.3, 0], [-1.44, 1.45, 0],
];

/** Even-spaced path over the ground; y bridges small dips so roads span creeks. */
function track(fn, hs, { step = .045, lift = .03 } = {}) {
 const raw = [], cum = [0];
 for (let i = 0; i <= 400; i++) raw.push(fn(i / 400));
 for (let i = 1; i <= 400; i++) cum.push(cum[i - 1] + Math.hypot(raw[i][0] - raw[i - 1][0], raw[i][1] - raw[i - 1][1]));
 const len = cum[400], n = Math.max(2, Math.ceil(len / step) + 1), ds = len / (n - 1), xs = new Float32Array(n), zs = new Float32Array(n), ys = new Float32Array(n);
 for (let i = 0, j = 0; i < n; i++) {
  const d = i * ds;
  while (j < 399 && cum[j + 1] < d) j++;
  const w = clamp((d - cum[j]) / (cum[j + 1] - cum[j] || 1));
  xs[i] = lerp(raw[j][0], raw[j + 1][0], w); zs[i] = lerp(raw[j][1], raw[j + 1][1], w);
 }
 const ground = Array.from(xs, (x, i) => hs(x, zs[i])), k = Math.round(.55 / ds);
 for (let i = 0; i < n; i++) {
  let sum = 0, c = 0;
  for (let j = Math.max(0, i - k); j <= Math.min(n - 1, i + k); j++) { sum += ground[j]; c++; }
  ys[i] = Math.max(ground[i], sum / c - .02) + lift;
 }
 const sx = new Float32Array(n), sz = new Float32Array(n);
 for (let i = 0; i < n; i++) {
  const a = Math.max(0, i - 1), b = Math.min(n - 1, i + 1), dx = xs[b] - xs[a], dz = zs[b] - zs[a], l = Math.hypot(dx, dz) || 1;
  sx[i] = -dz / l; sz[i] = dx / l; // horizontal right-hand side of travel
 }
 // Point at distance d (clamped), offset `off` to the side.
 const at = (d, off, out) => {
  const f = clamp(d, 0, len) / ds, i = Math.min(n - 2, Math.floor(f)), w = f - i;
  return out.set(lerp(xs[i], xs[i + 1], w) + lerp(sx[i], sx[i + 1], w) * off, lerp(ys[i], ys[i + 1], w), lerp(zs[i], zs[i + 1], w) + lerp(sz[i], sz[i + 1], w) * off);
 };
 return { xs, ys, zs, sx, sz, n, ds, len, at };
}

const NET_VERT = `attribute float aAlong; attribute float aAcross; attribute float aBuilt; attribute float aGone; attribute float aKind;
 varying float vAlong; varying float vAcross; varying float vBuilt; varying float vGone; varying float vKind;
 void main() { vAlong = aAlong; vAcross = aAcross; vBuilt = aBuilt; vGone = aGone; vKind = aKind;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`;
const NET_FRAG = `uniform float uYear; uniform float uTime; uniform float uPulse;
 varying float vAlong; varying float vAcross; varying float vBuilt; varying float vGone; varying float vKind;
 float band(float d, float w) { float f = fwidth(vAcross) * 1.2; return 1.0 - smoothstep(max(w, f * .5), max(w, f * .5) + f, d); }
 float hash(float n) { return fract(sin(n) * 43758.5453); }
 void main() {
  float age = uYear - vBuilt;
  if (age < 0.0) discard;
  float a = abs(vAcross), soft = 1.0 - smoothstep(.8, 1.0, a), alpha = 0.0; vec3 col = vec3(0.0), glow = vec3(0.0);
  vec3 gold = vec3(.95, .74, .38);
  if (vKind < .5) { // wagon trail: twin ruts, worn to a faint trace once roads arrive
   float worn = mix(.85, .16, smoothstep(1878.0, 1902.0, uYear));
   col = vec3(.78, .64, .44); alpha = (band(abs(a - .5), .16) * .9 + .2 * soft) * worn;
  } else if (vKind < 1.5) { // cattle trail: a broad trampled band, gone once the drives end
   float mott = .55 + .45 * hash(floor(vAlong * 9.0) + floor(a * 3.0) * 7.0);
   col = vec3(.55, .42, .3); alpha = soft * (1.0 - a * .6) * .5 * mott * (1.0 - smoothstep(1884.0, 1891.0, uYear));
  } else if (vKind < 2.5) { // rail: steel rails on timber ties over ballast
   float rails = band(abs(a - .42), .08), ties = step(fract(vAlong * 16.0), .4) * band(a, .78);
   col = mix(vec3(.2, .19, .18), vec3(.42, .32, .24), ties); col = mix(col, vec3(.62, .66, .7), rails * .8);
   alpha = max(rails * .9, max(ties * .8, soft * .5));
   // Abandoned branches lose their ties and fade to a dashed sepia trace.
   float h = smoothstep(vGone, vGone + 3.0, uYear), ember = exp(-pow((uYear - vGone - 1.0) / 1.2, 2.0)) * step(vGone, 9000.0);
   float dash = step(fract(vAlong * 2.2), .55) * band(a, .35);
   col = mix(col, vec3(.72, .55, .36), h); glow += vec3(.9, .5, .25) * ember; alpha = mix(alpha, dash * .45, h);
  } else if (vKind < 3.5) { // section-line dirt road
   col = vec3(.78, .67, .5); alpha = band(a, .55) * .48;
  } else if (vKind < 4.5) { // paved two-lane highway with edge and centre lines
   float edge = band(abs(a - .78), .07), centre = band(a, .07) * step(fract(vAlong * 4.0), .5);
   col = vec3(.27, .29, .32); col = mix(col, vec3(.86, .84, .78), edge * .5); col = mix(col, vec3(.98, .78, .3), centre * .8);
   alpha = soft * .95;
  } else if (vKind < 5.5) { // interstate: twin carriageways, widened in the 1990s
   float wide = smoothstep(0.0, 1.0, (uYear - 1994.0 - vAlong * .6) / 2.0), outer = mix(.64, .97, wide);
   float lane = step(.2, a) * (1.0 - smoothstep(outer - .03, outer, a));
   float lines = band(abs(a - (outer - .05)), .025) + band(abs(a - .24), .02) + band(abs(a - mix(.42, .5, wide)), .016) * step(fract(vAlong * 3.0), .45) + band(abs(a - .74), .016) * step(fract(vAlong * 3.0), .45) * wide;
   float lamps = band(a, .07) * smoothstep(1966.0, 1974.0, uYear) * pow(.5 + .5 * cos(vAlong * 12.566), 8.0);
   col = mix(vec3(.36, .38, .41), vec3(.9, .88, .82), clamp(lines, 0.0, 1.0) * lane * .6);
   col = mix(vec3(.15, .2, .16), col, lane); glow += gold * lamps * 2.4;
   alpha = max(max(lane * .97, step(a, .2) * .35), lamps);
  } else { // ramp
   col = vec3(.36, .38, .41); alpha = soft * .95;
  }
  // A bright construction front leads every new line; a closing pulse runs the whole network.
  float head = exp(-age * age / 1.4) * (vKind > .5 ? 1.0 : 0.0);
  float pulse = uPulse * pow(.5 + .5 * sin(vAlong * 1.7 - uTime * 5.0), 14.0) * (vKind > 1.5 && uYear < vGone ? 1.0 : 0.0);
  col = pow(col, vec3(2.2)) + glow + gold * (head * 1.8 + pulse * 1.6); // palette above is sRGB
  alpha = max(alpha, (head * .85 + pulse * .8) * soft);
  gl_FragColor = vec4(col, clamp(alpha, 0.0, 1.0));
  #include <tonemapping_fragment>
  #include <colorspace_fragment>
 }`;

// ---------------------------------------------------------------- vehicles
const _m = new THREE.Matrix4(), _e = new THREE.Euler(), _c = new THREE.Color();
const box = (w, h, d) => new THREE.BoxGeometry(w, h, d), cyl = (rt, rb, h, seg = 10, t0 = 0, tl = Math.PI * 2) => new THREE.CylinderGeometry(rt, rb, h, seg, 1, false, t0, tl), ball = r => new THREE.SphereGeometry(r, 10, 7);
/** One coloured piece of a vehicle (+x forward, +y up, +z right); `emit` = [colour, strength]. */
function part(geo, color, { x = 0, y = 0, z = 0, rx = 0, ry = 0, rz = 0, sx = 1, sy = 1, sz = 1, emit = null, shear = null } = {}) {
 geo.deleteAttribute('uv');
 if (shear) geo.applyMatrix4(_m.makeShear(...shear));
 geo.scale(sx, sy, sz);
 if (rx || ry || rz) geo.applyMatrix4(_m.makeRotationFromEuler(_e.set(rx, ry, rz)));
 geo.translate(x, y, z);
 const n = geo.attributes.position.count, col = new Float32Array(n * 3), em = new Float32Array(n * 3);
 _c.set(color); for (let i = 0; i < n; i++) col.set([_c.r, _c.g, _c.b], i * 3);
 if (emit) { _c.set(emit[0]).multiplyScalar(emit[1]); for (let i = 0; i < n; i++) em.set([_c.r, _c.g, _c.b], i * 3); }
 geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
 geo.setAttribute('aEmit', new THREE.BufferAttribute(em, 3));
 return geo;
}
const wheel = (x, z, r, color = '#151515', t = .022) => part(cyl(r, r, t, 10), color, { x, y: r, z, rx: Math.PI / 2 });
const wheels = (xs, z, r, color) => xs.flatMap(x => [wheel(x, z, r, color), wheel(x, -z, r, color)]);
const HEAD = ['#ffe2b0', 3.2], LED = ['#eef4ff', 3.4], TAIL = ['#ff3a24', 2.2], WARM = ['#ffcf8a', 1.5];
const lamp = (x, y, z, e, s = .016) => part(box(s * .5, s, s), '#222', { x, y, z, emit: e });
const lamps = (x, y, z, e, s) => [lamp(x, y, z, e, s), lamp(x, y, -z, e, s)];
const truck = (x, w = .085) => [part(box(.07, .028, w), '#141414', { x, y: .03 }), ...wheels([x - .022, x + .022], w / 2 - .004, .022)];

// Every model is built once; instance colour tints the parts painted light.
const MODELS = {
 wagon: () => [part(box(.24, .05, .11), '#6a4a2c', { y: .075 }), part(cyl(.062, .062, .22, 8, 0, Math.PI), '#e9e0c6', { y: .1, rz: Math.PI / 2 }),
  ...wheels([-.08, .08], .06, .04, '#2e2216'), part(box(.07, .045, .035), '#4a3626', { x: .2, y: .045, z: .03 }), part(box(.07, .045, .035), '#4a3626', { x: .2, y: .045, z: -.03 }), lamp(.125, .12, 0, ['#ffb35a', 3])],
 stage: () => [part(box(.15, .09, .1), '#6b2a20', { y: .12 }), part(box(.14, .016, .09), '#2a1a14', { y: .172 }), part(box(.06, .034, .104), '#000', { y: .13, emit: ['#ffbe6a', 1.2] }),
  part(box(.04, .03, .09), '#3a2418', { x: .09, y: .15 }), ...wheels([-.055, .06], .055, .045, '#c9a040'),
  ...[.2, .29].flatMap(x => [part(box(.065, .045, .03), '#3b2a1e', { x, y: .045, z: .028 }), part(box(.065, .045, .03), '#3b2a1e', { x, y: .045, z: -.028 })]), lamp(.12, .16, .05, ['#ffb35a', 3])],
 modelT: () => [part(box(.24, .02, .09), '#141416', { y: .05 }), part(box(.07, .045, .07), '#fff', { x: .075, y: .08 }), part(box(.09, .075, .085), '#fff', { x: -.02, y: .1 }),
  part(box(.12, .008, .095), '#151515', { x: -.02, y: .142 }), part(box(.008, .035, .07), '#b08a3a', { x: .113, y: .085 }), ...wheels([-.075, .075], .05, .032, '#d8cdb2', .012), ...lamps(.118, .1, .03, HEAD),
  part(cyl(.03, .03, .012, 10), '#151515', { x: -.125, y: .085, rz: Math.PI / 2 }), part(box(.006, .05, .08), '#3a3a3a', { x: .025, y: .13 })],
 sedan: () => [part(box(.3, .055, .11), '#fff', { y: .06 }), part(box(.14, .05, .1), '#fff', { x: -.02, y: .11 }), part(box(.12, .034, .104), '#1c2430', { x: -.02, y: .113 }),
  ...wheels([-.09, .09], .052, .03), ...lamps(.151, .07, .035, HEAD), ...lamps(-.151, .07, .04, TAIL, .012),
  part(box(.006, .032, .04), '#c8c8c0', { x: .152, y: .06 }), part(box(.012, .012, .116), '#c8c8c0', { x: .152, y: .038 }), part(box(.012, .012, .116), '#c8c8c0', { x: -.152, y: .038 }), ...[-.09, .09].map(x => part(box(.08, .03, .122), '#fff', { x, y: .055 }))],
 pickup: () => [part(box(.1, .07, .11), '#fff', { x: .03, y: .09 }), part(box(.08, .045, .105), '#fff', { x: .115, y: .07 }), part(box(.13, .04, .11), '#ddd', { x: -.085, y: .06 }),
  part(box(.06, .03, .114), '#1c2430', { x: .035, y: .1 }), ...wheels([-.09, .1], .052, .03), ...lamps(.156, .075, .035, HEAD), ...lamps(-.151, .07, .04, TAIL, .012)],
 boxtruck: () => [part(box(.09, .08, .11), '#fff', { x: .14, y: .095 }), part(box(.26, .13, .12), '#e8e4da', { x: -.045, y: .12 }), part(box(.03, .03, .114), '#1c2430', { x: .17, y: .115 }),
  ...wheels([-.12, -.06, .14], .055, .032), ...lamps(.186, .075, .04, HEAD), ...lamps(-.176, .07, .05, TAIL, .012)],
 semi: () => [part(box(.12, .12, .12), '#fff', { x: .24, y: .11 }), part(box(.07, .07, .11), '#fff', { x: .33, y: .08 }), part(box(.04, .05, .124), '#1c2430', { x: .27, y: .14 }),
  part(cyl(.008, .008, .12, 6), '#9aa0a8', { x: .19, y: .19, z: .05 }), part(box(.46, .14, .12), '#eceae4', { x: -.09, y: .15 }), part(box(.5, .02, .07), '#1a1a1a', { x: 0, y: .05 }),
  ...wheels([-.27, -.21, .19, .33], .056, .03), ...lamps(.366, .075, .04, HEAD), ...lamps(-.321, .08, .05, TAIL, .012), ...lamps(.14, .225, .055, ['#ffb040', 2], .01),
  part(box(.006, .05, .07), '#c8c8c0', { x: .367, y: .085 }), part(cyl(.008, .008, .12, 6), '#9aa0a8', { x: .19, y: .19, z: -.05 }), part(box(.03, .01, .124), '#222', { x: .3, y: .17 })],
 car70: () => [part(box(.34, .045, .12), '#fff', { y: .055 }), part(box(.15, .04, .11), '#fff', { x: -.03, y: .095 }), part(box(.13, .03, .114), '#1c2430', { x: -.03, y: .097 }),
  ...wheels([-.11, .11], .056, .028), ...lamps(.171, .06, .04, HEAD, .014), ...lamps(-.171, .06, .042, TAIL, .014),
  part(box(.012, .012, .124), '#c8c8c0', { x: .172, y: .04 }), part(box(.012, .012, .124), '#c8c8c0', { x: -.172, y: .04 })],
 suv: () => [part(box(.3, .08, .12), '#fff', { y: .075 }), part(box(.19, .05, .115), '#fff', { x: -.03, y: .14 }), part(box(.18, .034, .118), '#1a2028', { x: -.03, y: .14 }),
  ...wheels([-.1, .1], .058, .036), ...lamps(.151, .09, .042, LED, .014), ...lamps(-.151, .09, .045, TAIL, .014),
  ...[.045, -.045].map(z => part(box(.17, .008, .008), '#222', { x: -.03, y: .17, z })), part(box(.006, .03, .06), '#222', { x: .152, y: .07 })],
 ev: () => [part(box(.3, .05, .115), '#fff', { y: .06 }), part(box(.17, .042, .11), '#141a22', { x: -.01, y: .104 }),
  part(box(.006, .008, .11), '#000', { x: .151, y: .074, emit: ['#7ff0ff', 3.4] }), part(box(.006, .008, .11), '#000', { x: -.151, y: .074, emit: TAIL }),
  part(box(.2, .004, .117), '#000', { y: .04, emit: ['#3fd8f0', 1.2] }), ...wheels([-.095, .095], .055, .03), part(box(.1, .006, .09), '#fff', { x: -.03, y: .127 }), ...[.057, -.057].map(z => part(box(.15, .006, .004), '#000', { x: .01, y: .085, z, emit: ['#5fe6ff', 1.6] }))],
 // 4-4-0 American: boiler, flared stack, brass dome, red cab and cowcatcher, coal tender behind.
 steam: () => [part(box(.36, .03, .08), '#1a1a1a', { x: .07, y: .05 }), part(cyl(.045, .045, .24, 12), '#2a2c2e', { x: .12, y: .115, rz: Math.PI / 2 }),
  part(cyl(.047, .047, .03, 12), '#151515', { x: .245, y: .115, rz: Math.PI / 2 }), part(cyl(.036, .018, .07, 10), '#151515', { x: .215, y: .19 }),
  part(cyl(.022, .026, .03, 10), '#b08a3a', { x: .12, y: .165 }), part(box(.09, .1, .1), '#6a2a1e', { x: -.05, y: .13 }), part(box(.11, .012, .115), '#1a1a1a', { x: -.05, y: .186 }),
  part(box(.03, .03, .102), '#000', { x: -.05, y: .15, emit: ['#ff8a3a', 1.6] }), part(cyl(0, .05, .06, 4), '#8a2a1e', { x: .3, y: .045, rz: -Math.PI / 2, sz: .9 }),
  ...wheels([.01, .1], .042, .045, '#8a2a1e'), ...wheels([.2, .25], .04, .024), part(box(.03, .03, .03), '#222', { x: .245, y: .18 }), part(box(.006, .022, .022), '#000', { x: .262, y: .18, emit: ['#fff0c8', 4] }),
  part(cyl(.012, .016, .022, 8), '#c9a040', { x: .07, y: .17 }), part(cyl(.018, .022, .026, 8), '#2a2c2e', { x: .17, y: .165 }), ...[.047, -.047].map(z => part(box(.14, .01, .006), '#9aa0a8', { x: .1, y: .05, z })),
  part(box(.13, .08, .095), '#2a2224', { x: -.18, y: .1 }), part(box(.11, .02, .08), '#0b0b0b', { x: -.18, y: .145 }), ...wheels([-.22, -.14], .04, .024)],
 boxcar: () => [part(box(.34, .11, .1), '#fff', { y: .115 }), part(box(.34, .008, .03), '#3a3330', { y: .174 }), part(box(.08, .085, .104), '#777', { y: .11 }), ...truck(-.12), ...truck(.12)],
 // Streamlined cab unit: silver body, rounded nose with a red bonnet and a gold stripe.
 diesel: () => [part(box(.36, .12, .1), '#c8ccd0', { x: -.03, y: .12 }), part(ball(.06), '#c8ccd0', { x: .15, y: .12, sx: 1.5, sz: .83 }),
  part(box(.07, .045, .104), '#b22a20', { x: .15, y: .1, sx: 1 }), part(box(.4, .012, .102), '#d8a830', { x: 0, y: .085 }), part(box(.03, .02, .09), '#000', { x: .185, y: .16, emit: ['#9cc8ff', .7] }),
  part(box(.008, .02, .02), '#000', { x: .238, y: .14, emit: ['#fff0c8', 4] }), part(box(.2, .012, .05), '#2a2c30', { x: -.05, y: .185 }), ...truck(-.14), ...truck(.1), part(box(.22, .018, .102), '#1c2430', { x: -.06, y: .15 })],
 freight: () => [part(box(.32, .1, .1), '#fff', { x: -.04, y: .115 }), part(box(.1, .14, .11), '#fff', { x: .15, y: .135 }), part(box(.04, .08, .1), '#fff', { x: .22, y: .1 }),
  part(box(.012, .04, .094), '#1a2230', { x: .2, y: .18 }), part(box(.42, .012, .104), '#e2b43a', { x: 0, y: .08 }), ...lamps(.243, .07, .035, LED, .012), lamp(.207, .2, 0, LED, .012), ...truck(-.14), ...truck(.12)],
 stack: () => [part(box(.42, .025, .09), '#2a2a2c', { y: .045 }), part(box(.38, .075, .09), '#fff', { y: .095 }), ...truck(-.15), ...truck(.15)],
 stackTop: () => [part(box(.38, .072, .09), '#fff', { y: .171 }), part(box(.38, .004, .092), '#000', { y: .134 })],
 // Passenger: a silver cab unit and bilevel coaches with two rows of lit windows.
 amtrak: () => [part(box(.32, .13, .11), '#c8ccd2', { x: -.04, y: .125 }), part(box(.09, .1, .11), '#c8ccd2', { x: .15, y: .105, rz: -.4 }), part(box(.44, .014, .112), '#c22a2a', { x: -.01, y: .09 }),
  part(box(.44, .014, .112), '#2a4a9a', { x: -.01, y: .074 }), part(box(.03, .03, .1), '#000', { x: .155, y: .165, rz: -.4, emit: ['#9cc8ff', .6] }), ...lamps(.2, .07, .035, LED, .014), ...truck(-.14), ...truck(.12)],
 coach: () => [part(box(.4, .15, .11), '#c4c8cc', { y: .135 }), part(box(.36, .022, .112), '#000', { y: .115, emit: ['#ffd9a0', 1.8] }), part(box(.36, .022, .112), '#000', { y: .175, emit: ['#ffd9a0', 1.5] }),
  part(box(.4, .012, .112), '#2a4a9a', { y: .075 }), ...truck(-.14), ...truck(.14)],
 cow: () => [part(box(.05, .032, .026), '#fff', { y: .034 }), part(box(.018, .018, .018), '#fff', { x: .032, y: .045 })],
 // Aircraft are centred on their wings.
 biplane: () => [part(box(.32, .05, .05), '#fff', { x: -.02 }), part(cyl(.03, .03, .04, 10), '#333', { x: .16, rz: Math.PI / 2 }), part(box(.08, .008, .62), '#fff', { x: .05, y: .065 }),
  part(box(.075, .008, .54), '#fff', { x: .06, y: -.025 }), ...[-.2, .2].map(z => part(box(.006, .085, .006), '#555', { x: .05, y: .02, z })), part(box(.06, .06, .006), '#fff', { x: -.16, y: .04 }),
  part(box(.05, .006, .18), '#fff', { x: -.16, y: .01 }), part(cyl(.07, .07, .003, 14), '#999', { x: .185, rz: Math.PI / 2 }), ...[.05, -.05].map(z => part(cyl(.02, .02, .01, 8), '#151515', { x: .08, y: -.06, z, rx: Math.PI / 2 }))],
 propliner: () => [part(cyl(.05, .05, .56, 12), '#c9ced3', { rz: Math.PI / 2 }), part(ball(.05), '#c9ced3', { x: .28, sx: 1.6 }), part(cyl(.012, .05, .16, 12), '#c9ced3', { x: -.36, rz: Math.PI / 2 }),
  part(box(.14, .012, 1), '#bcc2c8', { x: .04, y: -.03 }), ...[-.2, .2].map(z => part(cyl(.03, .026, .14, 10), '#5a5f66', { x: .1, y: -.02, z, rz: Math.PI / 2 })),
  ...[-.2, .2].map(z => part(cyl(.012, .02, .03, 8), '#2a2c30', { x: .18, y: -.02, z, rz: -Math.PI / 2 })), part(box(.1, .13, .008), '#c9ced3', { x: -.4, y: .06, shear: [0, 0, -.5, 0, 0, 0] }),
  part(box(.08, .008, .34), '#c9ced3', { x: -.41, y: .01 }), part(box(.36, .014, .102), '#000', { x: .02, y: .012, emit: ['#ffd9a0', 1.5] }), part(box(.04, .02, .07), '#18202a', { x: .3, y: .03 })],
 jet: () => [part(cyl(.06, .06, .9, 12), '#e9ecef', { rz: Math.PI / 2 }), part(ball(.06), '#e9ecef', { x: .45, sx: 1.8 }), part(cyl(.015, .06, .2, 12), '#e9ecef', { x: -.55, rz: Math.PI / 2 }),
  ...[1, -1].map(s => part(box(.22, .014, .6).translate(0, 0, .33 * s), '#cfd4da', { y: -.03, shear: [0, 0, 0, 0, -.55 * s, 0] })),
  ...[.25, -.25, .47, -.47].map(z => part(cyl(.022, .022, .12, 8), '#9aa0a8', { x: .1 - .55 * Math.abs(z), y: -.07, z, rz: Math.PI / 2 })),
  part(box(.16, .2, .01), '#2a4a8a', { x: -.52, y: .12, shear: [0, 0, -.6, 0, 0, 0] }), ...[1, -1].map(s => part(box(.11, .01, .2).translate(0, 0, .1 * s), '#cfd4da', { x: -.55, y: .02, shear: [0, 0, 0, 0, -.5 * s, 0] })),
  part(box(.7, .012, .122), '#000', { x: .02, y: .022, emit: ['#ffd9a0', 1.3] }), part(box(.86, .01, .122), '#2a4a8a', { x: -.02, y: -.005 }), part(box(.04, .02, .08), '#18202a', { x: .5, y: .03 })],
 heli: () => [part(ball(.07), '#c8282a', { sx: 1.4, sz: .9 }), part(ball(.05), '#14202c', { x: .055, y: .018, sx: 1.1, sz: 1.2 }), part(cyl(.012, .022, .26, 8), '#c8282a', { x: -.2, y: .02, rz: Math.PI / 2 }),
  part(box(.04, .07, .006), '#e8e8e8', { x: -.33, y: .05 }), part(cyl(.035, .035, .004, 12), '#666', { x: -.33, y: .05, z: .01, rx: Math.PI / 2 }), part(box(.03, .04, .102), '#e8e8e8', { x: -.04, y: 0 }),
  ...[.05, -.05].flatMap(z => [part(box(.22, .008, .008), '#333', { y: -.085, z }), part(box(.006, .03, .006), '#333', { x: .05, y: -.07, z }), part(box(.006, .03, .006), '#333', { x: -.05, y: -.07, z })]),
  part(cyl(.008, .008, .05, 6), '#333', { y: .085 })],
 rotor: () => [part(box(.66, .006, .03), '#262626', { y: .11 }), part(box(.03, .006, .66), '#262626', { y: .11 })],
 // Town buildings.
 house: () => [part(box(.075, .05, .062), '#fff', { y: .025 }), part(cyl(.042, .042, .085, 3, Math.PI / 2), '#5a3a2e', { y: .071, rz: Math.PI / 2 }), part(box(.02, .016, .064), '#000', { x: .012, y: .024, emit: WARM })],
 elevator: () => [...[-.06, 0, .06].map(x => part(cyl(.03, .03, .26, 12), '#d9d4c8', { x, y: .13 })), part(box(.05, .09, .05), '#cfc9bc', { x: .1, y: .22 }), part(box(.22, .015, .04), '#bdb6a8', { x: .02, y: .27 })],
 tower: () => { const g = part(new THREE.BoxGeometry(.12, 1, .12, 1, 14, 1), '#34404e', { y: .5 }), p = g.attributes.position, em = g.attributes.aEmit; for (let i = 0; i < p.count; i++) { const row = Math.round(p.getY(i) * 14); if (row % 2 && row < 14 && Math.abs(p.getX(i)) + Math.abs(p.getZ(i)) > .1) em.setXYZ(i, .42, .31, .17); } return [g]; },
};

const vehicleMaterial = () => {
 const material = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .55, metalness: .2 });
 material.onBeforeCompile = shader => {
  shader.vertexShader = shader.vertexShader.replace('#include <common>', '#include <common>\nattribute vec3 aEmit; varying vec3 vEmitC;').replace('#include <color_vertex>', '#include <color_vertex>\nvEmitC = aEmit;');
  shader.fragmentShader = shader.fragmentShader.replace('#include <common>', '#include <common>\nvarying vec3 vEmitC;').replace('#include <emissivemap_fragment>', '#include <emissivemap_fragment>\ntotalEmissiveRadiance += vEmitC;');
 };
 material.customProgramCacheKey = () => 'kfm-transport-vehicle';
 return material;
};

/** Visibility of something that exists from year a to year b, fading at both ends. */
const span = (y, a, b, edge = 1.6) => smooth(a - edge, a + .4, y) * (1 - smooth(b - .4, b + edge, y));

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 const { hemi } = stage(scene, { fog: .02, sun: [7, 5, 4.5], sunColor: '#ffc690', sunIntensity: 2.5 });
 hemi.intensity = .8; hemi.color.set('#9fc4dd');
 const land = terrain({ segments: 220 });
 const u = liveSurface(land);
 u.tint.value.set('#1d2c3a'); u.tintMix.value = .1; u.grey.value = 0;
 const hs = gridSampler(land), sides = blockSides(land.sample), water = riverWater(land.sample);
 scene.add(land.mesh, sides, water);
 const random = rng(1860);

 // Network: every line in one mesh; the shader hides what is not yet built.
 const lines = {};
 for (const spec of NET) lines[spec.id] = { ...spec, ...track(spec.fn, hs) };
 const pos = [], along = [], acr = [], built = [], gone = [], kinds = [], index = [];
 for (const kind of ORDER) for (const l of Object.values(lines)) {
  if (l.kind !== kind) continue;
  const base = pos.length / 3, half = l.w / 2;
  for (let i = 0; i < l.n; i++) {
   for (const s of [1, -1]) {
    const x = l.xs[i] + l.sx[i] * half * s, z = l.zs[i] + l.sz[i] * half * s;
    pos.push(x, Math.max(hs(x, z) + .03, l.ys[i]) + (kind === 5 ? .012 : kind === 6 ? .008 : 0), z);
    along.push(i * l.ds); acr.push(s); built.push(lerp(l.y[0], l.y[1], i / (l.n - 1))); gone.push(l.gone ?? 9999); kinds.push(kind);
   }
   if (i < l.n - 1) { const a = base + i * 2; index.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
  }
 }
 const netGeo = new THREE.BufferGeometry();
 netGeo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
 for (const [name, arr] of [['aAlong', along], ['aAcross', acr], ['aBuilt', built], ['aGone', gone], ['aKind', kinds]]) netGeo.setAttribute(name, new THREE.Float32BufferAttribute(arr, 1));
 netGeo.setIndex(index);
 const nu = { uYear: { value: 1860 }, uTime: { value: 0 }, uPulse: { value: 0 } };
 const network = new THREE.Mesh(netGeo, new THREE.ShaderMaterial({ uniforms: nu, vertexShader: NET_VERT, fragmentShader: NET_FRAG, transparent: true, depthWrite: false, side: THREE.DoubleSide }));
 network.renderOrder = 2;
 scene.add(network);
 const builtAt = (l, d) => lerp(l.y[0], l.y[1], clamp(d / l.len));

 // Lights: one additive point cloud; every source owns fixed slots.
 const slots = [];
 const light = (color, size) => { slots.push([color, size]); return slots.length - 1; };

 // Instanced models; requests are counted first, meshes made once counts are known.
 const want = {};
 const take = (type, color = '#ffffff') => { (want[type] ??= []).push(color); return want[type].length - 1; };

 // ---- towns: access year = first line within reach of the centre.
 const towns = TOWNS.map(([x, z, size], i) => {
  let access = 9999, via = null;
  for (const l of Object.values(lines)) {
   if (l.kind === 1 || l.kind === 6) continue;
   for (let k = 0; k < l.n; k++) if (Math.hypot(l.xs[k] - x, l.zs[k] - z) < .32) { const y = lerp(l.y[0], l.y[1], k / (l.n - 1)); if (y < access) { access = y; via = { l, k }; } }
  }
  const count = [9, 14, 24][size], grow = [6, 3.6, 2][size], houses = [];
  for (let k = 0; k < count; k++) {
   const r = .09 + .052 * Math.sqrt(k) * (1 + size * .25), a = k * 2.39996 + i;
   const hx = Math.round((x + Math.cos(a) * r) / .07) * .07, hz = Math.round((z + Math.sin(a) * r) / .07) * .07;
   const tint = ['#efe6d4', '#e8dcc0', '#d9d2c6', '#c96f4f', '#f2efe8'][Math.floor(random() * 5)];
   houses.push({ x: hx, z: hz, y: hs(hx, hz), rot: random() < .5 ? 0 : Math.PI / 2, s: .8 + random() * .45, at: access + .6 + k * grow * (.7 + random() * .6), idx: take('house', tint), slot: light('#ffd89a', .32 + random() * .1) });
  }
  const town = { x, z, y: hs(x, z), size, access, houses, flash: light('#ffd89a', 2.6), glow: light('#ffcf8a', 1.5 + size * .5) };
  if (via?.l.kind === 2) { // grain elevators rise beside the track in rail towns
   const { l, k } = via, o = .2, ex = l.xs[k] + l.sx[k] * o, ez = l.zs[k] + l.sz[k] * o;
   town.elevator = { x: ex, z: ez, y: hs(ex, ez), rot: Math.atan2(-(l.sz[k]), l.sx[k]) + Math.PI / 2, at: Math.max(access + 8, 1888), idx: take('elevator'), slot: light('#ff4a3a', .16) };
  }
  if (size === 2) town.towers = [[.05, -.32, .9], [-.18, -.34, .62], [.25, -.4, .55], [-.05, -.55, .72], [.2, -.62, .4], [-.32, -.5, .42], [.38, -.25, .34]].map(([dx, dz, h], k) => ({ x: x + dx, z: z + dz, y: hs(x + dx, z + dz), h, at: 1956 + k * 7, idx: take('tower'), slot: light('#ff3a2a', .14) }));
  return town;
 });

 // ---- fleets: each runs in its era, only on lines already built there.
 const fleets = [];
 const roadFleet = (type, years, routes, count, { lane = .045, colors = ['#ffffff'], half = .15, lights = 'car' } = {}) => {
  const units = [];
  for (let i = 0; i < count; i++) {
   const l = lines[routes[i % routes.length]], dir = i % 2 ? -1 : 1, cycle = l.len + .8;
   const head = lights === 'lantern' ? [light('#ffb35a', .12)] : [light(lights === 'led' ? '#eef4ff' : lights === 'ev' ? '#8ff0ff' : '#ffe6b8', .2), light('#ff3a24', .1)];
   units.push({ l, dir, cycle, v: 0, d0: 0, lane: lane * (lights === 'lantern' ? .5 : 1) * (1 + (random() < .3 && l.kind === 5 ? .8 : 0)), parts: [{ type, idx: take(type, colors[i % colors.length]), back: 0, half: half * GS, lat: 0, g: GS }], head });
  }
  fleets.push({ years, units, mode: 'ground', lights });
 };
 const trainFleet = (years, consists, opts = {}) => {
  const units = consists.map(([route, dir, phase, cars]) => {
   const l = lines[route], parts = [];
   let back = 0;
   for (const [type, len0, color] of cars) { const len = len0 * TS; parts.push({ type, idx: take(type, color), back: back + len / 2, half: len / 2, lat: 0, g: TS }); if (type === 'stack') parts.push({ type: 'stackTop', idx: take('stackTop', STACK[(parts.length * 7) % STACK.length]), back: back + len / 2, half: len / 2, lat: 0, g: TS }); back += len + .02; }
   return { l, dir, cycle: l.len + back + 1, v: opts.v ?? .6, d0: phase * (l.len + back), lane: dir * (opts.lane ?? 0), parts, head: [light('#fff0c8', .34)], smoke: opts.smoke ? Array.from({ length: 12 }, () => light('#aeb6bb', .2)) : null };
  });
  fleets.push({ years, units, mode: 'ground', lights: 'train' });
 };
 const STACK = ['#c0392b', '#2e5d9a', '#d8d2c4', '#3f7a4a', '#d07a2a', '#7a7f86', '#a8322a', '#2a6f7a'];
 const BOX = ['#7a3b26', '#6e3420', '#8a5a2a', '#5a4a3a', '#7a3b26'];
 const DIRT = SECTION.flatMap((_, i) => [`ns${i}`, `ew${i}`]);

 roadFleet('wagon', [1850, 1899], ['trail'], 6, { half: .14, lights: 'lantern', lane: .03 });
 roadFleet('stage', [1850, 1893], ['trail'], 3, { half: .18, lights: 'lantern', lane: .03 });
 roadFleet('wagon', [1896, 1914], DIRT, 8, { half: .14, lights: 'lantern', lane: .02 });
 roadFleet('modelT', [1907, 1931], [...DIRT, 'H1', 'H2'], 18, { half: .13, colors: ['#1e1e20', '#1e1e20', '#1e1e20', '#24342a', '#3a2020'], lane: .03 });
 roadFleet('sedan', [1929, 1961], ['H1', 'H2', 'H3', 'H4', 'H1', 'H2', 'H3', 'H4', ...DIRT.slice(0, 4)], 18, { colors: ['#2f4a3a', '#6a2a2a', '#d8cfb0', '#26304a', '#3a3a3a', '#8a7a5a'] });
 roadFleet('pickup', [1932, 1966], ['H1', 'H2', 'H3', 'H4', ...DIRT.slice(4)], 8, { colors: ['#b04a2a', '#3a5a7a', '#5a6a3a', '#c8b070'] });
 roadFleet('boxtruck', [1930, 1966], ['H1', 'H2', 'H3'], 8, { half: .18, colors: ['#e8e4da', '#c8a040', '#a83a2a', '#3a6a5a'] });
 roadFleet('semi', [1950, 2030], ['H1', 'H2', 'H3', 'I1', 'I2', 'I1', 'I2', 'I1'], 16, { half: .34, colors: ['#e8e8e8', '#b8322a', '#2e4a7a', '#e2b43a', '#d8d8d8', '#3a6a4a'], lane: .085 });
 roadFleet('car70', [1964, 2003], ['I1', 'I2', 'I1', 'I2', 'H1', 'H2', 'H3'], 22, { half: .17, colors: ['#8a5a2a', '#c8a040', '#7aa0c8', '#b03a2a', '#3a5a3a', '#d8d4c8', '#b8bcc0'], lane: .085 });
 roadFleet('suv', [1999, 2030], ['I1', 'I2', 'I1', 'I2', 'H1', 'H2', 'H3'], 16, { colors: ['#d8dadc', '#2a2c30', '#8a9098', '#5a1a1a', '#e8e8e8', '#2a3a5a'], lane: .09, lights: 'led' });
 roadFleet('ev', [2008, 2030], ['I1', 'I2', 'I1', 'I2', 'H2'], 10, { colors: ['#f0f2f4', '#c8ccd0', '#3a4048', '#b8302a'], lane: .09, lights: 'ev' });
 // Traffic keeps its spacing: everyone on a carriageway moves at that road's pace,
 // evenly phased across every era's fleet, so vehicles never drive through each other.
 const PACE = { 0: 0, 3: .62, 4: .85, 5: 1.12 }, lanesOf = {};
 fleets.forEach((f, fi) => { const mine = {}; for (const unit of f.units) { const key = `${unit.l.id}${unit.dir}`; (mine[key] ??= []).push(unit); } for (const [key, list] of Object.entries(mine)) list.forEach((unit, r) => (lanesOf[key] ??= []).push([r / list.length + fi * .013, unit])); });
 // Interleave the fleets so each era's vehicles spread over the whole road.
 for (const group of Object.values(lanesOf)) group.sort((p, q) => p[0] - q[0]).forEach(([, unit], j) => {
  unit.v = unit.l.kind ? PACE[unit.l.kind] : unit.cycle / D; // trail traffic laps exactly once a loop, so 1860 restarts seamlessly
  unit.d0 = (j / group.length + (unit.dir < 0 ? .37 : 0)) * unit.cycle; unit.mates = group;
 });

 const steamCars = n => [['steam', .56, '#ffffff'], ...Array.from({ length: n }, (_, i) => ['boxcar', .36, BOX[i % BOX.length]])];
 trainFleet([1863, 1946], [['R1', 1, 0, steamCars(5)], ['R1', 1, .55, steamCars(4)], ['R2', -1, .3, steamCars(5)], ['B1', 1, .2, steamCars(3)], ['B2', 1, .6, steamCars(3)], ['B4', -1, .1, steamCars(2)]], { v: .55, smoke: true });
 const dieselCars = (n, a = 2) => [...Array.from({ length: a }, () => ['diesel', .48, '#ffffff']), ...Array.from({ length: n }, (_, i) => ['boxcar', .36, ['#7a3b26', '#9aa0a8', '#c8b070', '#3a5a7a', '#8a8a80'][i % 5]])];
 trainFleet([1940, 1986], [['R1', 1, .1, dieselCars(6)], ['R1', -1, .62, dieselCars(5)], ['R2', 1, .4, dieselCars(6)], ['B2', -1, .3, dieselCars(3, 1)], ['B5', 1, .5, dieselCars(3, 1)]], { v: .75, lane: .0 });
 const stackCars = n => [['freight', .48, '#2b4c8c'], ['freight', .48, '#d06a2a'], ...Array.from({ length: n }, (_, i) => ['stack', .42, STACK[i % STACK.length]])];
 trainFleet([1980, 2030], [['R1', 1, .05, stackCars(8)], ['R1', 1, .55, stackCars(7)], ['R2', -1, .35, stackCars(8)]], { v: .7 });
 trainFleet([1971, 2030], [['R1b', 1, .2, [['amtrak', .44, '#ffffff'], ...Array.from({ length: 5 }, () => ['coach', .42, '#ffffff'])]]], { v: 1.05 });

 // Cattle drives walk north to the railhead.
 const herd = { l: lines.cattle, dir: 1, cycle: lines.cattle.len + 2.4, v: .32, d0: 0, lane: 0, head: [], parts: Array.from({ length: 22 }, (_, i) => ({ type: 'cow', idx: take('cow', ['#7a4a2a', '#5a3a26', '#9a7050', '#3a2a20', '#d8c8b0'][i % 5]), back: (i % 11) * .13 + random() * .07, half: .05, lat: (random() - .5) * .3, wob: random() * TAU, g: CS })) };
 fleets.push({ years: [1867, 1886], units: [herd, { ...herd, d0: 1.2 + herd.cycle * .5, parts: herd.parts.slice(11) }], mode: 'ground', lights: 'none' });
 herd.parts = herd.parts.slice(0, 11);

 // Aircraft fly closed loops above the block, banking into their turns.
 const flyer = (type, years, curve, w, p0, color = '#ffffff', extra = {}) => fleets.push({ years, mode: 'air', units: [{ type, idx: take(type, color), curve, w, p0, nav: [light('#ff3a2a', .14), light('#3aff6a', .14), light('#ffffff', .2)], ...extra }] });
 const loop8 = (R, r, y, rot, dy = .25) => (p, out) => { const x = R * Math.sin(p), z = r * Math.sin(2 * p), c = Math.cos(rot), s = Math.sin(rot); return out.set(x * c - z * s, y + dy * Math.sin(2 * p + 1), x * s + z * c); };
 const ellipse = (R, r, y, rot, dy = .2) => (p, out) => { const x = R * Math.cos(p), z = r * Math.sin(p), c = Math.cos(rot), s = Math.sin(rot); return out.set(x * c - z * s, y + dy * Math.sin(3 * p), x * s + z * c); };
 flyer('biplane', [1913, 1937], loop8(4.6, 2.4, 3.1, .3), .26, 0, '#e2b43a');
 flyer('biplane', [1918, 1937], ellipse(5, 3.2, 3.4, -.5), -.22, 2, '#b8322a');
 flyer('propliner', [1935, 1966], ellipse(5.6, 3.4, 3.6, .2), .28, .5);
 flyer('propliner', [1938, 1966], loop8(5.2, 2.8, 3.3, -.9), -.25, 3.5);
 const contrail = () => Array.from({ length: 56 }, () => light('#dfe9f2', .2));
 flyer('jet', [1958, 2030], ellipse(6.4, 4.2, 4.3, .4, .15), .3, 0, '#ffffff', { trail: contrail() });
 flyer('jet', [1962, 2030], loop8(6, 3.2, 4.6, -.6, .15), -.24, 1.8, '#ffffff', { trail: contrail() });
 flyer('jet', [1975, 2030], ellipse(6.8, 3.6, 4.0, 2.1, .15), -.27, 4, '#ffffff', { trail: contrail() });
 const hover = (ax, az, fx, fz, y, ph) => (p, out) => out.set(ax * Math.sin(p * fx + ph), y + .18 * Math.sin(p * 2.3), az * Math.sin(p * fz));
 flyer('heli', [1951, 2030], hover(3.4, 2.6, 1, 1.5, 2.2, .4), .32, 0, '#ffffff', { rotor: take('rotor') });
 flyer('heli', [1985, 2030], hover(2.6, 3.2, 1.5, 1, 2.5, 2), -.28, 1, '#ffffff', { rotor: take('rotor') });

 // ---- hero chases: midway through each beat the camera glides down beside that era's signature vehicles.
 const grounds = fleets.filter(f => f.mode === 'ground').flatMap(f => f.units.map(u => ({ f, u })));
 const find = (type, route, dir) => grounds.find(({ u }) => u.parts[0].type === type && u.l.id === route && (dir === undefined || u.dir === dir));
 const alongAt = (l, x, z) => { let best = 0, bd = Infinity; for (let i = 0; i < l.n; i++) { const dd = (l.xs[i] - x) ** 2 + (z === undefined ? 0 : (l.zs[i] - z) ** 2); if (dd < bd) { bd = dd; best = i; } } return best * l.ds; };
 // Rephase a unit so its lead sits at (x[, z]) at time tm; lane- or line-mates shift with it and keep their spacing.
 const place = ({ f, u }, tm, x, z) => {
  const d = alongAt(u.l, x, z), shift = (u.dir > 0 ? d : u.l.len - d) + u.parts[0].back + .4 - u.v * tm - u.d0;
  for (const o of u.mates ? u.mates.map(m => m[1]) : f.units.filter(o => o.l === u.l && o.dir === u.dir)) o.d0 += shift;
  return u;
 };
 // An aircraft that flies with the chase: `from`/`to` are distances along the lead's heading over the chase.
 const escort = (type, color, from, to, side, up) => ({ type, idx: take(type, color), from, to, side, up, nav: [light('#ff3a2a', .14), light('#3aff6a', .14), light('#ffffff', .2)], trail: type === 'jet' ? contrail() : null, rotor: type === 'heli' ? take('rotor') : undefined });
 const hero = (t0, t1, [type, route, dir, x, z], cam, others = [], air = null) => {
  const tm = (t0 + t1) / 2, lead = place(find(type, route, dir), tm, x, z);
  if (cam.color) want[type][lead.parts[0].idx] = cam.color; // a signature paint job so the hero reads at a glance
  for (const [ty, ro, di, ox, oz] of others) place(find(ty, ro, di), tm, ox, oz);
  return { t0, t1, lead, air, cam: { back: 3, side: 1.5, up: 1, ahead: 1.2, lift: .3, ...cam } };
 };
 const HEROES = [
  hero(1, 4.8, ['wagon', 'trail', 1, 4.7], { side: 1.6 }, [['steam', 'R1', 1, 5.0]]),
  hero(6.2, 10.2, ['steam', 'R2', -1, 1.5], { back: 2.2, side: 2, up: 1.1, ahead: 1.4 }),
  hero(11.7, 15.2, ['modelT', 'ns3', undefined, 4.5, -3.2], {}, [], escort('biplane', '#e2b43a', -3, 3.5, .3, .85)),
  hero(16.8, 21.2, ['sedan', 'H4', -1, -3.3], { side: 1.5, color: '#8a2a2a' }, [['diesel', 'R1', -1, -3.0]], escort('propliner', '#ffffff', 6, -3, .8, 1.15)),
  hero(22.8, 27.2, ['semi', 'I2', 1, 3.4, -3.4], { back: 3.4, side: 1.6, color: '#c8322a' }, [], escort('jet', '#ffffff', 9, -4, -1.2, 1.5)),
  hero(29.2, 32.9, ['ev', 'I1', -1, -3.9], { back: 2.4, side: .8, up: 1.2, ahead: 1.4, color: '#eef2f5' }, [['amtrak', 'R1b', 1, -3.6], ['freight', 'R1', 1, -2.6]], escort('heli', '#ffffff', 4.2, 2.6, -.9, 1.05)),
 ];

 // Era clock: one dot per five-year step along the foot of the north wall.
 const clock = Array.from({ length: 34 }, (_, i) => ({ x: lerp(-5.6, 5.6, i / 33), slot: light('#f3d38e', .32) }));

 // Build instanced meshes now that every request is known.
 const material = vehicleMaterial(), meshes = {}, ZERO = new THREE.Matrix4().makeScale(0, 0, 0);
 for (const [type, colors] of Object.entries(want)) {
  const mesh = new THREE.InstancedMesh(mergeGeometries(MODELS[type]()), material, colors.length);
  mesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
  mesh.frustumCulled = false; // instances move anywhere; bounds would go stale
  colors.forEach((c, i) => { mesh.setMatrixAt(i, ZERO); mesh.setColorAt(i, _c.set(c)); });
  meshes[type] = mesh; scene.add(mesh);
 }
 const glow = glowPoints(slots.length, { size: .2 });
 slots.forEach(([c, s], i) => { _c.set(c); glow.colors.set([_c.r, _c.g, _c.b], i * 3); glow.sizes[i] = s; glow.alphas[i] = 0; });
 scene.add(glow);

 // Town buildings are static: place them once, scale them by year in update.
 const M = new THREE.Matrix4(), P = new THREE.Vector3(), Q = new THREE.Vector3(), F = new THREE.Vector3(), Up = new THREE.Vector3(), S = new THREE.Vector3(), Y = new THREE.Vector3(0, 1, 0), scl = new THREE.Vector3();
 const setLight = (slot, p, alpha, size) => { glow.positions[slot * 3] = p.x; glow.positions[slot * 3 + 1] = p.y; glow.positions[slot * 3 + 2] = p.z; glow.alphas[slot] = alpha; if (size !== undefined) glow.sizes[slot] = size; };
 const local = (fx, fy, fz) => Q.copy(P).addScaledVector(F, fx).addScaledVector(Up, fy).addScaledVector(S, fz);
 const compose = (k, sy = k) => { M.makeBasis(F, Up, S); M.scale(scl.set(k, sy, k)); M.setPosition(P); return M; };

 /** Pose on a line at distance d travelling `dir`; chord over the body length keeps curves smooth. */
 function pose(l, d, dir, off, half) {
  l.at(d + half * dir, off, F); l.at(d - half * dir, off, Q); l.at(d, off, P);
  F.sub(Q); if (F.lengthSq() < 1e-8) F.set(dir, 0, 0); F.normalize();
  P.y = Math.max(P.y, hs(P.x, P.z) + .03);
  S.crossVectors(F, Y).normalize(); Up.crossVectors(S, F);
 }
 const colorFor = (year, out) => out.set('#ffb35a').lerp(_tmpC.set('#ffd89a'), smooth(1905, 1935, year)).lerp(_tmpC.set('#e8f0ff'), smooth(2000, 2020, year) * .5);
 const _tmpC = new THREE.Color(), townCol = new THREE.Color();

 function update(t) {
  const year = eraYear(t), live = 1 - smooth(33.9, 34.3, t) + smooth(35.45, 35.95, t), pulse = window01(t, 32.8, 34.6, .5);
  nu.uYear.value = year; nu.uTime.value = t; nu.uPulse.value = pulse;
  glow.alphas.fill(0);

  // Towns: a flash when the first line arrives, then houses and lights fill in.
  colorFor(year, townCol);
  for (const [ti, town] of towns.entries()) {
   const reached = smooth(town.access, town.access + .6, year);
   P.set(town.x, town.y + .12, town.z);
   setLight(town.flash, P, live * smooth(town.access, town.access + .3, year) * (1 - smooth(town.access + .3, town.access + 4, year)) * .9 + pulse * (.35 + .25 * Math.sin(t * 5 + ti)) * reached);
   setLight(town.glow, P, reached * (.32 + .08 * town.size) * (.8 + .2 * smooth(1930, 2000, year)));
   for (const h of town.houses) {
    const k = smooth(h.at, h.at + 1.4, year);
    M.makeRotationY(h.rot); M.scale(scl.set(h.s * Math.max(k, 1e-4), h.s * Math.max(k, 1e-4), h.s * Math.max(k, 1e-4))); M.setPosition(h.x, h.y, h.z);
    meshes.house.setMatrixAt(h.idx, k > .001 ? M : ZERO);
    P.set(h.x, h.y + .07, h.z);
    setLight(h.slot, P, k * (.7 + .3 * smooth(1915, 1950, year)));
    glow.colors.set([townCol.r, townCol.g, townCol.b], h.slot * 3);
   }
   if (town.elevator) {
    const e = town.elevator, k = smooth(e.at, e.at + 3, year);
    M.makeRotationY(e.rot); M.scale(scl.set(1, Math.max(k, .001), 1)); M.setPosition(e.x, e.y, e.z);
    meshes.elevator.setMatrixAt(e.idx, k > .001 ? M : ZERO);
    P.set(e.x, e.y + .3 * k, e.z); setLight(e.slot, P, k * (.5 + .5 * (Math.sin(t * 3 + ti) > 0)) * smooth(1930, 1950, year));
   }
   if (town.towers) for (const w of town.towers) {
    const k = smooth(w.at, w.at + 6, year), h = w.h * k;
    M.makeRotationY(.08); M.scale(scl.set(1, Math.max(h, .001), 1)); M.setPosition(w.x, w.y, w.z);
    meshes.tower.setMatrixAt(w.idx, k > .001 ? M : ZERO);
    P.set(w.x, w.y + h + .03, w.z); setLight(w.slot, P, k * (Math.sin(t * 2.4 + w.h * 9) > .3 ? .9 : .15));
   }
  }

  // Vehicles: hidden types are zeroed once, visible ones re-posed every frame.
  for (const fleet of fleets) {
   const vis = span(year, fleet.years[0], fleet.years[1]) * live;
   if (vis < .002) {
    if (fleet.shown) { for (const unit of fleet.units) { if (unit.parts) for (const p of unit.parts) meshes[p.type].setMatrixAt(p.idx, ZERO); else meshes[unit.type].setMatrixAt(unit.idx, ZERO); if (unit.rotor !== undefined) meshes.rotor.setMatrixAt(unit.rotor, ZERO); } fleet.shown = false; }
    continue;
   }
   fleet.shown = true;
   for (const unit of fleet.units) (fleet.mode === 'air' ? flyUnit : groundUnit)(unit, t, year, vis, fleet.lights);
  }
  for (const m of Object.values(meshes)) m.instanceMatrix.needsUpdate = true;

  // Era clock: past steps stay lit, the current five-year step burns brightest.
  const f = clamp((year - 1860) / 5, 0, 33);
  for (const [i, dot] of clock.entries()) {
   const hi = smooth(i - .15, i, f) * (1 - smooth(i + .85, i + 1, f)) + (i === 33 ? smooth(32.85, 33, f) : 0);
   P.set(dot.x, -1.98, -HALF - .05);
   setLight(dot.slot, P, .12 + .33 * smooth(i - .15, i, f) + .55 * clamp(hi), .32 + .4 * clamp(hi));
  }

  // Hero chase: the escort flies with the lead vehicle while the camera rides alongside.
  let hw = 0, hh = null;
  for (const h of HEROES) {
   const w = smooth(h.t0, h.t0 + 1.2, t) * (1 - smooth(h.t1 - 1.2, h.t1, t));
   if (w > .002) { hw = w; hh = h; } else if (h.air) { meshes[h.air.type].setMatrixAt(h.air.idx, ZERO); if (h.air.rotor !== undefined) meshes.rotor.setMatrixAt(h.air.rotor, ZERO); }
  }
  if (hh) { heroFrame(hh, t); if (hh.air) escortAt(hh.air, hh, t, hw); }
  glow.commit();

  // Overview: the camera sways (seamless) around the block...
  orbit(camera, t, { radius: 21.5, height: 10.8, target: [0, -.55, 0], start: -.86 + .3 * Math.sin(t / D * TAU), speed: 0 });
  // ...and in each beat glides down to ride beside that era's vehicles, then back out.
  if (hh) {
   const e = hw * hw * (3 - 2 * hw), c = hh.cam;
   ov.copy(camera.position);
   camP.copy(HP).addScaledVector(HF, -c.back).addScaledVector(HS, c.side); camP.y = Math.max(camP.y + c.up, hs(camP.x, camP.z) + .3);
   look.copy(HP).addScaledVector(HF, c.ahead); look.y += c.lift;
   camera.position.lerpVectors(ov, camP, e);
   camera.lookAt(look.lerpVectors(TARGET, look, e));
  }
 }

 const HP = new THREE.Vector3(), HF = new THREE.Vector3(), HS = new THREE.Vector3(), HT = new THREE.Vector3(), ov = new THREE.Vector3(), camP = new THREE.Vector3(), look = new THREE.Vector3(), TARGET = new THREE.Vector3(0, -.55, 0);
 function leadAt(u, t) {
  const front = ((u.d0 + u.v * t) % u.cycle + u.cycle) % u.cycle - .4, p = u.parts[0], s = front - p.back;
  pose(u.l, u.dir > 0 ? s : u.l.len - s, u.dir, u.lane * u.dir + p.lat, p.half);
 }
 /** Lead position and a heading averaged over ±0.35 s, so the chase camera does not twitch on curves. */
 function heroFrame(h, t) {
  leadAt(h.lead, t - .35); HT.copy(F); leadAt(h.lead, t + .35); HT.add(F); leadAt(h.lead, t);
  HP.copy(P); HF.copy(HT).add(F).setY(0).normalize(); HS.set(-HF.z, 0, HF.x);
 }
 function escortAt(a, h, t, w) {
  const along = lerp(a.from, a.to, clamp((t - h.t0) / (h.t1 - h.t0))), sign = a.to > a.from ? 1 : -1;
  P.copy(HP).addScaledVector(HF, along).addScaledVector(HS, a.side); P.y += a.up + .06 * Math.sin(t * 1.3);
  F.copy(HF).multiplyScalar(sign); S.crossVectors(F, Y).normalize(); Up.crossVectors(S, F);
  const roll = .12 * Math.sin(t * .9); Q.copy(Up); Up.multiplyScalar(Math.cos(roll)).addScaledVector(S, -Math.sin(roll)); S.multiplyScalar(Math.cos(roll)).addScaledVector(Q, Math.sin(roll));
  meshes[a.type].setMatrixAt(a.idx, compose(w * AS));
  if (a.rotor !== undefined) { M.multiply(_m.makeRotationY(t * 23)); meshes.rotor.setMatrixAt(a.rotor, M); setLight(a.nav[0], local(-.02, .07 * AS, 0), w * (Math.sin(t * 6) > .4 ? 1 : .1)); return; }
  const span2 = { biplane: .31, propliner: .5, jet: .64 }[a.type] * AS;
  setLight(a.nav[0], local(-.06, 0, -span2), w * .9); setLight(a.nav[1], local(-.06, 0, span2), w * .9);
  if (a.trail) { // a straight contrail streaming back from the engines
   const n = a.trail.length / 2;
   for (let j = 0; j < n; j++) for (const side of [0, 1]) {
    const age = j / n; local(-.5 * AS - j * .16, -.04, (side ? .36 : -.36) * AS);
    setLight(a.trail[j * 2 + side], Q, w * Math.pow(1 - age, 1.3) * .35 * smooth(0, .05, age), .08 + age * .45);
   }
  }
 }

 function groundUnit(u, t, year, vis, kind) {
  const { l } = u, front = ((u.d0 + u.v * t) % u.cycle + u.cycle) % u.cycle - .4;
  let shown = 0;
  for (const p of u.parts) {
   const s = front - p.back, d = u.dir > 0 ? s : l.len - s;
   let k = vis * smooth(0, .25, s) * smooth(l.len, l.len - .25, s);
   if (k > .002) { const b = builtAt(l, d); k *= smooth(b + .2, b + 1, year) * (l.gone ? 1 - smooth(l.gone - 1.5, l.gone, year) : 1); }
   if (k < .002) { meshes[p.type].setMatrixAt(p.idx, ZERO); continue; }
   pose(l, d, u.dir, u.lane * u.dir + p.lat, p.half);
   if (p.wob !== undefined) { F.applyAxisAngle(Y, .35 * Math.sin(t * 2 + p.wob)); S.crossVectors(F, Y).normalize(); }
   meshes[p.type].setMatrixAt(p.idx, compose(k * p.g));
   if (p === u.parts[0]) {
    shown = k;
    if (kind === 'train') setLight(u.head[0], local(p.half * .95, .17 * p.g, 0), k * .95);
    else if (kind === 'lantern') setLight(u.head[0], local(p.half * .9, .13 * p.g, .02), k * (.5 + .1 * Math.sin(t * 9 + u.d0)));
    else if (kind !== 'none') { setLight(u.head[0], local(p.half + .03, .08 * p.g, 0), k * .85); setLight(u.head[1], local(-p.half, .08 * p.g, 0), k * .6); }
   }
  }
  // Steam: puffs leave the stack and drift up and downwind, from where the engine was.
  if (u.smoke && shown > 0) for (const [j, slot] of u.smoke.entries()) {
   const age = ((t * 1.1 + j / u.smoke.length) % 1), then = t - age * 1.2, fr = ((u.d0 + u.v * then) % u.cycle + u.cycle) % u.cycle - .4 - u.parts[0].back;
   if (fr < 0 || fr > l.len) continue;
   pose(l, u.dir > 0 ? fr : l.len - fr, u.dir, u.lane * u.dir, .1);
   local(.2 * TS, .24 * TS + age * .5, 0); Q.x += age * .35; Q.z += age * .18;
   setLight(slot, Q, shown * Math.pow(1 - age, 1.2) * .55, .2 + age * .7);
  }
 }

 const C0 = new THREE.Vector3(), C1 = new THREE.Vector3(), H0 = new THREE.Vector3(), H1 = new THREE.Vector3();
 function flyUnit(u, t, year, vis) {
  const p = u.p0 + u.w * t, e = .02 * Math.sign(u.w);
  u.curve(p, P); u.curve(p + e, C1); u.curve(p - e, C0);
  F.subVectors(C1, C0).normalize();
  // Bank into the turn: heading change per unit of arc sets the roll.
  H0.subVectors(P, C0).setY(0).normalize(); H1.subVectors(C1, P).setY(0).normalize();
  const turn = H0.x * H1.z - H0.z * H1.x, speed = C1.distanceTo(C0) / (2 * Math.abs(e)) * Math.abs(u.w), roll = clamp(-turn / (C1.distanceTo(C0) / 2 + 1e-4) * speed * .35, -.65, .65);
  S.crossVectors(F, Y).normalize(); Up.crossVectors(S, F);
  if (u.type === 'heli') { // nose down with forward speed, rotor spinning
   F.addScaledVector(Up, -.12).normalize(); Up.crossVectors(S, F);
  }
  const c = Math.cos(roll), s = Math.sin(roll); Q.copy(Up); Up.multiplyScalar(c).addScaledVector(S, -s); S.multiplyScalar(c).addScaledVector(Q, s);
  const k = vis;
  meshes[u.type].setMatrixAt(u.idx, compose(k * AS));
  const span2 = { biplane: .31, propliner: .5, jet: .64, heli: .0 }[u.type] * AS;
  if (u.type === 'heli') {
   M.multiply(_m.makeRotationY(t * 23 + u.p0));
   meshes.rotor.setMatrixAt(u.rotor, M);
   setLight(u.nav[0], local(-.02, .07 * AS, 0), k * (Math.sin(t * 6 + u.p0) > .4 ? 1 : .1));
   setLight(u.nav[2], local(.12 * AS, -.08 * AS, 0), k * .5, .22);
  } else {
   setLight(u.nav[0], local(-.06, 0, -span2), k * .9);
   setLight(u.nav[1], local(-.06, 0, span2), k * .9);
   setLight(u.nav[2], local({ biplane: -.18, propliner: -.44, jet: -.62 }[u.type] * AS, .04, 0), k * (Math.sin(t * 7 + u.p0 * 3) > .85 ? 1 : 0), .3);
  }
  if (u.trail) { // contrails: twin streams that widen and fade behind the engines
   const n = u.trail.length / 2;
   for (let j = 0; j < n; j++) {
    const q = p - Math.sign(u.w) * (j + 1) * .018, age = j / n;
    u.curve(q, C0); u.curve(q + e, C1); H0.subVectors(C1, C0).setY(0).normalize();
    for (const side of [0, 1]) {
     const o = side ? .36 * AS : -.36 * AS;
     Q.set(C0.x - H0.z * o, C0.y - .05, C0.z + H0.x * o);
     setLight(u.trail[j * 2 + side], Q, k * Math.pow(1 - age, 1.3) * .32 * smooth(0, .06, age), .1 + age * .5);
    }
   }
  }
 }

 update(0);
 return { scene, camera, update, dispose() { for (const m of Object.values(meshes)) m.dispose(); } };
}

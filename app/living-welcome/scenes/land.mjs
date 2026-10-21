import { THREE, HALF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, smooth, window01, lerp, clamp } from './kit.mjs';
import { SCENE_CATALOG } from './catalog.mjs';
// Land records & the public land survey: township and range lines draw out
// from an initial point, one township splits into its 36 sections, then the
// grid settles into dashed reference lines with a few case markers. Survey
// geometry only: no filled parcels, nothing that reads as ownership.

const T = SCENE_CATALOG.land.duration;
const S = 1.5; // township spacing (the six-mile grid at diorama scale)
const IPT = [-3, 1.5]; // initial point: principal meridian x = -3, baseline z = 1.5
const TOWNSHIP = [0, -1.5, 1.5, 0]; // the township that subdivides (minX, minZ, maxX, maxZ)
const LAG = .55; // each line starts this much later per township step from the axes
const CASES = [[-1.625, -.875], [2.375, -2.375], [-4.125, 3.375], [3.625, 2.875], [.375, -3.875]]; // section centres

// Lines are drawn in the terrain's own fragment shader, so they drape exactly
// with no z-fighting and cost nothing per frame beyond a few uniforms.
const HEAD = `
 uniform vec2 ipt; uniform vec4 tBox; uniform vec4 marks[5];
 uniform float gFront, gLag, gAlpha, gDash, gFocus, sFront, sAlpha, sCell, sHi, mAlpha;
 uniform vec3 cGold, cCase;
 float kLine(float d, float w, float aa) { return 1.0 - smoothstep(w, w + aa * 1.5, d); }
 float kDash(float s) { float f = fract(s); return smoothstep(0.0, 0.05, f) * (1.0 - smoothstep(0.55, 0.6, f)); }`;
const BODY = `
 vec2 aa = max(fwidth(vXZ), vec2(1e-4));
 vec2 rel = vXZ - ipt;
 vec2 idx = floor(rel / 1.5 + 0.5);
 vec2 dd = abs(rel - idx * 1.5);
 // Range lines (constant x) grow from the baseline, township lines (constant z) from the meridian.
 float fR = gFront - abs(idx.x) * gLag, fT = gFront - abs(idx.y) * gLag;
 float vR = 1.0 - smoothstep(fR - 0.08, fR, abs(rel.y));
 float vT = 1.0 - smoothstep(fT - 0.08, fT, abs(rel.x));
 float tipR = smoothstep(fR - 0.8, fR, abs(rel.y)), tipT = smoothstep(fT - 0.8, fT, abs(rel.x));
 float axR = 1.0 - step(0.5, abs(idx.x)), axT = 1.0 - step(0.5, abs(idx.y));
 float w = mix(0.016, 0.01, gDash);
 float lR = kLine(dd.x, w + axR * 0.012, aa.x) * vR * mix(1.0, kDash(rel.y / 0.2), gDash);
 float lT = kLine(dd.y, w + axT * 0.012, aa.y) * vT * mix(1.0, kDash(rel.x / 0.2), gDash);
 float haloR = exp(-dd.x * dd.x / 0.005) * vR, haloT = exp(-dd.y * dd.y / 0.005) * vT;
 vec2 tl = (vXZ - tBox.xy) / (tBox.zw - tBox.xy);
 float edgeOut = max(max(-tl.x, tl.x - 1.0), max(-tl.y, tl.y - 1.0));
 float kIn = 1.0 - step(0.0, edgeOut);
 float kNear = 1.0 - smoothstep(0.0, 0.03, edgeOut);
 float focus = mix(1.0, mix(0.3, 1.7, kNear), gFocus);
 float tip = max(tipR * (lR + haloR * 0.6), tipT * (lT + haloT * 0.6));
 glow += cGold * gAlpha * focus * (min(1.0, lR + lT) * (1.0 + (axR + axT) * 0.6) + (haloR + haloT) * mix(0.22, 0.08, gDash) + tip * 2.2 * (1.0 - gDash));
 // Sections: interior lines draw north→south and east→west; a light walks the
 // serpentine section order (1 at the north-east corner) and rests on one.
 vec2 sc = clamp(tl, 0.0, 1.0) * 6.0;
 vec2 si = floor(sc + 0.5);
 vec2 sd = abs(sc - si) * 0.25;
 float onX = step(0.5, si.x) * step(si.x, 5.5), onY = step(0.5, si.y) * step(si.y, 5.5);
 float fx = sFront * 1.8 - si.x * 0.16, fy = sFront * 1.8 - si.y * 0.16;
 float rNS = 1.0 - smoothstep(fx - 0.03, fx, tl.y);
 float rEW = 1.0 - smoothstep(fy - 0.03, fy, 1.0 - tl.x);
 float secs = (kLine(sd.x, 0.008, aa.x) * onX * rNS + kLine(sd.y, 0.008, aa.y) * onY * rEW) * kIn;
 vec2 cell = min(floor(sc), vec2(5.0));
 float n = cell.y * 6.0 + (mod(cell.y, 2.0) < 0.5 ? 5.0 - cell.x : cell.x);
 float lit = kIn * sHi * (1.0 - smoothstep(0.0, 1.0, abs(n - sCell)));
 vec2 cf = abs(fract(sc) - 0.5) * 2.0;
 float rim = smoothstep(0.8, 1.0, max(cf.x, cf.y));
 glow += cGold * (secs * sAlpha * 1.1 + lit * (0.14 + 0.75 * rim));
 // Case markers reference a section: a pulse ring and a hairline section square, never a fill.
 for (int i = 0; i < 5; i++) {
  vec4 m = marks[i];
  vec2 q = abs(vXZ - m.xy);
  float d = length(vXZ - m.xy);
  glow += cCase * (kLine(abs(d - m.z), 0.012, aa.x) * m.w + kLine(abs(max(q.x, q.y) - 0.125), 0.006, aa.x) * mAlpha * 0.8);
 }`;

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

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022 });
 const land = terrain({ segments: 256 });
 const u = liveSurface(land);
 u.tint.value.set('#0b2830');
 scene.add(land.mesh, blockSides(land.sample), riverWater(land.sample));

 const marks = CASES.map(([x, z]) => new THREE.Vector4(x, z, 0, 0));
 const g = {
  ipt: { value: new THREE.Vector2(...IPT) }, tBox: { value: new THREE.Vector4(...TOWNSHIP) }, marks: { value: marks },
  gFront: { value: 0 }, gLag: { value: LAG }, gAlpha: { value: 0 }, gDash: { value: 0 }, gFocus: { value: 0 },
  sFront: { value: 0 }, sAlpha: { value: 0 }, sCell: { value: 0 }, sHi: { value: 0 }, mAlpha: { value: 0 },
  cGold: { value: new THREE.Color('#ecbf68') }, cCase: { value: new THREE.Color('#8fd6ee') },
 };
 overlay(land.mesh.material, g, HEAD, BODY, 'kfm-land-plss');

 // Glow: pen heads at each drawing front, corner monuments, case cores and the initial point.
 const ranges = [], towns = [];
 for (let k = -2; k <= 6; k++) ranges.push(k); // x = -6 … 6
 for (let k = -5; k <= 3; k++) towns.push(k); // z = -6 … 6
 const corners = [];
 for (let i = -3; i <= 3; i++) for (let j = -3; j <= 3; j++) {
  const x = i * S, z = j * S;
  corners.push({ x, z, y: land.sample(x, z) + .05, kx: Math.abs((x - IPT[0]) / S), kz: Math.abs((z - IPT[1]) / S) });
 }
 const heads = (ranges.length + towns.length) * 2, C0 = heads, K0 = C0 + corners.length, P0 = K0 + CASES.length;
 const glow = glowPoints(P0 + 1, { size: .3, color: '#fff0c8' });
 const tint = (i, hex) => { const c = new THREE.Color(hex); glow.colors.set([c.r, c.g, c.b], i * 3); };
 corners.forEach((c, i) => { glow.positions.set([c.x, c.y, c.z], (C0 + i) * 3); tint(C0 + i, '#f3d38e'); });
 CASES.forEach(([x, z], i) => { glow.positions.set([x, land.sample(x, z) + .07, z], (K0 + i) * 3); tint(K0 + i, '#8fd6ee'); glow.sizes[K0 + i] = .42; });
 glow.positions.set([IPT[0], land.sample(...IPT) + .08, IPT[1]], P0 * 3); tint(P0, '#ffe6a8');
 scene.add(glow);

 function head(i, x, z, front) {
  const inside = 1 - smooth(HALF - .4, HALF + .05, Math.max(Math.abs(x), Math.abs(z)));
  const a = smooth(0, .3, front) * inside * (1 - g.gDash.value) * g.gAlpha.value;
  glow.alphas[i] = a;
  if (a > .001) glow.positions.set([x, land.sample(clamp(x, -HALF, HALF), clamp(z, -HALF, HALF)) + .06, z], i * 3);
 }

 function update(t) {
  const out = 1 - smooth(14.8, 15.8, t); // everything resolves back to bare land for the loop

  // Beat 1 (0–5.5 s): meridian and baseline first, then each line in turn, outward.
  g.gFront.value = lerp(0, 12.2, smooth(.3, 5.3, t));
  g.gAlpha.value = smooth(0, .4, t) * out;
  g.gDash.value = smooth(11, 12.2, t);
  u.tintMix.value = .3 * g.gAlpha.value;
  let i = 0;
  for (const k of ranges) { const f = g.gFront.value - Math.abs(k) * LAG, x = IPT[0] + k * S; head(i++, x, IPT[1] + f, f); head(i++, x, IPT[1] - f, f); }
  for (const k of towns) { const f = g.gFront.value - Math.abs(k) * LAG, z = IPT[1] + k * S; head(i++, IPT[0] + f, z, f); head(i++, IPT[0] - f, z, f); }

  // Beat 2 (5.5–11 s): focus one township; its 36 sections draw, then a light walks their order.
  g.gFocus.value = window01(t, 5.5, 11.4, .8);
  g.sFront.value = smooth(6.1, 8.3, t);
  g.sAlpha.value = smooth(5.9, 6.4, t) * out * lerp(1, .55, smooth(11, 12, t));
  g.sCell.value = 15 * smooth(7.7, 9.5, t);
  g.sHi.value = window01(t, 7.5, 11, .5);

  // Beat 3 (11–16 s): lines thin to dashed references, monuments mark corners, cases pulse.
  const ref = smooth(11.2, 12.4, t) * out;
  corners.forEach((c, j) => {
   const reach = Math.min(g.gFront.value - c.kx * LAG - Math.abs(c.z - IPT[1]), g.gFront.value - c.kz * LAG - Math.abs(c.x - IPT[0]));
   glow.alphas[C0 + j] = smooth(0, .5, reach) * g.gAlpha.value * (.35 + .55 * ref * (.75 + .25 * Math.sin(t * 2.4 + j)));
   glow.sizes[C0 + j] = .2 + .12 * ref;
  });
  g.mAlpha.value = smooth(11.6, 12.4, t) * out;
  CASES.forEach((_, j) => {
   const start = 11.8 + j * .35, ph = Math.max(0, t - start) / 1.6, p = ph % 1, on = smooth(start, start + .3, t) * out;
   marks[j].z = .04 + .5 * p; marks[j].w = (1 - p) * on * .9;
   glow.alphas[K0 + j] = on * (.65 + .35 * Math.sin(t * 3 + j * 1.7));
  });
  glow.alphas[P0] = g.gAlpha.value * (.55 + .9 * Math.exp(-Math.pow((t - .6) / .5, 2)));
  glow.sizes[P0] = .45 + .5 * Math.exp(-Math.pow((t - .6) / .6, 2));
  glow.commit();

  // Out-and-back drift keeps the loop seamless; lean in toward the township in beat 2.
  const lean = window01(t, 5.2, 11.6, 1.6);
  orbit(camera, 4.5 * (1 - Math.cos(t / T * Math.PI * 2)), {
   radius: lerp(21.5, 18.5, lean), height: lerp(10.5, 9, lean), target: [.35 * lean, -.6, -.35 * lean], start: -.95, speed: .045,
  });
 }
 update(0);
 return { scene, camera, update, dispose() {} };
}

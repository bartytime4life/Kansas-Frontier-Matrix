import { THREE, HALF, WORLD, RELIEF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, smooth, window01, lerp, clamp, rng } from './kit.mjs';
// Weather: radar reflectivity cells drift west → east as a stack of glowing
// slices (taller where echoes are stronger), wind streamlines trace the flow
// aloft, then lightning strikes out of the strongest cells.

const SEGMENTS = 200, LAYERS = 12, BASE = 2.15, GAP = .09, SPEED = .375; // cells and their texture drift at SPEED (world units / s)
const v3 = hex => { const c = new THREE.Color(hex); return `vec3(${c.r.toFixed(4)},${c.g.toFixed(4)},${c.b.toFixed(4)})`; };
// x0, z, radius, strength, life (s), phase. Lives divide the 16 s loop, so it repeats seamlessly.
const CELLS = [[-2.5, -2.4, 1.7, 1.2, 16, .15], [1.8, 1.8, 1.9, 1.25, 16, .6], [-3.8, 2.6, 1.3, .95, 8, .3], [3.3, -3.2, 1.4, 1.05, 8, .8], [.2, -.4, 1.2, .85, 16, .9], [-.8, 4.2, 1.1, .8, 8, .05], [4.2, 1.5, 1.3, .95, 16, .35], [-5, -.5, 1.2, .8, 16, .45]];
const SITE = [-1.1, -1.8];

/** Chain extra GLSL onto a liveSurface material (its own edits stay in place). */
function extendSurface(material, key, uniforms, { vDecl = '', vMain = '', fDecl = '', fColor = '', fEmissive = '' }) {
 const base = material.onBeforeCompile;
 material.onBeforeCompile = (shader, renderer) => {
  base?.(shader, renderer);
  Object.assign(shader.uniforms, uniforms);
  shader.vertexShader = shader.vertexShader.replace('#include <common>', `#include <common>\n${vDecl}`).replace('#include <begin_vertex>', `#include <begin_vertex>\n${vMain}`);
  shader.fragmentShader = shader.fragmentShader.replace('#include <common>', `#include <common>\n${fDecl}`)
   .replace('#include <alphamap_fragment>', `{\n${fColor}\n}\n#include <alphamap_fragment>`)
   .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>\n${fEmissive}`);
 };
 material.customProgramCacheKey = () => key;
}

function heightLookup(land, segments) {
 const n = segments + 1, step = WORLD / segments, b = land.base;
 return (x, z) => {
  const fx = clamp((x + HALF) / step, 0, segments - 1e-4), fz = clamp((z + HALF) / step, 0, segments - 1e-4);
  const i = Math.floor(fx), j = Math.floor(fz), u = fx - i, v = fz - j, k = j * n + i;
  return lerp(lerp(b[k], b[k + 1], u), lerp(b[k + n], b[k + n + 1], u), v) * RELIEF;
 };
}

// Reflectivity: Gaussian cells broken up by noise that advects with them. Two
// noise copies cross-fade every 8 s so the drift never needs to rewind.
const FIELD = `uniform vec4 uCells[${CELLS.length}]; uniform float uT, uSweep, uSweepA, uFlash; uniform vec2 uSite; uniform vec3 uFlashPos;
 float wHash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
 float wNoise(vec2 p) { vec2 i = floor(p), f = fract(p); f = f * f * (3. - 2. * f);
  return mix(mix(wHash(i), wHash(i + vec2(1., 0.)), f.x), mix(wHash(i + vec2(0., 1.)), wHash(i + vec2(1., 1.)), f.x), f.y); }
 float wFbm(vec2 p) { float s = 0., a = .5; for (int i = 0; i < 3; i++) { s += a * wNoise(p); p = p * 2.03 + 7.1; a *= .5; } return s; }
 float wRefl(vec2 p) {
  float r = 0.;
  for (int i = 0; i < ${CELLS.length}; i++) { vec2 d = (p - uCells[i].xy) / (uCells[i].z * 1.15); d.y *= 1.2; r += uCells[i].w * exp(-dot(d, d)); }
  float ph = fract(uT / 8.), w = abs(1. - 2. * ph);
  vec2 drift = vec2(${SPEED}, .03) * 8. * 1.3;
  float n = mix(wFbm(p * 1.3 - drift * ph), wFbm(p * 1.3 - drift * fract(ph + .5) + 5.2), w);
  return r * (.25 + 1.75 * n);
 }
 vec3 wRamp(float v) {
  vec3 c = mix(${v3('#1f9a52')}, ${v3('#52dc66')}, smoothstep(.12, .38, v));
  c = mix(c, ${v3('#f2d84a')}, smoothstep(.4, .62, v));
  c = mix(c, ${v3('#f28a36')}, smoothstep(.62, .8, v));
  return mix(c, ${v3('#e8363c')}, smoothstep(.8, 1.02, v));
 }
 float wSweepGlow(vec2 p) { vec2 q = p - uSite; float lag = mod(uSweepA - atan(q.y, q.x), 6.2832); return exp(-lag * 2.4) * .6 + exp(-lag * 60.) * .8; }`;

class Polyline extends THREE.Curve {
 constructor(points) { super(); this.points = points; }
 getPoint(u, target = new THREE.Vector3()) {
  const p = this.points, f = u * (p.length - 1), i = Math.min(p.length - 2, Math.floor(f));
  return target.lerpVectors(p[i], p[i + 1], f - i);
 }
}
/** A forked bolt from y = 1 (cloud base) to y = 0 (ground), scaled into place later. */
function bolt(random) {
 const group = new THREE.Group(), core = new THREE.MeshBasicMaterial({ color: '#f6f2ff', transparent: true, blending: THREE.AdditiveBlending, depthWrite: false });
 const halo = new THREE.MeshBasicMaterial({ color: '#9d86ff', transparent: true, blending: THREE.AdditiveBlending, depthWrite: false });
 const strand = (points, r) => {
  const curve = new Polyline(points), segs = (points.length - 1) * 2;
  group.add(new THREE.Mesh(new THREE.TubeGeometry(curve, segs, r, 4), core), new THREE.Mesh(new THREE.TubeGeometry(curve, segs, r * 4.5, 5), halo));
 };
 const main = [];
 let x = 0, z = 0;
 for (let i = 0; i <= 16; i++) { main.push(new THREE.Vector3(x, 1 - i / 16, z)); x += (random() - .5) * .16; z += (random() - .5) * .16; }
 strand(main, .014);
 for (let b = 0; b < 3; b++) {
  const from = main[3 + Math.floor(random() * 8)], dir = random() * Math.PI * 2, pts = [from.clone()];
  for (let i = 1; i <= 5; i++) pts.push(new THREE.Vector3(from.x + Math.cos(dir) * i * .05 + (random() - .5) * .05, from.y - i * .045, from.z + Math.sin(dir) * i * .05 + (random() - .5) * .05));
  strand(pts, .008);
 }
 group.userData = { core, halo };
 group.visible = false;
 return group;
}
// A strike's brightness d seconds after it begins: a sharp flash, flicker and one restrike.
const flashAt = d => d < 0 || d > .6 ? 0 : clamp(Math.exp(-d * 7) * (.55 + .45 * Math.cos(d * 95)) + .8 * Math.exp(-Math.pow((d - .2) / .04, 2)));

function cellState(c, t, out) {
 const [x0, z, r, strength, life, phase] = c, age = (t / life + phase) % 1;
 out.set(x0 + (age - .5) * life * SPEED, z, r, strength * Math.pow(Math.sin(Math.PI * age), 1.3));
 return out;
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 const { key, hemi } = stage(scene, { fog: .022, sunIntensity: 1.8 });
 const land = terrain({ segments: SEGMENTS });
 const u = liveSurface(land);
 u.grey.value = .3; u.tint.value.set('#3e5866'); u.tintMix.value = .14;
 const ground = heightLookup(land, SEGMENTS);
 scene.add(land.mesh, blockSides(land.sample), riverWater(land.sample));

 const wu = {
  uCells: { value: CELLS.map(() => new THREE.Vector4()) }, uT: { value: 0 }, uSweep: { value: 1 }, uSweepA: { value: 0 },
  uSite: { value: new THREE.Vector2(...SITE) }, uFlash: { value: 0 }, uFlashPos: { value: new THREE.Vector3() },
 };
 // The land under the storm: cell shadows, a faint echo footprint, radar range rings and beam.
 extendSurface(land.mesh.material, 'kfm-weather', wu, {
  vDecl: 'varying vec2 vXZ;', vMain: 'vXZ = position.xz;',
  fDecl: `${FIELD}\n varying vec2 vXZ; vec3 kEcho; float kRing, kBeam, kFl;`,
  fColor: `
   float v = wRefl(vXZ);
   kEcho = wRamp(v) * smoothstep(.15, .5, v);
   diffuseColor.rgb *= 1. - .42 * smoothstep(.2, .9, v);
   float r = length(vXZ - uSite), rr = r / 1.8;
   kRing = (1. - smoothstep(0., fwidth(rr) * 1.4, abs(fract(rr + .5) - .5))) * step(r, 5.6) * step(.5, r);
   kBeam = wSweepGlow(vXZ) * step(r, 5.6);
   kFl = uFlash * exp(-dot(vXZ - uFlashPos.xz, vXZ - uFlashPos.xz) / .7);`,
  fEmissive: `totalEmissiveRadiance += kEcho * .07 + ${v3('#7fd3ea')} * (kRing * .3 + kBeam * .2) * uSweep + ${v3('#cfc4ff')} * kFl * .45;`,
 });

 // Radar reflectivity as stacked slices: each higher slice needs a stronger echo.
 const layerGeo = new THREE.PlaneGeometry(WORLD + .2, WORLD + .2).rotateX(-Math.PI / 2);
 for (let k = 0; k < LAYERS; k++) {
  const material = new THREE.ShaderMaterial({
   uniforms: { ...wu, uK: { value: k / (LAYERS - 1) } },
   vertexShader: 'varying vec2 vXZ; void main(){ vec4 w = modelMatrix * vec4(position, 1.); vXZ = w.xz; gl_Position = projectionMatrix * viewMatrix * w; }',
   fragmentShader: `${FIELD}\n uniform float uK; varying vec2 vXZ;
    void main() {
     float edge = smoothstep(6.05, 5.4, max(abs(vXZ.x), abs(vXZ.y)));
     float v = wRefl(vXZ), th = .14 + uK * .78;
     float a = smoothstep(th, th + .18, v) * edge;
     if (a < .004) discard;
     vec3 col = wRamp(v) * mix(1., .55 + .8 * wSweepGlow(vXZ), uSweep);
     col += ${v3('#d8d0ff')} * uFlash * exp(-dot(vXZ - uFlashPos.xz, vXZ - uFlashPos.xz) / 1.3) * 1.8;
     gl_FragColor = vec4(col, a * (.3 - uK * .19));
    }`,
   transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide,
  });
  const slice = new THREE.Mesh(k ? layerGeo.clone() : layerGeo, material);
  slice.position.y = BASE + k * GAP; slice.renderOrder = 3 + k;
  scene.add(slice);
 }

 // Radar site: a small domed tower on the ridge, with a beacon.
 const sx = SITE[0], sz = SITE[1], sy = ground(sx, sz);
 const mast = new THREE.Mesh(new THREE.CylinderGeometry(.025, .04, .3, 8), new THREE.MeshStandardMaterial({ color: '#cfd8dc', roughness: .5 }));
 const dome = new THREE.Mesh(new THREE.SphereGeometry(.085, 20, 14), new THREE.MeshStandardMaterial({ color: '#f1f4f2', roughness: .35, emissive: '#7fd3ea', emissiveIntensity: .25 }));
 mast.position.set(sx, sy + .15, sz); dome.position.set(sx, sy + .34, sz);
 const beacon = glowPoints(1, { size: .5, color: '#8fd6ee' });
 beacon.positions.set([sx, sy + .36, sz]); beacon.commit();
 scene.add(mast, dome, beacon);

 // Wind aloft: streamline particles with fading trails above the cells.
 const WIND = 240, TRAIL = 12, STEP = .13, random = rng(9);
 const lane = new Float32Array(WIND), alt = new Float32Array(WIND), ph = new Float32Array(WIND), vel = new Float32Array(WIND);
 for (let i = 0; i < WIND; i++) { lane[i] = lerp(-5.6, 5.6, random()); alt[i] = lerp(2.75, 3.3, random()); ph[i] = random(); vel[i] = lerp(.9, 1.6, random()); }
 const windGeo = new THREE.BufferGeometry();
 windGeo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(WIND * (TRAIL - 1) * 6), 3));
 windGeo.setAttribute('color', new THREE.BufferAttribute(new Float32Array(WIND * (TRAIL - 1) * 6), 3));
 const wind = new THREE.LineSegments(windGeo, new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false }));
 wind.frustumCulled = false;
 const heads = glowPoints(WIND, { size: .16, color: '#d6f3fb' });
 scene.add(wind, heads);
 const wc = new THREE.Color('#8fd6ee');
 const stream = (x, z0, y0, out) => { out[0] = x; out[1] = y0 + .08 * Math.sin(.6 * x + z0); out[2] = z0 + .55 * Math.sin(.36 * x + 1.2 + .25 * z0) + .15 * Math.sin(.9 * x + z0); return out; };
 const edgeFade = (x, z) => smooth(HALF + .2, HALF - .6, Math.abs(x)) * smooth(HALF + .2, HALF - .6, Math.abs(z));

 // Lightning: one bolt per strike, placed in whichever live cell is strongest then.
 const STRIKES = [11.4, 12.15, 12.4, 13.1, 13.75, 14.05, 14.7], cell = new THREE.Vector4();
 const strikes = STRIKES.map((at, i) => {
  let best = null, score = -1;
  CELLS.forEach(c => { cellState(c, at, cell); const s = cell.w * edgeFade(cell.x, cell.y) * (i % 2 ? .9 + random() * .2 : 1); if (s > score) { score = s; best = cell.clone(); } });
  const x = clamp(best.x + (random() - .5) * best.z * .6, -HALF + .5, HALF - .5), z = clamp(best.y + (random() - .5) * best.z * .6, -HALF + .5, HALF - .5);
  const g = ground(x, z), mesh = bolt(random);
  mesh.position.set(x, g, z); mesh.scale.set(1, BASE - g, 1);
  scene.add(mesh);
  return { at, x, z, g, mesh };
 });
 const light = new THREE.PointLight('#cbbcff', 0, 0, 2);
 scene.add(light);
 const tmp = [0, 0, 0];

 function update(t) {
  wu.uT.value = t;
  CELLS.forEach((c, i) => cellState(c, t, wu.uCells.value[i]));

  // Beat 1 (0–5.5 s): the radar sweep paints the echoes; rings fade once the map is up.
  wu.uSweepA.value = t * Math.PI * 2 / 4;
  wu.uSweep.value = 1 - smooth(5, 6.5, t) + smooth(14.6, 16, t);

  // Beat 2 (5.5–11 s): streamlines flow west → east aloft, bending around the cells.
  const flowVis = window01(t, 5.2, 11.8, 1);
  wind.visible = heads.visible = flowVis > .01;
  if (wind.visible) {
   const p = windGeo.attributes.position.array, col = windGeo.attributes.color.array;
   let o = 0;
   for (let i = 0; i < WIND; i++) {
    const head = -HALF - 1.5 + (HALF * 2 + 3) * ((ph[i] + t * vel[i] / (WORLD + 3)) % 1);
    stream(head, lane[i], alt[i], tmp);
    heads.positions.set(tmp, i * 3);
    heads.alphas[i] = flowVis * edgeFade(tmp[0], tmp[2]) * .8;
    for (let j = 0; j < TRAIL - 1; j++) {
     const a0 = flowVis * Math.pow(1 - j / TRAIL, 1.6), a1 = flowVis * Math.pow(1 - (j + 1) / TRAIL, 1.6);
     stream(head - j * STEP, lane[i], alt[i], tmp);
     const f0 = a0 * edgeFade(tmp[0], tmp[2]) * .8;
     p[o] = tmp[0]; p[o + 1] = tmp[1]; p[o + 2] = tmp[2]; col[o] = wc.r * f0; col[o + 1] = wc.g * f0; col[o + 2] = wc.b * f0;
     stream(head - (j + 1) * STEP, lane[i], alt[i], tmp);
     const f1 = a1 * edgeFade(tmp[0], tmp[2]) * .8;
     p[o + 3] = tmp[0]; p[o + 4] = tmp[1]; p[o + 5] = tmp[2]; col[o + 3] = wc.r * f1; col[o + 4] = wc.g * f1; col[o + 5] = wc.b * f1;
     o += 6;
    }
   }
   windGeo.attributes.position.needsUpdate = windGeo.attributes.color.needsUpdate = true;
   heads.commit();
  }

  // Beat 3 (11–16 s): strikes flash from the strongest cells and light the land.
  let peak = 0, at = null;
  for (const s of strikes) {
   const f = flashAt(t - s.at);
   s.mesh.visible = f > .04;
   if (s.mesh.visible) { s.mesh.userData.core.opacity = f; s.mesh.userData.halo.opacity = f * .4; }
   if (f > peak) { peak = f; at = s; }
  }
  wu.uFlash.value = peak;
  if (at) { wu.uFlashPos.value.set(at.x, at.g, at.z); light.position.set(at.x, at.g + .9, at.z); }
  light.intensity = peak * 9;
  hemi.intensity = .9 + peak * .5;
  key.intensity = 1.8 - .25 * smooth(10.6, 11.6, t) * (1 - smooth(15, 16, t));

  orbit(camera, t, { radius: 22, height: 10.6 - 1.2 * window01(t, 4.5, 16, 3.5), target: [0, -.3, 0], start: -.95 + .3 * Math.sin(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update };
}

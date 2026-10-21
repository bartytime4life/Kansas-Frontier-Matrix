import { THREE, HALF, WORLD, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, ribbon, surfacePath, mainRiver, smooth, window01, lerp, clamp, easeInOut, rng, noise2, fbm, riverZ, TRIBUTARIES, tributaryPoint } from './kit.mjs';
// Ecology: land-cover classes wipe across the block, riparian corridors light up
// along the river and its tributaries, then the vegetation signal runs from
// spring green through summer to autumn gold.

const SEGMENTS = 256, CELL = .5, GRID = Math.round(WORLD / CELL);
const v3 = hex => { const c = new THREE.Color(hex); return `vec3(${c.r.toFixed(4)},${c.g.toFixed(4)},${c.b.toFixed(4)})`; };
// Spring → summer → autumn for each vegetated class.
const SEASON = { grass: ['#a6d46c', '#6f9c48', '#d9b45a'], crop: ['#86d45a', '#4e9a3c', '#e3b44c'], rip: ['#7fcf6a', '#2f7f43', '#d27a32'], wet: ['#62c3a0', '#3d9c8c', '#9a9a62'] };

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

function tributaryDistance(x, z) {
 let best = 99, reach = 0;
 for (const trib of TRIBUTARIES) {
  if (trib.side * (z - riverZ(x)) < 0) continue;
  const s = clamp(1 - Math.abs(z - riverZ(trib.x0)) / (HALF + .4)), [tx] = tributaryPoint(trib, s), d = Math.abs(x - tx);
  if (d < best) { best = d; reach = s; }
 }
 return [best, reach];
}

// Where each class sits: wetlands and towns along the river, cropland on the flats.
const WETLANDS = [[-4.3, .45, .5], [-1.5, -.5, .42], [1.2, .55, .46], [3.7, -.45, .5]];
const TOWNS = [[-2.4, .85, .5], [2.9, -.9, .58]];

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 const { key } = stage(scene, { fog: .022 });
 const land = terrain({ segments: SEGMENTS });
 liveSurface(land);
 scene.add(land.mesh, blockSides(land.sample), riverWater(land.sample));

 // Per-vertex class scores (riparian, wetland, developed, texture noise).
 const pos = land.geometry.attributes.position, cls = new Float32Array(pos.count * 4), n = noise2(57);
 for (let i = 0; i < pos.count; i++) {
  const x = pos.getX(i), z = pos.getZ(i), d = z - riverZ(x), grain = n(x * 2.6, z * 2.6), [td, reach] = tributaryDistance(x, z);
  let rip = Math.exp(-d * d / .34) + .2 * grain;
  rip = Math.max(rip, Math.exp(-td * td / .045) * smooth(.05, .3, reach) + .15 * grain);
  let wet = 0, dev = -1;
  for (const [wx, wd, r] of WETLANDS) { const dx = (x - wx) / (r * 1.6), dz = (z - riverZ(wx) - wd) / r; wet = Math.max(wet, Math.exp(-(dx * dx + dz * dz)) * (1 + .5 * grain)); }
  for (const [tx, tdz, r] of TOWNS) { const dx = Math.abs(x - tx), dz = Math.abs(z - riverZ(tx) - tdz); dev = Math.max(dev, 1 - Math.pow(Math.pow(dx, 4) + Math.pow(dz, 4), .25) / r + .12 * grain); }
  cls.set([rip, wet * 1.25, dev + .5, .5 + .5 * grain], i * 4);
 }
 land.geometry.setAttribute('aCls', new THREE.BufferAttribute(cls, 4));

 // Cropland as rectangular fields on the flatter ground; grassland elsewhere.
 const random = rng(23), crops = new Uint8Array(GRID * GRID * 4), cn = noise2(19);
 for (let j = 0; j < GRID; j++) for (let i = 0; i < GRID; i++) {
  const cx = -HALF + (i + .5) * CELL, cz = -HALF + (j + .5) * CELL, uu = cx / HALF, vv = cz / HALF;
  const hills = Math.exp(-Math.pow(uu - .38 + .12 * Math.sin(vv * 3.2), 2) / .02);
  const flat = Math.abs(land.sample(cx + .2, cz) - land.sample(cx - .2, cz)) + Math.abs(land.sample(cx, cz + .2) - land.sample(cx, cz - .2));
  const crop = fbm(cn, cx * .35, cz * .35, 3) + .25 - hills * .9 - flat * 1.4 > 0;
  crops.set([crop ? 255 : 0, Math.floor(random() * 255), 0, 255], (j * GRID + i) * 4);
 }
 const cropTex = new THREE.DataTexture(crops, GRID, GRID, THREE.RGBAFormat);
 cropTex.magFilter = cropTex.minFilter = THREE.NearestFilter; cropTex.needsUpdate = true;

 const eu = { uCrop: { value: cropTex }, uWipe: { value: -9 }, uWipeGlow: { value: 0 }, uCover: { value: 0 }, uRip: { value: 0 }, uVeg: { value: 0 }, uSeason: { value: 0 } };
 const season = k => `kSeason(${v3(SEASON[k][0])}, ${v3(SEASON[k][1])}, ${v3(SEASON[k][2])}, uSeason)`;
 extendSurface(land.mesh.material, 'kfm-ecology', eu, {
  vDecl: 'attribute vec4 aCls; varying vec4 vCls; varying vec2 vXZ;',
  vMain: 'vCls = aCls; vXZ = position.xz;',
  fDecl: `uniform sampler2D uCrop; uniform float uWipe, uWipeGlow, uCover, uRip, uVeg, uSeason;
   varying vec4 vCls; varying vec2 vXZ; float kEdge, kRipW;
   vec3 kSeason(vec3 a, vec3 b, vec3 c, float s) { return s < .5 ? mix(a, b, smoothstep(0., .5, s)) : mix(b, c, smoothstep(.5, 1., s)); }`,
  fColor: `
   vec3 nat = diffuseColor.rgb;
   float wDev = smoothstep(.47, .53, vCls.z);
   float wWet = smoothstep(.45, .55, vCls.y) * (1. - wDev);
   float wRip = smoothstep(.45, .55, vCls.x) * (1. - wDev) * (1. - wWet);
   vec2 g = (vXZ + ${HALF.toFixed(2)}) / ${CELL.toFixed(2)}, ci = floor(g), f = fract(g);
   vec4 cc = texture2D(uCrop, (ci + .5) / ${GRID.toFixed(1)});
   float wCrop = step(.5, cc.r) * (1. - wDev) * (1. - wWet) * (1. - wRip);
   float wGrass = max(0., 1. - wDev - wWet - wRip - wCrop);
   float tex = vCls.w;
   // Categorical land-cover colours, each with a little texture of its own.
   float e = min(min(f.x, 1. - f.x), min(f.y, 1. - f.y)) * ${CELL.toFixed(2)};
   float edge = 1. - smoothstep(.008, .014 + fwidth(e), e);
   vec2 st = abs(fract(vXZ * 5.5) - .5);
   float street = 1. - smoothstep(.04, .07 + fwidth(vXZ.x * 5.5), min(st.x, st.y));
   vec3 grassC = ${v3('#93b062')} * (.86 + .28 * tex);
   vec3 cropC = mix(${v3('#e6b452')}, ${v3('#cf8f45')}, cc.g) * (1. - .25 * edge);
   vec3 ripC = ${v3('#236b45')} * (.75 + .5 * tex);
   vec3 wetC = ${v3('#33a7b8')} * (.9 + .2 * tex);
   vec3 devC = mix(${v3('#c48a82')}, ${v3('#ecd2c2')}, street);
   vec3 classC = grassC * wGrass + cropC * wCrop + ripC * wRip + wetC * wWet + devC * wDev;
   // Seasonal vegetation signal replaces the class colours on vegetated ground.
   vec3 vegC = ${season('grass')} * (.86 + .28 * tex) * wGrass + ${season('crop')} * (.9 + .2 * cc.g) * (1. - .2 * edge) * wCrop
    + ${season('rip')} * (.75 + .5 * tex) * wRip + ${season('wet')} * wWet + devC * wDev;
   classC = mix(classC, vegC, uVeg);
   float fw = vXZ.x * .82 + vXZ.y * .42 + (tex - .5) * .9;
   float rev = 1. - smoothstep(uWipe - .7, uWipe, fw);
   kEdge = exp(-pow((fw - uWipe + .25) / .22, 2.)) * uWipeGlow;
   kRipW = (wRip + wWet * .7) * rev * uCover;
   diffuseColor.rgb = mix(nat, classC, rev * uCover);`,
  fEmissive: `totalEmissiveRadiance += ${v3('#8fd6ee')} * kEdge * .5 + ${v3('#6fe08a')} * kRipW * uRip * .14;`,
 });

 // Riparian corridors: thin glowing cores plus soft points drifting downstream.
 const paths = [surfacePath(mainRiver, land.sample, 220, .06), ...TRIBUTARIES.map(trib => surfacePath(s => tributaryPoint(trib, s), land.sample, 120, .06))];
 const lengths = paths.map(p => p.reduce((sum, q, i) => i ? sum + q.distanceTo(p[i - 1]) : 0, 0));
 const cores = paths.map(p => ribbon(p, { width: .05, color: '#bff5d2', additive: true, lift: .03 }));
 const halos = paths.map(p => ribbon(p, { width: .26, color: '#5fd49a', additive: true, opacity: .3, lift: .025 }));
 scene.add(...halos, ...cores);
 const reveals = [[5.6, 8], [6.6, 8.8], [7, 9.2], [7.4, 9.6], [7.8, 10]];
 const FLOW = 1500, flow = glowPoints(FLOW, { size: .22, color: '#86e8b4' }), random2 = rng(5);
 const total = lengths.reduce((a, b) => a + b, 0), fPath = new Uint8Array(FLOW), fPh = new Float32Array(FLOW), fOff = new Float32Array(FLOW * 2);
 for (let i = 0; i < FLOW; i++) {
  let r = random2() * total, k = 0;
  while (k < lengths.length - 1 && r > lengths[k]) { r -= lengths[k]; k++; }
  fPath[i] = k; fPh[i] = random2(); fOff[i * 2] = (random2() - .5) * (k ? .16 : .3); fOff[i * 2 + 1] = (random2() - .5) * (k ? .16 : .3);
  flow.sizes[i] = .16 + random2() * .26;
 }
 scene.add(flow);
 const at = (path, s, out) => { const f = s * (path.length - 1), i = Math.min(path.length - 2, Math.floor(f)); return out.lerpVectors(path[i], path[i + 1], f - i); };
 const tmp = new THREE.Vector3(), warm = new THREE.Color('#ffd9a8'), cool = new THREE.Color('#ffe2b8');

 function update(t) {
  // Beat 1 (0–5.5 s): a soft diagonal wipe paints the land-cover classes in.
  eu.uWipe.value = lerp(-8.6, 8.8, smooth(.3, 5.2, t));
  eu.uWipeGlow.value = window01(t, .3, 5.5, .5);
  eu.uCover.value = 1 - smooth(15, 16, t);

  // Beat 2 (5.5–11 s): corridors trace the river, then each tributary toward it.
  const glow = window01(t, 5.5, 16, 1) * (1 - .45 * smooth(11, 12.2, t));
  eu.uRip.value = glow;
  const shown = reveals.map(([a, b]) => easeInOut(smooth(a, b, t)));
  paths.forEach((_, k) => {
   cores[k].reveal(shown[k]); halos[k].reveal(shown[k]);
   cores[k].material.opacity = glow * .95; halos[k].material.opacity = glow * .3;
   cores[k].visible = halos[k].visible = glow > .01 && shown[k] > 0;
  });
  flow.visible = glow > .01;
  if (flow.visible) {
   for (let i = 0; i < FLOW; i++) {
    const k = fPath[i], s = (fPh[i] + t * .45 / lengths[k]) % 1;
    at(paths[k], s, tmp);
    flow.positions.set([tmp.x + fOff[i * 2], tmp.y + .05, tmp.z + fOff[i * 2 + 1]], i * 3);
    flow.alphas[i] = glow * (s < shown[k] ? 1 : 0) * (.5 + .3 * Math.sin(t * 3 + i));
   }
   flow.commit();
  }

  // Beat 3 (11–16 s): spring green → summer → autumn gold across the vegetation.
  eu.uVeg.value = smooth(10.8, 12, t) * (1 - smooth(15, 16, t));
  const s = smooth(11.6, 15, t);
  eu.uSeason.value = s;
  key.color.copy(cool).lerp(warm, s * eu.uVeg.value);

  orbit(camera, t, { radius: 21.5, height: 10.8 - 1.4 * window01(t, 4.5, 16, 3.5), target: [0, -.7, 0], start: -.95 + .3 * Math.sin(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update, dispose() { cropTex.dispose(); } };
}

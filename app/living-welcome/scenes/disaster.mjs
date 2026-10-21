import { THREE, HALF, WORLD, RELIEF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, glowTexture, POINT_SCALE, ribbon, surfacePath, smooth, window01, lerp, clamp, easeInOut, rng, noise2, riverZ } from './kit.mjs';
// Disaster: flood water rises through the river valley, fire detections spread
// across the uplands with smoke drifting downwind, then declared areas outline
// the counties the flood and fire touched.

const SEGMENTS = 256, FLOOD = .52;
const v3 = hex => { const c = new THREE.Color(hex); return `vec3(${c.r.toFixed(4)},${c.g.toFixed(4)},${c.b.toFixed(4)})`; };
const IGNITE = [1.25, -2.95], WIND = new THREE.Vector2(1, .32).normalize();

/** Chain extra GLSL onto a material, keeping whatever onBeforeCompile it already has. */
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

/** Normal-blended soft points (smoke): same layout as glowPoints, but they occlude. */
function softPoints(count) {
 const g = new THREE.BufferGeometry();
 for (const [k, n] of [['position', 3], ['color', 3], ['size', 1], ['alpha', 1]]) g.setAttribute(k, new THREE.BufferAttribute(new Float32Array(count * n), n));
 const material = new THREE.ShaderMaterial({
  uniforms: { map: { value: glowTexture() }, scale: POINT_SCALE },
  vertexShader: `attribute float size;attribute float alpha;attribute vec3 color;varying vec3 vColor;varying float vAlpha;uniform float scale;
   void main(){vColor=color;vAlpha=alpha;vec4 mv=modelViewMatrix*vec4(position,1.);gl_PointSize=size*scale/-mv.z;gl_Position=projectionMatrix*mv;}`,
  fragmentShader: `uniform sampler2D map;varying vec3 vColor;varying float vAlpha;
   void main(){float a=texture2D(map,gl_PointCoord).a*vAlpha;if(a<.004)discard;gl_FragColor=vec4(vColor,a);}`,
  transparent: true, depthWrite: false,
 });
 const points = new THREE.Points(g, material);
 points.frustumCulled = false;
 points.renderOrder = 4; // over the flood surface, under the glow points
 return points;
}

/** One mesh from many kit ribbons (the faint county grid), so it costs one draw call. */
function mergedRibbons(paths, options) {
 const positions = [], index = [];
 for (const path of paths) {
  const r = ribbon(path, options), off = positions.length / 3;
  positions.push(...r.geometry.attributes.position.array);
  for (const i of r.geometry.index.array) index.push(i + off);
  r.geometry.dispose(); r.material.dispose();
 }
 const geometry = new THREE.BufferGeometry();
 geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
 geometry.setIndex(index);
 const mesh = new THREE.Mesh(geometry, new THREE.MeshBasicMaterial({ color: options.color, transparent: true, opacity: 0, depthWrite: false, side: THREE.DoubleSide }));
 mesh.renderOrder = 2;
 return mesh;
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022 });
 const land = terrain({ segments: SEGMENTS });
 liveSurface(land);
 const ground = heightLookup(land, SEGMENTS);
 scene.add(land.mesh, blockSides(land.sample), riverWater(land.sample));

 // Fire spread: an ignition-time field stretched downwind (1 = edge of the burn).
 const n = noise2(71), pos = land.geometry.attributes.position, ign = new Float32Array(pos.count), decl = new Float32Array(pos.count);
 const ignition = (x, z) => {
  const qx = x - IGNITE[0], qz = z - IGNITE[1], along = qx * WIND.x + qz * WIND.y, across = -qx * WIND.y + qz * WIND.x;
  return Math.hypot(along / (along > 0 ? 2.7 : .85), across / 1.2) + .22 * n(x * 1.6, z * 1.6);
 };
 for (let i = 0; i < pos.count; i++) ign[i] = ignition(pos.getX(i), pos.getZ(i));

 // Flood surface: a strip along the valley that slopes downstream with the bed.
 const NX = 150, ND = 40, SPAN = 2.6, bed = new Float32Array(NX + 1);
 for (let i = 0; i <= NX; i++) {
  const x = lerp(-HALF, HALF, i / NX);
  let sum = 0;
  for (let k = -2; k <= 2; k++) { const xs = clamp(x + k * .25, -HALF, HALF); sum += ground(xs, riverZ(xs)); }
  bed[i] = sum / 5;
  if (i) bed[i] = Math.min(bed[i], bed[i - 1]); // water never runs uphill
 }
 const wPos = [], wGround = [], wEdge = [], wIndex = [];
 for (let i = 0; i <= NX; i++) for (let j = 0; j <= ND; j++) {
  const x = lerp(-HALF, HALF, i / NX), d = lerp(-SPAN, SPAN, j / ND), z = clamp(riverZ(x) + d, -HALF, HALF);
  wPos.push(x, bed[i], z); wGround.push(ground(x, z)); wEdge.push(Math.abs(d) / SPAN);
  if (i < NX && j < ND) { const a = i * (ND + 1) + j, b = a + ND + 1; wIndex.push(a, a + 1, b, b, a + 1, b + 1); } // wound so normals face up
 }
 const waterGeo = new THREE.BufferGeometry();
 waterGeo.setAttribute('position', new THREE.Float32BufferAttribute(wPos, 3));
 waterGeo.setAttribute('aGround', new THREE.Float32BufferAttribute(wGround, 1));
 waterGeo.setAttribute('aEdge', new THREE.Float32BufferAttribute(wEdge, 1));
 waterGeo.setIndex(wIndex); waterGeo.computeVertexNormals();
 const wu = { uLevel: { value: 0 }, uT: { value: 0 } };
 const water = new THREE.Mesh(waterGeo, new THREE.MeshStandardMaterial({ color: '#2f7f9e', roughness: .14, metalness: .15, transparent: true, opacity: .88, depthWrite: false, emissive: '#0d3446', emissiveIntensity: .7 }));
 extendSurface(water.material, 'kfm-disaster-water', wu, {
  vDecl: 'attribute float aGround; attribute float aEdge; uniform float uLevel; varying float vDepth; varying float vEdge; varying vec2 vXZ;',
  vMain: 'transformed.y += uLevel; vDepth = transformed.y - aGround; vEdge = aEdge; vXZ = position.xz;',
  fDecl: 'uniform float uT; varying float vDepth; varying float vEdge; varying vec2 vXZ; float kShore, kFlow;',
  fColor: `
   if (vDepth < 0.) discard;
   kShore = 1. - smoothstep(0., .03 + fwidth(vDepth) * 1.5, vDepth);
   diffuseColor.rgb = mix(${v3('#5fb0c4')}, ${v3('#1b5878')}, smoothstep(.02, .4, vDepth));
   diffuseColor.a *= smoothstep(1., .82, vEdge);
   kFlow = pow(.5 + .5 * sin(vXZ.x * 7. - uT * 2.4 + sin(vXZ.y * 5. + vXZ.x) * 1.6), 6.) * smoothstep(.02, .2, vDepth);`,
  fEmissive: `totalEmissiveRadiance += ${v3('#8fd6ee')} * (kShore * .75 + kFlow * .05);`,
 });
 water.renderOrder = 1;
 scene.add(water);

 // Counties: a staggered grid of township-like rectangles. Those the flood or fire touched are declared.
 const random = rng(13), XS = [-6, -4, -2, 0, 2, 4, 6], counties = [];
 for (let c = 0; c < 6; c++) {
  const jog = (random() - .5) * .7, zs = [-6, -4 + jog, -2 + jog, jog, 2 + jog, 4 + jog, 6];
  for (let r = 0; r < 6; r++) counties.push({ x0: XS[c], x1: XS[c + 1], z0: zs[r], z1: zs[r + 1] });
 }
 const floodDepth = (x, z) => { const i = clamp(Math.round((x + HALF) / WORLD * NX), 0, NX); return Math.abs(z - riverZ(x)) < SPAN * .8 ? bed[i] + FLOOD - .06 - ground(x, z) : -1; };
 for (const k of counties) {
  let hits = 0;
  for (let a = 0; a < 12; a++) for (let b = 0; b < 12; b++) {
   const x = lerp(k.x0, k.x1, (a + .5) / 12), z = lerp(k.z0, k.z1, (b + .5) / 12);
   if (floodDepth(x, z) > .04 || ignition(x, z) < .95) hits++;
  }
  k.declared = hits >= 5;
 }
 const outline = (k, inset) => surfacePath(s => {
  const x0 = k.x0 + inset, x1 = k.x1 - inset, z0 = k.z0 + inset, z1 = k.z1 - inset, w = x1 - x0, h = z1 - z0, p = s * 2 * (w + h);
  return p < w ? [x0 + p, z0] : p < w + h ? [x1, z0 + p - w] : p < 2 * w + h ? [x1 - (p - w - h), z1] : [x0, z1 - (p - 2 * w - h)];
 }, land.sample, 200, .035);
 const grid = mergedRibbons(counties.map(k => outline(k, 0)), { width: .03, color: '#e8c37c' });
 const declared = counties.filter(k => k.declared).map(k => ribbon(outline(k, .09), { width: .075, color: '#f3d38e', additive: true, lift: .01 }));
 declared.forEach(m => { m.renderOrder = 3; });
 scene.add(grid, ...declared);
 for (let i = 0; i < pos.count; i++) {
  const x = pos.getX(i), z = pos.getZ(i);
  decl[i] = counties.some(k => k.declared && x > k.x0 + .09 && x < k.x1 - .09 && z > k.z0 + .09 && z < k.z1 - .09) ? 1 : 0;
 }
 land.geometry.setAttribute('aIgn', new THREE.BufferAttribute(ign, 1));
 land.geometry.setAttribute('aDecl', new THREE.BufferAttribute(decl, 1));

 const du = { uBurn: { value: 0 }, uFront: { value: 0 }, uScar: { value: 0 }, uFill: { value: 0 }, uT: wu.uT };
 extendSurface(land.mesh.material, 'kfm-disaster-land', du, {
  vDecl: 'attribute float aIgn; attribute float aDecl; varying float vIgn; varying float vDecl; varying vec2 vXZ;',
  vMain: 'vIgn = aIgn; vDecl = aDecl; vXZ = position.xz;',
  fDecl: 'uniform float uBurn, uFront, uScar, uFill, uT; varying float vIgn; varying float vDecl; varying vec2 vXZ; float kFire, kEmber;',
  fColor: `
   float burnt = (1. - smoothstep(uBurn - .14, uBurn - .02, vIgn)) * uScar;
   float flick = .65 + .35 * sin(uT * 13. + vXZ.x * 23. + vXZ.y * 17.) * sin(uT * 7.3 - vXZ.y * 31.);
   kFire = exp(-pow((vIgn - uBurn + .03) / .045, 2.)) * uFront * flick;
   kEmber = burnt * uFront * smoothstep(.2, 0., uBurn - vIgn) * .5;
   diffuseColor.rgb = mix(diffuseColor.rgb, ${v3('#2a211b')} * (.8 + .4 * fract(sin(dot(floor(vXZ * 40.), vec2(12.9898, 78.233))) * 43758.5453)), burnt * .82);
   diffuseColor.rgb = mix(diffuseColor.rgb, ${v3('#e8c37c')}, vDecl * uFill * .16);`,
  fEmissive: `totalEmissiveRadiance += ${v3('#ff7a2a')} * (kFire * 1.6 + kEmber * .35) + ${v3('#e8c37c')} * vDecl * uFill * .06;`,
 });

 // Fire detections: hotspots inside the burn that light when the front reaches them.
 const HOT = 80, hot = glowPoints(HOT, { size: .3, color: '#ffb14a' }), hotIgn = new Float32Array(HOT), hotFlick = new Float32Array(HOT);
 for (let i = 0; i < HOT;) {
  const x = IGNITE[0] + (random() - .3) * 5.4, z = IGNITE[1] + (random() - .5) * 3.4, v = ignition(x, z);
  if (v > .95 || Math.abs(x) > HALF - .2 || Math.abs(z) > HALF - .2) continue;
  hot.positions.set([x, ground(x, z) + .05, z], i * 3); hotIgn[i] = v; hotFlick[i] = random() * 50; i++;
 }
 scene.add(hot);
 const burnAt = t => smooth(5.6, 9.8, t), hotC = new THREE.Color('#fff0c0'), coolC = new THREE.Color('#ff6a26'), c = new THREE.Color();

 // Smoke: each puff belongs to a hotspot and only exists once that hotspot is burning.
 const SMOKE = 900, smoke = softPoints(SMOKE), sSrc = new Uint8Array(SMOKE), sPh = new Float32Array(SMOKE), sLife = new Float32Array(SMOKE), sJit = new Float32Array(SMOKE * 2);
 for (let i = 0; i < SMOKE; i++) {
  const a = Math.floor(random() * HOT), b = Math.floor(random() * HOT);
  sSrc[i] = hotIgn[a] < hotIgn[b] ? a : b; // favour early hotspots so the plume builds from the start
  sPh[i] = random(); sLife[i] = 3.8 + random() * 1.6; sJit[i * 2] = random() - .5; sJit[i * 2 + 1] = random();
 }
 scene.add(smoke);
 const sa = smoke.geometry.attributes, warmS = new THREE.Color('#d98a52'), greyS = new THREE.Color('#aeb3b7'), darkS = new THREE.Color('#7b8288');

 function update(t) {
  wu.uT.value = t;
  // Beat 1 (0–5.5 s): the flood surface rises through the valley; it recedes for the loop.
  wu.uLevel.value = -.06 + (FLOOD + .06) * easeInOut(smooth(.3, 5.2, t)) * (1 - smooth(14.2, 15.8, t));
  water.visible = wu.uLevel.value > -.05;

  // Beat 2 (5.5–11 s): the fire front spreads downwind; hotspots light, smoke streams off.
  const burn = burnAt(t), live = window01(t, 5.5, 13.6, .9);
  du.uBurn.value = burn; du.uFront.value = live;
  du.uScar.value = smooth(5.6, 6.6, t) * (1 - smooth(14.6, 15.9, t));
  for (let i = 0; i < HOT; i++) {
   const lit = smooth(hotIgn[i], hotIgn[i] + .04, burn), age = clamp((burn - hotIgn[i]) / .4);
   hot.alphas[i] = lit * live * (.65 + .35 * Math.sin(t * 9 + hotFlick[i]));
   hot.sizes[i] = lerp(.75, .38, age);
   c.copy(hotC).lerp(coolC, age); hot.colors.set([c.r, c.g, c.b], i * 3);
  }
  hot.commit();
  const fade = 1 - smooth(14.4, 15.8, t);
  for (let i = 0; i < SMOKE; i++) {
   const k = sSrc[i], life = sLife[i], a = (t / life + sPh[i]) % 1, born = t - a * life;
   const alive = born > 5.6 && born < 13.2 && burnAt(born) > hotIgn[k] ? 1 : 0;
   const x0 = hot.positions[k * 3], y0 = hot.positions[k * 3 + 1], z0 = hot.positions[k * 3 + 2], run = a * 3.4, side = sJit[i * 2] * a * 1.1;
   sa.position.array.set([x0 + WIND.x * run - WIND.y * side, y0 + .08 + 1.5 * Math.pow(a, .8) + .08 * Math.sin(t * 1.3 + i), z0 + WIND.y * run + WIND.x * side], i * 3);
   sa.size.array[i] = .45 + 1.9 * a * (.7 + .6 * sJit[i * 2 + 1]);
   sa.alpha.array[i] = alive * fade * .62 * Math.pow(1 - a, 1.2) * smooth(0, .08, a) * smooth(HALF + 1.5, HALF, Math.abs(x0 + WIND.x * run));
   c.copy(warmS).lerp(greyS, smooth(0, .35, a)).lerp(darkS, smooth(.4, 1, a) * .6);
   sa.color.array.set([c.r, c.g, c.b], i * 3);
  }
  for (const k of ['position', 'size', 'alpha', 'color']) sa[k].needsUpdate = true;

  // Beat 3 (11–16 s): the county grid appears, then declared counties outline in gold.
  grid.material.opacity = .28 * window01(t, 10.8, 15.9, .8);
  grid.visible = grid.material.opacity > .005;
  const shown = window01(t, 11, 15.9, .8);
  declared.forEach((m, i) => {
   m.reveal(easeInOut(smooth(11.3 + i * .22, 12.3 + i * .22, t)));
   m.material.opacity = shown * (.85 + .15 * Math.sin(t * 4 + i));
   m.visible = shown > .01;
  });
  du.uFill.value = smooth(12.4, 13.6, t) * (1 - smooth(15, 15.9, t));

  orbit(camera, t, { radius: 21.5, height: 10.8 - 1.4 * window01(t, 4.5, 16, 3.5), target: [0, -.7, 0], start: -.95 + .3 * Math.sin(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update };
}

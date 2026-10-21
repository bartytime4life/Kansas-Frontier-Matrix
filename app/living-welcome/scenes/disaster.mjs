import { THREE, HALF, WORLD, RELIEF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, glowTexture, POINT_SCALE, ribbon, surfacePath, smooth, window01, lerp, clamp, easeInOut, rng, noise2, riverZ } from './kit.mjs';
// Disaster: flood water rises through the river valley, fire detections spread
// across the uplands with smoke drifting downwind, a tornado drops from a
// rotating storm and tracks across the plains, then declared areas outline the
// counties the flood, fire and tornado touched.

const SEGMENTS = 256, FLOOD = .52, D = 20;
const v3 = hex => { const c = new THREE.Color(hex); return `vec3(${c.r.toFixed(4)},${c.g.toFixed(4)},${c.b.toFixed(4)})`; };
const f1 = v => v.toFixed(4);
const IGNITE = [1.25, -2.95], WIND = new THREE.Vector2(1, .32).normalize();

// Tornado path: SW → NE across the plains, with a gentle bow. The parent storm
// moves steadily over [STORM0, STORM1]; the funnel touches down and lifts inside it.
const TA = new THREE.Vector2(-4.6, 4.4), TB = new THREE.Vector2(1.4, -1.4), TLEN = TA.distanceTo(TB), TD = TB.clone().sub(TA).normalize(), TP = new THREE.Vector2(-TD.y, TD.x), BEND = .5;
const STORM0 = 9.4, STORM1 = 15, TOUCH = 10.95, LIFT = 14.45, CLOUD = 3.9;
const trackS = t => clamp((t - STORM0) / (STORM1 - STORM0));
const S0 = trackS(TOUCH), S1 = trackS(LIFT);
const trackAt = s => { const b = BEND * Math.sin(s * Math.PI); return [TA.x + TD.x * TLEN * s + TP.x * b, TA.y + TD.y * TLEN * s + TP.y * b]; };
/** Damage-swath half-width at path position s (0 outside the touched-down stretch); mirrored in GLSL. */
const swathW = s => .3 * (.75 + .25 * Math.sin(s * 23)) * smooth(S0, S0 + .05, s) * (1 - .6 * smooth(S1 - .06, S1, s)) * (s <= S1 ? 1 : 0);
const trackCoords = (x, z) => { const qx = x - TA.x, qz = z - TA.y, s = (qx * TD.x + qz * TD.y) / TLEN; return [s, qx * TP.x + qz * TP.y - BEND * Math.sin(s * Math.PI)]; };
const GLSL_TRACK = `
 vec2 tq = vXZ - vec2(${f1(TA.x)}, ${f1(TA.y)});
 float ts = dot(tq, vec2(${f1(TD.x)}, ${f1(TD.y)})) / ${f1(TLEN)};
 float tl = dot(tq, vec2(${f1(TP.x)}, ${f1(TP.y)})) - ${f1(BEND)} * sin(ts * 3.14159265);
 float tw = max(1e-3, .3 * (.75 + .25 * sin(ts * 23.)) * smoothstep(${f1(S0)}, ${f1(S0 + .05)}, ts) * (1. - .6 * smoothstep(${f1(S1 - .06)}, ${f1(S1)}, ts)));
 float kTrack = (1. - smoothstep(tw * .5, tw, abs(tl))) * step(${f1(S0)}, ts) * step(ts, uTrkS1) * uTrkAmt;`;

// Cheap 3D value noise for the storm shaders.
const NOISE = `
 float h3(vec3 p) { p = fract(p * .3183099 + .1); p *= 17.; return fract(p.x * p.y * p.z * (p.x + p.y + p.z)); }
 float n3(vec3 x) { vec3 i = floor(x), f = fract(x); f = f * f * (3. - 2. * f);
  return mix(mix(mix(h3(i), h3(i + vec3(1, 0, 0)), f.x), mix(h3(i + vec3(0, 1, 0)), h3(i + vec3(1, 1, 0)), f.x), f.y),
   mix(mix(h3(i + vec3(0, 0, 1)), h3(i + vec3(1, 0, 1)), f.x), mix(h3(i + vec3(0, 1, 1)), h3(i + vec3(1, 1, 1)), f.x), f.y), f.z); }
 float fbm3(vec3 p) { return .5 * n3(p) + .27 * n3(p * 2.03 + 1.7) + .15 * n3(p * 4.1 + 3.1) + .08 * n3(p * 8.3 + 5.3); }`;

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

/** A transparent ShaderMaterial that still takes the scene fog, tone mapping and output colour space. */
function stormMaterial(uniforms, vertexShader, fragmentShader) {
 return new THREE.ShaderMaterial({
  uniforms: { ...THREE.UniformsUtils.clone(THREE.UniformsLib.fog), ...uniforms }, fog: true,
  vertexShader: `#include <fog_pars_vertex>\n${vertexShader}`,
  fragmentShader: `#include <fog_pars_fragment>\n${NOISE}\n${fragmentShader}`.replace(/}\s*$/, '#include <tonemapping_fragment>\n#include <colorspace_fragment>\n#include <fog_fragment>\n}'),
  transparent: true, depthWrite: false,
 });
}

function heightLookup(land, segments) {
 const n = segments + 1, step = WORLD / segments, b = land.base;
 return (x, z) => {
  const fx = clamp((x + HALF) / step, 0, segments - 1e-4), fz = clamp((z + HALF) / step, 0, segments - 1e-4);
  const i = Math.floor(fx), j = Math.floor(fz), u = fx - i, v = fz - j, k = j * n + i;
  return lerp(lerp(b[k], b[k + 1], u), lerp(b[k + n], b[k + n + 1], u), v) * RELIEF;
 };
}

/** Normal-blended soft points (smoke, dust, cloud puffs): same layout as glowPoints, but they occlude. */
function softPoints(count, renderOrder = 4) {
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
 points.renderOrder = renderOrder; // smoke sits over the flood surface, under the glow points
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

// A lightning stroke's brightness d seconds after it begins: flash, flicker, one restrike.
const flashAt = d => d < 0 || d > .6 ? 0 : clamp(Math.exp(-d * 7) * (.55 + .45 * Math.cos(d * 95)) + .8 * Math.exp(-Math.pow((d - .2) / .04, 2)));
const STROKES = [[11.35, 0], [12.55, 1], [13.2, 2], [14.05, 1]];

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 const { hemi, key } = stage(scene, { fog: .022 });
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

 // Counties: a staggered grid of township-like rectangles. Those the flood, fire or tornado touched are declared.
 const random = rng(13), XS = [-6, -4, -2, 0, 2, 4, 6], counties = [];
 for (let c = 0; c < 6; c++) {
  const jog = (random() - .5) * .7, zs = [-6, -4 + jog, -2 + jog, jog, 2 + jog, 4 + jog, 6];
  for (let r = 0; r < 6; r++) counties.push({ x0: XS[c], x1: XS[c + 1], z0: zs[r], z1: zs[r + 1] });
 }
 const floodDepth = (x, z) => { const i = clamp(Math.round((x + HALF) / WORLD * NX), 0, NX); return Math.abs(z - riverZ(x)) < SPAN * .8 ? bed[i] + FLOOD - .06 - ground(x, z) : -1; };
 const inSwath = (x, z) => { const [s, l] = trackCoords(x, z); return s >= S0 && Math.abs(l) < swathW(s) * .8; };
 for (const k of counties) {
  let hits = 0;
  for (let a = 0; a < 12; a++) for (let b = 0; b < 12; b++) {
   const x = lerp(k.x0, k.x1, (a + .5) / 12), z = lerp(k.z0, k.z1, (b + .5) / 12);
   if (floodDepth(x, z) > .04 || ignition(x, z) < .95 || inSwath(x, z)) hits++;
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

 const du = { uBurn: { value: 0 }, uFront: { value: 0 }, uScar: { value: 0 }, uFill: { value: 0 }, uT: wu.uT, uTrkS1: { value: 0 }, uTrkAmt: { value: 0 }, uStorm: { value: new THREE.Vector3() } };
 extendSurface(land.mesh.material, 'kfm-disaster-land', du, {
  vDecl: 'attribute float aIgn; attribute float aDecl; varying float vIgn; varying float vDecl; varying vec2 vXZ;',
  vMain: 'vIgn = aIgn; vDecl = aDecl; vXZ = position.xz;',
  fDecl: 'uniform float uBurn, uFront, uScar, uFill, uT, uTrkS1, uTrkAmt; uniform vec3 uStorm; varying float vIgn; varying float vDecl; varying vec2 vXZ; float kFire, kEmber, kScour;',
  fColor: `
   float burnt = (1. - smoothstep(uBurn - .14, uBurn - .02, vIgn)) * uScar;
   float flick = .65 + .35 * sin(uT * 13. + vXZ.x * 23. + vXZ.y * 17.) * sin(uT * 7.3 - vXZ.y * 31.);
   kFire = exp(-pow((vIgn - uBurn + .03) / .045, 2.)) * uFront * flick;
   kEmber = burnt * uFront * smoothstep(.2, 0., uBurn - vIgn) * .5;
   float grain = fract(sin(dot(floor(vXZ * 40.), vec2(12.9898, 78.233))) * 43758.5453);
   diffuseColor.rgb = mix(diffuseColor.rgb, ${v3('#2a211b')} * (.8 + .4 * grain), burnt * .82);
   ${GLSL_TRACK}
   // Scoured ground: dark, with cycloidal suction marks swept along the path.
   float marks = .7 + .3 * sin(tl * 55. + ts * 140. + sin(ts * 300.) * 2.);
   diffuseColor.rgb = mix(diffuseColor.rgb, ${v3('#2c241d')} * marks * (.85 + .3 * grain), kTrack * .88);
   kScour = kTrack * smoothstep(.04, 0., uTrkS1 - ts) * step(uTrkS1, ${f1(S1)});
   diffuseColor.rgb = mix(diffuseColor.rgb, ${v3('#e8c37c')}, vDecl * uFill * .16);
   diffuseColor.rgb *= 1. - uStorm.z * .45 * exp(-dot(vXZ - uStorm.xy, vXZ - uStorm.xy) / 7.); // the storm's shadow`,
  fEmissive: `totalEmissiveRadiance += ${v3('#ff7a2a')} * (kFire * 1.6 + kEmber * .35) + ${v3('#e8c37c')} * vDecl * uFill * .06 + ${v3('#8a7055')} * kScour * .25;`,
 });

 // Fire detections: hotspots inside the burn that light when the front reaches them.
 const HOT = 80, hot = glowPoints(HOT, { size: .3, color: '#ffb14a' }), hotIgn = new Float32Array(HOT), hotFlick = new Float32Array(HOT);
 for (let i = 0; i < HOT;) {
  const x = IGNITE[0] + (random() - .3) * 5.4, z = IGNITE[1] + (random() - .5) * 3.4, v = ignition(x, z);
  if (v > .95 || Math.abs(x) > HALF - .2 || Math.abs(z) > HALF - .2) continue;
  hot.positions.set([x, ground(x, z) + .05, z], i * 3); hotIgn[i] = v; hotFlick[i] = random() * 50; i++;
 }
 scene.add(hot);
 const burnAt = t => smooth(5.1, 9, t), hotC = new THREE.Color('#fff0c0'), coolC = new THREE.Color('#ff6a26'), c = new THREE.Color();

 // Smoke: each puff belongs to a hotspot and only exists once that hotspot is burning.
 const SMOKE = 900, smoke = softPoints(SMOKE), sSrc = new Uint8Array(SMOKE), sPh = new Float32Array(SMOKE), sLife = new Float32Array(SMOKE), sJit = new Float32Array(SMOKE * 2);
 for (let i = 0; i < SMOKE; i++) {
  const a = Math.floor(random() * HOT), b = Math.floor(random() * HOT);
  sSrc[i] = hotIgn[a] < hotIgn[b] ? a : b; // favour early hotspots so the plume builds from the start
  sPh[i] = random(); sLife[i] = 3.8 + random() * 1.6; sJit[i * 2] = random() - .5; sJit[i * 2 + 1] = random();
 }
 scene.add(smoke);
 const sa = smoke.geometry.attributes, warmS = new THREE.Color('#d98a52'), greyS = new THREE.Color('#aeb3b7'), darkS = new THREE.Color('#7b8288');

 // ── Tornado ──
 // Parent storm: a lathed cloud lens whose underside lowers into a wall cloud.
 // Shader noise in rotating polar coordinates turns it counter-clockwise (seen
 // from above), faster near the core, so the mesocyclone reads as rotating.
 const lens = [[0, -.62], [.45, -.6], [.9, -.5], [1.3, -.32], [1.7, -.17], [2.2, -.1], [2.7, -.03], [3, .08], [3.15, .3], [3, .58], [2.5, .82], [1.7, 1.02], [.8, 1.16], [0, 1.2]].map(([r, y]) => new THREE.Vector2(r, y));
 const lensCurve = new THREE.SplineCurve(lens).getPoints(48).map(p => new THREE.Vector2(Math.max(0, p.x), p.y)); // smooth profile, so the lumps don't facet
 const cu = { uT: { value: 0 }, uAmt: { value: 0 }, uFlash: { value: 0 }, uFlashAt: { value: new THREE.Vector2() } };
 const cloud = new THREE.Mesh(new THREE.LatheGeometry(lensCurve, 120), stormMaterial(cu, `
  uniform float uT; varying vec3 vP; varying vec3 vN; varying vec3 vW; varying float vSwirl;
  ${NOISE}
  void main() {
   vec3 p = position; float r = length(p.xz), a = atan(p.z, p.x) + (uT - ${f1(STORM0)}) * 1.4 / (r + 1.1);
   float lump = n3(vec3(cos(a) * r * 1.1, sin(a) * r * 1.1, p.y * 2. + 3.)) - .5 + .35 * (n3(vec3(cos(a) * r * 2.6, sin(a) * r * 2.6, p.y * 3. + 7.)) - .5);
   p += normal * lump * .42 * smoothstep(.1, .9, r); // cauliflower lumps
   vP = p; vN = normalize(normal); vSwirl = a;
   vec4 w = modelMatrix * vec4(p, 1.); vW = w.xyz;
   vec4 mvPosition = viewMatrix * w; gl_Position = projectionMatrix * mvPosition;
   #include <fog_vertex>
  }`, `
  uniform float uT, uAmt, uFlash; uniform vec2 uFlashAt; varying vec3 vP; varying vec3 vN; varying vec3 vW; varying float vSwirl;
  void main() {
   float r = length(vP.xz), a = vSwirl + log(r + .4) * 1.2; // logarithmic spiral arms
   float m = fbm3(vec3(cos(a) * (r * 1.4 + 1.), sin(a) * (r * 1.4 + 1.), vP.y * 1.5 + r * .6));
   float band = .5 + .5 * sin(a * 2.);
   float top = smoothstep(-.2, .7, vN.y), lit = .5 + .5 * dot(vN, normalize(vec3(6., 9., 4.)));
   vec3 col = mix(${v3('#101417')}, ${v3('#4e575d')}, top * .7 + lit * .35) * (.7 + .6 * m + .15 * band);
   col = mix(col, ${v3('#0e1418')}, smoothstep(1.2, 0., r) * (1. - top) * .6); // darker under the wall cloud
   float f = exp(-distance(vP.xz, uFlashAt) * .9);
   col += uFlash * f * ${v3('#b9c8ff')} * (.6 + .8 * m);
   float edge = 1. - smoothstep(2.1, 3.15, r + (m - .45) * 1.4);
   float soft = smoothstep(0., .18, abs(dot(normalize(vN), normalize(cameraPosition - vW)))); // feathered silhouette
   gl_FragColor = vec4(col, uAmt * edge * soft * (.82 + .18 * m));
  }`));
 cloud.scale.setScalar(1.25);
 cloud.renderOrder = 3; // before the funnel, whose top fades into it
 cloud.frustumCulled = false;

 // Ragged cloud puffs around the rim break the lathed silhouette.
 const PUFF = 90, puffs = softPoints(PUFF, 3.5), pTheta = new Float32Array(PUFF), pRad = new Float32Array(PUFF), pY = new Float32Array(PUFF), pSize = new Float32Array(PUFF);
 for (let i = 0; i < PUFF; i++) { pTheta[i] = random() * Math.PI * 2; pRad[i] = .8 + Math.sqrt(random()) * 3.1; pY[i] = (random() - .3) * .5 - .25 * (1 - pRad[i] / 3.1); pSize[i] = 2.6 + random() * 2.4; }
 const puffC = [new THREE.Color('#22282c').convertLinearToSRGB(), new THREE.Color('#4c5459').convertLinearToSRGB(), new THREE.Color(.7, .75, .95)];

 // Condensation funnel: an open cylinder bent and tapered entirely in the vertex
 // shader (rope → cone → rope), so the CPU only moves a few uniforms per frame.
 const fu = {
  uT: { value: 0 }, uBase: { value: new THREE.Vector3() }, uCtrl: { value: new THREE.Vector3() }, uTop: { value: new THREE.Vector3() },
  uR0: { value: .1 }, uR1: { value: .5 }, uDescend: { value: 0 }, uTouch: { value: 0 }, uRope: { value: 0 }, uAlpha: { value: 0 }, uBreak: { value: 0 }, uFlash: cu.uFlash,
 };
 const funnelGeo = new THREE.CylinderGeometry(1, 1, 1, 64, 96, true).translate(0, .5, 0);
 const funnel = new THREE.Mesh(funnelGeo, stormMaterial(fu, `
  uniform float uT, uR0, uR1, uDescend, uTouch, uRope; uniform vec3 uBase, uCtrl, uTop;
  varying float vV; varying float vY; varying float vAng; varying vec3 vN; varying vec3 vW;
  void main() {
   float v = position.y, y = mix(1. - uDescend, 1., v); // the geometry always spans tip → cloud
   vec3 c = mix(mix(uBase, uCtrl, y), mix(uCtrl, uTop, y), y);
   float wig = sin(y * 3.14159);
   c.x += uRope * .3 * sin(y * 9. + uT * 1.7) * wig;
   c.z += uRope * .3 * cos(y * 7. - uT * 1.3) * wig;
   float ang = atan(position.z, position.x);
   float r = mix(uR0, uR1, pow(y, 2.4)) * mix(smoothstep(0., .4, v), 1., uTouch);
   r *= 1. + .07 * sin(ang * 3. + y * 16. - uT * 11.) + .05 * sin(y * 40. - uT * 6.);
   vec3 p = c + vec3(position.x * r, 0., position.z * r);
   vV = v; vY = y; vAng = ang; vN = normalize(vec3(position.x, (uR1 - uR0) * .6, position.z)); vW = p;
   vec4 mvPosition = viewMatrix * vec4(p, 1.); gl_Position = projectionMatrix * mvPosition;
   #include <fog_vertex>
  }`, `
  uniform float uT, uAlpha, uTouch, uBreak, uFlash; varying float vV; varying float vY; varying float vAng; varying vec3 vN; varying vec3 vW;
  void main() {
   vec3 V = normalize(cameraPosition - vW), N = normalize(vN);
   float f = abs(dot(N, V)); // 1 facing the eye (thick core), 0 at the silhouette
   float a = vAng + uT * 4.2 - vY * 9.; // scrolls counter-clockwise; the offset with height twists the striations
   float m = fbm3(vec3(cos(a) * 1.3, sin(a) * 1.3, vY * 15. - uT * 1.1));
   float streak = fbm3(vec3(cos(a) * 3., sin(a) * 3., vY * 4.));
   float lit = .6 + .4 * dot(N, normalize(vec3(6., 9., 4.)));
   vec3 col = mix(${v3('#c9d0d3')}, ${v3('#5b6469')}, f * .75) * lit * (.75 + .45 * m);
   col = mix(col, ${v3('#6e5a46')}, uTouch * (1. - smoothstep(0., .28, vY)) * .75); // dust-stained foot
   col += uFlash * ${v3('#b9c8ff')} * (.2 + .5 * vY);
   float alpha = smoothstep(0., .45, f) * (.72 + .28 * streak);
   alpha *= 1. - smoothstep(.8, 1., vY); // melts into the cloud base
   alpha *= mix(smoothstep(0., .12, vV), smoothstep(0., .03, vV), uTouch);
   alpha *= 1. - uBreak * smoothstep(.42, .62, n3(vec3(vY * 6. - uT * .8, 1.7, 0.)) + (1. - vY) * .25); // rope breaks into pieces
   gl_FragColor = vec4(col, alpha * uAlpha);
  }`));
 funnel.renderOrder = 4;
 funnel.frustumCulled = false;

 // Debris and dust skirt: dust spirals in and up around the foot; small pieces orbit and lift.
 const DUST = 700, dust = softPoints(DUST, 4.5), dTheta = new Float32Array(DUST), dOmega = new Float32Array(DUST), dR = new Float32Array(DUST), dPh = new Float32Array(DUST), dRate = new Float32Array(DUST), dSz = new Float32Array(DUST);
 for (let i = 0; i < DUST; i++) { dTheta[i] = random() * Math.PI * 2; dR[i] = Math.pow(random(), .7); dOmega[i] = 3.2 / (dR[i] + .35); dPh[i] = random(); dRate[i] = .55 + random() * .5; dSz[i] = .6 + random() * .8; }
 const dustLo = new THREE.Color('#6a4e34').convertLinearToSRGB(), dustHi = new THREE.Color('#a48a6c').convertLinearToSRGB();
 const DEBRIS = 70, debris = new THREE.InstancedMesh(new THREE.BoxGeometry(.06, .018, .035), new THREE.MeshStandardMaterial({ color: '#3d3229', roughness: .9 }), DEBRIS);
 const bTheta = new Float32Array(DEBRIS), bR = new Float32Array(DEBRIS), bPh = new Float32Array(DEBRIS), bSpin = new Float32Array(DEBRIS * 3), bScale = new Float32Array(DEBRIS);
 for (let i = 0; i < DEBRIS; i++) { bTheta[i] = random() * Math.PI * 2; bR[i] = .2 + random() * .75; bPh[i] = random(); bScale[i] = .6 + random() * 1.1; for (let k = 0; k < 3; k++) bSpin[i * 3 + k] = (random() - .5) * 14; }
 debris.frustumCulled = false;
 const m4 = new THREE.Matrix4(), q4 = new THREE.Quaternion(), e4 = new THREE.Euler(), p4 = new THREE.Vector3(), s4 = new THREE.Vector3();

 // Lightning: soft additive flashes inside the parent cloud.
 const BOLT = [[.9, -.3], [-.7, .5], [.2, 1.1]];
 const flash = glowPoints(BOLT.length, { size: 7, color: '#c6d4ff' });
 scene.add(cloud, puffs, funnel, dust, debris, flash);

 function update(t) {
  wu.uT.value = t; cu.uT.value = t; fu.uT.value = t;
  // Beat 1 (0–5 s): the flood rises through the valley, eases back to a residual
  // pool after the fire beat, and drains before the loop restarts.
  wu.uLevel.value = -.06 + (FLOOD + .06) * smooth(.1, 4.4, t) * (1 - .6 * smooth(9.2, 11, t)) * (1 - smooth(18.2, 19.7, t));
  water.visible = wu.uLevel.value > -.05;

  // Beat 2 (5–10 s): the fire front spreads downwind; hotspots light, smoke streams off.
  const burn = burnAt(t), live = window01(t, 5, 10.4, .9);
  du.uBurn.value = burn; du.uFront.value = live;
  du.uScar.value = smooth(5.2, 6.2, t) * (1 - smooth(18.4, 19.7, t));
  for (let i = 0; i < HOT; i++) {
   const lit = smooth(hotIgn[i], hotIgn[i] + .04, burn), age = clamp((burn - hotIgn[i]) / .4);
   hot.alphas[i] = lit * live * (.65 + .35 * Math.sin(t * 9 + hotFlick[i]));
   hot.sizes[i] = lerp(.75, .38, age);
   c.copy(hotC).lerp(coolC, age); hot.colors.set([c.r, c.g, c.b], i * 3);
  }
  hot.commit();
  const fade = 1 - smooth(10, 11.4, t);
  smoke.visible = fade > 0 && t > 5;
  if (smoke.visible) {
   for (let i = 0; i < SMOKE; i++) {
    const k = sSrc[i], life = sLife[i], a = (t / life + sPh[i]) % 1, born = t - a * life;
    const alive = born > 5.2 && born < 10.2 && burnAt(born) > hotIgn[k] ? 1 : 0;
    const x0 = hot.positions[k * 3], y0 = hot.positions[k * 3 + 1], z0 = hot.positions[k * 3 + 2], run = a * 3.4, side = sJit[i * 2] * a * 1.1;
    sa.position.array.set([x0 + WIND.x * run - WIND.y * side, y0 + .08 + 1.5 * Math.pow(a, .8) + .08 * Math.sin(t * 1.3 + i), z0 + WIND.y * run + WIND.x * side], i * 3);
    sa.size.array[i] = .45 + 1.9 * a * (.7 + .6 * sJit[i * 2 + 1]);
    sa.alpha.array[i] = alive * fade * .62 * Math.pow(1 - a, 1.2) * smooth(0, .08, a) * smooth(HALF + 1.5, HALF, Math.abs(x0 + WIND.x * run));
    c.copy(warmS).lerp(greyS, smooth(0, .35, a)).lerp(darkS, smooth(.4, 1, a) * .6);
    sa.color.array.set([c.r, c.g, c.b], i * 3);
   }
   for (const k of ['position', 'size', 'alpha', 'color']) sa[k].needsUpdate = true;
  }

  // Beat 3 (10–15 s): a rotating storm drifts SW → NE; a rope funnel descends,
  // widens to a cone over a dust skirt, carves a damage swath, then ropes out.
  const s = trackS(t), [bx, bz] = trackAt(s), by = ground(bx, bz);
  const storm = smooth(9.2, 10.3, t) * (1 - smooth(14.5, 15.5, t));
  const girth = smooth(10.7, 11.9, t) * (1 - smooth(13.3, 14.2, t));
  const rope = (1 - girth) * smooth(10, 10.5, t), touch = smooth(10.85, 11.05, t) * (1 - smooth(14.2, 14.55, t));
  const [cx, cz] = trackAt(s + .05 + .05 * rope), cy = CLOUD + .5 * (1 - smooth(9.2, 10.6, t));
  cloud.visible = puffs.visible = storm > .003;
  let fl = 0, bolt = 0;
  for (const [at, k] of STROKES) { const f = flashAt(t - at); if (f > fl) { fl = f; bolt = k; } }
  fl *= storm;
  cu.uAmt.value = storm; cu.uFlash.value = fl; cu.uFlashAt.value.set(...BOLT[bolt]);
  hemi.intensity = .9 + .55 * fl; key.intensity = 2.4 * (1 - .3 * storm);
  du.uStorm.value.set(cx, cz, storm);
  if (cloud.visible) {
   cloud.position.set(cx, cy, cz);
   const pa = puffs.geometry.attributes;
   for (let i = 0; i < PUFF; i++) {
    const r = pRad[i], a = pTheta[i] - (t - STORM0) * 1.4 / (r * .8 + 1.1);
    pa.position.array.set([cx + Math.cos(a) * r, cy + pY[i] - .1, cz + Math.sin(a) * r], i * 3);
    pa.size.array[i] = pSize[i] * (.9 + .25 * Math.sin(t * .7 + i));
    pa.alpha.array[i] = storm * .4 * smooth(4, 2.6, r);
    c.copy(puffC[0]).lerp(puffC[1], clamp(.3 + pY[i] * 1.4 + .25 * Math.sin(i * 1.7))).lerp(puffC[2], fl * Math.exp(-Math.hypot(Math.cos(a) * r - BOLT[bolt][0], Math.sin(a) * r - BOLT[bolt][1]) * .9) * .7);
    pa.color.array.set([c.r, c.g, c.b], i * 3);
   }
   for (const k of ['position', 'size', 'alpha', 'color']) pa[k].needsUpdate = true;
  }
  BOLT.forEach(([ox, oz], i) => { flash.positions.set([cx + ox, cy - .1, cz + oz], i * 3); flash.alphas[i] = i === bolt ? fl * .85 : 0; });
  flash.commit(); flash.visible = fl > .01;

  const alpha = smooth(10, 10.3, t) * (1 - smooth(14.25, 14.8, t));
  funnel.visible = alpha > .003;
  if (funnel.visible) {
   fu.uAlpha.value = alpha; fu.uDescend.value = easeInOut(smooth(10, 11, t)) * (1 - .5 * smooth(14.2, 14.8, t));
   fu.uTouch.value = touch; fu.uRope.value = rope; fu.uBreak.value = smooth(13.9, 14.6, t);
   fu.uR0.value = lerp(.05, .32, girth); fu.uR1.value = lerp(.28, 1.05, girth);
   fu.uBase.value.set(bx, by - .02, bz); fu.uTop.value.set(cx, cy - .6, cz);
   const lag = .25 + .45 * rope; // the foot trails the storm, more so as it ropes out
   fu.uCtrl.value.set((bx + cx) / 2 - TD.x * lag, lerp(by, cy, .45), (bz + cz) / 2 - TD.y * lag);
  }

  dust.visible = touch > .003;
  if (dust.visible) {
   const da = dust.geometry.attributes, R = lerp(.45, 1, girth);
   for (let i = 0; i < DUST; i++) {
    const a = (t * dRate[i] + dPh[i]) % 1, r = R * (.25 + .75 * dR[i]) * (.45 + .8 * a), th = dTheta[i] - t * dOmega[i];
    const y = by + a * (1.7 - 1.2 * dR[i]) * (.4 + .6 * girth);
    da.position.array.set([bx + Math.cos(th) * r, y, bz + Math.sin(th) * r], i * 3);
    da.size.array[i] = dSz[i] * (.35 + .9 * a) * (.6 + .5 * girth);
    da.alpha.array[i] = touch * .5 * Math.pow(Math.sin(Math.PI * a), .8) * (.6 + .4 * dR[i]);
    c.copy(dustLo).lerp(dustHi, a * .8); da.color.array.set([c.r, c.g, c.b], i * 3);
   }
   for (const k of ['position', 'size', 'alpha', 'color']) da[k].needsUpdate = true;
  }
  const deb = touch * smooth(11.05, 11.6, t);
  debris.visible = deb > .01;
  if (debris.visible) {
   for (let i = 0; i < DEBRIS; i++) {
    const a = (t * .45 + bPh[i]) % 1, r = bR[i] * (.6 + .9 * a) * lerp(.6, 1, girth), th = bTheta[i] - t * 2.6 / (bR[i] + .3);
    p4.set(bx + Math.cos(th) * r, by + .03 + 2.2 * a * a * (1.2 - bR[i]), bz + Math.sin(th) * r);
    q4.setFromEuler(e4.set(t * bSpin[i * 3], t * bSpin[i * 3 + 1], t * bSpin[i * 3 + 2]));
    s4.setScalar(bScale[i] * deb * smooth(0, .06, a) * smooth(1, .85, a));
    debris.setMatrixAt(i, m4.compose(p4, q4, s4));
   }
   debris.instanceMatrix.needsUpdate = true;
  }
  // The swath follows the foot while it is down, then holds until the loop drains it.
  du.uTrkS1.value = clamp(s, S0, S1);
  du.uTrkAmt.value = smooth(TOUCH - .1, TOUCH + .3, t) * (1 - smooth(18.4, 19.7, t));

  // Beat 4 (15–20 s): the county grid appears, then declared counties outline in gold.
  grid.material.opacity = .28 * window01(t, 14.8, 19.8, .8);
  grid.visible = grid.material.opacity > .005;
  const shown = window01(t, 15, 19.8, .8);
  declared.forEach((m, i) => {
   m.reveal(easeInOut(smooth(15.3 + i * .16, 16.3 + i * .16, t)));
   m.material.opacity = shown * (.85 + .15 * Math.sin(t * 4 + i));
   m.visible = shown > .01;
  });
  du.uFill.value = smooth(16.4, 17.4, t) * (1 - smooth(19, 19.8, t));

  // Camera: a slow sway; for the tornado it drops low and swings round so the
  // storm crosses the frame side-on, then climbs back for the county map.
  const low = window01(t, 8, 16.6, 2.8);
  orbit(camera, t, { radius: 21.5 - 2.5 * low, height: 10.8 - 1.2 * window01(t, 3, 19.5, 2.5) - 2.7 * low, target: [0, -.7 + 1.9 * low, 0], start: -.95 + .3 * Math.sin(t / D * Math.PI * 2) - .75 * low, speed: 0 });
 }
 update(0);
 return { scene, camera, update };
}

import * as THREE from 'three';
// Shared building blocks for the welcome scenes. Everything here is synthetic:
// seeded noise shaped like the Kansas plains, never a measured surface.

export { THREE };
export const WORLD = 12; // terrain spans [-6, 6] on x (west→east) and z (north→south)
export const HALF = WORLD / 2;
export const RELIEF = 1.7; // world units of vertical relief at exaggeration 1

export const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
export const lerp = (a, b, t) => a + (b - a) * t;
export const smooth = (a, b, t) => { const x = clamp((t - a) / (b - a)); return x * x * (3 - 2 * x); };
export const easeInOut = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
/** 0→1→0 over [start, end] with `edge` seconds of fade at both ends. */
export const window01 = (t, start, end, edge = .8) => smooth(start, start + edge, t) * (1 - smooth(end - edge, end, t));

export function rng(seed = 1) {
 let a = seed >>> 0;
 return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
}

/** Seeded 2D gradient noise in roughly [-1, 1]. */
export function noise2(seed = 1) {
 const random = rng(seed), perm = new Uint8Array(512), grads = [];
 const p = [...Array(256).keys()];
 for (let i = 255; i > 0; i--) { const j = Math.floor(random() * (i + 1)); [p[i], p[j]] = [p[j], p[i]]; }
 for (let i = 0; i < 512; i++) perm[i] = p[i & 255];
 for (let i = 0; i < 256; i++) { const a = random() * Math.PI * 2; grads.push([Math.cos(a), Math.sin(a)]); }
 const fade = t => t * t * t * (t * (t * 6 - 15) + 10);
 return (x, y) => {
  const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
  const dot = (ix, iy, dx, dy) => { const g = grads[perm[(ix & 255) + perm[iy & 255]]]; return g[0] * dx + g[1] * dy; };
  const u = fade(xf), v = fade(yf);
  const a = lerp(dot(xi, yi, xf, yf), dot(xi + 1, yi, xf - 1, yf), u);
  const b = lerp(dot(xi, yi + 1, xf, yf - 1), dot(xi + 1, yi + 1, xf - 1, yf - 1), u);
  return lerp(a, b, v) * 1.42;
 };
}
export function fbm(n, x, y, octaves = 5, gain = .5, lacunarity = 2.03) {
 let sum = 0, amp = .5, freq = 1;
 for (let i = 0; i < octaves; i++) { sum += amp * n(x * freq, y * freq); freq *= lacunarity; amp *= gain; }
 return sum;
}

/** The synthetic river's centreline, z as a function of x (world units). */
export const riverZ = x => 1.1 * Math.sin(x * .43 + .6) + .45 * Math.sin(x * 1.18 + 2.1);
/** Tributary centrelines join the main river from the north and south. */
export const TRIBUTARIES = Object.freeze([
 { x0: -3.4, side: -1, bend: .6 }, { x0: -.6, side: 1, bend: -.5 }, { x0: 2.3, side: -1, bend: .4 }, { x0: 4.2, side: 1, bend: -.3 },
]);
export function tributaryPoint(trib, s) { // s: 0 at the far end, 1 at the confluence
 const z = trib.side * (HALF - .4) * (1 - s) + riverZ(trib.x0) * s;
 const x = trib.x0 + trib.bend * Math.sin(s * Math.PI) - (1 - s) * .6 * trib.side;
 return [x, z];
}

const heightCache = new Map();
/** Normalized height (≈0 river floor … 1 western uplands) of the shared synthetic plains. */
export function plainsHeight(seed = 7) {
 if (heightCache.has(seed)) return heightCache.get(seed);
 const n = noise2(seed), detail = noise2(seed + 11);
 const fn = (x, z) => {
  const u = x / HALF, v = z / HALF;
  let h = .52 - .28 * u + .3 * fbm(n, u * 1.4 + 3, v * 1.4 - 2, 5);
  h += .06 * fbm(detail, u * 7, v * 7, 3);
  // Dendritic dissection: creases of ridged noise read as small drainages.
  const crease = 1 - Math.abs(fbm(detail, u * 3.2 + 9, v * 3.2 - 4, 3) * 1.6);
  h -= .085 * Math.pow(clamp(crease), 6) * (.4 + .6 * smooth(-.6, .6, u));
  const hills = Math.exp(-Math.pow(u - .38 + .12 * Math.sin(v * 3.2), 2) / .018); // Flint Hills–like band
  h += hills * (.16 + .1 * detail(u * 9, v * 9));
  const d = z - riverZ(x);
  h -= .3 * Math.exp(-d * d / .09) + .14 * Math.exp(-d * d / .9);
  for (const trib of TRIBUTARIES) {
   const side = trib.side;
   if (side * (z - riverZ(x)) < 0) continue;
   const [tx] = tributaryPoint(trib, clamp(1 - Math.abs(z - riverZ(trib.x0)) / (HALF + .4)));
   const dx = x - tx;
   h -= .12 * Math.exp(-dx * dx / .05) * smooth(0, 1.2, Math.abs(z - side * HALF));
  }
  return clamp(h, 0, 1.1);
 };
 heightCache.set(seed, fn);
 return fn;
}

/** Kansas-toned hypsometric ramp: river bottoms → prairie greens → tan uplands. */
const RAMP = [[0, '#2f5a4a'], [.18, '#4f7a4c'], [.36, '#86955a'], [.52, '#b7a76b'], [.7, '#c99e6a'], [.86, '#a8775a'], [1, '#efe2c4']]
 .map(([t, c]) => [t, new THREE.Color(c)]);
export function hypsometric(t, target = new THREE.Color()) {
 t = clamp(t);
 for (let i = 1; i < RAMP.length; i++) if (t <= RAMP[i][0]) {
  const [t0, c0] = RAMP[i - 1], [t1, c1] = RAMP[i];
  return target.copy(c0).lerp(c1, (t - t0) / (t1 - t0));
 }
 return target.copy(RAMP[RAMP.length - 1][1]);
}
export const NATURAL = { low: new THREE.Color('#355a3c'), mid: new THREE.Color('#6d8148'), high: new THREE.Color('#a8955f'), dry: new THREE.Color('#9c8b55'), slope: new THREE.Color('#6b5a43'), riparian: new THREE.Color('#2b4f34') };

/**
 * A displaced terrain grid. `color(h, slope, x, z, out)` paints vertex colours.
 * `setRelief(k)` rescales heights in place (vertical exaggeration).
 */
export function terrain({ segments = 220, height = plainsHeight(), relief = RELIEF, color, material = {} } = {}) {
 const geometry = new THREE.PlaneGeometry(WORLD, WORLD, segments, segments);
 geometry.rotateX(-Math.PI / 2);
 const pos = geometry.attributes.position, count = pos.count, base = new Float32Array(count);
 for (let i = 0; i < count; i++) base[i] = height(pos.getX(i), pos.getZ(i));
 const colors = new Float32Array(count * 3);
 geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
 const mesh = new THREE.Mesh(geometry, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .93, metalness: 0, ...material }));
 const tmp = new THREE.Color();
 function setRelief(k) {
  for (let i = 0; i < count; i++) pos.setY(i, base[i] * k);
  pos.needsUpdate = true; geometry.computeVertexNormals();
 }
 function paint(fn = color) {
  const normal = geometry.attributes.normal;
  for (let i = 0; i < count; i++) {
   const slope = 1 - normal.getY(i);
   (fn || defaultColor)(base[i], slope, pos.getX(i), pos.getZ(i), tmp);
   colors[i * 3] = tmp.r; colors[i * 3 + 1] = tmp.g; colors[i * 3 + 2] = tmp.b;
  }
  geometry.attributes.color.needsUpdate = true;
 }
 setRelief(relief); paint();
 const sample = (x, z) => height(x, z) * relief;
 return { mesh, geometry, base, setRelief, paint, sample, height };
}
const tint = noise2(91);
function defaultColor(h, slope, x, z, out) {
 const n = tint(x * .9, z * .9), fine = tint(x * 4.1 + 7, z * 4.1);
 out.copy(NATURAL.low).lerp(NATURAL.mid, smooth(.12, .5, h + n * .08)).lerp(NATURAL.high, smooth(.55, .95, h + n * .06));
 out.lerp(NATURAL.dry, clamp(.5 + fine * .9) * .35);
 out.lerp(NATURAL.slope, clamp(slope * 7) * .7);
 const d = z - riverZ(x);
 return out.lerp(NATURAL.riparian, Math.exp(-d * d / .25) * .75);
}

/** Night-teal studio: background, fog, sky/ground fill and a warm key light. */
export function stage(scene, { background = '#061a24', fog = .045, sun = [6, 9, 4], sunColor = '#ffe2b8', sunIntensity = 2.4 } = {}) {
 scene.background = new THREE.Color(background);
 scene.fog = new THREE.FogExp2(background, fog);
 const hemi = new THREE.HemisphereLight('#bfe3f2', '#2b2418', .9);
 const key = new THREE.DirectionalLight(sunColor, sunIntensity);
 key.position.set(...sun);
 const rim = new THREE.DirectionalLight('#7fc4e0', .55);
 rim.position.set(-7, 4, -6);
 scene.add(hemi, key, key.target, rim);
 return { hemi, key, rim };
}

/** Slow cinematic orbit around `target`; angles in radians, speed in rad/s. */
export function orbit(camera, t, { radius = 13, height = 7.5, target = [0, 0, 0], start = -.6, speed = .045, bob = .25 } = {}) {
 const a = start + t * speed;
 camera.position.set(target[0] + Math.cos(a) * radius, target[1] + height + Math.sin(t * .35) * bob, target[2] + Math.sin(a) * radius);
 camera.lookAt(target[0], target[1], target[2]);
}

/** Shared point-size scale; the engine keeps it proportional to canvas pixels. */
export const POINT_SCALE = { value: 420 };

let glowTex = null;
/** Soft radial sprite used by every glowing point. */
export function glowTexture() {
 if (glowTex) return glowTex;
 const c = document.createElement('canvas'); c.width = c.height = 64;
 const g = c.getContext('2d'), grd = g.createRadialGradient(32, 32, 0, 32, 32, 32);
 grd.addColorStop(0, 'rgba(255,255,255,1)'); grd.addColorStop(.25, 'rgba(255,255,255,.75)'); grd.addColorStop(.6, 'rgba(255,255,255,.18)'); grd.addColorStop(1, 'rgba(255,255,255,0)');
 g.fillStyle = grd; g.fillRect(0, 0, 64, 64);
 glowTex = new THREE.CanvasTexture(c); glowTex.colorSpace = THREE.SRGBColorSpace;
 return glowTex;
}

/**
 * Additive glowing points with per-point size, colour and alpha.
 * Write into `.positions/.colors/.sizes/.alphas` then call `.commit()`.
 */
export function glowPoints(count, { size = .35, color = '#8fd6ee', opacity = 1, depthTest = true } = {}) {
 const geometry = new THREE.BufferGeometry();
 const positions = new Float32Array(count * 3), colors = new Float32Array(count * 3), sizes = new Float32Array(count).fill(size), alphas = new Float32Array(count).fill(1);
 const base = new THREE.Color(color);
 for (let i = 0; i < count; i++) { colors[i * 3] = base.r; colors[i * 3 + 1] = base.g; colors[i * 3 + 2] = base.b; }
 geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
 geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
 geometry.setAttribute('size', new THREE.BufferAttribute(sizes, 1));
 geometry.setAttribute('alpha', new THREE.BufferAttribute(alphas, 1));
 const material = new THREE.ShaderMaterial({
  uniforms: { map: { value: glowTexture() }, opacity: { value: opacity }, scale: POINT_SCALE },
  vertexShader: `attribute float size;attribute float alpha;attribute vec3 color;varying vec3 vColor;varying float vAlpha;uniform float scale;
   void main(){vColor=color;vAlpha=alpha;vec4 mv=modelViewMatrix*vec4(position,1.);gl_PointSize=size*scale/-mv.z;gl_Position=projectionMatrix*mv;}`,
  fragmentShader: `uniform sampler2D map;uniform float opacity;varying vec3 vColor;varying float vAlpha;
   void main(){vec4 t=texture2D(map,gl_PointCoord);gl_FragColor=vec4(vColor*t.rgb,t.a*vAlpha*opacity);}`,
  transparent: true, depthWrite: false, depthTest, blending: THREE.AdditiveBlending,
 });
 const points = new THREE.Points(geometry, material);
 points.frustumCulled = false;
 points.renderOrder = 5; // after water and overlays, which write or blend colour
 points.positions = positions; points.colors = colors; points.sizes = sizes; points.alphas = alphas;
 points.commit = () => { for (const k of ['position', 'color', 'size', 'alpha']) geometry.attributes[k].needsUpdate = true; };
 return points;
}

/**
 * A flat ribbon that follows `path` (array of Vector3) just above the surface.
 * `.reveal(p)` draws the first fraction p of its length.
 */
export function ribbon(path, { width = .06, color = '#e8c37c', opacity = 1, additive = false, lift = .02 } = {}) {
 const n = path.length, positions = new Float32Array(n * 2 * 3), indices = [];
 const up = new THREE.Vector3(0, 1, 0), dir = new THREE.Vector3(), side = new THREE.Vector3();
 for (let i = 0; i < n; i++) {
  dir.subVectors(path[Math.min(n - 1, i + 1)], path[Math.max(0, i - 1)]).normalize();
  side.crossVectors(up, dir).normalize().multiplyScalar(width / 2);
  const p = path[i];
  positions.set([p.x + side.x, p.y + lift, p.z + side.z, p.x - side.x, p.y + lift, p.z - side.z], i * 6);
  if (i < n - 1) { const a = i * 2; indices.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
 }
 const geometry = new THREE.BufferGeometry();
 geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
 geometry.setIndex(indices);
 const material = new THREE.MeshBasicMaterial({ color, transparent: true, opacity, depthWrite: false, side: THREE.DoubleSide, blending: additive ? THREE.AdditiveBlending : THREE.NormalBlending });
 const mesh = new THREE.Mesh(geometry, material);
 mesh.reveal = p => geometry.setDrawRange(0, Math.floor(clamp(p) * (n - 1)) * 6);
 mesh.reveal(1);
 mesh.renderOrder = 2;
 return mesh;
}

/** Sample a path over the surface: `fn(s)` returns [x, z] for s in [0, 1]. */
export function surfacePath(fn, sample, steps = 160, lift = .03) {
 const out = [];
 for (let i = 0; i <= steps; i++) { const [x, z] = fn(i / steps); out.push(new THREE.Vector3(x, sample(x, z) + lift, z)); }
 return out;
}
export const mainRiver = (s, from = -HALF, to = HALF) => { const x = lerp(from, to, s); return [x, riverZ(x)]; };

/** Free every geometry, material and texture under `root` (shared glow sprite excepted). */
export function disposeTree(root) {
 root.traverse(o => {
  o.geometry?.dispose?.();
  const mats = Array.isArray(o.material) ? o.material : o.material ? [o.material] : [];
  for (const m of mats) { for (const v of Object.values(m)) if (v?.isTexture && v !== glowTex) v.dispose(); for (const u of Object.values(m.uniforms || {})) if (u.value?.isTexture && u.value !== glowTex) u.value.dispose(); m.dispose(); }
 });
}

/**
 * GPU-driven surface controls for a `terrain()` result. Returns uniforms:
 *  relief   vertical exaggeration multiplier (1 = as built)
 *  sweep    world x of a west→east reveal front (vertices east of it lie flat); 99 = all revealed
 *  grey     0..1 blend toward neutral hillshade grey
 *  hypso    0..1 blend toward the hypsometric elevation ramp
 *  contour  0..1 strength of contour lines; contourStep = lines per unit of normalized height
 *  tint/tintMix  colour wash over the whole surface
 * Heights scale in the vertex shader and normals blend toward up as relief → 0,
 * so none of these needs a CPU rebuild.
 */
export function liveSurface(surface) {
 const { geometry, base } = surface, pos = geometry.attributes.position, count = pos.count;
 const hyps = new Float32Array(count * 3), tmp = new THREE.Color();
 for (let i = 0; i < count; i++) { hypsometric(base[i], tmp); hyps[i * 3] = tmp.r; hyps[i * 3 + 1] = tmp.g; hyps[i * 3 + 2] = tmp.b; }
 geometry.setAttribute('aH', new THREE.BufferAttribute(base, 1));
 geometry.setAttribute('aHypso', new THREE.BufferAttribute(hyps, 3));
 const u = {
  relief: { value: 1 }, sweep: { value: 99 }, sweepSoft: { value: 1.4 }, grey: { value: 0 }, hypso: { value: 0 },
  contour: { value: 0 }, contourStep: { value: 14 }, contourColor: { value: new THREE.Color('#2a1d12') },
  tint: { value: new THREE.Color('#ffffff') }, tintMix: { value: 0 },
 };
 const material = surface.mesh.material;
 material.onBeforeCompile = shader => {
  Object.assign(shader.uniforms, u);
  shader.vertexShader = shader.vertexShader
   .replace('#include <common>', `#include <common>
    attribute float aH; attribute vec3 aHypso; uniform float relief; uniform float sweep; uniform float sweepSoft;
    varying float vH; varying vec3 vHypso; float kRaise;`)
   .replace('#include <beginnormal_vertex>', `#include <beginnormal_vertex>
    kRaise = relief * (1.0 - smoothstep(sweep - sweepSoft, sweep, position.x));
    objectNormal = normalize(mix(vec3(0.0, 1.0, 0.0), objectNormal, clamp(kRaise, 0.0, 1.0)));`)
   .replace('#include <begin_vertex>', `#include <begin_vertex>
    transformed.y *= kRaise; vH = aH; vHypso = aHypso;`);
  shader.fragmentShader = shader.fragmentShader
   .replace('#include <common>', `#include <common>
    uniform float grey; uniform float hypso; uniform float contour; uniform float contourStep; uniform vec3 contourColor;
    uniform vec3 tint; uniform float tintMix; varying float vH; varying vec3 vHypso;`)
   .replace('#include <color_fragment>', `#include <color_fragment>
    diffuseColor.rgb = mix(diffuseColor.rgb, vHypso, hypso);
    diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.74), grey);
    diffuseColor.rgb = mix(diffuseColor.rgb, tint, tintMix);
    float cf = vH * contourStep; float cw = fwidth(cf);
    float cl = 1.0 - smoothstep(0.0, cw * 1.4, min(fract(cf), 1.0 - fract(cf)));
    float major = step(0.5, fract(floor(cf + 0.5) / 5.0 + 0.1));
    diffuseColor.rgb = mix(diffuseColor.rgb, contourColor, cl * contour * mix(0.55, 0.9, 1.0 - major));`);
 };
 material.customProgramCacheKey = () => 'kfm-live-surface';
 surface.uniforms = u;
 return u;
}

/** A glowing vertical curtain at x = `.at(x)`, used for scan and reveal fronts. */
export function scanCurtain({ color = '#7fe0ff', height = 1.8, depth = WORLD } = {}) {
 const c = document.createElement('canvas'); c.width = 4; c.height = 128;
 const g = c.getContext('2d'), grd = g.createLinearGradient(0, 128, 0, 0);
 grd.addColorStop(0, 'rgba(255,255,255,.9)'); grd.addColorStop(.25, 'rgba(255,255,255,.35)'); grd.addColorStop(1, 'rgba(255,255,255,0)');
 g.fillStyle = grd; g.fillRect(0, 0, 4, 128);
 const map = new THREE.CanvasTexture(c);
 const mesh = new THREE.Mesh(new THREE.PlaneGeometry(depth, height), new THREE.MeshBasicMaterial({ map, color, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide }));
 mesh.rotation.y = Math.PI / 2; mesh.position.y = height / 2;
 mesh.at = x => { mesh.position.x = x; };
 return mesh;
}


/** Strata used for block sides and cross-sections, top → bottom (depth in world units). */
export const STRATA = Object.freeze([
 { name: 'Soil', depth: .14, color: '#4a3726' },
 { name: 'Loess', depth: .32, color: '#a88a5c' },
 { name: 'Aquifer sand & gravel', depth: .75, color: '#c9b183', aquifer: true },
 { name: 'Shale', depth: .55, color: '#6e6a63' },
 { name: 'Limestone bedrock', depth: 99, color: '#9a9488' },
]);
/** Stratum colour at `depth` below the surface; boundaries wave with x/z. */
export function strataColor(depth, x, z, out = new THREE.Color()) {
 let top = 0;
 const wobble = .05 * Math.sin(x * 1.3 + z * .7) + .03 * Math.sin(x * 3.7 - z * 2.1);
 for (const layer of STRATA) {
  const bottom = top + layer.depth + wobble * (layer.aquifer ? 1.6 : 1);
  if (depth <= bottom) {
   out.set(layer.color);
   const band = .5 + .5 * Math.sin(depth * 46 + x * 2.3);
   return out.multiplyScalar(.9 + band * .12);
  }
  top = bottom;
 }
 return out.set(STRATA[STRATA.length - 1].color);
}

/**
 * Diorama walls: four sides from the surface down to `floor`, painted with
 * strata, so the terrain reads as a cut block of ground.
 */
export function blockSides(sample, { floor = -2.2, steps = 120, rows = 40, color = strataColor } = {}) {
 const group = new THREE.Group(), tmp = new THREE.Color();
 const edges = [
  s => [lerp(-HALF, HALF, s), HALF], s => [HALF, lerp(HALF, -HALF, s)],
  s => [lerp(HALF, -HALF, s), -HALF], s => [-HALF, lerp(-HALF, HALF, s)],
 ];
 for (const edge of edges) {
  const positions = [], colors = [], index = [];
  for (let i = 0; i <= steps; i++) {
   const [x, z] = edge(i / steps), top = sample(x, z);
   for (let j = 0; j <= rows; j++) {
    const y = lerp(top, floor, j / rows);
    positions.push(x, y, z);
    color(top - y, x, z, tmp); colors.push(tmp.r, tmp.g, tmp.b);
    if (i < steps && j < rows) { const a = i * (rows + 1) + j, b = a + rows + 1; index.push(a, b, a + 1, b, b + 1, a + 1); }
   }
  }
  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
  geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
  geometry.setIndex(index); geometry.computeVertexNormals();
  group.add(new THREE.Mesh(geometry, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 1, side: THREE.DoubleSide })));
 }
 const base = new THREE.Mesh(new THREE.PlaneGeometry(WORLD, WORLD), new THREE.MeshStandardMaterial({ color: '#4d4a44', roughness: 1 }));
 base.rotation.x = Math.PI / 2; base.position.y = floor;
 group.add(base);
 return group;
}

/** Glassy river water laid in the valley floor along `riverZ`. */
export function riverWater(sample, { width = .34, color = '#3f86a6', from = -HALF, to = HALF } = {}) {
 const path = surfacePath(s => mainRiver(s, from, to), (x, z) => sample(x, z), 220, .015);
 const mesh = ribbon(path, { width, color, opacity: .92 });
 mesh.material = new THREE.MeshStandardMaterial({ color, roughness: .18, metalness: .25, emissive: '#0d3446', emissiveIntensity: .6, transparent: true, opacity: .93, side: THREE.DoubleSide });
 mesh.renderOrder = 1;
 return mesh;
}

/** The standard hero shot: a camera that frames the block right of the cards. */
export function heroCamera({ fov = 30 } = {}) {
 const camera = new THREE.PerspectiveCamera(fov, 1, .1, 120);
 camera.userData.shift = .12; // engine pans the projection so the subject sits right of centre
 return camera;
}

/**
 * Bilinear height lookup into a built `terrain()` grid (world units, at its
 * relief). Far cheaper than re-evaluating the noise, so per-frame effects that
 * follow the ground (particles, moving sections) should use this.
 */
export function gridSampler(surface, relief = RELIEF) {
 const { base } = surface, seg = Math.round(Math.sqrt(base.length)) - 1, step = WORLD / seg;
 return (x, z) => {
  const fx = clamp((x + HALF) / step, 0, seg - 1e-6), fz = clamp((z + HALF) / step, 0, seg - 1e-6);
  const c = Math.floor(fx), r = Math.floor(fz), tx = fx - c, tz = fz - r, row = seg + 1;
  const a = base[r * row + c], b = base[r * row + c + 1], d = base[(r + 1) * row + c], e = base[(r + 1) * row + c + 1];
  return lerp(lerp(a, b, tx), lerp(d, e, tx), tz) * relief;
 };
}

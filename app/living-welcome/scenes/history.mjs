import { THREE, terrain, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, glowTexture, gridSampler, noise2, fbm, rng, riverZ, smooth, lerp, clamp } from './kit.mjs';
// History: one diorama lives through time. A figure steps out of a cave at dawn,
// a fire-lit camp grows into a village, the village gives way to a 1920s town at
// golden hour, a downtown of towers rises at blue hour, and an imagined city of
// light spreads to the edges before the night fades back to the dawn bluff.

const D = 36, TAU = Math.PI * 2, HERO = 1.6; // the cave walker is drawn larger than the crowd so the first beat reads
const CAVE = { x: -3.58, z: -2.7, dir: -.36 }; // mouth, and the way it faces (radians from +x toward +z)
const N = [Math.cos(CAVE.dir), Math.sin(CAVE.dir)];
const XS = -1, ZS = -2.4, BX = 1.1, BZ = .9, ROAD = .055, WALK = .088; // street grid (shared with the ground shader)
const G = [XS, ZS], DT = [-.6, -2.1], FC = [-.4, -1.2]; // town centre, downtown, future core
const FIRES = [[-2.45, -2.55], [-1.55, -3.35], [-1.35, -1.75], [-2.75, -3.75]];
const IGNITE = [6.4, 12, 12.6, 13.2];

const n1 = noise2(41), n2 = noise2(57);
// An east-facing limestone bluff on the west edge, with an alcove for the cave.
const edgeX = z => -3.95 + .22 * Math.sin(z * 1.3 + .4) + .1 * Math.sin(z * 3.1) - .95 * Math.exp(-(((z - CAVE.z) / .5) ** 2));
function height(x, z) {
 let h = .2 + .07 * fbm(n1, x * .25, z * .25, 4) + .025 * fbm(n2, x * 1.2, z * 1.2, 3);
 const e = edgeX(z);
 h += smooth(e + .3, e - .14, x) * (1.35 + .12 * fbm(n2, x * .6 + 5, z * .6, 3));
 const d = z - riverZ(x);
 return h - smooth(-3.6, -3.1, x) * (.2 * Math.exp(-d * d / .045) + .05 * Math.exp(-d * d / .4));
}
const onLand = (x, z, margin = .5) => (x < -3.7 || Math.abs(z - riverZ(x)) > margin) && (x > edgeX(z) + .55 || x < edgeX(z) - .4);

const C = hex => new THREE.Color(hex);
const PR1 = C('#4f6b3c'), PR2 = C('#7c8650'), DRY = C('#9a8a58'), LIME = C('#b6a688'), LIME2 = C('#7c6e59'), RIP = C('#35553a'), TMP = new THREE.Color();
function paint(h, slope, x, z, out) {
 const n = n1(x * .9 + 3, z * .9), f = n2(x * 3.7, z * 3.7 + 2);
 out.copy(PR1).lerp(PR2, clamp(.45 + n * .8)).lerp(DRY, clamp(.35 + f) * .3);
 const rock = clamp((slope - .1) * 4.5);
 if (rock > 0) out.lerp(TMP.copy(LIME).lerp(LIME2, clamp(.5 + .45 * Math.sin(h * 11 + n * .8) + .25 * f)), rock); // bedding planes
 const d = z - riverZ(x);
 return out.lerp(RIP, Math.exp(-d * d / .1) * .65 * smooth(-3.7, -3.2, x));
}

// Lighting tells the time: each era has its own sky, key light and fill.
const MOODS = {
 dawn: { top: '#26476a', low: '#0f2233', glow: '#e8946a', key: '#ffc896', keyI: 3.3, dir: [8, 2.6, -1.5], sky: '#bcd4e6', ground: '#4a382a', hemiI: 1.05, rimI: .45, stars: 0 },
 night: { top: '#10243a', low: '#06111c', glow: '#6a3e33', key: '#a8c0e6', keyI: 1.15, dir: [-5, 8, -4], sky: '#86a4cc', ground: '#2a2018', hemiI: 1.05, rimI: .5, stars: .8 },
 golden: { top: '#28425c', low: '#0d1c28', glow: '#f2a65a', key: '#ffbd70', keyI: 2.7, dir: [5, 2.3, 6], sky: '#cdbb9c', ground: '#3a2a1c', hemiI: .72, rimI: .5, stars: 0 },
 blue: { top: '#153554', low: '#071729', glow: '#4a86c0', key: '#a2bdf0', keyI: .8, dir: [-4, 6, 5], sky: '#7096c8', ground: '#151b24', hemiI: .55, rimI: .6, stars: .3 },
 future: { top: '#0e1434', low: '#03060f', glow: '#2a8fb4', key: '#a0d8ff', keyI: .45, dir: [-3, 8, 3], sky: '#5070a8', ground: '#0e0e1a', hemiI: .42, rimI: .7, stars: .7 },
};
for (const m of Object.values(MOODS)) for (const k of ['top', 'low', 'glow', 'key', 'sky', 'ground']) m[k] = C(m[k]);
const MOOD_KEYS = [[0, 'dawn'], [4.4, 'dawn'], [7.4, 'night'], [16.2, 'night'], [18.4, 'golden'], [22.2, 'golden'], [24.6, 'blue'], [28.3, 'blue'], [30.6, 'future'], [33.7, 'future'], [36, 'dawn']].map(([t, k]) => [t, MOODS[k]]);
// The camera starts close on the cave, pulls back as the settlement grows, and swoops home for the loop.
const CAM_KEYS = [
 [0, { T: [-3.25, .5, -2.65], r: 9.5, h: 3.2 }], [1.2, { T: [CAVE.x + N[0] * .4, height(CAVE.x, CAVE.z) + .3, CAVE.z + N[1] * .4], r: 4.8, h: 1.25 }], [4.5, null],
 [7.8, { T: [-2.6, .4, -2.6], r: 7, h: 2.9 }], [11.4, null], [14.8, { T: [-2.1, .2, -2.6], r: 10.5, h: 4.4 }], [16.4, null], [19.2, { T: [-1, 0, -2.4], r: 14.5, h: 6.8 }], [22.2, null],
 [25.2, { T: [-.7, .7, -2], r: 17.5, h: 8 }], [28.2, null], [31.2, { T: [-.3, 1.6, -.6], r: 24, h: 10 }], [33.6, null], [36, null],
];
CAM_KEYS.forEach((k, i) => { k[1] ??= i === CAM_KEYS.length - 1 ? CAM_KEYS[0][1] : CAM_KEYS[i - 1][1]; });
function keyed(keys, t) {
 for (let i = 1; i < keys.length; i++) if (t <= keys[i][0]) return [keys[i - 1][1], keys[i][1], smooth(keys[i - 1][0], keys[i][0], t)];
 const last = keys[keys.length - 1][1];
 return [last, last, 0];
}

const pop = p => p <= 0 ? 0 : p >= 1 ? 1 : 1 + 2.4 * (p - 1) ** 3 + 1.4 * (p - 1) ** 2; // ease out with a little overshoot
const life = (t, a, da, b = 1e9, db = .6) => pop(clamp((t - a) / da)) * (1 - smooth(b, b + db, t));
const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);

/** Merge [geometry, colour | (pos, out) => colour] parts into one flat-shaded geometry with vertex colours. */
function bake(parts) {
 const pos = [], nor = [], col = [], c = new THREE.Color(), p = new THREE.Vector3();
 for (const [geo, color] of parts) {
  const g = geo.index ? geo.toNonIndexed() : geo;
  g.computeVertexNormals();
  if (typeof color === 'string') c.set(color);
  const a = g.attributes.position, n = g.attributes.normal;
  for (let i = 0; i < a.count; i++) {
   p.fromBufferAttribute(a, i);
   if (typeof color === 'function') color(p, c);
   pos.push(p.x, p.y, p.z); nor.push(n.getX(i), n.getY(i), n.getZ(i)); col.push(c.r, c.g, c.b);
  }
  if (g !== geo) g.dispose();
  geo.dispose();
 }
 const out = new THREE.BufferGeometry();
 out.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
 out.setAttribute('normal', new THREE.Float32BufferAttribute(nor, 3));
 out.setAttribute('color', new THREE.Float32BufferAttribute(col, 3));
 return out;
}
const Box = (w, h, d, x = 0, y = 0, z = 0) => new THREE.BoxGeometry(w, h, d).translate(x, y, z);
function instanced(geometry, material, count, colors) {
 const mesh = new THREE.InstancedMesh(geometry, material, count);
 mesh.frustumCulled = false; // instances move; the cached bounds would cull them wrongly
 if (colors) { for (let i = 0; i < count; i++) mesh.setColorAt(i, colors(i, TMP)); mesh.instanceColor.needsUpdate = true; }
 return mesh;
}
const M4 = new THREE.Matrix4(), QU = new THREE.Quaternion(), V3 = new THREE.Vector3(), S3 = new THREE.Vector3(), UP = new THREE.Vector3(0, 1, 0);
function put(mesh, i, x, y, z, rot, sx, sy = sx, sz = sx) {
 QU.setFromAxisAngle(UP, rot); V3.set(x, y, z);
 if (sx < 1e-3 || sy < 1e-3 || sz < 1e-3) S3.setScalar(1e-5); else S3.set(sx, sy, sz); // a collapsed instance must not leave a flat footprint
 mesh.setMatrixAt(i, M4.compose(V3, QU, S3));
}
/** A point on a rectangle loop (x0, z0, w, d) at fraction s, with its heading. */
function rectPoint(x0, z0, w, d, s, out) {
 let u = (((s % 1) + 1) % 1) * 2 * (w + d);
 if (u < w) { out[0] = x0 + u; out[1] = z0; out[2] = 1; out[3] = 0; return out; }
 u -= w; if (u < d) { out[0] = x0 + w; out[1] = z0 + u; out[2] = 0; out[3] = 1; return out; }
 u -= d; if (u < w) { out[0] = x0 + w - u; out[1] = z0 + d; out[2] = -1; out[3] = 0; return out; }
 u -= w; out[0] = x0; out[1] = z0 + d - u; out[2] = 0; out[3] = -1; return out;
}

/** A rock outcrop at the foot of the bluff with a dark arched cave mouth (local +z faces out). */
function outcrop() {
 const group = new THREE.Group(), rn = noise2(5), W = .22, AH = .48;
 const arch = new THREE.Shape();
 arch.moveTo(-W, 0); arch.lineTo(W, 0); arch.lineTo(W, AH - W); arch.absarc(0, AH - W, W, 0, Math.PI, false); arch.lineTo(-W, 0);
 const face = new THREE.Shape([[-.56, 0], [.58, 0], [.62, .3], [.5, .6], [.3, .78], [.05, .84], [-.24, .8], [-.48, .62], [-.6, .32]].map(([x, y]) => new THREE.Vector2(x, y)));
 const hole = new THREE.Path(); hole.moveTo(-W, 0); hole.lineTo(W, 0); hole.lineTo(W, AH - W); hole.absarc(0, AH - W, W, 0, Math.PI, false); hole.lineTo(-W, 0);
 face.holes.push(hole);
 const rough = (amp, f) => (p, c) => { // displace by position so shared corners stay welded
  const k = Math.min(1, p.y * 8);
  p.x += rn(p.y * f + 3, p.z * f) * amp * k; p.y += rn(p.x * f, p.z * f + 7) * amp * .6 * k; p.z += rn(p.x * f + 11, p.y * f) * amp * k;
  return c.copy(LIME).lerp(LIME2, clamp(.5 + .5 * Math.sin(p.y * 30 + rn(p.x * 3, p.z * 3) * 4))).multiplyScalar(.85 + .15 * rn(p.x * 9, p.y * 9));
 };
 const parts = [[new THREE.ExtrudeGeometry(face, { depth: .32, bevelEnabled: true, bevelThickness: .05, bevelSize: .05, bevelSegments: 1, curveSegments: 10 }).translate(0, 0, -.32), rough(.06, 3.5)]];
 for (const [x, y, z, r, sy] of [[-.7, .36, -.5, .44, .9], [.72, .34, -.5, .44, .85], [-.05, 1, -.55, .46, .7], [0, .55, -1.38, .52, 1], [-.5, .95, -1.05, .45, .9], [.52, .9, -1.05, .45, .9], [0, 1.2, -1, .42, .8], [-1.05, .25, -.2, .3, .8], [1.02, .22, -.25, .28, .8], [-.62, .14, .05, .2, .8], [.66, .16, .02, .22, .75], [-.4, .8, -.1, .26, .7], [.42, .74, -.12, .25, .75], [.05, .9, -.2, .24, .6]]) {
  parts.push([new THREE.IcosahedronGeometry(r, 1).scale(1, sy, 1).translate(x, y, z), rough(r * .22, 3)]);
 }
 const rock = new THREE.Mesh(bake(parts), new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .95 }));
 // The tunnel: inner faces only, darkening with depth, so the mouth reads as a hollow.
 const tunnel = new THREE.ExtrudeGeometry(arch, { depth: .85, bevelEnabled: false, curveSegments: 10 }).translate(0, 0, -.85);
 const tc = [], ta = tunnel.attributes.position, near = C('#3a3027'), far = C('#020202');
 for (let i = 0; i < ta.count; i++) { TMP.copy(near).lerp(far, clamp(-ta.getZ(i) / .55)); tc.push(TMP.r, TMP.g, TMP.b); }
 tunnel.setAttribute('color', new THREE.Float32BufferAttribute(tc, 3));
 group.add(rock, new THREE.Mesh(tunnel, new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.BackSide })));
 return group;
}

/** The figure who steps out of the cave: jointed, so it can actually walk. */
function walker() {
 const cloth = new THREE.MeshStandardMaterial({ color: '#7c3b26', roughness: .9 }), skin = new THREE.MeshStandardMaterial({ color: '#6e4630', roughness: .8 }); // deeper than the limestone, so the figure separates
 const root = new THREE.Group(), body = new THREE.Group();
 root.add(body);
 body.add(new THREE.Mesh(new THREE.CylinderGeometry(.034, .055, .125, 8).translate(0, .168, 0), cloth));
 const head = new THREE.Mesh(new THREE.IcosahedronGeometry(.025, 1).translate(0, .016, 0), skin);
 head.position.y = .238; body.add(head);
 const limb = (w, h, x, y, mat) => { const pivot = new THREE.Group(); pivot.position.set(x, y, 0); pivot.add(new THREE.Mesh(new THREE.BoxGeometry(w, h, w * 1.1).translate(0, -h / 2, 0), mat)); body.add(pivot); return pivot; };
 const legs = [limb(.022, .11, -.017, .112, cloth), limb(.022, .11, .017, .112, cloth)];
 const arms = [limb(.018, .095, -.05, .218, skin), limb(.018, .095, .05, .218, skin)];
 return { root, body, head, legs, arms, cloth, skin, clothBase: cloth.color.clone(), skinBase: skin.color.clone() };
}

// Ground: the terrain shader paints camp clearings, the street grid, downtown
// paving and the future city's lit lanes, each grown by a radius uniform.
const GROUND_HEAD = `uniform vec4 uCamp[4]; uniform vec4 uTown; uniform vec4 uDown; uniform vec4 uFut; uniform vec3 uLane; varying vec3 vWP; varying float vNy;`;
const GROUND_FRAG = `
 vec2 gp = vWP.xz;
 float level = smoothstep(.8, .93, vNy);
 float rz = 1.1 * sin(gp.x * .43 + .6) + .45 * sin(gp.x * 1.18 + 2.1);
 float dry = max(smoothstep(.42, .6, abs(gp.y - rz)), 1.0 - smoothstep(-3.7, -3.3, gp.x));
 float camp = 0.0;
 for (int i = 0; i < 4; i++) { vec4 c = uCamp[i]; camp = max(camp, c.w * (1.0 - smoothstep(c.z * .5, c.z, length(gp - c.xy)))); }
 diffuseColor.rgb = mix(diffuseColor.rgb, vec3(.3, .23, .15), camp * .7 * level);
 vec2 dl = abs(fract(vec2((gp.x - ${XS.toFixed(2)}) / ${BX.toFixed(2)}, (gp.y - (${ZS.toFixed(2)})) / ${BZ.toFixed(2)}) + .5) - .5) * vec2(${BX.toFixed(2)}, ${BZ.toFixed(2)});
 float dm = min(dl.x, dl.y), aa = fwidth(dm) + .003;
 float road = 1.0 - smoothstep(${ROAD} - aa, ${ROAD} + aa, dm);
 float walk = (1.0 - smoothstep(${(ROAD + .045).toFixed(3)} - aa, ${(ROAD + .045).toFixed(3)} + aa, dm)) - road;
 float mt = uTown.w * (1.0 - smoothstep(uTown.z - .5, uTown.z, length(gp - uTown.xy))) * level * dry;
 diffuseColor.rgb = mix(diffuseColor.rgb, mix(diffuseColor.rgb * vec3(.95, 1.05, .9), mix(vec3(.62, .58, .5), vec3(.42, .36, .27), road), max(road, walk * .8)), mt);
 float md = uDown.w * (1.0 - smoothstep(uDown.z - .35, uDown.z, length(gp - uDown.xy))) * level * dry;
 diffuseColor.rgb = mix(diffuseColor.rgb, mix(vec3(.3, .3, .3), vec3(.06, .065, .075), road), md);
 float mf = uFut.w * (1.0 - smoothstep(uFut.z - .9, uFut.z, length(gp - uFut.xy))) * level;
 float edge = 1.0 - smoothstep(0.0, fwidth(dm) * 1.2, abs(dm - ${ROAD}));
 diffuseColor.rgb = mix(diffuseColor.rgb, mix(vec3(.07, .085, .11), vec3(.025, .03, .04), road), mf);
 totalEmissiveRadiance += uLane * mf * (edge * .28 + road * .03);`;

// Towers: window grids from world height and per-face metric coordinates, so
// floors keep their spacing however tall an instance grows.
const TOWER_HEAD = `attribute vec4 aBox; attribute float aGrow; varying vec3 vL; varying vec3 vNo; varying float vY; varying vec4 vBox; varying float vGrow;`;
const TOWER_FRAG_HEAD = `uniform float uWin; uniform float uFut; uniform float uTime; uniform vec3 uBuild; varying vec3 vL; varying vec3 vNo; varying float vY; varying vec4 vBox; varying float vGrow;
 float hh(vec3 p) { p = fract(p * .1031); p += dot(p, p.zyx + 31.32); return fract((p.x + p.y) * p.z); }`;
const TOWER_FRAG = `
 float style = vBox.w, seed = vBox.z, roof = step(.6, vNo.y);
 float cu = (style > 1.5 ? atan(vL.z, vL.x) * length(vL.xz) : (abs(vNo.x) > .5 ? vL.z : vL.x)) / .068;
 float fy = vY / .082, fl = floor(fy), ff = fract(fy), cf = fract(cu), ci = floor(cu);
 float pane = step(.2, ff) * step(ff, .82) * step(.18, cf) * step(cf, .82) * (1.0 - roof);
 float r = hh(vec3(ci, fl, seed * 97.0)), lit = pane * step(r, .5 + .15 * sin(uTime * .3 + seed * 20.0));
 vec3 base;
 if (style < .5) base = mix(mix(vec3(.05, .1, .14), vec3(.14, .22, .28), smoothstep(-1.0, 8.0, vY)), vec3(.02, .035, .05), pane * .6);
 else if (style < 1.5) base = mix(vec3(.52, .47, .4), vec3(.05, .05, .06), pane);
 else base = mix(vec3(.55, .62, .7), vec3(.03, .05, .08), step(.12, cf) * step(cf, .88) * step(.14, ff) * .85);
 diffuseColor.rgb *= mix(base, vec3(.1, .1, .11), roof);
 vec3 warm = mix(vec3(1.0, .7, .38), vec3(.7, .88, 1.0), step(.7, hh(vec3(ci + 3.0, fl, seed))));
 vec3 em = warm * lit * uWin * 1.5;
 if (style > 1.5) {
  float strip = step(mod(ci + floor(seed * 7.0), 4.0), .5) * smoothstep(.35, .5, cf) * (1.0 - smoothstep(.5, .65, cf));
  float band = step(mod(fl + floor(seed * 5.0), 9.0), .5);
  vec3 tint = mix(vec3(.3, .85, 1.0), vec3(.95, .45, 1.0), step(.75, seed));
  em = em * .5 + uFut * tint * ((strip * 1.4 + band * .7) * (1.0 - roof) + smoothstep(vBox.y - .1, vBox.y, vY) * .6 * (1.0 - roof));
 }
 if (style > 2.5) em = uFut * vec3(.6, .9, 1.0) * 1.5;
 float top = vBox.x + (vBox.y - vBox.x) * vGrow;
 em += uBuild * smoothstep(top - .16, top, vY) * (1.0 - vGrow) * step(.002, vGrow) * mix(1.6, .3, roof);
 totalEmissiveRadiance += em;`;
function towerMaterial(tu) {
 const m = new THREE.MeshStandardMaterial({ roughness: .42, metalness: .2 });
 m.onBeforeCompile = shader => {
  Object.assign(shader.uniforms, tu);
  shader.vertexShader = shader.vertexShader.replace('#include <common>', `#include <common>\n${TOWER_HEAD}`)
   .replace('#include <begin_vertex>', `#include <begin_vertex>
    vL = position * vec3(length(instanceMatrix[0].xyz), length(instanceMatrix[1].xyz), length(instanceMatrix[2].xyz)); vNo = normal; vBox = aBox; vGrow = aGrow;`)
   .replace('#include <project_vertex>', `#include <project_vertex>\n vY = (modelMatrix * instanceMatrix * vec4(transformed, 1.0)).y;`);
  shader.fragmentShader = shader.fragmentShader.replace('#include <common>', `#include <common>\n${TOWER_FRAG_HEAD}`)
   .replace('#include <color_fragment>', `#include <color_fragment>\n${TOWER_FRAG}`);
 };
 m.customProgramCacheKey = () => 'kfm-history-tower';
 return m;
}
const TUBE_VERT = 'varying float vU; void main() { vU = uv.x; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }';
const TUBE_FRAG = `uniform float uReveal; uniform float uOp; uniform float uTime; uniform vec3 uColor; varying float vU;
 void main() {
  if (vU > uReveal) discard;
  float p = fract(vU * 9.0 - uTime * .2), pulse = smoothstep(0.0, .03, p) * (1.0 - smoothstep(.03, .16, p));
  gl_FragColor = vec4(uColor * (.4 + pulse * 2.4), uOp);
  #include <colorspace_fragment>
 }`;
const SKY_FRAG = `uniform vec3 uTop; uniform vec3 uLow; uniform vec3 uGlow; uniform vec3 uGlowDir; uniform float uStars; varying vec3 vW;
 void main() {
  vec3 d = normalize(vW - cameraPosition);
  vec3 c = mix(uLow, uTop, smoothstep(-.72, -.04, d.y));
  float g = max(dot(d, uGlowDir), 0.0);
  c += uGlow * (pow(g, 5.0) * .22 + pow(g, 30.0) * .22) * smoothstep(-.85, -.1, d.y);
  float s = fract(sin(dot(floor(d * 260.0), vec3(12.9898, 78.233, 45.164))) * 43758.5453);
  c += vec3(.75, .85, 1.0) * step(.9988, s) * uStars * .7 * smoothstep(-.6, -.12, d.y);
  gl_FragColor = vec4(c, 1.0);
  #include <colorspace_fragment>
 }`;

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 const { key, hemi, rim } = stage(scene, { fog: .02 });
 const random = rng(1920);

 // Sky backdrop: a gradient dome with a glow band and a few stars at night.
 const su = { uTop: { value: new THREE.Color() }, uLow: { value: new THREE.Color() }, uGlow: { value: new THREE.Color() }, uGlowDir: { value: new THREE.Vector3(-.78, -.16, .6).normalize() }, uStars: { value: 0 } };
 const sky = new THREE.Mesh(new THREE.SphereGeometry(95, 40, 20), new THREE.ShaderMaterial({ uniforms: su, side: THREE.BackSide, depthWrite: false, fog: false,
  vertexShader: 'varying vec3 vW; void main() { vW = (modelMatrix * vec4(position, 1.0)).xyz; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }', fragmentShader: SKY_FRAG }));
 sky.renderOrder = -10; sky.frustumCulled = false;
 scene.add(sky);

 // Land: plains, a bluff, a river; the ground shader adds every era's surface.
 const land = terrain({ segments: 200, height, relief: 1, color: paint });
 const gs = gridSampler(land, 1);
 const gu = { uCamp: { value: FIRES.map(([x, z]) => new THREE.Vector4(x, z, .85, 0)) }, uTown: { value: new THREE.Vector4(...G, 0, 1) }, uDown: { value: new THREE.Vector4(...DT, 0, 1) }, uFut: { value: new THREE.Vector4(...FC, 0, 1) }, uLane: { value: C('#3fc8f0') } };
 const gm = land.mesh.material;
 gm.onBeforeCompile = shader => {
  Object.assign(shader.uniforms, gu);
  shader.vertexShader = shader.vertexShader.replace('#include <common>', '#include <common>\n varying vec3 vWP; varying float vNy;')
   .replace('#include <project_vertex>', '#include <project_vertex>\n vWP = (modelMatrix * vec4(transformed, 1.0)).xyz; vNy = normal.y;');
  shader.fragmentShader = shader.fragmentShader.replace('#include <common>', `#include <common>\n${GROUND_HEAD}`)
   .replace('#include <emissivemap_fragment>', `#include <emissivemap_fragment>\n${GROUND_FRAG}`);
 };
 gm.customProgramCacheKey = () => 'kfm-history-ground';
 const water = riverWater(land.sample, { from: -3.45, width: .28 });
 scene.add(land.mesh, blockSides(land.sample), water);

 // The cave and the figure who walks out of it.
 const cave = outcrop(), caveY = land.sample(CAVE.x, CAVE.z) - .02;
 cave.position.set(CAVE.x, caveY, CAVE.z); cave.rotation.y = Math.atan2(N[0], N[1]);
 const hero = walker();
 const shadow = new THREE.Mesh(new THREE.PlaneGeometry(.55, .55).rotateX(-Math.PI / 2), new THREE.MeshBasicMaterial({ map: glowTexture(), color: '#000000', transparent: true, depthWrite: false }));
 shadow.renderOrder = 2;
 scene.add(cave, hero.root, shadow);
 const P0 = [CAVE.x - N[0] * .52, CAVE.z - N[1] * .52], P1 = [CAVE.x + N[0] * .42, CAVE.z + N[1] * .42];
 const P2 = [FIRES[0][0] + Math.cos(-2.75) * .3, FIRES[0][1] + Math.sin(-2.75) * .3];

 // Lodges: three around the first fire, then rings around three more as the village grows.
 const lodges = [];
 const fits = (x, z, r) => onLand(x, z, .55) && dist([x, z], [CAVE.x, CAVE.z]) > 1 && lodges.every(l => dist([x, z], [l.x, l.z]) > r + l.r) && FIRES.every(f => dist([x, z], f) > .42)
  && Math.abs((x - P1[0]) * (P2[1] - P1[1]) - (z - P1[1]) * (P2[0] - P1[0])) / dist(P1, P2) > .3;
 const addLodge = (x, z, fire, dome, t0) => lodges.push({ x, z, r: dome ? .23 : .21, fire, dome, t0, rot: Math.atan2(FIRES[fire][0] - x, FIRES[fire][1] - z), shade: .8 + .25 * random() });
 [1.1, 1.95, 2.8].forEach((a, i) => addLodge(FIRES[0][0] + Math.cos(a) * .62, FIRES[0][1] + Math.sin(a) * .62, 0, false, 6.1 + i * .45));
 for (let f = 0; f < 4; f++) {
  const n = f ? 5 : 4, a0 = random() * TAU;
  for (let k = 0; k < n * 3 && lodges.filter(l => l.fire === f).length < (f ? n : 7); k++) {
   const a = a0 + k / n * TAU + random() * .4, rr = (f ? .58 : 1.05) + random() * .18, x = FIRES[f][0] + Math.cos(a) * rr, z = FIRES[f][1] + Math.sin(a) * rr;
   if (fits(x, z, .2)) addLodge(x, z, f, random() < .35, 0);
  }
 }
 for (const l of lodges) if (!l.t0) l.t0 = 11.6 + 2.2 * clamp(dist([l.x, l.z], FIRES[0]) / 2.2);
 for (const l of lodges) l.t1 = 16.4 + .8 * clamp(dist([l.x, l.z], G) / 2.5);
 const hideTone = (l, out) => out.set(l.dome ? '#b08e68' : '#dcbc90').multiplyScalar(l.shade);
 const cones = lodges.filter(l => !l.dome), domes = lodges.filter(l => l.dome);
 const coneGeo = bake([
  [new THREE.ConeGeometry(.2, .44, 11, 1, true).translate(0, .22, 0), '#ffffff'],
  ...[0, 1, 2, 3, 4].map(k => [new THREE.CylinderGeometry(.005, .005, .18, 3).translate(0, .09, 0).rotateZ(.32).rotateY(k / 5 * TAU + .4).translate(0, .37, 0), '#6a5038']),
  [new THREE.PlaneGeometry(.08, .11).rotateX(-.43).translate(0, .056, .178), '#2a1e15'],
 ]);
 const domeGeo = bake([
  [new THREE.SphereGeometry(.22, 12, 5, 0, TAU, 0, Math.PI / 2).scale(1, .7, 1), '#ffffff'],
  [Box(.085, .085, .1, 0, .042, .2), '#d8c8ae'], [new THREE.PlaneGeometry(.055, .065).translate(0, .034, .2505), '#2a1e15'],
 ]);
 const lodgeMat = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .92 }), lodgeU = { uFireGlow: { value: 0 } };
 lodgeMat.onBeforeCompile = shader => { // lodges face their fire on local +z, so that side catches its glow
  Object.assign(shader.uniforms, lodgeU);
  shader.vertexShader = shader.vertexShader.replace('#include <common>', '#include <common>\n varying float vFace;').replace('#include <begin_vertex>', '#include <begin_vertex>\n vFace = normal.z;');
  shader.fragmentShader = shader.fragmentShader.replace('#include <common>', '#include <common>\n uniform float uFireGlow; varying float vFace;')
   .replace('#include <emissivemap_fragment>', '#include <emissivemap_fragment>\n totalEmissiveRadiance += diffuseColor.rgb * vec3(1.0, .55, .28) * uFireGlow * (.12 + .5 * max(vFace, 0.0));');
 };
 lodgeMat.customProgramCacheKey = () => 'kfm-history-lodge';
 const coneMesh = instanced(coneGeo, lodgeMat, cones.length, (i, o) => hideTone(cones[i], o));
 const domeMesh = instanced(domeGeo, lodgeMat, domes.length, (i, o) => hideTone(domes[i], o));
 for (const l of lodges) l.y = land.sample(l.x, l.z) - .01;
 scene.add(coneMesh, domeMesh);

 // Fires: logs and stones, flames, sparks, a light pool and a real point light each.
 const hearthGeo = bake([
  ...[0, 1, 2].map(k => [new THREE.CylinderGeometry(.012, .012, .15, 5).rotateZ(Math.PI / 2).rotateY(k / 3 * Math.PI).translate(0, .016, 0), '#3d2a1c']),
  ...[...Array(8).keys()].map(k => [new THREE.DodecahedronGeometry(.022).translate(Math.cos(k / 8 * TAU) * .1, .01, Math.sin(k / 8 * TAU) * .1), '#77716a']),
 ]);
 const hearths = instanced(hearthGeo, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 1 }), 4);
 const poolMat = new THREE.MeshBasicMaterial({ map: glowTexture(), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending });
 const pools = instanced(new THREE.PlaneGeometry(1, 1).rotateX(-Math.PI / 2), poolMat, 4, (i, o) => o.setRGB(0, 0, 0));
 pools.renderOrder = 3;
 const fireY = FIRES.map(([x, z]) => land.sample(x, z));
 const SPARKS = 24, fireGlow = glowPoints(FIRES.length * (4 + SPARKS), { size: .3, color: '#ffa04a' });
 const lights = [0, 1, 2].map(() => { const l = new THREE.PointLight('#ff9a48', 0, 5, 2); scene.add(l); return l; });
 scene.add(hearths, pools, fireGlow);

 // People: the camp's own, who come out of their lodges to the fire, and 1920s walkers in hats.
 const bodyGeo = bake([
  [Box(.018, .09, .02, -.014, .045, 0), '#ffffff'], [Box(.018, .09, .02, .014, .045, 0), '#ffffff'],
  [new THREE.CylinderGeometry(.03, .046, .11, 7).translate(0, .14, 0), '#ffffff'],
  [Box(.015, .085, .017, -.042, .15, 0), '#ffffff'], [Box(.015, .085, .017, .042, .15, 0), '#ffffff'],
 ]);
 const camp = [];
 for (const [i, l] of lodges.entries()) {
  if (i > 2 && random() < .25) continue;
  const f = FIRES[l.fire], a = Math.atan2(l.z - f[1], l.x - f[0]) + (random() - .5) * .5, door = [l.x + Math.sin(l.rot) * .26, l.z + Math.cos(l.rot) * .26];
  camp.push({ door, spot: [f[0] + Math.cos(a) * .3, f[1] + Math.sin(a) * .3], fire: f, tOut: (l.t0 || 11.6) + .9 + random() * .5, roam: i > 2 && random() < .6, period: 7 + random() * 5, sink: l.t1 });
 }
 const walkers = [];
 const townBlocks = [];
 for (let i = -3; i <= 4; i++) for (let j = -3; j <= 3; j++) {
  const x0 = XS + i * BX, z0 = ZS + j * BZ, c = [x0 + BX / 2, z0 + BZ / 2];
  if (dist(c, G) > 3.3 || x0 < -3.25) continue;
  let ok = true;
  for (let a = 0; a <= 1; a += .5) for (let b = 0; b <= 1; b += .5) if (!onLand(x0 + a * BX, z0 + b * BZ, .5) || height(x0 + a * BX, z0 + b * BZ) > .45) ok = false;
  if (ok) townBlocks.push({ x0, z0, c, dn: dist(c, G) / 3.3, down: dist(c, DT) < 1.75 });
 }
 for (const b of townBlocks) if (b.dn < .75 && random() < .8) {
  const n = 1 + (random() < .4);
  for (let k = 0; k < n; k++) walkers.push({ x0: b.x0 + WALK, z0: b.z0 + WALK, w: BX - 2 * WALK, d: BZ - 2 * WALK, phase: random(), speed: (.05 + .03 * random()) * (random() < .5 ? 1 : -1) });
 }
 walkers.length = Math.min(walkers.length, 26);
 const PEOPLE = camp.length + walkers.length;
 const CAMP_CLOTH = ['#8a6a48', '#7b5a3e', '#9a7a55', '#6e5240', '#a3835e'], TOWN_CLOTH = ['#2f3440', '#3b3530', '#6a3030', '#2e4636', '#d8cfbd', '#4a4d55', '#7a6a4a'];
 const SKIN = ['#8d5f3f', '#7a4f35', '#a06c48', '#c89272', '#d9a787', '#6a432c'];
 const crowdMat = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .85 });
 const crowd = instanced(bodyGeo, crowdMat, PEOPLE, (i, o) => o.set(i < camp.length ? CAMP_CLOTH[i % 5] : TOWN_CLOTH[i % 7]));
 const heads = instanced(new THREE.IcosahedronGeometry(.021, 1).translate(0, .218, 0), new THREE.MeshStandardMaterial({ roughness: .8 }), camp.length, (i, o) => o.set(SKIN[i % 4]));
 const hatGeo = bake([[new THREE.IcosahedronGeometry(.021, 1).translate(0, .218, 0), '#ffffff'], [new THREE.CylinderGeometry(.031, .031, .005, 10).translate(0, .232, 0), '#2a2522'], [new THREE.CylinderGeometry(.018, .02, .024, 10).translate(0, .245, 0), '#2a2522']]);
 const hats = instanced(hatGeo, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .8 }), walkers.length, (i, o) => o.set(SKIN[(i * 5 + 2) % 6]));
 scene.add(crowd, heads, hats);

 // 1920s town: porch houses facing the streets, street trees, lamps and Model Ts.
 const houses = [], trees = [];
 for (const b of townBlocks) for (const row of [0, 1]) for (let k = 0; k < 3; k++) {
  const x = b.x0 + ROAD + .165 + k * .33, z = row ? b.z0 + BZ - .32 : b.z0 + .32;
  if (random() < .12 || dist([x, z], [CAVE.x, CAVE.z]) < 1.1) continue;
  const dn = dist([x, z], G) / 3.3, down = dist([x, z], DT) < 1.75;
  houses.push({ x, z, y: land.sample(x, z) - .005, rot: row ? 0 : Math.PI, s: .92 + .16 * random(), tall: random() < .3 ? 1.35 : 1, t0: 16.2 + 1.3 * dn + .2 * random(), t1: down ? 22 + .7 * dist([x, z], DT) / 1.75 : 28.2 + .8 * random(), lit: random() });
  if (k && random() < .55) trees.push({ x: b.x0 + ROAD + k * .33, z: row ? b.z0 + BZ - .1 : b.z0 + .1, s: .8 + .4 * random(), t0: 16.8 + 1.3 * dn, t1: down ? 22.1 : 28.3 + .6 * random(), green: random() });
 }
 const houseGeo = bake([
  [Box(.22, .18, .22, 0, .09, 0), '#ffffff'],
  [new THREE.ExtrudeGeometry(new THREE.Shape([new THREE.Vector2(-.135, 0), new THREE.Vector2(.135, 0), new THREE.Vector2(0, .12)]), { depth: .25, bevelEnabled: false }).translate(0, .18, -.125), '#5b4a42'],
  [Box(.2, .016, .075, 0, .008, .147), '#cfc6b8'], [Box(.22, .012, .085, 0, .118, .148), '#ffffff'],
  [Box(.012, .11, .012, -.09, .063, .18), '#f2efe8'], [Box(.012, .11, .012, .09, .063, .18), '#f2efe8'],
  [Box(.032, .09, .032, .06, .25, -.05), '#8a4a3a'], [Box(.05, .085, .004, 0, .044, .111), '#4a3a30'],
 ]);
 const winGeo = bake([
  ...[-.065, .065].map(x => [new THREE.PlaneGeometry(.04, .05).translate(x, .085, .1115), '#ffffff']),
  ...[-1, 1].flatMap(s => [-.05, .05].map(z => [new THREE.PlaneGeometry(.045, .05).rotateY(s * Math.PI / 2).translate(s * .1115, .1, z), '#ffffff'])),
  [new THREE.PlaneGeometry(.045, .05).rotateY(Math.PI).translate(0, .1, -.1115), '#ffffff'], [new THREE.PlaneGeometry(.035, .035).translate(0, .22, .1265), '#ffffff'],
 ]);
 const PAINT = ['#efe6d2', '#f4f1ea', '#e9d9a8', '#b9c7a6', '#c98e74', '#d7dde0', '#e6c9a0'];
 const houseMesh = instanced(houseGeo, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .85 }), houses.length, (i, o) => o.set(PAINT[i % PAINT.length]));
 const winMat = new THREE.MeshBasicMaterial({ color: '#ffffff' });
 const winMesh = instanced(winGeo, winMat, houses.length, (i, o) => o.set('#ffc777').multiplyScalar(houses[i].lit < .2 ? .05 : .55 + .45 * houses[i].lit));
 // Cottonwoods line the river from the first dawn until the future city replaces them.
 for (let k = 0; k < 140 && trees.length < 110; k++) {
  const x = lerp(-3.3, 5.7, random()), side = random() < .5 ? -1 : 1, z = riverZ(x) + side * (.36 + random() * .3);
  if (Math.abs(z) < 5.7 && townBlocks.every(b => !(x > b.x0 && x < b.x0 + BX && z > b.z0 && z < b.z0 + BZ))) trees.push({ x, z, s: 1.2 + .6 * random(), t0: -1, t1: 28.5 + .8 * random(), regrow: 34.4 + .6 * random(), green: random() });
 }
 for (const tr of trees) tr.y = land.sample(tr.x, tr.z) - .01;
 const treeGeo = bake([[new THREE.CylinderGeometry(.008, .012, .08, 5).translate(0, .04, 0), '#5a4430'], [new THREE.IcosahedronGeometry(.07, 0).scale(1, 1.15, 1).translate(0, .125, 0), '#ffffff']]);
 const treeMesh = instanced(treeGeo, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .9 }), trees.length, (i, o) => o.set('#3f6a34').lerp(TMP.set('#7a8a3c'), trees[i].green * .6));
 scene.add(houseMesh, winMesh, treeMesh);

 const lamps = [];
 for (let i = -3; i <= 4; i++) for (let j = -3; j <= 4; j++) {
  const x = XS + i * BX + .075, z = ZS + j * BZ + .075, dn = dist([x, z], G) / 3.3;
  if (dn < 1 && onLand(x, z, .45) && height(x, z) < .45 && x > -3.2 && dist([x, z], [CAVE.x, CAVE.z]) > 1) lamps.push({ x, z, y: land.sample(x, z), t0: 16.8 + 1.3 * dn, on: 17.8 + .9 * dn, t1: dist([x, z], DT) < 1.9 ? 22.2 : 28.3 + .6 * random() });
 }
 const postMesh = instanced(bake([[new THREE.CylinderGeometry(.006, .008, .19, 4).translate(0, .095, 0), '#2b2b2b'], [Box(.024, .02, .024, 0, .198, 0), '#3a3a3a']]), new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .6 }), lamps.length);
 const LOOPS = [[-2.1, -3.3], [-1, -2.4], [.1, -3.3], [-1, -4.2], [1.2, -2.4], [-2.1, -4.2]].filter(([x0, z0]) => townBlocks.some(b => Math.abs(b.x0 - x0) < .01 && Math.abs(b.z0 - z0) < .01));
 const cars = LOOPS.flatMap(([x0, z0], i) => [0, .5].map(ph => ({ x0: x0 + .028, z0: z0 + .028, w: BX - .056, d: BZ - .056, phase: ph + i * .13, speed: (.2 + .05 * (i % 3)) * (i % 2 ? 1 : -1) })));
 const carGeo = bake([
  [Box(.1, .045, .2, 0, .055, 0), '#ffffff'], [Box(.092, .065, .085, 0, .11, -.035), '#ffffff'], [Box(.098, .007, .095, 0, .146, -.035), '#141414'],
  [Box(.07, .02, .055, 0, .084, .02), '#a9c7d4'], [Box(.06, .05, .012, 0, .062, .104), '#b89a5a'],
  ...[-1, 1].flatMap(sx => [-1, 1].map(sz => [new THREE.CylinderGeometry(.027, .027, .014, 10).rotateZ(Math.PI / 2).translate(sx * .052, .027, sz * .065), '#121212'])),
 ]);
 const carMesh = instanced(carGeo, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .35, metalness: .3 }), cars.length, (i, o) => o.set(['#1e1f22', '#22261f', '#2a1f1c', '#1d2129'][i % 4]));
 const townGlow = glowPoints(lamps.length * 2 + cars.length * 2, { size: .2, color: '#ffd28a' });
 for (let i = 0; i < lamps.length; i++) townGlow.sizes[lamps.length + i] = .85;
 scene.add(postMesh, carMesh, townGlow);

 // Towers: today's downtown, then the slender towers of an imagined future.
 const tu = { uWin: { value: 0 }, uFut: { value: 0 }, uTime: { value: 0 }, uBuild: { value: C('#ffd28a') } };
 const tmat = towerMaterial(tu);
 const today = [], future = [], boxSegs = [], cylSegs = [];
 for (const b of townBlocks) {
  if (dist(b.c, DT) > 1.95) continue;
  const two = random() < .5, d = dist(b.c, DT);
  for (let k = 0; k < (two ? 2 : 1); k++) {
   const w = two ? .36 + .06 * random() : .6 + .22 * random(), dp = .48 + .18 * random(), x = two ? b.x0 + .3 + k * .5 : b.c[0] + (random() - .5) * .08;
   const H = (.8 + 2.7 * Math.exp(-((d / 1.25) ** 2))) * (.75 + .5 * random()), z = b.c[1] + (random() - .5) * .06;
   today.push({ x, z, w, d: dp, H, y: land.sample(x, z) - .01, t0: 22.6 + 1.1 * d / 1.95, t1: 33.9 + .5 * random(), style: random() < .7 ? 0 : 1 });
  }
 }
 const roadGap = (x, z, r) => { const dx = Math.abs((((x - XS) / BX + .5) % 1 + 1) % 1 - .5) * BX, dz = Math.abs((((z - ZS) / BZ + .5) % 1 + 1) % 1 - .5) * BZ; return Math.min(dx, dz) > ROAD + r + .03; };
 for (let k = 0; k < 6000 && future.length < 190; k++) {
  const x = lerp(-5.55, 5.55, random()), z = lerp(-5.55, 5.55, random()), r = .1 + .1 * random();
  if (!onLand(x, z, .48) || dist([x, z], [CAVE.x, CAVE.z]) < 1.5 || !roadGap(x, z, r)) continue;
  if (today.some(o => Math.abs(x - o.x) < o.w / 2 + r + .08 && Math.abs(z - o.z) < o.d / 2 + r + .08) || future.some(o => dist([x, z], [o.x, o.z]) < o.r + r + .14)) continue;
  const y = land.sample(x, z) - .01, dc = dist([x, z], FC);
  const H = (1.1 + 5 * Math.exp(-((dc / 2.7) ** 2))) * (.7 + .55 * random()) * (y > .8 ? .75 : 1);
  future.push({ x, z, r, y, H, cyl: random() < .62, dc, seed: random(), t0: 28.4 + 1.7 * clamp(dc / 7), t1: 33.4 + .8 * (1 - clamp(dc / 7)) });
 }
 for (const o of today) {
  const seg = (f0, f1, sw) => boxSegs.push({ o, f0, f1, sw, style: o.style });
  if (o.H > 1.6) { seg(0, .62, 1); seg(.62, 1, .72); } else seg(0, 1, 1);
  if (o.H > 2.8) cylSegs.push({ o, f0: 1, f1: 1.16, sw: .08, style: 3, spire: true });
 }
 for (const o of future) {
  (o.cyl ? cylSegs : boxSegs).push({ o, f0: 0, f1: 1, sw: 1, style: 2, fut: true });
  if (o.H > 3) cylSegs.push({ o, f0: 1, f1: 1.1, sw: .55, style: 2, fut: true });
  if (o.H > 4.6) cylSegs.push({ o, f0: 1.1, f1: 1.22, sw: .1, style: 3, fut: true });
 }
 const towerMesh = (geo, segs) => {
  const box = new Float32Array(segs.length * 4);
  segs.forEach((s, i) => box.set([s.o.y, s.o.y + s.o.H * s.f1, s.o.seed ?? (i * .618) % 1, s.style], i * 4));
  geo.setAttribute('aBox', new THREE.InstancedBufferAttribute(box, 4));
  const grow = new THREE.InstancedBufferAttribute(new Float32Array(segs.length), 1); grow.setUsage(THREE.DynamicDrawUsage);
  geo.setAttribute('aGrow', grow);
  const mesh = instanced(geo, tmat, segs.length, (i, o) => segs[i].fut ? o.setRGB(.92 + .08 * segs[i].o.seed, .96, 1) : o.setRGB(.9 + .1 * random(), .95, 1));
  mesh.grow = grow; mesh.segs = segs;
  return mesh;
 };
 const boxTowers = towerMesh(new THREE.BoxGeometry(1, 1, 1).translate(0, .5, 0), boxSegs);
 const cylTowers = towerMesh(new THREE.CylinderGeometry(.4, .5, 1, 8).translate(0, .5, 0), cylSegs);
 scene.add(boxTowers, cylTowers);

 // Sky bridges between neighbouring tall towers, three transit loops and holographic rings.
 const bridges = [];
 for (let i = 0; i < future.length && bridges.length < 30; i++) for (let j = i + 1; j < future.length; j++) {
  const a = future[i], b = future[j], d = dist([a.x, a.z], [b.x, b.z]);
  if (d < .5 || d > 1.05 || a.H < 2.2 || b.H < 2.2 || random() > .35) continue;
  const lo = Math.max(a.y, b.y) + .7, hi = Math.min(a.y + a.H, b.y + b.H) - .35;
  if (hi > lo) bridges.push({ x: (a.x + b.x) / 2, z: (a.z + b.z) / 2, y: lerp(lo, hi, random()), len: d, rot: Math.atan2(b.x - a.x, b.z - a.z), t0: 29.8 + .9 * random(), t1: 33.1 + .3 * random() });
  if (bridges.length >= 30) break;
 }
 const bridgeMat = new THREE.MeshStandardMaterial({ color: '#b8c8d4', emissive: '#4cd2ff', emissiveIntensity: 0, roughness: .3, metalness: .4 });
 const bridgeMesh = instanced(new THREE.BoxGeometry(1, 1, 1), bridgeMat, bridges.length);
 const tubes = [[2.3, 1.3, '#4fe0ff', 0], [3.5, 2.1, '#ff6fd8', 1.3], [4.7, 1.7, '#7fffd0', 2.6]].map(([R, y0, col, ph]) => {
  const pts = Array.from({ length: 48 }, (_, i) => { const a = i / 48 * TAU; const rr = R * (1 + .12 * Math.sin(3 * a + ph)); return new THREE.Vector3(FC[0] + Math.cos(a) * rr, y0 + .3 * Math.sin(2 * a + ph), FC[1] + Math.sin(a) * rr * .85); });
  const uniforms = { uReveal: { value: 0 }, uOp: { value: 0 }, uTime: { value: 0 }, uColor: { value: C(col) } };
  const mesh = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts, true), 260, .022, 5, true), new THREE.ShaderMaterial({ uniforms, vertexShader: TUBE_VERT, fragmentShader: TUBE_FRAG, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending }));
  mesh.renderOrder = 4; scene.add(mesh);
  return { mesh, uniforms, ph };
 });
 const tall = [...future].sort((a, b) => b.H - a.H);
 const ringHosts = tall.slice(0, 12), beamHosts = tall.slice(0, 4);
 const ringMat = new THREE.MeshBasicMaterial({ transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide });
 const rings = instanced(new THREE.RingGeometry(.92, 1, 48).rotateX(-Math.PI / 2), ringMat, ringHosts.length, (i, o) => o.set(i % 3 ? '#4fdcff' : '#ff7ae0'));
 rings.renderOrder = 4;
 const beamGeo = new THREE.CylinderGeometry(.03, .08, 1.2, 12, 1, true).translate(0, .6, 0), bc = [], ba = beamGeo.attributes.position;
 for (let i = 0; i < ba.count; i++) { const v = 1 - ba.getY(i) / 1.2; bc.push(v * .5, v * .9, v); }
 beamGeo.setAttribute('color', new THREE.Float32BufferAttribute(bc, 3));
 const beamMat = new THREE.MeshBasicMaterial({ vertexColors: true, transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide });
 const beams = instanced(beamGeo, beamMat, beamHosts.length);
 beamHosts.forEach((o, i) => put(beams, i, o.x, o.y + o.H * 1.22, o.z, 0, 1));
 beams.renderOrder = 4;
 scene.add(bridgeMesh, rings, beams);

 // Street light streams (today, then the whole future grid), flying craft, crowns and warning beacons.
 const lanes = [];
 for (let j = -3; j <= 9; j++) { const z = ZS + j * BZ; if (Math.abs(z) < 5.6) lanes.push({ alongX: true, c: z, a: -3.3, b: 5.6 }); }
 for (let i = -2; i <= 6; i++) { const x = XS + i * BX; if (x > -3.3 && x < 5.6) lanes.push({ alongX: false, c: x, a: -5.6, b: 5.6 }); }
 const flow = [];
 for (const [li, l] of lanes.entries()) for (const dir of [1, -1]) for (let k = 0; k < 13; k++) flow.push({ l, li, dir, phase: random(), speed: (.45 + .25 * random()) / (l.b - l.a) });
 const CRAFT = 70, cityGlow = glowPoints(flow.length + CRAFT * 3 + future.length + today.length, { size: .12, color: '#ffffff' });
 const craft = Array.from({ length: CRAFT }, () => ({ R: 1.2 + 4.8 * random(), y: 1.8 + 4.6 * random(), w: (.12 + .2 * random()) * (random() < .5 ? 1 : -1), a0: random() * TAU, ecc: .7 + .3 * random(), amber: random() < .2 }));
 const FLAME = [C('#ff7a2a'), C('#ffc45a'), C('#ff9a3a'), C('#ff8a3a')], EMBER = C('#ffb860'), POOL = C('#ff8a3a');
 const RED = C('#ff3b2f'), WHITE = C('#fff4e0'), TAIL = C('#ff4a36'), CYAN = C('#7fe8ff'), MAG = C('#ff86e6'), AMBER = C('#ffc36a'), LAMP = C('#ffcf7a');
 const F0 = flow.length, F1 = F0 + CRAFT * 3, F2 = F1 + future.length;
 for (let i = 0; i < CRAFT; i++) for (let k = 0; k < 3; k++) cityGlow.sizes[F0 + i * 3 + k] = [.16, .1, .07][k];
 for (let i = 0; i < future.length; i++) { cityGlow.sizes[F1 + i] = .18; (future[i].seed > .75 ? MAG : CYAN).toArray(cityGlow.colors, (F1 + i) * 3); }
 for (let i = 0; i < today.length; i++) { cityGlow.sizes[F2 + i] = .14; RED.toArray(cityGlow.colors, (F2 + i) * 3); }
 scene.add(cityGlow);

 const keyDir = new THREE.Vector3(), tmpA = new THREE.Vector3(), pt = [0, 0, 0, 0], pa = [0, 0], pb = [0, 0];
 function setGlow(g, i, x, y, z, a, col) { g.positions[i * 3] = x; g.positions[i * 3 + 1] = y; g.positions[i * 3 + 2] = z; g.alphas[i] = a; if (col) col.toArray(g.colors, i * 3); }

 function heroAt(t, out) { // position along the cave → ledge → fire path, and distance walked
  const L1 = dist(P0, P1), L2 = dist(P1, P2);
  if (t > 35) { out[0] = P0[0]; out[1] = P0[1]; return 0; } // back in the dark for the loop
  if (t < 3) { const s = smooth(.7, 3, t); out[0] = lerp(P0[0], P1[0], s); out[1] = lerp(P0[1], P1[1], s); return s * L1; }
  const s = smooth(4.4, 7, t); out[0] = lerp(P1[0], P2[0], s); out[1] = lerp(P1[1], P2[1], s); return L1 + s * L2;
 }
 function campAt(p, t, out) {
  const s = smooth(p.tOut, p.tOut + 1.8, t), tr = p.tOut + 1.8;
  const u = p.roam && t > tr ? .5 - .5 * Math.cos(TAU * (t - tr) / p.period) : 0;
  out[0] = lerp(lerp(p.door[0], p.spot[0], s), p.door[0], u); out[1] = lerp(lerp(p.door[1], p.spot[1], s), p.door[1], u);
 }

 function update(t) {
  // Time of day: sky, fog, key, fill and rim follow the era.
  const [ma, mb, mf] = keyed(MOOD_KEYS, t);
  su.uTop.value.copy(ma.top).lerp(mb.top, mf); su.uLow.value.copy(ma.low).lerp(mb.low, mf); su.uGlow.value.copy(ma.glow).lerp(mb.glow, mf);
  su.uStars.value = lerp(ma.stars, mb.stars, mf);
  scene.fog.color.copy(su.uLow.value).lerp(su.uTop.value, .35); scene.background.copy(su.uLow.value);
  key.color.copy(ma.key).lerp(mb.key, mf); key.intensity = lerp(ma.keyI, mb.keyI, mf);
  keyDir.fromArray(ma.dir).normalize().lerp(tmpA.fromArray(mb.dir).normalize(), mf).normalize();
  key.position.copy(keyDir).multiplyScalar(14);
  hemi.color.copy(ma.sky).lerp(mb.sky, mf); hemi.groundColor.copy(ma.ground).lerp(mb.ground, mf); hemi.intensity = lerp(ma.hemiI, mb.hemiI, mf);
  rim.intensity = lerp(ma.rimI, mb.rimI, mf);

  // Beat 1 (0–6 s): the figure walks out of the dark mouth, pauses on the ledge at dawn, then heads down to the flat.
  const hp = [0, 0], walked = heroAt(t, hp), ahead = [0, 0];
  heroAt(t + .05, ahead);
  const moving = Math.hypot(ahead[0] - hp[0], ahead[1] - hp[1]) > 1e-4;
  const inside = (hp[0] - CAVE.x) * N[0] + (hp[1] - CAVE.z) * N[1];
  const shown = t < 17.3 || t > 35.2, heroScale = t > 35.2 ? 1 : 1 - smooth(16.6, 17.3, t);
  hero.root.visible = shown && heroScale > .01;
  const hy = inside < .3 ? caveY + .02 : gs(hp[0], hp[1]);
  hero.root.position.set(hp[0], hy, hp[1]); hero.root.scale.setScalar(HERO * Math.max(heroScale, 1e-3));
  hero.root.rotation.y = moving ? Math.atan2(ahead[0] - hp[0], ahead[1] - hp[1]) : t < 4.4 || t > 35 ? Math.atan2(N[0], N[1]) : Math.atan2(FIRES[0][0] - hp[0], FIRES[0][1] - hp[1]);
  const phase = walked / .075 * Math.PI, swing = moving ? Math.sin(phase) : 0;
  hero.legs[0].rotation.x = .55 * swing; hero.legs[1].rotation.x = -.55 * swing; hero.arms[0].rotation.x = -.4 * swing; hero.arms[1].rotation.x = .4 * swing;
  hero.body.position.y = moving ? .006 * Math.abs(Math.cos(phase)) : .002 * Math.sin(t * 1.7);
  hero.head.rotation.y = .55 * Math.sin(smooth(3.1, 4.3, t) * TAU) * (t < 4.4 ? 1 : 0); // looks out across the plains
  const lit = lerp(.04, 1, smooth(-.4, .2, inside));
  hero.cloth.color.copy(hero.clothBase).multiplyScalar(lit); hero.skin.color.copy(hero.skinBase).multiplyScalar(lit);
  hero.cloth.emissive.setRGB(.5, .26, .1).multiplyScalar(.35 * lit); hero.skin.emissive.setRGB(.6, .3, .12).multiplyScalar(.35 * lit); // warm rim so it parts from the dark mouth
  shadow.position.set(hp[0], hy + .012, hp[1]); shadow.scale.setScalar(heroScale); shadow.visible = hero.root.visible;
  shadow.material.opacity = .6 * smooth(-.2, .3, inside);

  // Beats 2–3 (6–17 s): lodges rise around the first fire, then rings of lodges and new fires as the village grows.
  let ci = 0, di = 0;
  for (const l of lodges) {
   const g = life(t, l.t0, .9, l.t1, .7);
   put(l.dome ? domeMesh : coneMesh, l.dome ? di++ : ci++, l.x, l.y, l.z, l.rot, (.6 + .4 * g) * g, g, (.6 + .4 * g) * g);
  }
  coneMesh.instanceMatrix.needsUpdate = domeMesh.instanceMatrix.needsUpdate = true;
  coneMesh.visible = domeMesh.visible = t > 6 && t < 18.2;
  let gi = 0;
  FIRES.forEach(([x, z], f) => {
   const level = smooth(IGNITE[f], IGNITE[f] + .7, t) * (1 - smooth(16.5, 17.2, t)), y = fireY[f];
   const flick = .82 + .1 * Math.sin(t * 17 + f * 3) + .08 * Math.sin(t * 29.7 + f * 1.3);
   put(hearths, f, x, y, z, f, Math.max(smooth(IGNITE[f] - .4, IGNITE[f], t) * (1 - smooth(16.9, 17.5, t)), 1e-4));
   put(pools, f, x, y + .03, z, 0, 2.4 * level * (.95 + .05 * flick));
   pools.setColorAt(f, TMP.copy(POOL).multiplyScalar(.55 * level * flick));
   gu.uCamp.value[f].w = smooth(IGNITE[f] - .6, IGNITE[f] + 1.2, t) * (1 - smooth(16.6, 18, t));
   gu.uCamp.value[f].z = f ? .85 : lerp(.85, 1.3, smooth(11.6, 13.6, t));
   const sway = .012 * Math.sin(t * 7 + f);
   setGlow(fireGlow, gi++, x, y + .06, z, level * flick, FLAME[0]);
   setGlow(fireGlow, gi++, x + sway, y + .1, z, level * flick, FLAME[1]);
   setGlow(fireGlow, gi++, x + sway * 2, y + .17 + .02 * Math.sin(t * 11 + f), z, level * flick * .8, FLAME[2]);
   setGlow(fireGlow, gi++, x, y + .12, z, level * flick * .35, FLAME[3]);
   fireGlow.sizes[gi - 4] = .5; fireGlow.sizes[gi - 3] = .32; fireGlow.sizes[gi - 2] = .24; fireGlow.sizes[gi - 1] = 1.7;
   for (let k = 0; k < SPARKS; k++, gi++) { // embers rise, drift and fade
    const s = (t * .5 + k / SPARKS + f * .37) % 1, a = k * 2.39 + f;
    setGlow(fireGlow, gi, x + Math.cos(a) * .07 * s + .05 * s * Math.sin(t * 1.3 + k), y + .08 + s * .85, z + Math.sin(a) * .07 * s, level * (1 - s) ** 1.5 * (.6 + .4 * Math.sin(k * 7.7 + t * 9)), EMBER);
    fireGlow.sizes[gi] = .07;
   }
   if (f < 3) { lights[f].position.set(x, y + .3, z); lights[f].color.set('#ff9a48'); lights[f].intensity = level * flick * 2.8; lights[f].distance = 5; }
  });
  pools.instanceMatrix.needsUpdate = hearths.instanceMatrix.needsUpdate = pools.instanceColor.needsUpdate = true;
  fireGlow.commit();
  // A warm key follows the figure out of the cave and down to the first fire.
  const hk = smooth(.4, 1.4, t) * (1 - smooth(6.6, 7.6, t));
  if (hk > 0) { lights[1].position.set(hp[0] + N[0] * 1.1, hy + .6, hp[1] + N[1] * 1.1 - .25); lights[1].color.set('#ffcf9a'); lights[1].intensity = 1.5 * hk; lights[1].distance = 2.6; }
  const campLit = Math.max(...FIRES.map((_, f) => smooth(IGNITE[f], IGNITE[f] + .7, t))) * (1 - smooth(16.5, 17.2, t));
  lodgeU.uFireGlow.value = campLit;
  crowdMat.emissive.setRGB(.42, .22, .08).multiplyScalar(.6 * campLit); heads.material.emissive.setRGB(.5, .26, .1).multiplyScalar(.6 * campLit);
  fireGlow.visible = pools.visible = hearths.visible = t > 5.8 && t < 17.8;

  // People: the camp walks out to the fires; 1920s walkers circle the sidewalks.
  for (const [i, p] of camp.entries()) {
   campAt(p, t, pa); campAt(p, t + .05, pb);
   const v = Math.hypot(pb[0] - pa[0], pb[1] - pa[1]), s = t >= p.tOut ? 1 - smooth(p.sink, p.sink + .5, t) : 0;
   const rot = v > 1e-4 ? Math.atan2(pb[0] - pa[0], pb[1] - pa[1]) : Math.atan2(p.fire[0] - pa[0], p.fire[1] - pa[1]);
   const y = gs(pa[0], pa[1]) + (v > 1e-4 ? .006 * Math.abs(Math.sin(t * 11 + i)) : 0);
   put(crowd, i, pa[0], y, pa[1], rot, s); put(heads, i, pa[0], y, pa[1], rot, s);
  }
  const town = life(t, 17.6, .5, 22.2, .5);
  for (const [i, w] of walkers.entries()) {
   rectPoint(w.x0, w.z0, w.w, w.d, w.phase + t * w.speed / (2 * (w.w + w.d)), pt);
   const y = gs(pt[0], pt[1]) + .005 * Math.abs(Math.sin(t * 10 + i * 1.7)), rot = Math.atan2(pt[2], pt[3]) + (w.speed < 0 ? Math.PI : 0);
   put(crowd, camp.length + i, pt[0], y, pt[1], rot, town); put(hats, i, pt[0], y, pt[1], rot, town);
  }
  crowd.instanceMatrix.needsUpdate = heads.instanceMatrix.needsUpdate = hats.instanceMatrix.needsUpdate = true;
  heads.visible = t > 6.5 && t < 17.8; hats.visible = t > 17.5 && t < 22.8; crowd.visible = heads.visible || hats.visible;

  // Beat 4 (17–23 s): streets spread, houses rise with porches and lit windows, lamps and Model Ts come on.
  gu.uTown.value.z = 3.7 * smooth(16, 17.8, t) * (1 - smooth(30.4, 30.5, t));
  houses.forEach((h, i) => { const g = life(t, h.t0, .7, h.t1, .7); put(houseMesh, i, h.x, h.y, h.z, h.rot, h.s * (.7 + .3 * g), h.s * h.tall * g, h.s * (.7 + .3 * g)); });
  houseMesh.instanceMatrix.needsUpdate = true;
  winMesh.instanceMatrix.array.set(houseMesh.instanceMatrix.array); winMesh.instanceMatrix.needsUpdate = true;
  houseMesh.visible = winMesh.visible = t > 16.1 && t < 29.4;
  winMat.color.setScalar(1.7 * smooth(17.4, 18.8, t));
  trees.forEach((tr, i) => { const g = tr.t0 < 0 ? (1 - smooth(tr.t1, tr.t1 + .6, t)) + life(t, tr.regrow, .8) : life(t, tr.t0, .8, tr.t1, .6); put(treeMesh, i, tr.x, tr.y, tr.z, i, tr.s * g); });
  treeMesh.instanceMatrix.needsUpdate = true;
  lamps.forEach((l, i) => {
   const g = life(t, l.t0, .6, l.t1, .5), on = smooth(l.on, l.on + .4, t) * (1 - smooth(l.t1 - .2, l.t1 + .2, t));
   put(postMesh, i, l.x, l.y, l.z, 0, g);
   setGlow(townGlow, i, l.x, l.y + .19, l.z, on, LAMP); setGlow(townGlow, lamps.length + i, l.x, l.y + .18, l.z, on * .45, LAMP);
  });
  postMesh.instanceMatrix.needsUpdate = true;
  const carOn = life(t, 17.8, .5, 22.2, .5);
  cars.forEach((c, i) => {
   rectPoint(c.x0, c.z0, c.w, c.d, c.phase + t * c.speed / (2 * (c.w + c.d)), pt);
   const hx = pt[2] * Math.sign(c.speed), hz = pt[3] * Math.sign(c.speed), y = gs(pt[0], pt[1]);
   put(carMesh, i, pt[0], y, pt[1], Math.atan2(hx, hz), carOn);
   for (const s of [-1, 1]) setGlow(townGlow, lamps.length * 2 + i * 2 + (s + 1) / 2, pt[0] + hx * .11 - hz * s * .03, y + .065, pt[1] + hz * .11 + hx * s * .03, carOn * .9, WHITE);
  });
  carMesh.instanceMatrix.needsUpdate = true;
  carMesh.visible = t > 17.7 && t < 22.9; postMesh.visible = townGlow.visible = t > 16.7 && t < 29.4;
  townGlow.commit();

  // Beats 5–6 (23–36 s): towers grow floor by floor, then the future city rises out to the edges.
  gu.uDown.value.z = 2.3 * smooth(22.2, 23.8, t) * (1 - smooth(30.4, 30.5, t));
  gu.uFut.value.z = 9.5 * smooth(28.3, 30.4, t) * (1 - smooth(33.6, 35.3, t));
  tu.uTime.value = t;
  tu.uWin.value = smooth(23, 24.6, t) * (1 - .25 * smooth(29, 31, t));
  const fut = smooth(28.6, 30.4, t) * (1 - smooth(33.4, 34.8, t));
  tu.uFut.value = fut;
  tu.uBuild.value.set(t > 26 ? '#5fe0ff' : '#ffd28a');
  gu.uLane.value.set('#3fc8f0').multiplyScalar(fut);
  for (const mesh of [boxTowers, cylTowers]) {
   mesh.segs.forEach((s, i) => {
    const o = s.o, rise = smooth(o.t0, o.t0 + 1.3, t), g = rise * (1 - smooth(o.t1, o.t1 + .75, t));
    const w = s.fut ? o.r * 2 * (o.cyl || s.style === 3 ? 1 : 1.1) : o.w, dp = s.fut ? o.r * 2 * (o.cyl || s.style === 3 ? 1 : .9) : o.d;
    put(mesh, i, o.x, o.y + o.H * s.f0 * g, o.z, 0, w * s.sw, o.H * (s.f1 - s.f0) * g, dp * s.sw);
    mesh.grow.array[i] = rise; // the build glow marks rising tops only
   });
   mesh.instanceMatrix.needsUpdate = mesh.grow.needsUpdate = true;
   mesh.visible = t > 22.5 && t < 35.9;
  }
  bridges.forEach((b, i) => { const g = life(t, b.t0, .6, b.t1, .5); put(bridgeMesh, i, b.x, b.y, b.z, b.rot, .05, .035 * Math.min(1, g * 4), b.len * g); });
  bridgeMesh.instanceMatrix.needsUpdate = true; bridgeMesh.visible = t > 29.7 && t < 34.2;
  bridgeMat.emissiveIntensity = 1.2 * fut;
  for (const tb of tubes) { tb.uniforms.uReveal.value = smooth(29.4 + tb.ph * .4, 31.2 + tb.ph * .4, t); tb.uniforms.uOp.value = smooth(29.4, 29.8, t) * (1 - smooth(33.5, 34.3, t)); tb.uniforms.uTime.value = t; tb.mesh.visible = tb.uniforms.uOp.value > .01; }
  ringHosts.forEach((o, i) => put(rings, i, o.x, o.y + o.H * (.55 + .12 * Math.sin(t * .6 + i)), o.z, t * .3 + i, o.r * (2.1 + .15 * Math.sin(t * 2 + i))));
  rings.instanceMatrix.needsUpdate = true;
  ringMat.opacity = .8 * smooth(30, 31, t) * (1 - smooth(33.4, 34.2, t)); rings.visible = ringMat.opacity > .01;
  beamMat.opacity = .35 * smooth(30.4, 31.4, t) * (1 - smooth(33.4, 34, t)); beams.visible = beamMat.opacity > .01;
  // Light streams: white heads one way, red tails the other; cyan-white in the future grid.
  const rDown = 2.2 * smooth(23.2, 24.6, t), rFut = 9.5 * smooth(28.8, 30.8, t), streams = 1 - smooth(33.4, 34.2, t);
  for (const [i, f] of flow.entries()) {
   const l = f.l, s = (((f.phase + f.dir * t * f.speed) % 1) + 1) % 1, u = lerp(l.a, l.b, s), off = .022 * f.dir;
   const x = l.alongX ? u : l.c + off, z = l.alongX ? l.c + off : u;
   const dd = Math.hypot(x - DT[0], z - DT[1]), df = Math.hypot(x - FC[0], z - FC[1]);
   const land_ = onLand(x, z, .45) ? 1 : 0, a = Math.max((1 - smooth(rDown - .4, rDown, dd)) * land_, (1 - smooth(rFut - .8, rFut, df)) * (x > edgeX(z) + .5 ? 1 : 0)) * streams;
   setGlow(cityGlow, i, x, Math.max(gs(x, z), .15) + .03, z, a * .85, f.dir > 0 ? (t > 29 ? CYAN : WHITE) : (t > 29 ? MAG : TAIL));
  }
  // Flying craft orbit the core with short fading trails.
  const craftOn = smooth(29.8, 30.8, t) * (1 - smooth(33.3, 34.1, t));
  for (let i = 0; i < CRAFT; i++) {
   const c = craft[i];
   for (let k = 0; k < 3; k++) {
    const a = c.a0 + c.w * (t - k * .18);
    setGlow(cityGlow, F0 + i * 3 + k, FC[0] + Math.cos(a) * c.R, c.y + .15 * Math.sin(t * .8 + i), FC[1] + Math.sin(a) * c.R * c.ecc, craftOn * [1, .45, .2][k], c.amber ? AMBER : k ? CYAN : WHITE);
   }
  }
  future.forEach((o, i) => { const top = o.H > 4.6 ? 1.22 : o.H > 3 ? 1.1 : 1, g = smooth(o.t0 + 1, o.t0 + 1.4, t) * (1 - smooth(o.t1, o.t1 + .3, t)); setGlow(cityGlow, F1 + i, o.x, o.y + o.H * top + .03, o.z, g * fut * (.7 + .3 * Math.sin(t * 2.3 + i))); });
  today.forEach((o, i) => { const top = o.H > 2.8 ? 1.16 : 1, g = smooth(o.t0 + 1.2, o.t0 + 1.5, t) * (1 - smooth(o.t1, o.t1 + .3, t)); setGlow(cityGlow, F2 + i, o.x, o.y + o.H * top + .02, o.z, g * (o.H > 2 ? 1 : 0) * (Math.sin(t * 3 + i * 1.7) > .3 ? 1 : .15)); });
  cityGlow.commit(); cityGlow.visible = t > 23 && t < 35.2;
  if (t > 28) lights.forEach((l, i) => { // the fire lights become coloured city accents
   l.position.set(FC[0] + Math.cos(i * 2.1 + t * .1) * 2, 2.6 + i * .6, FC[1] + Math.sin(i * 2.1 + t * .1) * 2);
   l.color.set(i === 1 ? '#ff6fd8' : '#4fdcff'); l.distance = 7; l.intensity = 5 * fut;
  });
  else if (t > 17) for (const l of lights) l.intensity = 0;

  // Camera: close on the cave at dawn, wider with every era, then home again for the loop.
  const [ca, cb, cf] = keyed(CAM_KEYS, t);
  orbit(camera, t, { radius: lerp(ca.r, cb.r, cf), height: lerp(ca.h, cb.h, cf), target: [0, 1, 2].map(k => lerp(ca.T[k], cb.T[k], cf)), start: -.62 + .2 * Math.sin(t / D * TAU), speed: 0, bob: .12 });
 }
 update(0);
 return { scene, camera, update };
}

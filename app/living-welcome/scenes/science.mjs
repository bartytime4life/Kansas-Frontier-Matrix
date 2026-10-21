import { THREE, HALF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, smooth, window01, lerp, clamp, noise2, fbm } from './kit.mjs';
import { SCENE_CATALOG } from './catalog.mjs';
// Science & observation: monitoring stations sample the ground, a satellite
// swath sweeps a false-colour view across the block, then a model grid floats
// in to summarize the field. Every value is synthetic smooth noise.

const T = SCENE_CATALOG.science.duration;
const STATIONS = [[-4.2, -3.3], [-2, 2.8], [-.4, -1.6], [1.4, 3.6], [2.6, -3.4], [4.3, .1], [-5, .8]];
const DIR = new THREE.Vector2(-.6, -.8); // satellite ground track direction (unit)
const ACROSS = 6.2; // half-width of the swath
const ALT = 3.6;
const CELL = .5, N = 24; // model grid: 24 × 24 cells over the block

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
// Station rings and the satellite swath live in the terrain shader so they drape exactly.
// The false colour is a generic colour-infrared style composite: vigorous cover reads rose-red, bare ground cyan-grey.
const HEAD = `
 uniform vec4 st[7]; uniform float ringA, swFront, swA, fcMix, uTime; uniform vec2 swDir; uniform vec3 cRing, cScan;
 float kRing(float d, float w, float aa) { return 1.0 - smoothstep(w, w + aa * 1.5, d); }`;
const BODY = `
 float aw = max(fwidth(vXZ.x), 1e-4);
 for (int i = 0; i < 7; i++) {
  vec4 s = st[i];
  float d = length(vXZ - s.xy);
  float r1 = fract(s.z), r2 = fract(s.z + 0.5);
  glow += cRing * s.w * (ringA * (kRing(abs(d - r1 * 0.9), 0.012, aw) * (1.0 - r1) + kRing(abs(d - r2 * 0.9), 0.012, aw) * (1.0 - r2)) + exp(-d * d / 0.01) * 0.5);
 }
 float along = dot(vXZ, swDir), across = dot(vXZ, vec2(-swDir.y, swDir.x));
 float inSwath = 1.0 - smoothstep(${ACROSS.toFixed(2)} - 0.05, ${ACROSS.toFixed(2)}, abs(across));
 float behind = (1.0 - smoothstep(swFront - 0.25, swFront + 0.05, along)) * inSwath;
 vec3 c = diffuseColor.rgb;
 float veg = clamp((c.g - max(c.r, c.b)) * 9.0 + 0.25, 0.0, 1.0);
 float lum = dot(c, vec3(0.3, 0.6, 0.1));
 vec3 fc = mix(vec3(0.14, 0.3, 0.4), vec3(0.5, 0.03, 0.09), veg) * (0.55 + 2.2 * lum);
 diffuseColor.rgb = mix(c, fc, behind * fcMix);
 float band = (1.0 - smoothstep(0.0, 0.9, abs(along - swFront + 0.45))) * inSwath;
 float scan = 0.5 + 0.5 * sin(along * 110.0 - uTime * 26.0);
 float shimmer = 0.75 + 0.25 * sin(across * 23.0 + uTime * 9.0);
 float edge = (1.0 - smoothstep(0.0, 0.04 + aw, abs(along - swFront))) * inSwath + kRing(abs(abs(across) - ${ACROSS.toFixed(2)}), 0.01, aw) * (1.0 - smoothstep(swFront - 0.3, swFront + 0.3, along)) * 0.5;
 glow += cScan * swA * (band * (0.08 + 0.22 * scan * shimmer) + edge * 0.9);`;

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022 });
 const land = terrain({ segments: 256 });
 const u = liveSurface(land);
 u.tint.value.set('#0a2029');
 const water = riverWater(land.sample);
 scene.add(land.mesh, blockSides(land.sample), water);

 const st = STATIONS.map(([x, z]) => new THREE.Vector4(x, z, 0, 0));
 const g = {
  st: { value: st }, ringA: { value: 0 }, swFront: { value: -20 }, swA: { value: 0 }, fcMix: { value: 0 }, uTime: { value: 0 },
  swDir: { value: DIR }, cRing: { value: new THREE.Color('#8fd6ee') }, cScan: { value: new THREE.Color('#7fe0ff') },
 };
 overlay(land.mesh.material, g, HEAD, BODY, 'kfm-science-observe');

 // Stations: a tripod mast with an instrument box, a cross-arm and a small panel.
 const metal = new THREE.MeshStandardMaterial({ color: '#c9d3d6', metalness: .6, roughness: .35 });
 const panelMat = new THREE.MeshStandardMaterial({ color: '#1d3f5c', emissive: '#16405e', emissiveIntensity: .6, metalness: .3, roughness: .3 });
 const leg = new THREE.CylinderGeometry(.012, .016, .42, 6).translate(0, .21, 0);
 const mast = new THREE.CylinderGeometry(.014, .018, .9, 8).translate(0, .45, 0);
 const box = new THREE.BoxGeometry(.09, .1, .07).translate(0, .55, .04);
 const arm = new THREE.CylinderGeometry(.008, .008, .34, 6).rotateZ(Math.PI / 2).translate(0, .8, 0);
 const panel = new THREE.BoxGeometry(.18, .012, .13).rotateX(-.6).translate(0, .4, -.1);
 const stations = STATIONS.map(([x, z], i) => {
  const s = new THREE.Group();
  for (let k = 0; k < 3; k++) {
   const l = new THREE.Mesh(leg, metal), a = k / 3 * Math.PI * 2;
   l.position.set(Math.cos(a) * .17, -.06, Math.sin(a) * .17); l.rotation.set(Math.sin(a) * .42, 0, -Math.cos(a) * .42);
   s.add(l);
  }
  s.add(new THREE.Mesh(mast, metal), new THREE.Mesh(box, metal), new THREE.Mesh(arm, metal), new THREE.Mesh(panel, panelMat));
  s.position.set(x, land.sample(x, z), z); s.rotation.y = i * 1.3;
  scene.add(s);
  return s;
 });

 // Satellite: a small bus with two panels, a scan fan to the ground and a faint orbit trace.
 const sat = new THREE.Group();
 const bus = new THREE.Mesh(new THREE.BoxGeometry(.16, .12, .12), new THREE.MeshStandardMaterial({ color: '#e8d6a8', emissive: '#e8c37c', emissiveIntensity: .7, metalness: .5, roughness: .3 }));
 const wings = new THREE.Mesh(new THREE.BoxGeometry(.72, .01, .14), new THREE.MeshStandardMaterial({ color: '#244b72', emissive: '#2c6ea0', emissiveIntensity: 1, metalness: .4, roughness: .3 }));
 sat.add(bus, wings);
 sat.rotation.y = Math.atan2(DIR.x, DIR.y) + Math.PI / 2;
 scene.add(sat);
 const fanPos = new Float32Array(9), fanGeo = new THREE.BufferGeometry();
 fanGeo.setAttribute('position', new THREE.BufferAttribute(fanPos, 3));
 fanGeo.setAttribute('color', new THREE.Float32BufferAttribute([.05, .15, .2, .5, .88, 1, .5, .88, 1], 3));
 const fan = new THREE.Mesh(fanGeo, new THREE.MeshBasicMaterial({ vertexColors: true, transparent: true, opacity: 0, depthWrite: false, side: THREE.DoubleSide, blending: THREE.AdditiveBlending }));
 fan.frustumCulled = false;
 const trackPts = [];
 for (let i = 0; i <= 80; i++) { const a = lerp(-14, 14, i / 80); trackPts.push(new THREE.Vector3(DIR.x * a, ALT - a * a * .012, DIR.y * a)); }
 const track = new THREE.Line(new THREE.BufferGeometry().setFromPoints(trackPts), new THREE.LineBasicMaterial({ color: '#7fd3ea', transparent: true, opacity: 0, depthWrite: false }));
 scene.add(fan, track);

 // Model grid: floating tiles over the block, values from smooth noise, glowing cell edges.
 const field = noise2(77), pos = [], cen = [], corner = [], val = [], delay = [], index = [];
 for (let j = 0; j < N; j++) for (let i = 0; i < N; i++) {
  const x = -HALF + (i + .5) * CELL, z = -HALF + (j + .5) * CELL;
  const top = Math.max(...[[0, 0], [-.25, -.25], [.25, -.25], [-.25, .25], [.25, .25]].map(([dx, dz]) => land.sample(clamp(x + dx, -HALF, HALF), clamp(z + dz, -HALF, HALF))));
  const v = clamp(.5 + 1.9 * fbm(field, x * .16, z * .16, 3)), y = top + .32 + v * .18, b = pos.length / 3;
  for (const [cx, cz] of [[-1, -1], [1, -1], [1, 1], [-1, 1]]) { pos.push(x, y, z); cen.push(x, y, z); corner.push(cx, cz); val.push(v); delay.push((i + (N - 1 - j)) / (2 * N - 2)); }
  index.push(b, b + 2, b + 1, b, b + 3, b + 2);
 }
 const gridGeo = new THREE.BufferGeometry();
 gridGeo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
 gridGeo.setAttribute('aCenter', new THREE.Float32BufferAttribute(cen, 3));
 gridGeo.setAttribute('aCorner', new THREE.Float32BufferAttribute(corner, 2));
 gridGeo.setAttribute('aVal', new THREE.Float32BufferAttribute(val, 1));
 gridGeo.setAttribute('aDelay', new THREE.Float32BufferAttribute(delay, 1));
 gridGeo.setIndex(index);
 const gridU = { reveal: { value: 0 }, opacity: { value: 0 }, uTime: { value: 0 }, lo: { value: new THREE.Color('#123f4d') }, mid: { value: new THREE.Color('#5fb8d2') }, hi: { value: new THREE.Color('#f3d38e') } };
 const grid = new THREE.Mesh(gridGeo, new THREE.ShaderMaterial({
  uniforms: gridU, transparent: true, depthWrite: false, side: THREE.DoubleSide,
  vertexShader: `attribute vec3 aCenter; attribute vec2 aCorner; attribute float aVal; attribute float aDelay; uniform float reveal;
   varying vec2 vC; varying float vV; varying float vK; varying float vD;
   void main() {
    float k = smoothstep(aDelay * 0.7, aDelay * 0.7 + 0.3, reveal);
    vec3 p = aCenter + vec3(aCorner.x, 0.0, aCorner.y) * ${(CELL * .44).toFixed(3)} * k;
    p.y -= (1.0 - k) * 0.4;
    vC = aCorner; vV = aVal; vK = k; vD = aDelay;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
   }`,
  fragmentShader: `uniform vec3 lo, mid, hi; uniform float opacity, uTime; varying vec2 vC; varying float vV; varying float vK; varying float vD;
   void main() {
    vec3 c = vV < 0.5 ? mix(lo, mid, vV * 2.0) : mix(mid, hi, vV * 2.0 - 1.0);
    float e = max(abs(vC.x), abs(vC.y));
    float rim = smoothstep(0.8, 0.97, e);
    float pulse = 0.5 + 0.5 * sin(uTime * 2.2 - vD * 9.0);
    gl_FragColor = vec4(c * (0.8 + 0.35 * rim + 0.15 * pulse), (0.5 + 0.3 * rim) * vK * opacity);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
   }`,
 }));
 grid.renderOrder = 4; grid.frustumCulled = false;
 scene.add(grid);

 // Glow: blinking station tips, the satellite core and its nadir spot.
 const glow = glowPoints(STATIONS.length + 2, { size: .32, color: '#f3d38e', depthTest: true });
 const S0 = STATIONS.length;
 glow.colors.set([.85, .95, 1], S0 * 3); glow.sizes[S0] = 1.3;
 glow.colors.set([.5, .88, 1], (S0 + 1) * 3); glow.sizes[S0 + 1] = 1.1;
 scene.add(glow);

 function update(t) {
  const out = 1 - smooth(14.9, 15.9, t);
  g.uTime.value = gridU.uTime.value = t;

  // Beat 1 (0–5.5 s): stations rise; rings pulse out where each one samples the surface.
  g.ringA.value = lerp(1, .25, smooth(5.2, 6.5, t)) * out;
  stations.forEach((s, i) => {
   const p = clamp((t - .3 - i * .28) / .8), rise = p === 0 ? 0 : 1 + 2.2 * Math.pow(p - 1, 3) + 1.2 * Math.pow(p - 1, 2);
   const k = Math.max(.001, 1.4 * rise * (1 - smooth(15, 15.8, t)));
   s.scale.set(k, k, k); s.visible = k > .002;
   st[i].z = Math.max(0, t - 1 - i * .28) / 1.6; st[i].w = smooth(1 + i * .28, 1.5 + i * .28, t) * out;
   const blink = Math.pow(.5 + .5 * Math.sin(t * 4.2 + i * 1.9), 8);
   glow.positions.set([s.position.x, s.position.y + .84 * k, s.position.z], i * 3);
   glow.alphas[i] = s.visible ? (.35 + .65 * blink) * smooth(.2, .8, p) : 0;
  });

  // Beat 2 (5.5–11 s): the satellite crosses; its swath leaves a false-colour view behind.
  const pass = smooth(5.7, 10.4, t), front = lerp(-9.5, 9.5, pass);
  g.swFront.value = front;
  g.swA.value = window01(t, 5.6, 10.8, .6);
  g.fcMix.value = .85 * smooth(5.6, 6.2, t) * (1 - smooth(11, 12.4, t));
  const vis = window01(t, 5.4, 11, .7);
  sat.position.set(DIR.x * front, ALT - front * front * .012, DIR.y * front);
  sat.visible = vis > .01;
  glow.positions.set([sat.position.x, sat.position.y, sat.position.z], S0 * 3); glow.alphas[S0] = vis;
  const nx = DIR.x * front, nz = DIR.y * front, sx = -DIR.y * ACROSS, sz = DIR.x * ACROSS;
  fanPos.set([sat.position.x, sat.position.y, sat.position.z, nx + sx, .45, nz + sz, nx - sx, .45, nz - sz]);
  fanGeo.attributes.position.needsUpdate = true;
  fan.material.opacity = g.swA.value * .22;
  track.material.opacity = vis * .3;
  glow.positions.set([nx, land.sample(clamp(nx, -HALF, HALF), clamp(nz, -HALF, HALF)) + .1, nz], (S0 + 1) * 3);
  glow.alphas[S0 + 1] = g.swA.value * (Math.abs(nx) < HALF && Math.abs(nz) < HALF ? .8 : 0);
  glow.commit();

  // Beat 3 (11–16 s): the model grid assembles in a diagonal wave and holds the summary.
  gridU.reveal.value = smooth(10.9, 13.2, t);
  gridU.opacity.value = smooth(10.9, 11.4, t) * (1 - smooth(14.7, 15.7, t));
  grid.visible = gridU.opacity.value > .002;
  u.tintMix.value = .35 * gridU.opacity.value;

  orbit(camera, 4.5 * (1 - Math.cos(t / T * Math.PI * 2)), {
   radius: 21.5, height: lerp(10.5, 9.2, window01(t, 5, 11.2, 1.5)), target: [0, -.5, 0], start: -.95, speed: .045,
  });
 }
 update(0);
 return { scene, camera, update, dispose() { leg.dispose(); mast.dispose(); box.dispose(); arm.dispose(); panel.dispose(); } };
}

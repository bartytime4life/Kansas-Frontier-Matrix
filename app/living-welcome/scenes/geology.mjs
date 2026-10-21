import { THREE, HALF, terrain, liveSurface, riverWater, heroCamera, stage, orbit, glowPoints, smooth, window01, lerp, easeInOut } from './kit.mjs';
// Geology: a cut block lifts to show bedrock beds dipping beneath the plains,
// a synthetic seismic event sends P and S wavefronts through the beds, and
// surface stations light up and trace a seismogram as each wave arrives.

const DIP = .2; // bedding rises to the south-west, so the beds dip north-east, steepest across the sunlit east wall
const FLOOR = -2.75, T0 = 5.9, VP = 1.35, VS = .82;
const HYPO = new THREE.Vector3(3.5, -2.3, -4.1); // under the NE corner, close to the two walls the camera sees
const BEDS = ['#b9b09c', '#6d6862', '#c8a36c', '#8a5a44', '#55524d', '#d8cfb8'];
const STATIONS = [[-2.2, -3.6], [-.2, 2.1], [-4.4, -.6], [1.9, 4.2], [-5.1, -4.8], [-3.2, 3.6], [-.9, 5.3], [4.4, 5.2]];
const TRACE = 90; // points per seismogram trace: dense enough to read as one line

// Vertex side: walls drop from the surface to the floor as the block lifts; the surface ripples as the S wave passes.
const VERT_PARS = `uniform vec3 uHypo; uniform float uRP; uniform float uRS; uniform float uAP; uniform float uAS; uniform float uGrow;
 varying vec3 vKPos; varying float vTop;
 #ifdef KFM_WALL
 attribute float aTop;
 #endif`;
const VERT_MAIN = `
 #ifdef KFM_WALL
 transformed.y = mix(aTop, transformed.y, uGrow); vTop = aTop;
 #else
 { float ds = distance(transformed, uHypo);
   transformed.y += uAS * .05 * exp(-pow((ds - uRS) / .35, 2.0)) * sin((ds - uRS) * 9.0) + uAP * .02 * exp(-pow((ds - uRP) / .2, 2.0)); }
 vTop = transformed.y;
 #endif
 vKPos = transformed;
 #include <project_vertex>`;
// Fragment side: bed colours and contacts come from position, so beds stay crisp on coarse wall geometry.
const FRAG_PARS = `uniform vec3 uBeds[6]; uniform vec3 uHypo; uniform vec3 uColP; uniform vec3 uColS; uniform vec3 uGold; uniform vec3 uSoil; uniform vec3 uLoess;
 uniform float uRP; uniform float uRS; uniform float uAP; uniform float uAS; uniform float uBedGlow; uniform float uBedFront; uniform float uGeoMap;
 varying vec3 vKPos; varying float vTop;
 float kBed(vec3 p) { float b = p.y - ${DIP.toFixed(3)} * p.z + .1 * p.x + .09 * sin(p.z * .55 + p.x * .3); return b + .1 * sin(b * 1.9); }
 vec3 kBedColor(float w) { int k = int(mod(floor(w / .34), 6.0)); return uBeds[k] * (.9 + .1 * sin(w * 60.0)); }
 float kContact(float w) { float f = w / .34; float d = abs(fract(f + .5) - .5); return 1.0 - smoothstep(0.0, fwidth(f) * 1.5, d); }`;
const FRAG_COLOR = `#include <color_fragment>
 float kb = kBed(vKPos), kc = kContact(kb);
 #ifdef KFM_WALL
 float kDepth = vTop - vKPos.y, kWob = .04 * sin(vKPos.x * 1.7 + vKPos.z * 1.1);
 vec3 kCol = mix(kBedColor(kb) * (1.0 - .28 * kc), uLoess, 1.0 - smoothstep(.3 + kWob, .33 + kWob, kDepth));
 diffuseColor.rgb = mix(kCol, uSoil, 1.0 - smoothstep(.1, .12, kDepth));
 float kLine = 1.0;
 totalEmissiveRadiance += diffuseColor.rgb * .1; // keep the shaded north wall's beds legible
 #else
 diffuseColor.rgb = mix(diffuseColor.rgb, kBedColor(kb) * (1.0 - .35 * kc), uGeoMap);
 float kLine = uGeoMap;
 #endif`;
const FRAG_EMIT = `#include <emissivemap_fragment>
 { float d = distance(vKPos, uHypo);
   float wp = exp(-pow((d - uRP) / .15, 2.0)) * uAP, ws = exp(-pow((d - uRS) / .24, 2.0)) * uAS;
   float coda = uAP * .1 * step(d, uRP) * exp(-(uRP - d) * 1.1);
   float sweep = exp(-pow((kb - uBedFront) / .45, 2.0));
   totalEmissiveRadiance += uColP * (wp * 1.6 + coda) + uColS * ws * 1.25 + uGold * kc * kLine * (uBedGlow * (.2 + .9 * sweep) + (wp + ws) * 1.4); }`;

function patch(material, uniforms, key, define) {
 const previous = material.onBeforeCompile;
 material.defines = { ...material.defines, [define]: '' };
 material.onBeforeCompile = (shader, renderer) => {
  previous?.call(material, shader, renderer);
  Object.assign(shader.uniforms, uniforms);
  shader.vertexShader = shader.vertexShader.replace('#include <common>', `#include <common>\n${VERT_PARS}`).replace('#include <project_vertex>', VERT_MAIN);
  shader.fragmentShader = shader.fragmentShader.replace('#include <common>', `#include <common>\n${FRAG_PARS}`)
   .replace('#include <color_fragment>', FRAG_COLOR).replace('#include <emissivemap_fragment>', FRAG_EMIT);
 };
 material.customProgramCacheKey = () => key;
}

/** All four walls in one geometry; `aTop` lets the shader pull them up to the surface. */
function wallGeometry(sample, steps = 140, rows = 6) {
 const edges = [s => [lerp(-HALF, HALF, s), HALF], s => [HALF, lerp(HALF, -HALF, s)], s => [lerp(HALF, -HALF, s), -HALF], s => [-HALF, lerp(-HALF, HALF, s)]];
 const positions = [], tops = [], index = [];
 let base = 0;
 for (const edge of edges) {
  for (let i = 0; i <= steps; i++) {
   const [x, z] = edge(i / steps), top = sample(x, z);
   for (let j = 0; j <= rows; j++) {
    positions.push(x, lerp(top, FLOOR, j / rows), z); tops.push(top);
    if (i < steps && j < rows) { const a = base + i * (rows + 1) + j, b = a + rows + 1; index.push(a, b, a + 1, b, b + 1, a + 1); }
   }
  }
  base += (steps + 1) * (rows + 1);
 }
 const geometry = new THREE.BufferGeometry();
 geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
 geometry.setAttribute('aTop', new THREE.Float32BufferAttribute(tops, 1));
 geometry.setIndex(index); geometry.computeVertexNormals();
 return geometry;
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .02 });
 const block = new THREE.Group();
 scene.add(block);

 const land = terrain({ segments: 210 });
 liveSurface(land);
 const gu = {
  uBeds: { value: BEDS.map(c => new THREE.Color(c)) }, uHypo: { value: HYPO }, uGrow: { value: 1 },
  uColP: { value: new THREE.Color('#f3d38e') }, uColS: { value: new THREE.Color('#7fd3ea') }, uGold: { value: new THREE.Color('#e8c37c') },
  uSoil: { value: new THREE.Color('#4a3726') }, uLoess: { value: new THREE.Color('#a88a5c') },
  uRP: { value: 0 }, uRS: { value: 0 }, uAP: { value: 0 }, uAS: { value: 0 }, uBedGlow: { value: 0 }, uBedFront: { value: 3 }, uGeoMap: { value: 0 },
 };
 patch(land.mesh.material, gu, 'kfm-geology-surface', 'KFM_SURFACE');
 const wallMat = new THREE.MeshStandardMaterial({ roughness: .95, side: THREE.DoubleSide });
 patch(wallMat, gu, 'kfm-geology-wall', 'KFM_WALL');
 const walls = new THREE.Mesh(wallGeometry(land.sample), wallMat);
 const water = riverWater(land.sample);
 block.add(land.mesh, walls, water);

 // Hypocentre seen "through" the ground, with a faint plumb line to the epicentre.
 const epiY = land.sample(HYPO.x, HYPO.z);
 const focus = glowPoints(3, { size: 1, color: '#ffe2a8', depthTest: false });
 focus.positions.set([HYPO.x, HYPO.y, HYPO.z, HYPO.x, HYPO.y, HYPO.z, HYPO.x, epiY + .05, HYPO.z]);
 const plumbGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(HYPO.x, epiY + .05, HYPO.z), HYPO.clone()]);
 const plumb = new THREE.Line(plumbGeo, new THREE.LineDashedMaterial({ color: '#f3d38e', dashSize: .1, gapSize: .08, transparent: true, opacity: 0, depthTest: false, depthWrite: false }));
 plumb.computeLineDistances();
 block.add(focus, plumb);

 // Stations: a small mast and cap, a ground ring that pings on arrival, and a glowing trace.
 const capGeo = new THREE.OctahedronGeometry(.075), mastGeo = new THREE.CylinderGeometry(.014, .022, .26, 6), ringGeo = new THREE.RingGeometry(.09, .12, 40);
 ringGeo.rotateX(-Math.PI / 2);
 const mastMat = new THREE.MeshStandardMaterial({ color: '#c9c3b4', roughness: .5, metalness: .4 });
 const sky = new THREE.Color('#5fb8d6'), gold = new THREE.Color('#f3d38e');
 const stations = STATIONS.map(([x, z], i) => {
  const top = land.sample(x, z), group = new THREE.Group();
  group.position.set(x, top, z);
  const mast = new THREE.Mesh(mastGeo, mastMat); mast.position.y = .13;
  const capMat = new THREE.MeshStandardMaterial({ color: '#2d3a40', emissive: sky.clone(), emissiveIntensity: .6, roughness: .4 });
  const cap = new THREE.Mesh(capGeo, capMat); cap.position.y = .29;
  const ringMat = new THREE.MeshBasicMaterial({ color: '#f3d38e', transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide });
  const ring = new THREE.Mesh(ringGeo, ringMat); ring.position.y = .02;
  group.add(mast, cap, ring); block.add(group);
  const arrival = T0 + Math.hypot(x - HYPO.x, top - HYPO.y, z - HYPO.z) / VP;
  return { group, cap, capMat, ring, ringMat, top, arrival, seed: i * 1.73 + .4 };
 });
 const traces = glowPoints(STATIONS.length * (TRACE + 1), { size: .16, color: '#f3d38e' });
 block.add(traces);
 // Envelope of a synthetic seismogram: quiet, a sharp P onset, a bigger S packet, then coda.
 const envelope = Array.from({ length: TRACE }, (_, j) => { const u = j / (TRACE - 1); return 1.15 * (.012 + .1 * Math.exp(-Math.pow((u - .22) / .07, 2)) + .2 * Math.exp(-Math.pow((u - .52) / .13, 2)) + .04 * (1 - u)); });
 const right = new THREE.Vector3();

 function update(t) {
  orbit(camera, t, { radius: 23.5, height: 10.5 - 1.1 * window01(t, 4, 16, 4), target: [0, -1.05, 0], start: -.6 - .3 * Math.cos(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
  // Beat 1 (0–5.5 s): the block lifts and turns; walls extend to show dipping beds, mapped as outcrop bands on top.
  const lift = easeInOut(smooth(.2, 4.4, t)) * (1 - easeInOut(smooth(15, 15.95, t)));
  block.position.y = lerp(-.8, 0, lift);
  block.rotation.y = lerp(.22, 0, lift);
  gu.uGrow.value = Math.max(.02, easeInOut(smooth(.4, 4.6, t)) * (1 - easeInOut(smooth(15, 15.9, t))));
  gu.uGeoMap.value = lerp(.72, .3, smooth(5, 6.4, t)) * smooth(.8, 3.2, t) * (1 - smooth(14.8, 15.8, t));
  gu.uBedGlow.value = window01(t, .8, 6.2, 1);
  gu.uBedFront.value = lerp(2.8, -3.8, smooth(1, 5.4, t));

  // Beat 2 (5.5–11 s): the focus gathers, flashes, and P then S shells sweep out through the beds.
  const since = Math.max(0, t - T0), end = 1 - smooth(14.6, 15.5, t);
  gu.uRP.value = VP * since; gu.uRS.value = VS * Math.max(0, since - .15);
  gu.uAP.value = (t > T0 ? 1 : 0) * window01(t, T0 - .05, 15.4, .35) * (1 - .6 * smooth(3, 13, gu.uRP.value));
  gu.uAS.value = window01(t, T0 + .3, 15.4, .5) * .85 * (1 - .5 * smooth(2, 10, gu.uRS.value));
  const gather = smooth(5.1, T0, t), flash = t > T0 ? Math.exp(-since * 2.2) : 0;
  focus.sizes[0] = .5 + .25 * gather + 2.8 * flash; focus.alphas[0] = (t < T0 ? gather * (.55 + .2 * Math.sin(t * 15)) : .55 + .45 * Math.exp(-since * 1.2)) * end;
  focus.sizes[1] = 2.4 + 4 * flash; focus.alphas[1] = (gather * .18 + flash * .5) * end;
  focus.sizes[2] = .4 + 3 * flash; focus.alphas[2] = (gather * .25 + flash) * end;
  focus.commit();
  plumb.material.opacity = gather * .45 * end;

  // Beat 3 (11–16 s): stations arm, then each lights and draws its trace as the P wave reaches it.
  right.set(-camera.position.z, 0, camera.position.x).normalize(); // traces wiggle across the view, not into it
  let k = 0;
  for (const [i, s] of stations.entries()) {
   const arm = smooth(8.4 + i * .1, 9.4 + i * .1, t) * (1 - smooth(15.1, 15.8, t)), tau = t - s.arrival, hit = tau > 0 ? 1 : 0;
   s.group.visible = arm > .01; s.group.scale.setScalar(Math.max(.01, arm) * 1.7);
   s.capMat.emissive.copy(sky).lerp(gold, hit);
   s.capMat.emissiveIntensity = .6 + hit * (.8 + 2.2 * Math.exp(-tau * 2));
   s.cap.rotation.y = t * 1.2 + i;
   const ping = tau > 0 ? tau / 1.4 : 1;
   s.ring.scale.setScalar(1 + ping * 7); s.ringMat.opacity = ping < 1 ? (1 - ping) * .9 * arm : 0;
   const drawn = tau > 0 ? tau / 1.5 : 0, fade = arm * (1 - .55 * smooth(2.2, 4, tau));
   for (let j = 0; j < TRACE; j++, k++) {
    const u = j / (TRACE - 1), off = envelope[j] * Math.sin(j * .5 + s.seed) * (.6 + .4 * Math.sin(j * .17 + s.seed * 2));
    traces.positions[k * 3] = s.group.position.x + right.x * off;
    traces.positions[k * 3 + 1] = s.top + .58 + u * 1.3;
    traces.positions[k * 3 + 2] = s.group.position.z + right.z * off;
    traces.alphas[k] = u <= drawn ? fade : 0;
   }
   // A bright halo on the cap that flashes at the arrival.
   traces.positions.set([s.group.position.x, s.top + .49, s.group.position.z], k * 3);
   traces.sizes[k] = .7 + 1.8 * (tau > 0 ? Math.exp(-tau * 1.6) : 0); traces.alphas[k] = arm * (.25 + .75 * hit); k++;
  }
  traces.commit();

 }
 update(0);
 return { scene, camera, update, dispose() {} };
}

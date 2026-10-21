import { THREE, WORLD, RELIEF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, noise2, fbm, rng, smooth, window01, lerp, clamp } from './kit.mjs';
// Sky & light: a calculated sun path over the diorama drives key light, sky
// colour and terrain-cast shadows through one day, twilight and a starry night.

const D = 18, TAU = Math.PI * 2, DEG = 180 / Math.PI;
const LAT = 38.5 / DEG; // a mid-plains latitude tilts the equinox sun path toward the south
const DOME_R = 8.8, DOME_H = 4.8, DOME_Y = .1; // squashed dome so the noon sun stays in frame
const MOON = new THREE.Vector3(-.25, .75, .62).normalize();

// Hour angle: 0 at sunrise, π at sunset, 2π at the next sunrise, so the loop is
// one day. The sine term slows golden hour and twilight and hurries the night.
const hourAngle = t => { const u = TAU * t / D; return u + .6 * Math.sin(u); };
const sunVector = (h, out) => out.set(Math.cos(h), Math.sin(h) * Math.cos(LAT), Math.sin(h) * Math.sin(LAT));
const domePoint = (d, out) => out.set(d.x * DOME_R, DOME_Y + d.y * DOME_H, d.z * DOME_R);
// Seamless sway instead of a one-way orbit, so t = D matches t = 0.
const shoot = (camera, t) => orbit(camera, 9 + 5 * Math.sin(TAU * t / D), { radius: 28, height: 10, target: [0, .3, 0], start: -1.4, speed: .045 });

const stops = list => list.map(([x, c]) => [x, typeof c === 'number' ? c : new THREE.Color(c)]);
function ramp(list, x, out) { // list keyed by sun altitude in degrees
 if (x <= list[0][0]) return out ? out.copy(list[0][1]) : list[0][1];
 for (let i = 1; i < list.length; i++) if (x <= list[i][0]) {
  const [x0, a] = list[i - 1], [x1, b] = list[i], k = smooth(x0, x1, x);
  return out ? out.copy(a).lerp(b, k) : lerp(a, b, k);
 }
 const last = list[list.length - 1][1];
 return out ? out.copy(last) : last;
}
// Colour temperature by altitude: cool morning, white noon, warm afternoon.
const SUN_AM = stops([[-2, '#ff8a58'], [3, '#ffb48a'], [9, '#d4e2ff'], [26, '#e6eeff'], [48, '#fff9f1']]);
const SUN_PM = stops([[-2, '#ff5a24'], [3, '#ff8a3c'], [10, '#ffb56a'], [22, '#ffd8a2'], [36, '#ffefd8'], [48, '#fff9f1']]);
const HEMI = stops([[-18, '#22406e'], [-10, '#3b5590'], [-4, '#8a6f9e'], [1, '#d79a7c'], [8, '#c9cfd8'], [25, '#bfe3f2']]);
const HEMI_I = stops([[-18, .34], [-9, .36], [-2, .4], [6, .46], [20, .82], [40, .92]]);
const SKY_HI = stops([[-18, '#071a2c'], [-12, '#15284c'], [-6, '#4b3c62'], [-1, '#9c5238'], [4, '#8a5a3c'], [12, '#3c6478'], [30, '#2c6a86']]);
const SKY_LO = stops([[-18, '#02070f'], [-10, '#061024'], [-3, '#101a34'], [3, '#1a2632'], [14, '#0d3042'], [30, '#0c3446']]);
const GLOW = stops([[-12, '#4a3a8a'], [-6, '#b8567a'], [-2, '#ff7040'], [6, '#ffa050']]);

/** Max elevation tangent toward the east and west of each vertex: a cheap horizon map for cast shadows. */
function horizons(base, segs) {
 const n = segs + 1, cell = WORLD / segs, east = new Float32Array(n * n), west = new Float32Array(n * n);
 const offsets = [...new Set(Array.from({ length: 40 }, (_, k) => Math.round(1.16 ** k)))].filter(s => s * cell < 5);
 for (let r = 0; r < n; r++) for (let c = 0; c < n; c++) {
  const i = r * n + c, h = base[i];
  let e = 0, w = 0;
  for (const s of offsets) {
   if (c + s < n) e = Math.max(e, (base[i + s] - h) / s);
   if (c - s >= 0) w = Math.max(w, (base[i - s] - h) / s);
  }
  east[i] = e * RELIEF / cell; west[i] = w * RELIEF / cell;
 }
 return { east, west };
}

/** Soft Milky Way band: clouds and a dark rift, generated as data (no canvas needed). */
function milkyWayTexture(w = 384, h = 48) {
 const data = new Uint8Array(w * h * 4), n = noise2(41), m = noise2(43), r = rng(5);
 for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
  const a = x / w * TAU, v = y / (h - 1) * 2 - 1, ca = Math.cos(a) * 4, sa = Math.sin(a) * 4;
  const clouds = fbm(n, ca + v * 1.3, sa - v * .9, 4);
  const rift = Math.exp(-Math.pow(v - .16 * Math.sin(a * 3), 2) / .025) * smooth(-.15, .45, fbm(m, ca * 1.6, sa * 1.6 + v, 3));
  const core = Math.exp(-v * v / .16) * (.55 + .45 * Math.pow(.5 + .5 * Math.cos(a - 1.2), 2));
  const k = clamp(core * clamp(.5 + clouds * 1.1) * (1 - .75 * rift) + core * .18 * r());
  const warm = Math.exp(-v * v / .05);
  const i = (y * w + x) * 4;
  data[i] = 255 * k * lerp(.72, 1, warm); data[i + 1] = 255 * k * lerp(.82, .93, warm); data[i + 2] = 255 * k * lerp(1, .8, warm); data[i + 3] = 255;
 }
 const tex = new THREE.DataTexture(data, w, h, THREE.RGBAFormat);
 tex.colorSpace = THREE.SRGBColorSpace; tex.magFilter = tex.minFilter = THREE.LinearFilter; tex.wrapS = THREE.RepeatWrapping;
 tex.needsUpdate = true;
 return tex;
}

const line = (points, color, opacity) => new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), new THREE.LineBasicMaterial({ color, transparent: true, opacity, depthWrite: false }));

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 const { key, hemi, rim } = stage(scene, { fog: .02 });
 const land = terrain({ segments: 256 });
 const u = liveSurface(land);
 const sides = blockSides(land.sample);
 const water = riverWater(land.sample);
 scene.add(land.mesh, sides, water);

 // Cast shadows without shadow maps: the key light (directional light 0) is
 // masked wherever the sun sits below the local east/west horizon.
 const { east, west } = horizons(land.base, 256);
 land.geometry.setAttribute('aHorE', new THREE.BufferAttribute(east, 1));
 land.geometry.setAttribute('aHorW', new THREE.BufferAttribute(west, 1));
 const su = { sunTan: { value: 9 }, sunEast: { value: 1 } };
 const mat = land.mesh.material, live = mat.onBeforeCompile;
 mat.onBeforeCompile = (shader, renderer) => {
  live(shader, renderer);
  Object.assign(shader.uniforms, su);
  shader.vertexShader = shader.vertexShader
   .replace('#include <common>', `#include <common>
    attribute float aHorE; attribute float aHorW; uniform float sunEast; varying float vHor;`)
   .replace('#include <begin_vertex>', `#include <begin_vertex>
    vHor = mix(aHorW, aHorE, sunEast) * kRaise;`);
  shader.fragmentShader = shader.fragmentShader
   .replace('#include <common>', `#include <common>
    uniform float sunTan; varying float vHor;`)
   .replace('#include <lights_fragment_begin>', THREE.ShaderChunk.lights_fragment_begin.replace('getDirectionalLightInfo( directionalLight, directLight );',
    '$&\n directLight.color *= UNROLLED_LOOP_INDEX == 0 ? smoothstep(-0.012, 0.018, sunTan - vHor) : 1.0;'));
 };
 mat.customProgramCacheKey = () => 'kfm-sky-surface';

 // Backdrop: a gradient sphere with a warm glow toward the sun's azimuth and a halo around it.
 const skyU = {
  high: { value: new THREE.Color() }, low: { value: new THREE.Color() }, glow: { value: new THREE.Color() }, glowAmt: { value: 0 },
  sunDir: { value: new THREE.Vector3(1, 0, 0) }, sunPos: { value: new THREE.Vector3() }, halo: { value: new THREE.Color() }, haloAmt: { value: 0 },
 };
 const sky = new THREE.Mesh(new THREE.SphereGeometry(85, 48, 24), new THREE.ShaderMaterial({
  uniforms: skyU, side: THREE.BackSide, depthWrite: false,
  vertexShader: 'varying vec3 vW;void main(){vec4 w=modelMatrix*vec4(position,1.);vW=w.xyz;gl_Position=projectionMatrix*viewMatrix*w;}',
  fragmentShader: `uniform vec3 high;uniform vec3 low;uniform vec3 glow;uniform float glowAmt;uniform vec3 sunDir;uniform vec3 sunPos;uniform vec3 halo;uniform float haloAmt;varying vec3 vW;
   void main(){vec3 d=normalize(vW-cameraPosition);float h=smoothstep(-.66,-.04,d.y);vec3 c=mix(low,high,h);
    float az=max(dot(normalize(d.xz+vec2(1e-4)),normalize(sunDir.xz+vec2(1e-4))),0.);c+=glow*glowAmt*pow(az,2.5)*(.35+.65*h);
    float s=max(dot(d,normalize(sunPos-cameraPosition)),0.);c+=halo*haloAmt*(.55*pow(s,420.)+.28*pow(s,26.)+.1*pow(s,6.));
    gl_FragColor=vec4(c,1.);
    #include <colorspace_fragment>
    gl_FragColor.rgb+=(fract(sin(dot(gl_FragCoord.xy,vec2(12.9898,78.233)))*43758.5453)-.5)/255.;}`,
 }));
 sky.renderOrder = -3; sky.frustumCulled = false;
 scene.add(sky);

 // Celestial sphere: stars (denser along the galactic plane) and the Milky Way band,
 // placed so the band crosses the frame behind the block during the night beat.
 const probe = heroCamera(); shoot(probe, 15);
 const f = probe.getWorldDirection(new THREE.Vector3()), up = new THREE.Vector3(0, 1, 0);
 const right = new THREE.Vector3().crossVectors(f, up).normalize(), screenUp = new THREE.Vector3().crossVectors(right, f);
 const along = right.clone().addScaledVector(screenUp, .55).normalize(), pole = new THREE.Vector3().crossVectors(f, along).normalize();
 const celestial = new THREE.Group();
 const band = new THREE.Mesh(new THREE.SphereGeometry(70, 128, 6, 0, TAU, Math.PI / 2 - .17, .34), new THREE.MeshBasicMaterial({ map: milkyWayTexture(), transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide, fog: false }));
 band.quaternion.setFromUnitVectors(up, pole); band.renderOrder = -2;
 const STARS = 3600, stars = glowPoints(STARS, { size: .4, opacity: 0 }), random = rng(17), starA = new Float32Array(STARS), twinkle = new Float32Array(STARS * 2);
 const tints = ['#cfe2ff', '#fff1d6', '#ffffff', '#e4ecff', '#ffd7ae'].map(c => new THREE.Color(c)), v = new THREE.Vector3();
 for (let i = 0; i < STARS; i++) {
  v.set(random() * 2 - 1, random() * 2 - 1, random() * 2 - 1);
  if (v.lengthSq() < 1e-4) v.set(1, 0, 0);
  v.normalize();
  if (i < 1100) v.addScaledVector(pole, -v.dot(pole) * (1 - Math.pow(random(), 2) * .9)).normalize(); // crowd toward the band
  stars.positions.set([v.x * 62, v.y * 62, v.z * 62], i * 3);
  const c = tints[Math.floor(random() * (random() < .9 ? 4 : 5))];
  stars.colors.set([c.r, c.g, c.b], i * 3);
  const b = random();
  stars.sizes[i] = .38 + Math.pow(b, 7) * 1.5;
  starA[i] = .45 + .55 * Math.pow(b, 2);
  twinkle[i * 2] = 1.5 + random() * 3.5; twinkle[i * 2 + 1] = random() * TAU;
 }
 stars.renderOrder = -1; stars.commit();
 celestial.add(band, stars);
 scene.add(celestial);
 const celestialAxis = new THREE.Vector3(0, Math.sin(LAT), -Math.cos(LAT));

 // The sky dome over the block: rim-lit shell, horizon and altitude rings, the sun's path and hour ticks.
 const shellU = { color: { value: new THREE.Color('#8fd6ee') }, opacity: { value: .2 } };
 const shell = new THREE.Mesh(new THREE.SphereGeometry(1, 72, 18, 0, TAU, 0, Math.PI / 2), new THREE.ShaderMaterial({
  uniforms: shellU, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending,
  vertexShader: 'varying vec3 vN;varying vec3 vP;void main(){vN=normalize(normalMatrix*normal);vec4 mv=modelViewMatrix*vec4(position,1.);vP=mv.xyz;gl_Position=projectionMatrix*mv;}',
  fragmentShader: 'uniform vec3 color;uniform float opacity;varying vec3 vN;varying vec3 vP;void main(){float f=1.-abs(dot(normalize(vN),normalize(-vP)));gl_FragColor=vec4(color*pow(f,3.)*opacity,1.);}',
 }));
 shell.scale.set(DOME_R, DOME_H, DOME_R); shell.position.y = DOME_Y;
 const ring = (alt, n = 160) => Array.from({ length: n + 1 }, (_, i) => { const a = i / n * TAU; return new THREE.Vector3(Math.cos(a) * Math.cos(alt) * DOME_R, DOME_Y + Math.sin(alt) * DOME_H, Math.sin(a) * Math.cos(alt) * DOME_R); });
 const horizon = line(ring(0), '#e8c37c', .4), rings = [line(ring(30 / DEG), '#8fd6ee', .14), line(ring(60 / DEG), '#8fd6ee', .12)];
 const meridian = line(Array.from({ length: 81 }, (_, i) => { const a = i / 80 * Math.PI; return new THREE.Vector3(0, DOME_Y + Math.sin(a) * DOME_H, -Math.cos(a) * DOME_R); }), '#8fd6ee', .12);
 const tmp = new THREE.Vector3();
 const path = line(Array.from({ length: 121 }, (_, i) => domePoint(sunVector(lerp(-.1, Math.PI + .1, i / 120), tmp), new THREE.Vector3())), '#f3d38e', .5);
 const TICKS = 13, ticks = glowPoints(TICKS, { size: .3, color: '#f3d38e' });
 for (let k = 0; k < TICKS; k++) { domePoint(sunVector(k * Math.PI / 12, tmp), tmp); ticks.positions.set([tmp.x, tmp.y, tmp.z], k * 3); }
 ticks.commit();
 // Sun geometry: a ray from the block centre and a drop line to the horizon plane.
 const rayGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, .8, 0), new THREE.Vector3()]);
 const dropGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(), new THREE.Vector3()]);
 const ray = new THREE.Line(rayGeo, new THREE.LineBasicMaterial({ color: '#ffd89a', transparent: true, opacity: 0, depthWrite: false }));
 const drop = new THREE.Line(dropGeo, new THREE.LineBasicMaterial({ color: '#ffd89a', transparent: true, opacity: 0, depthWrite: false }));
 const sun = glowPoints(3, { color: '#fff4d8' }), moon = glowPoints(2, { color: '#e6eeff' });
 sun.sizes.set([1.4, 3.6, 7.5]); moon.sizes.set([1, 3.4]);
 domePoint(MOON, tmp);
 moon.positions.set([tmp.x, tmp.y, tmp.z, tmp.x, tmp.y, tmp.z]); moon.commit();
 const overlays = [shell, horizon, ...rings, meridian, path, ticks, ray, drop, sun, moon];
 scene.add(...overlays);

 const dir = new THREE.Vector3(), pos = new THREE.Vector3(), am = new THREE.Color(), pm = new THREE.Color(), sunColor = new THREE.Color();
 const fog = new THREE.Color(), nightHemi = new THREE.Color('#07090f'), dayGround = new THREE.Color('#2b2418'), moonColor = new THREE.Color('#a9c1ee');
 function update(t) {
  const h = hourAngle(t), hm = ((h % TAU) + TAU) % TAU;
  sunVector(h, dir);
  const alt = Math.asin(dir.y) * DEG, morning = smooth(-.25, .25, dir.x);
  const day = smooth(-1.5, 4, alt), night = 1 - smooth(-13, -5, alt), cool = 1 - smooth(-12, 0, alt);
  sunColor.copy(ramp(SUN_PM, alt, pm)).lerp(ramp(SUN_AM, alt, am), morning);

  // Key light: the sun by day, the moon by night; both are ~0 near -3°, where it switches.
  if (alt > -3) {
   key.position.copy(dir).multiplyScalar(16);
   key.color.copy(sunColor); key.intensity = 2.9 * day;
   su.sunTan.value = dir.y / Math.max(1e-3, Math.hypot(dir.x, dir.z));
  } else {
   key.position.copy(MOON).multiplyScalar(16);
   key.color.copy(moonColor); key.intensity = .9 * night;
   su.sunTan.value = 9;
  }
  su.sunEast.value = smooth(-.3, .3, dir.x);
  ramp(HEMI, alt, hemi.color); hemi.groundColor.copy(dayGround).lerp(nightHemi, cool);
  hemi.intensity = ramp(HEMI_I, alt);
  rim.intensity = .3 * day + .2 * night;
  u.tint.value.set('#24467a'); u.tintMix.value = .24 * cool; u.grey.value = .2 * cool;
  // Beat 2: a touch of extra relief while the sun is low makes the long shadows read.
  const k = 1 + .3 * window01(t, 5.5, 11.8, 1.8);
  u.relief.value = k; sides.scale.y = water.scale.y = k;

  // Sky colour through day, civil/nautical/astronomical twilight and night.
  ramp(SKY_HI, alt, skyU.high.value); ramp(SKY_LO, alt, skyU.low.value);
  ramp(GLOW, alt, skyU.glow.value); skyU.glowAmt.value = .55 * smooth(-12, -2, alt) * (1 - smooth(4, 18, alt));
  skyU.sunDir.value.copy(dir);
  domePoint(dir, pos);
  skyU.sunPos.value.copy(pos); skyU.halo.value.copy(sunColor); skyU.haloAmt.value = smooth(-5, 1, alt);
  fog.copy(skyU.low.value).lerp(skyU.high.value, .55);
  scene.fog.color.copy(fog); scene.background.copy(fog);

  // Dome overlays fade to a whisper during the night beat and return before dawn.
  const ov = lerp(.12, 1, 1 - window01(t, 10.6, 17.3, 1.4)), vis = smooth(-3, .5, alt);
  shellU.opacity.value = .22 * ov;
  horizon.material.opacity = .4 * ov; path.material.opacity = .5 * ov; meridian.material.opacity = .12 * ov;
  for (const r of rings) r.material.opacity = .13 * ov;
  for (let i = 0; i < TICKS; i++) { const d = hm - i * Math.PI / 12; ticks.alphas[i] = ov * (.4 + .6 * Math.exp(-d * d / .012)); }
  ticks.geometry.attributes.alpha.needsUpdate = true;
  sun.positions.set([pos.x, pos.y, pos.z, pos.x, pos.y, pos.z, pos.x, pos.y, pos.z]);
  sun.alphas.set([vis, vis * .5, vis * .2]);
  for (let i = 0; i < 3; i++) sun.colors.set([lerp(1, sunColor.r, i * .5), lerp(1, sunColor.g, i * .5), lerp(1, sunColor.b, i * .5)], i * 3);
  sun.commit();
  rayGeo.attributes.position.setXYZ(1, pos.x, pos.y, pos.z); rayGeo.attributes.position.needsUpdate = true;
  dropGeo.attributes.position.setXYZ(0, pos.x, pos.y, pos.z); dropGeo.attributes.position.setXYZ(1, pos.x, DOME_Y, pos.z); dropGeo.attributes.position.needsUpdate = true;
  ray.material.opacity = .32 * vis * ov; drop.material.opacity = .28 * vis * ov;

  // Beat 3: stars twinkle in, the Milky Way rises, a moon lights the block.
  celestial.visible = night > .002;
  if (celestial.visible) {
   stars.material.uniforms.opacity.value = night; band.material.opacity = .7 * night;
   for (let i = 0; i < STARS; i++) stars.alphas[i] = starA[i] * (.72 + .28 * Math.sin(t * twinkle[i * 2] + twinkle[i * 2 + 1]));
   stars.geometry.attributes.alpha.needsUpdate = true;
   celestial.quaternion.setFromAxisAngle(celestialAxis, (t - 14) * .02);
  }
  moon.alphas.set([night, night * .3]); moon.geometry.attributes.alpha.needsUpdate = true;
  moon.visible = night > .002; sun.visible = vis > .002;

  shoot(camera, t);
 }
 update(0);
 return { scene, camera, update, dispose() {} };
}

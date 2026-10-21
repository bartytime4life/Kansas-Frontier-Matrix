import { THREE, HALF, WORLD, RELIEF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, glowTexture, scanCurtain, smooth, window01, lerp, clamp, easeInOut, rng, noise2, fbm, riverZ, TRIBUTARIES, tributaryPoint } from './kit.mjs';
// Agriculture: a patchwork of centre-pivot circles and row-crop fields. A soil
// moisture map sweeps dry → wet, the fields green up through the season, then
// a rain band crosses and the moisture map wets up behind it.

const SEGMENTS = 256, CELL = .75, GRID = Math.round(WORLD / CELL), PIVOT_R = .345;
const v3 = hex => { const c = new THREE.Color(hex); return `vec3(${c.r.toFixed(4)},${c.g.toFixed(4)},${c.b.toFixed(4)})`; };

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

/** Bilinear lookup into the built terrain heights: cheap enough for per-frame particles. */
function heightLookup(land, segments = SEGMENTS) {
 const n = segments + 1, step = WORLD / segments, b = land.base;
 return (x, z) => {
  const fx = clamp((x + HALF) / step, 0, segments - 1e-4), fz = clamp((z + HALF) / step, 0, segments - 1e-4);
  const i = Math.floor(fx), j = Math.floor(fz), u = fx - i, v = fz - j, k = j * n + i;
  return lerp(lerp(b[k], b[k + 1], u), lerp(b[k + n], b[k + n + 1], u), v) * RELIEF;
 };
}

function tributaryDistance(x, z) {
 let best = 99;
 for (const trib of TRIBUTARIES) {
  if (trib.side * (z - riverZ(x)) < 0) continue;
  const [tx] = tributaryPoint(trib, clamp(1 - Math.abs(z - riverZ(trib.x0)) / (HALF + .4)));
  best = Math.min(best, Math.abs(x - tx));
 }
 return best;
}

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 stage(scene, { fog: .022 });
 const land = terrain({ segments: SEGMENTS });
 liveSurface(land);
 const ground = heightLookup(land);
 scene.add(land.mesh, blockSides(land.sample), riverWater(land.sample));

 // Field layout: one quarter-section-like cell per texel. Valleys, creeks and the
 // hills band stay in pasture; the rest is pivots, row crops or split fields.
 const random = rng(41), cells = new Uint8Array(GRID * GRID * 4), pivots = [];
 for (let j = 0; j < GRID; j++) for (let i = 0; i < GRID; i++) {
  const x0 = -HALF + i * CELL, z0 = -HALF + j * CELL, cx = x0 + CELL / 2, cz = z0 + CELL / 2;
  let river = 99, creek = 99, lo = 99, hi = -99;
  for (const [x, z] of [[x0, z0], [x0 + CELL, z0], [x0, z0 + CELL], [x0 + CELL, z0 + CELL], [cx, cz]]) {
   river = Math.min(river, Math.abs(z - riverZ(x))); creek = Math.min(creek, tributaryDistance(x, z));
   const h = land.sample(x, z); lo = Math.min(lo, h); hi = Math.max(hi, h);
  }
  const uu = cx / HALF, vv = cz / HALF, hills = Math.exp(-Math.pow(uu - .38 + .12 * Math.sin(vv * 3.2), 2) / .018);
  const farm = river > .5 && creek > .32 && hills < .3 && hi - lo < .34 && random() > .1;
  const r = random();
  const type = !farm ? 0 : r < .42 ? 1 : r < .62 ? 2 : r < .82 ? 3 : 4;
  const k = (j * GRID + i) * 4;
  cells[k] = type; cells[k + 1] = Math.floor(random() * 255); cells[k + 2] = Math.floor(random() * 255); cells[k + 3] = Math.floor(random() * 255);
  if (type === 1) pivots.push({ x: cx, z: cz, phase: cells[k + 2] / 255 * Math.PI * 2 });
 }
 const cellTex = new THREE.DataTexture(cells, GRID, GRID, THREE.RGBAFormat);
 cellTex.magFilter = cellTex.minFilter = THREE.NearestFilter; cellTex.needsUpdate = true;

 // Static wetness pattern: valley bottoms and lowlands hold water, uplands dry out.
 const pos = land.geometry.attributes.position, wet = new Float32Array(pos.count), wn = noise2(33);
 for (let i = 0; i < pos.count; i++) {
  const x = pos.getX(i), z = pos.getZ(i), d = z - riverZ(x);
  wet[i] = clamp(.55 - .5 * (land.base[i] - .45) + .38 * fbm(wn, x * .32, z * .32, 3) + .4 * Math.exp(-d * d / 1.4));
 }
 land.geometry.setAttribute('aWet', new THREE.BufferAttribute(wet, 1));

 const au = {
  uCells: { value: cellTex }, uMoist: { value: 1 }, uFront: { value: -9 }, uFrontGlow: { value: 0 }, uAhead: { value: .1 }, uBehind: { value: .8 },
  uRainX: { value: -9 }, uRainBoost: { value: 0 }, uShadow: { value: 0 }, uGreen: { value: 0 }, uArmT: { value: 0 }, uArmVis: { value: 0 },
 };
 extendSurface(land.mesh.material, 'kfm-agriculture', au, {
  vDecl: 'attribute float aWet; varying float vWet; varying vec2 vXZ;',
  vMain: 'vWet = aWet; vXZ = position.xz;',
  fDecl: `uniform sampler2D uCells; uniform float uMoist, uFront, uFrontGlow, uAhead, uBehind, uRainX, uRainBoost, uShadow, uGreen, uArmT, uArmVis;
   varying float vWet; varying vec2 vXZ; float kArm, kSpray, kFront; vec3 kMoistC;
   vec3 kMoistRamp(float m) {
    vec3 c = mix(${v3('#d8b46e')}, ${v3('#b8853a')}, smoothstep(0., .28, m));
    c = mix(c, ${v3('#4f9c86')}, smoothstep(.3, .56, m));
    c = mix(c, ${v3('#21809a')}, smoothstep(.56, .8, m));
    return mix(c, ${v3('#1b4e88')}, smoothstep(.8, 1., m));
   }`,
  fColor: `
   vec3 col = diffuseColor.rgb; float patt = 1.;
   vec2 g = (vXZ + ${HALF.toFixed(2)}) / ${CELL.toFixed(3)}, ci = floor(g), f = fract(g);
   vec4 cell = texture2D(uCells, (ci + .5) / ${GRID.toFixed(1)});
   float type = floor(cell.r * 255. + .5);
   kArm = 0.; kSpray = 0.;
   if (type > .5) {
    vec2 p = (f - .5) * ${CELL.toFixed(3)};
    float split = step(3.5, type), sideB = step(.5, f.x);
    float ph = fract(cell.g + split * sideB * .37);
    float grow = smoothstep(ph * .5, ph * .5 + .42, uGreen);
    vec3 soil = mix(${v3('#5e4029')}, ${v3('#8a6542')}, cell.a);
    vec3 leaf = mix(${v3('#6f9a34')}, ${v3('#8fd34e')}, smoothstep(.3, 1., grow));
    if (type < 1.5) {
     // Centre pivot: wheel-track rings, a rotating arm and a wet wake behind it.
     float r = length(p), aa = fwidth(r) + 1e-4;
     float inside = 1. - smoothstep(${PIVOT_R} - aa, ${PIVOT_R} + aa, r);
     float tc = r * 90., track = .5 + .5 * cos(tc * 6.2832);
     track = mix(.5, track, clamp(1.4 - fwidth(tc) * 2., 0., 1.));
     float cover = smoothstep(0., .25, grow) * mix(.55 + .45 * track, 1., smoothstep(.5, .95, grow));
     vec3 field = mix(soil * (.9 + .16 * track), leaf, cover);
     float armA = cell.b * 6.2832 + uArmT;
     vec2 ad = vec2(cos(armA), sin(armA));
     float along = dot(p, ad), perp = abs(p.x * ad.y - p.y * ad.x);
     float lag = mod(armA - atan(p.y, p.x), 6.2832);
     kArm = (1. - smoothstep(.009, .009 + fwidth(perp) * 1.5, perp)) * step(0., along) * step(along, ${PIVOT_R}) * uArmVis;
     kSpray = exp(-lag * 2.2) * inside * uArmVis;
     field *= 1. - .2 * kSpray;
     col = mix(mix(col, ${v3('#7f8d4c')}, .6), field, inside);
     patt = mix(1., .88 + .2 * track, inside);
    } else {
     // Row crops: drilled rows that fill in to a closed canopy as the season runs.
     float alongX = type < 2.5 ? 1. : type < 3.5 ? 0. : 1. - sideB;
     float sc = mix(f.x, f.y, alongX) * ${CELL.toFixed(3)} * 26.;
     float stripe = .5 + .5 * cos(sc * 6.2832);
     stripe = mix(.5, stripe, clamp(1.4 - fwidth(sc) * 2., 0., 1.));
     float cover = smoothstep(0., .2, grow) * mix(stripe, 1., smoothstep(.45, .95, grow));
     col = mix(soil * (.84 + .26 * stripe), leaf, cover);
     float seam = split * (1. - smoothstep(.006, .012 + fwidth(f.x), abs(f.x - .5) * ${CELL.toFixed(3)}));
     col = mix(col, ${v3('#9d8a5e')}, seam * .7);
     patt = .9 + .18 * stripe * (1. - cover);
    }
    // Section roads between fields.
    float e = min(min(f.x, 1. - f.x), min(f.y, 1. - f.y)) * ${CELL.toFixed(3)};
    float road = 1. - smoothstep(.01, .016 + fwidth(e), e);
    col = mix(col, ${v3('#c2ab7c')}, road * .85);
    patt *= 1. - .25 * road;
   }
   // Soil-moisture map: a wet front from the west, then a rain band's wake.
   float behind = 1. - smoothstep(uFront - 1.3, uFront + 1.3, vXZ.x);
   float lvl = mix(uAhead, uBehind, behind) + uRainBoost * (1. - smoothstep(uRainX - 1.4, uRainX + .5, vXZ.x));
   float m = clamp(lvl + .45 * (vWet - .5), 0., 1.);
   kMoistC = kMoistRamp(m);
   col = mix(col, kMoistC * patt, uMoist);
   kFront = exp(-pow((vXZ.x - uFront) / .24, 2.)) * uFrontGlow;
   col *= 1. - uShadow * exp(-pow((vXZ.x - uRainX + .6) / 1.7, 2.));
   diffuseColor.rgb = col;`,
  fEmissive: `totalEmissiveRadiance += kMoistC * .07 * uMoist + ${v3('#7fd3ea')} * (kFront * .45 + kSpray * .2) + ${v3('#f3d38e')} * kArm * .8;`,
 });

 const curtain = scanCurtain({ color: '#7fd3ea', height: 1.6 });
 curtain.material.opacity = 0;
 scene.add(curtain);

 // Spray along each pivot arm: a few faint points that ride the arm round.
 const SPRAY = 5, spray = glowPoints(pivots.length * SPRAY, { size: .2, color: '#9fe0f2' });
 scene.add(spray);

 // Rain band: falling streaks, ground splashes and a soft cloud deck above.
 const STREAKS = 700, TOP = 3.1, random2 = rng(77);
 const sx = new Float32Array(STREAKS), sz = new Float32Array(STREAKS), sp = new Float32Array(STREAKS);
 for (let i = 0; i < STREAKS; i++) { sx[i] = (random2() + random2() + random2() - 1.5) * .9; sz[i] = lerp(-HALF + .1, HALF - .1, random2()); sp[i] = random2(); }
 const rainGeo = new THREE.BufferGeometry();
 rainGeo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(STREAKS * 6), 3));
 rainGeo.setAttribute('color', new THREE.BufferAttribute(new Float32Array(STREAKS * 6), 3));
 const rain = new THREE.LineSegments(rainGeo, new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false }));
 rain.frustumCulled = false;
 const SPLASH = 260, splash = glowPoints(SPLASH, { size: .14, color: '#bfeaf7' });
 const kx = new Float32Array(SPLASH), kz = new Float32Array(SPLASH), kp = new Float32Array(SPLASH);
 for (let i = 0; i < SPLASH; i++) { kx[i] = (random2() + random2() - 1) * .9; kz[i] = lerp(-HALF + .2, HALF - .2, random2()); kp[i] = random2(); }
 const cloudMat = new THREE.SpriteMaterial({ map: glowTexture(), color: '#6b7e8c', transparent: true, opacity: 0, depthWrite: false });
 const clouds = [];
 for (let i = 0; i < 9; i++) {
  const s = new THREE.Sprite(cloudMat);
  s.userData = { dx: (random2() - .5) * .9, y: TOP + .15 + random2() * .25, z: lerp(-HALF - .4, HALF + .4, i / 8) + (random2() - .5) * .6 };
  s.scale.set(3.4 + random2() * 1.4, 1.6 + random2() * .6, 1);
  clouds.push(s);
 }
 scene.add(rain, splash, ...clouds);
 const rc = new THREE.Color('#9fd8ee');

 function update(t) {
  // Beat 1 (0–5.5 s): the moisture map wets up behind a front crossing west → east.
  const front = lerp(-HALF - 1.8, HALF + 1.8, easeInOut(smooth(.5, 5, t)));
  au.uFront.value = front; curtain.at(front);
  const frontVis = window01(t, .4, 5.3, .5);
  au.uFrontGlow.value = frontVis; curtain.material.opacity = frontVis * .42 * smooth(HALF + .8, HALF - .4, Math.abs(front));
  au.uMoist.value = 1 - smooth(4.6, 6.2, t) + .88 * smooth(10.6, 12, t) + .12 * smooth(14.6, 16, t);
  const dry = smooth(14.4, 16, t);
  au.uAhead.value = t < 8 ? .1 : lerp(.34, .1, dry);
  au.uBehind.value = t < 8 ? .8 : lerp(.34, .1, dry);

  // Beat 2 (5.5–11 s): fields green up at staggered dates; pivots sweep and spray.
  au.uGreen.value = smooth(5.8, 10.6, t) * (1 - smooth(14.6, 16, t));
  const armT = t * Math.PI * 2 / 16, armVis = window01(t, 5.6, 15.8, .9);
  au.uArmT.value = armT; au.uArmVis.value = armVis;
  spray.visible = armVis > .01;
  if (spray.visible) {
   pivots.forEach((pv, i) => {
    const a = pv.phase + armT, c = Math.cos(a), s = Math.sin(a);
    for (let k = 0; k < SPRAY; k++) {
     const r = PIVOT_R * (k + .7) / SPRAY, x = pv.x + c * r, z = pv.z + s * r, n = i * SPRAY + k;
     spray.positions.set([x, ground(x, z) + .07, z], n * 3);
     spray.alphas[n] = armVis * (.25 + .2 * Math.sin(t * 7 + n));
    }
   });
   spray.commit();
  }

  // Beat 3 (11–16 s): a rain band crosses; the moisture map wets behind it, then dries back.
  const rainX = lerp(-HALF - 3, HALF + 3, clamp((t - 11.2) / 4.2)), rainVis = window01(t, 11.1, 15.6, .5);
  au.uRainX.value = rainX;
  au.uRainBoost.value = .5 * smooth(11.2, 11.8, t) * (1 - dry);
  au.uShadow.value = .38 * rainVis;
  rain.visible = splash.visible = rainVis > .01;
  for (const s of clouds) { s.visible = rain.visible; s.position.set(rainX - .5 + s.userData.dx, s.userData.y, s.userData.z); }
  cloudMat.opacity = .5 * rainVis;
  if (rain.visible) {
   const p = rainGeo.attributes.position.array, col = rainGeo.attributes.color.array;
   for (let i = 0; i < STREAKS; i++) {
    const x = rainX + sx[i], z = sz[i], g = ground(x, z), fall = (sp[i] + t * 1.6) % 1, y = TOP - fall * (TOP - g);
    const a = rainVis * (Math.abs(x) < HALF - .05 ? 1 : 0) * (1 - Math.abs(sx[i]) / 1.6) * smooth(0, .08, fall);
    p.set([x, y, z, x - .05, y + .34, z], i * 6);
    col.set([rc.r * a, rc.g * a, rc.b * a, rc.r * a * .12, rc.g * a * .12, rc.b * a * .12], i * 6);
   }
   rainGeo.attributes.position.needsUpdate = rainGeo.attributes.color.needsUpdate = true;
   for (let i = 0; i < SPLASH; i++) {
    const x = rainX + kx[i], z = kz[i], s = (kp[i] + t * 2.1) % 1;
    splash.positions.set([x, ground(x, z) + .03, z], i * 3);
    splash.alphas[i] = rainVis * (Math.abs(x) < HALF - .05 ? 1 : 0) * Math.pow(1 - s, 3) * .6;
    splash.sizes[i] = .06 + s * .16;
   }
   splash.commit();
  }

  // Dip lower for the season's field detail, back up for the loop.
  orbit(camera, t, { radius: 21.5, height: 10.8 - 1.6 * window01(t, 4.5, 16, 3.5), target: [0, -.7, 0], start: -.95 + .3 * Math.sin(t / 16 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update, dispose() { cellTex.dispose(); } };
}

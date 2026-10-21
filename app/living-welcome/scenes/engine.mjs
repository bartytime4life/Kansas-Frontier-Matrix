import * as THREE from 'three';
import { SCENE_CATALOG, beatIndex } from './catalog.mjs';
import { SCENE_LOADERS } from './index.mjs';
import { disposeTree, clamp, POINT_SCALE } from './kit.mjs';

const MAX_DPR = 1.75, MIN_DPR = .75, SLOW_MS = 24, FAST_MS = 13, WIDE = 1.5;

/**
 * One WebGL renderer for every welcome scene. Only the selected scene exists;
 * switching disposes the previous one. Nothing renders while paused, and a
 * reduced-motion viewer gets a single still frame per scene.
 */
export function createSceneEngine(canvas, { onBeat, onReady, onError } = {}) {
 let renderer;
 try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false, stencil: false, powerPreference: 'high-performance' });
 } catch (error) { onError?.(error); return null; }
 renderer.outputColorSpace = THREE.SRGBColorSpace;
 renderer.toneMapping = THREE.ACESFilmicToneMapping;
 renderer.toneMappingExposure = 1.08;
 renderer.localClippingEnabled = true;
 let dpr = Math.min(MAX_DPR, window.devicePixelRatio || 1), ceiling = dpr;
 renderer.setPixelRatio(dpr);

 let current = null, wanted = null, token = 0, paused = true, reduced = false, frame = 0, last = 0, clock = 0, beat = -1, slow = 0, quick = 0, ema = 16;

 function resize() {
  const w = canvas.clientWidth || 1, h = canvas.clientHeight || 1;
  renderer.setSize(w, h, false);
  POINT_SCALE.value = 420 * h * dpr / 900; // glow sizes were tuned on a 900-device-pixel-tall stage
  const camera = current?.camera;
  if (camera?.isPerspectiveCamera) {
   camera.aspect = w / h;
   // Narrow and portrait screens keep the landscape horizontal extent by widening
   // the vertical field of view, so no scene crops its subject at the sides.
   const base = camera.userData.baseFov ??= camera.fov;
   camera.fov = camera.aspect >= WIDE ? base : THREE.MathUtils.radToDeg(2 * Math.atan(Math.tan(THREE.MathUtils.degToRad(base) / 2) * WIDE / camera.aspect));
   // Pan the projection (not the camera) so the subject sits right of the cards on wide screens.
   const shift = (camera.userData.shift ?? 0) * clamp((w / h - 1) / .8);
   if (shift) camera.setViewOffset(w, h, -w * shift, 0, w, h); else camera.clearViewOffset();
   camera.updateProjectionMatrix();
  }
  current?.resize?.(w, h);
 }
 const observer = new ResizeObserver(() => { resize(); if (!running()) draw(0); });
 observer.observe(canvas);

 const running = () => Boolean(current && !paused && !reduced && !document.hidden);
 function draw(dt) {
  if (!current) return;
  const duration = current.duration;
  const t = reduced ? duration * .62 : clock % duration;
  current.update(t, dt);
  renderer.render(current.scene, current.camera);
  const index = beatIndex(current.id, t);
  if (index !== beat) { beat = index; onBeat?.(current.id, index); }
 }
 function loop(now) {
  frame = 0;
  if (!running()) return;
  const ms = last ? now - last : 16.7;
  last = now;
  const dt = Math.min(.05, ms / 1000);
  clock += dt;
  draw(dt);
  adapt(ms);
  frame = requestAnimationFrame(loop);
 }
 // Trade pixel density for frame time, and win it back when there is headroom.
 function adapt(ms) {
  ema = ema * .94 + Math.min(ms, 80) * .06;
  if (ema > SLOW_MS) { quick = 0; if (++slow > 75 && dpr > MIN_DPR) { dpr = Math.max(MIN_DPR, dpr - .25); renderer.setPixelRatio(dpr); resize(); slow = 0; } }
  else if (ema < FAST_MS) { slow = 0; if (++quick > 360 && dpr < ceiling) { dpr = Math.min(ceiling, dpr + .25); renderer.setPixelRatio(dpr); resize(); quick = 0; } }
  else { slow = 0; quick = 0; }
 }
 function start() {
  if (frame || !running()) { if (current && !running()) draw(0); return; }
  last = 0; frame = requestAnimationFrame(loop);
 }
 function stop() { cancelAnimationFrame(frame); frame = 0; }
 const visibility = () => { if (document.hidden) stop(); else start(); };
 document.addEventListener('visibilitychange', visibility);
 // A lost GPU context (driver reset, too many contexts) must not freeze the
 // page: stop, fade out, and rebuild the current scene if the context returns.
 const lost = event => { event.preventDefault(); stop(); canvas.dataset.switching = 'true'; onError?.(new Error('WebGL context lost')); };
 const restored = () => { const id = wanted; wanted = null; if (current) { current.dispose?.(); current = null; } if (id) show(id); };
 canvas.addEventListener('webglcontextlost', lost);
 canvas.addEventListener('webglcontextrestored', restored);

 async function show(id) {
  if (!SCENE_LOADERS[id] || id === wanted) return;
  wanted = id;
  const mine = ++token;
  canvas.dataset.switching = 'true';
  let loaded;
  try { loaded = await SCENE_LOADERS[id](); } catch (error) { if (mine === token) onError?.(error); return; }
  if (mine !== token) return;
  // Let the fade-out finish before the swap so the cut lands in the dark.
  await new Promise(resolve => setTimeout(resolve, 160));
  if (mine !== token) return;
  const next = loaded.create({ THREE, renderer });
  const previous = current;
  current = { ...next, id, duration: SCENE_CATALOG[id].duration };
  if (previous) { previous.dispose?.(); disposeTree(previous.scene); }
  clock = 0; beat = -1;
  resize(); stop(); draw(0);
  delete canvas.dataset.switching;
  onReady?.(id);
  start();
 }

 return {
  show,
  setPaused(value) { paused = Boolean(value); if (paused) { stop(); if (current) draw(0); } else start(); },
  setReduced(value) { reduced = Boolean(value); stop(); if (current) draw(0); start(); },
  /** Jump to loop time `t` (seconds) and draw; used for review and stills. */
  seek(t) { clock = t; if (current) draw(0); },
  get sceneId() { return current?.id; },
  /** Average ms per frame for `frames` renders, waiting on the GPU each time (review only). */
  measure(frames = 60) {
   if (!current) return null;
   const gl = renderer.getContext(), pixel = new Uint8Array(4), start = performance.now();
   for (let i = 0; i < frames; i++) { draw(1 / 60); clock += 1 / 60; gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, pixel); }
   return { ms: (performance.now() - start) / frames, dpr, size: [canvas.width, canvas.height] };
  },
  get pixelRatio() { return dpr; },
  dispose() {
   token++; stop(); observer.disconnect(); document.removeEventListener('visibilitychange', visibility);
   canvas.removeEventListener('webglcontextlost', lost); canvas.removeEventListener('webglcontextrestored', restored);
   if (current) { current.dispose?.(); disposeTree(current.scene); current = null; }
   // No forceContextLoss: React may hand the same canvas to the next engine
   // (Strict Mode, fast refresh), and a detached canvas frees its context anyway.
   renderer.dispose();
  },
 };
}

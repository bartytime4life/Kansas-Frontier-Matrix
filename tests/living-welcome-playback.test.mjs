import test from 'node:test';
import assert from 'node:assert/strict';
import { bindPlayback, fitScene } from '../app/living-welcome/motion-playback.mjs';

function media() {
  const events = new Map(), pending = [];
  return { muted: false, playsInline: false, playing: false, released: false, pauses: 0,
    addEventListener(type, fn) { events.set(type, fn); }, removeEventListener(type) { events.delete(type); },
    play() { this.playing = true; return new Promise((resolve, reject) => pending.push({ resolve, reject })); },
    pause() { this.playing = false; this.pauses++; }, removeAttribute(name) { if (name === 'src') this.released = true; }, load() {},
    loaded() { events.get('loadeddata')?.(); }, pending, events,
  };
}
test('pause wins over a delayed play promise and loading cannot restart it', async () => {
  const video = media(), controller = bindPlayback(video);
  controller.setPaused(true); video.pending[0].resolve(); await Promise.resolve(); video.loaded();
  assert.equal(video.playing, false); assert.equal(video.pending.length, 1);
  controller.setPaused(false); assert.equal(video.playing, true); controller.dispose();
  assert.equal(video.released, true); assert.equal(video.events.size, 0); assert.equal(video.playing, false);
});
test('an older play completion does not stop a newer active request', async () => {
  const video = media(), controller = bindPlayback(video);
  video.loaded(); video.pending[0].resolve(); await Promise.resolve();
  assert.equal(video.playing, true); controller.dispose();
});
test('a detached video cannot restart, and a stale failure cannot affect its replacement', async () => {
  const video = media(); let failures = 0;
  const controller = bindPlayback(video, { onBlocked: () => failures++ }); controller.dispose();
  video.pending[0].reject(new Error('late network error')); await Promise.resolve(); await Promise.resolve();
  video.loaded(); assert.equal(failures, 0); assert.equal(video.playing, false); assert.equal(video.events.size, 0);
});
test('active playback failure is reported so the UI can offer a retry', async () => {
  const video = media(); let failures = 0;
  const controller = bindPlayback(video, { onBlocked: () => failures++ });
  video.pending[0].reject(new Error('blocked')); await Promise.resolve(); await Promise.resolve();
  assert.equal(failures, 1); controller.dispose();
});
test('portrait, archival and widescreen subjects fit the available frame without cropping', () => {
  for (const box of [{ x: 0, y: 0, w: 1440, h: 800 }, { x: 8, y: 500, w: 374, h: 760 }]) {
    for (const aspect of [2 / 3, 4 / 3, 16 / 9, 21 / 9]) {
      const r = fitScene(box, aspect);
      assert.ok(r.x >= box.x - 1e-8 && r.y >= box.y - 1e-8);
      assert.ok(r.x + r.w <= box.x + box.w + 1e-8 && r.y + r.h <= box.y + box.h + 1e-8);
      assert.ok(Math.abs(r.w / r.h - aspect) < 1e-9);
    }
  }
});

test('a reused media element restores its source after development-mode cleanup', () => {
  const video=media();
  const first=bindPlayback(video,{src:'/motion/tractor.webm'});first.dispose();
  const second=bindPlayback(video,{src:'/motion/tractor.webm'});
  assert.equal(video.src,'/motion/tractor.webm');assert.equal(video.playing,true);second.dispose();
});

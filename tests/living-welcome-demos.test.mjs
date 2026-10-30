import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile, readdir } from 'node:fs/promises';
import { componentHarness, findNode } from './component-harness.mjs';
import { MAP_DEMOS, mapDemos, demoDuration } from '../app/living-welcome/map-demos.mjs';
import { CATEGORY_IDS } from '../app/living-welcome/catalog.mjs';
import { bindPlayback } from '../app/living-welcome/motion-playback.mjs';
import { categoryGlimpse, capabilityPreviews } from '../app/living-welcome/capability-catalog.mjs';

function media() {
  const events = new Map(), pending = [];
  return { playing: false, released: false, currentTime: 0,
    addEventListener: (name, callback) => events.set(name, callback), removeEventListener: name => events.delete(name),
    play() { this.playing = true; return new Promise((resolve, reject) => pending.push({ resolve, reject })); },
    pause() { this.playing = false; }, removeAttribute(name) { if (name === 'src') this.released = true; }, load() {}, pending,
  };
}

async function capability() {
 const listeners = new Map(), document = { hidden: false, addEventListener: (name, fn) => listeners.set(name, fn), removeEventListener: name => listeners.delete(name) };
 const h = await componentHarness('app/living-welcome/CapabilityPreview.jsx', { './motion-playback.mjs': { bindPlayback } }, { document });
 const props = { demo: capabilityPreviews('weather')[0], paused: false }, video = media();
 const render = () => {
  const tree = h.render(h.exports.CapabilityPreview, props), node = findNode(tree, n => n.type === 'video');
  if (node) node.props.ref.current = video;
  h.commit(); return tree;
 };
 return { h, props, video, document, listeners, render };
}

test('all twenty-one categories have distinct, bounded layer demonstrations', () => {
 const ids = ['engineering','transport','aviation','weather','disaster','water','groundwater','geology','terrain','ecology','fauna','agriculture','history','land','people','government','public-safety','places','science','sky','evidence'];
 assert.equal(new Set(ids.map(id => categoryGlimpse(id)?.title)).size, 21);
 for (const id of ids) for (const field of ['title','summary','try','limit']) assert.ok(categoryGlimpse(id)[field], `${id}: ${field}`);
 assert.equal(categoryGlimpse('__proto__'), null);
 assert.deepEqual(capabilityPreviews('science'), [], 'terrain footage must not impersonate a satellite demonstration');
 assert.deepEqual(capabilityPreviews('geology'), [], 'groundwater footage must not impersonate the earthquake map');
});

test('opening a category loads a still, then only an explicitly requested tour decoder', async () => {
 const h = await capability(); let tree = h.render();
 assert.equal(findNode(tree, n => n.type === 'video'), undefined);
 assert.equal(findNode(tree, n => n.type === 'img').props.src, h.props.demo.poster);
 assert.equal(h.video.pending.length, 0);
 findNode(tree, n => n.type === 'button').props.onClick(); tree = h.render();
 assert.equal(findNode(tree, n => n.type === 'video').props.preload, 'none');
 assert.equal(h.video.src, h.props.demo.src);
 assert.equal(h.video.playing, true);
 h.props.demo = capabilityPreviews('weather')[1]; tree = h.render();
 assert.equal(findNode(tree, n => n.type === 'video'), undefined, 'changing tours never auto-downloads the next video');
 assert.equal(h.video.playing, false); assert.equal(h.video.released, true);
 h.h.dispose(); assert.equal(h.listeners.size, 0);
});

test('requested tours stop at the end, honor hidden/global pause, and can recover', async () => {
 const h = await capability(); let tree = h.render();
 findNode(tree, n => n.type === 'button').props.onClick(); tree = h.render();
 h.document.hidden = true; h.listeners.get('visibilitychange')(); tree = h.render();
 h.video.pending[0].resolve(); await Promise.resolve(); assert.equal(h.video.playing, false);
 h.document.hidden = false; h.listeners.get('visibilitychange')(); tree = h.render(); assert.equal(h.video.playing, true);
 h.props.paused = true; tree = h.render(); assert.equal(h.video.playing, false);
 assert.equal(findNode(tree, n => n.type === 'button').props.disabled, true);
 h.props.paused = false; tree = h.render();
 h.video.ended = true; h.video.currentTime = 7;
 findNode(tree, n => n.type === 'video').props.onEnded(); tree = h.render(); assert.equal(h.video.playing, false);
 findNode(tree, n => n.type === 'button').props.onClick(); tree = h.render(); assert.equal(h.video.currentTime, 0);
 findNode(tree, n => n.type === 'video').props.onError(); tree = h.render();
 assert.equal(findNode(tree, n => n.type === 'video'), undefined); assert.equal(h.video.playing, false);
 assert.ok(findNode(tree, n => n.props?.role === 'status'));
 findNode(tree, n => n.type === 'button').props.onClick(); tree = h.render(); assert.equal(h.video.playing, true);
 h.h.dispose(); assert.equal(h.video.playing, false);
});
async function demoPanel(extra = {}) {
  const listeners = new Map(), document = { hidden: false, addEventListener: (name, callback) => listeners.set(name, callback), removeEventListener: name => listeners.delete(name) };
  const calls = [], h = await componentHarness('app/living-welcome/MapDemoPanel.jsx', {
    './map-demos.mjs': { mapDemos, demoDuration }, './motion-playback.mjs': { bindPlayback },
  }, { document });
  const props = { category: 'weather', onTry: demo => calls.push(['try', demo.id]), onPlaybackChange: value => calls.push(['playing', value]), ...extra };
  const video = media();
  const render = () => {
    const tree = h.render(h.exports.MapDemoPanel, props), node = findNode(tree, node => node.type === 'video');
    if (node) node.props.ref.current = video;
    h.commit(); return tree;
  };
  return { h, props, calls, video, document, listeners, render };
}
function select(tree, number = 0) { return findNode(tree, node => node.props?.className === 'map-demo-choices').props.children[number]; }

test('each topic has two uniquely identified recordings with an existing tool destination', () => {
  const ids = new Set();
  for (const category of CATEGORY_IDS) {
    const demos = MAP_DEMOS[category]; assert.equal(demos.length, 2);
    demos.forEach((demo, index) => {
      assert.equal(demo.id, `${category}-${index + 1}`); assert.ok(!ids.has(demo.id)); ids.add(demo.id);
      assert.match(demo.src, /^\/welcome\/demos\/[a-z]+-[12]\.webm$/);
      assert.match(demo.poster, /^\/welcome\/demos\/[a-z]+-[12]\.jpg$/);
      assert.ok(demo.title && demo.caption && demo.sourceTime && demo.limitation);
      assert.ok(['action', 'topic'].includes(demo.destination.kind));
      if (demo.destination.kind === 'action') assert.ok(['layers', 'time', 'underground', 'qwen'].includes(demo.destination.value));
      else assert.ok(['weather', 'water', 'science', 'groundwater', 'history', 'transport', 'agriculture', 'land', 'terrain', 'places'].includes(demo.destination.value));
    });
  }
  assert.equal(ids.size, 16); assert.deepEqual(mapDemos('missing'), []);
});

test('reduced motion leaves demos as posters until an explicit selection, with just one mounted player', async () => {
  const h = await demoPanel({ reducedMotion: true }); let tree = h.render();
  assert.equal(findNode(tree, node => node.type === 'video'), undefined);
  assert.equal(h.video.pending.length, 0, 'no video request before selection');
  select(tree).props.onClick(); tree = h.render();
  assert.equal(findNode(tree, node => node.type === 'video').props.src, mapDemos('weather')[0].src);
  assert.equal(h.video.pending.length, 1, 'explicit Play overrides poster-only reduced motion');
  const fullSize = findNode(tree, node => node.props?.className === 'map-demo-full-size');
  assert.equal(fullSize.type, 'a'); assert.equal(fullSize.props.href, mapDemos('weather')[0].src);
  assert.equal(fullSize.props.target, '_blank'); assert.equal(fullSize.props.rel, 'noreferrer');
  select(tree, 1).props.onClick(); tree = h.render();
  const players = [];
  const collect = node => { if (!node || typeof node !== 'object') return; if (node.type === 'video') players.push(node); for (const child of [node.props?.children].flat(Infinity)) collect(child); };
  collect(tree); assert.equal(players.length, 1); assert.equal(players[0].props.src, mapDemos('weather')[1].src);
  assert.equal(h.video.released, true, 'old decoder source is released before replacement');
  findNode(tree, node => node.props?.['aria-label'] === 'Close map tour player').props.onClick(); tree = h.render();
  assert.equal(findNode(tree, node => node.type === 'video'), undefined); assert.equal(h.video.playing, false);
  h.h.dispose();
});

test('shared pause and hidden tabs beat a late successful play request', async () => {
  const h = await demoPanel(); let tree = h.render(); select(tree).props.onClick(); tree = h.render();
  h.props.paused = true; tree = h.render();
  h.video.pending[0].resolve(); await Promise.resolve();
  assert.equal(h.video.playing, false);
  assert.equal(select(tree).props.disabled, true);
  h.props.paused = false; tree = h.render(); assert.equal(h.video.playing, true);
  h.document.hidden = true; h.listeners.get('visibilitychange')(); tree = h.render();
  assert.equal(h.video.playing, false);
  h.video.pending.at(-1).resolve(); await Promise.resolve(); assert.equal(h.video.playing, false);
  h.h.dispose(); assert.equal(h.listeners.size, 0);
});

test('recorded playback can pause, replay, recover from failure and still open its real tool', async () => {
  const h = await demoPanel(); let tree = h.render(); select(tree).props.onClick(); tree = h.render();
  findNode(tree, node => node.type === 'video').props.onPlay(); tree = h.render();
  select(tree).props.onClick(); tree = h.render();
  assert.equal(tree.props['data-state'], 'playing', 'reselecting the playing recording does not leave a permanent loading state');
  findNode(tree, node => node.props?.['aria-label'] === 'Pause map tour').props.onClick(); tree = h.render();
  assert.equal(h.video.playing, false);
  findNode(tree, node => node.props?.['aria-label'] === 'Play map tour').props.onClick(); tree = h.render();
  assert.equal(h.video.playing, true);
  h.video.currentTime = 12; findNode(tree, node => node.type === 'video').props.onEnded(); tree = h.render();
  findNode(tree, node => node.props?.['aria-label'] === 'Replay map tour').props.onClick(); tree = h.render();
  assert.equal(h.video.currentTime, 0); assert.equal(h.video.playing, true);
  findNode(tree, node => node.type === 'video').props.onError(); tree = h.render();
  assert.equal(findNode(tree, node => node.type === 'video'), undefined);
  assert.ok(findNode(tree, node => node.props?.className === 'map-demo-failure'));
  findNode(tree, node => node.type === 'button' && node.props.children === 'Retry tour').props.onClick(); tree = h.render();
  assert.ok(findNode(tree, node => node.type === 'video'));
  findNode(tree, node => node.props?.className === 'welcome-text-action').props.onClick();
  assert.ok(h.calls.some(call => call[0] === 'try' && call[1] === 'weather-1'));
  h.h.dispose();
});

test('duration captions do not invent a duration before recording metadata exists', () => {
  assert.equal(demoDuration(null), 'Short demo'); assert.equal(demoDuration(16), '0:16'); assert.equal(demoDuration(65), '1:05'); assert.equal(demoDuration(59.8), '1:00');
});


// Inspect container headers directly so a manifest cannot accidentally bless a
// thumbnail-sized export as a high-definition map recording. No ffprobe or
// platform-specific media dependency is needed in the release test runner.
function jpegDimensions(bytes) {
  assert.equal(bytes.readUInt16BE(0), 0xffd8, 'poster is a JPEG');
  let cursor = 2;
  const frames = new Set([0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf]);
  while (cursor < bytes.length) {
    assert.equal(bytes[cursor++], 0xff, 'valid JPEG marker boundary');
    while (bytes[cursor] === 0xff) cursor++;
    const marker = bytes[cursor++];
    if (marker === 0xd9 || marker === 0xda) break;
    if (marker === 0x01 || marker >= 0xd0 && marker <= 0xd7) continue;
    const length = bytes.readUInt16BE(cursor);
    assert.ok(length >= 2 && cursor + length <= bytes.length, 'bounded JPEG segment');
    if (frames.has(marker)) return { width: bytes.readUInt16BE(cursor + 5), height: bytes.readUInt16BE(cursor + 3) };
    cursor += length;
  }
  assert.fail('poster has no decodable JPEG dimensions');
}
function webmDimensions(bytes) {
  assert.equal(bytes.readUInt32BE(0), 0x1a45dfa3, 'recording has an EBML/WebM header');
  const masters = new Set([0x1a45dfa3, 0x18538067, 0x1549a966, 0x1654ae6b, 0xae, 0xe0]);
  let width, height, durationUnits, timecodeScale = 1_000_000;
  function vint(offset, identifier = false) {
    const first = bytes[offset]; let length = 1, marker = 0x80;
    while (length <= 8 && !(first & marker)) { marker >>= 1; length++; }
    assert.ok(first && length <= 8 && offset + length <= bytes.length, 'bounded EBML integer');
    let value = BigInt(identifier ? first : first & (marker - 1));
    for (let index = 1; index < length; index++) value = value * 256n + BigInt(bytes[offset + index]);
    const unknown = !identifier && value === (1n << BigInt(7 * length)) - 1n;
    assert.ok(unknown || value <= BigInt(Number.MAX_SAFE_INTEGER), 'bounded EBML element size');
    return { value: unknown ? null : Number(value), length };
  }
  function scan(start, end, video = false, depth = 0) {
    assert.ok(depth < 10, 'bounded WebM hierarchy');
    for (let cursor = start; cursor < end;) {
      const id = vint(cursor, true), size = vint(cursor + id.length);
      const body = cursor + id.length + size.length, next = size.value === null ? end : body + size.value;
      assert.ok(body <= next && next <= end, 'bounded WebM element');
      if (video && (id.value === 0xb0 || id.value === 0xba)) {
        assert.ok(size.value > 0 && size.value <= 4, 'valid video dimension');
        if (id.value === 0xb0) width = bytes.readUIntBE(body, size.value);
        else height = bytes.readUIntBE(body, size.value);
      } else if (id.value === 0x2ad7b1) timecodeScale = bytes.readUIntBE(body, size.value);
      else if (id.value === 0x4489) {
        assert.ok(size.value === 4 || size.value === 8, 'valid WebM duration');
        durationUnits = size.value === 4 ? bytes.readFloatBE(body) : bytes.readDoubleBE(body);
      }
      if (masters.has(id.value)) scan(body, next, video || id.value === 0xe0, depth + 1);
      cursor = next;
    }
  }
  scan(0, bytes.length);
  assert.ok(width > 0 && height > 0, 'recording has a video track');
  return { width, height, durationSeconds: durationUnits === undefined ? null : durationUnits * timecodeScale / 1_000_000_000 };
}

test('all 16 rendered map tours ship real HD assets with matching fingerprints, frame provenance and observation clocks', async () => {
  const manifest = JSON.parse(await readFile('scripts/welcome-demos/runtime-assets.json', 'utf8'));
  const demos = Object.values(MAP_DEMOS).flat(), ids = new Set(demos.map(demo => demo.id));
  assert.equal(demos.length, 16); assert.equal(ids.size, 16);
  assert.equal(manifest.captures.length, 16, 'all recordings retain their capture provenance');
  const captures = new Map(manifest.captures.map(capture => [capture.id, capture]));
  assert.equal(captures.size, 16, 'capture IDs are unique');
  assert.deepEqual([...captures.keys()].sort(), [...ids].sort(), 'no recording is substituted or omitted');
  const expectedPaths = new Set(demos.flatMap(demo => [demo.src, demo.poster]));
  const fingerprints = new Map(manifest.files.map(file => [file.path, file]));
  assert.equal(manifest.files.length, 32); assert.equal(fingerprints.size, 32, 'asset fingerprints are unique');
  assert.deepEqual([...fingerprints.keys()].sort(), [...expectedPaths].sort(), 'every public demo and poster has provenance');
  const disk = (await readdir('public/welcome/demos')).filter(name => /\.(?:webm|jpg)$/.test(name)).map(name => `/welcome/demos/${name}`);
  assert.deepEqual(disk.sort(), [...expectedPaths].sort(), 'no public demo assets are missing or orphaned');
  let usedBytes = 0;
  for (const demo of demos) {
    const capture = captures.get(demo.id);
    assert.equal(capture.category, demo.category); assert.equal(capture.kind, 'rendered-software-tour');
    assert.equal(capture.width, 1280); assert.equal(capture.height, 720);
    assert.equal(capture.frameCount, 120, `${demo.id}: 120 actual map frames`);
    assert.equal(capture.playbackFps, 24); assert.equal(capture.encodedFrameCount, 168, `${demo.id}: final 7-second tour at 24 fps`);
    assert.ok(Number.isFinite(capture.captureWallSeconds) && capture.captureWallSeconds > 0, `${demo.id}: measured capture wall time retained`);
    assert.match(capture.inputFramesSha256, /^[0-9a-f]{64}$/, `${demo.id}: ordered native map-frame digest aggregate retained`);
    if (capture.inputFrameHashes !== undefined) {
      assert.equal(capture.inputFrameHashes.length, 120, `${demo.id}: one digest for each actual input frame`);
      for (const digest of capture.inputFrameHashes) assert.match(digest, /^[0-9a-f]{64}$/);
      assert.equal(createHash('sha256').update(capture.inputFrameHashes.join('\n')+'\n').digest('hex'), capture.inputFramesSha256, `${demo.id}: aggregate binds the ordered native frame digests`);
    }
    assert.ok(Number.isFinite(Date.parse(capture.capturedAt)), `${demo.id}: actual capture time retained`);
    assert.ok(Array.isArray(capture.sourceTimes) && capture.sourceTimes.length > 0 && capture.sourceTimes.every(value => typeof value === 'string' && value.trim()), `${demo.id}: source clocks retained`);
    assert.ok(Array.isArray(capture.attribution) && capture.attribution.length > 0 && capture.attribution.every(value => typeof value === 'string' && value.trim()), `${demo.id}: provider attribution retained`);
    assert.ok(Array.isArray(capture.sources), `${demo.id}: actual requested sources retained`);
    if (capture.nativeMapViewport) {
      assert.ok(capture.nativeMapViewport.pixelWidth >= 1280 && capture.nativeMapViewport.pixelHeight >= 720, `${demo.id}: native map pixels were not upscaled`);
      assert.ok(capture.nativeMapViewport.width >= 640 && capture.nativeMapViewport.height >= 360, `${demo.id}: bounded original map viewport`);
    } else {
      // The first exports retained a verified minimum-resolution proof rather
      // than measurements. Preserve that distinction without inventing values.
      const proof = capture.nativeResolutionProof;
      assert.ok(proof && Number.isFinite(proof.minimumPixelWidth) && proof.minimumPixelWidth >= 1280 && Number.isFinite(proof.minimumPixelHeight) && proof.minimumPixelHeight >= 720, `${demo.id}: native minimum-resolution proof retained`);
      assert.equal(proof.noUpscaling, true, `${demo.id}: native-resolution proof forbids upscaling`);
      assert.ok(typeof proof.verificationMethod === 'string' && proof.verificationMethod.trim(), `${demo.id}: resolution verification method retained`);
    }
    assert.deepEqual(capture.destination, demo.destination);
    assert.equal(demo.durationSeconds, 7, `${demo.id}: finalized playback duration, no placeholder`);
    assert.equal(capture.encodedFrameCount / capture.playbackFps, demo.durationSeconds, `${demo.id}: frame count agrees with final playback time`);
    assert.ok(typeof capture.cameraMethod === 'string' && capture.cameraMethod.trim(), `${demo.id}: actual camera sampling method retained`);
    for (const camera of [capture.start, capture.end]) {
      assert.ok(Array.isArray(camera?.center) && camera.center.length === 2 && camera.center.every(Number.isFinite), `${demo.id}: sampled camera center retained`);
      assert.ok(Number.isFinite(camera.zoom) && Number.isFinite(camera.bearing) && Number.isFinite(camera.pitch), `${demo.id}: sampled camera view retained`);
    }
    assert.doesNotMatch(demo.sourceTime, /actual forecast valid time recorded with this clip|coming soon|placeholder/i);
    if (demo.id === 'weather-2') {
      assert.ok(capture.sourceTimes.some(value => /valid.*\d{4}-\d{2}-\d{2}T/.test(value)), 'wind capture retains its actual forecast valid time');
      assert.match(demo.sourceTime, /\d{4}-\d{2}-\d{2}/, 'public wind demo names its recorded forecast clock');
    }
    for (const path of [demo.src, demo.poster]) {
      const fingerprint = fingerprints.get(path), bytes = await readFile(`public${path}`);
      assert.ok(Number.isInteger(fingerprint.bytes) && fingerprint.bytes > 0, `${path}: nonempty asset fingerprint`);
      assert.equal(bytes.length, fingerprint.bytes, `${path}: byte count matches publication artifact`);
      assert.match(fingerprint.sha256, /^[0-9a-f]{64}$/);
      assert.equal(createHash('sha256').update(bytes).digest('hex'), fingerprint.sha256, `${path}: SHA-256 matches publication artifact`);
      usedBytes += bytes.length;
      if (path.endsWith('.webm')) {
        assert.ok(bytes.length > 20_000, `${path}: real recorded video payload`);
        const dimensions = webmDimensions(bytes);
        assert.equal(dimensions.width, 1280); assert.equal(dimensions.height, 720);
        if (dimensions.durationSeconds !== null) assert.ok(Math.abs(dimensions.durationSeconds - demo.durationSeconds) <= .75, `${path}: container duration agrees with public caption`);
      } else assert.deepEqual(jpegDimensions(bytes), { width: 1280, height: 720 }, `${path}: full-resolution poster`);
    }
  }
  assert.equal(usedBytes, manifest.usedBytes, 'release byte total covers every packaged demo asset');
});

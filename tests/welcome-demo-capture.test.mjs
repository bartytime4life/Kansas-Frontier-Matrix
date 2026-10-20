import test from 'node:test';
import assert from 'node:assert/strict';
import { Readable } from 'node:stream';
import { capturePixelRatio, nativeCaptureReady, captureBasemapSourceIds, captureCameraAt, jpegDataUrlBytes } from '../scripts/welcome-demos/capture-metrics.mjs';
import { DEMO_SCENARIOS } from '../scripts/welcome-demos/scenarios.mjs';
import { captureRequestTarget, captureOriginAllowed, welcomeDemoCapturePlugin } from '../scripts/welcome-demos/capture-sink.mjs';

test('capture sink accepts only exact known demo filenames without query or traversal', () => {
  assert.deepEqual(captureRequestTarget('/__welcome-demo-capture/weather-1.webm'), { file: 'weather-1.webm', extension: 'webm' });
  assert.deepEqual(captureRequestTarget('/__welcome-demo-capture/weather-1.rejected.webm'), { file: 'weather-1.rejected.webm', extension: 'webm' });
  assert.equal(captureRequestTarget('/__welcome-demo-capture/weather-1.rejected.other.webm'), null);
  assert.deepEqual(captureRequestTarget('/__welcome-demo-capture/weather-1.frame-000.jpg'), { file: 'weather-1.frame-000.jpg', extension: 'jpg' });
  assert.deepEqual(captureRequestTarget('/__welcome-demo-capture/farming-2.frame-119.jpg'), { file: 'farming-2.frame-119.jpg', extension: 'jpg' });
  for (const name of ['weather-1.frame-120.jpg', 'weather-1.frame-999.jpg', 'weather-1.frame-1.jpg', 'weather-1.frame-000.jpg?path=/tmp/elsewhere']) assert.equal(captureRequestTarget(`/__welcome-demo-capture/${name}`), null);
  for (const path of ['/__welcome-demo-capture/../weather-1.webm', '/__welcome-demo-capture/weather-3.webm', '/__welcome-demo-capture/fake-1.webm', '/__welcome-demo-capture/weather-1.webm?path=/tmp/elsewhere', '/__welcome-demo-capture/weather-1.mp4', '/__welcome-demo-capture/weather-1.webm/anything']) assert.equal(captureRequestTarget(path), null, path);
});
test('capture requires the exact local same origin and a loopback connection', () => {
  assert.equal(captureOriginAllowed('http://127.0.0.1:5188', '127.0.0.1:5188', '127.0.0.1'), true);
  for (const [origin, host, remote] of [
    ['http://evil.example', '127.0.0.1:5188', '127.0.0.1'], ['http://127.0.0.1:5189', '127.0.0.1:5188', '127.0.0.1'],
    ['http://127.0.0.1:5188', '127.0.0.1:5188', '192.0.2.1'], ['http://localhost:5188', '127.0.0.1:5188', '127.0.0.1'],
    [undefined, '127.0.0.1:5188', '127.0.0.1'],
  ]) assert.equal(captureOriginAllowed(origin, host, remote), false);
});
async function rejectRequest({ url = '/__welcome-demo-capture/weather-1.webm', method = 'POST', origin = 'http://127.0.0.1:5188', type = 'video/webm', length, body = Buffer.from('fake data') } = {}) {
  let handler;
  welcomeDemoCapturePlugin().configureServer({ middlewares: { use(value) { handler = value; } } });
  const request = Readable.from([body]);
  request.url = url; request.method = method; request.headers = { origin, host: '127.0.0.1:5188', 'content-type': type, ...(length === undefined ? {} : { 'content-length': String(length) }) };
  request.socket = { remoteAddress: '127.0.0.1' };
  const response = { statusCode: 200, setHeader() {}, end(value) { this.body = value; } };
  await handler(request, response, () => { response.next = true; });
  return response;
}
test('sink rejects unsafe methods, origins, content types, oversized and invalid bytes before writing', async () => {
  assert.equal((await rejectRequest({ method: 'GET' })).statusCode, 404);
  assert.equal((await rejectRequest({ origin: 'https://attacker.example' })).statusCode, 403);
  assert.equal((await rejectRequest({ type: 'text/plain' })).statusCode, 415);
  assert.equal((await rejectRequest({ length: 33 * 1024 * 1024 })).statusCode, 413);
  assert.equal((await rejectRequest()).statusCode, 400);
  assert.equal((await rejectRequest({ url: '/__welcome-demo-capture/weather-1.json', type: 'application/json', body: Buffer.from('{"id":"other","kind":"recorded-software-demo"}') })).statusCode, 400);
});
test('all eight categories have two bounded recipes with truthful source limits and supported destinations', () => {
  assert.equal(DEMO_SCENARIOS.length, 16);
  assert.equal(new Set(DEMO_SCENARIOS.map(item => item.id)).size, 16);
  for (const category of ['weather', 'science', 'government', 'rivers', 'underground', 'history', 'transport', 'farming']) {
    assert.deepEqual(DEMO_SCENARIOS.filter(item => item.category === category).map(item => item.id), [`${category}-1`, `${category}-2`]);
  }
  for (const scene of DEMO_SCENARIOS) {
    assert.ok(scene.limitation && scene.sourceTime);
    assert.equal(scene.durationSeconds, 5);
    assert.ok(scene.start.center[0] >= -102.1 && scene.start.center[0] <= -94.5);
    assert.ok(scene.start.center[1] >= 36.9 && scene.start.center[1] <= 40.1);
    assert.ok(scene.destination.kind === 'topic' || scene.destination.kind === 'action' && scene.destination.value === 'underground');
  }
});

test('HD validation uses actual native map pixels without unnecessary GPU scaling', () => {
  assert.equal(capturePixelRatio(1280, 816), 1);
  assert.equal(capturePixelRatio(1280, 576), 1.25);
  assert.equal(capturePixelRatio(640, 360), 1.5);
  assert.equal(nativeCaptureReady({ width: 1920, height: 864, clientWidth: 1280, clientHeight: 576 }), true);
  assert.equal(nativeCaptureReady({ width: 1280, height: 816, clientWidth: 1280, clientHeight: 816 }), true);
  assert.equal(nativeCaptureReady({ width: 960, height: 540, clientWidth: 640, clientHeight: 360 }), false);
  assert.equal(nativeCaptureReady({ width: 1280, height: 720, clientWidth: 320, clientHeight: 180 }), false);
});
test('source readiness excludes hidden unrelated overlays while retaining actual basemap sources', () => {
  assert.deepEqual(captureBasemapSourceIds({ sources: {
    openmaptiles: { type: 'vector' }, 'external-old-weather': { type: 'raster' },
    'kfm-selection': { type: 'geojson' }, 'scene-stars': { type: 'geojson' },
  } }), ['openmaptiles']);
  assert.deepEqual(captureBasemapSourceIds({ sources: { 'esri-imagery': { type: 'raster' } } }), ['esri-imagery']);
});

test('manual capture clock interpolates only bounded camera fields', () => {
  const start = { center: [-100, 38], zoom: 6, pitch: 0, bearing: -10 };
  const end = { center: [-98, 39], zoom: 8, pitch: 40, bearing: 10 };
  assert.deepEqual(captureCameraAt(start, end, .5), { center: [-99, 38.5], zoom: 7, pitch: 20, bearing: 0 });
  assert.deepEqual(captureCameraAt(start, end, 5), end);
  assert.deepEqual(captureCameraAt(start, end, -2), start);
  assert.deepEqual(captureCameraAt(start, end, Number.NaN), start);
  assert.deepEqual(start.center, [-100, 38]);
});

test('synchronous frame decoding admits only bounded JPEG canvas output', () => {
  assert.deepEqual([...jpegDataUrlBytes('data:image/jpeg;base64,/9j/2Q==')], [255, 216, 255, 217]);
  for (const value of ['data:image/png;base64,/9j/2Q==', 'data:image/jpeg;base64,ZmFrZQ==', '', null]) assert.throws(() => jpegDataUrlBytes(value));
  assert.throws(() => jpegDataUrlBytes('data:image/jpeg;base64,' + 'A'.repeat(2_666_672)));
});

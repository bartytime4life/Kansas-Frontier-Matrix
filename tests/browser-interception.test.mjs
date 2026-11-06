import { isolateBrowserNetwork } from './browser-network.mjs';
import assert from "node:assert/strict";
import test from "node:test";
import vm from "node:vm";
import { isStaleInterceptionCancellation, createInterceptionErrorTracker } from "./browser-interception.mjs";

test("browser navigation cancellation never hides live-request or unrelated protocol failures", () => {
  const canceled = new Error(JSON.stringify({ code: -32602, message: "Invalid InterceptionId." }));
  assert.equal(isStaleInterceptionCancellation(canceled, 1, 2), true);
  assert.equal(isStaleInterceptionCancellation(canceled, 2, 2), false, "same-document failure remains fatal");
  assert.equal(isStaleInterceptionCancellation(canceled, 2, 2, true), true, "browser-confirmed cancellation can occur within a document");
  assert.equal(isStaleInterceptionCancellation(canceled, 2, 2, "true"), false, "cancellation requires positive confirmation");
  assert.equal(isStaleInterceptionCancellation(canceled, 3, 2), false, "only earlier navigation is eligible");
  for (const error of [
    new Error("CDP timeout: Fetch.fulfillRequest"),
    new Error('not JSON: {"code":-32602,"message":"Invalid InterceptionId."}'),
    new Error(JSON.stringify({ code: -32000, message: "Invalid InterceptionId." })),
    new Error(JSON.stringify({ code: -32602, message: "Invalid parameters" })),
    new Error(JSON.stringify({ code: -32602, message: "Invalid InterceptionId. Additional failure" })),
  ]) {
    assert.equal(isStaleInterceptionCancellation(error, 1, 2), false);
    assert.equal(isStaleInterceptionCancellation(error, 2, 2, true), false);
  }
});

function trackerHarness() {
  const timers = new Map(); let next = 0;
  const tracker = createInterceptionErrorTracker({
    setTimer(fn, delay) { assert.equal(delay, 1000); timers.set(++next, fn); return next; },
    clearTimer(id) { timers.delete(id); },
  });
  return { tracker, expire() { for (const fn of [...timers.values()]) fn(); }, timers };
}
const invalidId = () => new Error(JSON.stringify({ code: -32602, message: 'Invalid InterceptionId.' }));
const mediaRequest = () => ({ networkId: '7294.925', requestNavigation: 25, navigation: 25, url: '/welcome/motion/clouds-preview.webm' });

test('same-navigation media cancellation is confirmed before or after its Fetch error', async () => {
  for (const eventFirst of [true, false]) {
    const { tracker, timers } = trackerHarness();
    const event = { requestId: '7294.925', canceled: true };
    if (eventFirst) tracker.loadingFailed(event);
    tracker.failed(invalidId(), mediaRequest());
    let complete = false;
    const checked = tracker.assertHealthy().then(() => { complete = true; });
    await Promise.resolve();
    if (!eventFirst) {
      assert.equal(complete, false, 'qualification waits for confirmation, not just an empty error array');
      tracker.loadingFailed(event);
    }
    await checked;
    assert.equal(timers.size, 0);
    assert.deepEqual(tracker.errors, []);
  }
});

test('missing, mismatched and non-canceled events remain fatal after the bounded confirmation window', async () => {
  for (const event of [null, {requestId:'other',canceled:true}, {requestId:'7294.925',canceled:false}, {requestId:'7294.925',canceled:'true'}]) {
    const { tracker, expire, timers } = trackerHarness();
    tracker.failed(invalidId(), mediaRequest());
    if (event) tracker.loadingFailed(event);
    const checked = assert.rejects(tracker.assertHealthy(), /Invalid InterceptionId.*clouds-preview.webm.*navigation=25\/25/);
    expire(); await checked;
    tracker.loadingFailed({requestId:'7294.925',canceled:true});
    await assert.rejects(tracker.assertHealthy(), /Invalid InterceptionId/, 'late confirmation cannot erase a recorded failure');
    assert.equal(timers.size, 0);
  }
});

test('confirmation is request-specific and never swallows unrelated protocol errors', async () => {
  const {tracker,expire}=trackerHarness();
  tracker.failed(invalidId(),mediaRequest());
  tracker.failed(invalidId(),{...mediaRequest(),networkId:'second'});
  tracker.loadingFailed({requestId:'7294.925',canceled:true});
  const checked=assert.rejects(tracker.assertHealthy(), /network=second/);
  expire(); await checked;
  for (const error of [new Error('CDP timeout'),new Error('{"code":-32000,"message":"Invalid InterceptionId."}')]) {
    const {tracker,timers}=trackerHarness();
    tracker.loadingFailed({requestId:'7294.925',canceled:true});
    tracker.failed(error,mediaRequest());
    await assert.rejects(tracker.assertHealthy());
    assert.equal(timers.size,0);
  }
});

test('only navigation already stale at failure is immediately excused; missing IDs are fatal', async () => {
  const {tracker,timers}=trackerHarness();
  tracker.failed(invalidId(),{...mediaRequest(),requestNavigation:24});
  await tracker.assertHealthy(); assert.equal(timers.size,0);
  tracker.failed(invalidId(),{...mediaRequest(),networkId:undefined});
  await assert.rejects(tracker.assertHealthy(), /Invalid InterceptionId/);
  assert.equal(timers.size,0);
});

test('late paused requests need matching network and replaced document-loader evidence', async () => {
  for (const eventFirst of [true,false]) {
    const {tracker,timers}=trackerHarness();
    tracker.frameNavigated({frame:{id:'frame',loaderId:'old'}});
    const confirm=()=>{
      tracker.frameNavigated({frame:{id:'frame',loaderId:'new'}});
      tracker.requestWillBeSent({requestId:'7294.925',frameId:'frame',loaderId:'old'});
    };
    if(eventFirst)confirm();
    tracker.failed(invalidId(),mediaRequest());
    const checked=tracker.assertHealthy();
    if(!eventFirst)confirm();
    await checked; assert.equal(timers.size,0);
  }
  for (const identity of [
    {requestId:'7294.925',frameId:'frame',loaderId:'new'},
    {requestId:'other',frameId:'frame',loaderId:'old'},
    {requestId:'7294.925',frameId:'other',loaderId:'old'},
    {requestId:'7294.925',frameId:'frame',loaderId:''},
  ]) {
    const {tracker,expire}=trackerHarness();
    tracker.frameNavigated({frame:{id:'frame',loaderId:'old'}});
    tracker.frameNavigated({frame:{id:'frame',loaderId:'new'}});
    tracker.requestWillBeSent(identity);
    tracker.failed(invalidId(),mediaRequest());
    const checked=assert.rejects(tracker.assertHealthy(),/Invalid InterceptionId/);
    expire();await checked;
  }
});

test('network isolation refuses non-loopback or ambiguous origins before issuing CDP commands', async () => {
  for(const origin of ['https://127.0.0.1:5182/','http://example.com/','http://user@127.0.0.1:5182/','http://127.0.0.1:5182/path','http://127.0.0.1:5182/?query=1','http://127.0.0.1:5182/#fragment']) {
    let called=false;
    await assert.rejects(isolateBrowserNetwork(async()=>{called=true;},origin),/loopback origin/);
    assert.equal(called,false);
  }
});


test('ordinary navigation never pauses the engine; delayed-scene tests opt in without widening network access', async () => {
  for (const interceptScene of [false, true]) {
    const commands = [];
    await isolateBrowserNetwork(async (method, params) => commands.push({method, params}),
      'http://127.0.0.1:5182/', {interceptScene});
    const patterns = commands.find(x => x.method === 'Fetch.enable').params.patterns;
    assert.deepEqual(patterns, [
      {urlPattern: 'http://127.0.0.1:5182/api/*'},
      ...(interceptScene ? [{urlPattern: 'http://127.0.0.1:5182/assets/map-engine-*.js'}] : []),
    ]);
    assert.deepEqual(commands.find(x => x.method === 'Network.setBlockedURLs').params.urlPatterns,
      [{urlPattern: 'http://127.0.0.1:5182/*', block: false}, {urlPattern: '*://*:*/*', block: true}]);
  }
});

test('unavailable window APIs resolve locally while worker transport stays intercepted', async () => {
  const commands = [], sent = [];
  await isolateBrowserNetwork(async (method, params) => commands.push({ method, params }), 'http://127.0.0.1:5182/', { unavailableApis: true });
  assert.deepEqual(commands.find(command => command.method === 'Fetch.enable').params.patterns,
    [{ urlPattern: 'http://127.0.0.1:5182/api/*' }], 'worker API requests retain explicit transport isolation');
  const rules = commands.find(command => command.method === 'Network.setBlockedURLs').params.urlPatterns;
  assert.deepEqual(rules, [
    { urlPattern: 'http://127.0.0.1:5182/api/build', block: false },
    { urlPattern: 'http://127.0.0.1:5182/api/*', block: true },
    { urlPattern: 'http://127.0.0.1:5182/*', block: false },
    { urlPattern: '*://*:*/*', block: true },
  ], 'native page API reads remain blocked before reaching the actual server');
  const window = { fetch: async input => { sent.push(String(input)); return new Response('actual build or asset'); } };
  vm.runInNewContext(commands.find(command => command.method === 'Page.addScriptToEvaluateOnNewDocument').params.source,
    { window, location: { href: 'http://127.0.0.1:5182/' }, URL, Request, Response, DOMException });
  const unavailable = await window.fetch('/api/live-context?feed=census-counties');
  assert.equal(unavailable.status, 503);
  assert.deepEqual(await unavailable.json(), { error: 'Isolated navigation test: provider unavailable' });
  const controller = new AbortController(); controller.abort();
  await assert.rejects(window.fetch('/api/live-context', { signal: controller.signal }), { name: 'AbortError' });
  assert.deepEqual(sent, [], 'aborted and unavailable reads never invoke native fetch');
  assert.equal((await window.fetch('/api/build')).status, 200);
  assert.equal((await window.fetch('/assets/actual.js')).status, 200);
  assert.deepEqual(sent, ['/api/build', '/assets/actual.js']);
});

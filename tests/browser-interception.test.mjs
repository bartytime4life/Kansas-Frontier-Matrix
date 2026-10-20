import assert from "node:assert/strict";
import test from "node:test";
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

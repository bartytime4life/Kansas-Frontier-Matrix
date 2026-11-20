import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const imports = { "next/link": { default: "a" }, "next/dynamic": { default: () => "connection-map" }, "../connection-series": { VALUE_COLUMNS: {}, series: () => [] }, "./connections.css": {} };
const receipt = { captureId: "a".repeat(64), sourceId: "noaa-ncei", retrievedAt: "2026-11-19T12:00:00Z", byteLength: 100, entityBytes: 50, sha256: "b".repeat(64), validation: "structure-valid", partial: false, query: {}, limitation: "Fixture", entityHashes: [] };
const captured = { cached: false, receipt, view: { sourceId: receipt.sourceId, query: {}, rows: [{ value: 1 }], total: 1, partial: false, retrievedAt: receipt.retrievedAt, limitation: "Fixture", releaseState: "unreleased" } };
const profiled = { state: "complete", captured: 1, outcomes: [{ sourceId: receipt.sourceId, state: "quarantined", captureId: receipt.captureId }] };
const source = id => ({ id, name: id, kind: "table", fields: [{ key: "start", type: "date", default: "2026-11-19", label: "Start" }], configured: true, missing: [], holds: [], state: "ready", docs: "https://example.test/", limitation: "Fixture", limitBytes: 1000, releaseState: "unreleased" });
const catalog = { owner: true, sources: [source("noaa-ncei"), source("usdm-statistics")], host: { state: "ready", configured: true, paused: false, host: "Fixture", usedBytes: 0, limitBytes: 1000 } };
const response = body => ({ ok: true, json: async () => body });
const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };
const message = tree => findNode(tree, node => node.props?.["aria-live"] === "polite").props.children;
const panel = tree => findNode(tree, node => node.props?.["aria-label"] === "Verified capture");
const profileButton = tree => findNode(tree, node => node.type === "button" && node.props.children === "Capture configured profiles");
const actions = [
  { name: "capture", milliseconds: 60_000, value: captured, start: tree => findNode(tree, node => node.type === "form").props.onSubmit({ preventDefault() {} }), success: /Stored bytes verified/ },
  { name: "replay", milliseconds: 30_000, value: { ...captured, cached: true }, start: tree => findNode(tree, node => node.type === "button" && node.props.children === "Replay capture").props.onClick(), success: /Verified saved capture replayed/ },
  { name: "profiles", milliseconds: 120_000, value: profiled, start: tree => profileButton(tree).props.onClick(), success: /1 configured-profile capture\(s\) stored/ },
];
function clock() {
  const timers = new Map(); let next = 0;
  return {
    timers,
    globals: { setTimeout: (fn, milliseconds) => { const id = ++next; timers.set(id, { fn, milliseconds }); return id; }, clearTimeout: id => timers.delete(id) },
    expire(milliseconds) { const item = [...timers].find(([, timer]) => timer.milliseconds === milliseconds); assert.ok(item, `expected a ${milliseconds}ms action deadline`); timers.delete(item[0]); item[1].fn(); },
  };
}
async function setup(actionRequest) {
  const time = clock(); let statusCalls = 0;
  const h = await componentHarness("app/connections/workspace.tsx", imports, { ...time.globals, fetch: async (url, options) => {
    if (url.includes("action=view") || options?.method === "POST") return actionRequest(url, options);
    if (url.includes("action=captures")) return response({ captures: [receipt] });
    statusCalls++; return response(catalog);
  } });
  const render = () => { const tree = h.render(h.exports.default, {}); h.commit(); return tree; };
  render(); await settle(); await settle(); assert.equal(time.timers.size, 0);
  return { h, render, time, statusCalls: () => statusCalls };
}

for (const stage of ["fetch", "body"]) {
  test(`a stalled ${stage} times out each Connections action even when its adapter ignores abort`, async () => {
    for (const action of actions) {
      const delayed = deferred(); let signal;
      const { h, render, time, statusCalls } = await setup((_url, options) => {
        signal = options.signal;
        return stage === "fetch" ? delayed.promise : { ok: true, json: () => delayed.promise };
      });
      try {
        action.start(render()); await settle(); assert.equal(profileButton(render()).props.disabled, true);
        time.expire(action.milliseconds); await settle(); let tree = render();
        assert.equal(signal.aborted, true); assert.equal(time.timers.size, 0);
        assert.equal(profileButton(tree).props.disabled, false); assert.match(message(tree), /too long to respond/i);
        if (action.name === "replay") assert.match(message(tree), /try replaying.*again/i);
        else assert.match(message(tree), /may.*stored|may.*completed/i);
        if (action.name !== "replay") assert.match(message(tree), /saved captures before retrying/i);
        assert.equal(panel(tree), undefined); assert.equal(statusCalls(), 1, "timeouts do not schedule another capture or refresh");
        const timeoutMessage = message(tree);
        delayed.resolve(stage === "fetch" ? response(action.value) : action.value); await settle(); tree = render();
        assert.equal(message(tree), timeoutMessage); assert.equal(panel(tree), undefined); assert.equal(time.timers.size, 0);
      } finally { h.dispose(); }
    }
  });
}

test("stalled error bodies have the same deadline and recovery behavior", async () => {
  for (const action of actions) {
    const { h, render, time } = await setup(() => ({ ok: false, json: () => new Promise(() => {}) }));
    try {
      action.start(render()); await settle(); time.expire(action.milliseconds); await settle();
      assert.match(message(render()), /too long to respond/i); assert.equal(profileButton(render()).props.disabled, false);
    } finally { h.dispose(); }
  }
});

test("a valid retry after timeout succeeds and the older response cannot overwrite it", async () => {
  for (const action of actions) {
    const old = deferred(); let calls = 0;
    const { h, render, time } = await setup(() => ++calls === 1 ? old.promise : response(action.value));
    try {
      action.start(render()); await settle(); time.expire(action.milliseconds); await settle();
      action.start(render()); await settle(); await settle(); let tree = render();
      assert.match(message(tree), action.success); assert.equal(profileButton(tree).props.disabled, false); assert.equal(time.timers.size, 0);
      const success = message(tree);
      old.resolve(response(null)); await settle(); tree = render();
      assert.equal(message(tree), success); assert.equal(calls, 2); assert.equal(time.timers.size, 0);
    } finally { h.dispose(); }
  }
});

test("successful and rejected actions clear their deadlines without changing their existing messages", async () => {
  for (const action of actions) {
    for (const valid of [true, false]) {
      const { h, render, time } = await setup(() => response(valid ? action.value : null));
      try {
        action.start(render()); await settle(); await settle(); const tree = render();
        assert.equal(time.timers.size, 0); assert.equal(profileButton(tree).props.disabled, false);
        assert.match(message(tree), valid ? action.success : /invalid/i);
      } finally { h.dispose(); }
    }
  }
});

test("changing source or query cancels the old action and clears its deadline immediately", async () => {
  for (const change of ["source", "query"]) for (const action of actions) {
    const old = deferred(); let signal;
    const { h, render, time } = await setup((_url, options) => { signal = options.signal; return old.promise; });
    try {
      action.start(render()); await settle(); const tree = render();
      if (change === "source") findNode(tree, node => node.type === "button" && node.props?.["aria-pressed"] === false).props.onClick();
      else findNode(tree, node => node.type === "input").props.onChange({ target: { value: "2026-11-18" } });
      await settle(); assert.equal(signal.aborted, true); assert.equal(time.timers.size, 0);
      assert.equal(profileButton(render()).props.disabled, false); assert.equal(message(render()), "");
      old.resolve(response(action.value)); await settle(); assert.equal(message(render()), ""); assert.equal(panel(render()), undefined);
    } finally { h.dispose(); }
  }
});

test("unmount cancels every action and clears deadline resources even if fetch never settles", async () => {
  for (const action of actions) {
    let signal;
    const { h, render, time } = await setup((_url, options) => { signal = options.signal; return new Promise(() => {}); });
    action.start(render()); await settle(); assert.equal(time.timers.size, 1);
    h.dispose(); await settle(); assert.equal(signal.aborted, true); assert.equal(time.timers.size, 0);
    assert.equal(message(h.render(h.exports.default, {})), "");
  }
});

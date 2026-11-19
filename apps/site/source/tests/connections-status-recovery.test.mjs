import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";
import { catalog as providerCatalog } from "../app/api-connections-runtime/connections.mjs";

const imports = {
  "next/link": { default: "a" }, "next/dynamic": { default: () => "connection-map" },
  "../connection-series": { VALUE_COLUMNS: {}, series: () => [] }, "./connections.css": {},
};
const catalog = (owner = false) => ({
  owner,
  host: { state: "ready", configured: true, paused: false, host: "local test host", usedBytes: 0, limitBytes: 1000 },
  sources: [{ id: "noaa-ncei", name: "NOAA NCEI", kind: "table", fields: [], configured: true, missing: [], holds: [], state: "ready", docs: "https://example.test/", limitation: "Test source", limitBytes: 100, releaseState: "unreleased" }],
});
const response = body => ({ ok: true, json: async () => body });
const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };
const statusButton = tree => findNode(tree, node => node.type === "button" && /^(Refresh|Retry source|Refreshing)/.test(node.props.children));
const alert = tree => findNode(tree, node => node.props?.role === "alert");
const hasSource = tree => Boolean(findNode(tree, node => node.type === "strong" && node.props.children === "NOAA NCEI"));

async function setup(fetch, globals = {}) {
  const h = await componentHarness("app/connections/workspace.tsx", imports, { fetch, ...globals });
  const render = () => { const tree = h.render(h.exports.default, {}); h.commit(); return tree; };
  return { h, render };
}

function clock() {
  const timers = new Map(); let next = 0;
  return {
    timers,
    globals: { setTimeout: (fn, milliseconds) => { const id = ++next; timers.set(id, { fn, milliseconds }); return id; }, clearTimeout: id => timers.delete(id) },
    expire: () => { const timer = timers.values().next().value; assert.ok(timer); assert.equal(timer.milliseconds, 15_000); timer.fn(); },
  };
}

test("initial status failure is visible, retry announces pending, and a successful catalog replaces the failure", async () => {
  const retry = deferred(); let calls = 0;
  const { h, render } = await setup(() => ++calls === 1 ? Promise.reject(new Error("host offline")) : retry.promise);
  let tree = render(); await settle(); tree = render();
  assert.match(alert(tree).props.children, /Source status is unavailable/);
  assert.equal(findNode(tree, node => node.props?.role === "status"), undefined, "failure cannot remain a loading message");
  assert.equal(statusButton(tree).props.children, "Retry source status");
  assert.equal(statusButton(tree).props.disabled, false);
  statusButton(tree).props.onClick(); tree = render();
  assert.equal(alert(tree), undefined);
  assert.equal(statusButton(tree).props.disabled, true);
  assert.equal(statusButton(tree).props["aria-busy"], true);
  assert.match(findNode(tree, node => node.props?.role === "status").props.children, /Checking hosted/);
  retry.resolve(response(catalog())); await settle(); tree = render();
  assert.equal(alert(tree), undefined); assert.equal(hasSource(tree), true);
  assert.equal(statusButton(tree).props.children, "Refresh status");
  assert.equal(statusButton(tree).props.disabled, false);
  h.dispose();
});

test("a failed refresh preserves the previous catalog and identifies it as potentially out of date", async () => {
  let calls = 0;
  const { h, render } = await setup(() => ++calls === 1 ? Promise.resolve(response(catalog())) : Promise.reject(new Error("host offline")));
  render(); await settle(); let tree = render(); assert.equal(hasSource(tree), true);
  statusButton(tree).props.onClick(); tree = render();
  assert.equal(hasSource(tree), true); assert.equal(alert(tree), undefined);
  await settle(); tree = render();
  assert.equal(hasSource(tree), true); assert.match(alert(tree).props.children, /earlier status below may be out of date/);
  assert.equal(statusButton(tree).props.disabled, false);
  h.dispose();
});

test("manual status retry aborts on unmount and a late response cannot install its catalog", async () => {
  const retry = deferred(); let calls = 0, retrySignal;
  const { h, render } = await setup((_url, options) => {
    if (++calls === 1) return Promise.reject(new Error("host offline"));
    retrySignal = options.signal; return retry.promise;
  });
  render(); await settle(); let tree = render();
  statusButton(tree).props.onClick(); tree = render();
  assert.equal(retrySignal.aborted, false);
  h.dispose(); assert.equal(retrySignal.aborted, true);
  retry.resolve(response(catalog())); await settle(); tree = h.render(h.exports.default, {});
  assert.equal(hasSource(tree), false); assert.equal(alert(tree), undefined);
});

test("background status failure keeps a successful capture message and verified result visible", async () => {
  let statusCalls = 0;
  const result = { cached: true, view: { sourceId: "noaa-ncei", query: {}, rows: [], total: 0, partial: false, retrievedAt: "2026-11-09", limitation: "Test source", releaseState: "unreleased" }, receipt: { captureId: "test-capture" } };
  const { h, render } = await setup((url, options) => {
    if (options?.method === "POST") return Promise.resolve(response(result));
    if (url.includes("action=captures")) return Promise.resolve(response({ captures: [] }));
    return ++statusCalls === 1 ? Promise.resolve(response(catalog(true))) : Promise.reject(new Error("host offline"));
  });
  render(); await settle(); let tree = render();
  findNode(tree, node => node.type === "form").props.onSubmit({ preventDefault() {} });
  await settle(); tree = render();
  assert.match(alert(tree).props.children, /Source status is unavailable/);
  assert.ok(findNode(tree, node => node.props?.role === "status" && node.props.children === "Verified saved capture replayed."));
  assert.ok(findNode(tree, node => node.type === "section" && node.props["aria-label"] === "Verified capture"));
  h.dispose();
});

test("changing the selected source after capture cannot strand its independent status refresh", async () => {
  const background = deferred(); let statusCalls = 0, backgroundSignal;
  const result = { cached: true, view: { sourceId: "noaa-ncei", query: {}, rows: [], total: 0, partial: false, retrievedAt: "2026-11-09", limitation: "Test source", releaseState: "unreleased" }, receipt: { captureId: "test-capture" } };
  const { h, render } = await setup((url, options) => {
    if (options?.method === "POST") return Promise.resolve(response(result));
    if (url.includes("action=captures")) return Promise.resolve(response({ captures: [] }));
    if (++statusCalls === 1) return Promise.resolve(response(catalog(true)));
    backgroundSignal = options.signal; return background.promise;
  });
  render(); await settle(); let tree = render();
  findNode(tree, node => node.type === "form").props.onSubmit({ preventDefault() {} });
  await settle(); tree = render();
  assert.equal(statusButton(tree).props.disabled, true);
  findNode(tree, node => node.type === "button" && node.props["aria-pressed"] === true).props.onClick();
  assert.equal(backgroundSignal.aborted, false, "catalog refresh is owned independently of completed capture");
  background.resolve(response(catalog(true))); await settle(); tree = render();
  assert.equal(statusButton(tree).props.disabled, false);
  assert.equal(alert(tree), undefined);
  h.dispose();
});

test("stalled catalog status expires, releases retry, and ignores a late response", async () => {
  const stalled = deferred(), time = clock(); let calls = 0, signal;
  const { h, render } = await setup((_url, options) => {
    if (++calls === 1) { signal = options.signal; return stalled.promise; }
    return Promise.resolve(response(catalog()));
  }, time.globals);
  render(); await settle(); let tree = render();
  assert.equal(statusButton(tree).props.disabled, true);
  time.expire(); await settle(); tree = render();
  assert.equal(signal.aborted, true); assert.equal(time.timers.size, 0);
  assert.match(alert(tree).props.children, /took too long/);
  assert.equal(statusButton(tree).props.disabled, false);
  stalled.resolve(response(catalog())); await settle(); tree = render();
  assert.equal(hasSource(tree), false, "timed-out catalog cannot install late data");
  statusButton(tree).props.onClick(); await settle(); tree = render();
  assert.equal(hasSource(tree), true); assert.equal(alert(tree), undefined);
  assert.equal(time.timers.size, 0);
  h.dispose();
});

test("the same refresh deadline covers a stalled captures list and retains catalog recovery", async () => {
  const stalled = deferred(), time = clock(); let capturesSignal;
  const { h, render } = await setup((url, options) => {
    if (url.includes("action=captures")) { capturesSignal = options.signal; return stalled.promise; }
    return Promise.resolve(response(catalog(true)));
  }, time.globals);
  render(); await settle(); let tree = render();
  assert.equal(hasSource(tree), true); assert.equal(statusButton(tree).props.disabled, true);
  time.expire(); await settle(); tree = render();
  assert.equal(capturesSignal.aborted, true); assert.equal(time.timers.size, 0);
  assert.match(alert(tree).props.children, /took too long/);
  assert.equal(hasSource(tree), true); assert.equal(statusButton(tree).props.disabled, false);
  stalled.resolve(response({ captures: [{ captureId: "late-capture", sourceId: "noaa-ncei", retrievedAt: "2026-11-09", validation: "structure-valid" }] }));
  await settle(); tree = render();
  assert.doesNotMatch(JSON.stringify(tree), /late-capture/);
  h.dispose();
});

test("unmount settles stalled status work and clears its deadline even when fetch ignores abort", async () => {
  for (const stalledStep of ["catalog", "captures"]) {
    const stalled = deferred(), time = clock(); let signal;
    const { h, render } = await setup((url, options) => {
      if (stalledStep === "captures" && !url.includes("action=captures")) return Promise.resolve(response(catalog(true)));
      signal = options.signal; return stalled.promise;
    }, time.globals);
    render(); await settle(); const before = JSON.stringify(render());
    assert.equal(time.timers.size, 1);
    h.dispose(); await settle();
    assert.equal(signal.aborted, true); assert.equal(time.timers.size, 0, "aborted race cleans its timer without waiting for fetch");
    stalled.resolve(response(stalledStep === "catalog" ? catalog() : { captures: [{ captureId: "late-capture" }] }));
    await settle();
    assert.equal(JSON.stringify(h.render(h.exports.default, {})), before, "late response cannot update an unmounted owner");
  }
});

test("malformed successful catalogs cannot replace the last usable catalog or strand retry", async () => {
  const invalid = [
    {}, { ...catalog(), sources: null }, { ...catalog(), host: null },
    { ...catalog(), owner: "true" },
    { ...catalog(), sources: [{ ...catalog().sources[0], fields: null }] },
    { ...catalog(), sources: [{ ...catalog().sources[0], missing: null }] },
    { ...catalog(), host: { ...catalog().host, limitBytes: "1000" } },
  ];
  for (const value of invalid) {
    let calls = 0;
    const { h, render } = await setup(async () => response(++calls === 2 ? value : catalog()));
    try {
      render(); await settle(); let tree = render(); assert.equal(hasSource(tree), true);
      statusButton(tree).props.onClick(); await settle();
      tree = render();
      assert.equal(hasSource(tree), true);
      assert.match(alert(tree).props.children, /Source status is unavailable/);
      assert.equal(statusButton(tree).props.disabled, false);
      statusButton(tree).props.onClick(); await settle(); tree = render();
      assert.equal(alert(tree), undefined); assert.equal(hasSource(tree), true);
    } finally { h.dispose(); }
  }
});

test("an invalid initial catalog remains retryable without enabling owner capture controls", async () => {
  const { h, render } = await setup(async () => response({ ...catalog(true), sources: null }));
  try {
    render(); await settle(); const tree = render();
    assert.match(alert(tree).props.children, /Source status is unavailable/);
    assert.equal(hasSource(tree), false);
    assert.equal(findNode(tree, node => node.type === "form"), undefined);
    assert.equal(statusButton(tree).props.disabled, false);
  } finally { h.dispose(); }
});

test("malformed capture history stays out of rendering and preserves the previous history", async () => {
  const receipt = { captureId: "a".repeat(64), sourceId: "noaa-ncei", retrievedAt: "2026-11-19T12:00:00Z", byteLength: 100, entityBytes: 50, sha256: "b".repeat(64), validation: "structure-valid", partial: false, query: {}, limitation: "Fixture", entityHashes: [] };
  for (const value of [{}, { captures: null }, { captures: [null] }, { captures: [{ ...receipt, query: null }] }]) {
    let histories = 0;
    const { h, render } = await setup(async url => response(url.includes("action=captures") ? (++histories === 1 ? { captures: [receipt] } : value) : catalog(true)));
    try {
      render(); await settle(); let tree = render();
      const replay = () => findNode(tree, node => node.type === "button" && node.props.children === "Replay capture");
      assert.ok(replay()); statusButton(tree).props.onClick(); await settle(); await settle(); tree = render();
      assert.ok(replay(), "last valid history survives an invalid response");
      assert.match(alert(tree).props.children, /Source status is unavailable/);
      assert.equal(statusButton(tree).props.disabled, false);
    } finally { h.dispose(); }
  }
});


test("catalog validation accepts the server provider inventory and an empty inventory", async () => {
  for (const sources of [providerCatalog(), []]) {
    const { h, render } = await setup(async () => response({ ...catalog(), sources }));
    try {
      render(); await settle(); const tree = render();
      assert.equal(alert(tree), undefined);
      assert.equal(statusButton(tree).props.disabled, false);
      if(sources.length)assert.ok(findNode(tree, node => node.type === "strong" && node.props.children === sources[0].name));
      else assert.equal(findNode(tree, node => node.type === "form"), undefined);
    } finally { h.dispose(); }
  }
});

test("capture-history HTTP errors remain visible even when they contain a valid-looking list", async () => {
  const { h, render } = await setup(async url => url.includes("action=captures") ? { ok: false, json: async () => ({ captures: [] }) } : response(catalog(true)));
  try {
    render(); await settle(); await settle(); const tree = render();
    assert.match(alert(tree).props.children, /Source status is unavailable/);
    assert.equal(statusButton(tree).props.disabled, false);
  } finally { h.dispose(); }
});

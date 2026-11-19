import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";
import { scheduledProfiles } from "../app/api-connections-runtime/connections.mjs";

const imports = { "next/link": { default: "a" }, "next/dynamic": { default: () => "connection-map" }, "../connection-series": { VALUE_COLUMNS: {}, series: () => [] }, "./connections.css": {} };
const source = { id: "noaa-ncei", name: "NOAA NCEI", kind: "table", fields: [], configured: true, missing: [], holds: [], state: "ready", docs: "https://example.test/", limitation: "Fixture", limitBytes: 1000, releaseState: "unreleased" };
const catalog = { owner: true, sources: [source], host: { state: "ready", configured: true, paused: false, host: "Fixture", usedBytes: 0, limitBytes: 1000 } };
const response = body => ({ ok: true, json: async () => body });
const stored = { sourceId: "usdm-statistics", state: "quarantined", captureId: "a".repeat(64) };
const reused = { ...stored, state: "already-captured" };
const held = { sourceId: "usdm-statistics", state: "held", code: "PIPELINE_PAUSED_OR_BUSY" };
const complete = { state: "complete", captured: 1, outcomes: [stored] };
const button = tree => findNode(tree, node => node.type === "button" && node.props.children === "Capture configured profiles");
const message = tree => findNode(tree, node => node.props?.["aria-live"] === "polite").props.children;
async function setup(run) {
  let statusCalls = 0;
  const h = await componentHarness("app/connections/workspace.tsx", imports, { fetch: async (url, options) => {
    if (url === "/api/connections/run") { assert.equal(options.method, "POST"); return run(options); }
    if (url.includes("action=captures")) return response({ captures: [] });
    statusCalls++; return response(catalog);
  } });
  const render = () => { const tree = h.render(h.exports.default, {}); h.commit(); return tree; };
  render(); await settle(); await settle();
  return { h, render, statusCalls: () => statusCalls, run: () => button(render()).props.onClick() };
}

test("invalid profile results show a recoverable error without claiming stored captures or refreshing status", async () => {
  const bad = [null, [], {}, { state: "complete", captured: "1", outcomes: [stored] },
    { state: "complete", captured: -1, outcomes: [] }, { state: "complete", captured: 0.5, outcomes: [] },
    { ...complete, captured: NaN }, { ...complete, captured: Infinity }, { ...complete, captured: Number.MAX_SAFE_INTEGER + 1 },
    { ...complete, outcomes: null }, { ...complete, outcomes: [null] }, { ...complete, outcomes: [{}] },
    { ...complete, outcomes: [{ ...stored, sourceId: "" }] }, { ...complete, outcomes: [{ ...stored, sourceId: 7 }] },
    { ...complete, outcomes: [{ ...stored, state: "published" }] },
    { ...complete, outcomes: [{ ...stored, captureId: "not-an-id" }] },
    { ...complete, outcomes: [{ ...stored, captureId: null }] },
    { state: "partial", captured: 0, outcomes: [{ ...held, code: null }] },
    { state: "partial", captured: 0, outcomes: [{ ...held, code: "" }] },
    { state: "partial", captured: 0, outcomes: [{ ...held, sourceId: null }] },
  ];
  for (const value of bad) {
    let attempts = 0;
    const { h, render, run, statusCalls } = await setup(async () => response(++attempts === 1 ? value : complete));
    try {
      run(); await settle(); let tree = render();
      assert.match(message(tree), /invalid.*saved captures.*retry/i);
      assert.doesNotMatch(message(tree), /capture\(s\) stored/);
      assert.equal(button(tree).props.disabled, false); assert.equal(statusCalls(), 1);
      run(); await settle(); tree = render();
      assert.match(message(tree), /1 configured-profile capture\(s\) stored/);
      assert.equal(statusCalls(), 2);
    } finally { h.dispose(); }
  }
});

test("profile state, attempt limits and stored counts must agree with the outcomes", async () => {
  const bad = [{ state: "unknown", captured: 1, outcomes: [stored] },
    { state: "complete", captured: 0, outcomes: [] }, { ...complete, captured: 0 },
    { ...complete, captured: 2 }, { state: "complete", captured: 0, outcomes: [reused, held] },
    { state: "partial", captured: 1, outcomes: [stored] }, { state: "partial", captured: 1, outcomes: [held] },
    { state: "complete", captured: 3, outcomes: [stored, stored, stored] },
    { state: "schedule-disabled", captured: 1, outcomes: [] },
    { state: "schedule-disabled", captured: 0, outcomes: [reused] },
  ];
  for (const value of bad) {
    const { h, render, run, statusCalls } = await setup(async () => response(value));
    try { run(); await settle(); const tree = render(); assert.match(message(tree), /invalid/i); assert.equal(statusCalls(), 1); }
    finally { h.dispose(); }
  }
});

test("valid profile results distinguish disabled, stored, reused and held attempts", async () => {
  const cases = [
    [{ state: "schedule-disabled", captured: 0, outcomes: [] }, /Configured-profile capture is disabled\./],
    [complete, /1 configured-profile capture\(s\) stored/],
    [{ state: "complete", captured: 0, outcomes: [reused] }, /1 previously saved capture\(s\) reused/],
    [{ state: "complete", captured: 1, outcomes: [stored, reused] }, /1 configured-profile capture\(s\) stored; 1 previously saved capture\(s\) reused/],
    [{ state: "partial", captured: 1, outcomes: [stored, held] }, /1 configured-profile capture\(s\) stored; 1 profile\(s\) held/],
    [{ state: "partial", captured: 0, outcomes: [reused, held] }, /0 configured-profile capture\(s\) stored; 1 previously saved capture\(s\) reused; 1 profile\(s\) held/],
    [{ state: "partial", captured: 0, outcomes: [held, held] }, /0 configured-profile capture\(s\) stored; 2 profile\(s\) held/],
  ];
  for (const [value, expected] of cases) {
    const { h, render, run, statusCalls } = await setup(async () => response(value));
    try {
      run(); await settle(); const tree = render(); assert.match(message(tree), expected);
      if (value.state === "partial") assert.match(message(tree), /source setup and saved captures before retrying/i);
      if (value.captured > 0) assert.match(message(tree), /Review and release remain pending/);
      assert.equal(button(tree).props.disabled, false); assert.equal(statusCalls(), 2);
    } finally { h.dispose(); }
  }
});

test("non-JSON profile responses never expose parser or gateway text", async () => {
  for (const ok of [true, false]) {
    const { h, render, run } = await setup(async () => ({ ok, json: async () => { throw new SyntaxError("Unexpected token < private gateway body"); } }));
    try {
      run(); await settle(); const tree = render();
      assert.match(message(tree), ok ? /invalid.*saved captures.*retry/i : /not configured or enabled/i);
      assert.doesNotMatch(message(tree), /Unexpected token|private gateway/); assert.equal(button(tree).props.disabled, false);
    } finally { h.dispose(); }
  }
});

test("a superseded profile response cannot replace the current source message", async () => {
  let resolve, signal;
  const delayed = new Promise(done => { resolve = done; });
  const { h, render, run } = await setup(options => { signal = options.signal; return delayed; });
  try {
    run(); const tree = render();
    findNode(tree, node => node.type === "button" && node.props?.["aria-pressed"] === true).props.onClick();
    assert.equal(signal.aborted, true);
    resolve(response(complete)); await settle(); const current = render();
    assert.equal(message(current), ""); assert.equal(button(current).props.disabled, false);
  } finally { h.dispose(); }
});

test("actual scheduled-profile responses remain displayable for fresh, cached, held and disabled runs", async () => {
  const memory = new Map();
  const store = { claim: async () => "token", due: async plan => !memory.has(plan.id), reserve: async plan => plan.limitBytes + 16384,
    save: async (plan, captured) => memory.set(plan.id, captured), read: async id => memory.get(id), release: async () => {}, failure: async () => {} };
  const options = { env: { KFM_API_SCHEDULE_ENABLED: "true", KFM_API_CAPTURE_PROFILES: JSON.stringify([{ sourceId: "usdm-statistics" }]) }, at: 1704067200000,
    fetcher: async () => Response.json([{ mapDate: "2024-01-02", stateAbbreviation: "KS", statisticFormatID: 2, d0: 2 }]) };
  const cases = [
    [await scheduledProfiles(store, options), /1 configured-profile capture\(s\) stored/],
    [await scheduledProfiles(store, options), /1 previously saved capture\(s\) reused/],
    [await scheduledProfiles({ ...store, claim: async () => null }, options), /1 profile\(s\) held/],
    [await scheduledProfiles({}, {}), /Configured-profile capture is disabled/],
  ];
  for (const [value, expected] of cases) {
    const { h, render, run } = await setup(async () => response(value));
    try { run(); await settle(); assert.match(message(render()), expected); }
    finally { h.dispose(); }
  }
});

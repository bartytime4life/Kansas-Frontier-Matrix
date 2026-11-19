import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

// Actual SoilView hooks and real bounded response reads; controlled transport and timers.
// These synthetic descriptions are not USDA observations or browser acceptance.
const bounded = (await componentHarness("app/bounded-json.ts", {}, { TextDecoder })).exports;
const styles = new Proxy({}, { get: (_target, key) => String(key) });
const text = node => typeof node === "string" || typeof node === "number" ? String(node)
  : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(text).join(" ").replace(/\s+/g, " ") : "";
const original = [-95.25, 39], other = [-96, 38];
const fixture = (label = "SYNTHETIC-COMPONENT", { empty = false, partial = false } = {}) => ({
  rows: empty ? [] : [["map-unit", "MU", "Synthetic map unit", "component", label, 0, "Yes", "horizon", "A", 0, null, 0, null, 25]],
  retrievedAt: "2026-11-18T12:00:00.000Z", partial,
  sourceUrl: "https://sdmdataaccess.nrcs.usda.gov/", depthUnit: "cm", depthReference: "soil surface",
  limitation: "Synthetic alternatives, not a soil observation at this point.",
});
async function setup(initialAnchor = original) {
  const tasks = new Map(), requests = [], signals = []; let serial = 0;
  class TrackedController extends AbortController {
    constructor() {
      super(); const listeners = new Set(), add = this.signal.addEventListener.bind(this.signal), remove = this.signal.removeEventListener.bind(this.signal);
      this.signal.addEventListener = (type, fn, options) => { if (type === "abort") listeners.add(fn); add(type, fn, options); };
      this.signal.removeEventListener = (type, fn, options) => { if (type === "abort") listeners.delete(fn); remove(type, fn, options); };
      signals.push({ signal: this.signal, listeners });
    }
  }
  const h = await componentHarness("app/underground-panel.tsx", {
    "./subsurface-model": {}, "./subsurface-materials": {}, "./subsurface-slice": {},
    "./cutaway-locator": {}, "./subsurface-workers": {}, "./subsurface.module.css": { default: styles },
    "./bounded-json": bounded,
  }, {
    AbortController: TrackedController, URLSearchParams,
    setTimeout: (fn, delay) => { const id = ++serial; tasks.set(id, { fn, delay }); return id; },
    clearTimeout: id => tasks.delete(id),
    // Abort-ignoring headers expose stale-response bugs, not native fetch behavior.
    fetch: (url, options) => new Promise((resolve, reject) => requests.push({ url, options, resolve, reject })),
  }, "\nexport { SoilView };\n");
  let anchor = initialAnchor, tree;
  const draw = (next = anchor, commit = true) => { anchor = next; tree = h.render(h.exports.SoilView, { anchor }); if (commit) h.commit(); return tree; };
  const flush = async () => { await settle(); await settle(); draw(); };
  const fire = delay => { for (const [id, task] of [...tasks]) if (task.delay === delay) { tasks.delete(id); task.fn(); } };
  const reply = (request, value, status = 200) => {
    const response = value instanceof Response ? value : Response.json(value, { status }); request.response = response; request.resolve(response); return response;
  };
  const retry = () => {
    const button = findNode(tree, node => node.type === "button" && /retry soil lookup/i.test(text(node)));
    assert.ok(button && !button.props.disabled, "failed lookups offer an explicit retry"); button.props.onClick(); draw(); fire(400);
    return requests.at(-1);
  };
  const assertReleased = () => { assert.equal(tasks.size, 0); for (const entry of signals) assert.equal(entry.listeners.size, 0); };
  draw();
  return { h, draw, flush, fire, reply, retry, requests, signals, tasks, assertReleased, get tree() { return tree; } };
}
function lateBody(value) {
  let cancelled = 0;
  const response = new Response(new ReadableStream({
    start(controller) { controller.enqueue(new TextEncoder().encode(JSON.stringify(value))); },
    cancel() { cancelled++; return new Promise(() => {}); },
  }));
  return { response, cancelled: () => cancelled };
}

test("soil lookup remains debounced and keeps component proportions, zero/null values, units and source limits", async () => {
  const f = await setup();
  try {
    assert.equal(f.requests.length, 0); f.fire(400); assert.equal(f.requests.length, 1);
    assert.match(f.requests[0].url, /lon=-95\.250000&lat=39\.000000$/);
    const value = fixture(); value.rows.push(["map-unit", "MU", "Synthetic map unit", "second", "SYNTHETIC-ALTERNATIVE", 60, "Yes", "horizon-2", "B", 20, 50, 40, 35, 25]);
    f.reply(f.requests[0], value); await f.flush(); const view = text(f.tree);
    assert.match(view, /SYNTHETIC-COMPONENT/); assert.match(view, /SYNTHETIC-ALTERNATIVE/);
    assert.match(view, /0\s*% of map unit/); assert.match(view, /0\s*–\s*unknown cm/); assert.match(view, /sand 0\s*%, silt unknown\s*%, clay 25\s*%/);
    assert.match(view, /2 horizons returned/); assert.match(view, /do not identify the exact soil beneath the crosshair/);
    assert.match(view, /Live soil responses are not yet captured in the section export/); f.assertReleased();
  } finally { f.h.dispose(); }
});

test("the parent-style keyed remount cancels the old probe and the new view starts empty", async () => {
  const first = await setup(), next = await setup(other);
  try {
    first.fire(400); const old = first.requests[0]; first.h.dispose();
    assert.equal(old.options.signal.aborted, true); assert.match(text(next.tree), /Loading soil-map descriptions/);
    next.fire(400); next.reply(next.requests[0], fixture("SYNTHETIC-NEW-PROBE")); await next.flush();
    first.reply(old, fixture("SYNTHETIC-OLD-PROBE")); await settle(); await settle();
    assert.match(text(next.tree), /SYNTHETIC-NEW-PROBE/); assert.doesNotMatch(text(next.tree), /SYNTHETIC-OLD-PROBE/);
    next.assertReleased(); first.assertReleased();
  } finally { first.h.dispose(); next.h.dispose(); }
});

for (const status of [403, 503]) test(`HTTP ${status} cannot display otherwise matching soil rows`, async () => {
  const f = await setup();
  try {
    f.fire(400); const response = f.reply(f.requests[0], fixture("SYNTHETIC-DENIED"), status); await f.flush();
    assert.doesNotMatch(text(f.tree), /SYNTHETIC-DENIED|horizons returned/); assert.match(text(f.tree), /Soil source unavailable/i);
    assert.equal(response.bodyUsed, true); assert.equal(response.body.locked, false); f.assertReleased();
  } finally { f.h.dispose(); }
});

const invalid = {
  "error envelope": value => { value.error = "Soil source unavailable."; },
  "missing rows": value => { delete value.rows; },
  "non-array rows": value => { value.rows = {}; },
  "row width": value => { value.rows[0].pop(); },
  "nested cell": value => { value.rows[0][4] = { title: "not a scalar" }; },
  "too many horizons": value => { value.rows = Array(101).fill(value.rows[0]); },
  "partial flag": value => { value.partial = "false"; },
  "partial count": value => { value.partial = true; },
  "unmarked horizon cap": value => { value.rows = Array(100).fill(value.rows[0]); },
  "retrieval time": value => { value.retrievedAt = "not a timestamp"; },
  "depth unit": value => { value.depthUnit = "ft"; },
  "depth reference": value => { value.depthReference = "sea level"; },
  "source": value => { value.sourceUrl = "https://example.invalid/other-provider"; },
};
for (const [reason, mutate] of Object.entries(invalid)) test(`malformed soil ${reason} becomes unavailable without a render exception or empty-soil claim`, async () => {
  const f = await setup();
  try {
    f.fire(400); const value = fixture("SYNTHETIC-MALFORMED"); mutate(value); f.reply(f.requests[0], value); await f.flush();
    assert.match(text(f.tree), /Soil source unavailable/i); assert.doesNotMatch(text(f.tree), /SYNTHETIC-MALFORMED|None in the available|No soil horizons returned/); f.assertReleased();
  } finally { f.h.dispose(); }
});

for (const failure of ["invalid-json", "declared-size", "stream-size"]) test(`soil ${failure} is bounded and recoverable`, async () => {
  const f = await setup();
  try {
    f.fire(400); const response = failure === "invalid-json" ? new Response("{") : failure === "declared-size"
      ? new Response("{}", { headers: { "content-length": String(512 * 1024 + 1) } }) : new Response("x".repeat(512 * 1024 + 1));
    f.reply(f.requests[0], response); await f.flush(); assert.match(text(f.tree), /Soil source unavailable/i);
    assert.equal(response.body.locked, false); f.assertReleased();
    f.retry(); f.reply(f.requests[1], fixture("SYNTHETIC-RECOVERED")); await f.flush(); assert.match(text(f.tree), /SYNTHETIC-RECOVERED/); f.assertReleased();
  } finally { f.h.dispose(); }
});

for (const phase of ["headers", "body"]) {
  test(`soil ${phase} deadline releases resources, permits retry, and discards late data`, async () => {
    const f = await setup(); let response, cancelled = 0;
    try {
      f.fire(400); const old = f.requests[0];
      if (phase === "body") { response = new Response(new ReadableStream({ cancel() { cancelled++; return new Promise(() => {}); } })); f.reply(old, response); await f.flush(); assert.equal(response.body.locked, true); }
      f.fire(20000); await f.flush(); assert.equal(old.options.signal.aborted, true); assert.match(text(f.tree), /Soil source unavailable|timed out/i); f.assertReleased();
      f.retry(); f.reply(f.requests[1], fixture("SYNTHETIC-RETRY")); await f.flush(); assert.match(text(f.tree), /SYNTHETIC-RETRY/); f.assertReleased();
      if (phase === "headers") { const late = lateBody(fixture("SYNTHETIC-LATE")); f.reply(old, late.response); await f.flush(); assert.equal(late.cancelled(), 1); assert.equal(late.response.body.locked, false); }
      else { assert.equal(cancelled, 1); assert.equal(response.body.locked, false); }
      assert.match(text(f.tree), /SYNTHETIC-RETRY/); assert.doesNotMatch(text(f.tree), /SYNTHETIC-LATE/);
    } finally { f.h.dispose(); }
  });
  for (const exit of ["move", "unmount"]) test(`soil ${phase} ${exit} aborts, releases resources and ignores late results`, async () => {
    const f = await setup(); let response, cancelled = 0;
    try {
      f.fire(400); const old = f.requests[0];
      if (phase === "body") { response = new Response(new ReadableStream({ cancel() { cancelled++; return new Promise(() => {}); } })); f.reply(old, response); await f.flush(); }
      if (exit === "move") f.draw(other); else f.h.dispose(); await settle(); await settle();
      assert.equal(old.options.signal.aborted, true);
      if (exit === "move") { f.fire(400); f.reply(f.requests[1], fixture("SYNTHETIC-NEW")); await f.flush(); assert.match(text(f.tree), /SYNTHETIC-NEW/); }
      if (phase === "headers") { const late = lateBody(fixture("SYNTHETIC-OLD")); f.reply(old, late.response); await settle(); await settle(); assert.equal(late.cancelled(), 1); assert.equal(late.response.body.locked, false); }
      else { assert.equal(cancelled, 1); assert.equal(response.body.locked, false); }
      if (exit === "move") assert.doesNotMatch(text(f.draw()), /SYNTHETIC-OLD/); f.assertReleased();
    } finally { f.h.dispose(); }
  });
}

test("equal query coordinates do not restart the lookup just because the anchor array was replaced", async () => {
  const f = await setup();
  try {
    f.fire(400); f.reply(f.requests[0], fixture("SYNTHETIC-CURRENT")); await f.flush(); f.draw([...original]); f.fire(400);
    assert.equal(f.requests.length, 1); assert.match(text(f.tree), /SYNTHETIC-CURRENT/); f.assertReleased();
  } finally { f.h.dispose(); }
});

for (const partial of [false, true]) test(`valid ${partial ? "partial" : "empty"} soil results retain their scope and limitations`, async () => {
  const f = await setup();
  try {
    f.fire(400); const value = fixture("SYNTHETIC-PARTIAL", { empty: !partial, partial });
    if (partial) value.rows = Array(100).fill(value.rows[0]); f.reply(f.requests[0], value); await f.flush();
    assert.match(text(f.tree), partial ? /Partial: 100-horizon limit reached/ : /None in the available soil-map data|No soil horizons returned/); f.assertReleased();
  } finally { f.h.dispose(); }
});

import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

// Actual parent navigation/hooks, source validation and bounded reads. Transports,
// clocks and the record worker are controlled; these are not browser acceptance.
const materials = (await componentHarness("app/subsurface-materials.ts", {})).exports;
const model = (await componentHarness("app/subsurface-model.ts", { "./subsurface-materials": materials })).exports;
const slices = (await componentHarness("app/subsurface-slice.ts", { "./subsurface-model": model })).exports;
const locator = (await componentHarness("app/cutaway-locator.ts", {})).exports;
const bounded = (await componentHarness("app/bounded-json.ts", {}, { TextDecoder })).exports;
const styles = new Proxy({}, { get: (_target, key) => String(key) });
const text = node => typeof node === "string" || typeof node === "number" ? String(node)
  : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(text).join(" ").replace(/\s+/g, " ") : "";
const fixture = () => ({ version: 1, surveys: [{
  id: "synthetic-survey", title: "SYNTHETIC electrical survey", method: "electrical", status: "ready",
  sourceUrl: "https://example.invalid/published-survey", sourceTime: "2022", retrievedAt: "2026-11-18T12:00:00Z",
  limitation: "Synthetic test context, not geological evidence.", profiles: [{
    id: "synthetic-profile", title: "SYNTHETIC conductivity log", coordinates: [-95.25, 39],
    depthUnit: "ft", depthReference: "land-surface", valueUnit: "mS/m", samples: [{ depth: 0, value: 0 }, { depth: 1, value: 2 }],
  }],
}] });
function surveyNodes(tree, result = []) {
  if (tree && typeof tree === "object") {
    if (typeof tree.type === "function" && tree.type.name === "SurveyView") result.push(tree.props.survey);
    for (const child of [tree.props?.children].flat(Infinity)) surveyNodes(child, result);
  }
  return result;
}
async function setup() {
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
    "./subsurface-model": model, "./subsurface-materials": materials, "./subsurface-slice": slices,
    "./cutaway-locator": locator, "./subsurface-workers": { startSubsurfaceWorker: () => ({ postMessage() {}, terminate() {} }) },
    "./subsurface.module.css": { default: styles }, "./bounded-json": bounded,
  }, {
    AbortController: TrackedController, queueMicrotask,
    matchMedia: () => ({ matches: true, addEventListener() {}, removeEventListener() {} }),
    document: { hidden: false, addEventListener() {}, removeEventListener() {} },
    setTimeout: (fn, delay) => { const id = ++serial; tasks.set(id, { fn, delay }); return id; },
    clearTimeout: id => tasks.delete(id),
    // An abort-ignoring transport tests cleanup and obsolete completion handling.
    fetch: (url, options) => new Promise((resolve, reject) => requests.push({ url, options, resolve, reject })),
  });
  const props = { map: null, initialContext: null, year: 2026, redacted: false,
    onFlatMap() {}, onTerrain() {}, readElevation() { return null; }, isDrawing() { return false; },
    onDraw() {}, readTransect() { return []; }, onContext() {}, onInspect() {}, onClose() {}, onSave() {}, onReport() {},
  };
  let tree;
  const draw = () => { tree = h.render(h.exports.default, props); h.commit(); return tree; };
  const flush = async () => { await settle(); draw(); await settle(); draw(); };
  const fire = delay => { for (const [id, task] of [...tasks]) if (task.delay === delay) { tasks.delete(id); task.fn(); } };
  const tool = value => { findNode(tree, node => node.props?.["aria-label"] === "Underground tool").props.onChange({ target: { value } }); draw(); };
  const reply = (request, value, status = 200) => {
    const response = value instanceof Response ? value : Response.json(value, { status }); request.resolve(response); return response;
  };
  const retry = () => {
    const button = findNode(tree, node => node.type === "button" && /retry published surveys/i.test(text(node)));
    assert.ok(button && !button.props.disabled, "failed catalogue loads offer a retry"); button.props.onClick(); draw();
    assert.match(text(tree), /Loading published surveys/); assert.doesNotMatch(text(tree), /unavailable|timed out/i); return requests.at(-1);
  };
  const assertReleased = () => {
    assert.equal([...tasks.values()].filter(task => task.delay === 15000).length, 0, "survey deadline is released");
    for (const entry of signals) assert.equal(entry.listeners.size, 0, "abort listeners are released");
  };
  draw();
  return { h, draw, flush, fire, tool, reply, retry, requests, signals, tasks, assertReleased, get tree() { return tree; } };
}
function lateBody(value) {
  let cancelled = 0;
  const response = new Response(new ReadableStream({
    start(controller) { controller.enqueue(new TextEncoder().encode(JSON.stringify(value))); },
    cancel() { cancelled++; return new Promise(() => {}); },
  }));
  return { response, cancelled: () => cancelled };
}

test("survey loading is on demand with a visible pending state; the current catalogue and its holds remain cached across tool changes", async () => {
  const f = await setup();
  try {
    assert.equal(f.requests.length, 0); f.tool("surveys"); await f.flush();
    assert.equal(f.requests[0].url, "/data/subsurface/geophysics.json");
    assert.match(text(f.tree), /Loading published surveys/);
    assert.equal(findNode(f.tree, node => node.props?.["aria-label"] === "Published geophysical surveys").props["aria-busy"], true);
    const asset = JSON.parse(await readFile("public/data/subsurface/geophysics.json", "utf8"));
    f.reply(f.requests[0], asset); await f.flush();
    assert.equal(surveyNodes(f.tree).length, 7); assert.equal(surveyNodes(f.tree).flatMap(survey => survey.profiles).length, 21);
    assert.equal(surveyNodes(f.tree).flatMap(survey => survey.profiles).reduce((count, profile) => count + profile.samples.length, 0), 25479);
    assert.equal(surveyNodes(f.tree).find(survey => survey.id === "kgs-dpec-dg03").status, "held");
    assert.equal(findNode(f.tree, node => node.props?.["aria-label"] === "Published geophysical surveys").props["aria-busy"], false);
    assert.doesNotMatch(text(f.tree), /Loading published surveys|Published profiles are unavailable/); f.assertReleased();
    f.tool("section"); f.tool("surveys"); await f.flush(); assert.equal(f.requests.length, 1); assert.equal(surveyNodes(f.tree).length, 7);
  } finally { f.h.dispose(); }
});

test("a successful tool-return retry clears the previous unavailable message", async () => {
  const f = await setup();
  try {
    f.tool("surveys"); f.requests[0].reject(new Error("offline")); await f.flush(); assert.match(text(f.tree), /unavailable/i);
    f.tool("section"); f.tool("surveys"); f.reply(f.requests[1], fixture()); await f.flush();
    assert.equal(surveyNodes(f.tree).length, 1); assert.doesNotMatch(text(f.tree), /unavailable|timed out/i); f.assertReleased();
  } finally { f.h.dispose(); }
});

test("an empty catalogue is visible, cached, and does not imply that no surveys exist", async () => {
  const f = await setup();
  try {
    f.tool("surveys"); f.reply(f.requests[0], { version: 1, surveys: [] }); await f.flush();
    assert.match(text(f.tree), /No published survey entries were returned/); assert.match(text(f.tree), /does not establish that no surveys exist/i);
    assert.equal(surveyNodes(f.tree).length, 0); f.tool("section"); f.tool("surveys"); await f.flush(); assert.equal(f.requests.length, 1); f.assertReleased();
  } finally { f.h.dispose(); }
});

for (const status of [403, 503]) test(`HTTP ${status} with plausible profiles stays unavailable and supports an explicit retry`, async () => {
  const f = await setup();
  try {
    f.tool("surveys"); const response = f.reply(f.requests[0], fixture(), status); await f.flush();
    assert.equal(surveyNodes(f.tree).length, 0); assert.match(text(f.tree), /unavailable/i); assert.equal(response.bodyUsed, true);
    f.retry(); f.reply(f.requests[1], fixture()); await f.flush(); assert.equal(surveyNodes(f.tree).length, 1); assert.doesNotMatch(text(f.tree), /unavailable|timed out/i); f.assertReleased();
  } finally { f.h.dispose(); }
});

const malformed = {
  "error envelope": value => { value.error = "failed"; },
  "unsupported version": value => { value.version = 2; },
  "missing surveys": value => { delete value.surveys; },
  "invalid profile mixed with a valid survey": value => { const bad = structuredClone(value.surveys[0]); bad.id = "bad-survey"; bad.profiles[0].samples[1].depth = -1; value.surveys.push(bad); },
  "duplicate survey identity": value => { value.surveys.push(structuredClone(value.surveys[0])); },
  "duplicate profile identity": value => { value.surveys[0].profiles.push(structuredClone(value.surveys[0].profiles[0])); },
  "excess survey count": value => { value.surveys = Array.from({ length: 101 }, (_, index) => ({ ...value.surveys[0], id: `survey-${index}` })); },
};
for (const [reason, mutate] of Object.entries(malformed)) test(`malformed survey catalogue (${reason}) cannot silently appear complete`, async () => {
  const f = await setup();
  try {
    f.tool("surveys"); const value = fixture(); mutate(value); f.reply(f.requests[0], value); await f.flush();
    assert.equal(surveyNodes(f.tree).length, 0); assert.match(text(f.tree), /unavailable/i); assert.doesNotMatch(text(f.tree), /No published survey entries were returned/); f.assertReleased();
  } finally { f.h.dispose(); }
});

for (const failure of ["invalid-json", "declared-size", "stream-size"]) test(`survey ${failure} releases the body and supports recovery`, async () => {
  const f = await setup();
  try {
    f.tool("surveys"); const response = failure === "invalid-json" ? new Response("{") : failure === "declared-size"
      ? new Response("{}", { headers: { "content-length": String(2 * 1024 * 1024 + 1) } }) : new Response("x".repeat(2 * 1024 * 1024 + 1));
    f.reply(f.requests[0], response); await f.flush(); assert.match(text(f.tree), /unavailable/i); assert.equal(response.body.locked, false); f.assertReleased();
    f.retry(); f.reply(f.requests[1], fixture()); await f.flush(); assert.equal(surveyNodes(f.tree).length, 1); f.assertReleased();
  } finally { f.h.dispose(); }
});

for (const phase of ["headers", "body"]) {
  test(`a stalled survey ${phase} reaches a deadline and a late result cannot replace the retried catalogue`, async () => {
    const f = await setup(); let response, cancelled = 0;
    try {
      f.tool("surveys"); const old = f.requests[0];
      if (phase === "body") { response = new Response(new ReadableStream({ cancel() { cancelled++; return new Promise(() => {}); } })); f.reply(old, response); await f.flush(); assert.equal(response.body.locked, true); }
      f.fire(15000); await f.flush(); assert.equal(old.options.signal.aborted, true); assert.match(text(f.tree), /unavailable|timed out/i); f.assertReleased();
      f.retry(); const value = fixture(); value.surveys[0].title = "SYNTHETIC retry"; f.reply(f.requests[1], value); await f.flush();
      if (phase === "headers") { const late = lateBody(fixture()); f.reply(old, late.response); await f.flush(); assert.equal(late.cancelled(), 1); assert.equal(late.response.body.locked, false); }
      else { assert.equal(cancelled, 1); assert.equal(response.body.locked, false); }
      assert.equal(surveyNodes(f.tree)[0].title, "SYNTHETIC retry"); f.assertReleased();
    } finally { f.h.dispose(); }
  });
  for (const exit of ["tool-change", "unmount"]) test(`survey ${phase} ${exit} aborts, releases the body, and ignores an obsolete completion`, async () => {
    const f = await setup(); let response, cancelled = 0;
    try {
      f.tool("surveys"); const old = f.requests[0];
      if (phase === "body") { response = new Response(new ReadableStream({ cancel() { cancelled++; return new Promise(() => {}); } })); f.reply(old, response); await f.flush(); }
      if (exit === "tool-change") f.tool("section"); else f.h.dispose(); await settle(); await settle();
      assert.equal(old.options.signal.aborted, true); f.assertReleased();
      if (exit === "tool-change") { f.tool("surveys"); const value = fixture(); value.surveys[0].title = "SYNTHETIC current"; f.reply(f.requests[1], value); await f.flush(); }
      if (phase === "headers") { const late = lateBody(fixture()); f.reply(old, late.response); await settle(); await settle(); assert.equal(late.cancelled(), 1); assert.equal(late.response.body.locked, false); }
      else { assert.equal(cancelled, 1); assert.equal(response.body.locked, false); }
      if (exit === "tool-change") { f.draw(); assert.equal(surveyNodes(f.tree)[0].title, "SYNTHETIC current"); } f.assertReleased();
    } finally { f.h.dispose(); }
  });
}

test("survey method filtering reports a catalogue-specific absence and keeps export limits visible", async () => {
  const f = await setup();
  try {
    f.tool("surveys"); f.reply(f.requests[0], fixture()); await f.flush();
    const picker = findNode(f.tree, node => node.type === "select" && node.props.value === "all");
    picker.props.onChange({ target: { value: "seismic" } }); f.draw();
    assert.equal(surveyNodes(f.tree).length, 0); assert.match(text(f.tree), /No published survey entries in this catalogue match this method/);
    assert.match(text(f.tree), /survey profiles and live soil results are not included/); assert.equal(f.requests.length, 1); f.assertReleased();
  } finally { f.h.dispose(); }
});

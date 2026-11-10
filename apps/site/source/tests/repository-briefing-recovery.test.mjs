import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { componentHarness, findNode, settle as settleHooks } from "./component-harness.mjs";

// Execute the actual page effect and connection markup with its real parser and
// bounded reader. This isolates the read-only briefing from unrelated WebGL setup.
const source = await readFile("app/page.tsx", "utf8");
const effectStart = source.indexOf('  useEffect(() => {\n    if (!repositoryOpen) return;\n    const controller = new AbortController();');
const effectEnd = source.indexOf('  }, [repositoryOpen, repositoryRefreshKey]);', effectStart);
const markupStart = source.indexOf('<div className="repository-connection"');
const markupEnd = source.indexOf("\n          </section>", markupStart);
assert.ok(effectStart >= 0 && effectEnd > effectStart && markupStart >= 0 && markupEnd > markupStart, "the real repository briefing effect and markup must remain under test");
const effect = source.slice(effectStart, effectEnd + '  }, [repositoryOpen, repositoryRefreshKey]);'.length);
const markup = source.slice(markupStart, markupEnd);
const bounded = (await componentHarness("app/bounded-json.ts", {}, { TextDecoder, Uint8Array })).exports;
const settle = async () => { await settleHooks(); await settleHooks(); };
const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };
const textOf = node => typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g, " ") : "";
const button = (tree, text) => findNode(tree, node => node.type === "button" && node.props.children === text);
const stateOf = tree => tree.props["data-state"];
function clock() {
  const timers = new Map(); let serial = 0, now = Date.parse("2026-11-09T12:00:00Z");
  class FixtureDate extends Date { static now() { return now; } }
  return { timers, get now() { return now; }, globals: {
    Date: FixtureDate,
    setTimeout: (fn, delay) => { const id = ++serial; timers.set(id, { fn, delay }); return id; },
    clearTimeout: id => timers.delete(id),
  }, expire(delay) {
    const entry = [...timers].find(([, timer]) => timer.delay === delay); assert.ok(entry, `expected a ${delay}ms timer`);
    const [id, timer] = entry; timers.delete(id); now += delay; timer.fn();
  } };
}
const observation = (now, commit = "a") => ({ state:"ready", repository:"bartytime4life/Kansas-Frontier-Matrix", ref:"main", mode:"READ_ONLY_PUBLIC_METADATA", synchronization:"SITE_SOURCE_SEPARATE", commit:commit.repeat(40), observedAt:new Date(now).toISOString(), message:"Synthetic component fixture only" });
async function setup(dispatch) {
  const time = clock(), requests = [];
  const h = await componentHarness("app/repository-status.ts", {}, {
    ...time.globals, readBoundedJson:bounded.readBoundedJson, REPOSITORY_SNAPSHOT:{ commit:"c".repeat(40), shortCommit:"ccccccc" },
    fetch:(url, options) => { requests.push({ url, options }); return dispatch(url, options, time); },
  }, `\nimport { useEffect, useState } from "react";
export default function BriefingReadFixture({ open = true }) {
  const repositoryOpen = open;
  const [repositoryConnection, setRepositoryConnection] = useState({ state: "idle" });
  const [repositoryRefreshKey, setRepositoryRefreshKey] = useState(0);
  ${effect}
  return (${markup});
}`);
  let open = true;
  const render = () => { const tree = h.render(h.exports.default, { open }); h.commit(); return tree; };
  render(); await settle();
  return { h, render, time, requests, close:() => { open = false; return render(); }, reopen:() => { open = true; return render(); } };
}

test("stalled response headers reach a finite deadline, recover through retry and discard a late adapter", async () => {
  const late = deferred(); let calls = 0, lateCanceled = false;
  const f = await setup((_url, _options, time) => ++calls === 1 ? late.promise : Promise.resolve(Response.json(observation(time.now, "b"))));
  let tree = f.render(); assert.equal(stateOf(tree), "loading"); assert.equal(Boolean(button(tree, "Restart check").props.disabled), false);
  f.time.expire(15_000); await settle(); tree = f.render();
  assert.equal(stateOf(tree), "error"); assert.match(textOf(tree), /check timed out.*Retry the check/); assert.match(textOf(tree), /pinned snapshot remains available; no currentness claim is inferred/); assert.equal(f.requests[0].options.signal.aborted, true); assert.equal(f.time.timers.size, 0);
  button(tree, "Retry check").props.onClick(); f.render(); await settle(); tree = f.render(); assert.equal(stateOf(tree), "ready"); assert.match(textOf(tree), /main@bbbbbbb/);
  late.resolve(new Response(new ReadableStream({ cancel() { lateCanceled = true; } })));
  await settle(); tree = f.render(); assert.equal(lateCanceled, true); assert.equal(stateOf(tree), "ready"); assert.match(textOf(tree), /main@bbbbbbb/); f.h.dispose(); assert.equal(f.time.timers.size, 0);
});

test("the deadline covers a stalled body and cancels/releases its reader before retry", async () => {
  let canceled = false, calls = 0;
  const stalled = new Response(new ReadableStream({ start(controller) { controller.enqueue(new TextEncoder().encode('{"state":"ready",')); }, cancel() { canceled = true; } }));
  const f = await setup((_url, _options, time) => Promise.resolve(++calls === 1 ? stalled : Response.json(observation(time.now))));
  assert.equal(stalled.body.locked, true); f.time.expire(15_000); await settle(); let tree = f.render();
  assert.equal(stateOf(tree), "error"); assert.equal(canceled, true); assert.equal(stalled.body.locked, false); assert.equal(f.time.timers.size, 0);
  button(tree, "Retry check").props.onClick(); f.render(); await settle(); tree = f.render(); assert.equal(stateOf(tree), "ready"); assert.ok(button(tree, "Refresh")); f.h.dispose();
});

test("restart aborts/replaces a pending check and its late response cannot settle the replacement", async () => {
  const old = deferred(), fresh = deferred(); let calls = 0;
  const f = await setup(() => ++calls === 1 ? old.promise : fresh.promise); let tree = f.render();
  button(tree, "Restart check").props.onClick(); tree = f.render(); await settle();
  assert.equal(f.requests[0].options.signal.aborted, true); assert.equal(f.time.timers.size, 1); assert.equal(stateOf(tree), "loading");
  old.resolve(Response.json(observation(f.time.now, "a"))); await settle(); tree = f.render(); assert.equal(stateOf(tree), "loading"); assert.doesNotMatch(textOf(tree), /main@aaaaaaa/);
  fresh.resolve(Response.json(observation(f.time.now, "b"))); await settle(); tree = f.render(); assert.equal(stateOf(tree), "ready"); assert.match(textOf(tree), /main@bbbbbbb/); f.h.dispose(); assert.equal(f.time.timers.size, 0);
});

test("closing or unmounting promptly clears pending deadlines and suppresses late headers or bodies", async () => {
  for (const stage of ["headers", "body"]) for (const action of ["close", "unmount"]) {
    const late = deferred(); let canceled = false;
    const stalled = new Response(new ReadableStream({ cancel() { canceled = true; } }));
    const f = await setup(() => stage === "headers" ? late.promise : Promise.resolve(stalled));
    const before = textOf(f.render());
    if (action === "close") f.close(); else f.h.dispose();
    await settle(); assert.equal(f.requests[0].options.signal.aborted, true); assert.equal(f.time.timers.size, 0);
    if (stage === "headers") late.resolve(stalled);
    await settle(); assert.equal(canceled, true); assert.equal(stalled.body.locked, false); assert.equal(textOf(f.render()), before); f.h.dispose();
  }
});

test("HTTP failure, malformed or oversized JSON and invalid repository identity expose recovery without currentness", async () => {
  for (const kind of ["http", "json", "oversized", "identity"]) {
    let canceled = false;
    const f = await setup((_url, _options, time) => Promise.resolve(kind === "http" ? new Response(new ReadableStream({ cancel() { canceled = true; } }), { status:503 }) : kind === "json" ? new Response("not json") : kind === "oversized" ? new Response(new ReadableStream({ cancel() { canceled = true; } }), { headers:{ "Content-Length":"8193" } }) : Response.json({ ...observation(time.now), repository:"another/repo" })));
    await settle(); const tree = f.render(); assert.equal(stateOf(tree), "error"); assert.match(textOf(tree), /Retry the check.*pinned snapshot remains available/); assert.ok(button(tree, "Retry check")); assert.doesNotMatch(textOf(tree), /main@aaaaaaa|GitHub main matches/); assert.equal(f.time.timers.size, 0);
    if (kind === "http" || kind === "oversized") assert.equal(canceled, true); f.h.dispose();
  }
});

test("successful checks retain observation-based expiry and cleanup the expiry timer on close", async () => {
  const f = await setup((_url, _options, time) => Promise.resolve(Response.json(observation(time.now - 59_000)))); await settle(); let tree = f.render();
  assert.equal(stateOf(tree), "ready"); assert.deepEqual([...f.time.timers.values()].map(timer => timer.delay), [1_000]);
  f.time.expire(1_000); tree = f.render(); assert.equal(stateOf(tree), "stale"); assert.match(textOf(tree), /refresh needed/);
  button(tree, "Refresh").props.onClick(); f.render(); await settle(); assert.equal(f.time.timers.size, 1); f.close(); await settle(); assert.equal(f.time.timers.size, 0); f.h.dispose();
});

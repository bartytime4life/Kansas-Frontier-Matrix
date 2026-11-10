import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle as settleHooks } from "./component-harness.mjs";

// Actual inspector hooks/handlers and the real bounded JSON reader. Deferred
// transports deliberately ignore abort; these fixtures are not provider or browser proof.
const bounded = (await componentHarness("app/bounded-json.ts", {}, { TextDecoder, Uint8Array })).exports;
const bridge = (await componentHarness("app/kansas-bridge-records.ts", {})).exports;
const blm = (await componentHarness("app/blm-plss-records.ts", {})).exports;
const settle = async () => { await settleHooks(); await settleHooks(); };
const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };
const textOf = node => typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g, " ") : "";
const inspectButton = tree => findNode(tree, node => node.type === "button" && ["Inspect map center", "Checking…"].includes(node.props.children));
const cancelButton = tree => findNode(tree, node => node.type === "button" && node.props.children === "Cancel");
const profiles = [
  { name: "KDOT", file: "bridge-record-inspector.tsx", component: "BridgeRecordInspector", module: "./kansas-bridge-records", model: bridge, layer: "kdot-bridges-local", path: "/api/bridge-records", cap: 512 * 1024 },
  { name: "BLM", file: "blm-plss-inspector.tsx", component: "BlmPlssInspector", module: "./blm-plss-records", model: blm, layer: "blm-plss-sections", path: "/api/blm-plss-records", cap: 64 * 1024 },
];
function payload(profile, request, label = "SYNTHETIC-VALID", { empty = false, partial = false } = {}) {
  const params = new URL(request.url, "http://fixture.invalid").searchParams;
  const query = { layer: params.get("layer"), longitude: Number(params.get("longitude")), latitude: Number(params.get("latitude")), ...(profile.name === "KDOT" ? { radius: Number(params.get("radius")) } : {}) };
  const count = empty ? 0 : partial ? 2 : 1;
  const features = empty ? [] : profile.name === "KDOT"
    ? [{ attributes: { OBJECTID: 1, BRKEY: label, FIPS_STATE: "KANSAS" }, geometry: { x: query.longitude, y: query.latitude } }]
    : [{ attributes: { OBJECTID: 1, PLSSID: "KS060270S0010E0", FRSTDIVID: "KS060270S0010E0SN20", FRSTDIVTXT: "Section", FRSTDIVLAB: label } }];
  const raw = { features, geometryType: profile.name === "KDOT" ? "esriGeometryPoint" : "esriGeometryPolygon", spatialReference: { wkid: 4326 } };
  return profile.name === "KDOT" ? bridge.assembleBridgePages(empty ? [] : [raw], query, count) : blm.parseBlmPlssRecords(raw, query, count);
}
function lateResponse(value) {
  let cancelled = 0;
  const response = new Response(new ReadableStream({
    start(controller) { controller.enqueue(new TextEncoder().encode(JSON.stringify(value))); },
    cancel() { cancelled++; return new Promise(() => {}); },
  }));
  return { response, cancelled: () => cancelled };
}
async function setup(profile, dispatch) {
  const timers = new Map(), requests = [], signals = [], listeners = new Map(); let timerId = 0;
  class TrackedAbortController extends AbortController {
    constructor() {
      super(); const handlers = new Set(), add = this.signal.addEventListener.bind(this.signal), remove = this.signal.removeEventListener.bind(this.signal);
      this.signal.addEventListener = (type, fn, options) => { if (type === "abort") handlers.add(fn); add(type, fn, options); };
      this.signal.removeEventListener = (type, fn, options) => { if (type === "abort") handlers.delete(fn); remove(type, fn, options); };
      signals.push({ signal: this.signal, handlers });
    }
  }
  const center = { lng: -98, lat: 38 };
  const map = { getCenter: () => ({ ...center }), on(event, fn) { if (!listeners.has(event)) listeners.set(event, new Set()); listeners.get(event).add(fn); }, off(event, fn) { listeners.get(event)?.delete(fn); } };
  const h = await componentHarness(`app/${profile.file}`, { "./bounded-json": bounded, [profile.module]: profile.model }, {
    URLSearchParams, AbortController: TrackedAbortController,
    setTimeout: (fn, delay) => { const id = ++timerId; timers.set(id, { fn, delay }); return id; }, clearTimeout: id => timers.delete(id),
    fetch: (url, options) => { const request = { url, options }; requests.push(request); return dispatch(request, requests.length); },
  });
  let props = { layer: profile.layer, mapRef: { current: map }, enabled: true, reducedMotion: true };
  const render = next => { props = { ...props, ...next }; const tree = h.render(h.exports[profile.component], props); h.commit(); return tree; };
  render();
  return { h, render, requests, timers, listeners, signals,
    start() { const button = inspectButton(render()); assert.equal(button.props.disabled, false); button.props.onClick(); render(); },
    move(lng, lat) { center.lng = lng; center.lat = lat; for (const fn of listeners.get("movestart") ?? []) fn(); },
    expire() { const entry = [...timers].find(([, value]) => value.delay === 15_000); assert.ok(entry); timers.delete(entry[0]); entry[1].fn(); },
    assertReleased() { assert.equal(timers.size, 0); for (const entry of signals) assert.equal(entry.handlers.size, 0); },
  };
}

for (const profile of profiles) {
  test(`${profile.name}: an abort-ignoring header read reaches the 15s deadline, disposes late bytes, and retries`, async () => {
    const old = deferred();
    const f = await setup(profile, (request, call) => call === 1 ? old.promise : Promise.resolve(Response.json(payload(profile, request))));
    f.start(); assert.equal(inspectButton(f.render()).props.disabled, true);
    f.expire(); await settle(); let tree = f.render();
    assert.match(textOf(tree), /unavailable or timed out/i); assert.equal(inspectButton(tree).props.disabled, false);
    assert.equal(f.requests[0].options.signal.aborted, true); f.assertReleased();
    f.start(); await settle(); tree = f.render(); assert.match(textOf(tree), /SYNTHETIC-VALID/); f.assertReleased();
    const late = lateResponse(payload(profile, f.requests[0], "SYNTHETIC-OLD")); old.resolve(late.response); await settle();
    assert.equal(late.cancelled(), 1); assert.equal(late.response.body.locked, false); assert.doesNotMatch(textOf(f.render()), /SYNTHETIC-OLD/);
    const url = new URL(f.requests[1].url, "http://fixture.invalid"); assert.equal(url.pathname, profile.path);
    assert.deepEqual([...url.searchParams.keys()].sort(), ["layer", "longitude", "latitude", ...(profile.name === "KDOT" ? ["radius"] : [])].sort());
    assert.equal(url.searchParams.get("layer"), profile.layer); assert.equal(f.requests[1].options.cache, "no-store"); f.h.dispose();
  });

  test(`${profile.name}: stalled body cancellation is nonblocking, releases the reader and permits valid recovery`, async () => {
    let cancelled = 0;
    const response = new Response(new ReadableStream({ start(controller) { controller.enqueue(new TextEncoder().encode('{"records":')); }, cancel() { cancelled++; return new Promise(() => {}); } }));
    const f = await setup(profile, (request, call) => Promise.resolve(call === 1 ? response : Response.json(payload(profile, request))));
    f.start(); await settle(); assert.equal(response.body.locked, true);
    f.expire(); await settle(); assert.equal(cancelled, 1); assert.equal(response.body.locked, false); f.assertReleased();
    assert.match(textOf(f.render()), /unavailable or timed out/i); assert.equal(inspectButton(f.render()).props.disabled, false);
    f.start(); await settle(); assert.match(textOf(f.render()), /SYNTHETIC-VALID/); f.assertReleased(); f.h.dispose();
  });

  test(`${profile.name}: Cancel, map movement, disable and unmount clear pending resources in headers and body phases`, async () => {
    for (const phase of ["headers", "body"]) for (const exit of ["cancel", "move", "disable", "unmount"]) {
      const old = deferred(); let cancelled = 0;
      const response = new Response(new ReadableStream({ cancel() { cancelled++; return new Promise(() => {}); } }));
      const f = await setup(profile, (request, call) => call === 1 ? phase === "headers" ? old.promise : Promise.resolve(response) : Promise.resolve(Response.json(payload(profile, request, "SYNTHETIC-REPLACEMENT"))));
      f.start(); await settle();
      if (exit === "cancel") cancelButton(f.render()).props.onClick();
      else if (exit === "move") f.move(-97, 39);
      else if (exit === "disable") f.render({ enabled: false });
      else f.h.dispose();
      assert.equal(f.requests[0].options.signal.aborted, true, `${phase}/${exit}`); assert.equal(f.timers.size, 0, `${phase}/${exit}`);
      await settle(); f.assertReleased();
      if (exit !== "unmount") {
        let tree = f.render(); if (exit === "cancel") assert.match(textOf(tree), /cancelled/i); if (exit === "move") assert.match(textOf(tree), /Map moved/);
        tree = f.render({ enabled: true }); assert.equal(inspectButton(tree).props.disabled, false); f.start(); await settle();
        assert.match(textOf(f.render()), /SYNTHETIC-REPLACEMENT/);
      }
      if (phase === "headers") old.resolve(response); await settle();
      assert.equal(cancelled, 1, `${phase}/${exit}`); assert.equal(response.body.locked, false); f.assertReleased();
      if (exit !== "unmount") assert.match(textOf(f.render()), /SYNTHETIC-REPLACEMENT/);
      f.h.dispose(); assert.equal(listenersCount(f.listeners), 0);
    }
  });

  test(`${profile.name}: A→B→A lookups never accept earlier attempts at the same coordinates`, async () => {
    const pending = [deferred(), deferred(), deferred()];
    const f = await setup(profile, (_request, call) => pending[call - 1].promise);
    f.start(); f.move(-97, 39); f.start(); f.move(-98, 38); f.start();
    assert.equal(f.requests.length, 3); assert.equal(f.requests[0].options.signal.aborted, true); assert.equal(f.requests[1].options.signal.aborted, true);
    const first = lateResponse(payload(profile, f.requests[0], "SYNTHETIC-OLD-A")), second = lateResponse(payload(profile, f.requests[1], "SYNTHETIC-OLD-B"));
    pending[0].resolve(first.response); pending[1].resolve(second.response); await settle();
    assert.equal(first.cancelled(), 1); assert.equal(second.cancelled(), 1); assert.equal(inspectButton(f.render()).props.disabled, true);
    assert.doesNotMatch(textOf(f.render()), /SYNTHETIC-OLD/); pending[2].resolve(Response.json(payload(profile, f.requests[2], "SYNTHETIC-NEW-A"))); await settle();
    assert.match(textOf(f.render()), /SYNTHETIC-NEW-A/); assert.doesNotMatch(textOf(f.render()), /SYNTHETIC-OLD/); f.assertReleased(); f.h.dispose();
  });

  test(`${profile.name}: HTTP, network, JSON, byte-cap and response-binding failures keep prior original-scope results and allow an empty retry`, async () => {
    for (const failure of ["http", "network", "json", "declared-cap", "stream-cap", "query", "role", "provider-count", "record-count", ...(profile.name === "KDOT" ? ["page-count"] : ["partial-type"])]) {
      let failedResponse, cancelled = 0;
      const f = await setup(profile, (request, call) => {
        if (call === 1) return Promise.resolve(Response.json(payload(profile, request, "SYNTHETIC-PRIOR")));
        if (call > 2) return Promise.resolve(Response.json(payload(profile, request, "", { empty: true })));
        if (failure === "network") return Promise.reject(new Error("synthetic offline"));
        if (["http", "declared-cap"].includes(failure)) {
          failedResponse = new Response(new ReadableStream({ cancel() { cancelled++; return new Promise(() => {}); } }), { status: failure === "http" ? 503 : 200, headers: failure === "declared-cap" ? { "content-length": String(profile.cap + 1) } : {} });
        } else if (failure === "json") failedResponse = new Response("{");
        else if (failure === "stream-cap") failedResponse = new Response("x".repeat(profile.cap + 1));
        else {
          const body = payload(profile, request);
          if (failure === "query") body.query.longitude = -99;
          if (failure === "role") body.role = "ADMITTED";
          if (failure === "provider-count") body.providerCount = 0;
          if (failure === "record-count") body.records = Array(profile.name === "KDOT" ? bridge.BRIDGE_TOTAL_LIMIT + 1 : blm.BLM_PLSS_LIMIT + 1).fill(body.records[0]);
          if (failure === "page-count") body.pagesRead = 6;
          if (failure === "partial-type") body.partial = "false";
          failedResponse = Response.json(body);
        }
        return Promise.resolve(failedResponse);
      });
      f.start(); await settle(); f.move(-97, 39); f.start(); await settle(); let tree = f.render();
      assert.match(textOf(tree), /unavailable or timed out/i, failure); assert.match(textOf(tree), /SYNTHETIC-PRIOR/, failure);
      assert.match(textOf(tree), /38\.00000\s*,\s*-98\.00000/, failure); assert.doesNotMatch(textOf(tree), /39\.00000\s*,\s*-97\.00000/, failure);
      assert.equal(inspectButton(tree).props.disabled, false); f.assertReleased();
      if (["http", "declared-cap"].includes(failure)) assert.equal(cancelled, 1, failure);
      if (failedResponse) assert.equal(failedResponse.body.locked, false, failure);
      f.start(); await settle(); tree = f.render(); assert.doesNotMatch(textOf(tree), /SYNTHETIC-PRIOR/);
      assert.match(textOf(tree), profile.name === "KDOT" ? /No matching records.*does not establish that no bridge exists/ : /No BLM survey record.*does not establish unsurveyed land/);
      assert.match(textOf(tree), /39\.00000\s*,\s*-97\.00000/); f.assertReleased(); f.h.dispose();
    }
  });

  test(`${profile.name}: valid partial results retain counts, scope and the external-context boundary`, async () => {
    const f = await setup(profile, request => Promise.resolve(Response.json(payload(profile, request, "SYNTHETIC-PARTIAL", { partial: true }))));
    f.start(); await settle(); const tree = f.render(); assert.match(textOf(tree), /Partial.*1 shown from 2/);
    assert.match(textOf(tree), /SYNTHETIC-PARTIAL/); assert.match(textOf(tree), profile.name === "KDOT" ? /no structural-safety or access determination/ : /do not establish a parcel, owner, legal title/);
    f.assertReleased(); f.h.dispose();
  });
}

function listenersCount(listeners) { return [...listeners.values()].reduce((sum, handlers) => sum + handlers.size, 0); }

test("KDOT radius changes cancel immediately and an older radius cannot overwrite its replacement", async () => {
  const profile = profiles[0], old = deferred();
  const f = await setup(profile, (request, call) => call === 1 ? old.promise : Promise.resolve(Response.json(payload(profile, request, "SYNTHETIC-RADIUS-1000"))));
  f.start(); findNode(f.render(), node => node.type === "select").props.onChange({ target: { value: "1000" } });
  assert.equal(f.timers.size, 0); await settle(); assert.equal(f.requests[0].options.signal.aborted, true); f.assertReleased();
  f.start(); await settle(); assert.equal(new URL(f.requests[1].url, "http://fixture.invalid").searchParams.get("radius"), "1000");
  const late = lateResponse(payload(profile, f.requests[0], "SYNTHETIC-OLD-RADIUS")); old.resolve(late.response); await settle();
  assert.equal(late.cancelled(), 1); assert.match(textOf(f.render()), /SYNTHETIC-RADIUS-1000/); assert.doesNotMatch(textOf(f.render()), /SYNTHETIC-OLD-RADIUS/); f.assertReleased(); f.h.dispose();
});

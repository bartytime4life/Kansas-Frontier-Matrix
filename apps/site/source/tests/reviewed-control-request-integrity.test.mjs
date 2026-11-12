import assert from "node:assert/strict";
import test from "node:test";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import ts from "typescript";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

// Actual component effects, release/evidence models and bounded body readers. Transport,
// timers and downloads are controlled; this is not browser, WebGL or provider acceptance.
const modules = new Map();
async function load(name) {
  if (modules.has(name)) return modules.get(name);
  const job = (async () => {
    const js = ts.transpileModule(await readFile(`app/${name}.ts`, "utf8"), {
      compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
    }).outputText;
    const imports = {};
    for (const [, relative] of js.matchAll(/require\("\.\/([a-z-]+)"\)/g)) imports[`./${relative}`] = await load(relative);
    const exports = {};
    vm.runInNewContext(js, {
      exports, TextDecoder, TextEncoder, crypto,
      require(name) { assert.ok(name in imports, name); return imports[name]; },
    });
    return exports;
  })();
  modules.set(name, job);
  return job;
}
const cases = [
  ["water", "GovernedWaterControl"], ["weather", "GovernedWeatherControl"],
  ["soil", "GovernedSoilControl"], ["earthquakes", "GovernedEarthquakesControl"],
  ["storm-events", "GovernedStormEventsControl"],
];
const button = (tree, text) => findNode(tree, n => n.type === "button" && typeof n.props.children === "string" && n.props.children.includes(text));
function clock() {
  let serial = 0;
  const timers = new Map();
  return {
    timers,
    set(fn, delay) { timers.set(++serial, { fn, delay }); return serial; },
    clear(id) { timers.delete(id); },
    fire(delay) {
      for (const [id, entry] of [...timers]) if (entry.delay === delay) { timers.delete(id); entry.fn(); }
    },
  };
}
async function setup(kind, exportName, { evidenceStatus = 200 } = {}) {
  const fixture = async name => JSON.parse(await readFile(`tests/fixtures/governed-${kind}/${name}.json`, "utf8"));
  const monthly = ["earthquakes", "storm-events"].includes(kind);
  const initial = await fixture(monthly ? "layers-may" : "layers"), evidence = await fixture("evidence");
  for (const value of [initial, evidence]) value.data.approval_expires_at = "2099-01-01T00:00:00Z";
  const selected = monthly ? 5 : initial.data.stations[0].id;
  evidence.data.entries = evidence.data.entries.filter(row => monthly ? row.month === selected : row.station_id === selected);
  const fresh = structuredClone(initial);
  if (!monthly) {
    fresh.data.stations = fresh.data.stations.filter(s => s.id === selected);
    fresh.data.observations = fresh.data.observations.filter(o => o.station_id === selected);
  }
  const imports = {};
  for (const name of ["bounded-json", "governed-water", "governed-water-availability", `governed-${kind}-availability`]) imports[`./${name}`] = await load(name);
  const requests = [], downloads = [], blobs = new Map(), timers = clock();
  let disposed = false, now = Date.now();
  class ControlledDate extends Date { static now() { return now; } }
  const h = await componentHarness(`app/governed-${kind}-control.tsx`, imports, {
    Blob, Date: ControlledDate,
    // Deliberately permits late responses after abort, so current-view checks must also hold.
    fetch: (url, options = {}) => new Promise((resolve, reject) => requests.push({ url, options, resolve, reject })),
    setTimeout: timers.set, clearTimeout: timers.clear, setInterval: () => 1, clearInterval() {},
    URL: {
      createObjectURL(blob) { const url = `blob:fixture-${blobs.size}`; blobs.set(url, blob); return url; },
      revokeObjectURL: url => blobs.delete(url),
    },
    document: { createElement: () => ({ click() { downloads.push({ name: this.download, blob: blobs.get(this.href) }); } }) },
  });
  const props = { mapRef: { current: null }, styleReady: false };
  let tree;
  const draw = () => { tree = h.render(h.exports[exportName], props); h.commit(); return tree; };
  const flush = async () => { for (let i = 0; i < 4; i++) { await settle(); draw(); } };
  const respond = (request, value, status = 200) => {
    assert.ok(request, "requested transport exists");
    request.response = value instanceof Response ? value : Response.json(value, { status });
    request.resolve(request.response);
    return request.response;
  };
  draw(); timers.fire(0);
  if (monthly) {
    const boot = await fixture("bootstrap"); boot.data.months = [5]; boot.data.approval_expires_at = "2099-01-01T00:00:00Z";
    respond(requests.at(-1), boot); await flush();
  }
  respond(requests.at(-1), initial); await flush();
  respond(requests.at(-1), evidence, evidenceStatus); await flush();
  const start = () => {
    const before = requests.length, control = button(tree, "Export selected");
    assert.ok(control && !control.props.disabled, "valid initial evidence enables explicit export");
    control.props.onClick();
    return requests[before];
  };
  const advance = async request => {
    const before = requests.length;
    respond(request, fresh); await flush();
    return requests.slice(before).find(q => q.url.includes("/evidence?"));
  };
  const finish = async (request, { first = 200, second = 200 } = {}) => {
    if (request.url.includes("/evidence?")) { respond(request, evidence, second); await flush(); return; }
    const before = requests.length;
    respond(request, fresh, first); await flush();
    const next = requests.slice(before).find(q => q.url.includes("/evidence?"));
    if (next) { respond(next, evidence, second); await flush(); }
  };
  return {
    draw, flush, respond, start, advance, finish, requests, downloads, timers, fresh, evidence,
    get tree() { return tree; },
    expire() { now = Date.parse(initial.data.approval_expires_at); timers.fire(2147483647); },
    dispose() { if (!disposed) { disposed = true; h.dispose(); } },
  };
}
for (const [kind, name] of cases) {
  test(`${kind}: current successful export preserves the source and evidence`, async () => {
    const h = await setup(kind, name);
    try {
      await h.finish(h.start()); assert.equal(h.downloads.length, 1);
      const payload = JSON.parse(await h.downloads[0].blob.text());
      const key = kind === "earthquakes" ? "earthquakes" : kind === "storm-events" ? "events" : "observations";
      assert.deepEqual(payload[key], h.fresh); assert.deepEqual(payload.evidence, h.evidence);
    } finally { h.dispose(); }
  });
  for (const status of [403, 503]) for (const stage of [0, 1]) test(`${kind}: export refuses HTTP ${status} at stage ${stage + 1} despite matching released JSON`, async () => {
    const h = await setup(kind, name);
    try {
      await h.finish(h.start(), stage ? { second: status } : { first: status });
      assert.equal(h.downloads.length, 0); assert.match(JSON.stringify(h.tree), /Export withheld/);
    } finally { h.dispose(); }
  });
  test(`${kind}: failed evidence response cannot enable the export control`, async () => {
    const h = await setup(kind, name, { evidenceStatus: 503 });
    try {
      assert.equal(button(h.tree, "Export selected"), undefined);
      assert.match(JSON.stringify(h.tree), /Evidence request unavailable/);
    } finally { h.dispose(); }
  });
  for (const stage of [0, 1]) {
    test(`${kind}: unmount during stage ${stage + 1} cancels an export and a late response cannot download`, async () => {
      const h = await setup(kind, name), first = h.start(), request = stage ? await h.advance(first) : first;
      h.dispose(); await h.finish(request);
      assert.equal(h.downloads.length, 0); assert.equal(request.options.signal.aborted, true);
      assert.equal(request.response.bodyUsed, true, "late response body is discarded");
    });
    test(`${kind}: rechecking the release during stage ${stage + 1} invalidates the pending export`, async () => {
      const h = await setup(kind, name);
      try {
        const first = h.start(), request = stage ? await h.advance(first) : first;
        button(h.tree, "Check connection").props.onClick(); await h.finish(request);
        assert.equal(h.downloads.length, 0); assert.equal(request.options.signal.aborted, true);
      assert.equal(request.response.bodyUsed, true, "late response body is discarded");
      } finally { h.dispose(); }
    });
    test(`${kind}: an older stage ${stage + 1} export cannot overwrite the latest success`, async () => {
      const h = await setup(kind, name);
      try {
        const first = h.start(), older = stage ? await h.advance(first) : first, newer = h.start();
        await h.finish(newer); assert.equal(h.downloads.length, 1);
        await h.finish(older, { second: 503 });
        assert.equal(h.downloads.length, 1); assert.equal(older.options.signal.aborted, true);
        assert.match(JSON.stringify(h.tree), /Export includes source, evidence and release references/);
        assert.doesNotMatch(JSON.stringify(h.tree), /Export withheld/);
      } finally { h.dispose(); }
    });
    test(`${kind}: the export deadline cancels a stalled stage ${stage + 1} body without waiting for transport cleanup`, async () => {
      const h = await setup(kind, name);
      let control, cancelled = false;
      const body = new ReadableStream({ start(c) { control = c; }, cancel() { cancelled = true; return new Promise(() => {}); } });
      try {
        const first = h.start(), request = stage ? await h.advance(first) : first;
        assert.equal(request.options.signal, first.options.signal, "both stages share one owner and deadline");
        h.respond(request, new Response(body)); await h.flush();
        h.timers.fire(15000); await h.flush();
        assert.equal(cancelled, true); assert.equal(h.downloads.length, 0);
        assert.match(JSON.stringify(h.tree), /Export withheld/);
      } finally { h.dispose(); try { control.close(); } catch { /* Already canceled. */ } }
    });
  }
  test(`${kind}: an expired displayed release invalidates a pending export`, async () => {
    const h = await setup(kind, name);
    try {
      const request = h.start(); h.expire();
      // Even a newly approved matching pair cannot restore this expired view's export.
      for (const value of [h.fresh, h.evidence]) value.data.approval_expires_at = "2099-02-01T00:00:00Z";
      await h.finish(request);
      assert.equal(request.options.signal.aborted, true); assert.equal(h.downloads.length, 0);
      assert.match(JSON.stringify(h.tree), /Release approval expired/);
    } finally { h.dispose(); }
  });
}

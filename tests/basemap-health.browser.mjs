// Real MapLibre + the app's basemap health model in headless Chromium.
// Synthetic local tiles only: no provider requests. Investigates #5779.
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { spawn } from "node:child_process";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import ts from "typescript";
import { deflateSync } from "node:zlib";

// Same DevTools-pipe driver as the other Explorer browser acceptance files.
const chrome = process.env.KFM_TEST_CHROME ?? "google-chrome";
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
async function devtools(t) {
  const profile = await mkdtemp(join(tmpdir(), "kfm-basemap-health-"));
  const child = spawn(chrome, ["--headless=new", "--remote-debugging-pipe", `--user-data-dir=${profile}`, "--no-first-run",
    "--no-default-browser-check", "--disable-background-networking", "--disable-dev-shm-usage", "--enable-unsafe-swiftshader",
    "--use-angle=swiftshader", "--window-size=1440,900", "about:blank"], { stdio: ["ignore", "ignore", "pipe", "pipe", "pipe"] });
  let stderr = "", sequence = 0, buffer = "", closed = false;
  const pending = new Map(), listeners = new Set();
  child.stderr.on("data", chunk => { stderr = (stderr + chunk).slice(-12000); });
  const failPending = error => { closed = true; for (const entry of pending.values()) entry.reject(error); pending.clear(); };
  child.on("error", failPending);
  child.on("exit", code => failPending(new Error(`Chrome exited ${code}: ${stderr}`)));
  child.stdio[4].on("data", chunk => {
    buffer += chunk.toString();
    let index;
    while ((index = buffer.indexOf("\0")) >= 0) {
      const message = JSON.parse(buffer.slice(0, index)); buffer = buffer.slice(index + 1);
      if (message.id) { const item = pending.get(message.id); if (!item) continue; pending.delete(message.id); message.error ? item.reject(new Error(JSON.stringify(message.error))) : item.resolve(message.result); }
      else for (const listener of listeners) listener(message);
    }
  });
  const call = (method, params = {}, sessionId) => new Promise((resolve, reject) => {
    if (closed) { reject(new Error(`Chrome unavailable: ${stderr}`)); return; }
    const id = ++sequence;
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`CDP timeout: ${method}; ${stderr}`)); }, 60000);
    pending.set(id, { resolve: value => { clearTimeout(timer); resolve(value); }, reject: error => { clearTimeout(timer); reject(error); } });
    child.stdio[3].write(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }) + "\0");
  });
  t.after(async () => {
    try { await call("Browser.close"); } catch { child.kill(); }
    if (child.exitCode === null) await Promise.race([new Promise(resolve => child.once("exit", resolve)), pause(2000)]);
    if (child.exitCode === null) child.kill("SIGKILL");
    await rm(profile, { recursive: true, force: true, maxRetries: 3, retryDelay: 100 });
  });
  const { targetId } = await call("Target.createTarget", { url: "about:blank" });
  const { sessionId } = await call("Target.attachToTarget", { targetId, flatten: true });
  const pageErrors = [];
  listeners.add(message => { if (message.sessionId === sessionId && message.method === "Runtime.exceptionThrown") pageErrors.push(JSON.stringify(message.params.exceptionDetails).slice(0, 400)); });
  await call("Runtime.enable", {}, sessionId);
  await call("Emulation.setDeviceMetricsOverride", { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false }, sessionId);
  const evaluate = async expression => {
    const result = await call("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true }, sessionId);
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails).slice(0, 600));
    return result.result.value;
  };
  const navigate = url => call("Page.navigate", { url }, sessionId);
  return { evaluate, navigate, pageErrors };
}

// One opaque 256 px PNG for every tile that is allowed to load.
function png(size, rgb) {
  const crc = buf => { let c = ~0; for (const b of buf) { c ^= b; for (let k = 0; k < 8; k++) c = (c >>> 1) ^ (0xedb88320 & -(c & 1)); } return ~c >>> 0; };
  const chunk = (type, data) => { const len = Buffer.alloc(4); len.writeUInt32BE(data.length); const body = Buffer.concat([Buffer.from(type), data]); const sum = Buffer.alloc(4); sum.writeUInt32BE(crc(body)); return Buffer.concat([len, body, sum]); };
  const header = Buffer.alloc(13); header.writeUInt32BE(size, 0); header.writeUInt32BE(size, 4); header[8] = 8; header[9] = 2;
  const row = Buffer.concat([Buffer.from([0]), Buffer.alloc(size * 3, Buffer.from(rgb))]);
  return Buffer.concat([Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]), chunk("IHDR", header), chunk("IDAT", deflateSync(Buffer.concat(Array(size).fill(row)))), chunk("IEND", Buffer.alloc(0))]);
}
const TILE = png(256, [40, 70, 90]);

async function harness(t) {
  const health = ts.transpileModule(await readFile("app/basemap-health.ts", "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  const dist = new URL("../node_modules/maplibre-gl/dist/", import.meta.url);
  // Failure rules: "z" fails every tile at that zoom once; "z/x/y" fails that tile on every request.
  const rules = { once: new Set(), always: new Set() }, failed = new Set(), requests = [];
  const page = `<!doctype html><meta charset="utf-8"><style>html,body,#map{margin:0;width:100%;height:100%}</style><div id="map"></div>
<script type="module">
import * as maplibregl from "/maplibre/maplibre-gl.mjs";
maplibregl.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
${health.replace(/^export /gm, "")}
const health = createBasemapHealth();
health.beginStyle();
const style = { version: 8, sources: { base: { type: "raster", tiles: [location.origin + "/tiles/{z}/{x}/{y}.png"], tileSize: 256, maxzoom: 14 } }, layers: [{ id: "base", type: "raster", source: "base" }] };
const map = new maplibregl.Map({ container: "map", style, center: [-98.4, 38.5], zoom: 2, fadeDuration: 0, attributionControl: false });
const input = event => { const source = map.getSource("base"); return { sourceId: "base", sourceInstance: source, sourceSpec: source?.serialize(), event }; };
window.kfm = { map, health, errors: 0,
  view: () => { const b = map.getBounds(); return { west: b.getWest(), east: b.getEast(), south: b.getSouth(), north: b.getNorth(), zoom: map.getZoom() }; },
  settle: () => new Promise(resolve => { map.once("idle", () => resolve(null)); map.triggerRepaint(); }),
  idle: () => { if (typeof health.retainInView === "function") health.retainInView(window.kfm.view()); return health.warning(); },
};
map.on("error", event => { if (event.sourceId === "base") { window.kfm.errors++; health.error(input(event)); } });
map.on("sourcedata", event => { if (event.sourceId === "base") health.loaded(input(event)); });
map.once("load", () => { window.kfm.ready = true; });
</script>`;
  const server = createServer(async (request, response) => {
    const url = new URL(request.url, "http://local");
    const asset = url.pathname.match(/^\/maplibre\/(maplibre-gl(?:-shared|-worker)?\.mjs)$/);
    if (asset) { response.writeHead(200, { "Content-Type": "text/javascript" }); response.end(await readFile(new URL(asset[1], dist))); return; }
    const match = url.pathname.match(/^\/tiles\/(\d+)\/(\d+)\/(\d+)\.png$/);
    if (!match) { response.writeHead(200, { "Content-Type": "text/html" }); response.end(page); return; }
    const [z, x, y] = match.slice(1), key = `${z}/${x}/${y}`;
    requests.push(key);
    const fail = rules.always.has(key) || (rules.once.has(z) && !failed.has(key));
    if (fail) { failed.add(key); response.writeHead(503); response.end(); return; }
    response.writeHead(200, { "Content-Type": "image/png", "Cache-Control": "no-store" }); response.end(TILE);
  });
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  t.after(() => server.close());
  const tab = await devtools(t);
  await tab.navigate(`http://127.0.0.1:${server.address().port}/`);
  const deadline = Date.now() + 30000;
  while (!(await tab.evaluate("window.kfm?.ready === true").catch(() => false))) {
    if (Date.now() > deadline) throw new Error("MapLibre fixture did not load: " + tab.pageErrors.join("\n"));
    await pause(100);
  }
  const settle = () => tab.evaluate("window.kfm.settle()");
  const pageErrors = tab.pageErrors;
  const close = async () => {};
  return { tab, rules, failed, requests, pageErrors, settle, close };
}

test("a tile that fails mid-flight and is never needed again does not leave a permanent basemap warning", async t => {
  const h = await harness(t);
  try {
    await h.settle();
    h.rules.once.add("4"); h.rules.once.add("5");
    await h.tab.evaluate("void window.kfm.map.flyTo({ center: [-95.7, 39.05], zoom: 9, duration: 2500 })");
    await pause(3000); await h.settle();
    const result = await h.tab.evaluate("({ errors: window.kfm.errors, warning: window.kfm.idle(), zoom: window.kfm.map.getZoom() })");
    assert.ok(result.errors > 0, "the flight requested and failed intermediate-zoom tiles");
    assert.equal(h.pageErrors.length, 0, h.pageErrors.join("\n"));
    // Every tile the settled z9 view needs loaded; the failures were transient intermediate tiles.
    assert.equal(result.warning, null, `settled view is complete, but the health model still warns after ${result.errors} transient errors`);
  } finally { await h.close(); }
});

test("a missing tile in the settled view still warns, and returning to a pruned gap warns again", async t => {
  const h = await harness(t);
  try {
    await h.tab.evaluate("void window.kfm.map.jumpTo({ center: [-95.7, 39.05], zoom: 7 })");
    await h.settle();
    // 256 px raster tiles render one level above the map zoom; take the finest tile the settled view requested.
    const finest = Math.max(...h.requests.map(key => Number(key.split("/")[0])));
    const tile = h.requests.findLast(key => key.startsWith(`${finest}/`));
    assert.ok(tile, "the settled view requested its own tiles");
    h.rules.always.add(tile);
    await h.tab.evaluate("void window.kfm.map.refreshTiles('base')");
    await pause(1500); await h.settle();
    assert.match(await h.tab.evaluate("window.kfm.idle()") ?? "", /basemap tiles are unavailable/, "a real gap in view keeps the warning");
    // Move far away: the gap is no longer on screen.
    await h.tab.evaluate("void window.kfm.map.jumpTo({ center: [10, 50], zoom: 7 })");
    await h.settle();
    assert.equal(await h.tab.evaluate("window.kfm.idle()"), null, "an off-screen gap does not warn about the current view");
    // Return: MapLibre does not cache errored tiles, so it re-requests and reports the gap again.
    await h.tab.evaluate("void window.kfm.map.jumpTo({ center: [-95.7, 39.05], zoom: 7 })");
    await pause(1500); await h.settle();
    assert.match(await h.tab.evaluate("window.kfm.idle()") ?? "", /basemap tiles are unavailable/, "the persisting gap is reported again on return");
  } finally { await h.close(); }
});

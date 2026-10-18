import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import ts from "typescript";
import { webcrypto } from "node:crypto";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const read = name => readFile(new URL(`../app/${name}`, import.meta.url), "utf8");
const compile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText;
const load = async (name, dependencies = {}, globals = {}) => {
  const exports = {};
  vm.runInNewContext(compile(await read(name)), { exports, require: id => dependencies[id] ?? {}, URL, Date, Response, Headers, AbortSignal, setTimeout, clearTimeout, ...globals });
  return exports;
};
const profile = await load("public-profile.ts");
const packageId = "sha256:" + "a".repeat(64);

test("public copy maps only approved family artifact names, never arbitrary paths", () => {
  assert.equal(profile.IS_PUBLIC_COPY, true);
  assert.equal(profile.publicDataAsset("/data/subsurface/tile-165-255.json.gz"), "/api/governed/public/assets/subsurface/tile-165-255.json.gz");
  assert.equal(profile.publicDataAsset("/data/groundwater/kgs-depth-to-water.geojson"), "/api/governed/public/assets/groundwater/kgs-depth-to-water.geojson");
  for (const path of ["/data/subsurface/../private.json", "/data/subsurface/a.json?token=x", "https://example.org/x", "/data/subsurface/%2e%2e.json", "/data/raw/private.json"])
    assert.throws(() => profile.publicDataAsset(path), /PUBLIC_ASSET_PATH_INVALID/);
});

test("received bytes require an unexpired package-bound release, even on HTTP 200", () => {
  const response = (expires, id = packageId, status = 200) => new Response("{}", { status, headers: { "X-KFM-Public-Release-ID": id, "X-KFM-Public-Expires-At": expires } });
  assert.equal(profile.publicAssetLease(response("2099-01-01T00:00:00Z")).packageId, packageId);
  assert.throws(() => profile.publicAssetLease(response("2020-01-01T00:00:00Z")), /expired/);
  assert.throws(() => profile.publicAssetLease(response("2099-01-01T00:00:00Z", "unbound")), /unavailable/);
  assert.throws(() => profile.publicAssetLease(response("2099-01-01T00:00:00Z", packageId, 404)), /No approved/);
});

test("public basemap transport never contacts the visitor's loopback cache", async () => {
  let requests = 0;
  const cache = await load("basemap-cache.ts", { "./public-profile": profile }, { fetch: async () => { requests++; throw new Error("Unexpected network"); } });
  const url = "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/8/97/58";
  assert.equal(cache.basemapCacheRequest(url, "Tile").url, url);
  assert.equal(cache.basemapCacheEnabled(), false);
  assert.equal(await cache.connectBasemapCache(true), null);
  assert.equal(requests, 0);
});

test("public copy rejects every private companion client before a network request", async () => {
  let requests = 0;
  const globals = { fetch: async () => { requests++; throw new Error("Unexpected network"); } };
  const dependencies = { "./public-profile": profile, "./intake-desk-client": { INTAKE_DESK_ORIGIN: "http://127.0.0.1:8771" } };
  const downloads = await load("local-download-client.ts", dependencies, globals);
  const maps = await load("public-map-client.ts", dependencies, globals);
  const intake = await load("intake-desk-client.ts", dependencies, globals);
  const atlas = await load("local-atlas-client.ts", dependencies, globals);
  await assert.rejects(downloads.localDownloadRequest("/status"));
  await assert.rejects(maps.publicMapRequest("/status"));
  await assert.rejects(intake.intakeOverviewRequest());
  await assert.rejects(atlas.atlasRequest("/api/status", undefined, () => true));
  assert.equal(requests, 0);
});

test("shared URLs cannot reactivate unapproved provider overlays or imagery", () => {
  assert.equal(profile.publicContextSourceAllowed("nws-radar"), false);
  assert.equal(profile.publicContextSourceAllowed("blm-plss-townships"), false);
  assert.equal(profile.publicBasemap("imagery"), "standard");
  assert.equal(profile.publicBasemap("kansas-aerial"), "standard");
  assert.equal(profile.publicBasemap("midnight"), "midnight");
});

test("export revalidation refuses replacement, withdrawal and unreadable catalogs", async () => {
  let entries = [{ family: "subsurface", package_id: packageId, expires_at: "2099-01-01T00:00:00Z" }];
  const current = await load("public-profile.ts", {}, { fetch: async () => Response.json({ envelope: { outcome: "ANSWER" }, data: { entries } }) });
  assert.equal(await current.publicFamilyAvailable("subsurface", undefined, packageId), true);
  assert.equal(await current.publicFamilyAvailable("subsurface", undefined, "sha256:" + "b".repeat(64)), false);
  entries = [];
  assert.equal(await current.publicFamilyAvailable("subsurface", undefined, packageId), false);
  const failed = await load("public-profile.ts", {}, { fetch: async () => { throw new Error("Offline"); } });
  assert.equal(await failed.publicFamilyAvailable("subsurface"), false);
});

test("public geophysical rows require the current query lease and clear when the worker fails", async () => {
  const materials = await load("subsurface-materials.ts");
  const model = await load("subsurface-model.ts", { "./subsurface-materials": materials });
  const slices = await load("subsurface-slice.ts", { "./subsurface-model": model });
  const requests = [], messages = [], timers = new Map(); let timerId = 0;
  const worker = { postMessage: value => messages.push(value), terminate() {} };
  // Synthetic TEST-ONLY profile, never bundled or admitted as public data.
  const survey = { id: "test-survey", title: "Synthetic TEST-ONLY approved-path profile", method: "electrical", sourceUrl: "https://example.test/source", sourceTime: "2000-01-01", retrievedAt: "2000-01-02T00:00:00Z", status: "ready", limitation: "TEST-ONLY", profiles: [{ id: "p", title: "TEST-ONLY", coordinates: [-95,39], depthUnit: "m", depthReference: "land-surface", valueUnit: "ohm-m", samples: [{ depth: 1, value: 5 }, { depth: 2, value: 6 }] }] };
  assert.equal(model.validGeophysicalSurvey(survey), true);
  const h = await componentHarness("app/underground-panel.tsx", {
    "./public-profile": profile, "./subsurface-model": model, "./subsurface-materials": materials, "./subsurface-slice": slices,
    "./subsurface.module.css": { default: new Proxy({}, { get: (_, key) => key }) }, "./subsurface-workers": { startSubsurfaceWorker: () => worker }, "./cutaway-locator": {},
  }, {
    matchMedia: () => ({ matches: true, addEventListener() {}, removeEventListener() {} }), document: { hidden: false, addEventListener() {}, removeEventListener() {} }, window: { addEventListener() {}, removeEventListener() {} }, queueMicrotask,
    setInterval: () => 1, clearInterval() {}, setTimeout: fn => { const id = ++timerId; timers.set(id, fn); return id; }, clearTimeout: id => timers.delete(id),
    fetch: async url => { requests.push(url); return Response.json({ version: 1, surveys: [survey] }, { headers: { "X-KFM-Public-Release-ID": packageId, "X-KFM-Public-Expires-At": "2099-01-01T00:00:00Z" } }); },
  });
  const noop = () => {};
  const props = { map: null, initialContext: null, year: 2026, redacted: false, onContext: noop, onInspect: noop, onFlatMap: noop, onTerrain: noop, onDraw: noop, onClose: noop, onSave: noop, onReport: noop, isDrawing: () => false, readTransect: () => [], readElevation: () => null };
  const draw = () => { const tree = h.render(h.exports.default, props); h.commit(); return tree; };
  let tree = draw();
  findNode(tree, node => node.props?.["aria-label"] === "Underground tool").props.onChange({ target: { value: "surveys" } });
  draw(); for (const [id, fn] of [...timers]) { timers.delete(id); fn(); }
  assert.equal(requests.length, 0, "an unleased tool cannot request survey bytes");
  worker.onmessage({ data: { id: messages.at(-1).id, manifest: { sources: [], counties: [], totals: {} }, columns: [], publicLease: { packageId, expiresAt: Date.parse("2099-01-01T00:00:00Z") } } });
  draw(); await new Promise(resolve => setTimeout(resolve, 5)); await settle(); tree = draw();
  assert.deepEqual(requests, ["/api/governed/public/assets/subsurface/geophysics.json"]);
  assert.equal(findNode(tree, node => node.props?.survey?.id === survey.id)?.props.survey.title, survey.title);
  worker.onerror(); tree = draw();
  assert.equal(findNode(tree, node => node.props?.survey?.id === survey.id), undefined);
  h.dispose();
});

test("reviewed weather selects only exact station-local days and preserves null missingness", async () => {
  const helpers = await load("governed-weather-availability.ts");
  const rows = [{ station_id: "A", observation_date: "2026-10-10", element: "PRCP", value: null, withheld: "MISSING" },
    { station_id: "A", observation_date: "2026-10-12", element: "TMAX", value: 0, withheld: null },
    { station_id: "B", observation_date: "2026-10-11", element: "PRCP", value: 8, withheld: null }];
  assert.deepEqual(Array.from(helpers.weatherStationDays(rows, "A")), ["2026-10-10", "2026-10-12"]);
  assert.equal(helpers.weatherDayAt(rows, "A", "2026-10-11"), null);
  const missing = helpers.weatherDayAt(rows, "A", "2026-10-10");
  assert.equal(missing.values.PRCP.value, null);
  assert.equal(helpers.weatherValueText(missing.values.PRCP), "Withheld (missing)");
  assert.equal(helpers.weatherDayAt(rows, "A", "2026-10-12").values.TMAX.value, 0);
});

test("weather Previous/Next callbacks select the actual reviewed package days", async () => {
  const helpers = await load("governed-weather-availability.ts");
  const water = await load("governed-water-availability.ts");
  const layers = JSON.parse(await readFile(new URL("./fixtures/governed-weather/layers.json", import.meta.url), "utf8"));
  layers.data.approval_expires_at = "2099-01-01T00:00:00Z";
  const slots = new Map([[0, layers]]);
  let cursor = 0;
  const react = { useState(initial) { const key = cursor++; if (!slots.has(key)) slots.set(key, typeof initial === "function" ? initial() : initial); return [slots.get(key), value => slots.set(key, typeof value === "function" ? value(slots.get(key)) : value)]; }, useRef: current => ({ current }), useCallback: fn => fn, useEffect() {} };
  const jsx = (type, props) => ({ type, props });
  const component = await load("governed-weather-control.tsx", {
    react, "react/jsx-runtime": { jsx, jsxs: jsx, Fragment: "fragment" },
    "./governed-water-availability": water, "./governed-weather-availability": helpers,
    "./governed-water": { approvalRemainingMs: expiry => Date.parse(expiry) - Date.now() },
  });
  const draw = () => { cursor = 0; return component.GovernedWeatherControl({ mapRef: { current: null }, styleReady: false }); };
  const find = (node, predicate) => {
    if (!node || typeof node !== "object") return;
    if (predicate(node)) return node;
    for (const child of [node.props?.children].flat(Infinity)) { const result = find(child, predicate); if (result) return result; }
  };
  const days = Array.from(helpers.weatherStationDays(layers.data.observations, "USW00003928"));
  let tree = draw();
  const date = () => find(tree, node => node.props?.["aria-label"] === "Reviewed weather observation day");
  assert.equal(date().props.value, days.at(-1));
  find(tree, node => node.type === "button" && node.props.children === "Previous day").props.onClick(); tree = draw();
  assert.equal(date().props.value, days.at(-2));
  find(tree, node => node.type === "button" && node.props.children === "Next day").props.onClick(); tree = draw();
  assert.equal(date().props.value, days.at(-1));
  assert.equal(find(tree, node => node.type === "button" && node.props.children === "Next day").props.disabled, true);
});

test("source app excludes synthetic fixtures and retains the stronger repository subsurface hold", async () => {
  assert.doesNotMatch(await read("page.tsx"), /from ["']\.\/living-waters-(?:fixture|control)["']/);
  assert.match(await read("aquifer-volume-worker.ts"), /publicDataAsset/);
  assert.match(await read("subsurface-worker.ts"), /withheld pending rights, sensitivity and release review/);
  assert.match(await read("underground-panel.tsx"), /visibilitychange/);
});

test("public subsurface queries remain withheld without fetching any candidate bytes", async () => {
  const messages = [], requests = [];
  const scope = { location: { origin: "https://preview.example" }, postMessage: value => messages.push(value) };
  await load("subsurface-worker.ts", {}, {
    self: scope,
    fetch: async url => { requests.push(url); throw Error("Unexpected source read"); },
  });
  for (const [id, kind] of ["prepare", "search", "probe", "area"].entries()) {
    scope.onmessage({ origin: scope.location.origin, data: { id, kind } });
    const result = messages.at(-1);
    assert.equal(result.id, id);
    assert.equal(result.columns.length, 0);
    assert.equal(result.manifest.tiles.length, 0);
    assert.match(result.error, /withheld.*review/);
  }
  scope.onmessage({ origin: "https://foreign.example", data: { id: 99, kind: "area" } });
  assert.equal(messages.length, 4);
  assert.deepEqual(requests, []);
});

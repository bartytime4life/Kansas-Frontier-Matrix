import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const moduleUrl = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText).toString("base64")}`;
const helpersUrl = moduleUrl(await readFile("app/neon-lidar-preview.ts", "utf8"));
const helpers = await import(helpersUrl);
const { NEON_LIDAR_MAX_BYTES, parseNeonLidarPreview, neonLidarProbe, neonLidarProfile, neonElevationDomain, neonSampleColor, readNeonLidarLocalJson } = helpers;
const inventoryUrl = moduleUrl(await readFile("app/acquisition-inventory.ts", "utf8"));
const clientUrl = moduleUrl((await readFile("app/acquisition-client.ts", "utf8")).replace('from "./acquisition-inventory"', `from "${inventoryUrl}"`));
const client = await import(clientUrl);
const boundedUrl = moduleUrl(await readFile("app/bounded-json.ts", "utf8"));
const pilotUrl = moduleUrl((await readFile("app/neon-lidar-pilot-client.ts", "utf8")).replace('"./bounded-json"', JSON.stringify(boundedUrl)).replace('"./neon-lidar-preview"', JSON.stringify(helpersUrl)));
const pilotClient = await import(pilotUrl);


function fixture(width = 8) {
  const tile = "NEON_D06_KONZ_DP3_666000_4328000";
  return {
    schema_version: "kfm-neon-lidar-preview-v1", data_kind: "synthetic-test", generated_at: "2026-11-23T12:34:56.123456Z",
    source: {
      site: "KONZ", month: "2024-06", acquisition_run: "2024_KONZ_1", release: "RELEASE-2026", tile,
      attribution: "Synthetic analytic test fixture; no NEON observations", horizontal_crs: 'PROJCRS["NAD83 / UTM zone 14N"]', vertical_reference: "Synthetic vertical reference; not surveyed", vertical_reference_basis: "Synthetic test metadata",
      canopy_floor_m: 0.7, canopy_floor_basis: "Synthetic test floor",
      files: ["dtm", "dsm", "chm"].map(kind => ({ kind, name: `${tile}_${kind.toUpperCase()}.tif`, product: kind === "chm" ? "DP3.30015.001" : "DP3.30024.001", bytes: 1000, sha256: "a".repeat(64) })),
    },
    grid: { width, height: width, bounds: [666000, 4328000, 667000, 4329000], source_resolution_m: 1, preview_resolution_m: 1000 / width, sampling: "nearest-neighbor", dtm: Array(width ** 2).fill(-2.125), dsm: Array(width ** 2).fill(4.25), chm: Array(width ** 2).fill(6) },
    lifecycle: "local-preview-only", source_admitted: false, released: false,
  };
}
function rejected(mutate) { const input = fixture(); mutate(input); assert.equal(parseNeonLidarPreview(input), null); }

test("bounded square grids retain zeros, negative elevations, nulls and original precision", () => {
  for (const width of [8, 10, 64, 127, 128]) {
    const input = fixture(width); input.grid.dtm[0] = null; input.grid.dsm[1] = 0; input.grid.chm[2] = 0;
    const result = parseNeonLidarPreview(input); assert.ok(result);
    assert.equal(result.grid.dtm[0], null); assert.equal(result.grid.dsm[1], 0); assert.equal(result.grid.chm[2], 0); assert.equal(result.grid.dtm[1], -2.125);
  }
  for (const floor of [null, 0.7, 2]) { const input = fixture(); input.source.canopy_floor_m = floor; assert.ok(parseNeonLidarPreview(input)); }
  const provider = fixture(); provider.data_kind = "provider-files"; assert.ok(parseNeonLidarPreview(provider));
});

test("malformed numbers, dimensions, bounds and grid definitions fail closed", () => {
  for (const [key, value] of [["width", 7], ["width", 129], ["width", 8.5], ["height", 9], ["source_resolution_m", 2], ["preview_resolution_m", 100], ["sampling", "bilinear"]]) rejected(input => { input.grid[key] = value; });
  for (const value of [NaN, Infinity, -Infinity, "0", false, undefined]) for (const kind of ["dtm", "dsm", "chm"]) rejected(input => { input.grid[kind][0] = value; });
  rejected(input => { input.grid.chm[0] = -0.01; });
  rejected(input => { input.grid.dtm.pop(); });
  rejected(input => { input.grid.dsm.push(0); });
  for (const bounds of [[666000, 4328000, 667001, 4329000], [666000, 4328000, 665000, 4329000], [666001, 4328000, 667001, 4329000], [666000, 4328000, 667000, Infinity], [666000, 4328000, 667000]]) rejected(input => { input.grid.bounds = bounds; });
});

test("site, product, exact file identities, dates and provenance cannot silently disagree", () => {
  for (const [key, value] of [["site", "ABCD"], ["site", "KONA"], ["tile", "NEON_D06_KONZ_DP3_666001_4328000"], ["month", "2025-13"], ["month", "0000-01"], ["release", "PROVISIONAL"], ["release", "RELEASE-26"], ["horizontal_crs", "EPSG:4326"], ["vertical_reference", ""], ["canopy_floor_m", 1], ["canopy_floor_basis", ""]]) rejected(input => { input.source[key] = value; });
  for (const date of ["2026-02-30T00:00:00Z", "2026-11-23", "2026-11-23T12:00:00+00:00", "2026-11-23T25:00:00Z"]) rejected(input => { input.generated_at = date; });
  for (const [key, value] of [["kind", "dtm"], ["name", "../other.tif"], ["product", "DP3.30015.001"], ["sha256", "A".repeat(64)], ["bytes", 0], ["bytes", Number.MAX_SAFE_INTEGER + 1]]) rejected(input => { input.source.files[1][key] = value; });
  rejected(input => { input.source.files.pop(); });
  rejected(input => { input.source.horizontal_crs = "x".repeat(12001); });
  rejected(input => { input.source.attribution = "NEON\u0000"; });
  for (const [key, value] of [["source_admitted", true], ["released", true], ["lifecycle", "released"], ["data_kind", undefined]]) rejected(input => { input[key] = value; });
  assert.equal(parseNeonLidarPreview(null), null); assert.equal(parseNeonLidarPreview([]), null);
});

test("north-up probes use the precise nearest 1m source sample, preserve differences and reject off-grid indices", () => {
  const input = fixture(64); input.grid.dtm[0] = 10; input.grid.dsm[0] = 8; input.grid.chm[0] = 0;
  assert.deepEqual(neonLidarProbe(input, 0, 0), { row: 0, column: 0, dtm: 10, dsm: 8, chm: 0, easting: 666007.5, northing: 4328992.5, surfaceAboveGround: -2, differenceIssue: "negative" });
  const last = neonLidarProbe(input, 63, 63); assert.equal(last.easting, 666992.5); assert.equal(last.northing, 4328007.5);
  const uneven = neonLidarProbe(fixture(127), 126, 126); assert.equal(uneven.easting, 666996.5); assert.equal(uneven.northing, 4328003.5);
  input.grid.dtm[1] = null; input.grid.dsm[1] = 0; const missing = neonLidarProbe(input, 0, 1); assert.equal(missing.dsm, 0); assert.equal(missing.surfaceAboveGround, null); assert.equal(missing.differenceIssue, "missing");
  input.grid.dtm[2] = -1e308; input.grid.dsm[2] = 1e308; assert.equal(neonLidarProbe(input, 0, 2).differenceIssue, "nonfinite");
  for (const [row, col] of [[-1, 0], [64, 0], [0, 64], [0.5, 0], [0, NaN]]) assert.equal(neonLidarProbe(input, row, col), null);
});

test("recorded acquisition run must match the catalog year and site with a positive run number", () => {
  for (const run of [undefined, "", "2025_KONZ_1", "2024_KONA_1", "2024_UKFS_1", "2024_KONZ_0", "2024_KONZ_-1", "2024_KONZ_01", "2024_KONZ_1.5", "2024_KONZ_1/../2", "2024_KONZ_" + "1".repeat(100)]) rejected(input => { input.source.acquisition_run = run; });
  const repeated = fixture(); repeated.source.acquisition_run = "2024_KONZ_23"; assert.ok(parseNeonLidarPreview(repeated));
  const otherSite = fixture(); otherSite.source.site = "UKFS"; otherSite.source.acquisition_run = "2024_UKFS_2"; otherSite.source.tile = otherSite.source.tile.replace("KONZ", "UKFS"); otherSite.source.files.forEach(file => { file.name = file.name.replace("KONZ", "UKFS"); }); assert.ok(parseNeonLidarPreview(otherSite));
});

test("profiles retain discrete row and column measurements with native-center distances", () => {
  const input = fixture();
  for (let row = 0; row < 8; row++) for (let column = 0; column < 8; column++) {
    const index = row * 8 + column;
    input.grid.dtm[index] = 100 + row * 10 + column;
    input.grid.dsm[index] = input.grid.dtm[index] + column - 2;
    input.grid.chm[index] = row;
  }
  const across = neonLidarProfile(input, "row", 2);
  assert.equal(across.axis, "row"); assert.equal(across.fixedIndex, 2);
  assert.deepEqual(across.samples.map(sample => sample.dtm), [120, 121, 122, 123, 124, 125, 126, 127]);
  assert.deepEqual(across.samples.map(sample => sample.distance_m), [0, 125, 250, 375, 500, 625, 750, 875]);
  assert.deepEqual(across.samples.map(sample => [sample.row, sample.column]), Array.from({ length: 8 }, (_, column) => [2, column]));
  assert.equal(across.samples[0].easting, 666062.5); assert.equal(across.samples[0].northing, 4328687.5);
  assert.equal(across.samples[0].surfaceAboveGround, -2); assert.equal(across.samples[0].differenceIssue, "negative");
  const down = neonLidarProfile(input, "column", 3);
  assert.deepEqual(down.samples.map(sample => sample.dtm), [103, 113, 123, 133, 143, 153, 163, 173]);
  assert.deepEqual(down.samples.map(sample => sample.distance_m), [0, 125, 250, 375, 500, 625, 750, 875]);
  assert.equal(down.samples.at(-1).northing, 4328062.5); assert.equal(down.samples.at(-1).easting, 666437.5);
});

test("non-divisor profiles use actual nearest-center positions, not nominal grid spacing or tile edges", () => {
  const input = fixture(12);
  const expected = [0, 84, 167, 250, 334, 417, 500, 584, 667, 750, 834, 917];
  for (const axis of ["row", "column"]) {
    const profile = neonLidarProfile(input, axis, 11);
    assert.deepEqual(profile.samples.map(sample => sample.distance_m), expected);
    assert.equal(profile.samples.length, 12);
    assert.notEqual(profile.samples.at(-1).distance_m, 1000);
  }
});

test("profiles preserve per-surface NoData, zero, negative and overflow QA without changing source arrays", () => {
  const input = fixture(); input.grid.dtm.fill(null); input.grid.dsm.fill(null); input.grid.chm.fill(null);
  input.grid.dtm[0] = 0; input.grid.dsm[0] = 0; input.grid.chm[0] = 0;
  input.grid.dtm[2] = 2; input.grid.dsm[2] = 1;
  input.grid.dtm[3] = -1e308; input.grid.dsm[3] = 1e308;
  const original = structuredClone(input);
  input.grid.dtm = Object.freeze(input.grid.dtm); input.grid.dsm = Object.freeze(input.grid.dsm); input.grid.chm = Object.freeze(input.grid.chm);
  const samples = neonLidarProfile(input, "row", 0).samples;
  assert.deepEqual(samples.map(sample => sample.surfaceAboveGround), [0, null, -1, null, null, null, null, null]);
  assert.deepEqual(samples.map(sample => sample.differenceIssue), [null, "missing", "negative", "nonfinite", "missing", "missing", "missing", "missing"]);
  assert.equal(samples[0].chm, 0); assert.equal(samples[2].chm, null);
  assert.equal(samples[3].dtm, -1e308); assert.equal(samples[3].dsm, 1e308);
  assert.equal(neonLidarProfile(input, "row", 7).samples.every(sample => sample.dtm === null && sample.dsm === null && sample.chm === null), true);
  assert.deepEqual(input, original);
});

test("profiles reject invalid axis or fixed index without selecting a substitute sample", () => {
  const input = fixture();
  for (const axis of ["row", "column"]) for (const index of [-1, 8, 0.5, NaN, Infinity, "1", null, undefined]) assert.equal(neonLidarProfile(input, axis, index), null);
  for (const axis of ["diagonal", "", null, undefined]) assert.equal(neonLidarProfile(input, axis, 0), null);
});

test("shared elevation domain excludes NoData and CHM; color handles constants, saturation and extreme finite inputs", () => {
  const input = fixture(); input.grid.dtm[0] = -10; input.grid.dsm[0] = 20; input.grid.chm[0] = 1000;
  assert.deepEqual(neonElevationDomain(input), [-10, 20]);
  input.grid.dtm.fill(null); input.grid.dsm.fill(null); assert.equal(neonElevationDomain(input), null);
  input.grid.dtm.fill(0); assert.deepEqual(neonElevationDomain(input), [0, 0]);
  assert.equal(neonSampleColor(30, [0, 30]), neonSampleColor(100, [0, 30]));
  assert.notEqual(neonSampleColor(0, [0, 30]), neonSampleColor(30, [0, 30]));
  assert.doesNotMatch(neonSampleColor(0, [0, 0]), /NaN|Infinity/);
  assert.doesNotMatch(neonSampleColor(0, [-1e308, 1e308]), /NaN|Infinity/);
});

test("local reader enforces byte budgets before parsing and retires canceled reads", async () => {
  const input = fixture(); input.extra = "a".repeat(NEON_LIDAR_MAX_BYTES); assert.equal(parseNeonLidarPreview(input), null);
  const signal = new AbortController();
  await assert.rejects(readNeonLidarLocalJson({ size: NEON_LIDAR_MAX_BYTES + 1, text: () => assert.fail("oversize file must not be read") }, signal.signal), /2 MiB/);
  await assert.rejects(readNeonLidarLocalJson({ size: 1, text: async () => "é".repeat(NEON_LIDAR_MAX_BYTES / 2 + 1) }, signal.signal), /2 MiB/);
  let finish; const pending = readNeonLidarLocalJson({ size: 1, text: () => new Promise(resolve => { finish = resolve; }) }, signal.signal);
  signal.abort(); finish("{}"); await assert.rejects(pending, { name: "AbortError" });
});

test("empty panel explains cost and local boundaries, includes useful import controls and no sample terrain", async () => {
  const cssUrl = 'data:text/javascript,export default new Proxy({}, {get: (_, key) => key})';
  let source = ts.transpileModule(await readFile("app/neon-lidar-panel.tsx", "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText;
  for (const [from, to] of [["react", import.meta.resolve("react")], ["react/jsx-runtime", import.meta.resolve("react/jsx-runtime")], ["./acquisition-client", clientUrl], ["./neon-lidar-pilot-client", pilotUrl], ["./neon-lidar-preview", helpersUrl], ["./neon-lidar-panel.module.css", cssUrl]]) source = source.replaceAll(`from "${from}"`, `from "${to}"`);
  const { NeonLidarPanel } = await import(moduleUrl(source));
  const html = renderToStaticMarkup(createElement(NeonLidarPanel));
  assert.match(html, /Free, no subscription/); assert.match(html, /not uploaded/); assert.match(html, /2 MiB maximum/); assert.match(html, /starts with no sample terrain/);
  assert.match(html, /type="file"/); assert.match(html, /Clear preview/); assert.doesNotMatch(html, /<canvas/);
});

test("new file selection clears the old probe, stale read cannot replace a new grid, and cancel retires work", async () => {
  const harness = await componentHarness("app/neon-lidar-panel.tsx", { "./neon-lidar-preview": helpers, "./neon-lidar-pilot-client": pilotClient, "./acquisition-client": client, "./neon-lidar-panel.module.css": { default: new Proxy({}, { get: (_, key) => key }) } });
  const render = () => { const tree = harness.render(() => { const workspace = harness.exports.NeonLidarPanel(); return harness.exports.NeonLidarWorkspace(workspace.props); }); harness.commit(); return tree; };
  const fileInput = tree => findNode(tree, node => node.type === "input" && node.props.type === "file");
  const upload = (tree, value) => fileInput(tree).props.onChange({ target: { files: [value], value: "chosen.json" } });
  const localFile = data => ({ size: 1000, text: async () => JSON.stringify(data) });
  let tree = render(); upload(tree, localFile(fixture())); await settle(); tree = render();
  assert.ok(findNode(tree, node => node.type === "input" && node.props.type === "number"));
  const row = findNode(tree, node => node.type === "input" && node.props.type === "number"); row.props.onChange({ target: { value: "2" } }); tree = render();
  assert.equal(findNode(tree, node => node.type === "input" && node.props.type === "number").props.value, "2");
  let finish; upload(tree, { size: 1000, text: () => new Promise(resolve => { finish = resolve; }) }); tree = render();
  assert.equal(findNode(tree, node => node.type === "input" && node.props.type === "number"), undefined);
  const next = fixture(); next.source.month = "2024-07"; upload(tree, localFile(next)); await settle(); tree = render();
  assert.equal(findNode(tree, node => node.type === "input" && node.props.type === "number").props.value, "");
  finish(JSON.stringify(fixture())); await settle(); tree = render();
  assert.ok(findNode(tree, node => node.type === "span" && Array.isArray(node.props.children) && node.props.children.includes("2024-07")));
  let finishCanceled; upload(tree, { size: 1000, text: () => new Promise(resolve => { finishCanceled = resolve; }) }); tree = render();
  findNode(tree, node => node.type === "button" && node.props.children === "Cancel local read").props.onClick(); finishCanceled(JSON.stringify(fixture())); await settle(); tree = render();
  assert.equal(findNode(tree, node => node.type === "input" && node.props.type === "number"), undefined);
  harness.dispose();
});

test("row and column drafts can be cleared and retyped without restoring an old probe; canvas synchronizes both", async () => {
  const harness = await componentHarness("app/neon-lidar-panel.tsx", { "./neon-lidar-preview": helpers, "./neon-lidar-pilot-client": pilotClient, "./acquisition-client": client, "./neon-lidar-panel.module.css": { default: new Proxy({}, { get: (_, key) => key }) } });
  const render = () => { const tree = harness.render(() => { const workspace = harness.exports.NeonLidarPanel(); return harness.exports.NeonLidarWorkspace(workspace.props); }); harness.commit(); return tree; };
  const axis = (tree, suffix) => findNode(tree, node => node.type === "input" && node.props.type === "number" && node.props.id.endsWith(suffix));
  const canvas = tree => findNode(tree, node => typeof node.type === "function" && node.type.name === "GridCanvas");
  let tree = render();
  findNode(tree, node => node.type === "input" && node.props.type === "file").props.onChange({ target: { files: [{ size: 1000, text: async () => JSON.stringify(fixture()) }], value: "preview.json" } });
  await settle(); tree = render();
  axis(tree, "-row").props.onChange({ target: { value: "3" } }); tree = render();
  assert.equal(axis(tree, "-column").props.value, "1"); assert.equal(canvas(tree).props.selected.row, 2);
  axis(tree, "-row").props.onChange({ target: { value: "" } }); tree = render();
  assert.equal(axis(tree, "-row").props.value, ""); assert.equal(axis(tree, "-column").props.value, "1"); assert.equal(canvas(tree).props.selected, null);
  axis(tree, "-row").props.onChange({ target: { value: "7" } }); tree = render(); assert.equal(canvas(tree).props.selected.row, 6);
  axis(tree, "-column").props.onChange({ target: { value: "9" } }); tree = render();
  assert.equal(axis(tree, "-column").props.value, "9"); assert.equal(canvas(tree).props.selected, null);
  axis(tree, "-column").props.onChange({ target: { value: "" } }); tree = render();
  assert.equal(axis(tree, "-column").props.value, ""); assert.equal(axis(tree, "-row").props.value, "7");
  axis(tree, "-column").props.onChange({ target: { value: "4" } }); tree = render();
  assert.equal(canvas(tree).props.selected.row, 6); assert.equal(canvas(tree).props.selected.column, 3);
  canvas(tree).props.select({ row: 1, column: 5 }); tree = render();
  assert.equal(axis(tree, "-row").props.value, "2"); assert.equal(axis(tree, "-column").props.value, "6");
  harness.dispose();
});

test("acquisition pilot action shows dev/cache/unknown QA and retires canceled or replaced loads", async () => {
  const preview = fixture(), tile = "NEON_D06_KONZ_DP3_706000_4336000";
  preview.data_kind = "provider-files"; preview.source.month = "2024-09"; preview.source.acquisition_run = "2024_KONZ_10"; preview.source.tile = tile;
  preview.source.files.forEach(item => { item.name = `${tile}_${item.kind.toUpperCase()}.tif`; }); preview.grid.bounds = [706000, 4336000, 707000, 4337000];
  const receipt = { format: "kfm-neon-relay-pilot-v1", preview, generatedAt: "2026-11-23T23:00:00Z", cache: { state: "stale", at: "2026-11-23T22:00:00Z" }, review: { status: "pending", scientific_accuracy_verified: false, source_admitted: false, canopy_native_max_m: 83.41000366210938, canopy_native_cells_above_50m: 5, surface_minus_ground_native_max_m: 32.5, notes: ["Accuracy and vertical reference remain unverified."] } };
  let finish, reads = 0;
  const harness = await componentHarness("app/neon-lidar-panel.tsx", { "./neon-lidar-preview": helpers, "./neon-lidar-pilot-client": { ...pilotClient, readNeonLidarPilot: () => { reads++; return new Promise(resolve => { finish = resolve; }); } }, "./acquisition-client": client, "./neon-lidar-panel.module.css": { default: new Proxy({}, { get: (_, key) => key }) } });
  const render = () => { const tree = harness.render(() => { const workspace = harness.exports.NeonLidarPanel(); return harness.exports.NeonLidarWorkspace(workspace.props); }); harness.commit(); return tree; };
  const load = tree => findNode(tree, node => node.type === "button" && node.props.children === "Load Konza Prairie pilot").props.onClick();
  let tree = render(); assert.equal(reads, 0); load(tree); tree = render(); finish(receipt); await settle(); tree = render();
  assert.ok(findNode(tree, node => node.type === "time" && node.props.dateTime === receipt.cache.at));
  assert.ok(findNode(tree, node => node.type === "p" && Array.isArray(node.props.children) && node.props.children.some(text => typeof text === "string" && /independent accuracy and vertical reference are unverified/.test(text))));
  assert.ok(findNode(tree, node => node.type === "p" && Array.isArray(node.props.children) && node.props.children.some(text => typeof text === "string" && /cached preview is stale/.test(text))));
  load(tree); tree = render(); const priorFinish = finish;
  findNode(tree, node => node.type === "input" && node.props.type === "file").props.onChange({ target: { files: [{ size: 10000, text: async () => JSON.stringify(fixture()) }], value: "local.json" } });
  await settle(); priorFinish(receipt); await settle(); tree = render();
  assert.ok(findNode(tree, node => node.type === "strong" && node.props.children === "Synthetic test grid · not observed terrain."));
  assert.equal(findNode(tree, node => node.type === "time" && node.props.dateTime === receipt.cache.at), undefined);
  load(tree); tree = render(); findNode(tree, node => node.type === "button" && node.props.children === "Cancel local read").props.onClick(); finish(receipt); await settle(); tree = render();
  assert.equal(findNode(tree, node => node.type === "input" && node.props.type === "number"), undefined); harness.dispose();
});


test("embedded Science raster requires click or tap, retains keyboard input and ignores repeated cell selection", async () => {
  const imports = { "./neon-lidar-preview": helpers, "./neon-lidar-pilot-client": pilotClient, "./acquisition-client": client, "./neon-lidar-panel.module.css": { default: new Proxy({}, { get: (_, key) => key }) } };
  const harness = await componentHarness("app/neon-lidar-panel.tsx", imports);
  const render = () => { const tree = harness.render(() => { const controller = harness.exports.useNeonLidarPreview(); return harness.exports.NeonLidarWorkspace({ controller, embedded: true }); }); harness.commit(); return tree; };
  let tree = render(); findNode(tree, node => node.type === "input" && node.props.type === "file").props.onChange({ target: { files: [{ size: 1000, text: async () => JSON.stringify(fixture()) }], value: "fixture.json" } }); await settle(); tree = render();
  const canvas = findNode(tree, node => typeof node.type === "function" && node.type.name === "GridCanvas"); assert.equal(canvas.props.hover, false);
  assert.ok(findNode(tree, node => node.type === "input" && node.props.type === "number"));
  const drawing = await componentHarness("app/neon-lidar-panel.tsx", imports, {}, "\nexports.GridCanvas=GridCanvas;"); let selected = null;
  const props = { ...canvas.props, select: next => { selected = next; } };
  const grid = drawing.render(drawing.exports.GridCanvas, props), element = findNode(grid, node => node.type === "canvas");
  const event = { pointerType: "mouse", clientX: 125, clientY: 250, currentTarget: { getBoundingClientRect: () => ({ left: 0, top: 0, width: 1000, height: 1000 }) } };
  element.props.onPointerMove(event); assert.equal(selected, null); element.props.onPointerDown(event); assert.equal(selected.row, 2); assert.equal(selected.column, 1);
  harness.dispose(); drawing.dispose();
});

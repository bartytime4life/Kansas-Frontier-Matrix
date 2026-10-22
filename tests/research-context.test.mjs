import assert from "node:assert/strict";
import test from "node:test";
import { readFile } from "node:fs/promises";
import ts from "typescript";

const urls = new Map();
async function moduleUrl(name) {
  if (urls.has(name)) return urls.get(name);
  let js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  js = js.replaceAll('from "sunrise-sunset-js"', `from ${JSON.stringify(import.meta.resolve("sunrise-sunset-js"))}`)
    .replaceAll('from "polygon-clipping"', `from ${JSON.stringify(new URL("../node_modules/polygon-clipping/dist/polygon-clipping.esm.js", import.meta.url).href)}`);
  for (const [, dependency] of [...js.matchAll(/from "\.\/([a-z-]+)"/g)]) js = js.replaceAll(`from "./${dependency}"`, `from "${await moduleUrl(dependency)}"`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  urls.set(name, url);
  return url;
}
const county = await import(await moduleUrl("research-county"));
const r = await import(await moduleUrl("research-context"));
const catalog = await import(await moduleUrl("layer-workspaces"));
const saved = await import(await moduleUrl("saved-workspaces"));
const model = await import(await moduleUrl("workspace-model"));
const storage = await import(await moduleUrl("workspace-storage"));
const date = "2026-10-06T00:00:00Z";
const record = (featureId, coordinates = [-98, 38], patch = {}) => ({ kind: "provider", sourceId: "test-provider", featureId, title: `Point ${featureId}`,
  coordinates, sourceTitle: "Provider test source", sourceUrl: "https://example.org/records", sourceTime: "Observed 2026-10-05", retrievedAt: date,
  evidenceLabel: "EXTERNAL_CONTEXT_ONLY", limitation: "Partial loaded response; no KFM admission.", ...patch });
const anchor = record("anchor");
const coverage = [{ sourceId: "test-provider", title: "Provider test source", state: "partial", retrievedAt: date, limitation: "Loaded points only; response is partial." }];
const context = (records = [record("near", [-98, 38.1])]) => ({ version: 1, capturedAt: date, anchor, radiusMiles: 25, mapTime: "Present",
  ...r.nearbyResearch(anchor, records, 25), coverage });
const snapshot = { id: "research-test", createdAt: date, area: { kind: "viewport", label: "Kansas" },
  camera: { center: [-98.38, 38.48], zoom: 5.4, pitch: 0, bearing: 0 }, representation: "2D", projection: "mercator", basemap: "standard",
  committedTime: { start: 2026, end: 2026, label: "2026", mode: "instant" }, visibleLayers: [], selection: null, evidenceRefs: [],
  inspectableFeatureIds: [], inspectableRecordCount: 0, sourceBackedCount: 0, boundedCount: 0, policy: model.policyDecisionFromEvidenceState("MISSING_EVIDENCE") };
const workspace = { id: "workspace-test", name: "Research", savedAt: date, view: { center: [-98, 38], zoom: 5, bearing: 0, pitch: 0 },
  locationCameraRedacted: false, visibility: {}, opacity: {}, layerOrder: [], year: 2026, basemap: "standard", projection: "mercator", selection: null,
  report: { title: "Research", scope: "VIEWPORT", detail: "STANDARD", layerIds: [], sections: {}, query: "" } };

test("catalog filters compose without mutating selections; display and holds remain distinct", () => {
  const statuses = Object.freeze([
    Object.freeze({ selected: false, held: false, state: "ready", canDisplay: true }),
    Object.freeze({ selected: true, held: false, state: "ready", canDisplay: true }),
    Object.freeze({ selected: true, held: true, state: "ready", canDisplay: false }),
    Object.freeze({ selected: true, held: false, state: "error", canDisplay: false }),
    Object.freeze({ selected: true, held: false, state: "partial", canDisplay: true }),
  ]);
  const before = JSON.stringify(statuses);
  assert.equal(statuses.filter(s => catalog.catalogFilterMatches("all", s)).length, 5);
  assert.equal(statuses.filter(s => catalog.catalogFilterMatches("selected", s)).length, 4);
  assert.equal(statuses.filter(s => catalog.catalogFilterMatches("attention", s)).length, 3);
  assert.deepEqual(statuses.map(catalog.catalogDisplayStatus), ["Not selected", "Displayed", "Held", "Unavailable", "Displayed · partial response"]);
  assert.equal(catalog.catalogDisplayStatus({ ...statuses[1], state: "loading" }), "Loading");
  assert.equal(catalog.catalogDisplayStatus({ ...statuses[1], canDisplay: false }), "Selected · not displayed");
  assert.equal(JSON.stringify(statuses), before);
});

test("an existing dossier anchor survives other selections until explicitly replaced", () => {
  const next = record("other", [-99, 39]);
  assert.equal(r.chooseResearchAnchor(anchor, next), anchor);
  assert.equal(r.chooseResearchAnchor(anchor, null), anchor);
  assert.equal(r.chooseResearchAnchor(anchor, next, true), next);
  assert.equal(r.chooseResearchAnchor(null, next), next);
  assert.equal(r.chooseResearchAnchor(anchor, { ...next, coordinates: [NaN, 38] }, true), null);
});

test("source eligibility excludes holds, loading, wrong source/day, missing coordinates and non-points", () => {
  const source = { id: "test-provider", title: "Test points", url: "https://example.org/", time: "2026", limitation: "Context only" };
  const point = { type: "Feature", id: "1", geometry: { type: "Point", coordinates: [-98, 38, 123] }, properties: { name: "Supplied point" } };
  const payload = { feed: source.id, state: "partial", retrievedAt: date, sourceDay: "2026-10-05", data: { type: "FeatureCollection", features: [point,
    { ...point, id: "missing", geometry: null }, { ...point, id: "bad", geometry: { type: "Point", coordinates: [999, 38] } },
    { ...point, id: "area", geometry: { type: "Polygon", coordinates: [[[-98, 38], [-98, 39], [-97, 38], [-98, 38]]] } },
    { ...point, id: undefined }, { ...point, id: "line", geometry: { type: "LineString", coordinates: [[-98, 38], [-98, 39]] } },
  ] } };
  const points = r.providerResearchPoints(source, payload, true, "2026-10-05");
  assert.equal(points.length, 1);
  assert.deepEqual(points[0].coordinates, [-98, 38]);
  assert.equal(points[0].evidenceLabel, "EXTERNAL_CONTEXT_ONLY");
  for (const [body, eligible, day] of [[payload, false, "2026-10-05"], [{ ...payload, state: "loading" }, true, "2026-10-05"],
    [{ ...payload, feed: "wrong" }, true, "2026-10-05"], [payload, true, "2026-10-04"]]) {
    assert.deepEqual(r.providerResearchPoints(source, body, eligible, day), []);
  }
});

test("canceled and stale inventory reads cannot overwrite newer loaded data", async () => {
  const abort = new AbortController();
  let resolve;
  const old = new Promise(done => { resolve = done; });
  const accepted = [];
  const pending = r.readResearchInventory(() => old, abort.signal, value => accepted.push(value));
  abort.abort();
  await r.readResearchInventory(() => Promise.resolve("new"), new AbortController().signal, value => accepted.push(value));
  resolve("old"); await pending;
  await r.readResearchInventory(() => Promise.reject(new Error("unavailable")), new AbortController().signal, value => accepted.push(value));
  assert.deepEqual(accepted, ["new"]);
});

test("radius boundaries are inclusive, missing coordinates skipped, and no anchor counted", () => {
  const degrees = 25 / 3958.8 * 180 / Math.PI;
  const candidates = [anchor, record("boundary", [-98, 38 + degrees]), record("outside", [-98, 38 + degrees + 0.00001]),
    record("invalid", [null, 38]), record("nan", [NaN, 38])];
  const result = r.nearbyResearch(anchor, candidates, 25);
  assert.deepEqual(result.records.map(row => row.featureId), ["boundary"]);
  assert.equal(result.total, 1);
  assert.ok(r.researchDistanceMiles([0, 0], [180, 0]) > 12000);
  assert.deepEqual(r.nearbyResearch(anchor, [], 25), { records: [], total: 0 });
});

test("source identities deduplicate, ties are deterministic, nearest 50 retain the full count", () => {
  const records = Array.from({ length: 65 }, (_, i) => record(`id-${i}`, [-98, 38 + i / 1000]));
  records.push({ ...records[0], title: "older", retrievedAt: "2026-10-01T00:00:00Z" });
  records.push({ ...records[0], title: "same-time alternative" });
  records.push({ ...records[0], sourceId: "another-source" });
  const forward = r.nearbyResearch(anchor, records, 25);
  const reverse = r.nearbyResearch(anchor, [...records].reverse(), 25);
  assert.deepEqual(forward, reverse);
  assert.equal(forward.total, 66); assert.equal(forward.records.length, 50);
  assert.equal(new Set(forward.records.map(r.researchIdentity)).size, 50);
  assert.ok(forward.records.every((row, i) => !i || row.distanceMiles >= forward.records[i - 1].distanceMiles));
});

test("optional context validates bounds and rejects forged distances, extra geometry and provider evidence", () => {
  assert.equal(r.validResearchContext(context()), true);
  for (const value of [{ ...context(), radiusMiles: 10 }, { ...context(), total: -1 }, { ...context(), geometry: { coordinates: [1, 2] } },
    { ...context(), records: [{ ...context().records[0], distanceMiles: 0 }] }, { ...context(), records: [context().records[0], context().records[0]] },
    { ...context(), anchor: { ...anchor, sourceUrl: "javascript:alert(1)" } }, { ...context(), anchor: { ...anchor, evidenceLabel: "RELEASED" } },
    { ...context(), anchor: { ...anchor, kind: "registry", evidenceLabel: "RELEASED" } }, { ...context(), anchor: { ...anchor, distanceMiles: { coordinates: [1, 2] } } },
    { ...context(), anchor: { ...anchor, distanceMiles: 1 } }]) {
    assert.equal(r.validResearchContext(value), false);
  }
});

test("saved settings contain no cached results, copy their anchor and retain missing-source identities", () => {
  const original = structuredClone(context());
  const settings = r.persistableResearch(original, false, true);
  assert.deepEqual(settings.records, []); assert.equal(settings.total, 0);
  assert.equal(settings.coverage[0].sourceId, "test-provider");
  original.anchor.title = "changed later";
  assert.equal(settings.anchor.title, anchor.title);
  assert.equal(saved.validSavedWorkspaceRecord({ ...workspace, researchContext: settings }), true);
  assert.equal(saved.validSavedWorkspaceRecord(workspace), true);
  assert.equal(saved.validSavedWorkspaceRecord({ ...workspace, locationCameraRedacted: true, researchContext: settings }), false);
  assert.equal(saved.validSavedWorkspaceRecord({ ...workspace, locationCameraRedacted: undefined, researchContext: settings }), false);
});

test("storage refusal or quota failure cannot be reported as a successful save", () => {
  assert.equal(saved.writeSavedWorkspaceList({ setItem() { throw new Error("quota"); } }, "test", [workspace]), false);
  const writes = [];
  assert.equal(saved.writeSavedWorkspaceList({ setItem: (...args) => writes.push(args) }, "test", [workspace]), true);
  assert.equal(saved.parseSavedWorkspaceList(writes[0][1], 12).records.length, 1);
  assert.equal(saved.writeSavedWorkspaceList({ setItem() { assert.fail("invalid write"); } }, "test", [{ ...workspace, researchContext: { version: 2 } }]), false);
});

test("reports keep a dated detached context separate from evidence, while old drafts still read", () => {
  const captured = context();
  const report = model.createReportDraft(snapshot, [], undefined, captured);
  assert.equal(storage.validReportDraft(report), true);
  assert.deepEqual(report.includedEvidenceIds, []);
  assert.equal(report.researchContext.capturedAt, date);
  assert.notEqual(report.researchContext, captured);
  assert.equal(storage.validReportDraft(model.createReportDraft(snapshot, [])), true);
});

test("location-redacted workspaces and reports omit the entire dossier", () => {
  const withheld = { ...snapshot, camera: { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", bearing: "WITHHELD", pitch: "WITHHELD" } };
  assert.equal(r.persistableResearch(context(), true), undefined);
  const report = model.createReportDraft(withheld, [], undefined, context());
  assert.equal(report.researchContext, undefined);
  assert.equal(storage.validReportDraft(report), true);
  assert.equal(storage.validReportDraft({ ...report, researchContext: context() }), false);
});

test("exports keep source links, observation versus retrieval time, roles and coverage limits", () => {
  const text = r.researchMarkdown(context([record("html", [-98, 38.1], { title: '<img src=x> [fake](https://evil.example)' })]));
  assert.match(text, /(?:^|[\s(])https:\/\/example\.org\/records(?:$|[\s)])/);
  assert.match(text, /Source time: Observed 2026-10-05/);
  assert.match(text, /Retrieved: 2026-10-06T00:00:00Z/);
  assert.match(text, /provider point/); assert.match(text, /partial/);
  assert.match(text, /Provider context is not admitted KFM evidence/);
  assert.doesNotMatch(text, /<img|\[fake\]\(/);
});

// Synthetic Kansas polygon; not an Ellsworth County boundary fixture.
const box = [[-99, 37], [-97, 37], [-97, 39], [-99, 39], [-99, 37]];
const hole = [[-98.5, 37.5], [-97.5, 37.5], [-97.5, 38.5], [-98.5, 38.5], [-98.5, 37.5]];
const countyFeature = { type: "Feature", geometry: { type: "Polygon", coordinates: [box, hole] },
  properties: { geoid: "20053", featureId: "us-census-county-20053", name: "Synthetic county", vintage: "2020" } };
const countyPayload = (features = [countyFeature]) => ({ feed: "census-counties", state: "ready", data: { type: "FeatureCollection", features } });
const scope = () => county.researchCounties(countyPayload(), "ready")[0];

test("county membership respects holes, edges and disjoint multipolygons without changing source roles", () => {
  const rows = [record("inside", [-98.8, 38]), record("hole", [-98, 38]), record("edge", [-99, 38]), record("outside", [-96, 38]), record("hole-edge", [-98.5, 38])];
  assert.deepEqual(county.countyResearch(scope(), rows, countyPayload(), "ready").records.map(r => r.featureId), ["inside", "edge"]);
  const multi = { ...countyFeature, geometry: { type: "MultiPolygon", coordinates: [[box, hole], [[[-96, 37], [-95, 37], [-95, 38], [-96, 38], [-96, 37]]]] } };
  assert.equal(county.countyResearch(scope(), [record("island", [-95.5, 37.5])], countyPayload([multi]), "ready").records[0].evidenceLabel, "EXTERNAL_CONTEXT_ONLY");
});

test("missing, malformed, duplicate and wrong-edition boundaries hold the county scope closed", () => {
  for (const [payload, state] of [[undefined, "loading"], [countyPayload(), "error"], [{ ...countyPayload(), feed: "other" }, "ready"],
    [countyPayload([countyFeature, countyFeature]), "ready"], [countyPayload([null]), "ready"],
    [countyPayload([{ ...countyFeature, geometry: { type: "Polygon", coordinates: [null] } }]), "ready"],
    [countyPayload([{ ...countyFeature, geometry: { type: "MultiPolygon" } }]), "ready"], [countyPayload([{ ...countyFeature, properties: { ...countyFeature.properties, vintage: "2010" } }]), "ready"],
    [countyPayload([{ ...countyFeature, geometry: { type: "Polygon", coordinates: [box.slice(0, -1)] } }]), "ready"]]) {
    const result = county.countyResearch(scope(), [record("inside", [-98.8, 38])], payload, state);
    assert.equal(result.county.state, "unavailable"); assert.deepEqual(result.records, []);
  }
});

test("county filtering precedes nearest-50 truncation and never substitutes a radius for a hold", () => {
  const rows = Array.from({ length: 60 }, (_, i) => record(`outside-${i}`, [-98, 38 + i / 10000]));
  rows.push(record("inside", [-98.8, 38]));
  const scoped = county.countyResearch(scope(), rows, countyPayload(), "ready");
  assert.deepEqual(r.nearbyResearch(anchor, scoped.records, 100).records.map(row => row.featureId), ["inside"]);
  assert.equal(county.countyResearch(null, rows, undefined, "loading").records, rows);
});

test("county scope survives settings and reports; unavailable scopes cannot claim records", () => {
  const captured = { ...context(), county: scope() };
  assert.equal(r.validResearchContext(captured), true);
  const settings = r.persistableResearch(captured, false, true);
  assert.deepEqual(settings.county, scope()); assert.deepEqual(settings.records, []);
  assert.equal(saved.validSavedWorkspaceRecord({ ...workspace, researchContext: settings }), true);
  const report = model.createReportDraft(snapshot, [], undefined, captured);
  assert.equal(storage.validReportDraft(report), true);
  assert.match(r.researchMarkdown(report.researchContext), /GEOID 20053.*2020 Census boundary/);
  assert.deepEqual(report.includedEvidenceIds, []);
  assert.equal(r.validResearchContext({ ...captured, county: { ...scope(), geoid: 20053 } }), false);
  assert.equal(r.validResearchContext({ ...captured, county: { ...scope(), state: "unavailable" } }), false);
  assert.equal(r.persistableResearch(captured, true), undefined);
});

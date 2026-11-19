import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import * as jsxRuntime from "react/jsx-runtime";
import { renderToStaticMarkup } from "react-dom/server";

const recordSource = await readFile(new URL("../app/trail-place-record.ts", import.meta.url), "utf8");
const recordJavascript = ts.transpileModule(recordSource, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const recordModule = `data:text/javascript;base64,${Buffer.from(recordJavascript).toString("base64")}`;
const { safeTrailPlaceRecordUrl } = await import(recordModule);
const source = await readFile(new URL("../app/evidence-drawer-data.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "evidence-drawer-data.ts",
}).outputText.replace('"./trail-place-record"', JSON.stringify(recordModule));
const { drawerArtifactAttributes, parseUsgsStageDetail } = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

test("artifact fields expose allowlisted provider data but omit arbitrary and sensitive keys", () => {
  const fields = drawerArtifactAttributes("census-counties", { geoid: "20139", population: 0, housingUnits: 12, privateNote: "withhold", latitude: 38.7 });
  assert.deepEqual(fields, [
    { label: "County GEOID", value: "20139" },
    { label: "Population count", value: "0" },
    { label: "Housing units", value: "12" },
  ]);
  assert.deepEqual(drawerArtifactAttributes("usgs-wbd-watersheds", { arbitrary: "unsafe" }), []);
  assert.deepEqual(drawerArtifactAttributes("basemap", { name: "Creek", secret: "withhold" }), [{ label: "Name", value: "Creek" }]);
});

test("trail-site links accept only bounded HTTPS NPS and partner record URLs", () => {
  for (const url of ["https://www.nps.gov/places/neosho-crossing.htm", "https://nps.gov/places/fort.htm?view=history#visit", "https://www.kshs.org/kansapedia/fort", "https://kansasmemory.org/item/123"]) {
    assert.equal(safeTrailPlaceRecordUrl(` ${url} `), url);
    assert.deepEqual(drawerArtifactAttributes("nps-trail-places", { recordUrl: url }), [{ label: "NPS or partner page", value: url, href: url }]);
  }
  for (const value of [undefined, null, 12, "", "javascript:alert(1)", "http://www.nps.gov/places/fort.htm", "//www.nps.gov/places/fort.htm", "https://www.nps.gov.evil.example/fort", "https://www.nps.gov@evil.example/fort", "https://owner:secret@www.nps.gov/fort", "https://www.nps.gov:444/fort", "https://www.nps.gov/places/\nfort", "https://www.nps.gov/places/" + "x".repeat(240)]) {
    assert.equal(safeTrailPlaceRecordUrl(value), null, String(value));
    assert.deepEqual(drawerArtifactAttributes("nps-trail-places", { recordUrl: value }), [], String(value));
  }
  // Record properties cannot inject an arbitrary link into another drawer field.
  assert.deepEqual(drawerArtifactAttributes("basemap", { name: "Creek", href: "https://evil.example/" }), [{ label: "Name", value: "Creek" }]);
});

test("trail-site stories retain the adapter's 900-character bound without widening other fields", () => {
  const history = "An NPS account of the crossing and its history. ".repeat(16).trim();
  assert.ok(history.length > 240 && history.length < 900);
  assert.deepEqual(drawerArtifactAttributes("nps-trail-places", { history }), [{ label: "Why it matters", value: history }]);
  assert.equal(drawerArtifactAttributes("nps-trail-places", { history: "h".repeat(950) })[0].value.length, 900);
  assert.equal(drawerArtifactAttributes("nps-trail-places", { otherName: "n".repeat(950) })[0].value.length, 240);
  assert.equal(drawerArtifactAttributes("basemap", { name: "n".repeat(950) })[0].value.length, 240);
});

test("the actual drawer JSX renders a trail-site record link and the full bounded story", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const tree = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
  let drawerList;
  const visit = node => {
    if (ts.isJsxElement(node) && node.openingElement.tagName.getText(tree) === "dl"
      && node.openingElement.attributes.properties.some(attribute => ts.isJsxAttribute(attribute)
        && attribute.name.getText(tree) === "className" && attribute.initializer
        && ts.isStringLiteral(attribute.initializer) && attribute.initializer.text === "drawer-attribute-list")) drawerList = node.getText(tree);
    ts.forEachChild(node, visit);
  };
  visit(tree);
  assert.ok(drawerList, "the production drawer attribute list exists");
  const compiled = ts.transpileModule(`export const render = (selectedArtifactAttributes) => (${drawerList});`, {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX },
  }).outputText;
  const exports = {};
  new Function("exports", "require", compiled)(exports, name => {
    assert.equal(name, "react/jsx-runtime");
    return jsxRuntime;
  });
  const url = "https://www.nps.gov/places/neosho-crossing.htm";
  const history = "The route crossed the river here. ".repeat(16).trim();
  const markup = renderToStaticMarkup(exports.render(drawerArtifactAttributes("nps-trail-places", { recordUrl: url, history })));
  assert.ok(markup.includes(`<a href="${url}" target="_blank" rel="noreferrer">`), "the selected record URL is an actual link");
  assert.ok(markup.includes(history), "the full story reaches the rendered drawer");
  const unsafeMarkup = renderToStaticMarkup(exports.render(drawerArtifactAttributes("nps-trail-places", { recordUrl: "javascript:alert(1)", history: "A public historic site." })));
  assert.doesNotMatch(unsafeMarkup, /<a |javascript:/);
});

const stageResponse = {
  kind: "usgs-streamflow-bundle", mode: "station", parameterCode: "00065",
  queryStart: "2026-09-16T00:00:00.000Z", queryEnd: "2026-09-23T00:00:00.000Z", retrievedAt: "2026-09-23T00:01:00.000Z",
  partial: false, truncated: false,
  stations: [{ stationId: "USGS-06911900", agencyCode: "USGS", name: "DRAGOON C NR BURLINGAME, KS", county: "Osage County", huc: "10290101", drainageArea: 114, contributingDrainageArea: 114, siteTypeCode: "ST", latitude: 38.7, longitude: -95.8 }],
  observations: [
    { stationId: "USGS-06911900", parameterCode: "00065", observedAt: "2026-09-20T00:00:00.000Z", value: 3.25, unit: "ft", approvalStatus: "Provisional", qualifiers: [] },
    { stationId: "USGS-06911900", parameterCode: "00065", observedAt: "2026-09-21T00:00:00.000Z", value: null, unit: "ft", approvalStatus: null, qualifiers: [] },
  ],
};

test("stage detail keeps station metadata and dated history when the selected discharge frame is empty", () => {
  const detail = parseUsgsStageDetail(stageResponse, "USGS-06911900");
  assert.equal(detail.county, "Osage County");
  assert.equal(detail.drainageArea, 114);
  assert.equal(detail.observationCount, 2);
  assert.equal(detail.latest.value, 3.25);
  assert.equal(detail.recent[0].value, null);
});

test("stage detail rejects a different station or discharge masquerading as gauge height", () => {
  assert.throws(() => parseUsgsStageDetail(stageResponse, "USGS-06911901"));
  assert.throws(() => parseUsgsStageDetail({ ...stageResponse, parameterCode: "00060" }, "USGS-06911900"));
  assert.throws(() => parseUsgsStageDetail({ ...stageResponse, observations: [{ ...stageResponse.observations[0], stationId: "USGS-06911901" }] }, "USGS-06911900"));
});

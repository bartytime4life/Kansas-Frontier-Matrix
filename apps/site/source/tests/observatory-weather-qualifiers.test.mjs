import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import vm from "node:vm";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let source = await readFile(file, "utf8");
  for (const match of [...source.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    source = source.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  }
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  const url = `data:text/javascript;base64,${Buffer.from(code).toString("base64")}`;
  modules.set(file, url); return url;
}

// Import the real route with transport denied, then compile the real selected-
// record section and its formatter. This exercises its exact JSX without WebGL.
const priorFetch = globalThis.fetch;
let weather;
globalThis.fetch = async () => { throw new Error("No transport during fixture import"); };
try { weather = await import(await moduleUrl("app/api/event-atlas/weather/route.ts")); }
finally { globalThis.fetch = priorFetch; }
const source = await readFile("app/observatory/workspace.tsx", "utf8");
const ast = ts.createSourceFile("workspace.tsx", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
const sections = [], formatters = [];
function visit(node) {
  if (ts.isFunctionDeclaration(node) && node.name?.text === "weatherReadingText") formatters.push(node.getText(ast));
  if (ts.isJsxElement(node) && node.openingElement.attributes.properties.some(attribute => ts.isJsxAttribute(attribute)
    && attribute.name.getText(ast) === "className" && attribute.initializer?.getText(ast) === '"event-feature-values"')) sections.push(node.getText(ast));
  ts.forEachChild(node, visit);
}
visit(ast);
assert.equal(sections.length, 1); assert.equal(formatters.length, 1);
const code = ts.transpileModule(`${formatters[0]}\nexport const Inspector = ({ properties, track = "weather" }) => {
  const inspectedFeature = { properties }, chosen = { id: track }; return (${sections[0]});
};`, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText;
const exports = {}, jsx = (type, props) => ({ type, props });
vm.runInNewContext(code, { exports, require(name) {
  assert.equal(name, "react/jsx-runtime"); return { jsx, jsxs: jsx };
} });
const textOf = node => typeof node === "string" || typeof node === "number" ? String(node)
  : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g, " ").trim() : "";
function fields(properties, track) {
  const result = new Map();
  function visit(node) {
    if (!node || typeof node !== "object") return;
    const children = [node.props?.children].flat(Infinity);
    if (node.type === "div" && children.some(child => child?.type === "dt")) result.set(textOf(children.find(child => child?.type === "dt")), textOf(children.find(child => child?.type === "dd")));
    children.forEach(visit);
  }
  visit(exports.Inspector({ properties, track })); return result;
}
const DAY = "1900-05-19", STATION = "USC00143527";
const row = patch => ({ DATE: DAY, STATION, NAME: "SYNTHETIC QUALIFIER CHECK", LATITUDE: "38.85", LONGITUDE: "-99.3",
  TMAX: "70", TMAX_ATTRIBUTES: ",,0,0700", TMIN: "44", TMIN_ATTRIBUTES: ",,0,0700",
  PRCP: "0.00", PRCP_ATTRIBUTES: ",,0,0700", SNOW: "0.0", SNOW_ATTRIBUTES: ",,0,0700", SNWD: "0", SNWD_ATTRIBUTES: ",,0,0700", ...patch });
async function fixture(input) {
  const originalFetch = globalThis.fetch, original = JSON.stringify(input), requests = [];
  globalThis.fetch = async inputUrl => {
    const url = new URL(inputUrl); requests.push(url);
    assert.equal(url.origin, "https://www.ncei.noaa.gov"); assert.equal(url.pathname, "/access/services/data/v1");
    for (const [key, expected] of Object.entries({ dataset: "daily-summaries", startDate: DAY, endDate: DAY, units: "standard", includeAttributes: "1", dataTypes: "TMAX,TMIN,PRCP,SNOW,SNWD" })) assert.equal(url.searchParams.get(key), expected);
    assert.ok(url.searchParams.get("stations").split(",").includes(STATION));
    return Response.json([input]);
  };
  try {
    const response = await weather.GET(new Request(`https://synthetic.test/api/event-atlas/weather?day=${DAY}`));
    assert.equal(response.status, 200); assert.equal(requests.length, 1, "every fixture must reach the denied-by-default provider stub exactly once");
    const payload = await response.json(); assert.equal(payload.data.features.length, 1); assert.equal(payload.day, DAY);
    const properties = payload.data.features[0].properties;
    assert.equal(properties.station, STATION); assert.equal(properties.day, DAY); assert.equal(properties.source, requests[0].href);
    assert.equal(JSON.stringify(input), original, "normalization must not mutate the provider row");
    return { payload, properties, displayed: fields(properties) };
  } finally { globalThis.fetch = originalFetch; }
}
const AMOUNTS = [["PRCP", "precipitationInches", "precipitationAttributes", "Daily rain · in"], ["SNOW", "snowfallInches", "snowAttributes", "Daily snowfall · in"], ["SNWD", "snowDepthInches", "snowDepthAttributes", "Snow depth · in"]];

test("NOAA trace amounts survive the actual route and inspector without becoming measured zero", async () => {
  const input = row({ PRCP_ATTRIBUTES: "T,,0,0700", SNOW_ATTRIBUTES: "T,,0,0700", SNWD_ATTRIBUTES: "T,,0,0700" });
  const f = await fixture(input);
  for (const [code, key, attribute, label] of AMOUNTS) {
    assert.equal(f.properties[key], 0); assert.equal(f.properties[`${key}State`], "trace");
    assert.equal(f.properties[`${key}RawValue`], input[code]); assert.equal(f.properties[attribute], input[`${code}_ATTRIBUTES`]);
    assert.equal(f.displayed.get(label), "Trace (below reporting resolution)");
  }
  assert.match(f.payload.message, /Trace amounts are qualified, not measured zeros/);
});

test("NOAA presumed-zero missing amounts are withheld and retain their original values and flags", async () => {
  const input = row({ PRCP_ATTRIBUTES: "P,,0,0700", SNOW_ATTRIBUTES: "P,,0,0700", SNWD_ATTRIBUTES: "P,,0,0700" });
  const f = await fixture(input);
  for (const [code, key, attribute, label] of AMOUNTS) {
    assert.equal(f.properties[key], null); assert.equal(f.properties[`${key}State`], "missing-presumed-zero");
    assert.equal(f.properties[`${key}RawValue`], input[code]); assert.equal(f.properties[attribute], input[`${code}_ATTRIBUTES`]);
    assert.equal(f.displayed.get(label), "Withheld (missing presumed zero)");
  }
});

test("the actual inspector retains all five qualified rows when MapLibre omits null-valued properties", async () => {
  const f = await fixture(row({ TMAX_ATTRIBUTES: ",X,0,0700", TMIN: "-9999", PRCP_ATTRIBUTES: "P,,0,0700", SNOW_ATTRIBUTES: ",X,0,0700", SNWD: undefined }));
  const renderedProperties = Object.fromEntries(Object.entries(f.properties).filter(([, value]) => value !== null));
  for (const key of ["maximumF", "minimumF", "precipitationInches", "snowfallInches", "snowDepthInches"]) assert.equal(Object.hasOwn(renderedProperties, key), false);
  const displayed = fields(renderedProperties);
  assert.equal(displayed.get("Daily max · °F"), "Withheld (failed provider quality check)");
  assert.equal(displayed.get("Daily min · °F"), "Withheld (missing)");
  assert.equal(displayed.get("Daily rain · in"), "Withheld (missing presumed zero)");
  assert.equal(displayed.get("Daily snowfall · in"), "Withheld (failed provider quality check)");
  assert.equal(displayed.get("Snow depth · in"), "Withheld (missing)");
});

test("NOAA H and I precipitation zeros remain unresolved while H temperatures retain their hourly basis", async () => {
  for (const [flag, state, text] of [["H", "precipitation-noted", "Withheld (precipitation noted; amount unresolved)"], ["I", "precipitation-not-reported", "Withheld (no precipitation report)"]]) {
    const f = await fixture(row({ PRCP_ATTRIBUTES: `${flag},,0,0700`, TMAX_ATTRIBUTES: "H,,0,0700", TMIN: "0", TMIN_ATTRIBUTES: "H,,0,0700" }));
    assert.equal(f.properties.precipitationInches, null); assert.equal(f.properties.precipitationInchesState, state);
    assert.equal(f.properties.precipitationInchesRawValue, "0.00"); assert.equal(f.properties.precipitationAttributes, `${flag},,0,0700`);
    assert.equal(f.displayed.get("Daily rain · in"), text);
    const omitted = Object.fromEntries(Object.entries(f.properties).filter(([, value]) => value !== null));
    assert.equal(fields(omitted).get("Daily rain · in"), text);
    assert.equal(f.properties.maximumF, 70); assert.equal(f.properties.maximumFState, "reported"); assert.equal(f.properties.temperatureAttributes, "H,,0,0700");
    assert.equal(f.displayed.get("Daily max · °F"), "70"); assert.equal(f.displayed.get("Daily min · °F"), "0");
    const failed = await fixture(row({ PRCP_ATTRIBUTES: `${flag},X,0,0700` }));
    assert.equal(failed.properties.precipitationInches, null); assert.equal(failed.properties.precipitationInchesState, "quality-withheld");
    assert.equal(failed.displayed.get("Daily rain · in"), "Withheld (failed provider quality check)");
  }
});

test("unflagged genuine zeros and ordinary nonzero weather readings remain visible", async () => {
  const zero = await fixture(row({ TMIN: "0" }));
  for (const [, key, , label] of AMOUNTS) { assert.equal(zero.properties[key], 0); assert.equal(zero.properties[`${key}State`], "reported"); assert.equal(zero.displayed.get(label), "0"); }
  assert.equal(zero.displayed.get("Daily min · °F"), "0"); assert.equal(zero.displayed.get("Daily max · °F"), "70");
  const positive = await fixture(row({ PRCP: "1.25", SNOW: "2.5", SNWD: "4" }));
  for (const [label, value] of [["Daily rain · in", "1.25"], ["Daily snowfall · in", "2.5"], ["Snow depth · in", "4"]]) assert.equal(positive.displayed.get(label), value);
});

test("quality flags and missing sentinels take precedence over trace or presumed-zero qualifiers", async () => {
  const input = row({ TMAX_ATTRIBUTES: ",X,0,0700", TMIN_ATTRIBUTES: ",,6,1800", PRCP_ATTRIBUTES: "T,X,0,0700", SNOW_ATTRIBUTES: "P,X,0,0700", SNWD: "-9999", SNWD_ATTRIBUTES: "T,,0,0700" });
  const f = await fixture(input);
  for (const [, key, , label] of AMOUNTS.slice(0, 2)) { assert.equal(f.properties[key], null); assert.equal(f.properties[`${key}State`], "quality-withheld"); assert.equal(f.displayed.get(label), "Withheld (failed provider quality check)"); }
  assert.equal(f.properties.snowDepthInches, null); assert.equal(f.properties.snowDepthInchesState, "missing"); assert.equal(f.properties.snowDepthInchesRawValue, "-9999"); assert.equal(f.displayed.get("Snow depth · in"), "Withheld (missing)");
  assert.equal(f.displayed.get("Daily max · °F"), "Withheld (failed provider quality check)");
  assert.equal(f.displayed.get("Daily min · °F"), "44"); assert.equal(f.properties.temperatureAttributes, input.TMAX_ATTRIBUTES); assert.equal(f.properties.minimumTemperatureAttributes, input.TMIN_ATTRIBUTES);
});

test("unknown, absent and malformed measurement qualifiers cannot establish a measured zero", async () => {
  for (const attributes of ["Z,,0,0700", undefined, ",", 7, "T,,0,0700,unexpected"]) {
    const f = await fixture(row({ PRCP_ATTRIBUTES: attributes }));
    assert.equal(f.properties.precipitationInches, null); assert.equal(f.properties.precipitationInchesState, "unqualified");
    assert.equal(f.properties.precipitationInchesRawValue, "0.00"); assert.equal(f.displayed.get("Daily rain · in"), "Withheld (measurement qualifier unavailable)");
  }
  const inconsistent = await fixture(row({ TMAX: "0", TMAX_ATTRIBUTES: "T,,0,0700", PRCP: "1", PRCP_ATTRIBUTES: "T,,0,0700" }));
  assert.equal(inconsistent.properties.maximumF, null); assert.equal(inconsistent.properties.precipitationInches, null);
  assert.equal(inconsistent.displayed.get("Daily max · °F"), "Withheld (measurement qualifier unavailable)");
  assert.equal(inconsistent.displayed.get("Daily rain · in"), "Withheld (measurement qualifier unavailable)");
});

test("missing values stay missing while supported non-trace measurement flags retain their source qualifier", async () => {
  const missing = await fixture(row({ PRCP: undefined }));
  assert.equal(missing.properties.precipitationInches, null); assert.equal(missing.properties.precipitationInchesRawValue, null); assert.equal(missing.displayed.get("Daily rain · in"), "Withheld (missing)");
  const ordinary = await fixture(row({ PRCP: "1.25", PRCP_ATTRIBUTES: "A,,0,0700" }));
  assert.equal(ordinary.properties.precipitationInches, 1.25); assert.equal(ordinary.properties.precipitationAttributes, "A,,0,0700"); assert.equal(ordinary.displayed.get("Daily rain · in"), "1.25");
});

test("the actual inspector withholds legacy or unknown scalar qualifiers and preserves other source values", () => {
  assert.equal(fields({ precipitationInches: 0 }).get("Daily rain · in"), "Withheld (measurement qualifier unavailable)");
  assert.equal(fields({ precipitationInches: 0, precipitationInchesState: "future-state" }).get("Daily rain · in"), "Withheld (measurement qualifier unavailable)");
  assert.equal(fields({ precipitationInches: 1, precipitationInchesState: "trace" }).get("Daily rain · in"), "Withheld (inconsistent trace value)");
  assert.equal(fields({ population: 0, housingUnits: null }, "counties").get("Population"), "0");
  assert.equal(fields({ population: 0, housingUnits: null }, "counties").get("Housing units"), "Not supplied");
});

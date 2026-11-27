import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

// Use the real registry and its dependencies, without a browser or upstream requests.
const modules = new Map();
async function moduleUrl(file) {
  const resolved = path.resolve(file);
  if (modules.has(resolved)) return modules.get(resolved);
  let javascript = ts.transpileModule(await readFile(resolved, "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  for (const match of [...javascript.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    javascript = javascript.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(resolved), match[1]) + ".ts"))}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`;
  modules.set(resolved, url);
  return url;
}

const discovery = await import(await moduleUrl("app/research/discovery.ts"));
const { OFFICIAL_CONTEXT_SOURCES } = await import(await moduleUrl("app/live-context.ts"));
const { SOURCE_DOWNLOADS } = await import(await moduleUrl("app/source-downloads.ts"));
const sources = discovery.discoverySources(OFFICIAL_CONTEXT_SOURCES, SOURCE_DOWNLOADS);
const empty = { query: "", domain: "", kind: "", compare: [] };

test("every registered source has a unique identity, an inspectable source and a matching download entry", () => {
  assert.equal(sources.length, OFFICIAL_CONTEXT_SOURCES.length);
  assert.equal(new Set(sources.map(source => source.id)).size, sources.length);
  for (const source of sources) {
    assert.ok(source.sourceHref.startsWith("https://"), source.id);
    assert.ok(source.downloadHref, `${source.id} must join to an existing download`);
    assert.ok(source.downloadLabel);
    for (const field of ["freshness", "cadence", "boundary", "fallback", "attribution"]) assert.ok(source[field]?.trim(), `${source.id}: ${field}`);
    assert.equal(source.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
    const original = OFFICIAL_CONTEXT_SOURCES.find(item => item.id === source.id);
    assert.equal(source.freshness, original.freshness);
    assert.equal(source.boundary, original.boundary);
  }
});

test("search combines provider, subject, time and limitation terms without mutating the source registry", () => {
  const before = JSON.stringify(OFFICIAL_CONTEXT_SOURCES);
  assert.ok(discovery.discoverySearch(sources, { ...empty, query: "USGS streamflow" }).some(source => source.id === "usgs-streamflow"));
  assert.ok(discovery.discoverySearch(sources, { ...empty, query: "2022–2024 thickness" }).some(source => source.id === "kgs-saturated-thickness"));
  const groundwater = discovery.discoverySearch(sources, { ...empty, domain: "Aquifers & groundwater", query: "KGS" });
  assert.ok(groundwater.length > 0);
  assert.ok(groundwater.every(source => source.domain === "Aquifers & groundwater"));
  assert.deepEqual(discovery.discoverySearch(sources, { ...empty, query: "no-such-source-918773" }), []);
  assert.ok(discovery.discoverySearch(sources, { ...empty, kind: "MODEL_CANVAS" }).every(source => source.kind === "MODEL_CANVAS"));
  assert.equal(JSON.stringify(OFFICIAL_CONTEXT_SOURCES), before);
});

test("shared URLs reject unknown IDs and filters, bound query size and deduplicate comparison inputs", () => {
  const ids = sources.slice(0, 4).map(source => source.id);
  const state = discovery.readDiscoveryState(new URLSearchParams({ q: "a".repeat(1000), domain: "unknown", kind: "toString", compare: [ids[0], "not-a-source", ...ids].join(",") }), sources);
  assert.equal(state.query.length, 160);
  assert.equal(state.domain, "");
  assert.equal(state.kind, "");
  assert.deepEqual(state.compare, ids.slice(0, 3));
  assert.equal(discovery.readDiscoveryState(new URLSearchParams({ q: "water\u0000\n" }), sources).query, "water");
});

test("search and comparison state survives URL serialization, including punctuation and non-ASCII source domains", () => {
  const state = { ...empty, query: "water & flood / 2024", domain: sources[0].domain, kind: sources[0].kind, compare: sources.slice(0, 3).map(source => source.id) };
  assert.deepEqual(discovery.readDiscoveryState(discovery.discoveryParams(state), sources), state);
});

test("navigation blocks executable, credential-bearing and cross-origin relative URLs", () => {
  for (const url of ["javascript:alert(1)", "data:text/html,test", "//evil.example/", "/\\evil.example/", "https://user:password@example.org/", "http://example.org/", "file:///etc/passwd"]) assert.equal(discovery.discoveryLink(url), null, url);
  assert.equal(discovery.discoveryLink("/api/source-download?source=usgs-streamflow"), "/api/source-download?source=usgs-streamflow");
  assert.equal(discovery.discoveryLink("https://api.waterdata.usgs.gov/"), "https://api.waterdata.usgs.gov/");
});

test("each guided investigation joins real source IDs and map links retain exactly the selected context", () => {
  for (const investigation of discovery.INVESTIGATIONS) {
    assert.equal(investigation.ids.length, 3);
    for (const id of investigation.ids) assert.ok(sources.some(source => source.id === id), id);
    const url = new URL(discovery.sourceMapHref(investigation.ids), "https://kfm.example");
    assert.deepEqual(url.searchParams.get("ctx").split(","), [...investigation.ids]);
    assert.equal(url.searchParams.get("l"), "");
    assert.equal(url.searchParams.get("layerView"), "selected");
    assert.equal(url.searchParams.get("mapui"), "open");
    assert.equal(url.searchParams.get("maptab"), "display");
  }
});

test("research references remain separate from registered map data and retain review requirements", () => {
  for (const item of discovery.RESEARCH_FRONTIER) {
    assert.ok(!sources.some(source => source.id === item.id));
    assert.equal(discovery.discoveryLink(item.href), item.href);
    assert.ok(item.gate.length > 40);
    assert.match(item.checked, /^\d{4}-\d{2}-\d{2}$/);
  }
});


test("catalogue credits preserve provider and license names as readable text with inspectable links", () => {
  const civic = sources.find(source => source.id === "census-congress-119");
  const credits = discovery.discoveryAttribution(civic.attribution);
  assert.equal(credits.map(part => part.text).join(""), "U.S. Census Bureau · ACS 2025 generalized districts · Lewis et al. historical districts · MIT license");
  assert.deepEqual(credits.filter(part => part.href).map(part => part.href), ["https://www.census.gov/", "https://cdmaps.polisci.ucla.edu/", "/civic-history-license.txt"]);
  const deflock = discovery.discoveryAttribution(sources.find(source => source.id === "deflock-alpr").attribution);
  assert.equal(deflock.map(part => part.text).join(""), "DeFlock tagging · © OpenStreetMap contributors · ODbL");
  assert.deepEqual(deflock.filter(part => part.href).map(part => part.href), ["https://www.openstreetmap.org/copyright", "https://opendatacommons.org/licenses/odbl/1-0/"]);
  assert.deepEqual(discovery.discoveryAttribution("USGS · original attribution"), [{ text: "USGS · original attribution", href: null }]);
  assert.deepEqual(discovery.discoveryAttribution(""), []);
});

test("credit parsing rejects unsafe destinations and leaves unsupported markup inert", () => {
  for (const href of ["javascript:alert(1)", "data:text/html,test", "http://example.org/", "//example.org/", "/\\example.org/", "https://user:secret@example.org/"]) {
    assert.deepEqual(discovery.discoveryAttribution(`Before <a href="${href}">Provider terms</a> after`), [
      { text: "Before ", href: null }, { text: "Provider terms", href: null }, { text: " after", href: null },
    ]);
  }
  assert.deepEqual(discovery.discoveryAttribution("<a href='/license.txt'>Local license</a>"), [{ text: "Local license", href: "/license.txt" }]);
  for (const text of ['<img src=x onerror=alert(1)>', '<a href="https://example.org/" onclick="alert(1)">Credit</a>', '<a href="https://example.org/"><b>Credit</b></a>', '<a href="https://example.org/">unfinished']) {
    assert.deepEqual(discovery.discoveryAttribution(text), [{ text, href: null }]);
  }
});

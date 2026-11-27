import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
import { PUBLIC_LAB_SNAPSHOTS } from "../app/labs/public-snapshots.mjs";

// Join the real source registry without starting the application or contacting providers.
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
const { RESEARCH_PATHWAYS, pathwayComparisonHref } = await import(await moduleUrl("app/research/pathways.ts"));
const { OFFICIAL_CONTEXT_SOURCES } = await import(await moduleUrl("app/live-context.ts"));
const { TOPIC_STRUCTURE } = await import(await moduleUrl("app/layer-workspaces.ts"));
const { sourceMapHref } = await import(await moduleUrl("app/research/discovery.ts"));
const origin = "https://kfm.example";
const byId = id => RESEARCH_PATHWAYS.find(pathway => pathway.id === id);
const tool = href => RESEARCH_PATHWAYS.flatMap(pathway => pathway.tools).find(entry => entry.href === href);
const json = async file => JSON.parse(await readFile(new URL("../" + file, import.meta.url), "utf8"));

function localUrl(href) {
  assert.match(href, /^\/(?!\/)/, href);
  assert.doesNotMatch(href, /[\\\u0000-\u0020]/, href);
  const url = new URL(href, origin);
  assert.equal(url.origin, origin);
  assert.equal(url.username, "");
  assert.equal(url.password, "");
  assert.doesNotMatch(url.pathname, /(?:api|local-data|admin|knowledge)(?:\/|$)/);
  return url;
}

async function routeExists(href) {
  const url = localUrl(href);
  const directory = path.resolve("app", url.pathname.slice(1));
  const exists = await Promise.all(["tsx", "jsx", "ts", "js"].map(extension => access(path.join(directory, `page.${extension}`)).then(() => true, () => false)));
  assert.ok(exists.some(Boolean), `Missing public page: ${href}`);
  if (url.pathname === "/topics") {
    assert.ok(TOPIC_STRUCTURE.some(topic => "#" + topic.id === url.hash), href);
  }
  if (url.pathname === "/labs") {
    assert.deepEqual([...url.searchParams.keys()], ["story"], href);
    assert.ok(Object.hasOwn(PUBLIC_LAB_SNAPSHOTS, url.searchParams.get("story")), `Public snapshot missing: ${href}`);
  }
}

test("eight distinct fields connect to existing public tools with explicit coverage", async () => {
  assert.deepEqual(RESEARCH_PATHWAYS.map(pathway => pathway.id), ["water", "weather", "agriculture", "geology", "ecology", "history", "infrastructure", "communities"]);
  assert.equal(new Set(RESEARCH_PATHWAYS.map(pathway => pathway.title)).size, 8);
  for (const pathway of RESEARCH_PATHWAYS) {
    for (const field of ["title", "question", "summary", "scope", "boundary"]) {
      assert.ok(pathway[field].trim().length > 12, `${pathway.id}: ${field}`);
    }
    assert.ok(pathway.tools.length >= 2 && pathway.tools.length <= 3, pathway.id);
    assert.equal(new Set(pathway.tools.map(entry => entry.href)).size, pathway.tools.length);
    for (const entry of pathway.tools) {
      assert.ok(entry.label.trim());
      assert.ok(entry.scope.trim().length > 30, `${pathway.id}: ${entry.label} coverage`);
      await routeExists(entry.href);
    }
    await routeExists(pathway.topicHref);
  }
});

test("pathway comparisons join only registered context and retain exactly their source IDs", () => {
  const sourceIds = new Set(OFFICIAL_CONTEXT_SOURCES.map(source => source.id));
  for (const pathway of RESEARCH_PATHWAYS) {
    assert.ok(pathway.sourceIds.length >= 1 && pathway.sourceIds.length <= 3);
    assert.equal(new Set(pathway.sourceIds).size, pathway.sourceIds.length);
    for (const id of pathway.sourceIds) assert.ok(sourceIds.has(id), `${pathway.id}: ${id}`);
    const url = localUrl(pathwayComparisonHref(pathway));
    assert.equal(url.pathname, "/research");
    assert.equal(url.hash, "#comparison");
    assert.deepEqual([...url.searchParams.keys()], ["compare"]);
    assert.deepEqual(url.searchParams.get("compare").split(","), [...pathway.sourceIds]);
    const map = localUrl(sourceMapHref(pathway.sourceIds));
    assert.deepEqual(map.searchParams.get("ctx").split(","), [...pathway.sourceIds]);
    assert.equal(map.searchParams.get("layerView"), "selected");
    assert.equal(map.searchParams.get("mapui"), "open");
    assert.equal(map.searchParams.get("maptab"), "display");
    assert.equal(map.searchParams.get("l"), "");
  }
});

test("every connection names a different real field and the pathways remain traversable", () => {
  for (const pathway of RESEARCH_PATHWAYS) {
    assert.ok(pathway.connections.length > 0);
    assert.equal(new Set(pathway.connections).size, pathway.connections.length);
    for (const id of pathway.connections) {
      assert.ok(byId(id), `${pathway.id} -> ${id}`);
      assert.notEqual(id, pathway.id);
    }
    const visited = new Set(), queue = [pathway.id];
    while (queue.length) {
      const id = queue.shift();
      if (visited.has(id)) continue;
      visited.add(id);
      queue.push(...byId(id).connections);
    }
    assert.equal(visited.size, RESEARCH_PATHWAYS.length, `${pathway.id} connects across all subjects`);
  }
});

test("stated laboratory coverage remains tied to the shipping source manifests", async () => {
  const [climate, drought, soil, air, sunlight] = await Promise.all([
    "app/labs/heat-and-rain/snapshot-manifest.json", "app/labs/county-drought/snapshot-manifest.json",
    "app/labs/soil-profile/snapshot-manifest.json", "app/labs/daily-air-quality/snapshot-manifest.json",
    "app/labs/sunlight-and-sky/snapshot-manifest.json",
  ].map(json));
  for (const [href, manifest] of [["/labs/heat-and-rain", climate], ["/labs/county-drought", drought], ["/labs/soil-profile", soil], ["/labs/daily-air-quality", air], ["/labs/sunlight-and-sky", sunlight]]) {
    assert.ok(tool(href).scope.includes(`${manifest.period.from.slice(0, 4)}–${manifest.period.to.slice(0, 4)}`), href);
  }
  assert.equal(climate.stations.length, 3);
  assert.equal(drought.counties.length, 105);
  assert.equal(drought.snapshot.weeks, 313);
  assert.equal(soil.stations.length, 2);
  assert.equal(soil.depthsCm.length, 5);
  assert.equal(air.counties.length, 12);
  assert.equal(sunlight.points.length, 3);
  assert.ok(tool("/labs/county-drought").scope.includes(String(drought.counties.length)));
  assert.ok(tool("/labs/county-drought").scope.includes(String(drought.snapshot.weeks)));
  assert.ok(tool("/labs/daily-air-quality").scope.includes(String(air.counties.length)));
  assert.equal(PUBLIC_LAB_SNAPSHOTS["built-kansas"].records, 24877);
  assert.ok(tool("/labs?story=built-kansas").scope.includes(new Intl.NumberFormat("en-US").format(PUBLIC_LAB_SNAPSHOTS["built-kansas"].records)));
  for (const id of ["shaking-ground", "energy-shift", "census-mosaic"]) {
    const snapshot = PUBLIC_LAB_SNAPSHOTS[id];
    assert.ok(tool(`/labs?story=${id}`).scope.includes(`${snapshot.observed.from}–${snapshot.observed.to}`), id);
  }
});

test("sampling gaps, aggregate boundaries and the single Konza case remain explicit", () => {
  assert.match(byId("water").boundary, /not statewide flow coverage/);
  assert.match(byId("weather").boundary, /not personal exposure/);
  assert.match(byId("agriculture").boundary, /not a continuous soil column/);
  assert.match(byId("geology").boundary, /nearby states/);
  assert.match(byId("history").boundary, /selected cases, not complete statewide history/);
  assert.match(byId("infrastructure").boundary, /not current safety findings/);
  assert.match(byId("communities").boundary, /periods, not single years/);
  const ecology = byId("ecology");
  assert.match(ecology.scope, /no reviewed statewide species inventory/);
  assert.match(ecology.boundary, /not species abundance, absence or movement/);
  assert.match(tool("/labs/terrain").scope, /One sampled Konza Prairie NEON tile/);
  assert.match(tool("/labs/terrain").scope, /scientific review pending/);
  assert.equal(RESEARCH_PATHWAYS.flatMap(pathway => pathway.tools).filter(entry => /Konza|canopy/i.test(entry.label + " " + entry.scope)).length, 1);
  assert.ok(RESEARCH_PATHWAYS.flatMap(pathway => pathway.tools).every(entry => !/[?&](?:admitted|release|review)=/.test(entry.href)));
});

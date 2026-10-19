import assert from "node:assert/strict";
import { readFile, access } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode } from "./component-harness.mjs";

const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}
const topics = await import(await moduleUrl("app/layer-workspaces.ts"));
const context = await import(await moduleUrl("app/live-context.ts"));
const imagery = await import(await moduleUrl("app/earth-engine-context.ts"));
const features = await import(await moduleUrl("app/feature-catalog.ts"));
const atlas = await import(await moduleUrl("app/living-atlas.ts"));
const functions = await import(await moduleUrl("app/function-registry.ts"));

function nodes(tree, predicate) {
  const found = [];
  function visit(node) {
    if (!node || typeof node !== "object") return;
    if (predicate(node)) found.push(node);
    for (const child of [node.props?.children].flat(Infinity)) visit(child);
  }
  visit(tree); return found;
}

test("requested subjects have grouped subtopics, inspectable limits and real internal routes", async () => {
  const required = ["engineering", "science", "weather", "history", "land", "people"];
  const ids = topics.TOPIC_STRUCTURE.map(topic => topic.id);
  assert.equal(ids.length, 17);
  assert.equal(new Set(ids).size, ids.length);
  assert.ok(required.every(id => ids.includes(id)));
  assert.deepEqual(topics.LAYER_WORKSPACES.map(([id]) => id), ["all", ...ids]);
  for (const topic of topics.TOPIC_STRUCTURE) {
    assert.ok(topics.TOPIC_GROUPS.includes(topic.group));
    assert.ok(topic.facets.length >= 3 && topic.description && topic.limitation);
    for (const resource of topic.resources) {
      const url = new URL(resource.href, "https://example.test");
      await access(`app${url.pathname === "/" ? "" : url.pathname}/page.tsx`);
      if (url.pathname === "/") {
        assert.equal(url.searchParams.get("mapui"), "open");
        assert.ok(["measure", "scene", "history", "inspect", "compare"].includes(url.searchParams.get("maptab")));
      }
    }
  }
  assert.match(topics.topicDefinition("land").limitation, /Land ownership instruments are not connected/);
  assert.match(topics.topicDefinition("land").limitation, /Unreleased records and private parcel detail stay off the map/);
  assert.ok(topics.topicDefinition("land").resources.some(r => r.href === "/knowledge"));
  assert.match(topics.topicDefinition("people").limitation, /not individuals/);
  assert.match(topics.topicDefinition("ecology").limitation, /No species inventory/);
});

test("complete current source, imagery, feature and investigation inventories retain identity and posture", () => {
  const before = JSON.stringify([context.OFFICIAL_CONTEXT_SOURCES, imagery.EARTH_ENGINE_CONTEXT_LAYERS, features.FEATURE_CATALOG, atlas.LIVING_ATLAS_VIEWS, functions.FUNCTION_REGISTRY]);
  const known = new Set(topics.TOPIC_STRUCTURE.map(topic => topic.id));
  for (const source of context.OFFICIAL_CONTEXT_SOURCES) {
    const membership = topics.officialSourceTopics(source.id);
    assert.ok(membership.length, `unassigned source: ${source.id}`);
    assert.ok(membership.every(id => known.has(id)));
    assert.equal(source.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
  }
  for (const layer of imagery.EARTH_ENGINE_CONTEXT_LAYERS) assert.ok(topics.imageryTopics(layer.id).length, `unassigned imagery: ${layer.id}`);
  for (const feature of features.FEATURE_CATALOG) assert.ok(topics.featureTopics(feature.id).includes("evidence"));
  for (const view of atlas.LIVING_ATLAS_VIEWS) assert.ok(topics.atlasViewTopics(view.id).length, `unassigned investigation: ${view.id}`);
  for (const record of functions.FUNCTION_REGISTRY) assert.ok(topics.functionTopics(record.id).includes("evidence"));
  assert.deepEqual(topics.officialSourceTopics("kgs-unverified"), []);
  assert.deepEqual(topics.officialSourceTopics("blm-plss-unverified"), []);
  assert.deepEqual(topics.imageryTopics("ee-unverified"), []);
  assert.equal(JSON.stringify([context.OFFICIAL_CONTEXT_SOURCES, imagery.EARTH_ENGINE_CONTEXT_LAYERS, features.FEATURE_CATALOG, atlas.LIVING_ATLAS_VIEWS, functions.FUNCTION_REGISTRY]), before);
});

test("cross-disciplinary membership is specific; populations, surveys and models stay distinct", () => {
  const sources = context.OFFICIAL_CONTEXT_SOURCES;
  const ids = id => topics.filterOfficialSources(sources, id, "").map(source => source.id);
  assert.deepEqual(ids("people"), ["census-counties"]);
  assert.ok(ids("engineering").includes("kdot-bridges-state"));
  assert.ok(ids("history").includes("kdot-roads-1918"));
  assert.ok(ids("land").includes("blm-mlrs-leases-authorized"));
  assert.ok(ids("science").includes("noaa-nwm-analysis"));
  assert.ok(ids("weather").includes("nws-forecast-wind"));
  assert.ok(!ids("weather").includes("usgs-earthquakes"));
  assert.ok(!ids("land").includes("census-counties"));
  assert.ok(topics.registryLayerTopics("People / Land").includes("people"));
  assert.ok(topics.registryLayerTopics("Historical Geography").includes("history"));
  assert.ok(topics.featureTopics("ndvi-change").includes("ecology"));
});

test("all topic/view/search projections preserve selected source dates, opacity and catalog status", () => {
  const entries = [...context.OFFICIAL_CONTEXT_SOURCES.map(source => ({ id: source.id, title: source.title, keywords: source.domain, topics: topics.officialSourceTopics(source.id), selected: true })), ...imagery.EARTH_ENGINE_CONTEXT_LAYERS.map(layer => ({ id: layer.id, title: layer.title, keywords: layer.source, topics: topics.imageryTopics(layer.id), selected: true, imagery: true }))];
  const owner = { entries, opacity: .42, day: "2024-04-10", release: "HELD", paused: false };
  const before = JSON.stringify(owner), total = topics.selectedCatalogCount(entries);
  for (const [topic] of topics.LAYER_WORKSPACES) {
    for (const view of ["official", "selected", "local"]) {
      for (const query of ["", "science", "never matches"]) {
        entries.filter(entry => topics.layerEntryMatches(entry, view, topic, query));
        assert.equal(topics.selectedCatalogCount(entries), total);
      }
    }
  }
  assert.equal(JSON.stringify(owner), before);
  assert.equal(topics.catalogDisplayStatus({ selected: true, held: true, state: "ready", canDisplay: false }), "Held");
});

test("grouped accessible selector validates topic values and guides dispatch existing tools", async () => {
  const h = await componentHarness("app/topic-navigation.tsx", { "next/link": { default: "a" }, "./layer-workspaces": topics }, { URLSearchParams });
  let selected;
  const tree = h.render(h.exports.TopicSelect, { value: "weather", label: "Layer topic", onChange: value => { selected = value; } });
  const select = findNode(tree, node => node.type === "select");
  assert.equal(select.props["aria-label"], "Layer topic");
  assert.equal(nodes(tree, node => node.type === "optgroup").length, 4);
  assert.equal(nodes(tree, node => node.type === "option").length, 18);
  select.props.onChange({ target: { value: "engineering" } }); assert.equal(selected, "engineering");
  select.props.onChange({ target: { value: "__proto__" } }); assert.equal(selected, "all");
  let opened;
  const button = { id: "launcher" };
  const guide = h.render(h.exports.TopicGuide, { value: "engineering", onTool: (view, element) => { opened = [view, element]; } });
  findNode(guide, node => node.type === "button").props.onClick({ currentTarget: button });
  assert.deepEqual(opened, ["measure", button]);
  assert.equal(h.render(h.exports.TopicGuide, { value: "all" }), null);
  h.dispose();
});

test("rendered topic index binds counts to current inventories and opens valid topic and imagery links", async () => {
  const h = await componentHarness("app/topics/page.tsx", { "next/link": { default: "a" }, "../layer-workspaces": topics, "../live-context": context, "../earth-engine-context": imagery, "../feature-catalog": features, "./topics.module.css": { default: {} } });
  const tree = h.render(h.exports.default, {});
  const cards = nodes(tree, node => node.type === "article");
  assert.equal(cards.length, topics.TOPIC_STRUCTURE.length);
  for (const card of cards) {
    const summaries = nodes(card, node => node.type === "summary");
    assert.equal(summaries[0].props.children.at(-1), context.OFFICIAL_CONTEXT_SOURCES.filter(source => topics.officialSourceTopics(source.id).includes(card.props.id)).length);
    assert.ok(findNode(card, node => node.props?.href === `/?topic=${card.props.id}`));
  }
  for (const anchor of nodes(tree, node => typeof node.props?.href === "string" && node.props.href.startsWith("/?topic="))) {
    const params = new URLSearchParams(anchor.props.href.slice(2));
    assert.notEqual(topics.restoreTopic(params.get("topic")), "all");
  }
  for (const anchor of nodes(tree, node => typeof node.props?.href === "string" && node.props.href.startsWith("/"))) {
    const url = new URL(anchor.props.href, "https://example.test");
    await access(`app${url.pathname === "/" ? "" : url.pathname}/page.tsx`);
  }
  h.dispose();
});


test("topic and layer-view navigation round-trips without changing unrelated repeated URL keys", () => {
  const views = [["official", null], ["selected", "selected"], ["local", "imagery"]];
  for (const [topic] of topics.LAYER_WORKSPACES) {
    for (const [view, serializedView] of views) {
      const params = new URLSearchParams("ctx=census-counties&ctx=usgs-streamflow&time=1909&maptab=compare&mapui=open&tokenHint=not-a-secret");
      const unrelated = [...params.entries()];
      topics.serializeTopicSelection(params, topic, view);
      const restored = new URL(`https://example.test/?${params}`).searchParams;
      assert.equal(topics.restoreTopic(restored.get("topic")), topic);
      assert.equal(restored.get("topic"), topic === "all" ? null : topic);
      assert.equal(restored.get("layerView"), serializedView);
      const restoredView = restored.get("layerView") === "imagery" ? "local" : restored.get("layerView") === "selected" ? "selected" : "official";
      assert.equal(restoredView, view);
      assert.deepEqual([...restored.entries()].filter(([key]) => key !== "topic" && key !== "layerView"), unrelated);
    }
  }
});

test("clearing or invalid navigation removes stale values without widening URL state", () => {
  const params = new URLSearchParams("topic=water&topic=history&layerView=imagery&layerView=selected&layers=sources&base=standard");
  topics.serializeTopicSelection(params, "science", "selected");
  assert.deepEqual(params.getAll("topic"), ["science"]);
  assert.deepEqual(params.getAll("layerView"), ["selected"]);
  topics.serializeTopicSelection(params, "all", "official");
  assert.equal(params.toString(), "layers=sources&base=standard");
  topics.serializeTopicSelection(params, "__proto__", "unrecognized-view");
  assert.equal(params.toString(), "layers=sources&base=standard");
});

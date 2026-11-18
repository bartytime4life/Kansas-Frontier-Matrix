import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const load = async path => {
  const source = ts.transpileModule(await readFile(path, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
};
const guides = await load("app/landing-guides.ts");

test("every map guide is crawlable, plain-language and links only to public context layers", async () => {
  const context = await readFile("app/live-context.ts", "utf8");
  const reference = await readFile("app/kansas-reference-layers.ts", "utf8").catch(() => "");
  const slugs = new Set();
  assert.ok(guides.LANDING_GUIDES.length >= 16);
  // The bridges guide opens the counted-circle bridge layers without the 19,000-point local list.
  assert.deepEqual(guides.landingGuide("kansas-bridges").layers, ["kdot-bridges-state", "kdot-bridges-historic", "kdot-bridges-closed"]);
  for (const guide of guides.LANDING_GUIDES) {
    assert.match(guide.slug, /^[a-z0-9-]+$/);
    assert.ok(!slugs.has(guide.slug)); slugs.add(guide.slug);
    assert.ok(guide.description.length >= 70 && guide.description.length <= 170, `${guide.slug} description suits search snippets`);
    assert.doesNotMatch(`${guide.title} ${guide.description} ${guide.intro.join(" ")}`, /MapLibre|Qwen|bounded|evidence bundle|EXTERNAL_CONTEXT/i, "guides use plain language");
    assert.ok(guide.caution.length > 40);
    assert.ok(guide.layers.length >= 2 && guide.layers.length <= 4);
    for (const id of guide.layers) assert.ok(context.includes(`"${id}"`) || reference.includes(`"${id}"`), `${guide.slug} layer ${id} is a registered source`);
    const href = new URL(guides.guideMapHref(guide), "https://kansasfrontiermatrix.com");
    assert.equal(href.pathname, "/");
    assert.deepEqual(href.searchParams.get("ctx").split(","), [...guide.layers]);
    const [lon, lat] = href.searchParams.get("c").split(",").map(Number);
    assert.ok(lon > -102.1 && lon < -94.6 && lat > 37 && lat < 40, "the map opens over Kansas");
    assert.ok(Number(href.searchParams.get("z")) >= 5 && Number(href.searchParams.get("z")) <= 9);
  }
});

test("every guide has its own page and the topics page links the guide index", async () => {
  assert.match(await readFile("app/topics/page.tsx", "utf8"), /<Link href="\/explore">Map guides<\/Link>/);
  for (const guide of guides.LANDING_GUIDES) {
    const page = await readFile(`app/explore/${guide.slug}/page.tsx`, "utf8");
    assert.match(page, new RegExp(`guideMetadata\\("${guide.slug}"\\)`));
    assert.match(page, new RegExp(`<GuidePage slug="${guide.slug}" />`));
  }
});

test("guides cover the main Explorer themes, old and new, without repeating a layer stack", () => {
  const slugs = guides.LANDING_GUIDES.map(guide => guide.slug);
  for (const slug of ["storms-and-severe-weather", "fire-and-smoke", "aquifers-and-groundwater", "earthquakes-in-kansas",
    "land-cover-and-public-lands", "rivers-and-floods", "roads-and-railroads", "land-survey-and-soils",
    "lightning-and-the-sky", "kansas-aquifers", "terrain-and-slope"]) assert.ok(slugs.includes(slug), slug);
  const stacks = guides.LANDING_GUIDES.map(guide => [...guide.layers].sort().join(","));
  assert.equal(new Set(stacks).size, stacks.length, "each guide opens its own layer stack");
});

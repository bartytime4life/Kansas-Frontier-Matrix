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
  assert.ok(guides.LANDING_GUIDES.length >= 5);
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

test("guides for layers drawn as counted circles tell visitors what the circles are", () => {
  // These four guides open layers that show numbered circles at the zoom the guide opens at.
  for (const [slug, layer] of [["kansas-bridges", "kdot-bridges-state"], ["historic-places", "nps-nrhp-places"], ["frontier-trails", "nps-trail-places"], ["hunting-and-wildlife-areas", "kdwp-wiha-access"]]) {
    const guide = guides.landingGuide(slug);
    assert.ok(guide.layers.includes(layer), `${slug} opens ${layer}`);
    assert.match(guide.intro.join(" "), /numbered circles/i, `${slug} explains the numbered circles`);
    assert.match(guide.intro.join(" "), /zoom/i, `${slug} says zooming splits them`);
  }
});

test("the sitemap lists the guide index and every guide", async () => {
  const discovery = await readFile("app/crawler-discovery.ts", "utf8");
  assert.match(discovery, /\/explore<\/loc>/);
  assert.match(discovery, /LANDING_GUIDES\.map\(guide => `  <url><loc>\$\{PUBLIC_SITE_ORIGIN\}\/explore\/\$\{guide\.slug\}<\/loc>/);
  for (const guide of guides.LANDING_GUIDES) {
    const page = await readFile(`app/explore/${guide.slug}/page.tsx`, "utf8");
    assert.match(page, new RegExp(`guideMetadata\\("${guide.slug}"\\)`));
    assert.match(page, new RegExp(`<GuidePage slug="${guide.slug}" />`));
  }
});

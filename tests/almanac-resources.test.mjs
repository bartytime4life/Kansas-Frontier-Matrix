import assert from "node:assert/strict";
import { readFile, access } from "node:fs/promises";
import { createHash } from "node:crypto";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode } from "./component-harness.mjs";

const source = await readFile("app/almanac-resources.ts", "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const almanacs = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
const nodes = (tree, predicate) => {
  const result = [];
  function visit(node) { if (!node || typeof node !== "object") return; if (predicate(node)) result.push(node); for (const child of [node.props?.children].flat(Infinity)) visit(child); }
  visit(tree); return result;
};

test("both requested publications are distinct and each source has access, time, rights and scope", () => {
  assert.deepEqual(almanacs.ALMANAC_PUBLISHERS.map(item => item.id), ["farmers-almanac", "old-farmers-almanac"]);
  assert.equal(almanacs.ALMANAC_RESOURCES.length, 13);
  assert.equal(new Set(almanacs.ALMANAC_RESOURCES.map(item => item.id)).size, 13);
  for (const resource of almanacs.ALMANAC_RESOURCES) {
    assert.ok(almanacs.almanacPublisher(resource.publisherId));
    for (const key of ["title", "summary", "scope", "period", "accessNote", "limitation", "sourceUrl", "rightsUrl"]) assert.ok(resource[key], `${resource.id} missing ${key}`);
    assert.equal(new URL(resource.sourceUrl).protocol, "https:");
    assert.ok(["www.farmersalmanac.com", "www.almanac.com", "www.loc.gov"].includes(new URL(resource.sourceUrl).hostname));
    assert.ok(!("layerId" in resource) && !("evidenceRef" in resource));
  }
  const historical = almanacs.ALMANAC_RESOURCES.find(item => item.id === "ofa-1861-title");
  assert.match(historical.period, /1860.*1861/);
  assert.match(historical.scope, /Boston.*New England/);
  assert.match(historical.limitation, /one deposited title page, not the full issue/);
  const inaccessible = almanacs.ALMANAC_RESOURCES.find(item => item.id === "ofa-wichita-forecast");
  assert.equal(inaccessible.access, "CHECK_FAILED");
  assert.equal(inaccessible.treatment, "LINK_ONLY");
  assert.match(inaccessible.accessNote, /403/);
});

test("only provenance-bound permitted images are packaged; hashes, sizes and JPEG identity match", async () => {
  assert.equal(almanacs.ALMANAC_ASSETS.length, 2);
  let total = 0;
  for (const asset of almanacs.ALMANAC_ASSETS) {
    const resource = almanacs.ALMANAC_RESOURCES.find(item => item.id === asset.resourceId);
    assert.ok(resource && resource.treatment !== "LINK_ONLY");
    assert.equal(almanacs.almanacDisplayAsset(resource), asset);
    assert.ok(asset.rightsBasis && asset.rightsUrl && asset.credit && asset.alt);
    const bytes = await readFile(`public${asset.path}`);
    assert.equal(bytes.length, asset.bytes);
    assert.equal(bytes.subarray(0, 3).toString("hex"), "ffd8ff");
    assert.equal(createHash("sha256").update(bytes).digest("hex"), asset.sha256);
    let dimensions;
    for (let offset = 2; offset + 9 < bytes.length;) {
      assert.equal(bytes[offset], 0xff, "expected JPEG segment marker");
      const marker = bytes[offset + 1];
      if (marker === 0xc0 || marker === 0xc2) {
        dimensions = { height: bytes.readUInt16BE(offset + 5), width: bytes.readUInt16BE(offset + 7) };
        break;
      }
      offset += 2 + bytes.readUInt16BE(offset + 2);
    }
    assert.deepEqual(dimensions, { height: asset.height, width: asset.width });
    total += bytes.length;
  }
  assert.equal(total, 171336);
  for (const resource of almanacs.ALMANAC_RESOURCES.filter(item => item.treatment === "LINK_ONLY")) assert.equal(almanacs.almanacDisplayAsset(resource), null);
  const map = almanacs.ALMANAC_RESOURCES.find(item => item.id === "fa-winter-2026-2027");
  assert.equal(almanacs.almanacDisplayAsset({ ...map, publisherId: "old-farmers-almanac" }), null);
  assert.equal(almanacs.almanacDisplayAsset({ ...map, treatment: "PUBLIC_DOMAIN_IMAGE" }), null);
  assert.equal(almanacs.almanacDisplayAsset({ ...map, access: "CHECK_FAILED" }), null);
  assert.equal(almanacs.almanacDisplayAsset({ ...map, id: "unreviewed" }), null);
});

test("filters preserve material and posture, and navigation ignores unknown values", () => {
  const before = JSON.stringify(almanacs.ALMANAC_RESOURCES);
  assert.equal(almanacs.filterAlmanacResources("farmers-almanac", "all", "").length, 5);
  assert.equal(almanacs.filterAlmanacResources("old-farmers-almanac", "all", "").length, 8);
  assert.equal(almanacs.filterAlmanacResources("all", "weather", "").length, 7);
  assert.deepEqual(almanacs.filterAlmanacResources("old-farmers-almanac", "agriculture", "Wichita").map(item => item.id), ["ofa-wichita-planting"]);
  assert.deepEqual(almanacs.filterAlmanacResources("all", "history", "1861").map(item => item.id), ["ofa-1861-title"]);
  assert.deepEqual(almanacs.restoreAlmanacFilters("?publisher=old-farmers-almanac&topic=sky"), { publisher: "old-farmers-almanac", topic: "sky" });
  assert.deepEqual(almanacs.restoreAlmanacFilters("?publisher=__proto__&topic=javascript:alert(1)"), { publisher: "all", topic: "all" });
  assert.equal(JSON.stringify(almanacs.ALMANAC_RESOURCES), before);
});

test("library actually filters cards, retains withheld entries, and loads no publisher content", async () => {
  const h = await componentHarness("app/almanacs/library.tsx", { "next/link": { default: "a" }, "../almanac-resources": almanacs, "./almanacs.module.css": { default: {} } }, { window: { location: { search: "?publisher=old-farmers-almanac&topic=sky" } } });
  const render = () => h.render(h.exports.default, { initialFilters: almanacs.restoreAlmanacFilters("?publisher=old-farmers-almanac&topic=sky") });
  let tree = render(); h.commit(); tree = render();
  assert.deepEqual(nodes(tree, node => node.type === "article" && node.props.id?.startsWith("almanac-")).map(node => node.props.id), ["almanac-ofa-wichita-moon", "almanac-ofa-1861-title"]);
  assert.equal(nodes(tree, node => node.type === "img").length, 1);
  findNode(tree, node => node.type === "button" && node.props.children === "Clear filters").props.onClick(); tree = render();
  assert.equal(nodes(tree, node => node.type === "article" && node.props.id?.startsWith("almanac-")).length, 13);
  const images = nodes(tree, node => node.type === "img");
  assert.equal(images.length, 2);
  assert.ok(images.every(node => node.props.src.startsWith("/almanacs/") && node.props.alt && node.props.width && node.props.height));
  const failed = findNode(tree, node => node.props?.id === "almanac-ofa-wichita-forecast");
  assert.equal(failed.props["data-access"], "CHECK_FAILED");
  assert.equal(nodes(failed, node => node.type === "img").length, 0);
  findNode(tree, node => node.props?.["aria-label"] === "Search almanac references").props.onChange({ target: { value: "not a matching term" } }); tree = render();
  assert.ok(findNode(tree, node => node.type === "h3" && node.props.children === "No matching references"));
  findNode(tree, node => node.type === "button" && node.props.children === "Show all references").props.onClick(); tree = render();
  assert.equal(nodes(tree, node => node.type === "img").length, 2);
  h.dispose();
  const librarySource = await readFile("app/almanacs/library.tsx", "utf8");
  assert.doesNotMatch(librarySource, /\bfetch\(|XMLHttpRequest|<iframe|api\/|localStorage|navigator\.geolocation/);
});

test("server page validates deep-link filters before the first client render", async () => {
  const h = await componentHarness("app/almanacs/page.tsx", { "./library": { default: "AlmanacLibrary" }, "../almanac-resources": almanacs }, { URLSearchParams });
  const valid = await h.render(h.exports.default, { searchParams: Promise.resolve({ publisher: "old-farmers-almanac", topic: "sky" }) });
  assert.deepEqual(valid.props.initialFilters, { publisher: "old-farmers-almanac", topic: "sky" });
  const invalid = await h.render(h.exports.default, { searchParams: Promise.resolve({ publisher: "__proto__", topic: ["weather", "history"] }) });
  assert.deepEqual(invalid.props.initialFilters, { publisher: "all", topic: "all" });
  h.dispose();
});

test("both source candidates stay held and topic navigation reaches the implemented library", async () => {
  const discovery = await readFile("app/source-intelligence.ts", "utf8");
  for (const id of ["SRC-CAND-FARMERS-ALMANAC", "SRC-CAND-OLD-FARMERS-ALMANAC"]) {
    assert.ok(discovery.includes(`"${id}": "held"`));
    assert.ok(discovery.includes(`id: "${id}"`));
  }
  const topics = await readFile("app/layer-workspaces.ts", "utf8");
  for (const topic of ["weather", "agriculture", "sky", "history"]) assert.ok(topics.includes(`/almanacs?topic=${topic}`));
  await access("app/almanacs/page.tsx");
  const about = await readFile("app/about/page.tsx", "utf8");
  assert.ok(about.includes('href="/almanacs"'));
});

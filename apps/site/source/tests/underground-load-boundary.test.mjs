import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import test from "node:test";

test("the built main-map dependency list excludes the on-demand Underground implementation", async () => {
  const { default: manifest } = await import("../dist/server/__vite_rsc_assets_manifest.js");
  const readAsset = file => readFile(new URL(`../dist/client${file}`, import.meta.url), "utf8");
  const entries = Object.values(manifest.clientReferenceDeps);
  let mapEntry;
  for (const entry of entries) for (const file of entry.js) {
    if (/\/page-[^/]+\.js$/.test(file) && (await readAsset(file)).includes("Preparing spatial explorer")) mapEntry = entry;
  }
  assert.ok(mapEntry, "identify the actual main-map entry from its rendered loading surface");
  const chunks = await readdir(new URL("../dist/client/assets/", import.meta.url));
  const underground = chunks.filter(name => /^underground-panel-[^.]+\.js$/.test(name));
  assert.equal(underground.length, 1, "build a separate Underground implementation chunk");
  assert.ok(!mapEntry.js.includes(`/assets/${underground[0]}`), "do not statically preload the optional panel");
  const initial = (await Promise.all(mapEntry.js.map(readAsset))).join("\n");
  assert.doesNotMatch(initial, /Source assets are loading\./, "the Underground worker state remains outside the initial code");
  assert.match(await readAsset(`/assets/${underground[0]}`), /Source assets are loading\./);
});

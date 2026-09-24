import assert from "node:assert/strict";
import "./cloudflare-register.mjs";
import test from "node:test";

test("production worker serves discoverable Earth Engine workspace with honest access state", async () => {
  const { default: worker } = await import("../dist/server/index.js");
  const env = { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } };
  const ctx = { waitUntil() {}, passThroughOnException() {} };
  const response = await worker.fetch(new Request("http://localhost/earth-engine", { headers: { accept: "text/html" } }), env, ctx);
  assert.equal(response.status, 200);
  const html = await response.text();
  for (const label of ["Earth Engine datasets", "Earth Engine not connected", "Cropland Data Layer", "TerraClimate drought index", "Analysis year", "Download recipe", "Compare datasets"]) assert.ok(html.includes(label), label);
  assert.match(html, /href="\/data\?source=ee-cdl"/);
  assert.match(html, /No satellite data has been imported/);
  const home = await worker.fetch(new Request("http://localhost/", { headers: { accept: "text/html" } }), env, ctx);
  assert.equal(home.status, 200);
  assert.match(await home.text(), /href="\/earth-engine"/);
});

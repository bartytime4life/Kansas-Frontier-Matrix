import assert from "node:assert/strict";
import test from "node:test";

test("production Node handler serves discoverable Earth Engine workspace with honest access state", async () => {
  const { default: handler } = await import("../dist/server/index.js");
  const response = await handler(new Request("http://localhost/earth-engine", { headers: { accept: "text/html" } }));
  assert.equal(response.status, 200);
  const html = await response.text();
  for (const label of ["Earth Engine datasets", "live Earth Engine disconnected", "Cropland Data Layer", "TerraClimate drought index", "Analysis year", "Download recipe", "Compare datasets"]) assert.ok(html.includes(label), label);
  assert.match(html, /href="\/data\?source=ee-cdl"/);
  assert.match(html, /Installed coverage cannot be confirmed until the display inventory loads/);
  const home = await handler(new Request("http://localhost/", { headers: { accept: "text/html" } }));
  assert.equal(home.status, 200);
  const homeHtml = await home.text();
  assert.match(homeHtml, /href="\/earth-engine"/);
  assert.match(homeHtml, /id="earth-engine-context-controls"/);
  assert.match(homeHtml, /Earth Engine imagery/);
  assert.match(homeHtml, /aria-label="Earth Engine imagery layers"/);
  assert.doesNotMatch(homeHtml, /aria-label="Open installed Earth Engine layers"/);
});

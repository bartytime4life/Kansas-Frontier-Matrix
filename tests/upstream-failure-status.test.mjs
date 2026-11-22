import assert from "node:assert/strict";
import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { installPublicDelivery } from "../server/browser-headers.mjs";

// The application under the delivery layer, reduced to the ways a response can be written.
const app = (request, response) => {
  const url = new URL(request.url, "http://x"), status = Number(url.searchParams.get("status") ?? 200);
  const body = JSON.stringify({ message: "The exact historical radar frame is unavailable. No latest-image fallback was used." });
  if (url.searchParams.get("how") === "implicit") { response.statusCode = status; response.setHeader("Content-Type", "application/json"); response.end(body); }
  else if (url.searchParams.get("how") === "phrase") { response.writeHead(status, "Bad Gateway", { "Content-Type": "application/json" }); response.end(body); }
  else if (url.searchParams.get("how") === "raw") { response.writeHead(status, ["Content-Type", "application/json", "Cache-Control", "no-store"]); response.end(body); }
  else { response.writeHead(status, { "Content-Type": "application/json", "Cache-Control": "no-store" }); response.end(body); }
};
async function served(t) {
  const server = createServer(app);
  installPublicDelivery(server);
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  t.after(() => new Promise(resolve => server.close(resolve)));
  return `http://127.0.0.1:${server.address().port}`;
}

test("a public read that ends in 502 or 504 leaves as 503 with its body and names the route's status", async t => {
  const base = await served(t);
  for (const status of [502, 504]) for (const how of ["object", "implicit", "phrase", "raw"]) {
    const response = await fetch(`${base}/api/event-atlas/radar-frame?status=${status}&how=${how}`);
    assert.equal(response.status, 503, `${status} ${how}`);
    assert.equal(response.statusText, "Service Unavailable", `${status} ${how}`);
    assert.equal(response.headers.get("x-kfm-upstream-status"), String(status));
    assert.equal(response.headers.get("content-type"), "application/json");
    assert.match((await response.json()).message, /radar frame is unavailable/, "the route's explanation is intact");
    assert.equal(response.headers.get("x-content-type-options"), "nosniff", "the browser policy headers are still applied");
  }
  const head = await fetch(`${base}/api/drought-monitor?status=502`, { method: "HEAD" });
  assert.equal(head.status, 503); assert.equal(head.headers.get("x-kfm-upstream-status"), "502");
});

test("every other answer keeps its status", async t => {
  const base = await served(t);
  for (const status of [200, 400, 401, 404, 429, 500, 503]) {
    const response = await fetch(`${base}/api/live-context?status=${status}`);
    assert.equal(response.status, status); assert.equal(response.headers.get("x-kfm-upstream-status"), null);
    await response.arrayBuffer();
  }
  // Writes and the worker relays speak to machines that may act on the exact status.
  for (const method of ["POST", "PUT", "DELETE"]) {
    const response = await fetch(`${base}/api/home-worker/v1/claim?status=502`, { method });
    assert.equal(response.status, 502, method); assert.equal(response.headers.get("x-kfm-upstream-status"), null);
    await response.arrayBuffer();
  }
  // Pages and static files are not API reads.
  const page = await fetch(`${base}/observatory?status=502`);
  assert.equal(page.status, 502); await page.arrayBuffer();
});

test("the routes this protects still say why they failed", async () => {
  // A sample of the routes that answer 502 or 504 with an explanation in the body.
  for (const [path, text] of [
    ["app/api/event-atlas/radar-frame/route.ts", /The exact historical radar frame is unavailable/],
    ["app/api/drought-monitor/route.ts", /The Drought Monitor map is unavailable/],
    ["app/api/subsurface/resources/route.ts", /This source is unavailable/],
  ]) {
    const source = await readFile(path, "utf8");
    assert.match(source, text); assert.match(source, /status: ?502/);
  }
});

import test from "node:test";
import assert from "node:assert/strict";

// Run against the production build, not a source-text or mocked auth check.
const origin = process.env.KFM_NODE_TEST_ORIGIN ?? "http://127.0.0.1:5182";
test("legacy pricing endpoint is absent from the free Explorer", async () => {
  const response = await fetch(origin + "/api/reports/quote", {
    method: "POST",
    headers: { "Content-Type": "application/json", "x-role": "admin" },
    body: JSON.stringify({ role: "admin", paid: true, amount: 0 }),
  });
  assert.equal(response.status, 404);
});
test("anonymous map is public", async () => {
  const response = await fetch(origin, { redirect: "manual" });
  assert.equal(response.status, 200);
  assert.match(await response.text(), /Kansas Frontier Matrix/);
});
for (const path of [
  "/api/data-submissions",
  "/api/governed/water-admin/status",
  "/api/governed/weather-admin/status",
]) {
  test("forged dispatch and role headers cannot access " + path, async () => {
    const response = await fetch(origin + path, {
      headers: {
        "oai-authenticated-user-email": "steward@example.test",
        "oai-authenticated-user-id": "admin",
        "x-role": "admin",
      },
      redirect: "manual",
    });
    assert.equal(response.status, 401);
  });
}
test("map assets are served by the Node production server", async () => {
  const response = await fetch(origin + "/maplibre/maplibre-gl-worker.mjs");
  assert.equal(response.status, 200);
  assert.match(response.headers.get("content-type"), /javascript/);
  assert.ok((await response.text()).length > 1000);
});

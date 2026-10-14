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

for (const path of ['/downloads','/earth-engine-downloads/setup']) {
  test('legacy PC workbench URL redirects to hosted source status: ' + path, async () => {
    const response=await fetch(origin+path,{redirect:'manual'});
    assert.ok([302,303,307,308].includes(response.status));
    const destination=new URL(response.headers.get('location'),origin);
    assert.equal(destination.origin,new URL(origin).origin);
    assert.equal(destination.pathname,'/');
    assert.equal(destination.searchParams.get('layers'),'sources');
  });
}

test('hosted source status honestly reports the unconfigured archive without credentials', async () => {
  const response = await fetch(origin + '/api/source-pipeline/status');
  assert.equal(response.status,200);
  const body = await response.json();
  assert.equal(body.limitBytes,80_000_000_000); assert.equal(body.configured,false);
  assert.equal(body.releaseState,'unreleased'); assert.equal(body.usedBytes,null);
  assert.equal(body.sources.length,3);
  assert.doesNotMatch(JSON.stringify(body),/DB_PASSWORD|SESSION_KEY|CLIENT_SECRET|Bearer/);
});
for (const [path,method] of [['/api/source-pipeline/captures','GET'],['/api/source-pipeline/run','POST'],['/api/source-pipeline/control?action=resume','POST']]) {
  test('archive authority is denied to anonymous and forged staff requests: '+path,async()=>{
    const response=await fetch(origin+path,{method,headers:{'x-role':'admin','oai-authenticated-user-id':'203533328',Origin:'https://kansasfrontiermatrix.com'}});
    assert.equal(response.status,401);
  });
}

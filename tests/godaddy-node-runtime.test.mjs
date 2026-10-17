import test from "node:test";
import assert from "node:assert/strict";
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {join} from 'node:path';

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
test('every advertised browser module is served and staged with its exact build bytes',async()=>{
 const home=await (await fetch(origin)).text();
 const paths=[...new Set([...home.matchAll(/<link\b[^>]*>/g)].filter(match=>/rel="modulepreload"/.test(match[0])).map(match=>/href="([^"]+)"/.exec(match[0])?.[1]).filter(Boolean))];
 assert.ok(paths.length>0);
 for(const path of paths){
  assert.match(path,/^\/assets\/[A-Za-z0-9_.-]+\.js$/);
  const response=await fetch(origin+path);assert.equal(response.status,200,path);assert.match(response.headers.get('content-type'),/javascript/,path);
  const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
  const expected=await readFile(join('dist/client',path));
  assert.equal(sha(Buffer.from(await response.arrayBuffer())),sha(expected),path);
  assert.equal(sha(await readFile(join('public',path))),sha(expected),'staged '+path);
 }
});
test("hosted AI endpoint is present without requiring the owner's PC", async () => {
  const response = await fetch(origin + "/api/ai/status");
  assert.equal(response.status, 200);
  const status = await response.json();
  assert.equal(status.requiresLogin, false);
  assert.equal(status.configured, false);
  const home = await (await fetch(origin)).text();
  assert.match(home, /HOSTED AI/);
  assert.match(home, /No account is needed for chat/);
  assert.doesNotMatch(home, /OLLAMA · YOUR PC|PC offline/);
});
test("public crawler files are served with their text and XML media types", async () => {
  for (const [path, mediaType, expected] of [
    ["/robots.txt", "text/plain", "Sitemap: https://kansasfrontiermatrix.com/sitemap.xml"],
    ["/sitemap.xml", "application/xml", "<loc>https://kansasfrontiermatrix.com/about</loc>"],
  ]) {
    const response = await fetch(origin + path);
    assert.equal(response.status, 200);
    assert.ok(response.headers.get("content-type").startsWith(mediaType));
    assert.ok((await response.text()).includes(expected));
    const head = await fetch(origin + path, { method: "HEAD" });
    assert.equal(head.status, 200);
    assert.equal(await head.text(), "");
  }
  const robots = await (await fetch(origin + "/robots.txt")).text();
  assert.match(robots, /^Disallow: \/api\//m);
  assert.match(robots, /^Disallow: \/source-operations/m);
});
test("public metadata identifies the GoDaddy domain without changing the Sites snapshot", async () => {
  const home = await (await fetch(origin)).text();
  assert.match(home, /https:\/\/kansasfrontiermatrix\.com\/og-guided\.png/);
  const about = await (await fetch(origin + "/about")).text();
  assert.match(about, /<link rel="canonical" href="https:\/\/kansasfrontiermatrix\.com\/about"/);
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

import test, { before, after } from "node:test";
import assert from "node:assert/strict";
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {join} from 'node:path';
import {request as httpRequest} from 'node:http';
import {request as httpsRequest} from 'node:https';
import {installPublicDelivery} from '../server/browser-headers.mjs';

// Run against the production build, not a source-text or mocked auth check.
// CI supplies a separate startup process; a plain `npm test` owns an ephemeral
// listener so it exercises the same HTTP boundary without a hidden prerequisite.
let origin = process.env.KFM_NODE_TEST_ORIGIN;
let managedServer;
const previousNodeEnv = process.env.NODE_ENV;
before(async () => {
  if (origin) return;
  process.env.NODE_ENV = 'production';
  const {startProdServer} = await import('vinext/server/prod-server');
  const started = await startProdServer({port: 0, host: '127.0.0.1'});
  managedServer = started.server;
  installPublicDelivery(managedServer);
  origin = `http://127.0.0.1:${started.port}`;
});
after(async () => {
  if (process.env.KFM_NODE_TEST_ORIGIN) return;
  try {
    if (managedServer) {
      managedServer.closeAllConnections();
      await new Promise((resolve, reject) => managedServer.close(error => error ? reject(error) : resolve()));
    }
  } finally {
    if (previousNodeEnv === undefined) delete process.env.NODE_ENV;
    else process.env.NODE_ENV = previousNodeEnv;
  }
});
const proxyRequest = (path, headers) => new Promise((resolve, reject) => {
  const url = new URL(path, origin);
  const request = (url.protocol === 'https:' ? httpsRequest : httpRequest)(url, { headers }, response => {
    const chunks = []; let bytes = 0;
    response.on('data', chunk => {
      bytes += chunk.length;
      if (bytes > 2 * 1024 * 1024) request.destroy(new Error('TEST_RESPONSE_TOO_LARGE'));
      else chunks.push(chunk);
    });
    response.on('error', reject);
    response.on('end', () => resolve({ status: response.statusCode, headers: response.headers, text: Buffer.concat(chunks).toString('utf8') }));
  });
  const timer = setTimeout(() => request.destroy(new Error('TEST_RESPONSE_TIMEOUT')), 10000);
  request.on('close', () => clearTimeout(timer));
  request.on('error', reject); request.end();
});

test('published host and forwarding headers serve both the map and build identity', async () => {
  for (const headers of [
    { Host: 'kansasfrontiermatrix.com' },
    { Host: 'urdng3v1vk.c38.airoapp.ai' },
    { Host: 'urdng3v1vk.preview.c38.airoapp.ai' },
    { Host: '127.0.0.1:20011', 'X-Forwarded-Host': 'kansasfrontiermatrix.com', 'X-Forwarded-Proto': 'https' },
  ]) {
    const home = await proxyRequest('/', headers);
    assert.equal(home.status, 200); assert.match(home.text, /Kansas Frontier Matrix/);
    const build = await proxyRequest('/api/build', headers);
    assert.equal(build.status, 200); assert.equal(JSON.parse(build.text).application, 'urdng3v1vk');
  }
});

test('published www requests retain the fixed HTTPS apex redirect', async () => {
  for (const headers of [{ Host: 'www.kansasfrontiermatrix.com' },
    { Host: '127.0.0.1:20011', 'X-Forwarded-Host': 'www.kansasfrontiermatrix.com' }]) {
    const result = await proxyRequest('/about?from=proxy', headers);
    assert.equal(result.status, 308);
    assert.equal(result.headers.location, 'https://kansasfrontiermatrix.com/about?from=proxy');
  }
});
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
  const page = await fetch(origin);
  assert.equal(page.status, 200);
  const home = await page.text();
  assert.match(home, /id="qwen-map-panel"/);
  assert.match(home, /Chat with KFM/);
  assert.doesNotMatch(home, /No account is needed for chat|No login needed/);
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
  assert.doesNotMatch(robots, /^Disallow: \/source-operations/m);
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
    assert.equal(response.status, path === "/api/data-submissions" ? 404 : 401);
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
for (const [path,method,status] of [['/api/source-pipeline/captures','GET',404],['/api/source-pipeline/run','POST',401],['/api/source-pipeline/control?action=resume','POST',401]]) {
  test('archive authority is denied to anonymous and forged staff requests: '+path,async()=>{
    const response=await fetch(origin+path,{method,headers:{'x-role':'admin','oai-authenticated-user-id':'203533328',Origin:'https://kansasfrontiermatrix.com'}});
    assert.equal(response.status,status);
  });
}

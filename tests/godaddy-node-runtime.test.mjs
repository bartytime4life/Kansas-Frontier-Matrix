import test, { before, after } from "node:test";
import assert from "node:assert/strict";
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {join} from 'node:path';
import {createServer,request as httpRequest} from 'node:http';
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


// These are real static bytes from the existing production build. The MIME
// boundary must not take over the pinned framework's cache/range/file server.
test('welcome WebM GET, HEAD and Range requests preserve built assets with video MIME and nosniff',async()=>{
 const fingerprints=JSON.parse(await readFile('scripts/welcome-demos/runtime-assets.json','utf8'));
 const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
 for(const path of ['/welcome/demos/weather-1.webm','/welcome/motion/clouds-hd.webm']){
  const expected=await readFile(join('dist/client',path));
  assert.equal(sha(expected),sha(await readFile(join('public',path))),'built/public identity '+path);
  if(path.includes('/demos/'))assert.equal(sha(expected),fingerprints.files.find(file=>file.path===path).sha256,'published demo fingerprint');
  const get=await fetch(origin+path,{signal:AbortSignal.timeout(10000)});
  assert.equal(get.status,200);assert.equal(get.headers.get('content-type'),'video/webm');assert.equal(get.headers.get('x-content-type-options'),'nosniff');
  assert.equal(Number(get.headers.get('content-length')),expected.length);assert.equal(sha(Buffer.from(await get.arrayBuffer())),sha(expected),'GET bytes '+path);
  assert.equal(get.headers.get('cache-control'),'no-transform','existing public delivery policy is preserved');assert.ok(get.headers.get('etag'));
  const head=await fetch(origin+path,{method:'HEAD',signal:AbortSignal.timeout(10000)});
  assert.equal(head.status,200);assert.equal(head.headers.get('content-type'),'video/webm');assert.equal(head.headers.get('x-content-type-options'),'nosniff');
  for(const name of ['content-length','etag','cache-control'])assert.equal(head.headers.get(name),get.headers.get(name),name+' retained on HEAD');
  assert.equal((await head.arrayBuffer()).byteLength,0,'HEAD never streams a body');
  const ranged=await fetch(origin+path,{headers:{Range:'bytes=0-127'},signal:AbortSignal.timeout(10000)});
  // This pinned framework ignores Range and returns the complete 200 response.
  // Preserve that behavior; MIME repair must not fabricate partial delivery.
  assert.equal(ranged.status,200);assert.equal(ranged.headers.get('content-range'),null);
  assert.equal(ranged.headers.get('content-type'),'video/webm');assert.equal(ranged.headers.get('x-content-type-options'),'nosniff');
  for(const name of ['content-length','etag','cache-control'])assert.equal(ranged.headers.get(name),get.headers.get(name),name+' retained for Range');
  assert.equal(sha(Buffer.from(await ranged.arrayBuffer())),sha(expected),'Range retains framework full bytes');
  const rangeHead=await fetch(origin+path,{method:'HEAD',headers:{Range:'bytes=0-127'},signal:AbortSignal.timeout(10000)});
  assert.equal(rangeHead.status,200);assert.equal(rangeHead.headers.get('content-type'),'video/webm');assert.equal(rangeHead.headers.get('content-length'),get.headers.get('content-length'));assert.equal((await rangeHead.arrayBuffer()).byteLength,0);
  const conditional=await fetch(origin+path,{headers:{'If-None-Match':get.headers.get('etag')},signal:AbortSignal.timeout(10000)});
  assert.equal(conditional.status,304);assert.equal(conditional.headers.get('content-type'),null,'304 keeps framework no-content metadata');assert.equal(conditional.headers.get('etag'),get.headers.get('etag'));assert.equal((await conditional.arrayBuffer()).byteLength,0);
  const query=await fetch(origin+path+'?download=1',{method:'HEAD',signal:AbortSignal.timeout(10000)});assert.equal(query.status,200);assert.equal(query.headers.get('content-type'),'video/webm');
 }
});

test('welcome video MIME correction leaves real errors, encoded paths, other formats and methods unchanged',async()=>{
 const missing=await fetch(origin+'/welcome/demos/not-a-real-demo.webm',{signal:AbortSignal.timeout(10000)});
 assert.equal(missing.status,404);assert.notEqual(missing.headers.get('content-type'),'video/webm');assert.equal(missing.headers.get('x-content-type-options'),'nosniff');await missing.arrayBuffer();
 const poster=await fetch(origin+'/welcome/demos/weather-1.jpg',{method:'HEAD',signal:AbortSignal.timeout(10000)});
 assert.equal(poster.status,200);assert.match(poster.headers.get('content-type'),/^image\/jpeg/);
 const encoded=await fetch(origin+'/welcome/demos/weather%2D1.webm',{method:'HEAD',signal:AbortSignal.timeout(10000)});
 assert.equal(encoded.status,200);assert.equal(encoded.headers.get('content-type'),'application/octet-stream','only exact safe welcome paths receive correction');
 const post=await fetch(origin+'/welcome/demos/weather-1.webm',{method:'POST',signal:AbortSignal.timeout(10000)});
 assert.notEqual(post.headers.get('content-type'),'video/webm','non-GET/HEAD methods remain framework-owned');await post.arrayBuffer();
});

test('successful welcome video header commit handles Node overloads without changing range, cache, status or raw headers',async t=>{
 const body=Buffer.from('1a45dfa3','hex');
 const frameworkHeaders={'cOnTeNt-TyPe':'application/octet-stream','Content-Length':'4','Content-Range':'bytes 0-3/8','Cache-Control':'public, max-age=37','Accept-Ranges':'bytes'};
 const fixture=createServer((request,response)=>{
  const mode=new URL(request.url,'http://fixture.test').searchParams.get('mode');
  response.setHeader('Content-Type','application/octet-stream');
  if(mode==='error'){response.writeHead(404,{'Content-Type':'application/json','Content-Length':'4'});response.end('null');return;}
  if(mode==='implicit'){response.setHeader('Content-Length','4');response.end(body);return;}
  if(mode==='preset'){response.writeHead(200);response.end(body);return;}
  if(mode==='raw')response.writeHead(206,'KFM partial',['CONTENT-TYPE','application/octet-stream','Content-Type','text/plain','Content-Length','4','Content-Range','bytes 0-3/8','Cache-Control','public, max-age=37','Accept-Ranges','bytes','Set-Cookie','a=1','Set-Cookie','b=2']);
  else if(mode==='reason')response.writeHead(206,'KFM partial',frameworkHeaders);
  else response.writeHead(206,frameworkHeaders);
  response.end(body);
 });
 installPublicDelivery(fixture);
 await new Promise(resolve=>fixture.listen(0,'127.0.0.1',resolve));
 t.after(async()=>{fixture.closeAllConnections();await new Promise((resolve,reject)=>fixture.close(error=>error?reject(error):resolve()));});
 const base=`http://127.0.0.1:${fixture.address().port}`;
 for(const mode of ['object','reason','raw','preset','implicit'])for(const method of ['GET','HEAD']){
  const response=await fetch(base+'/welcome/demos/test-clip.webm?mode='+mode,{method,signal:AbortSignal.timeout(10000)});
  assert.equal(response.status,['preset','implicit'].includes(mode)?200:206);assert.equal(response.headers.get('content-type'),'video/webm');assert.equal(response.headers.get('x-content-type-options'),'nosniff');
  if(!['preset','implicit'].includes(mode)){
   assert.equal(response.headers.get('content-range'),'bytes 0-3/8');assert.equal(response.headers.get('cache-control'),'public, max-age=37');assert.equal(response.headers.get('accept-ranges'),'bytes');assert.equal(response.headers.get('content-length'),'4');
  }
  if(mode==='reason'||mode==='raw')assert.equal(response.statusText,'KFM partial','reason phrase preserved');
  if(mode==='raw')assert.deepEqual(response.headers.getSetCookie(),['a=1','b=2'],'unrelated duplicate raw headers retained');
  assert.deepEqual(Buffer.from(await response.arrayBuffer()),method==='HEAD'?Buffer.alloc(0):body,'body bytes preserved');
 }
 assert.equal(frameworkHeaders['cOnTeNt-TyPe'],'application/octet-stream','caller header object is not mutated');
 for(const [path,method]of [['/unrelated/test-clip.webm','GET'],['/welcome/demos/nested/test-clip.webm','GET'],['/welcome/demos/test.clip.webm','GET'],['/welcome/demos/test%2Dclip.webm','GET'],['/welcome/demos/test-clip.webm','POST']]){
  const response=await fetch(base+path+'?mode=object',{method,signal:AbortSignal.timeout(10000)});assert.equal(response.status,206);assert.equal(response.headers.get('content-type'),'application/octet-stream',`${method} ${path} is outside MIME repair`);await response.arrayBuffer();
 }
 const error=await fetch(base+'/welcome/demos/missing.webm?mode=error',{signal:AbortSignal.timeout(10000)});assert.equal(error.status,404);assert.equal(error.headers.get('content-type'),'application/json');assert.equal(await error.text(),'null');
});

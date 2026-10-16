import test from 'node:test';
import assert from 'node:assert/strict';
import { get } from 'node:http';
import { startProdServer } from 'vinext/server/prod-server';
import { installPublicDelivery } from '../server/browser-headers.mjs';

test('built Node responses carry browser policy, correct canonicals and public privacy',async(t)=>{
  const {server,port}=await startProdServer({port:0,host:'127.0.0.1',outDir:'dist'});
  installPublicDelivery(server);
  t.after(()=>new Promise(resolve=>{server.closeAllConnections();server.close(resolve);}));
  const origin=`http://127.0.0.1:${port}`;
  const withHost=(path,host)=>new Promise((resolve,reject)=>{
    get(origin+path,{headers:{Host:host}},response=>{response.resume();response.on('end',()=>resolve({status:response.statusCode,location:response.headers.location}));}).on('error',reject);
  });
  for (const path of ['/', '/about?view=guide', '/api/pc-ai/status']) {
    const response=await withHost(path,'www.kansasfrontiermatrix.com');
    assert.equal(response.status,308,path);
    assert.equal(response.location,'https://kansasfrontiermatrix.com'+path,path);
  }
  const lookalike=await withHost('/','wwwXkansasfrontiermatrixXcom');
  assert.notEqual(lookalike.status,308);
  for(const path of ['/','/about','/privacy','/robots.txt','/sitemap.xml','/favicon.svg','/missing-page-check','/%ZZ','/api/data-submissions']){
    const response=await fetch(origin+path);
    assert.equal(response.headers.get('strict-transport-security'),'max-age=86400',path);
    assert.equal(response.headers.get('x-content-type-options'),'nosniff',path);
    assert.ok(response.headers.get('permissions-policy')?.includes('geolocation=(self)'),path);
    const policy=response.headers.get('content-security-policy');
    assert.ok(policy?.includes("frame-ancestors 'self' https://host.godaddy.com"),path);
    assert.ok(policy.includes("object-src 'none'"),path);
    const body=await response.text();
    if(path==='/')assert.ok(response.headers.get('link')?.includes('<https://kansasfrontiermatrix.com/>; rel="canonical"'));
    if(path==='/about'||path==='/privacy'){
      assert.equal(response.status,200,path);
      assert.ok(body.includes(`href="https://kansasfrontiermatrix.com${path}"`),path);
      assert.ok(!response.headers.get('link')?.includes('rel="canonical"'),path);
      assert.ok(body.includes('Andy.barta.pro@gmail.com'),path);
      assert.ok(response.headers.get('cache-control')?.includes('no-transform'),path);
    }
    if(path==='/sitemap.xml')assert.ok(body.includes('<loc>https://kansasfrontiermatrix.com/privacy</loc>'));
    if(path==='/api/data-submissions')assert.equal(response.status,401);
    if(path==='/%ZZ')assert.equal(response.status,400);
  }
});

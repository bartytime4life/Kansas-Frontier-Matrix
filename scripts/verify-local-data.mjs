#!/usr/bin/env node
// Read-only production acceptance probe. Sequential small pages; never contacts worker/admin routes.
// Usage: node scripts/verify-local-data.mjs [https://kansasfrontiermatrix.com]
import assert from 'node:assert/strict';
const origin=new URL(process.argv[2]??'https://kansasfrontiermatrix.com');
if(origin.protocol!=='https:'||origin.username||origin.password||origin.pathname!=='/'||origin.search||origin.hash)throw new Error('Use an HTTPS origin');
const evidence=[],failures=[];
async function get(path){
 const start=Date.now(),response=await fetch(new URL(path,origin),{redirect:'error',cache:'no-store',signal:AbortSignal.timeout(25000)});
 const text=await response.text();let body;try{body=JSON.parse(text);}catch{body=text;}
 const item={path,status:response.status,at:new Date().toISOString(),ms:Date.now()-start,bytes:Buffer.byteLength(text),headers:Object.fromEntries(['cache-control','content-type','date','cf-cache-status'].map(k=>[k,response.headers.get(k)])),body};
 evidence.push(item);return item;
}
function check(label,fn){try{fn();}catch(error){failures.push({label,error:error.message});}}
const catalog=await get('/api/local-data'),build=await get('/api/build');
check('catalog',()=>{assert.equal(catalog.status,200);assert.equal(catalog.body.datasets.length,17);assert.equal(catalog.body.online,true);});
const queries={
 'storm-events':'county=Riley','ghcn-stations':'name=Wichita','ghcn-daily':'station=USW00003928&element=TMAX,PRCP&from=2025-07-01',
 'ghcndex-indices':'','ghcndex':'station=USW00003928&index=TXx&period=annual','asos-5min':'station=KTOP&from=2000-12-25&to=2000-12-25',
 'wind-stations':'name=Wichita','wind-observations':'station=ICT','wind-daily':'station=ICT&from=2025-06-01&to=2025-06-30',
 'prism-county':'variable=tmax&county=Riley&from=2024-01&to=2024-12','tiger-features':'layer=county&id=20161',
 'nwm-reaches':'name=Smoky%20Hill','nws-alerts':'','usgs-earthquakes':'','usgs-streamflow-sites':''
};
const samples=new Map();
async function sample(id,query){
 const path='/api/local-data/'+id+'?'+query+(id==='ghcndex-indices'?'':'&limit=2');
 const item=await get(path);samples.set(id,item);
 check(id,()=>{assert.equal(item.status,200);assert.equal(item.body.dataset,id);assert.equal(item.body.count,(item.body.rows??item.body.events).length);assert.ok(item.body.count>0);assert.ok(item.bytes<=1000000);assert.ok(Number.isFinite(Date.parse(item.body.generatedAt)));assert.ok(['live','fresh','stale'].includes(item.body.cache.state));assert.deepEqual(item.body.source,catalog.body.datasets.find(d=>d.id===id).source);});
 return item;
}
for(const [id,query] of Object.entries(queries))await sample(id,query);
await sample('nwm-streamflow','feature='+samples.get('nwm-reaches').body.rows[0].featureId);
await sample('usgs-streamflow','site='+samples.get('usgs-streamflow-sites').body.rows[0].site);
for(const id of ['nwm-reaches','nwm-streamflow'])check(id+' limitations',()=>{assert.match(samples.get(id).body.source.notes,/has not admitted/);assert.match(samples.get(id).body.source.notes,/pending/);});
check('NWS historical disclaimer',()=>assert.match(samples.get('nws-alerts').body.source.notes,/not a live alert feed/i));
check('GHCNDEX beta',()=>assert.match(samples.get('ghcndex').body.source.notes,/beta/i));
check('PRISM acquisition caveat',()=>assert.match(samples.get('prism-county').body.source.notes,/acquisition dates are not yet verified/i));
const again=await get(samples.get('nws-alerts').path);
check('cache repeat preserves answer',()=>{assert.deepEqual(again.body.rows,samples.get('nws-alerts').body.rows);assert.equal(again.body.generatedAt,samples.get('nws-alerts').body.generatedAt);});
const first=await get('/api/local-data/nws-alerts?limit=1&offset=0'),second=await get('/api/local-data/nws-alerts?limit=1&offset=1');
check('pagination',()=>assert.deepEqual([first.body.rows[0],second.body.rows[0]],again.body.rows));
for(const [path,status] of [
 ['/api/local-data/unknown',404],['/api/local-data/ghcn-daily',400],['/api/local-data/tiger-features?layer=roads',400],
 ['/api/local-data/nws-alerts?limit=51',400],['/api/local-data/nws-alerts?offset=-1',400],['/api/local-data/nws-alerts?offset=1001',400],
 ['/api/local-data/nws-alerts?bogus=1',400],['/api/local-data/nwm-reaches?bbox=-102,37,-94,40',400],
 ['/api/local-data/ghcn-daily?station=USW00003928&from=2025-02-30',400],['/api/local-data/nws-alerts?limit=1&limit=2',400]
 ]){const item=await get(path);check(path,()=>assert.equal(item.status,status));}
console.log(JSON.stringify({origin:origin.origin,build:build.body,failures,evidence},null,2));
process.exitCode=failures.length?1:0;

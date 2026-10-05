import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
import path from 'node:path';
import test from 'node:test';
import ts from 'typescript';
let js=ts.transpileModule(await readFile('app/api/hydrology/streamflow/route.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText.replace('from "next/server"',`from ${JSON.stringify(pathToFileURL(path.resolve('node_modules/next/server.js')).href)}`);
const {GET}=await import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
const time=new Date(Date.now()-600000).toISOString();
const ids=Array.from({length:100},(_,i)=>`USGS-${String(6800000+i).padStart(8,'0')}`);
const observation=(id,value=10)=>({type:'Feature',id,geometry:{type:'Point',coordinates:[-98,38]},properties:{time_series_id:id,monitoring_location_id:id,parameter_code:'00060',statistic_id:'00011',time,value,unit_of_measure:'ft^3/s',approval_status:'Provisional',qualifier:null,last_modified:time}});
const metadata=id=>({type:'Feature',id,geometry:{type:'Point',coordinates:[-98,38]},properties:{id,agency_code:'USGS',monitoring_location_number:id.slice(5),monitoring_location_name:id,site_type_code:'ST',hydrologic_unit_code:null,county_name:null,drainage_area:null,contributing_drainage_area:null}});
const collection=features=>Response.json({type:'FeatureCollection',features,numberReturned:features.length,links:[],timeStamp:time});
const request=()=>({nextUrl:new URL('https://local/api/hydrology/streamflow?mode=network&range=24h')});
async function run(failed=false){
 const original=globalThis.fetch;const batches=[];
 globalThis.fetch=async input=>{
  const url=new URL(input);
  if(url.pathname.includes('latest-continuous')){const [a,b]=url.searchParams.get('datetime').split('/');assert.equal(Date.parse(b)-Date.parse(a),30*86400000);return collection(ids.map(id=>observation(id)));}
  if(url.pathname.includes('monitoring-locations'))return collection(url.searchParams.get('monitoring_location_number').split(',').map(n=>metadata('USGS-'+n)));
  const requested=url.searchParams.get('monitoring_location_id').split(',');batches.push(requested);assert.ok(requested.length<=48);
  if(failed&&requested.includes(ids[50]))return new Response('',{status:503});
  return collection(requested.filter(id=>id!==ids[99]).map(id=>observation(id,id===ids[0]?0:10)));
 };
 try{const response=await GET(request());assert.equal(response.status,200);return{body:await response.json(),batches};}finally{globalThis.fetch=original;}
}
test('network retains more than 72 gauges, true zero and silent gauge metadata',async()=>{
 const{body,batches}=await run();assert.equal(body.stations.length,100);assert.equal(body.observations.length,99);assert.equal(batches.length,3);assert.equal(body.observations.find(o=>o.stationId===ids[0]).value,0);assert.equal(body.partial,true);assert.equal(body.truncated,false);assert.ok(body.stations.some(s=>s.stationId===ids[99]));
});
test('failed observation batch keeps its locations and healthy groups without invented readings',async()=>{
 const{body}=await run(true);assert.equal(body.stations.length,100);assert.equal(body.observations.length,51);assert.equal(body.partial,true);assert.equal(body.truncated,false);assert.equal(body.observations.some(o=>o.stationId===ids[50]),false);assert.match(body.limitation,/batches failed/);
});

test('provider rate limits are disclosed and repeated requests respect cooldown',async()=>{
 const original=globalThis.fetch;let calls=0;
 globalThis.fetch=async()=>{calls++;return new Response('',{status:429,headers:{'Retry-After':'600'}});};
 try {
  const first=await GET(request());assert.equal(first.status,429);
  assert.equal((await first.json()).code,'USGS_STREAMFLOW_RATE_LIMITED');
  assert.ok(Number(first.headers.get('Retry-After'))>=599);
  assert.equal((await GET(request())).status,429);assert.equal(calls,1);
 } finally {globalThis.fetch=original;}
});

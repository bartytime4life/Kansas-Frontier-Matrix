/** Offline CPU benchmark. No provider, browser, GPU or production-capacity claim. */
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {performance} from 'node:perf_hooks';
import ts from 'typescript';
const text=await readFile(new URL('../app/kansas-sky.ts',import.meta.url),'utf8');
const sky=await import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(text,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`);
const start=Date.parse('2026-11-03T12:00:00Z'),b=new sky.SkyBuffer(),ingest=[];
for(let i=0;i<80;i++){
 const at=start+i*10000, records=Array.from({length:3000},(_,j)=>({hex:(j+1).toString(16).padStart(6,'0'),callsign:null,registration:null,type:null,category:null,lon:-100+j%100*.04,lat:37+Math.floor(j/100)*.08,onGround:false,altBaroFt:1000+j*10,altGeomFt:null,groundSpeedKt:100,trackDeg:90,verticalRateFpm:null,squawk:null,emergency:null,military:false,positionAgeS:0,observedAt:new Date(at).toISOString(),positionMethod:'adsb_icao'}));
 const before=performance.now();b.ingest({retrievedAt:new Date(at).toISOString(),provider:{id:'adsb-lol'},records});ingest.push(performance.now()-before);
}
const samples=[],trails=[];let shown,geometry;
for(let i=0;i<100;i++){
 let before=performance.now();shown=sky.samplesAt(b.tracks(),start+785000);samples.push(performance.now()-before);
 before=performance.now();geometry=sky.trailSegments(b.tracks(),start+785000);trails.push(performance.now()-before);
}
const count=[...b.tracks().values()].reduce((sum,p)=>sum+p.length,0),vertices=geometry.reduce((sum,p)=>sum+p.points.length,0);
assert.equal(shown.length,3000);assert.ok(count<=sky.SKY_MAX_REGIONAL_POINTS);assert.ok(vertices<=sky.SKY_MAX_TRAIL_POINTS);
const stats=v=>{v.sort((a,b)=>a-b);return {medianMs:+v[Math.floor(v.length*.5)].toFixed(3),p95Ms:+v[Math.floor(v.length*.95)].toFixed(3),maxMs:+v.at(-1).toFixed(3)}};
console.log(JSON.stringify({scope:'synthetic Node CPU only',node:process.version,aircraft:shown.length,retainedPoints:count,trailPoints:vertices,ingest:stats(ingest),sample:stats(samples),trails:stats(trails)},null,2));

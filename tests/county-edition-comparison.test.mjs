import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const source=await readFile(new URL('../app/county-edition-comparison.ts',import.meta.url),'utf8');
const javascript=ts.transpileModule(source,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.ESNext}}).outputText;
const {decodeCountyEdition,compareCountyEditions}=await import(`data:text/javascript;base64,${Buffer.from(javascript).toString('base64')}`);
function fixture(edition,population=100){return {edition,source:`https://tigerweb.geo.census.gov/synthetic-fixture-${edition}`,retrievedAt:'2026-01-01T00:00:00Z',limitation:'Synthetic fixture, never served to users.',data:{type:'FeatureCollection',features:Array.from({length:105},(_,i)=>({properties:{geoid:`20${String(i*2+1).padStart(3,'0')}`,name:`Synthetic county ${i}`,vintage:edition,evidenceRole:'EXTERNAL_CONTEXT_ONLY',population,housingUnits:50}}))}};}
test('a complete FIPS join compares exact counts and reverses A/B without rewriting source data',()=>{
 const rawA=fixture('2010',100),rawB=fixture('2020',125),before=JSON.stringify([rawA,rawB]);
 const a=decodeCountyEdition(rawA,'2010'),b=decodeCountyEdition(rawB,'2020');
 const statewide=compareCountyEditions(a,b);assert.equal(statewide.matchedCounties,105);assert.deepEqual(statewide.population,{a:10500,b:13125,delta:2625,percent:25});
 const county=compareCountyEditions(a,b,'20001');assert.equal(county.matchedCounties,1);assert.equal(county.population.delta,25);
 const reversed=compareCountyEditions(b,a,'20001');assert.equal(reversed.population.delta,-25);assert.equal(reversed.population.percent,-20);
 assert.equal(statewide.evidenceRole,'EXTERNAL_CONTEXT_ONLY');assert.equal(statewide.publicationState,'NOT_KFM_RELEASE');assert.equal(statewide.sources[0].retrievedAt,rawA.retrievedAt);
 assert.equal(JSON.stringify([rawA,rawB]),before);
});
test('missing source counts do not become zero; zero denominators never invent percentage changes',()=>{
 const a=fixture('2010',0),b=fixture('2020',1);
 assert.equal(compareCountyEditions(decodeCountyEdition(a,'2010'),decodeCountyEdition(b,'2020'),'20001').population.percent,null);
 a.data.features[0].properties.population=null;
 const result=compareCountyEditions(decodeCountyEdition(a,'2010'),decodeCountyEdition(b,'2020'));
 assert.equal(result.population.a,null);assert.equal(result.population.delta,null);assert.equal(result.population.percent,null);assert.equal(result.population.b,105);assert.equal(result.housingUnits.delta,0);
});
test('incomplete, duplicate, mismatched, incorrectly dated or untrusted-source editions fail closed',()=>{
 for(const change of [v=>v.data.features.pop(),v=>v.data.features[1].properties.geoid='20001',v=>v.data.features[0].properties.vintage='2020',v=>v.data.features[0].properties.evidenceRole='RELEASED',v=>v.source='javascript:alert(1)',v=>v.retrievedAt='unknown',v=>v.data.features[0].properties.population=-1,v=>v.data.features[0].properties.population='100']){
  const v=fixture('2010');change(v);assert.throws(()=>decodeCountyEdition(v,'2010'));
 }
 const a=decodeCountyEdition(fixture('2010'),'2010'),b=decodeCountyEdition(fixture('2020'),'2020');b.rows[0].geoid='20999';assert.throws(()=>compareCountyEditions(a,b));assert.throws(()=>compareCountyEditions(a,a,'20999'));
});
test('aggregate precision overflow is withheld instead of displayed as an exact count',()=>{
 const a=decodeCountyEdition(fixture('2010',Number.MAX_SAFE_INTEGER),'2010'),b=decodeCountyEdition(fixture('2020',1),'2020');assert.throws(()=>compareCountyEditions(a,b),/exact integer range/);
});

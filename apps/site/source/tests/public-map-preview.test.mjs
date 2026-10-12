import assert from 'node:assert/strict';
import test from 'node:test';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
const compile=async file=>ts.transpileModule(await readFile(new URL('../app/'+file,import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const moduleURL=s=>`data:text/javascript;base64,${Buffer.from(s).toString('base64')}`;
const modelURL=moduleURL(await compile('public-map-preview-model.ts'));
const model=await import(modelURL);
const boundedURL=moduleURL(await compile('bounded-json.ts'));
const {GET}=await import(moduleURL((await compile('api/public-maps/preview/route.ts')).replace('"../../../bounded-json"',JSON.stringify(boundedURL)).replace('"../../../public-map-preview-model"',JSON.stringify(modelURL))));
const bounds=[-95.1,37.3,-94.7,37.7];
const point=(id=1,coordinates=[-94.9,37.5])=>({type:'Feature',geometry:{type:'Point',coordinates},properties:{objectid:id,documentnumber:34,mapscale:100}});
const polygon=(id=1)=>({type:'Feature',geometry:{type:'Polygon',coordinates:[[[-95,37.4],[-94.8,37.4],[-94.8,37.6],[-95,37.4]]]},properties:{OBJECTID:id,MapUnit:'Qal',Description:'Interpretation'}});
test('preview refuses unbounded areas and arbitrary kinds before network',async()=>{
 const old=globalThis.fetch;let calls=0;globalThis.fetch=async()=>{calls++;throw new Error('unexpected');};
 try {for(const query of ['kind=other&bounds='+bounds,'kind=kgs-m118&bounds=-102,37,-95,40','kind=kgs-m118&bounds=NaN,37,-95,38'])assert.equal((await GET(new Request('http://test/?'+query))).status,400);assert.equal(calls,0);}finally{globalThis.fetch=old;}
});
test('fixed endpoint preview keeps point document identities and map scale units',async()=>{
 const old=globalThis.fetch;let target,options;globalThis.fetch=async(u,o)=>{target=new URL(u);options=o;return Response.json({type:'FeatureCollection',features:[point(1),point(2)]});};
 try {const response=await GET(new Request(`http://test/?kind=osmre-nmmr&bounds=${bounds}`)),body=await response.json();assert.equal(response.status,200);assert.equal(target.hostname,'geodata.osmre.gov');assert.equal(target.searchParams.get('outSR'),'4326');assert.equal(target.searchParams.get('resultRecordCount'),'201');assert.equal(options.redirect,'manual');assert.equal(body.features.length,2);assert.equal(body.features[0].properties.mapscale,100);assert.match(body.source.limitation,/feet per inch/);}finally{globalThis.fetch=old;}
});
test('malformed and duplicate records remain explicit partial coverage',()=>{
 const result=model.parsePublicPreview({type:'FeatureCollection',features:[point(),point(),point(3,[0,0]),{bad:true}]},'osmre-nmmr',bounds);
 assert.equal(result.features.length,1);assert.equal(result.rejected,3);assert.equal(result.partial,true);
 const valid=model.parsePublicPreview({type:'FeatureCollection',features:[polygon()]},'kgs-m118',bounds);assert.equal(valid.features[0].properties.MapUnit,'Qal');assert.equal(valid.partial,false);
 const bad=polygon();bad.geometry.coordinates[0][3]=[-94.5,37.8];assert.equal(model.parsePublicPreview({type:'FeatureCollection',features:[bad]},'kgs-m118',bounds).features.length,0);
});
test('transfer limits are disclosed and response count is capped',()=>{
 const result=model.parsePublicPreview({type:'FeatureCollection',features:Array.from({length:201},(_,i)=>point(i)),properties:{exceededTransferLimit:true}},'osmre-nmmr',bounds);
 assert.equal(result.features.length,200);assert.equal(result.partial,true);
 assert.throws(()=>model.parsePublicPreview({type:'FeatureCollection',features:Array.from({length:202},(_,i)=>point(i))},'osmre-nmmr',bounds));
});
test('upstream redirects, HTML and oversized responses withhold preview',async()=>{
 const old=globalThis.fetch;
 try {for(const make of [()=>Response.redirect('https://unapproved.test'),()=>new Response('<html>Error</html>'),()=>new Response('x'.repeat(4_000_001))]) {globalThis.fetch=async()=>make();assert.equal((await GET(new Request(`http://test/?kind=kgs-m118&bounds=${bounds}`))).status,502);}}finally{globalThis.fetch=old;}
});
test('unknown preparation identities are rejected before reading local files',async()=>{
 const {inspectLocalReview,preparedMapProfile,ALLEN_REVIEW}=await import(moduleURL(await compile('local-geopdf-review.ts')));
 assert.equal(preparedMapProfile(ALLEN_REVIEW.sourceSha256),ALLEN_REVIEW);
 assert.equal(preparedMapProfile('0'.repeat(64)),undefined);
 await assert.rejects(inspectLocalReview([{size:1,arrayBuffer(){throw new Error('must not read');}}],new AbortController().signal,'0'.repeat(64)),/No pinned preparation/);
});

test('CNGM products use separately pinned polygon services and retain interpretation limits', async()=>{
 const old=globalThis.fetch;const targets=[];globalThis.fetch=async(url)=>{targets.push(new URL(url));return Response.json({type:'FeatureCollection',features:[polygon()]});};
 try {for(const kind of ['cngm-earth','cngm-quaternary','cngm-prequaternary','cngm-precambrian']){
  const response=await GET(new Request(`http://test/?kind=${kind}&bounds=${bounds}`)),body=await response.json();assert.equal(response.status,200);assert.equal(body.features.length,1);assert.match(body.source.limitation,/do not establish measured depth/);assert.equal(body.kind,kind);
 }assert.equal(new Set(targets.map(u=>u.pathname)).size,4);assert.ok(targets.every(u=>u.hostname==='services.arcgis.com'&&u.pathname.endsWith('/query')));
 assert.equal((await GET(new Request(`http://test/?kind=__proto__&bounds=${bounds}`))).status,400);
 }finally{globalThis.fetch=old;}
});

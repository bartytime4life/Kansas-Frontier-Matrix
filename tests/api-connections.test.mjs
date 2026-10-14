import assert from "node:assert/strict";import {test} from "node:test";import {PROVIDERS,makePlan,acquire,replay,captureOne,catalog} from "../app/api-connections-runtime/connections.mjs";import {jsonEntity,csvEntity} from "../app/api-connections-runtime/http-runtime.mjs";
const env={NASS_QUICK_STATS_KEY:"nass-fixture-key-0000000000000000",KFM_NASS_TERMS_ACCEPTED:"true",EIA_API_KEY:"eia-fixture-key-0000000000000000",CENSUS_API_KEY:"census-fixture-key-000000000000",AIRNOW_API_KEY:"airnow-fixture-key-000000000000",KFM_AIRNOW_ARCHIVE_AUTHORIZED:"true",EPA_AQS_KEY:"aqs-fixture-key-00000000000000",EPA_AQS_EMAIL:"fixture@example.invalid",KFM_KDOT_RIGHTS_REVIEWED:"true"};
const geo={type:"FeatureCollection",features:[{type:"Feature",id:"fixture",properties:{name:"Synthetic"},geometry:{type:"LineString",coordinates:[[-97.34,37.69],[-97.32,37.71]]}}]};
const csv=(head,row)=>head.join(",")+"\n"+row.map(String).join(",")+"\n";
function payload(id,request,q){
 if(request.preflight==="count")return {count:1};
 if(request.preflight==="metadata")return id==="dasc-imagery"?{extent:{xmin:0},pixelSizeX:0.3}:{type:"Feature Layer",capabilities:"Query"};
 if(request.preflight==="station")return csv(["Location_Identifier","Location_StatePostalCode","Location_TribalLandIndicator"],[q.station,"KS","N"]);
 if(id==="nass-quick-stats")return {data:[{state_alpha:"KS",Value:"(D)",unit_desc:"BU / ACRE",year:q.year}]};
 if(id==="usdm-statistics")return [{mapDate:"2023-12-26",stateAbbreviation:"KS",validStart:"2023-12-26",validEnd:"2024-01-01",statisticFormatID:Number(q.mode),d0:12}];
 if(id==="dasc-imagery"){const b=new Uint8Array(24);b.set([137,80,78,71]);new DataView(b.buffer).setUint32(16,768);new DataView(b.buffer).setUint32(20,768);return b;}
 if(id==="usgs-transect")return q.product==="nldi-process"?geo:{samples:[{locationId:0,location:{x:Number(q.lon),y:Number(q.lat),spatialReference:{wkid:4326}},value:"395.12",resolution:1,attributes:{VerticalDatum:"NAVD88"}}]};
 if(id==="kdot-kanplan")return geo;
 if(id==="planetary-stac")return {...geo,features:[{...geo.features[0],id:"scene-fixture",collection:q.collection,assets:{red:{href:"https://example.invalid/never-fetched.tif"}}}]};
 if(id==="usda-sda")return {Table:[["mukey","hzdept_r","hzdepb_r","awc_r"],["1","0","10","0.15"]]};
 if(id==="osm-overpass")return {elements:[{type:"way",id:1,version:2,timestamp:"2024-01-01T00:00:00Z",tags:{highway:"residential",name:"Fixture"},geometry:[{lon:-97.34,lat:37.69},{lon:-97.33,lat:37.70}]}]};
 if(id==="census-acs")return [["NAME","state","county","B01003_001E","B01003_001M"],["Fixture County, Kansas","20","001","-999999999","12"]];
 if(id==="eia-electricity")return {response:{total:2,data:[{location:"KS",period:"2024-01",generation:"1.2","generation-units":"million kilowatthours"}]}};
 if(id==="noaa-ncei")return [{STATION:q.station,NAME:"WICHITA, KS US",LATITUDE:"37.65",LONGITUDE:"-97.43",DATE:"2024-01-01",TMAX:"35",TMAX_ATTRIBUTES:"flag,source",PRCP:null}];
 if(id==="water-quality-portal")return csv(["Location_Identifier","Location_StatePostalCode","Activity_StartDate","Result_Measure","Result_MeasureUnit","Result_ResultDetectionCondition"],[q.station,"KS","2024-01-01","","mg/l","Not Detected"]);
 if(id==="nrcs-scan")return [{stationTriplet:q.station,data:[{stationElement:{elementCode:"SMS",ordinal:1,heightDepth:-2,durationName:"DAILY",storedUnitCode:"pct",derivedData:true},values:[{date:"2024-01-01",value:10.5,qcFlag:"V",qaFlag:"R",origValue:10.5}]}]}];
 if(id==="air-quality")return q.product==="airnow"?[{StateCode:"KS",AQI:25,DateObserved:"2024-01-01"}]:{Header:[{status:"Success"}],Data:[{state_code:"20",county_code:q.county,arithmetic_mean:2.3,units_of_measure:"Micrograms/cubic meter (LC)"}]};
 if(id==="library-of-congress")return {pagination:{total:12},results:[{id:"https://www.loc.gov/item/fixture/",title:"Fixture map",date:"1871",rights:["Review required"]}]};
 if(id==="iem-asos")return csv(["station","valid","tmpf","sknt","drct","metar"],[q.station,"2024-01-01 01:00","M","5","180","SYNTHETIC"]);
 throw new Error(id);
}
const fetcher=(plan,custom)=>{let i=0;return async(url,options)=>{const r=plan.requests[i++];assert.equal(options.redirect,"manual");assert.equal(options.method,r.method);for(const auth of r.auth??[])assert.equal(new URL(url).searchParams.get(auth.param),env[auth.secret]);const v=custom??payload(plan.sourceId,r,plan.query);return new Response(v instanceof Uint8Array?v:typeof v==="string"?v:JSON.stringify(v),{headers:{"Content-Type":r.format==="png"?"image/png":r.format==="csv"?"text/csv":"application/json"}});};};
assert.equal(PROVIDERS.length,16);
for(const p of PROVIDERS){
 test(p.spec.id+" binds source/query identity and rejects arbitrary parameters",async()=>{const a=await makePlan(p.spec.id,{},1704067200000);const b=await makePlan(p.spec.id,{},1704067200001);assert.equal(a.id,b.id);assert.match(a.id,/^[a-f0-9]{64}$/);await assert.rejects(makePlan(p.spec.id,{url:"http://127.0.0.1/secrets"}),/QUERY_REJECTED/);});
 test(p.spec.id+" captures, replays and detects byte tampering",async()=>{const plan=await makePlan(p.spec.id,{},1704067200000);const result=await acquire(plan,{env,fetcher:fetcher(plan)});const decoded=await replay(result);assert.equal(decoded.view.sourceId,p.spec.id);assert.equal(decoded.receipt.releaseState,"unreleased");for(const secret of Object.values(env).filter(x=>x!=="true"))assert.equal(new TextDecoder().decode(result.bytes).includes(secret),false);const changed={...result,bytes:result.bytes.slice()};changed.bytes[0]^=1;await assert.rejects(replay(changed),/CAPTURE_INTEGRITY_FAILED/);});
 test(p.spec.id+" rejects a mutated request before making a connection",async()=>{const plan=await makePlan(p.spec.id,{},1704067200000);plan.requests[0].url="https://attacker.invalid";await assert.rejects(acquire(plan,{env,fetcher:()=>assert.fail("Network must stay unused")}),/PLAN_INTEGRITY_FAILED/);});
}
test("key and provider consent holds make no network requests",async()=>{for(const p of PROVIDERS.filter(p=>p.spec.secrets||p.spec.confirmations||p.spec.productSecrets)){await assert.rejects(acquire(await makePlan(p.spec.id),{env:{},fetcher:()=>assert.fail("Held source fetched")}),/CREDENTIAL_REQUIRED|PROVIDER_REVIEW_REQUIRED/);}});
test("duplicate keys, nesting, nonfinite JSON and irregular CSV reject",()=>{assert.throws(()=>jsonEntity('{"a":1,"a":2}'),/DUPLICATE_JSON_KEY/);assert.throws(()=>jsonEntity('{"a":1e999}'),/PAYLOAD_REJECTED/);assert.throws(()=>jsonEntity("[".repeat(40)+"0"+"]".repeat(40)),/PAYLOAD_REJECTED/);assert.throws(()=>csvEntity("a,b\n1\n"),/PAYLOAD_REJECTED/);assert.deepEqual(csvEntity('a,b\n"x,y","a""b"\n'),[{a:"x,y",b:'a"b'}]);});
test("preflight count holds a wide query before downloading rows",async()=>{const plan=await makePlan("nass-quick-stats");let calls=0;await assert.rejects(acquire(plan,{env,fetcher:async()=>{calls++;return Response.json({count:5001});}}),/COUNT_REQUIRES_NARROWER_QUERY/);assert.equal(calls,1);});
test("unexpected payload stays invalid and cannot become a replay view",async()=>{const plan=await makePlan("usdm-statistics");const result=await acquire(plan,{env,fetcher:()=>Response.json({unknown:"shape"})});assert.equal(result.receipt.validation,"invalid");await assert.rejects(replay(result));});
test("redirects and body size reject; neither follows a redirect",async()=>{const plan=await makePlan("usdm-statistics");await assert.rejects(acquire(plan,{env,fetcher:()=>new Response(null,{status:302,headers:{Location:"http://127.0.0.1"}})}),/UPSTREAM_UNAVAILABLE/);await assert.rejects(acquire(plan,{env,fetcher:()=>new Response('[]',{headers:{"content-type":"application/json","content-length":String(plan.entityLimitBytes+1)}})}),/RESPONSE_TOO_LARGE/);});
test("AQS is a separate native concentration profile",async()=>{const plan=await makePlan("air-quality",{product:"aqs"});const v=await replay(await acquire(plan,{env,fetcher:fetcher(plan)}));assert.equal(v.view.rows[0].units_of_measure,"Micrograms/cubic meter (LC)");assert.equal(catalog({EPA_AQS_EMAIL:env.EPA_AQS_EMAIL,EPA_AQS_KEY:env.EPA_AQS_KEY}).find(x=>x.id==="air-quality").productStatuses.aqs.configured,true);});
test("NCEI all six products retain native values and flags",async()=>{const p=PROVIDERS.find(x=>x.spec.id==="noaa-ncei");for(const product of p.spec.fields[0].options){const plan=await makePlan(p.spec.id,{product});const v=await replay(await acquire(plan,{env,fetcher:fetcher(plan)}));assert.equal(v.view.rows[0].PRCP,null);assert.equal(v.view.rows[0].TMAX_ATTRIBUTES,"flag,source");}await makePlan(p.spec.id,{product:"global-summary-of-the-year",start:"2020-01-01",end:"2025-12-31"});});
test("capacity, pause and saved-byte readback govern the real capture path",async()=>{const saved=new Map();let released=0;const store={claim:async()=> "token",due:async p=>!saved.has(p.id),reserve:async p=>p.limitBytes+16384,save:async(p,r)=>saved.set(p.id,r),read:async id=>saved.get(id),failure:async()=>{},release:async()=>released++};const plan=await makePlan("usdm-statistics");const one=await captureOne(store,"usdm-statistics",{}, {env,fetcher:fetcher(plan)});assert.equal(one.cached,false);const two=await captureOne(store,"usdm-statistics",{}, {env,fetcher:()=>assert.fail("Cached data re-fetched")});assert.equal(two.cached,true);assert.equal(released,2);await assert.rejects(captureOne({...store,claim:async()=>null},"usdm-statistics",{}, {env}),/PIPELINE_PAUSED_OR_BUSY/);});

test("provider-echoed credentials are redacted before private storage",async()=>{const plan=await makePlan("eia-electricity");const payload={response:{total:1,data:[{location:"KS",period:"2024-01",generation:"1", "generation-units":"million kilowatthours"}]},request:{params:{api_key:env.EIA_API_KEY}}};const result=await acquire(plan,{env,fetcher:()=>Response.json(payload,{headers:{etag:env.EIA_API_KEY}})});assert.equal(new TextDecoder().decode(result.bytes).includes(env.EIA_API_KEY),false);assert.equal(JSON.stringify(result.receipt).includes(env.EIA_API_KEY),false);assert.ok(result.receipt.entityHashes[0].credentialRedactions>=1);assert.notEqual(result.receipt.entityHashes[0].receivedSha256,result.receipt.entityHashes[0].sha256);assert.equal((await replay(result)).view.total,1);});

const echoModes=[['nass-count','nass-quick-stats',{},0,'NASS_QUICK_STATS_KEY'],['nass-data','nass-quick-stats',{},1,'NASS_QUICK_STATS_KEY'],['census-acs','census-acs',{},0,'CENSUS_API_KEY'],['eia-generation','eia-electricity',{},0,'EIA_API_KEY'],['airnow','air-quality',{},0,'AIRNOW_API_KEY'],['epa-aqs','air-quality',{product:'aqs'},0,'EPA_AQS_KEY']];
for(const [mode,id,query,target,key] of echoModes)for(const variant of ['header-parameters','escaped-json'])test(mode+' omits credentials from '+variant+' and stored replay',async()=>{
 const plan=await makePlan(id,query,1704067200000),secret=env[key];let index=0;
 const value=await acquire(plan,{env,fetcher:async()=>{
  const active=index===target,r=plan.requests[index++];let v=payload(id,r,plan.query);
  if(active&&variant==='escaped-json'){
   if(Array.isArray(v)&&Array.isArray(v[0])){v[0].push('echo');for(const row of v.slice(1))row.push(secret);}
   else if(Array.isArray(v))v[0].echo=secret;
   else if(r.preflight)v.echo=secret;
   else if(v.response)v.response.data[0].echo=secret;
   else if(v.Data)v.Data[0].echo=secret;
   else v.data[0].echo=secret;
  }
  let text=JSON.stringify(v);if(active&&variant==='escaped-json'){const escaped=[...secret].map((c,i)=>i%2?'\\u'+c.charCodeAt(0).toString(16).padStart(4,'0'):c).join('');text=text.replace(secret,escaped);}
  return new Response(text,{headers:{'content-type':'application/json'+(active&&variant==='header-parameters'?'; echo='+secret:''),etag:secret,'last-modified':secret}});
 }});
 const replayed=await replay(value),bundle=JSON.parse(new TextDecoder().decode(value.bytes));
 assert.equal(JSON.stringify(value.receipt).includes(secret),false);assert.equal(JSON.stringify(replayed.view).includes(secret),false);
 for(const e of bundle.entities){assert.equal(JSON.stringify(JSON.parse(Buffer.from(e.entityBase64,'base64').toString('utf8'))).includes(secret),false);assert.equal(e.contentType,'application/json');assert.equal(e.etag,'');assert.equal(e.lastModified,'');}
});
test('malformed credentialed JSON is held before any private storage',async()=>{
 let saved=false;const store={claim:async()=> 'fixture',due:async()=>true,reserve:async()=>5000000,save:async()=>{saved=true},failure:async()=>{},release:async()=>{}};
 await assert.rejects(captureOne(store,'eia-electricity',{}, {env,fetcher:()=>new Response('{"bad":"\\\\u0073',{headers:{'content-type':'application/json'}})}),/PAYLOAD_REJECTED/);assert.equal(saved,false);
});
test('redacted JSON property collisions fail closed',async()=>{
 const p=await makePlan('eia-electricity');const v={response:{total:0,data:[]},[env.EIA_API_KEY]:1,'[credential-redacted]':2};
 await assert.rejects(acquire(p,{env,fetcher:()=>Response.json(v)}),/CREDENTIAL_REDACTION_AMBIGUOUS/);
});

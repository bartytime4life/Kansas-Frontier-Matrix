import test from "node:test";
import assert from "node:assert/strict";
import {readFile} from "node:fs/promises";
import ts from "typescript";
import {workerAuthorized} from "../server/capture-worker-access.mjs";
import {ARCHIVE_LIMIT_BYTES} from "../server/ingestion-config.mjs";
import {componentHarness,findNode,settle} from "./component-harness.mjs";

const environment={DB_HOST:"fixture.invalid",DB_NAME:"fixture",DB_USER:"fixture",DB_PASSWORD:"fixture-only",KFM_DB_TLS:"verified",KFM_DB_CA_PEM:"fixture-ca",KFM_PUBLIC_ORIGIN:"https://kansasfrontiermatrix.com",VINEXT_TRUSTED_HOSTS:"kansasfrontiermatrix.com,www.kansasfrontiermatrix.com",KFM_INGEST_ENABLED:"true",KFM_RUNTIME_ROLE:"published",KFM_ARCHIVE_CAPACITY_CONFIRMED_BYTES:String(ARCHIVE_LIMIT_BYTES),KFM_CAPTURE_WORKER_TOKEN:"a".repeat(43)};
test("machine control can resume and pause a fresh archive without browser authority or automatic activation",async()=>{
 const writes=[];let invalidations=0,ready=environment;
 const imports={
  "../../../../server/ingestion-store.mjs":{getIngestionStore:async()=>({setPaused:async(...args)=>writes.push(args)})},
  "../../../../server/ingestion-runner.mjs":{clearIngestionStatusCache:()=>invalidations++},
  "../../../../server/capture-worker-access.mjs":{workerAuthorized:request=>workerAuthorized(request,ready),json:(value,status=200)=>Response.json(value,{status})},
 };
 const code=ts.transpileModule(await readFile("app/api/source-pipeline/control/route.ts","utf8"),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
 const module={exports:{}};new Function("require","module","exports",code)(name=>{assert.ok(imports[name],name);return imports[name];},module,module.exports);
 const request=(query,headers={})=>new Request("https://kansasfrontiermatrix.com/api/source-pipeline/control?"+query,{method:"POST",headers});
 const token={Authorization:"Bearer "+environment.KFM_CAPTURE_WORKER_TOKEN};
 assert.equal((await module.exports.POST(request("action=resume",{Cookie:"__Host-kfm-owner="+"b".repeat(43),"x-role":"admin"}))).status,401);
 assert.equal((await module.exports.POST(request("action=resume",{...token,Origin:"https://evil.example"}))).status,401);
 assert.deepEqual(writes,[]);
 for(const query of ["action=delete","action=resume&extra=1","action=resume&action=pause"]){assert.equal((await module.exports.POST(request(query,token))).status,400);}
 assert.deepEqual(writes,[]);
 assert.deepEqual(await (await module.exports.POST(request("action=resume",token))).json(),{state:"scheduled"});
 assert.deepEqual(await (await module.exports.POST(request("action=pause",token))).json(),{state:"paused"});
 assert.deepEqual(writes,[[false,"capture-worker"],[true,"capture-worker"]]);assert.equal(invalidations,2);
 ready={...environment,KFM_INGEST_ENABLED:"false"};assert.equal((await module.exports.POST(request("action=resume",token))).status,401);assert.equal(writes.length,2);
});

test("selecting a public historical sheet keeps metadata and footprint fitting without private overlay requests",async t=>{
 const calls=[],fits=[];
 const sheet={id:1,scanId:123,year:1930,imprintYear:1932,scale:24000,name:"Fixture",state:"KS",series:"HTMC",datum:"NAD27",viewerHref:"https://ngmdb.usgs.gov/topoview/viewer/#12/38/-98",footprint:{type:"Feature",properties:{},geometry:{type:"Polygon",coordinates:[[[-98,38],[-97,38],[-97,39],[-98,38]]]}}};
 const h=await componentHarness("app/historical-topo-control.tsx",{"./historical-topo":{TOPO_PAGE_SIZE:24},"./browser-json-request":{browserJsonRequest:async url=>{calls.push(url);return {response:{ok:true},body:{state:"available",sheets:[sheet],more:false,retrievedAt:"2026-10-19T00:00:00Z"}};}}},{URLSearchParams,window:{innerWidth:1200,innerHeight:900,matchMedia:()=>({matches:true})}});t.after(()=>h.dispose());
 const props={map:{getCenter:()=>({lng:-98,lat:38}),fitBounds:(...args)=>fits.push(args)},styleReady:false,locationPrivate:false};
 const render=()=>{const tree=h.render(h.exports.HistoricalTopoControl,props);h.commit();return tree;};render();await settle();let tree=render();
 const result=findNode(tree,node=>node.type==="button"&&node.props.className==="historical-topo-result");assert.ok(result);result.props.onClick();tree=render();
 const details=findNode(tree,node=>typeof node.type==="function"&&node.type.name==="HistoricalTopoSheetDetails");assert.ok(details);const detail=details.type(details.props);
 const text=JSON.stringify(detail);assert.match(text,/Printed map year/);assert.match(text,/Open USGS TopoView/);assert.doesNotMatch(text,/Prepare this|Check status|Owner candidate|overlay|reviewed image/i);
 findNode(detail,node=>node.type==="button").props.onClick();assert.deepEqual(JSON.parse(JSON.stringify(fits[0][0])),[[-98,38],[-97,39]]);
 assert.equal(calls.length,1);assert.ok(calls[0].startsWith("/api/historical-topo?"));
});

for(const origin of ["https://kansasfrontiermatrix.com","https://urdng3v1vk.preview.c38.airoapp.ai","http://127.0.0.1:4173"]){
 test("reviewed imagery stays local while hosted discovery performs no private request: "+origin,async t=>{
  const calls=[];
  const h=await componentHarness("app/earth-engine-context-client.ts",{"./earth-engine-context":{EARTH_ENGINE_CATALOG_MAX_BYTES:10000,earthEngineSetYear:()=>2024,parseEarthEngineCatalog:()=>[]},"./browser-json-request":{browserJsonRequest:async url=>{calls.push(url);return {response:{ok:true,status:200},body:{}};}}},{window:{location:{origin}}});t.after(()=>h.dispose());
  const render=()=>{const value=h.render(h.exports.useEarthEngineContext);h.commit();return value;};render();await settle();let value=render();assert.equal(value.enabled,origin==="http://127.0.0.1:4173");assert.equal(value.loading,false);assert.equal(value.error,null);
  value.reload();render();await settle();value=render();assert.equal(value.loading,false);assert.equal(calls.length,origin==="http://127.0.0.1:4173"?2:0);
 });
}

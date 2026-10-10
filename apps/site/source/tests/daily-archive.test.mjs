import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
import { before, after, test } from "node:test";
import ts from "typescript";
import { captureDaily } from "../scripts/capture-daily-archive.mjs";
const compile=source=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString("base64")}`;
const modelUrl=compile(await readFile(new URL("../app/daily-archive.ts",import.meta.url),"utf8"));
const model=await import(modelUrl);
const store=await import(compile((await readFile(new URL("../app/daily-archive-store.ts",import.meta.url),"utf8")).replace('"./daily-archive"',JSON.stringify(modelUrl))));
const require=createRequire(import.meta.url);const runtimeRequire=createRequire(require.resolve("wrangler"));const {Miniflare,convertV4MiniflareOptions}=runtimeRequire("miniflare");
let runtime,db,bucket;
before(async()=>{
 runtime=new Miniflare(convertV4MiniflareOptions({modules:true,script:"export default {fetch(){return new Response('test')}}",d1Databases:["DB"],r2Buckets:["BUCKET"]}));
 db=await runtime.getD1Database("DB");bucket=await runtime.getR2Bucket("BUCKET");
 const sql=await readFile(new URL("../drizzle/0005_daily_archive.sql",import.meta.url),"utf8");
 for(const statement of sql.split('--> statement-breakpoint'))await db.prepare(statement).run();
});
after(async()=>{await runtime?.dispose();});
const feed="usgs-earthquakes";
const fixture=(overrides={})=>({feed,state:"ready",retrievedAt:new Date().toISOString(),upstreamUpdatedAt:null,featureCount:1,data:{type:"FeatureCollection",features:[{type:"Feature",geometry:{type:"Point",coordinates:[-98,38]},properties:{observedAt:"2026-10-08T22:00:00Z",magnitude:2,unit:"Mw"}}]},source:"USGS test fixture",limitation:"Deterministic fixture only",truncated:false,...overrides});
const reply=(overrides={})=>async()=>Response.json(fixture(overrides));
const reset=async()=>{for(const table of ["daily_archive_reviews","daily_archive_captures","daily_archive_lock","daily_archive_settings"])await db.prepare(`DELETE FROM ${table}`).run();};

test("UTC dates and coordinate validation reject malformed map data",()=>{
 assert.equal(model.archiveDay("2026-02-30"),false);assert.equal(model.archiveDay("2024-02-29"),true);
 assert.throws(()=>model.validateArchivePayload(fixture({featureCount:2}),feed));
 const bad=fixture();bad.data.features[0].geometry.coordinates=[-200,38];assert.throws(()=>model.validateArchivePayload(bad,feed));
 assert.throws(()=>model.validateArchivePayload(fixture({state:"empty"}),feed));
});

test("durable capture, idempotency and exact stored-byte readback",async()=>{
 await reset();const first=await store.captureArchive(db,bucket,feed,reply());
 assert.equal(first.status,"ready");const saved=await store.readArchiveCapture(db,bucket,first.id);
 assert.equal(saved.payload.data.features[0].properties.unit,"Mw");assert.equal(saved.entry.review,"pending");assert.equal(await store.archiveHash(saved.bytes),first.sha256);
 let called=false;const again=await store.captureArchive(db,bucket,feed,async()=>{called=true;throw Error();});
 assert.equal(again.id,first.id);assert.equal(called,false);
 const otherDay=new Date(Date.now()+86400000);const second=await store.captureArchive(db,bucket,feed,reply(),otherDay);assert.notEqual(second.id,first.id);
 assert.equal((await store.archiveCatalog(db,new Date().toISOString().slice(0,10))).days.length,2);
});

test("concurrent writers acquire one lease before any provider access",async()=>{
 await reset();let calls=0,release;const gate=new Promise(resolve=>release=resolve);
 const first=store.captureArchive(db,bucket,feed,async()=>{calls++;await gate;return Response.json(fixture());});
 while(!calls)await new Promise(resolve=>setTimeout(resolve,5));
 await assert.rejects(store.captureArchive(db,bucket,feed,reply()),/Another capture/);release();await first;assert.equal(calls,1);
});

test("failure remains visible, retry preserves previous attempts, and retries are bounded",async()=>{
 await reset();await assert.rejects(store.captureArchive(db,bucket,feed,async()=>new Response("provider down",{status:503})),/UPSTREAM_HTTP_503/);
 for(let i=0;i<3;i++)await store.captureArchive(db,bucket,feed,reply({state:"partial"}));
 await assert.rejects(store.captureArchive(db,bucket,feed,reply()),/retry limit/);
 const rows=(await store.archiveCatalog(db,new Date().toISOString().slice(0,10))).entries;
 assert.equal(rows.length,4);assert.equal(rows[3].status,"failed");assert.equal(rows[3].bytes,0);
});

test("storage and pause stop new transfer without deleting history",async()=>{
 await reset();await db.prepare("INSERT INTO daily_archive_settings(id,budget,paused) VALUES(1,16777216,1)").run();
 let calls=0;const acquire=async()=>{calls++;return Response.json(fixture());};
 await assert.rejects(store.captureArchive(db,bucket,feed,acquire),/paused/);
 await db.prepare("UPDATE daily_archive_settings SET paused=0").run();await store.captureArchive(db,bucket,feed,acquire);
 await assert.rejects(store.captureArchive(db,bucket,"nws-alerts",acquire),/budget reached/);assert.equal(calls,1);
});

test("invalid or oversized capture cannot become an empty successful day",async()=>{
 await reset();await assert.rejects(store.captureArchive(db,bucket,feed,reply({featureCount:9})),/INVALID_CAPTURE/);
 await assert.rejects(store.captureArchive(db,bucket,feed,async()=>new Response("{}",{headers:{"content-length":String(model.ARCHIVE_MAX_PAYLOAD+1)}})),/TOO_LARGE/);
 const rows=(await store.archiveCatalog(db,new Date().toISOString().slice(0,10))).entries;assert.ok(rows.every(row=>row.status==="failed"));
});

test("failed object write conservatively retains bytes and its recoverable object key",async()=>{
 await reset();const failedBucket={...bucket,put:async()=>{throw Error("disk full");}};
 await assert.rejects(store.captureArchive(db,failedBucket,feed,reply()));
 const [entry]=(await store.archiveCatalog(db,new Date().toISOString().slice(0,10))).entries;assert.equal(entry.status,"failed");assert.ok(entry.bytes>0);assert.ok(entry.object_key);
});

test("crash recovery records the interrupted attempt and preserves its reservation",async()=>{
 await reset();const old=new Date(Date.now()-700000).toISOString();const day=old.slice(0,10);
 await db.prepare("INSERT INTO daily_archive_captures(id,day,feed,attempt,status,started_at,bytes) VALUES('interrupted',?,?,1,'running',?,16777216)").bind(day,feed,old).run();
 await db.prepare("INSERT INTO daily_archive_lock VALUES(1,'old',?)").bind(old).run();await store.captureArchive(db,bucket,"nws-alerts",reply({feed:"nws-alerts"}));
 const row=await db.prepare("SELECT * FROM daily_archive_captures WHERE id='interrupted'").first();assert.equal(row.status,"failed");assert.equal(row.bytes,16777216);
});

test("append-only review holds the exact capture, while checksum tampering fails closed",async()=>{
 await reset();const result=await store.captureArchive(db,bucket,feed,reply());await store.reviewArchive(db,result.id,"held","Investigate coordinates");
 await assert.rejects(store.readArchiveCapture(db,bucket,result.id),/held/);assert.equal((await store.readArchiveCapture(db,bucket,result.id,true)).entry.review,"held");
 await store.reviewArchive(db,result.id,"reviewed","Source coordinates checked");const saved=await store.readArchiveCapture(db,bucket,result.id);assert.equal(saved.entry.review,"reviewed");
 assert.equal((await db.prepare("SELECT COUNT(*) AS n FROM daily_archive_reviews").first()).n,2);
 await bucket.put(saved.entry.object_key,new Uint8Array(saved.entry.bytes));await assert.rejects(store.readArchiveCapture(db,bucket,result.id),/checksum/);
});

test("no capture for a missing day and no fabricated empty map payload",async()=>{
 await reset();const catalog=await store.archiveCatalog(db,"2000-01-01");assert.deepEqual(catalog.entries,[]);assert.deepEqual(catalog.days,[]);
 await assert.rejects(store.readArchiveCapture(db,bucket,crypto.randomUUID()),/No stored capture/);
});

test("runner rejects credential redirection and stops paused runs before writes",async()=>{
 for(const origin of ["https://evil.test","http://localhost:4173","http://127.0.0.1:4173/path"])await assert.rejects(captureDaily(origin),/UNSUPPORTED/);
 await assert.rejects(captureDaily("http://127.0.0.1:4173","secret"),/DO_NOT_SEND/);
 let calls=0;const result=await captureDaily("http://127.0.0.1:4173",null,async()=>{calls++;return Response.json({storage:{paused:true}});});assert.equal(result.outcome,"paused");assert.equal(calls,1);
});

test("archive screen server-renders safely before a day or capture is loaded",async()=>{
 let source=await readFile(new URL("../app/daily-archive/workspace.tsx",import.meta.url),"utf8");
 source=source.replace('import Link from "next/link";','const Link = "a";')
   .replace('"react"',JSON.stringify(import.meta.resolve("react")))
   .replace('"../daily-archive"',JSON.stringify(modelUrl))
   .replace(/import \{ loadMapLibre[^;]+;/,'const loadMapLibre = () => Promise.reject(new Error("SSR cannot load map"));')
   .replace('import styles from "./archive.module.css";','const styles = {};').replace('import { applyArchiveMapData } from "../daily-archive-map";','const applyArchiveMapData = () => {};');
 const js=ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022,jsx:ts.JsxEmit.ReactJSX}}).outputText.replaceAll('"react/jsx-runtime"',JSON.stringify(import.meta.resolve("react/jsx-runtime")));
 const {default:Screen}=await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
 const {createElement}=await import("react");const {renderToStaticMarkup}=await import("react-dom/server");
 const html=renderToStaticMarkup(createElement(Screen));assert.match(html,/Daily archive/);assert.match(html,/No saved data/);assert.match(html,/Maximum archive bytes/);
});

test("daily scripts execute through the installed stable symlink",async()=>{
 const {mkdtemp,symlink,rm}=await import("node:fs/promises");const {tmpdir}=await import("node:os");const {spawnSync}=await import("node:child_process");const {fileURLToPath}=await import("node:url");
 const directory=await mkdtemp(`${tmpdir()}/kfm-daily-launcher-`);
 try{for(const name of ["capture-daily-archive.mjs","install-daily-archive-timer.mjs"]){const link=`${directory}/${name}`;await symlink(fileURLToPath(new URL(`../scripts/${name}`,import.meta.url)),link);const result=spawnSync(process.execPath,[link,"--invalid"],{encoding:"utf8"});assert.equal(result.status,1);assert.match(result.stderr,/USAGE|DAILY_CAPTURE_FAILED/);}}
 finally{await rm(directory,{recursive:true,force:true});}
});

test("runner verifies separate capture days when a run crosses midnight",async()=>{
 const records=[];let index=0;const requestedDays=[];
 const request=async(url,options)=>{
  const parsed=new URL(url);
  if(options.method==="POST"){const feed=parsed.searchParams.get("feed");const row={id:`row-${index}`,feed,status:"ready",day:index++===0?"2026-10-09":"2026-10-10"};records.push(row);return Response.json({outcome:"captured",id:row.id,day:row.day,status:row.status});}
  const day=parsed.searchParams.get("day")??"2026-10-10";requestedDays.push(day);
  return Response.json({day,storage:{paused:false},entries:records.filter(row=>row.day===day)});
 };
 const result=await captureDaily("http://127.0.0.1:4173",null,request);assert.equal(result.outcome,"complete");assert.equal(result.results.length,9);assert.ok(requestedDays.includes("2026-10-09"));
});


test("map switching and clearing work while the previous GeoJSON update is still loading",async()=>{
 const {applyArchiveMapData}=await import(compile(await readFile(new URL("../app/daily-archive-map.ts",import.meta.url),"utf8")));
 const state={};const map={isStyleLoaded:()=>false,getSource:key=>({setData:data=>state[key]=data})};
 const first=fixture();applyArchiveMapData(map,first,first.data);assert.equal(state.capture,first.data);
 const next=fixture({data:{type:"FeatureCollection",features:[]},featureCount:0,state:"empty"});
 applyArchiveMapData(map,next,null);assert.equal(state.capture,next.data);assert.equal(state.counties.features.length,0);
 applyArchiveMapData(map,null,null);assert.equal(state.capture.features.length,0);
});

import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
const compile=source=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString("base64")}`;
const state=globalThis.__archiveAuthTest={env:{},user:null,calls:0};
const token="o".repeat(43),workerToken="w".repeat(43);
const envUrl=compile('export const env=globalThis.__archiveAuthTest.env;');
const nextUrl=compile('export class NextRequest extends Request {get nextUrl(){return new URL(this.url)}}');
const storeUrl=compile(`export class ArchiveError extends Error {constructor(message,status=400){super(message);this.status=status}}
export const archiveHeaders={"Cache-Control":"private, no-store"};
export const archiveCatalog=async(db,day)=>{globalThis.__archiveAuthTest.calls++;return {day,storage:{paused:false,budget:100,used:1},entries:[{id:"capture",status:"ready",review:"held",review_note:"private note",object_key:"private key"}]}};
export const readArchiveCapture=async(db,bucket,id,inspect)=>{globalThis.__archiveAuthTest.calls++;return {entry:{id,day:"2026-10-11",feed:"usgs-earthquakes",review:inspect?"held":"pending"},payload:{private:true},bytes:new TextEncoder().encode('{"retained":true}')}};
export const captureArchive=async()=>{globalThis.__archiveAuthTest.calls++;return {outcome:"captured"}};
export const reviewArchive=async()=>{globalThis.__archiveAuthTest.calls++;return {review:"reviewed"}};`);
const dbUrl=compile('export function getRawDb(){globalThis.__archiveAuthTest.calls++;return {prepare:()=>({bind(){return this},all:async()=>({results:[]}),run:async()=>{globalThis.__archiveAuthTest.calls++}})}}');
const modelUrl=compile('export const archiveFeed=value=>value==="usgs-earthquakes";');
const liveUrl=compile('export async function GET(){globalThis.__archiveAuthTest.calls++;return Response.json({})}');
const authSource=(await readFile(new URL("../app/daily-archive-auth.ts",import.meta.url),"utf8")).replace('"cloudflare:workers"',JSON.stringify(envUrl)).replace('"./daily-archive-store"',JSON.stringify(storeUrl));
const authUrl=compile(authSource);
let source=await readFile(new URL("../app/api/daily-archive/route.ts",import.meta.url),"utf8");
for(const [name,url] of Object.entries({"cloudflare:workers":envUrl,"next/server":nextUrl,"../../../db":dbUrl,"../../daily-archive":modelUrl,"../../daily-archive-store":storeUrl,"../live-context/route":liveUrl,"../../daily-archive-auth":authUrl}))source=source.replace(JSON.stringify(name),JSON.stringify(url));
const route=await import(compile(source));const {NextRequest}=await import(nextUrl);
const request=(query="",method="GET",headers={},body)=>new NextRequest(`http://127.0.0.1:4173/api/daily-archive${query}`,{method,headers,...(body?{body:JSON.stringify(body)}:{})});
const reset=()=>{for(const key of Object.keys(state.env))delete state.env[key];state.env.BUCKET={};state.user=null;state.calls=0;};
const denied=async(req,status)=>{state.calls=0;const response=await route[req.method](req);assert.equal(response.status,status);assert.equal(state.calls,0,"authorization precedes D1/R2/provider access");};

test("anonymous catalog, payload, held download and every public-marker write are denied",async()=>{
 reset();
 for(const query of ["","?day=2026-10-11","?id=capture","?id=capture&action=download","?action=status"])await denied(request(query),401);
 for(const action of ["capture&feed=usgs-earthquakes","review","settings"])await denied(request(`?action=${action}`,"POST",{"X-KFM-Archive-Writer":"daily-v1"}),401);
 await denied(request("?id=capture&action=download","GET",{Authorization:`Bearer ${workerToken}`}),401);
});
test("capture credential can only capture and read bounded receipts without private review data",async()=>{
 reset();state.env.KFM_ARCHIVE_WORKER_TOKEN=workerToken;const headers={Authorization:`Bearer ${workerToken}`,"X-KFM-Archive-Writer":"daily-v1"};
 for(const query of ["","?id=capture","?id=capture&action=download"])await denied(request(query,"GET",headers),401);
 for(const action of ["review","settings"])await denied(request(`?action=${action}`,"POST",headers),401);
 const response=await route.GET(request("?action=status&day=2026-10-11","GET",headers));assert.equal(response.status,200);
 assert.deepEqual((await response.json()).entries,[{id:"capture",status:"ready"}]);
 assert.equal((await route.POST(request("?action=capture&feed=usgs-earthquakes","POST",headers))).status,200);
 assert.equal((await route.GET(request("?action=status&id=capture","GET",headers))).status,400);
 await denied(request("?action=capture&action=review","POST",headers),400);
 for(const value of ["daily-v1",`Bearer ${"x".repeat(43)}`,`Bearer ${workerToken}, Bearer ${workerToken}`,`bearer ${workerToken}`])await denied(request("?action=status","GET",{Authorization:value}),401);
});
test("local owner capability supports all reads including held bytes without granting worker curation",async()=>{
 reset();state.env.KFM_ARCHIVE_LOCAL_OWNER_TOKEN=token;state.env.KFM_ARCHIVE_WORKER_TOKEN=workerToken;
 const headers={Authorization:`Bearer ${token}`,"X-KFM-Archive-Writer":"daily-v1"};
 assert.equal((await route.GET(request())).status,401);
 const response=await route.GET(request("?id=capture&action=download","GET",headers));assert.equal(response.status,200);assert.equal(await response.text(),'{"retained":true}');
 assert.equal((await route.POST(request("?action=capture&feed=usgs-earthquakes","POST",headers))).status,200);
 await denied(new NextRequest("https://site.example/api/daily-archive",{headers}),401);
 state.env.KFM_ARCHIVE_LOCAL_OWNER_TOKEN=workerToken;await denied(request("?id=capture&action=download","GET",{Authorization:`Bearer ${workerToken}`}),401);
});

import test from "node:test";
import assert from "node:assert/strict";
import { randomBytes } from "node:crypto";
import { ARCHIVE_LIMIT_BYTES, OWNER_GITHUB_ID, ingestionConfig } from "../server/ingestion-config.mjs";
import { CAPTURE_SOURCES, captureRequest, fetchCapture } from "../server/ingestion-sources.mjs";
import { runIngestion } from "../server/ingestion-runner.mjs";
import { authenticateOwner, openFlow, ownerCallback, sameOrigin, sealFlow, workerAuthorized } from "../server/owner-auth.mjs";
const environment = { DB_HOST: "fixture.invalid", DB_NAME: "fixture", DB_USER: "fixture", DB_PASSWORD: "fixture-only", KFM_DB_TLS: "verified", KFM_DB_CA_PEM: "fixture-ca", KFM_PUBLIC_ORIGIN: "https://kansasfrontiermatrix.com", KFM_GITHUB_CLIENT_ID: "fixture-client", KFM_GITHUB_CLIENT_SECRET: "fixture-only", KFM_SESSION_KEY: randomBytes(32).toString("base64url"), KFM_INGEST_ENABLED: "true", KFM_RUNTIME_ROLE: "published", KFM_ARCHIVE_CAPACITY_CONFIRMED_BYTES: String(ARCHIVE_LIMIT_BYTES), KFM_CAPTURE_WORKER_TOKEN: randomBytes(32).toString("base64url") };
const fixture = { type: "FeatureCollection", features: [{ type: "Feature", id: "unchanged-id", geometry: { type: "Point", coordinates: [-98,38,3.5] }, properties: { value: null, unit_of_measure: "ft3/s", approval_status: "Provisional", time: "2026-10-14T01:00:00Z" } }] };
const reply = (value = fixture) => new Response(JSON.stringify(value), { headers: { "Content-Type": "application/geo+json; charset=utf-8" } });
test("archive readiness is deny-by-default and requires the exact chosen capacity", () => {
  assert.equal(ingestionConfig({}).ready, false); assert.equal(ingestionConfig(environment).ready, true);
  for (const key of ["DB_HOST","DB_PASSWORD","KFM_DB_CA_PEM","KFM_GITHUB_CLIENT_SECRET","KFM_INGEST_ENABLED","KFM_RUNTIME_ROLE","KFM_ARCHIVE_CAPACITY_CONFIRMED_BYTES"]) assert.equal(ingestionConfig({ ...environment, [key]: "" }).ready, false, key);
  assert.equal(ingestionConfig({ ...environment, KFM_PUBLIC_ORIGIN: "https://q9r9beo47t.preview.c38.airoapp.ai" }).ready, false);
  assert.equal(ingestionConfig({ ...environment, DB_HOST: "10.0.0.1" }).ready, false);
  assert.equal(ingestionConfig({ ...environment, KFM_ARCHIVE_CAPACITY_CONFIRMED_BYTES: "80000000001" }).ready, false);
});
test("capture identity is stable within its bucket and rejects arbitrary sources or URLs", async () => {
  const at = Date.parse("2026-10-14T05:03:00Z");
  const a = captureRequest("usgs-streamflow", at), b = captureRequest("usgs-streamflow", at + 1000);
  assert.equal(a.id, b.id); assert.notEqual(a.id, captureRequest("usgs-streamflow", at + 3_600_000).id);
  assert.equal(new URL(a.url).searchParams.get("state_code"), "20");
  assert.throws(() => captureRequest("http://127.0.0.1"), /SOURCE_NOT_ALLOWED/);
  await assert.rejects(fetchCapture({ ...a, url: "http://169.254.169.254" }, { fetcher: () => assert.fail("must not fetch") }), /SOURCE_NOT_ALLOWED/);
});
test("capture preserves bytes, nulls, units, revisions and provenance without release", async () => {
  const request = captureRequest("usgs-streamflow"); const bytes = JSON.stringify(fixture);
  const result = await fetchCapture(request, { fetcher: async (_url, init) => { assert.equal(init.redirect,"manual"); return reply(); } });
  assert.equal(result.bytes.toString(), bytes); assert.equal(result.receipt.sourceId, request.sourceId);
  assert.equal(result.receipt.sourceTimeStart, "2026-10-14T01:00:00.000Z");
  assert.equal(result.receipt.validation,"structure-valid"); assert.equal(result.receipt.rightsReview,"pending"); assert.equal(result.receipt.sensitivityReview,"pending"); assert.equal(result.receipt.releaseState,"unreleased"); assert.equal(result.receipt.lifecycle,"WORK/QUARANTINE");
});
test("malformed entity is privately quarantined; cap and provider paging stay partial", async () => {
  const request = captureRequest("usgs-earthquakes");
  const result = await fetchCapture(request,{fetcher: async()=>new Response("{bad json", {headers:{"Content-Type":"application/json"}})});
  assert.equal(result.receipt.validation,"invalid"); assert.equal(result.bytes.toString(),"{bad json");
  const partial = await fetchCapture(request,{fetcher:async()=>reply({...fixture,links:[{rel:"next",href:"https://untrusted.example"}]})});
  assert.equal(partial.receipt.partial,true);
});
test("redirect, wrong content, size and network failures are bounded and sanitized", async () => {
  const request=captureRequest("nws-alerts");
  for(const [response,code] of [[new Response("",{status:302,headers:{Location:"http://localhost"}}),"UPSTREAM_UNAVAILABLE"],[new Response("<html>",{headers:{"Content-Type":"text/html"}}),"CONTENT_TYPE_REJECTED"],[new Response("{}",{headers:{"Content-Type":"application/json","Content-Length":"9000000"}}),"RESPONSE_TOO_LARGE"]]) await assert.rejects(fetchCapture(request,{fetcher:async()=>response}),new RegExp(code));
  await assert.rejects(fetchCapture(request,{fetcher:async()=>{throw new Error("PRIVATE_KEY_IN_UPSTREAM_ERROR")}}),error=>error.message==="UPSTREAM_UNAVAILABLE");
  await assert.rejects(fetchCapture(request,{fetcher:async()=>new Response(new Uint8Array(request.limitBytes+1),{headers:{"Content-Type":"application/json"}})}),/RESPONSE_TOO_LARGE/);
});
test("unconfigured and paused/busy runner performs no provider I/O",async()=>{
  const never=()=>assert.fail("provider must not run");
  assert.equal((await runIngestion({config:ingestionConfig({}),fetcher:never})).state,"configuration-required");
  assert.equal((await runIngestion({config:ingestionConfig(environment),store:{claim:async()=>null},fetcher:never})).state,"paused-or-busy");
});
test("runner closes the lease, respects duplicate holds and stops at the hard limit",async()=>{
  let released=0, fetched=0, saved=0; const failures=[];
  const store={claim:async()=>"lease",due:async r=>r.sourceId!=="nws-alerts",reserve:async()=>9_000_000,save:async()=>{saved++},failure:async(...args)=>failures.push(args),release:async()=>{released++}};
  const result=await runIngestion({config:ingestionConfig(environment),store,fetcher:async()=>{fetched++;return reply()}});
  assert.equal(result.captured,2); assert.equal(saved,2); assert.equal(fetched,2); assert.equal(released,1);
  store.reserve=async()=>{throw new Error("ARCHIVE_LIMIT_REACHED")};
  const capped=await runIngestion({config:ingestionConfig(environment),store,fetcher:()=>assert.fail("no I/O beyond capacity")});
  assert.equal(capped.captured,0); assert.equal(capped.outcomes.length,1); assert.equal(failures[0][2],"ARCHIVE_LIMIT_REACHED"); assert.equal(released,2);
});
test("sealed OAuth state expires and rejects tampering",()=>{
  const flow={state:randomBytes(32).toString("base64url"),verifier:randomBytes(32).toString("base64url"),expires:Date.now()+300000}; const sealed=sealFlow(flow,environment);
  assert.deepEqual(openFlow(sealed,environment),flow); assert.equal(openFlow(sealed,environment,flow.expires+1),null); assert.equal(openFlow(sealed.slice(0,-1)+"!",environment),null);
});
function callbackRequest(flow,state=flow.state) {return new Request(`https://kansasfrontiermatrix.com/api/owner/callback?code=fixture-code&state=${encodeURIComponent(state)}`,{headers:{Cookie:`__Host-kfm-github-flow=${sealFlow(flow,environment)}`}})}
test("OAuth callback requires matched state, empty scopes and verified immutable owner ID",async()=>{
  const flow={state:randomBytes(32).toString("base64url"),verifier:randomBytes(32).toString("base64url"),expires:Date.now()+300000};
  const store={session:()=>assert.fail("must not sign in")};
  assert.equal((await ownerCallback(callbackRequest(flow,"x".repeat(43)),{environment,store,fetcher:()=>assert.fail("no exchange") })).status,403);
  assert.equal((await ownerCallback(callbackRequest(flow,"é".repeat(43)),{environment,store,fetcher:()=>assert.fail("no exchange") })).status,403);
  assert.equal((await ownerCallback(callbackRequest(flow),{environment,store,fetcher:async()=>Response.json({access_token:"fixture-token",token_type:"bearer",scope:"repo"})})).status,403);
  let calls=0; const wrongOwner=async()=>++calls===1?Response.json({access_token:"fixture-token",token_type:"bearer",scope:""}):Response.json({id:123,login:"bartytime4life"});
  assert.equal((await ownerCallback(callbackRequest(flow),{environment,store,fetcher:wrongOwner})).status,403);
  let session=null; calls=0;
  const signed=await ownerCallback(callbackRequest(flow),{environment,store:{session:async(token,expires)=>{session={token,expires}}},fetcher:async(url,init)=>{calls++;if(calls===1){assert.equal(new URLSearchParams(init.body).get("code_verifier"),flow.verifier);return Response.json({access_token:"fixture-token",token_type:"bearer",scope:""})} assert.equal(url,"https://api.github.com/user"); return Response.json({id:Number(OWNER_GITHUB_ID),login:"changed-login-is-not-authority"})}});
  assert.equal(signed.status,303); assert.match(session.token,/^[A-Za-z0-9_-]{43}$/); assert.notEqual(session.token,"fixture-token"); assert.match(signed.headers.get("set-cookie"),/HttpOnly; Secure; SameSite=Lax/);
});
test("forged roles, cross-origin actions and worker attempts cannot gain owner authority",async()=>{
  const config=ingestionConfig(environment);
  assert.equal(await authenticateOwner(new Request("https://kansasfrontiermatrix.com/api/source-pipeline/captures",{headers:{"x-role":"admin","oai-authenticated-user-id":OWNER_GITHUB_ID}}),{config,store:{authenticate:()=>assert.fail("no opaque token")}}),false);
  assert.equal(sameOrigin(new Request("https://kansasfrontiermatrix.com/api/source-pipeline/control",{headers:{Origin:"https://evil.example"}}),config),false);
  assert.equal(workerAuthorized(new Request("https://kansasfrontiermatrix.com/api/source-pipeline/run",{headers:{Authorization:`Bearer ${environment.KFM_CAPTURE_WORKER_TOKEN}`}}),environment),true);
  assert.equal(workerAuthorized(new Request("https://q9r9beo47t.preview.c38.airoapp.ai/api/source-pipeline/run",{headers:{Authorization:`Bearer ${environment.KFM_CAPTURE_WORKER_TOKEN}`}}),environment),false);
  assert.equal(workerAuthorized(new Request("https://kansasfrontiermatrix.com/api/source-pipeline/run",{headers:{Authorization:"Bearer "+"é".repeat(43)}}),environment),false);
});

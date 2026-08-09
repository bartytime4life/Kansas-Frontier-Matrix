import { describe, expect, it } from "vitest";
import fixtureSuite from "../../../fixtures/runtime/pmtiles_release_cache/cases.json";
import moduleSource from "../src/features/map_runtime/pmtiles_release_cache.ts?raw";
import { evaluatePmtilesCache, releaseScopedCacheKey } from "../src/features/map_runtime/pmtiles_release_cache";

type Candidate = typeof fixtureSuite.base;
function clone<T>(value:T):T{return JSON.parse(JSON.stringify(value)) as T;}
function mutate(base:Candidate,name:string):unknown{
 const v=clone(base);
 if(name==="NONE")return v;
 if(name==="FIRST_RUN_ONLINE"){v.request_mode="ONLINE";v.cache_snapshot.present=false;}
 else if(name==="FIRST_RUN_OFFLINE")v.cache_snapshot.present=false;
 else if(name==="PARTIAL")v.cache_snapshot.completion="PARTIAL";
 else if(name==="STALE_RELEASE")v.cache_snapshot.release_id="map-release:ks-demo-2025-999";
 else if(name==="POLICY_MISMATCH")v.cache_snapshot.policy_digest=`sha256:${"3c".repeat(32)}`;
 else if(name==="ARTIFACT_MISMATCH")v.cache_snapshot.artifact_digest=`sha256:${"4d".repeat(32)}`;
 else if(name==="MISSING_GLYPHS")v.cache_snapshot.assets.glyphs=false;
 else if(name==="MISSING_SPRITES")v.cache_snapshot.assets.sprites=false;
 else if(name==="WITHDRAWN")v.requested_release.release_state="WITHDRAWN";
 else if(name==="INTERNAL_SOURCE")v.requested_release.source_url_class="CANONICAL_INTERNAL";
 else if(name==="AUTHORITY_OVERCLAIM")v.authority.public_use_authorized=true;
 else if(name==="BAD_KEY")v.cache_snapshot.cache_key="kfm-pmtiles:wrong";
 else if(name==="INVALID_SHAPE")return {...v,unexpected:true};
 else throw new Error(name);
 return v;
}
describe("release-scoped PMTiles cache policy",()=>{
 it("replays every declared cache state",()=>{
  expect(fixtureSuite.source_idea).toBe("ML-Y-114");
  for(const c of fixtureSuite.cases){
   expect(evaluatePmtilesCache(mutate(fixtureSuite.base,c.mutation)),c.case_id).toMatchObject({outcome:c.expected_outcome,code:c.expected_code});
  }
 });
 it("derives the cache key from release, artifact, and policy identity",()=>{
  const release=fixtureSuite.base.requested_release;
  expect(releaseScopedCacheKey(release.release_id,release.artifact_digest,release.policy_digest)).toBe(fixtureSuite.base.cache_snapshot.cache_key);
 });
 it("never performs network or CacheStorage mutation",()=>{
  const result=evaluatePmtilesCache(clone(fixtureSuite.base));
  expect(result).toMatchObject({outcome:"PASS",mayRender:true,cacheMutated:false,networkRequested:false,authority:"NONE"});
  for(const forbidden of ["fetch(","caches.open(","cache.put(","cache.delete(","navigator.serviceWorker.register("])expect(moduleSource).not.toContain(forbidden);
 });
});

/**
 * Fixture-only release-scoped PMTiles cache policy.
 *
 * This module plans whether a future Service Worker may use, fetch, rebuild, or
 * deny one cache entry. It performs no fetch and does not call CacheStorage.
 */
export const PMTILES_CACHE_PROFILE =
  "kfm.pmtiles-release-cache-fixture.v1" as const;

export type CacheOutcome = "PASS" | "HOLD" | "DENY" | "ERROR";
export type CacheCode =
  | "PMTILES_CACHE_HIT_VERIFIED"
  | "PMTILES_CACHE_FETCH_REQUIRED"
  | "PMTILES_CACHE_OFFLINE_MISS"
  | "PMTILES_CACHE_PARTIAL"
  | "PMTILES_CACHE_RELEASE_MISMATCH"
  | "PMTILES_CACHE_POLICY_MISMATCH"
  | "PMTILES_CACHE_ARTIFACT_MISMATCH"
  | "PMTILES_CACHE_ASSET_INCOMPLETE"
  | "PMTILES_CACHE_RELEASE_WITHDRAWN"
  | "PMTILES_CACHE_SOURCE_CLASS_DENIED"
  | "PMTILES_CACHE_AUTHORITY_OVERCLAIM"
  | "PMTILES_CACHE_KEY_MISMATCH"
  | "PMTILES_CACHE_INPUT_INVALID";

export type CacheDecision = Readonly<{
  outcome: CacheOutcome;
  code: CacheCode;
  authority: "NONE";
  cacheMutated: false;
  networkRequested: false;
  mayRender: boolean;
  cacheKey: string | null;
}>;

type JsonRecord = Record<string, unknown>;
const DIGEST = /^sha256:[0-9a-f]{64}$/;
const ROOT_FIELDS = new Set(["profile","request_mode","requested_release","cache_snapshot","authority"]);
const RELEASE_FIELDS = new Set(["release_id","artifact_digest","policy_digest","source_url_class","release_state","required_assets"]);
const SNAPSHOT_FIELDS = new Set(["present","cache_key","release_id","artifact_digest","policy_digest","completion","assets"]);
const ASSET_FIELDS = new Set(["glyphs","pmtiles","sprites"]);
const AUTHORITY_FIELDS = new Set(["cache_mutated","network_requested","release_authorized","publication_authorized","public_use_authorized"]);

function record(value: unknown): value is JsonRecord {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
function exact(value: JsonRecord, fields: ReadonlySet<string>): boolean {
  const keys=Object.keys(value);
  return keys.length===fields.size && keys.every((key)=>fields.has(key));
}
function decision(outcome: CacheOutcome, code: CacheCode, cacheKey: string | null, mayRender=false): CacheDecision {
  return Object.freeze({outcome,code,authority:"NONE",cacheMutated:false,networkRequested:false,mayRender,cacheKey});
}
export function releaseScopedCacheKey(releaseId: string, artifactDigest: string, policyDigest: string): string {
  return `kfm-pmtiles:${releaseId}:${artifactDigest.slice(7,23)}:${policyDigest.slice(7,23)}`;
}
function parse(input: unknown): {root:JsonRecord; release:JsonRecord; snapshot:JsonRecord; assets:JsonRecord; authority:JsonRecord} | null {
  if(!record(input)||!exact(input,ROOT_FIELDS)||input.profile!==PMTILES_CACHE_PROFILE||!record(input.requested_release)||!record(input.cache_snapshot)||!record(input.authority)) return null;
  const release=input.requested_release, snapshot=input.cache_snapshot, authority=input.authority;
  if(!exact(release,RELEASE_FIELDS)||!exact(snapshot,SNAPSHOT_FIELDS)||!exact(authority,AUTHORITY_FIELDS)||!record(snapshot.assets)||!exact(snapshot.assets,ASSET_FIELDS)) return null;
  if(typeof release.release_id!=="string"||!DIGEST.test(String(release.artifact_digest))||!DIGEST.test(String(release.policy_digest))||!Array.isArray(release.required_assets)) return null;
  return {root:input,release,snapshot,assets:snapshot.assets,authority};
}
export function evaluatePmtilesCache(input: unknown): CacheDecision {
  const parsed=parse(input);
  if(parsed===null) return decision("ERROR","PMTILES_CACHE_INPUT_INVALID",null);
  const {root,release,snapshot,assets,authority}=parsed;
  const key=releaseScopedCacheKey(String(release.release_id),String(release.artifact_digest),String(release.policy_digest));
  if(Object.values(authority).some((value)=>value!==false)) return decision("DENY","PMTILES_CACHE_AUTHORITY_OVERCLAIM",key);
  if(release.source_url_class!=="GOVERNED_API") return decision("DENY","PMTILES_CACHE_SOURCE_CLASS_DENIED",key);
  if(release.release_state==="WITHDRAWN") return decision("DENY","PMTILES_CACHE_RELEASE_WITHDRAWN",key);
  if(snapshot.present!==true) {
    return root.request_mode==="ONLINE"
      ? decision("PASS","PMTILES_CACHE_FETCH_REQUIRED",key)
      : decision("HOLD","PMTILES_CACHE_OFFLINE_MISS",key);
  }
  if(snapshot.cache_key!==key) return decision("DENY","PMTILES_CACHE_KEY_MISMATCH",key);
  if(snapshot.release_id!==release.release_id) return decision("DENY","PMTILES_CACHE_RELEASE_MISMATCH",key);
  if(snapshot.policy_digest!==release.policy_digest) return decision("DENY","PMTILES_CACHE_POLICY_MISMATCH",key);
  if(snapshot.artifact_digest!==release.artifact_digest) return decision("DENY","PMTILES_CACHE_ARTIFACT_MISMATCH",key);
  if(snapshot.completion!=="COMPLETE") return decision("HOLD","PMTILES_CACHE_PARTIAL",key);
  if(assets.glyphs!==true||assets.pmtiles!==true||assets.sprites!==true) return decision("HOLD","PMTILES_CACHE_ASSET_INCOMPLETE",key);
  return decision("PASS","PMTILES_CACHE_HIT_VERIFIED",key,true);
}

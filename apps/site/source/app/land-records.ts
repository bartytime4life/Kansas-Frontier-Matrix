// Application projection of the monorepo land candidate / transfer contracts.
// Integrity checks never confer source admission, normalization or release.
export const LAND_SOURCE_ID = "land-records";
export const LAND_LIMIT = 10 * 1024 * 1024;
export const LAND_SOURCES: Record<string, { title: string; hosts: string[]; href: string; limitation: string }> = {
  "blm-glo": { title: "BLM · General Land Office", hosts: ["glorecords.blm.gov", "glo-entry-prod.blm.gov"], href: "https://glorecords.blm.gov/s/", limitation: "Historical patent and index entries. Keyword pages are partial; patents do not supply a sale price or present ownership." },
  "blm-mlrs": { title: "BLM · MLRS land tenure", hosts: ["reports.blm.gov", "mlrs.blm.gov"], href: "https://reports.blm.gov/reports/MLRS", limitation: "Redacted public reports only. Cases and proposed sales remain separate from completed transactions." },
  "kshs-land-sales": { title: "Kansas State Archives · land sales", hosts: ["www.kansashistory.gov", "www.kansasmemory.gov"], href: "https://www.kansashistory.gov/p/land-records-at-the-state-archives/11083", limitation: "Railroad sales and tract books need original-document and transcription review. Recorded principal is distinct from a verified purchase price." },
  "shawnee-tax-sales": { title: "Shawnee County · tax-sale results", hosts: ["snco.gov", "www.snco.gov", "cdn.snco.gov"], href: "https://snco.gov/counselor/prior_tax_sales.php", limitation: "Official auction results. Group prices belong to the whole sale unit; confirmation, title and deed recording need separate evidence." },
  "leavenworth-tax-sales": { title: "Leavenworth County · tax-sale results", hosts: ["www.leavenworthcounty.gov", "files.leavenworthcounty.gov"], href: "https://files.leavenworthcounty.gov/information/tax_sale/index.php", limitation: "Original documents required. Source retrieval failed TLS verification during the October 14 research; no live capture is claimed." },
  "sedgwick-deeds": { title: "Sedgwick County · recorded instruments", hosts: ["www.sedgwickcounty.org", "www.sedgwick.gov"], href: "https://www.sedgwickcounty.org/register-of-deeds/online-land-record-search/", limitation: "Lawful exports only. Online search is paid; free on-site access is available. Confidential sales questionnaires are excluded." },
  "johnson-deeds": { title: "Johnson County · recorded instruments", hosts: ["www.jocogov.org", "ims.jocogov.org"], href: "https://www.jocogov.org/department/treasury-taxation-and-vehicles", limitation: "Lawful exports with source and rights review. Assessed values and parcel context do not establish purchase prices or title." },
};
export type LandRecord = { profile: string; id: string; source_id: string; source_record_id: string; instrument_type: string; event_date: string; recording_date: string | null; state: string; county: string | null; transaction_status: string; parties: { role: string; label: string; living_status: string }[]; legal_description: string | null; acres: string | null; amount: { value: string; kind: string; currency: string } | null; notes: string | null; geometry: null; geometry_role: string; title_claim: string; sale_completion: string; rights_state: string; sensitivity_state: string; source_admission: string; review_state: string; release_state: string; flags: string[]; record_digest: string; evidence_ref: string };
type Json = unknown;
export type LandDocument = { source_url: string; sha256: string; bytes: number };
export type LandCoverage = { scope: string; complete: boolean; reported_total: number | null; start?: number; end?: number; excluded?: { locator: string; reason: string }[] };
export type LandManifest = { profile: string; source_id: string; source_url: string; retrieved_at: string; format: string; capture_method: string; payload_sha256: string; bytes: number; documents: LandDocument[]; total_bytes: number; source_admission: string; release_state: string; capture_id: string };
export type LandCandidate = { profile: string; capture_id: string; source_id: string; records: LandRecord[]; locators: Record<string,string[]>; coverage: LandCoverage; mapping: Record<string,string> | null; review_state: string; release_state: string; candidate_id: string };
export type LandEvidence = { profile: string; evidence_ref: string; record_digest: string; capture_id: string; candidate_id: string; source_url: string; retrieved_at: string; capture_method: string; members: { sha256: string; bytes: number }[]; locators: string[]; documents: LandDocument[]; review_state: string; release_state: string; bundle_digest: string; coverage?: LandCoverage };
export type LandTransfer = { profile: string; created_at: string; authority: string; review_state: string; release_state: string; transfer_digest: string; captures: { manifest: LandManifest; candidate: LandCandidate; evidence: LandEvidence[] }[]; objects: Record<string,string> };
const HASH = /^sha256:[a-f0-9]{64}$/;
const kinds: Record<string, string[]> = { "blm-glo": ["patent", "deed", "warranty_deed", "quitclaim_deed", "other_instrument"], "blm-mlrs": ["land_tenure_case", "sale_notice"], "kshs-land-sales": ["railroad_sale", "tract_book_entry", "deed"], "sedgwick-deeds": ["deed", "warranty_deed", "quitclaim_deed"], "johnson-deeds": ["deed", "warranty_deed", "quitclaim_deed"], "shawnee-tax-sales": ["tax_foreclosure_sale"], "leavenworth-tax-sales": ["tax_foreclosure_sale"] };
export function canonicalLand(value: Json): string {
  if (value === null || typeof value !== "object") { const encoded=JSON.stringify(value); if (encoded===undefined) return fail(); return encoded; }
  if (Array.isArray(value)) return `[${value.map(canonicalLand).join(",")}]`;
  return `{${Object.keys(value).sort().map(k => `${JSON.stringify(k)}:${canonicalLand((value as Record<string,unknown>)[k])}`).join(",")}}`;
}
export async function landDigest(value: Json): Promise<string> {
  const bytes = value instanceof Uint8Array ? value : new TextEncoder().encode(canonicalLand(value));
  const result = await crypto.subtle.digest("SHA-256", new Uint8Array(bytes).buffer);
  return "sha256:" + Array.from(new Uint8Array(result), b => b.toString(16).padStart(2,"0")).join("");
}
function fail(): never { throw new Error("Land bundle failed integrity, scope or review-state checks. Export it again from the audited pipeline."); }
function closed(v: Json, keys: string[]) { if (!v || typeof v !== "object" || Array.isArray(v) || Object.keys(v).sort().join("|") !== keys.sort().join("|")) fail(); }
function str(v: Json, limit: number, nullable = false) { if (v === null && nullable) return; if (typeof v !== "string" || !v.trim() || v.length > limit || /[\x00-\x08\x0b-\x1f\x7f]/.test(v)) fail(); }
function day(v: Json, nullable = false) { if (v === null && nullable) return; if (typeof v !== "string" || !/^\d{4}-\d\d-\d\d$/.test(v) || !Number.isFinite(Date.parse(v)) || new Date(v).toISOString().slice(0,10) !== v) fail(); }
function instant(v: Json) { if (typeof v !== "string" || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$/.test(v) || !Number.isFinite(Date.parse(v)) || new Date(v).toISOString().slice(0,19)+"Z" !== v || Date.parse(v) > Date.now()+1000) fail(); }
export function landSourceUrl(source: string, value: string) {
  str(value,2048); let url: URL; try { url = new URL(value); } catch { return fail(); }
  if (typeof source!=="string" || !Object.hasOwn(LAND_SOURCES,source) || url.protocol !== "https:" || !LAND_SOURCES[source].hosts.includes(url.hostname) || url.port || url.username || url.password || url.hash || /[\s\\]/.test(value)) fail();
  let query: string; try { query = decodeURIComponent(url.search); } catch { return fail(); }
  if (/token|secret|password|session|authorization|signature|api.?key|siwc/i.test(query)) fail();
  return value;
}
async function selfHash(value: object, field: string) { const item=value as Record<string,unknown>; const hash=item[field]; if (typeof hash!=="string"||!HASH.test(hash)) fail(); const rest=Object.fromEntries(Object.entries(item).filter(([key])=>key!==field)); if (await landDigest(rest)!==hash) fail(); }
export function decodeLandObject(value: string): Uint8Array {
  if (typeof value !== "string" || value.length%4 || !/^[A-Za-z0-9+/]*={0,2}$/.test(value) || !value.length) fail();
  let binary: string; try { binary = atob(value); } catch { return fail(); }
  if (btoa(binary) !== value || binary.length > LAND_LIMIT) fail();
  return Uint8Array.from(binary, c=>c.charCodeAt(0));
}
export async function validateLandTransfer(bytes: Uint8Array): Promise<LandTransfer> {
  if (!bytes.length || bytes.length > LAND_LIMIT) fail();
  let v: LandTransfer; let text: string;
  try { text = new TextDecoder("utf-8",{fatal:true}).decode(bytes); v = JSON.parse(text); } catch { return fail(); }
  // Reject duplicate JSON keys, alternate number forms and ambiguous encodings.
  if (canonicalLand(v) !== text!) fail();
  closed(v,["profile","created_at","authority","review_state","release_state","transfer_digest","captures","objects"]);
  if (v.profile !== "kfm.land-review-transfer/v1" || v.authority !== "PRIVATE_REVIEW_ONLY" || v.review_state !== "PENDING" || v.release_state !== "UNRELEASED") fail();
  instant(v.created_at); await selfHash(v,"transfer_digest");
  if (!Array.isArray(v.captures) || !v.captures.length || v.captures.length > 20 || !v.objects || typeof v.objects !== "object" || Array.isArray(v.objects) || Object.keys(v.objects).length > 100) fail();
  const sizes = new Map<string,number>();
  for (const [key,b64] of Object.entries(v.objects)) { if (!HASH.test(key)) fail(); const raw=decodeLandObject(b64 as string); if (await landDigest(raw)!==key) fail(); sizes.set(key,raw.length); }
  const used = new Set<string>(), captures = new Set<string>(); let count=0;
  for (const capture of v.captures) {
    closed(capture,["manifest","candidate","evidence"]); const m=capture.manifest,c=capture.candidate;
    closed(m,["profile","source_id","source_url","retrieved_at","format","capture_method","payload_sha256","bytes","documents","total_bytes","source_admission","release_state","capture_id"]);
    if (m.profile!=="kfm.land-records-capture/v1" || m.source_admission!=="PENDING" || m.release_state!=="UNRELEASED" || !["glo-text","mapped-csv"].includes(m.format) || (m.format==="glo-text" && m.source_id!=="blm-glo") || m.capture_method!==(m.format==="glo-text"?"BROWSER_DOM_TEXT":"EXPLICIT_EXPORT_OR_TRANSCRIPTION")) fail();
    landSourceUrl(m.source_id,m.source_url); instant(m.retrieved_at); await selfHash(m,"capture_id");
    if(captures.has(m.capture_id)) fail(); captures.add(m.capture_id);
    if (!Array.isArray(m.documents) || m.documents.length>10 || !Number.isSafeInteger(m.bytes) || sizes.get(m.payload_sha256)!==m.bytes) fail();
    const members = new Set<string>([m.payload_sha256]); let total=m.bytes;
    for(const d of m.documents){closed(d,["source_url","sha256","bytes"]);landSourceUrl(m.source_id,d.source_url);if(!Number.isSafeInteger(d.bytes)||sizes.get(d.sha256)!==d.bytes)fail();total+=d.bytes;members.add(d.sha256);}
    if(total!==m.total_bytes||total>LAND_LIMIT||(m.source_id.endsWith("tax-sales")&&!m.documents.length))fail();
    members.forEach(key=>used.add(key));
    closed(c,["profile","capture_id","source_id","records","locators","coverage","mapping","review_state","release_state","candidate_id"]);
    if(c.profile!=="kfm.land-records-batch/v1"||c.capture_id!==m.capture_id||c.source_id!==m.source_id||c.review_state!=="PENDING"||c.release_state!=="UNRELEASED"||!Array.isArray(c.records)||!c.records.length||!Array.isArray(capture.evidence)||capture.evidence.length!==c.records.length)fail();
    count+=c.records.length;if(count>1000)fail();await selfHash(c,"candidate_id");
    if(m.format==="glo-text"){
      closed(c.coverage,["scope","complete","reported_total","start","end",...(Object.hasOwn(c.coverage??{},"excluded")?["excluded"]:[])]);
      const cov=c.coverage;
      if(cov.scope!=="KEYWORD_RESULTS"||typeof cov.complete!=="boolean"||!Number.isSafeInteger(cov.start)||!Number.isSafeInteger(cov.end)||!Number.isSafeInteger(cov.reported_total)||cov.start!<1||cov.end!<cov.start!||cov.end!>cov.reported_total!||cov.end!-cov.start!>=100||c.mapping!==null)fail();
      if(cov.excluded!==undefined){if(!Array.isArray(cov.excluded)||cov.excluded.length>100)fail();for(const x of cov.excluded){closed(x,["locator","reason"]);if(typeof x.locator!=="string"||!/^result-card:\d+$/.test(x.locator)||x.reason!=="SURVEY_NOT_LAND_INSTRUMENT")fail();}}
    }else{
      closed(c.coverage,["scope","complete","reported_total"]);
      if(c.coverage.scope!=="EXPLICIT_EXPORT"||c.coverage.complete!==false||c.coverage.reported_total!==null||!c.mapping||typeof c.mapping!=="object"||Array.isArray(c.mapping))fail();
      const fields=["source_record_id","instrument_type","event_date","recording_date","county","state","transaction_status","grantor","grantee","legal_description","acres","amount","amount_kind","currency","notes"];
      if(["source_record_id","instrument_type","event_date","state","transaction_status"].some(k=>!Object.hasOwn(c.mapping!,k))||Object.keys(c.mapping).some(k=>!fields.includes(k))||new Set(Object.values(c.mapping)).size!==Object.keys(c.mapping).length)fail();for(const column of Object.values(c.mapping))str(column,2048);
    }
    const digests=new Set<string>();
    for(let i=0;i<c.records.length;i++){
      const r=c.records[i];
      closed(r,["profile","id","source_id","source_record_id","instrument_type","event_date","recording_date","state","county","transaction_status","parties","legal_description","acres","amount","notes","geometry","geometry_role","title_claim","sale_completion","rights_state","sensitivity_state","source_admission","review_state","release_state","flags","record_digest","evidence_ref"]);
      if(r.profile!=="kfm.land-instrument-candidate/v1"||r.source_id!==m.source_id||r.state!=="KS"||!kinds[r.source_id]?.includes(r.instrument_type)||r.geometry!==null||r.geometry_role!=="UNLOCATED"||r.title_claim!=="NOT_ESTABLISHED"||r.sale_completion!=="NOT_ESTABLISHED"||r.rights_state!=="PENDING"||r.source_admission!=="PENDING"||r.sensitivity_state!=="REVIEW_REQUIRED"||r.review_state!=="PENDING"||r.release_state!=="UNRELEASED")fail();
      str(r.source_record_id,256);day(r.event_date);day(r.recording_date,true);str(r.county,64,true);str(r.legal_description,8192,true);str(r.notes,4096,true);
      if(!["RECORDED","ISSUED","PROPOSED","CASE_ACTION","UNKNOWN","AUCTION_REPORTED"].includes(r.transaction_status)||r.event_date>m.retrieved_at.slice(0,10)&&r.transaction_status!=="PROPOSED"||r.recording_date&&r.recording_date>m.retrieved_at.slice(0,10))fail();
      if(r.instrument_type==="sale_notice"&&r.transaction_status!=="PROPOSED"||r.instrument_type==="land_tenure_case"&&!["CASE_ACTION","UNKNOWN"].includes(r.transaction_status)||r.instrument_type==="tax_foreclosure_sale"&&r.transaction_status!=="AUCTION_REPORTED"||r.transaction_status==="AUCTION_REPORTED"&&r.instrument_type!=="tax_foreclosure_sale")fail();
      const county: Record<string,string>={"shawnee-tax-sales":"Shawnee","leavenworth-tax-sales":"Leavenworth","sedgwick-deeds":"Sedgwick","johnson-deeds":"Johnson"};if(county[r.source_id]&&county[r.source_id]!==r.county)fail();
      if(r.acres!==null&&(typeof r.acres!=="string"||!/^\d{1,18}(?:\.\d{1,6})?$/.test(r.acres)||Number(r.acres)<=0))fail();
      if(!Array.isArray(r.parties)||r.parties.length>2)fail();for(const p of r.parties){closed(p,["role","label","living_status"]);if(!["grantor","grantee"].includes(p.role)||p.living_status!=="UNKNOWN")fail();str(p.label,256);}
      if(r.amount!==null){closed(r.amount,["value","kind","currency"]);if(typeof r.amount.value!=="string"||!/^\d{1,18}(?:\.\d{1,6})?$/.test(r.amount.value)||r.amount.currency!=="USD"||!["sale_price","consideration","nominal_consideration","recorded_principal","appraised_value","minimum_bid","auction_purchase_price"].includes(r.amount.kind))fail();if(r.instrument_type==="tax_foreclosure_sale"&&r.amount.kind!=="auction_purchase_price"||r.instrument_type!=="tax_foreclosure_sale"&&r.amount.kind==="auction_purchase_price"||["sale_notice","land_tenure_case"].includes(r.instrument_type)&&["sale_price","consideration","recorded_principal"].includes(r.amount.kind))fail();}
      if(!Array.isArray(r.flags)||r.flags.length>30||!r.flags.includes("RIGHTS_REVIEW_REQUIRED")||!r.flags.includes("SENSITIVITY_REVIEW_REQUIRED"))fail();for(const flag of r.flags)str(flag,100);
      const {record_digest,evidence_ref,...identity}=r;if(await landDigest(identity)!==record_digest||evidence_ref!=="kfm:evidence:land:"+record_digest.slice(7)||r.id!=="kfm:land:"+(await landDigest([r.source_id,r.source_record_id])).slice(7)||digests.has(record_digest))fail();digests.add(record_digest);
      const e=capture.evidence[i];closed(e,["profile","evidence_ref","record_digest","capture_id","candidate_id","source_url","retrieved_at","capture_method","members","locators","documents","review_state","release_state","bundle_digest"]);
      if(e.profile!=="kfm.land-evidence-bundle-candidate/v1"||e.review_state!=="PENDING"||e.release_state!=="UNRELEASED"||e.record_digest!==record_digest||e.evidence_ref!==evidence_ref||e.capture_id!==m.capture_id||e.candidate_id!==c.candidate_id||e.source_url!==m.source_url||e.retrieved_at!==m.retrieved_at||e.capture_method!==m.capture_method||canonicalLand(e.documents)!==canonicalLand(m.documents)||canonicalLand(e.members)!==canonicalLand([...members].sort().map(key=>({sha256:key,bytes:sizes.get(key)})))||canonicalLand(e.locators)!==canonicalLand(c.locators?.[record_digest])||!Array.isArray(e.locators)||!e.locators.length)fail();for(const locator of e.locators){if(typeof locator!=="string"||!/^(csv-row|result-card):\d+$/.test(locator))fail();}await selfHash(e,"bundle_digest");
    }
    if(Object.keys(c.locators??{}).sort().join()!==[...digests].sort().join())fail();
  }
  if([...sizes.keys()].some(key=>!used.has(key)))fail();
  return v as LandTransfer;
}
export function landRecords(transfer: LandTransfer): LandRecord[] {
  return [...new Map(transfer.captures.flatMap(c=>c.candidate.records).map(r=>[r.record_digest,r])).values()].sort((a,b)=>a.event_date.localeCompare(b.event_date)||a.record_digest.localeCompare(b.record_digest));
}
export function filterLandRecords(records: LandRecord[], params: URLSearchParams) {
  const allowed=["source","county","kind","start","end","q","after","record","object"];
  for(const k of params.keys())if(!allowed.includes(k)||params.getAll(k).length!==1)throw new Error("Invalid record filter.");
  const q=params.get("q")??"";if(q.length>150)throw new Error("Search is too long.");
  for(const k of ["source","county","kind"])if((params.get(k)?.length??0)>100)throw new Error("Invalid record filter.");
  for(const k of ["start","end"])if(params.get(k))day(params.get(k));
  if(params.get("start")&&params.get("end")&&params.get("start")!>params.get("end")!)throw new Error("Check the date range.");
  const after=params.get("after");if(after&&!/^\d{4}-\d\d-\d\d\|sha256:[a-f0-9]{64}$/.test(after))throw new Error("Invalid page cursor.");
  const selected=records.filter(r=>(!params.get("source")||r.source_id===params.get("source"))&&(!params.get("county")||r.county===params.get("county"))&&(!params.get("kind")||r.instrument_type===params.get("kind"))&&(!params.get("start")||r.event_date>=params.get("start")!)&&(!params.get("end")||r.event_date<=params.get("end")!)&&(!q||[r.source_record_id,r.notes,r.legal_description,...r.parties.map(p=>p.label)].join(" ").toLowerCase().includes(q.toLowerCase())));
  const page=selected.filter(r=>!after||`${r.event_date}|${r.record_digest}`>after).slice(0,51);const items=page.slice(0,50),last=items.at(-1);
  return {records:items,total:selected.length,nextCursor:page.length>50&&last?`${last.event_date}|${last.record_digest}`:null};
}

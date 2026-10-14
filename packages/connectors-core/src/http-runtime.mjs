/** Portable, bounded HTTP primitives. No source admission, persistence or release. */
export class ConnectionError extends Error {
  constructor(code, status = 400) { super(code); this.code = code; this.status = status; }
}
export const fail = (code, status) => { throw new ConnectionError(code, status); };
export const hash = async bytes => Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", bytes)), b => b.toString(16).padStart(2,"0")).join("");
export const stable = value => JSON.stringify(value, (_key, item) => item && typeof item === "object" && !Array.isArray(item) ? Object.fromEntries(Object.keys(item).sort().map(key=>[key,item[key]])) : item);
export function inputs(spec, supplied = {}) {
  if (!supplied || typeof supplied !== "object" || Array.isArray(supplied) || Object.keys(supplied).some(key => !spec.fields.some(field => field.key === key))) fail("QUERY_REJECTED");
  const result = {};
  for (const field of spec.fields) {
    const value = supplied[field.key] ?? field.default;
    if (typeof value !== "string" || value.length > 100 || !value.trim()) fail("QUERY_REJECTED");
    if (field.options && !field.options.includes(value)) fail("QUERY_REJECTED");
    if (field.type === "date" && (!/^\d{4}-\d{2}-\d{2}$/.test(value) || !Number.isFinite(Date.parse(value)) || new Date(value).toISOString().slice(0,10) !== value)) fail("QUERY_REJECTED");
    if (field.type === "number" && (!/^-?\d+(\.\d+)?$/.test(value) || !Number.isFinite(Number(value)) || Number(value) < field.min || Number(value) > field.max)) fail("QUERY_REJECTED");
    result[field.key] = value;
  }
  if (result.start && result.end) {
    const days = (Date.parse(result.end) - Date.parse(result.start)) / 86400000;
    if (days < 0 || days > (spec.maxDays ?? 31) || result.start < (spec.minDate ?? "1800-01-01") || result.end > new Date().toISOString().slice(0,10)) fail("DATE_RANGE_REJECTED");
  }
  return result;
}
export const field = (key, label, type, value, extra = {}) => ({key,label,type,default:value,...extra});
export const dates = (maxDays = 31) => [field("start","From (UTC)","date","2024-01-01"),field("end","Through (UTC)","date", maxDays < 31 ? "2024-01-07" : "2024-01-31")];
export const location = [field("lat","Latitude","number","37.69",{min:36.9,max:40.1}),field("lon","Longitude","number","-97.34",{min:-102.1,max:-94.5})];
export function area(q) { const lat = Number(q.lat), lon = Number(q.lon); const radius = Number(q.radius ?? "0.025"); return [Math.max(-102.1,lon-radius),Math.max(36.9,lat-radius),Math.min(-94.5,lon+radius),Math.min(40.1,lat+radius)]; }
export function url(base, params) { const value = new URL(base); for(const [key,item] of Object.entries(params)) value.searchParams.set(key,String(item)); return value.href; }
export const jsonRequest = (endpoint, params, extra = {}) => ({url:url(endpoint,params),method:"GET",format:"json",...extra});
export const postJson = (endpoint, body, extra = {}) => ({url:endpoint,method:"POST",body:JSON.stringify(body),format:"json",...extra});
export function configuration(spec, env = {}, query = {}) {
  const product = query.product ?? spec.fields.find(f=>f.key==="product")?.default;
  const missing = (spec.productSecrets?.[product] ?? spec.secrets ?? []).filter(key => typeof env[key] !== "string" || !env[key].trim()).map(key => key);
  const holds = (spec.productConfirmations?.[product] ?? spec.confirmations ?? []).filter(key => env[key] !== "true");
  return {configured:missing.length === 0 && holds.length === 0,missing,holds};
}
/** Reject duplicate JSON keys, excessive nesting and unexpected token syntax. */
export function jsonEntity(text) {
  let i = 0, tokens = 0;
  const ws = () => { while (/\s/.test(text[i] ?? "") && i < text.length) i++; };
  const string = () => { const start=i++; while(i<text.length) { if(text[i] === "\\") {i+=2;continue;} if(text[i++] === '"') return JSON.parse(text.slice(start,i)); } fail("PAYLOAD_REJECTED",502); };
  const item = depth => {
    if (depth>32 || ++tokens>150000) fail("PAYLOAD_REJECTED",502); ws();
    if(text[i]==='"') {string();return;}
    if(text[i]==="{" || text[i]==="[") {
      const object=text[i++]==="{", close=object?"}":"]", keys=new Set(); ws();
      if(text[i]===close){i++;return;}
      for(;;){ws(); if(object){if(text[i]!=='"') fail("PAYLOAD_REJECTED",502);const key=string();if(keys.has(key)) fail("DUPLICATE_JSON_KEY",502);keys.add(key);ws();if(text[i++]!==":") fail("PAYLOAD_REJECTED",502);} item(depth+1);ws();if(text[i]===close){i++;break;}if(text[i++]!==",") fail("PAYLOAD_REJECTED",502);}
      return;
    }
    const token=/^(?:true|false|null|-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)/.exec(text.slice(i));
    if(!token) fail("PAYLOAD_REJECTED",502);i+=token[0].length;
  };
  try {item(0);ws();if(i!==text.length) fail("PAYLOAD_REJECTED",502);return JSON.parse(text,(_key,value)=>{if(typeof value==="number"&&!Number.isFinite(value))fail("PAYLOAD_REJECTED",502);return value;});} catch(error){if(error instanceof ConnectionError) throw error;fail("PAYLOAD_REJECTED",502);}
}
export function csvEntity(text, limit=5000) {
  const rows=[];let row=[],cell="",quoted=false;
  for(let i=0;i<text.length;i++) { const c=text[i]; if(c==='"'){if(quoted&&text[i+1]==='"'){cell+='"';i++;}else if(!quoted&&cell.length) fail("PAYLOAD_REJECTED",502);else quoted=!quoted;}
    else if(!quoted&&(c===","||c==="\n"||c==="\r")){row.push(cell);cell="";if(c!==","){if(c==="\r"&&text[i+1]==="\n")i++;if(row.some(x=>x.length))rows.push(row);row=[];if(rows.length>limit+1)fail("ROW_LIMIT_REACHED",502);}}else cell+=c;
  }
  if(quoted)fail("PAYLOAD_REJECTED",502);if(cell.length||row.length){row.push(cell);rows.push(row);}
  if(!rows.length)return [];
  const header=rows.shift().map(x=>x.replace(/^\uFEFF/,""));if(new Set(header).size!==header.length||header.length>256)fail("PAYLOAD_REJECTED",502);
  return rows.map(r=>{if(r.length!==header.length)fail("PAYLOAD_REJECTED",502);return Object.fromEntries(header.map((k,i)=>[k,r[i]]));});
}
export function table(columns, rows) {
  if(!Array.isArray(columns)||!columns.length||columns.length>150||columns.some(x=>typeof x!=="string")||new Set(columns).size!==columns.length||!Array.isArray(rows)||rows.length>5000)fail("PAYLOAD_REJECTED",502);
  return rows.map(row=>{if(!Array.isArray(row)||row.length!==columns.length)fail("PAYLOAD_REJECTED",502);return Object.fromEntries(columns.map((key,i)=>[key,row[i]]));});
}
export function records(value, cap=1000) {
  if(!Array.isArray(value)||value.length>5000||value.some(x=>!x||typeof x!=="object"||Array.isArray(x))) fail("PAYLOAD_REJECTED",502);
  return {rows:value.slice(0,cap),partial:value.length>cap,total:value.length};
}
export function features(value, cap=500) {
  if(value?.type!=="FeatureCollection"||!Array.isArray(value.features)||value.features.length>5000)fail("PAYLOAD_REJECTED",502);
  const selected=value.features.slice(0,cap);let points=0;
  function coordinates(c){if(!Array.isArray(c))fail("GEOMETRY_REJECTED",502);if(typeof c[0]==="number"){if(++points>100000||c.length<2||c.some(n=>typeof n!=="number"||!Number.isFinite(n))||c[0]<-180||c[0]>180||c[1]<-90||c[1]>90)fail("GEOMETRY_REJECTED",502);}else for(const v of c)coordinates(v);}
  for(const f of selected){if(f?.type!=="Feature"||!f.properties||typeof f.properties!=="object"||Array.isArray(f.properties))fail("PAYLOAD_REJECTED",502);if(f.geometry){if(!["Point","MultiPoint","LineString","MultiLineString","Polygon","MultiPolygon"].includes(f.geometry.type))fail("GEOMETRY_REJECTED",502);coordinates(f.geometry.coordinates);}}
  return {rows:selected.map(f=>({...f.properties,source_feature_id:f.id??null})),features:selected,partial:value.features.length>cap||!!value.exceededTransferLimit||!!value.links?.some?.(x=>x.rel==="next"),total:value.features.length};
}
export async function readBounded(response, limit) {
  if(!response.body||Number(response.headers.get("content-length"))>limit)fail("RESPONSE_TOO_LARGE",502);
  const reader=response.body.getReader();const chunks=[];let length=0;
  try {for(;;){const {value,done}=await reader.read();if(done)break;length+=value.byteLength;if(length>limit){await reader.cancel();fail("RESPONSE_TOO_LARGE",502);}chunks.push(value);}}finally{reader.releaseLock();}
  const bytes=new Uint8Array(length);let at=0;for(const value of chunks){bytes.set(value,at);at+=value.length;}return bytes;
}
export async function transport(request, env, fetcher, signal, limit) {
  const endpoint=new URL(request.url); const headers={Accept:request.format==="csv"?"text/csv":request.format==="png"?"image/png":"application/json",...request.headers};
  for(const auth of request.auth??[]) {const value=env[auth.secret];if(typeof value!=="string"||!(auth.secret.endsWith("EMAIL")?/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/.test(value):/^[A-Za-z0-9_-]{16,128}$/.test(value)))fail("CREDENTIAL_REQUIRED",409);if(auth.header)headers[auth.header]=value;else endpoint.searchParams.set(auth.param,value);}
  let response;
  try {response=await fetcher(endpoint.href,{method:request.method,headers,body:request.body,redirect:"manual",cache:"no-store",signal});} catch {fail(signal.aborted?"UPSTREAM_TIMEOUT":"UPSTREAM_UNAVAILABLE",502);}
  if(response.status!==200){await response.body?.cancel();fail(response.status===429?"PROVIDER_RATE_LIMIT":response.status===401||response.status===403?"PROVIDER_ACCESS_HELD":"UPSTREAM_UNAVAILABLE",502);}
  const receivedType=response.headers.get("content-type")??"";
  if(request.format==="png"?!/^image\/png(?:;|$)/i.test(receivedType):request.format==="csv"?!/^(?:text\/(?:csv|plain)|application\/octet-stream)(?:;|$)/i.test(receivedType):!/^(?:application\/(?:geo\+)?json|text\/json)(?:;|$)/i.test(receivedType)){await response.body?.cancel();fail("CONTENT_TYPE_REJECTED",502);}
  // MIME parameters are unnecessary for replay and may echo query credentials.
  const type=receivedType.split(";")[0].toLowerCase();
  let bytes=await readBounded(response,limit);const originalSha256=await hash(bytes);let redactions=0;
  // Some key-based providers echo credentials in response metadata. Never store
  // those secrets; record the received digest and explicit storage transform.
  const scrub=text=>{for(const auth of request.auth??[]){const secret=env[auth.secret];for(const token of new Set([secret,encodeURIComponent(secret)])){if(text.includes(token)){const parts=text.split(token);redactions+=parts.length-1;text=parts.join("[credential-redacted]");}}}return text;};
  if(request.auth?.length){
   // All current credentialed profiles are JSON. Parse before storage so escaped
   // keys/values cannot retain a secret. Malformed credentialed bodies fail closed.
   if(request.format!=="json")fail("CREDENTIAL_FORMAT_HELD",502);
   const redact=value=>{
    if(typeof value==="string")return scrub(value);
    if(Array.isArray(value))return value.map(redact);
    if(value&&typeof value==="object"){const entries=Object.entries(value).map(([key,item])=>[scrub(key),redact(item)]);if(new Set(entries.map(([key])=>key)).size!==entries.length)fail("CREDENTIAL_REDACTION_AMBIGUOUS",502);return Object.fromEntries(entries);}
    return value;
   };
   const value=redact(jsonEntity(new TextDecoder("utf-8",{fatal:true}).decode(bytes)));
   if(redactions)bytes=new TextEncoder().encode(JSON.stringify(value));
  }
  if(bytes.length>limit)fail("RESPONSE_TOO_LARGE",502);
  // Untrusted validator headers are optional. Omit them for keyed requests;
  // their arbitrary encodings are not needed for the source-body integrity proof.
  const etag=request.auth?.length?"":(response.headers.get("etag")??"").slice(0,256),modified=request.auth?.length?"":(response.headers.get("last-modified")??"").slice(0,128);
  return {bytes,type,originalSha256,redactions,etag,modified};
}

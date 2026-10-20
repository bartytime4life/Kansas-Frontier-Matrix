// Shared by the KFM server (signer) and the home gateway (verifier) so both
// sides always agree on one request-signing scheme. No dependencies.
import {createHash,createHmac,randomBytes,timingSafeEqual} from 'node:crypto';

export const SIGNATURE_SCHEME='KFM-HOME-INFERENCE-V1';
export const SIGNATURE_HEADERS=Object.freeze({keyId:'x-kfm-key-id',timestamp:'x-kfm-timestamp',nonce:'x-kfm-nonce',signature:'x-kfm-signature'});
export const RESPONSE_SIGNATURE_HEADER='x-kfm-response-signature';
// A request older or newer than this is refused; the nonce cache covers the window.
export const SIGNATURE_MAX_SKEW_MS=60000;
export const MIN_SECRET_BYTES=32;

const KEY_ID=/^[A-Za-z0-9._-]{1,64}$/;
const NONCE=/^[A-Za-z0-9_-]{22,64}$/;
const SIGNATURE=/^[A-Za-z0-9_-]{43}$/;

export const bodyDigest=body=>createHash('sha256').update(body??'').digest('hex');

export function decodeSecret(value){
 if(typeof value!=='string'||!/^[A-Za-z0-9_-]+={0,2}$/.test(value))return null;
 const bytes=Buffer.from(value,'base64url');
 return bytes.length>=MIN_SECRET_BYTES?bytes:null;
}

export const newSecret=()=>randomBytes(MIN_SECRET_BYTES).toString('base64url');

function canonical({method,path,timestamp,nonce,body}){
 return [SIGNATURE_SCHEME,method.toUpperCase(),path,timestamp,nonce,bodyDigest(body)].join('\n');
}

export function signRequest({keyId,secret,method,path,body='',now=Date.now(),nonce=randomBytes(18).toString('base64url')}){
 const key=typeof secret==='string'?decodeSecret(secret):secret;
 if(!KEY_ID.test(keyId??'')||!Buffer.isBuffer(key)||key.length<MIN_SECRET_BYTES)throw Object.assign(new Error('SIGNING_KEY_INVALID'),{code:'SIGNING_KEY_INVALID'});
 const timestamp=String(Math.trunc(now));
 const signature=createHmac('sha256',key).update(canonical({method,path,timestamp,nonce,body})).digest('base64url');
 return {[SIGNATURE_HEADERS.keyId]:keyId,[SIGNATURE_HEADERS.timestamp]:timestamp,[SIGNATURE_HEADERS.nonce]:nonce,[SIGNATURE_HEADERS.signature]:signature};
}

const header=(headers,name)=>typeof headers?.get==='function'?headers.get(name):headers?.[name];

// Separate domain from request signatures. Authenticate the exact response bytes
// and HTTP status against this request's nonce, timestamp, method, path and body.
// Health and authenticated error replies need the same binding as successful chat.
export function signResponse({secret,requestHeaders,method,path,requestBody='',status,body}){
 const key=typeof secret==='string'?decodeSecret(secret):secret;
 if(!Buffer.isBuffer(key)||key.length<MIN_SECRET_BYTES)throw Object.assign(new Error('SIGNING_KEY_INVALID'),{code:'SIGNING_KEY_INVALID'});
 const canonical=['KFM-HOME-INFERENCE-RESPONSE-V1',header(requestHeaders,SIGNATURE_HEADERS.keyId),method.toUpperCase(),path,
  header(requestHeaders,SIGNATURE_HEADERS.timestamp),header(requestHeaders,SIGNATURE_HEADERS.nonce),bodyDigest(requestBody),String(status),bodyDigest(body)].join('\n');
 return createHmac('sha256',key).update(canonical).digest('base64url');
}

export function verifyResponse({headers,...request}){
 const supplied=header(headers,RESPONSE_SIGNATURE_HEADER);
 if(typeof supplied!=='string'||!SIGNATURE.test(supplied))return false;
 const expected=Buffer.from(signResponse(request),'base64url'),actual=Buffer.from(supplied,'base64url');
 return actual.length===expected.length&&timingSafeEqual(actual,expected);
}

// Bounded replay memory: a nonce is remembered for the full freshness window.
export function createNonceCache({limit=20000,clock=Date.now}={}){
 const seen=new Map();
 return {
  claim(nonce){
   const now=clock();
   for(const [value,expires]of seen){if(expires>now)break;seen.delete(value);}
   if(seen.has(nonce))return 'REPLAYED';
   if(seen.size>=limit)return 'REPLAY_CACHE_FULL';
   seen.set(nonce,now+2*SIGNATURE_MAX_SKEW_MS);
   return 'OK';
  },
  get size(){return seen.size;},
 };
}

// Returns {ok:true,key} or {ok:false,reason}. Reasons are for operator logs only;
// callers must answer every failure identically so they are not an oracle.
export function verifyRequest({headers,method,path,body,keys,nonces,now=Date.now()}){
 const read=name=>{const value=typeof headers.get==='function'?headers.get(name):headers[name];return typeof value==='string'?value:'';};
 const keyId=read(SIGNATURE_HEADERS.keyId),timestamp=read(SIGNATURE_HEADERS.timestamp),nonce=read(SIGNATURE_HEADERS.nonce),signature=read(SIGNATURE_HEADERS.signature);
 if(!keyId&&!timestamp&&!nonce&&!signature)return {ok:false,reason:'MISSING'};
 if(!KEY_ID.test(keyId)||!/^[0-9]{13}$/.test(timestamp)||!NONCE.test(nonce)||!SIGNATURE.test(signature))return {ok:false,reason:'MALFORMED'};
 const key=keys.get(keyId);
 if(!key)return {ok:false,reason:'UNKNOWN_KEY'};
 if(Math.abs(now-Number(timestamp))>SIGNATURE_MAX_SKEW_MS)return {ok:false,reason:'STALE'};
 const expected=createHmac('sha256',key.secret).update(canonical({method,path,timestamp,nonce,body})).digest();
 const supplied=Buffer.from(signature,'base64url');
 if(supplied.length!==expected.length||!timingSafeEqual(supplied,expected))return {ok:false,reason:'BAD_SIGNATURE'};
 // Claim the nonce only after the signature verifies, so forged traffic cannot fill the cache.
 const claim=nonces.claim(keyId+':'+nonce);
 if(claim!=='OK')return {ok:false,reason:claim};
 return {ok:true,key};
}

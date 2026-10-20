// Wire contract between the KFM web server (server/home-ai-model.mjs) and the
// home inference gateway (home-inference-gateway.mjs). This directory is copied
// as-is to the inference PC, so it imports nothing outside node: built-ins.
import {createHash,createHmac,randomBytes,timingSafeEqual} from 'node:crypto';

export const HOME_AI_CONTRACT='kfm-home-inference-v1';
export const HOME_AI_PATHS=Object.freeze({health:'/v1/health',discuss:'/v1/discuss'});
export const HOME_AI_HEADERS=Object.freeze({key:'x-kfm-key',time:'x-kfm-time',nonce:'x-kfm-nonce',signature:'x-kfm-signature',reply:'x-kfm-reply-signature'});
export const HOME_AI_MAX_REQUEST_BYTES=32768;
export const HOME_AI_MAX_RESPONSE_BYTES=24576;
export const HOME_AI_MAX_MESSAGE_BYTES=8192;
export const HOME_AI_MAX_MESSAGES=8;
// Signed requests are accepted for this long either side of the gateway clock.
export const HOME_AI_CLOCK_SKEW_MS=60000;
export const HOME_AI_FINISH_REASONS=Object.freeze(['stop','length','time_limit']);

const KEY_ID=/^[a-z0-9][a-z0-9-]{0,31}$/;
const NONCE=/^[A-Za-z0-9_-]{22,64}$/;
const SIGNATURE=/^[a-f0-9]{64}$/;
export const PROFILE_ID=/^[a-z0-9][a-z0-9-]{0,47}$/;
export const MODEL_TAG=/^[a-z0-9][a-z0-9._/-]{0,79}(?::[A-Za-z0-9._-]{1,64})?$/;
export const MODEL_DIGEST=/^sha256:[a-f0-9]{64}$/;
const CONTROL=/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/;

export const validKeyId=value=>typeof value==='string'&&KEY_ID.test(value);
// Secrets are at least 32 random bytes, written as unpadded base64url.
export const decodeSecret=value=>typeof value==='string'&&/^[A-Za-z0-9_-]{43,128}$/.test(value)?Buffer.from(value,'base64url'):null;
export const newSecret=()=>randomBytes(32).toString('base64url');
const sha256=value=>createHash('sha256').update(value).digest('hex');
const mac=(secret,value)=>createHmac('sha256',secret).update(value).digest('hex');
const same=(a,b)=>typeof a==='string'&&typeof b==='string'&&a.length===b.length&&timingSafeEqual(Buffer.from(a),Buffer.from(b));
const canonical=({method,path,time,nonce,body})=>[HOME_AI_CONTRACT,method,path,time,nonce,sha256(body)].join('\n');
const fail=code=>{throw Object.assign(new Error(code),{code});};

export function signRequest({keyId,secret,method,path,body='',clock=Date.now}){
 const time=String(clock()),nonce=randomBytes(24).toString('base64url');
 return {nonce,headers:{[HOME_AI_HEADERS.key]:keyId,[HOME_AI_HEADERS.time]:time,[HOME_AI_HEADERS.nonce]:nonce,[HOME_AI_HEADERS.signature]:mac(secret,canonical({method,path,time,nonce,body}))}};
}

// A bounded replay cache. When it is full of unexpired nonces, new requests are
// refused rather than evicting a nonce that could then be replayed.
export function createNonceCache({limit=4096,clock=Date.now}={}){
 const seen=new Map();
 return {claim(nonce){
  const now=clock();
  if(seen.size>=limit)for(const [key,expires]of seen)if(expires<=now)seen.delete(key);
  if(seen.has(nonce)||seen.size>=limit)return false;
  seen.set(nonce,now+2*HOME_AI_CLOCK_SKEW_MS);return true;
 },get size(){return seen.size;}};
}

// Returns the authenticated key ID or throws GATEWAY_UNAUTHORIZED. `get` reads
// one lower-case request header. `keys` maps key ID to a decoded secret.
export function verifyRequest({get,method,path,body='',keys,nonces,clock=Date.now}){
 const keyId=get(HOME_AI_HEADERS.key),time=get(HOME_AI_HEADERS.time),nonce=get(HOME_AI_HEADERS.nonce),signature=get(HOME_AI_HEADERS.signature);
 const secret=validKeyId(keyId)?keys.get(keyId):undefined;
 if(!secret||typeof time!=='string'||!/^\d{13}$/.test(time)||typeof nonce!=='string'||!NONCE.test(nonce)||typeof signature!=='string'||!SIGNATURE.test(signature))fail('GATEWAY_UNAUTHORIZED');
 if(Math.abs(clock()-Number(time))>HOME_AI_CLOCK_SKEW_MS)fail('GATEWAY_UNAUTHORIZED');
 if(!same(signature,mac(secret,canonical({method,path,time,nonce,body}))))fail('GATEWAY_UNAUTHORIZED');
 // Claim the nonce only after the signature verifies, so forged requests cannot fill the cache.
 if(!nonces.claim(nonce))fail('GATEWAY_UNAUTHORIZED');
 return keyId;
}

// The gateway binds each reply to the request nonce, so a misrouted hostname or a
// replayed response cannot be accepted as this request's model output.
export const signReply=(secret,nonce,status,body)=>mac(secret,[HOME_AI_CONTRACT,'reply',nonce,String(status),sha256(body)].join('\n'));
export const verifyReply=(secret,nonce,status,body,signature)=>typeof signature==='string'&&SIGNATURE.test(signature)&&same(signature,signReply(secret,nonce,status,body));

const text=(value,max)=>typeof value==='string'&&value.length>0&&Buffer.byteLength(value)<=max&&!CONTROL.test(value);
export const messageBytes=messages=>messages.reduce((total,message)=>total+Buffer.byteLength(message.content),0);

// The only request shape the gateway runs: one system message, then alternating
// user/assistant turns ending with the user's question. No tools, images,
// formats, model names or sampling options cross this boundary.
export function validDiscussRequest(value){
 if(!value||typeof value!=='object'||Array.isArray(value))return false;
 const keys=Object.keys(value);
 if(keys.length!==3||!['profile','depth','messages'].every(key=>keys.includes(key)))return false;
 if(typeof value.profile!=='string'||!PROFILE_ID.test(value.profile)||!['brief','expanded'].includes(value.depth))return false;
 const {messages}=value;
 if(!Array.isArray(messages)||messages.length<2||messages.length>HOME_AI_MAX_MESSAGES||messages.length%2!==0)return false;
 return messages.every((message,index)=>message&&typeof message==='object'&&Object.keys(message).length===2&&
  message.role===(index===0?'system':index%2===1?'user':'assistant')&&text(message.content,HOME_AI_MAX_MESSAGE_BYTES));
}

import {createHash} from 'node:crypto';
import {gzipSync} from 'node:zlib';
// Negotiate gzip only when the client actually accepts it; explicit q=0 wins.
const acceptsGzip=value=>{
 const tokens=(value??'').split(',').map(s=>s.trim().toLowerCase()).filter(Boolean),gzip=tokens.find(s=>s.split(';')[0].trim()==='gzip');
 if(!gzip)return false;const params=gzip.split(';').slice(1);const q=params.find(p=>p.trim().startsWith('q='));return q===undefined||/^\s*q=(?:0(?:\.\d{1,3})?|1(?:\.0{1,3})?)\s*$/.test(q)&&Number(q.split('=')[1])>0;
};
export function terrainResponse(value,{state,at,maxAge,tier,request,replyBytes=1000000}){
 const bytes=Buffer.from(JSON.stringify({...value,cache:{state,at:new Date(at).toISOString()}}));
 if(bytes.length>replyBytes)return Response.json({reasonCode:'REPLY_TOO_LARGE'},{status:413,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});
 const etag='W/"'+createHash('sha256').update(bytes).digest('hex')+'"',headers=new Headers({'Content-Type':'application/json','Cache-Control':'public, max-age='+maxAge,'X-Content-Type-Options':'nosniff','X-KFM-Terrain-Cache':tier,'Vary':'Accept-Encoding','ETag':etag});
 // A processing receipt must be re-requested, never held as a completed result.
 if(maxAge>0&&(request?.headers.get('if-none-match')??'').split(',').some(t=>t.trim()===etag||t.trim()==='*'))return new Response(null,{status:304,headers});
 let body=bytes;if(bytes.length>=1024&&acceptsGzip(request?.headers.get('accept-encoding'))){const packed=gzipSync(bytes,{level:4});if(packed.length<bytes.length){body=packed;headers.set('Content-Encoding','gzip');}}
 headers.set('Content-Length',String(body.length));return new Response(body,{headers});
}

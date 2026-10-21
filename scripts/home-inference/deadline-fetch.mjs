// Signed gateway replies arrive only when generation finishes. Node fetch's
// default 300-second headers timeout would cut off our longer queue allowance.
// Core HTTP has no independent headers deadline here: the caller's AbortSignal
// controls the entire request and response. Redirects are returned, never followed.
import {request as httpRequest} from 'node:http';
import {request as httpsRequest} from 'node:https';
import {Readable} from 'node:stream';

export function deadlineFetch(input,{method='GET',headers={},body,signal}={}){
 return new Promise((resolve,reject)=>{
  const url=new URL(input);
  if(!['http:','https:'].includes(url.protocol)||url.username||url.password){reject(new TypeError('Invalid transport URL'));return;}
  const request=url.protocol==='https:'?httpsRequest:httpRequest;
  const req=request(url,{method,headers:Object.fromEntries(new Headers(headers)),signal},res=>{
   try{
    const responseHeaders=new Headers();
    for(let i=0;i<res.rawHeaders.length;i+=2)responseHeaders.append(res.rawHeaders[i],res.rawHeaders[i+1]);
    const empty=method==='HEAD'||[204,205,304].includes(res.statusCode);
    if(empty)res.resume();
    resolve(new Response(empty?null:Readable.toWeb(res),{status:res.statusCode,headers:responseHeaders}));
   }catch(error){res.destroy();reject(error);}
  });
  req.setTimeout(0);
  req.on('error',reject);
  req.end(body);
 });
}

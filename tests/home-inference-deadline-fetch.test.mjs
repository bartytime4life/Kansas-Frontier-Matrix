import test from 'node:test';
import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {deadlineFetch} from '../scripts/home-inference/deadline-fetch.mjs';

test('deadline transport preserves signed bytes and refuses to follow redirects',async()=>{
 let followed=0,received='',receivedHeaders;
 const server=createServer(async(req,res)=>{
  if(req.url==='/target'){followed++;res.end('unexpected');return;}
  if(req.url==='/redirect'){res.writeHead(302,{Location:'/target'});res.end();return;}
  receivedHeaders=req.headers;
  for await(const chunk of req)received+=chunk;
  res.writeHead(200,{'Content-Type':'application/json','X-KFM-Response-Signature':'synthetic'});
  res.end('{"text":"County seat — café"}');
 });
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const origin='http://127.0.0.1:'+server.address().port;
 try{
  const response=await deadlineFetch(origin,{method:'POST',headers:{'Content-Type':'application/json'},body:'{"synthetic":true}',signal:AbortSignal.timeout(1000)});
  assert.equal(received,'{"synthetic":true}');
  assert.equal(receivedHeaders['user-agent'],'node');
  assert.equal(receivedHeaders.accept,'*/*');
  assert.equal(response.headers.get('x-kfm-response-signature'),'synthetic');
  assert.equal(await response.text(),'{"text":"County seat — café"}');
  assert.equal((await deadlineFetch(origin+'/redirect',{signal:AbortSignal.timeout(1000)})).status,302);
  assert.equal(followed,0);
 }finally{server.closeAllConnections();await new Promise(resolve=>server.close(resolve));}
});

test('the explicit deadline aborts both delayed headers and an unfinished response body',async()=>{
 const server=createServer((req,res)=>{if(req.url==='/body'){res.writeHead(200,{'Content-Type':'application/json'});res.flushHeaders();}});
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const origin='http://127.0.0.1:'+server.address().port;
 try{
  await assert.rejects(deadlineFetch(origin,{signal:AbortSignal.timeout(30)}));
  const response=await deadlineFetch(origin+'/body',{signal:AbortSignal.timeout(30)});
  await assert.rejects(response.text());
 }finally{server.closeAllConnections();await new Promise(resolve=>server.close(resolve));}
});

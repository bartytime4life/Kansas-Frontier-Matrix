import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {readFile} from 'node:fs/promises';
import test from 'node:test';

// Exercise the mirror dependency codec exports in separate React-server and
// ordinary SSR environments. These are harmless upstream transport regressions,
// not a code-execution payload or proof of an exploitable application route.
const encoder=`
import {renderToReadableStream} from 'react-server-dom-webpack/server.edge';
const kind=process.argv[1],backing=new ArrayBuffer(10000),view=new Uint8Array(backing);
view.fill(7);
let first=view,second=view;
if(kind==='alias'){second=new Uint8Array(backing);}
if(kind==='mixed-alias'){second=new DataView(backing);}
if(kind==='partial'){first=view.subarray(0,5000);second=view.subarray(5000);first.fill(1);second.fill(2);}
if(kind==='independent'){second=new Uint8Array(10000).fill(3);}
if(kind==='independent-data-view'){second=new DataView(new Uint8Array(10000).fill(3).buffer);}
const label='ordinary Flight data';
const errors=[];
const render=(model,options)=>renderToReadableStream(model,{},options);
const stream=await render(Promise.resolve({label,first,second}),
 {onError(error){errors.push(String(error.message));return 'KFM_TYPED_ARRAY_REGRESSION';}});
try{
 const wire=Buffer.from(await new Response(stream).arrayBuffer()).toString('base64');
 process.stdout.write(JSON.stringify({transport:'fulfilled',wire,errors,remainingBytes:backing.byteLength}));
}catch(error){process.stdout.write(JSON.stringify({transport:'rejected',message:error.message,errors}));}
`;
const decoder=`
import {readFileSync} from 'node:fs';
import {createFromReadableStream} from 'react-server-dom-webpack/client.edge';
const wire=Buffer.from(readFileSync(0,'utf8'),'base64');
try{
 const result=await createFromReadableStream(new Response(wire).body,
  {serverConsumerManifest:{moduleMap:null,serverModuleMap:null,moduleLoading:null}});
 const bytes=view=>Array.from(new Uint8Array(view.buffer,view.byteOffset,view.byteLength));
 process.stdout.write(JSON.stringify({status:'fulfilled',label:result.label,first:bytes(result.first),
  second:bytes(result.second),secondType:result.second.constructor.name,sameIdentity:result.first===result.second}));
}catch(error){process.stdout.write(JSON.stringify({status:'rejected',digest:error.digest,message:error.message}));}
`;
function run(source,args=[],input){
 return JSON.parse(execFileSync(process.execPath,args.concat(['--input-type=module','-e',source]),{
  cwd:process.cwd(),env:{...process.env,NODE_ENV:'production'},encoding:'utf8',input,timeout:10000,maxBuffer:1024*1024,
 }));
}
// Put the case after the evaluated source so Node exposes it as argv[1].
function roundTrip(kind){
 const encoded=JSON.parse(execFileSync(process.execPath,['--conditions=react-server','--input-type=module','-e',encoder,kind],{
  cwd:process.cwd(),env:{...process.env,NODE_ENV:'production'},encoding:'utf8',timeout:10000,maxBuffer:1024*1024,
 }));
 return{...encoded,decoded:encoded.transport==='fulfilled'?run(decoder,[],encoded.wire):null};
}

for(const kind of ['alias','mixed-alias']){
 test(`Flight refuses unsafe distinct full-buffer views: ${kind}`,()=>{
  assert.ok(Object.hasOwn(ArrayBuffer.prototype,'detached'),'the supported Node runtime exposes detached-buffer state');
  const result=roundTrip(kind);
  assert.ok(result.transport==='rejected'||result.decoded?.status==='rejected','distinct full-buffer views must not both enter the stream');
  assert.match([result.message,...result.errors].join('\n'),/detached (?:Array)?buffer|#612/i);
 });
}
test('Flight keeps independent arrays and ordinary fields intact',()=>{
 const result=roundTrip('independent');assert.deepEqual(result.errors,[]);assert.equal(result.decoded.status,'fulfilled');
 assert.equal(result.decoded.label,'ordinary Flight data');
 assert.deepEqual(result.decoded.first,new Array(10000).fill(7));assert.deepEqual(result.decoded.second,new Array(10000).fill(3));
});
test('Flight keeps an independent DataView intact',()=>{
 const result=roundTrip('independent-data-view');assert.deepEqual(result.errors,[]);assert.equal(result.decoded.status,'fulfilled');
 assert.equal(result.decoded.secondType,'DataView');assert.deepEqual(result.decoded.second,new Array(10000).fill(3));
});
test('Flight copies promised partial views without detaching their shared backing buffer',()=>{
 const result=roundTrip('partial');assert.deepEqual(result.errors,[]);assert.equal(result.decoded.status,'fulfilled');
 assert.deepEqual(result.decoded.first,new Array(5000).fill(1));assert.deepEqual(result.decoded.second,new Array(5000).fill(2));
 assert.equal(result.remainingBytes,10000);
});
test('Flight preserves repeated references to the same view',()=>{
 const result=roundTrip('identity');assert.deepEqual(result.errors,[]);assert.equal(result.decoded.status,'fulfilled');
 assert.equal(result.decoded.sameIdentity,true);assert.deepEqual(result.decoded.first,new Array(10000).fill(7));
});
test('both built mirror server environments select the patched direct codec',async()=>{
 const pkg=JSON.parse(await readFile('package.json','utf8'));
 assert.equal(pkg.dependencies.react,pkg.devDependencies['react-server-dom-webpack']);
 assert.equal(pkg.dependencies['react-dom'],pkg.dependencies.react);
 for(const file of ['dist/server/index.js','dist/server/ssr/index.js']){
  const code=await readFile(file,'utf8');
  assert.match(code,/node_modules\/react-server-dom-webpack\/cjs\//,file+' selects the direct codec');
  assert.doesNotMatch(code,/@vitejs\/plugin-rsc\/dist\/vendor\/react-server-dom\/cjs\//,file+' excludes the plugin fallback');
  assert.doesNotMatch(code,/node_modules\/next\/dist\/compiled\/react-server-dom/,file+' excludes the Next fallback');
  if(file==='dist/server/index.js')assert.ok(code.includes(JSON.stringify(pkg.dependencies.react)), 'the server contains the declared React version guard');
 }
});

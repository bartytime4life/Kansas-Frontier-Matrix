import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {nativeLidarBrowserFixtures} from './native-lidar-browser-fixtures.mjs';
async function setup({rootReady=true}={}){
 const scripts=[],fixtures=await nativeLidarBrowserFixtures(new URL('http://127.0.0.1:5197'),{solid:true});await fixtures.setup(async(method,args)=>{if(method==='Page.addScriptToEvaluateOnNewDocument')scripts.push(args.source);});
 const source=scripts.find(s=>s.includes('window.__solidVisibleCell=')),vertices=[];
 for(let row=0;row<96;row++)for(let col=0;col<96;col++)for(const [dx,dy] of [[0,0],[.01,0],[.01,.01],[0,0],[.01,.01],[0,.01]])vertices.push(-.8+col/60+dx,-.8+row/60+dy,0,.5,.5,.5,row*96+col+1);
 const reads=[],window={},rect={left:11.3,top:22.6,width:1280,height:704},canvas={getBoundingClientRect:()=>rect};let observer,observations=0,occluded=()=>false,answer=()=>null;const listeners=[];
 const document={documentElement:rootReady?{}:null,addEventListener:(type,fn,options)=>listeners.push({type,fn,options}),elementFromPoint:(x,y)=>occluded(x,y)?{}:canvas},layer={failed:false,pick(point){reads.push(point);return answer(point);}},map={getCanvas:()=>canvas,getLayer:()=>({implementation:layer})};
 class Observer{constructor(fn){observer=fn;}observe(root){assert.equal(root,document.documentElement);observations++;}}
 new Function('window','document','MutationObserver',source)(window,document,Observer);Object.assign(window,{__terrainAcceptanceMap:map,__solidFixtureVertices:Float32Array.from(vertices),__solidFixtureMatrix:[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],__solidFixtureFrames:7});
 return {window,rect,reads,layer,map,listeners,observations:()=>observations,ready:()=>{document.documentElement||={};for(const listener of listeners)listener.fn();},probe:()=>{reads.length=0;return window.__solidVisibleCell();},answer:fn=>{answer=fn;},occlude:fn=>{occluded=fn;observer();}};
}
test('solid probe bounds null-frame readbacks to64 spatially distributed actual pixels and finds coverage beyond the first64source cells',async()=>{
 const s=await setup();assert.equal(s.probe(),null);assert.equal(s.reads.length,64);assert.ok(Math.max(...s.reads.map(p=>p.y))-Math.min(...s.reads.map(p=>p.y))>s.rect.height*.6);assert.ok(Math.max(...s.reads.map(p=>p.x))-Math.min(...s.reads.map(p=>p.x))>s.rect.width*.6);
 const builds=s.window.__solidProbeStats.builds;assert.equal(s.probe(),null);assert.equal(s.reads.length,64);assert.equal(s.window.__solidProbeStats.builds,builds,'unchanged projected geometry is reused');
 s.answer(p=>p.x>s.rect.width*.6&&p.y<s.rect.height*.35?7000:null);const hit=s.probe();assert.equal(hit.index,7000);assert.ok(s.reads.length<=64);assert.equal(hit.frame,7);assert.ok(Number.isInteger(hit.x)&&Number.isInteger(hit.y));assert.equal(s.reads.at(-1).x,hit.x-s.rect.left);assert.equal(s.reads.at(-1).y,hit.y-s.rect.top);
 s.answer(()=>7001);assert.equal(s.probe().index,7001,'cached candidate must use a new real GPU-ID answer');assert.equal(s.reads.length,1);s.answer(()=>null);assert.equal(s.probe(),null,'an invalidated/background frame never reuses a cached source ID');assert.ok(s.reads.length<=64);
});
test('solid probe invalidates projection candidates on camera,geometry,resource,canvas and DOM occlusion changes without selecting covered pixels',async()=>{
 const s=await setup();s.answer(()=>8000);assert.equal(s.probe().index,8000);let builds=s.window.__solidProbeStats.builds;
 for(const change of [()=>{s.window.__solidFixtureMatrix[12]=.05;},()=>{s.window.__solidFixtureVertices=s.window.__solidFixtureVertices.slice();},()=>{const replacement={...s.layer};s.map.getLayer=()=>({implementation:replacement});},()=>{s.rect.width=900;},()=>{s.occlude(()=>false);}]){change();assert.equal(s.probe().index,8000);assert.equal(s.window.__solidProbeStats.builds,++builds);assert.ok(s.reads.length<=64);}
 const old=s.probe();s.occlude((x,y)=>x===old.x&&y===old.y);const newHit=s.probe();assert.ok(newHit);assert.notDeepEqual([newHit.x,newHit.y],[old.x,old.y]);assert.ok(!s.reads.some(p=>p.x===old.x-s.rect.left&&p.y===old.y-s.rect.top));s.occlude(()=>true);assert.equal(s.probe(),null);assert.equal(s.reads.length,0,'HUD-covered pixels are never passed to GPU picking');
});

test('solid probe attaches the DOM observer once when new-document injection precedes the document element',async()=>{
 const s=await setup({rootReady:false});assert.equal(s.observations(),0);assert.equal(s.listeners.length,1);assert.equal(s.listeners[0].type,'DOMContentLoaded');assert.deepEqual(s.listeners[0].options,{once:true});
 s.ready();assert.equal(s.observations(),1);s.ready();assert.equal(s.observations(),1,'duplicate readiness notifications cannot attach duplicate observers');
 s.answer(()=>9000);assert.equal(s.probe().index,9000);const builds=s.window.__solidProbeStats.builds,revision=s.window.__solidProbeDOMRevision;s.occlude(()=>false);assert.equal(s.window.__solidProbeDOMRevision,revision+1);assert.equal(s.probe().index,9000);assert.equal(s.window.__solidProbeStats.builds,builds+1,'the late-attached observer invalidates projected candidates after DOM changes');
});

test('solid browser readiness rejects the preceding selected mode, pending receipt and missing resource before recording request counts',async()=>{
 const source=await readFile('tests/explorer-startup.browser.mjs','utf8'),ast=ts.createSourceFile('explorer-startup.browser.mjs',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.JS);let readySource;
 const visit=node=>{if(ts.isVariableDeclaration(node)&&node.name.getText(ast)==='waitSolidReady')readySource=node.initializer.getText(ast);ts.forEachChild(node,visit);};visit(ast);assert.ok(readySource);
 let selected='Surface',state='idle',disabled=false,layer={failed:false};const inspect={textContent:'Inspect landscape in 3D',get disabled(){return disabled;}},selection=['Ground','Surface','Canopy height'].map(textContent=>({textContent,getAttribute:name=>name==='aria-label'?textContent:textContent===selected?'true':'false'}));
 const panel={querySelectorAll:selector=>selector==='[aria-label="Terrain layer selection"] button'?selection:selector==='button'?[inspect]:selector==='li'?[{querySelector:tag=>({textContent:tag==='strong'?'canopy':state})}]:[]},document={querySelector:()=>panel},window={__terrainAcceptanceMap:{getLayer:()=>layer?{implementation:layer}:undefined}},checks=[];
 const p={async wait(expression,label){assert.match(label,/selected canopy receipt and applied solid grid/);const evaluate=()=>!!new Function('document','window',`return (${expression});`)(document,window);checks.push(evaluate());selected='Canopy height';checks.push(evaluate());state='partial';disabled=true;checks.push(evaluate());disabled=false;layer=null;checks.push(evaluate());layer={failed:true};checks.push(evaluate());layer={failed:false};checks.push(evaluate());assert.deepEqual(checks,[false,false,false,false,false,true],'the old enabled Surface button, uncommitted receipt and unapplied/failed Canopy resources must not freeze acquisition counts');}};
 const waitReady=new Function('p',`return (${readySource});`)(p);await waitReady('canopy','Canopy height');
});

import assert from 'node:assert/strict';
import test from 'node:test';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const status={schema:'kfm-ee-download-control/v1',configured:false,project:null,destination:'/local/captures/earth-engine',sessionToken:'a'.repeat(43),active:null,jobs:[],authentication:'idle'};
const props={dataset:{id:'ee-cdl',recipeKind:'classes',recipe:'annual cropland classes'},year:2023,invalid:false};
const imports=state=>({'next/link':{default:'a'},'./use-local-downloads':{useLocalDownloads:()=>state},'./download-job':{DownloadJob:'job'},'./local-download-client':{downloadReasons:{},formatDownloadBytes:value=>`${value/1e9} GB`,parseDownloadStatus:value=>value},'./earth-engine/workspace.module.css':{default:new Proxy({},{get:(_,key)=>key})}});
const base=()=>({status,connection:'idle',announcement:'',actionNotice:'',cancelling:false,refresh(){},cancelJob(){}});
test('sign-in requires connection, sends only project through the shared session client, and opens official Google consent',async()=>{
 const calls=[],opened=[],state=base();state.connect=()=>{state.connection='connected';};state.post=async(path,body)=>{calls.push({path,body});return {response:{ok:true},body:{url:'https://accounts.google.com/o/oauth2/auth?state=test'}};};
 const h=await componentHarness('app/earth-engine-downloads.tsx',imports(state),{window:{open:(...args)=>opened.push(args)}});
 let tree=h.render(h.exports.default,props);h.commit();assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Sign in with Google Earth Engine').props.disabled,true);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Connect local downloads').props.onClick();
 findNode(tree,n=>n.props?.['aria-label']==='Earth Engine project ID').props.onChange({target:{value:'my-ee-project'}});tree=h.render(h.exports.default,props);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Sign in with Google Earth Engine').props.onClick();await settle();
 assert.equal(calls[0].path,'/auth/start');assert.deepEqual(JSON.parse(JSON.stringify(calls[0].body)),{project:'my-ee-project'});assert.equal(opened[0][0],'https://accounts.google.com/o/oauth2/auth?state=test');h.dispose();
});
test('download retry reuses selection id after uncertain transport and other years never display its job',async()=>{
 const calls=[],state={...base(),connection:'connected',status:{...status,configured:true,project:'my-ee-project',jobs:[{id:'a'.repeat(32),selection:{dataset:'ee-cdl',year:2022,maxBytes:8e9},state:'downloaded',bytes:100,completed:1,total:1,destination:'/data/2022',mapReady:false,createdAt:'2026-10-07'}]},post:async(path,body)=>{calls.push({path,body});throw new Error('connection lost');}};
 const h=await componentHarness('app/earth-engine-downloads.tsx',imports(state),{crypto:{randomUUID:()=> '12345678-1234-1234-1234-123456789abc'}});
 h.render(h.exports.default,props);h.commit();
 for(let i=0;i<2;i++){const tree=h.render(h.exports.default,props);assert.equal(findNode(tree,n=>n.type==='job'),undefined);findNode(tree,n=>n.type==='button'&&n.props.children==='Download 2023 to KFM').props.onClick();await settle();}
 assert.equal(calls.length,2);assert.deepEqual(calls[0],calls[1]);assert.equal(calls[0].path,'/downloads');assert.equal(calls[0].body.selection.year,2023);assert.equal(calls[0].body.selection.maxBytes,8e9);h.dispose();
});
test('download start remains busy until exact selection is confirmed then refreshes background jobs',async()=>{
 let finish,refreshes=0;const state={...base(),connection:'connected',status:{...status,configured:true,project:'my-ee-project'},refresh:()=>refreshes++,post:(_path,body)=>new Promise(resolve=>{finish=()=>resolve({response:{ok:true},body:{id:body.requestId,selection:body.selection,mapReady:false}});})};
 const h=await componentHarness('app/earth-engine-downloads.tsx',imports(state),{crypto:{randomUUID:()=> '12345678-1234-1234-1234-123456789abc'}});
 let tree=h.render(h.exports.default,props);h.commit();findNode(tree,n=>n.type==='button'&&n.props.children==='Download 2023 to KFM').props.onClick();tree=h.render(h.exports.default,props);
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Starting download…').props['aria-busy'],true);finish();await settle();tree=h.render(h.exports.default,props);
 assert.equal(refreshes,1);assert.match(JSON.stringify(tree),/Download started in the background/);assert.ok(findNode(tree,n=>n.type==='a'&&n.props.href==='/downloads'));h.dispose();
});
test('recipe navigation focuses the newly selected heading after render and respects reduced motion',async()=>{
 const datasets=[{id:'ee-cdl',title:'CDL',topic:'Crops',temporalMode:'annual',firstYear:2000,lastYear:2023},{id:'ee-water',title:'Water',topic:'Water',temporalMode:'annual',firstYear:2000,lastYear:2024}];
 const transitions=[];let reduced=true,renderedTitle='';
 const h=await componentHarness('app/earth-engine/workspace.tsx',{
  'next/link':{default:'a'},'../earth-engine-data':{EARTH_ENGINE_DATASETS:datasets,findEarthEngineDatasets:()=>datasets,buildEarthEngineRecipe:()=>'',earthEngineUrl:()=>'',earthEngineReviewPacket:()=>({})},
  '../earth-engine-context':{EARTH_ENGINE_CONTEXT_LAYERS:[],EARTH_ENGINE_SOURCE_YEARS:{}},'../earth-engine-context-client':{useEarthEngineContext:()=>({loading:false,manifests:[],error:null})},
  '../earth-engine-export':{buildEarthEngineExportRecipe:()=>''},'../source-history':{SourceHistory:'source-history'},'../earth-engine-downloads':{default:'downloads'},'./workspace.module.css':{default:new Proxy({},{get:(_,key)=>key})},
 },{URLSearchParams,window:{location:{search:''},matchMedia:query=>{assert.equal(query,'(prefers-reduced-motion: reduce)');return {matches:reduced};}},document:{getElementById:id=>{assert.equal(id,'recipe-workspace');return {scrollIntoView:options=>transitions.push({kind:'scroll',behavior:options.behavior})};}}});
 const render=()=>{const tree=h.render(h.exports.default);const heading=findNode(tree,n=>n.props?.id==='recipe-title');renderedTitle=heading.props.children;assert.equal(heading.props.tabIndex,-1);heading.props.ref.current={focus:options=>transitions.push({kind:'focus',title:renderedTitle,preventScroll:options.preventScroll})};h.commit();return tree;};
 let tree=render();assert.equal(transitions.length,0);
 const water=findNode(tree,n=>n.type==='article'&&findNode(n,c=>c.type==='button'&&c.props.children==='Water'));
 findNode(water,n=>n.type==='button'&&n.props.children==='Download / view years').props.onClick();assert.equal(transitions.length,0,'wait until the selected content is rendered');tree=render();
 assert.deepEqual(transitions,[{kind:'focus',title:'Water',preventScroll:true},{kind:'scroll',behavior:'instant'}]);
 reduced=false;const selected=findNode(tree,n=>n.type==='article'&&findNode(n,c=>c.type==='button'&&c.props.children==='Water'));findNode(selected,n=>n.type==='button'&&n.props.children==='Download / view years').props.onClick();render();
 assert.deepEqual(transitions.slice(2),[{kind:'focus',title:'Water',preventScroll:true},{kind:'scroll',behavior:'smooth'}]);h.dispose();
});

import assert from 'node:assert/strict';
import test from 'node:test';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const status={schema:'kfm-ee-download-control/v1',configured:false,project:null,destination:'/local/captures/earth-engine',sessionToken:'a'.repeat(43),active:null,jobs:[],authentication:'idle'};
const props={dataset:{id:'ee-cdl',recipeKind:'classes',recipe:'annual cropland classes'},year:2023,invalid:false};
const imports=state=>({'next/link':{default:'a'},'./use-local-downloads':{useLocalDownloads:()=>state},'./download-job':{DownloadJob:'job'},'./local-download-client':{downloadReasons:{},formatDownloadBytes:value=>`${value/1e9} GB`,parseDownloadStatus:value=>value},'./earth-engine/workspace.module.css':{default:new Proxy({},{get:(_,key)=>key})}});
const base=()=>({status,connection:'idle',announcement:'',actionNotice:'',cancelling:false,refresh(){},cancelJob(){},starting:false,setStarting(){},confirmStart(){}});
test('sign-in requires connection, does not require a project and sends an empty request through the shared session client, and opens official Google consent',async()=>{
 const calls=[],opened=[],state=base();state.connect=()=>{state.connection='connected';};state.post=async(path,body)=>{calls.push({path,body});return {response:{ok:true},body:{url:'https://accounts.google.com/o/oauth2/auth?state=test'}};};
 const h=await componentHarness('app/earth-engine-downloads.tsx',imports(state),{window:{open:(...args)=>opened.push(args)}});
 let tree=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state});h.commit();assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Sign in with Google').props.disabled,true);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Connect local downloads').props.onClick();
 tree=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state});
 findNode(tree,n=>n.type==='button'&&n.props.children==='Sign in with Google').props.onClick();await settle();
 assert.equal(calls[0].path,'/auth/start');assert.deepEqual(JSON.parse(JSON.stringify(calls[0].body)),{});assert.equal(opened[0][0],'https://accounts.google.com/o/oauth2/auth?state=test');h.dispose();
});
test('download retry reuses selection id after uncertain transport and other years never display its job',async()=>{
 const calls=[],state={...base(),connection:'connected',status:{...status,configured:true,project:'my-ee-project',jobs:[{id:'a'.repeat(32),selection:{dataset:'ee-cdl',year:2022,maxBytes:8e9},state:'downloaded',bytes:100,completed:1,total:1,destination:'/data/2022',mapReady:false,createdAt:'2026-10-07'}]},post:async(path,body)=>{calls.push({path,body});throw new Error('connection lost');}};
 const h=await componentHarness('app/earth-engine-downloads.tsx',imports(state),{crypto:{randomUUID:()=> '12345678-1234-1234-1234-123456789abc'}});
 h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state});h.commit();
 for(let i=0;i<2;i++){const tree=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state});assert.equal(findNode(tree,n=>n.type==='job'),undefined);findNode(tree,n=>n.type==='button'&&n.props.children==='Download 2023 to KFM').props.onClick();await settle();}
 assert.equal(calls.length,2);assert.deepEqual(calls[0],calls[1]);assert.equal(calls[0].path,'/downloads');assert.equal(calls[0].body.selection.year,2023);assert.equal(calls[0].body.selection.maxBytes,8e9);h.dispose();
});
test('download start remains busy until exact selection is confirmed then refreshes background jobs',async()=>{
 let finish,refreshes=0;const state={...base(),connection:'connected',status:{...status,configured:true,project:'my-ee-project'},refresh:()=>refreshes++,post:(_path,body)=>new Promise(resolve=>{finish=()=>resolve({response:{ok:true},body:{id:body.requestId,selection:body.selection,mapReady:false}});})};
 const h=await componentHarness('app/earth-engine-downloads.tsx',imports(state),{crypto:{randomUUID:()=> '12345678-1234-1234-1234-123456789abc'}});
 let tree=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state});h.commit();findNode(tree,n=>n.type==='button'&&n.props.children==='Download 2023 to KFM').props.onClick();tree=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state});
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Starting download…').props['aria-busy'],true);finish();await settle();tree=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state});
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

test('shared form uses the supplied controller, hides duplicate connection/jobs and rejects a conflicting start',async()=>{
 let hookCalls=0,posts=0,viewed=0;const state={...base(),connection:'connected',status:{...status,configured:true},post:async()=>{posts++;}};
 const deps=imports(state);deps['./use-local-downloads']={useLocalDownloads:()=>{hookCalls++;return state;}};
 const h=await componentHarness('app/earth-engine-downloads.tsx',deps);
 const shell=h.render(h.exports.default,{...props,downloads:state,compact:true});assert.equal(shell.type,h.exports.EarthEngineDownloadForm);assert.equal(hookCalls,0);
 let tree=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state,shared:true,compact:true,blockedByOtherDownload:true,onViewActivity:()=>viewed++});h.commit();
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Connect local downloads'),undefined);
 assert.equal(findNode(tree,n=>n.type==='job'),undefined);
 const start=findNode(tree,n=>n.type==='button'&&n.props.children==='Download 2023 to KFM');assert.equal(start.props.disabled,true);await start.props.onClick();assert.equal(posts,0);
 findNode(tree,n=>n.type==='button'&&n.props.children==='View activity').props.onClick();assert.equal(viewed,1);h.dispose();
});

test('shared start holds the global pending lock and selection changes suppress late confirmation',async()=>{
 let finish;const locks=[],state={...base(),connection:'connected',status:{...status,configured:true},setStarting:value=>locks.push(value),confirmStart:()=>locks.push('accepted'),post:(_path,body)=>new Promise(resolve=>{finish=()=>resolve({response:{ok:true},body:{id:body.requestId,selection:body.selection,mapReady:false}});})};
 const h=await componentHarness('app/earth-engine-downloads.tsx',imports(state),{crypto:{randomUUID:()=> '12345678-1234-1234-1234-123456789abc'}});
 let tree=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state,shared:true});h.commit();findNode(tree,n=>n.type==='button'&&n.props.children==='Download 2023 to KFM').props.onClick();assert.deepEqual(locks,[true]);
 h.render(h.exports.EarthEngineDownloadForm,{...props,year:2024,downloads:state,shared:true});h.commit();finish();await settle();tree=h.render(h.exports.EarthEngineDownloadForm,{...props,year:2024,downloads:state,shared:true});
 assert.deepEqual(locks,[true,'accepted']);assert.doesNotMatch(JSON.stringify(tree),/Download started in the background/);h.dispose();
});

test('standalone Earth Engine route still creates its own connection controller',async()=>{
 let hooks=0;const state=base(),deps=imports(state);deps['./use-local-downloads']={useLocalDownloads:()=>{hooks++;return state;}};
 const h=await componentHarness('app/earth-engine-downloads.tsx',deps);
 const shell=h.render(h.exports.default,props);assert.equal(hooks,0);
 const form=h.render(shell.type,shell.props);assert.equal(hooks,1);assert.equal(form.props.downloads,state);assert.equal(form.props.shared,undefined);
 const tree=h.render(form.type,form.props);h.commit();assert.ok(findNode(tree,n=>n.type==='button'&&n.props.children==='Connect local downloads'));h.dispose();
});

test('signed-in account still requires project verification and selected stored period is visible',async()=>{
 const calls=[],state={...base(),connection:'connected',status:{...status,signedIn:true,accountEmail:'owner@example.test',authentication:'project-required',projects:['test-project'],projectDiscovery:'complete'},library:{generatedAt:'2026-10-09T12:00:00Z',entries:[{lane:'raw',dataset:'ee-cdl',period:'2023',files:4,bytes:1e9},{lane:'raw',dataset:'ee-cdl',period:'2022',files:9,bytes:2e9}]},post:async(path,body)=>{calls.push({path,body});return {response:{ok:true},body:{checking:true}};}};
 const h=await componentHarness('app/earth-engine-downloads.tsx',imports(state));
 const render=()=>{const t=h.render(h.exports.EarthEngineDownloadForm,{...props,downloads:state});h.commit();return t;};
 let tree=render();assert.match(JSON.stringify(tree),/Signed in · owner@example.test/);assert.match(JSON.stringify(tree),/4 stored files/);
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Download 2023 to KFM').props.disabled,true);
 findNode(tree,n=>n.props?.['aria-label']==='Choose Earth Engine project').props.onChange({target:{value:'test-project'}});tree=render();await findNode(tree,n=>n.type==='button'&&n.props.children==='Check download access').props.onClick();await settle();assert.equal(calls[0].path,'/auth/check');assert.equal(calls[0].body.project,'test-project');
 state.status={...state.status,configured:true,project:'test-project',authentication:'connected'};tree=render();assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Download 2023 to KFM').props.disabled,false);h.dispose();
});

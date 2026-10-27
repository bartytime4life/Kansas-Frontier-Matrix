import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import test from 'node:test';
import ts from 'typescript';
import {componentHarness,findNode} from './component-harness.mjs';

const modelSource=await readFile(new URL('../app/workspace-model.ts',import.meta.url),'utf8');
const model={};
vm.runInNewContext(ts.transpileModule(modelSource,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText,{
 exports:model,require:()=>({persistableSubsurface:()=>null,persistableResearch:()=>null}),
});
const snapshot={id:'captured-map',createdAt:'2026-10-27T15:00:00Z',area:{kind:'viewport',label:'Kansas test view'},camera:{center:[-98,38],zoom:7,bearing:10,pitch:0},representation:'2D',projection:'mercator',basemap:'standard',committedTime:{start:2026,end:2026,label:'2026',mode:'instant'},visibleLayers:[],selection:null,evidenceRefs:[],inspectableFeatureIds:[],inspectableRecordCount:0,sourceBackedCount:0,boundedCount:0,policy:{outcome:'ABSTAIN',reason:'No released evidence',publicEffect:'NONE'}};

test('new stories retain the exact captured map and never inject demonstration evidence',()=>{
 for(const camera of [snapshot.camera,{center:'WITHHELD_BROWSER_LOCATION',zoom:'WITHHELD',bearing:'WITHHELD',pitch:'WITHHELD'}]){
  const captured={...snapshot,camera},story=model.createMapStory(captured);
  assert.equal(story.baseSnapshot,captured);assert.equal(story.scenes.length,1);
  assert.equal(story.scenes[0].snapshot,captured);assert.equal(story.scenes[0].motion,'none');
  assert.deepEqual(Array.from(story.scenes[0].evidenceRefs),[]);
  assert.ok(!JSON.stringify(story).includes('synthetic:'));assert.ok(!JSON.stringify(story).includes('deny-demo'));
 }
});

async function harness(mode='reports',saved=new Map()){
 const timers=new Map(),events=new Map(),writes=[];let next=0,fail=false;
 const save=(key,value)=>{if(fail)throw new Error('quota');saved.set(key,JSON.parse(value));writes.push({key,value:JSON.parse(value)});};
 const h=await componentHarness(new URL('../app/report-story-workspaces.tsx',import.meta.url),{
  './workspace-model':model,'./snapshot-map':{default:()=>null},'./assistant-panel':{default:()=>null},
  './assistant-context':{snapshotAssistantFocus:()=>({})},
  './workspace-storage':{REPORT_STORAGE_KEY:'report',STORY_STORAGE_KEY:'story',readDraft:key=>saved.get(key)??null},
  './fire-report-analysis':{FIRE_REPORT_SOURCES:[]},'./subsurface-model':{},'./research-context':{},'./category-basemap-keys':{isCategoryBasemapKey:()=>false},
 },{
  window:{localStorage:{setItem:save},setTimeout(fn){const id=++next;timers.set(id,fn);return id;},clearTimeout(id){timers.delete(id);},addEventListener(type,fn){events.set(type,fn);},removeEventListener(type){events.delete(type);},matchMedia:()=>({matches:true,addEventListener(){},removeEventListener(){}})},
  document:{hidden:false,addEventListener(){},removeEventListener(){}},
 });
 const props={mode,snapshot,evidenceRecords:[],onModeChange(){},onReturnToMap(){},onInspectEvidence(){},onApplyScene(){},getCurrentSnapshot:()=>snapshot};
 const render=()=>{const tree=h.render(h.exports.default,props);h.commit();return tree;};
 const edit=value=>{findNode(render(),n=>n.type==='input'&&n.props.maxLength===120).props.onChange({target:{value}});render();};
 const flush=()=>{for(const [id,fn] of [...timers]){timers.delete(id);fn();}};
 return {h,props,render,edit,flush,writes,saved,events,timers,fail(value){fail=value;}};
}

test('typing coalesces storage writes and saves the latest report text',async()=>{
 const p=await harness();p.render();p.edit('First');p.edit('Second');p.edit('Final report');
 assert.equal(p.writes.length,0);assert.equal(p.timers.size,1);p.flush();
 assert.equal(p.writes.length,1);assert.equal(p.saved.get('report').title,'Final report');p.h.dispose();
});
test('leaving before the debounce flushes the latest draft once',async()=>{
 const p=await harness();p.render();p.edit('Last edit before leaving');p.h.dispose();p.flush();
 assert.equal(p.writes.length,1);assert.equal(p.saved.get('report').title,'Last edit before leaving');
});
test('pagehide flushes without waiting for a timer, and never saves the inactive draft',async()=>{
 const saved=new Map([['story',{...model.createMapStory(snapshot),title:'Existing story'}]]),p=await harness('reports',saved);
 p.render();p.edit('Report on pagehide');p.events.get('pagehide')();p.flush();
 assert.equal(p.saved.get('report').title,'Report on pagehide');assert.equal(p.saved.get('story').title,'Existing story');assert.equal(p.writes.length,1);p.h.dispose();
});
test('quota failure keeps the draft exportable and Retry saving persists it after recovery',async()=>{
 const p=await harness();p.fail(true);p.render();p.edit('Retained after quota failure');p.flush();
 const retry=findNode(p.render(),n=>n.type==='button'&&n.props.children==='Retry saving');assert.ok(retry);
 assert.equal(p.writes.length,0);p.fail(false);retry.props.onClick();
 assert.equal(p.saved.get('report').title,'Retained after quota failure');p.h.dispose();
});

const page=ts.createSourceFile('page.tsx',await readFile(new URL('../app/page.tsx',import.meta.url),'utf8'),ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
let handler;
function visit(node){if(ts.isVariableDeclaration(node)&&node.name.getText(page)==='openPrimaryWorkspace')handler=node.initializer.arguments[0].getText(page);ts.forEachChild(node,visit);}visit(page);
const handlerJs=ts.transpileModule(`return ${handler};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
test('Reports and Stories each restore their own saved snapshot; fresh composition captures the current map',()=>{
 const restored=[],announcements=[],paused=[],report={id:'report-snapshot'},story={id:'story-snapshot'},fresh={id:'fresh-snapshot'};
 const scope={primaryWorkspace:'map',workspaceSnapshot:report,readDraftSnapshot:mode=>mode==='reports'?report:story,captureMapSnapshot:()=>fresh,setWorkspaceSnapshot:x=>restored.push(x),announce:x=>announcements.push(x),persistableResearch:()=>null,persistableSubsurface:()=>null,locationCameraRedacted:false,researchLocationRedacted:false,subsurfacePrivate:false,locationDerivedViewRef:{current:false}};
 for(const key of ['setFireReportContext','setResearchReportContext','setSubsurfaceReportContext','setPrimaryWorkspace','setMapContextOpen','setHelpOpen','setQwenOpen'])scope[key]=()=>{};
 for(const key of ['setPlaying','setStreamflowPlaying','setNoaaRadarPlaying','setLightningPlaying','setDaylightPlayback'])scope[key]=value=>paused.push(value);
 const open=new Function(...Object.keys(scope),handlerJs)(...Object.values(scope));open('reports');open('stories');open('reports',true);
 assert.deepEqual(restored,[report,story,fresh]);assert.ok(announcements[0].includes('resumed'));assert.ok(announcements[1].includes('saved map snapshot'));assert.ok(announcements[2].includes('current governed map'));
 assert.equal(paused.length,15);assert.ok(paused.every(value=>value===false));
});

test('reopening an active unsaved workspace never reads stale storage or remounts it; explicit fresh composition still works',()=>{
 for(const mode of ['reports','stories']){
  const changes=[],active={id:'unsaved-active-'+mode},fresh={id:'explicit-fresh-'+mode};let captures=0;
  const scope={primaryWorkspace:mode,workspaceSnapshot:active,readDraftSnapshot(){throw Error('Must not replace the active editor from storage');},captureMapSnapshot(){captures++;return fresh;},setWorkspaceSnapshot:x=>changes.push(x),announce(){},persistableResearch:()=>null,persistableSubsurface:()=>null,locationCameraRedacted:false,researchLocationRedacted:false,subsurfacePrivate:false,locationDerivedViewRef:{current:false}};
  for(const key of ['setFireReportContext','setResearchReportContext','setSubsurfaceReportContext','setPrimaryWorkspace','setMapContextOpen','setHelpOpen','setQwenOpen','setPlaying','setStreamflowPlaying','setNoaaRadarPlaying','setLightningPlaying','setDaylightPlayback'])scope[key]=()=>{};
  const open=new Function(...Object.keys(scope),handlerJs)(...Object.values(scope));
  open(mode);assert.deepEqual(changes,[]);assert.equal(captures,0);
  open(mode,true);assert.deepEqual(changes,[fresh]);assert.equal(captures,1);
 }
});

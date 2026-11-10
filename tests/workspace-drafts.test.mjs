import {scientific} from './scientific-report-harness.mjs';
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
const storage={};
vm.runInNewContext(ts.transpileModule(await readFile(new URL('../app/workspace-storage.ts',import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText,{
 exports:storage,require:()=>({LAYER_REGISTRY:[],BASEMAPS:{standard:{}},BUILD_UTC_YEAR:2026}),
});
const {REPORT_STORAGE_KEY:reportKey,STORY_STORAGE_KEY:storyKey}=storage;

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
 const timers=new Map(),events=new Map(),documentEvents=new Map(),writes=[],inside={};let next=0,fail=false;
 const save=(key,value)=>{if(fail)throw new Error('quota');saved.set(key,JSON.parse(value));writes.push({key,value:JSON.parse(value)});};
 const h=await componentHarness(new URL('../app/report-story-workspaces.tsx',import.meta.url),{
  './scientific-report':scientific,'./workspace-model':model,'./snapshot-map':{default:()=>null},'./assistant-panel':{default:()=>null},
  './assistant-context':{snapshotAssistantFocus:()=>({})},
  './workspace-storage':{...storage,readDraft:key=>saved.get(key)??null},
  './draft-save-status.module.css':{default:{status:'save-status',header:'save-header'}},
  './fire-report-analysis':{FIRE_REPORT_SOURCES:[]},'./subsurface-model':{},'./research-context':{},'./category-basemap-keys':{isCategoryBasemapKey:()=>false},
 },{
  window:{localStorage:{setItem:save},setTimeout(fn){const id=++next;timers.set(id,fn);return id;},clearTimeout(id){timers.delete(id);},addEventListener(type,fn){events.set(type,fn);},removeEventListener(type){events.delete(type);},matchMedia:()=>({matches:true,addEventListener(){},removeEventListener(){}})},
  document:{hidden:false,addEventListener(type,fn){documentEvents.set(type,fn);},removeEventListener(type){documentEvents.delete(type);}},
 });
 const props={mode,snapshot,evidenceRecords:[],onModeChange(){},onReturnToMap(){},onInspectEvidence(){},onApplyScene(){},getCurrentSnapshot:()=>snapshot};
 const render=(layoutOnly=false)=>{const tree=h.render(h.exports.default,props);tree.props.ref.current={contains:node=>node===inside};if(layoutOnly)h.commitLayout();else h.commit();return tree;};
 const edit=value=>{const tree=render();const toggle=findNode(tree,n=>n.type==='button'&&n.props.children==='Edit report');toggle?.props.onClick();findNode(render(),n=>n.type==='input'&&n.props.maxLength===120).props.onChange({target:{value}});render();};
 const flush=()=>{for(const [id,fn] of [...timers]){timers.delete(id);fn();}};
 const keydown=(patch={})=>{let prevented=false;documentEvents.get('keydown')({key:'s',ctrlKey:true,target:inside,preventDefault(){prevented=true;},...patch});return prevented;};
 return {h,props,render,edit,flush,writes,saved,events,timers,keydown,fail(value){fail=value;}};
}

test('typing coalesces storage writes and saves the latest report text',async()=>{
 const p=await harness();p.render();p.edit('First');p.edit('Second');p.edit('Final report');
 assert.equal(p.writes.length,0);assert.equal(p.timers.size,1);p.flush();
 assert.equal(p.writes.length,1);assert.equal(p.saved.get(reportKey).title,'Final report');p.h.dispose();
});
test('leaving before the debounce flushes the latest draft once',async()=>{
 const p=await harness();p.render();p.edit('Last edit before leaving');p.h.dispose();p.flush();
 assert.equal(p.writes.length,1);assert.equal(p.saved.get(reportKey).title,'Last edit before leaving');
});
test('pagehide flushes without waiting for a timer, and never saves the inactive draft',async()=>{
 const saved=new Map([[storyKey,{...model.createMapStory(snapshot),title:'Existing story'}]]),p=await harness('reports',saved);
 p.render();p.edit('Report on pagehide');p.events.get('pagehide')();p.flush();
 assert.equal(p.saved.get(reportKey).title,'Report on pagehide');assert.equal(p.saved.get(storyKey).title,'Existing story');assert.equal(p.writes.length,1);p.h.dispose();
});
test('quota failure keeps the draft exportable and Retry saving persists it after recovery',async()=>{
 const p=await harness();p.fail(true);p.render();p.edit('Retained after quota failure');p.flush();
 const retry=findNode(p.render(),n=>n.type==='button'&&n.props.children==='Retry saving');assert.ok(retry);
 assert.equal(p.writes.length,0);p.fail(false);retry.props.onClick();
 assert.equal(p.saved.get(reportKey).title,'Retained after quota failure');p.h.dispose();
});

const page=ts.createSourceFile('page.tsx',await readFile(new URL('../app/page.tsx',import.meta.url),'utf8'),ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
let handler;
function visit(node){if(ts.isVariableDeclaration(node)&&node.name.getText(page)==='openPrimaryWorkspace')handler=node.initializer.arguments[0].getText(page);ts.forEachChild(node,visit);}visit(page);
const handlerJs=ts.transpileModule(`return ${handler};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
test('Reports and Stories each restore their own saved snapshot; fresh composition captures the current map',()=>{
 const restored=[],announcements=[],paused=[],report={id:'report-snapshot'},story={id:'story-snapshot'},fresh={id:'fresh-snapshot'};
 const scope={primaryWorkspace:'map',workspaceSnapshot:report,readDraftSnapshot:mode=>mode==='reports'?report:story,captureMapSnapshot:()=>fresh,setWorkspaceSnapshot:x=>restored.push(x),announce:x=>announcements.push(x),persistableResearch:()=>null,persistableSubsurface:()=>null,locationCameraRedacted:false,researchLocationRedacted:false,subsurfacePrivate:false,locationDerivedViewRef:{current:false}};
 for(const key of ['setFireReportContext','setResearchReportContext','setSubsurfaceReportContext','setPrimaryWorkspace','setMapContextOpen','setHelpOpen','setQwenOpen','setChatLayoutSuspended'])scope[key]=()=>{};
 for(const key of ['setPlaying','setStreamflowPlaying','setNoaaRadarPlaying','setLightningPlaying','setDaylightPlayback'])scope[key]=value=>paused.push(value);
 const open=new Function(...Object.keys(scope),handlerJs)(...Object.values(scope));open('reports');open('stories');open('reports',true);
 assert.deepEqual(restored,[report,story,fresh]);assert.ok(announcements[0].includes('resumed'));assert.ok(announcements[1].includes('saved map snapshot'));assert.ok(announcements[2].includes('current governed map'));
 assert.equal(paused.length,15);assert.ok(paused.every(value=>value===false));
});

test('reopening an active unsaved workspace never reads stale storage or remounts it; explicit fresh composition still works',()=>{
 for(const mode of ['reports','stories']){
  const changes=[],active={id:'unsaved-active-'+mode},fresh={id:'explicit-fresh-'+mode};let captures=0;
  const scope={primaryWorkspace:mode,workspaceSnapshot:active,readDraftSnapshot(){throw Error('Must not replace the active editor from storage');},captureMapSnapshot(){captures++;return fresh;},setWorkspaceSnapshot:x=>changes.push(x),announce(){},persistableResearch:()=>null,persistableSubsurface:()=>null,locationCameraRedacted:false,researchLocationRedacted:false,subsurfacePrivate:false,locationDerivedViewRef:{current:false}};
  for(const key of ['setFireReportContext','setResearchReportContext','setSubsurfaceReportContext','setPrimaryWorkspace','setMapContextOpen','setHelpOpen','setQwenOpen','setChatLayoutSuspended','setPlaying','setStreamflowPlaying','setNoaaRadarPlaying','setLightningPlaying','setDaylightPlayback'])scope[key]=()=>{};
  const open=new Function(...Object.keys(scope),handlerJs)(...Object.values(scope));
  open(mode);assert.deepEqual(changes,[]);assert.equal(captures,0);
  open(mode,true);assert.deepEqual(changes,[fresh]);assert.equal(captures,1);
 }
});

test('dashboard and editor share the latest draft across layout changes',async()=>{
 const p=await harness();let tree=p.render();
 assert.ok(findNode(tree,n=>n.props?.['aria-label']==='Scientific report preview'));
 p.edit('Edited visual report');
 findNode(p.render(),n=>n.type==='button'&&n.props.children==='Dashboard').props.onClick();
 tree=p.render();assert.match(findNode(tree,n=>n.props?.['aria-label']==='Scientific report preview').props.dangerouslySetInnerHTML.__html,/Edited visual report/);
 findNode(tree,n=>n.type==='select'&&n.props.value==='overview').props.onChange({target:{value:'sources'}});
 tree=p.render();assert.match(findNode(tree,n=>n.props?.['aria-label']==='Scientific report preview').props.dangerouslySetInnerHTML.__html,/Edited visual report/);
 p.flush();assert.equal(p.saved.get(reportKey).title,'Edited visual report');p.h.dispose();
});

test('Save now and the scoped keyboard shortcut persist the latest report and story before debounce',async()=>{
 for(const [mode,key] of [['reports',reportKey],['stories',storyKey]]){
  const p=await harness(mode);p.render();p.edit('Manual save');
  findNode(p.render(),n=>n.type==='button'&&n.props.children==='Save now').props.onClick();
  assert.equal(p.saved.get(key).title,'Manual save');p.flush();assert.equal(p.writes.length,1);
  assert.equal(findNode(p.render(),n=>n.type==='button'&&n.props.children==='Save now').props.disabled,true);
  p.edit('Keyboard save');assert.equal(p.keydown({ctrlKey:false,metaKey:true}),true);
  assert.equal(p.saved.get(key).title,'Keyboard save');p.flush();assert.equal(p.writes.length,2);
  p.edit('Control save');assert.equal(p.keydown(),true);assert.equal(p.saved.get(key).title,'Control save');p.h.dispose();
 }
});

test('save shortcut leaves other scopes, composition, modifiers and the assistant untouched',async()=>{
 const p=await harness();p.render();p.edit('Pending keyboard edit');
 for(const patch of [{target:{}},{isComposing:true},{defaultPrevented:true},{shiftKey:true},{altKey:true},{ctrlKey:false},{key:'p'}])assert.equal(p.keydown(patch),false);
 assert.equal(p.writes.length,0);
 findNode(p.render(),n=>n.type==='button'&&n.props['aria-haspopup']==='dialog').props.onClick();p.render();
 assert.equal(p.keydown(),false);assert.equal(p.writes.length,0);p.h.dispose();
});

test('leaving after layout commit but before passive effects still saves the newest edit',async()=>{
 const p=await harness('stories');p.render();
 findNode(p.render(),n=>n.type==='input'&&n.props.maxLength===120).props.onChange({target:{value:'Immediate departure'}});
 p.render(true);p.h.dispose();p.flush();
 assert.equal(p.saved.get(storyKey).title,'Immediate departure');assert.equal(p.writes.length,1);
});

test('guiding question clamps pasted text to the reopen limit even without native maxlength enforcement',async()=>{
 const p=await harness('stories');const field=findNode(p.render(),n=>n.type==='textarea'&&n.props.maxLength===storage.MAX_DRAFT_TEXT_LENGTH);
 assert.ok(field);field.props.onChange({target:{value:'q'.repeat(storage.MAX_DRAFT_TEXT_LENGTH+1000)}});p.render();p.flush();
 const saved=p.saved.get(storyKey);assert.equal(saved.researchQuestion.length,storage.MAX_DRAFT_TEXT_LENGTH);assert.equal(storage.validStoryDraft(saved),true);p.h.dispose();
});

test('invalid and oversized drafts retain the previous saved copy and show recovery guidance',async()=>{
 for(const oversized of [false,true]){
  const previous=model.createMapStory(snapshot),bad={...previous,...(oversized?{extra:'x'.repeat(storage.MAX_DRAFT_CHARACTERS)}:{researchQuestion:'x'.repeat(storage.MAX_DRAFT_TEXT_LENGTH+1)})};
  const saved=new Map([[storyKey,bad]]),p=await harness('stories',saved);p.render();saved.set(storyKey,previous);p.flush();
  assert.equal(p.writes.length,0);assert.equal(saved.get(storyKey),previous);
  const status=findNode(p.render(),n=>n.type==='small'&&typeof n.props.children==='string'&&n.props.children.includes('export to keep your work'));
  assert.match(status.props.children,oversized?/too large/:/cannot be reopened/);
  assert.ok(findNode(p.render(),n=>n.type==='button'&&n.props.children==='Retry saving'));
  p.h.dispose();assert.equal(saved.get(storyKey),previous);
 }
});

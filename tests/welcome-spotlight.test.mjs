import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile, readdir } from 'node:fs/promises';
import { gunzipSync } from 'node:zlib';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
const compile=async name=>ts.transpileModule(await readFile(name,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const materials={};new Function('exports',await compile('app/subsurface-materials.ts'))(materials);
const data=JSON.parse(await readFile('app/living-welcome/subsurface-spotlight.json','utf8'));
const text=node=>typeof node==='string'||typeof node==='number'?String(node):[node?.props?.children].flat(Infinity).filter(v=>v!=null).map(text).join(' ');
const inKansas=([x,y])=>x>=-102.1&&x<=-94.5&&y>=36.9&&y<=40.1;
const https=url=>new URL(url).protocol==='https:';

test('spotlight records are the pinned tile records, unchanged, with a turn for every kind',async()=>{
 const wanted=new Set(data.records.filter(r=>r.kind!=='mine').map(r=>r.id)),tiles=new Map();
 for(const name of (await readdir('public/data/subsurface')).filter(n=>n.startsWith('tile-')))for(const row of JSON.parse(gunzipSync(await readFile(`public/data/subsurface/${name}`))))if(wanted.has(row.id))tiles.set(row.id,row);
 assert.equal(tiles.size,wanted.size);
 const kinds=data.records.map(r=>r.kind);for(const kind of ['well','core','mine'])assert.ok(kinds.filter(k=>k===kind).length>=5,`${kind} records`);
 assert.equal(new Set(data.records.map(r=>r.id)).size,data.records.length);
 for(const record of data.records){
  assert.ok(inKansas(record.coordinates)&&https(record.sourceUrl),record.id);assert.ok(record.label);
  const tile=tiles.get(record.id);
  if(record.kind==='well'){
   assert.deepEqual(record.coordinates,tile.coordinates);assert.equal(record.recordDate,tile.sourceTime);assert.equal(record.totalDepth,tile.totalDepth);assert.equal(record.sourceUrl,tile.sourceUrl);
   assert.deepEqual(record.intervals,tile.intervals.map(({top,bottom,description})=>({top,bottom,description})));
   assert.equal(record.intervals[0].top,0);assert.equal(record.intervals.at(-1).bottom,record.totalDepth);record.intervals.forEach((row,i)=>i&&assert.equal(row.top,record.intervals[i-1].bottom));
  }else if(record.kind==='core'){
   assert.deepEqual(record.coordinates,tile.coordinates);assert.equal(record.top,tile.intervals[0].top);assert.equal(record.bottom,tile.intervals[0].bottom);assert.equal(record.photosUrl,tile.photosUrl);assert.equal(record.depthReference,'drilled-depth');
   assert.ok(Number.isInteger(record.boxes)&&record.boxes>0&&record.boxes<=120);assert.ok(record.operator);
  }else{
   assert.match(record.kid,/^\d+$/);assert.ok(record.category&&record.status&&record.county);assert.ok(!/reserve|production/i.test(record.note??''),'reserve and production notes stay off the welcome');
  }
 }
 assert.deepEqual(data.sources.map(s=>s.id),['kgs-wwc5','kgs-core','kgs-core-boxes','kgs-mines']);
 for(const source of data.sources){assert.match(source.sha256,/^[a-f0-9]{64}$/);assert.ok(https(source.url)&&source.limitation&&Number.isFinite(Date.parse(source.retrievedAt)));}
});

const json=Object.freeze(data);
function stage(){
 const timers=new Map(),intervals=new Map(),pins=[],listeners=new Map();let next=0,visible=()=>true;
 const document={hidden:false,addEventListener:(id,fn)=>listeners.set(id,fn),removeEventListener:id=>listeners.delete(id),createElement:()=>({className:'',dataset:{}})};
 const engine={pin(element,coordinates){const pin={element,coordinates,removed:false};pins.push(pin);return()=>{pin.removed=true;};},project:(coordinates,topic)=>topic==='geology'&&visible(coordinates)?{x:500,y:500}:null};
 const host={getBoundingClientRect:()=>({left:0,top:0,width:1000,height:800}),ownerDocument:{querySelectorAll:()=>[]}};
 const globals={document,getComputedStyle:()=>({visibility:'visible',opacity:'1'}),setTimeout:(fn,ms)=>{const id=++next;timers.set(id,{fn,ms});return id;},clearTimeout:id=>timers.delete(id),setInterval:(fn,ms)=>{const id=++next;intervals.set(id,{fn,ms});return id;},clearInterval:id=>intervals.delete(id),Math:Object.assign(Object.create(Math),{random:()=>0})};
 return {timers,intervals,pins,listeners,document,engine,host,globals,setVisible:fn=>visible=fn};
}
async function spotlight(props={}){
 const s=stage();
 const harness=await componentHarness('app/living-welcome/SubsurfaceSpotlight.jsx',{'react-dom':{createPortal:(children,element)=>({type:'portal',props:{children,element}})},'./subsurface-spotlight.json':{__esModule:true,default:json},'../subsurface-materials':materials},s.globals);
 const state={engine:s.engine,host:s.host,paused:false,reduced:false,expanded:false,...props};
 // Inner components render in the same pass, so their pin effects run like React's.
 const expand=node=>Array.isArray(node)?node.map(expand):!node||typeof node!=='object'?node:typeof node.type==='function'?expand(node.type(node.props)):{...node,props:{...node.props,children:expand(node.props?.children)}};
 const draw=()=>harness.render(props=>expand(harness.exports.SubsurfaceSpotlight(props)),state);
 const render=()=>{draw();harness.commit();draw();harness.commit();return draw();};
 const fire=ms=>{const [id,timer]=[...s.timers].find(([,t])=>t.ms===ms);s.timers.delete(id);timer.fn();};
 return {...s,harness,state,render,fire};
}
const card=tree=>findNode(tree,node=>node.props?.['data-phase']);

test('a well rises first, then a core, then a mine, each pinned at its own record location',async()=>{
 const h=await spotlight({expanded:true});try{
  let tree=h.render();let shown=card(tree);
  assert.equal(shown.props['data-kind'],'well');assert.equal(shown.props['data-phase'],'in');
  const well=data.records.find(r=>r.kind==='well');assert.match(text(tree),/Water well · KGS WWC5/);assert.ok(text(tree).includes(well.label));
  assert.deepEqual(h.pins.at(-1).coordinates,well.coordinates);assert.equal(h.pins.at(-1).element.dataset.kind,'well');
  h.fire(9000);tree=h.render();assert.equal(card(tree).props['data-phase'],'out');
  h.fire(520);tree=h.render();shown=card(tree);assert.equal(shown.props['data-kind'],'core');assert.match(text(tree),/boxes in the KGS Core Library/);
  assert.equal(h.pins.find(p=>p.element.dataset.kind==='well'&&!p.element.className.includes('trail')).removed,true,'the previous card leaves the map');
  assert.ok(h.pins.some(p=>p.element.className.includes('welcome-spot--trail')&&!p.removed),'its spot stays as a faint marker');
  h.fire(9000);h.render();h.fire(520);tree=h.render();assert.equal(card(tree).props['data-kind'],'mine');
  const mine=data.records.find(r=>r.kind==='mine');assert.ok(text(tree).includes(mine.label),'the mine is labelled');assert.match(text(tree),/Not a current operating status/);
 }finally{h.harness.dispose();}
 assert.ok(h.pins.every(p=>p.removed));assert.equal(h.listeners.size,0);
});
test('behind the category cards each record is a labelled chip with one recorded fact',async()=>{
 const h=await spotlight();try{
  let tree=h.render();const well=data.records.find(r=>r.kind==='well');
  assert.ok(findNode(tree,node=>node.props?.className?.includes('welcome-spot-chip')));assert.ok(text(tree).includes(well.label));assert.match(text(tree),new RegExp(`${well.totalDepth} ft driller's log · ${well.recordDate.slice(0,4)}`));
  h.fire(9000);h.render();h.fire(520);tree=h.render();assert.match(text(tree),/ft cored · \d+ boxes/);
  h.fire(9000);h.render();h.fire(520);tree=h.render();const mine=data.records.find(r=>r.kind==='mine');assert.ok(text(tree).includes(mine.label),'the mine is labelled');assert.match(text(tree),new RegExp(`Mine · ${mine.county} County`));
 }finally{h.harness.dispose();}
});
test('pause, reduced motion and hidden documents hold the current record; Next works in the opened preview',async()=>{
 for(const start of [{paused:true},{reduced:true}]){
  const h=await spotlight({...start,expanded:true});try{
   let tree=h.render();assert.equal(card(tree).props['data-still'],true);assert.equal([...h.timers.values()].some(t=>t.ms===9000),false,'no automatic advance');
   const next=findNode(tree,node=>node.type==='button');assert.ok(findNode(tree,node=>node.type==='a'&&node.props.href===data.records[0].sourceUrl));
   next.props.onClick();tree=h.render();assert.equal(card(tree).props['data-phase'],'out');h.fire(520);tree=h.render();assert.equal(card(tree).props['data-kind'],'core');
  }finally{h.harness.dispose();}
 }
 const h=await spotlight();try{h.render();h.document.hidden=true;h.listeners.get('visibilitychange')();const tree=h.render();assert.equal(card(tree).props['data-still'],true);assert.equal([...h.timers.values()].some(t=>t.ms===9000),false);}finally{h.harness.dispose();}
 const compact=await spotlight();try{assert.equal(findNode(compact.render(),node=>node.type==='button'),undefined,'compact cards stay non-interactive');}finally{compact.harness.dispose();}
});
test('records that cannot be placed clear of the welcome panels wait; another kind may take the turn',async()=>{
 const h=await spotlight();try{
  h.setVisible(()=>false);assert.equal(h.render(),null);assert.ok([...h.timers.values()].some(t=>t.ms===1600),'retries later');
  h.setVisible(([x])=>x>-97);h.fire(1600);const tree=h.render();const shown=card(tree);assert.ok(shown);
  const pinned=h.pins.at(-1);assert.ok(pinned.coordinates[0]>-97);
  assert.equal(h.intervals.size,1);[...h.intervals.values()][0].fn();assert.equal(card(h.render()).props['data-phase'],'in','a card still clear of the panels stays');
  h.setVisible(()=>false);[...h.intervals.values()][0].fn();assert.equal(card(h.render()).props['data-phase'],'out','a covered card gives way early');assert.equal(h.intervals.size,0);
 }finally{h.harness.dispose();}
});

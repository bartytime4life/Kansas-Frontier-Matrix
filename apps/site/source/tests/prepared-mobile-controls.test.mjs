import assert from 'node:assert/strict';
import test from 'node:test';
import vm from 'node:vm';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const text=n=>typeof n==='string'||typeof n==='number'?String(n):[n?.props?.children].flat(Infinity).filter(Boolean).map(text).join(' ');
const button=(tree,name)=>findNode(tree,n=>n.type==='button'&&text(n)===name);
const presentation={};vm.runInNewContext(ts.transpileModule(await readFile('app/local-atlas-presentation.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS}}).outputText,{exports:presentation});
const data={type:'FeatureCollection',features:[{type:'Feature',geometry:{type:'Point',coordinates:[-100,38]},properties:{name:'Fixture',value:7}}]};
const member='geojson/temperature_f-01.geojson',profile={id:'normals',title:'Fixture collection',period:'Frozen fixture',fileCount:2,totalBytes:2,mapFiles:[member],tableFiles:[],members:[{file:member,bytes:1,sha256:'a'.repeat(64)}],sources:['https://example.test/'],limitation:'Synthetic only'};
const selection={files:new Map([[member,new Uint8Array([1]).buffer]])};
async function setup(pending=false){
 const frames=[],fits=[],events=[],overlays=[];let summary,resolve,signal,collapsed=false;
 const host={isConnected:true,closest:()=>({getBoundingClientRect:()=>({top:collapsed?565:94})}),querySelector:()=>({scrollIntoView:()=>events.push('scroll'),focus:()=>events.push('focus')})};
 const map={getCanvas:()=>({getBoundingClientRect:()=>({top:0,bottom:812})}),fitBounds:(b,o)=>fits.push({b,o})};
 const h=await componentHarness('app/prepared-collection-control.tsx',{
 './prepared-collection-pins':{PREPARED_COLLECTIONS:[profile]},'./prepared-collections':{inspectPreparedCollection:async(_id,_files,s)=>{signal=s;return pending?await new Promise(r=>resolve=r):selection},preparedText:()=>JSON.stringify(data),preparedTable:()=>null},
 './import-preview':{buildLocalImportPreview:()=>({renderAllowed:true,invalidFeatureCount:0,authority:'UNADMITTED_BROWSER_PREVIEW',publicEffect:'NONE',featureCollection:data,featureCount:1,bounds:[-100,38,-99,39],attribution:'Fixture'})},'./local-atlas-client':{parseAtlasPreview:v=>v},'./local-atlas-presentation':presentation,
 './local-atlas-map':{attachAtlasPreview:(_m,_p,_o,inspect,state)=>{const o={dispose(){this.disposed=true},inspect};overlays.push(o);state('visible');return o},atlasScale:()=>({min:7,max:7}),ATLAS_COLORS:{low:'blue',mid:'white',high:'red'}}
 },{window:{requestAnimationFrame:f=>frames.push(f)}});
 let props={map,styleReady:true,flatMap:true,suspended:false,compact:true,reducedMotion:true,onFlatMap(){},onPrivateView:()=>events.push('private'),onViewMap:()=>{collapsed=true;events.push('collapse')},onExpand:()=>{collapsed=false;events.push('expand')},onCompactReview:v=>summary=v},tree;
 const render=(patch={})=>{props={...props,...patch};tree=h.render(h.exports.PreparedCollectionControl,props);findNode(tree,n=>n.props?.className==='prepared-review').props.ref.current=host;h.commit();return tree};
 const stable=()=>{render();render()};stable();
 return{h,render,stable,flush(){while(frames.length)frames.shift()()},async choose(){findNode(tree,n=>n.type==='input'&&n.props.type==='file').props.onChange({target:{files:[{name:'fixture'}],value:'x'}});await settle();stable()},show(){button(tree,'Show verified view').props.onClick();stable()},fits,events,overlays,resolve:()=>resolve(selection),get signal(){return signal},get summary(){return summary},get tree(){return tree}};
}
test('prepared fit collapses before measuring exposed mobile map and marks camera private',async()=>{
 const s=await setup();await s.choose();s.show();assert.match(s.summary.title,/Fixture collection.*Temperature/);assert.match(s.summary.detail,/1 features.*°F.*Frozen/);assert.match(s.summary.range,/7–7.*°F/);s.summary.fit();assert.equal(s.fits.length,0);assert.deepEqual(s.events.slice(-2),['private','collapse']);s.flush();assert.equal(s.fits.length,1);assert.deepEqual(JSON.parse(JSON.stringify(s.fits[0].o.padding)),{top:32,left:24,right:24,bottom:263});assert.equal(s.fits[0].o.duration,0);s.h.dispose();assert.equal(s.summary,null);assert.equal(s.overlays.at(-1).disposed,true);
});
test('queued fits are retired by clear, member change, suspension and unmount',async()=>{
 for(const action of ['clear','member','suspend','unmount']){const s=await setup();await s.choose();s.show();s.summary.fit();if(action==='clear')s.summary.clearMap();if(action==='member')findNode(s.tree,n=>n.type==='select'&&n.props.value===member).props.onChange({target:{value:member}});if(action==='suspend')s.render({suspended:true});if(action==='unmount')s.h.dispose();else s.stable();s.flush();assert.equal(s.fits.length,0,action);if(action!=='unmount')s.h.dispose()}
});
test('compact hide, selection and inspection use actual child state and focus expanded inspector',async()=>{
 const s=await setup();await s.choose();s.show();s.summary.toggle();s.stable();assert.equal(s.summary.visible,false);assert.equal(s.overlays.at(-1).disposed,true);s.summary.toggle();s.stable();assert.equal(s.summary.visible,true);s.overlays.at(-1).inspect({name:'Fixture station',value:7});s.stable();assert.equal(s.summary.selected,'Fixture station');s.summary.inspect();s.flush();assert.deepEqual(s.events.slice(-3),['expand','scroll','focus']);s.summary.clearMap();s.stable();assert.equal(s.summary.hasPreview,false);assert.equal(s.summary.selected,null);s.h.dispose();
});
test('verification cancellation aborts pending response without resurrecting selection',async()=>{
 const s=await setup(true);await s.choose();assert.equal(s.summary.busy,true);s.summary.cancel();s.stable();assert.equal(s.signal.aborted,true);s.resolve();await settle();s.stable();assert.equal(s.summary.busy,false);assert.equal(s.summary.hasPreview,false);assert.match(s.summary.detail,/choose a prepared folder/);s.h.dispose();
});
test('parent exposes prepared actions outside inert hidden controls',async()=>{
 const Prepared=()=>null;const h=await componentHarness('app/local-atlas-control.tsx',{'./intake-desk-client':{INTAKE_DESK_ORIGIN:'http://127.0.0.1'},'./local-atlas-client':{AtlasRequestGate:class{clear(){}}},'./local-atlas-presentation':presentation,'./prepared-collection-control':{PreparedCollectionControl:Prepared},'./local-atlas-map':{ATLAS_COLORS:{}}});
 const props={map:null,styleReady:false,flatMap:true,suspended:false,compact:true,collapsed:true,onViewMap(){},onExpand(){},reducedMotion:true,onFlatMap(){},onArchive(){},onPrivateView(){}};let tree=h.render(h.exports.LocalAtlasControl,props),called='';const child=findNode(tree,n=>n.type===Prepared);
 child.props.onCompactReview({title:'Prepared frame',detail:'2 features · ft³/s · frozen',range:'2–7 ft³/s',status:'Private review visible',selected:'Station A',hasPreview:true,visible:true,canFit:true,busy:false,error:'',fit:()=>called='fit',toggle:()=>called='toggle',inspect:()=>called='inspect',clearMap:()=>called='clear'});
 tree=h.render(h.exports.LocalAtlasControl,props);const peek=findNode(tree,n=>n.props?.['aria-label']==='Prepared preview on map'),body=findNode(tree,n=>n.props?.id==='local-atlas-controls');assert.equal(body.props.hidden,true);assert.equal(body.props.inert,true);assert.match(text(peek),/Prepared frame.*ft³\/s.*Station A/);assert.doesNotMatch(text(peek),/choose local data/);
 for(const[name,expected]of[['Fit review','fit'],['Hide review','toggle'],['Inspect details','inspect'],['Clear map','clear']]){button(peek,name).props.onClick();assert.equal(called,expected)}
 child.props.onCompactReview({title:'Verifying',detail:'Device check',hasPreview:false,busy:true,error:'',cancel:()=>called='cancel'});tree=h.render(h.exports.LocalAtlasControl,props);button(tree,'Cancel verification').props.onClick();assert.equal(called,'cancel');h.dispose();
});

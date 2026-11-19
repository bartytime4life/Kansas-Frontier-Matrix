import assert from 'node:assert/strict';
import test from 'node:test';
import { componentHarness, settle } from './component-harness.mjs';

const types = ['surface','underground','solution','unspecified'];
const only = selected => Object.fromEntries(types.map(type => [type,type===selected]));
const row = operation => ({id:`minerals:${operation}`,mineOperation:operation,name:operation,coordinates:[-99.5,38.8],details:[],material:'Limestone',status:'Historical'});

test('changing mine operations clears old marks, separates cached counts and ignores delayed responses',async()=>{
  const requests=[],sources=new Map(),layers=new Map();let pendingUnderground;
  const map={
    getCenter:()=>({lng:-99.5,lat:38.8}),getBounds:()=>({getWest:()=>-99.55,getEast:()=>-99.45,getSouth:()=>38.75,getNorth:()=>38.85}),
    getCanvas:()=>({clientWidth:1000,clientHeight:700}),project:([x,y])=>({x,y}),unproject:([lng,lat])=>({lng,lat}),
    isStyleLoaded:()=>true,on(){},off(){},getLayer:id=>layers.get(id),addLayer:layer=>layers.set(layer.id,layer),removeLayer:id=>layers.delete(id),
    getSource:id=>sources.get(id),addSource(id,source){sources.set(id,{data:source.data,setData(data){this.data=data;}});},removeSource:id=>sources.delete(id),
  };
  const h=await componentHarness('app/geology-point-explorer.tsx',{
    './bounded-json':{readBoundedJson:r=>r.json()},
    './subsurface-workers':{startSubsurfaceWorker:()=>({postMessage(){},terminate(){}})},
    './underground-resources-model':{MINE_OPERATIONS:types,RESOURCE_SOURCES:{}},
    './geology-resource-grid':{geologyResourceCells:()=>[],layoutResourceGroups:groups=>groups},
    './geology-layer-controls':{GeologyLayerControls:()=>null},
    './geology-point-explorer.module.css':{default:new Proxy({},{get:(_,key)=>String(key)})},
  },{URLSearchParams,fetch:(url,options)=>{
    const query=new URL(url,'https://kfm.test').searchParams;requests.push({query,options});
    const operation=query.get('mineTypes');
    if(operation==='underground')return new Promise(resolve=>{pendingUnderground=resolve;});
    return Promise.resolve(query.get('mode')==='count'?Response.json({count:1}):Response.json({rows:[row(operation)],partial:false}));
  }});
  const props={map,enabled:true,redacted:false,monitoringVisible:false,pickingEnabled:()=>true,
    visibility:{well:false,core:false,oilgas:false,minerals:true},onVisibility(){},mineVisibility:only('surface'),onMineVisibility(){},earthquakeMode:'off',onEarthquakeMode(){},onUnderground(){},dockOpen:false};
  const render=()=>{const tree=h.render(h.exports.default,props);h.commit();return tree;};
  const ids=()=>[...sources.values()].flatMap(source=>source.data.features.map(feature=>feature.properties.id));
  try{
    render();render();await new Promise(resolve=>setImmediate(resolve));await settle();render();
    assert.deepEqual(ids(),['minerals:surface']);
    props.mineVisibility=only('underground');render();
    assert.deepEqual(ids(),[],'old surface marks disappear before the next response');
    assert.ok(pendingUnderground,'a different operation needs a fresh count');
    const delayed=requests.at(-1);
    props.mineVisibility=only('solution');render();
    assert.equal(delayed.options.signal.aborted,true);
    pendingUnderground(Response.json({count:1}));
    await new Promise(resolve=>setImmediate(resolve));await settle();render();
    assert.deepEqual(ids(),['minerals:solution']);
    assert.ok(requests.every(({query})=>query.get('kind')==='minerals'),'hidden oil/gas source is not requested');
    assert.equal(requests.filter(({query})=>query.get('mineTypes')==='underground').length,1,'aborted count cannot start a detail page');
    for(const operation of ['surface','solution'])assert.deepEqual(requests.filter(({query})=>query.get('mineTypes')===operation).map(({query})=>query.get('mode')??'page'),['count','page']);
    props.mineVisibility=only(null);const before=requests.length;render();await settle();render();
    assert.deepEqual(ids(),[]);assert.equal(requests.length,before,'no enabled mine operations means no source request');
  }finally{h.dispose();}
});

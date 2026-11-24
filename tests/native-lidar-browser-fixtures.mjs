// Explicit synthetic analytic transport for normal CI only. The installed map,
// production shaders, MRT color/ID frame, hit dispatcher and readings stay real.
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {groundFixture} from './kansas-ground-fixtures.mjs';
import {kansasFixture} from './kansas-lidar-fixtures.mjs';
import {pointFixture} from './native-lidar-fixtures.mjs';
import {terrainBrowserFixtures} from './terrain-detail-browser-fixtures.mjs';
export function nativeCloudFixture(){
  const base=pointFixture(),points=[];
  for(let row=0;row<41;row++)for(let col=0;col<41;col++)points.push([-10751800+col*3,4734600+row*3,354+row*.12+Math.sin(col/5)*2,1000+row*20+col,2,1,1,row===20&&col===20?4:0,207515600+points.length/100,0,points.length]);
  const chunk={...base.chunks[0],points},zs=points.map(p=>p[2]),manifest={...base.manifest,pointCount:points.length,bounds3857:[points[0][0],points[0][1],points.at(-1)[0],points.at(-1)[1]],heightRange:[Math.min(...zs),Math.max(...zs)],chunks:[{...base.manifest.chunks[0],pointCount:points.length,bytes:Buffer.byteLength(JSON.stringify(chunk))}]};
  manifest.source={...manifest.source,acquisition:'Synthetic CI source only; not observations',selection:'Synthetic analytic grid for GPU regression only; not native LiDAR density',notes:['Synthetic CI fixture, no real provider observations.']};
  return {manifest,chunks:[chunk],points};
}
export function nativeViewportFixture(query){
  const f=nativeCloudFixture(),requestKey=createHash('sha256').update(JSON.stringify(query)).digest('hex'),asset={...f.manifest.source.assets[0],project:'KS_Statewide_B6A_2018',eptUrl:f.manifest.source.eptUrl,coordinateEncodingM:[.001,.001,.001],acquisition:'Synthetic CI only; not observations',verticalReference:'Synthetic display fixture, no accuracy claim',gpsTimeType:'week'};
  const points={...f.manifest,format:'kfm-lidar-points-manifest-v2',captureId:'view-'+requestKey,source:{...f.manifest.source,project:'Kansas viewport',eptUrl:'https://usgs.entwine.io/',assets:[asset]}};delete points.cache;
  const chunk={...f.chunks[0],format:'kfm-lidar-points-chunk-v2',captureId:points.captureId};
  return {receipt:{format:'kfm-lidar-view-v1',requestKey,query,generatedAt:f.manifest.generatedAt,state:'ready',layers:['ground','surface','canopy','points'].map(kind=>({kind,state:kind==='ground'||kind==='points'?'ready':'idle',method:'Synthetic CI analytic source',message:'Synthetic rendering fixture; no native-provider acceptance'})),coverage:[{project:asset.project,eptUrl:asset.eptUrl,boundsWgs84:[-96.60,39.08,-96.57,39.11],acquisition:asset.acquisition,verticalReference:asset.verticalReference,qualification:'Synthetic GPU regression only'}],points,grid:null,reason:'Synthetic source fixture; no provider observations',limits:{maxPoints:100000,maxChunks:16,maxReplyBytes:1000000,maxTotalBytes:16777216,maxConcurrentChunks:2},cache:f.manifest.cache},chunk};
}
export async function nativeLidarBrowserFixtures(origin,{solid=false}={}){
  const terrain=await terrainBrowserFixtures(origin,{fail3dep:false}),fixture=nativeCloudFixture(),views=new Map(),hits={manifest:0,chunks:0,ground:0,instrumented:0};let latestGrid=null;
  const setupSource=`window.__nativeFixturePoints=${JSON.stringify(fixture.points)};window.__nativeFixtureFrames=0;window.__nativeFixtureErrors=[];window.__nativeVisiblePoint=()=>{const map=window.__terrainAcceptanceMap,layer=map?.getLayer('external-native-lidar-points')?.implementation,m=window.__nativeFixtureMatrix;if(!layer||!m||layer.failed)return null;const canvas=map.getCanvas(),r=canvas.getBoundingClientRect(),scale=Number(document.querySelector('[aria-label="Kansas LiDAR map identity"]')?.textContent.match(/([0-9.]+)× display/)?.[1]);if(!scale)return null;for(const p of window.__nativeFixturePoints){if(p[7]&4)continue;const lat=(2*Math.atan(Math.exp(p[1]/6378137))-Math.PI/2),v=[.5+p[0]/(2*Math.PI*6378137),.5-p[1]/(2*Math.PI*6378137),p[2]*scale/(2*Math.PI*6371008.8*Math.cos(lat)),1],clip=Array.from({length:4},(_,row)=>v.reduce((n,x,col)=>n+x*m[col*4+row],0));if(clip[3]<=0)continue;const x=(clip[0]/clip[3]+1)*r.width/2,y=(1-clip[1]/clip[3])*r.height/2;if(x<3||y<3||x>=r.width-3||y>=r.height-3||document.elementFromPoint(r.left+x,r.top+y)!==canvas)continue;const pageX=Math.round(r.left+x),pageY=Math.round(r.top+y),index=layer.pick({x:pageX-r.left,y:pageY-r.top});if(index!==null){const selected=window.__nativeFixturePoints[index];return {x:pageX,y:pageY,index,asset:selected[9],record:selected[10],z:selected[2],frames:window.__nativeFixtureFrames};}}return null;};`;
  return {...terrain,hits,get grid(){return latestGrid;},
    async setup(call){await terrain.setup(call);await call('Page.addScriptToEvaluateOnNewDocument',{source:setupSource+solidSetupSource});},
    async intercept(event,call){
      const url=new URL(event.request.url),fulfill=(value,type='application/json')=>call('Fetch.fulfillRequest',{requestId:event.requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:type}],body:Buffer.from(value).toString('base64')});
      if(url.origin===origin.origin&&url.pathname==='/api/terrain/ground'){const f=groundFixture(url.searchParams.get('bbox').split(',').map(Number));hits.ground++;if(solid)latestGrid=f.receipt.grid;else {f.receipt.grid=null;f.receipt.state='unavailable';f.receipt.reason='Synthetic point-only regression intentionally omits Ground; no provider request.';}await fulfill(JSON.stringify(f.receipt));return true;}
      if(url.origin===origin.origin&&url.pathname==='/api/lidar/view'){const query={bbox:url.searchParams.get('bbox').split(',').map(Number),zoom:Number(url.searchParams.get('zoom')),layers:url.searchParams.get('layers').split(',')},view=solid?solidViewportFixture(query):nativeViewportFixture(query);views.set(view.receipt.requestKey,view);hits.manifest++;await fulfill(JSON.stringify(view.receipt));return true;}
      const grid=url.pathname.match(/^\/api\/lidar\/view\/([a-f0-9]{64})\/grid$/);if(url.origin===origin.origin&&grid){const view=views.get(grid[1]);assert.ok(view?.grid);latestGrid=view.grid;await fulfill(JSON.stringify(view.grid));return true;}
      const chunk=url.pathname.match(/^\/api\/lidar\/view\/([a-f0-9]{64})\/0$/);if(url.origin===origin.origin&&chunk){assert.ok(views.has(chunk[1]));hits.chunks++;await fulfill(JSON.stringify(views.get(chunk[1]).chunk));return true;}
      if(url.origin===origin.origin&&/^\/assets\/maplibre-gl-[\w-]+\.js$/.test(url.pathname)){
        let js=await readFile(`dist/client${url.pathname}`,'utf8');const name=js.match(/([\w$]+) as Map,/)?.[1];assert.ok(name,'instrument actual installed map export');
        js+=`\n;{const proto=${name}.prototype,on=proto.on,add=proto.addLayer;const captured=new WeakSet();proto.on=function(...args){if(this.getContainer().id==='map-canvas'){window.__terrainAcceptanceMap=this;if(!captured.has(this)){captured.add(this);on.call(this,'click',event=>{const index=this.getLayer('external-native-lidar-points')?.implementation?.pick(event.point);window.__nativeDispatchedPick=index==null?null:{index,asset:window.__nativeFixturePoints[index][9],record:window.__nativeFixturePoints[index][10],z:window.__nativeFixturePoints[index][2],frame:window.__nativeFixtureFrames,cssX:event.point.x,cssY:event.point.y};const cell=this.getLayer('external-kansas-lidar-grid')?.implementation?.pick(event.point);window.__solidDispatchedPick=cell==null?null:{index:cell,frame:window.__solidFixtureFrames};});}}return on.apply(this,args);};proto.addLayer=function(layer,...args){if(layer.id==='external-native-lidar-points'){const render=layer.render;layer.render=function(gl,input){render.call(this,gl,input);window.__nativeFixtureMatrix=Array.from(input.defaultProjectionData.mainMatrix);window.__nativeFixtureFrames++;const error=gl.getError();if(error)window.__nativeFixtureErrors.push(error);};}if(layer.id==='external-kansas-lidar-grid'){const render=layer.render;layer.render=function(gl,input){const upload=gl.bufferData,matrix=gl.uniformMatrix4fv;gl.bufferData=function(target,values,...args){if(values instanceof Float32Array)window.__solidFixtureVertices=Array.from(values);return upload.call(this,target,values,...args);};gl.uniformMatrix4fv=function(location,transpose,value){window.__solidFixtureMatrix=Array.from(value);return matrix.call(this,location,transpose,value);};try{render.call(this,gl,input);}finally{gl.bufferData=upload;gl.uniformMatrix4fv=matrix;}window.__solidFixtureFrames++;const error=gl.getError();if(error)window.__nativeFixtureErrors.push(error);};}return add.call(this,layer,...args);};}\n`;
        await fulfill(js,'text/javascript');hits.instrumented++;return true;
      }
      return terrain.intercept(event,call);
    },
  };
}

function solidViewportFixture(query){
 const view=nativeViewportFixture(query),g=kansasFixture().grid,w=64,h=64,R=6378137,center=[-10751740,4734660],lat=(2*Math.atan(Math.exp(center[1]/R))-Math.PI/2),step=10/Math.cos(lat);
 const corners=Array.from({length:(w+1)*(h+1)},(_,i)=>{const x=center[0]+(i%(w+1)-w/2)*step,y=center[1]+(h/2-Math.floor(i/(w+1)))*step;return [x/R*180/Math.PI,(2*Math.atan(Math.exp(y/R))-Math.PI/2)*180/Math.PI];});
 const ground=Array.from({length:w*h},(_,i)=>Math.fround(350+Math.floor(i/w)*.25+Math.cos(i%w/6)*3)),surface=ground.map((z,i)=>i===2015?null:Math.fround(z+4+Math.abs(Math.sin(i%w/5))*8)),canopy=surface.map((z,i)=>z===null?null:Math.fround(1+Math.abs(Math.sin(i%w/5))*8));ground[2015]=null;
 const asset={...view.receipt.points.source.assets[0],id:0},grid={...g,requestKey:view.receipt.requestKey,width:w,height:h,bounds:[666000,4328000,666640,4328640],cellSizeM:[10,10],cornersWgs84:corners,ground,surface,canopy,groundCounts:ground.map(v=>v===null?0:5),surfaceCounts:surface.map(v=>v===null?0:8),vegetationCounts:canopy.map(v=>v===null?0:3),groundResidualM:ground.map(v=>v===null?null:.1),source:{...g.source,project:asset.project,eptUrl:asset.eptUrl,assets:[asset],acquisition:asset.acquisition,verticalReference:asset.verticalReference}};
 view.receipt.points=query.layers.includes('points')?view.receipt.points:null;view.receipt.grid={format:grid.format,width:w,height:h,sourceProject:grid.source.project};view.receipt.state='partial';view.receipt.layers.forEach(l=>{l.state=query.layers.includes(l.kind)?'partial':l.kind==='ground'?'ready':'idle';});view.grid=grid;return view;
}
const solidSetupSource=String.raw`
window.__solidFixtureFrames=0;
window.__solidProbeDOMRevision=0;
window.__solidProbeStats={calls:0,builds:0,reads:0,projected:0};
if(typeof MutationObserver==='function'){
 let observing=false;
 const observe=()=>{if(observing||!document.documentElement)return;observing=true;new MutationObserver(()=>{window.__solidProbeDOMRevision++;}).observe(document.documentElement,{subtree:true,childList:true,attributes:true,attributeFilter:['class','style','open','hidden','aria-hidden']});};
 observe();if(!observing)document.addEventListener('DOMContentLoaded',observe,{once:true});
}
window.__solidVisibleCell=()=>{
 const map=window.__terrainAcceptanceMap,layer=map?.getLayer('external-kansas-lidar-grid')?.implementation,m=window.__solidFixtureMatrix,v=window.__solidFixtureVertices,stats=window.__solidProbeStats;stats.calls++;stats.reads=0;
 if(!layer||layer.failed||!m||!v)return null;
 const canvas=map.getCanvas(),r=canvas.getBoundingClientRect(),key=[...m,r.left,r.top,r.width,r.height,window.__solidProbeDOMRevision].join(','),old=window.__solidProbeCache;
 let cache=old?.layer===layer&&old.vertices===v&&old.key===key?old:null;
 if(!cache){
  const projected=[];let last=0;stats.builds++;
  for(let i=0;i+20<v.length;i+=7){const id=v[i+6];if(id===last)continue;last=id;
   const x=(v[i]+v[i+7]+v[i+14])/3,y=(v[i+1]+v[i+8]+v[i+15])/3,z=(v[i+2]+v[i+9]+v[i+16])/3,w=x*m[3]+y*m[7]+z*m[11]+m[15];if(w<=0)continue;
   const px=((x*m[0]+y*m[4]+z*m[8]+m[12])/w+1)*r.width/2,py=(1-(x*m[1]+y*m[5]+z*m[9]+m[13])/w)*r.height/2;
   if(px<3||py<3||px>=r.width-3||py>=r.height-3)continue;projected.push({x:Math.round(r.left+px),y:Math.round(r.top+py)});
  }
  stats.projected=projected.length;
  const buckets=new Map();if(projected.length){const xs=projected.map(p=>p.x),ys=projected.map(p=>p.y),left=Math.min(...xs),right=Math.max(...xs),top=Math.min(...ys),bottom=Math.max(...ys),width=Math.max(1,right-left),height=Math.max(1,bottom-top);
   for(const p of projected){const col=Math.min(7,Math.floor((p.x-left)/width*8)),row=Math.min(7,Math.floor((p.y-top)/height*8)),id=row*8+col,cx=left+(col+.5)*width/8,cy=top+(row+.5)*height/8,distance=(p.x-cx)**2+(p.y-cy)**2;if(!buckets.has(id)||distance<buckets.get(id).distance)buckets.set(id,{...p,distance,priority:(col-3.5)**2+(row-3.5)**2});}
  }
  cache={layer,vertices:v,key,points:[...buckets.values()].sort((a,b)=>a.priority-b.priority),hit:null};window.__solidProbeCache=cache;
 }
 const seen=new Set(),candidates=cache.hit?[cache.hit,...cache.points]:cache.points;
 for(const p of candidates){const pixel=p.x+','+p.y;if(seen.has(pixel))continue;seen.add(pixel);if(stats.reads>=64)break;
  // Check the exact integer CSS pixel delivered by the real pointer dispatcher.
  // Cached projections never substitute for the current production GPU-ID read.
  if(document.elementFromPoint(p.x,p.y)!==canvas)continue;stats.reads++;const index=layer.pick({x:p.x-r.left,y:p.y-r.top});
  if(index!==null){cache.hit=p;return {index,x:p.x,y:p.y,frame:window.__solidFixtureFrames};}
 }
 cache.hit=null;return null;
};`;

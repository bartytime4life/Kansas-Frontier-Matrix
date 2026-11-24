// Explicit synthetic analytic transport for normal CI only. The installed map,
// production shaders, MRT color/ID frame, hit dispatcher and readings stay real.
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
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
export async function nativeLidarBrowserFixtures(origin){
  const terrain=await terrainBrowserFixtures(origin,{fail3dep:false}),fixture=nativeCloudFixture(),views=new Map(),hits={manifest:0,chunks:0,instrumented:0};
  const setupSource=`window.__nativeFixturePoints=${JSON.stringify(fixture.points)};window.__nativeFixtureFrames=0;window.__nativeFixtureErrors=[];window.__nativeVisiblePoint=()=>{const map=window.__terrainAcceptanceMap,layer=map?.getLayer('external-native-lidar-points')?.implementation,m=window.__nativeFixtureMatrix;if(!layer||!m||layer.failed)return null;const canvas=map.getCanvas(),r=canvas.getBoundingClientRect(),scale=Number(document.querySelector('[aria-label="Kansas LiDAR map identity"]')?.textContent.match(/([0-9.]+)× display/)?.[1]);if(!scale)return null;for(const p of window.__nativeFixturePoints){if(p[7]&4)continue;const lat=(2*Math.atan(Math.exp(p[1]/6378137))-Math.PI/2),v=[.5+p[0]/(2*Math.PI*6378137),.5-p[1]/(2*Math.PI*6378137),p[2]*scale/(2*Math.PI*6371008.8*Math.cos(lat)),1],clip=Array.from({length:4},(_,row)=>v.reduce((n,x,col)=>n+x*m[col*4+row],0));if(clip[3]<=0)continue;const x=(clip[0]/clip[3]+1)*r.width/2,y=(1-clip[1]/clip[3])*r.height/2;if(x<3||y<3||x>=r.width-3||y>=r.height-3||document.elementFromPoint(r.left+x,r.top+y)!==canvas)continue;const index=layer.pick({x,y});if(index!==null){const selected=window.__nativeFixturePoints[index];return {x:r.left+x,y:r.top+y,index,asset:selected[9],record:selected[10],z:selected[2],frames:window.__nativeFixtureFrames};}}return null;};`;
  return {...terrain,hits,
    async setup(call){await terrain.setup(call);await call('Page.addScriptToEvaluateOnNewDocument',{source:setupSource});},
    async intercept(event,call){
      const url=new URL(event.request.url),fulfill=(value,type='application/json')=>call('Fetch.fulfillRequest',{requestId:event.requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:type}],body:Buffer.from(value).toString('base64')});
      if(url.origin===origin.origin&&url.pathname==='/api/lidar/view'){const query={bbox:url.searchParams.get('bbox').split(',').map(Number),zoom:Number(url.searchParams.get('zoom')),layers:url.searchParams.get('layers').split(',')},view=nativeViewportFixture(query);views.set(view.receipt.requestKey,view);hits.manifest++;await fulfill(JSON.stringify(view.receipt));return true;}
      const chunk=url.pathname.match(/^\/api\/lidar\/view\/([a-f0-9]{64})\/0$/);if(url.origin===origin.origin&&chunk){assert.ok(views.has(chunk[1]));hits.chunks++;await fulfill(JSON.stringify(views.get(chunk[1]).chunk));return true;}
      if(url.origin===origin.origin&&/^\/assets\/maplibre-gl-[\w-]+\.js$/.test(url.pathname)){
        let js=await readFile(`dist/client${url.pathname}`,'utf8');const name=js.match(/([\w$]+) as Map,/)?.[1];assert.ok(name,'instrument actual installed map export');
        js+=`\n;{const proto=${name}.prototype,on=proto.on,add=proto.addLayer;proto.on=function(...args){if(this.getContainer().id==='map-canvas')window.__terrainAcceptanceMap=this;return on.apply(this,args);};proto.addLayer=function(layer,...args){if(layer.id==='external-native-lidar-points'){const render=layer.render;layer.render=function(gl,input){render.call(this,gl,input);window.__nativeFixtureMatrix=Array.from(input.defaultProjectionData.mainMatrix);window.__nativeFixtureFrames++;const error=gl.getError();if(error)window.__nativeFixtureErrors.push(error);};}return add.call(this,layer,...args);};}\n`;
        await fulfill(js,'text/javascript');hits.instrumented++;return true;
      }
      return terrain.intercept(event,call);
    },
  };
}

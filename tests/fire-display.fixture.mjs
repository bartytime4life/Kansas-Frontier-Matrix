// Browser-only synthetic renderer scene. Bundled in tests; never a public route.
import { loadMapLibre } from '../app/maplibre-seam';
import { applyOfficialContextState, OFFICIAL_CONTEXT_SOURCES } from '../app/live-context';
import { setFireDetectionMotion, FIRE_POINT_LAYER_IDS, FIRE_REPORT_FLAME_ID, currentFireFrame } from '../app/fire-detection-style';
const runtime = await loadMapLibre();
runtime.setWorkerUrl('/maplibre/maplibre-gl-worker.mjs');
const query=new URLSearchParams(location.search);
const features=[['high',-98.4,38.5],['nominal',-98.39,38.5],['low',-98.41,38.5]].map(([confidence,longitude,latitude],i)=>({
  type:'Feature',id:`fixture-${i}`,geometry:{type:'Point',coordinates:[longitude,latitude]},
  properties:{featureId:`fixture-${i}`,name:`SYNTHETIC ${confidence} detection`,confidence,scanKm:0.5,trackKm:0.4,dayNight:'Day',acquiredAt:'2026-10-23T12:00:00Z'},
}));
const reports={type:'FeatureCollection',features:[{...features[0],id:'fixture-report',geometry:{type:'Point',coordinates:[-98.4,38.508]},properties:{featureId:'fixture-report',name:'SYNTHETIC incident',incidentType:'Incident complex'}}]};
const visibility=Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map(s=>[s.id,['nasa-gibs-fire-points','nifc-fire-reports'].includes(s.id)]));
const opacity=Object.fromEntries(OFFICIAL_CONTEXT_SOURCES.map(s=>[s.id,1]));
const payloads={'nasa-gibs-fire-points':{data:{type:'FeatureCollection',features}},'nifc-fire-reports':{data:reports}};
const errors=[];
const map=new runtime.Map({container:'map',center:[-98.4,38.5],zoom:12,pitch:0,fadeDuration:0,canvasContextAttributes:{preserveDrawingBuffer:true},
  style:{version:8,sources:{},layers:[{id:'background',type:'background',paint:{'background-color':'#162d35'}}]}});
map.on('error',event=>errors.push(String(event.error?.message??event.error)));
await new Promise(resolve=>map.once('load',resolve));
if(query.has('fallback')) map.addImage=()=>{throw new Error('Synthetic unavailable image atlas');};
const sync=()=>applyOfficialContextState(map,visibility,opacity,payloads);
setFireDetectionMotion(false); sync();
const draw=()=>new Promise(resolve=>{map.once('render',()=>requestAnimationFrame(resolve));map.triggerRepaint();});
const ready=async()=>{for(let i=0;i<120;i++){await draw();if(map.areTilesLoaded())return;}throw new Error('fixture tiles did not load');};
const ids=[...OFFICIAL_CONTEXT_SOURCES.filter(s=>visibility[s.id]).flatMap(s=>s.interactiveLayerIds)];
map.on('click',event=>{
  const feature=map.queryRenderedFeatures(event.point,{layers:ids.filter(id=>map.getLayer(id))})[0];
  document.querySelector('#inspection').textContent=feature?JSON.stringify({id:feature.properties.featureId,source:feature.source,properties:feature.properties}):'No record';
});
// Test-local API: no production diagnostic hooks or source changes.
window.fireFixture={map,errors,draw,ready,sync,currentFireFrame,motion:setFireDetectionMotion,
  async view({zoom,pitch=0,globe=false,terrain=false,light=false}){
    map.setProjection({type:globe?'globe':'mercator'});
    map.setTerrain(null);
    if(terrain){
      // Flat 100m synthetic DEM, generated locally; tests draping, never provider terrain.
      const canvas=document.createElement('canvas');canvas.width=canvas.height=256;
      const ctx=canvas.getContext('2d');ctx.fillStyle='rgb(1,138,136)';ctx.fillRect(0,0,256,256);
      if(!map.getSource('fixture-dem'))map.addSource('fixture-dem',{type:'raster-dem',tiles:[canvas.toDataURL()],tileSize:256,maxzoom:14,encoding:'mapbox'});
      map.setTerrain({source:'fixture-dem',exaggeration:1});
    }
    map.setPaintProperty('background','background-color',light?'#e5e2d6':'#162d35');
    map.jumpTo({zoom,pitch,bearing:pitch?35:0,center:[-98.4,38.5]});sync();await ready();
  },
  async amount(amount){for(const id of ['nasa-gibs-fire-points','nifc-fire-reports'])opacity[id]=amount;sync();await ready();},
  async visible(value){for(const id of ['nasa-gibs-fire-points','nifc-fire-reports'])visibility[id]=value;sync();await ready();},
  point(id){const feature=id==='fixture-report'?reports.features[0]:features.find(f=>f.id===id);return map.project(feature.geometry.coordinates);},
  state(){return {errors,frame:currentFireFrame(),images:map.listImages().filter(id=>id.startsWith('kfm-fire')),layers:Object.fromEntries([...Object.values(FIRE_POINT_LAYER_IDS),FIRE_REPORT_FLAME_ID,'external-nifc-fire-reports-point'].filter(id=>map.getLayer(id)).map(id=>[id,{visibility:map.getLayoutProperty(id,'visibility'),opacity:map.getPaintProperty(id,map.getLayer(id).type==='symbol'?'icon-opacity':'circle-opacity')}]))};},
};
await ready(); document.body.dataset.ready='true';

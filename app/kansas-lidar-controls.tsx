'use client';
import {useEffect,useLayoutEffect,useMemo,useRef,useState,type RefObject} from 'react';
import type {Map as MapLibreMap} from './maplibre-seam';
import {createAcquisitionSession} from './acquisition-client';
import {readKansasLidarView} from './kansas-lidar-client';
import {canonicalLidarView,lidarGridCell,type KansasLidarView,type LidarViewReceipt} from './kansas-lidar-view';
import {createNativePointLayer,NATIVE_LIDAR_LAYER,registerNativeLidarPicker,type NativePointLayer,type NativeLayerOptions} from './native-lidar-layer';
import {createPreparedLidarGridLayer,KANSAS_LIDAR_GRID_LAYER,terrainGridDomain,type TerrainGrid,type LidarGridMode} from './kansas-lidar-grid-layer';
import {canonicalGroundQuery,groundCell,groundCorners,type GroundReceipt} from './kansas-ground';
import {groundColorValues,terrainColorDomain,terrainStudyJSON,type GroundColor} from './kansas-terrain-analysis';
import {readKansasGround} from './kansas-ground-client';
import {MAPLIBRE_EARTH_RADIUS_M,NATIVE_CLASS_COLORS,nativeAttributeDomain,nativePointEligible,nativePointPosition,type NativeColorMode} from './native-lidar';
import {createTerrainPreparationClient} from './terrain-preparation-client';
import type {PreparedTerrain} from './terrain-preparation-model';
import {useVisitorTerrainResources} from './visitor-terrain-resources';
import styles from './kansas-lidar-controls.module.css';
type Options={mapRef:RefObject<MapLibreMap|null>;styleReady:boolean;active:boolean;scale:number;reducedMotion:boolean;onViewMap:()=>void;onScale?:(value:number)=>void;onGround:()=>void;onNativeIntent?:()=>void;onSelected?:()=>void};
export function useKansasLidarView(options:Options){
  const [mode,setMode]=useState<LidarGridMode>('ground'),[pointsOn,setPointsOn]=useState(false),[opacity,setOpacity]=useState(85),[pointSize,setPointSize]=useState(3),[color,setColor]=useState<NativeColorMode>('elevation');
  const [result,setResult]=useState<KansasLidarView|null>(null),[receipt,setReceipt]=useState<LidarViewReceipt|null>(null),[phase,setPhase]=useState('idle'),[error,setError]=useState(''),[epoch,setEpoch]=useState(0),[selected,setSelected]=useState<{kind:'point'|'cell';index:number}|null>(null),[readingKind,setReadingKind]=useState<'point'|'cell'>('point'),[draft,setDraft]=useState(''),[applied,setApplied]=useState({points:false,grid:false});
  const resources=useVisitorTerrainResources(),markSlow=resources.markSlow;
  const [visible,setVisible]=useState(true),[preparer]=useState(createTerrainPreparationClient),[prepared,setPrepared]=useState<{grid:TerrainGrid;mode:LidarGridMode;scale:number;color:GroundColor;value:PreparedTerrain}|null>(null),[preparationPhase,setPreparationPhase]=useState('idle'),[preparationError,setPreparationError]=useState('');
  const preparationCache=useRef<typeof prepared>(null),refreshCache=useRef({ground:false,native:false});
  const [gridColor,setGridColor]=useState<GroundColor>('height'),[pinned,setPinned]=useState(false);
  const study=useRef<{id:number;bbox:[number,number,number,number];zoom:number}|null>(null),studyRevision=useRef(0),readingIntent=useRef(false);
  const [groundReceipt,setGroundReceipt]=useState<GroundReceipt|null>(null),[groundPhase,setGroundPhase]=useState('idle'),[groundError,setGroundError]=useState('');
  const [groundSession]=useState(createAcquisitionSession);
  const [session]=useState(createAcquisitionSession),latest=useRef(options),selection=useRef(selected),moving=useRef(false),pointLayer=useRef<NativePointLayer|null>(null),gridLayer=useRef<NativePointLayer|null>(null);
  const settings=useRef<NativeLayerOptions>({scale:options.scale,size:pointSize,color,gridColor,selected:null,opacity:opacity/100,framePixelLimit:resources.framePixelLimit});
  useLayoutEffect(()=>{latest.current=options;selection.current=selected;settings.current={scale:options.scale,size:pointSize,color,gridColor,selected:selected?.kind==='point'?selected.index:null,opacity:opacity/100,framePixelLimit:resources.framePixelLimit};},[options,pointSize,color,gridColor,selected,opacity,resources.framePixelLimit]);
  useEffect(()=>{const visibility=()=>{if(document.hidden){session.cancel();groundSession.cancel();preparer.cancel();}setVisible(!document.hidden);};visibility();document.addEventListener('visibilitychange',visibility);return()=>{document.removeEventListener('visibilitychange',visibility);preparer.cancel();};},[session,groundSession,preparer]);
  // An inactive/replaced map cannot retain a study-camera lease.
  // eslint-disable-next-line react-hooks/set-state-in-effect
  useEffect(()=>{if(!options.active||!options.styleReady){study.current=null;setPinned(false);}},[options.active,options.styleReady]);
  const wanted=options.active&&options.styleReady&&(pointsOn||mode!=='ground');
  useEffect(()=>{
    const map=options.mapRef.current;if(!map)return;
    const owned=(event:unknown)=>!!study.current&&(event as {kfmTerrainStudy?:number}|undefined)?.kfmTerrainStudy===study.current.id;
    const start=(event?:unknown)=>{
      pointLayer.current?.invalidate();gridLayer.current?.invalidate();
      if(owned(event))return;
      study.current=null;setPinned(false);if(moving.current)return;
      moving.current=true;readingIntent.current=false;selection.current=null;
      session.cancel();groundSession.cancel();preparer.cancel();setGroundReceipt(null);setGroundPhase('moving');setResult(null);setReceipt(null);setSelected(null);setDraft('');setPhase('moving');
    };
    const end=(event?:unknown)=>{if(owned(event))return;moving.current=false;setEpoch(n=>n+1);};
    // User gestures can interrupt an owned ease without a second movestart.
    const gesture=(event:unknown)=>{if((event as {originalEvent?:unknown})?.originalEvent)start(event);};
    map.on('movestart',start);map.on('moveend',end);for(const name of ['dragstart','zoomstart','rotatestart','pitchstart'] as const)map.on(name,gesture);
    return()=>{study.current=null;map.off('movestart',start);map.off('moveend',end);for(const name of ['dragstart','zoomstart','rotatestart','pitchstart'] as const)map.off(name,gesture);};
  },[options.mapRef,options.styleReady,session,groundSession,preparer]);
  useEffect(()=>{
    session.cancel();
    if(!visible)return;
    // These state changes mirror a new external viewport/request revision.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setResult(null);setReceipt(null);if(selection.current?.kind==='point'){selection.current=null;readingIntent.current=false;setSelected(null);setDraft('');}setError('');
    if(!wanted){setPhase('idle');return;}
    if(moving.current){setPhase('moving');return;}
    const map=options.mapRef.current;if(!map)return;const bounds=map.getBounds(),query=canonicalLidarView(study.current?.bbox??[bounds.getWest(),bounds.getSouth(),bounds.getEast(),bounds.getNorth()],study.current?.zoom??map.getZoom(),[...(mode!=='ground'?[mode]:[]),...(pointsOn?['points']:[])]);
    if(!query){setPhase('outside');return;}
    setPhase('waiting');const request=session.begin();
    const timer=setTimeout(()=>{setPhase('loading');const bypassCache=refreshCache.current.native;refreshCache.current.native=false;void readKansasLidarView(query,request.signal,r=>{if(request.current()){setReceipt(r);setPhase(r.state);}},{bypassCache}).then(data=>{if(request.current()&&latest.current.mapRef.current===map&&latest.current.active){setResult(data);if(!readingIntent.current)setReadingKind(data.points?'point':'cell');setReceipt(data.receipt);setPhase(data.receipt.state);}}).catch(e=>{if(request.current()){setError(e instanceof Error?e.message:'LiDAR view unavailable');setPhase('unavailable');}});},300);
    return()=>{if(timer)clearTimeout(timer);session.cancel();};
  },[wanted,mode,pointsOn,epoch,options.mapRef,options.active,options.styleReady,session,visible]);
  useEffect(()=>{
    groundSession.cancel();
    if(!visible)return;
    // A Ground grid belongs only to the committed current viewport.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setGroundReceipt(null);setGroundError('');
    if(!options.active||!options.styleReady||mode!=='ground'){setGroundPhase('idle');return;}
    if(moving.current){setGroundPhase('moving');return;}
    const map=options.mapRef.current;if(!map)return;const b=map.getBounds(),query=canonicalGroundQuery(study.current?.bbox??[b.getWest(),b.getSouth(),b.getEast(),b.getNorth()]);
    if(!query){setGroundPhase('outside');return;}
    setGroundPhase('waiting');const request=groundSession.begin();
    const publish=(response:GroundReceipt)=>{if(request.current()&&latest.current.mapRef.current===map&&latest.current.active){setGroundReceipt(response);setGroundPhase(response.state);if(response.grid&&!readingIntent.current)setReadingKind('cell');}};
    const timer=setTimeout(()=>{setGroundPhase('loading');const bypassCache=refreshCache.current.ground;refreshCache.current.ground=false;void readKansasGround(query,request.signal,publish,{bypassCache}).then(publish).catch(e=>{if(request.current()){setGroundError(e instanceof Error?e.message:'Ground grid unavailable');setGroundPhase('unavailable');}});},300);
    return()=>{clearTimeout(timer);groundSession.cancel();};
  },[mode,epoch,options.mapRef,options.active,options.styleReady,groundSession,visible]);
  const grid=mode==='ground'?groundReceipt?.grid??null:result?.grid??null;
  const groundAnalysis=prepared?.grid===grid?prepared.value.analysis:null;
  const preparedForRender=prepared?.grid===grid&&prepared.mode===mode&&prepared.scale===options.scale&&prepared.color===gridColor&&visible&&opacity>0?prepared.value:null;
  const cellsVisible=opacity>0;
  useEffect(()=>{
    preparer.cancel();
    // This mirrors a new current-viewport preparation job, never a CPU fallback.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setPreparationError('');
    const cached=preparationCache.current,matching=cached?.grid===grid&&cached.mode===mode&&cached.scale===options.scale&&cached.color===gridColor;
    if(!matching){preparationCache.current=null;setPrepared(null);}
    if(!grid||!options.active||!options.styleReady||!visible||!cellsVisible){setPreparationPhase(!visible?'paused':'idle');return;}
    if(matching){setPrepared(cached);setPreparationPhase(cached.value.eligibleCount?'prepared':'empty');return;}
    setPreparationPhase('preparing');let current=true;
    const previousAnalysis=cached?.grid===grid?cached.value.analysis:null;
    preparer.prepare({grid,mode,scale:options.scale,color:gridColor,analysis:previousAnalysis},{ready:value=>{if(current){if(previousAnalysis)value={...value,analysis:previousAnalysis};preparationCache.current={grid,mode,scale:options.scale,color:gridColor,value};setPrepared(preparationCache.current);setPreparationPhase(value.eligibleCount?'prepared':'empty');}},error:message=>{if(current){setPreparationError(message);setPreparationPhase('unavailable');}},slow:()=>{if(current)markSlow();}});
    return()=>{current=false;preparer.cancel();};
  },[grid,mode,options.scale,gridColor,options.active,options.styleReady,visible,cellsVisible,preparer,markSlow]);
  useEffect(()=>{
    const map=options.mapRef.current;if(!map)return;let disposed=false;
    const remove=(id:string,ref:RefObject<NativePointLayer|null>)=>{const layer=ref.current;ref.current=null;if(layer&&(map.getLayer(id) as unknown as {implementation?:unknown})?.implementation===layer)try{map.removeLayer(id);}catch{/* Renderer disposal owns final teardown. */}};
    const clear=()=>{registerNativeLidarPicker(map,null);remove(NATIVE_LIDAR_LAYER,pointLayer);remove(KANSAS_LIDAR_GRID_LAYER,gridLayer);setApplied({points:false,grid:false});};
    const sync=()=>{if(disposed)return;clear();if(!result&&!preparedForRender||!options.active||!options.styleReady||!visible||!cellsVisible||map.getProjection()?.type!=='mercator')return;
      try{
        const report=(kind:'grid'|'points')=>(text:string)=>{if(!disposed){setError(text);setApplied(previous=>({...previous,[kind]:false}));}};
        if(preparedForRender){if(map.getLayer(KANSAS_LIDAR_GRID_LAYER))throw Error('Analysis layer ID belongs to another resource');gridLayer.current=createPreparedLidarGridLayer(preparedForRender,{...settings.current,selected:selection.current?.kind==='cell'?selection.current.index:null},report('grid'));if(gridLayer.current.eligible>0)map.addLayer(gridLayer.current);else gridLayer.current=null;}
        if(result?.points&&pointsOn){if(map.getLayer(NATIVE_LIDAR_LAYER))throw Error('Native point layer ID belongs to another resource');pointLayer.current=createNativePointLayer(result.points,settings.current,report('points'));if(pointLayer.current.eligible>0)map.addLayer(pointLayer.current);else pointLayer.current=null;}
        setApplied({grid:!!gridLayer.current&&!gridLayer.current.failed,points:!!pointLayer.current&&!pointLayer.current.failed});
        registerNativeLidarPicker(map,point=>{const p=pointLayer.current?.pick(point);if(p!==null&&p!==undefined){readingIntent.current=true;setReadingKind('point');setSelected({kind:'point',index:p});setDraft(String(p+1));latest.current.onSelected?.();return true;}const cell=gridLayer.current?.pick(point);if(cell!==null&&cell!==undefined){readingIntent.current=true;setReadingKind('cell');setSelected({kind:'cell',index:cell});setDraft(String(cell+1));latest.current.onSelected?.();return true;}return false;});
      }catch(e){clear();setError(e instanceof Error?e.message:'LiDAR rendering unavailable');}
    };sync();map.on('style.load',sync);const lost=()=>{if(pointLayer.current||gridLayer.current){pointLayer.current?.invalidate();gridLayer.current?.invalidate();registerNativeLidarPicker(map,null);setApplied({points:false,grid:false});setError('Graphics context lost. Refresh this view after map recovery to retry native layers.');}};map.on('webglcontextlost',lost);const invalidate=()=>{pointLayer.current?.invalidate();gridLayer.current?.invalidate();};map.on('resize',invalidate);
    return()=>{disposed=true;map.off('style.load',sync);map.off('webglcontextlost',lost);map.off('resize',invalidate);clear();};
  },[result,preparedForRender,pointsOn,options.active,options.styleReady,options.mapRef,visible,cellsVisible]);
  // Mirror a contained external GPU settings failure into this control only.
  // eslint-disable-next-line react-hooks/set-state-in-effect
  useEffect(()=>{try{pointLayer.current?.update(settings.current);if(preparedForRender)gridLayer.current?.update({...settings.current,selected:selected?.kind==='cell'?selected.index:null});}catch(e){setError(e instanceof Error?e.message:'LiDAR settings unavailable');}},[options.scale,pointSize,color,gridColor,selected,opacity,preparedForRender,resources.framePixelLimit]);
  function inspectLandscape(){
    const current=latest.current,map=current.mapRef.current;if(!map||!grid||!preparedForRender||!applied.grid||!current.active||!current.styleReady||!visible)return;
    try{
      const corners=grid.format==='kfm-3dep-ground-grid-v1'?groundCorners(grid):grid.cornersWgs84,lons=corners.map(p=>p[0]),lats=corners.map(p=>p[1]),bbox:[number,number,number,number]=[Math.min(...lons),Math.min(...lats),Math.max(...lons),Math.max(...lats)];
      const heights=(mode==='canopy'?grid.ground.map((z,i)=>z!==null&&grid.format==='kfm-lidar-grid-v1'&&grid.canopy[i]!==null&&grid.canopy[i]!>=0?z+grid.canopy[i]!:null):grid.format==='kfm-3dep-ground-grid-v1'?grid.ground:grid[mode]).filter((z):z is number=>z!==null&&Number.isFinite(z));
      if(!heights.length)throw Error('No supported height cells');
      const canvas=map.getCanvas(),width=canvas.clientWidth,height=canvas.clientHeight,bearing=map.getBearing(),pitch=55,fov=map.getVerticalFieldOfView(),elevation=map.getCenterElevation();
      if(width<160||height<160||![bearing,fov].every(Number.isFinite)||fov<=0||fov>=90)throw Error('Map viewport unavailable');
      // Leave camera altitude above the actual scaled tops without changing its
      // public elevation/clamp. This is a display safety margin, not datum QA.
      const clearance=Math.max(100,Math.max(...heights)*current.scale-(Number.isFinite(elevation)?elevation:0)+100),latitude=(bbox[1]+bbox[3])/2*Math.PI/180;
      const maxZoom=Math.min(18,Math.log2((height/2/Math.tan(fov*Math.PI/360))*Math.cos(pitch*Math.PI/180)*2*Math.PI*MAPLIBRE_EARTH_RADIUS_M*Math.cos(latitude)/(512*clearance)));
      const camera=map.cameraForBounds([[bbox[0],bbox[1]],[bbox[2],bbox[3]]],{bearing,maxZoom,padding:{left:Math.max(28,width*.17),right:Math.max(28,width*.17),top:Math.max(36,height*.2),bottom:Math.max(36,height*.22)}});
      if(!camera||!Number.isFinite(camera.zoom))throw Error('Footprint could not be framed');
      const query=mode==='ground'?groundReceipt?.query:result?.receipt.query;
      map.stop(); // Finish an older owned ease while its original event tag is still current.
      study.current={id:++studyRevision.current,bbox:[...(query?.bbox??bbox)],zoom:query&&'zoom' in query?query.zoom:map.getZoom()};setPinned(true);setOpacity(100);
      map.easeTo({...camera,pitch,duration:current.reducedMotion?0:700,essential:false},{kfmTerrainStudy:study.current.id});current.onViewMap();
    }catch{study.current=null;setPinned(false);setError('This landscape could not be framed. Its source cells and readings are unchanged.');}
  }
  function followMap(){study.current=null;setPinned(false);latest.current.mapRef.current?.stop();moving.current=false;readingIntent.current=false;selection.current=null;session.cancel();groundSession.cancel();setSelected(null);setDraft('');setEpoch(n=>n+1);}
  function visualRelief(){latest.current.onScale?.(3);}
  function tilt3D(){changeAngle(false);}
  function lookDown(){changeAngle(true);}
  function changeAngle(overhead:boolean){
    const current=latest.current,map=current.mapRef.current;
    if(!map||!current.active||!current.styleReady)return;
    try{
      const center=map.getCenter(),zoom=map.getZoom(),bearing=map.getBearing(),pitch=map.getPitch();
      if(![center.lng,center.lat,zoom,bearing,pitch].every(Number.isFinite))throw Error('Current map camera is unavailable.');
      map.easeTo({center:[center.lng,center.lat],zoom,bearing,pitch:overhead?Math.min(pitch,35):60,duration:current.reducedMotion?0:600,essential:false});
      current.onViewMap();
    }catch{setError('The map angle could not be changed. Source values and layers are unchanged.');}
  }
  function detailHere(){
    const current=latest.current,map=current.mapRef.current;if(!map||!current.active||!current.styleReady)return;
    try{
      if(!map.getTerrain()||!Number.isFinite(map.getCenterElevation()))throw Error('terrain');
      const center=map.getCenter(),zoom=map.getZoom(),bearing=map.getBearing();if(![center.lng,center.lat,zoom,bearing].every(Number.isFinite))throw Error('camera');
      map.easeTo({center:[center.lng,center.lat],zoom:Math.max(zoom,17.5),bearing,pitch:55,duration:current.reducedMotion?0:600,essential:false});current.onViewMap();
    }catch{setError('Detail zoom needs loaded continuous elevation context. Use Ground, then retry the selected DEM in Continuous Kansas ground model. Coverage and analysis budgets still apply.');}
  }
  const count=readingKind==='cell'?(grid?grid.width*grid.height:0):result?.points?.points.length??0;
  function choose(value:string,kind:'point'|'cell'=readingKind){readingIntent.current=true;setReadingKind(kind);setDraft(value);const n=/^\d+$/.test(value)?Number(value)-1:-1,limit=kind==='point'?result?.points?.points.length??0:grid?(grid.width*grid.height):0;setSelected(Number.isSafeInteger(n)&&n>=0&&n<limit?{kind,index:n}:null);}
  function selectMode(value:LidarGridMode){if(value===mode)return;refreshCache.current={ground:false,native:false};preparer.cancel();readingIntent.current=false;selection.current=null;latest.current.onNativeIntent?.();session.cancel();groundSession.cancel();setSelected(null);setDraft('');setReadingKind('cell');setMode(value);if(value==='ground')latest.current.onGround();}
  function clear(){preparer.cancel();study.current=null;setPinned(false);readingIntent.current=false;selection.current=null;session.cancel();groundSession.cancel();setGroundReceipt(null);setEpoch(v=>v+1);setMode('ground');setPointsOn(false);setResult(null);setReceipt(null);setPhase('idle');setReadingKind('point');setSelected(null);setDraft('');setError('');}
  return {resources,visible,preparationPhase,preparationError,mode,pinned,inspectLandscape,followMap,visualRelief,groundAnalysis,gridColor,setGridColor,pointsOn,opacity,pointSize,color,result,receipt,grid,groundReceipt,groundPhase,nativePhase:phase,phase:mode==='ground'?groundPhase:phase,error:[groundError,error,preparationError].filter(Boolean).join(' '),selected,readingKind,draft,applied,active:options.active&&options.styleReady,scale:options.scale,count:count||0,viewMap:()=>latest.current.onViewMap(),lookDown,tilt3D,detailHere,selectMode,togglePoints:()=>{latest.current.onNativeIntent?.();session.cancel();setPointsOn(v=>!v);},setOpacity,setPointSize,setColor,choose,step:(delta:number)=>{const next=selected?Math.max(0,Math.min((count||1)-1,selected.index+delta)):0;choose(String(next+1),readingKind);},retry:()=>{refreshCache.current={ground:mode==='ground',native:wanted};setEpoch(n=>n+1);},clear,clearSelection:()=>{readingIntent.current=true;setSelected(null);setDraft('');}};
}
export type KansasLidarController=ReturnType<typeof useKansasLidarView>;
const metres=(v:number|null)=>v===null?'NoData':v.toFixed(3)+' m';
const modeLabel=(mode:LidarGridMode)=>mode==='ground'?'Ground':mode==='surface'?'Surface':'Canopy height';
export function KansasLidarLayers({controller:c}:{controller:KansasLidarController}){
  const point=c.selected?.kind==='point'?c.result?.points?.points[c.selected.index]:null,grid=c.grid,providerGrid=grid?.format==='kfm-3dep-ground-grid-v1'?grid:null,nativeGrid=grid?.format==='kfm-lidar-grid-v1'?grid:null,cell=c.selected?.kind==='cell'&&nativeGrid?lidarGridCell(nativeGrid,c.selected.index):null,sample=c.selected?.kind==='cell'&&providerGrid?groundCell(providerGrid,c.selected.index):null,asset=point?c.result?.points?.manifest.source.assets[point[9]]:null;
  const domain=useMemo(()=>c.result?.points?nativeAttributeDomain(c.result.points,c.color):null,[c.result,c.color]);
  const presentClasses=useMemo(()=>c.result?.points?[...new Set(c.result.points.points.filter(nativePointEligible).map(p=>p[4]))].sort((a,b)=>a-b):[],[c.result]);
  const analysis=c.groundAnalysis;
  const gridDomain=useMemo(()=>{if(providerGrid&&c.gridColor!=='height'){return analysis?terrainColorDomain(groundColorValues(providerGrid,c.gridColor,analysis),c.gridColor):null;}return grid?terrainGridDomain(grid,c.mode):null;},[grid,c.mode,providerGrid,c.gridColor,analysis]);
  const colorTitle=providerGrid&&c.gridColor==='slope'?'Slope':providerGrid&&c.gridColor==='local-relief'?'Local relief':modeLabel(c.mode),colorUnit=providerGrid&&c.gridColor==='slope'?'°':'m';
  function downloadStudy(){if(!c.groundReceipt?.grid||!analysis)return;const blob=new Blob([terrainStudyJSON(c.groundReceipt,analysis??undefined)],{type:'application/json'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='kfm-terrain-study-'+c.groundReceipt.requestKey.slice(0,12)+'.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}

  const stale=c.groundReceipt?.cache.state==='stale'||c.receipt?.cache.state==='stale'||c.result?.grid?.cache.state==='stale'||c.result?.points?.chunkCaches.some(cache=>cache.state==='stale');
  const phase=c.phase,reason=c.mode==='ground'?c.groundReceipt?.reason:c.receipt?.reason;
  return <section className={styles.panel} aria-label="Kansas LiDAR layers"><h3>A landscape, cell by cell</h3>
    <div className={styles.modes} role="group" aria-label="Terrain layer selection">{([['ground','Ground'],['surface','Surface'],['canopy','Canopy height']] as const).map(([mode,label])=><button key={mode} type="button" aria-pressed={c.mode===mode} disabled={!c.active} onClick={()=>c.selectMode(mode)}>{label}</button>)}</div>
    <button className={styles.inspect} type="button" disabled={!c.active||!grid||!c.applied.grid} onClick={c.inspectLandscape}>Inspect landscape in 3D</button><div className={styles.actions}><button type="button" disabled={!c.active} onClick={c.visualRelief}>3× visual relief</button><button type="button" onClick={c.viewMap}>View map</button></div><p className={styles.study}>{c.pinned?'Study area pinned · framing keeps these same cells and readings. Navigate the map or choose Follow map to load a new area.':'Following map · inspect the loaded footprint as an opaque landscape block.'}</p>{c.pinned&&<button type="button" onClick={c.followMap}>Follow map</button>}
    <p role="status">{!c.visible?'Terrain work paused while this tab is hidden.':!c.active?'Open the current Terrain map period.':phase==='outside'?'This view is outside the Kansas data window.':phase==='moving'||phase==='waiting'?'Waiting for this map view…':phase==='loading'?'Loading this landscape…':phase==='idle'?'Choose a layer for this map view.':phase==='processing'?'Preparing this landscape. Ground works across the Kansas view; surface and canopy need closer native detail.':reason??'Current source response loaded.'}</p>
    {c.error&&<p className={styles.error} role="alert">{c.error}</p>}{stale&&<p className={styles.notice}>Stale cached result · see source retrieval times below.</p>}
    <p aria-live="polite">{c.preparationPhase==='preparing'?'Preparing this landscape on your device…':c.preparationPhase==='unavailable'?'Solid preparation unavailable; continuous terrain and numeric source readings remain available.':c.preparationPhase==='empty'?'No supported solid cells in this grid.':c.applied.grid?'Solid landscape attached.':c.preparationPhase==='prepared'?'Attaching the prepared landscape…':''}</p>
    <p className={styles.displayNote}>{c.scale.toFixed(1)}× display · source readings unscaled. {c.applied.grid?'Solid height cells.':'Continuous elevation remains context.'} {c.opacity===0?'Cells hidden at 0% opacity.':''}</p>
    {gridDomain&&<div className={styles.legend} data-color={providerGrid?c.gridColor:'height'} aria-label={`${colorTitle} color in ${colorUnit==='°'?'degrees':'unscaled metres'}`}><strong>{colorTitle} · {colorUnit==='°'?'degrees':'unscaled metres'}</strong><i/><span>{gridDomain[0].toFixed(2)} {colorUnit}</span><span>{gridDomain[1].toFixed(2)} {colorUnit}</span></div>}
    {providerGrid&&<p>96 × 96 resampled Ground cells · mixed source resolution. Display spacing is not native LiDAR resolution. Broad views look flatter at real scale; zoom into a landform for finer display cells.</p>}
    {providerGrid&&<details><summary>Reveal landforms · {c.gridColor==='height'?'Height':colorTitle}</summary><label>Ground color<select value={c.gridColor} onChange={e=>c.setGridColor(e.target.value as GroundColor)}><option value="height">Height</option><option value="slope">Slope · degrees</option><option value="local-relief">Local relief · metres</option></select></label><p>Color changes, source height geometry stays unchanged. Horn3×3 slope uses local WGS84 east/north distances. Local relief subtracts the full 7×7 mean. Blue/yellow are below/above that mean with a symmetric zero-centered color scale; flat zero uses neutral color. Missing/edge neighborhoods stay NoData and use neutral color. These are output-grid derivatives, not native survey detail or archaeological evidence.</p><button type="button" onClick={downloadStudy} disabled={!analysis}>Download terrain study JSON</button></details>}
    {c.mode==='canopy'&&nativeGrid?.canopy.some(v=>v!==null&&v<0)&&<p>Negative canopy values remain inspectable but are omitted from the solid display.</p>}
    {c.mode!=='ground'&&<p>Surface and canopy need complete native support in views of at most 1 km². Zoom closer when detail is required. {c.mode==='canopy'?'Only classified vegetation with same-survey ground supports canopy height.':'Surface can include buildings and wires.'} Missing support stays missing.</p>}
    {c.mode!=='ground'&&c.receipt?.layers.some(l=>l.kind===c.mode&&l.state==='detail-required')&&<button type="button" disabled={!c.active} onClick={c.detailHere}>Zoom to detail here</button>}
    <div className={styles.actions}><button type="button" disabled={!c.active} onClick={c.retry}>Refresh this view</button><button type="button" disabled={!c.active} onClick={c.lookDown}>Look down here</button></div>
    <label>Layer opacity <output>{c.opacity}%</output><input type="range" min="0" max="100" value={c.opacity} onChange={e=>c.setOpacity(Number(e.target.value))}/></label>
    {(grid||c.result?.points)&&<div className={styles.reading}><strong>Click a cell to read its source height</strong>
      {point&&<output>{metres(point[2])}<small>native elevation · unscaled</small></output>}
      {sample&&<><output>{metres(sample.ground)}<small>Ground elevation · provider DEM · unscaled</small></output><p>Row {sample.row}, column {sample.column} · {sample.approximateSpacingM.map(v=>v.toFixed(1)).join(' × ')} m approximate local display footprint.</p></>}
      {sample&&analysis&&<p>Slope {analysis.slope[c.selected!.index]===null?'NoData':analysis.slope[c.selected!.index]!.toFixed(2)+'°'} · local relief {metres(analysis.localRelief[c.selected!.index])}. Windows 3×3 /7×7; unscaled Ground.</p>}
      {cell&&<><output>{metres(cell[c.mode])}<small>{c.mode==='canopy'?'canopy height':'derived surface elevation'} · unscaled</small></output><p>Row {cell.row}, column {cell.column}; ground {metres(cell.ground)}, surface {metres(cell.surface)}, canopy {metres(cell.canopy)}.</p></>}
      {!point&&!cell&&!sample&&<p>No source reading selected. Empty space has no reading.</p>}
      <details><summary>Sample navigation &amp; source reading</summary><div className={styles.actions}><button type="button" onClick={()=>c.step(-1)}>Previous record</button><button type="button" onClick={()=>c.step(1)}>Next record</button></div>{c.result?.points&&grid&&<label>Reading type<select value={c.readingKind} onChange={e=>c.choose('1',e.target.value as 'point'|'cell')}><option value="point">Native source record</option><option value="cell">Analysis cell</option></select></label>}<label>{c.readingKind==='cell'?'Analysis cell':'Source record'} · 1–{c.count}<input type="text" inputMode="numeric" value={c.draft} onChange={e=>c.choose(e.target.value)}/></label>
      {point&&<dl><dt>Original EPSG:3857 X / Y</dt><dd>{point[0]} / {point[1]} m</dd><dt>Longitude / latitude</dt><dd>{nativePointPosition(point).longitude.toFixed(7)} / {nativePointPosition(point).latitude.toFixed(7)}°</dd><dt>Class / intensity / return</dt><dd>{point[4]} / {point[3]} / {point[5]} of {point[6]}</dd><dt>Class flags / source GPS numeric</dt><dd>{point[7]} / {point[8]===null?'absent':point[8]} · {asset?.gpsTimeType??'unspecified'}; no calendar-date conversion{point[7]&1?' · synthetic record':''}{point[7]&4?' · withheld record':''}{point[4]===7||point[4]===18?' · noise class':''}</dd><dt>Exact native asset / record</dt><dd>{point[9]} / {point[10]}</dd><dt>Source survey / acquisition</dt><dd>{asset?.project} · {asset?.acquisition}</dd><dt>Vertical reference</dt><dd>{asset?.verticalReference}</dd></dl>}
      {sample&&providerGrid&&<dl><dt>Decoded provider F32 elevation</dt><dd>{sample.ground===null?'NoData':sample.ground+' m'}</dd><dt>Actual EPSG:3857 sample center</dt><dd>{sample.x3857} / {sample.y3857} m</dd><dt>Longitude / latitude</dt><dd>{sample.longitude.toFixed(7)} / {sample.latitude.toFixed(7)}°</dd><dt>Vertical reference / acquisition</dt><dd>{providerGrid.source.verticalReference} · {providerGrid.source.acquisition}</dd></dl>}
      {cell&&nativeGrid&&<><p>Support: ground {cell.groundCount}, surface {cell.surfaceCount}, vegetation {cell.vegetationCount}; ground residual {metres(cell.groundResidualM)}. Residual is model fit, not field accuracy.</p><p>{nativeGrid.source.project} · {nativeGrid.source.acquisition} · {nativeGrid.source.verticalReference}</p></>}
      <button type="button" onClick={c.clearSelection}>Clear reading</button></details>
    </div>}
    <details data-native-points="true"><summary>Optional raw LiDAR points {c.pointsOn?'· on':''}</summary><button type="button" aria-pressed={c.pointsOn} disabled={!c.active} onClick={c.togglePoints}>LiDAR points · {c.pointsOn?'on':'off'}</button>
      <p role="status">Native point view: {c.nativePhase} · {c.receipt?.reason}</p><p>Points follow the current view. The 100,000-return display LOD is not full survey density. Look down here keeps center, zoom and bearing with a more overhead angle; it does not promise full survey density.</p>
      {c.result?.points&&<><label>Point color<select value={c.color} onChange={e=>c.setColor(e.target.value as NativeColorMode)}><option value="elevation">Native elevation</option><option value="classification">Classification</option><option value="intensity">Native intensity</option></select></label><label>Point size <output>{c.pointSize}px</output><input aria-label="Native point size" type="range" min="1" max="6" value={c.pointSize} onChange={e=>c.setPointSize(Number(e.target.value))}/></label><p>{c.result.points.points.length.toLocaleString()} source returns · {c.result.points.points.filter(nativePointEligible).length.toLocaleString()} eligible. Synthetic/withheld flags and classes 7/18 noise stay inspectable but are omitted from display. At very close zoom, source heights can lie above the camera. No source RGB is present.</p>{c.color==='classification'&&<ul className={styles.classLegend}>{presentClasses.map(code=><li key={code}><i style={{background:`rgb(${(NATIVE_CLASS_COLORS[code]??[.7,.63,.82]).map(v=>v*255).join(',')})`}}/>{code} · {({0:'Created / unclassified',1:'Unclassified',2:'Ground',3:'Low vegetation',4:'Medium vegetation',5:'High vegetation',6:'Building',9:'Water'} as Record<number,string>)[code]??'Other source class'}</li>)}</ul>}{domain&&c.color!=='classification'&&<div className={styles.legend} data-color={c.color}><i/><span>{domain[0].toFixed(2)}{c.color==='elevation'?' m':''}</span><span>{domain[1].toFixed(2)}{c.color==='elevation'?' m':''}</span></div>}</>}
      <button type="button" onClick={c.clear}>Clear native layers</button>
    </details>
    <details className={styles.device}><summary>This device</summary><label>Terrain drawing<select value={c.resources.mode} onChange={e=>c.resources.setMode(e.target.value as 'automatic'|'lightweight')}><option value="automatic">Automatic</option><option value="lightweight">Lightweight</option></select></label><p>{c.resources.lightweight?'Lighter drawing buffer':'Standard drawing buffer'} · same source cells and readings. {c.resources.slow?'Slow preparation was detected; Automatic keeps lighter drawing for this visit.':'Only the current map view is prepared.'} This limit covers the terrain add-on, not the whole map or browser.</p><label className={styles.storage}><input type="checkbox" checked={c.resources.cache.enabled} disabled={!c.resources.cache.available||c.resources.busy} onChange={e=>void c.resources.setStorage(e.target.checked)}/>Use temporary terrain storage</label><p>{(c.resources.cache.usedBytes/1048576).toFixed(1)} of {(c.resources.cache.limitBytes/1048576).toFixed(0)} MiB used · public terrain only. {c.resources.cache.available?'Your browser may remove temporary data.':'Temporary storage is unavailable; the map still works.'}</p><button type="button" disabled={!c.resources.cache.available||c.resources.busy} onClick={()=>void c.resources.clear()}>Clear temporary data</button>{c.resources.error&&<p role="alert">{c.resources.error}</p>}</details>
    <details><summary>Sources, methods &amp; coverage</summary><p>Top illumination uses supported unscaled Horn 3×3 gradients with fixed northwest grid light at 45° (55% ambient + 45% diffuse). Missing neighborhoods use constant ambient color; they are not filled. Native Surface spacing is UTM grid metres. Solid cells and closure walls are display geometry, not surveyed cliffs or subsurface. Canopy tops are same-survey ground + canopy height. Readings remain unscaled; no source elevation is rebased. Layers use their own depth above context; DEM registration is unverified. Independent scientific accuracy, admission and release remain pending.</p>
      {c.groundReceipt&&<p>Ground: {c.groundReceipt.state} · {c.groundReceipt.reason} · transport cache {c.groundReceipt.cache.state} at {c.groundReceipt.cache.at}; generated {c.groundReceipt.generatedAt}. These are not flight dates.</p>}
      {providerGrid&&<><a href={providerGrid.source.requestUrl} target="_blank" rel="noreferrer">USGS 3DEP provider DEM source ↗</a><p>{providerGrid.source.acquisition} · {providerGrid.source.verticalReference}. Retrieved {providerGrid.source.retrievedAt}.</p><p>Nearest-neighbor provider-resampled F32 elevation. EPSG:3857 grid spacing {providerGrid.cellSize3857.map(v=>v.toFixed(2)).join(' × ')} projected metres; not physical ground spacing or native survey resolution. {providerGrid.excludedValues} source values excluded; masked cells remain missing.</p><code>{providerGrid.source.sha256}</code>{providerGrid.method.limitations.map((note,i)=><p key={i}>{note}</p>)}<a href={providerGrid.source.catalog.url} target="_blank" rel="noreferrer">Intersecting catalog candidates · {providerGrid.source.catalog.state} ↗</a><p>Catalog candidates are not per-cell lineage. {providerGrid.source.catalog.complete?'Catalog response complete.':'Catalog response incomplete or unavailable.'} Raw provider date/resolution attributes are retained without inventing flight dates or common metre units.</p>{providerGrid.source.catalog.candidates.map(record=><p key={record.id}>{record.name??`Record ${record.id}`} · acquisition attribute {record.acquisitionDate??'unknown'} · start/end {record.startDate??'unknown'} / {record.endDate??'unknown'} · source {record.source??'unknown'} · DEM type {record.demType??'unknown'} · resolution attributes {record.resolutionX??'unknown'} / {record.resolutionY??'unknown'} · datum {record.verticalDatum??'unknown'}{record.metadataUrl&&<a href={record.metadataUrl} target="_blank" rel="noreferrer">Provider metadata ↗</a>}</p>)}</>}
      {c.receipt&&<><p>Native cache {c.receipt.cache.state} at {c.receipt.cache.at}; generated {c.receipt.generatedAt}. Transport times are separate from acquisition dates.</p><ul className={styles.states}>{c.receipt.layers.map(layer=><li key={layer.kind}><strong>{layer.kind}</strong><span>{layer.state.replaceAll('-',' ')}</span><small>{layer.message} {layer.method}</small></li>)}</ul>{c.receipt.coverage.map((source,i)=><div key={i}><a href={source.eptUrl} target="_blank" rel="noreferrer">{source.project} ↗</a><p>{source.acquisition} · {source.verticalReference}</p><p>{source.qualification}</p></div>)}</>}
      {nativeGrid&&<><p>Ground: {nativeGrid.method.ground}</p><p>Surface: {nativeGrid.method.surface}</p><p>Canopy: {nativeGrid.method.canopy}</p><p>{nativeGrid.method.support}</p><p>{nativeGrid.width} × {nativeGrid.height} qualified analysis cells · {nativeGrid.cellSizeM.join(' × ')} m.</p>{nativeGrid.method.limitations.map((note,i)=><p key={i}>{note}</p>)}</>}
      {(c.result?.points?.manifest.source.assets??nativeGrid?.source.assets??[]).map(source=><p key={source.id}><a href={source.url} target="_blank" rel="noreferrer">{source.project} · native asset {source.id} ↗</a><code>{source.sha256}</code></p>)}<p>Hashes identify artifacts verified upstream, not cache-enveloped browser response hashes. No layer claims statewide uniform resolution, date, classification or native density.</p><a href="/terrain">Optional Konza 3D source example ↗</a><a href="/labs/terrain">Terrain Science ↗</a>
    </details>
  </section>;
}
export function KansasLidarBadge({controller:c,controlsOpen=false}:{controller:KansasLidarController;controlsOpen?:boolean}){
  if(controlsOpen||!c.applied.grid&&!c.applied.points||c.opacity===0)return null;
  const point=c.selected?.kind==='point'?c.result?.points?.points[c.selected.index]:null,grid=c.grid,providerGrid=grid?.format==='kfm-3dep-ground-grid-v1'?grid:null,nativeGrid=grid?.format==='kfm-lidar-grid-v1'?grid:null,cell=c.selected?.kind==='cell'&&nativeGrid?lidarGridCell(nativeGrid,c.selected.index):null,sample=c.selected?.kind==='cell'&&providerGrid?groundCell(providerGrid,c.selected.index):null;
  const assets=c.result?.points?.manifest.source.assets??[],asset=point?assets[point[9]]:null,source=asset??(c.applied.grid?nativeGrid?.source:null),surveys=[...new Set(assets.map(a=>a.project))],dates=[...new Set(assets.map(a=>a.acquisition))],pointDates=dates.length===1?dates[0]:'mixed acquisition; see source details',stale=c.groundReceipt?.cache.state==='stale'||c.receipt?.cache.state==='stale'||nativeGrid?.cache.state==='stale'||c.result?.points?.chunkCaches.some(cache=>cache.state==='stale');
  return <aside className={styles.badge} aria-label="Kansas LiDAR map identity"><strong>Terrain · {c.applied.grid?modeLabel(c.mode)+' cells · ':''}{c.applied.points?'native points':''}</strong>
    <span>{source?`${asset?'Selected point':'Grid'}: ${source.project} · ${source.acquisition}`:providerGrid?'USGS 3DEP mosaic · '+providerGrid.source.acquisition:`Points: ${surveys.length===1?surveys[0]:surveys.length+' source surveys'} · ${pointDates}`}</span>{c.applied.grid&&c.applied.points&&<span>Points: {surveys.length} source surveys · {pointDates}</span>}
    <span>{c.scale.toFixed(1)}× display · {c.opacity}% opacity · source values unscaled{providerGrid&&c.gridColor!=='height'?' · color '+c.gridColor:''}</span>{c.pinned&&<span>Study area pinned · navigate to follow map</span>}<span>Coverage-limited · DEM registration unverified{stale?' · stale cache':''}</span>
    {point&&<b>{point[2].toFixed(3)} m · asset {point[9]} / record {point[10]} · unscaled</b>}
    {cell&&<b>{modeLabel(c.mode)} {metres(cell[c.mode])} · row {cell.row}, column {cell.column} · unscaled · grid footprint only</b>}
    {sample&&<b>Ground {metres(sample.ground)} · row {sample.row}, column {sample.column} · unscaled · resampled 96²</b>}
  </aside>;
}

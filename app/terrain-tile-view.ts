import {useEffect,useLayoutEffect,useRef,useState,type RefObject} from 'react';
import type {Map as MapLibreMap} from './maplibre-seam';
import {createTerrainTileStore,terrainTilePlan,type TerrainTileSnapshot,type TerrainTileData} from './terrain-viewport-tiles';
import {createTerrainPreparationClient} from './terrain-preparation-client';
import type {PreparedTerrain} from './terrain-preparation-model';
import type {LidarGridMode} from './kansas-lidar-grid-layer';
import type {GroundColor} from './kansas-terrain-analysis';
type Options={mapRef:RefObject<MapLibreMap|null>;active:boolean;styleReady:boolean;enabled:boolean;mode:LidarGridMode;scale:number;color:GroundColor;lightweight:boolean;markSlow:()=>void};
export type PreparedTileView={value:PreparedTerrain;entries:TerrainTileData[];mode:LidarGridMode;scale:number;color:GroundColor};
/** Viewport acquisition and preparation are independent of the camera inspector.
 * Camera fits never pin a center patch or prevent surrounding tiles loading. */
export function useTerrainTileView(options:Options){
 const [snapshot,setSnapshot]=useState<TerrainTileSnapshot>({version:0,plan:{key:'idle',tiles:[],state:'outside'},entries:[],pending:0,failed:0}),[store]=useState(()=>createTerrainTileStore(setSnapshot)),[preparer]=useState(createTerrainPreparationClient);
 const [visible,setVisible]=useState(true),[navigating,setNavigating]=useState(false),[revision,setRevision]=useState(0),[refresh,setRefresh]=useState(0),[prepared,setPrepared]=useState<PreparedTileView|null>(null),[preparationPhase,setPreparationPhase]=useState('idle'),[error,setError]=useState('');
 const moving=useRef(false),lastRefresh=useRef(0),latest=useRef(options);
 useLayoutEffect(()=>{latest.current=options;},[options]);
 useEffect(()=>{const visibility=()=>{setVisible(!document.hidden);if(document.hidden){store.pause();preparer.cancel();}};visibility();document.addEventListener('visibilitychange',visibility);return()=>document.removeEventListener('visibilitychange',visibility);},[store,preparer]);
 useEffect(()=>()=>{store.dispose();preparer.dispose();},[store,preparer]);
 useEffect(()=>{
  const map=options.mapRef.current;if(!map)return;
  const start=()=>{moving.current=true;setNavigating(true);};
  const end=()=>{moving.current=false;setNavigating(false);setRevision(n=>n+1);};
  map.on('movestart',start);map.on('moveend',end);map.on('resize',end);
  return()=>{map.off('movestart',start);map.off('moveend',end);map.off('resize',end);};
 },[options.mapRef,options.styleReady]);
 useEffect(()=>{
  const map=options.mapRef.current;
  if(!map||!options.active||!options.styleReady||!options.enabled||!visible){store.pause();return;}
  if(moving.current)return;
  const timer=setTimeout(()=>{const b=map.getBounds(),plan=terrainTilePlan([b.getWest(),b.getSouth(),b.getEast(),b.getNorth()],map.getZoom(),options.mode,options.lightweight),bypass=lastRefresh.current!==refresh;lastRefresh.current=refresh;store.set(plan,options.mode,bypass);},160);
  return()=>clearTimeout(timer);
 },[options.mapRef,options.active,options.styleReady,options.enabled,options.mode,options.lightweight,visible,revision,refresh,store]);
 // A progress receipt does not rebuild geometry. Prepare only a changed set of
 // validated grids; nearby pans reuse exact tiles and their original times.
 const entries=snapshot.entries.filter(e=>e.grid),signature=entries.map(e=>e.tile.key).join('|')+':'+snapshot.version;
 useEffect(()=>{
  preparer.cancel();
  if(!options.enabled||!options.active||!options.styleReady||!visible||!entries.length)return;
  let current=true;
  // Mirror a new external worker job in this view's controls.
  // eslint-disable-next-line react-hooks/set-state-in-effect
  setError('');setPreparationPhase('preparing');
  const captured=entries,settings=latest.current;
  const timer=setTimeout(()=>preparer.prepare({grid:captured[0].grid!,tiles:captured.map(e=>({key:e.tile.key,grid:e.grid!})),mode:settings.mode,scale:settings.scale,color:settings.color,lightweight:settings.lightweight},{ready:value=>{if(current){setPrepared({value,entries:captured,mode:settings.mode,scale:settings.scale,color:settings.color});setPreparationPhase(value.eligibleCount?'prepared':'empty');}},error:message=>{if(current){setError(message);setPreparationPhase('unavailable');}},slow:()=>{if(current)latest.current.markSlow();}}),80);
  return()=>{current=false;clearTimeout(timer);preparer.cancel();};
 // Entries are immutable, identity is their source request key, not progress.
 // eslint-disable-next-line react-hooks/exhaustive-deps
 },[signature,options.mode,options.scale,options.color,options.lightweight,options.enabled,options.active,options.styleReady,visible,preparer]);
 const display=snapshot.plan.state==='ready'&&(entries.length>0||snapshot.pending>0)&&prepared?.mode===options.mode&&prepared.scale===options.scale&&prepared.color===options.color?prepared:null;
 const phase=snapshot.plan.state!=='ready'?snapshot.plan.state:snapshot.pending?'loading':snapshot.failed?'partial':snapshot.entries.some(e=>e.state==='detail-required')?'detail-required':snapshot.entries.some(e=>e.grid)?'ready':'no-coverage';
 return {snapshot,display,phase,preparationPhase,error,visible,navigating,revision,retry:()=>setRefresh(n=>n+1)};
}

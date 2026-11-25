import {KANSAS_LIDAR_WINDOW,canonicalLidarView,type KansasLidarView} from './kansas-lidar-view';
import {canonicalGroundQuery,type GroundReceipt} from './kansas-ground';
import {terrainCacheExpiry} from './visitor-terrain-cache';
import {readKansasGround} from './kansas-ground-client';
import {readKansasLidarView} from './kansas-lidar-client';
import type {LidarGridMode,TerrainGrid} from './kansas-lidar-grid-layer';
import type {TerrainFootprint} from './terrain-camera';
export type TerrainTile={key:string;bounds:TerrainFootprint;zoom:number};
export type TerrainTilePlan={key:string;tiles:TerrainTile[];state:'ready'|'outside'|'detail-required'};
export type TerrainTileData={tile:TerrainTile;grid:TerrainGrid|null;ground:GroundReceipt|null;native:KansasLidarView|null;state:string;error:string};
const latitude=(y:number)=>Math.atan(Math.sinh(Math.PI*(1-2*y)))*180/Math.PI;
const worldY=(lat:number)=>(1-Math.log(Math.tan(Math.PI/4+lat*Math.PI/360))/Math.PI)/2;
/** Stable, adjoining Web-Mercator tiles cover the ENTIRE visible bounds. A
 * coarser ground level bounds the horizon cost. Native jobs stay below 1 km²;
 * an over-wide view reports detail-required instead of showing a center patch. */
export function terrainTilePlan(bounds:TerrainFootprint,zoom:number,mode:LidarGridMode,lightweight=false):TerrainTilePlan{
 const empty=(state:TerrainTilePlan['state']):TerrainTilePlan=>({key:mode+':'+state,tiles:[],state});
 if(![...bounds,zoom].every(Number.isFinite)||bounds[0]>=bounds[2]||bounds[1]>=bounds[3])return empty('outside');
 const b=[Math.max(bounds[0],KANSAS_LIDAR_WINDOW[0]),Math.max(bounds[1],KANSAS_LIDAR_WINDOW[1]),Math.min(bounds[2],KANSAS_LIDAR_WINDOW[2]),Math.min(bounds[3],KANSAS_LIDAR_WINDOW[3])];
 if(b[0]>=b[2]||b[1]>=b[3])return empty('outside');
 const limit=lightweight?8:12,min=mode==='ground'?4:16;
 for(let z=Math.min(19,Math.max(min,Math.floor(zoom)));z>=min;z--){
  const n=2**z,x0=Math.floor((b[0]+180)/360*n),x1=Math.ceil((b[2]+180)/360*n)-1,y0=Math.floor(worldY(b[3])*n),y1=Math.ceil(worldY(b[1])*n)-1;
  if((x1-x0+1)*(y1-y0+1)>limit)continue;
  const tiles:TerrainTile[]=[];
  for(let y=y0;y<=y1;y++)for(let x=x0;x<=x1;x++)tiles.push({key:`${mode}:${z}/${x}/${y}`,zoom:z,bounds:[x/n*360-180,latitude((y+1)/n),(x+1)/n*360-180,latitude(y/n)]});
  const cx=(b[0]+b[2])/2,cy=(b[1]+b[3])/2;
  tiles.sort((a,c)=>Math.hypot((a.bounds[0]+a.bounds[2])/2-cx,(a.bounds[1]+a.bounds[3])/2-cy)-Math.hypot((c.bounds[0]+c.bounds[2])/2-cx,(c.bounds[1]+c.bounds[3])/2-cy));
  return {key:tiles.map(t=>t.key).sort().join('|'),tiles,state:'ready'};
 }
 return empty('detail-required');
}
export type TerrainTileSnapshot={version:number;plan:TerrainTilePlan;entries:TerrainTileData[];pending:number;failed:number};
type Loader=(tile:TerrainTile,mode:LidarGridMode,signal:AbortSignal,progress:(state:string)=>void,bypass:boolean)=>Promise<TerrainTileData>;
const load:Loader=async(tile,mode,signal,progress,bypass)=>{
 if(mode==='ground'){const q=canonicalGroundQuery(tile.bounds);if(!q)throw Error('Outside Kansas');const ground=await readKansasGround(q,signal,r=>progress(r.state),{bypassCache:bypass});if(ground.state==='processing')throw Error('This source tile is still processing. Refresh this view to retry.');return {tile,ground,native:null,grid:ground.grid,state:ground.state,error:''};}
 const q=canonicalLidarView(tile.bounds,tile.zoom,[mode]);if(!q)throw Error('Outside Kansas');const native=await readKansasLidarView(q,signal,r=>progress(r.state),{bypassCache:bypass});if(native.receipt.state==='processing')throw Error('This source tile is still processing. Refresh this view to retry.');return {tile,ground:null,native,grid:native.grid,state:native.receipt.layers.find(l=>l.kind===mode)?.state??native.receipt.state,error:''};
};
/** Two bounded acquisitions, stable keys, 24 in-memory receipts maximum.
 * Kept jobs survive overlapping pans. Obsolete and hidden jobs are canceled;
 * late completions cannot resurrect retired coverage. Public disk cache is
 * separately bounded by the existing opt-in 8 MiB cache. */
export function createTerrainTileStore(notify:(s:TerrainTileSnapshot)=>void,loader:Loader=load){
 let version=0,plan:TerrainTilePlan={key:'idle',tiles:[],state:'outside'},mode:LidarGridMode='ground',disposed=false,bypass=false;
 const splits=new Map<string,TerrainTile[]>(),expires=new Map<string,number>(),cache=new Map<string,TerrainTileData>(),active=new Map<string,{abort:AbortController;state:string}>();
 const snapshot=()=>({version,plan,entries:plan.tiles.map(t=>cache.get(t.key)).filter((v):v is TerrainTileData=>!!v),pending:plan.tiles.filter(t=>!cache.has(t.key)).length,failed:plan.tiles.filter(t=>cache.get(t.key)?.error).length});
 const emit=()=>{if(!disposed)notify(snapshot());};
 const prune=()=>{const wanted=new Set(plan.tiles.map(t=>t.key));for(const key of cache.keys()){if(cache.size<=24)break;if(!wanted.has(key)){cache.delete(key);expires.delete(key);}}};
 function refine(){
  if(mode==='ground')return;
  // Refine only a bounded source-budget result, never interpolate unsupported
  // surfaces. At most 24 source grids (8 on a lightweight initial plan) share
  // the SAME vertex/FBO budget; each child is still an independently validated
  // complete native request. Stable split keys survive neighboring pans.
  let changed=true;
  while(changed){changed=false;const next:TerrainTile[]=[];let size=plan.tiles.length;
   for(const tile of plan.tiles){
    let children=splits.get(tile.key);
    if(!children&&cache.get(tile.key)?.state==='detail-required'&&tile.zoom<18&&splits.size<64){
     const [west,south,east,north]=tile.bounds,midX=(west+east)/2,midY=latitude((worldY(south)+worldY(north))/2),z=tile.zoom+1,n=2**z;
     children=[[west,midY,midX,north],[midX,midY,east,north],[west,south,midX,midY],[midX,south,east,midY]].map(b=>({key:`${mode}:${z}/${Math.floor(((b[0]+b[2])/2+180)/360*n)}/${Math.floor(worldY((b[1]+b[3])/2)*n)}`,zoom:z,bounds:b as unknown as TerrainFootprint}));
    }
    if(children&&size+3<=24){splits.set(tile.key,children);next.push(...children);size+=3;changed=true;}
    else next.push(tile);
   }
   if(changed)plan={...plan,tiles:next,key:next.map(t=>t.key).sort().join('|')};
  }
 }
 function pump(){
  if(disposed)return;
  for(const tile of plan.tiles){
   if(active.size>=2)break;if(cache.has(tile.key)||active.has(tile.key))continue;
   const job={abort:new AbortController(),state:'loading'};active.set(tile.key,job);const jobMode=mode,skip=bypass;
   void loader(tile,jobMode,job.abort.signal,state=>{if(active.get(tile.key)===job){job.state=state;emit();}},skip).then(data=>{
    if(disposed||job.abort.signal.aborted||active.get(tile.key)!==job)return;
    // Move touched entries to the end of the LRU without changing receipt times.
    version++;cache.delete(tile.key);cache.set(tile.key,data);const receipts=[data.ground?.cache,data.native?.receipt.cache,data.native?.grid?.cache].filter((v):v is {state:'live'|'fresh'|'stale';at:string}=>!!v);expires.set(tile.key,terrainCacheExpiry(receipts)||Date.now()+60000);
   }).catch(error=>{if(!disposed&&!job.abort.signal.aborted&&active.get(tile.key)===job)cache.set(tile.key,{tile,grid:null,ground:null,native:null,state:'unavailable',error:error instanceof Error?error.message:'Tile unavailable'});}).finally(()=>{if(active.get(tile.key)!==job)return;active.delete(tile.key);refine();prune();emit();pump();});
  }
 }
 return {snapshot,set(next:TerrainTilePlan,nextMode:LidarGridMode,refresh=false){
  if(disposed)return;mode=nextMode;plan=next;bypass=refresh;if(refresh)splits.clear();refine();
  const wanted=new Set(plan.tiles.map(t=>t.key));
  for(const [key,job] of active)if(!wanted.has(key)||refresh){active.delete(key);job.abort.abort();}
  if(refresh)for(const key of wanted)cache.delete(key);
  // Reuse only unexpired exact source receipts; no timestamp renewal on a pan.
  for(const key of wanted)if((expires.get(key)??Infinity)<=Date.now()){cache.delete(key);expires.delete(key);}
  prune();emit();pump();
 },pause(){for(const job of active.values())job.abort.abort();active.clear();},dispose(){disposed=true;for(const job of active.values())job.abort.abort();active.clear();cache.clear();expires.clear();splits.clear();}};
}

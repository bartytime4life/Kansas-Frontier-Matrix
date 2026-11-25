import {KANSAS_LIDAR_WINDOW} from './kansas-lidar-view';
import type {TerrainTileSnapshot} from './terrain-viewport-tiles';
import type {LidarGridMode,TerrainGrid} from './kansas-lidar-grid-layer';
import type {TerrainFootprint} from './terrain-camera';
export type CoverageState='supported'|'gaps'|'pending'|'empty'|'closer'|'unavailable';
export const COVERAGE_LABELS:Record<CoverageState,string>={supported:'Supported',gaps:'Gaps in cells',pending:'Pending',empty:'No supported cells',closer:'Closer view needed',unavailable:'Unavailable'};
export type CoverageTile={key:string;number:number;bounds:TerrainFootprint;state:CoverageState;supported:number|null;total:number|null;source:string;acquisition:string;verticalReference:string;checkedAt:string|null;stale:boolean;reason:string};
export type TerrainCoverage={mode:LidarGridMode;tiles:CoverageTile[];bounds:TerrainFootprint|null;counts:Record<CoverageState,number>;supported:number;total:number;checked:number;planState:TerrainTileSnapshot['plan']['state']};
// Receipts and their grid arrays are immutable. Progress updates reuse this
// bounded weak cache instead of rescanning up to 24 grids on each render.
const supportCache=new WeakMap<TerrainGrid,Partial<Record<LidarGridMode,{supported:number;total:number}>>>();
function support(grid:TerrainGrid,mode:LidarGridMode){
 const cached=supportCache.get(grid)??{};if(cached[mode])return cached[mode];
 const values=grid.format==='kfm-3dep-ground-grid-v1'?(mode==='ground'?grid.ground:[]):grid[mode];
 const result={supported:values.reduce<number>((n,z,i)=>n+Number(z!==null&&Number.isFinite(z)&&(mode!=='canopy'||z>=0&&grid.ground[i]!==null)),0),total:values.length};
 cached[mode]=result;supportCache.set(grid,cached);return result;
}
function clipped(bounds:TerrainFootprint):TerrainFootprint|null{
 if(!bounds||bounds.length!==4||!bounds.every(Number.isFinite))return null;
 const b:[number,number,number,number]=[Math.max(bounds[0],KANSAS_LIDAR_WINDOW[0]),Math.max(bounds[1],KANSAS_LIDAR_WINDOW[1]),Math.min(bounds[2],KANSAS_LIDAR_WINDOW[2]),Math.min(bounds[3],KANSAS_LIDAR_WINDOW[3])];
 return b[0]<b[2]&&b[1]<b[3]?b:null;
}
/** Source support in CURRENT requested tiles, not a survey availability atlas,
 * area percentage, rendered mask, or accuracy claim. No provider requests. */
export function terrainCoverage(snapshot:TerrainTileSnapshot,mode:LidarGridMode):TerrainCoverage{
 const entries=new Map(snapshot.entries.map(e=>[e.tile.key,e]));
 const tiles:CoverageTile[]=[];
 for(const tile of snapshot.plan.tiles){
  if(!tile.key?.startsWith(mode+':'))continue;
  const e=entries.get(tile.key),bounds=clipped(e?.ground?.query.bbox??e?.native?.receipt.query.bbox??tile.bounds);if(!bounds)continue;
  const s=e?.grid?support(e.grid,mode):null,layer=e?.native?.receipt.layers.find(l=>l.kind===mode),cache=e?.ground?.cache??e?.native?.grid?.cache??e?.native?.receipt.cache;
  const state:CoverageState=e?.error||e?.state==='unavailable'?'unavailable':s?.supported?s.supported===s.total?'supported':'gaps':e?.state==='detail-required'?'closer':s||e?.state==='no-coverage'||layer?.state==='no-coverage'?'empty':e?'unavailable':'pending';
  const source=e?.grid?.source;
  tiles.push({key:tile.key,number:0,bounds,state,supported:s?.supported??null,total:s?.total??null,source:source?('project' in source?source.project:'USGS 3DEP resampled DEM'):'Source not loaded',acquisition:source?.acquisition??'Not established by this receipt',verticalReference:source?.verticalReference??'Not established by this receipt',checkedAt:cache?.at??null,stale:cache?.state==='stale'||e?.native?.receipt.cache.state==='stale',reason:e?.error||e?.ground?.reason||layer?.message||e?.native?.receipt.reason||COVERAGE_LABELS[state]});
 }
 // Geographic order stays stable as centre-first request priority changes.
 tiles.sort((a,b)=>b.bounds[3]-a.bounds[3]||a.bounds[0]-b.bounds[0]||a.key.localeCompare(b.key));tiles.forEach((t,i)=>{t.number=i+1;});
 const counts={supported:0,gaps:0,pending:0,empty:0,closer:0,unavailable:0};for(const t of tiles)counts[t.state]++;
 return {mode,tiles,bounds:tiles.length?[Math.min(...tiles.map(t=>t.bounds[0])),Math.min(...tiles.map(t=>t.bounds[1])),Math.max(...tiles.map(t=>t.bounds[2])),Math.max(...tiles.map(t=>t.bounds[3]))]:null,counts,supported:tiles.reduce((n,t)=>n+(t.supported??0),0),total:tiles.reduce((n,t)=>n+(t.total??0),0),checked:tiles.filter(t=>t.supported!==null).length,planState:snapshot.plan.state};
}
const y=(lat:number)=>Math.log(Math.tan(Math.PI/4+lat*Math.PI/360));
/** North-up Mercator diagram, same projection as the planned tile grid. */
export function coverageRect(bounds:TerrainFootprint,extent:TerrainFootprint){
 const west=extent[0],north=y(extent[3]),dx=extent[2]-west,dy=north-y(extent[1]),ratio=dx*Math.PI/180/dy;
 const width=Math.min(248,152*ratio),height=Math.min(152,248/ratio),left=(280-width)/2,top=26+(152-height)/2;
 return {x:left+(bounds[0]-west)/dx*width,y:top+(north-y(bounds[3]))/dy*height,width:(bounds[2]-bounds[0])/dx*width,height:(y(bounds[3])-y(bounds[1]))/dy*height};
}

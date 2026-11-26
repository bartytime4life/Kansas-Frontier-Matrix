import {groundCell,groundMercator,type GroundGrid} from './kansas-ground';
import type {TerrainGrid,LidarGridMode} from './kansas-lidar-grid-layer';
import type {TerrainTileData} from './terrain-viewport-tiles';
export type TransectCoordinate=readonly [number,number];
export const TRANSECT_LIMITS={vertices:64,stations:321,tiles:24} as const;
export const TRANSECT_METHOD='Bounded stations along a browser-drawn line; containing source cell, no height interpolation. Distances use a 6371008.8 m sphere and are approximate. Not every crossed cell is sampled. Guides break at missing stations, source tiles and nonadjacent cells. Vertical references are not harmonized; no cross-source slope, gain or fall is calculated. Resampled Ground is not native LiDAR resolution. Display exaggeration is ignored. Scientific accuracy, admission and release remain unverified.';
export type TransectStation={distance:number;coordinate:[number,number];value:number|null;tile:string|null;requestKey:string|null;index:number|null;row:number|null;column:number|null;center:[number,number]|null};
export type TransectSource={tile:string;requestKey:string;source:string;verticalReference:string;acquisition:string;horizontalCrs:string;spacing:number[];spacingUnits:string;hashes:string[];cacheTime:string|null;stale:boolean};
export type TerrainTransect={line:TransectCoordinate[];mode:LidarGridMode;length:number;stations:TransectStation[];sources:TransectSource[];supported:number;error:string|null};
const finite=(v:unknown):v is number=>typeof v==='number'&&Number.isFinite(v);
const rad=Math.PI/180;
function distance(a:TransectCoordinate,b:TransectCoordinate){const dlat=(b[1]-a[1])*rad,dlon=(b[0]-a[0])*rad,h=Math.sin(dlat/2)**2+Math.cos(a[1]*rad)*Math.cos(b[1]*rad)*Math.sin(dlon/2)**2;return 12742017.6*Math.asin(Math.sqrt(Math.min(1,h)));}
function contains(p:TransectCoordinate,b:readonly number[]){return p[0]>=b[0]&&p[0]<=b[2]&&p[1]>=b[1]&&p[1]<=b[3];}
type NativeGrid=Exclude<TerrainGrid,GroundGrid>;
type NativeIndex={bounds:number[];buckets:number[][]};
const nativeIndices=new WeakMap<NativeGrid,NativeIndex>();
function quad(g:NativeGrid,i:number){const k=Math.floor(i/g.width)*(g.width+1)+i%g.width;return [g.cornersWgs84[k],g.cornersWgs84[k+1],g.cornersWgs84[k+g.width+2],g.cornersWgs84[k+g.width+1]];}
function nativeIndex(g:NativeGrid){const cached=nativeIndices.get(g);if(cached)return cached;const xs=g.cornersWgs84.map(p=>p[0]),ys=g.cornersWgs84.map(p=>p[1]),bounds=[Math.min(...xs),Math.min(...ys),Math.max(...xs),Math.max(...ys)],buckets=Array.from({length:256},()=>[] as number[]),bucket=(v:number,a:number,b:number)=>Math.max(0,Math.min(15,Math.floor((v-a)/(b-a)*16)));
 for(let i=0;i<g.width*g.height;i++){const q=quad(g,i),x=q.map(p=>p[0]),y=q.map(p=>p[1]);for(let r=bucket(Math.min(...y),bounds[1],bounds[3]);r<=bucket(Math.max(...y),bounds[1],bounds[3]);r++)for(let c=bucket(Math.min(...x),bounds[0],bounds[2]);c<=bucket(Math.max(...x),bounds[0],bounds[2]);c++)buckets[r*16+c].push(i);}
 const result={bounds,buckets};nativeIndices.set(g,result);return result;
}
/** Geographic cell containment uses validated clockwise source corners, not an
 * assumed north-up WGS84 approximation to the native UTM grid. */
export function transectCell(g:TerrainGrid,p:TransectCoordinate):number|null{
 if(g.format==='kfm-3dep-ground-grid-v1'){const [x,y]=groundMercator(...p),b=g.bounds3857;if(x<b[0]||x>b[2]||y<b[1]||y>b[3])return null;const c=Math.min(g.width-1,Math.floor((x-b[0])/g.cellSize3857[0])),r=Math.min(g.height-1,Math.floor((b[3]-y)/g.cellSize3857[1]));return r*g.width+c;}
 const {bounds:b,buckets}=nativeIndex(g);if(!contains(p,b))return null;const c=Math.min(15,Math.floor((p[0]-b[0])/(b[2]-b[0])*16)),r=Math.min(15,Math.floor((p[1]-b[1])/(b[3]-b[1])*16));
 for(const i of buckets[r*16+c]){const q=quad(g,i);if(q.every((a,k)=>{const b=q[(k+1)%4];return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])<=1e-16;}))return i;}return null;
}
function metadata(e:TerrainTileData):TransectSource{const g=e.grid!,source=g.source,native=g.format==='kfm-lidar-grid-v1';return {tile:e.tile.key,requestKey:g.requestKey,source:native?g.source.project:'USGS 3DEP resampled DEM',verticalReference:source.verticalReference,acquisition:source.acquisition,horizontalCrs:native?g.analysisCrs:g.source.horizontalCrs,spacing:native?g.cellSizeM:g.cellSize3857,spacingUnits:native?'UTM grid metres':'Web Mercator metres; not ground distance or native resolution',hashes:native?g.source.assets.map(a=>a.sha256):[g.source.sha256],cacheTime:e.ground?.cache.at??e.native?.receipt.cache.at??null,stale:e.ground?.cache.state==='stale'||e.native?.receipt.cache.state==='stale'};}
/** At most 321 stations and 24 already validated tiles. No acquisition, worker,
 * GPU or browser-storage allocation; native spatial indices reuse immutable grids. */
export function terrainTransect(line:readonly TransectCoordinate[],entries:readonly TerrainTileData[],mode:LidarGridMode):TerrainTransect{
 const empty=(error:string|null):TerrainTransect=>({line:[],mode,length:0,stations:[],sources:[],supported:0,error});
 if(line.length<2)return empty(null);
 if(line.length>TRANSECT_LIMITS.vertices||line.some(p=>p.length!==2||!p.every(finite)||p[0]<-180||p[0]>180||p[1]<-85||p[1]>85))return empty('Use a line of 2–64 valid map points.');
 const cumulative=[0];for(let i=1;i<line.length;i++)cumulative.push(cumulative[i-1]+distance(line[i-1],line[i]));const length=cumulative.at(-1)!;if(length<.01)return empty('Draw a longer line.');
 const tiles=entries.filter(e=>e.grid&&e.tile.key.startsWith(mode+':')&&e.tile.bounds?.length===4&&(mode==='ground'||e.grid.format==='kfm-lidar-grid-v1')).slice(0,TRANSECT_LIMITS.tiles).sort((a,b)=>a.tile.key.localeCompare(b.tile.key));
 // Include the original bend vertices and 257 distance stations. Coincident
 // vertices collapse; the fixed cap is independent of line length or zoom.
 const distances=[...new Set([...cumulative,...Array.from({length:257},(_,i)=>i*length/256)])].sort((a,b)=>a-b),used=new Set<string>();let segment=1;
 const stations=distances.map(d=>{while(segment<line.length-1&&cumulative[segment]<d)segment++;const a=line[segment-1],b=line[segment],span=cumulative[segment]-cumulative[segment-1],t=span?(d-cumulative[segment-1])/span:0,p:[number,number]=[a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t];
  const missing:TransectStation={distance:d,coordinate:p,value:null,tile:null,requestKey:null,index:null,row:null,column:null,center:null};
  for(const e of tiles){if(!contains(p,e.tile.bounds))continue;const g=e.grid!,i=transectCell(g,p);if(i===null)continue;const value=g.format==='kfm-3dep-ground-grid-v1'?g.ground[i]:g[mode][i];
   // Preserve source identity even for a missing value. Never fall through to
   // an overlapping survey to conceal this source's missing support.
   const valid=finite(value)&&(mode!=='canopy'||value>=0&&finite(g.ground[i]));const q=g.format==='kfm-lidar-grid-v1'?quad(g,i):null,cell=g.format==='kfm-3dep-ground-grid-v1'?groundCell(g,i):null;
   used.add(e.tile.key);return {...missing,value:valid?value:null,tile:e.tile.key,requestKey:g.requestKey,index:i,row:Math.floor(i/g.width)+1,column:i%g.width+1,center:cell?[cell.longitude,cell.latitude] as [number,number]:q?[q.reduce((n,p)=>n+p[0],0)/4,q.reduce((n,p)=>n+p[1],0)/4] as [number,number]:null};
  }return missing;
 });return {line:line.map(p=>[...p]),mode,length,stations,sources:tiles.filter(e=>used.has(e.tile.key)).map(metadata),supported:stations.filter(s=>s.value!==null).length,error:null};
}
export function transectGeometry(profile:TerrainTransect){const values=profile.stations.flatMap(s=>s.value===null?[]:[s.value]),low=values.length?Math.min(...values):0,high=values.length?Math.max(...values):0,points=profile.stations.map(s=>s.value===null?null:{x:12+s.distance/profile.length*296,y:high===low?70:12+(high-s.value)/(high-low)*108}),paths:string[]=[];let path='',previous:TransectStation|null=null;
 profile.stations.forEach((s,i)=>{const p=points[i],joins=previous&&previous.tile===s.tile&&previous.requestKey===s.requestKey&&previous.row!==null&&s.row!==null&&previous.column!==null&&s.column!==null&&Math.abs(previous.row-s.row)<=1&&Math.abs(previous.column-s.column)<=1;
  if(!p||!joins){if(path)paths.push(path);path='';}if(p)path+=(path?'L':'M')+p.x.toFixed(2)+' '+p.y.toFixed(2);previous=p?s:null;
 });if(path)paths.push(path);return {points,paths,low,high};}
export function transectJSON(profile:TerrainTransect){return JSON.stringify({format:'kfm-terrain-transect-v1',mode:profile.mode,units:{height:'source metres, unscaled',distance:'approximate ground metres'},method:TRANSECT_METHOD,review:{scientificAccuracyVerified:false,sourceAdmitted:false,released:false},line:profile.line,lengthM:profile.length,supportedStations:profile.supported,sources:profile.sources,stations:profile.stations},null,2);}

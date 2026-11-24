import {createLidarGeometryLayer,type LidarGeometry,type NativeLayerOptions} from './native-lidar-layer';
import type {LidarAnalysisGrid} from './kansas-lidar-view';
import {MAPLIBRE_EARTH_RADIUS_M} from './native-lidar';
import {groundCorners,type GroundGrid} from './kansas-ground';
import {analyzeGroundGrid,groundColorValues,terrainColorDomain} from './kansas-terrain-analysis';
export const KANSAS_LIDAR_GRID_LAYER='external-kansas-lidar-grid';
export const TERRAIN_GRID_VERTEX_LIMIT=300_000;
export type LidarGridMode='ground'|'surface'|'canopy';
export type TerrainGrid=LidarAnalysisGrid|GroundGrid;
export const gridValues=(grid:TerrainGrid,mode:LidarGridMode):(number|null)[]=>grid.format==='kfm-3dep-ground-grid-v1'?(mode==='ground'?grid.ground:[]):grid[mode];
export function terrainGridDomain(grid:TerrainGrid,mode:LidarGridMode):[number,number]|null{
 const values=(mode==='canopy'?gridValues(grid,mode):grid.format==='kfm-3dep-ground-grid-v1'?grid.ground:[...grid.ground,...grid.surface]).filter((v):v is number=>v!==null&&Number.isFinite(v));
 return values.length?[Math.min(...values),Math.max(...values)]:null;
}
/** Solid display cells. Source tops remain absolute; the shared closure base and
 * walls are visual pedestals, not observed subsurface or vertical cliff faces. */
export function lidarGridGeometry(grid:TerrainGrid,mode:LidarGridMode):LidarGeometry&{closureBaseM:number;domain:[number,number]|null;corners:[number,number][]}{
 const values=gridValues(grid,mode),corners=grid.format==='kfm-3dep-ground-grid-v1'?groundCorners(grid):grid.cornersWgs84;
 const eligible=values.map((value,i)=>value!==null&&Number.isFinite(value)&&(mode!=='canopy'||value>=0&&grid.ground[i]!==null));
 const domain=terrainGridDomain(grid,mode),reference=(grid.format==='kfm-3dep-ground-grid-v1'?grid.ground:[...grid.ground,...grid.surface]).filter((v):v is number=>v!==null&&Number.isFinite(v));
 const low=reference.length?Math.min(...reference):0,high=reference.length?Math.max(...reference):0,closureBaseM=low-Math.max(1,(high-low)*.02);
 const position=(corner:readonly number[],height:number,scale:number):[number,number,number]=>{const lat=corner[1]*Math.PI/180;return [(corner[0]+180)/360,(180-180/Math.PI*Math.log(Math.tan(Math.PI/4+lat/2)))/360,height*scale/(2*Math.PI*MAPLIBRE_EARTH_RADIUS_M*Math.cos(lat))];};
 const top=(i:number)=>mode==='canopy'?grid.ground[i]!+values[i]!:values[i]!;
 const first=eligible.findIndex(Boolean),firstCorner=first<0?0:Math.floor(first/grid.width)*(grid.width+1)+first%grid.width;
 const origin=(scale:number)=>position(corners[firstCorner],first<0?0:top(first),scale);
 const eligibleCount=eligible.filter(Boolean).length;
 const analysis=grid.format==='kfm-3dep-ground-grid-v1'?analyzeGroundGrid(grid):null;
 return {id:KANSAS_LIDAR_GRID_LAYER,triangles:true,vertexLimit:TERRAIN_GRID_VERTEX_LIMIT,sourceCount:grid.width*grid.height,eligibleCount,isEligible:i=>eligible[i]===true,origin,closureBaseM,domain,corners,pack:options=>{
  const colors=grid.format==='kfm-3dep-ground-grid-v1'?groundColorValues(grid,options.gridColor??'height',analysis!):values,colorDomain=options.gridColor&&options.gridColor!=='height'&&grid.format==='kfm-3dep-ground-grid-v1'?terrainColorDomain(colors,options.gridColor)??[0,0]:domain??[0,0];
  const anchor=origin(options.scale),vertices:number[]=[],[min,max]=colorDomain;
  const vertex=(corner:number,z:number,color:readonly number[],id:number)=>{const p=position(corners[corner],z,options.scale);vertices.push(p[0]-anchor[0],p[1]-anchor[1],p[2]-anchor[2],...color,id+1);};
  const face=(indices:number[],heights:number[],color:readonly number[],id:number)=>{for(const k of [0,1,2,0,2,3])vertex(indices[k],heights[k],color,id);};
  const sides=(indices:number[],bottom:number,height:number,color:readonly number[],id:number)=>{if(bottom===height)return;for(let edge=0;edge<4;edge++){const a=indices[edge],b=indices[(edge+1)%4],shade=[.7,.85,.62,.8][edge];face([a,b,b,a],[bottom,bottom,height,height],color.map(v=>v*shade),id);}};
  values.forEach((value,i)=>{
   if(!eligible[i])return;const c=Math.floor(i/grid.width)*(grid.width+1)+i%grid.width,indices=[c,c+grid.width+1,c+grid.width+2,c+1],colorValue=colors[i],t=min===max?.5:Math.max(0,Math.min(1,((colorValue??min)-min)/(max-min))),color=colorValue===null?[.38,.44,.46]:grid.format==='kfm-3dep-ground-grid-v1'&&options.gridColor==='local-relief'?(t<=.5?[.18+(.65-.18)*t*2,.45+(.69-.45)*t*2,.76+(.65-.76)*t*2]:[.65+(.98-.65)*(t-.5)*2,.69+(.85-.69)*(t-.5)*2,.65+(.24-.65)*(t-.5)*2]):[.18+.8*t,.45+.4*t,.76-.52*t],height=top(i);
   face(indices,[height,height,height,height],color,i);
   if(mode==='canopy'){sides(indices,closureBaseM,grid.ground[i]!,[.29,.39,.35],i);sides(indices,grid.ground[i]!,height,color,i);}else sides(indices,closureBaseM,height,color,i);
  });
  if(vertices.length/7>TERRAIN_GRID_VERTEX_LIMIT)throw Error('Terrain cell geometry budget exceeded');
  return Float32Array.from(vertices);
 }};
}
export function createLidarGridLayer(grid:TerrainGrid,mode:LidarGridMode,settings:NativeLayerOptions,report:(message:string)=>void){return createLidarGeometryLayer(lidarGridGeometry(grid,mode),settings,report);}

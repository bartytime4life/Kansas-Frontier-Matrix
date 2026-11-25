import type {PreparedTerrain} from './terrain-preparation-model';
import {createLidarGeometryLayer,type LidarGeometry,type NativeLayerOptions} from './native-lidar-layer';
import type {LidarAnalysisGrid} from './kansas-lidar-view';
import {MAPLIBRE_EARTH_RADIUS_M,terrainHeightColor,terrainReliefColor} from './native-lidar';
import {groundCorners,type GroundGrid} from './kansas-ground';
import {analyzeGroundGrid,groundColorValues,terrainColorDomain,terrainGradients,terrainIllumination} from './kansas-terrain-analysis';
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
export function lidarGridGeometry(grid:TerrainGrid,mode:LidarGridMode,prepared?:ReturnType<typeof analyzeGroundGrid>|null,display?:{stride:number;domain:[number,number]|null;closureBaseM:number}):LidarGeometry&{closureBaseM:number;domain:[number,number]|null;corners:[number,number][]}{
 const values=gridValues(grid,mode),corners=grid.format==='kfm-3dep-ground-grid-v1'?groundCorners(grid):grid.cornersWgs84;
 const supported=values.map((value,i)=>value!==null&&Number.isFinite(value)&&(mode!=='canopy'||value>=0&&grid.ground[i]!==null));
 const stride=display?.stride??1,eligible=supported.map(()=>false),blocks=new Map<number,{row:number;col:number;endRow:number;endCol:number}>(),blockAt=new Map<string,number>();
 for(let row=0;row<grid.height;row+=stride)for(let col=0;col<grid.width;col+=stride){
  const endRow=Math.min(grid.height,row+stride),endCol=Math.min(grid.width,col+stride),i=Math.floor((row+endRow-1)/2)*grid.width+Math.floor((col+endCol-1)/2);
  // Every cell in the display footprint must be supported. The representative
  // is an exact source sample; downsampling cannot paint over NoData holes.
  let full=true;for(let y=row;y<endRow;y++)for(let x=col;x<endCol;x++)if(!supported[y*grid.width+x])full=false;
  if(full){eligible[i]=true;blocks.set(i,{row,col,endRow,endCol});blockAt.set(row+','+col,i);}
 }
 const domain=display?.domain??terrainGridDomain(grid,mode),reference=(grid.format==='kfm-3dep-ground-grid-v1'?grid.ground:[...grid.ground,...grid.surface]).filter((v):v is number=>v!==null&&Number.isFinite(v));
 const low=reference.length?Math.min(...reference):0,high=reference.length?Math.max(...reference):0,closureBaseM=display?.closureBaseM??low-Math.max(1,(high-low)*.02);
 const projected=corners.map(corner=>{const lat=corner[1]*Math.PI/180;return [(corner[0]+180)/360,(180-180/Math.PI*Math.log(Math.tan(Math.PI/4+lat/2)))/360,1/(2*Math.PI*MAPLIBRE_EARTH_RADIUS_M*Math.cos(lat))];});
 const position=(corner:number,height:number,scale:number):[number,number,number]=>[projected[corner][0],projected[corner][1],height*scale*projected[corner][2]];
 const top=(i:number)=>mode==='canopy'?grid.ground[i]!+values[i]!:values[i]!;
 const first=eligible.findIndex(Boolean),firstCorner=first<0?0:Math.floor(first/grid.width)*(grid.width+1)+first%grid.width;
 const origin=(scale:number)=>position(firstCorner,first<0?0:top(first),scale);
 const eligibleCount=eligible.filter(Boolean).length;
 const analysis=grid.format==='kfm-3dep-ground-grid-v1'?prepared??analyzeGroundGrid(grid):null;
 const gradients=mode==='canopy'?null:analysis?.gradients??(grid.format==='kfm-lidar-grid-v1'?terrainGradients(values,grid.width,grid.height,()=>grid.cellSizeM):null);
 return {id:KANSAS_LIDAR_GRID_LAYER,triangles:true,vertexLimit:TERRAIN_GRID_VERTEX_LIMIT,sourceCount:grid.width*grid.height,eligibleCount,isEligible:i=>eligible[i]===true,origin,closureBaseM,domain,corners,pack:options=>{
  const colors=grid.format==='kfm-3dep-ground-grid-v1'?groundColorValues(grid,options.gridColor??'height',analysis!):values,colorDomain=display?.domain??(options.gridColor&&options.gridColor!=='height'&&grid.format==='kfm-3dep-ground-grid-v1'?terrainColorDomain(colors,options.gridColor)??[0,0]:domain??[0,0]);
  const anchor=origin(options.scale),vertices=new Float32Array(eligibleCount*(mode==='canopy'?54:30)*7),[min,max]=colorDomain;let cursor=0;
  const vertex=(corner:number,z:number,color:readonly number[],id:number)=>{const p=position(corner,z,options.scale);vertices[cursor++]=p[0]-anchor[0];vertices[cursor++]=p[1]-anchor[1];vertices[cursor++]=p[2]-anchor[2];vertices[cursor++]=color[0];vertices[cursor++]=color[1];vertices[cursor++]=color[2];vertices[cursor++]=id+1;};
  const face=(indices:number[],heights:number[],color:readonly number[],id:number)=>{for(const k of [0,1,2,0,2,3])vertex(indices[k],heights[k],color,id);};
  const side=(indices:number[],edge:number,bottom:number,height:number,color:readonly number[],id:number)=>{if(bottom>=height)return;const a=indices[edge],b=indices[(edge+1)%4],shade=[.7,.85,.62,.8][edge];face([a,b,b,a],[bottom,bottom,height,height],color.map(v=>v*shade),id);};
  values.forEach((value,i)=>{
   if(!eligible[i])return;const block=blocks.get(i)!,{row,col,endRow,endCol}=block,indices=[row*(grid.width+1)+col,endRow*(grid.width+1)+col,endRow*(grid.width+1)+endCol,row*(grid.width+1)+endCol],colorValue=colors[i],t=min===max?.5:Math.max(0,Math.min(1,((colorValue??min)-min)/(max-min))),color=colorValue===null?[.38,.44,.46]:grid.format==='kfm-3dep-ground-grid-v1'&&options.gridColor==='local-relief'?terrainReliefColor(t):terrainHeightColor(t),height=top(i);
   face(indices,[height,height,height,height],color.map(v=>v*(gradients?terrainIllumination(gradients[i]):1)),i);
   // Emit only the exposed height interval. Adjacent cells must not carry two
   // coplanar full-depth walls: that duplicates hidden faces and causes z-fighting.
   const neighbors=[[row,col-stride],[row+stride,col],[row,col+stride],[row-stride,col]].map(([r,c])=>blockAt.get(r+','+c)??-1);
   neighbors.forEach((neighbor,edge)=>{const bottom=neighbor>=0&&eligible[neighbor]?Math.max(closureBaseM,top(neighbor)):closureBaseM;
    if(mode==='canopy'){side(indices,edge,bottom,Math.min(grid.ground[i]!,height),[.29,.39,.35],i);side(indices,edge,Math.max(bottom,grid.ground[i]!),height,color,i);}
    else side(indices,edge,bottom,height,color,i);
   });
  });
  if(cursor>vertices.length||cursor/7>TERRAIN_GRID_VERTEX_LIMIT)throw Error('Terrain cell geometry budget exceeded');
  return vertices.subarray(0,cursor);
 }};
}
export function createLidarGridLayer(grid:TerrainGrid,mode:LidarGridMode,settings:NativeLayerOptions,report:(message:string)=>void,prepared?:ReturnType<typeof analyzeGroundGrid>|null){return createLidarGeometryLayer(lidarGridGeometry(grid,mode,prepared),settings,report);}

/** Install worker-prepared vertices atomically; source values/IDs remain unchanged. */
export function createPreparedLidarGridLayer(prepared:PreparedTerrain,settings:NativeLayerOptions,report:(message:string)=>void){
 return createLidarGeometryLayer({id:KANSAS_LIDAR_GRID_LAYER,triangles:true,vertexLimit:TERRAIN_GRID_VERTEX_LIMIT,eligibleCount:prepared.eligibleCount,sourceCount:prepared.sourceCount,origin:()=>[...prepared.origin],isEligible:i=>prepared.eligible[i]===1,pack:options=>{if(options.scale!==prepared.settings.scale||(options.gridColor??'height')!==prepared.settings.color)throw Error('Terrain preparation no longer matches the display settings');return prepared.packed;}},settings,report);
}

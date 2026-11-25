import {lidarGridGeometry,terrainGridDomain,TERRAIN_GRID_VERTEX_LIMIT,type TerrainGrid,type LidarGridMode} from './kansas-lidar-grid-layer';
import {analyzeGroundGrid,groundColorValues,terrainColorDomain,type GroundColor} from './kansas-terrain-analysis';
export const TERRAIN_PREPARATION_MAX_BYTES=TERRAIN_GRID_VERTEX_LIMIT*7*4;
export type TerrainAnalysis=ReturnType<typeof analyzeGroundGrid>;
export type TerrainPreparationInput={grid:TerrainGrid;mode:LidarGridMode;scale:number;color:GroundColor;analysis?:TerrainAnalysis|null;tiles?:{key:string;grid:TerrainGrid}[];lightweight?:boolean};
export type PreparedTerrain={packed:Float32Array;origin:[number,number,number];eligible:Uint8Array;eligibleCount:number;sourceCount:number;analysis:TerrainAnalysis|null;settings:{mode:LidarGridMode;scale:number;color:GroundColor};tiles?:{key:string;start:number;count:number}[];domain?:[number,number]|null;stride?:number;analyses?:(TerrainAnalysis|null)[]};
export type TerrainPreparationRequest=TerrainPreparationInput&{id:number};
export type TerrainPreparationReply={id:number;result:PreparedTerrain}|{id:number;error:string};
/** Runs only in the dedicated worker. Reuses the scientific math and packing verbatim. */
export function prepareTerrain(request:TerrainPreparationRequest):PreparedTerrain{
 if(request.tiles)return prepareMosaic(request);
 const {grid,mode,scale,color}=request,count=validatePreparation(request);
 const analysis=grid.format==='kfm-3dep-ground-grid-v1'?(request.analysis??analyzeGroundGrid(grid)):null,geometry=lidarGridGeometry(grid,mode,analysis),packed=geometry.pack({scale,color:'elevation',gridColor:color,size:3,selected:null}),eligible=Uint8Array.from({length:count},(_,i)=>Number(geometry.isEligible(i)));
 if(packed.buffer.byteLength>TERRAIN_PREPARATION_MAX_BYTES||packed.length%7)throw Error('Terrain preparation exceeds its geometry budget');
 return {packed,origin:geometry.origin(scale),eligible,eligibleCount:geometry.eligibleCount,sourceCount:count,analysis,settings:{mode,scale,color}};
}

/** One shared GPU buffer/framebuffer for all adjoining source grids. Display LOD
 * chooses exact source samples and refuses blocks containing any NoData. */
function prepareMosaic(request:TerrainPreparationRequest):PreparedTerrain{
 const tiles=request.tiles!;
 if(!Array.isArray(tiles)||!tiles.length||tiles.length>(request.mode==='ground'?12:24)||new Set(tiles.map(t=>t.key)).size!==tiles.length)throw Error('Unsupported terrain tile count');
 const count=tiles.reduce((n,t)=>n+t.grid.width*t.grid.height,0),factor=request.mode==='canopy'?54:30;
 const target=Math.floor((request.lightweight?150000:TERRAIN_GRID_VERTEX_LIMIT)/factor*.85),stride=Math.max(1,Math.ceil(Math.sqrt(count/target)));
 let low=Infinity,high=-Infinity,colorLow=Infinity,colorHigh=-Infinity;
 for(const tile of tiles){
  if(typeof tile.key!=='string'||tile.key.length>100)throw Error('Invalid terrain tile');
  const grid=tile.grid; // Validate each bounded grid with the same source path.
  if(grid.width>96||grid.height>96||grid.width<1||grid.height<1||grid.ground.length!==grid.width*grid.height)throw Error('Invalid terrain grid');
  for(const z of grid.ground)if(z!==null){low=Math.min(low,z);high=Math.max(high,z);}
  if(grid.format==='kfm-lidar-grid-v1')for(const z of grid.surface)if(z!==null){low=Math.min(low,z);high=Math.max(high,z);}
  const domain=terrainGridDomainForMosaic(grid,request.mode,request.color);
  if(domain){colorLow=Math.min(colorLow,domain[0]);colorHigh=Math.max(colorHigh,domain[1]);}
 }
 const domain:NumberPair|null=Number.isFinite(colorLow)?[colorLow,colorHigh]:null,closureBaseM=Number.isFinite(low)?low-Math.max(1,(high-low)*.02):0;
 const analyses:(TerrainAnalysis|null)[]=[],parts:Float32Array[]=[],ranges:{key:string;start:number;count:number}[]=[],eligible=new Uint8Array(count);
 let origin:[number,number,number]|null=null,offset=0,length=0,eligibleCount=0;
 for(const tile of tiles){
  validatePreparation({...request,grid:tile.grid,tiles:undefined});
  const analysis=tile.grid.format==='kfm-3dep-ground-grid-v1'?analyzeGroundGrid(tile.grid):null;analyses.push(analysis);
  const geometry=lidarGridGeometry(tile.grid,request.mode,analysis,{stride,domain,closureBaseM});
  const localOrigin=geometry.origin(request.scale),packed=geometry.pack({scale:request.scale,color:'elevation',gridColor:request.color,size:3,selected:null});
  origin??=localOrigin;
  for(let i=0;i<packed.length;i+=7){packed[i]+=localOrigin[0]-origin[0];packed[i+1]+=localOrigin[1]-origin[1];packed[i+2]+=localOrigin[2]-origin[2];packed[i+6]+=offset;}
  const n=tile.grid.width*tile.grid.height;for(let i=0;i<n;i++)if(geometry.isEligible(i)){eligible[offset+i]=1;eligibleCount++;}
  ranges.push({key:tile.key,start:offset,count:n});offset+=n;length+=packed.length;
  if(length/7>TERRAIN_GRID_VERTEX_LIMIT)throw Error('Terrain mosaic exceeds its shared geometry budget');
  parts.push(packed);
 }
 const packed=new Float32Array(length);let cursor=0;for(const part of parts){packed.set(part,cursor);cursor+=part.length;}
 return {packed,origin:origin!,eligible,eligibleCount,sourceCount:count,analysis:null,settings:{mode:request.mode,scale:request.scale,color:request.color},tiles:ranges,domain,stride,analyses};
}
type NumberPair=[number,number];
function terrainGridDomainForMosaic(grid:TerrainGrid,mode:LidarGridMode,color:GroundColor):NumberPair|null{
 if(grid.format==='kfm-3dep-ground-grid-v1'&&color!=='height')return terrainColorDomain(groundColorValues(grid,color,analyzeGroundGrid(grid)),color);
 return terrainGridDomain(grid,mode);
}

function validatePreparation(request:TerrainPreparationRequest){
 const {grid,mode,scale,color}=request,count=grid?.width*grid?.height;
 if(!Number.isSafeInteger(request.id)||request.id<1||!grid||!['kfm-3dep-ground-grid-v1','kfm-lidar-grid-v1'].includes(grid.format)||!Number.isInteger(grid.width)||!Number.isInteger(grid.height)||grid.width<1||grid.height<1||grid.width>96||grid.height>96||count>9216||grid.ground.length!==count||!['ground','surface','canopy'].includes(mode)||grid.format==='kfm-3dep-ground-grid-v1'&&mode!=='ground'||!Number.isFinite(scale)||scale<.1||scale>5||!['height','slope','local-relief'].includes(color))throw Error('Unsupported terrain preparation request');
 return count;
}

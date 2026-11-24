import {lidarGridGeometry,TERRAIN_GRID_VERTEX_LIMIT,type TerrainGrid,type LidarGridMode} from './kansas-lidar-grid-layer';
import {analyzeGroundGrid,type GroundColor} from './kansas-terrain-analysis';
export const TERRAIN_PREPARATION_MAX_BYTES=TERRAIN_GRID_VERTEX_LIMIT*7*4;
export type TerrainAnalysis=ReturnType<typeof analyzeGroundGrid>;
export type TerrainPreparationInput={grid:TerrainGrid;mode:LidarGridMode;scale:number;color:GroundColor;analysis?:TerrainAnalysis|null};
export type PreparedTerrain={packed:Float32Array;origin:[number,number,number];eligible:Uint8Array;eligibleCount:number;sourceCount:number;analysis:TerrainAnalysis|null;settings:{mode:LidarGridMode;scale:number;color:GroundColor}};
export type TerrainPreparationRequest=TerrainPreparationInput&{id:number};
export type TerrainPreparationReply={id:number;result:PreparedTerrain}|{id:number;error:string};
/** Runs only in the dedicated worker. Reuses the scientific math and packing verbatim. */
export function prepareTerrain(request:TerrainPreparationRequest):PreparedTerrain{
 const {grid,mode,scale,color}=request,count=grid?.width*grid?.height;
 if(!Number.isSafeInteger(request.id)||request.id<1||!grid||!['kfm-3dep-ground-grid-v1','kfm-lidar-grid-v1'].includes(grid.format)||!Number.isInteger(grid.width)||!Number.isInteger(grid.height)||grid.width<1||grid.height<1||grid.width>96||grid.height>96||count>9216||grid.ground.length!==count||!['ground','surface','canopy'].includes(mode)||grid.format==='kfm-3dep-ground-grid-v1'&&mode!=='ground'||!Number.isFinite(scale)||scale<.1||scale>5||!['height','slope','local-relief'].includes(color))throw Error('Unsupported terrain preparation request');
 const analysis=grid.format==='kfm-3dep-ground-grid-v1'?(request.analysis??analyzeGroundGrid(grid)):null,geometry=lidarGridGeometry(grid,mode,analysis),packed=geometry.pack({scale,color:'elevation',gridColor:color,size:3,selected:null}),eligible=Uint8Array.from({length:count},(_,i)=>Number(geometry.isEligible(i)));
 if(packed.buffer.byteLength>TERRAIN_PREPARATION_MAX_BYTES||packed.length%7)throw Error('Terrain preparation exceeds its geometry budget');
 return {packed,origin:geometry.origin(scale),eligible,eligibleCount:geometry.eligibleCount,sourceCount:count,analysis,settings:{mode,scale,color}};
}

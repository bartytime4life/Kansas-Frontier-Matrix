import {createLidarGeometryLayer,type LidarGeometry,type NativeLayerOptions} from './native-lidar-layer';
import type {LidarAnalysisGrid} from './kansas-lidar-view';
import {MAPLIBRE_EARTH_RADIUS_M} from './native-lidar';
export const KANSAS_LIDAR_GRID_LAYER='external-kansas-lidar-grid';
export type LidarGridMode='ground'|'surface'|'canopy';
/** Each displayed quad is exactly one qualified analysis cell. Adjacent cells
 * are never bridged across missing support. Canopy uses that cell's own ground. */
export function lidarGridGeometry(grid:LidarAnalysisGrid,mode:LidarGridMode):LidarGeometry{
  const values=grid[mode],eligible=values.map((value,i)=>value!==null&&(mode!=='canopy'||grid.ground[i]!==null));
  const sourceValues=values.filter((v):v is number=>v!==null),low=Math.min(...sourceValues),high=Math.max(...sourceValues);
  const position=(corner:readonly number[],height:number,scale:number):[number,number,number]=>{const lat=corner[1]*Math.PI/180;return [(corner[0]+180)/360,(180-180/Math.PI*Math.log(Math.tan(Math.PI/4+lat/2)))/360,height*scale/(2*Math.PI*MAPLIBRE_EARTH_RADIUS_M*Math.cos(lat))];};
  const height=(i:number)=>mode==='canopy'?grid.ground[i]!+grid.canopy[i]!:values[i]!;
  const first=eligible.findIndex(Boolean),firstCorner=first<0?0:Math.floor(first/grid.width)*(grid.width+1)+first%grid.width;
  const origin=(scale:number)=>position(grid.cornersWgs84[firstCorner],first<0?0:height(first),scale);
  return {id:KANSAS_LIDAR_GRID_LAYER,triangles:true,sourceCount:values.length,eligibleCount:eligible.filter(Boolean).length,isEligible:i=>eligible[i]===true,origin,pack:options=>{
    const anchor=origin(options.scale),packed=new Float32Array(eligible.filter(Boolean).length*6*7);let offset=0;
    values.forEach((value,i)=>{if(!eligible[i])return;const c=Math.floor(i/grid.width)*(grid.width+1)+i%grid.width,corners=[c,c+grid.width+1,c+1,c+1,c+grid.width+1,c+grid.width+2],t=low===high?.5:(value!-low)/(high-low),color=[.18+.8*t,.45+.4*t,.76-.52*t];for(const corner of corners){const pos=position(grid.cornersWgs84[corner],height(i),options.scale);packed.set([pos[0]-anchor[0],pos[1]-anchor[1],pos[2]-anchor[2],...color,i+1],offset);offset+=7;}});return packed;
  }};
}
export function createLidarGridLayer(grid:LidarAnalysisGrid,mode:LidarGridMode,settings:NativeLayerOptions,report:(message:string)=>void){return createLidarGeometryLayer(lidarGridGeometry(grid,mode),settings,report);}

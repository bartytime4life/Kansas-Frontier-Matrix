import {groundCell} from './kansas-ground';
import {groundMetricScale} from './kansas-terrain-analysis';
import type {TerrainGrid,LidarGridMode} from './kansas-lidar-grid-layer';
import type {TerrainAnalysis} from './terrain-preparation-model';
/** A query key alone cannot bind a reading: immutable grid and drawn mask must match. */
export type TerrainInsightBinding={key:string;grid:TerrainGrid;mode:LidarGridMode;eligible:Uint8Array;start:number;analysis:TerrainAnalysis|null};
export type TerrainInsights={binding:TerrainInsightBinding;count:number;low:{index:number;value:number}|null;high:{index:number;value:number}|null;steepest:{index:number;value:number}|null;span:number|null};
export type TerrainRowProfile={row:number;values:(number|null)[];drawn:boolean[];indices:number[];distances:number[];distance:number;low:number|null;high:number|null;units:'approximate ground metres'|'UTM grid metres';mode:LidarGridMode};
const finite=(value:unknown):value is number=>typeof value==='number'&&Number.isFinite(value);
export function insightEligible(binding:TerrainInsightBinding,index:number){return Number.isInteger(index)&&index>=0&&index<binding.grid.width*binding.grid.height&&binding.eligible[binding.start+index]===1;}
export function sameInsightBinding(a:TerrainInsightBinding|null,b:TerrainInsightBinding|null){return !!a&&!!b&&a.key===b.key&&a.grid===b.grid&&a.mode===b.mode&&a.eligible===b.eligible&&a.start===b.start;}
export function terrainSourceValue(binding:TerrainInsightBinding,index:number):number|null{
 const {grid,mode}=binding;if(grid.format==='kfm-3dep-ground-grid-v1'&&mode!=='ground')throw Error('Terrain insight quantity does not match its Ground source');
 if(!Number.isInteger(index)||index<0||index>=grid.width*grid.height)return null;
 const value=grid.format==='kfm-3dep-ground-grid-v1'?grid.ground[index]:grid[mode][index];
 return finite(value)&&(mode!=='canopy'||value>=0&&finite(grid.ground[index]))?value:null;
}
export function terrainInsightValue(binding:TerrainInsightBinding,index:number):number|null{return insightEligible(binding,index)?terrainSourceValue(binding,index):null;}

/** One <=96² scan per immutable tile/mode/mask, never a whole-view statistic. */
export function readTerrainInsights(binding:TerrainInsightBinding):TerrainInsights{
 if(binding.grid.format==='kfm-3dep-ground-grid-v1'&&binding.mode!=='ground')throw Error('Terrain insight quantity does not match its Ground source');
 const size=binding.grid.width*binding.grid.height;if(size>9216||binding.grid.width>96||binding.grid.height>96)throw Error('Terrain insight source exceeds its bounded grid');
 let count=0,low:TerrainInsights['low']=null,high:TerrainInsights['high']=null,steepest:TerrainInsights['steepest']=null;
 for(let index=0;index<size;index++){const value=terrainInsightValue(binding,index);if(value===null)continue;count++;
  if(!low||value<low.value)low={index,value};if(!high||value>high.value)high={index,value};
  const slope=binding.grid.format==='kfm-3dep-ground-grid-v1'&&binding.mode==='ground'?binding.analysis?.slope[index]:null;
  if(finite(slope)&&(!steepest||slope>steepest.value))steepest={index,value:slope};
 }
 return {binding,count,low,high,steepest,span:low&&high?high.value-low.value:null};
}
export function insightCellCenter(binding:TerrainInsightBinding,index:number):[number,number]|null{
 if(!insightEligible(binding,index))return null;const {grid}=binding;
 if(grid.format==='kfm-3dep-ground-grid-v1'){const cell=groundCell(grid,index);return cell?[cell.longitude,cell.latitude]:null;}
 const row=Math.floor(index/grid.width),col=index%grid.width,i=row*(grid.width+1)+col,corners=[grid.cornersWgs84[i],grid.cornersWgs84[i+1],grid.cornersWgs84[i+grid.width+1],grid.cornersWgs84[i+grid.width+2]];
 return corners.every(point=>point?.length===2&&point.every(finite))?[corners.reduce((sum,p)=>sum+p[0],0)/4,corners.reduce((sum,p)=>sum+p[1],0)/4]:null;
}
/** Supported source row, including unrendered LOD samples. Navigation stays drawn-only. */
export function terrainRowProfile(binding:TerrainInsightBinding,row:number):TerrainRowProfile|null{
 const {grid}=binding;if(grid.format==='kfm-3dep-ground-grid-v1'&&binding.mode!=='ground')throw Error('Terrain insight quantity does not match its Ground source');if(!Number.isInteger(row)||row<0||row>=grid.height||grid.width>96)return null;
 const latitude=grid.format==='kfm-3dep-ground-grid-v1'?groundCell(grid,row*grid.width)!.latitude:0,spacing=grid.format==='kfm-3dep-ground-grid-v1'?grid.cellSize3857[0]*groundMetricScale(latitude)[0]:grid.cellSizeM[0];
 const values=Array.from({length:grid.width},(_,column)=>terrainSourceValue(binding,row*grid.width+column)),drawn=values.map((value,column)=>value!==null&&insightEligible(binding,row*grid.width+column)),indices=values.flatMap((value,column)=>value===null||!drawn[column]?[]:[row*grid.width+column]),distances=values.map((_,column)=>column*spacing),valid=values.filter(finite);
 return {row,values,drawn,indices,distances,distance:distances.at(-1)??0,low:valid.length?Math.min(...valid):null,high:valid.length?Math.max(...valid):null,units:grid.format==='kfm-3dep-ground-grid-v1'?'approximate ground metres':'UTM grid metres',mode:binding.mode};
}
/** Independent contiguous paths and dots preserve holes and isolated samples. */
export function terrainProfileGeometry(profile:TerrainRowProfile,width=280,height=100){
 const low=profile.low??0,high=profile.high??0,range=high-low,padding=8;
 const points=profile.values.map((value,column)=>value===null?null:{column,x:padding+(profile.values.length<2?0:column/(profile.values.length-1))*(width-padding*2),y:range===0?height/2:padding+(high-value)/range*(height-padding*2),value});
 const paths:string[]=[];let path='';for(const point of points){if(point){path+=(path?'L':'M')+point.x.toFixed(2)+' '+point.y.toFixed(2);}else if(path){paths.push(path);path='';}}if(path)paths.push(path);return {points,paths};
}

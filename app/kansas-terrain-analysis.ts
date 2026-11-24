import {groundCell,parseGroundReceipt,type GroundGrid,type GroundReceipt} from './kansas-ground';
export type GroundColor='height'|'slope'|'local-relief';
export const TERRAIN_ANALYSIS_RECIPE={height:'Unscaled decoded provider F32 elevation in metres',slope:{method:'Horn 3x3',units:'degrees',window:3,nulls:'All nine cells required',spacing:'Local WGS84 ellipsoid east/north factors for EPSG:3857 at center-row latitude',a:6378137,e2:0.0066943799901413165},localRelief:{method:'Center elevation minus unweighted full 7x7 box mean',units:'metres',window:7,nulls:'All 49 cells required'},localReliefColor:'Symmetric [-maxAbs,+maxAbs], zero centered; flat zero uses neutral color and [0,0] legend',scope:'Derivatives of the resampled output grid, not native survey resolution or archaeological evidence'} as const;
/** Local ellipsoidal distances per EPSG:3857 projected metre, not common x/y scale. */
export function groundMetricScale(latitude:number):[number,number]{const phi=latitude*Math.PI/180,s=Math.sin(phi),d=1-.0066943799901413165*s*s,c=Math.cos(phi);return [c/Math.sqrt(d),(1-.0066943799901413165)*c/Math.pow(d,1.5)];}
export function analyzeGroundGrid(grid:GroundGrid){
 const {width:w,height:h,ground:z}=grid,slope:(number|null)[]=new Array(w*h).fill(null),localRelief:(number|null)[]=new Array(w*h).fill(null);
 for(let row=0;row<h;row++){
  const cell=groundCell(grid,row*w)!,metric=groundMetricScale(cell.latitude),dx=grid.cellSize3857[0]*metric[0],dy=grid.cellSize3857[1]*metric[1];
  for(let col=0;col<w;col++){
   const index=row*w+col;if(z[index]===null)continue;
   if(row>0&&row<h-1&&col>0&&col<w-1){const a=[z[index-w-1],z[index-w],z[index-w+1],z[index-1],z[index],z[index+1],z[index+w-1],z[index+w],z[index+w+1]];if(a.every((v):v is number=>v!==null)){const x=(a[2]+2*a[5]+a[8]-a[0]-2*a[3]-a[6])/(8*dx),y=(a[0]+2*a[1]+a[2]-a[6]-2*a[7]-a[8])/(8*dy);slope[index]=Math.atan(Math.hypot(x,y))*180/Math.PI;}}
   if(row>=3&&row<h-3&&col>=3&&col<w-3){let sum=0,valid=true;for(let r=-3;r<=3;r++)for(let c=-3;c<=3;c++){const value=z[index+r*w+c];if(value===null)valid=false;else sum+=value;}if(valid)localRelief[index]=z[index]!-sum/49;}
  }
 }
 return {slope,localRelief};
}
export function groundColorValues(grid:GroundGrid,color:GroundColor,analysis=analyzeGroundGrid(grid)):(number|null)[]{return color==='slope'?analysis.slope:color==='local-relief'?analysis.localRelief:grid.ground;}
export function terrainColorDomain(values:readonly (number|null)[],color:GroundColor):[number,number]|null{
 const finite=values.filter((v):v is number=>v!==null&&Number.isFinite(v));if(!finite.length)return null;
 if(color==='local-relief'){const extent=Math.max(...finite.map(Math.abs));return extent===0?[0,0]:[-extent,extent];}
 return [Math.min(...finite),Math.max(...finite)];
}
export function terrainStudyJSON(receipt:GroundReceipt){
 const validated=parseGroundReceipt(receipt,receipt.query,receipt.requestKey);if(!validated?.grid)throw Error('No validated Ground grid to export');
 return JSON.stringify({format:'kfm-terrain-study-v1',source:validated,recipe:TERRAIN_ANALYSIS_RECIPE,derived:analyzeGroundGrid(validated.grid),limits:'Display grid analysis only. No cultural, archaeological or certified field-accuracy inference.'},null,2);
}

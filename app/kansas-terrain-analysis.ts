import {groundCell,parseGroundReceipt,type GroundGrid,type GroundReceipt} from './kansas-ground';
export type GroundColor='height'|'slope'|'local-relief';
export const TERRAIN_ANALYSIS_RECIPE={height:'Unscaled decoded provider F32 elevation in metres',slope:{method:'Horn 3x3',units:'degrees',window:3,nulls:'All nine cells required',spacing:'Local WGS84 ellipsoid east/north factors for EPSG:3857 at center-row latitude',a:6378137,e2:0.0066943799901413165},localRelief:{method:'Center elevation minus unweighted full 7x7 box mean',units:'metres',window:7,nulls:'All 49 cells required'},localReliefColor:'Symmetric [-maxAbs,+maxAbs], zero centered; flat zero uses neutral color and [0,0] legend',illumination:{method:'Supported Horn3x3 normals; fixed northwest grid light at 45 degrees',ambient:.55,diffuse:.45,unsupported:.82,heights:'Unscaled; independent of visual relief',nativeSpacing:'Native UTM grid metres; projection scale/registration not independently validated'},scope:'Derivatives of the resampled output grid, not native survey resolution or archaeological evidence'} as const;
/** Local ellipsoidal distances per EPSG:3857 projected metre, not common x/y scale. */
export function groundMetricScale(latitude:number):[number,number]{const phi=latitude*Math.PI/180,s=Math.sin(phi),d=1-.0066943799901413165*s*s,c=Math.cos(phi);return [c/Math.sqrt(d),(1-.0066943799901413165)*c/Math.pow(d,1.5)];}
export type TerrainGradient={east:number;north:number}|null;
/** Complete Horn support only. Rows run north to south; Y derivative is northward. */
export function terrainGradients(z:readonly(number|null)[],w:number,h:number,spacing:(row:number)=>readonly[number,number]):TerrainGradient[]{
 const gradients:TerrainGradient[]=new Array(w*h).fill(null);
 for(let row=1;row<h-1;row++){const [dx,dy]=spacing(row);if(!(dx>0&&dy>0))continue;
  for(let col=1;col<w-1;col++){const i=row*w+col,a=[z[i-w-1],z[i-w],z[i-w+1],z[i-1],z[i],z[i+1],z[i+w-1],z[i+w],z[i+w+1]];
   if(a.every((v):v is number=>v!==null&&Number.isFinite(v)))gradients[i]={east:(a[2]+2*a[5]+a[8]-a[0]-2*a[3]-a[6])/(8*dx),north:(a[0]+2*a[1]+a[2]-a[6]-2*a[7]-a[8])/(8*dy)};
  }
 }
 return gradients;
}
/** Artistic illumination of measured, unscaled normals; never an added height. */
export function terrainIllumination(gradient:TerrainGradient){
 if(!gradient)return .82;
 const dot=(-gradient.east*-.5-gradient.north*.5+Math.SQRT1_2)/Math.hypot(gradient.east,gradient.north,1);
 return .55+.45*Math.max(0,Math.min(1,dot));
}
export function analyzeGroundGrid(grid:GroundGrid){
 const {width:w,height:h,ground:z}=grid,gradients=terrainGradients(z,w,h,row=>{const metric=groundMetricScale(groundCell(grid,row*w)!.latitude);return [grid.cellSize3857[0]*metric[0],grid.cellSize3857[1]*metric[1]];}),slope=gradients.map(g=>g?Math.atan(Math.hypot(g.east,g.north))*180/Math.PI:null),localRelief:(number|null)[]=new Array(w*h).fill(null);
 for(let row=3;row<h-3;row++)for(let col=3;col<w-3;col++){
  const index=row*w+col;if(z[index]===null)continue;
  let sum=0,valid=true;for(let r=-3;r<=3;r++)for(let c=-3;c<=3;c++){const value=z[index+r*w+c];if(value===null)valid=false;else sum+=value;}
  if(valid)localRelief[index]=z[index]!-sum/49;
 }
 return {slope,localRelief,gradients};
}
export function groundColorValues(grid:GroundGrid,color:GroundColor,analysis=analyzeGroundGrid(grid)):(number|null)[]{return color==='slope'?analysis.slope:color==='local-relief'?analysis.localRelief:grid.ground;}
export function terrainColorDomain(values:readonly (number|null)[],color:GroundColor):[number,number]|null{
 const finite=values.filter((v):v is number=>v!==null&&Number.isFinite(v));if(!finite.length)return null;
 if(color==='local-relief'){const extent=Math.max(...finite.map(Math.abs));return extent===0?[0,0]:[-extent,extent];}
 return [Math.min(...finite),Math.max(...finite)];
}
export function terrainStudyJSON(receipt:GroundReceipt,prepared?:ReturnType<typeof analyzeGroundGrid>){
 const validated=parseGroundReceipt(receipt,receipt.query,receipt.requestKey);if(!validated?.grid)throw Error('No validated Ground grid to export');
 return JSON.stringify({format:'kfm-terrain-study-v1',source:validated,recipe:TERRAIN_ANALYSIS_RECIPE,derived:prepared??analyzeGroundGrid(validated.grid),limits:'Display grid analysis only. No cultural, archaeological or certified field-accuracy inference.'},null,2);
}

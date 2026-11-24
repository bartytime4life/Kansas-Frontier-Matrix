import {nativePointPosition,parseNativeAssets,parseNativeManifest,type NativeAsset,type NativeCache,type NativeDataset,type NativeManifest} from './native-lidar';
export const KANSAS_LIDAR_WINDOW=[-102.2,36.8,-94.4,40.2] as const;
export const KANSAS_LIDAR_STATES=['idle','processing','ready','partial','no-coverage','detail-required','unavailable'] as const;
export type LidarViewState=typeof KANSAS_LIDAR_STATES[number];
export type LidarViewLayer='ground'|'surface'|'canopy'|'points';
export type LidarViewQuery={bbox:[number,number,number,number];zoom:number;layers:('surface'|'canopy'|'points')[]};
export type LidarViewReceipt={format:'kfm-lidar-view-v1';requestKey:string;query:LidarViewQuery;generatedAt:string;state:LidarViewState;layers:{kind:LidarViewLayer;state:LidarViewState;method:string;message:string}[];coverage:{project:string;eptUrl:string;boundsWgs84:[number,number,number,number];acquisition:string;verticalReference:string;qualification:string}[];points:NativeManifest|null;grid:{format:'kfm-lidar-grid-v1';width:number;height:number;sourceProject:string}|null;reason:string|null;limits:{maxPoints:100000;maxChunks:16;maxReplyBytes:1000000;maxTotalBytes:16777216;maxConcurrentChunks:2};cache:NativeCache};
export type LidarAnalysisGrid={format:'kfm-lidar-grid-v1';requestKey:string;generatedAt:string;width:number;height:number;analysisCrs:'EPSG:32614'|'EPSG:32615';bounds:[number,number,number,number];cellSizeM:[number,number];cornersWgs84:[number,number][];ground:(number|null)[];surface:(number|null)[];canopy:(number|null)[];groundCounts:number[];surfaceCounts:number[];vegetationCounts:number[];groundResidualM:(number|null)[];source:{project:string;eptUrl:string;acquisition:string;verticalReference:string;assets:NativeAsset[]};method:{completeNativeSupport:true;ground:string;surface:string;canopy:string;support:string;limitations:string[]};review:{status:'pending';source_admitted:false;released:false;scientific_accuracy_verified:false};cache:NativeCache};
export type KansasLidarView={receipt:LidarViewReceipt;points:NativeDataset|null;grid:LidarAnalysisGrid|null};
const object=(v:unknown):v is Record<string,unknown>=>!!v&&typeof v==='object'&&!Array.isArray(v);
const finite=(v:unknown):v is number=>typeof v==='number'&&Number.isFinite(v);
const integer=(v:unknown,min:number,max:number):v is number=>Number.isSafeInteger(v)&&Number(v)>=min&&Number(v)<=max;
const text=(v:unknown,max=5000):v is string=>typeof v==='string'&&v.length>0&&v.length<=max&&!/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(v);
const utc=(v:unknown):v is string=>typeof v==='string'&&/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?Z$/.test(v)&&Number.isFinite(Date.parse(v))&&new Date(v).toISOString().slice(0,19)===v.slice(0,19);
const key=(v:unknown):v is string=>typeof v==='string'&&/^[a-f0-9]{64}$/.test(v);
const state=(v:unknown):v is LidarViewState=>KANSAS_LIDAR_STATES.includes(v as LidarViewState);
const cache=(v:unknown):v is NativeCache=>object(v)&&['live','fresh','stale'].includes(String(v.state))&&utc(v.at);
const ept=(project:unknown,url:unknown)=>text(project,180)&&/^[-A-Za-z0-9_.]+$/.test(project)&&url==='https://usgs-lidar-public.s3.amazonaws.com/'+project+'/ept.json';
const wgs=(v:unknown):v is [number,number,number,number]=>Array.isArray(v)&&v.length===4&&v.every(finite)&&v[0]<v[2]&&v[1]<v[3]&&v[0]>=-180&&v[2]<=180&&v[1]>=-85.1&&v[3]<=85.1;
export function canonicalLidarView(bounds:readonly number[],zoom:number,layers:readonly string[]):LidarViewQuery|null{
  if(bounds.length!==4||!bounds.every(finite)||!finite(zoom)||bounds[0]>=bounds[2]||bounds[1]>=bounds[3])return null;
  const bbox=[Math.max(bounds[0],KANSAS_LIDAR_WINDOW[0]),Math.max(bounds[1],KANSAS_LIDAR_WINDOW[1]),Math.min(bounds[2],KANSAS_LIDAR_WINDOW[2]),Math.min(bounds[3],KANSAS_LIDAR_WINDOW[3])].map(v=>Math.round(v*1e5)/1e5) as LidarViewQuery['bbox'];
  const selected=(['surface','canopy','points'] as const).filter(layer=>layers.includes(layer));
  return bbox[0]<bbox[2]&&bbox[1]<bbox[3]&&selected.length?{bbox,zoom:Math.round(Math.min(20,Math.max(4,zoom))*10)/10,layers:selected}:null;
}
export function lidarViewPath(query:LidarViewQuery){return '/api/lidar/view?bbox='+query.bbox.join(',')+'&zoom='+query.zoom.toFixed(1)+'&layers='+query.layers.join(',');}
export async function lidarViewRequestKey(query:LidarViewQuery){const bytes=new TextEncoder().encode(JSON.stringify(query)),digest=await globalThis.crypto.subtle.digest('SHA-256',bytes);return Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');}
export function parseLidarViewReceipt(v:unknown,expected:LidarViewQuery,expectedKey?:string):LidarViewReceipt|null{
  if(!object(v)||v.format!=='kfm-lidar-view-v1'||!key(v.requestKey)||(expectedKey!==undefined&&v.requestKey!==expectedKey)||!utc(v.generatedAt)||!state(v.state)||!cache(v.cache)||!object(v.query)||JSON.stringify(v.query.bbox)!==JSON.stringify(expected.bbox)||v.query.zoom!==expected.zoom||JSON.stringify(v.query.layers)!==JSON.stringify(expected.layers)||!(v.reason===null||text(v.reason)))return null;
  if(!Array.isArray(v.layers)||v.layers.length!==4||new Set(v.layers.map(l=>object(l)?l.kind:null)).size!==4||!v.layers.every(l=>object(l)&&['ground','surface','canopy','points'].includes(String(l.kind))&&state(l.state)&&text(l.method)&&text(l.message)))return null;
  if(!Array.isArray(v.coverage)||v.coverage.length>127||!v.coverage.every(c=>object(c)&&ept(c.project,c.eptUrl)&&wgs(c.boundsWgs84)&&text(c.acquisition)&&text(c.verticalReference)&&text(c.qualification)))return null;
  const limits=v.limits;if(!object(limits)||limits.maxPoints!==100000||limits.maxChunks!==16||limits.maxReplyBytes!==1000000||limits.maxTotalBytes!==16777216||limits.maxConcurrentChunks!==2)return null;
  const points=v.points===null?null:parseNativeManifest(object(v.points)?{...v.points,cache:v.cache}:v.points);if(v.points!==null&&(!points||points.format!=='kfm-lidar-points-manifest-v2'||points.captureId!=='view-'+v.requestKey))return null;
  if(points){
    const low=nativePointPosition([points.bounds3857[0],points.bounds3857[1],0]),high=nativePointPosition([points.bounds3857[2],points.bounds3857[3],0]),b=expected.bbox;
    if(low.longitude<b[0]-1e-8||low.latitude<b[1]-1e-8||high.longitude>b[2]+1e-8||high.latitude>b[3]+1e-8||!points.source.assets.every(asset=>(v.coverage as Record<string,unknown>[]).some(c=>c.project===asset.project&&c.eptUrl===asset.eptUrl)))return null;
  }
  const grid=v.grid;if(grid!==null&&(!object(grid)||grid.format!=='kfm-lidar-grid-v1'||!integer(grid.width,1,64)||!integer(grid.height,1,64)||!text(grid.sourceProject,180)))return null;
  return structuredClone({...v,query:expected,points}) as LidarViewReceipt;
}
export function parseLidarAnalysisGrid(v:unknown,receipt:LidarViewReceipt):LidarAnalysisGrid|null{
  const spec=receipt.grid;if(!spec||!object(v)||v.format!=='kfm-lidar-grid-v1'||v.requestKey!==receipt.requestKey||!utc(v.generatedAt)||!cache(v.cache)||v.width!==spec.width||v.height!==spec.height||!integer(v.width,1,64)||!integer(v.height,1,64)||!['EPSG:32614','EPSG:32615'].includes(String(v.analysisCrs)))return null;
  const b=v.bounds,cell=v.cellSizeM,n=v.width*v.height;if(!Array.isArray(b)||b.length!==4||!b.every(finite)||b.some(x=>Math.abs(x)>10_000_000)||b[0]>=b[2]||b[1]>=b[3]||(b[2]-b[0])*(b[3]-b[1])>1_000_000.01||!Array.isArray(cell)||cell.length!==2||!cell.every(x=>finite(x)&&x>0)||Math.abs(cell[0]*v.width-(b[2]-b[0]))>1e-6||Math.abs(cell[1]*v.height-(b[3]-b[1]))>1e-6)return null;
  const corners=v.cornersWgs84;if(!Array.isArray(corners)||corners.length!==(v.width+1)*(v.height+1)||!corners.every(p=>Array.isArray(p)&&p.length===2&&p.every(finite)&&p[0]>=-102.3&&p[0]<=-94.3&&p[1]>=36.7&&p[1]<=40.3))return null;
  const query=receipt.query.bbox,longitudes=corners.map(p=>p[0]),latitudes=corners.map(p=>p[1]);if(Math.max(...longitudes)<query[0]||Math.min(...longitudes)>query[2]||Math.max(...latitudes)<query[1]||Math.min(...latitudes)>query[3])return null;
  for(let r=0;r<v.height;r++)for(let c=0;c<v.width;c++){const i=r*(v.width+1)+c,q=[corners[i],corners[i+1],corners[i+v.width+2],corners[i+v.width+1]];for(let k=0;k<4;k++){const a=q[k],b=q[(k+1)%4],d=q[(k+2)%4];if((b[0]-a[0])*(d[1]-b[1])-(b[1]-a[1])*(d[0]-b[0])>=0)return null;}}
  for(const name of ['ground','surface','canopy','groundResidualM']){const a=v[name];if(!Array.isArray(a)||a.length!==n||!a.every(x=>x===null||finite(x)&&Math.abs(x)<=12000&&(name!=='groundResidualM'||x>=0)))return null;}
  for(const name of ['groundCounts','surfaceCounts','vegetationCounts']){const a=v[name];if(!Array.isArray(a)||a.length!==n||!a.every(x=>integer(x,0,2_000_000)))return null;}
  for(let i=0;i<n;i++){if((v.canopy as (number|null)[])[i]!==null&&((v.ground as (number|null)[])[i]===null||(v.vegetationCounts as number[])[i]===0)||(v.surface as (number|null)[])[i]!==null&&(v.surfaceCounts as number[])[i]===0)return null;}
  const source=v.source,method=v.method,review=v.review;if(!object(source)||source.project!==spec.sourceProject||!ept(source.project,source.eptUrl)||!text(source.acquisition)||!text(source.verticalReference))return null;
  const assets=parseNativeAssets(source.assets,2);if(!assets||!assets.every(a=>a.project===source.project&&a.eptUrl===source.eptUrl))return null;
  if(!object(method)||method.completeNativeSupport!==true||!['ground','surface','canopy','support'].every(k=>text(method[k]))||!Array.isArray(method.limitations)||method.limitations.length>30||!method.limitations.every(x=>text(x))||!object(review)||review.status!=='pending'||review.source_admitted!==false||review.released!==false||review.scientific_accuracy_verified!==false)return null;
  return structuredClone({...v,source:{...source,assets}}) as LidarAnalysisGrid;
}
export function lidarGridCell(grid:LidarAnalysisGrid,index:number){if(!Number.isInteger(index)||index<0||index>=grid.width*grid.height)return null;return {row:Math.floor(index/grid.width)+1,column:index%grid.width+1,ground:grid.ground[index],surface:grid.surface[index],canopy:grid.canopy[index],groundCount:grid.groundCounts[index],surfaceCount:grid.surfaceCounts[index],vegetationCount:grid.vegetationCounts[index],groundResidualM:grid.groundResidualM[index]};}

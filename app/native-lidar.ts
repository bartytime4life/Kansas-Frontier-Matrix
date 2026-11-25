/** Source-linked native returns. No interpolation, height normalization or datum conversion. */
export const NATIVE_POINT_LIMIT = 100_000;
export const NATIVE_POINT_COLUMNS = ['x','y','z','intensity','classification','returnNumber','numberOfReturns','classFlags','gpsTime','asset','record'] as const;
export type NativePoint = readonly [number,number,number,number,number,number,number,number,number|null,number,number];
export type NativeCache = { state:'live'|'fresh'|'stale'; at:string };
export type NativeAsset={id:number;url:string;sha256:string;bytes:number;pointCount:number;project?:string;eptUrl?:string;coordinateEncodingM?:[number,number,number];acquisition?:string;verticalReference?:string;gpsTimeType?:'week'|'adjusted-standard'|'absent'|'unspecified'};
export type NativeManifest = {
  format:'kfm-lidar-points-manifest-v1'|'kfm-lidar-points-manifest-v2'; captureId:string; generatedAt:string;
  source:{ provider:'USGS'; project:string; eptUrl:string; horizontalCrs:'EPSG:3857'; verticalReference:string; acquisition:string; coordinateEncodingM:[number,number,number]; selection:string; assets:NativeAsset[];notes:string[] };
  review:{status:'pending';source_admitted:false;released:false;scientific_accuracy_verified:false};
  pointCount:number; bounds3857:[number,number,number,number];heightRange:[number,number]; columns:typeof NATIVE_POINT_COLUMNS;
  chunks:{id:number;pointCount:number;bytes:number;sha256:string}[];cache:NativeCache;
};
export type NativeChunk = {format:'kfm-lidar-points-chunk-v1'|'kfm-lidar-points-chunk-v2';captureId:string;chunkId:number;points:NativePoint[];cache:NativeCache};
export type NativeDataset = {format:'kfm-native-lidar-v1';manifest:NativeManifest;points:readonly NativePoint[];chunkCaches:NativeCache[]};
const obj=(v:unknown):v is Record<string,unknown>=>!!v&&typeof v==='object'&&!Array.isArray(v);
const finite=(v:unknown):v is number=>typeof v==='number'&&Number.isFinite(v);
const integer=(v:unknown,min:number,max:number):v is number=>Number.isSafeInteger(v)&&Number(v)>=min&&Number(v)<=max;
const text=(v:unknown,max=2000):v is string=>typeof v==='string'&&v.trim().length>0&&v.length<=max&&!/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(v);
const date=(v:unknown):v is string=>typeof v==='string'&&/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z$/.test(v)&&Number.isFinite(Date.parse(v))&&new Date(v).toISOString().slice(0,19)===v.slice(0,19);
const hash=(v:unknown):v is string=>typeof v==='string'&&/^sha256:[a-f0-9]{64}$/.test(v);
const cache=(v:unknown):v is NativeCache=>obj(v)&&['live','fresh','stale'].includes(String(v.state))&&date(v.at);
export function parseNativeAssets(value:unknown,version:1|2):NativeAsset[]|null{
  if(!Array.isArray(value)||value.length<1||value.length>(version===2?128:32))return null;
  const assets:NativeAsset[]=[];
  for(const [id,a] of value.entries()){
    if(!obj(a)||a.id!==id||!hash(a.sha256)||!integer(a.bytes,1,version===2?8_000_000:1_000_000_000)||!integer(a.pointCount,1,version===2?2_000_000:10_000_000))return null;
    const project=version===1?'KS_Statewide_B6A_2018':a.project;
    if(typeof project!=='string'||!/^[-A-Za-z0-9_.]{1,180}$/.test(project)||project==='.'||project==='..')return null;
    const ept='https://usgs-lidar-public.s3.amazonaws.com/'+project+'/ept.json',prefix=ept.slice(0,-8)+'ept-data/';
    if(typeof a.url!=='string'||!a.url.startsWith(prefix)||!/^\d+-\d+-\d+-\d+\.laz$/.test(a.url.slice(prefix.length)))return null;
    const asset:NativeAsset={id,url:a.url,sha256:a.sha256,bytes:a.bytes,pointCount:a.pointCount};
    if(version===2){
      if(a.eptUrl!==ept||!Array.isArray(a.coordinateEncodingM)||a.coordinateEncodingM.length!==3||!a.coordinateEncodingM.every(n=>finite(n)&&n>0&&n<=1)||!text(a.acquisition)||!text(a.verticalReference)||!['week','adjusted-standard','absent','unspecified'].includes(String(a.gpsTimeType)))return null;
      Object.assign(asset,{project,eptUrl:ept,coordinateEncodingM:[...a.coordinateEncodingM],acquisition:a.acquisition,verticalReference:a.verticalReference,gpsTimeType:a.gpsTimeType});
    }
    assets.push(asset);
  }
  return assets;
}
export function parseNativeManifest(v:unknown):NativeManifest|null {
  if(!obj(v)||!['kfm-lidar-points-manifest-v1','kfm-lidar-points-manifest-v2'].includes(String(v.format))||typeof v.captureId!=='string'||!date(v.generatedAt)||!cache(v.cache)||!integer(v.pointCount,1,NATIVE_POINT_LIMIT))return null;
  const version=v.format==='kfm-lidar-points-manifest-v2'?2:1;
  if(version===2?!/^view-[a-f0-9]{64}$/.test(v.captureId):!/^[-a-zA-Z0-9_]{1,80}$/.test(v.captureId))return null;
  const s=v.source,r=v.review,b=v.bounds3857,h=v.heightRange,c=v.chunks;
  if(!obj(s)||s.provider!=='USGS'||s.project!==(version===2?'Kansas viewport':'KS_Statewide_B6A_2018')||s.eptUrl!==(version===2?'https://usgs.entwine.io/':'https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept.json')||s.horizontalCrs!=='EPSG:3857'||!text(s.verticalReference)||!text(s.acquisition)||!text(s.selection,5000)||!Array.isArray(s.coordinateEncodingM)||s.coordinateEncodingM.length!==3||!s.coordinateEncodingM.every(n=>finite(n)&&n>0&&n<=1)||!Array.isArray(s.notes)||s.notes.length>32||!s.notes.every(n=>text(n,5000)))return null;
  const assets=parseNativeAssets(s.assets,version);if(!assets)return null;
  if(s.coordinateEncodingM.some((n,i)=>n!==(version===1?.001:Math.min(...assets.map(a=>a.coordinateEncodingM![i])))))return null;
  if(!obj(r)||r.status!=='pending'||r.source_admitted!==false||r.released!==false||r.scientific_accuracy_verified!==false)return null;
  if(!Array.isArray(b)||b.length!==4||!b.every(finite)||!(b[0]<b[2]&&b[1]<b[3])||b.some(n=>Math.abs(n)>20_037_509)||!Array.isArray(h)||h.length!==2||!h.every(finite)||h[0]>h[1]||h.some(n=>Math.abs(n)>100_000)||(version===2&&(h[0]<-12000||h[1]>9000)))return null;
  if(!Array.isArray(v.columns)||v.columns.length!==NATIVE_POINT_COLUMNS.length||!v.columns.every((key,i)=>key===NATIVE_POINT_COLUMNS[i])||!Array.isArray(c)||c.length<1||c.length>16||!c.every((part,i)=>obj(part)&&part.id===i&&integer(part.pointCount,1,NATIVE_POINT_LIMIT)&&integer(part.bytes,1,899_999)&&hash(part.sha256))||c.reduce((n,p)=>n+Number(p.pointCount),0)!==v.pointCount)return null;
  return {format:v.format as NativeManifest['format'],captureId:v.captureId,generatedAt:v.generatedAt,source:{provider:s.provider,project:s.project as string,eptUrl:s.eptUrl as string,horizontalCrs:s.horizontalCrs,verticalReference:s.verticalReference,acquisition:s.acquisition,selection:s.selection,coordinateEncodingM:[...s.coordinateEncodingM] as [number,number,number],assets,notes:[...s.notes] as string[]},review:{status:'pending',source_admitted:false,released:false,scientific_accuracy_verified:false},pointCount:v.pointCount,bounds3857:[...b] as NativeManifest['bounds3857'],heightRange:[...h] as [number,number],columns:NATIVE_POINT_COLUMNS,chunks:c.map(p=>({...p})) as NativeManifest['chunks'],cache:{...v.cache}};
}
export function parseNativeChunk(v:unknown,m:NativeManifest,id:number):NativeChunk|null {
  const spec=m.chunks[id];
  if(!spec||!obj(v)||v.format!==(m.format==='kfm-lidar-points-manifest-v2'?'kfm-lidar-points-chunk-v2':'kfm-lidar-points-chunk-v1')||v.captureId!==m.captureId||v.chunkId!==id||!cache(v.cache)||!Array.isArray(v.points)||v.points.length!==spec.pointCount)return null;
  const [x0,y0,x1,y1]=m.bounds3857,[z0,z1]=m.heightRange;
  for(const row of v.points){
    if(!Array.isArray(row)||row.length!==11||!row.every((n,i)=>i===8?n===null||finite(n):finite(n)))return null;
    const [x,y,z,intensity,classification,ret,returns,flags,,asset,record]=row;
    if(x<x0||x>x1||y<y0||y>y1||z<z0||z>z1||!integer(intensity,0,65535)||!integer(classification,0,255)||!integer(ret,0,15)||!integer(returns,0,15)||!integer(flags,0,15)||!integer(asset,0,m.source.assets.length-1)||!integer(record,0,m.source.assets[asset].pointCount-1))return null;
    if(m.source.assets[asset].gpsTimeType==='absent'?row[8]!==null:!finite(row[8]))return null;
  }
  return {format:v.format as NativeChunk['format'],captureId:m.captureId,chunkId:id,points:v.points.map(p=>[...p] as unknown as NativePoint),cache:{...v.cache}};
}
export function assembleNativeDataset(manifest:NativeManifest,chunks:readonly NativeChunk[]):NativeDataset|null {
  if(chunks.length!==manifest.chunks.length)return null;
  const points:NativePoint[]=[],seen=new Set<string>();let x0=Infinity,y0=Infinity,x1=-Infinity,y1=-Infinity,z0=Infinity,z1=-Infinity;
  for(let id=0;id<chunks.length;id++){
    const chunk=parseNativeChunk(chunks[id],manifest,id);if(!chunk)return null;
    for(const p of chunk.points){const key=p[9]+':'+p[10];if(seen.has(key))return null;seen.add(key);points.push(p);x0=Math.min(x0,p[0]);y0=Math.min(y0,p[1]);x1=Math.max(x1,p[0]);y1=Math.max(y1,p[1]);z0=Math.min(z0,p[2]);z1=Math.max(z1,p[2]);}
  }
  if(points.length!==manifest.pointCount||[x0,y0,x1,y1,z0,z1].some((v,i)=>Math.abs(v-[...manifest.bounds3857,...manifest.heightRange][i])>1e-6))return null;
  return {format:'kfm-native-lidar-v1',manifest,points,chunkCaches:chunks.map(c=>({...c.cache}))};
}
export const nativePointEligible=(point:NativePoint)=>(point[7]&(1|4))===0&&point[4]!==7&&point[4]!==18;
export const WEB_MERCATOR_RADIUS_M=6378137,MAPLIBRE_EARTH_RADIUS_M=6371008.8;
/** XY uses EPSG3857's radius; altitude uses MapLibre's mean Earth circumference. */
export function nativePointPosition(point:Pick<NativePoint,0|1|2>,scale=1):{longitude:number;latitude:number;mercator:[number,number,number]} {
  if(!Number.isFinite(scale)||scale<.1||scale>5)throw new Error('Unsupported display height scale');
  const longitude=point[0]/WEB_MERCATOR_RADIUS_M*180/Math.PI,latitude=(2*Math.atan(Math.exp(point[1]/WEB_MERCATOR_RADIUS_M))-Math.PI/2)*180/Math.PI;
  return {longitude,latitude,mercator:[.5+point[0]/(2*Math.PI*WEB_MERCATOR_RADIUS_M),.5-point[1]/(2*Math.PI*WEB_MERCATOR_RADIUS_M),point[2]*scale/(2*Math.PI*MAPLIBRE_EARTH_RADIUS_M*Math.cos(latitude*Math.PI/180))]};
}
/** Sequential display colors shared by solid cells, elevation returns and legends.
 * Each stop has increasing relative luminance; this changes no source/domain. */
const TERRAIN_HEIGHT_STOPS = [
  [31, 77, 82], [69, 115, 99], [122, 158, 110], [186, 194, 125], [245, 219, 145],
] as const;
const TERRAIN_RELIEF_STOPS = [[31, 87, 103], [166, 176, 166], [245, 219, 145]] as const;
type TerrainColorStop = readonly [number, number, number];
function terrainRampColor(stops: readonly TerrainColorStop[], value: number): readonly [number, number, number] {
  const t = Math.max(0, Math.min(1, Number.isFinite(value) ? value : .5));
  const position = t * (stops.length - 1), index = Math.min(stops.length - 2, Math.floor(position));
  const fraction = position - index, low = stops[index], high = stops[index + 1];
  return [(low[0] + (high[0] - low[0]) * fraction) / 255,
    (low[1] + (high[1] - low[1]) * fraction) / 255,
    (low[2] + (high[2] - low[2]) * fraction) / 255];
}
function terrainRampCSS(stops: readonly TerrainColorStop[]) {
  return `linear-gradient(90deg,${stops.map((color, index) => `rgb(${color.join(',')}) ${index / (stops.length - 1) * 100}%`).join(',')})`;
}
export const TERRAIN_HEIGHT_RAMP_CSS = terrainRampCSS(TERRAIN_HEIGHT_STOPS);
export const TERRAIN_RELIEF_RAMP_CSS = terrainRampCSS(TERRAIN_RELIEF_STOPS);
export const terrainHeightColor = (t: number) => terrainRampColor(TERRAIN_HEIGHT_STOPS, t);
/** Negative/positive local relief uses a neutral zero; the legend stays symmetric. */
export const terrainReliefColor = (t: number) => terrainRampColor(TERRAIN_RELIEF_STOPS, t);

export type NativeColorMode='elevation'|'classification'|'intensity';
export const NATIVE_CLASS_COLORS:Readonly<Record<number,readonly [number,number,number]>>={0:[.6,.65,.7],1:[.72,.76,.82],2:[.83,.63,.34],3:[.45,.75,.42],4:[.22,.64,.36],5:[.08,.47,.3],6:[.89,.38,.32],7:[.85,.31,.72],9:[.25,.64,.9],18:[.85,.31,.72]};
export function nativeAttributeDomain(dataset:NativeDataset,mode:NativeColorMode):readonly [number,number]|null{
  let low=Infinity,high=-Infinity;const column=mode==='intensity'?3:2;
  for(const point of dataset.points){if(!nativePointEligible(point))continue;low=Math.min(low,point[column]);high=Math.max(high,point[column]);}
  return Number.isFinite(low)?[low,high]:null;
}
export function nativePointColor(point:NativePoint,mode:NativeColorMode,domain:readonly [number,number]):readonly [number,number,number] {
  if(mode==='classification')return NATIVE_CLASS_COLORS[point[4]]??[.7,.63,.82];
  const value=mode==='intensity'?point[3]:point[2],t=domain[1]===domain[0]?.5:Math.max(0,Math.min(1,(value-domain[0])/(domain[1]-domain[0])));
  return mode==='intensity'?[t,t,t]:terrainHeightColor(t);
}

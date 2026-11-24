import {createHash} from 'node:crypto';
import {LIDAR_POINTS_COLUMNS} from './lidar-points.mjs';
export const LIDAR_VIEW_ROUTES=Object.freeze({view:'/v1/lidar/view',chunk:'/v1/lidar/view/chunk',grid:'/v1/lidar/view/grid'});
export const LIDAR_VIEW_LIMITS=Object.freeze({maxPoints:100000,maxChunks:16,maxReplyBytes:1000000,maxTotalBytes:16777216,maxConcurrentChunks:2});
export const LIDAR_VIEW_STATES=Object.freeze(['idle','processing','ready','partial','no-coverage','detail-required','unavailable']);
const kinds=['ground','surface','canopy','points'],requestedKinds=kinds.slice(1);
const obj=v=>v!==null&&typeof v==='object'&&!Array.isArray(v);
const keys=(v,s)=>obj(v)&&Object.keys(v).sort().join(',')===s.split(',').sort().join(',');
const fin=v=>typeof v==='number'&&Number.isFinite(v);
const int=(v,min,max)=>Number.isSafeInteger(v)&&v>=min&&v<=max;
const text=(v,max=2000)=>typeof v==='string'&&v.length>0&&v.length<=max&&!/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(v);
const sha=v=>typeof v==='string'&&/^sha256:[a-f0-9]{64}$/.test(v);
export const validViewKey=v=>typeof v==='string'&&/^[a-f0-9]{64}$/.test(v);
const instant=v=>typeof v==='string'&&/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?Z$/.test(v)&&Number.isFinite(Date.parse(v));
const review=v=>keys(v,'status,source_admitted,released,scientific_accuracy_verified')&&v.status==='pending'&&v.source_admitted===false&&v.released===false&&v.scientific_accuracy_verified===false;
const bbox=(v,world=20037509)=>Array.isArray(v)&&v.length===4&&v.every(fin)&&v[0]<v[2]&&v[1]<v[3]&&v.every(n=>Math.abs(n)<=world);
const project=v=>typeof v==='string'&&/^[A-Za-z0-9_-]{1,160}$/.test(v);
const ept=(p,url)=>project(p)&&url===`https://usgs-lidar-public.s3.amazonaws.com/${p}/ept.json`;
export function normalizeLidarView(input){
 if(!keys(input,'bbox,zoom,layers')||!bbox(input.bbox,180)||input.bbox[0]<-102.2||input.bbox[2]>-94.4||input.bbox[1]<36.8||input.bbox[3]>40.2||!fin(input.zoom)||input.zoom<4||input.zoom>20||!Array.isArray(input.layers)||input.layers.length<1||input.layers.length>3||new Set(input.layers).size!==input.layers.length||input.layers.some(v=>!requestedKinds.includes(v)))throw Error('QUERY_INVALID');
 const query={bbox:input.bbox.map(v=>Math.round(v*1e5)/1e5),zoom:Math.round(input.zoom*10)/10,layers:requestedKinds.filter(k=>input.layers.includes(k))};
 if(!bbox(query.bbox,180))throw Error('QUERY_INVALID');return query;
}
export function lidarViewKey(input){return createHash('sha256').update(JSON.stringify(normalizeLidarView(input))).digest('hex');}
export function parseLidarViewSearch(search){
 if([...search.keys()].some(k=>!['bbox','zoom','layers'].includes(k)||search.getAll(k).length!==1)||search.size!==3)throw Error('QUERY_INVALID');
 const number=s=>typeof s==='string'&&/^-?(?:\d+(?:\.\d+)?|\.\d+)$/.test(s)?Number(s):NaN;
 return normalizeLidarView({bbox:(search.get('bbox')??'').split(',').map(number),zoom:number(search.get('zoom')),layers:(search.get('layers')??'').split(',')});
}
export function validNativeViewAsset(a,i){
 return keys(a,'id,url,sha256,bytes,pointCount,project,eptUrl,coordinateEncodingM,acquisition,verticalReference,gpsTimeType')&&a.id===i&&ept(a.project,a.eptUrl)&&typeof a.url==='string'&&a.url.startsWith(a.eptUrl.slice(0,-8)+'ept-data/')&&/^\d{1,2}-\d{1,10}-\d{1,10}-\d{1,10}\.laz$/.test(a.url.split('/').at(-1))&&a.url===a.eptUrl.slice(0,-8)+'ept-data/'+a.url.split('/').at(-1)&&sha(a.sha256)&&int(a.bytes,1,8000000)&&int(a.pointCount,1,2000000)&&Array.isArray(a.coordinateEncodingM)&&a.coordinateEncodingM.length===3&&a.coordinateEncodingM.every(n=>fin(n)&&n>0&&n<=1)&&text(a.acquisition)&&text(a.verticalReference)&&['week','adjusted-standard','absent','unspecified'].includes(a.gpsTimeType);
}
export function validNativeViewManifest(m,key){
 if(!validViewKey(key)||!keys(m,'format,captureId,generatedAt,source,review,pointCount,bounds3857,heightRange,chunks,columns')||m.format!=='kfm-lidar-points-manifest-v2'||m.captureId!=='view-'+key||!instant(m.generatedAt)||!review(m.review)||!int(m.pointCount,1,100000)||!bbox(m.bounds3857)||!Array.isArray(m.heightRange)||m.heightRange.length!==2||!m.heightRange.every(fin)||m.heightRange[0]>m.heightRange[1]||m.heightRange[0]<-12000||m.heightRange[1]>9000||!Array.isArray(m.columns)||m.columns.join(',')!==LIDAR_POINTS_COLUMNS.join(','))return false;
 const s=m.source;
 if(!keys(s,'provider,project,eptUrl,horizontalCrs,verticalReference,acquisition,coordinateEncodingM,selection,assets,notes')||s.provider!=='USGS'||s.project!=='Kansas viewport'||s.eptUrl!=='https://usgs.entwine.io/'||s.horizontalCrs!=='EPSG:3857'||!text(s.verticalReference)||!text(s.acquisition)||!text(s.selection)||!Array.isArray(s.coordinateEncodingM)||s.coordinateEncodingM.length!==3||!s.coordinateEncodingM.every(v=>fin(v)&&v>0&&v<=1)||!Array.isArray(s.assets)||s.assets.length<1||s.assets.length>128||!s.assets.every(validNativeViewAsset)||!Array.isArray(s.notes)||s.notes.length>32||!s.notes.every(v=>text(v)))return false;
 if(s.coordinateEncodingM.some((n,axis)=>n!==Math.min(...s.assets.map(a=>a.coordinateEncodingM[axis]))))return false;
 return Array.isArray(m.chunks)&&m.chunks.length>=1&&m.chunks.length<=16&&m.chunks.every((c,i)=>keys(c,'id,pointCount,bytes,sha256')&&c.id===i&&int(c.pointCount,1,15000)&&int(c.bytes,1,900000)&&sha(c.sha256))&&m.chunks.reduce((n,c)=>n+c.pointCount,0)===m.pointCount;
}
export function validNativeViewChunk(c,m,key,id){
 if(!validNativeViewManifest(m,key)||!int(id,0,m.chunks.length-1)||!keys(c,'format,captureId,chunkId,points')||c.format!=='kfm-lidar-points-chunk-v2'||c.captureId!==m.captureId||c.chunkId!==id||!Array.isArray(c.points)||c.points.length!==m.chunks[id].pointCount)return false;
 const seen=new Set(),b=m.bounds3857,h=m.heightRange;
 return c.points.every(r=>{
  if(!Array.isArray(r)||r.length!==11||r.some((n,i)=>i!==8&&!fin(n))||r[0]<b[0]||r[0]>b[2]||r[1]<b[1]||r[1]>b[3]||r[2]<h[0]||r[2]>h[1]||!int(r[3],0,65535)||!int(r[4],0,255)||!int(r[5],0,15)||!int(r[6],0,15)||!int(r[7],0,15)||!int(r[9],0,m.source.assets.length-1)||!int(r[10],0,m.source.assets[r[9]].pointCount-1))return false;
  if(m.source.assets[r[9]].gpsTimeType==='absent'?r[8]!==null:!fin(r[8]))return false;
  const identity=r[9]+':'+r[10];if(seen.has(identity))return false;seen.add(identity);return true;
 });
}
export function validLidarGrid(g,key){
 if(!validViewKey(key)||!keys(g,'format,requestKey,generatedAt,width,height,analysisCrs,bounds,cellSizeM,cornersWgs84,ground,surface,canopy,groundCounts,surfaceCounts,vegetationCounts,groundResidualM,source,method,review')||g.format!=='kfm-lidar-grid-v1'||g.requestKey!==key||!instant(g.generatedAt)||!int(g.width,1,64)||!int(g.height,1,64)||!['EPSG:32614','EPSG:32615'].includes(g.analysisCrs)||!bbox(g.bounds)||!review(g.review))return false;
 const n=g.width*g.height;
 if(!Array.isArray(g.cellSizeM)||g.cellSizeM.length!==2||g.cellSizeM.some((v,i)=>!fin(v)||v<=0||Math.abs(v-(g.bounds[i+2]-g.bounds[i])/(i===0?g.width:g.height))>1e-6)||!Array.isArray(g.cornersWgs84)||g.cornersWgs84.length!==(g.width+1)*(g.height+1)||!g.cornersWgs84.every(p=>Array.isArray(p)&&p.length===2&&p.every(fin)&&p[0]>=-102.3&&p[0]<=-94.3&&p[1]>=36.7&&p[1]<=40.3))return false;
 for(const band of ['ground','surface','canopy','groundResidualM'])if(!Array.isArray(g[band])||g[band].length!==n||!g[band].every(v=>v===null||fin(v)&&Math.abs(v)<=12000)||band==='groundResidualM'&&g[band].some(v=>v!==null&&v<0))return false;
 for(const band of ['groundCounts','surfaceCounts','vegetationCounts'])if(!Array.isArray(g[band])||g[band].length!==n||!g[band].every(v=>int(v,0,2000000)))return false;
 for(let i=0;i<n;i++)if(g.canopy[i]!==null&&(g.ground[i]===null||g.vegetationCounts[i]===0)||g.surface[i]!==null&&g.surfaceCounts[i]===0)return false;
 const s=g.source,t=g.method;
 return keys(s,'project,eptUrl,acquisition,verticalReference,assets')&&ept(s.project,s.eptUrl)&&text(s.acquisition)&&text(s.verticalReference)&&Array.isArray(s.assets)&&s.assets.length>=1&&s.assets.length<=128&&s.assets.every((a,i)=>validNativeViewAsset(a,i)&&a.project===s.project)&&keys(t,'completeNativeSupport,ground,surface,canopy,support,limitations')&&t.completeNativeSupport===true&&['ground','surface','canopy','support'].every(k=>text(t[k]))&&Array.isArray(t.limitations)&&t.limitations.length<=32&&t.limitations.every(v=>text(v));
}
export function validLidarView(v,query){
 let q;try{q=normalizeLidarView(query);}catch{return false;}const key=lidarViewKey(q);
 if(!keys(v,'format,requestKey,query,generatedAt,state,layers,coverage,points,grid,reason,limits')||v.format!=='kfm-lidar-view-v1'||v.requestKey!==key||JSON.stringify(v.query)!==JSON.stringify(q)||!instant(v.generatedAt)||!LIDAR_VIEW_STATES.includes(v.state)||v.reason!==null&&!text(v.reason)||JSON.stringify(v.limits)!==JSON.stringify(LIDAR_VIEW_LIMITS))return false;
 if(!Array.isArray(v.layers)||v.layers.length!==4||!v.layers.every((l,i)=>keys(l,'kind,state,method,message')&&l.kind===kinds[i]&&LIDAR_VIEW_STATES.includes(l.state)&&text(l.method)&&text(l.message)))return false;
 if(!Array.isArray(v.coverage)||v.coverage.length>127||!v.coverage.every(c=>keys(c,'project,eptUrl,boundsWgs84,acquisition,verticalReference,qualification')&&ept(c.project,c.eptUrl)&&bbox(c.boundsWgs84,180)&&text(c.acquisition)&&text(c.verticalReference)&&text(c.qualification)))return false;
 if(v.points!==null&&!validNativeViewManifest(v.points,key))return false;
 return v.grid===null||keys(v.grid,'format,width,height,sourceProject')&&v.grid.format==='kfm-lidar-grid-v1'&&int(v.grid.width,1,64)&&int(v.grid.height,1,64)&&project(v.grid.sourceProject);
}

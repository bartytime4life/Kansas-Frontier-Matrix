import {readFileSync,readdirSync,lstatSync,realpathSync,mkdirSync,openSync,closeSync,writeFileSync,constants,fstatSync,readSync,renameSync} from 'node:fs';
import {isAbsolute,resolve,join,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash,randomBytes} from 'node:crypto';
import {normalizeLidarView,lidarViewKey,LIDAR_VIEW_LIMITS,validLidarView,validNativeViewManifest,validNativeViewChunk,validLidarGrid,validViewKey} from './lidar-view-model.mjs';
const here=dirname(fileURLToPath(import.meta.url)),digest=b=>'sha256:'+createHash('sha256').update(b).digest('hex');
export const KANSAS_EPT_CATALOG_SHA256='sha256:982b601b234ad6de58c4d971d3a9c85d0abdd86b1b15dba3e2201b6e779dfcb1';
export const KANSAS_EPT_FOOTPRINTS_SHA256='sha256:85efbc7379c78e1ce66f0bb6ce8e8abf295b34c1d367c6409396542b9f560801';
let discovery=null;
export function loadLidarDiscovery(){
 if(discovery)return discovery;
 const a=readFileSync(join(here,'kansas-ept-catalog.json')),b=readFileSync(join(here,'kansas-ept-footprints.geojson'));
 if(a.length>512000||b.length>512000||digest(a)!==KANSAS_EPT_CATALOG_SHA256||digest(b)!==KANSAS_EPT_FOOTPRINTS_SHA256)throw Error('LIDAR_CATALOG_INVALID');
 const catalog=JSON.parse(a),geo=JSON.parse(b);if(catalog.format!=='kfm-kansas-public-ept-catalog-v1'||catalog.projects.length!==127||geo.type!=='FeatureCollection'||geo.features.length!==126)throw Error('LIDAR_CATALOG_INVALID');
 const projects=new Map();for(const p of catalog.projects){if(!/^[A-Za-z0-9_-]{1,160}$/.test(p.id)||p.eptUrl!==`https://usgs-lidar-public.s3.amazonaws.com/${p.id}/ept.json`||p.horizontalCrs!=='EPSG:3857'||p.dataType!=='laszip'||p.hierarchyType!=='json'||projects.has(p.id))throw Error('LIDAR_CATALOG_INVALID');projects.set(p.id,p);}
 const footprints=new Map(geo.features.map(f=>[f.properties.id,f.geometry]));discovery={catalog,projects,footprints};return discovery;
}
const intersects=(a,b)=>a[0]<b[2]&&a[2]>b[0]&&a[1]<b[3]&&a[3]>b[1];
const contains=(a,p)=>a[0]<=p[0]&&a[2]>=p[0]&&a[1]<=p[1]&&a[3]>=p[1];
function ringContains(ring,p){let inside=false;for(let i=0,j=ring.length-1;i<ring.length;j=i++){const a=ring[i],b=ring[j];if((a[1]>p[1])!==(b[1]>p[1])&&p[0]<(b[0]-a[0])*(p[1]-a[1])/(b[1]-a[1])+a[0])inside=!inside;}return inside;}
export function footprintContains(geometry,p){const polygons=geometry.type==='Polygon'?[geometry.coordinates]:geometry.type==='MultiPolygon'?geometry.coordinates:[];return polygons.some(poly=>ringContains(poly[0],p)&&!poly.slice(1).some(r=>ringContains(r,p)));}
export function viewProjects(query){const {projects,footprints}=loadLidarDiscovery();return [...projects.values()].filter(p=>intersects(p.boundsWgs84,query.bbox)&&(!footprints.has(p.id)||intersects(p.footprintBBoxWgs84,query.bbox)));}
export function selectViewProjects(query,max=16){
 const {footprints}=loadLidarDiscovery(),candidates=viewProjects(query),cells=[];
 for(let y=0;y<8;y++)for(let x=0;x<8;x++)cells.push([query.bbox[0]+(x+.5)/8*(query.bbox[2]-query.bbox[0]),query.bbox[1]+(y+.5)/8*(query.bbox[3]-query.bbox[1])]);
 const support=p=>new Set(cells.flatMap((c,i)=>contains(p.boundsWgs84,c)&&(!footprints.has(p.id)||footprintContains(footprints.get(p.id),c))?[i]:[]));
 const supports=new Map(candidates.map(p=>[p.id,support(p)])),covered=new Set(),selected=[];
 while(selected.length<max){let best=null,score=-1;for(const p of candidates){if(selected.includes(p))continue;const gain=[...supports.get(p.id)].filter(i=>!covered.has(i)).length;if(!gain)continue;const b=p.bounds3857,density=p.projectPointCount/((b[2]-b[0])*(b[3]-b[1]));const value=gain*1e9+Math.log1p(density);if(value>score){best=p;score=value;}}if(!best)break;selected.push(best);for(const i of supports.get(best.id))covered.add(i);}
 // A thin sliver may miss all discovery samples. Native support is still checked.
 if(!selected.length&&candidates.length)selected.push(candidates.sort((a,b)=>a.id.localeCompare(b.id))[0]);
 return selected;
}
export function lidarViewConfig(env=process.env){const root=env.KFM_LIDAR_VIEW_ROOT;return typeof root==='string'&&isAbsolute(root)?{root}:null;}
export function privateViewDir(path,create=false){
 if(create&&!lstatSafe(path))mkdirSync(path,{mode:0o700});
 if(!isAbsolute(path)||realpathSync(path)!==resolve(path))throw Error('LIDAR_STORAGE_UNSAFE');const s=lstatSync(path);if(!s.isDirectory()||s.uid!==process.getuid()||(s.mode&0o777)!==0o700)throw Error('LIDAR_STORAGE_UNSAFE');return path;
}
const lstatSafe=p=>{try{return lstatSync(p);}catch{return null;}};
export function readPrivateViewFile(path,max,sha=null){let fd;try{privateViewDir(dirname(path));fd=openSync(path,constants.O_RDONLY|constants.O_NOFOLLOW|constants.O_NONBLOCK);const before=fstatSync(fd);if(!before.isFile()||before.uid!==process.getuid()||(before.mode&0o777)!==0o600||before.nlink!==1||before.size<1||before.size>max)throw Error();const out=Buffer.alloc(before.size+1);let n=0,t;while(n<out.length&&(t=readSync(fd,out,n,out.length-n,null))>0)n+=t;const after=fstatSync(fd);if(n!==before.size||before.size!==after.size||before.ctimeMs!==after.ctimeMs||before.mtimeMs!==after.mtimeMs)throw Error();const bytes=out.subarray(0,n);if(sha&&digest(bytes)!==sha)throw Error();return bytes;}catch{throw Error('LIDAR_VIEW_NOT_READY');}finally{if(fd!==undefined)closeSync(fd);}}
export const viewAcquisition=p=>`Provider project ${p.id}; identifier year tokens ${(p.acquisition.identifierYearTokens??[]).join(', ')||'absent'} are not verified flight dates.`;
export const viewVertical=p=>p.verticalCrs?`EPT vertical code ${p.verticalCrs}; independent accuracy and map registration unverified.`:'EPT supplies no vertical code; native source reference and map registration are unverified.';
const areaKm2=q=>(q.bbox[2]-q.bbox[0])*111.32*Math.cos((q.bbox[1]+q.bbox[3])/2*Math.PI/180)*(q.bbox[3]-q.bbox[1])*111.32;
export function initialLidarView(input,state='processing',reason=null){
 const query=normalizeLidarView(input),key=lidarViewKey(query),candidates=viewProjects(query),detail=areaKm2(query)>1;
 const layers=['ground','surface','canopy','points'].map(kind=>({kind,state:kind==='ground'?'ready':!query.layers.includes(kind)?'idle':!candidates.length?'no-coverage':kind!=='points'&&detail?'detail-required':state,method:kind==='ground'?'USGS3DEP continuous DEM':kind==='points'?'Native multi-project EPT display LOD':'Complete same-survey native analysis required',message:kind==='ground'?'Continuous ground remains available across Kansas.':!query.layers.includes(kind)?'Layer is off.':!candidates.length?'No catalogued source footprint intersects this view.':kind!=='points'&&detail?'Zoom in to a view of at most 1 km² for complete native analysis; no surface/canopy is inferred from sparse points.':reason??'Preparing source-linked data for this map view.'}));
 const allDetail=query.layers.every(k=>k!=='points')&&detail;
 return {format:'kfm-lidar-view-v1',requestKey:key,query,generatedAt:new Date().toISOString(),state:!candidates.length?'no-coverage':allDetail?'detail-required':state,layers,coverage:candidates.map(p=>({project:p.id,eptUrl:p.eptUrl,boundsWgs84:p.boundsWgs84,acquisition:viewAcquisition(p),verticalReference:viewVertical(p),qualification:p.coverageQualification})),points:null,grid:null,reason,limits:LIDAR_VIEW_LIMITS};
}
export function requestLidarView(config,input){
 if(!config)throw Error('LIDAR_VIEW_NOT_CONFIGURED');const query=normalizeLidarView(input),key=lidarViewKey(query);privateViewDir(config.root);
 const jobs=privateViewDir(join(config.root,'jobs'),true),dir=join(jobs,key);if(!lstatSafe(dir)&&readdirSync(jobs).length>=2048)return initialLidarView(query,'unavailable','The bounded prepared-view store is full; existing files are preserved.');privateViewDir(dir,true);
 const readyPath=join(dir,'ready.json');if(lstatSafe(readyPath)){
  const receipt=JSON.parse(readPrivateViewFile(readyPath,4096));if(receipt.requestKey!==key||!/^sha256:[a-f0-9]{64}$/.test(receipt.viewSha256))throw Error('LIDAR_VIEW_NOT_READY');
  const view=JSON.parse(readPrivateViewFile(join(dir,'view.json'),900000,receipt.viewSha256));if(!validLidarView(view,query))throw Error('LIDAR_VIEW_NOT_READY');
  const failedAt=Date.parse(receipt.completedAt),attempts=readdirSync(jobs).filter(n=>n.startsWith('.failed-'+key+'-')).length;
  if(view.state!=='unavailable'||!Number.isFinite(failedAt)||Date.now()-failedAt<60000||attempts>=2||readdirSync(jobs).length>=2048)return view;
  // Keep failed receipts and any partial outputs. A later request can retry
  // transient public-source failures, at most three attempts for this key.
  try{renameSync(dir,join(jobs,'.failed-'+key+'-'+Date.now()+'-'+randomBytes(4).toString('hex')));privateViewDir(dir,true);}catch(e){if(e.code!=='ENOENT')throw e;return initialLidarView(query);}
 }
 const initial=initialLidarView(query);if(initial.state!=='processing')return initial;
 const queue=privateViewDir(join(config.root,'queue'),true),names=readdirSync(queue);if(names.length>=16&&!names.includes(key+'.json'))return initialLidarView(query,'unavailable','The bounded preparation queue is full; retry later.');
 const queued=join(queue,key+'.json');try{writeFileSync(queued,JSON.stringify({requestKey:key,query,requestedAt:new Date().toISOString()})+'\n',{mode:0o600,flag:'wx'});}catch(e){if(e.code!=='EEXIST')throw e;}
 return initial;
}
export function loadLidarViewReceipt(config,key){
 if(!config||!validViewKey(key))throw Error('QUERY_INVALID');privateViewDir(config.root);const dir=privateViewDir(join(config.root,'jobs',key)),r=JSON.parse(readPrivateViewFile(join(dir,'ready.json'),4096));
 if(r.requestKey!==key||!/^sha256:[a-f0-9]{64}$/.test(r.viewSha256))throw Error('LIDAR_VIEW_NOT_READY');const v=JSON.parse(readPrivateViewFile(join(dir,'view.json'),900000,r.viewSha256));if(!validLidarView(v,v.query)||v.requestKey!==key)throw Error('LIDAR_VIEW_NOT_READY');return v;
}
export function loadLidarViewArtifact(config,key,/** @type {number|'grid'} */ part){
 if(!config||!validViewKey(key)||part!=='grid'&&(!Number.isInteger(part)||part<0||part>15))throw Error('QUERY_INVALID');
 privateViewDir(config.root);const dir=privateViewDir(join(config.root,'jobs',key)),receipt=JSON.parse(readPrivateViewFile(join(dir,'ready.json'),4096));
 if(receipt.requestKey!==key||!/^sha256:[a-f0-9]{64}$/.test(receipt.viewSha256))throw Error('LIDAR_VIEW_NOT_READY');
 const v=JSON.parse(readPrivateViewFile(join(dir,'view.json'),900000,receipt.viewSha256));if(!validLidarView(v,v.query)||v.requestKey!==key)throw Error('LIDAR_VIEW_NOT_READY');
 if(part==='grid'){
  if(!v.grid||!/^sha256:[a-f0-9]{64}$/.test(receipt.gridSha256??''))throw Error('LIDAR_VIEW_NOT_READY');const g=JSON.parse(readPrivateViewFile(join(dir,'grid.json'),900000,receipt.gridSha256));if(!validLidarGrid(g,key)||g.width!==v.grid.width||g.height!==v.grid.height||g.source.project!==v.grid.sourceProject)throw Error('LIDAR_VIEW_NOT_READY');return g;
 }
 if(!v.points||!validNativeViewManifest(v.points,key)||!v.points.chunks[part])throw Error('LIDAR_VIEW_NOT_READY');
 const c=v.points.chunks[part],bytes=readPrivateViewFile(join(dir,`chunk-${part}.json`),900000,c.sha256),body=JSON.parse(bytes);
 if(c.bytes!==bytes.length||!validNativeViewChunk(body,v.points,key,part))throw Error('LIDAR_VIEW_NOT_READY');return body;
}

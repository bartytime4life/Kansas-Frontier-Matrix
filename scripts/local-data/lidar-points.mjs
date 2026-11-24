// Fixed, owner-private, hash-pinned derived native LiDAR return packages.
// No acquisition, directory browsing or visitor-selected path/URL.
import {constants,openSync,closeSync,fstatSync,lstatSync,readSync,realpathSync} from 'node:fs';
import {isAbsolute,resolve,join} from 'node:path';
import {createHash} from 'node:crypto';

export const LIDAR_POINTS_ROUTE='/v1/lidar/points';
export const LIDAR_POINTS_COLUMNS=Object.freeze(['x','y','z','intensity','classification','returnNumber','numberOfReturns','classFlags','gpsTime','asset','record']);
export const LIDAR_POINTS_MAX_CHUNKS=16;
export const LIDAR_POINTS_MAX_POINTS=100000;
export const LIDAR_POINTS_MAX_BYTES=900000;
export const LIDAR_POINTS_MANIFEST_MAX_BYTES=64000;
const EPT='https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept.json';
const object=v=>v!==null&&typeof v==='object'&&!Array.isArray(v);
const keys=(v,names)=>object(v)&&Object.keys(v).sort().join(',')===names.split(',').sort().join(',');
const finite=v=>typeof v==='number'&&Number.isFinite(v);
const integer=(v,min,max)=>Number.isSafeInteger(v)&&v>=min&&v<=max;
const hash=v=>typeof v==='string'&&/^sha256:[a-f0-9]{64}$/.test(v);
const text=(v,max=1000)=>typeof v==='string'&&v.length>0&&v.length<=max&&!/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(v);
const instant=v=>typeof v==='string'&&/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?Z$/.test(v)&&Number.isFinite(Date.parse(v));
const fail=()=>Object.assign(new Error('LIDAR_POINTS_NOT_READY'),{code:'LIDAR_POINTS_NOT_READY'});
function publicSafe(v,depth=0){
 if(depth>16)return false;
 if(typeof v==='string')return !/[?&](?:X-Amz-|X-Goog-|Signature=|GoogleAccessId=|apiToken=)/i.test(v);
 if(Array.isArray(v))return v.every(x=>publicSafe(x,depth+1));
 if(object(v))return Object.entries(v).every(([k,x])=>!/token|secret|password|signature/i.test(k)&&publicSafe(x,depth+1));
 return v===null||typeof v==='boolean'||finite(v);
}
export function validLidarPointsManifest(m){
 if(!keys(m,'format,captureId,generatedAt,source,review,pointCount,bounds3857,heightRange,chunks,columns')||m.format!=='kfm-lidar-points-manifest-v1'||!text(m.captureId,80)||!/^[a-z0-9-]+$/.test(m.captureId)||!instant(m.generatedAt)
  ||!integer(m.pointCount,1,LIDAR_POINTS_MAX_POINTS)||!Array.isArray(m.columns)||m.columns.join(',')!==LIDAR_POINTS_COLUMNS.join(',')
  ||!Array.isArray(m.bounds3857)||m.bounds3857.length!==4||!m.bounds3857.every(finite)||m.bounds3857[0]>=m.bounds3857[2]||m.bounds3857[1]>=m.bounds3857[3]
  ||m.bounds3857.some(x=>Math.abs(x)>20037509)||m.bounds3857[2]-m.bounds3857[0]>10000||m.bounds3857[3]-m.bounds3857[1]>10000
  ||!Array.isArray(m.heightRange)||m.heightRange.length!==2||!m.heightRange.every(finite)||m.heightRange[0]>m.heightRange[1]||m.heightRange[0]<-12000||m.heightRange[1]>9000)return false;
 const r=m.review,s=m.source;
 if(!keys(r,'status,source_admitted,released,scientific_accuracy_verified')||r.status!=='pending'||r.source_admitted!==false||r.released!==false||r.scientific_accuracy_verified!==false
  ||!keys(s,'provider,project,eptUrl,horizontalCrs,verticalReference,acquisition,coordinateEncodingM,selection,assets,notes')||s.provider!=='USGS'||s.project!=='KS_Statewide_B6A_2018'||s.eptUrl!==EPT||s.horizontalCrs!=='EPSG:3857'
  ||!text(s.verticalReference)||!text(s.acquisition)||!text(s.selection)||!Array.isArray(s.coordinateEncodingM)||s.coordinateEncodingM.length!==3||!s.coordinateEncodingM.every(x=>finite(x)&&x>0&&x<=1)
  ||!Array.isArray(s.notes)||s.notes.length<1||s.notes.length>20||!s.notes.every(x=>text(x))||!Array.isArray(s.assets)||s.assets.length<1||s.assets.length>32)return false;
 if(!s.assets.every((a,i)=>keys(a,'id,url,sha256,bytes,pointCount')&&a.id===i&&hash(a.sha256)&&integer(a.bytes,1,200000000)&&integer(a.pointCount,1,10000000)&&typeof a.url==='string'
  &&/^https:\/\/usgs-lidar-public\.s3\.amazonaws\.com\/KS_Statewide_B6A_2018\/ept-data\/\d{1,2}-\d{1,6}-\d{1,6}-\d{1,6}\.laz$/.test(a.url)))return false;
 if(!Array.isArray(m.chunks)||m.chunks.length<1||m.chunks.length>LIDAR_POINTS_MAX_CHUNKS
  ||!m.chunks.every((c,i)=>keys(c,'id,pointCount,bytes,sha256')&&c.id===i&&integer(c.pointCount,1,15000)&&integer(c.bytes,1,LIDAR_POINTS_MAX_BYTES)&&hash(c.sha256))
  ||m.chunks.reduce((n,c)=>n+c.pointCount,0)!==m.pointCount)return false;
 return publicSafe(m);
}
export function validLidarPointsChunk(c,m,id){
 if(!validLidarPointsManifest(m)||!integer(id,0,m.chunks.length-1)||!keys(c,'format,captureId,chunkId,points')||c.format!=='kfm-lidar-points-chunk-v1'||c.captureId!==m.captureId||c.chunkId!==id
  ||!Array.isArray(c.points)||c.points.length!==m.chunks[id].pointCount)return false;
 const [west,south,east,north]=m.bounds3857,[bottom,top]=m.heightRange,seen=new Set();
 for(const row of c.points){
  if(!Array.isArray(row)||row.length!==11||!row.every(finite)||row[0]<west||row[0]>east||row[1]<south||row[1]>north||row[2]<bottom||row[2]>top
   ||!integer(row[3],0,65535)||!integer(row[4],0,255)||!integer(row[5],0,15)||!integer(row[6],0,15)||!integer(row[7],0,15)
   ||!integer(row[9],0,m.source.assets.length-1)||!integer(row[10],0,m.source.assets[row[9]].pointCount-1))return false;
  const key=row[9]+':'+row[10];if(seen.has(key))return false;seen.add(key);
 }
 return publicSafe(c);
}
export function lidarPointsConfig(env=process.env){
 const directory=env.KFM_LIDAR_POINTS_DIR,manifestSha256=env.KFM_LIDAR_POINTS_MANIFEST_SHA256;
 return typeof directory==='string'&&isAbsolute(directory)&&hash(manifestSha256)?{directory,manifestSha256}:null;
}
function pinnedFile(directory,name,expected,max){
 let fd;
 try{
  if(!isAbsolute(directory)||realpathSync(directory)!==resolve(directory))throw fail();
  const parent=lstatSync(directory);if(!parent.isDirectory()||parent.uid!==process.getuid()||(parent.mode&0o777)!==0o700)throw fail();
  fd=openSync(join(directory,name),constants.O_RDONLY|constants.O_NOFOLLOW|constants.O_NONBLOCK);
  const before=fstatSync(fd);if(!before.isFile()||before.uid!==process.getuid()||(before.mode&0o777)!==0o600||before.nlink!==1||before.size<1||before.size>max)throw fail();
  const buffer=Buffer.alloc(before.size+1);let length=0,n;
  while(length<buffer.length&&(n=readSync(fd,buffer,length,buffer.length-length,null))>0)length+=n;
  const after=fstatSync(fd);if(length!==before.size||before.size!==after.size||before.mtimeMs!==after.mtimeMs||before.ctimeMs!==after.ctimeMs)throw fail();
  const bytes=buffer.subarray(0,length);if('sha256:'+createHash('sha256').update(bytes).digest('hex')!==expected)throw fail();
  return {value:JSON.parse(bytes.toString('utf8')),bytes:length};
 }catch{throw fail();}finally{if(fd!==undefined)closeSync(fd);}
}
export function loadLidarPoints(config,id=null){
 if(!config||!hash(config.manifestSha256))throw fail();
 const m=pinnedFile(config.directory,'manifest.json',config.manifestSha256,LIDAR_POINTS_MANIFEST_MAX_BYTES).value;
 if(!validLidarPointsManifest(m))throw fail();
 if(id===null)return m;
 if(!integer(id,0,m.chunks.length-1))throw fail();
 const c=pinnedFile(config.directory,`chunk-${id}.json`,m.chunks[id].sha256,LIDAR_POINTS_MAX_BYTES);
 if(c.bytes!==m.chunks[id].bytes||!validLidarPointsChunk(c.value,m,id))throw fail();
 return c.value;
}

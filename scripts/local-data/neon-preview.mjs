// Dev-only: read one explicitly configured, hash-pinned derived NEON pilot.
// No download, token access, directory listing, or visitor-selected filesystem path.
import {constants,openSync,closeSync,fstatSync,lstatSync,readSync,realpathSync} from 'node:fs';
import {isAbsolute,dirname,resolve} from 'node:path';
import {createHash} from 'node:crypto';

export const NEON_PREVIEW_ROUTE='/v1/neon/preview';
export const NEON_PREVIEW_MAX_BYTES=950000;
export const NEON_PREVIEW_FORMAT='kfm-neon-relay-pilot-v1';
const fail=()=>Object.assign(new Error('NEON_PREVIEW_NOT_READY'),{code:'NEON_PREVIEW_NOT_READY'});
const object=value=>value!==null&&typeof value==='object'&&!Array.isArray(value);
const instant=value=>typeof value==='string'&&value.length<=40&&Number.isFinite(Date.parse(value));
function publicShape(value){
 if(!object(value)||Object.keys(value).sort().join(',')!=='format,generatedAt,preview,review'||value.format!==NEON_PREVIEW_FORMAT||!instant(value.generatedAt))return false;
 const p=value.preview,r=value.review;
 if(!object(p)||p.schema_version!=='kfm-neon-lidar-preview-v1'||p.data_kind!=='provider-files'||p.source_admitted!==false||p.released!==false
  ||p.source?.site!=='KONZ'||p.source?.month!=='2024-09'||p.source?.release!=='RELEASE-2026'
  ||p.source?.tile!=='NEON_D06_KONZ_DP3_706000_4336000'||p.source?.acquisition_run!=='2024_KONZ_10')return false;
 const g=p.grid;
 if(!object(g)||!Number.isInteger(g.width)||g.width<8||g.width>128||g.height!==g.width
  ||!['dtm','dsm','chm'].every(kind=>Array.isArray(g[kind])&&g[kind].length===g.width*g.height&&g[kind].every(x=>x===null||typeof x==='number'&&Number.isFinite(x))))return false;
 if(!object(r)||r.status!=='pending'||r.scientific_accuracy_verified!==false||r.source_admitted!==false
  ||!Number.isFinite(r.canopy_native_max_m)||r.canopy_native_max_m<0
  ||!Number.isInteger(r.canopy_native_cells_above_50m)||r.canopy_native_cells_above_50m<0||r.canopy_native_cells_above_50m>1000000
  ||!Number.isFinite(r.surface_minus_ground_native_max_m)
  ||!Array.isArray(r.notes)||r.notes.length<1||r.notes.length>8||r.notes.some(note=>typeof note!=='string'||note.length<1||note.length>400))return false;
 // The operator pins a derived package, never a private API listing. Refuse credential-like
 // fields and signed capabilities even if a wrong file was accidentally configured.
 const safe=(node,depth=0)=>{
  if(depth>16)return false;
  if(typeof node==='string')return !/[?&](?:X-Goog-|Signature=|GoogleAccessId=|apiToken=)/i.test(node);
  if(Array.isArray(node))return node.every(item=>safe(item,depth+1));
  if(object(node))return Object.entries(node).every(([key,item])=>!/token|secret|password|signature/i.test(key)&&safe(item,depth+1));
  return node===null||typeof node==='boolean'||typeof node==='number'&&Number.isFinite(node);
 };
 return safe(value);
}

export function neonPreviewConfig(env=process.env){
 const path=env.KFM_NEON_PREVIEW_FILE,sha256=env.KFM_NEON_PREVIEW_SHA256;
 if(typeof path!=='string'||!isAbsolute(path)||typeof sha256!=='string'||!/^sha256:[a-f0-9]{64}$/.test(sha256))return null;
 return {path,sha256};
}

export function loadNeonPreview(config){
 let fd;
 try{
  if(!config||!isAbsolute(config.path)||realpathSync(config.path)!==resolve(config.path)||!/^sha256:[a-f0-9]{64}$/.test(config.sha256))throw fail();
  const parent=lstatSync(dirname(config.path));
  if(!parent.isDirectory()||parent.uid!==process.getuid()||(parent.mode&0o777)!==0o700)throw fail();
  fd=openSync(config.path,constants.O_RDONLY|constants.O_NOFOLLOW|constants.O_NONBLOCK);
  const before=fstatSync(fd);
  if(!before.isFile()||before.uid!==process.getuid()||(before.mode&0o777)!==0o600||before.nlink!==1||before.size<1||before.size>NEON_PREVIEW_MAX_BYTES)throw fail();
  const buffer=Buffer.alloc(before.size+1);let length=0,read;
  while(length<buffer.length&&(read=readSync(fd,buffer,length,buffer.length-length,null))>0)length+=read;
  const after=fstatSync(fd);
  if(length!==before.size||before.size!==after.size||before.mtimeMs!==after.mtimeMs||before.ctimeMs!==after.ctimeMs)throw fail();
  const bytes=buffer.subarray(0,length);
  if('sha256:'+createHash('sha256').update(bytes).digest('hex')!==config.sha256)throw fail();
  const value=JSON.parse(bytes.toString('utf8'));
  if(!publicShape(value))throw fail();
  return value;
 }catch{throw fail();}finally{if(fd!==undefined)closeSync(fd);}
}

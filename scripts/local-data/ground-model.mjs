import {createHash} from 'node:crypto';
export const GROUND_SERVICE='https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer';
export const GROUND_ROUTE='/v1/terrain/ground';
export const GROUND_SIZE=96;
const exact=(v,k)=>v&&typeof v==='object'&&!Array.isArray(v)&&Object.keys(v).sort().join(',')===k.split(',').sort().join(',');
const finite=n=>typeof n==='number'&&Number.isFinite(n),integer=(n,a,b)=>Number.isSafeInteger(n)&&n>=a&&n<=b;
const text=(s,max=2000)=>typeof s==='string'&&s.length>0&&s.length<=max&&!/[\u0000-\u001f\u007f]/.test(s);
const instant=s=>typeof s==='string'&&/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?Z$/.test(s)&&Number.isFinite(Date.parse(s));
const sha=s=>typeof s==='string'&&/^sha256:[a-f0-9]{64}$/.test(s);
export function normalizeGroundQuery(v){
 if(!exact(v,'bbox,size')||v.size!==96||!Array.isArray(v.bbox)||v.bbox.length!==4||!v.bbox.every(finite)||v.bbox[0]<-102.2||v.bbox[2]>-94.4||v.bbox[1]<36.8||v.bbox[3]>40.2)throw Error('QUERY_INVALID');
 const q={bbox:v.bbox.map(n=>Math.round(n*1e5)/1e5),size:96};if(q.bbox[0]>=q.bbox[2]||q.bbox[1]>=q.bbox[3])throw Error('QUERY_INVALID');return q;
}
export function parseGroundSearch(s){
 if(s.size!==2||[...s.keys()].some(k=>!['bbox','size'].includes(k)||s.getAll(k).length!==1))throw Error('QUERY_INVALID');
 const number=s=>/^-?(?:\d+(?:\.\d+)?|\.\d+)$/.test(s??'')?Number(s):NaN;
 return normalizeGroundQuery({bbox:(s.get('bbox')??'').split(',').map(number),size:number(s.get('size'))});
}
export const groundKey=q=>createHash('sha256').update(JSON.stringify(normalizeGroundQuery(q))).digest('hex');
export function groundBounds(q){const [w,s,e,n]=normalizeGroundQuery(q).bbox,R=6378137,rad=Math.PI/180;return [R*w*rad,R*Math.log(Math.tan(Math.PI/4+s*rad/2)),R*e*rad,R*Math.log(Math.tan(Math.PI/4+n*rad/2))];}
export function groundSourceUrl(query){return GROUND_SERVICE+'/exportImage?'+new URLSearchParams({bbox:groundBounds(query).join(','),bboxSR:'3857',imageSR:'3857',size:'96,96',format:'tiff',pixelType:'F32',f:'image',interpolation:'RSP_NearestNeighbor',adjustAspectRatio:'false'});}
export function groundCatalogUrl(query){return GROUND_SERVICE+'/query?'+new URLSearchParams({f:'json',where:'1=1',geometry:normalizeGroundQuery(query).bbox.join(','),geometryType:'esriGeometryEnvelope',inSR:'4326',spatialRel:'esriSpatialRelIntersects',returnGeometry:'false',outFields:'OBJECTID,Name,DEM_Type,Source,VerticalDatum,AcquisitionDate,StartDate,EndDate,Resolution_X,Resolution_Y,Metadata',resultRecordCount:'100',orderByFields:'OBJECTID'});}
function validCatalog(c,q){
 if(!exact(c,'state,url,sha256,bytes,retrievedAt,complete,candidateCount,candidates')||!['available','unavailable'].includes(c.state)||c.url!==groundCatalogUrl(q)||typeof c.complete!=='boolean'||!integer(c.candidateCount,0,100)||!Array.isArray(c.candidates)||c.candidates.length!==c.candidateCount)return false;
 if(c.state==='unavailable')return c.sha256===null&&c.bytes===0&&c.retrievedAt===null&&!c.complete&&c.candidateCount===0;
 return sha(c.sha256)&&integer(c.bytes,1,2000000)&&instant(c.retrievedAt)&&c.candidates.every(r=>exact(r,'id,name,demType,source,verticalDatum,acquisitionDate,startDate,endDate,resolutionX,resolutionY,metadataUrl')&&integer(r.id,0,1e10)&&['name','source','verticalDatum','metadataUrl'].every(k=>r[k]===null||text(r[k]))&&['demType','acquisitionDate','startDate','endDate'].every(k=>r[k]===null||finite(r[k])||text(r[k],200))&&['resolutionX','resolutionY'].every(k=>r[k]===null||finite(r[k]))&&(!r.metadataUrl||r.metadataUrl.startsWith('https://')));
}
export function validGroundView(v,input){
 let q;try{q=normalizeGroundQuery(input);}catch{return false;}
 if(!exact(v,'format,requestKey,query,generatedAt,state,reason,grid')||v.format!=='kfm-ground-view-v1'||v.requestKey!==groundKey(q)||JSON.stringify(v.query)!==JSON.stringify(q)||!instant(v.generatedAt)||!['processing','ready','partial','no-coverage','unavailable'].includes(v.state)||!(v.reason===null||text(v.reason)))return false;
 if(v.grid===null)return ['processing','unavailable'].includes(v.state);
 const g=v.grid;if(!exact(g,'format,requestKey,width,height,bounds3857,cellSize3857,ground,excludedValues,source,method,review')||g.format!=='kfm-3dep-ground-grid-v1'||g.requestKey!==v.requestKey||g.width!==96||g.height!==96||!integer(g.excludedValues,0,9216))return false;
 const b=groundBounds(q);if(!Array.isArray(g.bounds3857)||g.bounds3857.length!==4||!g.bounds3857.every((n,i)=>finite(n)&&Math.abs(n-b[i])<=1e-5)||!Array.isArray(g.cellSize3857)||g.cellSize3857.length!==2||!g.cellSize3857.every((n,i)=>finite(n)&&n>0&&Math.abs(n-(b[i+2]-b[i])/96)<=1e-6)||!Array.isArray(g.ground)||g.ground.length!==9216||!g.ground.every(n=>n===null||finite(n)&&n>=-12000&&n<=9000&&Math.fround(n)===n))return false;
 const count=g.ground.filter(n=>n!==null).length;if(v.state!==(count===9216?'ready':count?'partial':'no-coverage'))return false;
 const s=g.source;if(!exact(s,'provider,service,requestUrl,sha256,bytes,retrievedAt,horizontalCrs,verticalReference,acquisition,catalog')||s.provider!=='USGS'||s.service!==GROUND_SERVICE||s.requestUrl!==groundSourceUrl(q)||!sha(s.sha256)||!integer(s.bytes,1,2000000)||!instant(s.retrievedAt)||s.horizontalCrs!=='EPSG:3857'||!text(s.verticalReference)||!text(s.acquisition)||!validCatalog(s.catalog,q))return false;
 const m=g.method,r=g.review;return exact(m,'sampling,output,nativeResolution,catalogRole,limitations')&&m.sampling==='nearest-neighbor'&&m.output==='provider-resampled-F32-DEM'&&m.nativeResolution==='mixed; output spacing is not native resolution'&&m.catalogRole==='intersecting candidates, not per-cell lineage'&&Array.isArray(m.limitations)&&m.limitations.length<=16&&m.limitations.every(s=>text(s))&&exact(r,'status,source_admitted,released,scientific_accuracy_verified')&&r.status==='pending'&&r.source_admitted===false&&r.released===false&&r.scientific_accuracy_verified===false;
}

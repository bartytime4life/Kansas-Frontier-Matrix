/** Provider-resampled DEM samples are distinct from native laser-return analysis. */
export const GROUND_SIZE=96 as const;
export const GROUND_SERVICE='https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer';
const R=6378137,WINDOW=[-102.2,36.8,-94.4,40.2] as const;
export type GroundQuery={bbox:[number,number,number,number];size:96};
export type GroundCatalogCandidate={id:number;name:string|null;demType:string|number|null;source:string|null;verticalDatum:string|null;acquisitionDate:string|number|null;startDate:string|number|null;endDate:string|number|null;resolutionX:number|null;resolutionY:number|null;metadataUrl:string|null};
export type GroundGrid={format:'kfm-3dep-ground-grid-v1';requestKey:string;width:96;height:96;bounds3857:[number,number,number,number];cellSize3857:[number,number];ground:(number|null)[];excludedValues:number;source:{provider:'USGS';service:typeof GROUND_SERVICE;requestUrl:string;sha256:string;bytes:number;retrievedAt:string;horizontalCrs:'EPSG:3857';verticalReference:string;acquisition:string;catalog:{state:'available'|'unavailable';url:string;sha256:string|null;bytes:number;retrievedAt:string|null;complete:boolean;candidateCount:number;candidates:GroundCatalogCandidate[]}};method:{sampling:'nearest-neighbor';output:'provider-resampled-F32-DEM';nativeResolution:'mixed; output spacing is not native resolution';catalogRole:'intersecting candidates, not per-cell lineage';limitations:string[]};review:{status:'pending';source_admitted:false;released:false;scientific_accuracy_verified:false}};
export type GroundReceipt={format:'kfm-ground-view-v1';requestKey:string;query:GroundQuery;generatedAt:string;state:'processing'|'ready'|'partial'|'no-coverage'|'unavailable';reason:string|null;grid:GroundGrid|null;cache:{state:'live'|'fresh'|'stale';at:string}};
const object=(v:unknown):v is Record<string,unknown>=>!!v&&typeof v==='object'&&!Array.isArray(v);
const finite=(v:unknown):v is number=>typeof v==='number'&&Number.isFinite(v);
const integer=(v:unknown,min:number,max:number):v is number=>Number.isSafeInteger(v)&&Number(v)>=min&&Number(v)<=max;
const text=(v:unknown,max=5000):v is string=>typeof v==='string'&&v.length>0&&v.length<=max&&!/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(v);
const utc=(v:unknown):v is string=>typeof v==='string'&&/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{1,6})?Z$/.test(v)&&Number.isFinite(Date.parse(v))&&new Date(v).toISOString().slice(0,19)===v.slice(0,19);
const keys=(v:Record<string,unknown>,fields:string[])=>Object.keys(v).length===fields.length&&fields.every(k=>Object.hasOwn(v,k));
const hash=(v:unknown):v is string=>typeof v==='string'&&/^sha256:[a-f0-9]{64}$/.test(v);
const https=(v:unknown)=>{if(!text(v,12000))return false;try{const u=new URL(v);return u.protocol==='https:'&&!u.username&&!u.password&&!u.hash;}catch{return false;}};
export function canonicalGroundQuery(bounds:readonly number[]):GroundQuery|null{
 if(bounds.length!==4||!bounds.every(finite)||bounds[0]>=bounds[2]||bounds[1]>=bounds[3])return null;
 const bbox=[Math.max(bounds[0],WINDOW[0]),Math.max(bounds[1],WINDOW[1]),Math.min(bounds[2],WINDOW[2]),Math.min(bounds[3],WINDOW[3])].map(v=>Math.round(v*1e5)/1e5) as GroundQuery['bbox'];
 return bbox[0]<bbox[2]&&bbox[1]<bbox[3]?{bbox,size:GROUND_SIZE}:null;
}
export const groundPath=(q:GroundQuery)=>'/api/terrain/ground?bbox='+q.bbox.join(',')+'&size=96';
export async function groundRequestKey(query:GroundQuery){const bytes=new TextEncoder().encode(JSON.stringify(query)),digest=await globalThis.crypto.subtle.digest('SHA-256',bytes);return Array.from(new Uint8Array(digest),v=>v.toString(16).padStart(2,'0')).join('');}
export const groundMercator=(longitude:number,latitude:number):[number,number]=>[R*longitude*(Math.PI/180),R*Math.log(Math.tan(Math.PI/4+latitude*(Math.PI/180)/2))];
export const groundWgs84=(x:number,y:number):[number,number]=>[x/R*180/Math.PI,(2*Math.atan(Math.exp(y/R))-Math.PI/2)*180/Math.PI];
function candidate(v:unknown):boolean{
 if(!object(v)||!keys(v,['id','name','demType','source','verticalDatum','acquisitionDate','startDate','endDate','resolutionX','resolutionY','metadataUrl'])||!integer(v.id,0,Number.MAX_SAFE_INTEGER))return false;
 for(const name of ['name','source','verticalDatum'])if(v[name]!==null&&!text(v[name],2000))return false;
 for(const name of ['demType','acquisitionDate','startDate','endDate'])if(v[name]!==null&&!finite(v[name])&&!text(v[name],2000))return false;
 return ['resolutionX','resolutionY'].every(k=>v[k]===null||finite(v[k]))&&(v.metadataUrl===null||https(v.metadataUrl));
}
export const groundCatalogUrl=(query:GroundQuery)=>GROUND_SERVICE+'/query?'+new URLSearchParams({f:'json',where:'1=1',geometry:query.bbox.join(','),geometryType:'esriGeometryEnvelope',inSR:'4326',spatialRel:'esriSpatialRelIntersects',returnGeometry:'false',outFields:'OBJECTID,Name,DEM_Type,Source,VerticalDatum,AcquisitionDate,StartDate,EndDate,Resolution_X,Resolution_Y,Metadata',resultRecordCount:'100',orderByFields:'OBJECTID'});
function providerRequest(value:unknown,query:GroundQuery){
 if(!https(value))return false;const u=new URL(value as string),q=u.searchParams,b=groundMercator(query.bbox[0],query.bbox[1]),t=groundMercator(query.bbox[2],query.bbox[3]);
 if(q.size!==9||u.origin+u.pathname!==GROUND_SERVICE+'/exportImage')return false;
 for(const [k,v] of Object.entries({bboxSR:'3857',imageSR:'3857',size:'96,96',format:'tiff',pixelType:'F32',f:'image',interpolation:'RSP_NearestNeighbor',adjustAspectRatio:'false'}))if(q.getAll(k).length!==1||q.get(k)!==v)return false;
 const bounds=q.get('bbox')?.split(',').map(Number);return q.getAll('bbox').length===1&&!!bounds&&bounds.length===4&&bounds.every((v,i)=>finite(v)&&Math.abs(v-[...b,...t][i])<.001);
}
export function parseGroundReceipt(v:unknown,query:GroundQuery,requestKey:string):GroundReceipt|null{
 if(!object(v)||!keys(v,['format','requestKey','query','generatedAt','state','reason','grid','cache'])||v.format!=='kfm-ground-view-v1'||v.requestKey!==requestKey||!/^[a-f0-9]{64}$/.test(requestKey)||!object(v.query)||!keys(v.query,['bbox','size'])||JSON.stringify(v.query)!==JSON.stringify(query)||!utc(v.generatedAt)||!['processing','ready','partial','no-coverage','unavailable'].includes(String(v.state))||!(v.reason===null||text(v.reason))||!object(v.cache)||!keys(v.cache,['state','at'])||!['live','fresh','stale'].includes(String(v.cache.state))||!utc(v.cache.at))return null;
 if(v.grid===null)return ['ready','partial'].includes(String(v.state))?null:structuredClone(v) as GroundReceipt;
 const g=v.grid;if(!['ready','partial','no-coverage'].includes(String(v.state))||!object(g)||!keys(g,['format','requestKey','width','height','bounds3857','cellSize3857','ground','excludedValues','source','method','review'])||g.format!=='kfm-3dep-ground-grid-v1'||g.requestKey!==requestKey||g.width!==GROUND_SIZE||g.height!==GROUND_SIZE)return null;
 const b=g.bounds3857,cell=g.cellSize3857,n=GROUND_SIZE*GROUND_SIZE,lo=groundMercator(query.bbox[0],query.bbox[1]),hi=groundMercator(query.bbox[2],query.bbox[3]);
 if(!Array.isArray(b)||b.length!==4||!b.every(finite)||!b.every((x,i)=>Math.abs(x-[...lo,...hi][i])<=1e-5)||b[0]>=b[2]||b[1]>=b[3]||!Array.isArray(cell)||cell.length!==2||!cell.every(x=>finite(x)&&x>0)||Math.abs(cell[0]*GROUND_SIZE-(b[2]-b[0]))>.001||Math.abs(cell[1]*GROUND_SIZE-(b[3]-b[1]))>.001)return null;
 if(!Array.isArray(g.ground)||g.ground.length!==n||!g.ground.every(x=>x===null||finite(x)&&x>=-12000&&x<=9000&&Math.fround(x)===x)||!integer(g.excludedValues,0,n))return null;
 const count=g.ground.filter(x=>x!==null).length;if(v.state!==(count===n?'ready':count?'partial':'no-coverage'))return null;
 const s=g.source,m=g.method,r=g.review;
 if(!object(s)||!keys(s,['provider','service','requestUrl','sha256','bytes','retrievedAt','horizontalCrs','verticalReference','acquisition','catalog'])||s.provider!=='USGS'||s.service!==GROUND_SERVICE||!providerRequest(s.requestUrl,query)||!hash(s.sha256)||!integer(s.bytes,1,2_000_000)||!utc(s.retrievedAt)||s.horizontalCrs!=='EPSG:3857'||!text(s.verticalReference)||!text(s.acquisition))return null;
 const c=s.catalog;if(!object(c)||!keys(c,['state','url','sha256','bytes','retrievedAt','complete','candidateCount','candidates'])||!['available','unavailable'].includes(String(c.state))||c.url!==groundCatalogUrl(query)||!(c.sha256===null||hash(c.sha256))||!integer(c.bytes,0,2_000_000)||!(c.retrievedAt===null||utc(c.retrievedAt))||typeof c.complete!=='boolean'||!integer(c.candidateCount,0,100)||!Array.isArray(c.candidates)||c.candidates.length>100||c.candidates.length!==c.candidateCount||!c.candidates.every(candidate)||c.complete&&c.candidateCount!==c.candidates.length||c.state==='available'&&(!hash(c.sha256)||c.bytes===0||!utc(c.retrievedAt)))return null;
 if(c.state==='unavailable'&&(c.sha256!==null||c.bytes!==0||c.retrievedAt!==null||c.complete||c.candidateCount!==0))return null;
 if(!object(m)||!keys(m,['sampling','output','nativeResolution','catalogRole','limitations'])||m.sampling!=='nearest-neighbor'||m.output!=='provider-resampled-F32-DEM'||m.nativeResolution!=='mixed; output spacing is not native resolution'||m.catalogRole!=='intersecting candidates, not per-cell lineage'||!Array.isArray(m.limitations)||m.limitations.length>16||!m.limitations.every(x=>text(x,2000))||!object(r)||!keys(r,['status','source_admitted','released','scientific_accuracy_verified'])||r.status!=='pending'||r.source_admitted!==false||r.released!==false||r.scientific_accuracy_verified!==false)return null;
 return structuredClone(v) as GroundReceipt;
}
export function groundCorners(grid:GroundGrid):[number,number][]{return Array.from({length:(grid.width+1)*(grid.height+1)},(_,i)=>groundWgs84(grid.bounds3857[0]+i%(grid.width+1)*grid.cellSize3857[0],grid.bounds3857[3]-Math.floor(i/(grid.width+1))*grid.cellSize3857[1]));}
export function groundCell(grid:GroundGrid,index:number){
 if(!Number.isInteger(index)||index<0||index>=grid.width*grid.height)return null;
 const row=Math.floor(index/grid.width),column=index%grid.width,x=grid.bounds3857[0]+(column+.5)*grid.cellSize3857[0],y=grid.bounds3857[3]-(row+.5)*grid.cellSize3857[1],[longitude,latitude]=groundWgs84(x,y);
 return {row:row+1,column:column+1,ground:grid.ground[index],x3857:x,y3857:y,longitude,latitude,approximateSpacingM:grid.cellSize3857.map(v=>v*Math.cos(latitude*Math.PI/180))};
}

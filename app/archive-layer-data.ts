import type { Feature, FeatureCollection, Geometry, Position } from 'geojson';
import type { ArchiveLayer } from './archive-layer-catalog';
import { readBoundedJson } from './bounded-json';

export type ArchiveRow = Record<string, unknown>;
export type ArchiveAnswer = {
  dataset: string; total: number | null; count: number; rows: ArchiveRow[]; source: { provider: string; notes: string; coverage: string };
  hasMore?: boolean; nextCursor?: string | null; collection?: string;
  fieldChunk?: {field:string;start:number;nextStart:number|null;characters:number};
  generatedAt: string; cache?: { state: string; at: string }; unit?: string | null;
};
export type ArchiveProperties = { key: string; label: string; value: number | null; unit: string; period: string };
const record = (v: unknown): v is ArchiveRow => !!v && typeof v === 'object' && !Array.isArray(v);
const finite = (v: unknown): v is number => typeof v === 'number' && Number.isFinite(v);
export const textValue = (v: unknown): string => v === null || v === undefined ? 'Not supplied' : typeof v === 'object' ? JSON.stringify(v) : String(v);
export const rowKey = (row: ArchiveRow, index: number) => String(row.id ?? row.site ?? row.eventId ?? row.featureId ?? (record(row.county) ? row.county.geoid : undefined) ?? index);
export const rowLabel = (row: ArchiveRow, index: number) => {
  if(record(row.values)){
    const values=row.values;
    const label=['name','primary_name','title','label','oas_number','structure_number_008','station_id','registry_id','feature_name','lccn'].map(k=>values[k]).find(v=>typeof v==='string'&&v.trim()||typeof v==='number');
    return label!==undefined?String(label):`Record ${values.row_number??index+1}`;
  }
  return String(row.name ?? row.site ?? (record(row.county) ? row.county.name : undefined) ?? (record(row.properties) ? row.properties.headline ?? row.properties.place ?? row.properties.event : undefined) ?? row.type ?? row.id ?? row.featureId ?? `Record ${index + 1}`);
};

/** No geocoding, county-centroid substitution or inferred storm tracks. */
export function validArchiveGeometry(value: unknown): Geometry | null {
  if (!record(value) || typeof value.type !== 'string') return null;
  let vertices = 0;
  const pos = (v: unknown): v is Position => Array.isArray(v) && v.length >= 2 && finite(v[0]) && finite(v[1]) && Math.abs(v[0]) <= 180 && Math.abs(v[1]) <= 90 && ++vertices <= 120000;
  const line = (v: unknown) => Array.isArray(v) && v.length >= 2 && v.every(pos);
  const ring = (v: unknown) => Array.isArray(v) && v.length >= 4 && v.every(pos) && v[0][0] === v.at(-1)![0] && v[0][1] === v.at(-1)![1];
  const polygon = (v: unknown) => Array.isArray(v) && v.length > 0 && v.every(ring);
  const c = value.coordinates;
  const valid = value.type === 'Point' ? pos(c) : value.type === 'MultiPoint' ? Array.isArray(c) && c.length > 0 && c.every(pos)
    : value.type === 'LineString' ? line(c) : value.type === 'MultiLineString' ? Array.isArray(c) && c.length > 0 && c.every(line)
    : value.type === 'Polygon' ? polygon(c) : value.type === 'MultiPolygon' ? Array.isArray(c) && c.length > 0 && c.every(polygon) : false;
  // Earthquake depth is a measurement, not a positive map altitude.
  const xy = (a: unknown): unknown => Array.isArray(a) ? finite(a[0]) ? a.slice(0,2) : a.map(xy) : a;
  return valid ? {type:value.type,coordinates:xy(c)} as Geometry : null;
}

export function archiveFeatures(layer: ArchiveLayer, rows: readonly ArchiveRow[], counties = new Map<string, Geometry>()) {
  const features: Feature<Geometry, ArchiveProperties>[] = [], seen = new Set<string>();
  let unlocated = 0, duplicate = 0, missingValues = 0;
  rows.forEach((row,index) => {
    const key = rowKey(row,index);
    if (seen.has(key)) { duplicate++; return; }
    seen.add(key);
    let geometry: unknown = row.geometry;
    if (layer.kind === 'recovered' && record(row.values)) {
      try {geometry=JSON.parse(String(row.values.geometry_geojson));} catch {geometry=null;}
    }
    if (layer.kind === 'stations' || layer.kind === 'wind') geometry = {type:'Point',coordinates:[row.lon,row.lat]};
    if (layer.kind === 'storms') {
      const begin = record(row.location) && record(row.location.begin) ? row.location.begin : {};
      geometry = {type:'Point',coordinates:[begin.lon,begin.lat]};
    }
    if (layer.kind === 'prism') geometry = record(row.county) ? counties.get(String(row.county.geoid)) : null;
    const valid = validArchiveGeometry(geometry);
    // Specialized point feeds are scoped to Kansas and its surroundings. Raw
    // recovered collections may legitimately extend farther; reject their 0,0
    // placeholder without discarding real locations in other states.
    if (!valid || (valid.type==='Point' && (layer.kind==='recovered' ? valid.coordinates[0]===0&&valid.coordinates[1]===0 : valid.coordinates[0]<-103.5 || valid.coordinates[0]>-93.5 || valid.coordinates[1]<35.5 || valid.coordinates[1]>41.5))) { unlocated++; return; }
    const value = layer.kind === 'prism' && finite(row.mean) && finite(row.validCells) && row.validCells > 0 ? row.mean : null;
    if (layer.kind === 'prism' && value === null) missingValues++;
    features.push({type:'Feature',id:features.length,geometry:valid,properties:{key,label:rowLabel(row,index),value,unit:typeof row.unit === 'string' ? row.unit : '',period:typeof row.period === 'string' ? row.period : ''}});
  });
  return {collection:{type:'FeatureCollection',features} as FeatureCollection<Geometry,ArchiveProperties>,unlocated,duplicate,missingValues};
}

/** A fixed, displayed local window; never silently claim statewide completeness. */
export function archiveArea(center: readonly [number, number]): string {
  const [lon,lat] = center;
  if (!finite(lon) || !finite(lat) || lon < -103 || lon > -94 || lat < 36 || lat > 41) throw new Error('Move the map to Kansas before loading this reference.');
  return [lon-.5,lat-.5,lon+.5,lat+.5].map(n=>n.toFixed(5)).join(',');
}
export function archiveQuery(layer: ArchiveLayer, area: string, month: string, variable: string): Record<string,string> {
  if (layer.kind === 'recovered') return {collection:layer.reference!,limit:'20'};
  if (layer.kind === 'tiger') return {layer:layer.reference!,bbox:area,geometry:'1',limit:'20'};
  if (layer.kind === 'stations') return {bbox:area,limit:'500'};
  if (layer.kind === 'wind') return {limit:'100'};
  if (layer.kind === 'reaches') return {bbox:area,geometry:'1',limit:'50'};
  if (layer.kind === 'prism') {
    if (!/^\d{4}-(0[1-9]|1[0-2])$/.test(month) || !['ppt','tmax','tmin','tmean','tdmean','vpdmin','vpdmax','soltotal','solslope'].includes(variable)) throw new Error('Choose a valid month and climate measure.');
    return {variable,step:'monthly',resolution:'4km',product:'an',from:month,to:month,limit:'105'};
  }
  return {limit:layer.kind === 'storms' ? '200' : layer.kind === 'water' ? '500' : '50'};
}

// Multiple selected cards share the same small PC relay. Bound concurrent reads,
// including geometry joins, and remove cancelled work before it reaches the PC.
let activeReads=0;
const waitingReads: (()=>void)[]=[];
function acquireRead(signal: AbortSignal): Promise<()=>void> {
  signal.throwIfAborted();
  return new Promise((resolve,reject)=>{
    const cancel=()=>{const index=waitingReads.indexOf(start);if(index>=0)waitingReads.splice(index,1);reject(signal.reason);};
    const start=()=>{
      signal.removeEventListener('abort',cancel);
      if(signal.aborted){reject(signal.reason);waitingReads.shift()?.();return;}
      activeReads++;let released=false;
      resolve(()=>{if(released)return;released=true;activeReads--;waitingReads.shift()?.();});
    };
    if(activeReads<2)start();
    else if(waitingReads.length>=64)reject(new Error('Too many archive requests. Finish or remove a loading layer first.'));
    else {waitingReads.push(start);signal.addEventListener('abort',cancel,{once:true});}
  });
}
export async function fetchArchive(dataset: string, query: Record<string,string>, signal: AbortSignal, fetcher = fetch): Promise<ArchiveAnswer> {
  if (!/^[a-z][a-z0-9-]+$/.test(dataset)) throw new Error('Unknown dataset.');
  const release=await acquireRead(signal);
  let response: Response,value: unknown;
  try {
    signal.throwIfAborted();
    response = await fetcher(`/api/local-data/${dataset}?${new URLSearchParams(query)}`,{signal,credentials:'same-origin'});
    value = await readBoundedJson(response,1_000_000,signal);
  } finally {release();}
  if (response.status === 413 && Number(query.limit)>1) return fetchArchive(dataset,{...query,limit:String(Math.max(1,Math.floor(Number(query.limit)/2)))},signal,fetcher);
  if (!response.ok) throw new Error(response.status === 503 || response.status === 404 ? 'Archive service unavailable. No data has been added to the map.' : 'The archive request could not be completed.');
  if (!record(value) || value.dataset !== dataset || !['kfm-local-data-v1','kfm-local-data-storm-events-v1'].includes(String(value.format))) throw new Error('Unexpected archive response.');
  const rows = value.rows ?? value.events;
  const recovered=dataset==='recovered-observations'||dataset==='recovered-bulk';
  const validTotal=recovered ? value.total===null && value.collection===query.collection && typeof value.hasMore==='boolean' && (value.hasMore?typeof value.nextCursor==='string'&&value.nextCursor.length<=2500:value.nextCursor===null) : Number.isSafeInteger(value.total)&&Number(value.total)>= (Array.isArray(rows)?rows.length:0);
  if(query.field && (!record(value.fieldChunk)||value.fieldChunk.field!==query.field||value.fieldChunk.start!==Number(query.start??0)||!Number.isSafeInteger(value.fieldChunk.characters)||(value.fieldChunk.nextStart!==null&&value.fieldChunk.nextStart!==Number(query.start??0)+32768)))throw new Error('Incomplete field response.');
  if (!Array.isArray(rows) || rows.length > 2000 || !rows.every(record) || value.count !== rows.length || !validTotal || !record(value.source)) throw new Error('Incomplete archive response.');
  return {...value,rows} as unknown as ArchiveAnswer;
}

/** Exact GEOID join to the same TIGER edition used to derive the summaries. */
export async function countyShapes(signal: AbortSignal, fetcher = fetch): Promise<Map<string,Geometry>> {
  const shapes = new Map<string,Geometry>(); let offset = 0;
  while (offset < 300) {
    const answer = await fetchArchive('tiger-features',{layer:'county',geometry:'1',limit:'20',offset:String(offset)},signal,fetcher);
    for (const row of answer.rows) { const geometry = validArchiveGeometry(row.geometry); if (/^20\d{3}$/.test(String(row.id)) && geometry) shapes.set(String(row.id),geometry); }
    offset += answer.count;
    if (!answer.count || answer.total === null || offset >= answer.total) break;
  }
  return shapes;
}

export type ArchiveDetail = { title: string; dataset: string; query: Record<string,string> };
export function archiveDetails(layer: ArchiveLayer, row: ArchiveRow, from: string, to: string): ArchiveDetail[] {
  const range={from,to,limit:'100'};
  if (layer.kind === 'stations' && /^[A-Z0-9]{11}$/.test(String(row.id))) return [
    {title:'Daily weather observations',dataset:'ghcn-daily',query:{station:String(row.id),...range}},
    {title:'Annual climate indices',dataset:'ghcndex',query:{station:String(row.id),from:from.slice(0,4),to:to.slice(0,4),period:'annual',limit:'100'}},
    {title:'Climate index definitions',dataset:'ghcndex-indices',query:{}},
  ];
  if (layer.kind === 'wind' && /^[A-Z0-9]{3,4}$/.test(String(row.id))) {
    const station=String(row.id),icao=station.length===3?`K${station}`:station;
    return [
      {title:'Wind observations · UTC · knots',dataset:'wind-observations',query:{station,...range}},
      {title:'Daily wind summaries · knots',dataset:'wind-daily',query:{station,...range}},
      ...(['KCNK','KDDC','KGLD','KICT','KTOP'].includes(icao)?[{title:'NCEI five-minute readings · local standard time · archive ends 2022',dataset:'asos-5min',query:{station:icao,...range}}]:[]),
    ];
  }
  if (layer.kind === 'water' && /^USGS-\d{8,15}$/.test(String(row.site))) return [{title:'Retained gauge readings · original units',dataset:'usgs-streamflow',query:{site:String(row.site),...range}}];
  return [];
}

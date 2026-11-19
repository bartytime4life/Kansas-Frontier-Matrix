import { inKansas, validAreaBounds, validPosition, type AreaBounds, type Position } from "./subsurface-model";
export type ResourceKind = "oilgas" | "minerals";
export const MINE_OPERATIONS = ["surface", "underground", "solution", "unspecified"] as const;
export type MineOperation = typeof MINE_OPERATIONS[number];
export type MineVisibility = Readonly<Record<MineOperation, boolean>>;
const MINE_OPERATION_VALUES = {
  surface: ["Surface", "Surface or Pit", "Pit", "Pit or Lake Dredge", "River Dredge"],
  underground: ["Underground", "Subsurface"],
  solution: ["Solution Mine"],
} as const;
export const mineOperation = (value: unknown): MineOperation => {
  for (const [kind, values] of Object.entries(MINE_OPERATION_VALUES))
    if ((values as readonly unknown[]).includes(value)) return kind as MineOperation;
  return "unspecified";
};
export function parseMineOperations(value: string | null): MineOperation[] | null {
  if (value === null) return [...MINE_OPERATIONS];
  if (value === "none") return [];
  const values = value.split(",");
  if (values.length > 4 || new Set(values).size !== values.length || values.some(item => !(MINE_OPERATIONS as readonly string[]).includes(item))) return null;
  return MINE_OPERATIONS.filter(item => values.includes(item));
}
/** Only fixed source values enter SQL; unclassified and future source labels stay discoverable. */
export function mineOperationWhere(operations: readonly MineOperation[] = MINE_OPERATIONS): string {
  if (operations.some(item => !(MINE_OPERATIONS as readonly string[]).includes(item))) throw new Error("Invalid mine operation.");
  if (MINE_OPERATIONS.every(item => operations.includes(item))) return "1=1";
  const quoted = (values: readonly string[]) => values.map(value => `'${value}'`).join(",");
  return operations.map(kind => kind === "unspecified"
    ? `(QUARRY_TYPE IS NULL OR QUARRY_TYPE NOT IN (${quoted(Object.values(MINE_OPERATION_VALUES).flat())}))`
    : `QUARRY_TYPE IN (${quoted(MINE_OPERATION_VALUES[kind])})`).join(" OR ") || "1=0";
}
export type ResourceLocation = { id:string; coordinates:Position; name:string; material:string; status:string; details:[string,string][]; mineOperation?: MineOperation };
export const RESOURCE_SOURCES = {
  oilgas:{title:"Oil & gas wells",url:"https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Oil_and_Gas_Wells/FeatureServer/0",fields:"OBJECTID,KID,API_NUMBER,LEASE_NAME,WELL_NAME,STATUS,WELL_CLASS,ROTARY_TOTAL_DEPTH,COUNTY",link:"https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Oil_and_Gas_Wells/FeatureServer/0",limitation:"KGS recorded well locations. Status can describe completion or plugging, not current production. Total depth is reported in feet, often relative to the Kelly bushing; no verified underground trajectory is supplied."},
  minerals:{title:"Mines & minerals",url:"https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Quarries_and_Mines/FeatureServer/0",fields:"OBJECTID,KID,PRODUCT_CATEGORY,PRODUCT,QUARRY_TYPE,STATUS,ABANDONED_DURING_YEARS,LEASE_NAME,DATA_SOURCE,UPDATE_DATE",link:"https://www.kgs.ku.edu/Magellan/Minerals/index.html",limitation:"KGS/KDHE historical inventory, largely circa 2000. Recorded active/abandoned status is historical, not a present-day operating assessment. Points do not describe underground workings or mineral reserves."},
} as const;
const object=(v:unknown):v is Record<string,unknown>=>!!v&&typeof v==="object"&&!Array.isArray(v);
const label=(v:unknown)=>typeof v==="string"?v.trim().slice(0,300):typeof v==="number"&&Number.isFinite(v)?String(v):"";
const dateLabel=(v:unknown)=>{
  const timestamp=typeof v==="number"?v:typeof v==="string"&&/^\d{11,13}$/.test(v)?Number(v):NaN;
  return Number.isFinite(timestamp)&&timestamp>=-2208988800000&&timestamp<=4102444800000?new Date(timestamp).toISOString().slice(0,10):label(v);
};
export function resourceQuery(kind:ResourceKind,bounds:AreaBounds,offset=0,limit=200,operations?:readonly MineOperation[]){
  if(!validAreaBounds(bounds))throw new Error("Choose a local Kansas area.");
  if(!Number.isSafeInteger(offset)||offset<0||offset>1_000_000||!Number.isSafeInteger(limit)||limit<1||limit>500)throw new Error("Invalid resource page.");
  return `${RESOURCE_SOURCES[kind].url}/query?${new URLSearchParams({f:"geojson",where:kind==="minerals"?mineOperationWhere(operations):"1=1",geometry:bounds.join(","),geometryType:"esriGeometryEnvelope",spatialRel:"esriSpatialRelIntersects",inSR:"4326",outSR:"4326",returnGeometry:"true",outFields:RESOURCE_SOURCES[kind].fields,resultRecordCount:String(limit+1),resultOffset:String(offset),orderByFields:"OBJECTID ASC"})}`;
}
/** An ArcGIS count belongs to one requested envelope; adjacent envelopes may share boundary points. */
export function resourceCountQuery(kind:ResourceKind,bounds:AreaBounds,operations?:readonly MineOperation[]){
  if(!validResourceCountBounds(bounds))throw new Error("Choose a Kansas count region.");
  return `${RESOURCE_SOURCES[kind].url}/query?${new URLSearchParams({f:"json",where:kind==="minerals"?mineOperationWhere(operations):"1=1",geometry:bounds.join(","),geometryType:"esriGeometryEnvelope",spatialRel:"esriSpatialRelIntersects",inSR:"4326",returnCountOnly:"true",returnGeometry:"false"})}`;
}
export function validResourceCountBounds(value:unknown):value is AreaBounds{
  return Array.isArray(value)&&value.length===4&&value.every(Number.isFinite)
    &&value[0]>=-102.2&&value[2]<=-94.4&&value[1]>=36.8&&value[3]<=40.2
    &&value[2]>value[0]&&value[3]>value[1]&&value[2]-value[0]<=3&&value[3]-value[1]<=1.6;
}
export function resourceCount(value:unknown){
  if(!object(value)||value.error!==undefined||!Number.isSafeInteger(value.count)||Number(value.count)<0)throw new Error("Unrecognized source count.");
  return Number(value.count);
}
export function resourceLocations(value:unknown,kind:ResourceKind,bounds:AreaBounds,limit=200,operations:readonly MineOperation[]=MINE_OPERATIONS){
  if(!validAreaBounds(bounds)||!Number.isSafeInteger(limit)||limit<1||limit>500||!object(value)||value.type!=="FeatureCollection"||!Array.isArray(value.features)||value.features.length>limit+1)throw new Error("Unrecognized source response.");
  const seen=new Set<string>();let rejected=0;
  const rows:ResourceLocation[]=[];
  // The extra raw feature is lookahead only. Filtering it into this page would
  // repeat that record when the next request starts at the raw offset.
  for(const f of value.features.slice(0,limit)){
    if(!object(f)||!object(f.geometry)||f.geometry.type!=="Point"||!validPosition(f.geometry.coordinates)||!object(f.properties)){rejected++;continue;}
    const p=f.properties,c=f.geometry.coordinates;
    if(!inKansas(c)||c[0]<bounds[0]||c[0]>bounds[2]||c[1]<bounds[1]||c[1]>bounds[3]||!Number.isSafeInteger(p.OBJECTID)||Number(p.OBJECTID)<0){rejected++;continue;}
    if(kind==="minerals"&&!operations.includes(mineOperation(p.QUARRY_TYPE))){rejected++;continue;}
    const id=`${kind}:${p.OBJECTID}`;if(seen.has(id)){rejected++;continue;}seen.add(id);
    const pairs=kind==="oilgas"?[["KGS ID","KID"],["API number","API_NUMBER"],["Well class","WELL_CLASS"],["Formation","PRODUCING_FORMATION"],["Total depth (ft; source reference)","ROTARY_TOTAL_DEPTH"],["Spud date","SPUD_DATE"],["Completion date","COMPLETION_DATE"],["Plug date","PLUG_DATE"],["County","COUNTY"],["Location method","LONGITUDE_LATITUDE_SOURCE"]]:[["KGS ID","KID"],["Category","PRODUCT_CATEGORY"],["Operation type","QUARRY_TYPE"],["Abandoned during","ABANDONED_DURING_YEARS"],["Inventory source","DATA_SOURCE"],["Record updated","UPDATE_DATE"]];
    const details=pairs.map(([name,key]):[string,string]=>[name,key.endsWith("_DATE")?dateLabel(p[key]):label(p[key])]).filter(([,v])=>v!=="");
    rows.push({id,coordinates:c,...(kind==="minerals"?{mineOperation:mineOperation(p.QUARRY_TYPE)}:{}),name:[label(p.LEASE_NAME),kind==="oilgas"?label(p.WELL_NAME):""].filter(Boolean).join(" · ")||`${kind==="oilgas"?"Well":"Mine / quarry"} ${label(p.KID)||p.OBJECTID}`,material:label(kind==="oilgas"?p.WELL_CLASS:p.PRODUCT)||label(p.PRODUCT_CATEGORY)||"Not specified",status:label(p.STATUS)||"Not specified",details});
  }
  return {rows:rows.slice(0,limit),partial:value.features.length>limit||value.exceededTransferLimit===true||(object(value.properties)&&value.properties.exceededTransferLimit===true),rejected};
}

import { inKansas, validAreaBounds, validPosition, type AreaBounds, type Position } from "./subsurface-model";
export type ResourceKind = "oilgas" | "minerals";
export type ResourceLocation = { id:string; coordinates:Position; name:string; material:string; status:string; details:[string,string][] };
export const RESOURCE_SOURCES = {
  oilgas:{title:"Oil & gas wells",url:"https://services.kansasgis.org/arcgis8/rest/services/oilgas/oilgas_general/MapServer/0",fields:"OBJECTID,KID,API_NUMBER,LEASE_NAME,WELL_NAME,STATUS,WELL_CLASS,ROTARY_TOTAL_DEPTH,PRODUCING_FORMATION,SPUD_DATE,COMPLETION_DATE,PLUG_DATE,COUNTY,LONGITUDE_LATITUDE_SOURCE",link:"https://www.kgs.ku.edu/Magellan/Qualified/ogwell_fgdc.html",limitation:"KGS recorded well locations. Status can describe completion or plugging, not current production. Total depth is reported in feet, often relative to the Kelly bushing; no verified underground trajectory is supplied."},
  minerals:{title:"Mines & minerals",url:"https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Quarries_and_Mines/FeatureServer/0",fields:"OBJECTID,KID,PRODUCT_CATEGORY,PRODUCT,QUARRY_TYPE,STATUS,ABANDONED_DURING_YEARS,LEASE_NAME,DATA_SOURCE,UPDATE_DATE",link:"https://www.kgs.ku.edu/Magellan/Minerals/index.html",limitation:"KGS/KDHE historical inventory, largely circa 2000. Recorded active/abandoned status is historical, not a present-day operating assessment. Points do not describe underground workings or mineral reserves."},
} as const;
const object=(v:unknown):v is Record<string,unknown>=>!!v&&typeof v==="object"&&!Array.isArray(v);
const label=(v:unknown)=>typeof v==="string"?v.trim().slice(0,300):typeof v==="number"&&Number.isFinite(v)?String(v):"";
export function resourceQuery(kind:ResourceKind,bounds:AreaBounds){
  if(!validAreaBounds(bounds))throw new Error("Choose a local Kansas area.");
  return `${RESOURCE_SOURCES[kind].url}/query?${new URLSearchParams({f:"geojson",where:"1=1",geometry:bounds.join(","),geometryType:"esriGeometryEnvelope",spatialRel:"esriSpatialRelIntersects",inSR:"4326",outSR:"4326",returnGeometry:"true",outFields:RESOURCE_SOURCES[kind].fields,resultRecordCount:"201",orderByFields:"OBJECTID ASC"})}`;
}
export function resourceLocations(value:unknown,kind:ResourceKind,bounds:AreaBounds){
  if(!validAreaBounds(bounds)||!object(value)||value.type!=="FeatureCollection"||!Array.isArray(value.features)||value.features.length>201)throw new Error("Unrecognized source response.");
  const seen=new Set<string>();let rejected=0;
  const rows:ResourceLocation[]=[];
  for(const f of value.features){
    if(!object(f)||!object(f.geometry)||f.geometry.type!=="Point"||!validPosition(f.geometry.coordinates)||!object(f.properties)){rejected++;continue;}
    const p=f.properties,c=f.geometry.coordinates;
    if(!inKansas(c)||c[0]<bounds[0]||c[0]>bounds[2]||c[1]<bounds[1]||c[1]>bounds[3]||!Number.isSafeInteger(p.OBJECTID)||Number(p.OBJECTID)<0){rejected++;continue;}
    const id=`${kind}:${p.OBJECTID}`;if(seen.has(id)){rejected++;continue;}seen.add(id);
    const pairs=kind==="oilgas"?[["KGS ID","KID"],["API number","API_NUMBER"],["Well class","WELL_CLASS"],["Formation","PRODUCING_FORMATION"],["Total depth (ft; source reference)","ROTARY_TOTAL_DEPTH"],["Spud date","SPUD_DATE"],["Completion date","COMPLETION_DATE"],["Plug date","PLUG_DATE"],["County","COUNTY"],["Location method","LONGITUDE_LATITUDE_SOURCE"]]:[["KGS ID","KID"],["Category","PRODUCT_CATEGORY"],["Operation type","QUARRY_TYPE"],["Abandoned during","ABANDONED_DURING_YEARS"],["Inventory source","DATA_SOURCE"],["Record updated","UPDATE_DATE"]];
    const details=pairs.map(([name,key]):[string,string]=>[name,label(p[key])]).filter(([,v])=>v!=="");
    rows.push({id,coordinates:c,name:[label(p.LEASE_NAME),kind==="oilgas"?label(p.WELL_NAME):""].filter(Boolean).join(" · ")||`${kind==="oilgas"?"Well":"Mine / quarry"} ${label(p.KID)||p.OBJECTID}`,material:label(kind==="oilgas"?p.WELL_CLASS:p.PRODUCT)||label(p.PRODUCT_CATEGORY)||"Not specified",status:label(p.STATUS)||"Not specified",details});
  }
  return {rows:rows.slice(0,200),partial:value.features.length>200||value.exceededTransferLimit===true||(object(value.properties)&&value.properties.exceededTransferLimit===true),rejected};
}

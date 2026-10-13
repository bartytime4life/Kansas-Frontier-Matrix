/** Bounded source context. A preview is never a mine footprint or admitted layer. */
export type PreviewBounds = [number, number, number, number];
export const PREVIEW_SOURCES = {
  "kgs-m118": {
    url: "https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/State_Geology_GeMS/FeatureServer/14",
    fields: "OBJECTID,MapUnit,IdentityConfidence,Label,Symbol,DataSourceID,Notes,MapUnitPolys_ID,Name,Fullname,Description",
    attribution: "Kansas Geological Survey · M-118 (2008), GeMS conversion 2023–2024",
    limitation: "Interpreted surficial geology at 1:500,000. Zooming does not add mapping accuracy. Rights review and source admission remain pending.",
  },
  "cngm-earth": {
    url: "https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/National_Earth_Surface_v2/FeatureServer/6",
    fields: "*",
    attribution: "USGS · Cooperative National Geologic Map v2 · Earth surface · September 3, 2026",
    limitation: "Earth surface map-unit interpretations from a national compilation with varying source scales. These polygons do not establish measured depth or a continuous subsurface model. Preview only; source admission remains pending.",
  },
  "cngm-quaternary": {
    url: "https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/National_Quaternary_v2/FeatureServer/5",
    fields: "*",
    attribution: "USGS · Cooperative National Geologic Map v2 · Quaternary · September 3, 2026",
    limitation: "Quaternary map-unit interpretations from a national compilation with varying source scales. These polygons do not establish measured depth or a continuous subsurface model. Preview only; source admission remains pending.",
  },
  "cngm-prequaternary": {
    url: "https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/National_PreQuaternary_v2/FeatureServer/6",
    fields: "*",
    attribution: "USGS · Cooperative National Geologic Map v2 · Pre-Quaternary · September 3, 2026",
    limitation: "Pre-Quaternary map-unit interpretations from a national compilation with varying source scales. These polygons do not establish measured depth or a continuous subsurface model. Preview only; source admission remains pending.",
  },
  "cngm-precambrian": {
    url: "https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/National_Precambrian_v2/FeatureServer/5",
    fields: "*",
    attribution: "USGS · Cooperative National Geologic Map v2 · Precambrian · September 3, 2026",
    limitation: "Precambrian map-unit interpretations include inferred buried geology from borehole and geophysical evidence, with varying source scales. These polygons do not establish measured depth or a continuous subsurface model. Preview only; source admission remains pending.",
  },
  "osmre-nmmr": {
    url: "https://geodata.osmre.gov/arcgis/rest/services/NMMR/MineMap_Points/MapServer/0",
    fields: "*",
    attribution: "OSMRE · National Mine Map Repository",
    limitation: "Historical mine-map index locations, not mine footprints or current hazard assessments. Maps and locations may be incomplete or inaccurate. Map scale is feet per inch.",
  },
} as const;
export type PublicPreviewKind = keyof typeof PREVIEW_SOURCES;
export const isPublicPreviewKind = (value: string | null): value is PublicPreviewKind => value !== null && Object.hasOwn(PREVIEW_SOURCES, value);
export function validPreviewBounds(b: number[]): b is PreviewBounds {
  return b.length === 4 && b.every(Number.isFinite) && b[0] >= -102.06 && b[2] <= -94.58 && b[1] >= 36.99 && b[3] <= 40.01
    && b[0] < b[2] && b[1] < b[3] && b[2] - b[0] <= .61 && b[3] - b[1] <= .61;
}
export function publicPreviewQuery(kind: PublicPreviewKind, bounds: PreviewBounds) {
  if (!validPreviewBounds(bounds)) throw new Error("Choose a smaller Kansas map area.");
  return `${PREVIEW_SOURCES[kind].url}/query?${new URLSearchParams({f:"geojson",where:"1=1",geometry:bounds.join(","),geometryType:"esriGeometryEnvelope",spatialRel:"esriSpatialRelIntersects",inSR:"4326",outSR:"4326",outFields:PREVIEW_SOURCES[kind].fields,returnGeometry:"true",resultRecordCount:"201",maxAllowableOffset:"0.0001",geometryPrecision:"6"})}`;
}
const object = (v: unknown): v is Record<string, unknown> => !!v && typeof v === "object" && !Array.isArray(v);
export type PreviewFeature = {type:"Feature"; id:string; geometry:{type:"Point"|"Polygon"|"MultiPolygon";coordinates:unknown};properties:Record<string,string|number|null>};
export type PublicPreview = {type:"FeatureCollection";features:PreviewFeature[];partial:boolean;rejected:number};
export function parsePublicPreview(value: unknown, kind: PublicPreviewKind, bounds: PreviewBounds): PublicPreview {
  if (!validPreviewBounds(bounds) || !object(value) || value.type !== "FeatureCollection" || !Array.isArray(value.features) || value.features.length > 201) throw new Error("Unrecognized source response.");
  let vertices = 0, rejected = 0;
  const ids = new Set<string>(), features: PreviewFeature[] = [];
  const coordinate = (v: unknown): v is number[] => Array.isArray(v) && v.length >= 2 && v.length <= 3 && v.every(n=>typeof n === "number" && Number.isFinite(n)) && Math.abs(v[0])<=180 && Math.abs(v[1])<=90 && ++vertices <= 100_000;
  const ring = (v: unknown): boolean => Array.isArray(v) && v.length >= 4 && v.length <= 100_000 && v.every(coordinate) && v[0][0] === v[v.length-1][0] && v[0][1] === v[v.length-1][1];
  const polygon = (v: unknown): boolean => Array.isArray(v) && v.length > 0 && v.length <= 500 && v.every(ring);
  for (const f of value.features) {
    if (!object(f) || !object(f.geometry) || !object(f.properties)) {rejected++;continue;}
    const g=f.geometry, p=f.properties, rawId=p.OBJECTID??p.objectid??f.id;
    const id=typeof rawId === "number" || typeof rawId === "string" ? String(rawId).slice(0,100) : "";
    const validGeometry=kind === "osmre-nmmr" ? g.type === "Point" && coordinate(g.coordinates) && g.coordinates[0]>=bounds[0] && g.coordinates[0]<=bounds[2] && g.coordinates[1]>=bounds[1] && g.coordinates[1]<=bounds[3]
      : g.type === "Polygon" ? polygon(g.coordinates) : g.type === "MultiPolygon" && Array.isArray(g.coordinates) && g.coordinates.length>0 && g.coordinates.length<=500 && g.coordinates.every(polygon);
    if (!id || ids.has(id) || !validGeometry) {rejected++;continue;}
    ids.add(id);
    const properties:Record<string,string|number|null>={};
    for (const [key,val] of Object.entries(p).slice(0,60)) if (typeof val === "string" || typeof val === "number" && Number.isFinite(val) || val === null) properties[key.slice(0,100)] = typeof val === "string" ? val.slice(0,3000) : val;
    features.push({type:"Feature",id,geometry:g as PreviewFeature["geometry"],properties});
  }
  return {type:"FeatureCollection",features:features.slice(0,200),rejected,partial:rejected>0 || value.features.length>200 || value.exceededTransferLimit===true || object(value.properties)&&value.properties.exceededTransferLimit===true};
}

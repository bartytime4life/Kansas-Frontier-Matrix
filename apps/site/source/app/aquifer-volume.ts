import clipping from "polygon-clipping";
import type { MultiPolygon, Polygon } from "polygon-clipping";
export type VolumeBounds = [number, number, number, number];
export type AquiferEnvelope = { id: string; geometry: MultiPolygon; depthFeet: [number,number]; thicknessFeet: [number,number]; shallowMeters: number; deepMeters: number };
export type AquiferVolume = { bounds: VolumeBounds; envelopes: AquiferEnvelope[]; heldClasses: number; truncated: boolean; period: "2022–2024" };
export const AQUIFER_VOLUME_ASSETS = [
  {url:"/data/groundwater/kgs-depth-to-water.geojson",sha256:"f2e1ef67d056b9f7710367235f47ad891bc891a37c6d7ce4945e46b6f18353b0",count:10},
  {url:"/data/groundwater/kgs-saturated-thickness.geojson",sha256:"ee9cf91a8189d7eec49378042b49aa3a249f0e5c4113b6fb38cb73799b3a3ac4",count:8},
] as const;
const depthRanges: Record<string,[number,number]> = {"Under 25":[0,25],"25 to 50":[25,50],"50 to 100":[50,100],"100 to 150":[100,150],"150 to 200":[150,200],"200 to 250":[200,250],"250 to 300":[250,300],"300 to 350":[300,350]};
const thicknessRanges: Record<string,[number,number]> = {"Under 50":[0,50],"50 to 100":[50,100],"100 to 150":[100,150],"150 to 200":[150,200],"200 to 250":[200,250],"250 to 300":[250,300]};
export function validVolumeBounds(b: unknown): b is VolumeBounds {
  return Array.isArray(b) && b.length===4 && b.every(Number.isFinite) && b[0]>=-102.2 && b[2]<=-94.4 && b[1]>=36.8 && b[3]<=40.2 && b[2]>b[0] && b[3]>b[1] && b[2]-b[0]<=1 && b[3]-b[1]<=1;
}
/** Values are source intervals, never class IDs or invented midpoint elevations. */
export function envelopeDepths(depth: [number,number], thickness: [number,number]) {
  if (![...depth,...thickness].every(v=>Number.isFinite(v)&&v>=0) || depth[1]<=depth[0] || thickness[1]<=thickness[0]) throw new Error("Invalid source range");
  return {shallowMeters:depth[0]*.3048,deepMeters:(depth[1]+thickness[1])*.3048};
}
export function buildAquiferVolume(depthData: GeoJSON.FeatureCollection, thicknessData: GeoJSON.FeatureCollection, bounds: VolumeBounds): AquiferVolume {
  if (!validVolumeBounds(bounds)) throw new Error("Zoom to a Kansas view no wider than one degree before preparing the aquifer envelope.");
  const region: Polygon = [[[bounds[0],bounds[1]],[bounds[2],bounds[1]],[bounds[2],bounds[3]],[bounds[0],bounds[3]],[bounds[0],bounds[1]]]];
  let heldClasses=0;
  const prepare = (data: GeoJSON.FeatureCollection,ranges: Record<string,[number,number]>,max:number) => {
    if(data.type!=="FeatureCollection" || !Array.isArray(data.features) || data.features.length!==max) throw new Error("Unexpected aquifer snapshot");
    return data.features.flatMap(f=>{
      if(f.geometry?.type!=="MultiPolygon" || f.properties?.period!=="2022–2024") throw new Error("Incompatible aquifer geometry or period");
      const geometry=clipping.intersection(f.geometry.coordinates as MultiPolygon,region);
      if(!geometry.length)return [];
      const range=f.properties.hasValue===true ? ranges[f.properties.classLabel] : null;
      if(!range){heldClasses++;return [];}
      return [{geometry,range}];
    });
  };
  const depths=prepare(depthData,depthRanges,10),thicknesses=prepare(thicknessData,thicknessRanges,8);
  const envelopes: AquiferEnvelope[]=[];let vertices=0,parts=0,truncated=false;
  for(const d of depths)for(const t of thicknesses){
    const geometry=clipping.intersection(d.geometry,t.geometry);if(!geometry.length)continue;
    const n=geometry.flat(2).length;
    if(vertices+n>20000||envelopes.length>=64||parts+geometry.length>256){truncated=true;continue;}
    vertices+=n;parts+=geometry.length;envelopes.push({id:`${d.range.join('-')}:${t.range.join('-')}`,geometry,depthFeet:d.range,thicknessFeet:t.range,...envelopeDepths(d.range,t.range)});
  }
  return {bounds,envelopes,heldClasses,truncated,period:"2022–2024"};
}
export function projectVolumePosition(lon: number,lat: number,bounds:VolumeBounds) {
  const mercator=(a:number)=>Math.log(Math.tan(Math.PI/4+a*Math.PI/360));
  const span=(bounds[2]-bounds[0])*Math.PI/180;
  return {x:((lon-bounds[0])/(bounds[2]-bounds[0])-.5)*6,z:((mercator(bounds[3])+mercator(bounds[1]))/2-mercator(lat))/span*6};
}
export function volumeDepthScale(bounds:VolumeBounds){return 6/(6378137*(bounds[2]-bounds[0])*Math.PI/180*Math.cos((bounds[1]+bounds[3])/2*Math.PI/180));}

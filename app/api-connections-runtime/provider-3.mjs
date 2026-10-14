import {field,location,inputs,postJson,jsonRequest,features,fail} from "./http-runtime.mjs";
export const spec={id:"usgs-transect",name:"USGS 3DEP / NLDI transect",kind:"terrain cross-section",intervalMs:86400000,limitBytes:1048576,docs:"https://api.water.usgs.gov/docs/nldi-pygeoapi/xsatendpts/",limitation:"21 selected land-surface elevation samples along a geographic transect. Native resolution, datum, acquisition metadata and missing samples remain explicit. 3DEP reports actual raster resolution; the resolution control applies only to NLDI. No bathymetry, water depth, velocity or flood model. NLDI execution currently reports an upstream elevation timeout.",fields:[field("product","Sampling service","select","3dep-samples",{options:["3dep-samples","nldi-process"]}),...location,field("endLat","End latitude","number","37.71",{min:36.9,max:40.1}),field("endLon","End longitude","number","-97.32",{min:-102.1,max:-94.5}),field("resolution","NLDI requested resolution (m)","select","10",{options:["1","3","5","10","30"]})]};
const points=q=>Array.from({length:21},(_,i)=>[Number(q.lon)+(Number(q.endLon)-Number(q.lon))*i/20,Number(q.lat)+(Number(q.endLat)-Number(q.lat))*i/20]);
export function plan(q){
 q=inputs(spec,q);if(Math.abs(Number(q.endLat)-Number(q.lat))>0.1||Math.abs(Number(q.endLon)-Number(q.lon))>0.1)fail("TRANSECT_TOO_LONG");
 return {query:q,requests:[q.product==="3dep-samples"?jsonRequest("https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/getSamples",{f:"json",geometry:JSON.stringify({points:points(q),spatialReference:{wkid:4326}}),geometryType:"esriGeometryMultipoint",returnFirstValueOnly:"true",interpolation:"RSP_BilinearInterpolation",outFields:"VerticalDatum,Name,AcquisitionDate,StartDate,EndDate",renderingRule:JSON.stringify({rasterFunction:"None"})}):postJson("https://api.water.usgs.gov/nldi/pygeoapi/processes/nldi-xsatendpts/execution?f=json",{inputs:[{id:"lat",value:[Number(q.lat),Number(q.endLat)]},{id:"lon",value:[Number(q.lon),Number(q.endLon)]},{id:"numpts",value:21},{id:"3dep_res",value:Number(q.resolution)}]},{headers:{"Content-Type":"application/json"}})]};
}
export function parse(v,q){
 if(q.product==="nldi-process")return features(v);
 if(v?.error||!Array.isArray(v?.samples)||v.samples.length>21)fail("PAYLOAD_REJECTED",502);
 const requested=points(q),seen=new Set(),rows=[];let missing=0;
 for(const s of v.samples){
  const i=s.locationId,p=s.location;if(!Number.isInteger(i)||i<0||i>20||seen.has(i)||!p||!Number.isFinite(p.x)||!Number.isFinite(p.y)||(p.spatialReference?.latestWkid??p.spatialReference?.wkid)!==4326||Math.abs(p.x-requested[i][0])>0.00002||Math.abs(p.y-requested[i][1])>0.00002)fail("SAMPLE_IDENTITY_REJECTED",502);
  seen.add(i);const value=typeof s.value==="string"&&s.value.trim()?Number(s.value):typeof s.value==="number"?s.value:NaN;
  const elevationM=Number.isFinite(value)&&value>=-100&&value<=2000?value:null;if(elevationM===null)missing++;
  rows.push({...s,datum:s.attributes?.VerticalDatum??null,elevationM,unit:"m",longitude:p.x,latitude:p.y});
 }
 rows.sort((a,b)=>a.locationId-b.locationId);
 return {rows,total:rows.length,partial:rows.length<21||missing>0,features:rows.map(r=>({type:"Feature",id:r.locationId,properties:r,geometry:{type:"Point",coordinates:[r.longitude,r.latitude]}}))};
}

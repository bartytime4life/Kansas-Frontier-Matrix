type KeyPair={source:string;target:string};
export type CollectionRelationship={
 targetCollection:string;title:string;namespace:string;keys:readonly KeyPair[];
 joinStatus:'not_executed';cardinality:'unverified_across_captures';checks:readonly string[];
 documentation:{url:string;sha256:string;checkedAt:string};
};
const prefix='observations-usgs-';
function relation(target:string,key:string,title:string,extra:string):CollectionRelationship{
 return {targetCollection:prefix+target,title,namespace:key==='monitoring_location_id'?'USGS agency-qualified monitoring location':'USGS time series; confirm data_type',
  keys:[{source:key,target:key}],joinStatus:'not_executed',cardinality:'unverified_across_captures',
  checks:['Preserve provider identifiers and leading zeros; do not substitute file/row keys.',
   'Archived captures can repeat provider IDs. Identify the relevant metadata version; a unique or current match has not been established.',extra],
  documentation:{url:'https://api.waterdata.usgs.gov/ogcapi/v1/collections/combined-metadata/schema?f=json',
   sha256:'31e20e45402e26d2575026deddc23462f66ca848880e0f2021c69af316b35f55',checkedAt:'2026-11-18'}};
}
const station=()=>relation('sites','monitoring_location_id','Inspect station context','Check station type, vertical/horizontal reference and capture edition. A station record does not validate an observation.');
const series=()=>relation('series','time_series_id','Inspect series context','Match data type, parameter, statistic, unit, sublocation and period; metadata boundaries can include gaps or lag observations.');
const relationships:Readonly<Record<string,readonly CollectionRelationship[]>>={
 [prefix+'daily-values']:[station(),series()],
 [prefix+'field-measurements']:[station()],
 [prefix+'peaks']:[station(),series()],
 [prefix+'series']:[station(),
  relation('daily-values','time_series_id','Inspect daily observations','Confirm a daily-value series and matching parameter, statistic and units; not every captured series has daily records.'),
  relation('peaks','time_series_id','Inspect peak observations','Confirm a peak series and matching parameter, units and comparison period; absence from a page is not absence of observations.')],
 [prefix+'sites']:[
  relation('series','monitoring_location_id','Inspect station series','Check data type, parameter, statistic, unit and period; station metadata may have multiple series or captured versions.'),
  relation('daily-values','monitoring_location_id','Inspect daily observations','Match series, parameter, statistic, unit and observation date before comparing values.'),
  relation('field-measurements','monitoring_location_id','Inspect field measurements','Match reading type, method, datum, unit and qualifiers. Field-measurement series IDs use a separate namespace.'),
  relation('peaks','monitoring_location_id','Inspect peak observations','Match parameter, unit, water year and comparison period; partial peak dates remain partial.')],
};
export function collectionRelationships(id:string):readonly CollectionRelationship[]{
 return Object.hasOwn(relationships,id)?relationships[id]:[];
}
export function collectionProviderIdentity(id:string){
 if(id===prefix+'sites')return {fields:['monitoring_location_id'],namespace:'USGS monitoring location'};
 if(id===prefix+'series')return {fields:['time_series_id','data_type'],namespace:'USGS combined metadata series'};
 return null;
}

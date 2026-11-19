import type {FieldRole} from './collection-metadata';
import {usgsDictionary} from './usgs-field-dictionary';

export type FieldDocument = {
 id:string; title:string; url:string; edition:string|null; sha256:string|null; checkedAt:string; scope:string;
};
export type DocumentedField = {
 label?:string; role:FieldRole; definition:string; unit?:string; unitField?:string; reference?:string; encoding?:string;
 codes?:Readonly<Record<string,string>>; sources:readonly string[];
};

const format='faa-ddof-format-2026-05-21', faq='faa-obstacle-faq', normalizer='kfm-faa-normalizer';
export const FAA_FIELD_DICTIONARY_REVISION='faa-ddof-2026-05-21-v1';
const documents:readonly FieldDocument[]=[
 {id:format,title:'FAA daily obstacle format',
  url:'https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/DailyDOF/media/DDOF_README_05-21-2026.pdf',
  edition:'2026-05-21',sha256:'9d845743b688a0a032a3bfff661de9f756d5f947f158e7c92fcd00e17222514c',checkedAt:'2026-11-18',
  scope:'Format definitions, pp. 2–7; this documentation edition does not establish the edition or accuracy of an archived record.'},
 {id:faq,title:'FAA obstacle data FAQ',url:'https://www.faa.gov/air_traffic/flight_info/aeronav/obst_data/odtfaqs/',
  edition:null,sha256:null,checkedAt:'2026-11-18',scope:'Quantity/array interpretation and year-plus-day-of-year encoding.'},
 {id:normalizer,title:'KFM FAA capture and normalization',
  url:'https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/323539a8bf3abd2cd153c257c01fe4dbb1ef7af0/tools/local_data/sql_feed_structures.py#L326-L393',
  edition:'323539a8bf3abd2cd153c257c01fe4dbb1ef7af0',sha256:null,checkedAt:'2026-11-18',
  scope:'Mapping of fixed-width source columns to the archived KFM table; decimal coordinates and point geometry are derived.'},
];

const faa:Readonly<Record<string,DocumentedField>>={
 file_id:{role:'identity',definition:'KFM archived-file key; combine with row_number for the stored row identity.',sources:[normalizer]},
 row_number:{role:'identity',definition:'KFM row key within the archived file.',sources:[normalizer]},
 oas_number:{role:'identity',label:'FAA obstacle identifier',definition:'Provider obstacle identifier; it can recur across archived captures.',sources:[format,normalizer]},
 oas_code:{role:'identity',definition:'State/country prefix of the provider obstacle identifier.',sources:[format,normalizer]},
 obstacle_number:{role:'identity',definition:'Serial portion of the provider obstacle identifier.',sources:[format,normalizer]},
 verification_status:{role:'quality',definition:'FAA verification category, separate from KFM or AI review.',
  codes:{O:'FAA verified',U:'FAA unverified'},sources:[format]},
 country:{role:'identity',definition:'Provider country identifier.',sources:[format]},
 state:{role:'identity',definition:'Provider state identifier.',sources:[format]},
 city:{role:'location',definition:'Provider city label.',sources:[format]},
 lat_degrees:{role:'location',definition:'Latitude degree component.',unit:'degree',sources:[format]},
 lat_minutes:{role:'location',definition:'Latitude minute component.',unit:'arcminute',sources:[format]},
 lat_seconds:{role:'location',definition:'Latitude second component.',unit:'arcsecond',sources:[format]},
 lat_hemisphere:{role:'location',definition:'Latitude hemisphere.',codes:{N:'North',S:'South'},sources:[format]},
 lon_degrees:{role:'location',definition:'Longitude degree component.',unit:'degree',sources:[format]},
 lon_minutes:{role:'location',definition:'Longitude minute component.',unit:'arcminute',sources:[format]},
 lon_seconds:{role:'location',definition:'Longitude second component.',unit:'arcsecond',sources:[format]},
 lon_hemisphere:{role:'location',definition:'Longitude hemisphere.',codes:{E:'East',W:'West'},sources:[format]},
 obstacle_type:{role:'category',definition:'Provider structure classification.',sources:[format]},
 quantity:{role:'value',label:'Obstacles represented',unit:'obstacles',
  definition:'Structures represented by a record; a legacy array can contain several at one point, not separately located features.',sources:[format,faq]},
 agl_height_ft:{role:'value',label:'Height above ground',unit:'ft',reference:'AGL',
  definition:'Height to the tallest structure or attachment, relative to ground.',sources:[format,faq]},
 amsl_height_ft:{role:'value',label:'Height above mean sea level',unit:'ft',reference:'AMSL',
  definition:'Obstacle-top elevation relative to mean sea level.',sources:[format]},
 lighting:{role:'category',definition:'Provider lighting category.',
  codes:{R:'Red',D:'Medium white strobe and red',H:'High-intensity white strobe and red',M:'Medium white strobe',S:'High-intensity white strobe',
   F:'Flood lighting',C:'Dual medium catenary',W:'Synchronized red',L:'Lighted; type unspecified',N:'None',U:'Unknown'},sources:[format]},
 horizontal_accuracy:{role:'quality',definition:'Horizontal tolerance category; code numbers are not measured distances.',
  codes:{'1':'±20 ft','2':'±50 ft','3':'±100 ft','4':'±250 ft','5':'±500 ft','6':'±1000 ft','7':'±0.5 NM','8':'±1 NM','9':'Unknown'},sources:[format]},
 vertical_accuracy:{role:'quality',definition:'Vertical tolerance category; letters are not measured heights.',
  codes:{A:'±3 ft',B:'±10 ft',C:'±20 ft',D:'±50 ft',E:'±125 ft',F:'±250 ft',G:'±500 ft',H:'±1000 ft',I:'Unknown'},sources:[format]},
 marking:{role:'category',definition:'Provider marking category.',
  codes:{P:'Orange, or orange-and-white paint',W:'White paint',M:'Marked',F:'Flag',S:'Spherical marker',N:'None',U:'Unknown'},sources:[format]},
 faa_study_number:{role:'identity',definition:'Provider aeronautical-study reference.',sources:[format]},
 action:{role:'category',definition:'Provider record-action category.',codes:{A:'Add',C:'Change'},sources:[format]},
 julian_date:{role:'time',label:'Provider action date',encoding:'YYYYDDD',
  definition:'Action date encoded as year and day-of-year, not a construction or observation date.',sources:[format,faq]},
 latitude:{role:'location',definition:'KFM decimal latitude from source angular components.',unit:'degree',sources:[normalizer]},
 longitude:{role:'location',definition:'KFM signed decimal longitude from source angular components.',unit:'degree',sources:[normalizer]},
 geometry_geojson:{role:'location',definition:'KFM point from the stored decimal longitude and latitude.',sources:[normalizer]},
};

export function documentedField(collectionId:string|undefined,name:string):DocumentedField|undefined {
 const fields=collectionId==='observations-faa-obstacles'?faa:usgsDictionary(collectionId)?.fields;
 return fields&&Object.hasOwn(fields,name)?fields[name]:undefined;
}
export function fieldDocuments(collectionId:string):readonly FieldDocument[]{
 return collectionId==='observations-faa-obstacles'?documents:usgsDictionary(collectionId)?.documents??[];
}
export function fieldDictionaryRevision(collectionId:string):string|null{
 return collectionId==='observations-faa-obstacles'?FAA_FIELD_DICTIONARY_REVISION:usgsDictionary(collectionId)?.revision??null;
}
export function recordedUnit(collectionId:string,field:string,values:Record<string,unknown>):string|null{
 const definition=documentedField(collectionId,field);
 if(definition?.unit)return definition.unit;
 const key=definition?.unitField;
 const value=key&&Object.hasOwn(values,key)?values[key]:null;
 return typeof value==='string'&&value.trim()?value:null;
}
export function documentedCode(collectionId:string,name:string,code:string):string|null{
 const codes=documentedField(collectionId,name)?.codes;
 return codes&&Object.hasOwn(codes,code)?codes[code]:null;
}
export function collectionFieldNotes(collectionId:string):readonly string[]{
 return collectionId==='observations-faa-obstacles'?[
  'Height values use feet. AGL and AMSL describe different vertical references; no vertical datum or unit conversion is inferred.',
  'Accuracy codes are categories, not distances to average. Height summaries keep FAA verification and accuracy categories separate; unknown codes and missing values remain unchanged.',
  'Quantity can describe a legacy array at one stored point; feature count and represented-obstacle count are different.',
  'The action date is a record-maintenance date. Documentation edition, capture currency, retrieval time and observation time remain distinct.',
 ]:usgsDictionary(collectionId)?.notes??[];
}

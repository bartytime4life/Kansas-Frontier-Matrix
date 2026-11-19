import type {DocumentedField,FieldDocument} from './collection-field-dictionary';

const combined='usgs-combined-context',station='usgs-station-context',series='usgs-series-context',units='usgs-site-unit-reference',normalizer='kfm-usgs-context-normalizer';
const checkedAt='2026-11-18';
const document=(id:string,collection:string,sha256:string):FieldDocument=>({id,title:'USGS '+collection+' definitions',
 url:`https://api.waterdata.usgs.gov/ogcapi/v1/collections/${collection}/schema?f=json`,edition:null,sha256,checkedAt,
 scope:'Provider schema snapshot; documentation retrieval is not a source-capture edition or data review.'});
const combinedDoc=document(combined,'combined-metadata','31e20e45402e26d2575026deddc23462f66ca848880e0f2021c69af316b35f55');
const stationDoc=document(station,'monitoring-locations','173ef4bb9aa5aa00e73b7bad53840ef1c5e172039a311007c9d313c16bb5a0a6');
const seriesDoc=document(series,'time-series-metadata','70bd2b539c0b17bc22aa510bc54536b91527a92b6aa53d13cb953be313cc6648');
const normalization:FieldDocument={id:normalizer,title:'KFM station and series capture mapping',
 url:'https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/3b9697c513d2ab655e52e947f1b25d12d0e41df2/tools/local_data/sql_feed_water.py#L274-L340',
 edition:'3b9697c513d2ab655e52e947f1b25d12d0e41df2',sha256:null,checkedAt,
 scope:'Provider-to-KFM field aliases and the separate captured station/series tables.'};
const unitDoc:FieldDocument={id:units,title:'USGS site service units',
 url:'https://waterservices.usgs.gov/docs/site-service/site-service-details/',edition:null,sha256:null,checkedAt,
 scope:'Station altitude in feet and drainage area in square miles; no unit conversion is performed.'};
const keyFields={
 file_id:{role:'identity',definition:'KFM archived-capture key, not a provider station or observation date.',sources:[normalizer]},
 row_number:{role:'identity',definition:'KFM row key inside the capture.',sources:[normalizer]},
 monitoring_location_id:{role:'identity',definition:'Agency-qualified provider station identity; may recur in archived captures.',sources:[combined]},
} satisfies Record<string,DocumentedField>;
const siteFields:Readonly<Record<string,DocumentedField>>={
 ...keyFields,
 longitude:{role:'location',unit:'degree',sourceField:'x',definition:'Published provider geometry x-coordinate retained by KFM.',sources:[normalizer,station]},
 latitude:{role:'location',unit:'degree',sourceField:'y',definition:'Published provider geometry y-coordinate retained by KFM.',sources:[normalizer,station]},
 agency_code:{role:'identity',definition:'Reporting-agency code.',sources:[station]},
 site_no:{role:'identity',sourceField:'monitoring_location_number',definition:'Provider site number; retain leading zeros and agency context.',sources:[normalizer,station]},
 name:{role:'category',sourceField:'monitoring_location_name',definition:'Provider station name.',sources:[normalizer,station]},
 state_code:{role:'identity',definition:'Provider state identifier.',sources:[station]},
 county_code:{role:'identity',definition:'County identifier requiring state context.',sources:[station]},
 county_name:{role:'location',definition:'Provider county label.',sources:[station]},
 site_type_code:{role:'identity',definition:'Hydrologic-setting identifier.',sources:[station]},
 site_type:{role:'category',definition:'Hydrologic-setting description.',sources:[station]},
 hydrologic_unit_code:{role:'identity',definition:'Provider hydrologic-unit identifier; retain leading zeros.',sources:[station]},
 basin_code:{role:'identity',definition:'USGS basin subdivision identifier.',sources:[station]},
 drainage_area:{role:'value',unit:'mi²',definition:'Station drainage area.',sources:[station,units]},
 contributing_drainage_area:{role:'value',unit:'mi²',definition:'Contributing runoff area, distinct from total drainage area.',sources:[station]},
 altitude:{role:'value',unit:'ft',referenceField:'vertical_datum',definition:'Station altitude relative to its reported vertical datum.',sources:[station,units]},
 altitude_accuracy:{role:'quality',unit:'ft',definition:'Reported altitude uncertainty; retain with altitude rather than average as an observation.',sources:[station]},
 vertical_datum:{role:'category',definition:'Station vertical reference; missing datum stays unknown.',sources:[station]},
 horizontal_positional_accuracy:{role:'quality',definition:'Provider coordinate-accuracy description, not a distance to average.',sources:[station]},
 original_horizontal_datum:{role:'category',definition:'Pre-conversion datum, distinct from the published WGS84 coordinate system.',sources:[station]},
 time_zone_abbreviation:{role:'category',definition:'Station time-zone label, not an observation timestamp or a guaranteed historical offset.',sources:[station]},
 uses_daylight_savings:{role:'category',definition:'Provider daylight-saving flag; no clock conversion is inferred.',sources:[station]},
 district_code:{role:'identity',definition:'Managing USGS district; it can differ from the station state.',sources:[station]},
 aquifer_code:{role:'identity',definition:'Local aquifer identifier.',sources:[station]},
 national_aquifer_code:{role:'identity',definition:'National aquifer-system identifier.',sources:[station]},
 aquifer_type_code:{role:'identity',definition:'Aquifer-confinement category identifier.',sources:[station]},
 well_constructed_depth:{role:'value',unit:'ft',reference:'Land surface',definition:'Finished well depth below land surface.',sources:[station]},
 hole_constructed_depth:{role:'value',unit:'ft',reference:'Land surface',definition:'Drilled hole depth below land surface; separate from finished well depth.',sources:[station]},
 construction_date:{role:'time',definition:'Reported well-completion date; preserve partial or missing values.',sources:[station]},
};
const seriesFields:Readonly<Record<string,DocumentedField>>={
 ...keyFields,
 time_series_id:{role:'identity',sourceField:'id',definition:'Provider series identity, interpreted with data_type and capture edition.',sources:[combined,normalizer]},
 data_type:{role:'category',definition:'Provider computational-period type, not an observed value.',sources:[combined]},
 parameter_code:{role:'identity',definition:'Parameter identifier; preserve leading zeros.',sources:[series]},
 parameter_name:{role:'category',definition:'Provider parameter label.',sources:[series]},
 statistic_id:{role:'identity',definition:'Statistic identifier, distinct from the measured value.',sources:[combined]},
 unit_of_measure:{role:'unit',definition:'Provider unit convention for the series; confirm each observation’s reported unit.',sources:[series]},
 computation_identifier:{role:'category',definition:'Computation applied to produce the series.',sources:[series]},
 sublocation_identifier:{role:'identity',definition:'Within-station series location identifier.',sources:[series]},
 primary_flag:{role:'quality',sourceField:'primary',definition:'USGS primary-series designation, not individual-observation approval or AI review.',sources:[series,normalizer]},
 web_description:{role:'category',definition:'Provider display description.',sources:[series]},
 parameter_description:{role:'category',definition:'Provider explanation of the parameter.',sources:[series]},
 period_begin:{role:'time',sourceField:'begin',definition:'Earliest reported observation boundary; the interval can contain gaps.',sources:[series,normalizer]},
 period_end:{role:'time',sourceField:'end',definition:'Reported latest-observation boundary; metadata can lag newer observations.',sources:[series,normalizer]},
 last_modified:{role:'time',definition:'Provider metadata refresh, separate from an observation time.',sources:[series]},
 parent_time_series_id:{role:'identity',definition:'Provider parent-series identity; a parent may be absent from the captured metadata.',sources:[series]},
 thresholds:{role:'quality',definition:'Operational limits retained as metadata; they are not observations or user-applied filters.',sources:[series]},
};
const sharedNotes=[
 'These are archived metadata records, not new observations. Provider IDs may repeat across captures; a matching ID does not establish a unique or current record.',
 'Provider identities, capture editions, parameter/statistic definitions and units must be checked before comparison. File/row identity is preserved.',
];
const dictionaries={
 'observations-usgs-sites':{fields:siteFields,documents:[combinedDoc,stationDoc,unitDoc,normalization],revision:'usgs-sites-2026-11-18-v1',notes:[...sharedNotes,
  'Altitude summaries keep vertical datums and reported accuracy separate. Missing datums remain unknown; no elevation or coordinate conversion is performed.',
  'Original horizontal datum describes the source before conversion, not the published coordinate system. A station time-zone label alone does not establish an observation offset.']},
 'observations-usgs-series':{fields:seriesFields,documents:[combinedDoc,seriesDoc,normalization],revision:'usgs-series-2026-11-18-v1',notes:[...sharedNotes,
  'Period boundaries do not prove continuous coverage. Metadata may lag observations; primary flags and operational thresholds do not establish individual-observation approval.',
  'The captured table contains daily/peak series metadata. Field-measurement series use a different provider metadata namespace; no field-series join is inferred.']},
};
export function usgsContextDictionary(id:string|undefined){
 return id&&Object.hasOwn(dictionaries,id)?dictionaries[id as keyof typeof dictionaries]:null;
}

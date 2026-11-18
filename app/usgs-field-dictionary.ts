import type {DocumentedField,FieldDocument} from './collection-field-dictionary';

const normalizer='kfm-usgs-normalizer';
const normalization:FieldDocument={id:normalizer,title:'KFM USGS capture and normalization',
 url:'https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/3b9697c513d2ab655e52e947f1b25d12d0e41df2/tools/local_data/sql_feed_water.py#L274-L595',
 edition:'3b9697c513d2ab655e52e947f1b25d12d0e41df2',sha256:null,checkedAt:'2026-11-18',
 scope:'Mapping of provider columns and KFM capture keys, coordinates and derived measurement kind.'};
const hashes={daily:'1063a4f64b76a41ebd79cf349a4a2e3a6f629c4eb86334f88d3f9eaf32678d9d',
 'field-measurements':'bed43a636be3a99c19169391cf8071a8a246078f8c92f714909f3067a7540b48',
 peaks:'235f44ede1e8e4a2193146dabea4dd11003ce3e3ecfc06204e6373c045a47363'};
type Kind=keyof typeof hashes;
function schema(kind:Kind):FieldDocument{
 return {id:'usgs-'+kind+'-schema',title:'USGS '+kind+' field definitions',
  url:`https://api.waterdata.usgs.gov/ogcapi/v1/collections/${kind}/schema?f=json`,edition:null,sha256:hashes[kind],
  checkedAt:'2026-11-18',scope:'Provider JSON schema snapshot. Its API version and retrieval date do not establish a captured observation edition or review.'};
}
function common(source:string):Record<string,DocumentedField>{
 return {
  file_id:{role:'identity',definition:'KFM source-capture reference; not an observation timestamp.',sources:[normalizer]},
  row_number:{role:'identity',definition:'KFM row key within its captured source file.',sources:[normalizer]},
  monitoring_location_id:{role:'identity',definition:'Provider location identifier combining agency and site identifiers.',sources:[source]},
  parameter_code:{role:'identity',definition:'Five-character identifier for the observed constituent and its measurement convention; retain leading zeros.',sources:[source]},
  value:{role:'value',label:'Observed value',unitField:'unit_of_measure',
   definition:'Provider observation value; original text preserves reported precision. Units come from the same row.',sources:[source]},
  unit_of_measure:{role:'unit',definition:'Provider-reported unit for this observation; missing units remain unknown.',sources:[source]},
  time:{role:'time',label:'Observation date/time',definition:'Date or time represented by the observation; preserve the supplied precision.',sources:[source]},
  qualifier:{role:'quality',definition:'Provider observation qualifiers, retained without inferred code meanings.',sources:[source]},
  last_modified:{role:'time',label:'Provider record refresh',definition:'Provider record-refresh time; a refresh need not indicate a changed observation.',sources:[source]},
 };
}
function fields(kind:Kind):Readonly<Record<string,DocumentedField>>{
 const source=schema(kind).id,base=common(source),sources=[source];
 const series:DocumentedField={role:'identity',definition:'Provider series identifier; links to time-series metadata.',sources};
 const approval:DocumentedField={role:'quality',definition:'USGS review status, separate from KFM acceptance or AI review.',
  codes:{Approved:'USGS approved',Provisional:'USGS provisional; subject to revision'},sources};
 const coordinates={
  longitude:{role:'location',definition:'Provider geometry x-coordinate retained by KFM without reprojection.',sources:[normalizer]},
  latitude:{role:'location',definition:'Provider geometry y-coordinate retained by KFM without reprojection.',sources:[normalizer]},
 } satisfies Record<string,DocumentedField>;
 if(kind==='daily')return {...base,time_series_id:series,approval_status:approval,
  statistic_id:{role:'identity',definition:'Identifier for the daily statistic, not a measured number.',
   codes:{'00001':'Maximum','00002':'Minimum','00003':'Mean'},sources}};
 if(kind==='field-measurements')return {...base,...coordinates,approval_status:approval,
  field_measurements_series_id:{role:'identity',definition:'Provider series for a location, parameter and reading type.',sources},
  field_visit_id:{role:'identity',definition:'Provider visit identifier; one visit can contain several measurements.',sources},
  reading_type:{role:'category',definition:'Provider distinction between reference readings, discharge and mean gage-height measurements.',
   codes:{ReferencePrimary:'Reference reading',Discharge:'Discharge measurement',MeanGageHeight:'Mean gage-height measurement'},sources},
  kind:{role:'category',definition:'KFM classification from reading type and parameter code, not an additional observation.',sources:[normalizer]},
  observing_procedure_code:{role:'identity',definition:'Provider observing-method identifier.',sources},
  observing_procedure:{role:'category',definition:'Provider observing-method description.',sources},
  time_of_day:{role:'time',definition:'Reported observation time of day; unknown time or offset remains unknown.',sources},
  vertical_datum:{role:'category',definition:'Provider vertical-reference context; no elevation conversion is inferred.',sources},
  measuring_agency:{role:'category',definition:'Agency that performed the measurement.',sources},
  control_condition:{role:'quality',definition:'Reported condition of the flow-control feature.',sources},
  measurement_rated:{role:'quality',definition:'Provider qualitative measurement-quality rating, not a value to average.',sources},
  sublocation_identifier:{role:'identity',definition:'Optional within-location measurement identifier.',sources}};
 return {...base,...coordinates,time_series_id:series,
  water_year:{role:'time',definition:'Hydrologic year spanning October 1 through September 30, distinct from calendar year.',sources},
  year:{role:'time',definition:'Reported calendar year of the peak.',sources},
  month:{role:'time',definition:'Reported peak month; null means unknown.',sources},
  day:{role:'time',definition:'Reported day of month; null means unknown.',sources},
  time_of_day:{role:'time',definition:'Reported peak time of day; null means unknown.',sources},
  peak_since:{role:'time',label:'Peak comparison start year',definition:'Start year of the peak comparison period when supplied; not a magnitude or observation date.',sources}};
}
const notes=[
 'Observation units come from each row. Missing units are not inferred from a parameter code or another record; no unit conversion is performed.',
 'Provider approval, qualifiers and measurement quality are distinct from KFM acceptance and AI review.',
 'Observation time, provider record refresh and archive retrieval time remain separate. Missing or partial source dates are not completed by the app.',
];
const dictionaries=Object.fromEntries((['daily','field-measurements','peaks'] as const).map(kind=>[
 'observations-usgs-'+(kind==='daily'?'daily-values':kind),{
  fields:fields(kind),documents:[schema(kind),normalization],revision:'usgs-'+kind+'-2026-11-18-v1',
  notes:[...notes,...(kind==='field-measurements'?['Field values remain separate by reading type, datum, observing method, sublocation, agency, control condition and quality rating.']:[]),
   ...(kind==='peaks'?['Water year differs from calendar year. peak_since is a comparison start year; incomplete peak dates remain incomplete.']:[])],
 }
]));
export function usgsDictionary(id:string|undefined){
 return id&&Object.hasOwn(dictionaries,id)?dictionaries[id]:null;
}

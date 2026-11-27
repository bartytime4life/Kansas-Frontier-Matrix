import {additionalUSGSSampleFields} from './usgs-sample-dictionary';
import type {DocumentedField,FieldDocument} from './collection-field-dictionary';
import type {FieldRole} from './collection-metadata';

const guide='wqp-result-guide',schema='wqx3-outbound-schema',mapping='kfm-water-quality-mapping';
const revision='water-quality-2026-11-19-v1';
const documents:readonly FieldDocument[]=[
 {id:guide,title:'Water Quality Portal result field definitions',url:'https://www.waterqualitydata.us/portal_userguide/',
  edition:null,sha256:'ab44cc71d81098c76d54748654d9b46b73b0b8349f1c9430469801df4eb555bb',checkedAt:'2026-11-19',
  scope:'Legacy result-profile semantics and sampling/analysis context; this guide warns that its legacy USGS coverage omits additions after March 11, 2024.'},
 {id:schema,title:'EPA WQX 3.0 outbound field mapping and definitions',
  url:'https://www.epa.gov/system/files/other-files/2025-07/schema_outbound_wqx3.0.csv',edition:'2025-07',
  sha256:'2174cdc24ab1d88d47b4d25ba4c0961b4c78c2c0a7b25add0ea7189b80e51d44',checkedAt:'2026-11-27',
  scope:'WQX 3.0 field definitions and legacy aliases. Documentation versions do not establish the edition, coverage or accuracy of captured records.'},
 {id:mapping,title:'KFM water-quality capture mappings',
  url:'https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/3618a710b6bcc997288554f501f6ec5d995e8ce5/tools/local_data',
  edition:'3618a710b6bcc997288554f501f6ec5d995e8ce5',sha256:null,checkedAt:'2026-11-19',
  scope:'sql_feed_water.py WQP_RESULT_COLUMNS and sql_feed_institutions.py SAMPLES_HEADER/_samples_column; capture keys and column aliases only, not record approval.'},
];
// Explicit provider aliases, not a name-based inference or a cross-provider record join.
const shared:readonly (readonly [string,string,string,string,FieldRole,string])[]=[
 ["organization_identifier", "org_identifier", "OrganizationIdentifier", "Org_Identifier", "identity", "Organization namespace for activities and projects; preserve the supplied identifier."],
 ["activity_identifier", "activity_activity_identifier", "ActivityIdentifier", "Activity_ActivityIdentifier", "identity", "Provider activity identifier within its organization; one activity can have several results."],
 ["activity_type_code", "activity_type_code", "ActivityTypeCode", "Activity_TypeCode", "category", "Reported activity type, including sampling or quality-control activities; do not assume an ambient sample."],
 ["activity_media_name", "activity_media", "ActivityMediaName", "Activity_Media", "category", "Environmental medium sampled, such as water, sediment or tissue."],
 ["activity_media_subdivision_name", "activity_media_subdivision", "ActivityMediaSubdivisionName", "Activity_MediaSubdivision", "category", "More specific environmental matrix within the sample medium."],
 ["activity_start_date", "activity_start_date", "ActivityStartDate", "Activity_StartDate", "time", "Reported start date of the sampling activity, distinct from laboratory analysis and archive retrieval."],
 ["activity_start_time", "activity_start_time", "ActivityStartTime/Time", "Activity_StartTime", "time", "Reported local activity start time; retain its separate time-zone field without inferring UTC."],
 ["activity_start_time_zone_code", "activity_start_time_zone", "ActivityStartTime/TimeZoneCode", "Activity_StartTimeZone", "time", "Provider time-zone designation for activity start; missing zones remain unknown."],
 ["activity_depth_height_value", "activity_depth_height_measure", "ActivityDepthHeightMeasure/MeasureValue", "Activity_DepthHeightMeasure", "value", "Reported vertical position of the sampling activity; its reference point must be checked separately."],
 ["activity_depth_height_unit_code", "activity_depth_height_measure_unit", "ActivityDepthHeightMeasure/MeasureUnitCode", "Activity_DepthHeightMeasureUnit", "unit", "Recorded unit for activity depth or height only."],
 ["project_identifier", "project_identifier", "ProjectIdentifier", "Project_Identifier", "identity", "Project identifier scoped to the reporting organization."],
 ["monitoring_location_identifier", "location_identifier", "MonitoringLocationIdentifier", "Location_Identifier", "identity", "Provider monitoring-location identifier; preserve its namespace and leading zeros."],
 ["activity_comment_text", "activity_comment", "ActivityCommentText", "Activity_Comment", "category", "Provider comments about the activity, retained as source text rather than measured values."],
 ["hydrologic_condition", "activity_hydrologic_condition", "HydrologicCondition", "Activity_HydrologicCondition", "category", "Reported hydrologic condition associated with sampling."],
 ["hydrologic_event", "activity_hydrologic_event", "HydrologicEvent", "Activity_HydrologicEvent", "category", "Reported hydrologic event associated with sampling; this label does not establish causation."],
 ["sample_collection_method_identifier", "sample_collection_method_identifier", "SampleCollectionMethod/MethodIdentifier", "SampleCollectionMethod_Identifier", "identity", "Identifier of the sample-collection procedure; interpret with its method namespace."],
 ["sample_collection_method_identifier_context", "sample_collection_method_identifier_context", "SampleCollectionMethod/MethodIdentifierContext", "SampleCollectionMethod_IdentifierContext", "identity", "Publisher or system namespace of the collection-method identifier."],
 ["result_detection_condition_text", "result_result_detection_condition", "ResultDetectionConditionText", "Result_ResultDetectionCondition", "quality", "Reported detection condition; a nondetect is not a zero or proof of absence."],
 ["characteristic_name", "result_characteristic", "CharacteristicName", "Result_Characteristic", "category", "Reported substance or property evaluated; a shared name alone does not establish comparable methods or chemical forms."],
 ["result_sample_fraction_text", "result_sample_fraction", "ResultSampleFractionText", "Result_SampleFraction", "category", "Reported physical portion of the sample, such as dissolved or total; keep fractions separate."],
 ["result_measure_value", "result_measure", "ResultMeasureValue", "Result_Measure", "value", "Reported result text in its own recorded unit. Censored text remains literal; numeric values still require detection-condition and qualifier checks."],
 ["result_measure_unit_code", "result_measure_unit", "ResultMeasure/MeasureUnitCode", "Result_MeasureUnit", "unit", "Recorded unit of the result only; do not reuse it for detection limits or depth."],
 ["measure_qualifier_code", "result_measure_qualifier_code", "MeasureQualifierCode", "Result_MeasureQualifierCode", "quality", "Provider result qualifiers; retain unknown codes without inferred meanings."],
 ["result_status_identifier", "result_measure_status_identifier", "ResultStatusIdentifier", "Result_MeasureStatusIdentifier", "quality", "Provider result acceptability under its QA/QC criteria, distinct from KFM acceptance or AI review."],
 ["statistical_base_code", "result_statistical_base", "StatisticalBaseCode", "Result_StatisticalBase", "category", "Reported procedure used to derive a statistical result."],
 ["result_value_type_name", "result_measure_type", "ResultValueTypeName", "Result_MeasureType", "category", "Reported basis of value determination, such as measured, estimated or calculated."],
 ["result_weight_basis_text", "result_weight_basis", "ResultWeightBasisText", "Result_WeightBasis", "category", "Sample weight basis, such as wet or dry weight; keep different bases separate."],
 ["result_time_basis_text", "result_time_basis", "ResultTimeBasisText", "Result_TimeBasis", "category", "Reported duration basis of the measurement; do not equate results with different durations."],
 ["result_temperature_basis_text", "result_measure_temperature_basis", "ResultTemperatureBasisText", "Result_MeasureTemperatureBasis", "category", "Reported controlled analysis-temperature basis, not an ambient temperature observation."],
 ["result_particle_size_basis_text", "result_measure_particle_size_basis", "ResultParticleSizeBasisText", "Result_MeasureParticleSizeBasis", "category", "Reported particle-size portion represented by the result."],
 ["precision_value", "data_quality_precision_value", "PrecisionValue", "DataQuality_PrecisionValue", "quality", "Provider precision descriptor for agreement among measurements; not a concentration result or a universal uncertainty unit."],
 ["result_comment_text", "data_quality_result_comment", "ResultCommentText", "DataQuality_ResultComment", "category", "Provider comments about the result; retained without numeric interpretation."],
 ["usgs_pcode", "usgs_pcode", "USGSPCode", "USGSpcode", "identity", "USGS five-character constituent parameter code; retain leading zeros and do not infer missing units."],
 ["result_depth_height_value", "result_depth_height_measure", "ResultDepthHeightMeasure/MeasureValue", "ResultDepthHeight_Measure", "value", "Reported vertical position associated with the result; distinct from activity depth and concentration."],
 ["result_depth_height_unit_code", "result_depth_height_measure_unit", "ResultDepthHeightMeasure/MeasureUnitCode", "ResultDepthHeight_MeasureUnit", "unit", "Recorded unit of result depth or height only."],
 ["subject_taxonomic_name", "result_biological_taxon", "SubjectTaxonomicName", "ResultBiological_Taxon", "category", "Reported organism taxon associated with the biological result or tissue sample."],
 ["sample_tissue_anatomy_name", "result_biological_sample_tissue_anatomy", "SampleTissueAnatomyName", "ResultBiological_SampleTissueAnatomy", "category", "Reported anatomical material of the tissue sample; keep tissue types separate."],
 ["result_analytical_method_identifier", "result_analytical_method_identifier", "ResultAnalyticalMethod/MethodIdentifier", "ResultAnalyticalMethod_Identifier", "identity", "Analytical-method identifier assigned by its publisher; interpret with its namespace and description."],
 ["result_analytical_method_identifier_context", "result_analytical_method_identifier_context", "ResultAnalyticalMethod/MethodIdentifierContext", "ResultAnalyticalMethod_IdentifierContext", "identity", "Publisher or system namespace of the analytical-method identifier."],
 ["result_analytical_method_name", "result_analytical_method_name", "ResultAnalyticalMethod/MethodName", "ResultAnalyticalMethod_Name", "category", "Provider analytical-method title; matching names alone do not establish method equivalence."],
 ["laboratory_name", "lab_info_name", "LaboratoryName", "LabInfo_Name", "category", "Reported laboratory responsible for the analysis."],
 ["analysis_start_date", "lab_info_analysis_start_date", "AnalysisStartDate", "LabInfo_AnalysisStartDate", "time", "Reported date laboratory analysis began, distinct from sample collection and record refresh."],
 ["result_laboratory_comment_text", "lab_info_laboratory_comment", "ResultLaboratoryCommentText", "LabInfo_LaboratoryComment", "category", "Provider comments about laboratory procedures, retained as source text."],
 ["detection_quantitation_limit_type_name", "detection_limit_type_a", "DetectionQuantitationLimitTypeName", "DetectionLimit_TypeA", "category", "Reported kind of detection or quantitation limit; limits of different types are not interchangeable."],
 ["detection_quantitation_limit_value", "detection_limit_measure_a", "DetectionQuantitationLimitMeasure/MeasureValue", "DetectionLimit_MeasureA", "value", "Reported analytical detection or quantitation threshold, not a detected concentration or a regulatory standard. Use its own unit and limit type."],
 ["detection_quantitation_limit_unit_code", "detection_limit_measure_unit_a", "DetectionQuantitationLimitMeasure/MeasureUnitCode", "DetectionLimit_MeasureUnitA", "unit", "Recorded unit for this analytical limit only; it can differ from the result unit."],
 ["provider_name", "provider_name", "ProviderName", "ProviderName", "category", "Source-system name supplied by the provider; distinct from the sampling organization or an AI reviewer."],
];
function fields(modern:boolean):Record<string,DocumentedField>{
 const result:Record<string,DocumentedField>={
  file_id:{role:'identity',definition:'KFM archived-file key; combine with row_number for stored capture identity.',sources:[mapping]},
  row_number:{role:'identity',definition:'KFM row identity within its archived source file, not a provider result identifier.',sources:[mapping]},
 };
 for(const [old,name,oldSource,sourceField,role,definition] of shared){
  result[modern?name:old]={role,definition,sourceField:modern?sourceField:oldSource,sources:[modern?schema:guide,mapping]};
 }
 const unitPairs=modern?{
  result_measure:'result_measure_unit',activity_depth_height_measure:'activity_depth_height_measure_unit',
  result_depth_height_measure:'result_depth_height_measure_unit',detection_limit_measure_a:'detection_limit_measure_unit_a',
 }:{result_measure_value:'result_measure_unit_code',activity_depth_height_value:'activity_depth_height_unit_code',
  result_depth_height_value:'result_depth_height_unit_code',detection_quantitation_limit_value:'detection_quantitation_limit_unit_code'};
 for(const [field,unitField] of Object.entries(unitPairs))result[field].unitField=unitField;
 return result;
}
const legacy=fields(false),modern=fields(true);
function extra(name:string,sourceField:string,role:FieldRole,definition:string,options:Partial<DocumentedField>={}){
 modern[name]={role,definition,sourceField,sources:[schema,mapping],...options};
}
extra('result_method_speciation','Result_MethodSpeciation','category','Chemical form or reporting speciation of the result; do not pool different forms.');
extra('result_characteristic_user_supplied','Result_CharacteristicUserSupplied','category','Provider-supplied observed-property label; preserve it alongside the mapped characteristic.');
extra('result_cas_number','Result_CASNumber','identity','Reported Chemical Abstracts Service registry identifier; no chemical identity is inferred when absent.');
extra('result_measure_identifier','Result_MeasureIdentifier','identity','Provider result identifier; retain organization/activity and capture context rather than deduplicating on it alone.');
extra('result_depth_height_altitude_reference_point','ResultDepthHeight_AltitudeReferencePoint','category','Provider reference point for result depth or height; missing references remain unknown.');
modern.result_depth_height_measure.referenceField='result_depth_height_altitude_reference_point';
extra('activity_bottom_depth_altitude_reference_point','Activity_BottomDepthAltitudeReferencePoint','category','Provider depth/altitude reference associated with the activity; inspect the source before comparing vertical positions.');
extra('last_change_date','LastChangeDate','time','Provider record-change date, distinct from sampling, analysis and archive retrieval.');
for(const suffix of ['a','b']){
 const letter=suffix.toUpperCase();
 if(suffix==='b'){
  extra('detection_limit_type_b','DetectionLimit_TypeB','category','Reported type of the second analytical limit; A and B do not imply lower and upper bounds.');
  extra('detection_limit_measure_b','DetectionLimit_MeasureB','value','Second reported analytical threshold, not a second observation or regulatory limit.',{unitField:'detection_limit_measure_unit_b'});
  extra('detection_limit_measure_unit_b','DetectionLimit_MeasureUnitB','unit','Recorded unit for the second analytical limit only.');
 }
 extra('detection_limit_comment_'+suffix,'DetectionLimit_Comment'+letter,'category','Provider commentary about analytical limit '+letter+'.');
}
for(const [name,sourceField,definition] of [
 ['sample_collection_method_name','SampleCollectionMethod_Name','Provider title of the sample-collection procedure.'],
 ['result_analytical_method_description','ResultAnalyticalMethod_Description','Provider description of the analytical procedure.'],
 ['result_analytical_method_qualifier_type','ResultAnalyticalMethod_QualifierType','Provider qualification of the analytical method.'],
 ['result_comparable_method_modification','Result_ComparableMethodModification','Provider description of changes to a comparable method; this does not establish equivalence.'],
] as const)extra(name,sourceField,'category',definition);
for(const [name,sourceField] of [
 ['result_comparable_method_identifier','Result_ComparableMethodIdentifier'],
 ['result_comparable_method_identifier_context','Result_ComparableMethodIdentifierContext'],
] as const)extra(name,sourceField,'identity','Provider comparable-method reference; retain identifier and namespace without assuming interchangeable results.');
Object.assign(modern,additionalUSGSSampleFields([schema,mapping]));
modern.activity_depth_height_measure.referenceField='activity_bottom_depth_altitude_reference_point';

const notes=[
 'Results, analytical detection/quantitation limits and regulatory thresholds describe different things. A nondetect is not zero or proof of absence; no censoring substitution or compliance conclusion is made.',
 'Numeric summaries describe reported numbers within their recorded contexts, not verified detections. Qualifiers, status, fractions, matrices, chemical forms, tissue types, methods, laboratories and analytical limits must be checked before comparison.',
 'Every measurement uses its own recorded unit. Unknown units and depth references remain unknown; no conversion or missing value is inferred.',
 'Activity dates/times and zones, analysis dates, provider record changes and archive retrieval are different clocks. No UTC conversion or temporal join is performed.',
 'Provider QA/QC status is not KFM acceptance or AI review. Provider identifiers can recur across captures; no result deduplication or cross-provider equivalence is inferred.',
];
const dictionaries={
 'observations-wqp-results':{fields:legacy,documents,revision,notes:[...notes,
  'The captured legacy WQP profile is distinct from the USGS WQX 3.0 samples profile. Its USGS data does not establish coverage after March 11, 2024.']},
 'observations-usgs-samples-results':{fields:modern,documents,revision:'water-quality-2026-11-27-v2',notes:[...notes,
  'This capture uses the USGS WQX 3.0 full physical/chemical profile. All 183 archived fields have sourced definitions; that does not establish record accuracy, completeness or comparable sampling designs. Analytical limit A/B are not assumed lower/upper bounds.',
  'Original and provider-standardized coordinates retain separate horizontal datums. Activity depths use their recorded reference point; no missing datum, geometry or coordinate conversion is inferred.',
  'The provider schema describes AlternateLocation_IdentifierCount as a monitoring-location designator despite its name. It remains identity metadata rather than an inferred count.']},
};
export function waterQualityDictionary(id:string|undefined){
 return id&&Object.hasOwn(dictionaries,id)?dictionaries[id as keyof typeof dictionaries]:undefined;
}

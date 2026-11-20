// The previous group keys are retained solely to reopen pre-dictionary investigations.
export const previousWaterQualityDimensions:Readonly<Record<string,Readonly<Record<string,readonly string[]>>>>={
 'observations-usgs-samples-results': {
  result_measure: [
   'result_characteristic', 'usgs_pcode', 'result_measure_unit', 'activity_media', 'activity_media_subdivision',
   'result_sample_fraction',
   'result_measure_type', 'result_weight_basis', 'result_time_basis', 'result_measure_temperature_basis',
   'result_measure_particle_size_basis', 'result_statistical_base', 'result_result_detection_condition',
   'result_measure_qualifier_code', 'result_measure_status_identifier', 'result_analytical_method_identifier',
   'result_analytical_method_identifier_context', 'result_analytical_method_name',
  ],
  activity_location_horz_accuracy_measure: ['activity_location_horz_accuracy_measure_unit'],
  activity_depth_height_measure: ['activity_depth_height_measure_unit'],
  activity_top_depth_measure: ['activity_top_depth_measure_unit'],
  activity_bottom_depth_measure: ['activity_bottom_depth_measure_unit'],
  group_summary_weight_measure: ['group_summary_weight_measure_unit'],
  result_depth_height_measure: ['result_depth_height_measure_unit', 'result_depth_height_altitude_reference_point'],
  detection_limit_measure_a: ['result_characteristic', 'detection_limit_type_a', 'detection_limit_measure_unit_a'],
  detection_limit_measure_b: ['result_characteristic', 'detection_limit_type_b', 'detection_limit_measure_unit_b'],
 },
 'observations-wqp-results': {
  result_measure_value: [
   'characteristic_name', 'usgs_pcode', 'result_measure_unit_code', 'activity_media_name', 'activity_media_subdivision_name',
   'result_sample_fraction_text',
   'result_value_type_name', 'result_weight_basis_text', 'result_time_basis_text', 'result_temperature_basis_text',
   'result_particle_size_basis_text', 'statistical_base_code', 'result_detection_condition_text',
   'measure_qualifier_code', 'result_status_identifier', 'result_analytical_method_identifier',
   'result_analytical_method_identifier_context', 'result_analytical_method_name',
  ],
  activity_depth_height_value: ['activity_depth_height_unit_code'],
  result_depth_height_value: ['result_depth_height_unit_code'],
  detection_quantitation_limit_value: ['characteristic_name', 'detection_quantitation_limit_type_name', 'detection_quantitation_limit_unit_code'],
 },
};
const resultContext={
 'observations-usgs-samples-results':[
  'result_method_speciation','result_characteristic_user_supplied','result_cas_number',
  'result_biological_taxon','result_biological_sample_tissue_anatomy',
  'sample_collection_method_identifier','sample_collection_method_identifier_context',
  'result_analytical_method_qualifier_type','result_analytical_method_description',
  'result_comparable_method_identifier','result_comparable_method_identifier_context','result_comparable_method_modification','lab_info_name',
  'detection_limit_type_a','detection_limit_measure_a','detection_limit_measure_unit_a',
  'detection_limit_type_b','detection_limit_measure_b','detection_limit_measure_unit_b',
 ],
 'observations-wqp-results':[
  'subject_taxonomic_name','sample_tissue_anatomy_name','sample_collection_method_identifier',
  'sample_collection_method_identifier_context','laboratory_name',
  'detection_quantitation_limit_type_name','detection_quantitation_limit_value','detection_quantitation_limit_unit_code',
 ],
};
export const waterQualityDimensions:Readonly<Record<string,Readonly<Record<string,readonly string[]>>>>=Object.fromEntries(
 Object.entries(previousWaterQualityDimensions).map(([id,fields])=>{
  const result=id==='observations-wqp-results'?'result_measure_value':'result_measure';
  const context=[...fields[result],...resultContext[id as keyof typeof resultContext]];
  const limitFields=id==='observations-wqp-results'?['detection_quantitation_limit_value']:['detection_limit_measure_a','detection_limit_measure_b'];
  return [id,{...fields,[result]:context,...Object.fromEntries(limitFields.map(field=>[field,[...new Set([
   ...context.filter(key=>key!==field),...(fields[field]??[]),
  ])]]))}];
 })
);

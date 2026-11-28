import type {DocumentedField,FieldDocument} from './collection-field-dictionary';

const guide='fhwa-nbi-coding-guide',load='fhwa-nbi-load-2011',assigned='fhwa-nbi-assigned-2011';
const condition='fhwa-nbi-condition-2018',format='fhwa-nbi-legacy-record-format',mapping='kfm-nbi-normalizer';
const documents:readonly FieldDocument[]=[
 {id:guide,title:'FHWA Recording and Coding Guide',url:'https://www.fhwa.dot.gov/bridge/mtguide.pdf',
  edition:'December 1995; posted PDF includes 2000 revision markings',sha256:'9c3ec3e89e11f23709f95d46ed861880c0ef11e491c9a4991c73bf7a39708361',checkedAt:'2026-11-27',
  scope:'Legacy items 1, 3, 5A, 8, 27, 31, 58–72, 90–93 and 106. Printed pages 1–3, 6, 13, 16, 37–57, 62–64 and 69; format documentation does not establish an archived record edition.'},
 {id:load,title:'FHWA revisions to design load and rating methods',url:'https://www.fhwa.dot.gov/bridge/110202.pdf',
  edition:'2011-02-02',sha256:'84cee25b87a3b80cfccd0f127fc0bb49764380f852b973c30db84a741db32549',checkedAt:'2026-11-27',
  scope:'Pages 1–4 revise item 31 and items 63/65. Code meanings changed; archive year alone does not prove which coding revision a retained record follows.'},
 {id:assigned,title:'FHWA assigned load-rating code revision',url:'https://www.fhwa.dot.gov/bridge/nbi/111115.pdf',
  edition:'2011-11-15',sha256:'c60bc0ec3571103ee5ec0f6ff971f36708f6bf62b1361d1d04a9dbc58925f342',checkedAt:'2026-11-27',
  scope:'Pages 1–4 add assigned-rating codes A–F to items 63/65; the attached table describes methods, not an independently verified rating or current capacity.'},
 {id:condition,title:'FHWA Coding Guide-based bridge condition procedure',url:'https://www.fhwa.dot.gov/tpm/guidance/hif18023.pdf',
  edition:'April 2018',sha256:'453db3e9e2ac9a845516fa4194b6ff717a9a64fa56317e001f5c591f0a085522',checkedAt:'2026-11-27',
  scope:'Printed page 7, Table 2 defines Good/Fair/Poor from applicable items 58, 59, 60 and 62. No retrospective classification or safety conclusion is computed here.'},
 {id:format,title:'FHWA legacy NBI record format',url:'https://www.fhwa.dot.gov/bridge/nbi/format.cfm',
  edition:null,sha256:null,checkedAt:'2026-11-27',
  scope:'Legacy record-format table identifies condition, appraisal and inspection items and the added Bridge Condition / Lowest Condition Code summary fields; layouts vary across annual files.'},
 {id:mapping,title:'KFM NBI capture and normalization',
  url:'https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/490d61906ebb2760565858f41bc1bad436e65c32/tools/local_data/sql_feed_bulk.py#L112-L354',
  edition:'490d61906ebb2760565858f41bc1bad436e65c32',sha256:'4bd971f1a065e3a225032b176ea94c53e46ad5b9b39366c129ef45b0cd75a810',checkedAt:'2026-11-27',
  scope:'Provider columns are retained as text after outer quote removal. KFM adds capture keys and the requested archive year; missing annual columns stay null.'},
];

const componentCodes={N:'Not applicable','9':'Excellent','8':'Very good','7':'Good','6':'Satisfactory','5':'Fair',
 '4':'Poor','3':'Serious','2':'Critical','1':'Imminent failure condition','0':'Failed condition'};
const channelCodes={N:'Not over a waterway','9':'No noteworthy channel deficiencies','8':'Stable banks and channel protection',
 '7':'Minor protection damage or drift','6':'Bank slumping, minor damage or slight channel restriction',
 '5':'Eroding protection, major damage or vegetation restriction','4':'Severe undermining, damage or debris deposits',
 '3':'Failed protection or channel movement threatening the crossing','2':'Channel changes place the bridge near collapse',
 '1':'Closed for channel failure; corrective action may allow light service','0':'Closed for channel failure; replacement required'};
const culvertCodes={N:'Structure is not a culvert','9':'No deficiencies','8':'No noteworthy culvert deficiencies; insignificant drift marks',
 '7':'Minor cracking, surface damage or scour without misalignment','6':'Initial deterioration, localized scour or moderate metal pitting',
 '5':'Moderate to major deterioration, minor settlement or localized metal distortion',
 '4':'Large damage, considerable settlement/scour or widespread metal distortion',
 '3':'Severe movement, fill loss, perforation or excessive deterioration','2':'Collapse or partial failure with major fill loss or undermining',
 '1':'Closed; corrective action may allow light service','0':'Closed; replacement required'};
const appraisalCodes={'9':'Above desirable criteria','8':'At desirable criteria','7':'Above minimum criteria','6':'At minimum criteria',
 '5':'Above minimum adequacy for retention','4':'At minimum tolerable limits','3':'Intolerable; corrective action priority',
 '2':'Intolerable; replacement priority','1':'Unused in the general appraisal guide','0':'Bridge closed in the general appraisal guide'};
const designCodes={'0':'Edition-dependent: 1995 guide Other or Unknown; February 2011 revision Unknown',
 '1':'M 9 / H 10','2':'M 13.5 / H 15','3':'MS 13.5 / HS 15','4':'M 18 / H 20','5':'MS 18 / HS 20',
 '6':'MS 18 + Mod / HS 20 + Mod (military loading)','7':'Pedestrian','8':'Railroad',
 '9':'MS 22.5 / HS 25; February 2011 revision includes greater loads','A':'HL 93 (added February 2011)',
 B:'Greater than HL 93 configuration (added February 2011)',C:'Other design loading (added February 2011)'};
const methodCodes={'0':'Field evaluation and documented engineering judgment (added February 2011)','1':'Load Factor (LF)','2':'Allowable Stress (AS)',
 '3':'Load and Resistance Factor Rating (LRFR)','4':'Load testing','5':'No rating analysis/evaluation or rating documentation',
 '6':'LF rating factor using MS18 (added February 2011)','7':'AS rating factor using MS18 (added February 2011)','8':'LRFR rating factor using HL-93 (added February 2011)',
 A:'Assigned LFD rating reported in metric tons',B:'Assigned ASD rating reported in metric tons',C:'Assigned LRFD rating reported in metric tons',
 D:'Assigned LFD rating factor using MS18',E:'Assigned ASD rating factor using MS18',F:'Assigned LRFD rating factor using HL93'};
const conditionSources=[guide],appraisalSources=[guide];
const recordTypeCodes={
 '1':'Route carried on the structure','2':'Single route passing under the structure',
 ...Object.fromEntries(Array.from({length:26},(_,index)=>[String.fromCharCode(65+index),`Under-route record ${index+1} at a multiple-route crossing`])),
};
const fields:Readonly<Record<string,DocumentedField>>={
 file_id:{role:'identity',definition:'KFM archived source-file key; combine with row_number for stored capture identity.',sources:[mapping]},
 row_number:{role:'identity',definition:'KFM row key within a captured source file, not a bridge identifier or observation time.',sources:[mapping]},
 nbi_year:{role:'time',label:'Archive year',encoding:'YYYY',definition:'KFM-requested annual NBI file year, separate from inspection, construction, capture time and coding-guide revision.',sources:[mapping]},
 state_code_001:{role:'identity',definition:'Provider state identifier. Preserve its supplied text; delimited exports need not include the region digit described by the legacy three-character state/region format.',sources:[guide,mapping]},
 structure_number_008:{role:'identity',label:'Provider structure identifier',definition:'Agency-assigned structure identifier within a State, retained as text. On/under route records can share it; repeated annual captures are not new bridges.',encoding:'Up to 15 characters in the legacy format',sources:[guide,mapping]},
 county_code_003:{role:'identity',definition:'County/parish FIPS identifier within its State; preserve leading zeros and the source edition.',encoding:'Three-character county code in the legacy format',sources:[guide]},
 record_type_005a:{role:'category',definition:'Inventory-route relationship to the structure, not a measurement or a separate bridge count.',encoding:'1 = on; 2 = single under route; A–Z = multiple under routes in sequence',codes:recordTypeCodes,sources:[guide]},
 year_built_027:{role:'time',label:'Construction completion year',encoding:'YYYY',definition:'Reported construction completion year; the guide permits a best estimate when unknown. It is not an inspection date.',sources:[guide]},
 year_reconstructed_106:{role:'time',label:'Latest reconstruction year',encoding:'YYYY; 0000 means no reconstruction',definition:'Reported completion year of the latest qualifying reconstruction. Code 0000 denotes no reconstruction, not calendar year zero.',sources:[guide]},
 design_load_031:{role:'category',label:'Design live-load code',definition:'Named design live-load configuration, not a measured weight or current load capacity. Code 0 and 9 meanings depend on the coding revision.',codes:designCodes,sources:[guide,load]},
 deck_cond_058:{role:'quality',label:'Deck condition code',definition:'Recorded overall deck component condition on the legacy ordinal scale. N applies to culverts and structures without decks.',codes:componentCodes,sources:conditionSources},
 superstructure_cond_059:{role:'quality',label:'Superstructure condition code',definition:'Recorded physical condition of structural members on the legacy ordinal scale. N applies to culverts.',codes:componentCodes,sources:conditionSources},
 substructure_cond_060:{role:'quality',label:'Substructure condition code',definition:'Recorded physical condition of piers, abutments, foundations and other substructure components. N applies to culverts.',codes:componentCodes,sources:conditionSources},
 channel_cond_061:{role:'quality',label:'Channel condition code',definition:'Recorded channel, bank and protection condition; item-specific descriptions differ from deck/superstructure/substructure condition codes.',codes:channelCodes,sources:conditionSources},
 culvert_cond_062:{role:'quality',label:'Culvert condition code',definition:'Recorded overall culvert alignment, settlement, joints, structural condition and scour. Its item-specific descriptions differ from the component table.',codes:culvertCodes,sources:conditionSources},
 bridge_condition:{role:'quality',label:'Provider bridge condition class',definition:'Retained provider summary classification under the Coding Guide-based performance-measure definitions; not a new KFM assessment or source approval.',codes:{G:'Good: applicable lowest code 7–9',F:'Fair: applicable lowest code 5–6',P:'Poor: applicable lowest code 0–4'},sources:[format,condition,mapping]},
 lowest_rating:{role:'quality',label:'Provider lowest condition code',definition:'Retained lowest applicable code among items 58, 59, 60 and 62; channel item 61 is excluded. Interpret the originating component table; this ordinal code has no physical unit.',sources:[format,condition,mapping]},
 opr_rating_meth_063:{role:'category',label:'Operating-rating method code',definition:'Reported method used for item 64. The 1995 guide and 2011 revisions describe different code sets; a method code is not a load magnitude.',codes:methodCodes,sources:[guide,load,assigned]},
 inv_rating_meth_065:{role:'category',label:'Inventory-rating method code',definition:'Reported method used for item 66. The 1995 guide and 2011 revisions describe different code sets; a method code is not a load magnitude.',codes:methodCodes,sources:[guide,load,assigned]},
 structural_eval_067:{role:'quality',label:'Structural appraisal code',definition:'Legacy calculated structural appraisal combining component condition and inventory-rating criteria. General appraisal N is invalid here; code 0 does not by itself establish actual closure.',codes:{...appraisalCodes,'0':'Structural appraisal 0; can follow component code 1 without actual closure'},sources:appraisalSources},
 deck_geometry_eval_068:{role:'quality',label:'Deck geometry appraisal code',definition:'Legacy appraisal of roadway width and vertical clearance, not geometry coordinates or a physical width. N applies to specified culverts with roadway-width code 0000.',codes:{...appraisalCodes,N:'Not applicable under the item-specific criteria'},sources:appraisalSources},
 undclrence_eval_069:{role:'quality',label:'Underclearance appraisal code',definition:'Legacy appraisal of vertical/horizontal underclearance, not a measured clearance. N applies unless the crossing is over a highway or railroad.',codes:{...appraisalCodes,N:'Not over a highway or railroad'},sources:appraisalSources},
 posting_eval_070:{role:'quality',label:'Bridge posting appraisal code',definition:'Legacy comparison of operating rating with State legal loads; separate from actual posted/open/closed status in item 41.',codes:{'5':'At or above legal loads','4':'0.1–9.9% below legal loads','3':'10.0–19.9% below legal loads','2':'20.0–29.9% below legal loads','1':'30.0–39.9% below legal loads','0':'More than 39.9% below legal loads'},sources:appraisalSources},
 waterway_eval_071:{role:'quality',label:'Waterway adequacy appraisal code',definition:'Legacy appraisal of flow passage, overtopping and traffic interruption. Numeric meanings depend on functional-class columns in its own table; do not reuse the component condition legend.',codes:{N:'Bridge not over a waterway','0':'Bridge closed in the item-specific table'},sources:appraisalSources},
 appr_road_eval_072:{role:'quality',label:'Approach alignment appraisal code',definition:'Legacy approach-road alignment appraisal relative to the existing highway, rather than current design standards. N is invalid; the general guide leaves code 1 unused.',codes:appraisalCodes,sources:appraisalSources},
 date_of_inspect_090:{role:'time',label:'Last routine inspection month/year',encoding:'MMYY; century not supplied',definition:'Recorded month and two-digit year of the last routine inspection. Preserve leading zeros and unresolved century; no day or exact timestamp is supplied.',sources:[guide]},
 fracture_092a:{role:'quality',label:'Fracture-critical inspection requirement',encoding:'Y plus two-digit interval in months, or N plus blanks',definition:'Legacy special-inspection requirement and designated interval for fracture-critical details; distinct from the inspection date in 93A.',sources:[guide]},
 undwater_look_see_092b:{role:'quality',label:'Underwater inspection requirement',encoding:'Y plus two-digit interval in months, or N plus blanks',definition:'Legacy underwater special-inspection requirement and designated interval; distinct from the inspection date in 93B.',sources:[guide]},
 spec_inspect_092c:{role:'quality',label:'Other special inspection requirement',encoding:'Y plus two-digit interval in months, or N plus blanks',definition:'Legacy other-special-inspection requirement and designated interval; distinct from the inspection date in 93C.',sources:[guide]},
 fracture_last_date_093a:{role:'time',label:'Last fracture-critical inspection month/year',encoding:'MMYY; blank when corresponding 92A is N',definition:'Month and two-digit year of the last applicable fracture-critical inspection. Blank is not a zero date; the century and day are not supplied.',sources:[guide]},
 undwater_last_date_093b:{role:'time',label:'Last underwater inspection month/year',encoding:'MMYY; blank when corresponding 92B is N',definition:'Month and two-digit year of the last applicable underwater inspection. Blank is not a zero date; the century and day are not supplied.',sources:[guide]},
 spec_last_date_093c:{role:'time',label:'Last other-special inspection month/year',encoding:'MMYY; blank when corresponding 92C is N',definition:'Month and two-digit year of the last applicable other-special inspection. Blank is not a zero date; the century and day are not supplied.',sources:[guide]},
};
const notes=[
 'These definitions cover selected legacy NBI fields, not the replacement SNBI schema. Documentation editions and archive years do not prove each retained record follows that edition.',
 'Condition and appraisal values are ordinal provider codes, not physical measurements. Channel and culvert descriptions have separate tables; no code average or current safety conclusion is established.',
 'N means not applicable only where the item permits it. Blank, null and unrecognized codes remain literal and are not converted to zero or assigned a meaning.',
 'Routine and critical-feature dates encode month plus two-digit year (MMYY). The app does not infer a century, day, timezone or inspection currency; archive, construction and reconstruction years remain distinct.',
 'Design-load codes 0 and 9 changed and method codes 0 and 6–8 were added in February 2011; assigned method codes A–F were added in November 2011. The combined legend documents these revisions without silently assigning a latest-edition meaning to old records.',
 'Operating/inventory method labels do not determine units for exported items 64/66. Their numeric values and unit handling are unchanged by this dictionary.',
 'Provider condition classes are retained, not recomputed. They are distinct from KFM acceptance, source admission, AI review and permission to publish.',
];

export function nbiDictionary(collectionId:string|undefined){
 return collectionId==='bulk-nbi-bridges'?{fields,documents,revision:'nbi-legacy-2026-11-27-v1',notes}:undefined;
}

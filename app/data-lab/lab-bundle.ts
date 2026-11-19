import {
  LAB_MAX_PAGES, LAB_MAX_ROWS, measurementDistribution, profileCollection, storyBrief,
  type LabSnapshot, type MeasurementBin,
} from '../collection-lab';
import { type Collection } from '../collection-metadata';
import {fieldDictionaryRevision} from '../collection-field-dictionary';
import { recoveredCollection } from '../recovered-collections';

const FORMAT = 'kfm-record-lab-bundle-v1';
export const MAX_LAB_BUNDLE_BYTES = 8 * 1024 * 1024;
export type LabRange = Pick<MeasurementBin, 'lower' | 'upper' | 'includeUpper'>;
export type LabMeasurementView = { field: string; context: string; range: LabRange | null };

function record(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

export function sameRange(a: LabRange | null | undefined, b: LabRange) {
  return a?.lower === b.lower && a.upper === b.upper && a.includeUpper === b.includeUpper;
}

export function createLabBundle(
  collection: Collection,
  snapshot: LabSnapshot,
  question: string,
  view: LabMeasurementView | null,
  profile = profileCollection(collection, snapshot),
) {
  const defaultField = profile.fields.find(field => field.groups.length);
  const defaultView = defaultField ? { field: defaultField.name, context: defaultField.groups[0].context, range: null } : null;
  return JSON.stringify({
    format: FORMAT,
    collection: collection.id,
    fieldDictionaryRevision:fieldDictionaryRevision(collection.id),
    question,
    view: view ?? defaultView,
    capture: { pages: snapshot.pages, hasMore: snapshot.hasMore, reads: snapshot.answers.map(captureRead) },
    profile,
    records: snapshot.rows,
    brief: storyBrief(collection, snapshot, question, profile),
  });
}

function captureRead(value: unknown): LabSnapshot['answers'][number] {
  if (!record(value)) throw new Error('The bundle has an invalid read receipt.');
  const generatedAt = value.generatedAt;
  const provider = record(value.source) ? value.source.provider : undefined;
  if (generatedAt != null && (typeof generatedAt !== 'string' || generatedAt.length > 80)) throw new Error('The bundle has an invalid retrieval time.');
  if (provider != null && (typeof provider !== 'string' || provider.length > 500)) throw new Error('The bundle has an invalid provider name.');
  const cache = value.cache;
  if (cache != null && (!record(cache) || typeof cache.state !== 'string' || cache.state.length > 40 || typeof cache.at !== 'string' || cache.at.length > 80)) {
    throw new Error('The bundle has an invalid cache receipt.');
  }
  return {
    ...(typeof generatedAt === 'string' ? { generatedAt } : {}),
    ...(typeof provider === 'string' ? { source: { provider } } : {}),
    ...(record(cache) ? { cache: { state: String(cache.state), at: String(cache.at) } } : {}),
  };
}

function viewFromBundle(value: unknown, collection: Collection, snapshot: LabSnapshot, profile: ReturnType<typeof profileCollection>): LabMeasurementView | null {
  if (value == null) return null;
  if (!record(value) || typeof value.field !== 'string' || typeof value.context !== 'string') {
    throw new Error('The saved measurement selection is invalid.');
  }
  const field = profile.fields.find(candidate => candidate.name === value.field);
  if (!field?.groups.some(candidate => candidate.context === value.context)) {
    throw new Error('The saved measurement context does not match the bundle’s records.');
  }
  const distribution = measurementDistribution(collection, snapshot, value.field, value.context);
  if (!distribution.count) throw new Error('The saved measurement context does not match the bundle’s records.');
  const range = value.range;
  if (range === null) return { field: value.field, context: value.context, range: null };
  if (!record(range) || typeof range.lower !== 'number' || typeof range.upper !== 'number' || typeof range.includeUpper !== 'boolean') {
    throw new Error('The saved measurement range is invalid.');
  }
  const candidate = { lower: range.lower, upper: range.upper, includeUpper: range.includeUpper };
  if (!distribution.bins.some(bin => sameRange(candidate, bin))) throw new Error('The saved range does not match this measurement distribution.');
  return { field: value.field, context: value.context, range: candidate };
}

// Only the known pre-dictionary water grouping is eligible for this upgrade.
// Validate it against the retained rows; arbitrary or new-format views stay strict.
function previousWaterContext(collection:Collection,view:Record<string,unknown>,rows:LabSnapshot['rows']){
 if(typeof view.field!=='string'||typeof view.context!=='string')return false;
 const dimensions=collection.id==='observations-usgs-field-measurements'?
  ['parameter_code','unit_of_measure','kind','reading_type','vertical_datum','approval_status','qualifier']:
  collection.id==='observations-usgs-peaks'?['parameter_code','unit_of_measure','qualifier']:null;
 if(!dimensions)return false;
 if(view.field!=='value')return (
  collection.id==='observations-usgs-peaks'&&view.field==='peak_since'||
  collection.id==='observations-usgs-field-measurements'&&['measurement_rated','control_condition'].includes(view.field)
 )&&view.context==='Unit and measurement context not supplied';
 return rows.some(row=>{
  const values=row.values;
  if(!record(values))return false;
  const context=Object.fromEntries(dimensions.filter(key=>{
   const value=values[key];
   return ['string','number'].includes(typeof value)&&String(value).trim();
  }).map(key=>[key,String(values[key])]));
  return view.context===(Object.keys(context).length?JSON.stringify(context):'Unit and measurement context not supplied');
 });
}

export function openLabBundle(contents: string) {
  if (contents.length > MAX_LAB_BUNDLE_BYTES) throw new Error('Choose a Record Lab JSON file under 8 MB.');
  let value: unknown;
  try { value = JSON.parse(contents); } catch { throw new Error('This file is not valid JSON.'); }
  if (!record(value) || typeof value.question !== 'string' || value.question.length > 600 || !Array.isArray(value.records) || value.records.length > LAB_MAX_ROWS) {
    throw new Error('Choose a valid Record Lab JSON bundle.');
  }

  const providedProfile = value.profile;
  const legacy = value.format === undefined;
  const legacyCollection = record(providedProfile) && record(providedProfile.collection) ? providedProfile.collection : null;
  const legacySample = record(providedProfile) && providedProfile.format === 'kfm-collection-profile-v1' && record(providedProfile.sample) ? providedProfile.sample : null;
  const collectionId = legacy ? legacyCollection?.id : value.collection;
  const collection = typeof collectionId === 'string' ? recoveredCollection(collectionId) : null;
  if (!collection || (!legacy && value.format !== FORMAT)) throw new Error('The bundle references an unknown collection or format.');

  const capture = legacy ? legacySample : value.capture;
  if (!record(capture) || typeof capture.pages !== 'number' || !Number.isInteger(capture.pages)
      || capture.pages < 1 || capture.pages > LAB_MAX_PAGES || typeof capture.hasMore !== 'boolean') {
    throw new Error('The bundle has an invalid sample receipt.');
  }
  const ids = new Set<string>();
  const rows = value.records.map(row => {
    if (!record(row) || typeof row.id !== 'string' || !row.id || row.id.length > 4096 || ids.has(row.id) || !record(row.values)) {
      throw new Error('The bundle contains an invalid or repeated record identity.');
    }
    ids.add(row.id);
    return row;
  });
  let reads: unknown = capture.reads;
  if (legacy) {
    const times = capture.retrievedAt;
    const cache = capture.cache;
    if (capture.rows !== rows.length || !Array.isArray(times) || !Array.isArray(cache)) throw new Error('The bundle has an incomplete sample receipt.');
    reads = times.map((generatedAt, index) => ({
      generatedAt,
      cache: cache[index],
      source: legacyCollection && record(legacyCollection.provenance) ? legacyCollection.provenance : null,
    }));
  }
  if (!Array.isArray(reads) || reads.length !== capture.pages) throw new Error('The bundle does not account for every captured read.');
  const snapshot: LabSnapshot = { answers: reads.map(captureRead), rows, pages: capture.pages, hasMore: capture.hasMore, origin: 'saved-bundle' };
  let profile: ReturnType<typeof profileCollection>;
  try {
    JSON.stringify(rows, (_key, field) => {
      if (typeof field === 'number' && !Number.isFinite(field)) throw new Error('Invalid number');
      return field;
    });
    profile = profileCollection(collection, snapshot);
  } catch {
    throw new Error('The bundle contains record values that could not be read.');
  }
  // Earlier FAA exports pooled accuracy categories and had no documented units.
  // Keep their exact records/question, but explicitly reset the obsolete view
  // rather than pretending an old range describes one of the new quality groups.
  const oldView=value.view;
  const oldRange=record(oldView)?oldView.range:undefined;
  const validOldRange=oldRange===null||(record(oldRange)&&typeof oldRange.lower==='number'&&Number.isFinite(oldRange.lower)
    &&typeof oldRange.upper==='number'&&Number.isFinite(oldRange.upper)&&oldRange.lower<=oldRange.upper&&typeof oldRange.includeUpper==='boolean');
  const upgrade=collection.id==='observations-faa-obstacles'&&value.fieldDictionaryRevision==null
    &&record(oldView)&&['quantity','agl_height_ft','amsl_height_ft','horizontal_accuracy'].includes(String(oldView.field))
    &&oldView.context==='Unit and measurement context not supplied'&&validOldRange;
  const waterUpgrade=value.fieldDictionaryRevision==null&&validOldRange&&record(oldView)
    &&previousWaterContext(collection,oldView,rows);
  return { collection, snapshot, question: value.question,
    view:upgrade||waterUpgrade?null:viewFromBundle(value.view, collection, snapshot, profile),
    notice:upgrade||waterUpgrade?`${upgrade?'FAA':'USGS'} field definitions have changed. Your records and question were preserved; choose a measurement context again.`:null };
}

import type {ArchiveAnswer,ArchiveRow} from '../archive-layer-data';
type CollectionDescriptor={id:string;title:string;database:string;geometry:unknown;columns:readonly string[]};
const normalize=(value:string)=>value.normalize('NFKD').replace(/\p{M}/gu,'').toLowerCase();

/** Search catalog metadata only; matching a field does not establish retained data or coverage. */
export function matchingCollections<T extends CollectionDescriptor>(collections:readonly T[],query:string,mappedOnly=false):T[]{
 const words=normalize(query).match(/[\p{L}\p{N}]+/gu)??[];
 return collections.filter(collection=>{
  if(mappedOnly&&!collection.geometry)return false;
  const text=normalize([collection.title,collection.id,collection.database,...collection.columns].join(' '));
  return words.every(word=>text.includes(word));
 });
}

/** Preserve the text-search context, unrelated query parameters and in-page anchor. */
export function collectionLocation(search:string,hash:string,id:string,find:string,mappedOnly:boolean):string{
 const params=new URLSearchParams(search);
 if(id)params.set('collection',id);
 if(find.trim())params.set('find',find.trim());else params.delete('find');
 if(mappedOnly)params.set('mapped','1');else params.delete('mapped');
 return `/data-library?${params}${hash}`;
}

export const COMPARISON_LIMIT=4;
export const COMPARISON_RECORD_BYTES=65536;
export const COMPARISON_FIELD_LIMIT=200;
export type ComparedRecord={
 key:string;collection:{id:string;title:string;database:string};row:ArchiveRow;
 dataset:string;retrievedAt:string;source:ArchiveAnswer['source'];cache:ArchiveAnswer['cache']|null;
};
export const comparisonKey=(collectionId:string,id:unknown)=>JSON.stringify([collectionId,String(id)]);
const fields=(row:ArchiveRow):Record<string,unknown>=>row.values&&typeof row.values==='object'&&!Array.isArray(row.values)?row.values as Record<string,unknown>:{};
export function comparisonFields(records:readonly ComparedRecord[]):string[]{
 return [...new Set(records.flatMap(record=>Object.keys(fields(record.row))))];
}
/** Only a bounded copy of an already-read public response. No join, refresh or release. */
export function pinComparison(records:readonly ComparedRecord[],collection:CollectionDescriptor,row:ArchiveRow,answer:ArchiveAnswer):ComparedRecord[]{
 if(answer.dataset!==`recovered-${collection.database}`||answer.collection!==collection.id||
   !(typeof row.id==='string'&&row.id.length>0||typeof row.id==='number'&&Number.isFinite(row.id))||!answer.rows.includes(row))
  throw new Error('This record cannot be tied to the selected collection response.');
 const key=comparisonKey(collection.id,row.id);
 if(records.some(record=>record.key===key))return [...records];
 if(records.length>=COMPARISON_LIMIT)throw new Error('The comparison holds four records. Remove one before adding another.');
 const candidate={key,collection:{id:collection.id,title:collection.title,database:collection.database},row,
  dataset:answer.dataset,retrievedAt:answer.generatedAt,source:answer.source,cache:answer.cache??null};
 const json=JSON.stringify(candidate);
 if(new TextEncoder().encode(json).length>COMPARISON_RECORD_BYTES)throw new Error('This record exceeds the 64 KiB comparison limit. Use the original page download to keep it intact.');
 const next=[...records,JSON.parse(json) as ComparedRecord];
 if(comparisonFields(next).length>COMPARISON_FIELD_LIMIT)throw new Error('These records exceed the 200-field comparison limit. Remove a record before adding this one.');
 return next;
}
export function comparisonValue(record:ComparedRecord,field:string):string{
 const values=fields(record.row);
 if(!Object.hasOwn(values,field))return 'Field absent';
 const value=values[field];
 if(value===null)return 'Not supplied (null)';
 if(value==='')return 'Empty text';
 if(value&&typeof value==='object'&&'longField' in value&&'preview' in value)return `Preview only: ${String(value.preview)}`;
 return typeof value==='object'?JSON.stringify(value):String(value);
}
export function comparisonExport(records:readonly ComparedRecord[]){
 return {format:'kfm-archive-comparison-v1',status:'personal-comparison-not-a-release',
  notes:'Snapshots of already-read record pages. Retrieval time is not observation time. Original fields, units and dates are not normalized or joined. Long-field markers remain previews; no additional content was fetched.',records};
}

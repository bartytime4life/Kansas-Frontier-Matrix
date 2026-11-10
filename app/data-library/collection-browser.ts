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

import {RECOVERED_COLLECTIONS} from '../../recovered-collections';
import {collectionMetadata,relatedCollections,RESEARCH_PACKS,packCollections} from '../../collection-metadata';
import {ARCHIVE_LAYERS,ARCHIVE_DATASET_USES} from '../../archive-layer-catalog';

/** Catalog descriptions only. Source values continue through the existing relay. */
export function GET(request:Request){
 const params=new URL(request.url).searchParams;
 if([...params.keys()].some(k=>k!=='collection')||params.getAll('collection').length>1)return Response.json({error:'Use one optional collection identifier.'},{status:400});
 const id=params.get('collection'),collections=id?RECOVERED_COLLECTIONS.filter(c=>c.id===id):RECOVERED_COLLECTIONS;
 if(id!==null&&!collections.length||id==='')return Response.json({error:'Unknown collection.'},{status:404});
 return Response.json({format:'kfm-collection-catalog-v1',scope:'Catalog metadata and research opportunities; collection totals, source approval and live availability are not established.',
  collections:collections.map(c=>({...collectionMetadata(c),related:relatedCollections(c).map(r=>({id:r.collection.id,reason:r.reason,joinCandidates:r.joinCandidates}))})),
  researchPacks:RESEARCH_PACKS.map(p=>({id:p.id,title:p.title,question:p.question,limitation:p.note,collections:packCollections(p.id).map(c=>c.id)})),
  mapLayers:ARCHIVE_LAYERS.map(l=>({id:l.id,title:l.title,dataset:l.dataset,collection:l.reference??null,topics:l.topics,provider:l.provider,sourceUrl:l.sourceUrl,limitation:l.note})),
  datasetUses:{...ARCHIVE_DATASET_USES,'archive-search':'bounded archive discovery; search results retain their source identities','near-observations':'bounded nearby observation discovery; distance does not establish relationships','near-bulk':'bounded nearby bulk-record discovery; distance does not establish relationships'}},
  {headers:{'Cache-Control':'public, max-age=300','X-Content-Type-Options':'nosniff'}});
}

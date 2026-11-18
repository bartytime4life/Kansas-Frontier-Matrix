'use client';
import Link from 'next/link';
import {collectionMetadata,collectionPacks,collectionUrl,labUrl,packCollections,relatedCollections,type Collection} from './collection-metadata';
import {recoveredMapUrl} from './recovered-collections';

export default function CollectionMetadataPanel({collection, inLab = false}:{collection:Collection; inLab?:boolean}){
 const metadata=collectionMetadata(collection),related=relatedCollections(collection);
 return <section aria-label="Collection metadata and connections">
  <h3>Source context &amp; connections</h3><p>{metadata.description}</p>
  <dl><dt>Collection identity</dt><dd><code>{metadata.id}</code></dd>
   <dt>Topics</dt><dd>{metadata.topics.join(' · ')}</dd>
   <dt>Record keys</dt><dd>{metadata.recordIdentity.join(' + ')}</dd>
   <dt>Geometry</dt><dd>{metadata.spatial.geometryField??'No stored geometry'}</dd>
   <dt>Time fields to inspect</dt><dd>{metadata.temporal.candidateFields.join(', ')||'No time field identified in the catalog'}</dd>
   <dt>Provider, rights, edition &amp; review</dt><dd>Inspect record lineage and provider documentation. Collection names do not establish these fields.</dd></dl>
  {!inLab&&<p><Link href={labUrl(collection.id)}>Open in the record lab →</Link></p>}
  <details><summary>Field dictionary · {metadata.fields.length} fields</summary>
   <p>Documented fields link to their sources. Other roles are hints from field names; their definitions and units remain unspecified.</p>
   {metadata.documentation.length>0&&<><p>Documentation editions describe the format; they do not establish a record’s edition, accuracy or review.</p>
    <ul>{metadata.documentation.map(d=><li key={d.id}><a href={d.url}>{d.title}</a>{d.edition&&` · documentation edition ${d.edition}`} · checked {d.checkedAt}</li>)}</ul>
    <ul>{metadata.fieldNotes.map(note=><li key={note}>{note}</li>)}</ul></>}
   <ul>{metadata.fields.map(f=><li key={f.name}>
    <code>{f.name}</code> · {f.label} · {f.role}{f.roleBasis==='field_name_hint'&&' (name-based hint)'}
    {f.definition&&<p>{f.definition}{f.unit&&` Unit: ${f.unit}.`}{f.reference&&` Reference: ${f.reference}.`}{f.encoding&&` Encoding: ${f.encoding}.`}</p>}
    {f.codes&&<p>Codes: {Object.entries(f.codes).map(([code,meaning])=>`${code} = ${meaning}`).join(' · ')}. Unlisted codes remain uninterpreted.</p>}
    {f.sources.length>0&&<p>Sources: {f.sources.map((id,index)=>{
     const source=metadata.documentation.find(d=>d.id===id);
     return source&&<span key={id}>{index>0&&' · '}<a href={source.url}>{source.title}</a></span>;
    })}</p>}
   </li>)}</ul>
  </details>
  <details><summary>Related collections &amp; comparison opportunities</summary><p>These are research connections, not completed joins or evidence of causation. Match identities, geographic scope and editions before combining rows.</p><ul>{related.map(r=><li key={r.collection.id}><a href={collectionUrl(r.collection.id)}>{r.collection.title}</a> · {r.reason}{r.joinCandidates.length>0&&<small> · shared identity candidates: {r.joinCandidates.join(', ')}; namespace and edition still need verification</small>}</li>)}</ul></details>
  <details><summary>Story questions &amp; map bundles</summary>{collectionPacks(collection.id).map(p=>{
   const map=packCollections(p.id).filter(c=>c.geometry).slice(0,6);
   return <article key={p.id}><h4>{p.title}</h4><p>{p.question}</p><p>{p.note}</p>{(!inLab||map.length>0)&&<p>{!inLab&&<a href={labUrl(collection.id,p.id)}>Start a source-linked brief</a>}{map.length>0&&<>{!inLab&&' · '}<Link href={recoveredMapUrl(map.map(c=>c.id))}>Map {map.length} related geometry collections</Link></>}</p>}</article>;
  })}</details>
 </section>;
}

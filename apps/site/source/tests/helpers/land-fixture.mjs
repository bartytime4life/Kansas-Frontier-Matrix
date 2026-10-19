// Synthetic private-review fixture shared by validation and upload tests.
export function landFixtures(land) {
const bytes=v=>new TextEncoder().encode(land.canonicalLand(v));
const clone=v=>JSON.parse(JSON.stringify(v));
async function rehash(v){
  for(const x of v.captures){
    const m=x.manifest,c=x.candidate;delete m.capture_id;m.capture_id=await land.landDigest(m);c.capture_id=m.capture_id;
    for(const r of c.records){delete r.record_digest;delete r.evidence_ref;r.id='kfm:land:'+(await land.landDigest([r.source_id,r.source_record_id])).slice(7);r.record_digest=await land.landDigest(r);r.evidence_ref='kfm:evidence:land:'+r.record_digest.slice(7);}
    c.locators=Object.fromEntries(c.records.map((r,i)=>[r.record_digest,['csv-row:'+(i+2)]]));delete c.candidate_id;c.candidate_id=await land.landDigest(c);
    x.evidence=[];for(const r of c.records){const members=[...new Set([m.payload_sha256,...m.documents.map(d=>d.sha256)])].sort().map(k=>({sha256:k,bytes:land.decodeLandObject(v.objects[k]).length}));const e={profile:'kfm.land-evidence-bundle-candidate/v1',evidence_ref:r.evidence_ref,record_digest:r.record_digest,capture_id:m.capture_id,candidate_id:c.candidate_id,source_url:m.source_url,retrieved_at:m.retrieved_at,capture_method:m.capture_method,members,locators:c.locators[r.record_digest],documents:m.documents,review_state:'PENDING',release_state:'UNRELEASED'};e.bundle_digest=await land.landDigest(e);x.evidence.push(e);}
  }
  delete v.transfer_digest;v.transfer_digest=await land.landDigest(v);return v;
}
async function fixture(){
  const raw=new TextEncoder().encode('SYNTHETIC CSV EXPORT ONLY'),doc=new TextEncoder().encode('%PDF-SYNTHETIC ORIGINAL ONLY'),sha=await land.landDigest(raw),dsha=await land.landDigest(doc);
  const r={profile:'kfm.land-instrument-candidate/v1',source_id:'shawnee-tax-sales',source_record_id:'SYNTHETIC-CASE:TRACT-1',instrument_type:'tax_foreclosure_sale',event_date:'2001-05-20',recording_date:null,state:'KS',county:'Shawnee',transaction_status:'AUCTION_REPORTED',parties:[],legal_description:null,acres:null,amount:{value:'23.10',kind:'auction_purchase_price',currency:'USD'},notes:'Synthetic review record only',geometry:null,geometry_role:'UNLOCATED',title_claim:'NOT_ESTABLISHED',sale_completion:'NOT_ESTABLISHED',rights_state:'PENDING',sensitivity_state:'REVIEW_REQUIRED',source_admission:'PENDING',review_state:'PENDING',release_state:'UNRELEASED',flags:['RIGHTS_REVIEW_REQUIRED','SENSITIVITY_REVIEW_REQUIRED']};
  const source='https://cdn.snco.gov/counselor/document/SYNTHETIC.pdf';
  const m={profile:'kfm.land-records-capture/v1',source_id:r.source_id,source_url:source,retrieved_at:'2026-10-13T20:00:00Z',format:'mapped-csv',capture_method:'EXPLICIT_EXPORT_OR_TRANSCRIPTION',payload_sha256:sha,bytes:raw.length,documents:[{source_url:source,sha256:dsha,bytes:doc.length}],total_bytes:raw.length+doc.length,source_admission:'PENDING',release_state:'UNRELEASED'};
  const c={profile:'kfm.land-records-batch/v1',source_id:r.source_id,records:[r],coverage:{scope:'EXPLICIT_EXPORT',complete:false,reported_total:null},mapping:{source_record_id:'ID',instrument_type:'Kind',event_date:'Date',state:'State',transaction_status:'Status'},review_state:'PENDING',release_state:'UNRELEASED'};
  return rehash({profile:'kfm.land-review-transfer/v1',created_at:'2026-10-13T20:00:00Z',authority:'PRIVATE_REVIEW_ONLY',review_state:'PENDING',release_state:'UNRELEASED',captures:[{manifest:m,candidate:c,evidence:[]}],objects:{[sha]:Buffer.from(raw).toString('base64'),[dsha]:Buffer.from(doc).toString('base64')}});
}
  return { bytes, rehash, fixture, clone };
}

#!/usr/bin/env python3
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
import jsonschema

BAD=("/raw/","/work/","/quarantine/","/processed/","data/processed/air/")
REQ=["publication_manifest.json","release_manifest.json","promotion_decision.json","evidence_bundle.json","run_receipt.json"]

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def dump(p,d): Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(json.dumps(d,sort_keys=True,indent=2)+"\n",encoding='utf-8')
def sid(prefix,*parts): return prefix+"-"+hashlib.sha256("|".join(parts).encode()).hexdigest()[:12]
def badref(s):
 s=(s or "").lower().replace('\\\\','/')
 return any(b in s for b in BAD)
def validate(doc,schema): jsonschema.validate(instance=doc,schema=load(schema))

def process_dir(pub_dir, include_retracted):
 d=Path(pub_dir); m={n:(d/n) for n in REQ}
 if not m['publication_manifest.json'].exists(): return None,["missing_publication_manifest"]
 miss=[k for k,v in m.items() if not v.exists()]
 if miss: return None,[f"missing_{x.removesuffix('.json')}" for x in miss]
 pman,rel,prom,evd,rr=[load(m[n]) for n in REQ]
 denies=[]
 for refk in ["release_manifest_ref","promotion_decision_ref","evidence_bundle_ref","run_receipt_ref","attestation_ref","aqs_reconciliation_ref"]:
  if refk in pman and badref(pman.get(refk,"")): denies.append("unsafe_manifest_ref")
 if prom.get('decision')!='approved_for_catalog': denies.append('promotion_decision_not_approved_for_catalog')
 if rel.get('public_readiness',{}).get('status') not in {'catalog_candidate','published'}: denies.append('release_manifest_not_public_ready')
 if evd.get('measurements',{}).get('nowcast_truth_status')!='operational_evidence_not_validated_aqs_truth': denies.append('nowcast_label_violation')
 srcs=evd.get('sources',[]); fixture=any(s.get('source_class')=='fixture' for s in srcs)
 avg=evd.get('measurements',{}).get('averaging_window','nowcast_hourly')
 if evd.get('measurements',{}).get('source_class')=='epa_aqs_validated' and avg!='24h_validated': denies.append('aqs_missing_24h_validated')
 if pman.get('status') in {'tombstoned','retracted'} and not include_retracted: denies.append('retracted_filtered')
 for a in pman.get('published_artifacts',[]):
  if not a.get('sha256'): denies.append('missing_sha256')
  if badref(a.get('path','')): denies.append('unsafe_artifact_path')
 meta={"publication_manifest":pman,"release_manifest":rel,"promotion_decision":prom,"evidence_bundle":evd,"run_receipt":rr,"fixture":fixture,"avg":avg}
 return meta,sorted(set(denies))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--publication-dir',action='append',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--allow-fixture-candidate-index',action='store_true'); ap.add_argument('--include-retracted',action='store_true'); ap.add_argument('--dry-run',action='store_true')
 a=ap.parse_args(); out=Path(a.out_dir)
 entries=[]; recs=[]; traces=[]; blocked=[]; src_refs=[]
 for pd in a.publication_dir:
  meta,denies=process_dir(pd,a.include_retracted)
  if meta is None: blocked.extend(denies); continue
  p=meta['publication_manifest']; e=meta['evidence_bundle']; fixture=meta['fixture']
  pub_id=p.get('publication_id',sid('pub',pd)); src_refs.append(str(Path(pd)/'publication_manifest.json'))
  if fixture and not a.allow_fixture_candidate_index: denies.append('fixture_candidate_not_allowed')
  if p.get('status')=='published_fixture_blocked': denies.append('published_fixture_blocked')
  if denies: blocked.extend(denies); continue
  vis='retracted' if p.get('status') in {'tombstoned','retracted'} else ('candidate_only' if fixture else 'public_readable')
  rec_status='retracted' if vis=='retracted' else ('candidate' if fixture else 'public_readable')
  if fixture and rec_status=='public_readable': blocked.append('fixture_public_readable_forbidden'); continue
  ref=f"publication://{pub_id}/qa_summary"
  entry={"entry_id":sid('entry',pub_id),"publication_id":pub_id,"artifact_refs":[{"ref":f"publication://{pub_id}/publication_manifest","sha256":hashlib.sha256(json.dumps(p,sort_keys=True).encode()).hexdigest()}],"catalog_refs":meta['release_manifest'].get('catalog_refs',[]),"provenance_ref":f"publication://{pub_id}/provenance_trace.json","qa_summary_ref":ref,"measurement_summary":{"pollutant":"pm25","units":"ug_m3","averaging_window":meta['avg'],"nowcast_is_operational":True,"nowcast_is_validated_aqs_truth":False},"visibility":vis,"retraction_state":"retracted" if vis=='retracted' else "active"}
  rec={"schema_version":"v1","record_id":sid('record',pub_id),"domain":"atmosphere.air","publication_id":pub_id,"time_window":{"from":"2026-01-01T00:00:00Z","to":"2026-01-01T01:00:00Z"},"aggregation":"county","measurements":{"source_class":(e.get('sources',[{}])[0].get('source_class') or 'fixture'),"averaging_window":meta['avg'],"units":"ug_m3","nowcast_is_operational":True,"nowcast_is_validated_aqs_truth":False},"qa":{"qa_summary_ref":ref},"provenance":{"publication_manifest_ref":f"publication://{pub_id}/publication_manifest.json","release_manifest_ref":f"publication://{pub_id}/release_manifest.json","evidence_bundle_ref":f"publication://{pub_id}/evidence_bundle.json","provenance_ref":f"publication://{pub_id}/public_provenance_trace.json"},"catalog":{"catalog_ref":f"publication://{pub_id}/catalog"},"status":rec_status}
  trace={"schema_version":"v1","trace_id":sid('trace',pub_id),"domain":"atmosphere.air","publication_id":pub_id,"chain":["QA Summary","EvidenceBundle","PromotionDecision","ReleaseManifest","PublicationManifest","PublicIndex/PublicApiRecord"],"public_safe_refs":[rec['provenance'][k] for k in ['publication_manifest_ref','release_manifest_ref','evidence_bundle_ref','provenance_ref']],"redactions":["internal filesystem paths removed"],"generated_at":now()}
  entries.append(entry); recs.append(rec); traces.append(trace)
 idx_status='fixture_candidate_index' if recs and all(r['status']=='candidate' for r in recs) else 'public_index_candidate'
 if blocked:
  idx={"schema_version":"v1","index_id":sid('index','blocked',now()),"domain":"atmosphere.air","generated_at":now(),"source_publication_manifest_refs":src_refs,"entries":[],"public_boundary_checks":{"deny_reasons":sorted(set(blocked))},"status":"public_index_blocked"}
  if not a.dry_run: dump(out/'public_index.blocked.json',idx)
  print('DENY '+','.join(sorted(set(blocked))))
  return 0 if a.dry_run else 1
 idx={"schema_version":"v1","index_id":sid('index',*sorted([e['publication_id'] for e in entries])),"domain":"atmosphere.air","generated_at":now(),"source_publication_manifest_refs":src_refs,"entries":entries,"public_boundary_checks":{"safe_refs_only":True},"status":idx_status}
 status={"schema_version":"v1","domain":"atmosphere.air","generated_at":now(),"latest_publication_id":entries[-1]['publication_id'] if entries else "","latest_index_id":idx['index_id'],"counts":{"records":len(recs)},"blocked_count":0,"retracted_count":sum(1 for r in recs if r['status']=='retracted'),"fixture_candidate_count":sum(1 for r in recs if r['status']=='candidate'),"warnings":[],"status":"fixture_only" if recs and all(r['status']=='candidate' for r in recs) else "green"}
 if a.dry_run: return 0
 dump(out/'public_index.json',idx)
 dump(out/'public_status.json',status)
 for r in recs: dump(out/f"public_api_record.{r['record_id']}.json",r)
 for t in traces: dump(out/f"public_provenance_trace.{t['trace_id']}.json",t)
 for sf in ['public_index.schema.json','public_api_record.schema.json','public_status.schema.json','public_provenance_trace.schema.json']:
  pass
 return 0
if __name__=='__main__': raise SystemExit(main())

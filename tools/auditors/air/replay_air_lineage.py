#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
from datetime import datetime, timezone
BAD=("/raw/","/work/","/quarantine/","/processed/","data/processed/air/")
CHAIN=["qa_summary","evidence_bundle","promotion_decision","release_manifest","publication_manifest","public_index","public_api_record","public_status","public_provenance_trace"]
def ts(v=None): return v or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def load(p): return json.loads(Path(p).read_text())
def dump(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")
def bad(s):
 s=(s or '').lower().replace('\\\\','/')
 return any(b in s for b in BAD)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--read-model-dir',required=True); ap.add_argument('--publication-dir'); ap.add_argument('--out-dir',required=True); ap.add_argument('--as-of'); ap.add_argument('--allow-fixture',action='store_true'); ap.add_argument('--dry-run',action='store_true')
 a=ap.parse_args(); rd=Path(a.read_model_dir); pd=Path(a.publication_dir or a.read_model_dir)
 miss=[]; checks=[]; deny=[]
 refs={k:pd/f"{k}.json" for k in CHAIN[:5]}; refs.update({"public_index":rd/'public_index.json',"public_status":rd/'public_status.json'})
 api=list(rd.glob('public_api_record*.json')); prv=list(rd.glob('public_provenance_trace*.json'))
 if not api: miss.append('public_api_record')
 if not prv: miss.append('public_provenance_trace')
 for k,p in refs.items():
  if not p.exists(): miss.append(k)
 objs={k:load(p) for k,p in refs.items() if p.exists()}
 if api: objs['public_api_record']=load(api[0])
 if prv: objs['public_provenance_trace']=load(prv[0])
 for m in miss: deny.append(f"missing_{m}")
 fixture=False
 if 'evidence_bundle' in objs:
  fixture=any(s.get('source_class')=='fixture' for s in objs['evidence_bundle'].get('sources',[]))
  if objs['evidence_bundle'].get('measurements',{}).get('nowcast_truth_status')!='operational_evidence_not_validated_aqs_truth': deny.append('nowcast_labelled_validated_truth')
 if 'promotion_decision' in objs and objs['promotion_decision'].get('decision')!='approved_for_catalog': deny.append('promotion_not_approved')
 for name,obj in objs.items():
  text=json.dumps(obj)
  if any(x in text.lower() for x in ['data/raw/','data/work/','data/quarantine/','data/processed/air/']): deny.append(f'unsafe_ref_{name}')
 if 'publication_manifest' in objs:
  for art in objs['publication_manifest'].get('published_artifacts',[]):
   if not art.get('sha256'): deny.append('missing_sha256')
 if bad(art.get('path','')): deny.append('unsafe_artifact_path')
 result='deny' if deny else 'pass'
 if fixture and not a.allow_fixture: deny.append('fixture_not_allowed'); result='deny'
 report={"schema_version":"v1","audit_id":"audit-"+hashlib.sha256((str(rd)+ts(a.as_of)).encode()).hexdigest()[:12],"domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"root_ref":str(rd),"chain":CHAIN,"hash_checks":[{"name":"publication_manifest_sha256_present","passed":'missing_sha256' not in deny}],"path_safety_checks":[{"name":"no_internal_path_exposure","passed":not any('unsafe_' in d for d in deny)}],"semantic_checks":[{"name":"nowcast_not_validated_aqs_truth","passed":'nowcast_labelled_validated_truth' not in deny}],"missing_refs":miss,"result":result}
 events=[{"schema_version":"v1","event_id":"evt-"+report['audit_id'],"domain":"atmosphere.air","event_type":"lineage_audit","created_at":ts(a.as_of),"actor":"fixture-non-production-auditor","subject_refs":[str(rd)],"result":result,"details":{"deny_reasons":sorted(set(deny)),"fixture_backed":fixture}}]
 if not a.dry_run:
  out=Path(a.out_dir); dump(out/'lineage_audit_report.json',report); (out/'ops_events.jsonl').write_text("\n".join(json.dumps(e,sort_keys=True) for e in events)+"\n")
 print(json.dumps({"result":result,"deny":sorted(set(deny))},sort_keys=True))
 return 0 if (not deny or a.dry_run or (fixture and a.allow_fixture)) else 1
if __name__=='__main__': raise SystemExit(main())

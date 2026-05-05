#!/usr/bin/env python3
import argparse,json,hashlib,sys
from pathlib import Path
J=lambda p: json.loads(Path(p).read_text())
BAD=('RAW','WORK','QUARANTINE','data/processed/air/')
def main():
 a=argparse.ArgumentParser(); a.add_argument('dirs',nargs='+'); a.add_argument('--source-read-model-dir'); a.add_argument('--as-of'); x=a.parse_args()
 ok=True
 for d in x.dirs:
  d=Path(d); rep={'schema_version':'v1','audit_id':'audit-1','domain':'atmosphere.air','generated_at':x.as_of or '2026-04-30T00:00:00Z','as_of':x.as_of or '2026-04-30T00:00:00Z','rebuild_manifest_ref':str(d/'read_model_rebuild_manifest.json'),'checks':[],'hash_checks':[],'lineage_checks':[],'path_safety_checks':[],'semantic_checks':[],'result':'pass'}
  for n in ['read_model_rebuild_plan.json','read_model_rebuild_manifest.json','public_index.json','public_delta_feed.json','read_model_version_index.json']:
   if not (d/n).exists(): rep['result']='deny'; rep['checks'].append(f'missing:{n}')
  if x.source_read_model_dir and (d/'public_index.json').exists():
   s=J(Path(x.source_read_model_dir)/'public_index.json'); n=J(d/'public_index.json')
   if s.get('version_id')==n.get('version_id'): rep['result']='deny'; rep['semantic_checks'].append('source index mutated in place')
  txt='\n'.join([p.read_text(errors='ignore') for p in d.glob('**/*.json')])
  if any(b in txt for b in BAD): rep['result']='deny'; rep['path_safety_checks'].append('unsafe path reference')
  if '"nowcast_label": "validated_aqs_truth"' in txt: rep['result']='deny'; rep['semantic_checks'].append('nowcast labelled validated truth')
  (d/'rebuild_audit_report.json').write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n')
  st='PASS' if rep['result']=='pass' else 'DENY'; print(f'{st} {d}')
  ok=ok and rep['result']=='pass'
 sys.exit(0 if ok else 1)
if __name__=='__main__': main()

import json
from pathlib import Path

def main():
 e=[]
 t=json.loads(Path('fixtures/domains/hydrology/triplets/hydrology_synthetic_streamflow.triplet_delta.json').read_text())
 l=json.loads(Path('fixtures/domains/hydrology/layer_manifests/hydrology_synthetic_streamflow.layer_manifest_candidate.json').read_text())
 r=json.loads(Path('fixtures/domains/hydrology/release_dry_runs/hydrology_synthetic_streamflow.publish_denied.json').read_text())
 if t.get('graph_projection') is not True: e.append('triplet graph_projection')
 if l.get('public_release_allowed') is not False: e.append('layer public flag')
 if r.get('finite_result') not in {'DENY','ABSTAIN','READY_FOR_REVIEW'}: e.append('release dry run result')
 print('PASS catalog/triplet/layer manifests' if not e else f'FAIL {e}')
 return 0 if not e else 1
if __name__=='__main__': raise SystemExit(main())

import json
from pathlib import Path

def main():
 e=[]
 good=json.loads(Path('fixtures/domains/hydrology/evidence_bundles/hydrology_synthetic_streamflow.evidence_bundle.json').read_text())
 bad=json.loads(Path('fixtures/domains/hydrology/evidence_bundles/hydrology_synthetic_streamflow.invalid_raw_support.evidence_bundle.json').read_text())
 if good.get('finite_state') not in {'EVIDENCE_BUNDLE_READY_INTERNAL','EVIDENCE_BUNDLE_READY_FOR_REVIEW'}: e.append('good state')
 if 'RawCapture' in good.get('support_object_types',[]): e.append('good includes raw')
 if bad.get('finite_state') not in {'DENY','ABSTAIN','ERROR'}: e.append('bad not fail closed')
 print('PASS evidence bundle from processed' if not e else f'FAIL {e}')
 return 0 if not e else 1
if __name__=='__main__': raise SystemExit(main())

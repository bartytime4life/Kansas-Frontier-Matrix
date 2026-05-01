#!/usr/bin/env python
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--rollforward-refresh-dir',required=True);p.add_argument('--format',choices=['text','json'],default='text');a=p.parse_args();d=Path(a.rollforward_refresh_dir)
keys=['reentry_maintenance_refresh_closure_record.json','reentry_remediation_refresh_rollforward_plan.json','reentry_candidate_artifact_refresh_preview_manifest.json']
out={k:(d/k).exists() for k in keys}
print(json.dumps(out,indent=2) if a.format=='json' else '\n'.join(f'{k}: {v}' for k,v in out.items()))

#!/usr/bin/env python3
import json, sys
from pathlib import Path

BAD=("/raw/","/work/","/quarantine/","/data/processed/air/")
ALLOWED_PREFIX=("data/catalog/air/publication_candidate/","data/published/air/","tests/fixtures/air/publication_boundary/")

def load(p): return json.loads(Path(p).read_text())

def check_dir(d):
    issues=[]; d=Path(d)
    m=d/'publication_manifest.json'
    if not m.exists(): return ["missing_publication_manifest"]
    man=load(m)
    for a in man.get('published_artifacts',[]):
        if not a.get('sha256'): issues.append('missing_sha256')
        p=(a.get('path') or '').lower()
        if any(t in p for t in BAD): issues.append('forbidden_artifact_path')
        s=a.get('source_ref','')
        if not any(seg in s for seg in ALLOWED_PREFIX): issues.append('source_ref_outside_governed_paths')
    eb=d/'evidence_bundle.json'
    if eb.exists() and load(eb).get('measurements',{}).get('nowcast_truth_status')!='operational_evidence_not_validated_aqs_truth': issues.append('nowcast_truth_label_violation')
    if man.get('status')=='published' and any('fixture' in (a.get('source_ref','')) for a in man.get('published_artifacts',[])): issues.append('fixture_marked_as_published_truth')
    return issues

def main():
    if len(sys.argv)<2: print('usage: audit_air_public_boundary.py <dir> [<dir>...]'); return 2
    rc=0
    for d in sys.argv[1:]:
        issues=check_dir(d)
        if issues: rc=1; print(f"DENY {d}: {','.join(sorted(set(issues)))}")
        else: print(f"PASS {d}")
    return rc
if __name__=='__main__': raise SystemExit(main())

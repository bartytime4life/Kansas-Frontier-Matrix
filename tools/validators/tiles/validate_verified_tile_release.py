#!/usr/bin/env python3
import argparse, hashlib, json, re
from pathlib import Path
from jsonschema import Draft202012Validator

FORBIDDEN = re.compile(r'(^|/)(RAW|WORK|QUARANTINE)(/|$)', re.I)

def load(p): return json.loads(Path(p).read_text())
def sha(b): return 'sha256:'+hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('evidence')
    ap.add_argument('--fixture-root', default=None)
    ap.add_argument('--out', default='ValidationReport.v1.json')
    a=ap.parse_args()
    ev=load(a.evidence)
    root=Path(a.fixture_root or Path(a.evidence).parent)
    schema=load('schemas/tiles/verified_tile_release_evidence.schema.json')
    errs=[]
    for e in Draft202012Validator(schema).iter_errors(ev): errs.append(f"schema:{'.'.join(map(str,e.path)) or '<root>'}:{e.message}")
    for req in ('EvidenceBundle','ReleaseManifest','RunReceipt','VerifierTrace'):
        ref=ev.get('required_refs',{}).get(req)
        if not ref: errs.append(f'missing required ref {req}')
        elif not (root/ref).exists(): errs.append(f'unresolved ref {req}:{ref}')
    if ev.get('runtime_contract',{}).get('allow_unverified_render') is not False: errs.append('runtime contract must deny unverified render')
    for p in ev.get('public_artifacts',[]):
        if FORBIDDEN.search(p): errs.append('public artifact references forbidden zone')
    tr=ev.get('trace',{})
    if tr.get('masked_pct',999)>15 or tr.get('avg_tile_size_kb',999)>60 or tr.get('avg_fetch_verify_ms',999)>120 or tr.get('memory_mb',999)>50 or tr.get('changed_tile_verification_pct',0)<100 or tr.get('produced_tile_count_deviation_pct',999)>1:
        errs.append('verifier trace thresholds failed')
    if not ev.get('rollback_ref') or not ev.get('correction_ref'): errs.append('missing correction/rollback link')
    idx_ref=root/'index.bin'
    if idx_ref.exists() and ev.get('indexDigest')!=sha(idx_ref.read_bytes()): errs.append('stale or missing indexDigest')
    for t in ev.get('tiles',[]):
        if t.get('change_type')=='modified' and not t.get('prior_digest'): errs.append('modified tile missing prior_digest')
        br=t.get('bytes_ref')
        if br and (root/br).exists() and ev.get('hash_algorithm')=='sha256':
            if t.get('digest')!=sha((root/br).read_bytes()): errs.append(f"mismatched tile digest {t.get('tile_id')}")
    result='ALLOW' if not errs else 'DENY'
    report={"schema_version":"v1","object_type":"ValidationReport","validator":"validate_verified_tile_release","target":a.evidence,"result":result if result in {"ALLOW","DENY","ERROR"} else "ERROR","errors":errs}
    Path(a.out).write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report))
    return 0 if not errs else 1

if __name__=='__main__':
    raise SystemExit(main())

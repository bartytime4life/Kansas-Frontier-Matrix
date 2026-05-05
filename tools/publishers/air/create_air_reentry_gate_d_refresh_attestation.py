#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from _reentry_publication_boundary_refresh_lib import ts,writej
ap=argparse.ArgumentParser(); ap.add_argument('--release-candidate-refresh-dir',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--attester',default='fixture-release-manager'); ap.add_argument('--role',default='release_manager'); ap.add_argument('--statement',default='fixture_publication_boundary_refresh_attestation'); ap.add_argument('--signature',default='fixture-signature'); ap.add_argument('--signature-type',default='fixture_signature'); ap.add_argument('--as-of'); ap.add_argument('--fixture-only',action='store_true'); ap.add_argument('--dry-run',action='store_true')
a=ap.parse_args(); as_of=ts(a.as_of)
prod_allowed = False if a.signature_type=='fixture_signature' else (not a.fixture_only)
if a.signature_type=='fixture_signature' and prod_allowed: raise SystemExit('DENY fixture signature cannot authorize production')
obj={"schema_version":"v1","attestation_id":"gate-d-refresh-attestation","domain":"atmosphere.air","created_at":as_of,"as_of":as_of,"gate":"D","subject_refs":[str(Path(a.release_candidate_refresh_dir))],"attester":a.attester,"role":a.role,"statement":a.statement,"signature":a.signature,"signature_type":a.signature_type,"fixture_backed":bool(a.fixture_only or a.signature_type=='fixture_signature'),"production_use_allowed":False if a.signature_type=='fixture_signature' else prod_allowed,"status":"fixture_attested" if (a.fixture_only or a.signature_type=='fixture_signature') else "candidate_attested"}
out=Path(a.out_dir)
if not a.dry_run:
 writej(out/'reentry_gate_d_refresh_attestation.json',obj); (out/'reentry_publication_boundary_refresh_events.jsonl').write_text('{"event_type":"gate_d_refresh_attestation_created","result":"pass"}\n')
print('PASS')

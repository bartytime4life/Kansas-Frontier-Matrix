#!/usr/bin/env python3
from _reentry_deployment_readiness_refresh_common import *
import argparse,uuid
p=argparse.ArgumentParser();p.add_argument('--deployment-readiness-refresh-dir',action='append',required=True);p.add_argument('--decision',required=True);p.add_argument('--decided-by',required=True);p.add_argument('--role',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--signature',default='fixture-signature');p.add_argument('--signature-type',default='fixture_signature');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');a=p.parse_args();
if 'production' in a.decision: fail('production blocked')
d=J(Path(a.deployment_readiness_refresh_dir[0])/'reentry_deployment_readiness_refresh_manifest.json')
out={"schema_version":"v1","decision_id":f"rmr-{uuid.uuid5(uuid.NAMESPACE_URL,a.as_of or 'now').hex[:12]}","domain":"atmosphere.air","decided_at":ts(a.as_of),"as_of":ts(a.as_of),"decided_by":a.decided_by,"role":a.role,"subject_refs":[],"deployment_readiness_refresh_manifest_ref":"reentry_deployment_readiness_refresh_manifest.json","deployment_readiness_refresh_report_ref":"reentry_deployment_readiness_refresh_report.json","deployment_readiness_refresh_decision_ref":"reentry_deployment_readiness_refresh_decision.json","decision":a.decision,"rationale":"fixture-backed governance preview only","required_actions":[],"signature":a.signature,"signature_type":a.signature_type,"fixture_backed":True,"status":"fixture_decision"}
W(Path(a.out_dir)/'reentry_release_manager_refresh_decision.json',out)
print('PASS')

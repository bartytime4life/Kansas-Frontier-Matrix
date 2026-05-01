#!/usr/bin/env python
import argparse
from _assurance_common import *
p=argparse.ArgumentParser();[p.add_argument(x,required=True) for x in ('--assurance-plan','--recertification-record','--out-dir')];p.add_argument('--scope',default='fixture_metadata_review');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');a=p.parse_args();plan=j(a.assurance_plan)
out={"schema_version":"1.0.0","maintenance_plan_id":"mw-"+h(a.assurance_plan)[:12],"domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"continuous_assurance_plan_ref":a.assurance_plan,"release_closure_dossier_ref":plan.get('release_closure_dossier_ref',''),"client_delivery_manifest_ref":plan.get('client_delivery_manifest_ref',''),"maintenance_scope":[a.scope],"planned_actions":["metadata review only"],"preconditions":[],"hold_points":[],"rollback_preconditions":[],"stakeholder_notice_refs":[],"forbidden_actions":["no deploy commands"],"safety_checks":[],"status":"fixture_maintenance_plan"}
w(Path(a.out_dir)/'maintenance_window_plan.json',out);print('PASS')

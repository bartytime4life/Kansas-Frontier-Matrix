#!/usr/bin/env python
import argparse
from _assurance_common import *
p=argparse.ArgumentParser();[p.add_argument(x,required=True) for x in ('--assurance-plan','--recertification-record','--out-dir')];p.add_argument('--reason',default='fixture_future_review');p.add_argument('--replacement-ref',default='candidate:none');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');a=p.parse_args();plan=j(a.assurance_plan)
out={"schema_version":"1.0.0","deprecation_candidate_id":"dep-"+h(a.assurance_plan)[:12],"domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"continuous_assurance_plan_ref":a.assurance_plan,"release_closure_dossier_ref":plan.get('release_closure_dossier_ref',''),"client_delivery_manifest_ref":plan.get('client_delivery_manifest_ref',''),"reason":a.reason,"candidate_scope":["candidate-only"],"affected_artifacts":[],"replacement_refs":[a.replacement_ref],"notice_requirements":[],"risk_assessment":[],"evidence_refs":[a.recertification_record],"status":"fixture_deprecation_candidate"}
w(Path(a.out_dir)/'deprecation_candidate_record.json',out);print('PASS')

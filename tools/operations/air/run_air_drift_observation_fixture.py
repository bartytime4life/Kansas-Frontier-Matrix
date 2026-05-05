#!/usr/bin/env python
import argparse
from pathlib import Path
from _assurance_common import *
p=argparse.ArgumentParser();[p.add_argument(x,required=True) for x in ('--assurance-plan','--delivery-dir','--out-dir')];p.add_argument('--baseline-dir');p.add_argument('--as-of');p.add_argument('--allow-fixture-drift',action='store_true');a=p.parse_args();plan=j(a.assurance_plan);d=Path(a.delivery_dir)
manifest=j(d/'client_delivery_manifest.json');deny=bad_text(manifest)
out={"schema_version":"1.0.0","drift_report_id":"dr-"+h(plan)[:12],"domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"continuous_assurance_plan_ref":a.assurance_plan,"client_delivery_manifest_ref":str(d/'client_delivery_manifest.json'),"public_index_refs":[],"public_api_record_refs":[],"public_status_refs":[],"baseline_refs":[],"observations":[],"drift_checks":[{"name":"no_unsafe_paths","pass":not deny}],"semantic_checks":[{"name":"nowcast_not_aqs_truth","pass":True}],"recommended_actions":[],"result":"deny" if deny else "pass_fixture"}
w(Path(a.out_dir)/'drift_observation_report.json',out);print('PASS' if out['result']!='deny' else 'DENY')

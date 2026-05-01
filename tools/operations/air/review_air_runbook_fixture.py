#!/usr/bin/env python
import argparse
from pathlib import Path
from _assurance_common import *
p=argparse.ArgumentParser();[p.add_argument(x,required=True) for x in ('--assurance-plan','--handoff-dir','--out-dir')];p.add_argument('--as-of');p.add_argument('--allow-fixture-runbook-review',action='store_true');a=p.parse_args();rb=j(Path(a.handoff_dir)/'runbook_activation_candidate.json')
deny=bad_text(rb)
out={"schema_version":"1.0.0","runbook_review_id":"rr-"+h(a.assurance_plan)[:12],"domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"continuous_assurance_plan_ref":a.assurance_plan,"runbook_activation_candidate_ref":str(Path(a.handoff_dir)/'runbook_activation_candidate.json'),"operational_handoff_package_ref":str(Path(a.handoff_dir)/'operational_handoff_package.json'),"review_scope":["fixture"],"checks":[],"findings":[],"recommended_updates":[],"forbidden_actions":["no live ops"],"status":"blocked" if deny else "fixture_review_passed"}
w(Path(a.out_dir)/'runbook_review_record.json',out);print('PASS' if not deny else 'DENY')

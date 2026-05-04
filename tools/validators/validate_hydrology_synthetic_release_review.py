import json,sys
p='fixtures/domains/hydrology/review_records/hydrology_synthetic_streamflow.synthetic_public_release.review_record.json'
o=json.load(open(p))
req=['review_record_id','evidence_bundle_ids','policy_decision_ids','release_candidate_ids','finite_state']
assert all(k in o for k in req)
assert o['finite_state']=='APPROVED_SYNTHETIC_PUBLIC_RELEASE'
assert o['synthetic'] and o['no_network'] and o['not_official_source_data']
print('ok')

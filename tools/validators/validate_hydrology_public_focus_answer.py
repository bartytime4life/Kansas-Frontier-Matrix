import json
ans=json.load(open('fixtures/domains/hydrology/focus/hydrology_synthetic_streamflow.public_answer_released.json'))
absn=json.load(open('fixtures/domains/hydrology/focus/hydrology_synthetic_streamflow.public_abstain_unreleased.json'))
err=json.load(open('fixtures/domains/hydrology/focus/hydrology_synthetic_streamflow.public_error_invalid_evidence_ref.json'))
assert ans['finite_state']=='ANSWER' and ans['release_manifest_ids']
assert absn['finite_state']=='ABSTAIN'
assert err['finite_state']=='ERROR'
assert ans['model_runtime_used'] is False and ans['direct_model_output_used'] is False
print('ok')

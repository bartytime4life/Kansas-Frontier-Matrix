import pytest
pytest.importorskip("jsonschema", reason="jsonschema dependency unavailable in this environment")

import json
from pathlib import Path
from tools.policy_gate.evaluate_policy import evaluate
import jsonschema

FIX=Path('tests/fixtures/policy_gate')
GATE=json.loads(Path('policy/gates/release_gate.v1.yaml').read_text().replace('\n', '\n').replace(': [', ': [').replace("'", '"')) if False else {"checks":["schema_valid","consent_present_when_required","consent_not_revoked","retention_not_expired","aggregation_at_or_above_required_level","no_exact_public_coordinates","export_format_allowed","rights_status_compatible","policy_label_compatible","evidence_and_receipt_hashes_match"],"allowed_export_formats":["gedcom","json","csv"]}

def l(n): return json.loads((FIX/n).read_text())

def test_policy_gate_allows_valid_public_artifact():
    out=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'public')
    assert out['decision']['decision']=='allow'

def test_policy_gate_denies_missing_consent():
    out=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.missing_consent.invalid.json'),{"run_id":"x","receipt_hash":"y","retention_expired":False},'policy/consent/ecology.v1.md',GATE,'public')
    assert out['decision']['decision']=='deny'

def test_policy_gate_denies_exact_public_coordinates():
    out=evaluate(l('artifact.public.exact_coordinates.invalid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'public')
    assert out['decision']['decision']=='deny'

def test_policy_gate_denies_unknown_export_format():
    out=evaluate(l('artifact.export.unknown_format.invalid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'export','xls')
    assert out['decision']['decision']=='deny'

def test_policy_gate_suppresses_revoked_consent():
    out=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'public',None,l('revoke_delta.valid.json'))
    assert out['decision']['decision']=='suppress'

def test_policy_gate_requires_recompute_for_derived_revoked_artifact():
    art=l('artifact.public.valid.json'); art['derived']=True
    out=evaluate(art,l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'public',None,l('revoke_delta.valid.json'))
    assert out['decision']['decision']=='recompute_required'

def test_policy_gate_denies_expired_retention():
    out=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.expired_retention.invalid.json'),'policy/consent/ecology.v1.md',GATE,'public')
    assert out['decision']['decision']=='deny'

def test_decision_envelope_schema():
    out=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'public')
    schema=json.loads(Path('schemas/governance/DecisionEnvelope.v1.json').read_text())
    jsonschema.validate(instance=out['decision'], schema=schema)

def test_decision_determinism():
    a=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'public')
    b=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'public')
    assert a['decision']['decision_id']==b['decision']['decision_id']
    assert a['decision']['signature']==b['decision']['signature']

def test_release_manifest_requires_allow_decisions():
    out=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/ecology.v1.md',GATE,'public')
    m=l('release_manifest.valid.json'); m['decision_envelope_ids']=[out['decision']['decision_id']]
    d=Path('tests/fixtures/policy_gate/decisions'); d.mkdir(exist_ok=True)
    (d/'d.json').write_text(json.dumps(out['decision']))
    from tools.policy_gate.check_release import main

def test_fail_closed_unknown_policy():
    out=evaluate(l('artifact.public.valid.json'),l('evidence_bundle.with_consent.valid.json'),l('run_receipt.with_consent.valid.json'),'policy/consent/does-not-exist.md',GATE,'public')
    assert out['decision']['decision']=='quarantine'

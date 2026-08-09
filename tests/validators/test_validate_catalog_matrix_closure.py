from __future__ import annotations
import importlib.util, json, socket, subprocess, sys, tempfile
from pathlib import Path
from unittest import mock
from jsonschema import Draft202012Validator, FormatChecker
ROOT=Path(__file__).resolve().parents[2]
VALIDATOR=ROOT/'tools/validators/validate_catalog_matrix_closure.py'
SCHEMA=ROOT/'schemas/contracts/v1/data/catalog_matrix_closure_profile.schema.json'
FIXTURES=ROOT/'fixtures/data/catalog_matrix/closure'
MANIFEST=FIXTURES/'expected_findings_manifest.json'
SPEC=importlib.util.spec_from_file_location('validate_catalog_matrix_closure',VALIDATOR); assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=MODULE; SPEC.loader.exec_module(MODULE)
def cases(): return json.loads(MANIFEST.read_text())['cases']
def test_schema_is_closed_and_points_to_current_validator():
    schema=json.loads(SCHEMA.read_text()); Draft202012Validator.check_schema(schema)
    assert schema['additionalProperties'] is False
    assert schema['x-kfm']['validator']=='tools/validators/validate_catalog_matrix_closure.py'
def test_manifest_has_exact_polarity():
    assert len(cases())==12
    assert {c['case_kind'] for c in cases()}=={'VALID','SCHEMA_NEGATIVE','SEMANTIC_NEGATIVE'}
def test_exact_manifest_results():
    for case in cases():
        result=MODULE.validate(FIXTURES/case['path'])
        assert result.outcome==case['expected_outcome'],case['case_id']
        assert sorted({f.code for f in result.findings})==sorted(case['expected_findings']),case['case_id']
def test_schema_and_semantic_negative_separation():
    validator=Draft202012Validator(json.loads(SCHEMA.read_text()),format_checker=FormatChecker())
    for case in cases():
        errors=list(validator.iter_errors(json.loads((FIXTURES/case['path']).read_text())))
        if case['case_kind']=='SCHEMA_NEGATIVE': assert errors,case['case_id']
        elif case['case_kind']=='SEMANTIC_NEGATIVE': assert not errors,case['case_id']
def test_internal_reference_is_denied_without_echo():
    result=MODULE.validate(FIXTURES/'semantic_invalid/semantic_internal_reference.json')
    rendered=json.dumps([f.__dict__ for f in result.findings])
    assert 'INTERNAL_REFERENCE_DENIED' in rendered and 'internal:evidence:secret' not in rendered
def test_duplicate_nonfinite_and_symlink_fail_closed():
    with tempfile.TemporaryDirectory() as directory:
        root=Path(directory); duplicate=root/'duplicate.json'; nonfinite=root/'nonfinite.json'
        duplicate.write_text('{"id":"a","id":"b"}'); nonfinite.write_text('{"value":NaN}')
        assert {f.code for f in MODULE.validate(duplicate).findings}=={'JSON_DUPLICATE_KEY'}
        assert {f.code for f in MODULE.validate(nonfinite).findings}=={'JSON_NONFINITE_NUMBER'}
        target=root/'target.json'; link=root/'link.json'; target.write_text('{}')
        try: link.symlink_to(target)
        except (OSError,NotImplementedError): return
        assert {f.code for f in MODULE.validate(link).findings}=={'INPUT_SYMLINK_DENIED'}
def test_no_network_deterministic_replay_and_cli():
    with mock.patch.object(socket,'create_connection',side_effect=AssertionError('network')),mock.patch.object(socket,'socket',side_effect=AssertionError('network')):
        first=[MODULE.validate(FIXTURES/c['path']) for c in cases()]; second=[MODULE.validate(FIXTURES/c['path']) for c in cases()]
    assert first==second
    run=subprocess.run([sys.executable,str(VALIDATOR),'--fixtures'],cwd=ROOT,text=True,capture_output=True)
    assert run.returncode==0,run.stdout+run.stderr
    assert 'CATALOG_MATRIX_CLOSURE_FIXTURES_VALID cases=12' in run.stdout
def test_cli_exit_codes_are_finite():
    for path,expected in [(FIXTURES/'valid/valid_ready_hydrology.json',0),(FIXTURES/'semantic_invalid/semantic_digest_mismatch.json',1),(ROOT/'missing.json',2)]:
        run=subprocess.run([sys.executable,str(VALIDATOR),str(path)],cwd=ROOT,text=True,capture_output=True)
        assert run.returncode==expected,run.stdout+run.stderr

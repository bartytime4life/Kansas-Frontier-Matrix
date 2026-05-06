import json
from pathlib import Path
from tools.soilgrids import soilgrids_independent_verifier as m


def test_rejects_missing_verifier_spec(tmp_path):
    try:
        m.main(["--verifier-spec", str(tmp_path/"missing.json"), "--output-root", str(tmp_path/"out"), "--mode", "full-verify"])
        assert False
    except FileNotFoundError:
        assert True


def test_rejects_unsupported_schema():
    try:
        m.validate_verifier_spec({"schema":"Nope.v1"})
        assert False
    except m.VerifierError as e:
        assert e.code == 100


def test_verifier_spec_hash_stable():
    s = json.loads(Path("verifier/verifier_spec_example.json").read_text())
    assert m.compute_verifier_spec_hash(s) == m.compute_verifier_spec_hash(s)


def test_verification_plan_hash_stable():
    s = json.loads(Path("verifier/verifier_spec_example.json").read_text())
    p = m.build_verification_plan("full-verify", "abc", s, [], None, None, None)
    assert m.compute_verification_plan_hash(p) == m.compute_verification_plan_hash(p)


def test_stdout_only_receipt_path_on_success(tmp_path, capsys):
    spec = tmp_path/"verifier_spec.json"
    spec.write_text(Path("verifier/verifier_spec_example.json").read_text())
    rc = m.main(["--verifier-spec", str(spec), "--output-root", str(tmp_path/"out"), "--mode", "full-verify"])
    out = capsys.readouterr().out.strip()
    assert rc == 0
    assert out.endswith("verifier_receipt.json")

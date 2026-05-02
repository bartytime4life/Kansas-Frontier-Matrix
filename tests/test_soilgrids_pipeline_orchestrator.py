import json
from pathlib import Path

import pytest

import soilgrids_pipeline_orchestrator as m


def _spec(tmp_path: Path):
    w = tmp_path / "workspace"
    w.mkdir()
    (w / "receipt.json").write_text(json.dumps({"schema": "RunReceipt.v1", "status": "success", "spec_hash": "abc"}))
    (w / "out.txt").write_text("ok")
    script = tmp_path / "ok.py"
    script.write_text("import json, pathlib; p=pathlib.Path('workspace/receipt.json'); p.write_text(json.dumps({'schema':'RunReceipt.v1','status':'success','spec_hash':'abc'})); pathlib.Path('workspace/out.txt').write_text('ok')")
    return {
        "schema": "PipelineSpec.v1",
        "pipeline_id": "p1",
        "workspace": str(tmp_path),
        "network_profile": "offline-fixture",
        "mutation_profile": "local-only",
        "stages": [
            {
                "stage_id": "layer01",
                "layer": 1,
                "enabled": True,
                "execution_backend": "subprocess",
                "command": ["python", str(script)],
                "expected_receipt_schema": "RunReceipt.v1",
                "receipt_path": "workspace/receipt.json",
                "expected_outputs": ["workspace/out.txt"],
                "depends_on": [],
                "policy": {"required": True},
            }
        ],
    }


def test_rejects_missing_pipeline_spec(tmp_path):
    with pytest.raises(m.SpecError):
        m.load_pipeline_spec(tmp_path / "missing.json")


def test_pipeline_spec_hash_stable(tmp_path):
    s = _spec(tmp_path)
    assert m.compute_pipeline_spec_hash(s) == m.compute_pipeline_spec_hash(s)


def test_plan_hash_stable(tmp_path):
    s = _spec(tmp_path)
    p = m.build_pipeline_plan(s)
    assert m.compute_plan_hash(p) == m.compute_plan_hash(p)


def test_subprocess_stage_success(tmp_path):
    s = _spec(tmp_path)
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(s))
    receipt, code = m.orchestrate_pipeline(spec_path, tmp_path / "runs", "execute-local", deterministic_run_id=True)
    assert code == 0
    assert receipt.exists()


def test_plan_only_executes_no_stages(tmp_path):
    s = _spec(tmp_path)
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(s))
    receipt, code = m.orchestrate_pipeline(spec_path, tmp_path / "runs", "plan-only", deterministic_run_id=True)
    d = json.loads(receipt.read_text())
    assert code == 0
    assert d["status"] == "planned"


def test_stdout_only_receipt_path_on_success(tmp_path, capsys):
    s = _spec(tmp_path)
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(s))
    code = m.main(["--pipeline-spec", str(spec_path), "--run-root", str(tmp_path / "runs"), "--mode", "plan-only", "--deterministic-run-id"])
    out = capsys.readouterr().out.strip()
    assert code == 0
    assert out.endswith("pipeline_run_receipt.json")

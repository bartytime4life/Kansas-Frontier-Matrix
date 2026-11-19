from __future__ import annotations

from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "packages/pipelines-core/src"))

from pipelines_core.core import PipelineError, Stage, canonical_bytes, run_pipeline

SPEC = "sha256:" + "a" * 64


def run(stages, value=None, **kwargs):
    return run_pipeline(stages, value, spec_hash=SPEC, code_ref="git:synthetic-v1", **kwargs)


def test_pipeline_composes_real_outputs_and_schema_valid_receipts():
    stages = [
        Stage("normalize", lambda c: [str(x).strip().upper() for x in c["input"]]),
        Stage("count", lambda c: {"count": len(c["dependencies"]["normalize"])}, ("normalize",)),
    ]
    result = run(stages, [" ks ", "ne"])
    assert result["artifacts"] == {"normalize": ["KS", "NE"], "count": {"count": 2}}
    assert result["outcome"] == "SUCCESS"
    assert result["source_admitted"] is result["release_authorized"] is result["publication_authorized"] is False
    validator = Draft202012Validator(json.loads((ROOT / "schemas/contracts/v1/runtime/run_receipt.schema.json").read_text()))
    for step in result["steps"]:
        validator.validate(step["receipt"])
        assert step["receipt"]["outputs"] == ["sha256:" + hashlib.sha256(canonical_bytes(result["artifacts"][step["name"]])).hexdigest()]


def test_replay_and_stage_declaration_order_are_deterministic():
    a = Stage("a", lambda c: c["input"])
    b = Stage("b", lambda c: c["dependencies"]["a"], ("a",))
    assert run([b, a], {"z": 1, "a": 2}) == run([a, b], {"a": 2, "z": 1})
    assert run([a], 1)["run_id"] != run([a], 2)["run_id"]


def test_inputs_and_dependency_results_cannot_be_mutated_by_another_stage():
    original = {"items": [1]}
    def mutate(c):
        c["input"]["items"].append(2)
        c["dependencies"]["a"]["items"].append(3)
        return c["dependencies"]["a"]
    result = run([Stage("a", lambda c: c["input"]), Stage("b", mutate, ("a",))], original)
    assert original == {"items": [1]}
    assert result["artifacts"]["a"] == original
    assert result["artifacts"]["b"] == {"items": [1, 3]}


def test_failure_blocks_descendants_but_preserves_independent_branch():
    calls = []
    def fail(c):
        raise RuntimeError("secret-provider-token-never-returned")
    result = run([Stage("a", fail), Stage("b", lambda c: calls.append("b"), ("a",)),
                  Stage("c", lambda c: {"kept": True})])
    assert calls == []
    assert result["outcome"] == "PARTIAL"
    assert result["artifacts"] == {"c": {"kept": True}}
    assert [s["reason_code"] for s in result["steps"]] == ["STAGE_EXECUTION_FAILED", "COMPLETED", "DEPENDENCY_FAILED"]
    assert "secret-provider" not in json.dumps(result)
    assert result["steps"][-1]["receipt"]["outputs"] == []


def test_validator_rejection_does_not_expose_or_deliver_invalid_output():
    def reject(value):
        raise ValueError("private rejected value")
    result = run([Stage("a", lambda c: {"private": "payload"}, validate=reject)])
    assert result["outcome"] == "FAIL"
    assert result["artifacts"] == {}
    assert "private" not in json.dumps(result)


@pytest.mark.parametrize("validator", [lambda v: False, lambda v: True, lambda v: []])
def test_non_raising_validator_must_return_none(validator):
    assert run([Stage("a", lambda c: 1, validate=validator)])["steps"][0]["reason_code"] == "VALIDATOR_CONTRACT_INVALID"


@pytest.mark.parametrize("stages,code", [
    ([], "STAGE_COUNT_INVALID"),
    ([Stage("a", lambda c: 1), Stage("a", lambda c: 2)], "STAGE_INVALID"),
    ([Stage("a", lambda c: 1, ("missing",))], "DEPENDENCY_MISSING"),
    ([Stage("a", lambda c: 1, ("a",))], "DEPENDENCY_CYCLE"),
    ([Stage("a", lambda c: 1, ("b",)), Stage("b", lambda c: 1, ("a",))], "DEPENDENCY_CYCLE"),
    ([Stage("a", lambda c: 1, ("b", "b")), Stage("b", lambda c: 1)], "DEPENDENCIES_INVALID"),
    ([Stage("bad/name", lambda c: 1)], "STAGE_INVALID"),
])
def test_invalid_graph_is_rejected_before_any_work(stages, code):
    calls = []
    stages = [replace(stage, transform=lambda c: calls.append("called")) for stage in stages]
    with pytest.raises(PipelineError, match=code):
        run(stages)
    assert calls == []


@pytest.mark.parametrize("value,code", [(float("nan"), "ARTIFACT_NONFINITE"),
    (float("inf"), "ARTIFACT_NONFINITE"), ({1: "coerced"}, "ARTIFACT_KEYS_INVALID"),
    ((1, 2), "ARTIFACT_NOT_JSON"), (b"binary", "ARTIFACT_NOT_JSON"),
    ("x" * (4 * 1024 * 1024), "ARTIFACT_BYTE_LIMIT")])
def test_invalid_input_is_rejected(value, code):
    with pytest.raises(PipelineError, match=code):
        run([Stage("a", lambda c: 1)], value)


def test_cycles_and_deeply_nested_artifacts_are_bounded():
    value = []; value.append(value)
    with pytest.raises(PipelineError, match="ARTIFACT_STRUCTURE_LIMIT"):
        canonical_bytes(value)
    assert run([Stage("a", lambda c: value)])["outcome"] == "FAIL"


def test_failed_pipeline_has_no_successful_receipt():
    result = run([Stage("a", lambda c: float("nan"))])
    assert result["outcome"] == "FAIL"
    assert result["steps"][0]["receipt"]["outcome"] == "FAIL"
    assert result["steps"][0]["reason_code"] == "ARTIFACT_NONFINITE"


def test_code_and_declared_validation_inputs_are_bound_to_run_identity():
    stages = [Stage("a", lambda c: 1)]
    first = run(stages)
    second = run_pipeline(stages, None, spec_hash=SPEC, code_ref="git:synthetic-v2")
    assert first["run_id"] != second["run_id"]
    assert first["run_id"] != run(stages, validation_refs=["schema:synthetic"])["run_id"]


def test_cancellation_is_not_converted_to_a_failed_data_record():
    def cancel(c):
        raise KeyboardInterrupt
    with pytest.raises(KeyboardInterrupt):
        run([Stage("a", cancel)])


def test_total_artifact_budget_is_enforced_across_stages(monkeypatch):
    import pipelines_core.core as core
    monkeypatch.setattr(core, "MAX_TOTAL_ARTIFACT_BYTES", 20)
    result = run([Stage("a", lambda c: "0123456789"), Stage("b", lambda c: "0123456789")])
    assert result["outcome"] == "PARTIAL"
    assert set(result["artifacts"]) == {"a"}
    assert result["steps"][1]["reason_code"] == "ARTIFACT_TOTAL_BYTE_LIMIT"


@pytest.mark.parametrize("refs", [["same", "same"], "not-an-array", [True], ["bad\nref"]])
def test_invalid_reference_bindings_are_rejected(refs):
    with pytest.raises(PipelineError, match="REFERENCES_INVALID"):
        run([Stage("a", lambda c: 1)], validation_refs=refs)


def test_existing_mesonet_normalizer_runs_as_a_pipeline_and_holds_invalid_station():
    from pipelines.domains.soil.mesonet_normalizer.fixture_normalizer import normalize_fixture
    fixture = json.loads((ROOT / "fixtures/domains/soil/mesonet_normalizer/valid/native_station_record.json").read_text())
    def normalize(context):
        result = normalize_fixture(context["input"])
        if not result.ok:
            raise PipelineError("NORMALIZATION_HELD")
        return result.candidate
    stages = [Stage("normalize", normalize), Stage("summary", lambda c: {
        "cadence": c["dependencies"]["normalize"]["observation"]["output_cadence_minutes"],
        "public_use_allowed": c["dependencies"]["normalize"]["governance"]["public_use_allowed"],
    }, ("normalize",))]
    result = run(stages, fixture)
    assert result["outcome"] == "SUCCESS"
    assert result["artifacts"]["summary"] == {"cadence": 5, "public_use_allowed": False}
    fixture["station"]["station_health"] = "UNKNOWN"
    held = run(stages, fixture)
    assert held["outcome"] == "FAIL"
    assert held["artifacts"] == {}
    assert held["steps"][1]["reason_code"] == "DEPENDENCY_FAILED"

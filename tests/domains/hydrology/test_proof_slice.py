"""Gate, integrity, and determinism tests for the synthetic Hydrology proof slice."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "pipelines/domains/hydrology/proof_slice.py"
SPEC = importlib.util.spec_from_file_location("kfm_hydrology_proof_slice", MODULE_PATH)
assert SPEC and SPEC.loader
proof_slice = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = proof_slice
SPEC.loader.exec_module(proof_slice)

PROFILE = ROOT / proof_slice.DEFAULT_PROFILE
FIXTURES = "fixtures/domains/hydrology/proof_slice"
THIN_SLICE_ASSERTIONS = set(range(1, 11))


@pytest.fixture(scope="module")
def record() -> dict:
    return proof_slice.build_record()


@pytest.fixture(scope="module")
def context() -> dict:
    registry = proof_slice.build_registry(ROOT)
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    inputs = proof_slice.PinnedInputs()
    for entry in (profile["packet"], profile["base_request"], *profile["evidence_bundles"], *profile["cases"]):
        inputs.pin(entry)
    return {
        "profile": profile,
        "inputs": inputs,
        "packet": inputs.load(profile["packet"]["path"]),
        "packet_digest": profile["packet"]["sha256"],
        "bundle_validator": proof_slice._schema_validator("evidence_bundle.schema.json", registry=registry),
        "base": inputs.load(profile["base_request"]["path"]),
    }


def decide(context: dict, **overrides: object) -> proof_slice.Decision:
    request = copy.deepcopy(context["base"])
    request.update(overrides)
    return proof_slice.decide(
        request,
        profile=context["profile"],
        inputs=context["inputs"],
        packet=context["packet"],
        packet_digest=context["packet_digest"],
        bundle_validator=context["bundle_validator"],
    )


def test_every_pinned_case_reaches_its_expected_outcome(record: dict) -> None:
    assert record["outcome"] == "PASS"
    assert record["packet_validation"] == {"outcome": "PASS", "findings": []}
    assert [case["case_id"] for case in record["cases"] if not case["matched"]] == []
    assert len(record["cases"]) == 14


def test_all_ten_thin_slice_assertions_are_covered(record: dict) -> None:
    covered = {case["thin_slice_assertion"] for case in record["cases"]} - {None}
    assert covered == THIN_SLICE_ASSERTIONS


def test_every_outcome_class_is_exercised(record: dict) -> None:
    assert {case["envelope"]["outcome"] for case in record["cases"]} == {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


def test_record_declares_no_effects_and_synthetic_posture(record: dict) -> None:
    assert record["posture"] == "SYNTHETIC_FIXTURE_ONLY"
    assert set(record["effects"].values()) == {False}
    assert record["rollback_rehearsal"]["outcome"] == "PASS"
    assert record["rollback_rehearsal"]["pointer_after_rollback"] == record["rollback_rehearsal"]["pointer_before"]


def test_record_spec_hash_covers_its_content(record: dict) -> None:
    body = {key: value for key, value in record.items() if key != "spec_hash"}
    assert proof_slice.compute_spec_hash(body) == record["spec_hash"]["value"]


def test_run_is_deterministic_and_passes() -> None:
    code, first = proof_slice.run()
    again, second = proof_slice.run()
    assert (code, again) == (0, 0)
    assert first == second


def test_answer_carries_citation_obligations_and_evidence(context: dict) -> None:
    decision = decide(context)
    assert decision.outcome == "ANSWER"
    assert "CITE_SYNTHETIC_FIXTURE" in decision.obligations
    assert decision.evidence_refs[0] == "hydrology:proof-slice:bundle:fixture-v1"


def test_stale_answer_requires_a_stale_badge(context: dict) -> None:
    decision = decide(context, scenario_id="stale")
    assert (decision.outcome, decision.reason_code) == ("ANSWER", "FRESHNESS_THRESHOLD_EXCEEDED")
    assert "DISPLAY_STALE_BADGE" in decision.obligations


@pytest.mark.parametrize(
    "requested",
    [
        "data/raw/hydrology/x.json",
        "data/work/hydrology/x.json",
        "data/quarantine/hydrology/x.json",
        "data/published/raw/hydrology/x.json",
        "data/published/../raw/x.json",
        "/data/published/x.json",
        "fixtures/domains/hydrology/x.json",
    ],
)
def test_non_public_paths_are_denied(context: dict, requested: str) -> None:
    decision = decide(context, requested_artifact=requested)
    assert (decision.outcome, decision.reason_code) == ("DENY", "PUBLIC_RAW_PATH_DENIED")


def test_trust_membrane_gate_precedes_evidence(context: dict) -> None:
    decision = decide(context, surface="browser_direct_model", evidence_bundle=None)
    assert decision.reason_code == "UI_DIRECT_MODEL_CALL_DENIED"


def test_unavailable_evaluator_is_an_error_even_with_bad_evidence(context: dict) -> None:
    decision = decide(context, policy_evaluator="unavailable", evidence_bundle=None)
    assert (decision.outcome, decision.reason_code) == ("ERROR", "POLICY_EVALUATOR_UNAVAILABLE")


def test_unpinned_evidence_bundle_is_an_error(context: dict) -> None:
    decision = decide(context, evidence_bundle="fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json")
    assert (decision.outcome, decision.reason_code) == ("ERROR", "EVIDENCE_INPUT_NOT_PINNED")


def test_regulatory_context_may_be_shown_as_context(context: dict) -> None:
    decision = decide(context, feature_source_role="regulatory_context", presented_as="regulatory_context_overlay")
    assert decision.outcome == "ANSWER"


@pytest.mark.parametrize(
    "role, presented",
    [
        ("regulatory_context", "observed_flood_event"),
        ("regulatory_context", "observed_gauge_series"),
        ("synthetic_observation", "observed_flood_event"),
        ("synthetic_observation", "regulatory_context_overlay"),
    ],
)
def test_source_role_collapse_is_denied(context: dict, role: str, presented: str) -> None:
    decision = decide(context, feature_source_role=role, presented_as=presented)
    assert (decision.outcome, decision.reason_code) == ("DENY", "SOURCE_ROLE_COLLAPSE")


def test_unknown_scenario_is_an_error(context: dict) -> None:
    decision = decide(context, scenario_id="not-declared")
    assert (decision.outcome, decision.reason_code) == ("ERROR", "SCENARIO_UNKNOWN")


@pytest.fixture
def scratch_profile(request: pytest.FixtureRequest):
    written: list[Path] = []

    def make(profile: dict) -> str:
        relative = f"{FIXTURES}/_test_{request.node.name[:40]}.profile.json"
        path = ROOT / relative
        path.write_text(json.dumps(profile), encoding="utf-8")
        written.append(path)
        return relative

    yield make
    for path in written:
        path.unlink(missing_ok=True)


def test_digest_mismatch_stops_the_run(scratch_profile) -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    profile["cases"][0]["sha256"] = "sha256:" + "0" * 64
    code, output = proof_slice.run(scratch_profile(profile))
    assert code == 2
    assert "pinned digest mismatch" in json.loads(output)["reason"]


def test_unused_pinned_input_with_a_bad_digest_stops_the_run(scratch_profile) -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    profile["evidence_bundles"].append(
        {"path": f"{FIXTURES}/README.md", "sha256": "sha256:" + "0" * 64}
    )
    code, output = proof_slice.run(scratch_profile(profile))
    assert code == 2
    assert "pinned digest mismatch" in json.loads(output)["reason"]


def test_unused_pinned_input_that_is_missing_stops_the_run(scratch_profile) -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    profile["evidence_bundles"].append(
        {"path": f"{FIXTURES}/does-not-exist.json", "sha256": "sha256:" + "0" * 64}
    )
    code, output = proof_slice.run(scratch_profile(profile))
    assert code == 2
    assert "not a regular file" in json.loads(output)["reason"]


def test_wrong_expectation_fails_the_record(scratch_profile) -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    profile["cases"][0]["expected_outcome"] = "DENY"
    code, output = proof_slice.run(scratch_profile(profile))
    assert code == 1
    record = json.loads(output)
    assert record["outcome"] == "FAIL"
    assert [case["case_id"] for case in record["cases"] if not case["matched"]] == ["01-answer-current"]


def test_schema_invalid_profile_stops_the_run(scratch_profile) -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    profile["posture"] = "REAL_SOURCE"
    code, output = proof_slice.run(scratch_profile(profile))
    assert code == 2
    assert "schema-invalid" in json.loads(output)["reason"]


def test_absolute_or_parent_profile_paths_are_refused() -> None:
    assert proof_slice.run("/etc/passwd")[0] == 2
    assert proof_slice.run("../outside.json")[0] == 2


def test_output_into_lifecycle_storage_is_refused(capsys: pytest.CaptureFixture[str]) -> None:
    target = ROOT / "data/proofs/hydrology/record.json"
    assert proof_slice.main(["--output", str(target)]) == 2
    assert not target.exists()


def test_output_path_receives_the_record(tmp_path: Path) -> None:
    target = tmp_path / "record.json"
    assert proof_slice.main(["--output", str(target)]) == 0
    assert json.loads(target.read_text(encoding="utf-8"))["outcome"] == "PASS"


def test_profile_pins_match_committed_bytes() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    for entry in (profile["packet"], profile["base_request"], *profile["evidence_bundles"], *profile["cases"]):
        actual = "sha256:" + hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        assert actual == entry["sha256"], entry["path"]


def test_every_case_fixture_is_pinned() -> None:
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    pinned = {entry["path"] for entry in profile["cases"]}
    on_disk = {path.relative_to(ROOT).as_posix() for path in (ROOT / FIXTURES / "cases").glob("*.json")}
    assert on_disk == pinned

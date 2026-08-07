from __future__ import annotations

import copy
import json
import os
import socket
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.governance.validate_implementation_review_packet import (
    EXIT_ERROR,
    EXIT_HOLD,
    FIXTURE_PATH,
    MAX_DECISIONS,
    evaluate_bound_documents,
    evaluate_paths,
    payload,
    render_markdown,
    run_fixture_suite,
)
from tools.validators.governance.implementation_change_context_model import (
    evaluate_document as evaluate_context_document,
)
from tools.validators.governance.validate_implementation_decision_record import (
    evaluate_document as evaluate_decision_document,
)


def _cases() -> dict[str, dict[str, object]]:
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    return {case["name"]: case for case in manifest["cases"]}


def _write_packet(
    root: Path,
    context: dict[str, object],
    decisions: list[dict[str, object]],
) -> tuple[Path, list[Path]]:
    context_path = root / "context.json"
    context_path.write_text(json.dumps(context), encoding="utf-8")
    decision_paths: list[Path] = []
    for index, decision in enumerate(decisions):
        path = root / f"decision-{index}.json"
        path.write_text(json.dumps(decision), encoding="utf-8")
        decision_paths.append(path)
    return context_path, decision_paths


def test_fixture_manifest_has_exact_polarity() -> None:
    ok, result = run_fixture_suite()
    assert ok, result
    assert result == {
        "authority": "NONE",
        "outcome": "PASS",
        "cases": 7,
        "mismatches": [],
    }


def test_ready_packet_is_exact_bound_and_non_authoritative() -> None:
    case = _cases()["ready-exact-binding"]
    with tempfile.TemporaryDirectory() as directory:
        context_path, decision_paths = _write_packet(
            Path(directory), case["context"], case["decisions"]
        )
        packet = evaluate_paths(context_path, decision_paths)
    result = payload(packet)
    assert packet.evaluation.outcome == "READY"
    assert result["renderable"] is True
    assert result["decision_count"] == 1
    assert result["covered_path_count"] == 2
    assert result["uncovered_path_count"] == 2
    assert set(result["permissions"].values()) == {False}


def test_reference_set_mismatch_fails_closed() -> None:
    case = _cases()["error-reference-set-mismatch"]
    evaluation = evaluate_bound_documents(
        case["context"],
        evaluate_context_document(case["context"]),
        [],
    )
    assert evaluation.outcome == "ERROR"
    assert [finding.code for finding in evaluation.findings] == [
        "DECISION_REFERENCE_SET_MISMATCH"
    ]


def test_change_reference_and_scope_must_bind_to_context() -> None:
    cases = _cases()
    for name, expected in (
        ("error-change-ref-mismatch", "DECISION_CHANGE_REF_MISMATCH"),
        ("error-path-outside-change", "DECISION_PATH_OUTSIDE_CHANGE"),
    ):
        case = cases[name]
        rows = [
            (
                Path("decision.json"),
                case["decisions"][0],
                evaluate_decision_document(case["decisions"][0]),
            )
        ]
        evaluation = evaluate_bound_documents(
            case["context"], evaluate_context_document(case["context"]), rows
        )
        assert evaluation.outcome == "ERROR"
        assert [finding.code for finding in evaluation.findings] == [expected]


def test_invalid_record_id_is_not_reflected_in_findings() -> None:
    case = copy.deepcopy(_cases()["error-invalid-decision-input"])
    decision = case["decisions"][0]
    decision["record_id"] = "/tmp/private-local-input.json"
    rows = [
        (
            Path("private-local-input.json"),
            decision,
            evaluate_decision_document(decision),
        )
    ]
    evaluation = evaluate_bound_documents(
        case["context"], evaluate_context_document(case["context"]), rows
    )
    rendered = json.dumps(
        [{"code": finding.code, "field": finding.field} for finding in evaluation.findings]
    )
    with tempfile.TemporaryDirectory() as directory:
        context_path, decision_paths = _write_packet(
            Path(directory), case["context"], [decision]
        )
        diagnostic = json.dumps(payload(evaluate_paths(context_path, decision_paths)))
    assert evaluation.outcome == "ERROR"
    assert "private-local-input" not in rendered
    assert "private-local-input" not in diagnostic
    assert "decision[0]" in rendered
    assert "decision[0]" in diagnostic


def test_input_hold_is_preserved_without_becoming_approval() -> None:
    case = _cases()["hold-draft-decision"]
    rows = [
        (
            Path("draft.json"),
            case["decisions"][0],
            evaluate_decision_document(case["decisions"][0]),
        )
    ]
    evaluation = evaluate_bound_documents(
        case["context"], evaluate_context_document(case["context"]), rows
    )
    assert evaluation.outcome == "HOLD"
    assert [finding.code for finding in evaluation.findings] == [
        "DECISION_RECORD_DRAFT"
    ]


def test_invalid_decision_input_is_not_renderable() -> None:
    case = _cases()["error-invalid-decision-input"]
    with tempfile.TemporaryDirectory() as directory:
        context_path, decision_paths = _write_packet(
            Path(directory), case["context"], case["decisions"]
        )
        packet = evaluate_paths(context_path, decision_paths)
    assert packet.evaluation.outcome == "ERROR"
    assert payload(packet)["renderable"] is False
    try:
        render_markdown(packet)
    except ValueError as error:
        assert "not renderable" in str(error)
    else:
        raise AssertionError("ERROR packet rendered")


def test_renderer_is_deterministic_and_prioritizes_hold_records() -> None:
    case = copy.deepcopy(_cases()["ready-exact-binding"])
    ready = case["decisions"][0]
    held = copy.deepcopy(ready)
    held["record_id"] = "kfm:implementation-decision:review-packet:0002"
    held["title"] = "Held review attention"
    held["status"] = "DRAFT"
    held["governance"]["truth_label"] = "NEEDS_VERIFICATION"
    held["validation_refs"] = []
    case["context"]["implementation_decision_refs"] = sorted(
        [ready["record_id"], held["record_id"]]
    )

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        context_path, decision_paths = _write_packet(
            root, case["context"], [ready, held]
        )
        first = evaluate_paths(context_path, decision_paths)
        second = evaluate_paths(context_path, list(reversed(decision_paths)))
        rendered_first = render_markdown(first)
        rendered_second = render_markdown(second)

    assert first.evaluation.outcome == second.evaluation.outcome == "HOLD"
    assert rendered_first == rendered_second
    assert rendered_first.index(":0002") < rendered_first.index(":0001")
    assert "DECISION_RECORD_DRAFT" in rendered_first
    assert "changed-file contents" in rendered_first
    assert "diff --git" not in rendered_first
    assert str(root) not in rendered_first


def test_renderer_lists_uncovered_paths_as_informational() -> None:
    case = _cases()["ready-exact-binding"]
    with tempfile.TemporaryDirectory() as directory:
        context_path, decision_paths = _write_packet(
            Path(directory), case["context"], case["decisions"]
        )
        rendered = render_markdown(evaluate_paths(context_path, decision_paths))
    assert "### Uncovered destination paths" in rendered
    assert "schemas/contracts/v1/governance/implementation_change_context.schema.json" in rendered
    assert "Uncovered paths are informational" in rendered


def test_duplicate_record_ids_are_error() -> None:
    case = copy.deepcopy(_cases()["ready-exact-binding"])
    duplicate = copy.deepcopy(case["decisions"][0])
    case["context"]["implementation_decision_refs"] = [duplicate["record_id"]]
    with tempfile.TemporaryDirectory() as directory:
        context_path, decision_paths = _write_packet(
            Path(directory), case["context"], [case["decisions"][0], duplicate]
        )
        packet = evaluate_paths(context_path, decision_paths)
    assert packet.evaluation.outcome == "ERROR"
    assert {finding.code for finding in packet.evaluation.findings} == {
        "DECISION_DUPLICATE_RECORD_ID"
    }


def test_decision_count_is_bounded_before_loading() -> None:
    case = _cases()["ready-exact-binding"]
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        context_path, _ = _write_packet(root, case["context"], [])
        packet = evaluate_paths(
            context_path,
            [root / f"missing-{index}.json" for index in range(MAX_DECISIONS + 1)],
        )
    assert packet.evaluation.outcome == "ERROR"
    assert [finding.code for finding in packet.evaluation.findings] == [
        "DECISION_LIMIT_EXCEEDED"
    ]


def test_fixture_suite_is_no_network() -> None:
    with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
        ok, result = run_fixture_suite()
    assert ok, result


def test_hold_cli_uses_exit_three_and_renders_review_view() -> None:
    case = _cases()["hold-draft-decision"]
    script = (
        REPO_ROOT
        / "tools/validators/governance/validate_implementation_review_packet.py"
    )
    with tempfile.TemporaryDirectory() as directory:
        context_path, decision_paths = _write_packet(
            Path(directory), case["context"], case["decisions"]
        )
        result = subprocess.run(
            [sys.executable, str(script), str(context_path), *map(str, decision_paths), "--render"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode == EXIT_HOLD
    assert result.stdout.startswith("# Implementation review packet")
    assert "Packet:** `HOLD`" in result.stdout


def test_error_cli_refuses_markdown_and_emits_bounded_json() -> None:
    case = _cases()["error-change-ref-mismatch"]
    script = (
        REPO_ROOT
        / "tools/validators/governance/validate_implementation_review_packet.py"
    )
    with tempfile.TemporaryDirectory() as directory:
        context_path, decision_paths = _write_packet(
            Path(directory), case["context"], case["decisions"]
        )
        result = subprocess.run(
            [sys.executable, str(script), str(context_path), *map(str, decision_paths), "--render"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode == EXIT_ERROR
    output = json.loads(result.stdout)
    assert output["outcome"] == "ERROR"
    assert output["renderable"] is False
    assert output["findings"][0]["code"] == "DECISION_CHANGE_REF_MISMATCH"


def test_cases_cli_output_is_deterministic() -> None:
    script = (
        REPO_ROOT
        / "tools/validators/governance/validate_implementation_review_packet.py"
    )
    environment = dict(os.environ)
    environment["KFM_NO_NETWORK"] = "1"
    command = [sys.executable, str(script), "--cases"]
    first = subprocess.run(
        command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True
    )
    second = subprocess.run(
        command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True
    )
    assert first.returncode == second.returncode == 0
    assert first.stdout == second.stdout

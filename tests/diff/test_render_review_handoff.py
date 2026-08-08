from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools/diff/render_review_handoff.py"
FIXTURES = ROOT / "tests/diff/fixtures/review_handoff"
SPEC = importlib.util.spec_from_file_location("render_review_handoff", TOOL)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _command(*extra: str) -> list[str]:
    return [
        sys.executable,
        str(TOOL),
        "--diff-report",
        str(FIXTURES / "diff_report.json"),
        "--context",
        str(FIXTURES / "context.json"),
        "--policy-map",
        str(FIXTURES / "policy_map.json"),
        *extra,
    ]


def test_golden_json_is_byte_stable() -> None:
    first = subprocess.run(_command(), cwd=ROOT, capture_output=True, text=True, check=False)
    second = subprocess.run(_command(), cwd=ROOT, capture_output=True, text=True, check=False)
    assert first.returncode == 0, first.stderr
    assert first.stdout == second.stdout
    assert first.stdout == (FIXTURES / "expected.json").read_text(encoding="utf-8")

    value = json.loads(first.stdout)
    assert value["handoff_state"] == "HOLD_UNMAPPED_POLICY_IMPACT"
    assert value["policy_impact"]["unmapped_changed_fields"] == ["new_field"]
    assert value["review_handoff"]["allowed_decisions"] == [
        "approve",
        "reject",
        "request_changes",
    ]
    assert value["review_handoff"]["review_record_schema_ref"] == (
        "schemas/contracts/v1/governance/review_record.schema.json"
    )


def test_fail_on_unmapped_impact_is_validation_exit_one() -> None:
    completed = subprocess.run(
        _command("--fail-on-unmapped-impact"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 1
    assert json.loads(completed.stdout)["handoff_state"] == "HOLD_UNMAPPED_POLICY_IMPACT"


def test_markdown_uses_same_normalized_handoff_without_raw_values() -> None:
    completed = subprocess.run(
        _command("--format", "markdown"),
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0
    assert "# KFM diff review handoff" in completed.stdout
    assert "`policy_state`" in completed.stdout
    assert "fixture:left.json" not in completed.stdout
    assert "expected_value" not in completed.stdout


def test_duplicate_keys_fail_closed(tmp_path: Path) -> None:
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text(
        '{"tool":"stable-diff","tool":"other","status":"same","summary":{"added":[],"removed":[],"changed":[]}}',
        encoding="utf-8",
    )
    completed = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--diff-report",
            str(duplicate),
            "--context",
            str(FIXTURES / "context.json"),
            "--policy-map",
            str(FIXTURES / "policy_map.json"),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 2
    assert json.loads(completed.stdout)["error"]["code"] == "JSON_DUPLICATE_KEY"


def test_symlink_input_is_denied(tmp_path: Path) -> None:
    link = tmp_path / "diff-link.json"
    try:
        link.symlink_to(FIXTURES / "diff_report.json")
    except (OSError, NotImplementedError):
        return
    completed = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--diff-report",
            str(link),
            "--context",
            str(FIXTURES / "context.json"),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 2
    assert json.loads(completed.stdout)["error"]["code"] == "INPUT_SYMLINK_DENIED"


def test_handoff_subject_binds_all_three_inputs() -> None:
    diff_path = FIXTURES / "diff_report.json"
    context_path = FIXTURES / "context.json"
    policy_path = FIXTURES / "policy_map.json"
    output = MODULE.build_handoff(
        MODULE.validate_diff_report(MODULE.load_json_object(diff_path)),
        MODULE.validate_context(MODULE.load_json_object(context_path)),
        MODULE.validate_policy_map(MODULE.load_json_object(policy_path)),
        diff_sha256=MODULE._sha256(diff_path),
        context_sha256=MODULE._sha256(context_path),
        policy_map_sha256=MODULE._sha256(policy_path),
    )
    subject = output["review_handoff"]["subject_ref"]
    assert subject.startswith("urn:kfm:diff-review-handoff:sha256:")
    assert len(subject.rsplit(":", 1)[1]) == 64

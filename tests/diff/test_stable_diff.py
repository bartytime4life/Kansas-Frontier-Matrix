from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.diff.stable_diff import (
    EXIT_CHANGED,
    EXIT_ERROR,
    EXIT_OK,
    compare_paths,
    main,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_same_objects_ignore_key_order() -> None:
    report, exit_code = compare_paths(
        FIXTURES / "same" / "left.json",
        FIXTURES / "same" / "right.json",
    )

    assert exit_code == EXIT_OK
    assert report["status"] == "same"
    assert report["blocking"] is False
    assert report["summary"] == {"added": [], "removed": [], "changed": []}


def test_changed_objects_emit_sorted_top_level_summary() -> None:
    report, exit_code = compare_paths(
        FIXTURES / "changed" / "left.json",
        FIXTURES / "changed" / "right.json",
    )

    assert exit_code == EXIT_OK
    assert report["status"] == "changed"
    assert report["blocking"] is False
    assert report["summary"] == {
        "added": ["alpha_added", "zeta_added"],
        "removed": ["beta_removed", "omega_removed"],
        "changed": ["nested_changed", "shared_changed"],
    }


def test_fail_on_change_is_blocking_and_returns_one() -> None:
    report, exit_code = compare_paths(
        FIXTURES / "changed" / "left.json",
        FIXTURES / "changed" / "right.json",
        fail_on_change=True,
    )

    assert exit_code == EXIT_CHANGED
    assert report["status"] == "changed"
    assert report["blocking"] is True


def test_malformed_json_fails_closed() -> None:
    report, exit_code = compare_paths(
        FIXTURES / "malformed" / "invalid.json",
        FIXTURES / "same" / "right.json",
    )

    assert exit_code == EXIT_ERROR
    assert report["status"] == "error"
    assert report["blocking"] is True
    assert report["error"]["code"] == "LEFT_JSON_INVALID"


@pytest.mark.parametrize(
    ("payload", "error_code"),
    [
        ('{"duplicate": 1, "duplicate": 2}', "LEFT_JSON_DUPLICATE_KEY"),
        ('{"value": NaN}', "LEFT_JSON_NONFINITE_NUMBER"),
        ('["not", "an", "object"]', "LEFT_ROOT_NOT_OBJECT"),
    ],
)
def test_ambiguous_or_unsupported_json_fails_closed(
    tmp_path: Path, payload: str, error_code: str
) -> None:
    left = tmp_path / "left.json"
    left.write_text(payload, encoding="utf-8")

    report, exit_code = compare_paths(
        left,
        FIXTURES / "same" / "right.json",
    )

    assert exit_code == EXIT_ERROR
    assert report["status"] == "error"
    assert report["error"]["code"] == error_code


def test_missing_input_fails_closed(tmp_path: Path) -> None:
    report, exit_code = compare_paths(
        tmp_path / "missing.json",
        FIXTURES / "same" / "right.json",
    )

    assert exit_code == EXIT_ERROR
    assert report["error"] == {
        "code": "LEFT_NOT_FOUND",
        "message": "left input does not exist.",
    }


def test_cli_writes_deterministic_report(tmp_path: Path) -> None:
    output = tmp_path / "report.json"

    exit_code = main(
        [
            "--left",
            str(FIXTURES / "changed" / "left.json"),
            "--right",
            str(FIXTURES / "changed" / "right.json"),
            "--output",
            str(output),
            "--fail-on-change",
        ]
    )

    assert exit_code == EXIT_CHANGED
    raw = output.read_text(encoding="utf-8")
    assert raw.endswith("\n")
    assert json.loads(raw)["summary"] == {
        "added": ["alpha_added", "zeta_added"],
        "removed": ["beta_removed", "omega_removed"],
        "changed": ["nested_changed", "shared_changed"],
    }

    second_exit_code = main(
        [
            "--left",
            str(FIXTURES / "changed" / "left.json"),
            "--right",
            str(FIXTURES / "changed" / "right.json"),
            "--output",
            str(output),
            "--fail-on-change",
        ]
    )

    assert second_exit_code == EXIT_CHANGED
    assert raw == output.read_text(encoding="utf-8")


def test_cli_prints_machine_readable_error(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(
        [
            "--left",
            str(FIXTURES / "malformed" / "invalid.json"),
            "--right",
            str(FIXTURES / "same" / "right.json"),
        ]
    )

    assert exit_code == EXIT_ERROR
    report = json.loads(capsys.readouterr().out)
    assert report["status"] == "error"
    assert report["error"]["code"] == "LEFT_JSON_INVALID"

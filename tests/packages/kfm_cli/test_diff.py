"""Real and adverse handoffs for the installed CLI's local diff command."""

from __future__ import annotations

import json
import subprocess
from unittest.mock import patch

from typer.testing import CliRunner

from kfm_cli.cli import build_app


runner = CliRunner()


def test_diff_comparison_uses_caller_paths_and_exit_polarity(tmp_path) -> None:
    left = tmp_path / "left.json"
    right = tmp_path / "right.json"
    left.write_text('{"a":1}', encoding="utf-8")
    right.write_text('{"a":2,"b":3}', encoding="utf-8")
    changed = runner.invoke(build_app(), ["diff", "--left", str(left),
                                          "--right", str(right), "--fail-on-change"])
    assert changed.exit_code == 1
    report = json.loads(changed.stdout)
    assert report["status"] == "changed" and report["blocking"] is True
    assert report["summary"] == {"added": ["b"], "removed": [], "changed": ["a"]}
    same = runner.invoke(build_app(), ["diff", "--left", str(left), "--right", str(left)])
    assert same.exit_code == 0
    assert json.loads(same.stdout)["status"] == "same"


def test_invalid_input_fails_closed(tmp_path) -> None:
    left = tmp_path / "left.json"
    right = tmp_path / "right.json"
    left.write_text('{"a":1,"a":2}', encoding="utf-8")
    right.write_text('{"a":1}', encoding="utf-8")
    result = runner.invoke(build_app(), ["diff", "--left", str(left), "--right", str(right)])
    assert result.exit_code == 2
    assert json.loads(result.stdout)["error"]["code"] == "LEFT_JSON_DUPLICATE_KEY"


def test_invalid_child_report_cannot_be_presented_as_success(tmp_path) -> None:
    with patch("kfm_cli.cli.subprocess.run", return_value=subprocess.CompletedProcess(
        [], 0, '{"tool":"stable-diff","status":"same","secret":"raw"}', "raw"
    )):
        result = runner.invoke(build_app(), ["diff", "--left", str(tmp_path / "left"),
                                            "--right", str(tmp_path / "right")])
    assert result.exit_code == 2
    assert json.loads(result.stdout)["error"]["code"] == "COMPARATOR_ERROR"
    assert "raw" not in result.stdout

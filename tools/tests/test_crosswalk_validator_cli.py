from __future__ import annotations

from pathlib import Path

import pytest

from tools.validators.crosswalk import validate_crosswalk_sql as validator


def test_run_validator_parses_pipe_output(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    sql_file = tmp_path / "validator.sql"
    sql_file.write_text("select 1;", encoding="utf-8")

    class _Proc:
        stdout = "negative_overlap|0\nweight_out_of_bounds|2\n"

    def fake_run(*args, **kwargs):  # noqa: ANN001, ANN002
        return _Proc()

    monkeypatch.setattr(validator.subprocess, "run", fake_run)
    rows = validator.run_validator("postgresql://local", sql_file)
    assert rows == [("negative_overlap", 0), ("weight_out_of_bounds", 2)]


def test_main_fail_on_errors(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(validator, "parse_args", lambda: type("A", (), {
        "dsn": "postgresql://local",
        "sql": validator.DEFAULT_SQL,
        "fail_on_errors": True,
    })())
    monkeypatch.setattr(validator, "run_validator", lambda dsn, sql: [("x", 1)])
    assert validator.main() == 1

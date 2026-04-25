#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

import sys

sys.path.insert(0, str(Path("tools/ci").resolve()))
from render_json_io import read_json_object  # noqa: E402


def _templates(prefix: str) -> dict[str, str]:
    return {
        "not_found": f"{prefix}: missing {{path}}",
        "non_utf8": f"{prefix}: non-utf8 {{path}}",
        "invalid_json": f"{prefix}: invalid json {{path}} {{exc}}",
        "unreadable": f"{prefix}: unreadable {{path}} {{exc}}",
        "wrong_type": f"{prefix}: wrong type {{path}}",
    }


def test_read_json_object_success() -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "ok.json"
        path.write_text('{"x": 1}', encoding="utf-8")

        payload = read_json_object(str(path), **_templates("ok"))
        assert payload == {"x": 1}


def test_read_json_object_missing_file(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc:
        read_json_object("does-not-exist.json", **_templates("missing"))

    assert exc.value.code == 2
    assert "missing: missing does-not-exist.json" in capsys.readouterr().err


def test_read_json_object_non_utf8(capsys: pytest.CaptureFixture[str]) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "bad.json"
        path.write_bytes(b"\xff\xfe")

        with pytest.raises(SystemExit) as exc:
            read_json_object(str(path), **_templates("utf8"))

    assert exc.value.code == 2
    assert f"utf8: non-utf8 {path}" in capsys.readouterr().err


def test_read_json_object_invalid_json(capsys: pytest.CaptureFixture[str]) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "bad.json"
        path.write_text("{broken", encoding="utf-8")

        with pytest.raises(SystemExit) as exc:
            read_json_object(str(path), **_templates("json"))

    assert exc.value.code == 2
    assert f"json: invalid json {path}" in capsys.readouterr().err


def test_read_json_object_unreadable_path(capsys: pytest.CaptureFixture[str]) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td)

        with pytest.raises(SystemExit) as exc:
            read_json_object(str(path), **_templates("read"))

    assert exc.value.code == 2
    assert f"read: unreadable {path}" in capsys.readouterr().err


def test_read_json_object_wrong_type(capsys: pytest.CaptureFixture[str]) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "bad.json"
        path.write_text("[]", encoding="utf-8")

        with pytest.raises(SystemExit) as exc:
            read_json_object(str(path), **_templates("type"))

    assert exc.value.code == 2
    assert f"type: wrong type {path}" in capsys.readouterr().err

#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path
from typing import Any, Callable

import pytest


def _load_read_json_object() -> Callable[..., dict[str, Any]]:
    module_path = Path("tools/ci/render_json_io.py").resolve()
    spec = importlib.util.spec_from_file_location("render_json_io", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load module spec: {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.read_json_object


def _templates(prefix: str) -> dict[str, str]:
    return {
        "not_found": f"{prefix}: missing {{path}}",
        "non_utf8": f"{prefix}: non-utf8 {{path}}",
        "invalid_json": f"{prefix}: invalid json {{path}} {{exc}}",
        "unreadable": f"{prefix}: unreadable {{path}} {{exc}}",
        "wrong_type": f"{prefix}: wrong type {{path}}",
    }


@pytest.fixture(scope="module")
def read_json_object() -> Callable[..., dict[str, Any]]:
    return _load_read_json_object()


def test_read_json_object_success(read_json_object: Callable[..., dict[str, Any]]) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "ok.json"
        path.write_text('{"x": 1}', encoding="utf-8")

        payload = read_json_object(str(path), **_templates("ok"))
        assert payload == {"x": 1}


def test_read_json_object_missing_file(
    read_json_object: Callable[..., dict[str, Any]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as exc:
        read_json_object("does-not-exist.json", **_templates("missing"))

    assert exc.value.code == 2
    assert "missing: missing does-not-exist.json" in capsys.readouterr().err


def test_read_json_object_non_utf8(
    read_json_object: Callable[..., dict[str, Any]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "bad.json"
        path.write_bytes(b"\xff\xfe")

        with pytest.raises(SystemExit) as exc:
            read_json_object(str(path), **_templates("utf8"))

    assert exc.value.code == 2
    assert f"utf8: non-utf8 {path}" in capsys.readouterr().err


def test_read_json_object_invalid_json(
    read_json_object: Callable[..., dict[str, Any]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "bad.json"
        path.write_text("{broken", encoding="utf-8")

        with pytest.raises(SystemExit) as exc:
            read_json_object(str(path), **_templates("json"))

    assert exc.value.code == 2
    assert f"json: invalid json {path}" in capsys.readouterr().err


def test_read_json_object_unreadable_path(
    read_json_object: Callable[..., dict[str, Any]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td)

        with pytest.raises(SystemExit) as exc:
            read_json_object(str(path), **_templates("read"))

    assert exc.value.code == 2
    assert f"read: unreadable {path}" in capsys.readouterr().err


def test_read_json_object_wrong_type(
    read_json_object: Callable[..., dict[str, Any]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "bad.json"
        path.write_text("[]", encoding="utf-8")

        with pytest.raises(SystemExit) as exc:
            read_json_object(str(path), **_templates("type"))

    assert exc.value.code == 2
    assert f"type: wrong type {path}" in capsys.readouterr().err


def test_read_json_object_tolerates_bad_template(
    read_json_object: Callable[..., dict[str, Any]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    templates = _templates("bad-template")
    templates["not_found"] = "bad-template: missing {unknown_placeholder}"

    with pytest.raises(SystemExit) as exc:
        read_json_object("does-not-exist.json", **templates)

    assert exc.value.code == 2
    assert "bad-template: missing {unknown_placeholder}" in capsys.readouterr().err


def test_read_json_object_tolerates_non_string_template(
    read_json_object: Callable[..., dict[str, Any]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    templates = _templates("bad-template")
    templates["not_found"] = None  # type: ignore[assignment]

    with pytest.raises(SystemExit) as exc:
        read_json_object("does-not-exist.json", **templates)

    assert exc.value.code == 2
    assert "None" in capsys.readouterr().err

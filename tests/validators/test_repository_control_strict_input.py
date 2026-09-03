from __future__ import annotations

import io
import json
from pathlib import Path

import pytest

from tools.validators.repository_control import fetch_bounded_issue_comments as helper

ROOT = Path(__file__).resolve().parents[2]
BINDING_PATH = ROOT / "docs/governance/REPOSITORY_TRANSITION_CONTROL_SOURCE.md"


class Response:
    def __init__(self, raw: bytes) -> None:
        self._stream = io.BytesIO(raw)
        self.status = 200

    def read(self, size: int = -1) -> bytes:
        return self._stream.read(size)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        return None


def capture_raw(
    tmp_path: Path,
    raw: bytes,
    **limits: int,
):
    def opener(request, *, timeout: int):
        assert timeout == helper.REQUEST_TIMEOUT_SECONDS
        return Response(raw)

    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"
    result = helper.capture_to_files(
        repository="bartytime4life/Kansas-Frontier-Matrix",
        control_issue=4024,
        token="test-token",
        comments_output=comments_path,
        status_output=status_path,
        opener=opener,
        **limits,
    )
    return result, comments_path, status_path


@pytest.mark.parametrize("token", [b"NaN", b"Infinity", b"-Infinity", b"1e1000000"])
def test_non_finite_numeric_input_is_unavailable_without_echo(
    tmp_path: Path, token: bytes
) -> None:
    raw = b'[{"id":' + token + b',"body":"DO_NOT_ECHO"}]'
    result, comments_path, status_path = capture_raw(tmp_path, raw)

    assert (result.status, result.reason_code) == (
        "UNAVAILABLE",
        "CONTROL_SOURCE_PAGE_JSON_INVALID",
    )
    assert comments_path.read_text(encoding="utf-8") == "[]\n"
    assert json.loads(status_path.read_text(encoding="utf-8"))["status"] == "UNAVAILABLE"
    rendered = json.dumps(result.as_dict(), sort_keys=True)
    assert token.decode("ascii") not in rendered
    assert "DO_NOT_ECHO" not in rendered


def test_overlong_integer_is_unavailable(tmp_path: Path) -> None:
    token = b"9" * (helper.MAX_INTEGER_DIGITS + 1)
    raw = b'[{"id":' + token + b"}]"
    result, comments_path, _ = capture_raw(tmp_path, raw)

    assert result.reason_code == "CONTROL_SOURCE_PAGE_JSON_INVALID"
    assert comments_path.read_text(encoding="utf-8") == "[]\n"


def test_excessive_json_depth_is_unavailable(tmp_path: Path) -> None:
    nesting = helper.MAX_JSON_DEPTH + 2
    raw = (
        b'[{"id":1,"extra":'
        + (b"[" * nesting)
        + b"0"
        + (b"]" * nesting)
        + b"}]"
    )
    result, comments_path, _ = capture_raw(tmp_path, raw)

    assert result.reason_code == "CONTROL_SOURCE_PAGE_DEPTH_EXCEEDED"
    assert comments_path.read_text(encoding="utf-8") == "[]\n"


@pytest.mark.parametrize("exception", [ValueError("invalid"), RecursionError("deep")])
def test_parser_limit_exceptions_are_normalized(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, exception: Exception
) -> None:
    def fail_loads(*args, **kwargs):
        raise exception

    monkeypatch.setattr(helper.json, "loads", fail_loads)
    result, comments_path, status_path = capture_raw(tmp_path, b"[]")

    assert result.reason_code == "CONTROL_SOURCE_PAGE_JSON_INVALID"
    assert comments_path.read_text(encoding="utf-8") == "[]\n"
    assert '"status":"UNAVAILABLE"' in status_path.read_text(encoding="utf-8")


def test_page_node_limit_is_unavailable(tmp_path: Path) -> None:
    raw = b'[{"id":1,"extra":[0,1,2,3,4,5,6,7,8]}]'
    result, comments_path, _ = capture_raw(
        tmp_path,
        raw,
        max_page_nodes=8,
        max_total_nodes=128,
    )

    assert result.reason_code == "CONTROL_SOURCE_PAGE_NODES_EXCEEDED"
    assert comments_path.read_text(encoding="utf-8") == "[]\n"


def test_strict_serializer_rejects_non_finite_values() -> None:
    with pytest.raises(helper.CaptureError) as caught:
        helper._strict_json_text({"value": float("nan")})

    assert caught.value.reason_code == "CONTROL_SOURCE_SERIALIZATION_INVALID"


def test_binding_note_describes_active_bounded_control() -> None:
    binding = BINDING_PATH.read_text(encoding="utf-8")
    lowered = binding.lower()

    assert "workflow-active" in lowered
    assert "pr #4237" in lowered
    assert "fetch_bounded_issue_comments.py" in binding
    assert "three trusted-base helpers" in lowered
    assert "16 mib" in lowered
    assert "1,000,000 json nodes" in lowered
    assert "allow_nan=false" in lowered
    assert "required-status-check not installed" in lowered
    assert "proposed and not applied" in lowered
    assert "does not authorize a ruleset" in lowered
    assert "proposed; branch-only; exact-main-reconciled; not workflow-active" not in lowered

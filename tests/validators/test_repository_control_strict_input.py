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


def assert_unavailable_output(
    *,
    result,
    comments_path: Path,
    status_path: Path,
    reason_code: str,
    forbidden_tokens: tuple[str, ...] = (),
) -> None:
    comments_text = comments_path.read_text(encoding="utf-8")
    status_text = status_path.read_text(encoding="utf-8")
    result_text = json.dumps(result.as_dict(), sort_keys=True, allow_nan=False)

    assert (result.status, result.reason_code) == ("UNAVAILABLE", reason_code)
    assert comments_text == "[]\n"
    assert json.loads(status_text) == {
        "control_issue": 4024,
        "repository": "bartytime4life/Kansas-Frontier-Matrix",
        "schema_version": "1.0.0",
        "status": "UNAVAILABLE",
    }
    assert len(comments_text.encode("utf-8")) == 3
    assert len(status_text.encode("utf-8")) < 256
    for token in forbidden_tokens:
        assert token not in comments_text
        assert token not in status_text
        assert token not in result_text


@pytest.mark.parametrize("token", [b"NaN", b"Infinity", b"-Infinity", b"1e1000000"])
def test_non_finite_numeric_input_is_unavailable_without_echo(
    tmp_path: Path, token: bytes
) -> None:
    marker = "DO_NOT_ECHO_NON_FINITE"
    raw = (
        b'[{"id":'
        + token
        + b',"body":"'
        + marker.encode("utf-8")
        + b'"}]'
    )
    result, comments_path, status_path = capture_raw(tmp_path, raw)

    assert_unavailable_output(
        result=result,
        comments_path=comments_path,
        status_path=status_path,
        reason_code="CONTROL_SOURCE_PAGE_JSON_INVALID",
        forbidden_tokens=(token.decode("ascii"), marker),
    )


def test_overlong_integer_is_unavailable_without_malformed_json_shortcut(
    tmp_path: Path,
) -> None:
    token = "9" * (helper.MAX_INTEGER_DIGITS + 1)
    marker = "DO_NOT_ECHO_INTEGER"
    raw = (
        b'[{"id":'
        + token.encode("ascii")
        + b',"body":"'
        + marker.encode("utf-8")
        + b'"}]'
    )
    result, comments_path, status_path = capture_raw(tmp_path, raw)

    assert_unavailable_output(
        result=result,
        comments_path=comments_path,
        status_path=status_path,
        reason_code="CONTROL_SOURCE_PAGE_JSON_INVALID",
        forbidden_tokens=(token, marker),
    )


def test_excessive_json_depth_is_unavailable_without_echo(tmp_path: Path) -> None:
    nesting = helper.MAX_JSON_DEPTH + 2
    marker = "DO_NOT_ECHO_DEPTH"
    raw = (
        b'[{"id":1,"body":"'
        + marker.encode("utf-8")
        + b'","extra":'
        + (b"[" * nesting)
        + b"0"
        + (b"]" * nesting)
        + b"}]"
    )
    result, comments_path, status_path = capture_raw(tmp_path, raw)

    assert_unavailable_output(
        result=result,
        comments_path=comments_path,
        status_path=status_path,
        reason_code="CONTROL_SOURCE_PAGE_DEPTH_EXCEEDED",
        forbidden_tokens=(marker,),
    )


@pytest.mark.parametrize("exception", [ValueError("invalid"), RecursionError("deep")])
def test_parser_limit_exceptions_are_normalized(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, exception: Exception
) -> None:
    def fail_loads(*args, **kwargs):
        raise exception

    with monkeypatch.context() as parser_patch:
        parser_patch.setattr(helper.json, "loads", fail_loads)
        result, comments_path, status_path = capture_raw(tmp_path, b"[]")

    assert_unavailable_output(
        result=result,
        comments_path=comments_path,
        status_path=status_path,
        reason_code="CONTROL_SOURCE_PAGE_JSON_INVALID",
        forbidden_tokens=(str(exception),),
    )


def test_page_node_limit_is_unavailable(tmp_path: Path) -> None:
    marker = "DO_NOT_ECHO_NODE_LIMIT"
    raw = (
        b'[{"id":1,"body":"'
        + marker.encode("utf-8")
        + b'","extra":[0,1,2,3,4,5,6,7,8]}]'
    )
    result, comments_path, status_path = capture_raw(
        tmp_path,
        raw,
        max_page_nodes=8,
        max_total_nodes=128,
    )

    assert_unavailable_output(
        result=result,
        comments_path=comments_path,
        status_path=status_path,
        reason_code="CONTROL_SOURCE_PAGE_NODES_EXCEEDED",
        forbidden_tokens=(marker,),
    )


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_strict_serializer_rejects_non_finite_values(value: float) -> None:
    with pytest.raises(helper.CaptureError) as caught:
        helper._strict_json_text({"value": value})

    assert caught.value.reason_code == "CONTROL_SOURCE_SERIALIZATION_INVALID"


def test_binding_note_distinguishes_current_main_from_candidate_hardening() -> None:
    binding = BINDING_PATH.read_text(encoding="utf-8")
    lowered = binding.lower()

    assert "current-main workflow-active advisory" in lowered
    assert "candidate bounded-input hardening" in lowered
    assert "pr #4237" in lowered
    assert "current protected-main workflow still uses two trusted-base validators" in lowered
    assert "candidate adds a third trusted-base capture helper" in lowered
    assert "fetch_bounded_issue_comments.py" in binding
    assert "if the candidate bytes are integrated" in lowered
    assert "16 mib" in lowered
    assert "1,000,000 json nodes" in lowered
    assert "allow_nan=false" in lowered
    assert "required-status-check not installed" in lowered
    assert "proposed and not applied" in lowered
    assert "does not authorize a ruleset" in lowered
    assert "proposed; branch-only; exact-main-reconciled; not workflow-active" not in lowered

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


def test_binding_note_distinguishes_main_bounds_from_branch_only_length_fix() -> None:
    binding = BINDING_PATH.read_text(encoding="utf-8")
    lowered = binding.lower()
    normalized = " ".join(lowered.split())

    assert "current-main workflow-active advisory" in normalized
    assert "three-helper bounded capture integrated" in normalized
    assert "declared content-length completeness correction validated branch-only" in normalized
    assert "pr #4237" in normalized
    assert "pr #4239" in normalized
    assert "pr #4238" in normalized
    assert "current protected-main workflow uses three trusted-base helpers" in normalized
    assert "fetch_bounded_issue_comments.py" in binding
    assert "100 pages" in normalized
    assert "16 mib" in normalized
    assert "1,000,000 json nodes" in normalized
    assert "allow_nan=false" in normalized
    assert "it does not inspect or compare a declared `content-length`" in normalized
    assert "silently short response as complete" in normalized
    assert "fix/repository-control-content-length-completeness-20260903" in binding
    assert "5fe7ca322c838f5de3d677977a12302ba3c9e6f6" in binding
    assert "841ce3565e297e2a4778dd56cd4a4ef3e9e6b78f" in binding
    assert (
        "the two issue comments transcribed the final tree as "
        "`841ce7988aabc4b864a275e61c7253003848f082`"
    ) in normalized
    assert "that value is not the tree of exact head" in normalized
    assert "must not be used as its identity" in normalized
    assert "9047c59d2ba91618078713ebffc2989ac282ab9b" in binding
    assert "174733cb47d00ed688c168d3deee5015ba316e3e" in binding
    assert "5533902911" in binding
    assert "5534073715" in binding
    assert "not integrated into protected main" in normalized
    assert "no pull request exists for it" in normalized
    assert "a missing `content-length` remains permissible" in normalized
    assert "not independent human or capability-separated review" in normalized
    assert "5532535765" in binding
    assert "5532579086" in binding
    assert "5532649271" in binding
    assert "5533558088" in binding
    assert "connected github capability exposes ruleset reads" in normalized
    assert "no administration-write operation" in normalized
    assert "no ruleset mutation was attempted" in normalized
    assert "owner authorization expired at `2026-09-03t23:30:00z`" in normalized
    assert "no settings operation may reuse the expired authorization" in normalized
    assert "a new owner decision" in normalized
    assert "publishing that package did not renew authority or apply the setting" in normalized
    assert "does not itself authorize a ruleset mutation" in normalized

    stale_phrases = (
        "candidate bounded-input hardening",
        "current protected-main workflow still uses two trusted-base validators",
        "candidate adds a third trusted-base capture helper",
        "if the candidate bytes are integrated",
        "the bounded-input changes described below remain a branch-local hardening proposal",
        "bounded capture and truncated-response hardening integrated",
        "truncated-response handling are present on current main",
        "the bounded-capture and truncated-response code is now on main",
        "incomplete-response failure modes",
    )
    for phrase in stale_phrases:
        assert phrase not in normalized

from __future__ import annotations

import io
import json
from email.message import Message
from pathlib import Path

from tools.validators.repository_control import fetch_bounded_issue_comments as helper


class Response:
    def __init__(self, raw: bytes, content_lengths: list[str] | None = None) -> None:
        self._stream = io.BytesIO(raw)
        self.status = 200
        self.bytes_read = 0
        self.headers = Message()
        for value in content_lengths or []:
            self.headers["Content-Length"] = value

    def read(self, size: int = -1) -> bytes:
        chunk = self._stream.read(size)
        self.bytes_read += len(chunk)
        return chunk

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        return None


def capture(
    tmp_path: Path,
    raw: bytes,
    content_lengths: list[str] | None,
    **limits: int,
):
    response = Response(raw, content_lengths)

    def opener(_request, *, timeout: int):
        assert timeout == helper.REQUEST_TIMEOUT_SECONDS
        return response

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
    return result, response, comments_path, status_path


def assert_unavailable(
    *,
    result,
    comments_path: Path,
    status_path: Path,
    reason_code: str,
) -> None:
    assert (result.status, result.reason_code) == ("UNAVAILABLE", reason_code)
    assert comments_path.read_text(encoding="utf-8") == "[]\n"
    assert json.loads(status_path.read_text(encoding="utf-8")) == {
        "control_issue": 4024,
        "repository": "bartytime4life/Kansas-Frontier-Matrix",
        "schema_version": "1.0.0",
        "status": "UNAVAILABLE",
    }


def test_exact_declared_content_length_is_accepted(tmp_path: Path) -> None:
    raw = b'[{"id":1}]'
    result, response, comments_path, status_path = capture(
        tmp_path,
        raw,
        [str(len(raw))],
    )

    assert result.status == "AVAILABLE"
    assert result.reason_code == "CONTROL_SOURCE_CAPTURE_BOUNDED"
    assert result.comments == 1
    assert response.bytes_read == len(raw)
    assert json.loads(comments_path.read_text(encoding="utf-8")) == [[{"id": 1}]]
    assert json.loads(status_path.read_text(encoding="utf-8"))["status"] == "AVAILABLE"


def test_silent_short_body_is_rejected_even_when_prefix_is_valid_json(
    tmp_path: Path,
) -> None:
    raw = b"[]"
    result, response, comments_path, status_path = capture(
        tmp_path,
        raw,
        [str(len(raw) + 32)],
    )

    assert response.bytes_read == len(raw)
    assert_unavailable(
        result=result,
        comments_path=comments_path,
        status_path=status_path,
        reason_code="CONTROL_SOURCE_CONTENT_LENGTH_MISMATCH",
    )


def test_conflicting_duplicate_content_lengths_are_rejected(tmp_path: Path) -> None:
    raw = b"[]"
    result, _response, comments_path, status_path = capture(
        tmp_path,
        raw,
        [str(len(raw)), str(len(raw) + 1)],
    )

    assert_unavailable(
        result=result,
        comments_path=comments_path,
        status_path=status_path,
        reason_code="CONTROL_SOURCE_CONTENT_LENGTH_INVALID",
    )


def test_declared_content_length_over_page_budget_fails_before_body_read(
    tmp_path: Path,
) -> None:
    result, response, comments_path, status_path = capture(
        tmp_path,
        b"[]",
        ["65"],
        max_page_bytes=64,
        max_total_bytes=1024,
    )

    assert response.bytes_read == 0
    assert_unavailable(
        result=result,
        comments_path=comments_path,
        status_path=status_path,
        reason_code="CONTROL_SOURCE_PAGE_BYTES_EXCEEDED",
    )


def test_missing_content_length_preserves_existing_bounded_behavior(
    tmp_path: Path,
) -> None:
    raw = b"[]"
    result, response, comments_path, status_path = capture(
        tmp_path,
        raw,
        None,
    )

    assert result.status == "AVAILABLE"
    assert result.reason_code == "CONTROL_SOURCE_CAPTURE_BOUNDED"
    assert result.comments == 0
    assert response.bytes_read == len(raw)
    assert json.loads(comments_path.read_text(encoding="utf-8")) == []
    assert json.loads(status_path.read_text(encoding="utf-8"))["status"] == "AVAILABLE"

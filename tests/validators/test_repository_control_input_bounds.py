from __future__ import annotations

import io
import json
import subprocess
import sys
from http.client import IncompleteRead
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from tools.validators.repository_control import fetch_bounded_issue_comments as helper

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = ROOT / ".github/workflows/repository-control.yml"


class Response:
    def __init__(self, value: object, *, raw: bytes | None = None) -> None:
        encoded = raw
        if encoded is None:
            encoded = json.dumps(value, separators=(",", ":")).encode("utf-8")
        self._stream = io.BytesIO(encoded)
        self.status = 200
        self.bytes_read = 0

    def read(self, size: int = -1) -> bytes:
        chunk = self._stream.read(size)
        self.bytes_read += len(chunk)
        return chunk

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        return None


def opener_for(pages: dict[int, object]):
    def open_request(request, *, timeout: int):
        assert timeout == helper.REQUEST_TIMEOUT_SECONDS
        page = int(parse_qs(urlparse(request.full_url).query)["page"][0])
        return Response(pages.get(page, []))

    return open_request


def test_bounded_capture_reads_complete_pages_and_writes_exact_status(
    tmp_path: Path,
) -> None:
    pages = {
        1: [{"id": 1}, {"id": 2}],
        2: [{"id": 3}],
    }
    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"

    result = helper.capture_to_files(
        repository="bartytime4life/Kansas-Frontier-Matrix",
        control_issue=4024,
        token="test-token",
        comments_output=comments_path,
        status_output=status_path,
        opener=opener_for(pages),
        per_page=2,
        max_pages=3,
        max_page_bytes=1024,
        max_total_bytes=4096,
    )

    assert result.status == "AVAILABLE"
    assert result.reason_code == "CONTROL_SOURCE_CAPTURE_BOUNDED"
    assert result.pages == 2
    assert result.comments == 3
    assert json.loads(comments_path.read_text(encoding="utf-8")) == [
        pages[1],
        pages[2],
    ]
    assert json.loads(status_path.read_text(encoding="utf-8")) == {
        "schema_version": "1.0.0",
        "repository": "bartytime4life/Kansas-Frontier-Matrix",
        "control_issue": 4024,
        "status": "AVAILABLE",
    }


def test_sentinel_page_rejects_more_than_the_admitted_page_count(
    tmp_path: Path,
) -> None:
    pages = {
        1: [{"id": 1}],
        2: [{"id": 2}],
        3: [{"id": 3}],
    }
    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"

    result = helper.capture_to_files(
        repository="bartytime4life/Kansas-Frontier-Matrix",
        control_issue=4024,
        token="test-token",
        comments_output=comments_path,
        status_output=status_path,
        opener=opener_for(pages),
        per_page=1,
        max_pages=2,
        max_page_bytes=1024,
        max_total_bytes=4096,
    )

    assert result.status == "UNAVAILABLE"
    assert result.reason_code == "CONTROL_SOURCE_PAGE_LIMIT_EXCEEDED"
    assert json.loads(comments_path.read_text(encoding="utf-8")) == []
    assert json.loads(status_path.read_text(encoding="utf-8"))["status"] == "UNAVAILABLE"


def test_oversized_page_is_stopped_before_json_loading_and_fails_closed(
    tmp_path: Path,
) -> None:
    oversized = b"[" + (b" " * 128) + b"]"

    def open_request(request, *, timeout: int):
        return Response([], raw=oversized)

    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"
    result = helper.capture_to_files(
        repository="bartytime4life/Kansas-Frontier-Matrix",
        control_issue=4024,
        token="test-token",
        comments_output=comments_path,
        status_output=status_path,
        opener=open_request,
        max_page_bytes=64,
        max_total_bytes=1024,
    )

    assert result.status == "UNAVAILABLE"
    assert result.reason_code == "CONTROL_SOURCE_PAGE_BYTES_EXCEEDED"
    assert comments_path.read_text(encoding="utf-8") == "[]\n"


def test_incomplete_http_read_is_normalized_to_unavailable(
    tmp_path: Path,
) -> None:
    class TruncatedResponse:
        status = 200

        def read(self, size: int = -1) -> bytes:
            raise IncompleteRead(b"DO_NOT_ECHO", 32)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, traceback) -> None:
            return None

    def open_request(_request, *, timeout: int):
        assert timeout == helper.REQUEST_TIMEOUT_SECONDS
        return TruncatedResponse()

    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"
    result = helper.capture_to_files(
        repository="bartytime4life/Kansas-Frontier-Matrix",
        control_issue=4024,
        token="test-token",
        comments_output=comments_path,
        status_output=status_path,
        opener=open_request,
    )

    assert result.status == "UNAVAILABLE"
    assert result.reason_code == "CONTROL_SOURCE_FETCH_FAILED"
    assert comments_path.read_text(encoding="utf-8") == "[]\n"
    assert json.loads(status_path.read_text(encoding="utf-8")) == {
        "schema_version": "1.0.0",
        "repository": "bartytime4life/Kansas-Frontier-Matrix",
        "control_issue": 4024,
        "status": "UNAVAILABLE",
    }
    serialized = json.dumps(result.as_dict(), sort_keys=True)
    assert "DO_NOT_ECHO" not in serialized
    assert "IncompleteRead" not in serialized


def test_aggregate_byte_limit_is_enforced_before_later_page_materialization(
    tmp_path: Path,
) -> None:
    pages = {
        1: [{"body": "a" * 40}],
        2: [{"body": "b" * 40}],
    }
    encoded_pages = {
        page: json.dumps(value, separators=(",", ":")).encode("utf-8")
        for page, value in pages.items()
    }
    responses: dict[int, Response] = {}

    def open_request(request, *, timeout: int):
        assert timeout == helper.REQUEST_TIMEOUT_SECONDS
        page = int(parse_qs(urlparse(request.full_url).query)["page"][0])
        response = Response([], raw=encoded_pages.get(page, b"[]"))
        responses[page] = response
        return response

    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"
    maximum = len(encoded_pages[1]) + 5

    result = helper.capture_to_files(
        repository="bartytime4life/Kansas-Frontier-Matrix",
        control_issue=4024,
        token="test-token",
        comments_output=comments_path,
        status_output=status_path,
        opener=open_request,
        per_page=1,
        max_pages=3,
        max_page_bytes=1024,
        max_total_bytes=maximum,
    )

    assert result.status == "UNAVAILABLE"
    assert result.reason_code == "CONTROL_SOURCE_TOTAL_BYTES_EXCEEDED"
    assert json.loads(comments_path.read_text(encoding="utf-8")) == []
    assert responses[1].bytes_read == len(encoded_pages[1])
    assert responses[2].bytes_read == 6
    assert sum(response.bytes_read for response in responses.values()) == maximum + 1


def test_duplicate_page_keys_are_rejected_without_echoing_values(
    tmp_path: Path,
) -> None:
    raw = b'[{"id":1,"id":"DO_NOT_ECHO"}]'

    def open_request(request, *, timeout: int):
        return Response([], raw=raw)

    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"
    result = helper.capture_to_files(
        repository="bartytime4life/Kansas-Frontier-Matrix",
        control_issue=4024,
        token="test-token",
        comments_output=comments_path,
        status_output=status_path,
        opener=open_request,
    )

    assert result.status == "UNAVAILABLE"
    assert result.reason_code == "CONTROL_SOURCE_PAGE_JSON_INVALID"
    assert "DO_NOT_ECHO" not in json.dumps(result.as_dict(), sort_keys=True)
    assert comments_path.read_text(encoding="utf-8") == "[]\n"


def test_cli_missing_token_writes_unavailable_for_downstream_classification(
    tmp_path: Path,
) -> None:
    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"
    completed = subprocess.run(
        [
            sys.executable,
            str(
                ROOT
                / "tools/validators/repository_control/fetch_bounded_issue_comments.py"
            ),
            "--repository",
            "bartytime4life/Kansas-Frontier-Matrix",
            "--control-issue",
            "4024",
            "--comments-output",
            str(comments_path),
            "--status-output",
            str(status_path),
        ],
        cwd=ROOT,
        env={},
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 0
    output = json.loads(completed.stdout)
    assert output["status"] == "UNAVAILABLE"
    assert output["reason_code"] == "CONTROL_SOURCE_TOKEN_UNAVAILABLE"
    assert comments_path.read_text(encoding="utf-8") == "[]\n"
    assert json.loads(status_path.read_text(encoding="utf-8"))["status"] == "UNAVAILABLE"


def test_cli_rejects_abbreviated_options(tmp_path: Path) -> None:
    comments_path = tmp_path / "comments.json"
    status_path = tmp_path / "status.json"
    completed = subprocess.run(
        [
            sys.executable,
            str(
                ROOT
                / "tools/validators/repository_control/fetch_bounded_issue_comments.py"
            ),
            "--repository",
            "bartytime4life/Kansas-Frontier-Matrix",
            "--control-issue",
            "4024",
            "--comments-output",
            str(comments_path),
            "--status-output",
            str(status_path),
            "--api",
            "https://api.github.com",
        ],
        cwd=ROOT,
        env={"GH_TOKEN": "test-token"},
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 2
    assert "unrecognized arguments: --api" in completed.stderr
    assert not comments_path.exists()
    assert not status_path.exists()


def test_workflow_uses_trusted_base_bounded_capture_without_slurp() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "fetch_bounded_issue_comments.py?ref=${KFM_BASE_SHA}" in workflow
    assert 'python3 "${RUNNER_TEMP}/fetch-bounded-issue-comments.py"' in workflow
    assert '--repository "${GITHUB_REPOSITORY}"' in workflow
    assert '--control-issue "${KFM_CONTROL_ISSUE}"' in workflow
    assert '--comments-output "${comments_path}"' in workflow
    assert '--status-output "${status_path}"' in workflow
    assert "--paginate" not in workflow
    assert "--slurp" not in workflow
    assert "/issues/${KFM_CONTROL_ISSUE}/comments?per_page=100" not in workflow

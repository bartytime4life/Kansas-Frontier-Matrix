from __future__ import annotations

import base64
import io
import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.validators.repository_control.validate_control_source_availability import (
    InputError,
    LimitError,
    MAX_CONTROL_SOURCE_BYTES,
    MAX_CONTROL_SOURCE_COMMENTS,
    MAX_ENCODED_COMMENT_RECORD_BYTES,
    evaluate,
    normalize_comment_stream,
)

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = (
    ROOT
    / "tools/validators/repository_control/validate_control_source_availability.py"
)
WORKFLOW = ROOT / ".github/workflows/repository-control.yml"
REPOSITORY = "bartytime4life/Kansas-Frontier-Matrix"
CONTROL_ISSUE = 4024


def encoded(*records: object) -> bytes:
    return b"".join(
        base64.b64encode(
            json.dumps(
                record,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            ).encode("utf-8")
        )
        + b"\n"
        for record in records
    )


def status(value: str) -> dict[str, object]:
    return {
        "schema_version": "1.0.0",
        "repository": REPOSITORY,
        "control_issue": CONTROL_ISSUE,
        "status": value,
    }


def test_stream_normalizes_objects_deterministically(tmp_path: Path) -> None:
    output = tmp_path / "comments.json"
    records = ({"body": "é", "id": 2}, {"id": 1, "user": {"login": "owner"}})

    count, byte_count = normalize_comment_stream(
        io.BytesIO(encoded(*records)),
        output,
        max_comments=2,
        max_bytes=1024,
        max_encoded_record_bytes=512,
    )

    expected = json.dumps(
        list(records),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ) + "\n"
    assert (count, byte_count) == (2, len(expected.encode("utf-8")))
    assert output.read_text(encoding="utf-8") == expected


@pytest.mark.parametrize(
    ("stream", "limits"),
    [
        (encoded({"id": 1}, {"id": 2}), {"max_comments": 1}),
        (encoded({"body": "x" * 40}), {"max_bytes": 16}),
        (encoded({"id": 1}), {"max_encoded_record_bytes": 8}),
    ],
)
def test_stream_limits_fail_before_output(
    tmp_path: Path,
    stream: bytes,
    limits: dict[str, int],
) -> None:
    output = tmp_path / "comments.json"
    kwargs = {
        "max_comments": 10,
        "max_bytes": 1024,
        "max_encoded_record_bytes": 512,
        **limits,
    }
    with pytest.raises(LimitError):
        normalize_comment_stream(io.BytesIO(stream), output, **kwargs)
    assert not output.exists()


@pytest.mark.parametrize(
    "stream",
    [
        b"not-base64!\n",
        base64.b64encode(b'{"id":1,"id":2}') + b"\n",
        encoded([{"id": 1}]),
    ],
)
def test_stream_rejects_invalid_records_without_output(
    tmp_path: Path,
    stream: bytes,
) -> None:
    output = tmp_path / "comments.json"
    with pytest.raises(InputError):
        normalize_comment_stream(io.BytesIO(stream), output, max_bytes=1024)
    assert not output.exists()


def test_status_states_have_finite_fail_closed_reasons() -> None:
    cases = {
        "AVAILABLE": ("PASS", "CONTROL_SOURCE_AVAILABLE", 0),
        "UNAVAILABLE": ("REGRESSION", "CONTROL_SOURCE_UNAVAILABLE", 1),
        "INVALID": ("REGRESSION", "CONTROL_SOURCE_RESPONSE_INVALID", 1),
        "OVER_LIMIT": ("REGRESSION", "CONTROL_SOURCE_LIMIT_EXCEEDED", 1),
    }
    for value, expected in cases.items():
        result = evaluate(
            status(value),
            expected_repository=REPOSITORY,
            expected_control_issue=CONTROL_ISSUE,
        )
        assert (result.outcome_class, result.reason_code, result.exit_code) == expected


def test_normalizer_cli_success_invalid_and_limit_outcomes(tmp_path: Path) -> None:
    cases = [
        (encoded({"id": 1}), 0, "CONTROL_SOURCE_STREAM_NORMALIZED", ["--max-comments", "2"]),
        (b"SENSITIVE-INVALID-BASE64!\n", 1, "CONTROL_SOURCE_RESPONSE_INVALID", []),
        (encoded({"id": 1}, {"id": 2}), 2, "CONTROL_SOURCE_LIMIT_EXCEEDED", ["--max-comments", "1"]),
    ]
    for index, (stdin, returncode, reason, extra) in enumerate(cases):
        output = tmp_path / f"comments-{index}.json"
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--normalize-comments-stream",
                "--comments-output",
                str(output),
                "--max-bytes",
                "1024",
                "--max-encoded-record-bytes",
                "512",
                *extra,
            ],
            cwd=ROOT,
            input=stdin,
            capture_output=True,
            check=False,
        )
        assert completed.returncode == returncode
        assert json.loads(completed.stdout)["reason_code"] == reason
        assert b"SENSITIVE-INVALID-BASE64" not in completed.stdout


def test_workflow_streams_and_bounds_before_transition_loading() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "if gh api \\" in workflow
    assert "--paginate" in workflow
    assert "--jq '.[] | @base64'" in workflow
    assert "--slurp" not in workflow
    assert "--normalize-comments-stream" in workflow
    assert 'pipeline_status=("${PIPESTATUS[@]}")' in workflow
    assert 'source_status="INVALID"' in workflow
    assert 'source_status="OVER_LIMIT"' in workflo
    assert f'KFM_CONTROL_SOURCE_MAX_COMMENTS: "{MAX_CONTROL_SOURCE_COMMENTS}"' in workflow
    assert f'KFM_CONTROL_SOURCE_MAX_BYTES: "{MAX_CONTROL_SOURCE_BYTES}"' in workflow
    assert (
        "KFM_CONTROL_SOURCE_MAX_ENCODED_RECORD_BYTES: "
        f'"{MAX_ENCODED_COMMENT_RECORD_BYTES}"'
    ) in workflow
    assert workflow.index("Read and bound repository-control issue comments") < workflow.index(
        "Require an exact owner transition record"
    )

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/pipelines-core/src"
sys.path.insert(0, str(PACKAGE_SRC))

from pipelines_core.backfill_window import BackfillPlanError, plan_backfill_window

FIXTURES = REPO_ROOT / "fixtures/contracts/v1/runtime/backfill_window_plan"
CLI = REPO_ROOT / "scripts/plan_backfill_window.py"
REQUEST_SCHEMA = REPO_ROOT / "schemas/contracts/v1/runtime/backfill_window_request.schema.json"
PLAN_SCHEMA = REPO_ROOT / "schemas/contracts/v1/runtime/backfill_window_plan.schema.json"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("schema_path", [REQUEST_SCHEMA, PLAN_SCHEMA])
def test_schema_is_valid_draft_2020_12(schema_path: Path) -> None:
    Draft202012Validator.check_schema(_load(schema_path))


@pytest.mark.parametrize("name", ["rebuild", "noop"])
def test_valid_fixture_matches_expected_plan(name: str) -> None:
    request = _load(FIXTURES / "valid" / f"{name}.request.json")
    expected = _load(FIXTURES / "valid" / f"{name}.expected.json")
    assert plan_backfill_window(request) == expected
    Draft202012Validator(_load(PLAN_SCHEMA)).validate(expected)


def test_manifest_key_order_does_not_change_identity() -> None:
    request = _load(FIXTURES / "valid" / "rebuild.request.json")
    reordered = {
        **request,
        "manifest": {
            "parameters": {"units": "m3/m3", "depth_cm": [5, 10]},
            "source_head": request["manifest"]["source_head"],
            "schema_version": "v1",
        },
    }
    first = plan_backfill_window(request)
    second = plan_backfill_window(reordered)
    assert second["spec_hash"] == first["spec_hash"]
    assert second["dedupe_key"] == first["dedupe_key"]
    assert second["plan_id"] == first["plan_id"]
    assert second["artifact_uri"] == first["artifact_uri"]


def test_changed_current_hash_requests_rebuild() -> None:
    request = _load(FIXTURES / "valid" / "rebuild.request.json")
    request["current_published_spec_hash"] = "sha256:" + "b" * 64
    plan = plan_backfill_window(request)
    assert plan["decision"] == "REBUILD"
    assert plan["reason_codes"] == ["CURRENT_SPEC_CHANGED"]
    assert plan["write_authority"] is False


@pytest.mark.parametrize(
    ("fixture", "code"),
    [
        ("reverse_window.request.json", "WINDOW_ORDER_INVALID"),
        ("unsafe_dataset_id.request.json", "DATASET_ID_INVALID"),
    ],
)
def test_invalid_fixtures_fail_closed(fixture: str, code: str) -> None:
    with pytest.raises(BackfillPlanError) as exc:
        plan_backfill_window(_load(FIXTURES / "invalid" / fixture))
    assert exc.value.code == code


def test_window_is_bounded_to_366_days() -> None:
    request = _load(FIXTURES / "valid" / "rebuild.request.json")
    request["window"]["end"] = "2027-04-03T00:00:00Z"
    with pytest.raises(BackfillPlanError) as exc:
        plan_backfill_window(request)
    assert exc.value.code == "WINDOW_TOO_LARGE"


def test_non_utc_or_subsecond_time_is_denied() -> None:
    request = _load(FIXTURES / "valid" / "rebuild.request.json")
    request["window"]["start"] = "2026-04-01T00:00:00+00:00"
    with pytest.raises(BackfillPlanError) as exc:
        plan_backfill_window(request)
    assert exc.value.code == "WINDOW_NOT_UTC_Z"

    request = _load(FIXTURES / "valid" / "rebuild.request.json")
    request["window"]["start"] = "2026-04-01T00:00:00.100000Z"
    with pytest.raises(BackfillPlanError) as exc:
        plan_backfill_window(request)
    assert exc.value.code == "WINDOW_SUBSECOND_UNSUPPORTED"


def test_nonfinite_manifest_is_not_canonical_json() -> None:
    request = _load(FIXTURES / "valid" / "rebuild.request.json")
    request["manifest"]["bad"] = float("nan")
    with pytest.raises(BackfillPlanError) as exc:
        plan_backfill_window(request)
    assert exc.value.code == "MANIFEST_NOT_CANONICAL_JSON"


def test_cli_emits_planning_only_answer() -> None:
    completed = subprocess.run(
        [sys.executable, str(CLI), str(FIXTURES / "valid" / "rebuild.request.json")],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "ANSWER"
    assert payload["plan"]["decision"] == "REBUILD"
    assert set(payload["authority"].values()) == {False}


def test_cli_invalid_request_returns_deny() -> None:
    completed = subprocess.run(
        [sys.executable, str(CLI), str(FIXTURES / "invalid" / "reverse_window.request.json")],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 1
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "DENY"
    assert payload["plan"] is None
    assert any(item["code"] == "WINDOW_ORDER_INVALID" for item in payload["findings"])


def test_cli_duplicate_key_is_operational_error(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.json"
    path.write_text('{"dataset_id":"a","dataset_id":"b"}', encoding="utf-8")
    completed = subprocess.run(
        [sys.executable, str(CLI), str(path)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 1
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "ERROR"
    assert payload["findings"] == [{"code": "JSON_DUPLICATE_KEY", "path": "/"}]

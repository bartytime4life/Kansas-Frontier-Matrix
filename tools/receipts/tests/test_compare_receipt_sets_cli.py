from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tools.receipts.compare_receipt_sets", *args],
        check=False,
        text=True,
        capture_output=True,
    )


def manifest(*, manifest_id: str, receipts: list[dict[str, object]]) -> dict[str, object]:
    return {
        "manifest_id": manifest_id,
        "receipts": receipts,
    }


def test_cli_prints_diff_summary(tmp_path: Path) -> None:
    left_path = tmp_path / "left.json"
    right_path = tmp_path / "right.json"

    write_json(
        left_path,
        manifest(
            manifest_id="left",
            receipts=[
                {
                    "receipt_type": "validator_result",
                    "receipt_ref": "validator.json",
                    "decision": "pass",
                }
            ],
        ),
    )
    write_json(
        right_path,
        manifest(
            manifest_id="right",
            receipts=[
                {
                    "receipt_type": "validator_result",
                    "receipt_ref": "validator.json",
                    "decision": "fail",
                },
                {
                    "receipt_type": "promotion_result",
                    "receipt_ref": "promotion.json",
                    "decision": "pass",
                },
            ],
        ),
    )

    result = run_cli("--left", str(left_path), "--right", str(right_path))

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["summary"] == {
        "added_count": 1,
        "removed_count": 0,
        "changed_count": 1,
    }
    assert result.stderr == ""


def test_cli_writes_diff_file_when_out_is_provided(tmp_path: Path) -> None:
    left_path = tmp_path / "left.json"
    right_path = tmp_path / "right.json"
    out_path = tmp_path / "nested" / "diff.json"

    write_json(left_path, manifest(manifest_id="left", receipts=[]))
    write_json(right_path, manifest(manifest_id="right", receipts=[]))

    result = run_cli(
        "--left",
        str(left_path),
        "--right",
        str(right_path),
        "--out",
        str(out_path),
    )

    assert result.returncode == 0
    assert out_path.exists()
    written = json.loads(out_path.read_text(encoding="utf-8"))
    assert written["left_manifest_ref"] == "left"
    assert written["right_manifest_ref"] == "right"

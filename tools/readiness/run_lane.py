#!/usr/bin/env python3
"""Run or describe one bounded KFM readiness lane."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "control_plane" / "readiness" / "lanes.json"
SCHEMA = (
    ROOT
    / "schemas"
    / "contracts"
    / "v1"
    / "governance"
    / "readiness_lanes.schema.json"
)
LANE_IDS = ("policy", "fixtures", "proof-slice", "catalog")
MAX_OUTPUT = 65_536


class ReadinessError(ValueError):
    """A deterministic lane configuration failure."""


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReadinessError(f"unreadable registry input: {path}") from exc


def load_registry() -> dict[str, Any]:
    registry = read_json(REGISTRY)
    schema = read_json(SCHEMA)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(registry),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        raise ReadinessError("registry schema validation failed")
    ids = tuple(item["id"] for item in registry["lanes"])
    if ids != LANE_IDS:
        raise ReadinessError(f"lane order must be {LANE_IDS!r}")
    for lane in registry["lanes"]:
        if lane["status"] == "IMPLEMENTED":
            if lane["command"] is None or lane["hold_reason"] is not None:
                raise ReadinessError(f"{lane['id']}: invalid implemented state")
        elif lane["command"] is not None or lane["hold_reason"] is None:
            raise ReadinessError(f"{lane['id']}: invalid hold state")
    return registry


def lane_by_id(registry: dict[str, Any], lane_id: str) -> dict[str, Any]:
    return next(item for item in registry["lanes"] if item["id"] == lane_id)


def digest(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def result(lane: dict[str, Any], status: str, reason: str, **extra: Any) -> dict[str, Any]:
    payload = {
        "schema_version": "kfm.readiness-lane-result/v1",
        "lane": lane["id"],
        "status": status,
        "reason": reason,
        "scope": lane["scope"],
        "authority_boundary": lane["authority_boundary"],
        "effects": {
            "source_admitted": False,
            "reviewed_fixture_overwritten": False,
            "catalog_published": False,
            "release_authorized": False,
            "deployment_performed": False,
        },
    }
    payload.update(extra)
    return payload


def required_paths(lane: dict[str, Any]) -> list[str]:
    return [path for path in lane["required_paths"] if not (ROOT / path).is_file()]


def run_policy(lane: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    missing = required_paths(lane)
    if missing:
        return 3, result(
            lane,
            "HOLD",
            "REQUIRED_PATH_MISSING",
            missing_paths=missing,
        )

    configured = os.environ.get("OPA_BIN")
    binary = configured or shutil.which("opa")
    if not binary:
        return 3, result(
            lane,
            "HOLD",
            "OPA_BINARY_UNAVAILABLE",
            command=lane["command"],
        )

    command = [binary, *lane["command"][1:]]
    environment = os.environ.copy()
    environment.update(
        {
            "KFM_NO_NETWORK": "1",
            "PYTHONHASHSEED": "0",
            "TZ": "UTC",
        }
    )
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=120,
        )
    except (OSError, subprocess.TimeoutExpired):
        return 2, result(lane, "ERROR", "OPA_EXECUTION_ERROR")

    stdout = completed.stdout[: MAX_OUTPUT + 1]
    stderr = completed.stderr[: MAX_OUTPUT + 1]
    if len(stdout) > MAX_OUTPUT or len(stderr) > MAX_OUTPUT:
        return 2, result(lane, "ERROR", "OPA_OUTPUT_LIMIT")
    receipt = {
        "command": ["opa", *lane["command"][1:]],
        "exit_code": completed.returncode,
        "stdout_bytes": len(stdout),
        "stdout_sha256": digest(stdout),
        "stderr_bytes": len(stderr),
        "stderr_sha256": digest(stderr),
    }
    if completed.returncode != 0:
        return 1, result(lane, "FAIL", "OPA_TEST_FAILED", receipt=receipt)
    return 0, result(lane, "PASS", "BOUNDED_REGO_PAIR_PASSED", receipt=receipt)


def run_lane(lane: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    if lane["status"] == "HOLD":
        return 3, result(
            lane,
            "HOLD",
            lane["hold_reason"],
            missing_paths=required_paths(lane),
        )
    if lane["id"] == "policy":
        return run_policy(lane)
    raise ReadinessError(f"no runner for implemented lane: {lane['id']}")


def canonical(value: dict[str, Any]) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("lane", choices=LANE_IDS)
    parser.add_argument(
        "--describe",
        action="store_true",
        help="validate and print lane configuration without executing it",
    )
    args = parser.parse_args()
    try:
        registry = load_registry()
        lane = lane_by_id(registry, args.lane)
        if args.describe:
            print(canonical({"schema_version": registry["schema_version"], "lane": lane}))
            return 0
        code, payload = run_lane(lane)
    except ReadinessError as exc:
        print(
            canonical(
                {
                    "schema_version": "kfm.readiness-lane-result/v1",
                    "lane": args.lane,
                    "status": "ERROR",
                    "reason": str(exc),
                }
            )
        )
        return 2
    print(canonical(payload))
    return code


if __name__ == "__main__":
    raise SystemExit(main())

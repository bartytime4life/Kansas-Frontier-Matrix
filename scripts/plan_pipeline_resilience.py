#!/usr/bin/env python3
"""Validate and plan one pipeline resilience decision without network or writes."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_SRC = REPO_ROOT / "packages/pipelines-core/src"
sys.path.insert(0, str(PACKAGE_SRC))

from pipelines_core.pipeline_resilience import (
    PipelineResiliencePlanError,
    plan_pipeline_resilience,
)

REQUEST_SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/runtime/pipeline_resilience_request.schema.json"
)
PLAN_SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/runtime/pipeline_resilience_plan.schema.json"
)
MAX_INPUT_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _load_input(
    path: Path,
) -> tuple[dict[str, Any] | None, list[dict[str, str]], bool]:
    try:
        if path.is_symlink():
            return None, [{"code": "INPUT_SYMLINK_DENIED", "path": "/"}], True
        if not path.is_file():
            return None, [{"code": "INPUT_NOT_FILE", "path": "/"}], True
        if path.stat().st_size > MAX_INPUT_BYTES:
            return None, [{"code": "INPUT_TOO_LARGE", "path": "/"}], True
        payload = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except UnicodeError:
        return None, [{"code": "JSON_NOT_UTF8", "path": "/"}], True
    except DuplicateKeyError:
        return None, [{"code": "JSON_DUPLICATE_KEY", "path": "/"}], True
    except NonFiniteNumberError:
        return None, [{"code": "JSON_NONFINITE_NUMBER", "path": "/"}], True
    except json.JSONDecodeError:
        return None, [{"code": "JSON_INVALID", "path": "/"}], True
    except (OSError, RecursionError, ValueError):
        return None, [{"code": "INPUT_UNREADABLE", "path": "/"}], True
    if not isinstance(payload, dict):
        return None, [{"code": "ROOT_NOT_OBJECT", "path": "/"}], False
    return payload, [], False


def _schema_findings(
    path: Path, payload: dict[str, Any]
) -> list[dict[str, str]]:
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(
        schema, format_checker=FormatChecker()
    )
    errors = sorted(
        validator.iter_errors(payload),
        key=lambda item: list(item.absolute_path),
    )
    findings: list[dict[str, str]] = []
    for error in errors[:MAX_FINDINGS]:
        pointer = "/" + "/".join(
            str(part).replace("~", "~0").replace("/", "~1")
            for part in error.absolute_path
        )
        findings.append({"code": "SCHEMA_INVALID", "path": pointer or "/"})
    if len(errors) > MAX_FINDINGS:
        findings.append({"code": "SCHEMA_FINDINGS_TRUNCATED", "path": "/"})
    return findings


def _operator_safe_plan(plan: Mapping[str, Any]) -> dict[str, Any]:
    """Project a validated plan without propagating restricted access metadata."""

    trigger = plan["trigger"]
    return {
        "projection": "operator-safe-v1",
        "plan_id": plan["plan_id"],
        "planner_version": plan["planner_version"],
        "pipeline_id": plan["pipeline_id"],
        "step_id": plan["step_id"],
        "contract_version": plan["contract_version"],
        "spec_hash": plan["spec_hash"],
        "idempotency_key": plan["idempotency_key"],
        "decision": plan["decision"],
        "reason_codes": plan["reason_codes"],
        "trigger": {
            "type": trigger["type"],
            "environment": trigger["environment"],
            "concurrency_group": trigger["concurrency_group"],
            "decision": trigger["decision"],
            "reason_codes": trigger["reason_codes"],
        },
        "retry": plan["retry"],
        "backpressure": plan["backpressure"],
        "circuit_breaker": plan["circuit_breaker"],
        "delivery": plan["delivery"],
        "kill_switch": plan["kill_switch"],
        "required_receipts": plan["required_receipts"],
        "observability_requirements": plan["observability_requirements"],
        "write_authority": False,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Plan deterministic trigger, retry, backpressure, replay, "
            "and kill-switch decisions."
        )
    )
    parser.add_argument("input", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    payload, findings, operational_error = _load_input(args.input)
    plan: dict[str, Any] | None = None

    if payload is not None:
        findings.extend(_schema_findings(REQUEST_SCHEMA, payload))
        if not findings:
            try:
                plan = plan_pipeline_resilience(payload)
            except PipelineResiliencePlanError as exc:
                findings.append({"code": exc.code, "path": exc.field})
            if plan is not None:
                findings.extend(_schema_findings(PLAN_SCHEMA, plan))

    outcome = "ANSWER" if not findings else (
        "ERROR" if operational_error else "DENY"
    )
    result = {
        "ok": not findings,
        "outcome": outcome,
        "plan": (
            _operator_safe_plan(plan)
            if not findings and plan is not None
            else None
        ),
        "findings": sorted(
            findings, key=lambda item: (item["path"], item["code"])
        ),
        "scope": "planning-only-pipeline-resilience",
        "authority": {
            "network_fetch": False,
            "source_activation": False,
            "artifact_write": False,
            "workflow_mutation": False,
            "database_mutation": False,
            "policy_evaluation": False,
            "signature_operation": False,
            "promotion": False,
            "release": False,
            "publication": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())

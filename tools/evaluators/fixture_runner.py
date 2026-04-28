from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


class EvaluatorError(ValueError):
    pass


def _load_json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise EvaluatorError(f"invalid JSON at {path}: {exc}") from exc

    if not isinstance(value, dict):
        raise EvaluatorError(f"JSON document must be an object: {path}")

    return value


def _validator(schema_path: Path) -> Draft202012Validator:
    schema = _load_json_object(schema_path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def _validate_payload(payload: dict[str, Any], schema_path: Path, label: str) -> None:
    validator = _validator(schema_path)
    errors = sorted(validator.iter_errors(payload), key=lambda item: list(item.path))
    if errors:
        details = "; ".join(
            f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
            for error in errors
        )
        raise EvaluatorError(f"{label} failed schema validation: {details}")


def _sha256_hex(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    digest = hashlib.sha256(canonical).hexdigest()
    return f"sha256:{digest}"


@dataclass(frozen=True)
class FixtureEvaluation:
    report: dict[str, Any]


def evaluate_fixture(*, config: dict[str, Any], fixture: dict[str, Any]) -> FixtureEvaluation:
    metrics_by_name = {
        metric["name"]: metric
        for metric in config["metrics"]
        if metric.get("enabled", True)
    }

    metric_breakdown: dict[str, float] = {}
    metric_rows: list[dict[str, Any]] = []
    failure_flags: list[str] = []

    for metric_result in fixture["metric_results"]:
        name = metric_result["name"]
        if name not in metrics_by_name:
            continue

        metric_cfg = metrics_by_name[name]
        passed = bool(metric_result["passed"])
        score = float(metric_result["score"])
        reason_code = metric_result["reason_code"]
        explanation = metric_result["explanation"]

        row = {
            "name": name,
            "score": score,
            "passed": passed,
            "reason_code": reason_code,
            "severity": "info" if passed else "blocking",
            "explanation": {"summary": explanation},
        }
        metric_rows.append(row)
        metric_breakdown[name] = score

        if not passed and metric_cfg.get("must_pass", False):
            failure_flags.append(metric_cfg.get("failure_flag") or reason_code)

    normalized_flags = sorted({flag for flag in failure_flags if flag})

    outcome = "ALLOW"
    if any(flag.startswith("ERROR") for flag in normalized_flags):
        outcome = "ERROR"
    elif normalized_flags:
        has_abstention_metric = any(
            not row["passed"] and metrics_by_name[row["name"]].get("kind") == "abstention"
            for row in metric_rows
            if row["name"] in metrics_by_name
        )
        outcome = "ABSTAIN" if has_abstention_metric else "DENY"

    report = {
        "report_type": "kfm.evaluator_report.v1",
        "evaluator": config["evaluator"],
        "evaluator_version": config.get("evaluator_version", "v1"),
        "subject_ref": fixture["subject_ref"],
        "subject_type": fixture["subject_type"],
        "evaluator_spec_hash": _sha256_hex(config),
        "artifact_spec_hash": fixture.get("artifact_spec_hash", _sha256_hex(fixture)),
        "outcome": outcome,
        "metric_breakdown": metric_breakdown,
        "failure_flags": normalized_flags,
        "metrics": metric_rows,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    return FixtureEvaluation(report=report)


def run_fixture_evaluation(
    *,
    config_path: Path,
    fixture_path: Path,
    report_schema_path: Path,
    config_schema_path: Path,
    fixture_schema_path: Path,
) -> FixtureEvaluation:
    config = _load_json_object(config_path)
    fixture = _load_json_object(fixture_path)

    _validate_payload(config, config_schema_path, "config")
    _validate_payload(fixture, fixture_schema_path, "fixture")

    evaluation = evaluate_fixture(config=config, fixture=fixture)
    _validate_payload(evaluation.report, report_schema_path, "report")

    return evaluation

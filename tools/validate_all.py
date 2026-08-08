#!/usr/bin/env python3
"""Run the bounded KFM core validator set in deterministic order.

This is repository validation orchestration only. A zero exit proves that the
selected local validators completed under their own contracts. It does not
resolve evidence, execute release authority, promote data, or publish anything.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

TOOL_NAME = "kfm-validate-all"
SCHEMA_VERSION = "1.0.0"
EXIT_OK = 0
EXIT_VALIDATION = 1
EXIT_ERROR = 2
MAX_DIAGNOSTIC_CHARS = 8_000

REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ValidatorSpec:
    """One named, ordered validator invocation."""

    name: str
    path: Path
    args: tuple[str, ...] = ("--fixtures",)


@dataclass(frozen=True)
class ValidatorResult:
    """One finite child-validator result."""

    name: str
    outcome: str
    exit_code: int | None
    warnings: tuple[str, ...]
    diagnostics: tuple[str, ...]

    @property
    def blocking(self) -> bool:
        return self.outcome in {"FAIL", "ERROR"}


DEFAULT_REGISTRY: tuple[ValidatorSpec, ...] = (
    ValidatorSpec("dataset-version", REPO_ROOT / "tools/validators/validate_dataset_version.py"),
    ValidatorSpec("layer-manifest", REPO_ROOT / "tools/validators/validate_layer_manifest.py"),
    ValidatorSpec("release-manifest", REPO_ROOT / "tools/validators/validate_release_manifest.py"),
    ValidatorSpec("evidence-bundle", REPO_ROOT / "tools/validators/validate_evidence_bundle.py"),
    ValidatorSpec(
        "runtime-response-envelope",
        REPO_ROOT / "tools/validators/validate_runtime_response_envelope.py",
    ),
    ValidatorSpec("release-decision", REPO_ROOT / "tools/validators/validate_release_decision.py"),
    ValidatorSpec(
        "promotion-decision",
        REPO_ROOT / "tools/validators/validate_promotion_decision.py",
    ),
)

PROFILES: Mapping[str, tuple[str, ...]] = {
    "core": tuple(spec.name for spec in DEFAULT_REGISTRY),
    "schema": tuple(spec.name for spec in DEFAULT_REGISTRY),
}


class OrchestratorError(ValueError):
    """A deterministic configuration or selection failure."""


def _safe_lines(value: str) -> tuple[str, ...]:
    normalized = value.replace("\r\n", "\n").replace("\r", "\n")
    if len(normalized) > MAX_DIAGNOSTIC_CHARS:
        normalized = normalized[:MAX_DIAGNOSTIC_CHARS] + "\n[diagnostics truncated]"
    return tuple(line for line in normalized.splitlines() if line.strip())


def _warning_lines(lines: Iterable[str]) -> tuple[str, ...]:
    return tuple(line for line in lines if line.lstrip().upper().startswith("WARNING"))


def _child_environment() -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "KFM_NO_NETWORK": "1",
            "NO_PROXY": "*",
            "PIP_DISABLE_PIP_VERSION_CHECK": "1",
            "PIP_NO_INPUT": "1",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
            "PYTHONUNBUFFERED": "1",
            "TZ": "UTC",
        }
    )
    return env


def run_validator(
    spec: ValidatorSpec,
    *,
    repo_root: Path = REPO_ROOT,
) -> ValidatorResult:
    """Run one validator with bounded diagnostics and finite outcomes."""

    path = spec.path if spec.path.is_absolute() else repo_root / spec.path
    if not path.is_file():
        return ValidatorResult(
            name=spec.name,
            outcome="ERROR",
            exit_code=None,
            warnings=(),
            diagnostics=("validator file is missing",),
        )

    command = [sys.executable, str(path), *spec.args]
    try:
        completed = subprocess.run(
            command,
            cwd=repo_root,
            env=_child_environment(),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except OSError:
        return ValidatorResult(
            name=spec.name,
            outcome="ERROR",
            exit_code=None,
            warnings=(),
            diagnostics=("validator process could not be started",),
        )

    stdout = _safe_lines(completed.stdout)
    stderr = _safe_lines(completed.stderr)
    warnings = _warning_lines((*stdout, *stderr))
    if completed.returncode == 0:
        outcome = "WARNING" if warnings else "PASS"
    elif completed.returncode == 1:
        outcome = "FAIL"
    else:
        outcome = "ERROR"

    return ValidatorResult(
        name=spec.name,
        outcome=outcome,
        exit_code=completed.returncode,
        warnings=warnings,
        diagnostics=(*stdout, *stderr),
    )


def _selected_registry(
    registry: Sequence[ValidatorSpec],
    *,
    profile: str,
    only: Sequence[str],
) -> tuple[ValidatorSpec, ...]:
    names = [spec.name for spec in registry]
    if len(names) != len(set(names)):
        raise OrchestratorError("validator registry contains duplicate names")

    index = {spec.name: spec for spec in registry}
    if only:
        requested: list[str] = []
        for raw in only:
            requested.extend(part.strip() for part in raw.split(",") if part.strip())
    else:
        if profile not in PROFILES:
            raise OrchestratorError(f"unknown profile: {profile}")
        requested = list(PROFILES[profile])

    unknown = sorted(set(requested) - set(index))
    if unknown:
        raise OrchestratorError("unknown validator selection: " + ", ".join(unknown))

    requested_set = set(requested)
    return tuple(spec for spec in registry if spec.name in requested_set)


def run_validators(
    specs: Sequence[ValidatorSpec],
    *,
    repo_root: Path = REPO_ROOT,
    fail_on_warning: bool = False,
) -> tuple[dict[str, object], int]:
    """Run the selected validators in registry order and build one stable report."""

    results = tuple(run_validator(spec, repo_root=repo_root) for spec in specs)
    warning_count = sum(result.outcome == "WARNING" for result in results)
    fail_count = sum(result.outcome == "FAIL" for result in results)
    error_count = sum(result.outcome == "ERROR" for result in results)

    if error_count:
        outcome = "ERROR"
        exit_code = EXIT_ERROR
    elif fail_count or (fail_on_warning and warning_count):
        outcome = "FAIL"
        exit_code = EXIT_VALIDATION
    elif warning_count:
        outcome = "WARNING"
        exit_code = EXIT_OK
    else:
        outcome = "PASS"
        exit_code = EXIT_OK

    report: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_NAME,
        "outcome": outcome,
        "fail_on_warning": fail_on_warning,
        "summary": {
            "selected": len(results),
            "passed": sum(result.outcome == "PASS" for result in results),
            "warnings": warning_count,
            "failed": fail_count,
            "errors": error_count,
        },
        "results": [
            {
                "name": result.name,
                "outcome": result.outcome,
                "exit_code": result.exit_code,
                "warnings": list(result.warnings),
                "diagnostics": list(result.diagnostics),
            }
            for result in results
        ],
        "authority_boundary": (
            "Validation orchestration is not evidence closure, policy approval, "
            "promotion, release, deployment, or publication authority."
        ),
    }
    return report, exit_code


def _json_text(report: Mapping[str, object]) -> str:
    return json.dumps(
        report,
        allow_nan=False,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ) + "\n"


def _text_report(report: Mapping[str, object]) -> str:
    lines = [
        f"{TOOL_NAME}: {report['outcome']}",
        "NAME\tOUTCOME\tEXIT",
    ]
    for item in report["results"]:  # type: ignore[index]
        assert isinstance(item, dict)
        exit_value = "-" if item["exit_code"] is None else str(item["exit_code"])
        lines.append(f"{item['name']}\t{item['outcome']}\t{exit_value}")
    summary = report["summary"]
    assert isinstance(summary, dict)
    lines.append(
        "summary: "
        + " ".join(
            f"{key}={summary[key]}"
            for key in ("selected", "passed", "warnings", "failed", "errors")
        )
    )
    lines.append(str(report["authority_boundary"]))
    return "\n".join(lines) + "\n"


def _junit_text(report: Mapping[str, object]) -> str:
    summary = report["summary"]
    assert isinstance(summary, dict)
    suite = ET.Element(
        "testsuite",
        {
            "name": TOOL_NAME,
            "tests": str(summary["selected"]),
            "failures": str(summary["failed"]),
            "errors": str(summary["errors"]),
            "skipped": "0",
        },
    )
    for item in report["results"]:  # type: ignore[index]
        assert isinstance(item, dict)
        case = ET.SubElement(
            suite,
            "testcase",
            {"classname": TOOL_NAME, "name": str(item["name"])},
        )
        diagnostics = "\n".join(str(value) for value in item["diagnostics"])
        outcome = item["outcome"]
        if outcome == "FAIL":
            node = ET.SubElement(case, "failure", {"message": "validator failed"})
            node.text = diagnostics
        elif outcome == "ERROR":
            node = ET.SubElement(case, "error", {"message": "validator error"})
            node.text = diagnostics
        elif outcome == "WARNING":
            output = ET.SubElement(case, "system-out")
            output.text = diagnostics
    xml = ET.tostring(suite, encoding="unicode", short_empty_elements=True)
    return '<?xml version="1.0" encoding="utf-8"?>\n' + xml + "\n"


def serialize_report(report: Mapping[str, object], output_format: str) -> str:
    if output_format == "json":
        return _json_text(report)
    if output_format == "junit":
        return _junit_text(report)
    if output_format == "text":
        return _text_report(report)
    raise OrchestratorError(f"unknown output format: {output_format}")


def _write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        delete=False,
    ) as stream:
        stream.write(content)
        temporary = Path(stream.name)
    temporary.replace(path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", default="core", choices=sorted(PROFILES))
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="Run only named validators; may be repeated or comma separated.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json", "junit"),
        default="text",
        dest="output_format",
    )
    parser.add_argument("--report", type=Path)
    parser.add_argument("--list", action="store_true", dest="list_validators")
    parser.add_argument("--fail-on-warning", action="store_true")
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    registry: Sequence[ValidatorSpec] | None = None,
    repo_root: Path = REPO_ROOT,
) -> int:
    args = build_parser().parse_args(argv)
    active_registry = tuple(registry or DEFAULT_REGISTRY)

    if args.list_validators:
        for spec in active_registry:
            print(spec.name)
        return EXIT_OK

    try:
        selected = _selected_registry(
            active_registry,
            profile=args.profile,
            only=args.only,
        )
        report, exit_code = run_validators(
            selected,
            repo_root=repo_root,
            fail_on_warning=args.fail_on_warning,
        )
        rendered = serialize_report(report, args.output_format)
        if args.report is not None:
            _write_atomic(args.report, rendered)
        print(rendered, end="")
        return exit_code
    except OrchestratorError as exc:
        error_report = {
            "schema_version": SCHEMA_VERSION,
            "tool": TOOL_NAME,
            "outcome": "ERROR",
            "error": {"code": "ORCHESTRATOR_CONFIGURATION_ERROR", "message": str(exc)},
            "authority_boundary": (
                "No validator result, evidence closure, policy approval, promotion, "
                "release, deployment, or publication authority was created."
            ),
        }
        print(_json_text(error_report), end="")
        return EXIT_ERROR
    except OSError:
        print(
            _json_text(
                {
                    "schema_version": SCHEMA_VERSION,
                    "tool": TOOL_NAME,
                    "outcome": "ERROR",
                    "error": {
                        "code": "REPORT_WRITE_ERROR",
                        "message": "The validation report could not be written.",
                    },
                    "authority_boundary": (
                        "No validator result, evidence closure, policy approval, promotion, "
                        "release, deployment, or publication authority was created."
                    ),
                }
            ),
            end="",
        )
        return EXIT_ERROR


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the fixture-only Habitat ModelRunReceipt profile.

The validator checks closed shape, deterministic identity, run chronology,
input closure, source-role preservation, output inventory, uncertainty and
validation references, and explicit non-authority. It performs no model run,
source access, evidence resolution, policy evaluation, review, release, or
publication operation.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for import_root in (REPO_ROOT, HASHING_SRC):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))

from hashing import compute_spec_hash  # noqa: E402

SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/habitat/model_run_receipt.schema.json"
)
FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/domains/habitat/model_run_receipt/cases.json"
)
PROFILE = "kfm.habitat-model-run-receipt.fixture.v1"
PREFIX = "kfm:model-run-receipt:habitat:"
MAX_BYTES = 2 * 1024 * 1024
MAX_FINDINGS = 100
LIMITATIONS = (
    "FIXTURE_ONLY",
    "MODEL_OUTPUT_NOT_OBSERVATION",
    "NO_EVIDENCE_OR_PROOF_AUTHORITY",
    "NO_POLICY_OR_REVIEW_AUTHORITY",
    "NO_RELEASE_OR_PUBLICATION_AUTHORITY",
    "RECEIPT_IS_PROCESS_MEMORY_ONLY",
)
NON_EFFECTS = (
    "no_model_or_transform_execution",
    "no_source_or_network_access",
    "no_evidence_or_proof_resolution",
    "no_policy_or_review_decision",
    "no_lifecycle_catalog_release_or_publication_write",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(item).replace("~", "~0").replace("/", "~1") for item in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("MODEL_RUN_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("MODEL_RUN_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("MODEL_RUN_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("MODEL_RUN_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("MODEL_RUN_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("MODEL_RUN_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("MODEL_RUN_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    errors = sorted(
        islice(_schema_validator().iter_errors(value), MAX_FINDINGS),
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    return tuple(
        sorted(
            {
                Finding("MODEL_RUN_SCHEMA_INVALID", _pointer(error.absolute_path))
                for error in errors
            }
        )
    )


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = copy.deepcopy(dict(value))
    subject.pop("receipt_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def expected_inputs_digest(value: Mapping[str, Any]) -> str:
    return compute_spec_hash(value.get("inputs", []))


def _duplicate_or_unsorted(
    values: list[str], duplicate_code: str, order_code: str, path: str
) -> set[Finding]:
    findings: set[Finding] = set()
    if len(values) != len(set(values)):
        findings.add(Finding(duplicate_code, path))
    if values != sorted(values):
        findings.add(Finding(order_code, path))
    return findings


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    expected_hash, expected_id = canonical_identity(value)
    if value["spec_hash"] != expected_hash:
        findings.add(Finding("MODEL_RUN_SPEC_HASH_MISMATCH", "/spec_hash"))
    if value["receipt_id"] != expected_id:
        findings.add(Finding("MODEL_RUN_RECEIPT_ID_MISMATCH", "/receipt_id"))
    if value["inputs_digest"] != expected_inputs_digest(value):
        findings.add(Finding("MODEL_RUN_INPUTS_DIGEST_MISMATCH", "/inputs_digest"))
    if value["limitations"] != list(LIMITATIONS):
        findings.add(Finding("MODEL_RUN_LIMITATIONS_MISMATCH", "/limitations"))

    started = _time(value["started_at"])
    completed = _time(value["completed_at"])
    recorded = _time(value["recorded_at"])
    if started is None or completed is None or recorded is None or not started <= completed <= recorded:
        findings.add(Finding("MODEL_RUN_TIME_ORDER_INVALID", "/completed_at"))

    input_refs = [item["input_ref"] for item in value["inputs"]]
    findings.update(
        _duplicate_or_unsorted(
            input_refs,
            "MODEL_RUN_INPUT_REF_DUPLICATE",
            "MODEL_RUN_INPUT_ORDER_INVALID",
            "/inputs",
        )
    )
    evidence_refs = list(value["evidence_refs"])
    findings.update(
        _duplicate_or_unsorted(
            evidence_refs,
            "MODEL_RUN_EVIDENCE_REF_DUPLICATE",
            "MODEL_RUN_EVIDENCE_ORDER_INVALID",
            "/evidence_refs",
        )
    )
    output_refs = [item["output_ref"] for item in value["outputs"]]
    findings.update(
        _duplicate_or_unsorted(
            output_refs,
            "MODEL_RUN_OUTPUT_REF_DUPLICATE",
            "MODEL_RUN_OUTPUT_ORDER_INVALID",
            "/outputs",
        )
    )

    if value["run_state"] == "COMPLETED":
        if not value["outputs"]:
            findings.add(Finding("MODEL_RUN_COMPLETED_OUTPUT_REQUIRED", "/outputs"))
        if value["failure_reason_codes"]:
            findings.add(
                Finding("MODEL_RUN_COMPLETED_FAILURE_REASON_FORBIDDEN", "/failure_reason_codes")
            )
    else:
        if value["outputs"]:
            findings.add(Finding("MODEL_RUN_FAILED_OUTPUT_FORBIDDEN", "/outputs"))
        if not value["failure_reason_codes"]:
            findings.add(Finding("MODEL_RUN_FAILED_REASON_REQUIRED", "/failure_reason_codes"))

    return tuple(sorted(findings))


def validate_payload(value: object) -> Result:
    if not isinstance(value, Mapping):
        return Result("DENY", (Finding("MODEL_RUN_SCHEMA_INVALID", "/"),))
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    findings = _semantic_findings(value)
    return Result("DENY" if findings else "PASS", findings)


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest must be an object")
    return value


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [
        item.replace("~1", "/").replace("~0", "~")
        for item in pointer.removeprefix("/").split("/")
    ]
    target: Any = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _set_pointer(value, mutation["path"], mutation["value"])
    value["inputs_digest"] = expected_inputs_digest(value)
    value["spec_hash"], value["receipt_id"] = canonical_identity(value)
    for mutation in case.get("assertion_mutations", []):
        _set_pointer(value, mutation["path"], mutation["value"])
    return value


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if findings:
        return Result("ERROR", findings)
    return validate_payload(value)


def serialize(path: Path, result: Result) -> str:
    payload = {
        "authority": "NONE",
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "input": path.name,
        "non_effects": list(NON_EFFECTS),
        "outcome": result.outcome,
        "profile": PROFILE,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def _run_fixtures() -> int:
    manifest = load_fixtures()
    rows: list[dict[str, Any]] = []
    suite_match = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        match = result.outcome == case["expected_outcome"] and actual == case["expected_findings"]
        suite_match = suite_match and match
        rows.append({"case_id": case["case_id"], "match": match, "outcome": result.outcome})
    print(
        json.dumps(
            {
                "authority": "NONE",
                "case_count": len(rows),
                "cases": rows,
                "non_effects": list(NON_EFFECTS),
                "profile": PROFILE,
                "suite_match": suite_match,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if suite_match else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("path cannot be combined with --fixtures")
        return _run_fixtures()
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(serialize(args.path, result))
    return 0 if result.outcome == "PASS" else 2 if result.outcome == "ERROR" else 1


if __name__ == "__main__":
    raise SystemExit(main())

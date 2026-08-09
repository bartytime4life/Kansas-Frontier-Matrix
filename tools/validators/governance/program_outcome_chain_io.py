"""Bounded I/O, schema checks, fixture replay, and serialization."""
from __future__ import annotations

import copy
import json
import math
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

from program_outcome_chain_model import (
    CASES,
    MAX_FILE_BYTES,
    MAX_SCHEMA_FINDINGS,
    ROOT,
    SCHEMA,
    SCOPE,
    Finding,
    ValidationResult,
    assign_identity,
    build_fixture_base,
)
from program_outcome_chain_semantics import (
    outcome_for,
    semantic_findings,
)


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _nonfinite(_: str) -> object:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [
                Finding("INPUT_SYMLINK_DENIED", "/")
            ]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except UnicodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1")
        for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(
    candidate: Mapping[str, Any],
) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )
        errors = list(
            islice(
                validator.iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        ValueError,
        RecursionError,
    ):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding(
            "SCHEMA_INVALID",
            _pointer(error.absolute_path),
        )
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda error: (
                _pointer(error.absolute_path),
                str(error.validator),
            ),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(
            Finding("SCHEMA_FINDINGS_TRUNCATED", "/")
        )
    return findings


def validate_payload(
    candidate: Mapping[str, Any],
) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(
        outcome_for(list(ordered)),
        ordered,
    )


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult(
            "ERROR",
            tuple(sorted(set(findings))),
        )
    return validate_payload(candidate)


def _set_pointer(
    candidate: dict[str, Any],
    pointer: str,
    value: Any,
) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
        if part
    ]
    if not parts:
        raise ValueError("invalid mutation path")
    current: Any = candidate
    for part in parts[:-1]:
        if isinstance(current, dict):
            if part not in current:
                raise ValueError("unknown mutation path")
            current = current[part]
        elif isinstance(current, list):
            try:
                current = current[int(part)]
            except (ValueError, IndexError):
                raise ValueError(
                    "unknown mutation path"
                ) from None
        else:
            raise ValueError("unknown mutation path")
    final = parts[-1]
    if isinstance(current, dict):
        if final not in current:
            raise ValueError("unknown mutation path")
        current[final] = copy.deepcopy(value)
    elif isinstance(current, list):
        try:
            current[int(final)] = copy.deepcopy(value)
        except (ValueError, IndexError):
            raise ValueError(
                "unknown mutation path"
            ) from None
    else:
        raise ValueError("invalid mutation path")


def _load_fixture_document() -> dict[str, Any]:
    document, findings = _read(CASES)
    if (
        document is None
        or findings
        or not isinstance(document.get("bases"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(
    document: Mapping[str, Any],
    case: Mapping[str, Any],
) -> dict[str, Any]:
    bases = document["bases"]
    base_name = case.get("base")
    if (
        not isinstance(bases, Mapping)
        or base_name not in bases
        or not isinstance(bases[base_name], Mapping)
    ):
        raise ValueError("unknown fixture base")
    candidate = build_fixture_base(dict(bases[base_name]))
    for mutation in case.get("mutations", []):
        if (
            not isinstance(mutation, Mapping)
            or not isinstance(mutation.get("path"), str)
            or "value" not in mutation
        ):
            raise ValueError("invalid fixture mutation")
        _set_pointer(
            candidate,
            mutation["path"],
            mutation["value"],
        )
    if case.get("reassign_identity", True):
        candidate = assign_identity(candidate)
    return candidate


def run_fixture_suite() -> tuple[bool, dict[str, Any]]:
    try:
        document = _load_fixture_document()
        reports: list[dict[str, Any]] = []
        all_ok = True
        for raw_case in document["cases"]:
            if not isinstance(raw_case, Mapping):
                raise ValueError("invalid fixture case")
            candidate = materialize_case(
                document,
                raw_case,
            )
            result = validate_payload(candidate)
            expected = raw_case.get("expected")
            if not isinstance(expected, Mapping):
                raise ValueError("invalid expected outcome")
            expected_codes = expected.get("finding_codes")
            if not isinstance(expected_codes, list):
                raise ValueError(
                    "invalid expected finding codes"
                )
            actual_codes = sorted(
                {finding.code for finding in result.findings}
            )
            ok = (
                result.outcome == expected.get("outcome")
                and actual_codes == sorted(expected_codes)
            )
            all_ok = all_ok and ok
            reports.append(
                {
                    "case_id": raw_case.get("case_id"),
                    "actual": {
                        "outcome": result.outcome,
                        "finding_codes": actual_codes,
                    },
                    "expected": {
                        "outcome": expected.get("outcome"),
                        "finding_codes": sorted(expected_codes),
                    },
                    "ok": ok,
                }
            )
        return all_ok, {
            "profile": document.get("profile"),
            "cases": reports,
            "authority": authority_non_effects(),
        }
    except (
        OSError,
        UnicodeError,
        ValueError,
        RuntimeError,
    ):
        return False, {
            "profile": (
                "kfm.governance.program-outcome-chain."
                "fixture-suite.v1"
            ),
            "cases": [],
            "error": "FIXTURE_MANIFEST_INVALID",
            "authority": authority_non_effects(),
        }


def authority_non_effects() -> dict[str, bool]:
    return {
        "activates_source": False,
        "resolves_evidence": False,
        "evaluates_policy": False,
        "approves_review": False,
        "establishes_causation": False,
        "promotes": False,
        "releases": False,
        "publishes": False,
    }


def serialize(
    path: Path,
    result: ValidationResult,
) -> str:
    try:
        name = (
            path.resolve()
            .relative_to(ROOT.resolve())
            .as_posix()
        )
    except (OSError, ValueError):
        name = path.name
    return json.dumps(
        {
            "file": name,
            "outcome": result.outcome,
            "findings": [
                {
                    "code": finding.code,
                    "path": finding.path,
                }
                for finding in result.findings
            ],
            "scope": SCOPE,
            "authority": authority_non_effects(),
        },
        sort_keys=True,
        separators=(",", ":"),
    )

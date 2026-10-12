#!/usr/bin/env python3
"""CLI and fixture-polarity runner for AdvisoryEventEnvelope validation."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators.advisory_event_envelope_support import (
    FIXTURE_BASES_ROOT,
    FIXTURE_CASES,
    FIXTURE_ROOT,
    SCOPE,
    Finding,
    ValidationResult,
    _read_object,
    canonical_event_id,
    validate_envelope,
    validate_envelope_object,
)

def _outcome(result: ValidationResult) -> str:
    if result.ok:
        return "PASS"
    return "ERROR" if result.error else "REJECT"


def _render(label: str | Path, result: ValidationResult) -> dict[str, Any]:
    return {
        "path": label.as_posix() if isinstance(label, Path) else label,
        "ok": result.ok,
        "outcome": _outcome(result),
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "scope": SCOPE,
        "authority": {
            "network_fetch": False,
            "source_activation": False,
            "alert_authority": False,
            "lifecycle_write": False,
            "release": False,
            "publication": False,
            "public_use": False,
        },
    }


def _decode_json_pointer(value: Any) -> list[str] | None:
    """Decode a restricted RFC 6901 pointer used by the fixture manifest."""

    if not isinstance(value, str) or not value.startswith("/") or value == "/":
        return None
    decoded: list[str] = []
    for raw_part in value[1:].split("/"):
        output: list[str] = []
        index = 0
        while index < len(raw_part):
            character = raw_part[index]
            if character != "~":
                output.append(character)
                index += 1
                continue
            if index + 1 >= len(raw_part) or raw_part[index + 1] not in {"0", "1"}:
                return None
            output.append("~" if raw_part[index + 1] == "0" else "/")
            index += 2
        decoded.append("".join(output))
    return decoded


def _apply_fixture_patch(
    envelope: dict[str, Any],
    patch: Mapping[str, Any],
    *,
    case_index: int,
    patch_index: int,
) -> Finding | None:
    location = f"/cases/{case_index}/patches/{patch_index}"
    operation = patch.get("op")
    parts = _decode_json_pointer(patch.get("path"))
    if operation not in {"replace", "remove"} or parts is None:
        return Finding("FIXTURE_PATCH_INVALID", location)
    if operation == "replace" and "value" not in patch:
        return Finding("FIXTURE_PATCH_INVALID", location)

    parent: Any = envelope
    for part in parts[:-1]:
        if not isinstance(parent, dict) or part not in parent:
            return Finding("FIXTURE_PATCH_INVALID", location)
        parent = parent[part]
    key = parts[-1]
    if not isinstance(parent, dict) or key not in parent:
        return Finding("FIXTURE_PATCH_INVALID", location)

    if operation == "remove":
        del parent[key]
    else:
        parent[key] = copy.deepcopy(patch["value"])
    return None


def _materialize_fixture_cases() -> tuple[list[dict[str, Any]], list[Finding]]:
    document, findings = _read_object(FIXTURE_CASES)
    if document is None:
        return [], findings

    bases = document.get("bases")
    cases = document.get("cases")
    if (
        document.get("profile") != "kfm.advisory-event-envelope.fixture-cases.v1"
        or not isinstance(bases, Mapping)
        or not isinstance(cases, list)
        or document.get("base_count") != len(bases)
        or document.get("case_count") != len(cases)
        or not bases
        or not cases
    ):
        return [], [Finding("FIXTURE_MANIFEST_INVALID", "/")]

    base_documents: dict[str, dict[str, Any]] = {}
    for base_name, base_ref in bases.items():
        if not isinstance(base_name, str) or not base_name or not isinstance(base_ref, str):
            return [], [Finding("FIXTURE_MANIFEST_INVALID", "/bases")]
        relative = Path(base_ref)
        if (
            relative.is_absolute()
            or ".." in relative.parts
            or relative.parts != ("bases", f"{base_name}.json")
        ):
            return [], [Finding("FIXTURE_BASE_FILE_INVALID", f"/bases/{base_name}")]
        base_path = FIXTURE_ROOT / relative
        try:
            base_path.relative_to(FIXTURE_BASES_ROOT)
        except ValueError:
            return [], [Finding("FIXTURE_BASE_FILE_INVALID", f"/bases/{base_name}")]
        base, base_findings = _read_object(base_path)
        if base is None or base_findings:
            return [], [Finding("FIXTURE_BASE_FILE_INVALID", f"/bases/{base_name}")]
        base_documents[base_name] = base

    materialized: list[dict[str, Any]] = []
    seen_names: set[str] = set()
    allowed_classes = {"valid", "invalid", "semantic_invalid"}
    for case_index, item in enumerate(cases):
        location = f"/cases/{case_index}"
        if not isinstance(item, Mapping):
            return [], [Finding("FIXTURE_CASE_INVALID", location)]
        name = item.get("name")
        case_class = item.get("class")
        expected_ok = item.get("expected_ok")
        expected_code = item.get("expected_code")
        base_name = item.get("base")
        patches = item.get("patches")
        if (
            not isinstance(name, str)
            or not name
            or name in seen_names
            or case_class not in allowed_classes
            or not isinstance(expected_ok, bool)
            or (expected_code is not None and not isinstance(expected_code, str))
            or not isinstance(base_name, str)
            or base_name not in bases
            or not isinstance(patches, list)
            or (case_class == "valid") != expected_ok
            or (expected_ok and expected_code is not None)
            or (not expected_ok and not expected_code)
        ):
            return [], [Finding("FIXTURE_CASE_INVALID", location)]

        envelope = copy.deepcopy(base_documents[base_name])
        if not isinstance(envelope, dict):
            return [], [Finding("FIXTURE_MANIFEST_INVALID", f"/bases/{base_name}")]
        for patch_index, patch in enumerate(patches):
            if not isinstance(patch, Mapping):
                return [], [
                    Finding(
                        "FIXTURE_PATCH_INVALID",
                        f"{location}/patches/{patch_index}",
                    )
                ]
            patch_finding = _apply_fixture_patch(
                envelope,
                patch,
                case_index=case_index,
                patch_index=patch_index,
            )
            if patch_finding is not None:
                return [], [patch_finding]

        seen_names.add(name)
        materialized.append(
            {
                "name": name,
                "class": case_class,
                "expected_ok": expected_ok,
                "expected_code": expected_code,
                "base": base_name,
                "patches": copy.deepcopy(patches),
                "envelope": envelope,
            }
        )
    return materialized, []


def load_fixture_cases() -> list[dict[str, Any]]:
    """Return materialized fixture cases or raise for malformed fixture metadata."""

    cases, findings = _materialize_fixture_cases()
    if findings:
        codes = ",".join(f"{finding.code}:{finding.path}" for finding in findings)
        raise ValueError(f"fixture manifest invalid: {codes}")
    return cases


def validate_fixture_polarity() -> tuple[bool, list[dict[str, Any]]]:
    cases, findings = _materialize_fixture_cases()
    if findings:
        result = ValidationResult(tuple(sorted(set(findings))))
        return False, [_render(FIXTURE_CASES, result)]

    rows: list[dict[str, Any]] = []
    ok = True
    for item in cases:
        result = validate_envelope_object(item["envelope"])
        rows.append(_render(f"case:{item['name']}", result))
        codes = {finding.code for finding in result.findings}
        case_ok = result.ok == item["expected_ok"]
        if item["expected_code"] is not None:
            case_ok = case_ok and item["expected_code"] in codes
        ok = ok and case_ok
    return ok, rows


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate fixture-only AdvisoryEventEnvelope records.")
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true", help="validate positive and negative fixture polarity")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        ok, rows = validate_fixture_polarity()
        print(json.dumps({"ok": ok, "cases": rows}, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if not args.paths:
        raise SystemExit("provide at least one path or use --fixtures")
    rows = [_render(path, validate_envelope(path)) for path in args.paths]
    ok = all(row["ok"] for row in rows)
    print(json.dumps({"ok": ok, "results": rows}, sort_keys=True, separators=(",", ":")))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

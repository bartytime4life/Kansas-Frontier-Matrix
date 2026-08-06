#!/usr/bin/env python3
"""Validate proposed renderer-neutral MapContextEnvelope records.

A passing result proves bounded fixture shape and local consistency only. It does
not resolve evidence, evaluate policy, authenticate review, establish release
state, authorize public use, or prove a deployed map/runtime path.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA_PATH = ROOT / "schemas/contracts/v1/ui/map_context_envelope.schema.json"
FIXTURE_ROOT = ROOT / "fixtures/ui/map_context_envelope"
CASE_PATH = FIXTURE_ROOT / "cases.json"
MAX_JSON_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 64
MAX_TTL_SECONDS = 15 * 60
SCOPE = "map-context-envelope-renderer-neutral-fixture-only"

_INTERNAL_PREFIXES = (
    "raw:",
    "work:",
    "quarantine:",
    "canonical:",
    "internal:",
    "proof:",
    "model:",
    "direct-model:",
)


class DuplicateKeyError(ValueError):
    """Raised when a parsed JSON object repeats a key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or infinity tokens."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _load_json_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        raw = path.read_bytes()
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (OSError, RecursionError, ValueError):
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1")
        for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        errors = sorted(
            _schema_validator().iter_errors(value),
            key=lambda error: (
                _pointer(error.absolute_path),
                str(error.validator),
            ),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _parse_utc(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed.astimezone(timezone.utc)


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _sorted_unique_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _identity_subject(value: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: copy.deepcopy(item)
        for key, item in value.items()
        if key not in {"envelope_id", "spec_hash"}
    }


def _identity_hash(value: Mapping[str, Any]) -> str:
    return compute_spec_hash(_identity_subject(value))


def _identity_id(value: Mapping[str, Any]) -> str:
    digest = _identity_hash(value).removeprefix("sha256:")
    return f"map-context-envelope:{digest[:24]}"


def _filter_sort_key(value: Any) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def _internal_ref(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    lowered = value.lower()
    return lowered.startswith(_INTERNAL_PREFIXES) or any(
        marker in lowered
        for marker in (
            "/raw/",
            "/work/",
            "/quarantine/",
            "/canonical/",
            "/internal/",
            "/proofs/",
            "/model-runtime/",
        )
    )


def _reference_values(value: Mapping[str, Any]) -> list[str]:
    refs: list[str] = []
    for item in _array(value.get("evidence_refs")):
        if isinstance(item, str):
            refs.append(item)
    for item in _array(value.get("release_refs")):
        if isinstance(item, str):
            refs.append(item)

    area = _mapping(value.get("area_scope"))
    geography_ref = area.get("geography_ref")
    if isinstance(geography_ref, str):
        refs.append(geography_ref)

    for layer in _array(value.get("layers")):
        if not isinstance(layer, dict):
            continue
        release_ref = layer.get("release_ref")
        if isinstance(release_ref, str):
            refs.append(release_ref)
        for item in _array(layer.get("evidence_refs")):
            if isinstance(item, str):
                refs.append(item)

    for selection in _array(value.get("selections")):
        if not isinstance(selection, dict):
            continue
        for item in _array(selection.get("evidence_refs")):
            if isinstance(item, str):
                refs.append(item)
    return refs


def _semantic_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    assembled = _parse_utc(value.get("assembled_at"))
    expires = _parse_utc(value.get("expires_at"))
    if assembled is not None and expires is not None:
        ttl = (expires - assembled).total_seconds()
        if ttl <= 0:
            findings.append(
                Finding("CONTEXT_TIME_ORDER_INVALID", "/expires_at")
            )
        elif ttl > MAX_TTL_SECONDS:
            findings.append(
                Finding("CONTEXT_TTL_EXCEEDED", "/expires_at")
            )

    window = _mapping(value.get("time_window"))
    start = _parse_utc(window.get("start"))
    end = _parse_utc(window.get("end"))
    if start is not None and end is not None:
        if start > end:
            findings.append(
                Finding("TIME_WINDOW_ORDER_INVALID", "/time_window")
            )
        if assembled is not None and end > assembled:
            findings.append(
                Finding("TIME_WINDOW_AFTER_ASSEMBLY", "/time_window/end")
            )

    layers = _array(value.get("layers"))
    layer_ids = [
        item.get("layer_id")
        for item in layers
        if isinstance(item, dict)
    ]
    if (
        len(layer_ids) != len(layers)
        or not all(isinstance(item, str) for item in layer_ids)
        or layer_ids != sorted(set(layer_ids))
    ):
        findings.append(Finding("LAYERS_NOT_CANONICAL", "/layers"))

    selections = _array(value.get("selections"))
    selection_keys = [
        (item.get("layer_id"), item.get("feature_id"))
        for item in selections
        if isinstance(item, dict)
    ]
    if (
        len(selection_keys) != len(selections)
        or not all(
            isinstance(layer_id, str) and isinstance(feature_id, str)
            for layer_id, feature_id in selection_keys
        )
        or selection_keys != sorted(set(selection_keys))
    ):
        findings.append(
            Finding("SELECTIONS_NOT_CANONICAL", "/selections")
        )

    filters = _array(value.get("filters"))
    filter_keys = [_filter_sort_key(item) for item in filters]
    if filter_keys != sorted(set(filter_keys)):
        findings.append(Finding("FILTERS_NOT_CANONICAL", "/filters"))

    ref_arrays: list[tuple[str, Any]] = [
        ("/evidence_refs", value.get("evidence_refs")),
        ("/release_refs", value.get("release_refs")),
    ]
    for index, layer in enumerate(layers):
        if isinstance(layer, dict):
            ref_arrays.append(
                (f"/layers/{index}/evidence_refs", layer.get("evidence_refs"))
            )
    for index, selection in enumerate(selections):
        if isinstance(selection, dict):
            ref_arrays.append(
                (
                    f"/selections/{index}/evidence_refs",
                    selection.get("evidence_refs"),
                )
            )
    if any(not _sorted_unique_strings(items) for _, items in ref_arrays):
        findings.append(Finding("REFS_NOT_CANONICAL", "/"))

    known_layers = {
        item
        for item in layer_ids
        if isinstance(item, str)
    }
    if any(
        isinstance(item, dict)
        and isinstance(item.get("layer_id"), str)
        and item["layer_id"] not in known_layers
        for item in selections
    ):
        findings.append(
            Finding("SELECTION_LAYER_UNRESOLVED", "/selections")
        )

    expected_releases = sorted(
        {
            item["release_ref"]
            for item in layers
            if isinstance(item, dict)
            and isinstance(item.get("release_ref"), str)
        }
    )
    if value.get("release_refs") != expected_releases:
        findings.append(
            Finding("RELEASE_UNION_MISMATCH", "/release_refs")
        )

    expected_evidence = sorted(
        {
            ref
            for item in [*layers, *selections]
            if isinstance(item, dict)
            for ref in _array(item.get("evidence_refs"))
            if isinstance(ref, str)
        }
    )
    if value.get("evidence_refs") != expected_evidence:
        findings.append(
            Finding("EVIDENCE_UNION_MISMATCH", "/evidence_refs")
        )

    if any(_internal_ref(item) for item in _reference_values(value)):
        findings.append(
            Finding("INTERNAL_REFERENCE_DENIED", "/")
        )

    area = _mapping(value.get("area_scope"))
    bbox = area.get("bbox")
    if (
        area.get("scope_type") == "VIEWPORT"
        and isinstance(bbox, list)
        and len(bbox) == 4
        and all(
            isinstance(item, (int, float)) and not isinstance(item, bool)
            for item in bbox
        )
        and not (bbox[0] < bbox[2] and bbox[1] < bbox[3])
    ):
        findings.append(
            Finding("BBOX_ORDER_INVALID", "/area_scope/bbox")
        )

    for index, item in enumerate(filters):
        if not isinstance(item, dict):
            continue
        operator = item.get("operator")
        values = _array(item.get("values"))
        valid_arity = (
            (operator == "EQ" and len(values) == 1)
            or (operator == "IN" and len(values) >= 1)
            or (operator == "BETWEEN" and len(values) == 2)
        )
        if not valid_arity:
            findings.append(
                Finding("FILTER_ARITY_INVALID", f"/filters/{index}/values")
            )

    expected_hash = _identity_hash(value)
    if value.get("spec_hash") != expected_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if value.get("envelope_id") != (
        "map-context-envelope:"
        + expected_hash.removeprefix("sha256:")[:24]
    ):
        findings.append(
            Finding("ENVELOPE_ID_MISMATCH", "/envelope_id")
        )

    return findings


def validate_value(value: Mapping[str, Any]) -> ValidationResult:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return ValidationResult(tuple(sorted(set(schema_findings))))
    findings = _semantic_findings(value)
    return ValidationResult(tuple(sorted(set(findings))))


def validate(path: Path) -> ValidationResult:
    value, findings = _load_json_object(path)
    if value is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_value(value)


def _navigate(root: Any, path: Sequence[Any]) -> tuple[Any, Any]:
    if not path:
        raise ValueError("patch path must not be empty")
    parent = root
    for part in path[:-1]:
        parent = parent[part]
    return parent, path[-1]


def _apply_patch(value: dict[str, Any], patch: Mapping[str, Any]) -> None:
    operation = patch.get("op")
    path = patch.get("path")
    if not isinstance(path, list):
        raise ValueError("patch path must be an array")
    parent, leaf = _navigate(value, path)
    if operation == "set":
        parent[leaf] = copy.deepcopy(patch.get("value"))
    elif operation == "delete":
        del parent[leaf]
    elif operation == "reverse":
        target = parent[leaf]
        if not isinstance(target, list):
            raise ValueError("reverse patch target must be an array")
        target.reverse()
    else:
        raise ValueError("unknown patch operation")


def _case_record(
    document: Mapping[str, Any],
    case: Mapping[str, Any],
) -> dict[str, Any]:
    base = case.get("base")
    if base not in {"viewport", "geography"}:
        raise ValueError("unknown fixture base")
    base_path = FIXTURE_ROOT / f"base_{base}.json"
    value = json.loads(base_path.read_text(encoding="utf-8"))
    for patch in _array(case.get("patches")):
        if not isinstance(patch, dict):
            raise ValueError("patch must be an object")
        _apply_patch(value, patch)
    if case.get("recompute_identity", True):
        value["spec_hash"] = _identity_hash(value)
        value["envelope_id"] = _identity_id(value)
    return value


def fixture_suite() -> tuple[bool, tuple[dict[str, Any], ...]]:
    document = json.loads(CASE_PATH.read_text(encoding="utf-8"))
    raw_cases = document.get("cases")
    if not isinstance(raw_cases, list) or not raw_cases:
        return False, ()
    rows: list[dict[str, Any]] = []
    all_match = True
    for case in raw_cases:
        if not isinstance(case, dict):
            all_match = False
            continue
        case_id = case.get("case_id")
        try:
            result = validate_value(_case_record(document, case))
            actual_findings = sorted({item.code for item in result.findings})
            actual_outcome = "PASS" if result.ok else "FAIL"
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError, KeyError, TypeError):
            actual_findings = ["FIXTURE_BUILD_ERROR"]
            actual_outcome = "FAIL"
        expected_findings = case.get("expected_findings")
        expected_outcome = case.get("expected_outcome")
        suite_match = (
            isinstance(case_id, str)
            and actual_findings == expected_findings
            and actual_outcome == expected_outcome
        )
        all_match = all_match and suite_match
        rows.append(
            {
                "case_id": case_id,
                "findings": actual_findings,
                "outcome": actual_outcome,
                "scope": SCOPE,
                "suite_match": suite_match,
            }
        )
    return all_match, tuple(rows)


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "field": item.field}
                for item in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate proposed renderer-neutral MapContextEnvelope records."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        passed, rows = fixture_suite()
        for row in rows:
            print(
                json.dumps(
                    row,
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
        return 0 if passed else 1

    if not args.files:
        parser.error("provide one or more files or use --fixtures")

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

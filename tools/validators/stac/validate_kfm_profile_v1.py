#!/usr/bin/env python3
"""Validate the draft KFM STAC trust-extension profile without network access.

This validator checks a bounded STAC 1.0.0 Item projection, deterministic
identity, and separation among catalog, receipt, proof, release, and publication
references. A PASS establishes only conformance to this draft profile. It does
not establish complete external STAC conformance, authenticate referenced
objects, admit a source, close evidence, approve policy or review, release,
publish, deploy, or permit public use.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages" / "hashing" / "src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))

try:
    from hashing import compute_spec_hash
except ImportError as exc:  # pragma: no cover - fail-closed hosted path
    _HASH_IMPORT_ERROR: Exception | None = exc
else:
    _HASH_IMPORT_ERROR = None

SCHEMA_PATH = ROOT / "schemas/contracts/v1/stac/kfm-profile-v1.schema.json"
FIXTURE_ROOT = ROOT / "fixtures/contracts/v1/stac/kfm-profile-v1"
MANIFEST_PATH = FIXTURE_ROOT / "fixture_manifest.json"
SCOPE = "kfm-stac-trust-extension-draft-v1"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
KFM_LINK_ORDER = {
    "kfm:receipt": 0,
    "kfm:proof": 1,
    "kfm:release": 2,
}
REFERENCE_FIELDS = {
    "kfm:run_receipt_ref": "kfm:receipt",
    "kfm:proof_ref": "kfm:proof",
    "kfm:release_ref": "kfm:release",
}
TRUST_DEPENDENCIES = {
    "UNRESOLVED": (False, False, False),
    "CATALOG_ONLY": (False, False, False),
    "RECEIPT_BOUND": (True, False, False),
    "PROOF_BOUND": (True, True, False),
    "RELEASE_LINKED": (True, True, True),
}
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_COMPLEXITY_LIMIT",
    "JSON_DUPLICATE_KEY",
    "JSON_INVALID",
    "JSON_NONFINITE_NUMBER",
    "JSON_NOT_UTF8",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON uses NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    """One stable, value-free finding."""

    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    """Finite result for one candidate file."""

    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
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
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _load_schema() -> Mapping[str, Any]:
    try:
        value = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("schema unavailable") from exc
    if not isinstance(value, Mapping):
        raise RuntimeError("schema root must be an object")
    Draft202012Validator.check_schema(value)
    return value


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        validator = Draft202012Validator(
            _load_schema(),
            format_checker=FormatChecker(),
        )
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, ValueError, RuntimeError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]

    errors = sorted(
        errors,
        key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
    )
    findings = [
        Finding("SCHEMA_INVALID", _pointer(item.absolute_path))
        for item in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    """Return the full Item with only properties.kfm:spec_hash omitted."""

    subject = copy.deepcopy(dict(candidate))
    properties = subject.get("properties")
    if not isinstance(properties, dict):
        raise ValueError("properties must be an object")
    properties.pop("kfm:spec_hash", None)
    return subject


def compute_item_spec_hash(candidate: Mapping[str, Any]) -> str:
    """Compute RFC 8785 JCS + SHA-256 over the declared identity subject."""

    if _HASH_IMPORT_ERROR is not None:
        raise RuntimeError("hashing package unavailable") from _HASH_IMPORT_ERROR
    return compute_spec_hash(identity_subject(candidate))


def _is_canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _kfm_links(candidate: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    links = candidate.get("links")
    if not isinstance(links, list):
        return []
    return [
        item
        for item in links
        if isinstance(item, Mapping) and item.get("rel") in KFM_LINK_ORDER
    ]


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    properties = candidate.get("properties")
    if not isinstance(properties, Mapping):
        return findings

    supplied_hash = properties.get("kfm:spec_hash")
    if isinstance(supplied_hash, str):
        try:
            expected_hash = compute_item_spec_hash(candidate)
        except (TypeError, ValueError, RuntimeError, RecursionError):
            expected_hash = None
        if expected_hash is None:
            findings.append(Finding("HASHING_UNAVAILABLE", "/properties/kfm:spec_hash"))
        elif supplied_hash != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/properties/kfm:spec_hash"))

    reason_codes = properties.get("kfm:reason_codes")
    if not _is_canonical_strings(reason_codes):
        findings.append(
            Finding("REASON_CODES_NOT_CANONICAL", "/properties/kfm:reason_codes")
        )

    extensions = candidate.get("stac_extensions")
    if not _is_canonical_strings(extensions):
        findings.append(Finding("EXTENSIONS_NOT_CANONICAL", "/stac_extensions"))

    refs = [
        properties.get("kfm:run_receipt_ref"),
        properties.get("kfm:proof_ref"),
        properties.get("kfm:release_ref"),
    ]
    present_refs = [item for item in refs if isinstance(item, str)]
    if len(present_refs) != len(set(present_refs)):
        findings.append(Finding("REFERENCE_ROLE_COLLAPSE", "/properties"))

    trust_class = properties.get("kfm:trust_class")
    expected = TRUST_DEPENDENCIES.get(trust_class)
    actual = tuple(isinstance(item, str) for item in refs)
    if expected is not None and actual != expected:
        findings.append(
            Finding("TRUST_CLASS_DEPENDENCY_MISMATCH", "/properties/kfm:trust_class")
        )

    catalog_state = properties.get("kfm:catalog_state")
    if trust_class == "UNRESOLVED" and catalog_state != "CANDIDATE":
        findings.append(
            Finding("CATALOG_STATE_INCONSISTENT", "/properties/kfm:catalog_state")
        )
    if trust_class in {"CATALOG_ONLY", "PROOF_BOUND", "RELEASE_LINKED"}:
        if catalog_state != "CATALOGED":
            findings.append(
                Finding("CATALOG_STATE_INCONSISTENT", "/properties/kfm:catalog_state")
            )

    release_ref = properties.get("kfm:release_ref")
    release_state = properties.get("kfm:release_state")
    if (release_state == "RELEASE_LINKED") != isinstance(release_ref, str):
        findings.append(
            Finding("RELEASE_STATE_INCONSISTENT", "/properties/kfm:release_state")
        )

    publication_state = properties.get("kfm:publication_state")
    if publication_state == "PUBLICATION_LINKED" and (
        not isinstance(release_ref, str) or release_state != "RELEASE_LINKED"
    ):
        findings.append(
            Finding(
                "PUBLICATION_STATE_INCONSISTENT",
                "/properties/kfm:publication_state",
            )
        )

    kfm_links = _kfm_links(candidate)
    link_keys = [
        (KFM_LINK_ORDER[str(item.get("rel"))], str(item.get("href")))
        for item in kfm_links
    ]
    if link_keys != sorted(set(link_keys)):
        findings.append(Finding("KFM_LINKS_NOT_CANONICAL", "/links"))

    by_relation: dict[str, list[str]] = {relation: [] for relation in KFM_LINK_ORDER}
    for item in kfm_links:
        relation = item.get("rel")
        href = item.get("href")
        if isinstance(relation, str) and isinstance(href, str):
            by_relation[relation].append(href)

    for field, relation in REFERENCE_FIELDS.items():
        ref = properties.get(field)
        hrefs = by_relation[relation]
        pointer = f"/properties/{field.replace('~', '~0').replace('/', '~1')}"
        if isinstance(ref, str):
            if hrefs != [ref]:
                findings.append(Finding("REFERENCE_LINK_MISMATCH", pointer))
        elif hrefs:
            findings.append(Finding("REFERENCE_LINK_ORPHANED", pointer))

    return findings


def _derive_outcome(findings: Sequence[Finding]) -> str:
    if any(item.code in ERROR_CODES or item.code == "HASHING_UNAVAILABLE" for item in findings):
        return "ERROR"
    if findings:
        return "FAIL"
    return "PASS"


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        ordered = tuple(sorted(set(findings)))
        return ValidationResult(_derive_outcome(ordered), ordered)

    schema_findings = _schema_findings(candidate)
    findings.extend(schema_findings)
    if not schema_findings:
        findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_derive_outcome(ordered), ordered)


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority_created": False,
            "file": _display_path(path),
            "findings": [
                {"code": item.code, "path": item.path} for item in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _load_manifest() -> Mapping[str, Any]:
    try:
        value = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, Mapping) else {}


def run_fixture_profile() -> int:
    manifest = _load_manifest()
    valid = manifest.get("valid")
    invalid = manifest.get("invalid")
    if not isinstance(valid, Mapping) or not isinstance(invalid, Mapping):
        return 1

    passed = True
    seen: set[str] = set()
    for group_name, group in (("valid", valid), ("invalid", invalid)):
        for filename, expected in sorted(group.items()):
            if not isinstance(filename, str) or not isinstance(expected, Mapping):
                passed = False
                continue
            path = FIXTURE_ROOT / group_name / filename
            result = validate_record(path)
            print(_serialize(path, result))
            actual_codes = sorted({item.code for item in result.findings})
            expected_codes = sorted(expected.get("findings", []))
            expected_outcome = expected.get("outcome")
            if result.outcome != expected_outcome or actual_codes != expected_codes:
                passed = False
                print(
                    json.dumps(
                        {
                            "actual": {
                                "findings": actual_codes,
                                "outcome": result.outcome,
                            },
                            "expected": {
                                "findings": expected_codes,
                                "outcome": expected_outcome,
                            },
                            "file": _display_path(path),
                            "outcome": "FIXTURE_POLARITY_ERROR",
                        },
                        sort_keys=True,
                        separators=(",", ":"),
                    ),
                    file=sys.stderr,
                )
            seen.add(f"{group_name}/{filename}")

    fixture_files = {
        path.relative_to(FIXTURE_ROOT).as_posix()
        for path in FIXTURE_ROOT.glob("*/*.json")
    }
    if fixture_files != seen:
        passed = False
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate the draft KFM STAC trust-extension profile."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        if args.files:
            print("--fixtures cannot be combined with file arguments", file=sys.stderr)
            return 2
        return run_fixture_profile()
    if not args.files:
        print("at least one file or --fixtures is required", file=sys.stderr)
        return 2

    exit_code = 0
    for path in args.files:
        result = validate_record(path)
        print(_serialize(path, result))
        if result.outcome == "ERROR":
            exit_code = max(exit_code, 2)
        elif result.outcome == "FAIL":
            exit_code = max(exit_code, 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

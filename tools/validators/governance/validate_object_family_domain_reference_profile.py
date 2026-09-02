#!/usr/bin/env python3
"""Validate fixture-only object-family/domain reference candidates.

A PASS proves bounded local consistency only. It does not assign an owner,
adopt a sensitivity default, mutate a register, authorize a cross-domain join,
evaluate policy, release data, or publish a surface.
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

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = (
    ROOT
    / "schemas/contracts/v1/governance/"
    "object_family_domain_reference_profile.schema.json"
)
FIXTURES = (
    ROOT
    / "fixtures/contracts/v1/governance/"
    "object_family_domain_reference_profile/cases.json"
)
DOMAIN_REGISTER = ROOT / "control_plane/domain_lane_register.yaml"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:object-family-domain-reference:"
_DENIED_REFERENCE_MARKERS = (
    "://",
    "data/raw",
    "data/work",
    "data/quarantine",
    "postgres",
    "neo4j",
    "s3:",
    "select ",
    "match (",
    "sparql ",
    "cypher",
)


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    profile_state: str | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("OBJECT_FAMILY_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("OBJECT_FAMILY_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("OBJECT_FAMILY_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("OBJECT_FAMILY_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("OBJECT_FAMILY_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("OBJECT_FAMILY_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("OBJECT_FAMILY_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("OBJECT_FAMILY_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"matrix_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def expected_summary(value: Mapping[str, Any]) -> dict[str, Any]:
    families = value["families"]
    domain_owned = sum(1 for family in families if family["owner"]["kind"] == "DOMAIN")
    return {
        "family_count": len(families),
        "domain_owned_count": domain_owned,
        "cross_cutting_count": len(families) - domain_owned,
        "profile_state": "REVIEW_REQUIRED",
        "canonical_register_written": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("OBJECT_FAMILY_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("OBJECT_FAMILY_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("OBJECT_FAMILY_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _domain_ids(repo_root: Path) -> tuple[set[str] | None, Finding | None]:
    path = repo_root / DOMAIN_REGISTER.relative_to(ROOT)
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
        entries = value["entries"]
        result = {
            entry["lane_id"]
            for entry in entries
            if isinstance(entry, Mapping) and isinstance(entry.get("lane_id"), str)
        }
    except (OSError, UnicodeError, yaml.YAMLError, KeyError, TypeError):
        return None, Finding("OBJECT_FAMILY_DOMAIN_REGISTER_UNAVAILABLE", "/source_snapshot/domain_lane_register_ref")
    return result, None


def _reference_findings(
    value: Mapping[str, Any], repo_root: Path, known_domains: set[str]
) -> set[Finding]:
    findings: set[Finding] = set()
    families = value["families"]
    family_ids = [family["family_id"] for family in families]
    if family_ids != sorted(family_ids):
        findings.add(Finding("OBJECT_FAMILY_ORDER_INVALID", "/families"))
    if len(family_ids) != len(set(family_ids)):
        findings.add(Finding("OBJECT_FAMILY_ID_DUPLICATE", "/families"))

    root = repo_root.resolve()
    for index, family in enumerate(families):
        base = f"/families/{index}"
        owner = family["owner"]
        owner_domain = owner["domain_id"]
        citing = family["citing_domain_ids"]
        if citing != sorted(citing):
            findings.add(Finding("OBJECT_FAMILY_CITING_ORDER_INVALID", base + "/citing_domain_ids"))
        if len(citing) != len(set(citing)):
            findings.add(Finding("OBJECT_FAMILY_CITING_DOMAIN_DUPLICATE", base + "/citing_domain_ids"))
        if owner_domain is not None and owner_domain not in known_domains:
            findings.add(Finding("OBJECT_FAMILY_OWNER_DOMAIN_UNKNOWN", base + "/owner/domain_id"))
        for citing_index, domain_id in enumerate(citing):
            if domain_id not in known_domains:
                findings.add(
                    Finding(
                        "OBJECT_FAMILY_CITING_DOMAIN_UNKNOWN",
                        f"{base}/citing_domain_ids/{citing_index}",
                    )
                )
        if owner_domain is not None and owner_domain in citing:
            findings.add(Finding("OBJECT_FAMILY_OWNER_CITED_AS_CONSUMER", base + "/citing_domain_ids"))

        contract_ref = owner["contract_ref"]
        lowered = contract_ref.casefold()
        if any(marker in lowered for marker in _DENIED_REFERENCE_MARKERS):
            findings.add(Finding("OBJECT_FAMILY_DIRECT_STORE_REFERENCE_DENIED", base + "/owner/contract_ref"))
        if not contract_ref.startswith("contracts/"):
            findings.add(Finding("OBJECT_FAMILY_CONTRACT_REFERENCE_OUTSIDE_CONTRACTS", base + "/owner/contract_ref"))
        candidate = repo_root / contract_ref
        try:
            resolved = candidate.resolve(strict=True)
        except OSError:
            findings.add(Finding("OBJECT_FAMILY_CONTRACT_REFERENCE_MISSING", base + "/owner/contract_ref"))
        else:
            if root not in resolved.parents or not resolved.is_file() or candidate.is_symlink():
                findings.add(Finding("OBJECT_FAMILY_CONTRACT_REFERENCE_UNSAFE", base + "/owner/contract_ref"))
    return findings


def validate_payload(
    value: Mapping[str, Any], *, repo_root: Path = ROOT, check_repository: bool = True
) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)

    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("OBJECT_FAMILY_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("OBJECT_FAMILY_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["matrix_id"] != expected_id:
            findings.add(Finding("OBJECT_FAMILY_ID_MISMATCH", "/matrix_id"))

    if value["summary"] != expected_summary(value):
        findings.add(Finding("OBJECT_FAMILY_SUMMARY_MISMATCH", "/summary"))

    if check_repository:
        known_domains, domain_finding = _domain_ids(repo_root)
        if domain_finding is not None:
            return Result("ERROR", None, (domain_finding,))
        assert known_domains is not None
        findings.update(_reference_findings(value, repo_root, known_domains))

    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    return Result("PASS", "REVIEW_REQUIRED", ())


def validate_file(path: Path, *, repo_root: Path = ROOT) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", None, findings)
    return validate_payload(value, repo_root=repo_root)


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = replacement
    else:
        cursor[last] = replacement


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if not case.get("preserve_summary", False):
        document["summary"] = expected_summary(document)
    document["spec_hash"], document["matrix_id"] = canonical_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "matrix_id_override" in case:
        document["matrix_id"] = case["matrix_id_override"]
    return document


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": finding.code, "path": finding.path} for finding in result.findings]
        if (
            result.outcome != case["expected_outcome"]
            or result.profile_state != case["expected_profile_state"]
            or actual != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_profile_state": case["expected_profile_state"],
                    "actual_profile_state": result.profile_state,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "authority": {
                "assigns_owner": False,
                "writes_register": False,
                "authorizes_cross_domain_mutation": False,
                "evaluates_sensitivity_policy": False,
                "authorizes_release": False,
                "publishes": False,
            },
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "profile_state": result.profile_state,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())

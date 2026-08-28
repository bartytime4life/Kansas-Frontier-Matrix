#!/usr/bin/env python3
"""Validate fixture-only renderer capability profile candidates.

A PASS proves declaration completeness only. It does not select, install,
execute, probe, admit, release, deploy, or publish a renderer. ABSTAIN means a
synthetic declaration is incomplete and no capability or fallback is inferred.
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

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/ui/renderer_capability_profile.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/ui/renderer_capability_profile/cases.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:renderer-capability:"
_DENIED_REFERENCE_MARKERS = (
    "://",
    "data/raw",
    "data/work",
    "data/quarantine",
    "postgres",
    "neo4j",
    "s3:",
    "npm:",
    "pip:",
    "select ",
    "match (",
    "sparql ",
    "cypher",
)
_ALLOWED_SURFACES = {
    "MAPLIBRE_GL_JS": {"BROWSER", "TEST"},
    "MAPLIBRE_NATIVE": {"NATIVE", "TEST"},
    "MAPLIBRE_RS": {"TEST"},
    "HEADLESS": {"SERVER", "TEST"},
}


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
            return None, (Finding("RENDERER_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("RENDERER_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("RENDERER_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("RENDERER_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("RENDERER_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("RENDERER_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("RENDERER_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("RENDERER_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"candidate_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def expected_compatibility(value: Mapping[str, Any]) -> dict[str, Any]:
    required = value["required_capabilities"]
    declared = set(value["declared_capabilities"])
    missing = sorted(capability for capability in required if capability not in declared)
    if not missing:
        state, disposition = "FULL", "SUBSTITUTE_CANDIDATE"
    elif len(missing) < len(required):
        state, disposition = "PARTIAL", "HOLD"
    else:
        state, disposition = "INCOMPATIBLE", "REJECT"
    return {
        "missing_capabilities": missing,
        "state": state,
        "disposition": disposition,
        "review_required": True,
        "production_selection_authorized": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("RENDERER_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("RENDERER_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("RENDERER_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _reference_findings(value: Mapping[str, Any], repo_root: Path) -> set[Finding]:
    findings: set[Finding] = set()
    contract_refs = value["contract_refs"]
    if contract_refs != sorted(contract_refs):
        findings.add(Finding("RENDERER_CONTRACT_REFERENCE_ORDER_INVALID", "/contract_refs"))
    if len(contract_refs) != len(set(contract_refs)):
        findings.add(Finding("RENDERER_CONTRACT_REFERENCE_DUPLICATE", "/contract_refs"))

    root = repo_root.resolve()
    for index, contract_ref in enumerate(contract_refs):
        path = f"/contract_refs/{index}"
        lowered = contract_ref.casefold()
        if any(marker in lowered for marker in _DENIED_REFERENCE_MARKERS):
            findings.add(Finding("RENDERER_DIRECT_REFERENCE_DENIED", path))
        candidate = repo_root / contract_ref
        try:
            resolved = candidate.resolve(strict=True)
        except OSError:
            findings.add(Finding("RENDERER_CONTRACT_REFERENCE_MISSING", path))
        else:
            if root not in resolved.parents or not resolved.is_file() or candidate.is_symlink():
                findings.add(Finding("RENDERER_CONTRACT_REFERENCE_UNSAFE", path))

    implementation_ref = value["renderer"]["implementation_ref"]
    if any(marker in implementation_ref.casefold() for marker in _DENIED_REFERENCE_MARKERS):
        findings.add(Finding("RENDERER_IMPLEMENTATION_REFERENCE_DENIED", "/renderer/implementation_ref"))
    return findings


def _semantic_findings(value: Mapping[str, Any], repo_root: Path) -> set[Finding]:
    findings = _reference_findings(value, repo_root)
    required = value["required_capabilities"]
    declared = value["declared_capabilities"]
    if required != sorted(required):
        findings.add(Finding("RENDERER_REQUIRED_CAPABILITY_ORDER_INVALID", "/required_capabilities"))
    if declared != sorted(declared):
        findings.add(Finding("RENDERER_DECLARED_CAPABILITY_ORDER_INVALID", "/declared_capabilities"))

    renderer = value["renderer"]
    kind = renderer["renderer_kind"]
    surface = renderer["runtime_surface"]
    if surface == "BROWSER" and kind != "MAPLIBRE_GL_JS":
        findings.add(Finding("RENDERER_BROWSER_RULE_VIOLATION", "/renderer/renderer_kind"))
    elif surface not in _ALLOWED_SURFACES[kind]:
        findings.add(Finding("RENDERER_RUNTIME_SURFACE_INVALID", "/renderer/runtime_surface"))

    if value["compatibility"] != expected_compatibility(value):
        findings.add(Finding("RENDERER_COMPATIBILITY_MISMATCH", "/compatibility"))
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
        findings.add(Finding("RENDERER_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("RENDERER_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["candidate_id"] != expected_id:
            findings.add(Finding("RENDERER_ID_MISMATCH", "/candidate_id"))

    if check_repository:
        findings.update(_semantic_findings(value, repo_root))
    elif value["compatibility"] != expected_compatibility(value):
        findings.add(Finding("RENDERER_COMPATIBILITY_MISMATCH", "/compatibility"))

    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    state = value["compatibility"]["state"]
    if state == "FULL":
        return Result("PASS", "REVIEW_REQUIRED", ())
    if state == "PARTIAL":
        return Result("ABSTAIN", "REVIEW_REQUIRED", ())
    return Result(
        "DENY",
        None,
        (Finding("RENDERER_CAPABILITY_SET_INCOMPATIBLE", "/declared_capabilities"),),
    )


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
    if not case.get("preserve_compatibility", False):
        document["compatibility"] = expected_compatibility(document)
    document["spec_hash"], document["candidate_id"] = canonical_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "candidate_id_override" in case:
        document["candidate_id"] = case["candidate_id_override"]
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
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
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
                "selects_renderer": False,
                "loads_renderer": False,
                "performs_runtime_probe": False,
                "reads_store": False,
                "evaluates_policy": False,
                "authorizes_release": False,
                "deploys": False,
                "publishes": False,
            },
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "path": item.path} for item in result.findings
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
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())

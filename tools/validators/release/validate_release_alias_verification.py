#!/usr/bin/env python3
"""Validate fixture-only ReleaseAliasVerification records."""
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
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/release/release_alias_verification.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/release/release_alias_verification/cases.json"
PREFIX = "kfm:release-alias-verification:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100


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


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
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
            return None, (Finding("ALIAS_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("ALIAS_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("ALIAS_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("ALIAS_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("ALIAS_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("ALIAS_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ALIAS_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"verification_id", "spec_hash"}}
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def transition_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    action = value["action"]
    observed = value["observed"]
    prior = value["expected_prior"]
    proposed = value["proposed"]
    findings: set[Finding] = set()

    if action == "INITIAL_BIND":
        initial_ok = (
            observed["state"] == "UNBOUND"
            and observed["target_release_ref"] is None
            and observed["target_manifest_digest"] is None
            and observed["target_spec_hash"] is None
            and observed["revision"] in {0, None}
            and prior["release_ref"] is None
            and prior["manifest_digest"] is None
            and prior["spec_hash"] is None
            and prior["revision"] in {0, None}
            and proposed["revision"] == 1
        )
        if not initial_ok:
            findings.add(Finding("ALIAS_INITIAL_STATE_INVALID", "/observed"))
    elif observed["state"] == "BOUND":
        expected = {
            "release_ref": observed["target_release_ref"],
            "manifest_digest": observed["target_manifest_digest"],
            "spec_hash": observed["target_spec_hash"],
            "revision": observed["revision"],
        }
        if prior != expected:
            findings.add(Finding("ALIAS_PRIOR_STATE_MISMATCH", "/expected_prior"))
        if observed["revision"] is None or proposed["revision"] != observed["revision"] + 1:
            findings.add(Finding("ALIAS_REVISION_NON_MONOTONIC", "/proposed/revision"))
        if (
            proposed["release_ref"] == observed["target_release_ref"]
            and (
                proposed["manifest_digest"] != observed["target_manifest_digest"]
                or proposed["spec_hash"] != observed["target_spec_hash"]
            )
        ):
            findings.add(Finding("ALIAS_TARGET_NOT_IMMUTABLE", "/proposed/release_ref"))

    if action == "CORRECTION" and proposed["correction_ref"] is None:
        findings.add(Finding("ALIAS_CORRECTION_REF_REQUIRED", "/proposed/correction_ref"))
    if action != "CORRECTION" and proposed["correction_ref"] is not None:
        findings.add(Finding("ALIAS_CORRECTION_REF_FORBIDDEN", "/proposed/correction_ref"))
    if proposed["rollback_ref"] is None:
        findings.add(Finding("ALIAS_ROLLBACK_REF_REQUIRED", "/proposed/rollback_ref"))
    return tuple(sorted(findings))


def recompute_result(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["evaluation_state"] == "ERROR" or value["observed"]["state"] == "ERROR":
        return {"outcome": "ERROR", "reason_codes": ["ALIAS_STATE_ERROR"]}
    if value["observed"]["state"] == "UNKNOWN":
        return {"outcome": "HOLD", "reason_codes": ["ALIAS_STATE_UNKNOWN"]}
    findings = transition_findings(value)
    if findings:
        return {"outcome": "DENY", "reason_codes": [finding.code for finding in findings]}
    return {"outcome": "READY", "reason_codes": ["ALIAS_TRANSITION_READY"]}


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("ALIAS_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("ALIAS_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("ALIAS_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("ALIAS_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("ALIAS_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["verification_id"] != expected_id:
            findings.add(Finding("ALIAS_ID_MISMATCH", "/verification_id"))
    if value["result"] != recompute_result(value):
        findings.add(Finding("ALIAS_RESULT_MISMATCH", "/result"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    result = value["result"]
    if result["outcome"] == "READY":
        return Result("PASS", ())
    if result["outcome"] == "HOLD":
        return Result("ABSTAIN", (Finding("ALIAS_STATE_UNKNOWN", "/result/outcome"),))
    if result["outcome"] == "DENY":
        return Result("DENY", tuple(Finding(code, _reason_path(code)) for code in result["reason_codes"]))
    return Result("ERROR", (Finding("ALIAS_STATE_ERROR", "/result/outcome"),))


def _reason_path(code: str) -> str:
    return {
        "ALIAS_PRIOR_STATE_MISMATCH": "/expected_prior",
        "ALIAS_INITIAL_STATE_INVALID": "/observed",
        "ALIAS_REVISION_NON_MONOTONIC": "/proposed/revision",
        "ALIAS_TARGET_NOT_IMMUTABLE": "/proposed/release_ref",
        "ALIAS_CORRECTION_REF_REQUIRED": "/proposed/correction_ref",
        "ALIAS_CORRECTION_REF_FORBIDDEN": "/proposed/correction_ref",
        "ALIAS_ROLLBACK_REF_REQUIRED": "/proposed/rollback_ref",
    }[code]


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["result"] = copy.deepcopy(case.get("result_override", recompute_result(document)))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["verification_id"] = case.get("verification_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    passed = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        match = result.outcome == case["expected_outcome"] and actual == case["expected_findings"]
        print(json.dumps({"case_id": case["case_id"], "outcome": result.outcome, "findings": actual, "suite_match": match}, sort_keys=True, separators=(",", ":")))
        passed = passed and match
    return 0 if passed else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "non_effects": [
                "no_alias_mutation",
                "no_release_issue",
                "no_cache_invalidation",
                "no_promotion",
                "no_deployment",
                "no_publication",
            ],
            "outcome": result.outcome,
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
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())

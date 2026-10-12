"""Validate the inactive, fixture-only Fauna tile field allowlist profile.

The validator compares synthetic encoded-property names with a candidate
LayerManifest public-field allowlist and the inactive domain policy profile.
It does not read or build tile bytes, inspect geometry or values, decide
policy or review, promote, release, deploy, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

import yaml
from jsonschema import Draft202012Validator
from yaml.nodes import MappingNode

REPO_ROOT = Path(__file__).resolve().parents[5]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/fauna/tile_field_allowlist.schema.json"
POLICY_PATH = REPO_ROOT / "policy/domains/fauna/tile_field_allowlist.yaml"
FIXTURE_PATH = REPO_ROOT / "fixtures/domains/fauna/layers/tile_field_allowlist_cases.json"
SCOPE = "domains.fauna.tile_field_allowlist.fixture"
PROFILE = "kfm.fauna.tile-field-allowlist.fixture.v1"
MAX_POLICY_BYTES = 65_536
MAX_JSON_BYTES = 1_048_576
FIELD_NAME = re.compile(r"^[a-z][a-z0-9_]{0,79}$")
AUTHORITY_KEYS = {
    "evidence_authority",
    "policy_decision_authority",
    "promotion_authority",
    "publication_authority",
    "public_use_authority",
    "release_authority",
    "review_authority",
}
CANDIDATE_KEYS = {
    "authority_claims",
    "encoded_fields",
    "exposure",
    "layer_manifest_public_field_allowlist",
    "object_type",
    "profile",
    "style_only_protection",
    "vector_format",
}


class DuplicateKeyError(ValueError):
    """Raised when JSON or YAML repeats a mapping key."""


class InputError(ValueError):
    """Raised when bounded local input cannot be evaluated safely."""


class StrictLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def _construct_mapping(loader: StrictLoader, node: MappingNode, deep: bool = False) -> dict[object, object]:
    loader.flatten_mapping(node)
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in result
        except TypeError as exc:
            raise InputError("unhashable YAML mapping key") from exc
        if duplicate:
            raise DuplicateKeyError(str(key))
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _json_pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _nonfinite(_value: str) -> object:
    raise InputError("non-finite JSON number")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise InputError("non-finite JSON number")
    return parsed


def _contains_surrogate(value: object, active: set[int] | None = None) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if not isinstance(value, (Mapping, list)):
        return False
    active = set() if active is None else active
    identity = id(value)
    if identity in active:
        raise InputError("recursive input")
    active.add(identity)
    try:
        if isinstance(value, Mapping):
            return any(
                _contains_surrogate(key, active) or _contains_surrogate(item, active)
                for key, item in value.items()
            )
        return any(_contains_surrogate(item, active) for item in value)
    finally:
        active.remove(identity)


def _read_bounded(path: Path, byte_limit: int) -> str:
    try:
        if path.is_symlink() or not path.is_file():
            raise InputError("input is not a regular file")
        if path.stat().st_size > byte_limit:
            raise InputError("input exceeds byte limit")
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise InputError("input cannot be read safely") from exc


def load_policy(path: Path = POLICY_PATH) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        value = yaml.load(_read_bounded(path, MAX_POLICY_BYTES), Loader=StrictLoader)
        if not isinstance(value, dict):
            return None, (Finding("POLICY_ROOT_NOT_OBJECT", "$"),)
        if _contains_surrogate(value):
            return None, (Finding("POLICY_UNPAIRED_SURROGATE", "$"),)
    except DuplicateKeyError:
        return None, (Finding("POLICY_DUPLICATE_KEY", "$"),)
    except (InputError, yaml.YAMLError, RecursionError, ValueError):
        return None, (Finding("POLICY_INPUT_INVALID", "$"),)
    return value, ()


def load_json_object(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        value = json.loads(
            _read_bounded(path, MAX_JSON_BYTES),
            object_pairs_hook=_json_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
        if not isinstance(value, dict):
            return None, (Finding("JSON_ROOT_NOT_OBJECT", "$"),)
        if _contains_surrogate(value):
            return None, (Finding("JSON_UNPAIRED_SURROGATE", "$"),)
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "$"),)
    except (InputError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("JSON_INPUT_INVALID", "$"),)
    return value, ()


def _load_schema() -> dict[str, Any]:
    value, findings = load_json_object(SCHEMA_PATH)
    if value is None or findings:
        raise InputError("canonical schema is unreadable")
    return value


def _json_path(parts: Sequence[object]) -> str:
    return "$" + "".join(
        f"[{part}]" if isinstance(part, int) else f".{part}" for part in parts
    )


def _schema_findings(policy: object) -> set[Finding]:
    try:
        validator = Draft202012Validator(_load_schema())
        errors = sorted(
            validator.iter_errors(policy),
            key=lambda error: (list(error.absolute_path), str(error.validator)),
        )
    except (InputError, OSError, json.JSONDecodeError, RecursionError):
        return {Finding("POLICY_SCHEMA_UNAVAILABLE", "$")}
    return {
        Finding("POLICY_SCHEMA_INVALID", _json_path(list(error.absolute_path)))
        for error in errors[:100]
    }


def _sorted_unique_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _compile_patterns(patterns: Sequence[str]) -> tuple[re.Pattern[str], ...] | None:
    try:
        return tuple(re.compile(pattern, flags=re.ASCII) for pattern in patterns)
    except re.error:
        return None


def validate_policy(policy: object) -> ValidationResult:
    findings = _schema_findings(policy)
    if findings or not isinstance(policy, dict):
        return ValidationResult("DENY", tuple(sorted(findings)))

    collection_paths = (
        "allowed_public_fields",
        "forbidden_exact_fields",
        "forbidden_field_patterns",
        "required_public_fields",
    )
    for name in collection_paths:
        if not _sorted_unique_strings(policy[name]):
            findings.add(Finding("POLICY_COLLECTION_NOT_SORTED_UNIQUE", f"$.{name}"))

    allowed = set(policy["allowed_public_fields"])
    required = set(policy["required_public_fields"])
    forbidden = set(policy["forbidden_exact_fields"])
    if not required <= allowed:
        findings.add(Finding("POLICY_REQUIRED_FIELD_NOT_ALLOWED", "$.required_public_fields"))
    if allowed & forbidden:
        findings.add(Finding("POLICY_ALLOWED_FIELD_FORBIDDEN", "$.allowed_public_fields"))

    compiled = _compile_patterns(policy["forbidden_field_patterns"])
    if compiled is None:
        findings.add(Finding("POLICY_REGEX_INVALID", "$.forbidden_field_patterns"))
    elif any(pattern.search(field) for pattern in compiled for field in allowed):
        findings.add(Finding("POLICY_ALLOWED_FIELD_MATCHES_DENY_PATTERN", "$.allowed_public_fields"))

    return ValidationResult("DENY" if findings else "PASS", tuple(sorted(findings)))


def _candidate_collection(candidate: Mapping[str, Any], name: str, findings: set[Finding]) -> set[str] | None:
    value = candidate.get(name)
    path = f"$.{name}"
    if (
        not isinstance(value, list)
        or not value
        or len(value) > 256
        or any(not isinstance(item, str) or FIELD_NAME.fullmatch(item) is None for item in value)
    ):
        findings.add(Finding("FIELD_COLLECTION_INVALID", path))
        return None
    if value != sorted(set(value)):
        findings.add(Finding("FIELD_COLLECTION_NOT_SORTED_UNIQUE", path))
        return None
    return set(value)


def evaluate_candidate(policy: Mapping[str, Any], candidate: object) -> ValidationResult:
    policy_result = validate_policy(policy)
    if policy_result.outcome != "PASS":
        return policy_result

    findings: set[Finding] = set()
    if not isinstance(candidate, dict) or set(candidate) != CANDIDATE_KEYS:
        return ValidationResult(
            "DENY",
            (Finding("CANDIDATE_SHAPE_INVALID", "$"),),
        )
    if candidate.get("object_type") != "FaunaTileFieldCandidate" or candidate.get("profile") != PROFILE:
        findings.add(Finding("CANDIDATE_SHAPE_INVALID", "$"))
    if candidate.get("vector_format") not in policy["applies_to"]["vector_formats"]:
        findings.add(Finding("VECTOR_FORMAT_OUT_OF_SCOPE", "$.vector_format"))
    if candidate.get("exposure") != policy["applies_to"]["exposure"]:
        findings.add(Finding("EXPOSURE_OUT_OF_SCOPE", "$.exposure"))
    if not isinstance(candidate.get("style_only_protection"), bool):
        findings.add(Finding("CANDIDATE_SHAPE_INVALID", "$.style_only_protection"))
    elif candidate["style_only_protection"]:
        findings.add(Finding("STYLE_ONLY_PROTECTION_FORBIDDEN", "$.style_only_protection"))

    authority = candidate.get("authority_claims")
    if (
        not isinstance(authority, dict)
        or set(authority) != AUTHORITY_KEYS
        or any(value is not False for value in authority.values())
    ):
        findings.add(Finding("AUTHORITY_CLAIM_FORBIDDEN", "$.authority_claims"))

    encoded = _candidate_collection(candidate, "encoded_fields", findings)
    manifest = _candidate_collection(
        candidate,
        "layer_manifest_public_field_allowlist",
        findings,
    )
    if encoded is None or manifest is None:
        return ValidationResult("DENY", tuple(sorted(findings)))

    allowed = set(policy["allowed_public_fields"])
    required = set(policy["required_public_fields"])
    forbidden = set(policy["forbidden_exact_fields"])
    patterns = _compile_patterns(policy["forbidden_field_patterns"])
    assert patterns is not None

    for field in sorted(encoded | manifest):
        if field in forbidden or any(pattern.search(field) for pattern in patterns):
            findings.add(Finding("FORBIDDEN_FIELD_DECLARED", f"$.fields.{field}"))
    for field in sorted(encoded - allowed):
        findings.add(Finding("ENCODED_FIELD_NOT_POLICY_ALLOWLISTED", f"$.encoded_fields.{field}"))
    for field in sorted(manifest - allowed):
        findings.add(
            Finding(
                "LAYER_MANIFEST_FIELD_NOT_POLICY_ALLOWLISTED",
                f"$.layer_manifest_public_field_allowlist.{field}",
            )
        )
    for field in sorted(encoded - manifest):
        findings.add(Finding("ENCODED_FIELD_NOT_IN_LAYER_MANIFEST", f"$.encoded_fields.{field}"))
    for field in sorted(required - encoded):
        findings.add(Finding("REQUIRED_PUBLIC_FIELD_MISSING", f"$.encoded_fields.{field}"))
    for field in sorted(required - manifest):
        findings.add(
            Finding(
                "REQUIRED_PUBLIC_FIELD_NOT_IN_LAYER_MANIFEST",
                f"$.layer_manifest_public_field_allowlist.{field}",
            )
        )

    return ValidationResult("DENY" if findings else "PASS", tuple(sorted(findings)))


def run_fixture_suite(
    policy: Mapping[str, Any] | None = None,
    fixture_path: Path = FIXTURE_PATH,
) -> tuple[bool, dict[str, object]]:
    if policy is None:
        loaded, load_findings = load_policy()
        if loaded is None or load_findings:
            return False, {
                "authority": "NONE",
                "cases": [],
                "findings": [finding.code for finding in load_findings],
                "ok": False,
                "outcome": "ERROR",
                "scope": SCOPE,
            }
        policy = loaded
    policy_result = validate_policy(policy)
    suite, suite_findings = load_json_object(fixture_path)
    if policy_result.outcome != "PASS" or suite is None or suite_findings:
        codes = policy_result.codes + [finding.code for finding in suite_findings]
        return False, {
            "authority": "NONE",
            "cases": [],
            "findings": sorted(set(codes)),
            "ok": False,
            "outcome": "ERROR" if suite is None else "DENY",
            "scope": SCOPE,
        }
    if set(suite) != {"cases", "profile"} or suite.get("profile") != PROFILE or not isinstance(suite.get("cases"), list):
        return False, {
            "authority": "NONE",
            "cases": [],
            "findings": ["FIXTURE_SUITE_SHAPE_INVALID"],
            "ok": False,
            "outcome": "ERROR",
            "scope": SCOPE,
        }

    replay: list[dict[str, object]] = []
    ok = bool(suite["cases"])
    seen_ids: set[str] = set()
    for entry in suite["cases"]:
        case_ok = False
        if isinstance(entry, dict) and set(entry) == {"candidate", "case_id", "expected"}:
            case_id = entry.get("case_id")
            expected = entry.get("expected")
            if (
                isinstance(case_id, str)
                and re.fullmatch(r"[a-z][a-z0-9_]{2,79}", case_id)
                and case_id not in seen_ids
                and isinstance(expected, dict)
                and set(expected) == {"finding_codes", "outcome"}
                and _sorted_unique_strings(expected.get("finding_codes"))
            ):
                seen_ids.add(case_id)
                result = evaluate_candidate(policy, entry.get("candidate"))
                actual_codes = result.codes
                case_ok = result.outcome == expected.get("outcome") and actual_codes == expected.get("finding_codes")
                replay.append(
                    {
                        "actual_findings": actual_codes,
                        "actual_outcome": result.outcome,
                        "case_id": case_id,
                        "expected_findings": expected.get("finding_codes"),
                        "expected_outcome": expected.get("outcome"),
                        "ok": case_ok,
                    }
                )
        if not case_ok and not (
            isinstance(entry, dict)
            and isinstance(entry.get("case_id"), str)
            and any(item.get("case_id") == entry.get("case_id") for item in replay)
        ):
            replay.append({"case_id": entry.get("case_id") if isinstance(entry, dict) else None, "ok": False})
        ok = ok and case_ok

    return ok, {
        "authority": "NONE",
        "cases": replay,
        "findings": [] if ok else ["FIXTURE_REPLAY_MISMATCH"],
        "ok": ok,
        "outcome": "PASS" if ok else "ERROR",
        "scope": SCOPE,
    }


def _result_payload(result: ValidationResult) -> dict[str, object]:
    return {
        "authority": "NONE",
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "outcome": result.outcome,
        "scope": SCOPE,
    }


def _print(payload: object) -> None:
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--candidate", type=Path)
    mode.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    policy, load_findings = load_policy(args.policy)
    if policy is None or load_findings:
        _print(
            _result_payload(
                ValidationResult("ERROR", tuple(sorted(load_findings)))
            )
        )
        return 2
    policy_result = validate_policy(policy)
    if policy_result.outcome != "PASS":
        _print(_result_payload(policy_result))
        return 1

    if args.fixtures:
        ok, report = run_fixture_suite(policy)
        _print(report)
        return 0 if ok else 1
    if args.candidate is not None:
        candidate, candidate_findings = load_json_object(args.candidate)
        if candidate is None or candidate_findings:
            result = ValidationResult("ERROR", tuple(sorted(candidate_findings)))
        else:
            result = evaluate_candidate(policy, candidate)
        _print(_result_payload(result))
        return 0 if result.outcome == "PASS" else (2 if result.outcome == "ERROR" else 1)

    _print(_result_payload(policy_result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

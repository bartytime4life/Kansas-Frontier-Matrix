"""Validate the proposed public-safe StoryNode projection.

The validator is deterministic, fixture-first, bounded, and no-network. It
checks the closed Draft 2020-12 schema plus finite trust-inheritance rules.
A pass does not establish evidence truth, citation validity, policy approval,
review authority, release state, correction authenticity, publication, or
public-use permission.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/ui/story_node.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/ui/story_node"
EXPECTED_MANIFEST = FIXTURES_ROOT / "expected_findings_manifest.json"
MAX_JSON_BYTES = 256 * 1024
MAX_SCHEMA_FINDINGS = 50

REF_FIELDS = (
    "evidence_bundle_refs",
    "citation_validation_refs",
    "policy_decision_refs",
    "release_refs",
    "review_refs",
    "correction_refs",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _load_json(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/", "symbolic links are denied")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/", "input is not a regular file")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/", "input exceeds 256 KiB")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/", "duplicate object member")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/", "numbers must be finite")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/", "input is not valid JSON")]
    except (OSError, UnicodeError, RecursionError, ValueError):
        return None, [Finding("INPUT_UNREADABLE", "/", "input could not be read safely")]
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/", "root must be an object")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(payload: Mapping[str, object]) -> list[Finding]:
    errors = list(islice(_schema_validator().iter_errors(payload), MAX_SCHEMA_FINDINGS + 1))
    errors = sorted(errors, key=lambda item: (_pointer(item.absolute_path), str(item.validator)))
    findings = [
        Finding(
            "SCHEMA_INVALID",
            _pointer(error.absolute_path),
            f"schema constraint failed: {error.validator}",
        )
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/", "schema findings truncated"))
    return findings


def _support(payload: Mapping[str, object]) -> dict[str, list[str] | str]:
    raw = payload.get("support")
    if not isinstance(raw, dict):
        return {}
    support: dict[str, list[str] | str] = {}
    for field in REF_FIELDS:
        value = raw.get(field)
        support[field] = [item for item in value if isinstance(item, str)] if isinstance(value, list) else []
    rollback = raw.get("rollback_ref")
    if isinstance(rollback, str):
        support["rollback_ref"] = rollback
    return support


def _refs(support: Mapping[str, object], field: str) -> list[str]:
    value = support.get(field)
    return [item for item in value if isinstance(item, str)] if isinstance(value, list) else []


def _has_any_support(support: Mapping[str, object], *, include_policy: bool = True) -> bool:
    fields = REF_FIELDS if include_policy else tuple(item for item in REF_FIELDS if item != "policy_decision_refs")
    return any(_refs(support, field) for field in fields) or isinstance(support.get("rollback_ref"), str)


def _semantic_findings(payload: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    state = payload.get("state")
    outcome = payload.get("outcome")
    reason = payload.get("reason_code")
    body_ref = payload.get("body_ref")
    node_id = payload.get("id")
    trust = payload.get("trust_state")
    trust_map = trust if isinstance(trust, dict) else {}
    support = _support(payload)
    supersession = payload.get("supersession")
    supersession_map = supersession if isinstance(supersession, dict) else {}

    expected_outcome = {
        "READY": "ANSWER",
        "PARTIAL": "ABSTAIN",
        "ABSTAINED": "ABSTAIN",
        "BLOCKED": "DENY",
        "ERROR": "ERROR",
        "SUPERSEDED": "ABSTAIN",
    }.get(state)
    if expected_outcome is not None and outcome != expected_outcome:
        findings.append(
            Finding("STATE_OUTCOME_MISMATCH", "/outcome", "node state requires its finite outcome")
        )

    if state != "READY" and isinstance(body_ref, str):
        findings.append(
            Finding("NONREADY_BODY_REF_DENIED", "/body_ref", "non-ready nodes cannot expose governed body content")
        )

    citations = _refs(support, "citation_validation_refs")
    evidence = _refs(support, "evidence_bundle_refs")
    if citations and not evidence:
        findings.append(
            Finding("CITATION_WITHOUT_EVIDENCE", "/support/citation_validation_refs", "citations require evidence references")
        )

    correction_refs = _refs(support, "correction_refs")
    correction_state = trust_map.get("correction")
    if correction_state == "CORRECTED" and not correction_refs:
        findings.append(
            Finding("CORRECTED_REFS_REQUIRED", "/support/correction_refs", "corrected nodes require correction references")
        )
    if correction_refs and correction_state not in {"CORRECTED", "SUPERSEDED"}:
        findings.append(
            Finding("CORRECTION_STATE_MISMATCH", "/trust_state/correction", "correction references require corrected or superseded state")
        )
    if isinstance(support.get("rollback_ref"), str) and correction_state not in {"CORRECTED", "SUPERSEDED"}:
        findings.append(
            Finding("ROLLBACK_STATE_MISMATCH", "/support/rollback_ref", "rollback reference requires correction lineage")
        )

    if state == "READY":
        if reason != "SUPPORTED":
            findings.append(Finding("READY_REASON_INVALID", "/reason_code", "ready node requires SUPPORTED"))
        if not isinstance(body_ref, str):
            findings.append(Finding("READY_BODY_REF_REQUIRED", "/body_ref", "ready node requires governed body reference"))
        required_refs = {
            "evidence_bundle_refs": "READY_EVIDENCE_REQUIRED",
            "citation_validation_refs": "READY_CITATION_REQUIRED",
            "policy_decision_refs": "READY_POLICY_REF_REQUIRED",
            "release_refs": "READY_RELEASE_REF_REQUIRED",
            "review_refs": "READY_REVIEW_REF_REQUIRED",
        }
        for field, code in required_refs.items():
            if not _refs(support, field):
                findings.append(Finding(code, f"/support/{field}", "ready node requires governed support"))
        expected = {
            "policy": "ALLOW",
            "review": "REVIEWED",
            "release": "RELEASED",
            "freshness": "CURRENT",
        }
        for key, value in expected.items():
            if trust_map.get(key) != value:
                findings.append(
                    Finding("READY_TRUST_STATE_INVALID", f"/trust_state/{key}", "ready trust state is not release-safe")
                )
        if trust_map.get("rights") not in {"CLEARED", "GENERALIZED"}:
            findings.append(
                Finding("READY_RIGHTS_INVALID", "/trust_state/rights", "ready node requires cleared or generalized rights")
            )
        if trust_map.get("sensitivity") not in {"PUBLIC", "GENERALIZED"}:
            findings.append(
                Finding("READY_SENSITIVITY_INVALID", "/trust_state/sensitivity", "ready node requires public-safe sensitivity")
            )
        if supersession_map:
            findings.append(
                Finding("READY_SUPERSESSION_DENIED", "/supersession", "ready node cannot be superseded")
            )

    elif state == "PARTIAL":
        if reason not in {"PARTIAL_SUPPORT", "MISSING_EVIDENCE", "STALE_EVIDENCE", "CITATION_UNRESOLVED"}:
            findings.append(
                Finding("PARTIAL_REASON_INVALID", "/reason_code", "partial node requires a partial-support reason")
            )
        if trust_map.get("policy") != "ABSTAIN":
            findings.append(
                Finding("PARTIAL_POLICY_INVALID", "/trust_state/policy", "partial node requires ABSTAIN policy")
            )
        if supersession_map:
            findings.append(
                Finding("PARTIAL_SUPERSESSION_DENIED", "/supersession", "partial node cannot carry supersession")
            )

    elif state == "ABSTAINED":
        if reason not in {"MISSING_EVIDENCE", "STALE_EVIDENCE", "CITATION_UNRESOLVED", "RELEASE_UNAVAILABLE"}:
            findings.append(
                Finding("ABSTAIN_REASON_INVALID", "/reason_code", "abstained node requires a bounded abstention reason")
            )
        if trust_map.get("policy") != "ABSTAIN":
            findings.append(
                Finding("ABSTAIN_POLICY_INVALID", "/trust_state/policy", "abstained node requires ABSTAIN policy")
            )
        if evidence or citations:
            findings.append(
                Finding("ABSTAIN_CURRENT_SUPPORT_DENIED", "/support", "abstained node cannot expose current evidence or citations")
            )
        if supersession_map:
            findings.append(
                Finding("ABSTAIN_SUPERSESSION_DENIED", "/supersession", "use SUPERSEDED state for replacement lineage")
            )

    elif state == "BLOCKED":
        if reason not in {"POLICY_DENIED", "RIGHTS_UNRESOLVED", "SENSITIVE_DETAIL_RESTRICTED"}:
            findings.append(
                Finding("BLOCKED_REASON_INVALID", "/reason_code", "blocked node requires a denial reason")
            )
        if trust_map.get("policy") != "DENY":
            findings.append(
                Finding("BLOCKED_POLICY_INVALID", "/trust_state/policy", "blocked node requires DENY policy")
            )
        if _has_any_support(support, include_policy=False):
            findings.append(
                Finding("BLOCKED_SUPPORT_LEAK", "/support", "blocked node cannot expose evidence, release, review, correction, or rollback support")
            )
        if reason == "RIGHTS_UNRESOLVED" and trust_map.get("rights") != "UNRESOLVED":
            findings.append(
                Finding("RIGHTS_REASON_STATE_MISMATCH", "/trust_state/rights", "rights denial requires unresolved rights")
            )
        if reason == "SENSITIVE_DETAIL_RESTRICTED" and (
            trust_map.get("sensitivity") not in {"RESTRICTED", "UNKNOWN"}
            and trust_map.get("rights") != "WITHHELD"
        ):
            findings.append(
                Finding("SENSITIVITY_REASON_STATE_MISMATCH", "/trust_state/sensitivity", "sensitive denial requires restricted posture")
            )
        if supersession_map:
            findings.append(
                Finding("BLOCKED_SUPERSESSION_DENIED", "/supersession", "blocked node cannot carry supersession")
            )

    elif state == "ERROR":
        if reason != "UPSTREAM_ERROR":
            findings.append(
                Finding("ERROR_REASON_INVALID", "/reason_code", "error node requires UPSTREAM_ERROR")
            )
        if trust_map.get("policy") != "ERROR":
            findings.append(
                Finding("ERROR_POLICY_INVALID", "/trust_state/policy", "error node requires ERROR policy")
            )
        if _has_any_support(support):
            findings.append(
                Finding("ERROR_SUPPORT_LEAK", "/support", "error node cannot expose governed support")
            )
        if supersession_map:
            findings.append(
                Finding("ERROR_SUPERSESSION_DENIED", "/supersession", "error node cannot carry supersession")
            )

    elif state == "SUPERSEDED":
        if reason != "SUPERSEDED":
            findings.append(
                Finding("SUPERSEDED_REASON_INVALID", "/reason_code", "superseded node requires SUPERSEDED reason")
            )
        expected = {"policy": "ABSTAIN", "release": "WITHDRAWN", "correction": "SUPERSEDED"}
        for key, value in expected.items():
            if trust_map.get(key) != value:
                findings.append(
                    Finding("SUPERSEDED_TRUST_STATE_INVALID", f"/trust_state/{key}", "superseded node trust state is invalid")
                )
        if not correction_refs:
            findings.append(
                Finding("SUPERSEDED_CORRECTION_REQUIRED", "/support/correction_refs", "superseded node requires correction reference")
            )
        disallowed = (
            _refs(support, "evidence_bundle_refs")
            + _refs(support, "citation_validation_refs")
            + _refs(support, "release_refs")
            + _refs(support, "review_refs")
        )
        if disallowed or isinstance(support.get("rollback_ref"), str):
            findings.append(
                Finding("SUPERSEDED_SUPPORT_LEAK", "/support", "superseded node cannot expose prior support")
            )
        replacement = supersession_map.get("superseded_by")
        if not supersession_map:
            findings.append(
                Finding("SUPERSESSION_RECORD_REQUIRED", "/supersession", "superseded node requires replacement record")
            )
        elif replacement == node_id:
            findings.append(
                Finding("SUPERSESSION_SELF_REFERENCE", "/supersession/superseded_by", "replacement node must differ")
            )

    if trust_map.get("rights") == "UNRESOLVED" and not (
        state == "BLOCKED" and reason == "RIGHTS_UNRESOLVED"
    ):
        findings.append(
            Finding("UNRESOLVED_RIGHTS_FAIL_CLOSED", "/trust_state/rights", "unresolved rights require blocked denial")
        )
    if trust_map.get("release") == "UNRELEASED" and state == "READY":
        findings.append(
            Finding("UNRELEASED_READY_DENIED", "/trust_state/release", "unreleased node cannot be ready")
        )
    if trust_map.get("release") == "WITHDRAWN" and state != "SUPERSEDED":
        findings.append(
            Finding("WITHDRAWN_STATE_INVALID", "/trust_state/release", "withdrawn node must be superseded")
        )
    if trust_map.get("review") == "PENDING" and state == "READY":
        findings.append(
            Finding("PENDING_REVIEW_READY_DENIED", "/trust_state/review", "pending review cannot be ready")
        )
    if trust_map.get("freshness") == "STALE" and state == "READY":
        findings.append(
            Finding("STALE_READY_DENIED", "/trust_state/freshness", "stale node cannot be ready")
        )

    return findings


def validate_payload(path: Path) -> tuple[Finding, ...]:
    payload, findings = _load_json(path)
    if payload is None:
        return tuple(sorted(findings))
    schema_findings = _schema_findings(payload)
    if schema_findings:
        return tuple(sorted(set(schema_findings)))
    return tuple(sorted(set(_semantic_findings(payload))))


def _load_expected_manifest() -> dict[str, object]:
    value, findings = _load_json(EXPECTED_MANIFEST)
    if value is None or findings:
        raise ValueError("expected findings manifest is invalid")
    return value


def run_fixtures() -> int:
    try:
        manifest = _load_expected_manifest()
    except ValueError:
        print("STORY_NODE_FIXTURES_ERROR expected findings manifest is invalid")
        return 2

    valid_names = manifest.get("valid")
    invalid_map = manifest.get("invalid")
    if not isinstance(valid_names, list) or not valid_names or not isinstance(invalid_map, dict) or not invalid_map:
        print("STORY_NODE_FIXTURES_ERROR nonempty valid and invalid lanes are required")
        return 2

    failures: list[str] = []
    for name in valid_names:
        if not isinstance(name, str):
            failures.append("valid/<non-string>")
            continue
        path = FIXTURES_ROOT / "valid" / name
        if validate_payload(path):
            failures.append(f"valid/{name}")

    for name, expected in sorted(invalid_map.items()):
        if not isinstance(name, str) or not isinstance(expected, list):
            failures.append(f"invalid/{name}")
            continue
        path = FIXTURES_ROOT / "semantic_invalid" / name
        actual = {item.code for item in validate_payload(path)}
        expected_codes = {item for item in expected if isinstance(item, str)}
        if actual != expected_codes:
            failures.append(f"semantic_invalid/{name}")

    if failures:
        for name in failures:
            print(f"STORY_NODE_FIXTURE_POLARITY_FAIL file={name}")
        return 1

    print(
        "STORY_NODE_FIXTURES_VALID "
        f"valid={len(valid_names)} invalid={len(invalid_map)} "
        "no_network=true projection_only=true authority=false"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("payload", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.payload is not None:
            raise SystemExit("--fixtures cannot be combined with a payload")
        return run_fixtures()
    if args.payload is None:
        raise SystemExit("payload is required unless --fixtures is used")
    findings = validate_payload(args.payload)
    if not findings:
        print(f"STORY_NODE_VALID file={args.payload.name}")
        return 0
    for finding in findings:
        print(
            "STORY_NODE_INVALID "
            f"code={finding.code} field={finding.field} detail={finding.detail}"
        )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

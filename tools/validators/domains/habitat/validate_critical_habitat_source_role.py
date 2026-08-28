#!/usr/bin/env python3
"""Validate a fixture-only Habitat critical-habitat source-role candidate.

This validator proves only that a synthetic candidate keeps regulatory critical
habitat and modeled habitat in separate source-role and claim lanes. A pass
does not verify an official source descriptor, rights, sensitivity, evidence,
policy, review, release, publication, or public-use readiness.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


PROFILE = "kfm.habitat.critical-habitat-source-role.v1"
MAX_BYTES = 1_000_000
MAX_DEPTH = 32
MAX_NODES = 2_048

EXPECTED_PAIRINGS = {
    "REGULATORY_CRITICAL_HABITAT": ("REGULATORY", "DESIGNATION_CONTEXT"),
    "MODELED_HABITAT": ("MODELED", "SUITABILITY_MODEL"),
}
ALLOWED_KEYS = frozenset(
    {
        "candidate_id",
        "claim_kind",
        "evidence_refs",
        "feature_kind",
        "governance",
        "profile",
        "public_use_requested",
        "source_descriptor_ref",
        "source_role",
        "status",
    }
)
REQUIRED_KEYS = ALLOWED_KEYS
GOVERNANCE_KEYS = frozenset(
    {
        "authority_created",
        "evidence_closure_claimed",
        "policy_evaluated",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
        "release_ref",
    }
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_constant(value: str) -> None:
    raise NonFiniteNumberError(value)


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError(value)
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("HABITAT_ROLE_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("HABITAT_ROLE_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("HABITAT_ROLE_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except UnicodeDecodeError:
        return None, (Finding("HABITAT_ROLE_JSON_NOT_UTF8", "/"),)
    except DuplicateKeyError:
        return None, (Finding("HABITAT_ROLE_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("HABITAT_ROLE_JSON_NONFINITE_NUMBER", "/"),)
    except json.JSONDecodeError:
        return None, (Finding("HABITAT_ROLE_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("HABITAT_ROLE_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("HABITAT_ROLE_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _bounded(value: object) -> bool:
    pending: list[tuple[object, int]] = [(value, 0)]
    seen: set[int] = set()
    nodes = 0
    while pending:
        item, depth = pending.pop()
        nodes += 1
        if nodes > MAX_NODES or depth > MAX_DEPTH:
            return False
        if isinstance(item, (dict, list)):
            marker = id(item)
            if marker in seen:
                return False
            seen.add(marker)
        if isinstance(item, dict):
            pending.extend((child, depth + 1) for child in item.values())
        elif isinstance(item, list):
            pending.extend((child, depth + 1) for child in item)
    return True


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _ref_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and len(value) <= 32
        and all(_nonempty_string(item) for item in value)
        and value == sorted(set(value))
    )


def validate_payload(payload: object) -> Result:
    """Return deterministic anti-collapse findings for one synthetic candidate."""
    findings: list[Finding] = []
    if not isinstance(payload, Mapping):
        return Result("DENY", (Finding("HABITAT_ROLE_ROOT_NOT_OBJECT", "/"),))
    if not _bounded(payload):
        return Result(
            "DENY",
            (Finding("HABITAT_ROLE_DOCUMENT_BOUNDS_EXCEEDED", "/"),),
        )

    keys = set(payload)
    findings.extend(
        Finding("HABITAT_ROLE_FIELD_MISSING", f"/{key}")
        for key in sorted(REQUIRED_KEYS - keys)
    )
    findings.extend(
        Finding("HABITAT_ROLE_FIELD_UNEXPECTED", f"/{key}")
        for key in sorted(keys - ALLOWED_KEYS)
    )

    if payload.get("profile") != PROFILE:
        findings.append(Finding("HABITAT_ROLE_PROFILE_INVALID", "/profile"))
    if payload.get("status") != "PROPOSED_INACTIVE":
        findings.append(Finding("HABITAT_ROLE_STATUS_INVALID", "/status"))
    if not _nonempty_string(payload.get("candidate_id")):
        findings.append(
            Finding("HABITAT_ROLE_CANDIDATE_ID_INVALID", "/candidate_id")
        )
    if not _nonempty_string(payload.get("source_descriptor_ref")):
        findings.append(
            Finding("HABITAT_ROLE_SOURCE_REF_MISSING", "/source_descriptor_ref")
        )
    if not _ref_list(payload.get("evidence_refs")):
        findings.append(
            Finding("HABITAT_ROLE_EVIDENCE_REFS_INVALID", "/evidence_refs")
        )

    feature_kind = payload.get("feature_kind")
    source_role = payload.get("source_role")
    claim_kind = payload.get("claim_kind")
    expected = EXPECTED_PAIRINGS.get(feature_kind)
    if expected is None:
        findings.append(
            Finding("HABITAT_ROLE_FEATURE_KIND_INVALID", "/feature_kind")
        )
    else:
        expected_role, expected_claim = expected
        if source_role != expected_role:
            code = (
                "MODELED_AS_CRITICAL_DENIED"
                if feature_kind == "REGULATORY_CRITICAL_HABITAT"
                and source_role == "MODELED"
                else "REGULATORY_AS_MODELED_DENIED"
                if feature_kind == "MODELED_HABITAT"
                and source_role == "REGULATORY"
                else "CRITICAL_HABITAT_SOURCE_ROLE_INVALID"
            )
            findings.append(Finding(code, "/source_role"))
        if claim_kind != expected_claim:
            code = (
                "CRITICAL_HABITAT_PRESENCE_CLAIM_DENIED"
                if claim_kind == "SPECIES_PRESENCE"
                else "CRITICAL_HABITAT_CLAIM_KIND_INVALID"
            )
            findings.append(Finding(code, "/claim_kind"))

    if payload.get("public_use_requested") is not False:
        findings.append(
            Finding("HABITAT_ROLE_PUBLIC_USE_DENIED", "/public_use_requested")
        )

    governance = payload.get("governance")
    if not isinstance(governance, Mapping):
        findings.append(
            Finding("HABITAT_ROLE_GOVERNANCE_INVALID", "/governance")
        )
    else:
        governance_keys = set(governance)
        for key in sorted(GOVERNANCE_KEYS - governance_keys):
            findings.append(
                Finding(
                    "HABITAT_ROLE_GOVERNANCE_FIELD_MISSING",
                    f"/governance/{key}",
                )
            )
        for key in sorted(governance_keys - GOVERNANCE_KEYS):
            findings.append(
                Finding(
                    "HABITAT_ROLE_GOVERNANCE_FIELD_UNEXPECTED",
                    f"/governance/{key}",
                )
            )
        for key in sorted(GOVERNANCE_KEYS - {"release_ref"}):
            if key in governance and governance.get(key) is not False:
                findings.append(
                    Finding(
                        "HABITAT_ROLE_AUTHORITY_GRANT_DENIED",
                        f"/governance/{key}",
                    )
                )
        if "release_ref" in governance and governance.get("release_ref") is not None:
            findings.append(
                Finding("HABITAT_ROLE_RELEASE_REF_DENIED", "/governance/release_ref")
            )

    return Result(
        "PASS" if not findings else "DENY",
        tuple(sorted(set(findings))),
    )


def serialize(path: Path, result: Result) -> str:
    value = {
        "candidate": path.name,
        "finding_count": len(result.findings),
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "outcome": result.outcome,
        "scope": "fixture-only-critical-habitat-source-role",
    }
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    payload, read_findings = _read(args.candidate)
    if read_findings:
        result = Result("ERROR", read_findings)
        exit_code = 2
    else:
        result = validate_payload(payload)
        exit_code = 0 if result.ok else 1
    print(serialize(args.candidate, result))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

"""Validate the proposed public-safe EvidenceDrawerPayload projection.

The validator is fixture-first and no-network. It checks a closed JSON Schema
and the finite cross-field rules already enforced by the Explorer adapter,
including correction-chain acyclicity and negative-history non-resolution. A
pass does not establish evidence truth, policy approval, review authority,
release state, publication, or public-use permission.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/ui/evidence_drawer_payload.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/ui/evidence_drawer_payload"
MAX_JSON_BYTES = 256 * 1024
MAX_SCHEMA_FINDINGS = 50


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


def _history(payload: Mapping[str, object]) -> tuple[list[Mapping[str, object]], list[Mapping[str, object]]]:
    raw = payload.get("history")
    if not isinstance(raw, dict):
        return [], []
    negatives = raw.get("negative_outcomes")
    corrections = raw.get("corrections")
    return (
        [item for item in negatives if isinstance(item, dict)] if isinstance(negatives, list) else [],
        [item for item in corrections if isinstance(item, dict)] if isinstance(corrections, list) else [],
    )


def _has_cycle(corrections: Sequence[Mapping[str, object]]) -> bool:
    edges: dict[str, str] = {}
    for item in corrections:
        prior = item.get("prior_evidence_ref")
        active = item.get("active_evidence_ref")
        if not isinstance(prior, str) or not isinstance(active, str):
            continue
        if prior in edges:
            return True
        edges[prior] = active
    for start in edges:
        seen: set[str] = set()
        cursor: str | None = start
        while cursor is not None:
            if cursor in seen:
                return True
            seen.add(cursor)
            cursor = edges.get(cursor)
    return False


def _semantic_findings(payload: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    outcome = payload.get("outcome")
    reason = payload.get("reason_code")
    refs = payload.get("evidence_refs")
    citations = payload.get("citations")
    trust = payload.get("trust_state")
    refs_list = [item for item in refs if isinstance(item, str)] if isinstance(refs, list) else []
    citations_list = citations if isinstance(citations, list) else []
    trust_map = trust if isinstance(trust, dict) else {}
    negatives, corrections = _history(payload)

    allowed_negative_reasons = {
        "HELD": {"HELD_EVIDENCE"},
        "DENIED": {"POLICY_DENIED", "RIGHTS_UNRESOLVED", "SENSITIVE_DETAIL_RESTRICTED"},
        "SUPERSEDED": {"SUPERSEDED_EVIDENCE"},
        "REVOKED": {"REVOKED_EVIDENCE"},
        "WITHDRAWN": {"WITHDRAWN_EVIDENCE"},
    }
    for index, item in enumerate(negatives):
        state = item.get("state")
        reason_code = item.get("reason_code")
        if (
            isinstance(state, str)
            and isinstance(reason_code, str)
            and reason_code not in allowed_negative_reasons.get(state, set())
        ):
            findings.append(
                Finding(
                    "NEGATIVE_STATE_REASON_MISMATCH",
                    f"/history/negative_outcomes/{index}/reason_code",
                    "negative state and reason code must describe the same disposition",
                )
            )

    if _has_cycle(corrections):
        findings.append(Finding("CORRECTION_CYCLE", "/history/corrections", "correction history must be acyclic"))

    current_refs = set(refs_list)
    negative_refs = {
        item.get("evidence_ref") for item in negatives if isinstance(item.get("evidence_ref"), str)
    }
    if current_refs.intersection(negative_refs):
        findings.append(Finding("NEGATIVE_HISTORY_CURRENT_OVERLAP", "/history/negative_outcomes", "historical evidence cannot be current support"))

    if outcome == "ANSWER":
        if reason != "SUPPORTED":
            findings.append(Finding("ANSWER_REASON_INVALID", "/reason_code", "ANSWER requires SUPPORTED"))
        if not refs_list:
            findings.append(Finding("ANSWER_EVIDENCE_REQUIRED", "/evidence_refs", "ANSWER requires evidence"))
        if not citations_list:
            findings.append(Finding("ANSWER_CITATION_REQUIRED", "/citations", "ANSWER requires citations"))
        expected = {
            "policy": "ALLOW", "review": "REVIEWED", "release": "RELEASED", "freshness": "CURRENT"
        }
        for key, value in expected.items():
            if trust_map.get(key) != value:
                findings.append(Finding("ANSWER_TRUST_STATE_INVALID", f"/trust_state/{key}", f"ANSWER requires {key}={value}"))
        if trust_map.get("correction") == "SUPERSEDED":
            findings.append(Finding("ANSWER_SUPERSEDED_DENIED", "/trust_state/correction", "superseded evidence cannot answer"))
        if corrections and trust_map.get("correction") != "CORRECTED":
            findings.append(
                Finding(
                    "CORRECTION_STATE_REQUIRED",
                    "/trust_state/correction",
                    "ANSWER correction history requires CORRECTED trust state",
                )
            )
        if trust_map.get("correction") == "CORRECTED":
            if not corrections:
                findings.append(Finding("CORRECTION_HISTORY_REQUIRED", "/history/corrections", "corrected ANSWER requires correction history"))
            prior_refs = {
                item.get("prior_evidence_ref")
                for item in corrections
                if isinstance(item.get("prior_evidence_ref"), str)
            }
            superseded_refs = {
                item.get("evidence_ref")
                for item in negatives
                if item.get("state") == "SUPERSEDED" and isinstance(item.get("evidence_ref"), str)
            }
            if prior_refs != superseded_refs or any(
                item.get("state") != "SUPERSEDED" for item in negatives
            ):
                findings.append(
                    Finding(
                        "CORRECTION_PRIOR_NOT_SUPERSEDED",
                        "/history/negative_outcomes",
                        "ANSWER history must contain exactly the superseded correction priors",
                    )
                )
            terminal_refs = {
                item.get("active_evidence_ref")
                for item in corrections
                if isinstance(item.get("active_evidence_ref"), str)
                and item.get("active_evidence_ref") not in prior_refs
            }
            if not terminal_refs or not terminal_refs.issubset(current_refs):
                findings.append(
                    Finding(
                        "CORRECTION_ACTIVE_REF_UNBOUND",
                        "/history/corrections",
                        "every terminal correction target must be current evidence",
                    )
                )
        elif negatives:
            findings.append(
                Finding(
                    "ANSWER_HISTORY_UNBOUND",
                    "/history/negative_outcomes",
                    "ANSWER history is allowed only as a complete correction chain",
                )
            )

    elif outcome == "ABSTAIN":
        if reason == "SUPPORTED" or trust_map.get("policy") != "ABSTAIN":
            findings.append(Finding("ABSTAIN_STATE_INVALID", "/outcome", "ABSTAIN requires non-supported reason and ABSTAIN policy"))
        required_state = {
            "SUPERSEDED_EVIDENCE": "SUPERSEDED",
            "HELD_EVIDENCE": "HELD",
            "WITHDRAWN_EVIDENCE": "WITHDRAWN",
            "REVOKED_EVIDENCE": "REVOKED",
        }.get(reason)
        if required_state and not any(item.get("state") == required_state for item in negatives):
            findings.append(Finding("NEGATIVE_HISTORY_REQUIRED", "/history/negative_outcomes", f"{reason} requires {required_state} history"))
        if reason == "SUPERSEDED_EVIDENCE" and trust_map.get("correction") != "SUPERSEDED":
            findings.append(Finding("SUPERSEDED_STATE_INVALID", "/trust_state/correction", "superseded abstention requires SUPERSEDED correction state"))

    elif outcome == "DENY":
        if reason == "SUPPORTED" or trust_map.get("policy") != "DENY":
            findings.append(Finding("DENY_STATE_INVALID", "/outcome", "DENY requires non-supported reason and DENY policy"))
        if refs_list or citations_list:
            findings.append(Finding("DENY_SUPPORT_LEAK", "/evidence_refs", "DENY cannot expose current support"))
        if negatives or corrections:
            findings.append(Finding("DENY_HISTORY_LEAK", "/history", "DENY public projection cannot expose history identifiers"))

    elif outcome == "ERROR":
        if reason != "UPSTREAM_ERROR" or trust_map.get("policy") != "ERROR":
            findings.append(Finding("ERROR_STATE_INVALID", "/outcome", "ERROR requires UPSTREAM_ERROR and ERROR policy"))
        if refs_list or citations_list or negatives or corrections:
            findings.append(Finding("ERROR_DETAIL_LEAK", "/", "ERROR cannot expose evidence or history"))

    return findings


def validate_payload(path: Path) -> tuple[Finding, ...]:
    payload, findings = _load_json(path)
    if payload is None:
        return tuple(sorted(findings))
    schema_findings = _schema_findings(payload)
    if schema_findings:
        return tuple(sorted(set(schema_findings)))
    return tuple(sorted(set(_semantic_findings(payload))))


def _expected_code(path: Path) -> str | None:
    sidecar = path.with_suffix(".expected_code.txt")
    try:
        if sidecar.is_symlink() or not sidecar.is_file() or sidecar.stat().st_size > 128:
            return None
        code = sidecar.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError):
        return None
    return code or None


def run_fixtures() -> int:
    valid = sorted((FIXTURES_ROOT / "valid").glob("*.json"))
    invalid = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))
    if not valid or not invalid:
        print("EVIDENCE_DRAWER_FIXTURES_ERROR nonempty valid and invalid lanes are required")
        return 2
    failures: list[str] = []
    for path in valid:
        if validate_payload(path):
            failures.append(f"valid/{path.name}")
    for path in invalid:
        findings = validate_payload(path)
        expected = _expected_code(path)
        if expected is None or expected not in {item.code for item in findings}:
            failures.append(f"invalid/{path.name}")
    if failures:
        for name in failures:
            print(f"EVIDENCE_DRAWER_FIXTURE_POLARITY_FAIL file={name}")
        return 1
    print(
        "EVIDENCE_DRAWER_FIXTURES_VALID "
        f"valid={len(valid)} invalid={len(invalid)} no_network=true projection_only=true"
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
        print(f"EVIDENCE_DRAWER_PAYLOAD_VALID file={args.payload.name}")
        return 0
    for finding in findings:
        print(
            "EVIDENCE_DRAWER_PAYLOAD_INVALID "
            f"code={finding.code} field={finding.field} detail={finding.detail}"
        )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

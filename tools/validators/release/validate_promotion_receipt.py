"""Validate PROPOSED PromotionReceipt candidates without network or mutation.

A successful result proves bounded JSON shape, A-G finite-outcome consistency,
declared transition prerequisites, and canonical SHA-256 receipt integrity only.
It does not authenticate referenced evidence, policy, review, attestation, or
release records and does not promote, publish, or write any object.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/promotion_receipt.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/release/promotion_receipt"
MAX_JSON_BYTES = 2 * 1024 * 1024
STATUS_PRECEDENCE = {"PASS": 0, "ABSTAIN": 1, "DENY": 2, "ERROR": 3}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> object:
    raise ValueError("non-finite number")


def _parse_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError("non-finite number")
    return parsed


def load_document(path: Path) -> tuple[dict[str, object] | None, tuple[str, ...]]:
    """Read one bounded, duplicate-free JSON object."""

    try:
        if path.is_symlink() or not path.is_file():
            return None, ("INPUT_NOT_FILE",)
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, ("INPUT_TOO_LARGE",)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_float,
        )
    except DuplicateKeyError:
        return None, ("JSON_DUPLICATE_KEY",)
    except (json.JSONDecodeError, UnicodeError, ValueError, RecursionError):
        return None, ("JSON_INVALID",)
    except OSError:
        return None, ("INPUT_UNREADABLE",)
    if not isinstance(value, dict):
        return None, ("JSON_ROOT_INVALID",)
    return value, ()


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def canonical_digest(document: Mapping[str, object]) -> str:
    """Digest canonical JSON after excluding the top-level integrity member."""

    payload = {key: value for key, value in document.items() if key != "integrity"}
    encoded = json.dumps(
        payload,
        ensure_ascii=True,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _gate_statuses(document: Mapping[str, object]) -> list[str]:
    gates = document.get("gates")
    if not isinstance(gates, list):
        return []
    statuses: list[str] = []
    for gate in gates:
        if isinstance(gate, dict) and isinstance(gate.get("status"), str):
            statuses.append(gate["status"])
    return statuses


def derived_status(statuses: Sequence[str]) -> str | None:
    """Apply ERROR > DENY > ABSTAIN > PASS to seven gate statuses."""

    if not statuses or any(status not in STATUS_PRECEDENCE for status in statuses):
        return None
    return max(statuses, key=STATUS_PRECEDENCE.__getitem__)


def validate_document(document: Mapping[str, object]) -> tuple[str, ...]:
    """Return stable, non-value-bearing finding codes."""

    schema_errors = list(_validator().iter_errors(document))
    if schema_errors:
        return ("SCHEMA_INVALID",)

    findings: set[str] = set()
    evaluation = document["evaluation"]
    transition = document["transition"]
    integrity = document["integrity"]
    assert isinstance(evaluation, dict)
    assert isinstance(transition, dict)
    assert isinstance(integrity, dict)

    overall = derived_status(_gate_statuses(document))
    if overall != evaluation["status"]:
        findings.add("OVERALL_STATUS_MISMATCH")

    expected_readiness = "APPROVE_READY" if overall == "PASS" else "BLOCKED"
    if evaluation["readiness"] != expected_readiness:
        findings.add("READINESS_MISMATCH")

    if integrity["receipt_digest"] != canonical_digest(document):
        findings.add("RECEIPT_DIGEST_MISMATCH")

    if transition["applied"] is True:
        if overall != "PASS" or evaluation["readiness"] != "APPROVE_READY":
            findings.add("TRANSITION_APPLIED_WHILE_BLOCKED")
        if document["decision_ref"] is None:
            findings.add("TRANSITION_DECISION_REF_MISSING")
        support_fields = (
            "evidence_refs",
            "policy_refs",
            "review_refs",
            "attestation_refs",
        )
        if any(not document[field] for field in support_fields):
            findings.add("TRANSITION_SUPPORT_INCOMPLETE")

    return tuple(sorted(findings))


def validate_path(path: Path) -> tuple[str, ...]:
    document, findings = load_document(path)
    if document is None:
        return findings
    return validate_document(document)


def _expected_code(path: Path) -> str | None:
    sidecar = path.with_suffix(".expected_code.txt")
    try:
        if sidecar.is_symlink() or not sidecar.is_file() or sidecar.stat().st_size > 256:
            return None
        lines = [line.strip() for line in sidecar.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, UnicodeError):
        return None
    return lines[0] if len(lines) == 1 else None


def run_fixtures(root: Path = FIXTURES_ROOT) -> int:
    valid = sorted((root / "valid").glob("*.json"))
    invalid = sorted((root / "invalid").glob("*.json"))
    if not valid or not invalid:
        print("PROMOTION_RECEIPT_FIXTURES_ERROR nonempty valid and invalid lanes required")
        return 2

    failures: list[str] = []
    for path in valid:
        findings = validate_path(path)
        if findings:
            failures.append(f"valid/{path.name}:{','.join(findings)}")
    for path in invalid:
        findings = validate_path(path)
        expected = _expected_code(path)
        if expected is None or expected not in findings:
            failures.append(f"invalid/{path.name}:expected={expected}:actual={','.join(findings)}")

    if failures:
        for failure in failures:
            print(f"PROMOTION_RECEIPT_FIXTURE_POLARITY_FAIL {failure}")
        return 1
    print(
        "PROMOTION_RECEIPT_FIXTURES_VALID "
        f"valid={len(valid)} invalid={len(invalid)} no_network=true non_publisher=true"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate PromotionReceipt candidates without network or mutation."
    )
    parser.add_argument("receipts", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.receipts:
            raise SystemExit("--fixtures cannot be combined with receipt paths")
        return run_fixtures()
    if not args.receipts:
        raise SystemExit("at least one receipt path is required unless --fixtures is used")

    failed = False
    for path in sorted(args.receipts):
        findings = validate_path(path)
        if findings:
            failed = True
            for code in findings:
                print(f"PROMOTION_RECEIPT_INVALID file={path.name} code={code}")
        else:
            print(f"PROMOTION_RECEIPT_VALID file={path.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Validate fixture-only database mutation transaction receipt candidates.

The validator checks an embedded RunReceipt declaration, canonical hashes, UTC
transaction bounds, row-count arithmetic, finite outcome coherence, and a
recovery-target declaration. It never connects to a database, parses or runs
SQL, authenticates a transaction or row count, restores data, executes policy,
or grants review, promotion, release, publication, or public-use authority.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.local_resolver import build_registry

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/runtime/database_mutation_transaction_receipt.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/runtime/database_mutation_transaction_receipt/cases.json"
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = dict(candidate)
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def compute_run_receipt_digest(candidate: Mapping[str, object]) -> str:
    return canonical_hash(candidate.get("run_receipt"))


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(
        _load_schema(),
        registry=build_registry(REPO_ROOT),
        format_checker=FormatChecker(),
    )
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding(
            "SCHEMA_INVALID",
            "/" + "/".join(str(part) for part in error.absolute_path),
        )
        for error in errors[:100]
    ]


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


def _canonical_string_array(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []

    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.append(
            Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash")
        )
    if candidate.get("run_receipt_digest") != compute_run_receipt_digest(candidate):
        findings.append(
            Finding("RUN_RECEIPT_DIGEST_MISMATCH", "/run_receipt_digest")
        )

    observed_at = _parse_utc(candidate.get("observed_at"))
    if observed_at is None:
        findings.append(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    transaction = candidate.get("transaction")
    run_receipt = candidate.get("run_receipt")
    mutations = candidate.get("mutations")
    totals = candidate.get("totals")
    recovery_target = candidate.get("recovery_target")
    assert isinstance(transaction, dict)
    assert isinstance(run_receipt, dict)
    assert isinstance(mutations, list)
    assert isinstance(totals, dict)
    assert isinstance(recovery_target, dict)

    began_at = _parse_utc(transaction.get("began_at"))
    ended_at = _parse_utc(transaction.get("ended_at"))
    if began_at is None:
        findings.append(
            Finding("UTC_TIMESTAMP_REQUIRED", "/transaction/began_at")
        )
    if ended_at is None:
        findings.append(
            Finding("UTC_TIMESTAMP_REQUIRED", "/transaction/ended_at")
        )
    if began_at is not None and ended_at is not None and began_at >= ended_at:
        findings.append(
            Finding("TRANSACTION_BOUNDARY_INVALID", "/transaction/ended_at")
        )
    if observed_at is not None and ended_at is not None and ended_at > observed_at:
        findings.append(
            Finding("OBSERVATION_PRECEDES_TRANSACTION_END", "/observed_at")
        )

    if run_receipt.get("stage") != "database_mutation":
        findings.append(
            Finding("RUN_STAGE_MISMATCH", "/run_receipt/stage")
        )
    for field in (
        "inputs",
        "outputs",
        "source_descriptor_refs",
        "validation_refs",
    ):
        if not _canonical_string_array(run_receipt.get(field)):
            findings.append(
                Finding("RUN_REFS_NOT_CANONICAL", f"/run_receipt/{field}")
            )

    expected_statement_ids = [
        f"statement:{index:04d}" for index in range(1, len(mutations) + 1)
    ]
    observed_statement_ids = [
        item.get("statement_id") for item in mutations if isinstance(item, dict)
    ]
    if observed_statement_ids != expected_statement_ids:
        findings.append(
            Finding("STATEMENT_ORDER_NOT_CANONICAL", "/mutations")
        )

    attempted_total = 0
    affected_total = 0
    for index, mutation in enumerate(mutations):
        assert isinstance(mutation, dict)
        attempted = mutation.get("attempted_rows")
        affected = mutation.get("affected_rows")
        assert isinstance(attempted, int) and isinstance(affected, int)
        attempted_total += attempted
        affected_total += affected
        if affected > attempted:
            findings.append(
                Finding(
                    "AFFECTED_ROWS_EXCEED_ATTEMPTED",
                    f"/mutations/{index}/affected_rows",
                )
            )

    expected_totals = {
        "statement_count": len(mutations),
        "attempted_rows": attempted_total,
        "affected_rows": affected_total,
    }
    if totals != expected_totals:
        findings.append(Finding("TOTALS_MISMATCH", "/totals"))

    transaction_outcome = transaction.get("outcome")
    persisted_state = transaction.get("persisted_state")
    run_outcome = run_receipt.get("outcome")
    expected_mapping = {
        "COMMITTED": ("SUCCESS", "PERSISTED"),
        "ROLLED_BACK": ("SUCCESS", "NOT_PERSISTED"),
        "FAILED_BEFORE_COMMIT": ("FAIL", "NOT_PERSISTED"),
        "INDETERMINATE": ("PARTIAL", "UNKNOWN"),
    }
    expected_run_outcome, expected_persisted_state = expected_mapping[
        transaction_outcome
    ]
    if run_outcome != expected_run_outcome:
        findings.append(
            Finding("RUN_OUTCOME_MISMATCH", "/run_receipt/outcome")
        )
    if persisted_state != expected_persisted_state:
        findings.append(
            Finding("PERSISTED_STATE_MISMATCH", "/transaction/persisted_state")
        )

    mode = transaction.get("mode")
    if transaction_outcome == "COMMITTED" and mode != "APPLY":
        findings.append(
            Finding("MODE_OUTCOME_MISMATCH", "/transaction/mode")
        )
    if mode == "ROLLBACK_REHEARSAL" and transaction_outcome != "ROLLED_BACK":
        findings.append(
            Finding("MODE_OUTCOME_MISMATCH", "/transaction/outcome")
        )

    if transaction_outcome == "INDETERMINATE":
        findings.append(
            Finding("TRANSACTION_OUTCOME_INDETERMINATE", "/transaction/outcome")
        )
    if recovery_target.get("resolution") == "UNRESOLVED":
        findings.append(
            Finding("RECOVERY_TARGET_UNRESOLVED", "/recovery_target/resolution")
        )
    return findings


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(sorted(schema_findings)))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    abstain_codes = {
        "RECOVERY_TARGET_UNRESOLVED",
        "TRANSACTION_OUTCOME_INDETERMINATE",
    }
    if not codes:
        outcome = "PASS"
    elif codes <= abstain_codes:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(sorted(findings)))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        if value is None:
            target.pop(key, None)
        else:
            target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["run_receipt_digest"] = compute_run_receipt_digest(candidate)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    tamper = entry.get("tamper")
    if tamper == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    elif tamper == "run_receipt_digest":
        candidate["run_receipt_digest"] = "sha256:" + "e" * 64
    return candidate


def validate_fixture_manifest(
    path: Path = FIXTURE_PATH,
) -> list[dict[str, object]]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append(
            {
                "name": entry["name"],
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only database mutation transaction receipts."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate = json.loads(args.input.read_text(encoding="utf-8"))
    result = validate_candidate(candidate)
    print(
        json.dumps(
            {"outcome": result.outcome, "codes": result.codes},
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

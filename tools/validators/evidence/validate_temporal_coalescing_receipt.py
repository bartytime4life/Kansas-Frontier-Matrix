"""Validate fixture-only temporal coalescing receipt candidates.

The validator proves closed shape, deterministic digests, half-open UTC interval
coverage, exact fact-key preservation, and identifier lineage. It does not run a
transform, resolve evidence, authenticate a RunReceipt, execute policy, approve
review, promote, release, deploy, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/evidence/temporal_coalescing_receipt.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/evidence/temporal_coalescing_receipt/cases.json"
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


def compute_interval_set_digest(interval_set: Mapping[str, object]) -> str:
    return canonical_hash(interval_set.get("intervals"))


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(
        _load_schema(), format_checker=FormatChecker()
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
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed


def _interval_sort_key(interval: Mapping[str, object]) -> tuple[object, ...]:
    return (
        interval.get("fact_key"),
        interval.get("valid_from"),
        interval.get("valid_to"),
        interval.get("interval_id"),
    )


def _inspect_intervals(
    intervals: object, field: str
) -> tuple[list[Finding], dict[str, Mapping[str, object]], bool]:
    findings: list[Finding] = []
    by_id: dict[str, Mapping[str, object]] = {}
    valid = True
    if not isinstance(intervals, list):
        return findings, by_id, False

    if intervals != sorted(intervals, key=_interval_sort_key):
        findings.append(Finding("INTERVAL_ORDER_NOT_CANONICAL", field))

    for index, interval in enumerate(intervals):
        if not isinstance(interval, dict):
            valid = False
            continue
        interval_id = interval.get("interval_id")
        if isinstance(interval_id, str):
            if interval_id in by_id:
                findings.append(
                    Finding("DUPLICATE_INTERVAL_ID", f"{field}/{index}/interval_id")
                )
            by_id[interval_id] = interval
        start = _parse_utc(interval.get("valid_from"))
        end = _parse_utc(interval.get("valid_to"))
        if start is None or end is None:
            findings.append(
                Finding("UTC_TIMESTAMP_REQUIRED", f"{field}/{index}")
            )
            valid = False
        elif start >= end:
            findings.append(
                Finding("INTERVAL_NOT_POSITIVE", f"{field}/{index}")
            )
            valid = False
    return findings, by_id, valid


def _coverage(
    intervals: Sequence[Mapping[str, object]], *, merge_adjacency: bool
) -> dict[str, tuple[tuple[datetime, datetime], ...]]:
    grouped: dict[str, list[tuple[datetime, datetime]]] = {}
    for interval in intervals:
        fact_key = interval["fact_key"]
        start = _parse_utc(interval["valid_from"])
        end = _parse_utc(interval["valid_to"])
        assert isinstance(fact_key, str) and start is not None and end is not None
        grouped.setdefault(fact_key, []).append((start, end))

    result: dict[str, tuple[tuple[datetime, datetime], ...]] = {}
    for fact_key, spans in grouped.items():
        merged: list[list[datetime]] = []
        for start, end in sorted(spans):
            if not merged:
                merged.append([start, end])
                continue
            last = merged[-1]
            touches = start == last[1]
            overlaps = start < last[1]
            if overlaps or (merge_adjacency and touches):
                if end > last[1]:
                    last[1] = end
            else:
                merged.append([start, end])
        result[fact_key] = tuple((start, end) for start, end in merged)
    return result


def _has_output_overlap(intervals: Sequence[Mapping[str, object]]) -> bool:
    grouped: dict[str, list[tuple[datetime, datetime]]] = {}
    for interval in intervals:
        start = _parse_utc(interval["valid_from"])
        end = _parse_utc(interval["valid_to"])
        fact_key = interval["fact_key"]
        assert start is not None and end is not None and isinstance(fact_key, str)
        grouped.setdefault(fact_key, []).append((start, end))
    return any(
        current[0] < previous[1]
        for spans in grouped.values()
        for previous, current in zip(sorted(spans), sorted(spans)[1:])
    )


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.append(
            Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash")
        )

    observed_at = candidate.get("observed_at")
    if _parse_utc(observed_at) is None:
        findings.append(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    for name in ("input_set", "output_set"):
        interval_set = candidate.get(name)
        if isinstance(interval_set, dict):
            expected = compute_interval_set_digest(interval_set)
            if interval_set.get("digest") != expected:
                findings.append(
                    Finding(f"{name.upper()}_DIGEST_MISMATCH", f"/{name}/digest")
                )

    input_set = candidate.get("input_set")
    output_set = candidate.get("output_set")
    assert isinstance(input_set, dict) and isinstance(output_set, dict)
    inputs = input_set.get("intervals")
    outputs = output_set.get("intervals")
    input_findings, inputs_by_id, inputs_valid = _inspect_intervals(
        inputs, "/input_set/intervals"
    )
    output_findings, outputs_by_id, outputs_valid = _inspect_intervals(
        outputs, "/output_set/intervals"
    )
    findings.extend(input_findings)
    findings.extend(output_findings)
    assert isinstance(inputs, list) and isinstance(outputs, list)

    evidence_refs = candidate.get("evidence_refs")
    if isinstance(evidence_refs, list) and evidence_refs != sorted(set(evidence_refs)):
        findings.append(
            Finding("EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs")
        )

    lineage = candidate.get("lineage")
    lineage_inputs: set[str] = set()
    lineage_outputs: set[str] = set()
    lineage_by_output: dict[str, list[str]] = {}
    if isinstance(lineage, list):
        for index, edge in enumerate(lineage):
            if not isinstance(edge, dict):
                continue
            output_id = edge.get("output_interval_id")
            input_ids = edge.get("input_interval_ids")
            if isinstance(output_id, str) and isinstance(input_ids, list):
                lineage_outputs.add(output_id)
                lineage_by_output[output_id] = [
                    item for item in input_ids if isinstance(item, str)
                ]
                lineage_inputs.update(lineage_by_output[output_id])
                if output_id not in outputs_by_id:
                    findings.append(
                        Finding(
                            "LINEAGE_OUTPUT_UNKNOWN",
                            f"/lineage/{index}/output_interval_id",
                        )
                    )
                for input_id in lineage_by_output[output_id]:
                    if input_id not in inputs_by_id:
                        findings.append(
                            Finding(
                                "LINEAGE_INPUT_UNKNOWN",
                                f"/lineage/{index}/input_interval_ids",
                            )
                        )
                if output_id in outputs_by_id:
                    output_fact = outputs_by_id[output_id].get("fact_key")
                    if any(
                        inputs_by_id[input_id].get("fact_key") != output_fact
                        for input_id in lineage_by_output[output_id]
                        if input_id in inputs_by_id
                    ):
                        findings.append(
                            Finding(
                                "LINEAGE_FACT_KEY_MISMATCH",
                                f"/lineage/{index}",
                            )
                        )

    if lineage_outputs != set(outputs_by_id):
        findings.append(
            Finding("LINEAGE_OUTPUT_CLOSURE_MISMATCH", "/lineage")
        )
    if lineage_inputs != set(inputs_by_id):
        findings.append(
            Finding("LINEAGE_INPUT_CLOSURE_MISMATCH", "/lineage")
        )

    policy = candidate.get("interval_policy")
    operation = candidate.get("operation")
    assert isinstance(policy, dict) and isinstance(operation, str)
    expected_overlap = {
        "COALESCE": "COALESCE",
        "SPLIT": "SPLIT",
        "PRESERVE": "PRESERVE",
    }[operation]
    if policy.get("overlap") != expected_overlap:
        findings.append(
            Finding("OPERATION_POLICY_MISMATCH", "/interval_policy/overlap")
        )
    if operation != "COALESCE" and policy.get("adjacency") != "PRESERVE":
        findings.append(
            Finding("OPERATION_POLICY_MISMATCH", "/interval_policy/adjacency")
        )

    if inputs_valid and outputs_valid:
        # Coverage is the mathematical union of half-open spans, so adjacent
        # spans have the same coverage as their combined span regardless of
        # whether the declared output representation preserves that boundary.
        # Operation-specific checks below enforce the requested representation.
        input_coverage = _coverage(inputs, merge_adjacency=True)
        output_coverage = _coverage(outputs, merge_adjacency=True)
        coverage_equal = input_coverage == output_coverage
        if not coverage_equal:
            findings.append(Finding("COVERAGE_MISMATCH", "/output_set/intervals"))

        if coverage_equal and operation == "COALESCE":
            if len(outputs) >= len(inputs):
                findings.append(
                    Finding("COALESCE_NOT_REDUCING", "/output_set/intervals")
                )
            canonical_count = sum(len(spans) for spans in input_coverage.values())
            if len(outputs) != canonical_count:
                findings.append(
                    Finding(
                        "COALESCE_OUTPUT_NOT_CANONICAL", "/output_set/intervals"
                    )
                )
        elif coverage_equal and operation == "SPLIT":
            if len(outputs) <= len(inputs):
                findings.append(
                    Finding("SPLIT_NOT_EXPANDING", "/output_set/intervals")
                )
            if _has_output_overlap(outputs):
                findings.append(
                    Finding("SPLIT_OUTPUT_OVERLAP", "/output_set/intervals")
                )
        elif coverage_equal and operation == "PRESERVE":
            input_values = sorted(
                (item["fact_key"], item["valid_from"], item["valid_to"])
                for item in inputs
            )
            output_values = sorted(
                (item["fact_key"], item["valid_from"], item["valid_to"])
                for item in outputs
            )
            if input_values != output_values:
                findings.append(
                    Finding("PRESERVE_VALUE_MISMATCH", "/output_set/intervals")
                )
            if len(outputs) != len(inputs):
                findings.append(
                    Finding("PRESERVE_COUNT_MISMATCH", "/output_set/intervals")
                )
            if any(len(input_ids) != 1 for input_ids in lineage_by_output.values()):
                findings.append(
                    Finding("PRESERVE_LINEAGE_NOT_ONE_TO_ONE", "/lineage")
                )

    if candidate.get("method_resolution") == "UNRESOLVED":
        findings.append(Finding("METHOD_UNRESOLVED", "/method_resolution"))
    return findings


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(sorted(schema_findings)))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes == {"METHOD_UNRESOLVED"}:
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
    for name in ("input_set", "output_set"):
        interval_set = candidate[name]
        assert isinstance(interval_set, dict)
        interval_set["digest"] = compute_interval_set_digest(interval_set)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    tamper = entry.get("tamper")
    if tamper == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    elif tamper == "output_digest":
        output_set = candidate["output_set"]
        assert isinstance(output_set, dict)
        output_set["digest"] = "sha256:" + "e" * 64
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
        description="Validate fixture-only temporal coalescing receipts."
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
